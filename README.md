# Liquid State Large Language Model Harness

This is a self-improving harness for LLMs (currently tested on OpenAI Codex 5.3 low/xhigh and Codex Spark). It is based on the core idea of heirarchical rubrics, such that there is a meta-rubric that is used to score the rubric, and a meta-meta-rubric to score that rubric, and so on. Rubric dimensions correspond to N roles in a company, with each role contributing a number of dimensions to each layer of rubric. Rubrics are scored by judges. Additionally, the entire chain of rubrics is repeatedly destabilized and redeveloped. The prompts, such as AGENTS.md, encourage the LLM to act as a Liquid State Machine on the Edge of Chaos. This harness is capable of self-improvement, which is how it has been developed thus far. It is not particularly efficient or effective, and can only be used with a Pro-tier ($200/month) subscription to GPT. Benefits include that it is relatively well developed, and easy to use. Additionally, large numbers of sub-agent swarms have been repeatedly deployed to seek out and fix bugs in the project. However, there are no tests.

## Default Workflow

Use this as the primary operator path:

```bash
./rdd --prompt <prompt.txt> --depth <N>
```

Example:

```bash
./rdd --prompt prompt.txt --depth 5
```

## Quickstart

```bash
# 1) Start a run
./rdd --prompt prompt.txt --depth 5

# 2) Resolve latest run directory
RUN_DIR="$(ls -td runs/* 2>/dev/null | head -n 1)"

# 3) Inspect stability state and next required chain
sed -n '1,260p' "$RUN_DIR/STABILITY_STATUS.md"

# 4) Inspect latest recheck decision
LATEST_ITER="$(ls -td "$RUN_DIR"/iterations/iteration_* 2>/dev/null | head -n 1)"
sed -n '1,260p' "$LATEST_ITER/judge_recheck/FINAL_DECISION.md"
```

## Stability Model (Chaos To Recovery)

Stability is not immediate pass-through. For a given depth `N`, every adjacency chain must reconverge:

`Rubric_N -> Rubric_(N-1) -> ... -> Rubric_1 -> Rubric_0`.

A chain only counts as recovered when all required gates pass:

- `decision=ACCEPT`
- `recheck_mean=100.0`
- `recheck_total_defects=0`
- `recheck_blocking_defects=0`
- `identity_lock=yes`
- `prompt_satisfaction=yes`

Before recovery can count, each chain must first show prompt-linked destabilization:

- non-trivial baseline defects (`baseline_total_defects >= 3`)
- baseline quality in the edge band (`40.0 <= baseline_mean <= 95.0`)
- explicit prompt linkage in judge artifacts

Recovery must occur in later iteration(s), not the same counted step as first destabilization (`min_recovery_iteration_gap=1`).

## Core Commands

```bash
# Recompute stability from existing artifacts
python3 scripts/rbd_stabilize.py \
  --project-root "$RUN_DIR" \
  --iterations-dir iterations \
  --depth 5 \
  --required-streak 1 \
  --output "$RUN_DIR/STABILITY_STATUS.md" \
  --json-output "$RUN_DIR/STABILITY_STATUS.json"

# Pretty-print all rubric layers
python3 scripts/render_rubrics.py --run-dir "$RUN_DIR" --chunk-size 8

# Render compact LSM dashboard
python3 scripts/render_lsm_dashboard.py --run-dir "$RUN_DIR"

# Render per-epoch chain stats
python3 scripts/render_epoch_batch_link_stats.py --run-dir "$RUN_DIR"

# Validate rubric quality and anti-gaming constraints
python3 scripts/validate_rubric_excellence.py --run-dir "$RUN_DIR"
```

## Script Index

| Script | Purpose | Use when |
| --- | --- | --- |
| `./rdd` | Primary entrypoint (`scripts/rdd.sh`). | Normal operation. |
| `scripts/rdd.sh` | Applies default profile and forwards advanced options. | You need wrapper-level control. |
| `scripts/rbd_autonomous.sh` | Creates run scaffold and drives autonomous stabilization. | You need model/timeout/iteration tuning. |
| `scripts/rbd_parallel_links.py` | Parallel epoch orchestrator across chain links. | You are debugging/controlling merge order and epochs. |
| `scripts/rbd_stabilize.py` | Computes or drives stability (including single-chain mode). | You need stability recompute or targeted chain execution. |
| `scripts/rbd_run.sh` | Run setup and policy emission (`AGENTS.md`, schema, scaffolding). | You need setup-only (`--skip-exec`) or emitter testing. |
| `scripts/emit_agents_md.py` | Generates run `AGENTS.md`, schema, and dimensions metadata. | You are developing AGENTS/rubric policy generation. |
| `scripts/render_rubrics.py` | Produces readable rubric tables from JSON/scorecards. | You need rubric inspection. |
| `scripts/render_lsm_dashboard.py` | Produces compact run dashboard. | You need at-a-glance convergence view. |
| `scripts/render_epoch_batch_link_stats.py` | Produces per-epoch link metrics. | You need mechanism-level debug traces. |
| `scripts/validate_rubric_excellence.py` | Validates rubric structure, evidence, and anti-gaming rules. | Quality gates fail or results look over-optimistic. |
| `scripts/rbd_compare.sh` | Baseline vs candidate process comparison. | You are evaluating process changes. |
| `scripts/rbd_mine.sh` | Self-improvement mining and candidate promotion. | You want iterative process improvement campaigns. |

## Run Output Layout

Each run at `runs/<run_name>/` is expected to include:

- `prompt.txt`, `AGENTS.md`, `RUBRIC_SCHEMA.json`
- `STABILITY_STATUS.md`, `STABILITY_STATUS.json`
- `RUBRICS_PRETTY_PRINT.md`, `RUBRIC_SCORECARD_SUMMARY.md`
- `ARTIFACT_MANIFEST.md`, `PROMPT_SATISFACTION.md`, `FINAL_STATUS.md`
- `iterations/iteration_XXX/...`
- `rubrics/`, `scorecards/`, `collateral/`, `evidence/`, `deltas/`, `contradictions/`

## Troubleshooting

### Timeouts or early exits

```bash
./rdd --prompt prompt.txt --depth 5 --codex-timeout-seconds 1800
./rdd --prompt prompt.txt --depth 5 --codex-timeout-seconds 0
```

### Stalled progression

```bash
RUN_DIR="$(ls -td runs/* 2>/dev/null | head -n 1)"
sed -n '1,260p' "$RUN_DIR/STABILITY_STATUS.md"
LATEST_ITER="$(ls -td "$RUN_DIR"/iterations/iteration_* 2>/dev/null | head -n 1)"
sed -n '1,260p' "$LATEST_ITER/judge_recheck/PRIORITIZED_DEFECTS.md"
```

If it is still improving but not converged, increase budget:

```bash
./rdd --prompt prompt.txt --depth 5 --max-autonomous-iterations 40
```

### Missing collateral/evidence linkage

```bash
RUN_DIR="$(ls -td runs/* 2>/dev/null | head -n 1)"
python3 scripts/validate_rubric_excellence.py --run-dir "$RUN_DIR"
```

Check for:

- `collateral/Rubric_<k>/manifest_iteration_XXX.md`
- `collateral/Rubric_<k>/access_log_iteration_XXX.md`

### `stable: false` after many iterations

Typical causes:

- one or more chains still have recheck blockers/defects,
- `prompt_satisfaction` is not explicitly `yes`,
- destabilization/recovery accounting not yet satisfied for one or more chains.

Primary diagnostics:

- `STABILITY_STATUS.md`
- `STABILITY_STATUS.json`
- latest `iterations/iteration_XXX/judge_recheck/FINAL_DECISION.md`

## Terminology

- `rubric-driven development`: prompt-driven iterative development governed by auditable rubrics.
- `Rubric_0..Rubric_N`: hierarchy where `Rubric_0` scores project artifacts and each higher rubric scores the one below it.
- `stability`: full-chain perfect reconvergence after required destabilization with explicit prompt satisfaction.

## Requirements

- `bash`
- `python3`
- `codex` in `PATH`
