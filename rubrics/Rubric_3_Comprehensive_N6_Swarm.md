# Rubric_3 Comprehensive Meta-Meta-Meta Rubric (N=6 Swarm, Role Model N=16)

- generated_utc: 2026-02-24T05:40:00Z
- target_scored: `rubrics/Rubric_2_Comprehensive_N6_Swarm.md`
- target_role_pack_scored: `rubrics/Rubric_2_Role_Expansion_Pack_N16.md`
- authority_chain: `Rubric_3 -> Rubric_2 -> Rubric_1 -> Rubric_0 -> Project Artifact`
- scoring_mode: `Rubric_3 scores Rubric_2 governance quality and meta-judging rigor only`

## Purpose

`Rubric_3` evaluates whether `Rubric_2` can reliably improve `Rubric_1` without narrative inflation, authority conflict, or replay drift. `Rubric_3` does not score project artifacts directly; it scores the quality of the rubric that scores the rubric.

## Scope Boundary

1. `Rubric_3` never assigns direct product/document quality scores.
2. `Rubric_3` scores only `Rubric_2` design, operational behavior, anti-gaming execution, and adjudication integrity.
3. `Rubric_3` scores must be replayable from `Rubric_2` collateral and iteration records.

## Scored Collateral Contract (Mandatory)

For every `Rubric_3 -> Rubric_2` iteration, scoring must consume and cite:

| Collateral class | Required examples |
| --- | --- |
| Rubric_2 definition collateral | `rubrics/Rubric_2_Comprehensive_N6_Swarm.md`, `rubrics/Rubric_2_Role_Expansion_Pack_N16.md` |
| Rubric_2 iteration outputs | `iterations/iteration_XXX/judge_baseline/*`, `iterations/iteration_XXX/judge_recheck/*`, `iterations/iteration_XXX/SCORE_DELTA.md`, `iterations/iteration_XXX/STATUS.md` |
| Rubric_2 collateral logs | `collateral/Rubric_2/manifest_iteration_XXX.md`, `collateral/Rubric_2/access_log_iteration_XXX.md` |
| Protocol authority | `AGENTS.md`, `iterations/iteration_XXX/SNAPSHOT.md` |

A `Rubric_3` non-zero score is invalid when collateral refs cannot be replayed to manifest entries.

## Rubric_3 Dimension Framework (Top-Level)

| Section | Focus |
| --- | --- |
| C1 | Meta-authority integrity and scope purity |
| C2 | Rubric_2 discriminability and anchor discipline |
| C3 | Rubric_2 anti-gaming execution fidelity |
| C4 | Evidence-chain replayability and contradiction closure |
| C5 | Delta efficacy from Rubric_2 into Rubric_1 quality |
| C6 | Independent adjudication robustness and operational sustainability |

## Scoring Contract

1. Anchors are strict `0/25/50/75/90/100`.
2. No non-zero score without explicit `who/what/where` evidence and `collateral_refs`.
3. Any authority-chain contradiction unresolved at iteration close causes overall FAIL.
4. `PERFECT PASS` requires all role cells at `100`, zero defects, and independent recheck.

## Anti-Gaming Gates

| Gate ID | Condition | Effect |
| --- | --- | --- |
| M3-1 | Non-zero score with missing replayable collateral | Set affected cell to `0` |
| M3-2 | Claimed Rubric_2 improvement without baseline/recheck delta evidence | Cap C5 to `50` |
| M3-3 | Recheck executed by same authority as author | Overall FAIL |
| M3-4 | Snapshot/freeze/reopen protocol missing or violated | Overall FAIL |
| M3-5 | Chain mismatch between expected and executed evaluation chain | Overall FAIL |

## Iteration Protocol

1. Snapshot `Rubric_0..Rubric_3`.
2. Freeze target collateral manifests for `Rubric_2`.
3. Execute baseline `Rubric_3 -> Rubric_2` scoring and emit ordered defects.
4. Improve `Rubric_2` if defects exist.
5. Run independent recheck with adversarial spot checks.
6. Accept only with `decision=ACCEPT`, `recheck_mean=100.0`, `recheck_total_defects=0`, and `recheck_blocking_defects=0`.

## Decision Rule

`Rubric_2` is accepted as governing authority for `Rubric_1` only when `Rubric_3` issues a full `100%` pass with replayable evidence and all anti-gaming gates satisfied.
