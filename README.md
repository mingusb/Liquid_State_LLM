# Liquid State Large Language Model Harness (LSLLM)

Prompt-driven autonomous development harness using nested rubric chains (`Rubric_0..Rubric_N`) with strict stability gates.

## Overview

This project runs rubric-driven development where:

- `Rubric_0` scores the project artifact.
- each higher rubric scores the rubric below it.
- chain-level judging, remediation, and recheck loops continue until stability criteria are satisfied.

The harness has been exercised with Codex 5.3 (`low` and `xhigh`) and Codex Spark runs. It is actively under development.

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

For depth `N`, all adjacency chains must reconverge:

```text
Rubric_N -> Rubric_(N-1) -> ... -> Rubric_1 -> Rubric_0
```

A chain only counts as recovered when all required gates pass:

- `decision=ACCEPT`
- `recheck_mean=100.0`
- `recheck_total_defects=0`
- `recheck_blocking_defects=0`
- `identity_lock=yes`
- `prompt_satisfaction=yes`

Before recovery is recognized, each chain must first demonstrate prompt-linked destabilization:

- non-trivial baseline defects: `baseline_total_defects >= 3`
- baseline quality in edge band: `40.0 <= baseline_mean <= 95.0`
- explicit prompt linkage in judge artifacts

Recovery must occur in later iterations (not the same counted step as first destabilization):

- `min_recovery_iteration_gap=1`

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
| `scripts/rbd_parallel_links.py` | Parallel epoch orchestrator across chain links. | You are debugging or controlling merge order and epochs. |
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

Each run in `runs/<run_name>/` should include:

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

### Missing collateral or evidence linkage

```bash
RUN_DIR="$(ls -td runs/* 2>/dev/null | head -n 1)"
python3 scripts/validate_rubric_excellence.py --run-dir "$RUN_DIR"
```

Check for both files per rubric:

- `collateral/Rubric_<k>/manifest_iteration_XXX.md`
- `collateral/Rubric_<k>/access_log_iteration_XXX.md`

### `stable: false` after many iterations

Common causes:

- one or more chains still have blockers/defects at recheck
- `prompt_satisfaction` is not explicitly `yes`
- destabilization/recovery accounting is not yet satisfied for one or more chains

Primary diagnostics:

- `STABILITY_STATUS.md`
- `STABILITY_STATUS.json`
- latest `iterations/iteration_XXX/judge_recheck/FINAL_DECISION.md`

## Latest Dashboard

Source snapshot: `scorecards/LSM_DASHBOARD.md`

To regenerate with current run data:

```bash
python3 scripts/render_lsm_dashboard.py --run-dir "$RUN_DIR"
```

### Snapshot

- run: `depth5_codex_low_restart_20260226T015701Z`
- epochs: `19`
- final_phase: `reservoir_perturbation`
- stable: `no`

### Legend

```text
+-----------+----------+--------------------+------------------+-------------------+------------+
| TOKEN     | KIND     | D1                 | D2               | D3                | D4         |
+-----------+----------+--------------------+------------------+-------------------+------------+
| [S][D][M] | cell     | chain code triplet |                  |                   |            |
| S         | phase    | 3 = edge           | 4 = train        | 5 = reconv        | 6 = stable |
| D         | decision | A = accept         | P = prov         | R = reject        |            |
| M         | marker   | * = perfect        | ! = block        | x = prompt-miss   | . = other  |
| MG        | merged   | link selected      | this epoch       |                   |            |
| AFT       | merged   | merged-link        | after score      |                   |            |
| Delta     | merged   | merged-link        | delta            | (after-baseline)  |            |
| B         | merged   | merged-link        | blocking defects |                   |            |
| D         | merged   | merged-link        | total defects    |                   |            |
| EX        | example  | 5A* = ideal        | 4P! = blocked    | 4Px = prompt-miss |            |
+-----------+----------+--------------------+------------------+-------------------+------------+
```

### Unified LSM Table

```text
+--------------+------+------+------+------+------+-----+-----+-----+---+---+
| ROW          | 5>4  | 4>3  | 3>2  | 2>1  | 1>0  | MG  | AFT | Dlt | B | D |
+--------------+------+------+------+------+------+-----+-----+-----+---+---+
| E01          | 3P!  | 3P!  | 3P!  | 4P!  | 4Px  | 5>4 | 88  | +14 | 1 | 2 |
| E02          | ...  | 4P!  | 3P!  | 5P*  | 4P!  | 4>3 | 88  | +26 | 1 | 1 |
| E03          | ...  | ...  | 5P!  | 4P!  | 3P!  | 3>2 | 92  | +24 | 1 | 1 |
| E04          | ...  | ...  | ...  | 4P!  | 5P.  | 2>1 | 91  | +19 | 1 | 1 |
| E05          | ...  | ...  | ...  | ...  | 3P!  | 1>0 | 96  | +34 | 1 | 1 |
| E06          | 5P!  | 5A*  | 5A*  | 5P*  | 6A*  | 5>4 | 91  | +19 | 1 | 3 |
| E07          | ...  | 5P!  | 3R!  | 5P!  | 5P!  | 4>3 | 91  | +19 | 1 | 1 |
| E08          | ...  | ...  | 3P!  | 3P!  | 4P!  | 3>2 | 91  | +17 | 1 | 1 |
| E09          | ...  | ...  | ...  | 5P!  | 3P!  | 2>1 | 93  | +22 | 1 | 1 |
| E10          | ...  | ...  | ...  | ...  | 3P!  | 1>0 | 96  | +24 | 1 | 1 |
| E11          | 5P.  | 5P.  | 4P!  | 5P.  | 5A*  | 5>4 | 96  | +14 | 0 | 2 |
| E12          | ...  | 5P.  | 4P!  | 5P!  | 3P!  | 4>3 | 93  | +19 | 0 | 1 |
| E13          | ...  | ...  | 5P!  | 4P!  | 5P!  | 3>2 | 92  | +18 | 1 | 2 |
| E14          | ...  | ...  | ...  | 3P.  | 5A*  | 2>1 | 89  | +17 | 0 | 2 |
| E15          | ...  | ...  | ...  | ...  | 5P!  | 1>0 | 96  | +25 | 1 | 1 |
| E16          | 5A*  | 4P.  | 5P.  | 4P!  | 6A*  | 5>4 | 100 | +14 | 0 | 0 |
| E17          | ...  | 3P!  | 4P!  | 3P!  | 5A*  | 4>3 | 94  | +22 | 1 | 1 |
| E18          | ...  | ...  | 4P!  | 5P!  | 3P!  | 3>2 | 84  | +12 | 1 | 2 |
| E19          | ...  | ...  | ...  | 4P!  | 4Px  | 2>1 | 90  | +17 | 1 | 1 |
| AVG_AFTER    | 93.8 | 93.2 | 90.6 | 91.9 | 96.0 | -   | -   | -   | - | - |
| PERFECT_CNT  | 1    | 1    | 1    | 2    | 5    | -   | -   | -   | - | - |
| BLK_EPOCHS   | 2    | 4    | 10   | 12   | 13   | -   | -   | -   | - | - |
| PROMPT_NO    | 0    | 0    | 0    | 0    | 2    | -   | -   | -   | - | - |
| SEEN         | 4    | 8    | 12   | 16   | 19   | -   | -   | -   | - | - |
+--------------+------+------+------+------+------+-----+-----+-----+---+---+
```

## Terminology

- `rubric-driven development`: prompt-driven iterative development governed by auditable rubrics.
- `Rubric_0..Rubric_N`: hierarchy where `Rubric_0` scores project artifacts and each higher rubric scores the one below it.
- `stability`: full-chain perfect reconvergence after required destabilization and explicit prompt satisfaction.

## Requirements

- `bash`
- `python3`
- `codex` in `PATH`
