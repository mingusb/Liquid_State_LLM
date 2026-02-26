# Rubric_2 Comprehensive Meta-Meta Rubric (N=6 Swarm, Role Model N=16)

- generated_utc: 2026-02-24T21:30:00Z
- target_scored: `rubrics/Rubric_1_Comprehensive_N6_Swarm.md`
- target_role_pack_scored: `rubrics/Rubric_1_Role_Expansion_Pack_N16.md`
- authority_chain: `Rubric_2 -> Rubric_1 -> Rubric_0 -> Project Artifact`
- scoring_mode: `Rubric_2 scores Rubric_1 quality and governance behavior only`

## Purpose

`Rubric_2` evaluates whether `Rubric_1` is strong enough to improve `Rubric_0` without gaming, ambiguity, or governance drift. The target is not the product artifact directly; the target is the quality of the rubric that governs the artifact rubric.

## Scope Boundary

1. `Rubric_2` does not score project artifact quality directly.
2. `Rubric_2` scores `Rubric_1` design, operationalization, anti-gaming rigor, and delta effectiveness.
3. `Rubric_2` evidence must be replayable from `Rubric_1` collateral, not narrative summaries alone.

## Scored Collateral Contract (Mandatory)

`Rubric_2` must have direct access to `Rubric_1` collateral that it scores. At minimum, each `Rubric_2` iteration must consume and cite:

| Collateral class | Required examples |
| --- | --- |
| Rubric definition collateral | `rubrics/Rubric_1_Comprehensive_N6_Swarm.md`, `rubrics/Rubric_1_Role_Expansion_Pack_N16.md` |
| Rubric_1 score outputs | `rubrics/Rubric_1/iteration_XXX.json`, `scorecards/Rubric_1_grid_iteration_XXX.md` |
| Rubric_1 evidence trail | `evidence/iteration_XXX.md`, `deltas/iteration_XXX.md`, `contradictions/iteration_XXX.md` |
| Rubric_1 judging collateral | `iterations/iteration_XXX/judge_baseline/*`, `iterations/iteration_XXX/judge_recheck/*` |
| Rubric_1 collateral logs | `collateral/Rubric_1/manifest_iteration_XXX.md`, `collateral/Rubric_1/access_log_iteration_XXX.md` |

A `Rubric_2` score is invalid when:

- non-zero cells do not cite collateral paths from the `Rubric_1` manifest,
- collateral coverage is below 100%,
- or access logs cannot be replayed from recorded files.

## Rubric_2 Dimension Framework (Top-Level)

| Section | Focus |
| --- | --- |
| B1 | Meta-governance integrity and authority safety |
| B2 | Rubric_1 discriminative power and falsifiability |
| B3 | Rubric_1 anti-gaming depth and attack resistance |
| B4 | Evidence-chain replayability and contradiction closure |
| B5 | Delta quality: whether Rubric_1 actually improves Rubric_0 outcomes |
| B6 | Operational sustainability across iterations and roles |

## Role Model (Same 16-role model)

| Role ID | Role concern inside Rubric_2 |
| --- | --- |
| R0 | Executive governance safety and decision integrity |
| R1 | Product-governance actionability and prioritization utility |
| R2 | Architecture coherence and control topology soundness |
| R3 | Delivery-organization operability and ownership clarity |
| R4 | Engineering falsifiability and implementation precision |
| R5 | Verification depth, mutation resistance, and regression confidence |
| R6 | Runtime resilience, observability, and platform reproducibility |
| R7 | Threat realism, exploit resistance, and integrity hardening |
| R8 | Privacy/legal compliance enforceability and evidence sufficiency |
| R9 | Data and model validity, drift controls, and fairness defenses |
| R10 | UX/document quality realism and perceptual trust signals |
| R11 | Documentation traceability, readability, and publication correctness |
| R12 | Release/change governance and environment-parity controls |
| R13 | Operability/customer impact and incident response readiness |
| R14 | Cost-of-assurance realism and vendor/control reliability |
| R15 | Independent assurance quality and non-conflicted adjudication |

## Rubric_2 Scoring Contract

1. Anchors are strict `0/25/50/75/90/100`.
2. No non-zero score without explicit `who/what/where` evidence and collateral citation.
3. Every scored cell must include `collateral_refs` mapping to `target_collateral_manifest`.
4. `target_collateral_coverage_percent` must be `100` for pass.
5. Any unresolved contradiction about `Rubric_1` interpretation caps affected dimensions at `50`.
6. Perfect pass requires every cell at `100` and independent replay by non-author judges.

## Anti-Gaming Gates

| Gate ID | Condition | Effect |
| --- | --- | --- |
| M2-1 | Non-zero score with no collateral-backed evidence | Set affected cell to `0` |
| M2-2 | `Rubric_1` claims improvement without before/after defect burn-down proof | Cap B5 to `50` |
| M2-3 | `Rubric_1` anti-gaming checks are descriptive but non-executable | Cap B3 to `25` |
| M2-4 | Contradictions in `Rubric_1` remain unresolved at iteration close | Overall FAIL |
| M2-5 | Retroactive edits in Rubric_1 after snapshot without reopen | Overall FAIL |
| M2-6 | Judge independence conflict in Rubric_2 adjudication | Cap affected role at `75` |

## Iteration Protocol

1. Snapshot `Rubric_0`, `Rubric_1`, and `Rubric_2`.
2. Freeze `Rubric_1` collateral manifest for the iteration.
3. Execute baseline `Rubric_2 -> Rubric_1` scoring and publish ordered defects.
4. Improve `Rubric_1` to close those defects.
5. Independently re-score `Rubric_1` with adversarial checks.
6. Accept iteration only when all gates pass and `Rubric_2` issues `100%` across cells.

## Required Outputs For Rubric_2

- `rubrics/Rubric_2_Comprehensive_N6_Swarm.md`
- `rubrics/Rubric_2_Role_Expansion_Pack_N16.md`
- `collateral/Rubric_2/manifest_iteration_XXX.md`
- `collateral/Rubric_2/access_log_iteration_XXX.md`
- `rubrics/Rubric_2/iteration_XXX.json`
- `scorecards/Rubric_2_grid_iteration_XXX.md`

## Decision Rule

`Rubric_1` is accepted for governing `Rubric_0` only when `Rubric_2` assigns a full `100%` pass with replayable collateral-backed evidence.
