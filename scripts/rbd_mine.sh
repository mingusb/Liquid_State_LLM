#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/rbd_mine.sh --depth <N> --prompt <prompt.txt> [--prompt <prompt2.txt> ...]
                      [--prompt-list <prompts.txt>]
                      [--iterations 1] [--rounds 1]
                      [--out-dir eval/mine_<ts>]
                      [--self-timeout-seconds 1800]
                      [--compare-timeout-seconds 900]
                      [--judge-timeout-seconds 300]
                      [--project-vision required|disabled]
                      [--judge-vision required|disabled]
                      [--promote-min-mean-delta 0]
                      [--no-promote] [--dry-run]

Purpose:
  Mine for better toolkit revisions by:
  1) Generating a candidate toolkit via a self-improvement run.
  2) Evaluating candidate vs current baseline across one or more prompts.
  3) Promoting candidate source files into this project only when metrics improve.

Promotion gate (default):
  - self-improve run succeeded
  - candidate emitter exists
  - no compare failures
  - total judged rounds > 0
  - candidate wins > baseline wins
  - mean delta (candidate - baseline) > promote_min_mean_delta
  - prompt-level positive mean deltas in at least half of evaluated prompts

Outputs:
  - <out_dir>/iter_*/self_improve_prompt.txt
  - <out_dir>/iter_*/ITERATION_SUMMARY.md
  - <out_dir>/iter_*/iteration_metrics.json
  - <out_dir>/iter_*/decision.env
  - <out_dir>/mining_log.tsv
  - <out_dir>/MINING_SUMMARY.md
  - <out_dir>/final_project_source/
USAGE
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

DEPTH=""
ITERATIONS="1"
ROUNDS="1"
OUT_DIR=""
PROMPT_LIST_FILE=""
SELF_TIMEOUT_SECONDS="1800"
COMPARE_TIMEOUT_SECONDS="900"
JUDGE_TIMEOUT_SECONDS="300"
PROJECT_VISION="required"
JUDGE_VISION="required"
PROMOTE_MIN_MEAN_DELTA="0"
NO_PROMOTE="0"
DRY_RUN="0"

declare -a PROMPTS_RAW=()
declare -a PROMPTS=()

trim() {
  local s="$1"
  s="${s#"${s%%[![:space:]]*}"}"
  s="${s%"${s##*[![:space:]]}"}"
  printf '%s' "$s"
}

slugify() {
  local s="$1"
  s="${s//[^A-Za-z0-9_-]/_}"
  printf '%s' "$s"
}

write_self_improve_prompt() {
  local out_file="$1"
  local iteration="$2"

  {
    echo "Improve this rubric-driven development toolkit itself."
    echo
    echo "Iteration context:"
    echo "- iteration: ${iteration}"
    echo "- objective: produce a candidate revision that performs better than current_project."
    echo "- project_vision_policy: ${PROJECT_VISION}"
    echo "- judge_vision_policy: ${JUDGE_VISION}"
    echo
    echo "Evaluation prompt suite (must guide your optimization target):"
    for prompt in "${PROMPTS[@]}"; do
      echo "- \`${prompt}\`"
    done
    cat <<'EOF'

Context:
- A baseline snapshot is available in `current_project/`.
- Produce candidate revision in `candidate_project/`.

Required deliverables:
1. Create drop-in candidate files:
   - `candidate_project/scripts/emit_agents_md.py`
   - `candidate_project/scripts/rbd_run.sh`
   - `candidate_project/scripts/rbd_compare.sh` (if changed)
   - `candidate_project/README.md` (if behavior changed)
2. Keep existing CLIs backward compatible unless strongly justified.
3. Improve quality on the prompt suite, with emphasis on:
   - better prompt-to-artifact fulfillment quality,
   - better visual/perceptual quality scoring with explicit image evidence (when vision is enabled),
   - better use of Vision tool (`view_image`) in development/judging when policy enables vision,
   - better anti-gaming rigor and evidence integrity,
   - better reproducibility and maintainability.
4. Add:
   - `candidate_project/CHANGELOG.md`
   - `candidate_project/TEST_PLAN.md`
5. Show fail-before/pass-after verification where practical.

Acceptance expectation:
- Candidate should be plausible to beat baseline under blinded comparison on the prompt suite.
EOF
  } > "$out_file"
}

copy_current_project_snapshot() {
  local run_dir="$1"
  mkdir -p "$run_dir/current_project/scripts"
  cp "$REPO_ROOT/scripts/emit_agents_md.py" "$run_dir/current_project/scripts/emit_agents_md.py"
  cp "$REPO_ROOT/scripts/rbd_run.sh" "$run_dir/current_project/scripts/rbd_run.sh"
  cp "$REPO_ROOT/scripts/rbd_compare.sh" "$run_dir/current_project/scripts/rbd_compare.sh"
  cp "$REPO_ROOT/README.md" "$run_dir/current_project/README.md"
}

while (( $# > 0 )); do
  case "$1" in
    --depth) DEPTH="${2:-}"; shift 2 ;;
    --prompt) PROMPTS_RAW+=("${2:-}"); shift 2 ;;
    --prompt-list) PROMPT_LIST_FILE="${2:-}"; shift 2 ;;
    --iterations) ITERATIONS="${2:-}"; shift 2 ;;
    --rounds) ROUNDS="${2:-}"; shift 2 ;;
    --out-dir) OUT_DIR="${2:-}"; shift 2 ;;
    --self-timeout-seconds) SELF_TIMEOUT_SECONDS="${2:-}"; shift 2 ;;
    --compare-timeout-seconds) COMPARE_TIMEOUT_SECONDS="${2:-}"; shift 2 ;;
    --judge-timeout-seconds) JUDGE_TIMEOUT_SECONDS="${2:-}"; shift 2 ;;
    --project-vision) PROJECT_VISION="${2:-}"; shift 2 ;;
    --judge-vision) JUDGE_VISION="${2:-}"; shift 2 ;;
    --promote-min-mean-delta) PROMOTE_MIN_MEAN_DELTA="${2:-}"; shift 2 ;;
    --no-promote) NO_PROMOTE="1"; shift 1 ;;
    --dry-run) DRY_RUN="1"; shift 1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "error: unknown argument: $1" >&2; usage; exit 1 ;;
  esac
done

if [[ -z "$DEPTH" ]]; then
  echo "error: --depth is required" >&2
  usage
  exit 1
fi

if [[ -n "$PROMPT_LIST_FILE" ]]; then
  if [[ ! -f "$PROMPT_LIST_FILE" ]]; then
    echo "error: prompt list file not found: $PROMPT_LIST_FILE" >&2
    exit 1
  fi
  while IFS= read -r raw || [[ -n "$raw" ]]; do
    line="$(trim "$raw")"
    [[ -z "$line" ]] && continue
    [[ "${line:0:1}" == "#" ]] && continue
    PROMPTS_RAW+=("$line")
  done < "$PROMPT_LIST_FILE"
fi

if (( ${#PROMPTS_RAW[@]} == 0 )); then
  echo "error: provide at least one --prompt or --prompt-list" >&2
  exit 1
fi

if ! [[ "$DEPTH" =~ ^[0-9]+$ ]]; then
  echo "error: --depth must be integer >= 0" >&2
  exit 1
fi
if ! [[ "$ITERATIONS" =~ ^[0-9]+$ ]] || (( ITERATIONS < 1 )); then
  echo "error: --iterations must be integer >= 1" >&2
  exit 1
fi
if ! [[ "$ROUNDS" =~ ^[0-9]+$ ]] || (( ROUNDS < 1 )); then
  echo "error: --rounds must be integer >= 1" >&2
  exit 1
fi
if ! [[ "$SELF_TIMEOUT_SECONDS" =~ ^[0-9]+$ ]] || (( SELF_TIMEOUT_SECONDS < 60 )); then
  echo "error: --self-timeout-seconds must be integer >= 60" >&2
  exit 1
fi
if ! [[ "$COMPARE_TIMEOUT_SECONDS" =~ ^[0-9]+$ ]] || (( COMPARE_TIMEOUT_SECONDS < 60 )); then
  echo "error: --compare-timeout-seconds must be integer >= 60" >&2
  exit 1
fi
if ! [[ "$JUDGE_TIMEOUT_SECONDS" =~ ^[0-9]+$ ]] || (( JUDGE_TIMEOUT_SECONDS < 60 )); then
  echo "error: --judge-timeout-seconds must be integer >= 60" >&2
  exit 1
fi
if [[ "$PROJECT_VISION" != "required" && "$PROJECT_VISION" != "disabled" ]]; then
  echo "error: --project-vision must be one of: required, disabled" >&2
  exit 1
fi
if [[ "$JUDGE_VISION" != "required" && "$JUDGE_VISION" != "disabled" ]]; then
  echo "error: --judge-vision must be one of: required, disabled" >&2
  exit 1
fi
if ! [[ "$PROMOTE_MIN_MEAN_DELTA" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
  echo "error: --promote-min-mean-delta must be numeric" >&2
  exit 1
fi

for raw_prompt in "${PROMPTS_RAW[@]}"; do
  if [[ ! -f "$raw_prompt" ]]; then
    echo "error: prompt file not found: $raw_prompt" >&2
    exit 1
  fi
  prompt_abs="$(cd "$(dirname "$raw_prompt")" && pwd)/$(basename "$raw_prompt")"
  PROMPTS+=("$prompt_abs")
done

ts="$(date +%Y%m%d_%H%M%S)"
if [[ -z "$OUT_DIR" ]]; then
  OUT_DIR="$REPO_ROOT/eval/mine_${ts}"
fi
mkdir -p "$OUT_DIR"

{
  echo "# Prompt Suite"
  echo
  i=1
  for p in "${PROMPTS[@]}"; do
    echo "${i}. \`${p}\`"
    i=$((i + 1))
  done
} > "$OUT_DIR/PROMPT_SUITE.md"

printf "iteration\tpromoted\tself_run_ok\tcandidate_ready\tcompare_fail\tmean_delta\tcandidate_wins\tbaseline_wins\tties\tprompts_positive\tprompts_evaluated\ttotal_judgments\n" > "$OUT_DIR/mining_log.tsv"

for (( iter=1; iter<=ITERATIONS; iter++ )); do
  iter_dir="$OUT_DIR/iter_${iter}"
  mkdir -p "$iter_dir"

  self_prompt="$iter_dir/self_improve_prompt.txt"
  write_self_improve_prompt "$self_prompt" "$iter"

  run_name="mine_iter${iter}_self_improve"
  run_dir="$iter_dir/${run_name}"
  rm -rf "$run_dir"
  mkdir -p "$run_dir"
  copy_current_project_snapshot "$run_dir"

  self_run_ok=1
  candidate_ready=1
  compare_fail=0

  if [[ "$DRY_RUN" == "1" ]]; then
    self_run_ok=0
    candidate_ready=0
  else
    if ! CODEX_TIMEOUT_SECONDS="$SELF_TIMEOUT_SECONDS" \
      "$REPO_ROOT/scripts/rbd_run.sh" \
        --prompt "$self_prompt" \
        --depth "$DEPTH" \
        --name "$run_name" \
        --project-vision "$PROJECT_VISION" \
        --out-root "$iter_dir"; then
      self_run_ok=0
    fi

    candidate_root="$run_dir/candidate_project"
    candidate_emitter="$candidate_root/scripts/emit_agents_md.py"
    if [[ ! -f "$candidate_emitter" ]]; then
      candidate_ready=0
    fi

    if (( self_run_ok == 1 && candidate_ready == 1 )); then
      idx=0
      for prompt in "${PROMPTS[@]}"; do
        idx=$((idx + 1))
        base="$(basename "$prompt")"
        slug="$(slugify "${base%.*}")"
        compare_dir="$iter_dir/compare_${idx}_${slug}"
        rm -rf "$compare_dir"

        if ! CODEX_TIMEOUT_SECONDS="$COMPARE_TIMEOUT_SECONDS" \
          JUDGE_TIMEOUT_SECONDS="$JUDGE_TIMEOUT_SECONDS" \
          "$REPO_ROOT/scripts/rbd_compare.sh" \
            --prompt "$prompt" \
            --depth "$DEPTH" \
            --baseline-emitter "$REPO_ROOT/scripts/emit_agents_md.py" \
            --candidate-emitter "$candidate_emitter" \
            --project-vision "$PROJECT_VISION" \
            --judge-vision "$JUDGE_VISION" \
            --rounds "$ROUNDS" \
            --baseline-version "iter${iter}_baseline" \
            --candidate-version "iter${iter}_candidate" \
            --out-dir "$compare_dir"; then
          compare_fail=1
        fi
      done
    fi
  fi

  python3 - "$iter_dir" "${#PROMPTS[@]}" "$NO_PROMOTE" "$compare_fail" "$self_run_ok" "$candidate_ready" "$PROMOTE_MIN_MEAN_DELTA" <<'PY'
import csv
import json
import math
import statistics
import sys
from pathlib import Path

iter_dir = Path(sys.argv[1])
prompt_count = int(sys.argv[2])
no_promote = int(sys.argv[3])
compare_fail = int(sys.argv[4])
self_run_ok = int(sys.argv[5])
candidate_ready = int(sys.argv[6])
min_mean_delta = float(sys.argv[7])

rows = []
prompt_stats = []
for compare_dir in sorted(iter_dir.glob("compare_*")):
    csv_path = compare_dir / "judge_results.csv"
    if not csv_path.is_file():
        continue
    prompt_rows = list(csv.DictReader(csv_path.open(newline="", encoding="utf-8")))
    deltas = [float(r["delta_candidate_minus_baseline"]) for r in prompt_rows]
    wins_candidate = sum(1 for r in prompt_rows if r["winner_condition"] == "candidate")
    wins_baseline = sum(1 for r in prompt_rows if r["winner_condition"] == "baseline")
    ties = sum(1 for r in prompt_rows if r["winner_condition"] == "tie")
    mean_delta = statistics.mean(deltas) if deltas else 0.0
    prompt_stats.append(
        {
            "compare_dir": compare_dir.name,
            "rounds": len(prompt_rows),
            "mean_delta": mean_delta,
            "candidate_wins": wins_candidate,
            "baseline_wins": wins_baseline,
            "ties": ties,
        }
    )
    rows.extend(prompt_rows)

total_judgments = len(rows)
candidate_wins = sum(1 for r in rows if r["winner_condition"] == "candidate")
baseline_wins = sum(1 for r in rows if r["winner_condition"] == "baseline")
ties = sum(1 for r in rows if r["winner_condition"] == "tie")
deltas = [float(r["delta_candidate_minus_baseline"]) for r in rows]
mean_delta = statistics.mean(deltas) if deltas else 0.0
median_delta = statistics.median(deltas) if deltas else 0.0
prompts_evaluated = len(prompt_stats)
prompts_positive = sum(1 for s in prompt_stats if s["mean_delta"] > 0)
majority_threshold = math.ceil(prompts_evaluated / 2) if prompts_evaluated else 1

promote = (
    no_promote == 0
    and compare_fail == 0
    and self_run_ok == 1
    and candidate_ready == 1
    and total_judgments > 0
    and candidate_wins > baseline_wins
    and mean_delta > min_mean_delta
    and prompts_positive >= majority_threshold
)

metrics = {
    "self_run_ok": self_run_ok,
    "candidate_ready": candidate_ready,
    "compare_fail": compare_fail,
    "total_judgments": total_judgments,
    "candidate_wins": candidate_wins,
    "baseline_wins": baseline_wins,
    "ties": ties,
    "mean_delta": mean_delta,
    "median_delta": median_delta,
    "prompts_positive": prompts_positive,
    "prompts_evaluated": prompts_evaluated,
    "prompt_count_requested": prompt_count,
    "promote_min_mean_delta": min_mean_delta,
    "promote_decision": int(promote),
    "prompt_stats": prompt_stats,
}

(iter_dir / "iteration_metrics.json").write_text(
    json.dumps(metrics, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)

summary_lines = []
summary_lines.append("# Iteration Summary")
summary_lines.append("")
summary_lines.append(f"- self_run_ok: `{self_run_ok}`")
summary_lines.append(f"- candidate_ready: `{candidate_ready}`")
summary_lines.append(f"- compare_fail: `{compare_fail}`")
summary_lines.append(f"- total_judgments: `{total_judgments}`")
summary_lines.append(f"- candidate_wins: `{candidate_wins}`")
summary_lines.append(f"- baseline_wins: `{baseline_wins}`")
summary_lines.append(f"- ties: `{ties}`")
summary_lines.append(f"- mean_delta: `{mean_delta:.4f}`")
summary_lines.append(f"- median_delta: `{median_delta:.4f}`")
summary_lines.append(f"- prompts_positive: `{prompts_positive}` / `{prompts_evaluated}`")
summary_lines.append(f"- promote_decision: `{int(promote)}`")
summary_lines.append("")
summary_lines.append("| Compare Dir | Rounds | Mean Delta | Candidate Wins | Baseline Wins | Ties |")
summary_lines.append("| --- | ---: | ---: | ---: | ---: | ---: |")
if prompt_stats:
    for s in prompt_stats:
        summary_lines.append(
            f"| {s['compare_dir']} | {s['rounds']} | {s['mean_delta']:.4f} | "
            f"{s['candidate_wins']} | {s['baseline_wins']} | {s['ties']} |"
        )
else:
    summary_lines.append("| (none) | 0 | 0.0000 | 0 | 0 | 0 |")
summary_lines.append("")

(iter_dir / "ITERATION_SUMMARY.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

env_lines = [
    f"PROMOTE={int(promote)}",
    f"SELF_RUN_OK={self_run_ok}",
    f"CANDIDATE_READY={candidate_ready}",
    f"COMPARE_FAIL={compare_fail}",
    f"TOTAL_JUDGMENTS={total_judgments}",
    f"CANDIDATE_WINS={candidate_wins}",
    f"BASELINE_WINS={baseline_wins}",
    f"TIES={ties}",
    f"MEAN_DELTA={mean_delta:.6f}",
    f"PROMPTS_POSITIVE={prompts_positive}",
    f"PROMPTS_EVALUATED={prompts_evaluated}",
]
(iter_dir / "decision.env").write_text("\n".join(env_lines) + "\n", encoding="utf-8")
PY

  # shellcheck disable=SC1090
  source "$iter_dir/decision.env"

  if (( PROMOTE == 1 )) && [[ "$DRY_RUN" != "1" ]]; then
    candidate_root="$run_dir/candidate_project"
    cp "$candidate_root/scripts/emit_agents_md.py" "$REPO_ROOT/scripts/emit_agents_md.py"
    if [[ -f "$candidate_root/scripts/rbd_run.sh" ]]; then
      cp "$candidate_root/scripts/rbd_run.sh" "$REPO_ROOT/scripts/rbd_run.sh"
    fi
    if [[ -f "$candidate_root/scripts/rbd_compare.sh" ]]; then
      cp "$candidate_root/scripts/rbd_compare.sh" "$REPO_ROOT/scripts/rbd_compare.sh"
    fi
    if [[ -f "$candidate_root/README.md" ]]; then
      cp "$candidate_root/README.md" "$REPO_ROOT/README.md"
    fi
    chmod +x "$REPO_ROOT/scripts/emit_agents_md.py" "$REPO_ROOT/scripts/rbd_run.sh" "$REPO_ROOT/scripts/rbd_compare.sh"
  fi

  printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" \
    "$iter" "$PROMOTE" "$SELF_RUN_OK" "$CANDIDATE_READY" "$COMPARE_FAIL" "$MEAN_DELTA" \
    "$CANDIDATE_WINS" "$BASELINE_WINS" "$TIES" "$PROMPTS_POSITIVE" "$PROMPTS_EVALUATED" "$TOTAL_JUDGMENTS" \
    >> "$OUT_DIR/mining_log.tsv"
done

mkdir -p "$OUT_DIR/final_project_source/scripts"
cp "$REPO_ROOT/scripts/emit_agents_md.py" "$OUT_DIR/final_project_source/scripts/emit_agents_md.py"
cp "$REPO_ROOT/scripts/rbd_run.sh" "$OUT_DIR/final_project_source/scripts/rbd_run.sh"
cp "$REPO_ROOT/scripts/rbd_compare.sh" "$OUT_DIR/final_project_source/scripts/rbd_compare.sh"
cp "$REPO_ROOT/README.md" "$OUT_DIR/final_project_source/README.md"

python3 - "$OUT_DIR" "${#PROMPTS[@]}" "$DEPTH" "$ITERATIONS" "$ROUNDS" "$NO_PROMOTE" "$DRY_RUN" <<'PY'
import csv
import sys
from pathlib import Path

out_dir = Path(sys.argv[1])
prompt_count = int(sys.argv[2])
depth = int(sys.argv[3])
iterations = int(sys.argv[4])
rounds = int(sys.argv[5])
no_promote = int(sys.argv[6])
dry_run = int(sys.argv[7])

log_path = out_dir / "mining_log.tsv"
rows = []
with log_path.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    rows = list(reader)

promotions = sum(int(r["promoted"]) for r in rows)
last_row = rows[-1] if rows else None

lines = []
lines.append("# Mining Summary")
lines.append("")
lines.append(f"- prompt_count: `{prompt_count}`")
lines.append(f"- depth: `N={depth}`")
lines.append(f"- iterations_requested: `{iterations}`")
lines.append(f"- judge_rounds_per_prompt: `{rounds}`")
lines.append(f"- no_promote: `{no_promote}`")
lines.append(f"- dry_run: `{dry_run}`")
lines.append(f"- promotions_applied: `{promotions}`")
if last_row:
    lines.append(f"- final_iteration_mean_delta: `{float(last_row['mean_delta']):.4f}`")
    lines.append(f"- final_iteration_candidate_wins: `{last_row['candidate_wins']}`")
    lines.append(f"- final_iteration_baseline_wins: `{last_row['baseline_wins']}`")
lines.append("")
lines.append("| Iteration | Promoted | Self Run OK | Candidate Ready | Compare Fail | Mean Delta | Candidate Wins | Baseline Wins | Ties | Prompts Positive | Prompts Evaluated | Total Judgments |")
lines.append("| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
if rows:
    for r in rows:
        lines.append(
            f"| {r['iteration']} | {r['promoted']} | {r['self_run_ok']} | {r['candidate_ready']} | "
            f"{r['compare_fail']} | {float(r['mean_delta']):.4f} | {r['candidate_wins']} | "
            f"{r['baseline_wins']} | {r['ties']} | {r['prompts_positive']} | "
            f"{r['prompts_evaluated']} | {r['total_judgments']} |"
        )
else:
    lines.append("| 0 | 0 | 0 | 0 | 0 | 0.0000 | 0 | 0 | 0 | 0 | 0 | 0 |")
lines.append("")
lines.append("Final selected source snapshot:")
lines.append(f"- `final_project_source/scripts/emit_agents_md.py`")
lines.append(f"- `final_project_source/scripts/rbd_run.sh`")
lines.append(f"- `final_project_source/scripts/rbd_compare.sh`")
lines.append(f"- `final_project_source/README.md`")
lines.append("")
lines.append("Detailed per-iteration metrics:")
for i in range(1, iterations + 1):
    lines.append(f"- `iter_{i}/ITERATION_SUMMARY.md`")
    lines.append(f"- `iter_{i}/iteration_metrics.json`")

(out_dir / "MINING_SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
PY

echo "mining complete: $OUT_DIR"
