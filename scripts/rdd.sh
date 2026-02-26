#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/rdd.sh --prompt <prompt.txt> --depth <N> [advanced options...]

Default profile:
  - parallel_links=true
  - max_parallel_epochs=auto (>= max_autonomous_iterations and >= 3*depth; floor 12)
  - required_streak=1
  - require_chain_destabilization=true
  - min_destabilization_defects=3
  - min_destabilization_baseline_mean=40
  - max_destabilization_baseline_mean=95
  - min_recovery_iteration_gap=1
  - max_autonomous_iterations=20
  - codex_timeout_seconds=0 (disabled)
  - codex_no_progress_seconds=0
  - codex_reasoning_effort=xhigh

Notes:
  - This is the default entrypoint for prompt-driven autonomous development.
  - Any additional args are forwarded to `scripts/rbd_autonomous.sh`.
USAGE
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROMPT=""
DEPTH=""
FORWARD_ARGS=()

while (( $# > 0 )); do
  case "$1" in
    --prompt|-p) PROMPT="${2:-}"; shift 2 ;;
    --depth|-d) DEPTH="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    --) shift; FORWARD_ARGS+=("$@"); break ;;
    *) FORWARD_ARGS+=("$1"); shift 1 ;;
  esac
done

if [[ -z "$PROMPT" || -z "$DEPTH" ]]; then
  echo "error: --prompt and --depth are required" >&2
  usage
  exit 1
fi
if ! [[ "$DEPTH" =~ ^[0-9]+$ ]]; then
  echo "error: --depth must be an integer >= 0" >&2
  usage
  exit 1
fi

PARALLEL_LINKS_FLAG="--parallel-links"
case "${RDD_PARALLEL_LINKS:-1}" in
  0|false|FALSE|no|NO) PARALLEL_LINKS_FLAG="" ;;
esac

MAX_PARALLEL_EPOCHS="${RDD_MAX_PARALLEL_EPOCHS:-}"
if [[ -z "$MAX_PARALLEL_EPOCHS" ]]; then
  MAX_PARALLEL_EPOCHS=$(( DEPTH * 3 ))
  if (( MAX_PARALLEL_EPOCHS < 12 )); then
    MAX_PARALLEL_EPOCHS=12
  fi
  MAX_AUTONOMOUS_ITERS="${RDD_MAX_AUTONOMOUS_ITERATIONS:-20}"
  if [[ "$MAX_AUTONOMOUS_ITERS" =~ ^[0-9]+$ ]] && (( MAX_AUTONOMOUS_ITERS > MAX_PARALLEL_EPOCHS )); then
    MAX_PARALLEL_EPOCHS="$MAX_AUTONOMOUS_ITERS"
  fi
fi

exec "$SCRIPT_DIR/rbd_autonomous.sh" \
  --prompt "$PROMPT" \
  --depth "$DEPTH" \
  $PARALLEL_LINKS_FLAG \
  --max-parallel-epochs "$MAX_PARALLEL_EPOCHS" \
  --required-streak "${RDD_REQUIRED_STREAK:-1}" \
  --max-autonomous-iterations "${RDD_MAX_AUTONOMOUS_ITERATIONS:-20}" \
  --codex-timeout-seconds "${RDD_CODEX_TIMEOUT_SECONDS:-0}" \
  --codex-no-progress-seconds "${RDD_CODEX_NO_PROGRESS_SECONDS:-0}" \
  --codex-reasoning-effort "${RDD_CODEX_REASONING_EFFORT:-xhigh}" \
  --min-destabilization-defects "${RDD_MIN_DESTABILIZATION_DEFECTS:-3}" \
  --min-destabilization-baseline-mean "${RDD_MIN_DESTABILIZATION_BASELINE_MEAN:-40}" \
  --max-destabilization-baseline-mean "${RDD_MAX_DESTABILIZATION_BASELINE_MEAN:-95}" \
  --min-recovery-iteration-gap "${RDD_MIN_RECOVERY_ITERATION_GAP:-1}" \
  "${FORWARD_ARGS[@]}"
