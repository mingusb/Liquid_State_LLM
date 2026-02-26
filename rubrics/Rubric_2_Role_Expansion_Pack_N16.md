# Rubric_2 Role Expansion Pack (N=16)

- generated_utc: 2026-02-24T21:30:00Z
- objective: Role-specific meta-meta criteria for evaluating `Rubric_1` quality.
- scope: `Rubric_2` evaluates `Rubric_1` only.
- scored_collateral_source: `collateral/Rubric_1/manifest_iteration_XXX.md`

## Role Expansion Index

| Role ID | Role | Rubric_2 focus when scoring Rubric_1 |
| --- | --- | --- |
| R0 | Executive Sponsor / Business Owner | Decision safety, authority integrity, and non-gamable governance outcomes |
| R1 | Product Manager | Prioritization utility, decision discriminability, and planning actionability |
| R2 | Product Architect / Enterprise Architect | Structural coherence, boundary clarity, and architecture-risk integration |
| R3 | Engineering Manager | Role accountability, handoff operability, and execution consistency |
| R4 | Software Engineer | Falsifiability, technical precision, and enforceable scoring logic |
| R5 | QA / Test Engineer | Testability, mutation resistance, and adversarial verification depth |
| R6 | SRE / Platform Engineer | Replay stability, observability sufficiency, and environment reproducibility |
| R7 | Security Engineer / Security Architect | Attack realism, evidence integrity, and exploit-resistance controls |
| R8 | Privacy / Compliance / Legal | Regulatory enforceability, lawful handling, and audit sufficiency |
| R9 | Data / AI Engineer or Scientist | Data validity, drift control, and bias/fairness challenge rigor |
| R10 | UX Researcher / Designer | User-impact realism, readability, and perceptual quality discriminators |
| R11 | Technical Writer / DocOps / PDF Owner | Traceable communication quality and publication-grade evidence linkage |
| R12 | DevOps / Release Manager | Change governance, snapshot integrity, and release-readiness consistency |
| R13 | Operations / Support / Customer Success | Runbook/actionability quality and incident-closure practicality |
| R14 | FinOps / Procurement / Vendor Management | Cost-of-assurance realism without control dilution |
| R15 | Internal Audit / Assurance | Independent replayability, contradiction adjudication quality, and anti-gaming assurance |

## Cross-Role Minimum Sub-Dimensions

Every role row above must, at minimum, score these sub-dimensions while evaluating `Rubric_1`:

1. `Coverage Sufficiency`: Does `Rubric_1` cover the role's critical failure modes without blind spots?
2. `Discriminative Anchors`: Are anchor levels behaviorally distinct and resistant to narrative inflation?
3. `Evidence Admissibility`: Can all non-zero claims be replayed from admissible collateral?
4. `Anti-Gaming Strength`: Does `Rubric_1` include executable checks for likely manipulation patterns?
5. `Delta Efficacy`: Do `Rubric_1` changes measurably improve `Rubric_0` decisions and outcomes?
6. `Contradiction Closure`: Are cross-role conflicts resolved with explicit owners, rationale, and proof?

## Scored-Collateral Access Requirements

For each role evaluation in `Rubric_2`:

1. Pull target collateral paths from `collateral/Rubric_1/manifest_iteration_XXX.md`.
2. Record consumed collateral in `collateral/Rubric_2/access_log_iteration_XXX.md` with:
   - path,
   - purpose,
   - used_by_cells.
3. Reject any non-zero score where `collateral_refs` do not resolve to manifest entries.
4. Require `target_collateral_coverage_percent = 100` before issuing pass.

## Required Deliverables For This Pack

- `rubrics/Rubric_2_Role_Expansion_Pack_N16.md`
- `collateral/Rubric_2/manifest_iteration_XXX.md`
- `collateral/Rubric_2/access_log_iteration_XXX.md`
- `rubrics/Rubric_2/iteration_XXX.json`
- `scorecards/Rubric_2_grid_iteration_XXX.md`
