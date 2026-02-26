#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/rbd_compare.sh --prompt <prompt.txt> --depth <N> --baseline-emitter <path> --candidate-emitter <path> [--rounds 3] [--out-dir eval/compare_<ts>] [--baseline-version v1] [--candidate-version v2] [--project-vision required|disabled] [--judge-vision required|disabled]

Purpose:
  Compare two AGENTS emitter variants by running two full project builds
  and blinded judging on resulting artifacts/process evidence.

Outputs:
  - <out_dir>/baseline_run_path.txt
  - <out_dir>/candidate_run_path.txt
  - <out_dir>/judge_results.csv
  - <out_dir>/SUMMARY.md
USAGE
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROMPT=""
DEPTH=""
BASELINE_EMITTER=""
CANDIDATE_EMITTER=""
ROUNDS="3"
OUT_DIR=""
BASELINE_VERSION="baseline"
CANDIDATE_VERSION="candidate"
RUN_OUT_ROOT=""
JUDGE_TIMEOUT_SECONDS="${JUDGE_TIMEOUT_SECONDS:-600}"
PROJECT_VISION="required"
JUDGE_VISION="required"

while (( $# > 0 )); do
  case "$1" in
    --prompt) PROMPT="${2:-}"; shift 2 ;;
    --depth) DEPTH="${2:-}"; shift 2 ;;
    --baseline-emitter) BASELINE_EMITTER="${2:-}"; shift 2 ;;
    --candidate-emitter) CANDIDATE_EMITTER="${2:-}"; shift 2 ;;
    --rounds) ROUNDS="${2:-}"; shift 2 ;;
    --out-dir) OUT_DIR="${2:-}"; shift 2 ;;
    --baseline-version) BASELINE_VERSION="${2:-}"; shift 2 ;;
    --candidate-version) CANDIDATE_VERSION="${2:-}"; shift 2 ;;
    --project-vision) PROJECT_VISION="${2:-}"; shift 2 ;;
    --judge-vision) JUDGE_VISION="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "error: unknown argument: $1" >&2; usage; exit 1 ;;
  esac
done

if [[ -z "$PROMPT" || -z "$DEPTH" || -z "$BASELINE_EMITTER" || -z "$CANDIDATE_EMITTER" ]]; then
  echo "error: --prompt --depth --baseline-emitter --candidate-emitter are required" >&2
  usage
  exit 1
fi

if [[ ! -f "$PROMPT" ]]; then
  echo "error: prompt file not found: $PROMPT" >&2
  exit 1
fi
if [[ ! -f "$BASELINE_EMITTER" ]]; then
  echo "error: baseline emitter not found: $BASELINE_EMITTER" >&2
  exit 1
fi
if [[ ! -f "$CANDIDATE_EMITTER" ]]; then
  echo "error: candidate emitter not found: $CANDIDATE_EMITTER" >&2
  exit 1
fi
if ! [[ "$DEPTH" =~ ^[0-9]+$ ]]; then
  echo "error: --depth must be integer >= 0" >&2
  exit 1
fi
if ! [[ "$ROUNDS" =~ ^[0-9]+$ ]] || (( ROUNDS < 1 )); then
  echo "error: --rounds must be integer >= 1" >&2
  exit 1
fi
if ! [[ "$JUDGE_TIMEOUT_SECONDS" =~ ^[0-9]+$ ]] || (( JUDGE_TIMEOUT_SECONDS < 60 )); then
  echo "error: JUDGE_TIMEOUT_SECONDS must be integer >= 60" >&2
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
if ! command -v codex >/dev/null 2>&1; then
  echo "error: codex command not found in PATH" >&2
  exit 1
fi

ts="$(date +%Y%m%d_%H%M%S)"
if [[ -z "$OUT_DIR" ]]; then
  OUT_DIR="eval/compare_${ts}"
fi
RUN_OUT_ROOT="${OUT_DIR}/runs"
mkdir -p "$OUT_DIR" "$RUN_OUT_ROOT"

if [[ ! -f "${SCRIPT_DIR}/rbd_run.sh" ]]; then
  echo "error: missing runner script: ${SCRIPT_DIR}/rbd_run.sh" >&2
  exit 1
fi

# Build baseline condition.
"${SCRIPT_DIR}/rbd_run.sh" \
  --prompt "$PROMPT" \
  --depth "$DEPTH" \
  --name "baseline_d${DEPTH}_${ts}" \
  --out-root "$RUN_OUT_ROOT" \
  --project-vision "$PROJECT_VISION" \
  --emitter "$BASELINE_EMITTER" \
  --emitter-version "$BASELINE_VERSION"

baseline_run="${RUN_OUT_ROOT}/baseline_d${DEPTH}_${ts}"
echo "$baseline_run" > "${OUT_DIR}/baseline_run_path.txt"

# Build candidate condition.
"${SCRIPT_DIR}/rbd_run.sh" \
  --prompt "$PROMPT" \
  --depth "$DEPTH" \
  --name "candidate_d${DEPTH}_${ts}" \
  --out-root "$RUN_OUT_ROOT" \
  --project-vision "$PROJECT_VISION" \
  --emitter "$CANDIDATE_EMITTER" \
  --emitter-version "$CANDIDATE_VERSION"

candidate_run="${RUN_OUT_ROOT}/candidate_d${DEPTH}_${ts}"
echo "$candidate_run" > "${OUT_DIR}/candidate_run_path.txt"

if [[ "$JUDGE_VISION" == "required" ]]; then
cat > "${OUT_DIR}/HOLDOUT_RUBRIC.md" <<'EOF'
# Holdout Rubric: Artifact + Process Quality (0..100)

Score each condition on these weighted criteria:

| id | dimension | weight |
| --- | --- | ---: |
| H01 | Prompt Fulfillment Quality | 20 |
| H02 | Functional Correctness / Verification | 18 |
| H03 | Visual Quality / UX Readability | 18 |
| H04 | Evidence Integrity | 14 |
| H05 | Anti-Gaming Rigor | 14 |
| H06 | Maintainability / Process Clarity | 8 |
| H07 | Rubric Coherence / Axis Sanity | 8 |

Aggregate score:
`overall = sum(weight * criterion_score) / sum(weight)`
EOF
else
cat > "${OUT_DIR}/HOLDOUT_RUBRIC.md" <<'EOF'
# Holdout Rubric: Artifact + Process Quality (0..100)

Score each condition on these weighted criteria:

| id | dimension | weight |
| --- | --- | ---: |
| H01 | Prompt Fulfillment Quality | 24 |
| H02 | Functional Correctness / Verification | 22 |
| H03 | Evidence Integrity | 18 |
| H04 | Anti-Gaming Rigor | 16 |
| H05 | Maintainability / Process Clarity | 10 |
| H06 | Rubric Coherence / Axis Sanity | 10 |

Aggregate score:
`overall = sum(weight * criterion_score) / sum(weight)`
EOF
fi

echo "round,label_A,label_B,score_A,score_B,score_baseline,score_candidate,delta_candidate_minus_baseline,winner_condition,confidence" > "${OUT_DIR}/judge_results.csv"

for (( r=1; r<=ROUNDS; r++ )); do
  round_dir="${OUT_DIR}/round_${r}"
  mkdir -p "$round_dir"

  if (( r % 2 == 1 )); then
    label_A="baseline"
    label_B="candidate"
    path_A="$baseline_run"
    path_B="$candidate_run"
  else
    label_A="candidate"
    label_B="baseline"
    path_A="$candidate_run"
    path_B="$baseline_run"
  fi

  cp -R "$path_A" "${round_dir}/A"
  cp -R "$path_B" "${round_dir}/B"

  {
    echo "# Condition A Visual Files"
    echo
    find "${round_dir}/A" -type f \
      \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.webp" -o -iname "*.svg" -o -iname "*.pdf" -o -iname "*.html" \) \
      | sed "s#^${round_dir}/A/##" \
      | sort
  } > "${round_dir}/A_VISUAL_FILES.md"
  {
    echo "# Condition B Visual Files"
    echo
    find "${round_dir}/B" -type f \
      \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.webp" -o -iname "*.svg" -o -iname "*.pdf" -o -iname "*.html" \) \
      | sed "s#^${round_dir}/B/##" \
      | sort
  } > "${round_dir}/B_VISUAL_FILES.md"

  if [[ "$JUDGE_VISION" == "required" ]]; then
  cat > "${round_dir}/judge_schema.json" <<'EOF'
{
  "type": "object",
  "properties": {
    "score_A": { "type": "number", "minimum": 0, "maximum": 100 },
    "score_B": { "type": "number", "minimum": 0, "maximum": 100 },
    "winner_label": { "type": "string", "enum": ["A", "B", "tie"] },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "visual_review_notes": { "type": "string", "minLength": 1 },
    "rationale": { "type": "string" }
  },
  "required": ["score_A", "score_B", "winner_label", "confidence", "visual_review_notes", "rationale"],
  "additionalProperties": false
}
EOF
  else
  cat > "${round_dir}/judge_schema.json" <<'EOF'
{
  "type": "object",
  "properties": {
    "score_A": { "type": "number", "minimum": 0, "maximum": 100 },
    "score_B": { "type": "number", "minimum": 0, "maximum": 100 },
    "winner_label": { "type": "string", "enum": ["A", "B", "tie"] },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "rationale": { "type": "string" }
  },
  "required": ["score_A", "score_B", "winner_label", "confidence", "rationale"],
  "additionalProperties": false
}
EOF
  fi

  {
    echo "# Blinded Comparison Task"
    echo
    echo "Condition A is in directory: \`A/\`"
    echo "Condition B is in directory: \`B/\`"
    echo
    echo "Score each condition using ONLY this holdout rubric:"
    cat "${OUT_DIR}/HOLDOUT_RUBRIC.md"
    echo
    echo "Judge based on:"
    echo "- Prompt fulfillment artifacts"
    echo "- Test evidence"
    if [[ "$JUDGE_VISION" == "required" ]]; then
      echo "- Visual evidence and perceptual quality (layout/readability/polish)"
    fi
    echo "- Rubric scorecards and evidence"
    echo "- Anti-gaming controls and contradiction handling"
    if [[ "$JUDGE_VISION" == "required" ]]; then
      echo
      echo "Vision requirements:"
      echo "- Inspect \`A/VISUAL_EVIDENCE_INDEX.md\` and \`B/VISUAL_EVIDENCE_INDEX.md\` when present."
      echo "- Inspect listed visual files from \`A_VISUAL_FILES.md\` and \`B_VISUAL_FILES.md\`."
      echo "- Use \`view_image\` on representative images/screenshots before scoring H03."
      echo "- If user-visible surfaces exist but visual evidence/review is weak, penalize H03/H04/H05."
    fi
    echo
    echo "Return strict JSON matching schema."
  } > "${round_dir}/judge_prompt.md"

  timeout --signal=TERM --kill-after=30s "${JUDGE_TIMEOUT_SECONDS}s" \
    codex exec \
      --skip-git-repo-check \
      --sandbox danger-full-access \
      -c approval_policy=never \
      -C "$round_dir" \
      --output-schema "${round_dir}/judge_schema.json" \
      -o "${round_dir}/judge_result.json" \
      - < "${round_dir}/judge_prompt.md" \
      > "${round_dir}/judge.stdout.log" 2> "${round_dir}/judge.stderr.log"

  python3 - "$round_dir/judge_result.json" "$label_A" "$label_B" "${OUT_DIR}/judge_results.csv" "$JUDGE_VISION" <<'PY'
import csv
import json
import sys

result_path, label_a, label_b, out_csv, judge_vision = sys.argv[1:6]
data = json.load(open(result_path, "r", encoding="utf-8"))

score_a = float(data["score_A"])
score_b = float(data["score_B"])
winner = data["winner_label"]
conf = float(data["confidence"])
if judge_vision == "required":
    visual_notes = str(data.get("visual_review_notes", "")).strip()
    if not visual_notes:
        raise SystemExit("judge_result missing visual_review_notes")

score_baseline = score_a if label_a == "baseline" else score_b
score_candidate = score_a if label_a == "candidate" else score_b
delta = score_candidate - score_baseline

if winner == "tie":
    winner_condition = "tie"
elif winner == "A":
    winner_condition = label_a
else:
    winner_condition = label_b

round_num = int(result_path.split("round_")[-1].split("/")[0])
with open(out_csv, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([
        round_num,
        label_a,
        label_b,
        f"{score_a:.4f}",
        f"{score_b:.4f}",
        f"{score_baseline:.4f}",
        f"{score_candidate:.4f}",
        f"{delta:.4f}",
        winner_condition,
        f"{conf:.4f}",
    ])
PY
done

python3 - "${OUT_DIR}/judge_results.csv" "${OUT_DIR}/SUMMARY.md" "$PROJECT_VISION" "$JUDGE_VISION" <<'PY'
import csv
import statistics
import sys

rows = list(csv.DictReader(open(sys.argv[1], newline="", encoding="utf-8")))
out_path = sys.argv[2]
project_vision = sys.argv[3]
judge_vision = sys.argv[4]

deltas = [float(r["delta_candidate_minus_baseline"]) for r in rows]
wins_candidate = sum(1 for r in rows if r["winner_condition"] == "candidate")
wins_baseline = sum(1 for r in rows if r["winner_condition"] == "baseline")
ties = sum(1 for r in rows if r["winner_condition"] == "tie")
mean_delta = statistics.mean(deltas) if deltas else 0.0
median_delta = statistics.median(deltas) if deltas else 0.0

with open(out_path, "w", encoding="utf-8") as f:
    f.write("# Process Comparison Summary\n\n")
    f.write(f"- project_vision: `{project_vision}`\n")
    f.write(f"- judge_vision: `{judge_vision}`\n")
    f.write(f"- rounds: `{len(rows)}`\n")
    f.write(f"- candidate wins: `{wins_candidate}`\n")
    f.write(f"- baseline wins: `{wins_baseline}`\n")
    f.write(f"- ties: `{ties}`\n")
    f.write(f"- mean delta (candidate - baseline): `{mean_delta:.4f}`\n")
    f.write(f"- median delta (candidate - baseline): `{median_delta:.4f}`\n\n")
    if mean_delta > 0 and wins_candidate > wins_baseline:
        f.write("Conclusion: candidate emitter shows improved process/artifact quality.\n")
    elif mean_delta < 0 and wins_baseline > wins_candidate:
        f.write("Conclusion: baseline emitter remains stronger for this prompt.\n")
    else:
        f.write("Conclusion: no clear superiority signal.\n")
PY

echo "comparison complete: $OUT_DIR"
