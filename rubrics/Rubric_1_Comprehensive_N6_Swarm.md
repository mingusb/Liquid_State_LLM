# Rubric_1 Comprehensive Meta-Rubric (N=6 Swarm, Role Model N=16)

- generated_utc: 2026-02-24T00:49:58Z
- target_scored: `rubrics/Rubric_0_Comprehensive_N6_Swarm.md`
- target_role_pack_scored: `rubrics/Rubric_0_Role_Expansion_Pack_N16.md`
- authority_chain: `Rubric_1 -> Rubric_0 -> Project Artifact`
- role_model: Reuses the same 16-role model as Rubric_0.

## Purpose

Rubric_1 scores the quality of Rubric_0: coverage completeness, anchor discriminability, evidence replayability, contradiction handling, anti-gaming strength, and operational adjudication fitness.

## Scope Boundary

1. Rubric_1 does not score the project artifact directly.
2. Rubric_1 scores Rubric_0 design and operation quality only.
3. Rubric_1 evidence must be reproducible from Rubric_0 artifacts and logs.

## Scored Collateral Contract (Mandatory)

Rubric_1 scoring is valid only when every non-zero role/cell claim is backed by
manifest-resolved collateral with replayable access logs.

### Canonical collateral topology for Rubric_1

| Collateral class | Required artifacts |
| --- | --- |
| Rubric_0 definitions | `rubrics/Rubric_0_Comprehensive_N6_Swarm.md`, `rubrics/Rubric_0_Role_Expansion_Pack_N16.md` |
| Rubric_1 scored outputs | `rubrics/Rubric_1/iteration_XXX.json`, `scorecards/Rubric_1_grid_iteration_XXX.md` |
| Iteration evidence trail | `evidence/iteration_XXX.md`, `deltas/iteration_XXX.md`, `contradictions/iteration_XXX.md` |
| Rubric_1 collateral logs | `collateral/Rubric_1/manifest_iteration_XXX.md`, `collateral/Rubric_1/access_log_iteration_XXX.md` |
| Judge traces | `iterations/iteration_XXX/judge_baseline/*`, `iterations/iteration_XXX/judge_recheck/*` |

### Enforcement rules

1. Every non-zero score must include `collateral_refs` that resolve to entries in `collateral/Rubric_1/manifest_iteration_XXX.md`.
2. Every consumed collateral item must appear in `collateral/Rubric_1/access_log_iteration_XXX.md` with `path`, `purpose`, and `used_by_cells`.
3. `target_collateral_coverage_percent` must equal `100` for any PASS decision.
4. Missing required collateral classes or unresolved manifest/access-log references force FAIL.
5. Publication is blocked when collateral replay cannot reproduce role/cell claims.

## Role Model (Same Roles As Rubric_0)

| Role ID | Role | Rubric_1 Expansion File |
| --- | --- | --- |
| R0 | Executive Sponsor / Business Owner | `swarm_outputs/meta_rubric_role_expansions/R0_executive_sponsor_business_owner_rubric1.md` |
| R1 | Product Manager | `swarm_outputs/meta_rubric_role_expansions/R1_product_manager_rubric1.md` |
| R2 | Product Architect / Enterprise Architect | `swarm_outputs/meta_rubric_role_expansions/R2_product_architect_enterprise_architect_rubric1.md` |
| R3 | Engineering Manager | `swarm_outputs/meta_rubric_role_expansions/R3_engineering_manager_rubric1.md` |
| R4 | Software Engineer | `swarm_outputs/meta_rubric_role_expansions/R4_software_engineer_rubric1.md` |
| R5 | QA / Test Engineer | `swarm_outputs/meta_rubric_role_expansions/R5_qa_test_engineer_rubric1.md` |
| R6 | SRE / Platform Engineer | `swarm_outputs/meta_rubric_role_expansions/R6_sre_platform_engineer_rubric1.md` |
| R7 | Security Engineer / Security Architect | `swarm_outputs/meta_rubric_role_expansions/R7_security_engineer_security_architect_rubric1.md` |
| R8 | Privacy / Compliance / Legal | `swarm_outputs/meta_rubric_role_expansions/R8_privacy_compliance_legal_rubric1.md` |
| R9 | Data / AI Engineer or Scientist | `swarm_outputs/meta_rubric_role_expansions/R9_data_ai_engineer_scientist_rubric1.md` |
| R10 | UX Researcher / Designer | `swarm_outputs/meta_rubric_role_expansions/R10_ux_researcher_designer_rubric1.md` |
| R11 | Technical Writer / DocOps / PDF Owner | `swarm_outputs/meta_rubric_role_expansions/R11_technical_writer_docops_pdf_owner_rubric1.md` |
| R12 | DevOps / Release Manager | `swarm_outputs/meta_rubric_role_expansions/R12_devops_release_manager_rubric1.md` |
| R13 | Operations / Support / Customer Success | `swarm_outputs/meta_rubric_role_expansions/R13_operations_support_customer_success_rubric1.md` |
| R14 | FinOps / Procurement / Vendor Management | `swarm_outputs/meta_rubric_role_expansions/R14_finops_procurement_vendor_management_rubric1.md` |
| R15 | Internal Audit / Assurance | `swarm_outputs/meta_rubric_role_expansions/R15_internal_audit_assurance_rubric1.md` |


## Rubric_1 Scoring Contract

1. Every role dimension R0..R15 must be scored using explicit `0/25/50/75/90/100` anchors.
2. No non-zero score without `who/what/where` evidence tied to Rubric_0 artifacts.
3. Any unresolved contradiction between role judgments caps affected role scores at `50` until resolved.
4. Any detected score inflation or fabricated evidence triggers hard fail for affected role(s).
5. Rubric_1 `PERFECT PASS` requires all role dimensions at `100` with independent replayable evidence.
6. Every non-zero role/cell score also requires manifest-resolved `collateral_refs`.
7. PASS requires `target_collateral_coverage_percent=100` and replayable access logs.

## Rubric_1 Aggregation And Decision Bands

1. Role meta-score (for each role) = mean of that role's scored sub-dimensions.
2. Rubric_1 aggregate score = mean of role meta-scores across R0..R15 (equal weights unless pre-approved governance override).
3. Apply anti-gaming gates `M1..M6` before assigning a decision band.
4. Any active overall-fail gate (`M3` or `M4`) forces `FAIL` regardless of aggregate score.
5. Decision bands:

| Aggregate Score | Decision | Required Action |
| ---: | --- | --- |
| 0-59 | FAIL | block Rubric_0 certification; full remediation plan |
| 60-74 | CONDITIONAL FAIL | limited pilot scoring only with explicit waiver |
| 75-84 | CONDITIONAL PASS | constrained use with dated corrective actions |
| 85-94 | PASS | approved for normal meta-governance use |
| 95-99 | HIGH-ASSURANCE PASS | approved with benchmark-quality assurance |
| 100 | PERFECT PASS | all roles at 100 with independent replayable evidence |

## Rubric_1 Anti-Gaming Gates

| Gate ID | Condition | Effect |
| --- | --- | --- |
| M1 | Non-zero score without replayable evidence | Set affected cell to 0 |
| M1B | Non-zero score without manifest-resolved collateral reference | Set affected cell to 0 |
| M2 | Anchor claims not discriminable across 0/25/50/75/90/100 | Cap dimension at 50 |
| M3 | Contradictions unresolved across adjacent role decisions | Overall FAIL |
| M4 | Retroactive rubric edits after freeze without change log | Overall FAIL |
| M5 | Judge-role conflict of interest without independent review | Cap affected role at 75 |
| M6 | Cosmetic/narrative quality used in place of measurable controls | Cap affected cell at 25 |
| M7 | Collateral manifest/access-log coverage below 100% | Overall FAIL |
| M8 | Missing required collateral classes in iteration package | Overall FAIL |

## Required Outputs For Rubric_1

- `rubrics/Rubric_1_Comprehensive_N6_Swarm.md`
- `rubrics/Rubric_1_Role_Expansion_Pack_N16.md`
- `rubrics/Rubric_1/iteration_XXX.json`
- `scorecards/Rubric_1_grid_iteration_XXX.md`
- `evidence/iteration_XXX.md`
- `deltas/iteration_XXX.md`
- `contradictions/iteration_XXX.md`
- `collateral/Rubric_1/manifest_iteration_XXX.md`
- `collateral/Rubric_1/access_log_iteration_XXX.md`
- `swarm_outputs/meta_rubric_role_expansions/R0_executive_sponsor_business_owner_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R1_product_manager_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R2_product_architect_enterprise_architect_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R3_engineering_manager_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R4_software_engineer_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R5_qa_test_engineer_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R6_sre_platform_engineer_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R7_security_engineer_security_architect_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R8_privacy_compliance_legal_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R9_data_ai_engineer_scientist_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R10_ux_researcher_designer_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R11_technical_writer_docops_pdf_owner_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R12_devops_release_manager_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R13_operations_support_customer_success_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R14_finops_procurement_vendor_management_rubric1.md`
- `swarm_outputs/meta_rubric_role_expansions/R15_internal_audit_assurance_rubric1.md`

## Role Expansion Pack

- `rubrics/Rubric_1_Role_Expansion_Pack_N16.md`

## Rubric_2 Compatibility Addendum (Mandatory for `Rubric_2 -> Rubric_1`)

This addendum defines explicit interoperability guarantees so `Rubric_2` can score
`Rubric_1` without interpretation drift.

### Compatibility requirements

1. `PERFECT PASS` requires all role dimensions at `100` and independent replay by
   non-author judges (the recheck judge authority must not be baseline author
   authority for the same scope).
2. Improvement claims are invalid without before/after defect evidence:
   - baseline prioritized defects,
   - author burndown closure check,
   - independent recheck prioritized defects,
   - role/mean score deltas,
   - final decision record.
3. Iteration protocol is strict and ordered:
   - snapshot all rubric layers in scope,
   - freeze collateral manifest and access log,
   - baseline judge pass,
   - author remediation,
   - independent adversarial recheck,
   - final accept/reject decision.
4. After snapshot freeze, any rubric or collateral edit requires explicit reopen
   record and impact replay before publication.

### Additional required outputs for Rubric_1 governance iterations

- `iterations/iteration_XXX/SNAPSHOT.md`
- `iterations/iteration_XXX/judge_baseline/PRIORITIZED_DEFECTS.md`
- `iterations/iteration_XXX/author_deltas/DEFECT_BURNDOWN_CHECK.md`
- `iterations/iteration_XXX/judge_recheck/PRIORITIZED_DEFECTS.md`
- `iterations/iteration_XXX/SCORE_DELTA.md`
- `iterations/iteration_XXX/judge_recheck/FINAL_DECISION.md`
