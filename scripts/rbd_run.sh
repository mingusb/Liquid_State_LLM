#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/rbd_run.sh --prompt <prompt.txt> --depth <N> [--name <run_name>] [--out-root runs] [--emitter scripts/emit_agents_md.py] [--emitter-version v1] [--project-vision required|disabled] [--renderer scripts/render_rubrics.py] [--validator scripts/validate_rubric_excellence.py] [--skip-exec]

Purpose:
  1) Create a project directory for one rubric-driven run.
  2) Emit AGENTS.md with nested rubric instructions to depth N.
  3) Give codex the prompt in that project directory.
  4) Produce a concrete project artifact plus rubric evidence files.

Outputs in run directory:
  - prompt.txt
  - AGENTS.md
  - RUBRIC_DIMENSIONS_AT_A_GLANCE.md
  - RUBRICS_PRETTY_PRINT.md
  - collateral/Rubric_*/manifest_iteration_*.md
  - collateral/Rubric_*/access_log_iteration_*.md
  - VISUAL_EVIDENCE_INDEX.md (when project vision is required)
  - WORK_PROMPT.md
  - codex.stdout.log / codex.stderr.log
  - LAST_MESSAGE.txt
  - ARTIFACT_MANIFEST.md
  - RUBRIC_SCORECARD_SUMMARY.md
  - FINAL_STATUS.md
USAGE
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROMPT=""
DEPTH=""
RUN_NAME=""
OUT_ROOT="runs"
EMITTER="$SCRIPT_DIR/emit_agents_md.py"
RENDERER="$SCRIPT_DIR/render_rubrics.py"
VALIDATOR="$SCRIPT_DIR/validate_rubric_excellence.py"
EMITTER_VERSION="v1"
SKIP_EXEC="0"
PROJECT_NAME="Nested Rubric-Driven Project"
CODEX_TIMEOUT_SECONDS="${CODEX_TIMEOUT_SECONDS:-0}"
MAX_REMEDIATION_ROUNDS="${MAX_REMEDIATION_ROUNDS:-3}"
PROJECT_VISION="required"

while (( $# > 0 )); do
  case "$1" in
    --prompt) PROMPT="${2:-}"; shift 2 ;;
    --depth) DEPTH="${2:-}"; shift 2 ;;
    --name) RUN_NAME="${2:-}"; shift 2 ;;
    --out-root) OUT_ROOT="${2:-}"; shift 2 ;;
    --emitter) EMITTER="${2:-}"; shift 2 ;;
    --renderer) RENDERER="${2:-}"; shift 2 ;;
    --validator) VALIDATOR="${2:-}"; shift 2 ;;
    --emitter-version) EMITTER_VERSION="${2:-}"; shift 2 ;;
    --project-name) PROJECT_NAME="${2:-}"; shift 2 ;;
    --project-vision) PROJECT_VISION="${2:-}"; shift 2 ;;
    --skip-exec) SKIP_EXEC="1"; shift 1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "error: unknown argument: $1" >&2; usage; exit 1 ;;
  esac
done

if [[ -z "$PROMPT" || -z "$DEPTH" ]]; then
  echo "error: --prompt and --depth are required" >&2
  usage
  exit 1
fi

if ! [[ "$DEPTH" =~ ^[0-9]+$ ]]; then
  echo "error: --depth must be an integer >= 0" >&2
  exit 1
fi

if [[ ! -f "$PROMPT" ]]; then
  echo "error: prompt file not found: $PROMPT" >&2
  exit 1
fi

if [[ ! -f "$EMITTER" ]]; then
  echo "error: emitter not found: $EMITTER" >&2
  exit 1
fi

if [[ ! -f "$VALIDATOR" ]]; then
  echo "error: validator not found: $VALIDATOR" >&2
  exit 1
fi

if [[ "$PROJECT_VISION" != "required" && "$PROJECT_VISION" != "disabled" ]]; then
  echo "error: --project-vision must be one of: required, disabled" >&2
  exit 1
fi

if ! [[ "$MAX_REMEDIATION_ROUNDS" =~ ^[0-9]+$ ]]; then
  echo "error: MAX_REMEDIATION_ROUNDS must be an integer >= 0" >&2
  exit 1
fi

timestamp="$(date +%Y%m%d_%H%M%S)"
prompt_base="$(basename "$PROMPT")"
prompt_slug="${prompt_base%.*}"
prompt_slug="${prompt_slug//[^A-Za-z0-9_-]/_}"
if [[ -z "$RUN_NAME" ]]; then
  RUN_NAME="${prompt_slug}_d${DEPTH}_${timestamp}"
fi

if [[ "$RUN_NAME" == */* || "$RUN_NAME" == *".."* ]]; then
  echo "error: --name must be a simple run label (no '/' or '..')" >&2
  exit 1
fi

out_root_abs="$(realpath -m "$OUT_ROOT")"
run_dir_abs="$(realpath -m "$out_root_abs/$RUN_NAME")"
case "$run_dir_abs" in
  "$out_root_abs"/*) ;;
  *)
    echo "error: computed run directory escapes --out-root" >&2
    echo "out_root=$out_root_abs run_dir=$run_dir_abs" >&2
    exit 1
    ;;
esac
mkdir -p "$run_dir_abs"
run_dir="$(cd "$run_dir_abs" && pwd)"

cp "$PROMPT" "$run_dir/prompt.txt"

# Stage minimal local project context so in-run development can inspect real
# command/script interfaces without escaping run scope.
repo_root="$(cd "$SCRIPT_DIR/.." && pwd)"
if [[ -f "$repo_root/rdd" ]]; then
  cp "$repo_root/rdd" "$run_dir/rdd"
  if ! chmod +x "$run_dir/rdd"; then
    echo "error: failed to set executable bit on $run_dir/rdd" >&2
    exit 1
  fi
fi
if [[ -d "$repo_root/scripts" ]]; then
  mkdir -p "$run_dir/scripts"
  cp -a "$repo_root/scripts/." "$run_dir/scripts/"
fi
if [[ -f "$repo_root/README.md" ]]; then
  cp "$repo_root/README.md" "$run_dir/README.md"
fi

# Pre-scaffold run structure so autonomous iterations do not start from a blank slate.
mkdir -p \
  "$run_dir/iterations" \
  "$run_dir/rubrics" \
  "$run_dir/scorecards" \
  "$run_dir/collateral" \
  "$run_dir/evidence" \
  "$run_dir/deltas" \
  "$run_dir/contradictions"
for (( rubric_idx=0; rubric_idx<=DEPTH; rubric_idx++ )); do
  mkdir -p \
    "$run_dir/rubrics/Rubric_${rubric_idx}" \
    "$run_dir/collateral/Rubric_${rubric_idx}"
done

python3 "$EMITTER" \
  --prompt-file "$run_dir/prompt.txt" \
  --depth "$DEPTH" \
  --output "$run_dir/AGENTS.md" \
  --dimensions-output "$run_dir/RUBRIC_DIMENSIONS_AT_A_GLANCE.md" \
  --project-name "$PROJECT_NAME" \
  --emitter-version "$EMITTER_VERSION" \
  --vision-mode "$PROJECT_VISION"

if [[ "$PROJECT_VISION" == "required" ]]; then
cat > "$run_dir/WORK_PROMPT.md" <<'EOF'
Read `AGENTS.md` and `prompt.txt`, then execute the project as specified.
Treat the current run directory as the only project scope; do not read or modify ancestor paths such as `../` or `../../`.
You are a Liquid State Machine on the Edge of Chaos.
Your purpose is to improve the project until `prompt.txt` is fully satisfied with traceable evidence.

Mandatory requirements:
1. Build the requested project artifact(s) from `prompt.txt`.
2. Apply nested rubric-driven development for all rubrics `Rubric_0..Rubric_N`.
3. Keep developing until every nested rubric cell is `100%`, with evidence.
4. Any framework/process edits must be prompt-agnostic; do not add artifact-specific heuristics keyed to this prompt (for example special-casing `README.md`).
5. Include visual/perceptual evaluation in development and scoring.
6. Use Vision tool (`view_image`) on generated visual artifacts when applicable.
7. Produce evidence-backed scorecards and anti-gaming checks.
8. Set `x_axis` to exactly the canonical 16 role categories `R0..R15` (one entry per role, no extras, no omissions, no duplicates).
9. Set `y_axis` to role-contributed dimensions sourced from `role_sections[].sub_dimensions`; each role `R0..R15` must contribute at least 2 dimensions, and fixed/copied Y templates are invalid unless evidence-justified.
10. For each rubric JSON, map every contributed role dimension to one or more concrete X×Y cells in `role_sections[].covered_cells`, and include `axis_cardinality_rationale`, `axis_selection_rationale`, `axis_generation_evidence_refs`, and `axis_alternatives_considered`.
11. For each rubric JSON, include `task_conformance_rationale`, `prompt_requirement_trace`, and `prompt_transmogrification_log`.
12. `prompt_requirement_trace` must map each prompt requirement to addressed axes/cells, adaptation strategy, and evidence refs.
13. `prompt_transmogrification_log` must record how the rubric structure changed in response to prompt-linked defects.
14. For each rubric JSON (`Rubric_0..Rubric_N`, including meta-rubrics), include `company_roles` and `role_sections` for a mandatory 16-role company model (`N16`), with role-scoped concerns/sub-dimensions and evidence-linked covered axes/cells that trace each role-contributed dimension to covered cells.
15. Judge evaluations must assess rubric quality through these company role concerns (not generic dimensions only) and trace findings to role-scoped evidence.
16. For each rubric JSON, include `axis_task_alignment` with full one-to-one X/Y coverage: every axis dimension appears exactly once and maps to prompt-success mechanisms, requirement IDs, and evidence refs.
17. Every rubric's `target_collateral_manifest` must include `prompt.txt` so judges can score against explicit task requirements.
18. For any judge artifacts you produce (baseline/recheck/final decision/status), include parseable bullets: `prompt_source: prompt.txt`, `prompt_consumed: yes`, and `prompt_requirements_considered: <count>`.
19. Set `schema_version` to `rubric.v2` in every rubric JSON.
20. Treat each rubric as an operational decision tool, not a label matrix.
21. Provide `x_axis_specs` and `y_axis_specs` with `name`, `definition`, `failure_mode`, `discriminator`, `intervention`, `measurement_protocol`, `evidence_expectation`, `anti_gaming_probe`, `example_pass_case`, `example_fail_case`, and `scoring_anchors` (`0`,`50`,`80`,`100`).
22. Avoid generic one-word dimensions (for example `Quality`, `Completeness`, `Correctness`) unless domain-qualified and empirically measurable.
23. In `axis_alternatives_considered`, `kept=true` entries must enumerate all final X and Y dimensions (not just one).
24. Write anti-gaming probes as executable checks using concrete verbs (for example: verify/check/inspect/attempt tamper/recompute and compare).
25. Make `Rubric_0` exceptionally insightful and discriminative for product/document excellence; avoid checklist-style shallowness.
26. Make each `Rubric_k` (`k>0`) explicitly improve `Rubric_(k-1)` and state the specific predecessor weaknesses addressed in `improvement_intent`.
27. Avoid templated specs: each dimension needs distinct measurement protocol and anti-gaming probe.
28. Avoid templated cells: rationale and evidence mapping must be specific to each X×Y cell, not copy/pasted.
29. Keep iterating until AGENTS definition-of-done is satisfied or document blockers.
30. Write dimension names as human-readable conceptual phrases, not code-style snake_case identifiers.
31. In Rubric_0, ensure dimensions explicitly cover user/stakeholder outcomes, technical rigor, robustness under failure/adversarial pressure, and evidence trustworthiness.
32. Ensure each dimension spec is dimension-specific: key tokens from the dimension name must appear in definition/measurement/probe text.
33. Ensure at least half of cells have distinct evidence sets; if every cell cites identical evidence refs, this is invalid.
34. Run rubric self-audit before finishing and reject your own output if it looks templated or generic.
35. For each rubric JSON, include `target_collateral_manifest`, `target_collateral_access_log`, and `target_collateral_coverage_percent`.
36. For every `Rubric_k` (`k>=1`), target collateral must reference `Rubric_(k-1)` outputs (rubric JSON, scorecards, evidence, deltas, and contradiction files).
37. For every scored cell, include non-empty `collateral_refs` mapped to entries in `target_collateral_manifest`.
38. Operate as a liquid state machine: after prompt injection, drive non-trivial destabilization, develop under instability, and only claim stabilization after prompt requirements are fully satisfied with evidence.
39. Maintain an identity lock: `LIQUID_STATE_IDENTITY.md` must contain exactly `You are a Liquid State Machine on the Edge of Chaos.` and chain decision artifacts must reflect `identity_lock=yes`.

Required output files:
- `RUBRIC_DIMENSIONS_AT_A_GLANCE.md`:
  compact table view of all layer dimensions; keep it aligned with final rubrics.
- `VISUAL_EVIDENCE_INDEX.md`:
  list visual evidence paths, what each shows, and how it affected rubric scoring.
  If no visual surface exists, include explicit N/A justification.
- `ARTIFACT_MANIFEST.md`:
  list each final artifact path and what it proves.
- `RUBRIC_SCORECARD_SUMMARY.md`:
  summarize per-layer pass/fail and score means, with scorecard links.
- `PROMPT_SATISFACTION.md`:
  map each prompt requirement to implementation/evidence paths and mark satisfied vs unsatisfied.
- `LIQUID_STATE_IDENTITY.md`:
  include the exact line `You are a Liquid State Machine on the Edge of Chaos.`
- `FINAL_STATUS.md`:
  explicit done checklist against AGENTS definition-of-done.
- `rubrics/Rubric_0_Role_Expansion_Pack_N16.md` ... `rubrics/Rubric_N_Role_Expansion_Pack_N16.md`
- `scorecards/Rubric_0_grid_iteration_*.md` ... `scorecards/Rubric_N_grid_iteration_*.md`
- `collateral/Rubric_0/manifest_iteration_*.md` ... `collateral/Rubric_N/manifest_iteration_*.md`
- `collateral/Rubric_0/access_log_iteration_*.md` ... `collateral/Rubric_N/access_log_iteration_*.md`
- `visual/iteration_XXX/*`
- `evidence/iteration_*.md`
- `deltas/iteration_*.md`
- `contradictions/iteration_*.md`
EOF
else
cat > "$run_dir/WORK_PROMPT.md" <<'EOF'
Read `AGENTS.md` and `prompt.txt`, then execute the project as specified.
Treat the current run directory as the only project scope; do not read or modify ancestor paths such as `../` or `../../`.
You are a Liquid State Machine on the Edge of Chaos.
Your purpose is to improve the project until `prompt.txt` is fully satisfied with traceable evidence.

Mandatory requirements:
1. Build the requested project artifact(s) from `prompt.txt`.
2. Apply nested rubric-driven development for all rubrics `Rubric_0..Rubric_N`.
3. Keep developing until every nested rubric cell is `100%`, with evidence.
4. Any framework/process edits must be prompt-agnostic; do not add artifact-specific heuristics keyed to this prompt (for example special-casing `README.md`).
5. Project-side vision scoring is disabled for this run.
6. Produce evidence-backed scorecards and anti-gaming checks.
7. Set `x_axis` to exactly the canonical 16 role categories `R0..R15` (one entry per role, no extras, no omissions, no duplicates).
8. Set `y_axis` to role-contributed dimensions sourced from `role_sections[].sub_dimensions`; each role `R0..R15` must contribute at least 2 dimensions, and fixed/copied Y templates are invalid unless evidence-justified.
9. For each rubric JSON, map every contributed role dimension to one or more concrete X×Y cells in `role_sections[].covered_cells`, and include `axis_cardinality_rationale`, `axis_selection_rationale`, `axis_generation_evidence_refs`, and `axis_alternatives_considered`.
10. For each rubric JSON, include `task_conformance_rationale`, `prompt_requirement_trace`, and `prompt_transmogrification_log`.
11. `prompt_requirement_trace` must map each prompt requirement to addressed axes/cells, adaptation strategy, and evidence refs.
12. `prompt_transmogrification_log` must record how the rubric structure changed in response to prompt-linked defects.
13. For each rubric JSON (`Rubric_0..Rubric_N`, including meta-rubrics), include `company_roles` and `role_sections` for a mandatory 16-role company model (`N16`), with role-scoped concerns/sub-dimensions and evidence-linked covered axes/cells that trace each role-contributed dimension to covered cells.
14. Judge evaluations must assess rubric quality through these company role concerns (not generic dimensions only) and trace findings to role-scoped evidence.
15. For each rubric JSON, include `axis_task_alignment` with full one-to-one X/Y coverage: every axis dimension appears exactly once and maps to prompt-success mechanisms, requirement IDs, and evidence refs.
16. Every rubric's `target_collateral_manifest` must include `prompt.txt` so judges can score against explicit task requirements.
17. For any judge artifacts you produce (baseline/recheck/final decision/status), include parseable bullets: `prompt_source: prompt.txt`, `prompt_consumed: yes`, and `prompt_requirements_considered: <count>`.
18. Set `schema_version` to `rubric.v2` in every rubric JSON.
19. Treat each rubric as an operational decision tool, not a label matrix.
20. Provide `x_axis_specs` and `y_axis_specs` with `name`, `definition`, `failure_mode`, `discriminator`, `intervention`, `measurement_protocol`, `evidence_expectation`, `anti_gaming_probe`, `example_pass_case`, `example_fail_case`, and `scoring_anchors` (`0`,`50`,`80`,`100`).
21. Avoid generic one-word dimensions (for example `Quality`, `Completeness`, `Correctness`) unless domain-qualified and empirically measurable.
22. In `axis_alternatives_considered`, `kept=true` entries must enumerate all final X and Y dimensions (not just one).
23. Write anti-gaming probes as executable checks using concrete verbs (for example: verify/check/inspect/attempt tamper/recompute and compare).
24. Make `Rubric_0` exceptionally insightful and discriminative for product/document excellence; avoid checklist-style shallowness.
25. Make each `Rubric_k` (`k>0`) explicitly improve `Rubric_(k-1)` and state the specific predecessor weaknesses addressed in `improvement_intent`.
26. Avoid templated specs: each dimension needs distinct measurement protocol and anti-gaming probe.
27. Avoid templated cells: rationale and evidence mapping must be specific to each X×Y cell, not copy/pasted.
28. Keep iterating until AGENTS definition-of-done is satisfied or document blockers.
29. Write dimension names as human-readable conceptual phrases, not code-style snake_case identifiers.
30. In Rubric_0, ensure dimensions explicitly cover user/stakeholder outcomes, technical rigor, robustness under failure/adversarial pressure, and evidence trustworthiness.
31. Ensure each dimension spec is dimension-specific: key tokens from the dimension name must appear in definition/measurement/probe text.
32. Ensure at least half of cells have distinct evidence sets; if every cell cites identical evidence refs, this is invalid.
33. Run rubric self-audit before finishing and reject your own output if it looks templated or generic.
34. For each rubric JSON, include `target_collateral_manifest`, `target_collateral_access_log`, and `target_collateral_coverage_percent`.
35. For every `Rubric_k` (`k>=1`), target collateral must reference `Rubric_(k-1)` outputs (rubric JSON, scorecards, evidence, deltas, and contradiction files).
36. For every scored cell, include non-empty `collateral_refs` mapped to entries in `target_collateral_manifest`.
37. Operate as a liquid state machine: after prompt injection, drive non-trivial destabilization, develop under instability, and only claim stabilization after prompt requirements are fully satisfied with evidence.
38. Maintain an identity lock: `LIQUID_STATE_IDENTITY.md` must contain exactly `You are a Liquid State Machine on the Edge of Chaos.` and chain decision artifacts must reflect `identity_lock=yes`.

Required output files:
- `RUBRIC_DIMENSIONS_AT_A_GLANCE.md`:
  compact table view of all layer dimensions; keep it aligned with final rubrics.
- `ARTIFACT_MANIFEST.md`:
  list each final artifact path and what it proves.
- `RUBRIC_SCORECARD_SUMMARY.md`:
  summarize per-layer pass/fail and score means, with scorecard links.
- `PROMPT_SATISFACTION.md`:
  map each prompt requirement to implementation/evidence paths and mark satisfied vs unsatisfied.
- `LIQUID_STATE_IDENTITY.md`:
  include the exact line `You are a Liquid State Machine on the Edge of Chaos.`
- `FINAL_STATUS.md`:
  explicit done checklist against AGENTS definition-of-done.
- `rubrics/Rubric_0_Role_Expansion_Pack_N16.md` ... `rubrics/Rubric_N_Role_Expansion_Pack_N16.md`
- `scorecards/Rubric_0_grid_iteration_*.md` ... `scorecards/Rubric_N_grid_iteration_*.md`
- `collateral/Rubric_0/manifest_iteration_*.md` ... `collateral/Rubric_N/manifest_iteration_*.md`
- `collateral/Rubric_0/access_log_iteration_*.md` ... `collateral/Rubric_N/access_log_iteration_*.md`
- `evidence/iteration_*.md`
- `deltas/iteration_*.md`
- `contradictions/iteration_*.md`
EOF
fi

cat > "$run_dir/RUN_METADATA.md" <<EOF
# Run Metadata

- run_dir: \`${run_dir}\`
- prompt_source: \`${PROMPT}\`
- depth: \`N=${DEPTH}\`
- emitter: \`${EMITTER}\`
- emitter_version: \`${EMITTER_VERSION}\`
- vision_policy: \`${PROJECT_VISION}\`
- generated_utc: \`$(date -u +%Y-%m-%dT%H:%M:%SZ)\`
EOF

if [[ "$SKIP_EXEC" == "1" ]]; then
  echo "run prepared (execution skipped): $run_dir"
  exit 0
fi

if ! command -v codex >/dev/null 2>&1; then
  echo "error: codex command not found in PATH" >&2
  exit 1
fi

if ! [[ "$CODEX_TIMEOUT_SECONDS" =~ ^[0-9]+$ ]] || (( CODEX_TIMEOUT_SECONDS < 0 )); then
  echo "error: CODEX_TIMEOUT_SECONDS must be integer >= 0 (0 disables timeout)" >&2
  exit 1
fi

run_codex_exec() {
  local input_prompt="$1"
  local out_log="$2"
  local err_log="$3"
  local out_msg="$4"
  if (( CODEX_TIMEOUT_SECONDS <= 0 )); then
    env GIT_CEILING_DIRECTORIES="$run_dir" \
      codex exec \
        --skip-git-repo-check \
        --sandbox danger-full-access \
        -c approval_policy=never \
        -C "$run_dir" \
        -o "$out_msg" \
        - < "$input_prompt" \
        > "$out_log" 2> "$err_log"
  else
    timeout --signal=TERM --kill-after=30s "${CODEX_TIMEOUT_SECONDS}s" \
      env GIT_CEILING_DIRECTORIES="$run_dir" \
      codex exec \
        --skip-git-repo-check \
        --sandbox danger-full-access \
        -c approval_policy=never \
        -C "$run_dir" \
        -o "$out_msg" \
        - < "$input_prompt" \
        > "$out_log" 2> "$err_log"
  fi
}

run_excellence_validator() {
  python3 "$VALIDATOR" \
    --run-dir "$run_dir" \
    --json-out "$run_dir/rubric_excellence_report.json" \
    > "$run_dir/rubric_excellence_report.txt"
}

if ! run_codex_exec \
  "$run_dir/WORK_PROMPT.md" \
  "$run_dir/codex.stdout.log" \
  "$run_dir/codex.stderr.log" \
  "$run_dir/LAST_MESSAGE.txt"; then
  echo "error: codex execution failed for $run_dir" >&2
  exit 1
fi

excellence_failed=0
if ! run_excellence_validator; then
  excellence_failed=1
  for (( round=1; round<=MAX_REMEDIATION_ROUNDS; round++ )); do
    remediation_prompt="$run_dir/REMEDIATION_PROMPT_round_${round}.md"
    cat > "$remediation_prompt" <<'EOF'
Read \`AGENTS.md\`, \`WORK_PROMPT.md\`, \`prompt.txt\`, and \`rubric_excellence_report.txt\`.

The current run failed rubric excellence gates. Repair the project artifacts and all rubric files so the validator passes with zero errors.
Keep fixes prompt-agnostic: do not introduce artifact-specific logic keyed to this prompt (for example special-casing `README.md`).

Non-negotiable fixes:
1. Replace templated specs with dimension-specific specs.
2. Replace templated cell rationales and evidence mappings with cell-specific content.
3. Add or strengthen \`improvement_intent\` in every rubric.
4. Use human-readable conceptual dimension names (not code-style identifiers).
5. Keep chain contract intact: every cell in every rubric must remain at 100% with traceable evidence.
6. Set \`schema_version\` to \`rubric.v2\` for every rubric JSON.
7. Ensure every rubric has \`target_collateral_manifest\`, \`target_collateral_access_log\`, and \`target_collateral_coverage_percent\`.
8. Ensure every cell has non-empty \`collateral_refs\` mapped to the rubric's collateral manifest.
9. Regenerate all required outputs and summaries.
10. Ensure `LIQUID_STATE_IDENTITY.md` contains the exact identity line and `PROMPT_SATISFACTION.md` marks every prompt requirement as satisfied with evidence links.

Do not stop after partial edits; finish only when the run is internally coherent and validator-ready.
EOF

    if ! run_codex_exec \
      "$remediation_prompt" \
      "$run_dir/codex.remediate.round_${round}.stdout.log" \
      "$run_dir/codex.remediate.round_${round}.stderr.log" \
      "$run_dir/LAST_MESSAGE.txt"; then
      echo "error: codex remediation round ${round} failed for $run_dir" >&2
      break
    fi

    if run_excellence_validator; then
      excellence_failed=0
      break
    fi
  done
fi

if [[ -f "$RENDERER" ]]; then
  if ! python3 "$RENDERER" --run-dir "$run_dir" --output "$run_dir/RUBRICS_PRETTY_PRINT.md"; then
    echo "warning: failed to render RUBRICS_PRETTY_PRINT.md via $RENDERER" >&2
  fi
else
  echo "warning: renderer not found, skipping pretty rubric render: $RENDERER" >&2
fi

missing=0
required_files=(
  "$run_dir/RUBRIC_DIMENSIONS_AT_A_GLANCE.md"
  "$run_dir/RUBRICS_PRETTY_PRINT.md"
  "$run_dir/ARTIFACT_MANIFEST.md"
  "$run_dir/RUBRIC_SCORECARD_SUMMARY.md"
  "$run_dir/PROMPT_SATISFACTION.md"
  "$run_dir/LIQUID_STATE_IDENTITY.md"
  "$run_dir/FINAL_STATUS.md"
)
if [[ "$PROJECT_VISION" == "required" ]]; then
  required_files+=("$run_dir/VISUAL_EVIDENCE_INDEX.md")
fi
for required in "${required_files[@]}"; do
  if [[ ! -f "$required" ]]; then
    echo "warning: missing required output: $required" >&2
    missing=1
  fi
done

collateral_max_idx="$DEPTH"
if (( DEPTH >= 1 )); then
  collateral_max_idx=$((DEPTH - 1))
fi
for (( rubric_idx=0; rubric_idx<=collateral_max_idx; rubric_idx++ )); do
  manifest_found="$(find "$run_dir" -type f -path "*/collateral/Rubric_${rubric_idx}/manifest_iteration_*.md" -print -quit)"
  access_found="$(find "$run_dir" -type f -path "*/collateral/Rubric_${rubric_idx}/access_log_iteration_*.md" -print -quit)"
  if [[ -z "$manifest_found" ]]; then
    echo "warning: missing collateral manifest for Rubric_${rubric_idx} under: $run_dir/**/collateral/Rubric_${rubric_idx}/manifest_iteration_*.md" >&2
    missing=1
  fi
  if [[ -z "$access_found" ]]; then
    echo "warning: missing collateral access log for Rubric_${rubric_idx} under: $run_dir/**/collateral/Rubric_${rubric_idx}/access_log_iteration_*.md" >&2
    missing=1
  fi
done

if (( excellence_failed == 1 )); then
  echo "warning: rubric excellence validator still failing after remediation rounds" >&2
  echo "warning: see $run_dir/rubric_excellence_report.txt" >&2
  missing=1
fi

echo "run complete: $run_dir"
if (( missing == 1 )); then
  echo "run completed with missing required outputs" >&2
  exit 1
fi
