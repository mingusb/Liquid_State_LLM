![Liquid State LLM Harness](docs/images/lsllm-harness-hero.png)

# Liquid State Large Language Model Harness

A Liquid State Machine on the Edge of Chaos is a neural computation model that dynamically balances order and variability, enabling flexible, adaptive learning. This harness enables self-improvement for large language models and has been tested on OpenAI Codex 5.3 (`low`/`xhigh`) and Codex Spark. It uses hierarchical rubrics, where each rubric is evaluated by a higher-level meta-rubric, creating a multi-layered scoring system. Rubric dimensions align with `N` company roles, with each role contributing specific dimensions at each layer. Judges score the rubrics, and the rubric chain is regularly destabilized and redeveloped. Prompts such as `AGENTS.md` guide the LLM to function as a Liquid State Machine on the Edge of Chaos, which may enhance generalization and support extrageneralization (Maass, 2000). The harness is self-improving and has evolved through this process. It currently requires a Pro-tier GPT subscription ($200/month) and is not yet highly efficient or effective. Its main advantages are ease of use and ongoing development. Sub-agent swarms are frequently deployed to identify and resolve bugs, though formal tests are not yet implemented.

## Default Workflow

Follow this primary operator workflow:

```bash
# Launch an autonomous rubric evaluation chain.
# The depth parameter specifies how many rubric layers are included.
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

# 2) Resolve the latest run directory
RUN_DIR="$(ls -td runs/* 2>/dev/null | head -n 1)"

# 3) Inspect stability state and next required chain
sed -n '1,260p' "$RUN_DIR/STABILITY_STATUS.md"

# 4) Inspect the latest recheck decision
LATEST_ITER="$(ls -td "$RUN_DIR"/iterations/iteration_* 2>/dev/null | head -n 1)"
sed -n '1,260p' "$LATEST_ITER/judge_recheck/FINAL_DECISION.md"
```

## Stability Model (Chaos To Recovery)

Stability is not achieved immediately. For each depth `N`, all adjacency chains must reconverge. Operating on the edge of chaos is designed to maximize generalization while maintaining accuracy, so that convergence through this stability model not only signals system robustness but also promotes faster adaptation and more reliable outcomes in practical deployments.

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

Each run in `runs/<run_name>/` should include the following files:

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

If the process continues to improve but has not converged, increase the iteration budget:

```bash
./rdd --prompt prompt.txt --depth 5 --max-autonomous-iterations 40
```

### Missing collateral or evidence linkage

```bash
RUN_DIR="$(ls -td runs/* 2>/dev/null | head -n 1)"
python3 scripts/validate_rubric_excellence.py --run-dir "$RUN_DIR"
```

Check for:

- `collateral/Rubric_<k>/manifest_iteration_XXX.md`
- `collateral/Rubric_<k>/access_log_iteration_XXX.md`

### `stable: false` after many iterations

Typical causes:

- one or more chains still have recheck blockers/defects
- `prompt_satisfaction` is not explicitly `yes`
- destabilization/recovery accounting not yet satisfied for one or more chains

Primary diagnostics:

- `STABILITY_STATUS.md`
- `STABILITY_STATUS.json`
- latest `iterations/iteration_XXX/judge_recheck/FINAL_DECISION.md`

## Terminology

- Rubric-driven development: prompt-driven iterative development governed by auditable rubrics.
- `Rubric_0..Rubric_N`: hierarchy where `Rubric_0` scores project artifacts and each higher rubric scores the one below it.
- stability: full-chain perfect reconvergence after required destabilization with explicit prompt satisfaction.

## Requirements

- `bash`
- `python3`
- `codex` in `PATH`

## Dashboard (Latest Snapshot)

Rendered from `scorecards/LSM_DASHBOARD.md`.

```text
# LSM Dashboard (Narrow)

- run: `depth5_codex_low_restart_20260226T015701Z`
- epochs: `19`
- final_phase: `reservoir_perturbation`
- stable: `no`

Legend (fixed-width):
+-----------+----------+--------------------+------------------+-------------------+------------+
| TOKEN     | KIND     | D1                 | D2               | D3                | D4         |
+-----------+----------+--------------------+------------------+-------------------+------------+
| [S][D][M] | cell     | chain code triplet |                  |                   |            |
| S         | phase    | 3 = edge           | 4 = train        | 5 = reconv        | 6 = stable |
| D         | decision | A = accept         | P = prov         | R = reject        |            |
| M         | marker   | * = perfect        | ! = block        | x = prompt-miss   | . = other  |
| MG        | merged   | link selected      | this epoch       |                   |            |
| AFT       | merged   | merged-link        | after score      |                   |            |
| Δ         | merged   | merged-link        | delta            | (after-baseline)  |            |
| B         | merged   | merged-link        | blocking defects |                   |            |
| D         | merged   | merged-link        | total defects    |                   |            |
| EX        | example  | 5A* = ideal        | 4P! = blocked    | 4Px = prompt-miss |            |
+-----------+----------+--------------------+------------------+-------------------+------------+

## Unified LSM Table

+--------------+------+------+------+------+------+-----+-----+-----+---+---+
| ROW          | 5>4  | 4>3  | 3>2  | 2>1  | 1>0  | MG  | AFT | Δ   | B | D |
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
| Σ_AVG_AFTER  | 93.8 | 93.2 | 90.6 | 91.9 | 96.0 | -   | -   | -   | - | - |
| Σ_PERFECT    | 1    | 1    | 1    | 2    | 5    | -   | -   | -   | - | - |
| Σ_BLK_EPOCHS | 2    | 4    | 10   | 12   | 13   | -   | -   | -   | - | - |
| Σ_PROMPT_NO  | 0    | 0    | 0    | 0    | 2    | -   | -   | -   | - | - |
| Σ_SEEN       | 4    | 8    | 12   | 16   | 19   | -   | -   | -   | - | - |
+--------------+------+------+------+------+------+-----+-----+-----+---+---+
```

## Idealized Perfect Depth-5 Rubric (Pretty Print)

```text
+----------+---------------------+-------------------------+----+----+-------+--------+------+
| Rubric   | Scores              | Target                  | X  | Y  | Cells | Mean   | Gate |
+----------+---------------------+-------------------------+----+----+-------+--------+------+
| Rubric_5 | Rubric_4            | Meta-meta-meta control  | 16 | 10 | 160   | 100.0% | PASS |
| Rubric_4 | Rubric_3            | Meta-meta control       | 16 | 12 | 192   | 100.0% | PASS |
| Rubric_3 | Rubric_2            | Meta control            | 16 | 16 | 256   | 100.0% | PASS |
| Rubric_2 | Rubric_1            | Rubric-quality control  | 16 | 18 | 288   | 100.0% | PASS |
| Rubric_1 | Rubric_0            | Rubric adequacy control | 16 | 20 | 320   | 100.0% | PASS |
| Rubric_0 | Project artifact(s) | Prompt objective output | 16 | 24 | 384   | 100.0% | PASS |
+----------+---------------------+-------------------------+----+----+-------+--------+------+

X-axis roles (shared across Rubric_0..Rubric_5):
+-----+--------------------------------------+
| ID  | Role                                 |
+-----+--------------------------------------+
| R0  | Chief Executive Officer              |
| R1  | Chief Operating Officer              |
| R2  | Chief Financial Officer              |
| R3  | Chief Technology Officer             |
| R4  | Chief Product Officer                |
| R5  | Head of Engineering                  |
| R6  | Staff Software Engineer              |
| R7  | Quality Assurance Lead               |
| R8  | Site Reliability Engineer            |
| R9  | Security Engineer                    |
| R10 | Data and Analytics Lead              |
| R11 | UX Research and Design Lead          |
| R12 | Customer Success Lead                |
| R13 | Technical Documentation Lead         |
| R14 | Compliance and Risk Officer          |
| R15 | Independent External Auditor         |
+-----+--------------------------------------+

Perfect-chain hard gate vector:
+---------------------------+---------+
| Criterion                 | Value   |
+---------------------------+---------+
| decision                  | ACCEPT  |
| recheck_mean              | 100.0   |
| recheck_total_defects     | 0       |
| recheck_blocking_defects  | 0       |
| identity_lock             | yes     |
| prompt_satisfaction       | yes     |
| contradictions_open       | 0       |
+---------------------------+---------+

Y-axis dimension families by rubric depth:
+----------+----------------------------------------------------------------------------------+
| Rubric   | Y dimension family set                                                           |
+----------+----------------------------------------------------------------------------------+
| Rubric_0 | Prompt Coverage; Product Utility; Technical Correctness; Reliability; Security; |
|          | Privacy; Accessibility; UX Clarity; IA/Content; Performance; Maintainability;   |
|          | Testability; Auditability; Compliance; Observability; Recovery Quality;          |
|          | Operability; Cost Efficiency; Traceability; Anti-Gaming Resistance;              |
|          | Contradiction Handling; Evidence Quality; Outcome Fit; Longevity                 |
| Rubric_1 | Coverage Adequacy; Dimension Discrimination; Prompt Trace Fidelity; Evidence     |
|          | Sufficiency; Anti-Gaming Strength; Scoring Anchor Precision; Residual Variance   |
|          | Capture; Contradiction Resolution Quality; Cell-level Explainability;            |
|          | Axis Completeness; Axis Independence; Role Balance; Failure Sensitivity;         |
|          | Regression Detection; Measurement Rigor; Audit Reproducibility;                  |
|          | Reliability Under Adversarial Inputs; Prompt Drift Resistance;                   |
|          | Overfit Resistance; Judge Agreement                                               |
| Rubric_2 | Meta-Rubric Specificity; Remediation Guidance Value; Evaluation Consistency;     |
|          | Blindspot Detection; Incentive Alignment; Penalty Calibration; Upgrade Path       |
|          | Clarity; Chain-Coupling Awareness; Stability-Plasticity Balance; Frontier         |
|          | Discovery Strength; Error Taxonomy Quality; Defect Prioritization Quality;        |
|          | Evidence Model Robustness; Novelty Capture; Prompt Morphology Response;           |
|          | Governance Fitness; Recovery Predictiveness; Self-Improvement Utility             |
| Rubric_3 | Meta^3 Calibration Accuracy; Hierarchy Coherence; Emergent Axis Creativity;      |
|          | Meta-overfit Controls; Cross-level Contradiction Detection; Convergence           |
|          | Provability; Dynamical Stability Control; Quality Upper-bound Pressure;           |
|          | Evaluation Coverage Closure; Strategic Residual Capture; Anti-Gaming              |
|          | Escalation Integrity; Role-weight Fairness; Decision Boundary Sharpness;          |
|          | Adaptive Thresholding; Proof-carrying Remediation                                 |
| Rubric_4 | Meta^4 Legibility; Chain Governance Fitness; Failure-mode Isolation;              |
|          | Recursion Soundness; Dependency Invalidation Correctness; Reconvergence           |
|          | Policy Coherence; Goal Alignment Under Drift; Anti-cheating Meta Guards;          |
|          | Audit Trace Compression; Resource-Efficiency Pressure; Judge Independence          |
| Rubric_5 | Meta^5 Objective Integrity; Recursion Purpose Preservation;                       |
|          | System-level Generalization; Catastrophic Shortcut Prevention;                    |
|          | Convergence Ethics and Safety; Meta-policy Continuity; Stability Warranty;        |
|          | Multi-run Transfer Robustness; Strategic Tradeoff Governance;                     |
|          | Final Adjudication Soundness                                                      |
+----------+----------------------------------------------------------------------------------+
```
