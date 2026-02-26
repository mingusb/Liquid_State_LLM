#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/rbd_autonomous.sh \
    --prompt <prompt.txt> \
    --depth <N> \
    [--name <run_name>] \
    [--out-root runs] \
    [--project-vision required|disabled] \
    [--required-streak 1] \
    [--max-autonomous-iterations 16] \
    [--codex-timeout-seconds 0] \
    [--codex-no-progress-seconds 0] \
    [--codex-reasoning-effort xhigh] \
    [--min-destabilization-defects 3] \
    [--min-destabilization-baseline-mean 40] \
    [--max-destabilization-baseline-mean 95] \
    [--min-recovery-iteration-gap 1] \
    [--parallel-links] \
    [--max-parallel-epochs auto] \
    [--allow-prestable-chains] \
    [--codex-model <model>] \
    [--codex-bin codex]

Purpose:
  1) Generate a prompt-coupled run directory with AGENTS.md.
  2) Drive that run to stability autonomously.
  3) Keep rubric development tied to prompt implementation while stabilizing all chains.
USAGE
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROMPT=""
DEPTH=""
RUN_NAME=""
OUT_ROOT="runs"
PROJECT_VISION="required"
REQUIRED_STREAK="1"
MAX_AUTONOMOUS_ITERATIONS="16"
CODEX_TIMEOUT_SECONDS="${CODEX_TIMEOUT_SECONDS:-0}"
CODEX_NO_PROGRESS_SECONDS="${CODEX_NO_PROGRESS_SECONDS:-0}"
CODEX_REASONING_EFFORT="${CODEX_REASONING_EFFORT:-xhigh}"
CODEX_MODEL=""
CODEX_BIN="codex"
REQUIRE_CHAIN_DESTABILIZATION="1"
MIN_DESTABILIZATION_DEFECTS="3"
MIN_DESTABILIZATION_BASELINE_MEAN="40.0"
MAX_DESTABILIZATION_BASELINE_MEAN="95.0"
MIN_RECOVERY_ITERATION_GAP="1"
PARALLEL_LINKS="0"
MAX_PARALLEL_EPOCHS=""

# Pass-through options for emitter/run setup.
EMITTER="$SCRIPT_DIR/emit_agents_md.py"
EMITTER_VERSION="v1"
PROJECT_NAME="Nested Rubric-Driven Project"

while (( $# > 0 )); do
  case "$1" in
    --prompt) PROMPT="${2:-}"; shift 2 ;;
    --depth) DEPTH="${2:-}"; shift 2 ;;
    --name) RUN_NAME="${2:-}"; shift 2 ;;
    --out-root) OUT_ROOT="${2:-}"; shift 2 ;;
    --project-vision) PROJECT_VISION="${2:-}"; shift 2 ;;
    --required-streak) REQUIRED_STREAK="${2:-}"; shift 2 ;;
    --max-autonomous-iterations) MAX_AUTONOMOUS_ITERATIONS="${2:-}"; shift 2 ;;
    --codex-timeout-seconds) CODEX_TIMEOUT_SECONDS="${2:-}"; shift 2 ;;
    --codex-no-progress-seconds) CODEX_NO_PROGRESS_SECONDS="${2:-}"; shift 2 ;;
    --codex-reasoning-effort) CODEX_REASONING_EFFORT="${2:-}"; shift 2 ;;
    --min-destabilization-defects) MIN_DESTABILIZATION_DEFECTS="${2:-}"; shift 2 ;;
    --min-destabilization-baseline-mean) MIN_DESTABILIZATION_BASELINE_MEAN="${2:-}"; shift 2 ;;
    --max-destabilization-baseline-mean) MAX_DESTABILIZATION_BASELINE_MEAN="${2:-}"; shift 2 ;;
    --min-recovery-iteration-gap) MIN_RECOVERY_ITERATION_GAP="${2:-}"; shift 2 ;;
    --parallel-links) PARALLEL_LINKS="1"; shift 1 ;;
    --max-parallel-epochs) MAX_PARALLEL_EPOCHS="${2:-}"; shift 2 ;;
    --allow-prestable-chains) REQUIRE_CHAIN_DESTABILIZATION="0"; shift 1 ;;
    --codex-model) CODEX_MODEL="${2:-}"; shift 2 ;;
    --codex-bin) CODEX_BIN="${2:-}"; shift 2 ;;
    --emitter) EMITTER="${2:-}"; shift 2 ;;
    --emitter-version) EMITTER_VERSION="${2:-}"; shift 2 ;;
    --project-name) PROJECT_NAME="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "error: unknown argument: $1" >&2; usage; exit 1 ;;
  esac
done

if [[ -z "$PROMPT" || -z "$DEPTH" ]]; then
  echo "error: --prompt and --depth are required" >&2
  usage
  exit 1
fi
if [[ ! -f "$PROMPT" ]]; then
  echo "error: prompt file not found: $PROMPT" >&2
  exit 1
fi
if ! [[ "$DEPTH" =~ ^[0-9]+$ ]]; then
  echo "error: --depth must be an integer >= 0" >&2
  exit 1
fi
if ! [[ "$REQUIRED_STREAK" =~ ^[0-9]+$ ]] || (( REQUIRED_STREAK < 1 )); then
  echo "error: --required-streak must be an integer >= 1" >&2
  exit 1
fi
if ! [[ "$MAX_AUTONOMOUS_ITERATIONS" =~ ^[0-9]+$ ]] || (( MAX_AUTONOMOUS_ITERATIONS < 1 )); then
  echo "error: --max-autonomous-iterations must be an integer >= 1" >&2
  exit 1
fi
if ! [[ "$CODEX_TIMEOUT_SECONDS" =~ ^[0-9]+$ ]] || (( CODEX_TIMEOUT_SECONDS < 0 )); then
  echo "error: --codex-timeout-seconds must be an integer >= 0 (0 disables timeout)" >&2
  exit 1
fi
if ! [[ "$CODEX_NO_PROGRESS_SECONDS" =~ ^[0-9]+$ ]] || (( CODEX_NO_PROGRESS_SECONDS < 0 )); then
  echo "error: --codex-no-progress-seconds must be an integer >= 0 (0 disables no-progress watchdog)" >&2
  exit 1
fi
if [[ "$CODEX_REASONING_EFFORT" != "minimal" && "$CODEX_REASONING_EFFORT" != "low" && "$CODEX_REASONING_EFFORT" != "medium" && "$CODEX_REASONING_EFFORT" != "high" && "$CODEX_REASONING_EFFORT" != "xhigh" ]]; then
  echo "error: --codex-reasoning-effort must be one of: minimal, low, medium, high, xhigh" >&2
  exit 1
fi
if ! [[ "$MIN_DESTABILIZATION_DEFECTS" =~ ^[0-9]+$ ]] || (( MIN_DESTABILIZATION_DEFECTS < 1 )); then
  echo "error: --min-destabilization-defects must be an integer >= 1" >&2
  exit 1
fi
if ! [[ "$MIN_RECOVERY_ITERATION_GAP" =~ ^[0-9]+$ ]] || (( MIN_RECOVERY_ITERATION_GAP < 1 )); then
  echo "error: --min-recovery-iteration-gap must be an integer >= 1" >&2
  exit 1
fi
if [[ -n "$MAX_PARALLEL_EPOCHS" ]] && { ! [[ "$MAX_PARALLEL_EPOCHS" =~ ^[0-9]+$ ]] || (( MAX_PARALLEL_EPOCHS < 1 )); }; then
  echo "error: --max-parallel-epochs must be an integer >= 1" >&2
  exit 1
fi
if ! python3 - "$MIN_DESTABILIZATION_BASELINE_MEAN" "$MAX_DESTABILIZATION_BASELINE_MEAN" <<'PY'
import sys
lo = float(sys.argv[1])
hi = float(sys.argv[2])
ok = 0 <= lo < hi <= 100
sys.exit(0 if ok else 1)
PY
then
  echo "error: require 0 <= --min-destabilization-baseline-mean < --max-destabilization-baseline-mean <= 100" >&2
  exit 1
fi

if [[ -z "$MAX_PARALLEL_EPOCHS" ]]; then
  MAX_PARALLEL_EPOCHS=$(( DEPTH * 3 ))
  if (( MAX_PARALLEL_EPOCHS < 12 )); then
    MAX_PARALLEL_EPOCHS=12
  fi
  if (( MAX_AUTONOMOUS_ITERATIONS > MAX_PARALLEL_EPOCHS )); then
    MAX_PARALLEL_EPOCHS="$MAX_AUTONOMOUS_ITERATIONS"
  fi
fi

if [[ "$PARALLEL_LINKS" == "1" ]]; then
  min_parallel_epochs="$DEPTH"
  if [[ "$REQUIRE_CHAIN_DESTABILIZATION" == "1" ]]; then
    min_parallel_epochs=$(( DEPTH * 2 ))
  fi
  if (( MAX_PARALLEL_EPOCHS < min_parallel_epochs )); then
    echo "autonomous_info=raising_max_parallel_epochs from ${MAX_PARALLEL_EPOCHS} to ${min_parallel_epochs} (depth=${DEPTH}, require_chain_destabilization=${REQUIRE_CHAIN_DESTABILIZATION})"
    MAX_PARALLEL_EPOCHS="$min_parallel_epochs"
  fi
  if (( MAX_AUTONOMOUS_ITERATIONS < MAX_PARALLEL_EPOCHS )); then
    echo "autonomous_info=raising_max_autonomous_iterations from ${MAX_AUTONOMOUS_ITERATIONS} to ${MAX_PARALLEL_EPOCHS} to match epoch budget"
    MAX_AUTONOMOUS_ITERATIONS="$MAX_PARALLEL_EPOCHS"
  fi
fi

prepare_cmd=(
  "$SCRIPT_DIR/rbd_run.sh"
  --prompt "$PROMPT"
  --depth "$DEPTH"
  --out-root "$OUT_ROOT"
  --project-vision "$PROJECT_VISION"
  --emitter "$EMITTER"
  --emitter-version "$EMITTER_VERSION"
  --project-name "$PROJECT_NAME"
  --skip-exec
)
if [[ -n "$RUN_NAME" ]]; then
  prepare_cmd+=(--name "$RUN_NAME")
fi
prepare_output="$("${prepare_cmd[@]}")"
printf '%s\n' "$prepare_output"

run_dir="$(printf '%s\n' "$prepare_output" | sed -n 's/^run prepared (execution skipped): //p' | tail -n 1)"
if [[ -z "$run_dir" ]]; then
  echo "error: failed to detect run directory from rbd_run output" >&2
  exit 1
fi

if [[ "$run_dir" != /* ]]; then
  run_dir="$(cd "$run_dir" && pwd)"
fi

echo "autonomous stability target: $run_dir"

if [[ "$PARALLEL_LINKS" == "1" ]]; then
  parallel_cmd=(
    python3 "$SCRIPT_DIR/rbd_parallel_links.py"
    --project-root "$run_dir"
    --iterations-dir iterations
    --depth "$DEPTH"
    --required-streak "$REQUIRED_STREAK"
    --max-epochs "$MAX_PARALLEL_EPOCHS"
    --codex-timeout-seconds "$CODEX_TIMEOUT_SECONDS"
    --codex-no-progress-seconds "$CODEX_NO_PROGRESS_SECONDS"
    --codex-reasoning-effort "$CODEX_REASONING_EFFORT"
    --codex-bin "$CODEX_BIN"
  )
  if [[ "$REQUIRE_CHAIN_DESTABILIZATION" == "1" ]]; then
    parallel_cmd+=(
      --require-chain-destabilization
      --min-destabilization-defects "$MIN_DESTABILIZATION_DEFECTS"
      --min-destabilization-baseline-mean "$MIN_DESTABILIZATION_BASELINE_MEAN"
      --max-destabilization-baseline-mean "$MAX_DESTABILIZATION_BASELINE_MEAN"
      --min-recovery-iteration-gap "$MIN_RECOVERY_ITERATION_GAP"
    )
  fi
  parallel_cmd+=(--max-total-iterations "$MAX_AUTONOMOUS_ITERATIONS")
  if [[ -n "$CODEX_MODEL" ]]; then
    parallel_cmd+=(--codex-model "$CODEX_MODEL")
  fi
  if (
    cd "$run_dir"
    "${parallel_cmd[@]}"
  ); then
    :
  else
    rc=$?
    echo "autonomous run failed (parallel mode): rc=$rc" >&2
    echo "run directory: $run_dir" >&2
    echo "stability status: $run_dir/STABILITY_STATUS.md" >&2
    exit "$rc"
  fi
else
  stabilize_cmd=(
    python3 "$SCRIPT_DIR/rbd_stabilize.py"
    --project-root "$run_dir"
    --iterations-dir iterations
    --depth "$DEPTH"
    --required-streak "$REQUIRED_STREAK"
    --request-stability
    --max-autonomous-iterations "$MAX_AUTONOMOUS_ITERATIONS"
    --codex-timeout-seconds "$CODEX_TIMEOUT_SECONDS"
    --codex-no-progress-seconds "$CODEX_NO_PROGRESS_SECONDS"
    --codex-reasoning-effort "$CODEX_REASONING_EFFORT"
    --codex-bin "$CODEX_BIN"
    --output STABILITY_STATUS.md
    --json-output STABILITY_STATUS.json
  )
  if [[ "$REQUIRE_CHAIN_DESTABILIZATION" == "1" ]]; then
    stabilize_cmd+=(
      --require-chain-destabilization
      --min-destabilization-defects "$MIN_DESTABILIZATION_DEFECTS"
      --min-destabilization-baseline-mean "$MIN_DESTABILIZATION_BASELINE_MEAN"
      --max-destabilization-baseline-mean "$MAX_DESTABILIZATION_BASELINE_MEAN"
      --min-recovery-iteration-gap "$MIN_RECOVERY_ITERATION_GAP"
    )
  fi
  if [[ -n "$CODEX_MODEL" ]]; then
    stabilize_cmd+=(--codex-model "$CODEX_MODEL")
  fi
  if (
    cd "$run_dir"
    "${stabilize_cmd[@]}"
  ); then
    :
  else
    rc=$?
    echo "autonomous run failed (sequential mode): rc=$rc" >&2
    echo "run directory: $run_dir" >&2
    echo "stability status: $run_dir/STABILITY_STATUS.md" >&2
    exit "$rc"
  fi
fi

promote_latest_parallel_worker_outputs() {
  local latest_worker_dir
  latest_worker_dir="$(
    find "$run_dir" -type f -path "*/parallel_epochs*/epoch_*/workers/*/FINAL_STATUS.md" -printf '%T@ %h\n' \
      | sort -nr \
      | awk 'NR==1 { print $2 }'
  )"
  if [[ -z "$latest_worker_dir" || ! -d "$latest_worker_dir" ]]; then
    return
  fi

  local run_level_files=(
    "ARTIFACT_MANIFEST.md"
    "PROMPT_SATISFACTION.md"
    "LIQUID_STATE_IDENTITY.md"
    "RUBRIC_SCORECARD_SUMMARY.md"
    "FINAL_STATUS.md"
    "OBJECTIVE_SPEC.md"
    "BEST_KNOWN_FRONTIER.md"
  )

  local file
  for file in "${run_level_files[@]}"; do
    if [[ -f "$latest_worker_dir/$file" ]]; then
      cp "$latest_worker_dir/$file" "$run_dir/$file"
    fi
  done
}

if [[ "$PARALLEL_LINKS" == "1" ]]; then
  promote_latest_parallel_worker_outputs
fi

if [[ -f "$SCRIPT_DIR/render_rubrics.py" ]]; then
  if ! python3 "$SCRIPT_DIR/render_rubrics.py" --run-dir "$run_dir" --output "$run_dir/RUBRICS_PRETTY_PRINT.md"; then
    rc=$?
    echo "warning: rubric renderer failed: rc=$rc (run continues)" >&2
  fi
fi

echo "autonomous run complete: $run_dir"
echo "stability status: $run_dir/STABILITY_STATUS.md"
