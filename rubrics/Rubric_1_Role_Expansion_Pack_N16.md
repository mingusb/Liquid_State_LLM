# Rubric_1 Role Expansion Pack (N=16)

- generated_utc: 2026-02-24T00:49:58Z
- objective: Role-specific meta-rubrics for scoring Rubric_0 quality and anti-gaming rigor.
- scope: Rubric_1 evaluates Rubric_0 only.
- source_dir: `swarm_outputs/meta_rubric_role_expansions/`

## Index

| Role ID | Role | File | Words | Lines |
| --- | --- | --- | ---: | ---: |
| R0 | Executive Sponsor / Business Owner | `swarm_outputs/meta_rubric_role_expansions/R0_executive_sponsor_business_owner_rubric1.md` | 3760 | 138 |
| R1 | Product Manager | `swarm_outputs/meta_rubric_role_expansions/R1_product_manager_rubric1.md` | 3699 | 130 |
| R2 | Product Architect / Enterprise Architect | `swarm_outputs/meta_rubric_role_expansions/R2_product_architect_enterprise_architect_rubric1.md` | 3758 | 139 |
| R3 | Engineering Manager | `swarm_outputs/meta_rubric_role_expansions/R3_engineering_manager_rubric1.md` | 3970 | 143 |
| R4 | Software Engineer | `swarm_outputs/meta_rubric_role_expansions/R4_software_engineer_rubric1.md` | 4502 | 143 |
| R5 | QA / Test Engineer | `swarm_outputs/meta_rubric_role_expansions/R5_qa_test_engineer_rubric1.md` | 4530 | 145 |
| R6 | SRE / Platform Engineer | `swarm_outputs/meta_rubric_role_expansions/R6_sre_platform_engineer_rubric1.md` | 4507 | 151 |
| R7 | Security Engineer / Security Architect | `swarm_outputs/meta_rubric_role_expansions/R7_security_engineer_security_architect_rubric1.md` | 4128 | 139 |
| R8 | Privacy / Compliance / Legal | `swarm_outputs/meta_rubric_role_expansions/R8_privacy_compliance_legal_rubric1.md` | 4769 | 152 |
| R9 | Data / AI Engineer or Scientist | `swarm_outputs/meta_rubric_role_expansions/R9_data_ai_engineer_scientist_rubric1.md` | 4844 | 165 |
| R10 | UX Researcher / Designer | `swarm_outputs/meta_rubric_role_expansions/R10_ux_researcher_designer_rubric1.md` | 4748 | 154 |
| R11 | Technical Writer / DocOps / PDF Owner | `swarm_outputs/meta_rubric_role_expansions/R11_technical_writer_docops_pdf_owner_rubric1.md` | 5001 | 162 |
| R12 | DevOps / Release Manager | `swarm_outputs/meta_rubric_role_expansions/R12_devops_release_manager_rubric1.md` | 4763 | 157 |
| R13 | Operations / Support / Customer Success | `swarm_outputs/meta_rubric_role_expansions/R13_operations_support_customer_success_rubric1.md` | 4797 | 164 |
| R14 | FinOps / Procurement / Vendor Management | `swarm_outputs/meta_rubric_role_expansions/R14_finops_procurement_vendor_management_rubric1.md` | 5089 | 166 |
| R15 | Internal Audit / Assurance | `swarm_outputs/meta_rubric_role_expansions/R15_internal_audit_assurance_rubric1.md` | 4908 | 163 |


---

## Cross-Role Collateral-Chain Enforcement (R0..R15)

This section is authoritative for role-level scoring admissibility. It applies
to every role expansion in this file.

### Mandatory role-level collateral rules

1. No non-zero role/cell score without `who/what/where` evidence and manifest-resolved `collateral_refs`.
2. Every `collateral_ref` must resolve to `collateral/Rubric_1/manifest_iteration_XXX.md`.
3. Every resolved collateral item must be replayable in `collateral/Rubric_1/access_log_iteration_XXX.md` with:
   - `path`
   - `purpose`
   - `used_by_cells`
4. Role PASS is invalid when required collateral classes are missing:
   - `rubrics/Rubric_1/iteration_XXX.json`
   - `scorecards/Rubric_1_grid_iteration_XXX.md`
   - `evidence/iteration_XXX.md`
   - `deltas/iteration_XXX.md`
   - `contradictions/iteration_XXX.md`
   - `collateral/Rubric_1/manifest_iteration_XXX.md`
   - `collateral/Rubric_1/access_log_iteration_XXX.md`
5. `target_collateral_coverage_percent` must be `100` for any role-level PASS.
6. Missing manifest/access-log linkage triggers hard fail for affected role cells.

### Role enforcement matrix

| Role | Non-zero collateral refs required | Access-log replay required | Coverage must be 100% |
| --- | --- | --- | --- |
| R0 | Yes | Yes | Yes |
| R1 | Yes | Yes | Yes |
| R2 | Yes | Yes | Yes |
| R3 | Yes | Yes | Yes |
| R4 | Yes | Yes | Yes |
| R5 | Yes | Yes | Yes |
| R6 | Yes | Yes | Yes |
| R7 | Yes | Yes | Yes |
| R8 | Yes | Yes | Yes |
| R9 | Yes | Yes | Yes |
| R10 | Yes | Yes | Yes |
| R11 | Yes | Yes | Yes |
| R12 | Yes | Yes | Yes |
| R13 | Yes | Yes | Yes |
| R14 | Yes | Yes | Yes |
| R15 | Yes | Yes | Yes |


---

## R0 Executive Sponsor / Business Owner

- source_file: `swarm_outputs/meta_rubric_role_expansions/R0_executive_sponsor_business_owner_rubric1.md`
- words: 3760
- lines: 138

# R0 Executive Sponsor / Business Owner Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

## 1) Role mission and decision rights for evaluating Rubric_0 quality

### Mission
R0 evaluates whether Rubric_0 is decision-safe for capital, risk, and fiduciary governance. The question is not whether a delivery artifact is good; the question is whether Rubric_0 can produce reproducible, auditable, anti-gaming decisions that executives can trust for go/pivot/stop and release authority.

### Scope guardrail
- This meta-rubric scores the quality of Rubric_0 design, scoring mechanics, evidence controls, and adjudication behavior.
- This meta-rubric does not directly score product code, documents, or operational artifacts.

### Decision rights (non-delegable for Rubric_0 quality governance)
1. Approve or reject Rubric_0 for production governance use.
2. Require revisions when Rubric_0 logic is non-replayable, contradictory, or easy to game.
3. Set and approve any weighting overrides to Rubric_0 only through documented governance charter updates.
4. Enforce gate precedence (`G1..G6`, `RG1..RG4`) over weighted arithmetic.
5. Block scores above `75` without independent evidence and above `90` without replay/recomputation proof.
6. Freeze scoring cycles to versioned rubric snapshots; prohibit retroactive score inflation.
7. Commission independent assurance when scoring integrity is disputed.
8. Require contradiction register closure before executive decisions rely on Rubric_0 outputs.
9. Enforce exception expiry and compensating-control validity in rubric operations.
10. Own the close-loop improvement cycle for Rubric_0 and verify delta impact.

### Rubric_1 scoring protocol for this role
- Anchor scale per sub-dimension: `0`, `25`, `50`, `75`, `90`, `100`.
- Default weighting: equal weight across all sub-dimensions unless pre-approved governance override exists before cycle start.
- Any hard-fail tripwire in Section 6 invalidates Rubric_0 scoring for that cycle.
- Non-zero Rubric_1 scores require explicit `who/what/where` evidence.

## 2) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R0-M1 Decision-band actionability | Rubric_0 yields unambiguous decisions and required actions at each score band. | No band overlap in text; 20-case simulation shows evaluator agreement >=90% on decision label and required action; disputed cases resolved with documented rule, not discretion. | Who: R0 governance lead + independent reviewer. What: band simulation sheet, dispute log, final adjudication rules. Where: governance repo and scoring workbook archive. |
| R0-M2 Strategy-to-rubric coverage completeness | Rubric_0 covers executive objectives, domain sections (A1..A6), and role layer (R0..R15) without material blind spots. | 100% board-level objectives map to at least one domain and one role concern; unmapped critical risk count = 0; overlap conflicts explicitly resolved. | Who: R0 + PMO + enterprise architect. What: objective-to-rubric trace matrix, gap analysis, conflict resolution memo. Where: portfolio governance folder and rubric mapping workbook. |
| R0-M3 Weighting and capital-risk proportionality | Rubric_0 weighting and gates reflect downside exposure and fiduciary obligations. | Sensitivity test shows no low-risk dimension can mask critical control failure; chartered weight changes include rationale and impact simulation; gate outcomes dominate weighted averages when triggered. | Who: R0 + finance controller + risk lead. What: weighting charter, sensitivity model, gate override test results. Where: investment committee records and rubric model artifacts. |
| R0-M4 Gate enforceability and precedence clarity | Global and role-layer hard gates are operationally enforceable and non-contradictory. | Truth-table replay confirms `G1..G6` and `RG1..RG4` consistently override arithmetic scoring; any triggered gate yields the documented fail effect in 100% of sampled runs. | Who: R0 governance analyst + internal audit observer. What: gate truth table, replay logs, contradiction findings. Where: scoring engine logs and assurance workpapers. |
| R0-M5 Anchor specificity and monotonicity | Rubric_0 anchors contain explicit, progressively stricter tests from `0` to `100`. | For sampled sub-dimensions, anchor criteria are measurable and monotonic; no anchor uses undefined adjectives as sole test; threshold contradictions = 0. | Who: rubric owner + QA reviewer. What: anchor lint checklist, threshold consistency report. Where: rubric text repository and quality review log. |
| R0-M6 Evidence admissibility and provenance rigor | Rubric_0 defines admissible evidence rules that prevent unverifiable claims. | Admissibility checks enforce freshness, provenance, and backfill cutoff; screenshots-only evidence rejected unless source export exists; missing mandatory evidence consistently caps scores. | Who: evidence custodian + evaluator + audit observer. What: admissibility checklist runs, rejected-evidence register, cap application log. Where: evidence vault and cycle adjudication records. |
| R0-M7 Independent replayability and recomputation | Rubric_0 scoring can be independently replayed and recomputed with stable outcomes. | At least two non-author replays complete from documented inputs; score variance <=5 points total and <=1 anchor step per sub-dimension; recomputed KPIs match published values within declared tolerance. | Who: independent reviewer 1 + independent reviewer 2. What: replay runbooks, replay logs, recomputation reports. Where: replay environment artifacts and signed witness reports. |
| R0-M8 Contradiction handling effectiveness | Rubric_0 detects, ages, and resolves contradictions across sources, roles, and decisions. | Critical contradictions are logged within SLA, adjudicated with owner/date/rationale, and closed before pass decisions; unresolved critical contradiction count at decision time = 0. | Who: adjudication chair + affected role owners. What: contradiction register, SLA aging dashboard, closure evidence. Where: governance tracker and adjudication minutes. |
| R0-M9 Anti-gaming control coverage depth | Rubric_0 anti-gaming catalog covers high-probability manipulation patterns with enforceable consequences. | Controls explicitly test cherry-picking, denominator drift, narrative drift, backdating, survivorship bias, and evidence laundering; each control has fail consequence tied to cap/fail logic. | Who: R0 + R15 + QA lead. What: anti-gaming control matrix, challenge results, consequence application log. Where: rubric control appendix and audit sampling records. |
| R0-M10 Score inflation resistance | Rubric_0 resists unjustified score escalation through caps, independent review requirements, and replay gates. | Attempted inflation scenarios cannot push score above policy limits; >75 blocked without independent evidence; >90 blocked without cross-environment replay; >100 impossible by construction. | Who: R0 governance lead + red-team evaluator. What: inflation attack test suite, blocked-attempt evidence, policy compliance report. Where: adversarial test logs and scoring engine outputs. |
| R0-M11 Accountability and ownership clarity | Each rubric control, threshold, and corrective action has a single accountable owner and independent checker. | 100% of critical controls have named owner role, reviewer role, and decision SLA; orphaned controls = 0; ownership transitions leave no open gap over SLA. | Who: R0 office + HRBP + PMO. What: control RACI map, ownership transition log, SLA compliance report. Where: governance roster and role-accountability register. |
| R0-M12 Cross-role handoff operability | Rubric_0 enables clear handoffs and dispute resolution among role evaluators. | Handoff packages include acceptance criteria, timestamps, and escalation paths; sampled disputes resolved within SLA; silent acceptance is disallowed in operations. | Who: R0 + role leads (R1/R2/R7/R8/R12/R14/R15). What: handoff packets, return reasons, escalation records. Where: cross-role adjudication board and workflow system. |
| R0-M13 Exception and waiver governance integrity | Rubric_0 exceptions are controlled, time-bound, and auditable. | 100% exceptions include rationale, compensating control, owner, expiry, and renewal review; expired exceptions active in scoring = 0. | Who: R0 + control owner + internal audit. What: waiver register, compensating-control tests, expiry audit report. Where: GRC platform and governance ledger. |
| R0-M14 Temporal/version governance and cutoff control | Rubric_0 versions are frozen per cycle and changes are diffed and approved. | Each scoring cycle references immutable rubric version ID; post-cutoff edits cannot alter cycle score without formal re-open; undocumented version drift = 0. | Who: rubric maintainer + release manager + audit reviewer. What: version tags, diff approvals, cycle freeze records. Where: git history and release governance archive. |
| R0-M15 Reporting reconciliation and executive transparency | Rubric_0 outputs reconcile to raw evidence and are transparent to executive review. | Random sample reconciliation shows <=1% unexplained variance between reported and source-derived metrics; unresolved material reconciliation issues at sign-off = 0. | Who: R0 + finance + internal audit. What: reconciliation workbook, variance log, executive report appendix. Where: board reporting pack and source data extracts. |
| R0-M16 Improvement loop and delta re-validation discipline | Rubric_0 is improved through measured corrective cycles and validated deltas. | Every cycle records rubric defects, fixes, and impact hypotheses; next cycle re-tests changed sections; repeat defects trend downward across two cycles. | Who: rubric owner + R0 + R15. What: corrective-action backlog, delta test results, trend chart. Where: rubric change log and retrospective records. |

## 3) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R0-M1 Decision-band actionability | Bands missing or contradictory; decisions are arbitrary. | Bands exist but overlap or lack required actions. | Bands mostly distinct; evaluator agreement <70%. | Non-overlapping bands; >=85% agreement in case simulation. | >=95% agreement with independent reviewer replay. | Two cycles >=95% agreement and zero unresolved decision disputes. |
| R0-M2 Strategy-to-rubric coverage completeness | Critical objectives/risks have no rubric coverage. | Partial mapping exists; major blind spots remain. | Most objectives mapped; some critical gaps unresolved. | Full objective mapping; no critical blind spots. | Independent review confirms mapping accuracy and no unresolved gaps. | Two cycles maintain complete mapping despite portfolio changes. |
| R0-M3 Weighting and capital-risk proportionality | Weights arbitrary; critical risk can be averaged away. | Weights declared without rationale or sensitivity test. | Basic rationale exists; masking risk not fully tested. | Sensitivity-tested weights; gate precedence prevents masking. | Independent challenge confirms robust risk-proportional behavior. | Multi-cycle evidence shows stable, governance-approved proportionality. |
| R0-M4 Gate enforceability and precedence clarity | Gates undefined or not applied. | Gates documented but precedence conflicts exist. | Gates mostly applied; occasional manual overrides without rule. | Gate truth table enforced in all sampled runs. | Independent replay confirms deterministic gate behavior. | Two cycles with zero precedence violations or undocumented overrides. |
| R0-M5 Anchor specificity and monotonicity | Anchor criteria vague and non-measurable. | Some measurable anchors; monotonic progression breaks. | Most anchors measurable; minor threshold ambiguity persists. | All anchors measurable and strictly monotonic. | Independent lint/review finds no ambiguity in sampled set. | Two cycles with zero anchor ambiguity findings. |
| R0-M6 Evidence admissibility and provenance rigor | Evidence rules absent; unverifiable claims accepted. | Rules exist but frequently bypassed. | Rules applied inconsistently; backfill leakage remains. | Rules consistently enforce freshness, provenance, and cutoffs. | Independent audit confirms consistent admissibility outcomes. | Two cycles with zero inadmissible evidence accepted. |
| R0-M7 Independent replayability and recomputation | Scoring cannot be replayed independently. | Author-only reruns; replay instructions incomplete. | One independent replay passes with high variance. | Two independent replays pass within declared tolerance. | Cross-environment replay and recomputation match thresholds met. | Two-cycle replay stability with <=5 point variance each cycle. |
| R0-M8 Contradiction handling effectiveness | Contradictions ignored; pass decisions proceed anyway. | Contradictions logged ad hoc without closure discipline. | Register exists; critical contradiction aging breaches SLA. | Critical contradictions resolved before pass decisions. | Independent audit confirms closure quality and rationale traceability. | Two cycles with no unresolved critical contradiction at sign-off. |
| R0-M9 Anti-gaming control coverage depth | No anti-gaming controls defined. | Controls exist but omit common manipulation patterns. | Coverage broad but consequences weak or inconsistently applied. | Controls cover major patterns with enforced consequences. | Surprise challenges demonstrate controls detect manipulation reliably. | Two cycles with successful detection and no unmitigated gaming pattern. |
| R0-M10 Score inflation resistance | Inflated scores routinely pass without scrutiny. | Cap rules documented but easily bypassed. | Caps apply in some cases; escalation paths weak. | Inflation tests fail to breach >75/>90 policy gates. | Independent red-team confirms resistance to inflation attempts. | Two cycles with zero successful inflation attempts. |
| R0-M11 Accountability and ownership clarity | Critical controls have no owners. | Owners listed but reviewer/SLA missing. | Most controls owned; transition gaps create exposure. | All critical controls have owner, reviewer, and SLA. | Independent sample confirms accountability works during turnover. | Two cycles with no critical ownership gap beyond SLA. |
| R0-M12 Cross-role handoff operability | Handoffs undefined; disputes stall scoring. | Handoffs informal; acceptance criteria unclear. | Handoffs structured; SLA misses frequent. | Binary acceptance/return process works within SLA. | Independent sampling shows low rework and clear escalation. | Two cycles with sustained SLA compliance and low repeat defects. |
| R0-M13 Exception and waiver governance integrity | Exceptions untracked or open-ended. | Register exists; expiries and controls often missing. | Most waivers valid; expired waivers occasionally active. | All waivers time-bound with tested compensating controls. | Independent audit verifies waiver validity and expiry enforcement. | Two cycles with zero expired or unsupported waivers. |
| R0-M14 Temporal/version governance and cutoff control | Rubric versions unmanaged; cycle scope mutable. | Version tags exist; cutoff enforcement weak. | Frozen versions used, but post-cutoff edits leak into scores. | Immutable version per cycle; re-open required for changes. | Independent diff audit confirms no unauthorized retroactive scoring change. | Two cycles with complete version integrity and change traceability. |
| R0-M15 Reporting reconciliation and executive transparency | Reported scores cannot be tied to source evidence. | Reconciliation performed selectively and late. | Reconciliation mostly complete; variance handling weak. | Routine reconciliation; material issues resolved before sign-off. | Independent reviewer reproduces reported metrics with <=1% variance. | Two cycles with zero unresolved material reconciliation defects. |
| R0-M16 Improvement loop and delta re-validation discipline | No formal rubric improvement loop. | Issues logged without owners or follow-through. | Fixes shipped; delta impact rarely re-tested. | Every change has owner, hypothesis, and next-cycle re-test. | Independent review confirms delta tests close prior defects. | Two cycles show downward repeat-defect trend and stable gains. |

## 4) Role-specific anti-gaming checks for rubric-evaluation gaming risks

| Check ID | Gaming risk pattern | Evaluator challenge test | Consequence if failed |
| --- | --- | --- | --- |
| R0-AG1 | Selective scenario sampling to make Rubric_0 look robust. | Force inclusion of adverse and borderline cases in simulation set; compare decision stability. | Rubric_1 cap at `50` for R0-M1 and R0-M3. |
| R0-AG2 | Weight tuning to inflate overall score while critical controls stay weak. | Run sensitivity sweep with critical-control failures injected. | R0-M3 and R0-M10 set to `0` for cycle. |
| R0-AG3 | Backdated rubric approvals or evidence cut-off manipulation. | Diff approval timestamps against cycle freeze timestamp and version history. | Whole Rubric_1 evaluation invalidated for cycle. |
| R0-AG4 | Cosmetic anti-gaming matrix with no enforced consequences. | Trace sampled anti-gaming failures to actual cap/fail application logs. | R0-M9 capped at `25`; executive sign-off blocked. |
| R0-AG5 | Independent replay performed by non-independent parties. | Verify reviewer independence and non-author status via access/activity records. | Scores above `75` disallowed across all sub-dimensions. |
| R0-AG6 | Contradiction register closed administratively without evidence resolution. | Re-open random closed contradictions and verify source-level reconciliation. | R0-M8 set to `0`; cycle marked `FAIL`. |
| R0-AG7 | Reconciliation laundering through rounded summaries only. | Recompute reported totals from raw data extracts and compare variance. | R0-M15 capped at `25`; board report reissue required. |
| R0-AG8 | Exception expiry bypass through silent renewal. | Audit renewal trail for pre-expiry approval and compensating-control retest. | R0-M13 set to `0`; exception-dependent scores voided. |
| R0-AG9 | Anchor inflation via ambiguous language reinterpretation. | Blind-score same cases with two evaluator teams and compare anchor drift. | R0-M5 capped at `50`; anchor text must be revised before reuse. |
| R0-AG10 | Change-log suppression to hide rubric weakening changes. | Compare scoring version to git diff and approval ledger for missing deltas. | R0-M14 set to `0`; cycle requires full re-evaluation. |

## 5) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

| ID | Tripwire / hard-fail condition | Invalidation effect | Required recovery evidence |
| --- | --- | --- | --- |
| R0-HF1 | Any confirmed fabrication, tamper, or backdating in Rubric_0 evaluation evidence. | Rubric_0 scoring invalid for cycle; executive decision use prohibited. | Forensic report, accountable action, and clean re-run under supervised controls. |
| R0-HF2 | Gate logic conflict: same case yields both pass and fail under documented rules. | Rubric_0 scoring halted until gate logic is corrected and replayed. | Corrected truth table, regression test, and independent witness replay. |
| R0-HF3 | Critical contradiction unresolved at executive decision time. | Automatic `FAIL` on Rubric_0 governance readiness. | Closed contradiction record with rationale, owner, and verification evidence. |
| R0-HF4 | Score above `75` assigned without independent reviewer evidence. | Affected scores invalidated and reset to maximum `50`. | Independent reviewer package and rescored output. |
| R0-HF5 | Score above `90` assigned without cross-environment replay and recomputation proof. | Affected scores invalidated and reset to maximum `75`. | Cross-environment replay logs and recomputation match report. |
| R0-HF6 | Post-cutoff rubric edits used to retroactively improve same-cycle score. | Entire cycle invalidated; re-open required with new cycle ID. | Version freeze evidence, approved reopen memo, full rescore artifacts. |
| R0-HF7 | Missing mandatory evidence exceeds 20% for Rubric_0 evaluation package. | Rubric_0 scoring invalidated for incompleteness. | Completed evidence manifest with provenance and freshness checks. |
| R0-HF8 | Expired waiver or waiver without compensating control used in scoring justification. | Waiver-dependent rows invalidated; overall cycle cannot pass. | Valid renewed waiver, tested compensating control, audit attestation. |
| R0-HF9 | Reported Rubric_0 outputs cannot be reconciled to source data within 1% variance on material metrics. | Executive report invalid; no decision authority until corrected. | Reconciled data pack and independent reconciliation sign-off. |
| R0-HF10 | Two consecutive cycles fail to close previously identified critical Rubric_0 design defects. | Rubric_0 decertified for governance use pending redesign. | Defect closure evidence and successful recertification replay. |

## 6) Cross-role dependencies and adjudication handoffs

| Partner role | Required handoff into R0 meta-evaluation | Acceptance criteria | Escalation / adjudication trigger |
| --- | --- | --- | --- |
| R1 Product Manager | Objective hierarchy and requirement intent mappings used by Rubric_0. | Mapping completeness check passes; no ambiguous objective ownership. | Escalate if objective traceability is missing or contradictory. |
| R2 Product Architect / Enterprise Architect | Architecture-risk rationale supporting weighting and gate severity. | Risk-class mapping aligns with rubric gate logic and NFR priorities. | Escalate if architectural criticality is downgraded without approval. |
| R3 Engineering Manager | Delivery-flow and defect-governance evidence used in practical rubric operation. | Operational SLAs and corrective loops are evidence-backed and current. | Escalate if cadence data is stale or manipulated. |
| R5 QA / Test Engineer | Verification design, falsifiability checks, and mutation/replay evidence. | Test oracles are explicit and replay logs support assigned anchors. | Escalate if pass claims are not falsifiable or replayable. |
| R7 Security Engineer | Integrity controls for evidence provenance and tamper resistance. | Chain-of-custody and control integrity meet mandatory policy thresholds. | Escalate on any integrity gap affecting scoring credibility. |
| R8 Privacy / Compliance / Legal | Legal/privacy/control obligations impacting gate and fail logic. | Obligations are mapped to hard gates with current applicability. | Escalate on unresolved legal-control contradiction. |
| R12 DevOps / Release Manager | Version freeze, change-control, and cross-environment replay infrastructure. | Rubric versioning, environment parity, and replay artifacts are reproducible. | Escalate if cutoff/version controls fail or replay infra is unstable. |
| R14 FinOps / Procurement / Vendor Management | Cost-of-assurance and governance-effort evidence for operational feasibility. | Rubric operations are sustainable without reducing required assurance rigor. | Escalate if cost pressure drives weakening of mandatory controls. |
| R15 Internal Audit / Assurance | Independent sampling results, assurance opinions, and defect closure validation. | Independence criteria met; findings and severities are evidence-defensible. | Escalate on independence conflict or repeated unclosed critical findings. |

### Adjudication handoff sequence
1. R0 opens cycle with frozen Rubric_0 version ID and evidence cutoff timestamp.
2. Each partner role submits signed handoff package with `who/what/where` references.
3. R15 performs independent sample and contradiction check before final anchor assignment.
4. R0 adjudication board resolves returned handoffs within SLA and records decision rationale.
5. Final Rubric_1 decision is issued only after tripwire scan confirms no active hard-fail.

## 7) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle point | Improvement action on Rubric_0 | Required evidence artifact | Pass criterion |
| --- | --- | --- | --- |
| Pre-cycle | Freeze Rubric_0 version, weights, gate rules, and evidence cutoff policy. | Version tag, approved change memo, cutoff notice. | 100% evaluators use same immutable rubric version. |
| Pre-cycle | Re-validate anchor text for monotonic thresholds and ambiguity removal. | Anchor lint report and approved wording diff. | Zero critical anchor ambiguity findings. |
| Pre-cycle | Refresh anti-gaming matrix against latest observed manipulation attempts. | Updated anti-gaming catalog with mapped consequences. | All high-frequency gaming patterns have active control tests. |
| Pre-cycle | Confirm contradiction SLA, escalation path, and owner roster. | Current contradiction SOP and accountable-owner list. | No unassigned contradiction workflow step. |
| Mid-cycle | Run surprise replay on sampled scored rows. | Replay logs, variance report, adjudication notes. | Variance within tolerance; breaches trigger immediate correction. |
| Mid-cycle | Audit admissibility and provenance on random evidence sample. | Evidence sample audit sheet and failure actions. | No inadmissible evidence retained in scored set. |
| Mid-cycle | Execute score-inflation red-team challenge. | Inflation challenge report with blocked attempts. | No successful unauthorized score escalation. |
| Mid-cycle | Reconcile interim executive summary metrics to source data. | Reconciliation workbook and discrepancy log. | Material variance resolved before cycle close. |
| End-cycle | Re-test all modified Rubric_0 sections (delta-based re-evaluation). | Delta test matrix with pass/fail evidence links. | 100% changed sections revalidated before certification. |
| End-cycle | Verify closure of critical defects found in previous cycle. | Defect closure packets with effectiveness tests. | No carried critical defect without approved exception. |
| End-cycle | Publish candid meta-review: what changed, why, and measured impact. | Cycle retrospective with before/after score impact analysis. | Improvement claims are evidence-backed and replayable. |
| End-cycle | Approve or deny Rubric_0 for next-cycle governance use. | Signed decision record and conditions register. | Decision aligns with tripwire status and anchor outcomes. |


---

## R1 Product Manager

- source_file: `swarm_outputs/meta_rubric_role_expansions/R1_product_manager_rubric1.md`
- words: 3699
- lines: 130

# R1 Product Manager Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

## 1) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R1 evaluates whether Rubric_0 is decision-usable for product governance: clear enough to drive prioritization, strict enough to resist score inflation, and operational enough to run on release and planning cadence. This meta-rubric scores the quality of Rubric_0 itself, not the quality of project artifacts scored by Rubric_0.

### Decision rights (R1 meta-evaluator)
1. Accept or reject Rubric_0 for use in product planning/release decisions based on evidence-replayable quality tests.
2. Require rewording/removal of Rubric_0 criteria that are ambiguous, non-falsifiable, or non-auditable.
3. Block use of Rubric_0 scores when contradiction-handling, evidence integrity, or gate logic fails.
4. Trigger cross-role adjudication when Rubric_0 creates conflicting obligations across R1/R2/R6/R7/R8/R12/R15.
5. Approve rubric version increments only when delta impact and migration effects are documented.

### Scoring and admissibility rules
- Anchor scale: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero meta-score requires explicit `who/what/where` evidence.
- No sub-dimension may score above `50` without replayable evidence.
- No sub-dimension may score above `75` without independent reviewer validation.
- No sub-dimension may score above `90` without in-cycle adversarial challenge evidence.
- Evidence created after cycle cutoff is excluded from current-cycle meta-scoring.

## 2) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R1-M1 Objective-to-Dimension Alignment Integrity | Rubric_0 dimensions and role rows map to product decision types and strategic outcomes. | 100% top-level sections and role rows map to at least one concrete decision type (`prioritize`, `scope`, `go/no-go`, `pivot/stop`); orphan criteria count = 0. | Who: R1 owner + R0 sponsor reviewer. What: objective-to-rubric mapping matrix. Where: governance repository and rubric version review minutes. |
| R1-M2 Problem-Framing Coverage Adequacy | Rubric_0 consistently evaluates problem statement quality, scope boundaries, and non-goals. | Sample 20 Rubric_0 rows across A1/A2 and role layer; >=95% include actor, impact metric, time window, boundary, and non-goal expectations. | Who: R1 + R10 research counterpart. What: sampled row audit sheet. Where: rubric source files and sampling workbook. |
| R1-M3 KPI/Guardrail Specification Precision | Rubric_0 metric language is formula-based and resistant to metric gaming. | For all metric-bearing rows: formula, denominator, owner, refresh cadence, and guardrail are explicit; unversioned formula changes = 0. | Who: R1 + R9 data reviewer. What: KPI-definition conformance check. Where: rubric text, metric dictionary, change log. |
| R1-M4 Prioritization and Tradeoff Decision Utility | Rubric_0 can be used to rank options under capacity and risk constraints. | Replay two historical planning decisions using Rubric_0: rank order reproducibility variance <= 1 position for top 10; tradeoff rationale completeness >=95%. | Who: R1 + R3 + finance observer. What: replay simulation outputs. Where: portfolio decision archive and replay packet. |
| R1-M5 Requirement-to-Evidence Traceability Design | Rubric_0 criteria specify evidence requirements that are directly testable. | 15% random sample of scored rows: each non-zero score includes valid `who/what/where`; missing-source evidence rate <=2%. | Who: R1 meta-reviewer + R15 independent checker. What: traceability audit log. Where: scoring packet and evidence index. |
| R1-M6 Contradiction Detection and Resolution Protocol Quality | Rubric_0 defines how conflicting claims/controls are detected, aged, escalated, and resolved. | Contradiction register schema exists; severity tiers and SLA defined; critical contradiction carry-over into decision close = 0. | Who: R1 + R2/R8/R12 adjudicators. What: contradiction policy and sampled contradiction cases. Where: rubric governance docs and cycle contradiction log. |
| R1-M7 Evidence Replayability and Score Recompute Reliability | Independent reviewers can reproduce sub-scores and aggregate scores from raw evidence. | Independent replay on >=20% of scored rows reproduces anchor values exactly; aggregate recomputation difference = 0. | Who: non-author reviewer + R15. What: replay runbook, recompute worksheet, variance log. Where: evidence vault and scoring workbook. |
| R1-M8 Scoring Determinism and Gate Precedence Clarity | Rubric_0 scoring math, weighting, and gate precedence are explicit and non-contradictory. | Formula definitions complete; precedence order (`row`, `role`, `global`) unambiguous; dry-run shows identical outcomes across two evaluators. | Who: R1 + R12 release governance reviewer. What: scoring logic spec and dry-run transcript. Where: rubric master file and adjudication test records. |
| R1-M9 Anchor Discrimination and Inflation Resistance | Anchor language distinguishes quality levels behaviorally and limits unjustified high scores. | Anchor delta test: 75/90/100 require materially stronger evidence than 50; high-score concentration >30% requires forced resample review. | Who: R1 + R15. What: anchor differentiation review and score distribution analysis. Where: rubric anchor tables and cycle score distribution dashboard. |
| R1-M10 Anti-Gaming Control Coverage and Enforceability | Rubric_0 contains explicit controls for backfill, cherry-pick, denominator, and authority gaming. | Each major section + role layer has anti-gaming checks and enforcement action; failed control triggers deterministic score consequence in rules. | Who: R1 + R7/R15. What: anti-gaming control matrix and challenge-test results. Where: rubric anti-gaming sections and challenge logs. |
| R1-M11 Hard-Gate and Tripwire Executability | Rubric_0 hard-fail conditions are measurable, testable, and operationally enforceable. | Every tripwire has trigger, detection method, immediate effect, and recovery proof; scenario replay across 3 cycles yields consistent decisions. | Who: R1 + R12 + R8. What: tripwire completeness audit and scenario replay report. Where: rubric gates section and governance simulation records. |
| R1-M12 Cross-Role Handoff and Adjudication Operability | Rubric_0 supports role handoffs with clear entry/exit criteria and arbitration path. | For critical handoffs (`R1-R2`, `R1-R7`, `R1-R8`, `R1-R12`, `R1-R15`): entry/exit criteria + SLA + escalation owner all present and used in cycle. | Who: R1 + counterpart role leads. What: handoff conformance review. Where: role expansion docs and adjudication logs. |
| R1-M13 Operational Cadence Fit and Review Latency | Rubric_0 can be executed within planning/release timelines without decision stalls. | Median meta-evaluation completion time <=3 business days for release cycles and <=7 business days for quarterly planning; missed-SLA reviews <=10%. | Who: R1 operations owner + PMO. What: cycle timing metrics and bottleneck report. Where: review tracker and governance calendar. |
| R1-M14 Rubric Versioning and Change Governance Discipline | Rubric_0 changes are versioned, impact-assessed, and migration-safe. | Semantic version present; each change lists rationale, affected rows, expected scoring impact, and back-compat notes; undocumented edits = 0. | Who: R1 rubric owner + R15 observer. What: version history, change proposals, approval records. Where: rubric repository and change-control log. |
| R1-M15 Delta Re-evaluation and Learning Loop Effectiveness | Rubric_0 is improved through closed-loop analysis of scoring errors and drift. | >=90% prior-cycle rubric improvement actions closed by due date; false-positive/false-negative patterns tracked and reflected in updates. | Who: R1 + R3 + R15. What: action tracker, error taxonomy, delta outcome report. Where: retrospective records and rubric changelog. |
| R1-M16 Decision Outcome Calibration Utility | Rubric_0 scores correlate with downstream decision quality and risk outcomes. | Quarterly calibration uses fixed cohorts (`low` <=50, `high` >=90), fixed outcome window (90 days post-decision), and fixed adverse-outcome taxonomy (`severity_1_incident`, `regulatory_breach`, `missed_primary_kpi_by_>20pct`). Pass requires low cohort adverse-outcome rate >=1.5x high cohort and `p_value < 0.05`; unexplained calibration drift = 0. | Who: R1 + R9 analytics + R0 governance sponsor. What: calibration study (cohort definitions, outcome taxonomy, statistical test output) and variance explanation memo. Where: outcome analytics workspace and governance review deck. |

## 3) Anchor table (explicit behavioral anchors at 0/25/50/75/90/100)

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R1-M1 Objective-to-Dimension Alignment Integrity | Rubric_0 criteria are not linked to product decisions. | Partial mapping exists; many rubric rows are decision-orphaned. | Most rows mapped, but key decision classes are missing or duplicated ambiguously. | All major decision classes mapped with named ownership and review cadence. | Independent sample confirms mapping correctness and no material orphan criteria. | Two cycles with 100% maintained mapping and zero mapping disputes at adjudication. |
| R1-M2 Problem-Framing Coverage Adequacy | Rubric_0 omits problem-framing checks. | Problem framing exists as prose only; boundary/non-goal tests missing. | Core problem checks present but inconsistent across sections/roles. | Problem, boundary, and non-goal checks are explicit and consistently testable. | Cross-role review confirms coverage prevents scope laundering in sampled decisions. | Two cycles with no critical decision accepted without complete problem-framing evidence. |
| R1-M3 KPI/Guardrail Specification Precision | Metric criteria are undefined or non-computable. | KPIs listed but formulas/denominators/owners are missing for many rows. | Most KPI definitions exist; guardrail logic is weak or inconsistently specified. | KPI and guardrail definitions are complete and version-controlled. | Independent recomputation validates metric definitions and denominator stability. | Two cycles with zero unapproved formula changes and no metric-gaming finding. |
| R1-M4 Prioritization and Tradeoff Decision Utility | Rubric_0 cannot support ranking decisions. | Ranking is possible only with subjective interpretation. | Ranking model exists, but replayed decisions produce unstable ordering. | Replay produces stable rankings and explicit tradeoff records. | Scenario stress tests preserve coherent ranking under capacity/risk shifts. | Two planning cycles show reproducible prioritization with documented opportunity-cost decisions. |
| R1-M5 Requirement-to-Evidence Traceability Design | Non-zero scores are granted without traceable evidence requirements. | Evidence fields exist but are optional or frequently incomplete. | Evidence requirements are mostly explicit; sampling reveals recurring source gaps. | Evidence requirements are explicit and consistently enforced for non-zero scores. | Independent audit sample confirms high traceability and low evidence defect rate. | Two cycles with zero unsupported non-zero scores in independent sampling. |
| R1-M6 Contradiction Detection and Resolution Protocol Quality | Contradictions are neither logged nor resolved. | Contradictions are logged ad hoc without SLA or owner. | Register exists with owners, but critical contradictions age past decision cutoff. | Contradictions are severity-ranked, SLA-managed, and resolved before decisions. | Independent adjudication confirms resolution quality and score updates are consistent. | Two cycles with zero unresolved critical contradictions at final scoring. |
| R1-M7 Evidence Replayability and Score Recompute Reliability | Scores cannot be reproduced from available evidence. | Partial reproduction possible; many rows rely on unverifiable interpretation. | Most rows reproducible; recomputation variance occurs in weighted totals. | Independent replay reproduces row and aggregate scores consistently. | Adversarial replay by non-author reviewer passes with no material variance. | Two cycles with full replay success and deterministic recompute across reviewers. |
| R1-M8 Scoring Determinism and Gate Precedence Clarity | Scoring math and gates are contradictory or undefined. | Formulas exist but gate precedence is ambiguous and applied inconsistently. | Scoring mostly deterministic; edge cases require manual arbitration. | Deterministic math and precedence rules are explicit for normal and edge cases. | Independent dry-runs produce identical outputs, including gate-triggered fail paths. | Two cycles with zero precedence disputes and exact evaluator agreement. |
| R1-M9 Anchor Discrimination and Inflation Resistance | Anchor levels are indistinguishable; inflation is unchecked. | Anchor wording differs cosmetically, allowing arbitrary scoring jumps. | Anchor differences exist but evidence thresholds for high scores are weak. | Clear behavioral anchor separation; high scores require stronger evidence and review gates. | Score-distribution monitoring detects and corrects inflation attempts in-cycle. | Two cycles with stable distribution and no unjustified 90/100 grants on audit sample. |
| R1-M10 Anti-Gaming Control Coverage and Enforceability | No anti-gaming controls are defined. | Controls listed but not linked to enforcement actions. | Controls exist and are sometimes run; failures do not consistently affect scores. | Controls run on cadence; failures trigger rule-based score consequences. | Surprise challenge tests validate controls against real gaming attempts. | Two cycles with full control execution and documented prevention of attempted gaming patterns. |
| R1-M11 Hard-Gate and Tripwire Executability | Hard gates are absent or non-operational. | Gates exist but triggers/effects are too vague for consistent enforcement. | Most gates executable; some lack detection method or recovery proof. | All gates have precise trigger, detection source, effect, and recovery criteria. | Scenario replays show consistent enforcement across reviewers and cycles. | Two cycles with zero gate ambiguity and no disputed hard-fail application. |
| R1-M12 Cross-Role Handoff and Adjudication Operability | Handoffs and adjudication paths are undefined. | Handoffs named but missing entry/exit criteria or owner accountability. | Handoffs mostly defined; SLA/escalation behavior inconsistent in practice. | Critical handoffs have clear criteria, SLA, and arbitration owner, and are used reliably. | Cross-role audits confirm handoff quality and low rework from ambiguity. | Two cycles with no critical handoff failure causing decision delay or invalid score. |
| R1-M13 Operational Cadence Fit and Review Latency | Rubric_0 review routinely misses decision windows. | Review is possible only through deadline-breaking manual effort. | Cadence usually met, but frequent bottlenecks reduce decision usefulness. | Review cycle meets SLA in most cases with manageable operational effort. | Cycle timing is stable across release and planning modes with low bottleneck recurrence. | Two cycles with sustained SLA compliance and no delayed go/no-go due to rubric process. |
| R1-M14 Rubric Versioning and Change Governance Discipline | Rubric changes are ad hoc and untracked. | Versions exist, but changes lack impact analysis and approval trail. | Change records are present, but migration/back-compat guidance is incomplete. | Versioning, approvals, and impact notes are complete and consistently applied. | Independent reviewer can trace any score delta to specific approved rubric changes. | Two cycles with zero undocumented edits and clean migration across version updates. |
| R1-M15 Delta Re-evaluation and Learning Loop Effectiveness | No learning loop; same rubric defects recur. | Improvement actions are logged but mostly unowned or overdue. | Actions are tracked and partially closed; scoring error classes persist. | Improvement actions close on time and reduce known scoring defects. | Delta analysis shows measurable reduction in false positives/negatives after updates. | Two cycles with sustained defect reduction and proactive rubric refinements. |
| R1-M16 Decision Outcome Calibration Utility | Rubric scores show no relationship to downstream outcomes. | Calibration attempted, but data quality prevents reliable interpretation. | Weak directional relationship exists; drift remains unexplained. | Calibration shows meaningful correlation and informs threshold tuning. | Independent statistical review validates correlation and drift explanation quality. | Two cycles with stable predictive calibration and documented threshold improvements. |

## 4) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Anchor inflation scan: automatically flag any cycle where `90/100` density exceeds `30%` without corresponding independent-validation artifacts.
2. Denominator lock check: reject scorecards where population definitions changed after poor results without pre-approved change record.
3. Backfill exclusion audit: compare artifact creation timestamps to cycle cutoff; exclude post-cutoff evidence from current-cycle scoring.
4. Contradiction suppression check: reconcile contradiction register against adjudication minutes; hidden critical contradictions invalidate affected scores.
5. Replay challenge quota: re-score at least `20%` of rows by a non-author reviewer each cycle.
6. Formula tamper detection: diff KPI/weighting formulas vs prior approved version; unapproved edits trigger score freeze.
7. Authority spoof check: validate approver identity/role at decision time (not current role) against HR/IAM snapshot.
8. Cherry-pick control: require full sample distribution when citing qualitative evidence; positive-only excerpts are inadmissible.
9. Weighting bias simulation: run equal-weight and risk-weight scenarios; unexplained extreme divergence requires adjudication.
10. Retroactive wording drift check: detect in-cycle rubric text edits that change interpretation after scoring started.
11. Silent override detection: compare computed score output vs published score; any manual override requires signed rationale and counter-sign.
12. Cross-role consistency test: sample paired evaluations across R1/R2/R7/R8/R12 for same condition; unexplained divergence beyond one anchor step triggers review.

## 5) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

| ID | Tripwire / hard-fail condition | Immediate effect | Minimum recovery proof |
| --- | --- | --- | --- |
| R1-MHF1 | Evidence fabrication, tampering, or backdated approval in any Rubric_0 evaluation artifact. | Entire Rubric_0 cycle score invalid (`FAIL`). | Forensic closure report, corrected evidence chain, and independent re-score. |
| R1-MHF2 | Critical contradiction remains unresolved at decision close (release or portfolio gate). | Rubric_0 score publication blocked. | Contradiction resolution record with updated scoring and cross-role sign-off. |
| R1-MHF3 | Independent replay cannot reproduce >=10% sampled row scores. | Cycle result invalid; mandatory full replay. | Replay pass report with variance = 0 on required sample. |
| R1-MHF4 | Hard gate triggered in Rubric_0 but ignored in published decision outcome. | Published score revoked; governance escalation required. | Corrected decision record and documented gate-precedence retraining. |
| R1-MHF5 | Non-zero scores assigned without required `who/what/where` evidence in >5% sampled rows. | Cap overall meta-score at `25`; invalidate affected dimensions. | Evidence completion and independent resampling below defect threshold. |
| R1-MHF6 | Unapproved rubric version change during active scoring window. | All in-window scores invalid until re-run on a single approved version. | Version freeze evidence and complete re-score on approved hash. |
| R1-MHF7 | Manual score override without signed rationale and authorized approvers. | Override voided; affected role/domain score reset pending adjudication. | Signed override package and independent reviewer concurrence. |
| R1-MHF8 | Required anti-gaming challenge tests not executed for cycle. | No score above `50` permitted for affected scope. | Completed challenge-test evidence and replayed scoring. |
| R1-MHF9 | Role handoff SLA breaches cause missing mandatory evidence for final decision. | Decision status forced to conditional fail. | Completed handoffs with accepted entry/exit criteria and re-adjudication. |
| R1-MHF10 | Calibration study shows inverse relationship (high scores with worse outcomes) and no corrective action. | Rubric_0 marked unfit-for-decision for next cycle. | Root-cause analysis, threshold redesign, and successful pilot recalibration. |

## 6) Cross-role dependencies and adjudication handoffs

| Counterpart role | R1 must provide (outbound) | R1 must receive (inbound) | Entry criteria | Exit/acceptance criteria | SLA |
| --- | --- | --- | --- | --- | --- |
| R0 Executive Sponsor | Rubric_0 fitness recommendation, decision impact summary, threshold-change proposal | Risk appetite changes, decision policy constraints | Calibration and replay data complete | Signed governance decision on rubric adoption/change | 5 business days |
| R2 Product Architect | Contradiction list affecting architecture-related rubric rows | Technical feasibility and architecture-control conflict rulings | Contradictions tagged by severity | Updated contradiction resolutions reflected in scoring packet | 3 business days |
| R3 Engineering Manager | Operational burden metrics and cadence-risk report | Delivery impact feedback from rubric execution | Two-cycle execution timing data available | Joint approved cadence adjustments | Weekly governance cadence |
| R7 Security Architect | Anti-gaming gap report for integrity/spoof risks | Security validation of evidence and identity controls | Integrity control matrix drafted | Security-signed control adequacy note | 3 business days |
| R8 Privacy/Compliance/Legal | Rubric wording for legal/privacy gating and tripwire logic | Legal enforceability confirmation and mandatory wording corrections | Candidate text for gate rows drafted | Approved legal/privacy wording committed | Before release-cycle scoring |
| R9 Data/AI | Calibration model assumptions and score distribution extracts | Statistical validity review and drift diagnostics | Outcome dataset quality checks passed | Signed calibration validation memo | 4 business days |
| R12 DevOps/Release Manager | Gate precedence test cases and decision-latency metrics | Release governance replay results and execution logs | Gate simulation scenarios prepared | Gate execution consistency attested | Per release train |
| R15 Internal Audit/Assurance | Evidence manifest and replay package for sampled rows | Independent replay result and control test findings | Evidence packet hash locked | Audit replay passes and findings disposition recorded | 5 business days |

### Adjudication rules
1. Any unresolved dispute on contradiction severity or gate precedence escalates to `R0 + R15` within 1 business day.
2. Handoff acceptance is binary (`accepted` or `returned`) with defect class and due date; silent acceptance is invalid.
3. Returned handoffs require corrected resubmission and full trace to impacted Rubric_0 rows before score publication.

## 7) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle phase | Checklist item | Evidence artifact | Delta re-evaluation rule |
| --- | --- | --- | --- |
| Cycle start | Lock rubric version hash and publish scoring window. | Version lock record and governance notice. | Any later hash change forces full cycle restart. |
| Cycle start | Reconfirm sub-dimension ownership and reviewer independence roster. | Owner matrix and independence attestations. | Conflict found -> reassign owner before scoring. |
| Design review | Run anchor discrimination review on all 16 sub-dimensions. | Anchor-delta audit worksheet. | Weakly separated anchors must be revised and re-approved. |
| Design review | Validate contradiction protocol fields (severity, owner, SLA, closure proof). | Contradiction protocol conformance report. | Missing field blocks scoring kickoff. |
| Data prep | Execute evidence source integrity scan (timestamps, provenance, authority). | Evidence integrity scan log. | Integrity defect -> affected scope scored `0` until corrected. |
| Scoring run | Perform non-author replay on >=20% sampled rows. | Replay worksheet and variance report. | Any variance >0 anchor steps requires full-dimension replay. |
| Scoring run | Recompute aggregate score independently from raw row scores. | Recompute script output and checksum. | Any mismatch invalidates published score draft. |
| Adjudication | Resolve all critical contradictions and update impacted scores. | Signed contradiction closure log. | Open critical contradiction blocks publication. |
| Adjudication | Run anti-gaming challenge set (denominator, backfill, override, authority). | Challenge results with pass/fail and enforcement action. | Failed challenge caps affected dimension at `50` max. |
| Publication | Publish final score with gate-trigger summary and evidence index. | Final scorecard, gate report, evidence manifest. | Missing manifest invalidates score publication. |
| Post-cycle | Compare predicted risk bands vs actual outcome bands. | Calibration report with risk-ratio table. | Drift beyond threshold requires threshold/anchor update proposal. |
| Post-cycle | Classify scoring defects (false positive, false negative, ambiguity, latency). | Defect taxonomy and frequency chart. | Top 3 defect classes must receive owned corrective actions. |
| Post-cycle | Close improvement actions with due dates and owner acceptance. | Action tracker with closure proof. | <90% on-time closure triggers next-cycle readiness warning. |
| Next-cycle readiness | Re-score prior cycle sample with updated rubric to quantify delta. | Delta re-score packet and variance explanation memo. | Unexplained delta >1 anchor step per row requires rollback of rubric update. |


---

## R2 Product Architect / Enterprise Architect

- source_file: `swarm_outputs/meta_rubric_role_expansions/R2_product_architect_enterprise_architect_rubric1.md`
- words: 3758
- lines: 139

# R2 Product Architect / Enterprise Architect Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

## 1) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R2 evaluates whether Rubric_0 is architected as an executable control system rather than a narrative document. The role is accountable for structural integrity, contradiction containment, evidence replayability, anti-gaming robustness, and deterministic scoring operations. R2 evaluates Rubric_0 design quality only, not delivery artifact quality.

### Decision rights (Rubric_0 meta-evaluation)
| Decision area | R2 authority | Non-delegable boundary | Required co-signers | Required decision evidence |
| --- | --- | --- | --- | --- |
| Rubric_0 architecture baseline | Final technical authority on structural model quality | Cannot approve if section boundaries are ambiguous or contradictory | R1, R3 | Baseline architecture map, issue log, signed adjudication record |
| Contradiction arbitration protocol | Final on contradiction taxonomy and closure rules | Cannot waive unresolved critical contradiction paths | R7, R8, R15 | Contradiction matrix, severity map, closure SLA policy |
| Evidence admissibility schema | Final on mandatory evidence fields and provenance controls | Cannot permit non-replayable evidence for non-zero scoring | R5, R15 | Evidence schema spec, replay procedure, immutable-link standard |
| Anchor model quality gate | Final on anchor specificity and monotonicity tests | Cannot accept anchors that allow subjective inflation | R5, R3 | Anchor lint report, calibration outcomes |
| Scoring aggregation integrity | Final on arithmetic determinism and precedence logic | Cannot permit multiple valid totals from same inputs | R12, R15 | Reference calculator, tie-break rules, recomputation test logs |
| Anti-gaming control package | Joint authority with control roles | Cannot reduce anti-gaming minimum set for cycle close | R7, R15 | Anti-gaming checklist, exception ledger |
| Hard-fail / tripwire catalog | Final recommendation, not unilateral override | Cannot close hard-fail without independent replay | R0, R15 | Tripwire evidence, replay certificate, closure sign-off |
| Rubric_0 version promotion | Recommend pass/hold for new rubric version | Cannot promote when required delta re-evaluation is missing | R0, R1, R3 | Diff pack, impact map, re-score report |

### Meta-scoring operating rule
- Anchor set for each sub-dimension: `0/25/50/75/90/100`.
- Any non-zero anchor requires admissible `who/what/where` evidence.
- Rubric_1 cycle score for R2 = mean of all sub-dimensions after caps and tripwire overrides.
- Any triggered hard-fail in Section 5 invalidates Rubric_0 scoring for that cycle.

## 2) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R2M-01 Rubric system boundary architecture | Rubric_0 clearly defines what is in-scope, out-of-scope, and cross-layer interactions. | Test that A1-A6 and role layer boundaries are explicitly stated; verify no row evaluates artifact outcomes directly in meta sections; verify each gate states scope of effect. | Who: R2 lead reviewer. What: scope map and boundary checklist. Where: Rubric_0 master document and review log. |
| R2M-02 Coverage completeness and non-overlap | Required quality domains are covered once with controlled cross-reference, not duplicated inconsistently. | Enumerate required domains from Rubric_0 intent and role pack; detect duplicate criteria with conflicting thresholds; confirm each domain has exactly one primary owner section. | Who: R2 + R1. What: domain coverage matrix and overlap diff. Where: Rubric_0 section index and role expansion pack. |
| R2M-03 Canonical terminology integrity | Terms are unambiguous and consistently defined across Rubric_0. | Build term dictionary from headings/tables; flag same term with divergent meaning; verify mandatory terms (`tripwire`, `critical`, `evidence`) have one canonical definition. | Who: R2 + R11. What: glossary lint report. Where: Rubric_0 text corpus and terminology register. |
| R2M-04 Contradiction handling protocol strength | Rubric_0 contains explicit contradiction detection, severity grading, SLA, and closure rules. | Verify contradiction classes exist (requirement-vs-control, score-vs-evidence, cross-role); replay 5 sampled contradictions through workflow; confirm unresolved critical contradiction blocks scoring. | Who: R2 + R15. What: contradiction protocol test sheet. Where: contradiction register and adjudication records. |
| R2M-05 Evidence admissibility schema rigor | Rubric_0 prescribes enforceable minimum evidence fields for scoring. | Confirm every scored claim requires `who/what/where/time/version`; verify late/backfilled evidence exclusion rule; verify provenance tamper checks are defined. | Who: R2 + R5. What: evidence schema conformance audit. Where: Rubric_0 evidence rules and sample scorecards. |
| R2M-06 Evidence replayability and recomputation | Independent reviewer can reproduce sampled scores from raw evidence with bounded variance. | Recompute at least 15% sampled rows; require same anchor result or documented rationale for delta; verify replay instructions are complete without tacit knowledge. | Who: independent reviewer (not original scorer). What: replay runbook and recompute logs. Where: immutable evidence store and scoring workbook. |
| R2M-07 Anchor specificity and monotonic behavior | Anchors are behaviorally explicit, progressively stricter, and non-overlapping. | Check each sub-dimension has all 6 anchors; verify anchor language contains observable tests; detect anchor inversions (90 easier than 75). | Who: R2 + R5. What: anchor monotonicity lint and calibration notes. Where: Rubric_0 anchor tables and reviewer calibration pack. |
| R2M-08 Scoring determinism and arithmetic integrity | Rubric_0 scoring formula yields one deterministic result per admissible input set. | Recalculate totals in two independent calculators; confirm equal result; verify weight sums, cap precedence, and rounding rules are explicit. | Who: R2 + R12. What: calculation parity report. Where: scoring model spec, scripts, and score outputs. |
| R2M-09 Gate and tripwire precedence clarity | Rubric_0 defines hard-gate precedence over averages without ambiguity. | Simulate cases with high averages but active gate; verify outcome forced per policy; verify gate IDs map to explicit enforcement action. | Who: R2 + R7 + R15. What: precedence test scenarios. Where: gate catalog and adjudication SOP. |
| R2M-10 Anti-gaming control sufficiency | Rubric_0 includes adversarial controls that are executable each cycle. | Confirm required anti-gaming checks have owner, cadence, and sample size; run one surprise challenge; verify failed check applies cap/hold automatically. | Who: R2 + R15. What: anti-gaming execution log. Where: cycle control checklist and score adjustment records. |
| R2M-11 Score inflation resistance | Rubric_0 prevents unjustified high scores from weak evidence or narrow sampling. | Detect denominator changes across cycles; audit high-score rows for independent evidence; verify 90+ requires additional controls and no open major findings. | Who: R2 + R0 + R15. What: inflation audit report. Where: historical score ledger and evidence packs. |
| R2M-12 Cross-role interoperability | Rubric_0 role layer handoffs are consistent, testable, and conflict-resolvable. | Sample 10 cross-role dependencies; verify both sides use same trigger, SLA, and acceptance criterion; detect circular approvals. | Who: R2 + R3 + R6. What: handoff compatibility matrix. Where: role expansion pack and governance workflow docs. |
| R2M-13 Exception and waiver governance quality | Rubric_0 controls exception use with expiry, owner, compensating control, and closure evidence. | Check exception template completeness; verify expired exception auto-fail behavior; confirm renewal requires fresh evidence, not copy-forward. | Who: R2 + R7 + R8. What: exception lifecycle audit. Where: waiver register and cycle decision log. |
| R2M-14 Operational adjudication usability | Rubric_0 can be executed by reviewers within defined cadence without interpretation drift. | Time-box dry run of full scoring cycle; measure unresolved reviewer ambiguities; confirm checklist maps to every scoring step and override path. | Who: R2 + R3 + R12. What: dry-run timing and ambiguity log. Where: adjudication runbook and meeting minutes. |
| R2M-15 Versioning and delta traceability | Rubric_0 changes are diffed, impact-scored, and re-evaluated before adoption. | Verify semantic versioning policy exists; verify each changed row has rationale and impacted dimensions; confirm prior-cycle comparability statement. | Who: R2 + R1 + R15. What: rubric diff dossier. Where: version control history and change approval records. |
| R2M-16 Audit reproducibility and assurance readiness | External/internal assurance can reproduce conclusions without author presence. | Conduct blind replay by assurance reviewer; verify all cited evidence is accessible and immutable; confirm adjudication trail is complete end-to-end. | Who: R15 with R2 observer. What: assurance replay certificate. Where: audit evidence store and adjudication archive. |

## 3) Anchor table (explicit behavioral anchors for every sub-dimension)

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R2M-01 Rubric system boundary architecture | Boundaries absent; rubric scope not definable. | Boundaries partially stated but conflicting across sections. | Major boundaries stated; meta-vs-artifact lines still leak. | Boundaries clear for most sections with minor clarifications needed. | Fully explicit boundaries with no material leakage in sampled rows. | Fully explicit and independently verified across two cycles with zero leakage. |
| R2M-02 Coverage completeness and non-overlap | Critical domains missing or duplicated inconsistently. | Coverage list exists but major gaps/duplication unresolved. | Most domains covered; overlap causes inconsistent scoring. | Complete domain coverage with controlled cross-references. | No material overlap conflicts in independent sample audit. | Complete, non-overlapping coverage sustained across two rubric revisions. |
| R2M-03 Canonical terminology integrity | Core terms undefined or contradictory. | Glossary exists but terms differ by section author. | Key terms defined; several operational terms still ambiguous. | Canonical definitions applied consistently in scoring rows. | Terminology lint passes with only minor editorial defects. | Zero semantic drift across sections and role pack, independently confirmed. |
| R2M-04 Contradiction handling protocol strength | No contradiction process; conflicts ignored. | Contradictions logged ad hoc; no SLA/severity framework. | Framework exists but does not enforce scoring consequences. | Structured process with severity, SLA, and closure ownership. | Critical contradictions reliably block scoring until closure evidence. | Multi-cycle proof that contradiction protocol prevents recurring unresolved conflicts. |
| R2M-05 Evidence admissibility schema rigor | Non-zero scores accepted without evidence schema. | Schema exists but missing mandatory fields or enforcement. | Mandatory fields defined; late/backfill controls weak. | Enforced schema with admissibility checks before scoring. | Proven rejection of inadmissible evidence in cycle audit. | Zero inadmissible evidence accepted across independent audits for two cycles. |
| R2M-06 Evidence replayability and recomputation | Scores cannot be replayed from source evidence. | Replay possible only with scorer interpretation. | Partial replay; major rows fail recomputation parity. | >=85% sampled rows replay successfully with documented method. | >=95% sampled rows replay with parity and traceable deltas. | 100% sampled replay parity across independent reviewers and tools. |
| R2M-07 Anchor specificity and monotonic behavior | Anchors missing or purely subjective language. | Anchors present but vague; thresholds not observable. | Observable tests exist but monotonic progression is inconsistent. | All anchors observable and mostly monotonic. | Monotonicity lint clean; calibration variance within defined band. | Two-cycle calibration shows stable interpretation with no anchor inversion. |
| R2M-08 Scoring determinism and arithmetic integrity | Different calculators produce different totals. | Formula partly specified; precedence and rounding ambiguous. | Deterministic core with unresolved cap/gate order edge cases. | Deterministic results for standard and edge-case scenarios. | Independent recompute parity achieved for full sampled cycle. | Deterministic parity sustained across toolchains and version updates. |
| R2M-09 Gate and tripwire precedence clarity | Gates can be bypassed by averaging. | Gate definitions exist but effects are inconsistent. | Precedence written but not validated with scenario testing. | Precedence validated with explicit fail scenarios. | No tested scenario allows gate bypass or contradictory outcome. | Two-cycle evidence of strict gate precedence with zero override drift. |
| R2M-10 Anti-gaming control sufficiency | No anti-gaming protocol or execution record. | Controls listed but owner/cadence unspecified. | Controls executable but sample size/cap rules weak. | Full control set with owner, cadence, sample size, and consequences. | Surprise challenge and recompute checks run and enforced each cycle. | Control package repeatedly detects and corrects attempted gaming behaviors. |
| R2M-11 Score inflation resistance | High scores assigned without strong evidence. | Basic controls exist but inflation paths remain open. | Inflation checks present; denominator drift not controlled. | Inflation controls include denominator freeze and independent review for high anchors. | 90+ scores consistently backed by stronger evidence and clean controls. | Multi-cycle inflation audit shows no unjustified upward drift after controls. |
| R2M-12 Cross-role interoperability | Role handoffs are undefined or contradictory. | Handoffs listed but acceptance criteria missing. | Criteria exist but SLA/ownership mismatch across roles. | Handoffs include aligned trigger, owner, SLA, and acceptance tests. | Independent sample shows high handoff acceptance without rework loops. | Cross-role adjudication operates with no unresolved circular dependencies. |
| R2M-13 Exception and waiver governance quality | Exceptions untracked or perpetual. | Exceptions logged without expiry or compensating controls. | Governance exists but renewals are weakly justified. | Exceptions time-bounded with owner and closure criteria. | Expired exceptions auto-trigger scoring hold and escalation. | Exception volume and age trend down with verified closure quality. |
| R2M-14 Operational adjudication usability | Rubric_0 cannot be executed consistently by reviewers. | Execution relies on tribal knowledge and ad hoc interpretation. | Runbook exists; frequent ambiguity causes timeline slips. | End-to-end cycle executable within defined SLA with low ambiguity. | Dry-run and live cycle both meet SLA with minimal interpretation drift. | Repeatable execution across teams without facilitator dependency. |
| R2M-15 Versioning and delta traceability | Rubric changes are undocumented or untraceable. | Version labels exist but no row-level impact mapping. | Diffs captured; impact and comparability partially missing. | Row-level diff and impact mapping required for each change. | Delta re-scoring performed for all impacted dimensions before promotion. | Version governance yields full comparability and auditable change lineage. |
| R2M-16 Audit reproducibility and assurance readiness | Assurance reviewer cannot reproduce conclusions. | Partial evidence available; key links mutable or inaccessible. | Most evidence reproducible; adjudication trail has gaps. | Assurance replay succeeds for sampled decisions. | Full replay succeeds with immutable evidence and complete trail. | Reproducibility passes independent assurance across two consecutive cycles. |

## 4) Role-specific anti-gaming checks (rubric-evaluation gaming risks)

1. Freeze scoring population denominators at cycle start; any mid-cycle denominator change requires R15 approval and dual reporting (`old` and `new`).
2. Require independent reviewer sign-off for every `90` or `100` anchor assignment.
3. Recompute at least 15% random sampled rows from raw evidence; variance above one anchor level invalidates sampled row scores.
4. Run one surprise contradiction challenge per cycle using injected conflicting evidence references.
5. Reject any evidence artifact whose creation timestamp is after decision cutoff for that cycle.
6. Detect anchor shopping by comparing reviewer draft anchors versus final anchors; undocumented upgrades are invalid.
7. Block weighted-average execution when any hard gate is active; prevent spreadsheet override of gate precedence.
8. Detect glossary drift by diffing canonical term definitions against prior approved version; unexplained drift triggers hold.
9. Compare exception renewal text to prior cycle; repeated copy-forward without new evidence is auto-rejected.
10. Require cross-tool scoring parity (reference calculator vs implementation calculator) before score publication.
11. Enforce reviewer independence: a scorer cannot independently validate their own high-anchor evidence.
12. Detect sampling bias: if sampled rows under-represent high scores by more than 10 percentage points, resample mandatory.
13. Track override rate; if manual overrides exceed 5% of scored rows, cycle enters inflation-risk review.
14. Publish inflation dashboard showing high-anchor density, evidence strength mix, and unresolved finding count trend.

## 5) Tripwires and hard-fail conditions (invalidate Rubric_0 scoring)

| ID | Condition | Detection method | Enforcement |
| --- | --- | --- | --- |
| R2-HF-01 | Any confirmed evidence fabrication, tampering, or provenance mismatch in Rubric_0 scoring package. | Forensic hash/provenance check and audit replay. | Invalidate Rubric_0 cycle score; set cycle result to `INVALID`; initiate investigation. |
| R2-HF-02 | Unresolved critical contradiction between Rubric_0 sections, gates, or role rules. | Contradiction register aging and severity review. | Invalidate scoring until contradiction closure evidence is accepted. |
| R2-HF-03 | Gate/tripwire precedence can be bypassed by arithmetic averaging in executed scoring workflow. | Scenario replay with active gate plus high section averages. | Invalidate published score and require scoring engine correction plus full recompute. |
| R2-HF-04 | Missing admissibility fields (`who/what/where/time/version`) for any non-zero scored row in sampled audit. | Evidence schema conformance scan on scored rows. | Invalidate affected dimension scores; if >5% rows impacted, invalidate full cycle. |
| R2-HF-05 | Independent replay cannot reproduce sampled scores within one anchor level and no justified rationale exists. | Blind replay audit of sampled rows. | Invalidate cycle and require replay remediation before rescoring. |
| R2-HF-06 | Any `90+` score lacks independent reviewer verification evidence. | High-anchor verification audit. | Downgrade to `50` for affected rows; if systemic (>3 rows), invalidate cycle. |
| R2-HF-07 | Rubric_0 version promoted without documented delta impact and re-evaluation report. | Version promotion gate audit. | Promotion void; previous approved version remains in force. |
| R2-HF-08 | Exception used to bypass mandatory anti-gaming control without authorized sign-off and expiry. | Exception ledger completeness check. | Invalidate cycle and open control-bypass incident. |
| R2-HF-09 | Cross-role handoff criteria materially conflict (e.g., incompatible SLA or acceptance conditions) and remain unresolved. | Handoff compatibility matrix review. | Invalidate role-layer scoring until adjudication record resolves conflict. |
| R2-HF-10 | Scoring model produces non-deterministic results across approved calculators from same inputs. | Dual-calculator parity test. | Invalidate score publication; require deterministic fix and recompute. |
| R2-HF-11 | Critical glossary term has conflicting definitions that change scoring interpretation. | Terminology drift and ambiguity audit. | Invalidate impacted sub-dimensions until canonical definition is restored and rescored. |
| R2-HF-12 | Reviewer independence breach (same individual authored evidence, scored row, and validated high anchor). | Reviewer role-separation audit. | Invalidate affected rows; repeat offenses invalidate full cycle. |

## 6) Cross-role dependencies and adjudication handoffs

| Counterparty role | Required input to R2 meta-evaluation | R2 handoff output | Acceptance criteria | SLA / cadence |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor | Risk appetite for rubric strictness, override policy boundaries | Recommendation to approve/hold Rubric_0 version | Signed decision with no open hard-fail | Per cycle close |
| R1 Product Manager | Operational usability feedback from rubric users | Clarified rubric flow and ambiguity resolutions | Top ambiguity defects resolved or accepted with due date | Weekly during cycle |
| R3 Engineering Manager | Execution friction data (time-to-score, rework loops) | Workflow simplification and tooling requirements | Dry-run cycle meets adjudication SLA | Bi-weekly |
| R5 QA/Test Engineer | Calibration variance and test protocol findings | Anchor/test rewrites for reproducibility | Calibration variance within approved tolerance | Every scoring cycle |
| R6 SRE/Platform | Reliability of scoring pipeline and evidence systems | Control requirements for scoring platform resilience | No unresolved Sev-1 scoring platform risk | Weekly operations review |
| R7 Security Architect | Integrity and tamper-resistance control requirements | Updated evidence integrity controls and exceptions | Mandatory integrity controls mapped with owner and due date | Monthly and pre-promotion |
| R8 Privacy/Compliance/Legal | Retention, access, and legal admissibility constraints | Compliance mapping for evidence handling rules | No unresolved high-severity legal/privacy gap | Monthly and release gate |
| R12 DevOps/Release Manager | Promotion workflow and tooling gate behavior | Deterministic scoring gate and release criteria | Promotion blocked automatically on active hard-fail | Per rubric version release |
| R15 Internal Audit/Assurance | Independent replay and assurance sampling outcomes | Remediation plan and closure evidence for assurance findings | Assurance replay passes without manual interpretation | Quarterly or on-demand |

Handoff rules:
1. Every handoff artifact must include `owner`, `decision timestamp`, `version`, and immutable evidence links.
2. Handoff state is binary: `accepted` or `returned`; silent acceptance is invalid.
3. Returned handoffs require defect class (`contradiction`, `evidence`, `determinism`, `interoperability`, `governance`) and resubmission deadline.
4. Two consecutive returned handoffs for the same defect class trigger mandatory R0 adjudication.

## 7) Cycle improvement checklist (improve Rubric_0 and re-evaluate deltas)

| Cycle phase | Improvement checklist item | Owner | Evidence artifact | Pass criterion |
| --- | --- | --- | --- | --- |
| Pre-cycle baseline | Freeze Rubric_0 version and scoring population definitions. | R2 + R12 | Version lock record and denominator manifest | No uncontrolled population drift in cycle |
| Pre-cycle baseline | Refresh canonical glossary and contradiction taxonomy. | R2 + R11 + R15 | Glossary diff and taxonomy approval record | Zero conflicting critical term definitions |
| Pre-cycle baseline | Reconfirm anti-gaming minimum controls and sample size plan. | R2 + R15 | Signed anti-gaming plan | All mandatory controls assigned with cadence |
| Calibration | Run cross-reviewer anchor calibration on 10 representative rows. | R2 + R5 | Calibration score spread report | Variance within agreed tolerance band |
| Calibration | Execute deterministic scoring parity test across calculators. | R2 + R12 | Parity test logs | 100% parity on test cases |
| Mid-cycle control | Perform random replay of at least 15% scored rows. | Independent reviewer + R2 observer | Replay audit log | >=95% sampled rows within one anchor level |
| Mid-cycle control | Run contradiction aging review and enforce closure SLA. | R2 + R15 | Contradiction aging dashboard | No unresolved critical contradiction past SLA |
| Mid-cycle control | Audit high-anchor (`90+`) evidence independence. | R15 + R2 | High-anchor verification report | 100% high anchors independently verified |
| Mid-cycle control | Audit exception renewals for copy-forward behavior. | R2 + R7 + R8 | Exception renewal diff report | Zero unsubstantiated renewals |
| Pre-close | Produce rubric delta impact map for changed rows. | R2 + R1 | Delta impact dossier | Every changed row mapped to impacted dimensions |
| Pre-close | Re-score only impacted rows, then full aggregate recompute. | R2 + R12 | Re-score worksheet and recompute log | Aggregate score traceable to row-level changes |
| Pre-close | Confirm no active hard-fail tripwire before publishing score. | R2 + R15 + R0 | Hard-fail clearance checklist | All hard-fails closed or cycle marked INVALID |
| Post-cycle learning | Publish defect backlog for Rubric_0 architecture improvements. | R2 + R3 | Prioritized remediation backlog | All critical defects have owner and due date |
| Post-cycle learning | Validate next-cycle comparability statement and baseline carry-forward. | R2 + R15 | Comparability statement | Historical trend remains interpretable after changes |


---

## R3 Engineering Manager

- source_file: `swarm_outputs/meta_rubric_role_expansions/R3_engineering_manager_rubric1.md`
- words: 3970
- lines: 143

# R3 Engineering Manager Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 evaluates the quality, rigor, anti-gaming strength, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 1) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R3 (Engineering Manager) evaluates whether Rubric_0 can drive predictable, evidence-based engineering governance decisions under real delivery pressure. The role is accountable for testing Rubric_0 for contradiction safety, replayability, score integrity, gate enforceability, and operational fit in recurring cycles.

### Decision rights
| Decision domain | R3 authority | Non-delegable rule | Escalation boundary |
| --- | --- | --- | --- |
| Rubric_0 operational readiness | Approve, conditionally approve, or reject Rubric_0 for cycle use | Cannot approve Rubric_0 if hard-fail conditions are active | Escalate to R0 and R15 within 1 business day |
| Gate and tripwire enforceability | Require correction when gate precedence or trigger logic is ambiguous | No scoring publication with unresolved gate ambiguity | Escalate to R12 and R7 for release-impacting defects |
| Evidence admissibility discipline | Enforce strict `who/what/where`, timestamp, provenance, and cutoff rules | No non-zero score without admissible evidence | Escalate to R15 for forensic review on tampering signs |
| Anchor reliability and calibration | Require anchor clarifications and calibration reruns | No score >75 if anchor interpretation drift is unresolved | Escalate to R1/R2 for semantic conflicts affecting product/architecture dimensions |
| Score integrity controls | Block publication if replay or recomputation checks fail | No score publication from non-replayable evidence | Escalate to R0 governance forum same cycle |
| Rubric change governance | Approve or reject Rubric_0 delta proposals for next cycle | No retroactive re-score without versioned reopen record | Escalate to R15 when change control breach is detected |
| Cross-role adjudication closure | Force accept/return decisions on handoffs with SLA | No silent handoff acceptance | Escalate to owning role lead after SLA breach |
| Corrective action closure verification | Accept only measurable remediation closure | No closure on checklist-only claims | Escalate overdue critical actions to R0 after 5 business days |

### Admissibility and scoring protocol for this meta-rubric
- Allowed anchors: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires explicit admissible evidence (`who/what/where`) captured before cycle cutoff.
- Any active hard-fail condition invalidates Rubric_0 scoring for the cycle.

## 2) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R3M-01 Decision-Coverage Completeness | Rubric_0 covers all Engineering Manager governance decision classes required to operate safely and predictably. | Build decision catalog (commitment, quality gate, incident learning, dependency, risk escalation, debt, staffing, release readiness). Pass if >=95% mapped to Rubric_0 clauses and 100% of safety-critical decisions mapped. | Who: R3 lead evaluator + R1 + R12 reviewer. What: decision-to-clause trace matrix with open gap log. Where: rubric review workbook and governance decision register. |
| R3M-02 Clause-to-Anchor Traceability Integrity | Every evaluable Rubric_0 clause is traceable to explicit anchors and scoring consequences. | Bidirectional trace check: clause -> anchor -> score row -> evidence requirement. Pass if orphan clauses = 0 and broken links = 0 in sampled and full scan. | Who: R3 evaluator + R15 reviewer. What: traceability matrix, link-validation report. Where: rubric schema repo and audit workpapers. |
| R3M-03 Contradiction Handling and Resolution Determinism | Rubric_0 resolves contradictory requirements with explicit precedence, owner, SLA, and scoring consequence. | Run contradiction scenarios (for example scope growth vs security gate, schedule vs quality gate). Pass if all scenarios produce deterministic outcome and unresolved critical contradictions aged >5 business days = 0. | Who: R3 + R2 + R7 adjudicators. What: contradiction register, precedence rules, resolution logs. Where: adjudication tracker and rubric governance minutes. |
| R3M-04 Evidence Admissibility Specificity | Rubric_0 defines admissible evidence precisely enough to block narrative-only scoring. | Sample non-zero rows. Pass if >=98% include complete who/what/where + timestamp + source provenance, and post-cutoff evidence is excluded from current-cycle scoring. | Who: R3 scorer + R5 evidence checker. What: admissibility checklist, cutoff log, exclusion list. Where: evidence vault and scoring ledger. |
| R3M-05 Evidence Replayability and Recompute Fidelity | Independent reviewers can replay Rubric_0 scores and recompute metrics from raw evidence. | Replay >=15% of scored rows including at least one from A1..A6 and role layer. Pass if score delta <=5 points and gate state matches 100% on sampled rows. | Who: independent scorer (non-author) + R15 witness. What: replay transcript, recomputation worksheet, variance report. Where: immutable artifacts store and replay runbook repo. |
| R3M-06 Anchor Separability and Monotonicity | Anchor levels are behaviorally distinct, non-overlapping, and logically increasing in rigor. | Anchor lint + blind rater test. Pass if adjacent-anchor disagreement due to ambiguity <=20% and no reverse-monotonic rules detected. | Who: R3 calibration facilitator + cross-role raters. What: anchor ambiguity log, calibration results. Where: calibration deck and scoring QA workspace. |
| R3M-07 Hard-Gate and Tripwire Coherence | Rubric_0 gate/tripwire logic is complete, precedence-ordered, and impossible to bypass silently. | Simulate G1..G6 and RG1..RG4 plus role tripwires. Pass if every triggered hard gate forces fail/invalid outcome and precedence path is deterministic. | Who: R3 + R12 + R7 control reviewers. What: gate simulation matrix, precedence map, bypass test logs. Where: governance test harness and release control records. |
| R3M-08 Weighting and Aggregation Robustness | Scoring math produces stable outcomes aligned to risk, without masking critical weakness. | Recompute weighted scores from raw row values. Run sensitivity test where high-risk dimensions degrade. Pass if formulas reconcile exactly and masking test fails by design (cannot hide critical failure). | Who: R3 + finance/analytics reviewer + R15. What: aggregation formula sheet, sensitivity analysis, reconciliation logs. Where: scoring workbook and audit archive. |
| R3M-09 Anti-Gaming Protocol Executability | Rubric_0 anti-gaming controls are explicit, runnable each cycle, and evidenced. | Verify execution of mandatory controls: sampling, surprise challenge, raw-log recompute, backfill exclusion, contradiction aging, provenance checks. Pass only if all required controls executed. | Who: R3 owner + R15 observer. What: anti-gaming execution checklist, sample results, challenge outputs. Where: anti-gaming run log and governance portal. |
| R3M-10 Score Inflation Resistance | Rubric_0 structurally resists inflated scoring via weak evidence, lenient anchors, or denominator manipulation. | Enforce high-score guardrails: >75 requires independent corroboration; >90 requires successful challenge test. Check distribution drift; any >15-point jump must have approved delta rationale. | Who: R3 scorer + R15 validator. What: high-score evidence pack, distribution analysis, jump-justification approvals. Where: scoring history database and audit dashboard. |
| R3M-11 Inter-Rater Reliability and Calibration Strength | Different qualified scorers produce consistent Rubric_0 outcomes from identical evidence. | Dual-score common packet each cycle. Pass if median variance <=10 points, gate decisions agree 100%, and unresolved scorer disputes aged >5 business days = 0. | Who: two independent scorers + R3 calibration owner. What: dual-score comparison, dispute log, calibration actions. Where: scorer workspace and adjudication register. |
| R3M-12 Operational Throughput and Evaluator Load | Rubric_0 can be executed within delivery cadence without creating decision latency or process failure. | Time-box dry run + live cycle. Pass if scoring completes within 5 business days after cutoff, first-pass completion >=90%, and release-decision backlog due to rubric latency = 0. | Who: R3 + R12 + PMO coordinator. What: cycle timing report, rework log, pending-decision dashboard. Where: governance calendar and cycle close report. |
| R3M-13 Exception Governance and Expiry Enforcement | Rubric_0 exception paths are controlled, temporary, and auditable. | Sample exception records. Pass if each has owner, rationale, compensating control, expiry, and renewal evidence; active expired exceptions = 0. | Who: R3 + risk owner + R15. What: exception register, expiry audit, compensating-control tests. Where: GRC system and exception evidence store. |
| R3M-14 Versioning and Change-Control Integrity | Rubric_0 updates are versioned, approved, impact-assessed, and non-retroactive by default. | Check that each rubric change has diff, impact analysis, effective date, approvers, and reopen record if rescoring occurred. Pass if unauthorized edits = 0. | Who: R3 rubric owner + R11 doc owner + R15. What: version history, change requests, impact assessments. Where: rubric repository and governance change log. |
| R3M-15 Cross-Role Handoff Operability | Rubric_0 defines usable handoffs for scoring and adjudication across roles. | Measure handoff quality. Pass if >=90% first-pass acceptance, all returns include defect class and due date, and silent acceptance count = 0. | Who: R3 + counterpart role leads (R1/R2/R5/R6/R7/R8/R12/R15). What: handoff records, return reasons, SLA tracker. Where: adjudication board and handoff ledger. |
| R3M-16 Remediation Actionability and Delta Re-evaluation | Rubric_0 findings produce actionable fixes and measurable next-cycle improvement. | Pass if >=90% actions have owner/date/verification metric, on-time closure >=90%, and post-change delta re-score is executed on impacted rows plus gate recheck. | Who: R3 remediation owner + R0 sponsor + R15 verifier. What: action tracker, closure evidence, delta re-score report. Where: remediation register and cycle close package. |

## 3) Anchor table (0/25/50/75/90/100) for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R3M-01 Decision-Coverage Completeness | No decision coverage map exists. | Partial map exists; critical decision classes missing. | Most classes mapped; at least one safety-critical gap remains. | >=95% mapped and all safety-critical classes covered. | Independent review confirms coverage and closes all critical gaps within SLA. | Two consecutive cycles with zero critical coverage gaps. |
| R3M-02 Clause-to-Anchor Traceability Integrity | Clauses cannot be traced to anchors or score rows. | One-way mapping only; many orphan clauses. | Bidirectional mapping exists but orphan/broken links remain. | Full bidirectional mapping with orphan and broken links at 0. | Independent replay confirms sampled scores trace end-to-end. | Two cycles with zero traceability defects in audit sample. |
| R3M-03 Contradiction Handling and Resolution Determinism | Contradictions are ignored or handled ad hoc. | Contradictions logged but no precedence or SLA exists. | Precedence exists but outcomes vary by reviewer. | Deterministic protocol with owner/SLA is operating. | Independent scenario tests produce consistent outcomes. | Two cycles with no aged critical contradictions and full replayable resolution logs. |
| R3M-04 Evidence Admissibility Specificity | Evidence rules are absent; narrative claims accepted. | Rules exist but who/what/where or cutoff criteria are vague. | Rules defined, enforcement inconsistent, and exceptions undocumented. | Admissibility is explicit and consistently enforced for sampled rows. | All sampled non-zero scores have complete admissible evidence; invalid evidence auto-zeroed. | Two cycles with zero admissibility breaches under independent audit. |
| R3M-05 Evidence Replayability and Recompute Fidelity | Scores cannot be replayed from stored evidence. | Partial replay possible; major score/gate mismatches common. | Replay works for some rows; recomputation variance exceeds tolerance. | >=90% sampled replay success with <=5 point variance and matching gates. | >=95% sampled replay success and recomputed metrics match tolerances. | Two independent teams replay sampled critical rows with identical gate outcomes. |
| R3M-06 Anchor Separability and Monotonicity | Anchors are vague, overlapping, and non-operational. | Anchor text differs cosmetically but remains non-testable. | Anchors are partly testable; adjacent overlap still frequent. | Anchors are behaviorally distinct with observable pass tests. | Blind-rater calibration shows strong agreement and low ambiguity drift. | Two cycles with stable interpretation and no monotonicity defects. |
| R3M-07 Hard-Gate and Tripwire Coherence | Gate logic conflicts or is bypassable. | Gates listed but precedence and trigger consequences unclear. | Most gates function, but simulation finds bypass paths. | Full gate/tripwire precedence works across defined scenarios. | No pass possible with active hard gate; controls verified independently. | Two cycles with zero gate-bypass findings, including red-team tests. |
| R3M-08 Weighting and Aggregation Robustness | Aggregation formula undefined or incorrect. | Formula exists but weights inconsistent or non-reproducible. | Weights sum correctly but sensitivity risks are not tested. | Formulas reconcile exactly and weighting rationale is documented. | Sensitivity tests confirm high-risk weakness cannot be masked. | Multi-cycle recomputation always matches published score without unexplained drift. |
| R3M-09 Anti-Gaming Protocol Executability | Anti-gaming controls absent. | Controls documented but not executed reliably. | Partial execution with missing mandatory checks. | All mandatory anti-gaming checks executed with evidence. | Red-team detection rate is high and corrective actions are timely. | Two cycles with sustained detection performance and no skipped mandatory checks. |
| R3M-10 Score Inflation Resistance | Rubric permits unsupported high scores. | Caps exist on paper but are frequently bypassed. | High-score checks exist with inconsistent enforcement. | >75 and >90 guardrails enforced consistently. | Distribution and jump analysis catches and corrects inflation attempts. | Two cycles with zero unsupported high-score outcomes. |
| R3M-11 Inter-Rater Reliability and Calibration Strength | Single-rater process only; no calibration. | Multiple raters used ad hoc with frequent unresolved disagreement. | Dual scoring present but variance is high or persistent. | Variance <=10 and gate agreement is complete after calibration. | Drift trends decrease and dispute aging remains within SLA. | Two cycles with stable high reliability and zero unresolved gate disagreement. |
| R3M-12 Operational Throughput and Evaluator Load | Rubric execution misses decision windows routinely. | Process runs but often late and rework-heavy. | Timeliness is mixed; cycle pressure causes scoring debt. | Scoring completes within SLA with manageable rework. | First-pass completion is high and release decisions are not delayed by rubric process. | Sustained on-time execution across high-load cycles without quality loss. |
| R3M-13 Exception Governance and Expiry Enforcement | Exceptions are informal, ownerless, or perpetual. | Exceptions logged without expiry or compensating controls. | Ownership/expiry defined, but overdue exceptions persist. | Full lifecycle governance with expiry enforcement is operating. | No active expired exceptions; renewals are justified with fresh evidence. | Two cycles with declining exception volume and zero unauthorized renewal. |
| R3M-14 Versioning and Change-Control Integrity | Rubric changes are uncontrolled and untraceable. | Versions exist but impact and approval records are missing. | Change control exists; occasional retroactive edits occur. | Versioned, approved, impact-assessed changes with effective dates are standard. | Delta testing and dependency rechecks run for each approved change. | Two cycles with zero unauthorized edits and complete audit trail. |
| R3M-15 Cross-Role Handoff Operability | Handoffs are undefined or unusable. | Roles identified but no acceptance criteria or SLA. | Templates exist; return loops and silent acceptance are common. | Handoffs meet >=90% first-pass acceptance with explicit return reasons. | SLA compliance is strong and defect classes are tracked to closure. | Two cycles with stable low-friction adjudication and minimal escalation. |
| R3M-16 Remediation Actionability and Delta Re-evaluation | Findings do not result in concrete actions. | Actions listed without owners, dates, or verification metrics. | Action plans exist but closure timeliness and delta re-score are inconsistent. | SMART actions with high closure rate and required delta re-score are standard. | Closed actions show measurable rubric-quality improvement on re-score. | Two cycles with sustained improvement and no repeated critical defect class. |

## 4) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Baseline freeze check: hash Rubric_0 version and scoring template at cycle start; reject scoring against un-hashed variants.
2. Anchor cherry-pick check: if evidence satisfies only lower anchors but scorer assigns higher anchor, flag and require adjudication.
3. Orphan-row check: auto-scan for scored rows with no clause ID or no required evidence field.
4. Backfill exclusion check: reject evidence created after cutoff unless cycle is formally reopened.
5. Time-sequence check: ensure chronology `evidence capture -> scoring -> approval`; out-of-order records are inadmissible.
6. Recompute check: independently recompute sampled metrics from raw logs; dashboard-only evidence is insufficient.
7. High-score corroboration check: scores >75 require independent reviewer evidence; >90 require challenge-test evidence in same cycle.
8. Denominator governance check: detect denominator narrowing that inflates rates (for example excluding failed rows without approved rule).
9. Weight-tamper check: detect mid-cycle weight changes or silent normalization changes; force invalidation on unauthorized edits.
10. Gate bypass simulation: execute synthetic failing scenarios to confirm hard gates still block pass outcomes.
11. Reviewer-collusion control: rotate at least one scorer/reviewer each cycle for sampled rows.
12. Contradiction aging check: unresolved critical contradiction beyond SLA auto-triggers tripwire.
13. Exception laundering check: repeated short renewals for same exception require executive re-approval.
14. Appeal abuse check: repeated score appeals without new evidence are logged and excluded from score changes.

## 5) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (caps and mandatory remediation)
| ID | Trigger condition | Immediate effect |
| --- | --- | --- |
| R3M-TW-01 | Replay variance >5 points on >10% sampled rows | Cap R3M-05 at `50`; mandatory replay root-cause analysis |
| R3M-TW-02 | Any critical contradiction unresolved >5 business days | Cap R3M-03 at `50`; freeze publication until adjudicated |
| R3M-TW-03 | Any mandatory anti-gaming control not executed in cycle | Cap R3M-09 at `25`; no sub-dimension may score above `90` |
| R3M-TW-04 | Any >75 score lacks independent corroboration evidence | Cap R3M-10 at `25`; re-score affected rows |
| R3M-TW-05 | First-pass cross-role handoff acceptance <80% | Cap R3M-15 at `50`; require handoff contract correction |
| R3M-TW-06 | Scoring cycle misses SLA by >2 business days | Cap R3M-12 at `50`; trigger throughput remediation plan |

### Hard-fail conditions (Rubric_0 score invalid for cycle)
| ID | Hard-fail condition | Evidence test | Effect |
| --- | --- | --- | --- |
| R3M-HF-01 | Evidence fabrication, tampering, or backdated approval | Hash/timestamp/immutability mismatch | Mark Rubric_0 cycle result as `INVALID`; mandatory forensic review |
| R3M-HF-02 | Published score ignores any active global hard gate (G1..G6) or role gate (RG1..RG4) | Gate-state log contradicts published decision | `INVALID`; all downstream decisions blocked until re-run |
| R3M-HF-03 | Final score cannot be reproduced from immutable evidence package | Independent replay fails on critical sample | `INVALID`; full-cycle re-scoring required |
| R3M-HF-04 | Unauthorized rubric version/weight/anchor change after cutoff affects scoring | Version diff without approved change record | `INVALID`; revert to approved baseline and re-score |
| R3M-HF-05 | Active unresolved critical contradiction at publication time | Contradiction register shows open critical item | `INVALID`; adjudication closure required before publication |
| R3M-HF-06 | >10% of non-zero scored rows lack required who/what/where evidence | Admissibility audit sample extrapolation | `INVALID`; evidence remediation + re-score |
| R3M-HF-07 | Post-cutoff evidence used to increase current-cycle score without formal reopen record | Cutoff audit and reopen log mismatch | `INVALID`; score rollback to pre-cutoff state |
| R3M-HF-08 | Expired exception used to bypass gate or retain score credit | Exception register vs scoring decision mismatch | `INVALID`; exception governance breach escalation |

## 6) Cross-role dependencies and adjudication handoffs

| Counterpart role | Dependency into R3 meta-evaluation | R3 handoff / adjudication output | Acceptance criteria | SLA / escalation |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor | Risk appetite, governance charter, and approval authority boundaries | Rubric_0 readiness verdict (`approve/conditional/reject`) with hard-fail status | Decision and residual risks explicitly recorded | Escalate in 1 business day for unresolved critical governance defects |
| R1 Product Manager | Problem/KPI/scope governance expectations to test rubric completeness | Coverage-gap report for A1/A2 and role-layer product interactions | No unresolved critical coverage gap for PM-related controls | Escalate in 2 business days on unresolved contradiction |
| R2 Product Architect | Architecture/NFR contradiction scenarios for deterministic resolution tests | Contradiction adjudication outcomes and precedence corrections | Scenario outcomes deterministic and reproducible | Escalate in 2 business days on critical design-rule conflict |
| R5 QA / Test Engineer | Evidence admissibility and replay test design support | Evidence integrity verdict and replay variance report | Replay sample passes tolerance and admissibility completeness | Escalate same cycle if replay fails threshold |
| R6 SRE / Platform | Reliability gate realism and operational cadence constraints | Operability feedback on rubric throughput and gate enforceability | Rubric process does not delay critical runtime decisions | Escalate within 24 hours on release-impacting delay risk |
| R7 Security | Security/privacy hard-gate correctness and non-bypass checks | Gate coherence findings for security-critical controls | No pass path with active security hard gate | Escalate immediately for gate bypass vulnerability |
| R8 Privacy/Compliance/Legal | Obligation-to-control mapping and legal cutoff constraints | Compliance admissibility and contradiction resolution decisions | Mandatory obligations mapped and contradiction-free | Escalate within 1 business day on legal blocking issue |
| R12 DevOps/Release Manager | Release control evidence, gate logs, and decision timestamps | Publication authorization recommendation for rubric score package | Full evidence chain and gate-state consistency | Escalate same day if approval-chain or timestamp integrity fails |
| R15 Internal Audit/Assurance | Independent assurance sampling, forensic checks, and dispute arbitration | Independent assurance memo and final adjudication disposition | Audit replay and integrity checks pass with no material exception | Escalate immediately on tampering/independence breach |

Adjudication rule: each handoff is explicitly marked `accepted` or `returned`. Silent acceptance is invalid. Returned handoffs must include defect class, owner, due date, and resubmission timestamp.

## 7) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle point | Checklist item | Evidence artifact | Pass criterion |
| --- | --- | --- | --- |
| Pre-cycle baseline | Freeze Rubric_0 version, weights, anchors, and gate definitions. | Baseline hash manifest and approval record. | 100% scoring uses frozen baseline. |
| Pre-cycle baseline | Refresh decision-coverage matrix and open-gap register. | Updated coverage map and gap log. | No unresolved critical coverage gaps. |
| Pre-cycle baseline | Refresh contradiction catalog and precedence rules. | Contradiction register with owner/SLA fields. | Critical contradictions open at start = 0. |
| Pre-cycle baseline | Reconfirm evidence admissibility schema and cutoff timestamp. | Admissibility schema version + cutoff notice. | Schema fields complete and approved before scoring start. |
| Calibration prep | Run anchor ambiguity lint and resolve vague terms. | Anchor lint report and approved wording changes. | Zero unresolved high-severity ambiguity findings. |
| Calibration prep | Execute dual-rater calibration on common evidence pack. | Calibration results and variance analysis. | Median variance <=10; gate agreement 100%. |
| Anti-gaming run | Execute mandatory anti-gaming protocol and red-team scenarios. | Anti-gaming checklist, challenge outputs, closure actions. | All mandatory checks executed and evidenced. |
| Scoring execution | Complete scoring within cycle SLA using admissible evidence only. | Time log, scoring ledger, admissibility audit sample. | Scoring closed <=5 business days after cutoff. |
| Adjudication | Resolve returns/disputes with explicit accept/return decisions. | Handoff ledger and dispute resolution records. | Silent acceptance count = 0; all returns classified. |
| Publication gate | Apply tripwires and hard-fail checks before publishing result. | Tripwire/hard-fail evaluation report. | No publication if any hard-fail active. |
| Post-cycle improvement | Convert all failed checks into SMART remediation actions. | Remediation action register with owners/dates/metrics. | 100% failed checks have owner and due date. |
| Delta implementation | Apply approved Rubric_0 changes with versioned diffs. | Change requests, diffs, impact assessments, approvals. | Unauthorized edits = 0. |
| Delta re-evaluation | Re-score impacted sub-dimensions and rerun gate coherence tests. | Delta re-score report and gate simulation results. | All impacted rows re-evaluated; no new critical contradiction. |
| Cycle close | Publish cycle retrospective with trend metrics and carryover risks. | Retrospective report and next-cycle risk register. | Closure approved by R3 and R15 with tracked carryovers. |


---

## R4 Software Engineer

- source_file: `swarm_outputs/meta_rubric_role_expansions/R4_software_engineer_rubric1.md`
- words: 4502
- lines: 143

# R4 Software Engineer Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

## 2) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R4 meta-evaluation determines whether Rubric_0 is technically executable as an engineering control system: precise enough to produce consistent software-quality decisions, strict enough to resist score inflation, and operational enough to run on release cadence. This rubric evaluates Rubric_0 design quality only, not project artifact quality.

### Decision rights (R4 meta-evaluator)
| Decision area | R4 authority | Non-delegable boundary | Required co-signers | Required decision evidence |
| --- | --- | --- | --- | --- |
| R4 criteria quality gate | Accept/hold Rubric_0 for engineering decision use | Cannot accept ambiguous, non-falsifiable engineering criteria | R2, R5 | Criteria lint report, ambiguity log, approved remediation record |
| Traceability model integrity | Final recommendation on trace-chain adequacy for engineering scoring | Cannot waive missing critical trace stages | R1, R15 | Trace-chain conformance matrix, sampled reverse-trace results |
| Replayability readiness | Approve/hold use of Rubric_0 scores for release governance | Cannot approve non-replayable high anchors | R12, R15 | Independent replay transcript, recompute parity report |
| Contradiction protocol operability | Require updates to contradiction taxonomy/SLA/enforcement | Cannot close unresolved Severity-1 contradiction by narrative justification | R2, R7, R8 | Contradiction aging dashboard, closure evidence pack |
| Gate precedence integrity | Validate that hard gates override averages deterministically | Cannot allow arithmetic bypass of hard gates | R12, R15 | Scenario replay outputs, precedence rule tests |
| Anti-gaming sufficiency | Require anti-gaming controls and challenge tests before cycle close | Cannot permit 90/100 scoring when required controls are skipped | R7, R15 | Anti-gaming execution ledger, challenge outcomes |
| High-anchor approval | Recommend approval of 90/100 assignments in role-layer scoring | Cannot approve 90/100 without independent evidence and replay | R15 | High-anchor evidence packet, reviewer independence attestation |
| Rubric version promotion | Recommend promotion/rollback of Rubric_0 revisions | Cannot promote without row-level delta impact and re-score evidence | R0, R1, R2 | Diff map, delta re-score report, comparability note |

### Meta-scoring admissibility rules
- Anchor set is fixed: `0/25/50/75/90/100`.
- Any non-zero score requires explicit `who/what/where` evidence.
- No sub-dimension may exceed `50` without replayable evidence artifacts.
- No sub-dimension may exceed `75` without independent reviewer evidence.
- No sub-dimension may exceed `90` without adversarial challenge evidence from the same cycle.
- Evidence created after cycle cutoff is excluded from that cycle unless formal waiver exists.

## 3) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R4M-01 Engineering concern coverage completeness | Rubric_0 covers all mandatory software-engineering quality concerns with no material omission. | Map Rubric_0 R4 concerns against canonical set (correctness, modularity, testing/oracles, failure handling, performance/efficiency, security/supply-chain, observability/diagnostics, data integrity, CI/CD safety): coverage must be 100%; conflicting duplicate concern definitions = 0. | Who: R4 meta-evaluator + R2 counterpart. What: concern-to-row coverage matrix and duplication diff. Where: `rubrics/Rubric_0_Comprehensive_N6_Swarm.md`, `rubrics/Rubric_0_Role_Expansion_Pack_N16.md`, role index workbook. |
| R4M-02 Role boundary and ownership clarity | Rubric_0 clearly separates R4 responsibilities from adjacent roles and defines ownership. | Sample 30 engineering-relevant rows; each row must have one accountable role and explicit handoff path to R5/R6/R7/R8/R12 when applicable; unresolved ownership conflicts = 0. | Who: R4 + R3 governance reviewer. What: ownership lint report and handoff conflict log. Where: role layer tables and role expansion pack handoff sections. |
| R4M-03 Trace-chain specification quality | Rubric_0 defines an enforceable requirement-to-release trace chain for engineering decisions. | Verify trace chain stages are explicitly defined and measurable (`source->requirement->spec/design->implementation->verification->release`); critical-chain completeness threshold and orphan/ghost controls are explicit; any missing critical-stage rule fails test. | Who: R4 + R1 + R15. What: trace-rule conformance checklist and sampled reverse-trace results. Where: A2 definitions/matrix and role-layer scoring protocol. |
| R4M-04 Correctness criteria falsifiability | Rubric_0 correctness criteria are testable and resistant to narrative pass claims. | For correctness-related rows, verify explicit pass/fail thresholds, edge-condition requirements, and reproducible defect metrics; at least one falsification test exists per row. | Who: R4 + R5. What: correctness row audit sheet and falsification method register. Where: R4 role expansion rows and A3 scoring tables. |
| R4M-05 Risk-based test and oracle rigor design | Rubric_0 demands test depth proportional to risk and requires strong oracle semantics. | Verify rubric text enforces risk-to-test mapping, positive/negative/error-path coverage, and oracle quality checks (not just execution pass rate); seeded-defect or mutation-style strength check is specified for high-risk scope. | Who: R4 + R5. What: test-rigor criteria matrix and oracle rule audit. Where: R4 and R5 role expansion sections, A3 verification criteria. |
| R4M-06 Failure-mode and recovery evaluation depth | Rubric_0 includes explicit engineering checks for error handling, degradation, and recovery. | Confirm criteria include timeout/retry/backoff/fallback expectations, fault-injection or failure simulation, and recovery success measures (RTO/RPO or equivalent); untested recovery claims must be disallowed from high anchors. | Who: R4 + R6. What: failure-mode criteria checklist and recovery-gate review notes. Where: R4 role rows, architecture resilience rows, and reliability sections. |
| R4M-07 Security and supply-chain control coverage | Rubric_0 engineering rules cover code security and dependency integrity with enforceable consequences. | Confirm explicit criteria for secure coding, secret handling, dependency/SBOM hygiene, signature/provenance checks, and CVE remediation timeliness; at least one hard consequence exists for unresolved critical control failure. | Who: R4 + R7. What: security-control coverage map and consequence linkage table. Where: R4 security/supply-chain rows, A4/A6 control sections. |
| R4M-08 Observability and diagnostics evaluation adequacy | Rubric_0 requires telemetry and diagnostics sufficient for engineering incident response. | Verify criteria require logs/metrics/traces for critical paths, measurable coverage thresholds, and operability hooks (correlation IDs, health diagnostics); incident replay detectability requirement must be explicit. | Who: R4 + R6 + R13 reviewer. What: observability criteria audit and drill-evidence mapping. Where: R4 observability/diagnostics rows and reliability/operations sections. |
| R4M-09 Data integrity and migration safety criteria quality | Rubric_0 has enforceable checks for schema/data changes and rollback safety. | Confirm migration/reconciliation/rollback criteria include measurable thresholds and explicit tripwire effect for corruption risk; verify data integrity controls are linked to evidence requirements. | Who: R4 + data engineering reviewer + R15. What: migration-safety rule audit and tripwire linkage proof. Where: R4 data integrity row, A2 data/spec rows, tripwire catalog. |
| R4M-10 CI/CD gate and rollback governance executability | Rubric_0 encodes deterministic release-gate behavior for engineering quality controls. | Verify mandatory gate list, bypass policy, and rollback readiness checks are explicit; scenario replay with active gate failure must produce deterministic block outcome every time. | Who: R4 + R12. What: gate precedence scenario results and bypass-control audit. Where: global/role gate sections, release governance rows. |
| R4M-11 Evidence admissibility and provenance enforcement | Rubric_0 evidence rules are concrete enough to prevent unverifiable scoring. | Confirm non-zero scoring requires `who/what/where` and provenance fields (`time/version/hash` or equivalent); screenshots-only evidence is inadmissible unless paired with source export; completeness/freshness thresholds are explicit. | Who: R4 + R15. What: evidence schema conformance report and inadmissibility exceptions log. Where: role scoring protocol, required evidence package, evidence threshold section. |
| R4M-12 Independent replay and recompute determinism | Rubric_0 scores can be replayed and recomputed consistently by non-authors. | Independent replay on sampled rows reproduces anchors exactly; aggregate recompute variance must be zero under same inputs; metric reconstruction tolerance policy is explicit and enforced. | Who: independent reviewer + R4 observer + R15. What: replay transcript, recomputation worksheet, variance ledger. Where: evidence vault, scoring model workbook, calibration log. |
| R4M-13 Contradiction protocol strength | Rubric_0 contradiction handling is complete, timely, and enforceable. | Verify contradiction taxonomy, severity levels, precedence rules, owners, and SLA are explicit; unresolved Severity-1 contradiction must trigger release/scoring fail without override loophole. | Who: R4 + R2 + R8 + R15. What: contradiction protocol conformance audit and aging report. Where: contradiction protocol tables and adjudication records. |
| R4M-14 Anchor monotonicity and discrimination strength | Rubric_0 anchors distinguish quality levels behaviorally and prevent anchor jumping. | For every scored row, verify anchors 0/25/50/75/90/100 are all present, observable, and strictly increasing in evidence burden; any inversion or overlap that enables unsupported jump is logged as defect. | Who: R4 + R5 calibration lead. What: anchor lint output and calibration disagreement report. Where: all anchor tables in Rubric_0 and role pack. |
| R4M-15 Aggregation and gate-precedence determinism | Rubric_0 scoring math yields one outcome after caps, gates, and overrides. | Two independent calculators must return identical totals from same row inputs; precedence order (`row caps -> role gates -> global gates`) must produce deterministic final verdict in scenario tests. | Who: R4 + R12 + R15. What: dual-calculator parity report and precedence test harness output. Where: scoring formula spec, gating rules, adjudication simulation archive. |
| R4M-16 Score inflation resistance and high-anchor guardrails | Rubric_0 prevents unjustified high scores in engineering-relevant dimensions. | Verify >75 requires independent evidence; >90 requires replay/adversarial validation; cycle-level high-anchor density anomaly triggers mandatory resample and justification. | Who: R4 + R15 + R0 observer. What: high-anchor audit, distribution dashboard, exception justifications. Where: role scorecards, anti-gaming records, calibration minutes. |
| R4M-17 Cross-role interface consistency and handoff testability | Rubric_0 defines interoperable handoffs for engineering-related adjudication. | For R4 handoffs (R1/R2/R5/R6/R7/R8/R12/R15), verify each has trigger, required artifact set, acceptance criteria, and SLA; sampled handoff acceptance rate >=90% without re-interpretation loops. | Who: R4 + counterpart role owners. What: handoff compatibility matrix and return/rework log. Where: role expansion pack cross-role tables and adjudication workflow logs. |
| R4M-18 Versioning, delta re-scoring, and cadence fit | Rubric_0 updates are controlled, impact-assessed, and operationally executable on cycle cadence. | Each rubric change must include row-level diff and expected scoring impact; impacted rows must be re-scored with explained deltas; review cycle SLA adherence must meet governance targets. | Who: R4 rubric owner + R1 + R15. What: version diff dossier, delta re-score packet, cycle timing report. Where: rubric repo history, change-control records, cycle tracker. |

## 4) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R4M-01 Engineering concern coverage completeness | Major engineering concerns are missing from Rubric_0. | Concern list exists but omits multiple mandatory areas or duplicates conflict. | Most concerns present; at least one mandatory concern is weakly specified or duplicated inconsistently. | All mandatory concerns are covered once with clear mapping and no material omission. | Independent audit confirms complete, non-conflicting coverage. | Two consecutive cycles maintain full coverage with zero material omission findings. |
| R4M-02 Role boundary and ownership clarity | R4 scope is undefined or conflicts heavily with other roles. | Boundaries are named but ownership/escalation rules are mostly absent. | Boundaries exist but sampled rows show recurring ownership ambiguity. | R4 boundaries and escalation paths are explicit and operational in sampled rows. | Cross-role review confirms minimal ownership conflict and low handoff rework. | Two cycles with zero unresolved critical ownership conflicts in R4-related rows. |
| R4M-03 Trace-chain specification quality | No enforceable trace-chain model exists. | Trace terms are present but chain stages and thresholds are undefined. | Chain stages are defined, but critical thresholds/orphan/ghost handling are incomplete. | Full chain and threshold logic are explicit and enforceable for critical scope. | Independent reverse-trace sampling validates chain executability with only minor defects. | Two cycles with complete critical-chain conformance and no unresolved ghost/orphan critical defects. |
| R4M-04 Correctness criteria falsifiability | Correctness is judged by narrative only. | Some tests exist, but pass/fail conditions are mostly subjective. | Core pass/fail checks exist; edge-case or falsification rules are weak. | Correctness criteria are measurable, falsifiable, and include edge conditions. | Independent challenge tests confirm correctness rules reject weak evidence. | Two cycles with stable correctness scoring and no major falsifiability defect in audits. |
| R4M-05 Risk-based test and oracle rigor design | Rubric_0 does not require risk-based testing or meaningful oracles. | Testing is mostly happy-path and oracle semantics are ambiguous. | Risk mapping exists but high-risk coverage and oracle strength checks are uneven. | Risk-based depth and oracle quality rules are explicit for critical scope. | Independent review validates strong oracle design and high-risk test expectations. | Two cycles with no critical rubric-audit finding for risk-test/oracle insufficiency. |
| R4M-06 Failure-mode and recovery evaluation depth | Failure/recovery criteria are absent. | Error/recovery mentioned but no measurable requirements exist. | Some measurable failure checks exist; recovery validation remains incomplete. | Failure-mode, degradation, and recovery criteria are operational and testable. | Fault-injection and recovery challenge evidence supports high-confidence scoring. | Two cycles with complete failure/recovery rubric controls and no critical gap findings. |
| R4M-07 Security and supply-chain control coverage | Security/supply-chain controls are missing or non-enforceable. | Controls listed but lack measurable thresholds or consequences. | Controls mostly present; enforcement of critical violations is inconsistent. | Controls and consequences are explicit for secure coding and dependency integrity. | Independent security audit confirms enforceable high-severity control logic. | Two cycles with zero critical control-coverage defect in Rubric_0 audits. |
| R4M-08 Observability and diagnostics evaluation adequacy | Rubric_0 allows scoring without telemetry/diagnostics requirements. | Basic telemetry expectations exist but are vague and non-measurable. | Measurable telemetry rules exist; diagnostics or incident-detectability checks are partial. | Telemetry and diagnostics requirements are measurable and operationally sufficient. | Independent drill-based review confirms criteria are decision-usable. | Two cycles with no critical observability-criteria deficiency in meta-audits. |
| R4M-09 Data integrity and migration safety criteria quality | Data/migration safety is not governed by Rubric_0. | Data safety is mentioned but lacks measurable gating or tripwires. | Migration and rollback checks exist but integrity thresholds or consequences are weak. | Data integrity and migration rules are measurable with explicit fail conditions. | Independent replay of migration criteria shows deterministic gate behavior. | Two cycles with zero unresolved critical data-safety rubric defect. |
| R4M-10 CI/CD gate and rollback governance executability | Gate logic is absent or bypassable by averaging. | Gates are defined but ambiguous; bypass and rollback rules are weak. | Gate set is mostly explicit; edge-case precedence still requires manual interpretation. | Gate and rollback governance are explicit and consistently executable. | Independent scenario replay shows no bypass path for mandatory failed gates. | Two cycles with deterministic gate enforcement and zero unresolved precedence disputes. |
| R4M-11 Evidence admissibility and provenance enforcement | Non-zero scores can be assigned without admissible evidence. | Evidence rules exist but provenance/admissibility fields are often missing. | Evidence schema mostly defined; enforcement gaps remain in sampling. | Evidence admissibility is explicit and enforced for non-zero scoring. | Independent audit confirms low evidence-defect rate and effective inadmissibility controls. | Two cycles with zero unsupported non-zero scores in sampled engineering-relevant rows. |
| R4M-12 Independent replay and recompute determinism | Scores cannot be replayed or recomputed from evidence. | Partial replay possible only with author interpretation. | Most rows replay; aggregate recomputation still shows unexplained variance. | Independent replay and recompute are consistent for sampled rows and totals. | Adversarial replay by non-author reviewers reproduces outcomes with no material variance. | Two cycles with full replay parity and deterministic recomputation across toolchains. |
| R4M-13 Contradiction protocol strength | No contradiction protocol or severity handling exists. | Contradictions are tracked ad hoc without SLA/authority rules. | Protocol exists but Severity-1 closure and enforcement are inconsistent. | Severity, SLA, authority, and closure evidence requirements are operational. | Independent adjudication confirms unresolved Severity-1 contradictions block scoring/release. | Two cycles with zero Severity-1 contradiction carried past SLA into published scores. |
| R4M-14 Anchor monotonicity and discrimination strength | Anchors are missing or indistinguishable. | Anchors exist but are mostly narrative and overlap heavily. | Anchors are partially measurable; multiple rows still allow subjective jumps. | Anchors are behaviorally distinct and monotonic for all scored rows. | Calibration audit shows low reviewer drift and no material anchor inversion. | Two cycles with stable calibration and zero unresolved anchor-monotonicity defect. |
| R4M-15 Aggregation and gate-precedence determinism | Same inputs produce different outcomes across calculators/reviewers. | Formula components exist but precedence/rounding are ambiguous. | Core scoring is deterministic; gate/cap precedence edge cases still diverge. | Deterministic formula and precedence yield one outcome for standard and edge cases. | Independent parity testing passes across all tested scenarios. | Two cycles with exact parity and zero precedence-dispute escalations. |
| R4M-16 Score inflation resistance and high-anchor guardrails | High scores are granted without stronger evidence gates. | Guardrails are stated but easy to bypass or inconsistently applied. | Guardrails exist; high-anchor approvals still show weak challenge depth. | High-anchor assignments require independent evidence and stricter checks. | Distribution audit and challenge tests actively detect and correct inflation attempts. | Two cycles with no unjustified 90/100 grants in independent audit sampling. |
| R4M-17 Cross-role interface consistency and handoff testability | Engineering handoffs are undefined or contradictory. | Handoffs listed but missing trigger/input/output/SLA detail. | Most handoffs are defined; acceptance criteria or SLAs are inconsistent. | Handoffs are complete, testable, and mostly accepted without rework loops. | Cross-role sampling confirms high acceptance and low contradiction churn. | Two cycles with no critical score delay caused by handoff ambiguity/conflict. |
| R4M-18 Versioning, delta re-scoring, and cadence fit | Rubric changes are ad hoc and break cycle execution. | Versions are labeled but no row-level impact or re-score method exists. | Versioning and diffs exist; delta explanations and cadence compliance are inconsistent. | Controlled versioning, row-level impact maps, and delta re-scoring are operational. | Independent review can trace major score deltas to approved rubric changes. | Two cycles with clean comparability, on-time cadence, and zero undocumented rubric edits. |

## 5) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Anchor-jump audit: flag any 50->90 or 75->100 change without new independent evidence artifacts and replay logs.
2. Denominator freeze check: block cycle close if row population changed after scoring start without approved change record and dual reporting.
3. Backfill exclusion check: compare artifact timestamps to cutoff; exclude post-cutoff evidence from current-cycle scoring unless waiver exists.
4. Evidence laundering check: reject polished summaries that lack trace to raw source artifacts.
5. Ghost-link challenge: sample trace links and attempt reverse traversal; unresolved ghost or orphan links invalidate affected rows.
6. Gate-bypass simulation: run scenarios with failed mandatory gates and high averages; any pass outcome indicates exploitable scoring logic.
7. Formula tamper detection: diff scoring formulas/weights vs approved baseline; unapproved changes freeze publication.
8. High-anchor density check: if 90/100 density rises by more than 15 points cycle-over-cycle, trigger mandatory independent resampling.
9. Reviewer-independence enforcement: block high-anchor approval if scorer, evidence author, and validator are the same person.
10. Contradiction suppression check: reconcile contradiction register with meeting minutes and issue tracker; hidden critical contradictions force hold.
11. Exception expiry enforcement: expired waivers must auto-fail associated rows; no evergreen exception carry-forward.
12. Replay witness rotation: require at least one non-author replay operator each cycle; repeated same-operator replay requires secondary witness.

## 6) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

| ID | Tripwire / hard-fail condition | Detection method | Immediate effect | Minimum closure evidence |
| --- | --- | --- | --- | --- |
| R4-MHF-01 | Confirmed evidence fabrication, tampering, or forged provenance in any Rubric_0 scoring artifact. | Hash/provenance forensic audit. | Entire Rubric_0 cycle scoring invalid (`FAIL`). | Forensic closure report, corrected evidence chain, independent full re-score. |
| R4-MHF-02 | Any unresolved Severity-1 contradiction past SLA in engineering-relevant rubric logic. | Contradiction aging dashboard and adjudication log review. | Score publication blocked; cycle marked `INVALID` until resolved. | Signed contradiction resolution pack and impacted-row rescoring evidence. |
| R4-MHF-03 | Independent replay cannot reproduce >=10% sampled engineering-relevant row anchors. | Blind replay sampling and variance ledger. | Invalidate affected dimensions; full-cycle replay required before publication. | Replay pass report with parity on required sample. |
| R4-MHF-04 | Hard gate can be bypassed by arithmetic averaging or manual override in scoring workflow. | Gate-precedence scenario test and score-engine audit. | Published score revoked; cycle fails determinism gate. | Corrected scoring engine/rules and full recomputation evidence. |
| R4-MHF-05 | Non-zero scores assigned without required admissibility fields in >5% sampled rows. | Evidence schema conformance scan. | Affected dimensions set to `0`; if systemic, full cycle invalidated. | Completed admissibility remediation and independent re-sampling below threshold. |
| R4-MHF-06 | Any 90/100 anchor assignment lacks independent reviewer evidence or replay proof. | High-anchor evidence audit. | Affected rows downgraded to `50`; systemic pattern triggers cycle hold. | Independent validation + replay evidence and corrected scorecard. |
| R4-MHF-07 | Unapproved Rubric_0 version/text change occurs during active scoring window. | Version/hash diff against cycle lock record. | All in-window scores invalid until re-run on approved version hash. | Version freeze proof and complete rescoring packet. |
| R4-MHF-08 | Mandatory anti-gaming controls are skipped for cycle close. | Anti-gaming execution ledger completeness check. | No score above `50` allowed for affected scope; publication blocked if unresolved. | Completed control runs with enforced consequences and updated scorecard. |
| R4-MHF-09 | Cross-role handoff criteria conflict on critical engineering controls and remain unresolved. | Handoff compatibility matrix and returned-handoff log. | Role-layer scoring invalid until adjudication closes conflict. | Signed adjudication decision with synchronized handoff criteria and rescored rows. |
| R4-MHF-10 | Dual calculator recompute from identical inputs produces different final verdicts. | Independent parity test across approved calculators. | Determinism failure; cycle score invalid. | Corrected arithmetic specification and parity pass evidence. |

## 7) Cross-role dependencies and adjudication handoffs

| Counterpart role | Required inbound to R4 meta-evaluation | R4 outbound handoff | Acceptance criteria | SLA / cadence |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor | Risk appetite and strictness policy for rubric use in release decisions. | Recommendation to approve/hold Rubric_0 version and threshold changes. | Signed decision with no open R4-MHF conditions. | Per cycle close |
| R1 Product Manager | Requirement-governance intent and scope-change policy constraints. | Findings on trace-chain and requirement-to-code criteria quality. | Requirement-governance conflicts resolved and reflected in rubric updates. | 3 business days |
| R2 Product Architect | Architecture-boundary and contradiction precedence decisions. | Engineering-criteria boundary defects and contradiction protocol gaps. | No unresolved boundary conflict for critical engineering controls. | 3 business days |
| R3 Engineering Manager | Execution-cadence data and operational burden feedback. | Cadence fit and adjudication-latency recommendations for Rubric_0. | Cycle SLA remains feasible without weakening controls. | Weekly during active cycle |
| R5 QA/Test Engineer | Oracle/calibration findings and verification-replay defects. | Required rubric updates for test-rigor/oracle criteria. | Joint sign-off on revised test-rigor anchor language. | 2 business days |
| R6 SRE/Platform Engineer | Reliability, observability, and recovery validation constraints. | Rubric control updates for failure-mode and operability criteria. | Reliability controls are measurable and replayable in scoring rules. | Weekly reliability sync |
| R7 Security Engineer | Security-control and supply-chain risk adjudication inputs. | Security/supply-chain rubric defect log and remediation requirements. | Critical security rubric defects closed or explicitly blocked. | 2 business days for critical issues |
| R8 Privacy/Compliance/Legal | Legal/privacy precedence and mandatory-control interpretation. | Contradiction and gate wording updates affecting regulated engineering paths. | Legal/privacy control wording approved and synchronized across sections. | Before release-cycle scoring |
| R12 DevOps/Release Manager | Gate execution behavior and release-decision workflow evidence. | Determinism/gate-precedence validation results and required workflow changes. | No gate-bypass path remains in operational scoring workflow. | Per release train |
| R15 Internal Audit/Assurance | Independent replay results and control-test findings. | Final evidence package, corrected scorecard, and unresolved-risk disclosure. | Assurance replay succeeds without author assistance. | 5 business days |

Adjudication rules:
1. Handoff status is binary: `accepted` or `returned`; silent acceptance is invalid.
2. Every returned handoff must include defect class, impacted rubric rows, owner, and due date.
3. Any unresolved critical handoff dispute escalates to `R0 + R15` within 1 business day.

## 8) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle phase | Checklist item | Evidence artifact | Delta re-evaluation rule |
| --- | --- | --- | --- |
| Cycle start | Lock Rubric_0 version hash and scoring population denominator. | Version lock record and denominator manifest. | Any mid-cycle change requires restart or approved dual-run. |
| Cycle start | Refresh sub-dimension ownership and reviewer-independence roster. | Ownership matrix and conflict-of-interest attestations. | Independence breach invalidates affected high-anchor scoring. |
| Pre-calibration | Run anchor monotonicity lint on all engineering-relevant rows. | Anchor lint report and defect list. | Unfixed monotonicity defect blocks calibration close. |
| Pre-calibration | Validate contradiction protocol fields (severity, SLA, precedence, owner). | Contradiction protocol conformance sheet. | Missing required field blocks scoring kickoff. |
| Calibration | Execute two-reviewer scoring on representative sample and compare anchor spread. | Calibration spread log and reconciliation notes. | Any >=25-point disagreement requires joint evidence replay. |
| Mid-cycle control | Perform independent replay on at least 20% sampled engineering-relevant rows. | Replay transcript and variance ledger. | Any unexplained anchor mismatch triggers full sub-dimension replay. |
| Mid-cycle control | Run gate-bypass and formula-tamper adversarial checks. | Adversarial test outputs and enforcement actions. | Failed check freezes publication until corrected and rerun. |
| Mid-cycle control | Audit high-anchor assignments for evidence depth and independence. | High-anchor audit report. | Missing independent evidence downgrades row and reopens adjudication. |
| Pre-close | Recompute final scores via two approved calculators. | Dual-calculator parity report. | Any mismatch invalidates draft scorecard. |
| Pre-close | Reconcile contradiction register, handoff returns, and unresolved exceptions. | Consolidated closure log. | Any open Severity-1 item blocks publication. |
| Publication | Publish final score with evidence index and triggered caps/gates summary. | Final scorecard, evidence manifest, gate summary. | Missing manifest or gate summary invalidates publication. |
| Post-cycle | Quantify false-positive/false-negative scoring patterns in Rubric_0 criteria. | Error taxonomy and frequency report. | Top 3 error classes must receive owned corrective actions. |
| Post-cycle | Apply rubric updates and perform impacted-row delta re-score. | Change log with impacted rows and delta score report. | Unexplained delta >1 anchor step requires rollback or additional evidence. |
| Next-cycle readiness | Verify previous cycle actions closed with objective proof. | Remediation closure tracker and proof links. | <90% on-time closure triggers readiness warning and stricter sampling next cycle. |

This Rubric_1 instrument is intentionally conservative. It scores Rubric_0 only when controls are explicit, evidence is replayable, contradictions are resolved within SLA, and high anchors withstand anti-gaming challenge. If those conditions degrade, score must degrade.


---

## R5 QA / Test Engineer

- source_file: `swarm_outputs/meta_rubric_role_expansions/R5_qa_test_engineer_rubric1.md`
- words: 4530
- lines: 145

# R5 QA / Test Engineer Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

## 2) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R5 evaluates whether Rubric_0 is an executable quality-control system for testing governance, not a narrative checklist. R5 scores Rubric_0 on verification rigor, falsifiability, evidence integrity, anti-gaming resilience, contradiction handling, and operational usability in real release cadence.

This meta-rubric evaluates Rubric_0 itself and never scores product artifact quality directly.

### Decision rights (R5 meta-evaluator)
| Decision area | R5 authority | Non-delegable boundary | Required co-signers | Required decision evidence |
| --- | --- | --- | --- | --- |
| QA meta-rubric fitness recommendation | Recommend `approve`, `conditional approve`, or `hold` for Rubric_0 use in release gating | Cannot approve if any hard-fail tripwire in Section 6 is active | R1, R12, R15 | Signed fit-gap assessment, hard-fail status sheet, evidence index |
| Evidence admissibility policy quality | Final QA judgment on whether Rubric_0 evidence rules are auditable and replayable | Cannot accept non-replayable evidence rules for non-zero scoring | R15 | Evidence schema conformance audit and replay log |
| Verification anchor quality | Final QA judgment on whether Rubric_0 anchors are falsifiable and behaviorally discriminative | Cannot pass anchors that permit subjective score inflation | R2 | Anchor monotonicity and discrimination report |
| Gate enforcement design quality | Final QA judgment on whether Rubric_0 gates/tripwires are operationally enforceable | Cannot accept gates that can be bypassed by averaging or manual override | R12, R15 | Gate precedence simulation and override audit |
| Contradiction protocol quality | Joint authority on contradiction lifecycle sufficiency | Cannot close unresolved critical contradiction risk in scoring logic | R2, R8, R15 | Contradiction protocol test results and aging register |
| Delta re-evaluation readiness | Final QA recommendation for rubric version promotion from test-governance perspective | Cannot recommend promotion without delta impact and replay-based re-score evidence | R1, R0 | Version diff dossier, impacted-row re-score report |

### Meta-scoring admissibility rules
- Anchor scale: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires explicit `who/what/where` evidence.
- No sub-dimension may score above `50` without replayable raw evidence.
- No sub-dimension may score above `75` without independent reviewer validation.
- No sub-dimension may score above `90` without adversarial challenge evidence in the same cycle.
- Evidence created after cycle cutoff is excluded from current-cycle scoring.

## 3) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R5-M01 QA concern coverage completeness | Rubric_0 fully covers QA-critical governance concerns across A2/A3/A4/A5/A6 and role layer. | Build QA concern catalog from R5 role expansion and map to Rubric_0 rows; critical concern coverage >=95%; no unmapped critical concern. | Who: R5 meta-review lead + R2 reviewer. What: concern-to-row mapping matrix and gap log. Where: Rubric_0 master, R5 expansion, review workbook. |
| R5-M02 Requirement-to-test traceability rule quality | Rubric_0 requires bidirectional requirement-test-evidence linkage for non-zero quality claims. | Sample 20 scored rows touching requirements/verification; >=95% include explicit bidirectional linkage rules; broken-link tolerance <=2%. | Who: R5 + R1 counterpart. What: traceability conformance audit sheet. Where: Rubric_0 row text, sampled scorecards, evidence manifests. |
| R5-M03 Oracle falsifiability and anchor precision | Rubric_0 criteria are objectively falsifiable and avoid subjective pass language. | Lint rows for vague terms (`good`, `adequate`, `robust` without test clause); <=2% unresolved vagueness in sampled rows; each high anchor includes measurable threshold. | Who: R5 + R2. What: falsifiability lint report and anchor precision checklist. Where: Rubric_0 anchor tables and scoring policy. |
| R5-M04 Negative/boundary/failure-path expectation strength | Rubric_0 enforces testing of non-happy paths and state/limit failures at rubric-design level. | Verify rows explicitly require negative, boundary, and failure-path evidence in QA-relevant sections; absence rate <=5% on critical rows. | Who: R5 + R4 reviewer. What: scenario expectation audit and exceptions register. Where: Rubric_0 role layer and section criteria. |
| R5-M05 Test data governance criteria quality | Rubric_0 defines test-data fidelity, masking, and compliance expectations in a testable way. | Check criteria specify data class, privacy constraint, freshness, and admissibility conditions; confirm conflict-free alignment with privacy/legal controls. | Who: R5 + R8 + data steward. What: test-data control mapping and conflict check. Where: Rubric_0 text, privacy/control registry, cycle adjudication notes. |
| R5-M06 Environment parity and reproducibility criteria quality | Rubric_0 requires deterministic replay across controlled environments. | Verify explicit parity/replay requirements (`configuration source`, `environment manifest`, `replay procedure`); run non-author replay on sample rows. | Who: R5 + R6 + R12. What: replay procedure conformance and parity audit. Where: Rubric_0 criteria, runbooks, replay transcripts. |
| R5-M07 Automation stability and flake-control criteria quality | Rubric_0 defines reliable automation-signal requirements and anti-flake controls. | Confirm criteria include first-fail retention, flake metrics, quarantine governance, retry-masking controls, and score consequences for non-compliance. | Who: R5 + R3. What: automation-governance audit and flake-control checklist. Where: Rubric_0 anti-gaming/gate sections and sampled adjudication packets. |
| R5-M08 CI/CD quality-gate enforceability design | Rubric_0 gate logic is executable, tamper-resistant, and not bypassable by discretion. | Simulate failed mandatory gate with high average score; expected outcome must remain `FAIL`; unauthorized bypass handling must be explicit with deterministic penalty. | Who: R5 + R12 + R15. What: gate precedence simulation report. Where: Rubric_0 global gates, role gates, scoring model docs. |
| R5-M09 Performance/capacity verification criteria quality | Rubric_0 provides measurable NFR verification criteria with replayable thresholds. | Verify NFR rows include named metric, threshold, dataset/workload definition, and pass/fail logic; recompute sample metric outcomes from raw evidence. | Who: R5 perf reviewer + R6. What: NFR criteria audit and recompute sheet. Where: Rubric_0 NFR-related rows and evidence bundle. |
| R5-M10 Security/privacy/abuse verification criteria quality | Rubric_0 integrates adversarial security/privacy/abuse validation expectations, not scanner-only language. | Confirm threat/misuse test expectations, closure conditions, and hard-fail ties to global gates; critical-path omission tolerance = 0. | Who: R5 security QA + R7 + R8. What: adversarial-control mapping and omission scan. Where: Rubric_0 security/privacy sections and tripwire catalog. |
| R5-M11 Reliability/failover/recovery verification criteria quality | Rubric_0 requires explicit resilience validation and recovery proof criteria. | Verify criteria include fault scenarios, restore integrity checks, and RTO/RPO-like evidence constraints; replay sample resilience claims for reproducibility. | Who: R5 + R6. What: resilience-criteria conformance report and replay log. Where: Rubric_0 reliability criteria and cycle evidence archive. |
| R5-M12 Defect severity calibration rule quality | Rubric_0 defines objective severity classification and closure evidence standards. | Audit whether criteria require severity rationale, impact class, reproducible repro, retest closure proof, and anti-severity-laundering checks. | Who: R5 + R13 + R3. What: severity-governance audit and misclassification challenge results. Where: Rubric_0 defect-related criteria and adjudication records. |
| R5-M13 Regression governance criteria quality | Rubric_0 enforces impact-based regression selection and stale-suite control. | Verify regression criteria require change-impact mapping, suite freshness checks, and recurrence prevention linkage; test for explicit penalties on stale coverage. | Who: R5 + R4 + R12. What: regression-governance audit worksheet. Where: Rubric_0 QA rows, release governance logs. |
| R5-M14 Evidence admissibility and provenance schema quality | Rubric_0 evidence rules are complete, auditable, and resistant to tampering/backfill. | Validate mandatory fields (`who/what/where/time/version/hash`) and post-cutoff exclusion rule; sample evidence packages for completeness >=95%. | Who: R5 evidence owner + R15. What: admissibility schema validation report. Where: Rubric_0 evidence protocol and sample cycle evidence index. |
| R5-M15 Independent replayability and recomputation determinism | Rubric_0 enables independent re-scoring with stable outcomes from the same evidence. | Non-author replay >=20% sampled rows; anchor agreement >=95%; aggregate recompute variance = 0; any unexplained variance triggers hold. | Who: independent QA reviewer + R15 observer. What: replay packet, recompute logs, variance register. Where: immutable evidence store and score workbook. |
| R5-M16 Contradiction handling and adjudication quality | Rubric_0 contradiction protocol is explicit, SLA-bound, and score-impacting. | Verify contradiction schema includes class, severity, owner, SLA, closure proof, and forced score recalculation rules; unresolved critical contradiction at cycle close = 0. | Who: R5 + R2 + R8 + R15. What: contradiction process conformance and aging audit. Where: contradiction register, adjudication minutes, Rubric_0 protocol text. |
| R5-M17 Score inflation resistance and high-anchor controls | Rubric_0 blocks unjustified high scores through stronger evidence and independent checks. | Analyze high-anchor (`90/100`) density, evidence strength, and reviewer independence; require deterministic caps when controls fail; unexplained 90+ density spikes trigger rescore. | Who: R5 + R15 + R0 observer. What: inflation analytics and cap-enforcement report. Where: score distribution dashboard, high-score evidence samples, approval logs. |
| R5-M18 Operational usability and cycle-latency fit | Rubric_0 can be executed on release cadence with low interpretation drift and clear handoffs. | Timebox end-to-end scoring simulation; release-cycle execution <=3 business days and planning-cycle <=7 business days; ambiguity-induced rework <=10%. | Who: R5 + R3 + R12. What: dry-run timing report, ambiguity log, handoff defect log. Where: governance tracker and cycle retrospectives. |

## 4) Anchor table (explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension)

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R5-M01 QA concern coverage completeness | QA-critical concerns are mostly absent from Rubric_0. | Some QA concerns are present, but critical coverage gaps are untracked. | Most concerns covered, but critical unmapped items remain. | Critical concerns are mapped with minor non-critical gaps. | Independent review confirms near-complete critical coverage with controlled gaps. | Two cycles show complete critical coverage with zero unresolved mapping disputes. |
| R5-M02 Requirement-to-test traceability rule quality | Rubric_0 allows non-zero scoring without traceability rules. | Traceability mentioned but one-way or optional. | Bidirectional intent exists, but enforcement/sampling is weak. | Bidirectional linkage rules are explicit and consistently enforceable. | Independent sample audit confirms strong linkage integrity and low defect rate. | Two cycles with zero unsupported non-zero traceability claims in audit sample. |
| R5-M03 Oracle falsifiability and anchor precision | Criteria are subjective and non-falsifiable. | Some measurable language exists, but many rows remain vague. | Most rows are testable, but high-anchor criteria are under-specified. | Rows use measurable pass/fail language with clear high-anchor thresholds. | Independent lint finds minimal vagueness and consistent measurable anchors. | Two cycles with no material ambiguity disputes in adjudication. |
| R5-M04 Negative/boundary/failure-path expectation strength | Rubric_0 evaluates only happy-path evidence. | Non-happy-path expectations are sparse and optional. | Negative/boundary expectations exist but are inconsistent on critical rows. | Critical rows explicitly require negative, boundary, and failure-path evidence. | Independent sampling confirms consistent enforcement across sections/roles. | Two cycles with zero critical scoring decisions accepted without failure-path evidence expectations. |
| R5-M05 Test data governance criteria quality | Test-data governance is absent or contradictory. | Governance language exists but omits compliance or fidelity controls. | Core controls exist, but freshness/classification rules are incomplete. | Data-fidelity and compliance controls are explicit, auditable, and consistent. | Cross-role review confirms no unresolved policy conflict in sampled use. | Two cycles with full control conformance and no admissibility dispute on data criteria. |
| R5-M06 Environment parity and reproducibility criteria quality | Rubric_0 does not require reproducible environments. | Reproducibility mentioned without operational requirements. | Basic parity requirements exist; non-author replay remains unreliable. | Explicit parity and replay criteria enable reliable non-author reproduction. | Cross-environment replay succeeds for sampled rows with defined tolerances. | Two cycles of successful non-author cold-start replay for all sampled critical rows. |
| R5-M07 Automation stability and flake-control criteria quality | Rubric_0 ignores flake and retry masking risks. | Flake is acknowledged, but no enforceable thresholds or penalties exist. | Flake controls exist but enforcement is inconsistent. | Flake thresholds, quarantine policy, and retry-masking penalties are explicit and applied. | Independent challenge confirms controls detect and penalize masking behavior. | Two cycles with full control execution and no unpenalized flake-masking event. |
| R5-M08 CI/CD quality-gate enforceability design | Gate logic is bypassable or undefined. | Gates exist but precedence and bypass consequences are ambiguous. | Gates are mostly enforceable, but edge-case override paths are unclear. | Mandatory gates are deterministic with explicit bypass penalties and precedence over averages. | Scenario replay confirms no bypass path under adversarial conditions. | Two cycles with zero unauthorized bypass and no gate-precedence dispute. |
| R5-M09 Performance/capacity verification criteria quality | NFR verification criteria are absent or non-measurable. | NFR criteria exist as narrative without thresholds or workload definitions. | Thresholds exist, but recompute/replay requirements are incomplete. | NFR criteria are measurable, replayable, and tied to explicit pass/fail logic. | Independent recompute confirms correctness on sampled claims. | Two cycles with reproducible NFR scoring and zero unresolved threshold interpretation conflict. |
| R5-M10 Security/privacy/abuse verification criteria quality | Adversarial verification is absent; scanner-only language dominates. | Security/privacy criteria exist but miss abuse-path expectations. | Adversarial criteria are partially defined with weak closure logic. | Threat, privacy, and abuse verification requirements are explicit and enforceable. | Critical-path coverage and hard-fail linkages pass independent audit. | Two cycles with no critical-path omission and consistent hard-fail enforcement. |
| R5-M11 Reliability/failover/recovery verification criteria quality | Resilience claims are untestable in Rubric_0. | Resilience mentioned without drill/recovery evidence requirements. | Drill expectations exist, but integrity and reproducibility checks are weak. | Fault/recovery evidence rules are explicit with integrity checks and timing constraints. | Blind replay sample confirms reliable adjudication outcomes. | Two cycles with deterministic resilience scoring and zero unresolved recovery-proof dispute. |
| R5-M12 Defect severity calibration rule quality | Severity rules are absent or arbitrary. | Severity bands exist but lack objective impact criteria. | Objective criteria exist but misclassification controls are weak. | Severity and closure rules are objective, auditable, and anti-laundering aware. | Independent challenge shows consistent classification across reviewers. | Two cycles with no material severity-laundering finding and reproducible closure decisions. |
| R5-M13 Regression governance criteria quality | Regression governance is missing or purely generic. | Regression is required without impact linkage or freshness controls. | Impact linkage exists but stale-suite management is weak. | Impact-based regression and freshness controls are explicit with score consequences. | Independent sample confirms governance rules prevent stale-suite acceptance. | Two cycles with no severe governance misses attributable to stale/untargeted regression criteria. |
| R5-M14 Evidence admissibility and provenance schema quality | Rubric_0 permits unverifiable evidence for scoring. | Evidence fields are partial; provenance integrity is weak. | Most required fields exist, but cutoff/hash enforcement is inconsistent. | Complete admissibility schema with enforced provenance and cutoff rules. | Independent sample shows high completeness and reliable tamper detection. | Two cycles with zero inadmissible evidence accepted in sampled audits. |
| R5-M15 Independent replayability and recomputation determinism | Scores cannot be replayed from provided evidence. | Partial replay possible only with scorer interpretation. | Replay succeeds inconsistently and aggregate recompute varies. | Independent replay and recompute are stable for most sampled rows. | Replay and recompute pass with near-zero unexplained variance. | Two cycles with full sampled replay parity and deterministic aggregate recomputation. |
| R5-M16 Contradiction handling and adjudication quality | Contradictions are unmanaged and non-blocking. | Contradictions are logged ad hoc without SLA or score impact rules. | Protocol exists but critical contradiction closure is inconsistent. | Protocol is explicit with severity, SLA, and mandatory score-impact handling. | Independent audit confirms critical contradictions are resolved before finalization. | Two cycles with zero unresolved critical contradictions at score publication. |
| R5-M17 Score inflation resistance and high-anchor controls | High scores are granted without stronger evidence or checks. | Inflation controls are listed but not enforceable. | Controls run inconsistently; high-anchor justification quality varies. | High-anchor controls are explicit, independent, and enforce deterministic caps. | Distribution and evidence-strength audits catch and correct inflation attempts. | Two cycles with stable high-anchor distribution and zero unjustified 90/100 findings on audit sample. |
| R5-M18 Operational usability and cycle-latency fit | Rubric_0 execution routinely misses decision windows. | Rubric_0 is usable only with heavy ad hoc interpretation and delay. | Cadence is mostly achievable but ambiguity causes frequent rework. | Rubric_0 executes within SLA with manageable ambiguity and clear handoffs. | Multi-team dry runs show low interpretation drift and predictable cycle timing. | Two cycles with sustained SLA compliance and no decision delay caused by rubric design defects. |

## 5) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Enforce denominator freeze at cycle start for all scored populations; any in-cycle denominator change requires approved change record and dual reporting (`pre-change` and `post-change`).
2. Require independent validation evidence for every `90` or `100` assignment; absence auto-caps affected row at `50`.
3. Run non-author replay on at least `20%` of scored rows; unexplained replay mismatch above one anchor level invalidates affected row scores.
4. Recompute aggregate scores from raw row-level evidence using an independent calculator; any mismatch blocks publication.
5. Reject post-cutoff evidence for current cycle, including backdated uploads discovered via timestamp/provenance audit.
6. Detect anchor shopping by diffing draft vs final anchors; undocumented upward adjustments are invalid.
7. Run contradiction suppression audit by reconciling contradiction register against adjudication minutes; hidden critical contradictions invalidate cycle output.
8. Perform retry-masking audit on QA-related governance criteria; if first-fail outcomes are omitted, related sub-dimensions are capped at `50`.
9. Sample high-score rows and verify `who/what/where/time/version/hash` completeness; incomplete evidence downgrades row to `0`.
10. Run silent-override detection by diffing computed scores against published scores; any manual override requires signed rationale and authorized co-signers.
11. Conduct cross-role consistency checks on sampled shared conditions (R5/R7/R8/R12/R15); unexplained divergence greater than one anchor step triggers adjudication hold.
12. Track high-anchor density and evidence-strength ratio each cycle; unexplained 90+ spike triggers mandatory full resampling before publication.

## 6) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

| ID | Tripwire / hard-fail condition | Detection method | Immediate effect | Minimum recovery proof |
| --- | --- | --- | --- | --- |
| R5-MHF-01 | Evidence fabrication, tampering, or provenance mismatch in any scoring package. | Hash/provenance forensic audit and replay check. | Entire Rubric_0 cycle marked `INVALID`. | Forensic closure report, corrected immutable evidence chain, independent full re-score. |
| R5-MHF-02 | Critical contradiction remains unresolved at score publication cutoff. | Contradiction register aging and severity review. | Publication blocked; cycle cannot close. | Signed closure record and rescored impacted rows. |
| R5-MHF-03 | Mandatory gate/tripwire precedence can be bypassed by averaging or manual override. | Gate precedence simulation plus score override audit. | Published score revoked; cycle invalidated. | Corrected scoring logic and complete recomputation. |
| R5-MHF-04 | Non-zero score assigned without required `who/what/where` evidence in sampled audit above 5% defect rate. | Evidence admissibility sampling audit. | Cycle invalidated for affected scope; if systemic, full cycle invalid. | Evidence completion, defect-rate reduction below threshold, independent resample pass. |
| R5-MHF-05 | Independent replay fails on sampled rows above tolerance without justified rationale. | Non-author replay and variance analysis. | Score publication blocked pending remediation. | Replay pass report meeting defined tolerance and adjudicated variance closures. |
| R5-MHF-06 | Any `90+` score lacks independent reviewer validation artifact. | High-anchor validation audit. | Affected rows downgraded to `50`; systemic failure invalidates cycle. | Independent validations completed and affected rows rescored. |
| R5-MHF-07 | Unauthorized CI/CD gate bypass is accepted by Rubric_0 logic without deterministic penalty. | Gate event log review and scenario replay. | Rubric_0 deemed unfit for release decisions this cycle. | Updated gate rules with enforced penalties and successful replay test. |
| R5-MHF-08 | Evidence added after cutoff is included in current-cycle scoring. | Cutoff timestamp reconciliation audit. | Current-cycle score invalidated. | Cutoff-compliant rescoring with audit trail. |
| R5-MHF-09 | Reviewer independence breach: same person authored evidence, scored row, and approved high anchor. | Role-separation/IAM audit. | Affected rows invalidated; repeated pattern invalidates cycle. | Corrected reviewer assignments and independent rescoring. |
| R5-MHF-10 | Required anti-gaming challenge suite is not executed for cycle. | Control-execution checklist audit. | No row may score above `50` for affected scope. | Completed challenge suite and replayed scoring. |
| R5-MHF-11 | Rubric version changes during active scoring window without approved change-control protocol. | Version hash and change-log audit. | In-window scores invalid; scoring window reset required. | Version freeze evidence and full re-score on approved hash. |
| R5-MHF-12 | Calibration shows inverse risk signal (higher scores correlate with worse outcomes) and no corrective action plan exists. | Quarterly calibration analysis and governance review. | Rubric_0 marked `HOLD` for next cycle use. | Root-cause analysis, anchor/threshold redesign, and pilot recalibration pass. |

## 7) Cross-role dependencies and adjudication handoffs

| Counterpart role | Required input to R5 meta-evaluation | R5 outbound handoff | Acceptance criteria | SLA / cadence |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor / Business Owner | Risk appetite boundaries and decision policy for rubric adoption | Rubric_0 fitness recommendation with hard-fail status | Signed decision with explicit accept/hold and due dates for gaps | Per cycle close |
| R1 Product Manager | Requirement/governance usability feedback and ambiguity reports | Traceability/testability quality findings and required rubric rewrites | Returned findings resolved or accepted with named owner/date | Weekly during active cycle |
| R2 Product Architect / Enterprise Architect | Structural contradiction analysis and terminology clarifications | QA-specific enforceability and anchor precision defects | No unresolved structural contradiction on QA-critical rows | Within 3 business days per issue |
| R3 Engineering Manager | Execution-friction and reviewer-latency data | Operational simplification recommendations for rubric flow | Cycle-latency defects assigned and tracked to closure | Bi-weekly |
| R4 Software Engineer | Failure-path and regression realism feedback on rubric criteria | Regression and edge-case governance improvement proposals | Critical failure-path expectations are explicit and testable | Weekly |
| R6 SRE / Platform Engineer | Replay environment constraints, reliability drill learnings | Reproducibility and resilience-criteria quality findings | Replay criteria are operationally executable in target environments | Weekly and pre-release |
| R7 Security Engineer / Security Architect | Threat-model and abuse-case governance expectations | Security/abuse verification criteria quality findings | No critical threat-path omission in rubric QA criteria | Pre-release cycle and monthly governance |
| R8 Privacy / Compliance / Legal | Evidence admissibility legal/privacy constraints and retention rules | Privacy-admissibility conflict log and required rubric corrections | No unresolved legal/privacy contradiction in evidence rules | Pre-release and on policy changes |
| R12 DevOps / Release Manager | CI/CD enforcement behavior and override audit logs | Gate-precedence validation and bypass-risk findings | Deterministic gate enforcement accepted by release governance | Per release train |
| R13 Operations / Support / Customer Success | Escaped-defect and severity outcome patterns for calibration | Severity calibration and feedback-loop rubric improvements | Escaped-defect lessons mapped to rubric updates | Weekly operations review |
| R15 Internal Audit / Assurance | Independent replay findings and control-test results | Remediation plan for evidence integrity/replay gaps | Audit replay pass on sampled critical rows | Per cycle close and quarterly assurance |

### Handoff adjudication rules
1. Every handoff artifact must include `owner`, `timestamp`, `rubric version`, `affected sub-dimensions`, and immutable evidence links.
2. Handoff state is binary: `accepted` or `returned`; silent acceptance is invalid.
3. Returned handoffs must include defect class (`evidence`, `contradiction`, `determinism`, `inflation`, `operability`) and resubmission due date.
4. Two consecutive returns for the same defect class escalate to `R0 + R15` adjudication within 1 business day.

## 8) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle phase | Improvement checklist item | Owner(s) | Evidence artifact | Pass criterion | Delta re-evaluation rule |
| --- | --- | --- | --- | --- | --- |
| Cycle start | Freeze Rubric_0 version hash, scoring population, and cutoff timestamp. | R5 + R12 | Version lock record and cutoff notice. | Zero uncontrolled in-cycle version/population drift. | Any drift forces cycle restart on approved baseline. |
| Cycle start | Confirm reviewer independence roster and high-anchor validation assignments. | R5 + R15 | Independence matrix and assignment log. | No role-separation conflicts in planned scoring flow. | Conflict found requires reassignment before scoring begins. |
| Design review | Run sub-dimension anchor monotonicity and falsifiability lint. | R5 + R2 | Anchor lint report and defect log. | No unresolved critical anchor ambiguity. | Critical ambiguity blocks scoring kickoff. |
| Design review | Execute contradiction protocol conformance test (schema + SLA + score impact). | R5 + R2 + R8 | Contradiction protocol test sheet. | All required contradiction fields and rules present. | Missing field/rule blocks publication readiness. |
| Data prep | Validate evidence admissibility schema (`who/what/where/time/version/hash`) on sample packets. | R5 + R15 | Admissibility scan report. | Sample completeness >=95% and no tamper signal. | Failed scan triggers remediation and re-sampling before scoring. |
| Scoring run | Perform non-author replay on >=20% sampled rows and log variance. | Independent reviewer + R5 observer | Replay workbook and variance register. | Replay variance within approved tolerance. | Excess variance requires impacted-dimension replay. |
| Scoring run | Recompute aggregate score using independent calculator and compare output. | R5 + R12 | Recompute log and parity check. | Exact aggregate parity. | Any mismatch invalidates draft score publication. |
| Mid-cycle control | Run anti-gaming challenge set (denominator, backfill, override, retry masking). | R5 + R15 | Challenge execution report. | All mandatory checks executed with outcomes recorded. | Failed control applies defined cap/hold before publication. |
| Pre-close | Audit high-anchor rows for independent validation and evidence strength. | R5 + R15 | High-anchor audit report. | 100% of `90+` rows independently validated. | Missing validation downgrades affected rows and triggers rescore. |
| Pre-close | Resolve all critical contradictions and update impacted scores. | R5 + R2 + R8 | Signed contradiction closure log. | Zero unresolved critical contradictions at close. | Any open critical contradiction blocks publication. |
| Publication | Publish final score, hard-fail status, and evidence index with immutable links. | R5 owner | Final scorecard package. | Package is complete and reproducible by non-author reviewer. | Missing manifest or link integrity failure invalidates publication. |
| Post-cycle | Run calibration: compare score bands vs downstream risk/outcome bands. | R5 + R9 + R13 | Calibration study and variance memo. | Directional calibration holds within defined tolerance. | Inverse/unstable calibration requires corrective action plan before next cycle. |
| Post-cycle | Classify rubric defects (false positive, false negative, ambiguity, latency, inflation). | R5 + R3 + R15 | Defect taxonomy report. | Top defect classes have assigned owners and due dates. | Unowned critical defect blocks next-cycle readiness sign-off. |
| Next-cycle readiness | Re-score impacted prior-cycle sample using updated rubric and explain deltas. | R5 + R1 + R2 | Delta re-score dossier and explanation log. | Unexplained row delta greater than one anchor step = 0. | Unexplained deltas require rollback or further revision before promotion. |


---

## R6 SRE / Platform Engineer

- source_file: `swarm_outputs/meta_rubric_role_expansions/R6_sre_platform_engineer_rubric1.md`
- words: 4507
- lines: 151

# R6 SRE / Platform Engineer Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 evaluates the quality, rigor, anti-gaming strength, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 1) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R6 (SRE / Platform Engineer) evaluates whether Rubric_0 can be executed as a reliable runtime-governance instrument under production pressure. The role is accountable for determining if Rubric_0 is contradiction-safe, evidence-replayable, inflation-resistant, gate-enforceable, and fast enough to support real release and incident decisions.

### Decision rights
| Decision domain | R6 authority on Rubric_0 quality | Non-delegable rule | Escalation boundary |
| --- | --- | --- | --- |
| Runtime-governance coverage adequacy | Approve/return Rubric_0 reliability-governance coverage before scoring cycle opens | Cannot approve if any critical runtime decision class is unmapped | Escalate to R0 and R2 within 1 business day |
| Evidence admissibility for reliability claims | Accept/reject evidence standards used for non-zero scoring | No non-zero score without complete `who/what/where`, provenance, and cutoff discipline | Escalate to R15 for integrity review on any tamper sign |
| Replay and recomputation sufficiency | Require replay protocol fixes before publication | No score publication when independent replay of sampled rows fails tolerance | Escalate to R15 and R12 same cycle |
| Contradiction-resolution determinism | Require precedence and SLA corrections for conflicting rubric clauses | No publication with active unresolved Severity-1 contradiction at cutoff | Escalate to R2/R7/R8 based on contradiction class |
| Gate and tripwire enforceability | Block publication when gate logic is bypassable or ambiguous | No pass outcome allowed with active `G1..G6` or `RG1..RG4` fail condition | Escalate immediately to R0 governance forum |
| Score inflation resistance controls | Enforce high-score guardrails and challenge evidence requirements | No score >75 without independent corroboration; no score >90 without challenge evidence | Escalate to R15 on repeat inflation pattern |
| Operational cadence fitness | Approve/return rubric execution model based on cycle latency and evaluator load | Cannot approve process that routinely misses release/incident decision windows | Escalate to R3 and R12 for workflow redesign |
| Rubric delta governance | Approve/reject Rubric_0 deltas for next cycle with impact scope | No retroactive re-score without versioned reopen record and approvers | Escalate to R11 + R15 on change-control breach |

### Admissibility and scoring protocol for this meta-rubric
- Allowed anchors: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires admissible evidence captured before cycle cutoff.
- Any hard-fail in Section 5 marks Rubric_0 cycle scoring `INVALID`.

## 2) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R6M-01 Runtime Governance Decision-Coverage Completeness | Rubric_0 covers all critical SRE/platform governance decisions needed for safe operations. | Build decision catalog (SLO policy, release gating, incident command, capacity, dependency risk, restore/DR, exception control). Pass if >=95% mapped and 100% of safety-critical decisions mapped to explicit rubric clauses. | Who: R6 lead evaluator + R3 + R12. What: decision-to-clause trace matrix, gap ledger. Where: rubric review workbook and governance decision register. |
| R6M-02 SLI/SLO and Error-Budget Clause Testability | Rubric_0 reliability clauses are measurable, queryable, and linked to deterministic actions. | Sample reliability clauses. Pass if each sampled clause specifies metric formula/query source, threshold, trigger action, and owner; undefined trigger-action pairs = 0 in sample. | Who: R6 observability owner + R1 reviewer. What: clause testability audit, metric-definition checklist. Where: rubric clause matrix and observability references. |
| R6M-03 Incident and Escalation Governance Evaluability | Rubric_0 can consistently evaluate detection, triage, incident command, and escalation quality. | Replay incident-evidence packets across two scorers. Pass if severity-class interpretation and escalation compliance decisions agree 100% on critical samples. | Who: R6 incident reviewer + R13 + R15 witness. What: incident scoring replay logs, disagreement register. Where: incident evidence packet store and calibration board records. |
| R6M-04 Change Safety Gate Evaluability | Rubric_0 defines executable scoring criteria for canary/progressive delivery, abort, rollback, and freeze gates. | Run synthetic release scenarios (gate-pass, gate-fail, waiver). Pass if each scenario yields deterministic score impact and gate consequence with no manual interpretation gap. | Who: R6 + R12 + R4 reviewers. What: release gate simulation matrix, waiver-decision audit. Where: release control test harness and rubric gate map. |
| R6M-05 Capacity, Saturation, and Resilience Coverage Adequacy | Rubric_0 sufficiently evaluates proactive capacity control and resilience validation practices. | Cross-check rubric clauses against required capacity/resilience evidence classes (forecasts, headroom, saturation alarms, fault-injection/game-day outcomes). Pass if required class coverage = 100%. | Who: R6 capacity owner + R2 architect reviewer. What: evidence-class crosswalk, missing-control log. Where: reliability control catalog and rubric trace workbook. |
| R6M-06 Backup/Restore/DR Proof Requirement Strength | Rubric_0 blocks high scoring when restore and DR claims are not proven by replayable drills. | Sample all rows with backup/DR claims scored >50. Pass if each has restore/failover drill evidence, timing outcomes, integrity checks, and witness record. | Who: R6 DR owner + R8 + R15. What: restore/DR admissibility audit and replay report. Where: drill artifact store and scoring ledger. |
| R6M-07 Platform Dependency and Supply-Path Control Coverage | Rubric_0 evaluates dependency reliability, lifecycle risk, fallback viability, and platform hygiene controls. | Validate that rubric explicitly checks owner assignment, SLA/SLO tracking, EOL handling, and tested fallback for critical dependencies. Pass if critical dependency control omissions = 0. | Who: R6 platform owner + R7 + R14. What: dependency-control completeness review. Where: dependency register, risk board records, rubric mapping sheet. |
| R6M-08 Contradiction Handling Determinism | Rubric_0 resolves conflicting requirements or evidence using explicit precedence, owner, timer, and consequence rules. | Execute contradiction scenarios (for example: feature rollout request vs exhausted error budget; restore success claim vs failed drill evidence). Pass if outcome path is deterministic and Severity-1 unresolved contradictions past SLA = 0. | Who: R6 adjudicator + R2 + R7 + R8. What: contradiction scenario log, precedence table, closure timestamps. Where: adjudication tracker and governance minutes. |
| R6M-09 Evidence Admissibility Specificity | Rubric_0 defines precise admissibility rules that prevent narrative-only scoring. | Audit non-zero sampled rows. Pass if >=98% include complete `who/what/where`, timestamp, provenance hash/link, and cutoff eligibility; inadmissible evidence is excluded. | Who: R6 scorer + R5 evidence checker. What: admissibility checklist and exclusion report. Where: evidence vault and score workbook. |
| R6M-10 Evidence Replayability and Recomputation Fidelity | Independent evaluators can replay Rubric_0 scoring and recompute underlying metrics from source evidence. | Replay >=15% of scored rows including gate-sensitive rows. Pass if score variance <=5 points and gate-state outcomes match 100% for sampled rows. | Who: independent non-author scorer + R15 witness. What: replay transcript, recomputation worksheets, variance report. Where: immutable artifact store and replay runbook repository. |
| R6M-11 Anchor Separability and Monotonicity | Rubric_0 anchor levels are behaviorally distinct, testable, and increasing in rigor without overlap. | Run blind anchor calibration on common packet. Pass if adjacent-anchor ambiguity disputes <=20% and no reverse-monotonic scoring rule is found. | Who: R6 calibration lead + cross-role raters. What: ambiguity log, calibration summary, monotonicity lint output. Where: calibration workspace and scoring QA records. |
| R6M-12 Aggregation and Weighting Robustness | Rubric_0 score math is reproducible and prevents masking of critical reliability weakness. | Recompute formulas and run sensitivity test by degrading critical reliability rows. Pass if formulas reconcile exactly and masking test fails (critical weakness cannot be hidden by unrelated high scores). | Who: R6 + R3 + R15. What: formula reconciliation sheet, sensitivity analysis. Where: scoring model workbook and audit archive. |
| R6M-13 Score Inflation Resistance and High-Score Guardrails | Rubric_0 structurally prevents unsupported high scoring and detects inflation patterns. | Verify all scores >75 include independent corroboration and >90 include challenge evidence; inspect distribution jumps >15 points for approved rationale. | Who: R6 scoring owner + R15 validator. What: high-score evidence pack, jump-analysis report, rationale approvals. Where: score history database and governance dashboard. |
| R6M-14 Anti-Gaming Protocol Executability | Rubric_0 anti-gaming controls are explicit, mandatory, and actually executable each cycle. | Execute control checklist (sampling, recompute, denominator drift check, cutoff check, contradiction aging check, provenance check). Pass only if all mandatory controls run with evidence. | Who: R6 owner + R15 observer. What: anti-gaming execution checklist and challenge outputs. Where: anti-gaming run log and cycle control board. |
| R6M-15 Hard-Gate and Tripwire Coherence | Rubric_0 gate/tripwire model (`G1..G6`, `RG1..RG4`, role tripwires) is complete, precedence-ordered, and non-bypassable. | Simulate triggered combinations and precedence conflicts. Pass if every hard-gate trigger forces invalid/fail outcome and precedence path is deterministic. | Who: R6 + R12 + R7 + R15. What: gate simulation matrix, precedence map, bypass test records. Where: governance test harness and release-control records. |
| R6M-16 Operational Throughput and Decision-Latency Fit | Rubric_0 evaluation can be executed within operational cadence without delaying release or incident decisions. | Time-box dry run + live cycle measurement. Pass if scoring closes within 5 business days after cutoff, first-pass completion >=90%, and rubric-caused decision backlog = 0. | Who: R6 operations lead + R3 + R12. What: cycle timing report, rework log, pending-decision dashboard. Where: governance calendar and cycle close report. |
| R6M-17 Cross-Role Handoff and Adjudication Operability | Rubric_0 supports clear, SLA-bound handoffs and dispute closure with counterpart roles. | Sample critical handoffs (R1/R2/R7/R8/R12/R15). Pass if first-pass acceptance >=90%, silent acceptance = 0, and returned handoffs always include defect class + due date. | Who: R6 + counterpart role leads. What: handoff ledger, return reasons, SLA tracker. Where: adjudication board records and workflow system. |
| R6M-18 Versioning and Delta Re-evaluation Discipline | Rubric_0 changes are controlled, impact-assessed, and re-evaluated on affected rows/gates only with explicit reopen records. | Check each rubric delta for version hash, approvers, impact scope, and re-score evidence. Pass if unauthorized edits = 0 and impacted rows/gates were re-tested. | Who: R6 rubric owner + R11 + R15. What: version history, approved diffs, delta re-score report. Where: rubric repo and governance change log. |

## 3) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R6M-01 Runtime Governance Decision-Coverage Completeness | Critical runtime decision classes are missing. | Partial mapping exists; multiple safety-critical decisions unmapped. | Most classes mapped, but at least one critical gap remains. | >=95% mapped and all safety-critical classes covered. | Independent review confirms complete critical coverage and timely gap closure. | Two cycles with zero critical decision-coverage gaps. |
| R6M-02 SLI/SLO and Error-Budget Clause Testability | Reliability clauses are non-measurable prose. | Clauses mention metrics but omit formulas/trigger actions. | Core metrics defined; trigger-action ambiguity remains in important cases. | Clauses are measurable with formula, threshold, action, and owner. | Independent scorer reproduces clause interpretation with no critical disagreement. | Two cycles with zero ambiguous trigger-action clauses in critical scope. |
| R6M-03 Incident and Escalation Governance Evaluability | Incident governance scoring is ad hoc and non-repeatable. | Incident criteria exist but severity/escalation interpretation diverges heavily. | Criteria mostly usable but critical-case disagreement persists. | Incident scoring is consistent and replayable for critical samples. | Cross-role replay confirms deterministic severity/escalation decisions. | Two cycles with zero unresolved critical incident-scoring disputes. |
| R6M-04 Change Safety Gate Evaluability | Release safety gates are absent or non-operational in rubric logic. | Gates listed but consequences and waiver rules are unclear. | Most gates executable; some pass/fail outcomes depend on reviewer judgment. | Canary/rollback/freeze gates are deterministic and evidence-bound. | Independent release-scenario replay matches gate decisions consistently. | Two cycles with zero gate-interpretation defects in critical releases. |
| R6M-05 Capacity, Saturation, and Resilience Coverage Adequacy | Rubric omits capacity/resilience control evaluation. | Controls named but key evidence classes missing. | Coverage exists but includes material blind spots in critical services. | Required control/evidence classes are complete and testable. | Independent sampling confirms no critical control omission. | Two cycles with no missed critical capacity/resilience control class. |
| R6M-06 Backup/Restore/DR Proof Requirement Strength | Rubric accepts backup/DR claims without drill proof. | Drill proof requested inconsistently; restore integrity evidence often absent. | Restore/DR proof rules exist, but enforcement is uneven. | High scoring requires restore/failover timing and integrity proof. | Independent witness replay succeeds on sampled critical systems. | Two cycles with zero accepted backup/DR claim lacking proof evidence. |
| R6M-07 Platform Dependency and Supply-Path Control Coverage | Dependency reliability controls are missing. | Basic inventory checks exist, but fallback/EOL/SLA controls are missing. | Controls mostly present; critical dependency exceptions not consistently governed. | Full critical dependency control set with owner, lifecycle, and fallback checks. | Independent audit confirms no hidden unmanaged critical dependency risk. | Two cycles with zero unmanaged critical dependency control gaps. |
| R6M-08 Contradiction Handling Determinism | Conflicting rules are unresolved or settled informally. | Contradictions logged but no precedence/SLA consequence is defined. | Precedence exists but outcomes vary by reviewer in critical cases. | Deterministic contradiction protocol with owner and timer is operating. | Independent scenario replay yields identical outcomes across reviewers. | Two cycles with no Severity-1 contradiction aging beyond SLA. |
| R6M-09 Evidence Admissibility Specificity | Narrative claims are accepted as evidence. | Admissibility rules exist but key fields/provenance are optional. | Rules defined but enforcement is inconsistent on sampled rows. | Admissibility is explicit and consistently enforced for non-zero scores. | Independent audit finds near-zero admissibility defects and proper exclusion behavior. | Two cycles with zero material admissibility violations. |
| R6M-10 Evidence Replayability and Recomputation Fidelity | Scores cannot be replayed from evidence package. | Replay works sporadically with major score/gate mismatch. | Replay partially works; variance frequently exceeds tolerance. | Sampled rows replay within tolerance and gate outcomes match. | Independent non-author replay has high success and low variance. | Two cycles with stable replay success and no material recomputation discrepancy. |
| R6M-11 Anchor Separability and Monotonicity | Anchors are overlapping and non-testable. | Anchor text differs superficially but remains ambiguous. | Anchors partly testable; adjacent-level overlap still frequent. | Anchors are distinct, testable, and monotonic in rigor. | Calibration results show strong agreement and low ambiguity drift. | Two cycles with zero monotonicity defects and stable interpretation. |
| R6M-12 Aggregation and Weighting Robustness | Score math is undefined or non-reproducible. | Formula exists but reconciliation fails or critical masking is possible. | Formula reconciles, but masking and sensitivity behavior is not proven. | Formula reconciles exactly and sensitivity tests enforce critical-risk visibility. | Independent recomputation repeatedly matches published outputs. | Two cycles with no unexplained aggregation drift or masking defect. |
| R6M-13 Score Inflation Resistance and High-Score Guardrails | Unsupported high scores are common and unchecked. | Guardrails exist on paper but are routinely bypassed. | Guardrails applied inconsistently; inflation signals often unresolved. | >75 and >90 guardrails enforced with required evidence. | Distribution/jump checks catch and correct inflation attempts promptly. | Two cycles with zero unsupported high-score outcomes. |
| R6M-14 Anti-Gaming Protocol Executability | Mandatory anti-gaming checks are absent. | Checks listed but not run reliably each cycle. | Partial anti-gaming execution with missing mandatory controls. | All mandatory controls executed and evidenced each cycle. | Surprise challenge performance is strong and corrective actions are timely. | Two cycles with sustained anti-gaming execution and no skipped mandatory control. |
| R6M-15 Hard-Gate and Tripwire Coherence | Gate/tripwire logic is contradictory or bypassable. | Gates exist but precedence and invalidation consequences are unclear. | Most gates work, but simulations still find bypass paths. | Full precedence model works and active hard-gates always invalidate pass. | Independent red-team simulation finds no bypassable hard-gate path. | Two cycles with zero gate-bypass findings in assurance testing. |
| R6M-16 Operational Throughput and Decision-Latency Fit | Rubric process routinely misses operational decision windows. | Process is executable only with repeated deadline exceptions. | Timeliness is mixed; backlog appears during high-load periods. | Cycle SLA is met with acceptable rework and no blocked critical decision. | Throughput remains stable across release and incident-heavy cycles. | Two cycles with sustained SLA compliance and no rubric-induced decision delay. |
| R6M-17 Cross-Role Handoff and Adjudication Operability | Handoffs are undefined; disputes stall unresolved. | Handoffs named but lack acceptance criteria/SLA/escalation ownership. | Handoffs mostly defined; return loops and silent acceptance remain common. | Handoffs meet SLA with explicit accept/return criteria and closure behavior. | Independent sampling confirms low rework and deterministic adjudication outcomes. | Two cycles with no critical handoff failure causing score publication delay. |
| R6M-18 Versioning and Delta Re-evaluation Discipline | Rubric changes are uncontrolled and retroactive. | Version labels exist but approval/impact/reopen records are missing. | Change control exists; occasional scope leakage in delta re-score occurs. | Versioned, approved changes with scoped impact and required re-testing are standard. | Independent audit confirms clean change trail and correct impacted-row re-score. | Two cycles with zero unauthorized edits and complete delta re-evaluation evidence. |

## 4) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Baseline freeze check: hash Rubric_0 content, anchor table, and weight model at cycle start; reject scoring on non-hashed variants.
2. Score-band gate check: enforce `>75` independent corroboration and `>90` challenge evidence; auto-flag any exception.
3. Denominator drift check: detect silent denominator narrowing in reliability-rate claims across cycle snapshots.
4. Cutoff integrity check: reject post-cutoff evidence unless formal cycle reopen record exists.
5. Provenance check: require immutable links/hashes for logs, dashboards, and drill outputs cited in scoring.
6. Contradiction suppression check: compare contradiction register against final score packet; hidden open contradictions force escalation.
7. Replay witness rotation: require at least one non-author replay witness each cycle for sampled critical rows.
8. Waiver laundering check: detect repeated short waivers for same control without new risk treatment.
9. Gate bypass simulation: run synthetic failing release/incident scenarios to verify hard-gate invalidation still triggers.
10. Inflation jump check: any sub-dimension jump >15 points requires approved delta rationale and evidence replay.
11. Anchoring cherry-pick check: if only lower-anchor tests pass but higher anchor is assigned, auto-return row.
12. Evidence-pack completeness check: scored rows with missing `who/what/where` or source location are treated as inadmissible.
13. Cross-rater divergence check: unexplained >1-anchor divergence between independent scorers triggers adjudication replay.
14. Timeline integrity check: verify chronology `evidence capture -> scoring -> approval -> publication`; out-of-order records invalidate affected rows.

## 5) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (score caps, publication holds, and invalidation if unresolved by cutoff)
| ID | Trigger condition | Immediate effect | If unresolved at publication cutoff |
| --- | --- | --- | --- |
| R6M-TW-01 | Replay variance >5 points on >10% sampled rows | Cap `R6M-10` at `50`; mandatory replay root-cause analysis | Mark cycle `INVALID` |
| R6M-TW-02 | Any Severity-1 contradiction open past SLA | Cap `R6M-08` at `50`; publication hold | Mark cycle `INVALID` |
| R6M-TW-03 | Any mandatory anti-gaming control skipped | Cap `R6M-14` at `25`; no sub-dimension may exceed `90` | Mark cycle `INVALID` |
| R6M-TW-04 | Any score >75 lacks independent corroboration | Cap `R6M-13` at `25`; re-score affected rows | Mark cycle `INVALID` |
| R6M-TW-05 | Gate simulation finds bypass path for hard gate/tripwire logic | Cap `R6M-15` at `25`; immediate gate logic correction required | Mark cycle `INVALID` |
| R6M-TW-06 | Scoring cycle misses SLA by >2 business days due to rubric process | Cap `R6M-16` at `50`; operational remediation plan required | Publication blocked until corrected or cycle marked `INVALID` |

### Hard-fail conditions (Rubric_0 score invalid for cycle)
| ID | Hard-fail condition | Evidence test | Effect |
| --- | --- | --- | --- |
| R6M-HF-01 | Evidence fabrication, tampering, or backdated approval in scoring package (`G1`) | Hash/timestamp/provenance mismatch | Cycle result `INVALID`; forensic review mandatory |
| R6M-HF-02 | Unresolved critical contradiction at cutoff (`G2`) | Contradiction register and SLA aging audit | Cycle result `INVALID` until closed with evidence |
| R6M-HF-03 | Unresolved legal/privacy/security mandatory-control breach at release point (`G3`) | R7/R8 blocker status and control evidence audit | Cycle result `INVALID` |
| R6M-HF-04 | Critical path operability gate failed yet score published as pass (`G4`) | Operability/accessibility gate logs vs published decision | Cycle result `INVALID` |
| R6M-HF-05 | Independent replay/recompute cannot reproduce material claims (`G5`) | Witness replay failure on critical sample | Cycle result `INVALID`; full re-score required |
| R6M-HF-06 | Publication without required authority-chain approvals (`G6`) | Approval chain audit and signature/timestamp check | Cycle result `INVALID`; governance breach escalation |
| R6M-HF-07 | Any critical role score <60 without enforced overall fail (`RG1`) | Role-layer score audit | Cycle result `INVALID` |
| R6M-HF-08 | Role evidence package fails integrity/provenance checks (`RG4`) | Evidence integrity audit for affected role package | Affected role score = 0 and cycle marked `INVALID` pending remediation |
| R6M-HF-09 | Unauthorized post-cutoff rubric edit (anchors/weights/gates) affects score | Version diff without approved reopen/change record | Cycle result `INVALID`; revert and re-score |
| R6M-HF-10 | Active expired exception used to bypass reliability gate during scoring | Exception register vs score decision cross-check | Cycle result `INVALID` until exception governance corrected |

## 6) Cross-role dependencies and adjudication handoffs

| Counterpart role | Dependency into R6 meta-evaluation | R6 adjudication/handoff output | Acceptance criteria | SLA / escalation |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor / Business Owner | Governance charter, decision-right boundaries, risk appetite | Rubric_0 readiness verdict with hard-fail status and residual risk note | Decision state (`approve/conditional/reject`) and invalidation status explicitly recorded | Escalate critical governance deadlock within 1 business day |
| R1 Product Manager | Service criticality commitments and policy conflicts with delivery scope | Contradiction decisions for SLO/error-budget vs feature-scope pressure | Deterministic precedent and dated closure plan | Escalate in 2 business days for unresolved Severity-1 conflict |
| R2 Product Architect / Enterprise Architect | NFR budgets, dependency topology, resilience design assumptions | Coverage-gap findings for reliability architecture controls in Rubric_0 | No unresolved critical architecture-to-rubric contradiction | Escalate in 2 business days |
| R3 Engineering Manager | Delivery cadence constraints and ownership model for execution load | Throughput/latency feasibility decision and remediation requirements | Cycle SLA model accepted by both R3 and R6 | Escalate same cycle on repeated SLA miss risk |
| R5 QA / Test Engineer | Evidence quality, replay protocol inputs, and sample design | Joint admissibility and replay variance report | Replay tolerance met and evidence defects triaged | Escalate immediately if replay failure exceeds threshold |
| R7 Security Engineer / Architect | Security gate expectations and bypass-risk findings | Security-sensitive contradiction and gate-coherence adjudication outcomes | No pass path with active security hard gate | Immediate escalation for gate bypass vulnerability |
| R8 Privacy / Compliance / Legal | Legal cutoff constraints, retention obligations, exception controls | Compliance contradiction disposition and admissibility constraints | Mandatory legal controls mapped and unresolved blockers = 0 | Escalate within 1 business day on legal blocker |
| R12 DevOps / Release Manager | Release-control logs, approvals, and gate state evidence | Publication authorization recommendation for rubric score package | Gate-state consistency and approval chain integrity verified | Same-day escalation on release-governance inconsistency |
| R14 FinOps / Procurement / Vendor Mgmt | Cost/contract constraints that may pressure reliability controls | Decision record when cost tradeoff risks rubric integrity or score inflation | Reliability controls not weakened without approved exception path | Escalate within 2 business days on unresolved tradeoff conflict |
| R15 Internal Audit / Assurance | Independent assurance sampling, forensic checks, arbitration support | Final assurance memo and adjudication closure status | Audit replay succeeds and material exception count = 0 | Immediate escalation on integrity breach |

Adjudication rule: every handoff must be explicitly `accepted` or `returned`. Silent acceptance is invalid. Returned handoffs must include defect class, owner, due date, and resubmission timestamp.

## 7) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle point | Checklist item | Evidence artifact | Delta re-evaluation rule |
| --- | --- | --- | --- |
| Pre-cycle baseline | Freeze Rubric_0 version hash, anchors, weights, and gate definitions. | Baseline hash manifest and approval record. | Any unapproved hash change forces cycle restart. |
| Pre-cycle baseline | Refresh runtime decision-coverage matrix and unresolved-gap register. | Updated decision-to-clause trace matrix and gap log. | Any new critical gap blocks scoring start. |
| Pre-cycle baseline | Refresh contradiction catalog, precedence rules, and SLA timers. | Contradiction register with owner/timer fields. | Open Severity-1 contradiction at start requires explicit exception or delay. |
| Pre-cycle baseline | Reconfirm admissibility schema (`who/what/where`, provenance, cutoff). | Admissibility schema version and cutoff notice. | Schema change mid-cycle requires reopen approval and impacted-row re-score. |
| Calibration prep | Run anchor ambiguity lint and monotonicity check. | Anchor lint report and approved wording updates. | Any unresolved high-severity anchor defect caps related rows at `50`. |
| Calibration prep | Execute dual-rater scoring on common packet. | Calibration comparison and dispute log. | >1-anchor unexplained divergence triggers calibration rerun. |
| Anti-gaming execution | Run full mandatory anti-gaming checklist and challenge scenarios. | Anti-gaming run log, challenge outputs, corrective actions. | Skipped mandatory control triggers tripwire `R6M-TW-03`. |
| Scoring execution | Complete scoring using admissible evidence only. | Scoring ledger, admissibility audit sample, timing report. | Inadmissible scored rows must be re-scored before publication. |
| Replay assurance | Perform independent replay and recomputation sample. | Witness replay transcripts and variance report. | Variance breach triggers tripwire `R6M-TW-01` and re-score. |
| Handoff adjudication | Resolve cross-role returns/disputes with explicit decisions. | Handoff ledger and adjudication closure records. | Any unresolved critical return at cutoff blocks publication. |
| Publication gate | Apply tripwire and hard-fail checks before publishing scores. | Tripwire/hard-fail evaluation report with sign-offs. | Any active hard-fail marks cycle `INVALID`. |
| Post-cycle remediation | Convert all failed checks into SMART corrective actions. | Action register with owners, dates, verification metrics. | Unowned or undated critical action prevents cycle closure. |
| Delta implementation | Apply approved Rubric_0 changes with versioned diffs and impact tags. | Change requests, diff package, impact analysis. | Unauthorized edit triggers hard-fail `R6M-HF-09`. |
| Delta re-evaluation | Re-score impacted sub-dimensions and rerun gate/coherence tests. | Delta re-score packet and gate simulation rerun report. | Impacted rows/gates not re-tested => publication blocked. |
| Cycle close | Publish retrospective with trend deltas, repeated defect classes, and carryover risks. | Cycle retrospective and carryover risk register. | Closure requires R6 + R15 confirmation and tracked carryovers. |


---

## R7 Security Engineer / Security Architect

- source_file: `swarm_outputs/meta_rubric_role_expansions/R7_security_engineer_security_architect_rubric1.md`
- words: 4128
- lines: 139

# R7 Security Engineer / Security Architect Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 scores the quality, rigor, anti-gaming strength, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 1) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R7 evaluates whether Rubric_0 behaves like an enforceable security control system under adversarial pressure. The role validates that Rubric_0 can prevent unsafe score publication, resist security-governance gaming, and produce reproducible security-relevant rubric outcomes with clear accountability.

### Decision rights
| Decision domain | R7 authority | Non-delegable boundary | Escalation path |
| --- | --- | --- | --- |
| Security sufficiency of Rubric_0 | Approve, conditionally approve, or reject Rubric_0 for security-governed scoring cycles | Cannot approve if any security hard-fail condition is active | Escalate to R0 and R15 within 1 business day |
| Security gate precedence quality | Require rewrite when security gates can be bypassed by averaging or ordering ambiguity | No score publication with unresolved gate precedence defect | Escalate to R12 and R3 immediately when release decisions depend on affected score |
| Evidence admissibility for security rows | Enforce strict evidence schema and cutoff rules for all non-zero security-related rubric scores | No non-zero score for security rows without admissible evidence | Escalate to R15 on tamper/fabrication indicators |
| Contradiction resolution for security conflicts | Force explicit resolution of critical contradictions affecting security scoring logic | Cannot permit publication with unresolved critical contradiction | Escalate to R2 and R8 for unresolved architecture/legal conflicts |
| Anti-gaming control execution | Block scoring cycle closure if mandatory anti-gaming controls are skipped | No cycle close when mandatory controls are not evidenced | Escalate to R0 governance forum same cycle |
| High-anchor security score authorization | Challenge or cap unjustified high anchors in security-relevant rubric dimensions | No `90`/`100` without independent challenge evidence in current cycle | Escalate to R15 for independence breach |
| Rubric delta security sign-off | Accept or reject Rubric_0 deltas affecting security gate logic, evidence, or anchors | No delta promotion without impact map and targeted re-evaluation | Escalate to R12 for deployment hold |
| Emergency invalidation | Invalidate cycle scoring when hard-fail conditions compromise trust in Rubric_0 evaluation | No conditional publication when invalidation criteria are met | Escalate to R0, R3, R15 immediately |

### Meta-scoring rule
1. Allowed anchors: `0`, `25`, `50`, `75`, `90`, `100`.
2. Any non-zero anchor requires explicit `who/what/where` evidence.
3. Any active hard-fail in Section 5 invalidates Rubric_0 scoring for the cycle.

## 2) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R7M-01 Security decision-surface coverage completeness | Rubric_0 covers all security-governance decision classes needed for scoring integrity. | Build decision catalog (threat-model quality, authn/authz control quality, vuln/patch governance, secrets/crypto, supply chain, telemetry/detection, exception handling, incident handling). Pass if >=95% mapped and 100% of critical classes mapped to explicit scoring clauses. | Who: R7 lead evaluator + R3 reviewer. What: decision-to-clause trace matrix and unmapped-gap log. Where: Rubric_0 master file and role expansion references. |
| R7M-02 Security control-family coverage and non-overlap | Security control families in Rubric_0 are complete and not duplicated with conflicting criteria. | Perform overlap lint across clauses for identity, authorization, crypto, vulnerability, telemetry, supply chain, incident, and exception controls. Pass if critical family gaps = 0 and conflicting duplicate criteria = 0. | Who: R7 + R2. What: control-family map, conflict register, closure notes. Where: rubric analysis workbook and adjudication tracker. |
| R7M-03 Security gate and precedence determinism | Rubric_0 security gates/tripwires have unambiguous ordering and deterministic outcomes. | Simulate scenarios with high average scores plus triggered security gates. Pass if gate outcomes are deterministic in 100% of scenarios and no averaging path bypasses a triggered security hard gate. | Who: R7 + R12 + R15. What: gate simulation suite, precedence map, test logs. Where: governance test harness and cycle evidence archive. |
| R7M-04 Contradiction handling and closure rigor | Rubric_0 defines security contradiction classes, owners, SLA, and mandatory scoring consequences. | Inject contradictions (for example high performance score vs missing security gate evidence). Pass if all contradictions are classified, assigned, resolved or escalated within SLA, and unresolved critical contradictions block publication. | Who: R7 adjudicator + R2 + R8. What: contradiction register, SLA aging report, closure decisions. Where: adjudication board records. |
| R7M-05 Evidence admissibility specificity | Rubric_0 evidence rules for security-related scoring are precise enough to reject narrative-only claims. | Sample non-zero security-relevant rows. Pass if >=98% include `who/what/where/time/version` and post-cutoff evidence is excluded from the current cycle. | Who: R7 scorer + R5 verifier. What: admissibility audit checklist and exclusion log. Where: evidence vault and scoring ledger. |
| R7M-06 Evidence provenance integrity and tamper-evidence | Rubric_0 requires immutable, tamper-evident provenance for security-relevant scoring evidence. | Validate hash/timestamp linkage and signer identity on sampled evidence. Pass if provenance chain completeness >=98% and tamper anomalies are zero unresolved by cycle close. | Who: R7 + R15 forensic reviewer. What: provenance validation report, hash audit, anomaly tickets. Where: immutable store, signing logs, forensic workpapers. |
| R7M-07 Evidence replayability and recompute fidelity | Independent reviewers can reproduce security-relevant rubric scores from source evidence. | Replay >=15% sampled rows including all security-critical gate rows. Pass if anchor variance <=1 level, numeric variance <=5 points, and gate states match 100%. | Who: independent reviewer (non-author) + R15 witness. What: replay transcript, recompute sheets, variance report. Where: replay workspace and immutable evidence package. |
| R7M-08 Anchor specificity, separability, and monotonicity | Security-related anchors in Rubric_0 are behaviorally distinct, testable, and stricter as score increases. | Run anchor lint and blind calibration. Pass if every security sub-dimension has observable criteria at each anchor, no inversion (`90` easier than `75`), and ambiguity-driven disagreement <=20%. | Who: R7 calibration owner + cross-role raters. What: lint output, calibration report, ambiguity log. Where: calibration repository and scoring QA folder. |
| R7M-09 Adversarial test realism in rubric design | Rubric_0 requires adversarial validation of scoring claims, not checklist-only compliance. | Verify rubric requires challenge tests (red/purple simulation, replay attacks, exception abuse probes) for high anchors. Pass if all `90+` paths require current-cycle adversarial evidence. | Who: R7 + R5 + R15. What: adversarial requirement matrix, executed challenge logs. Where: anti-gaming runbook and challenge archive. |
| R7M-10 Exploitability weighting and severity calibration quality | Rubric_0 weights security findings using exploitability and blast radius, not count-based severity theater. | Recompute sampled scoring rows with exploitability factors. Pass if KEV/actively exploitable findings always outrank equivalent non-exploitable findings and severity tie-breakers are explicit. | Who: R7 + R14 risk-cost observer. What: severity rubric, recompute sheet, calibration notes. Where: scoring workbook and vulnerability policy annex. |
| R7M-11 Exception governance and compensating-control testability | Rubric_0 controls exception lifecycle with expiry, owner, rationale, and tested compensating controls. | Sample exceptions used in scoring decisions. Pass if active expired exceptions = 0, renewal without new evidence = 0, and compensating controls are tested at required cadence. | Who: R7 governance owner + R8 + R15. What: exception register audit, control test reports, renewal decisions. Where: GRC system and exception ledger. |
| R7M-12 Temporal freshness and staleness resistance | Rubric_0 enforces freshness windows so stale security evidence cannot support current-cycle high scores. | Audit evidence age against policy windows (for example threat-model updates, control-test recency). Pass if stale evidence usage in non-zero rows <=2% and none on security critical gates. | Who: R7 + R3. What: freshness audit, stale-evidence exception log. Where: scoring package and evidence metadata index. |
| R7M-13 Anti-gaming protocol executability | Rubric_0 anti-gaming steps are concrete, assignable, and executed every cycle. | Verify execution of required controls: independent sampling, surprise challenge, raw-log recompute, cutoff enforcement, contradiction aging checks, and provenance checks. Pass only if all mandatory steps have evidence. | Who: R7 cycle owner + R15 observer. What: anti-gaming checklist, execution logs, failed-control actions. Where: cycle close packet and control dashboard. |
| R7M-14 Score inflation resistance and high-score proof thresholds | Rubric_0 structurally resists inflated security-related scoring. | Enforce guardrails: `>75` requires independent corroboration; `>90` requires successful adversarial challenge; detect score jumps >15 points cycle-over-cycle and require approved rationale. | Who: R7 scorer + R15 validator. What: high-score evidence pack, distribution trend report, jump-approval records. Where: historical scoring ledger and audit dashboard. |
| R7M-15 Cross-role security handoff operability | Rubric_0 defines clear, enforceable cross-role handoffs for security-related scoring adjudication. | Sample handoffs with R1/R2/R6/R8/R12/R15. Pass if first-pass acceptance >=90%, silent acceptance = 0, and returned handoffs always include defect class, owner, due date, and resubmission timestamp. | Who: R7 + counterpart role leads. What: handoff matrix, SLA report, return-defect log. Where: adjudication tracker and governance records. |
| R7M-16 Rubric change control and delta re-evaluation integrity | Rubric_0 changes affecting security scoring are versioned, impact-assessed, and re-evaluated before publication. | Verify every changed security-relevant clause has approved diff, impact map, effective date, and targeted re-score plus gate re-simulation. Pass if unauthorized edits = 0. | Who: R7 rubric owner + R12 + R15. What: change dossier, impact map, delta re-score report. Where: rubric repository and release governance log. |

## 3) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R7M-01 Security decision-surface coverage completeness | No security decision catalog; major classes missing. | Partial mapping exists; multiple critical classes absent. | Most classes mapped; at least one critical class unmapped. | >=95% classes mapped and all critical classes mapped. | Independent review confirms mapping completeness with no critical gaps. | Two consecutive cycles with zero critical mapping gaps and clean independent verification. |
| R7M-02 Security control-family coverage and non-overlap | Control-family coverage is fragmented and contradictory. | Families listed but conflicts and gaps are frequent. | Coverage mostly present; some duplicate/conflicting criteria remain. | Complete family coverage with conflict register resolved for critical items. | Independent lint finds no critical conflict or family gap. | Two cycles with stable complete coverage and zero critical overlap defects. |
| R7M-03 Security gate and precedence determinism | Gate order undefined; outcomes depend on scorer interpretation. | Gates exist but precedence ambiguous and bypassable. | Most cases deterministic; edge-case bypasses remain. | Deterministic precedence across standard and edge scenarios. | Independent simulations confirm no bypass path under active security gate. | Two cycles with zero precedence defects and successful adversarial bypass tests. |
| R7M-04 Contradiction handling and closure rigor | Contradictions are untracked or ignored. | Contradictions tracked ad hoc without SLA or owner. | Workflow exists but critical contradictions can age unresolved. | Contradictions classified, owned, and resolved/escalated within SLA. | Independent replay shows deterministic contradiction outcomes and enforced block on unresolved critical items. | Two cycles with no aged critical contradiction and complete replayable closure trail. |
| R7M-05 Evidence admissibility specificity | Narrative-only claims accepted for non-zero scores. | Evidence rules exist but required fields are vague/incomplete. | Required fields mostly defined; enforcement inconsistent. | Admissibility schema enforced with high completeness and cutoff discipline. | Independent audit confirms sampled non-zero rows all satisfy admissibility requirements. | Two cycles with zero admissibility breaches on independent audit sample. |
| R7M-06 Evidence provenance integrity and tamper-evidence | Provenance chain absent or unverifiable. | Partial provenance exists; signer/time/hash gaps are common. | Provenance controls present but anomalies remain unresolved. | Provenance chain completeness high with timely anomaly resolution. | Independent forensic checks show tamper-evident integrity and chain continuity. | Two cycles with zero unresolved tamper anomalies and full provenance verification. |
| R7M-07 Evidence replayability and recompute fidelity | Scores cannot be replayed from evidence. | Replay possible only with author interpretation and large variance. | Partial replay works; gate-state mismatches or variance above tolerance persist. | Sampled replay succeeds with acceptable score variance and matching gate state. | Independent replay achieves high fidelity and clean gate-state parity. | Two independent teams reproduce sampled results with no material variance. |
| R7M-08 Anchor specificity, separability, and monotonicity | Anchors are subjective, overlapping, or incomplete. | Anchors present but mostly non-testable and ambiguous. | Testable anchors exist, but adjacent anchor overlap remains significant. | Anchors are observable, distinct, and monotonic for most security rows. | Calibration demonstrates low ambiguity-driven disagreement and no inversions. | Two cycles with stable calibration and zero monotonicity defects. |
| R7M-09 Adversarial test realism in rubric design | High scores require no adversarial evidence. | Adversarial checks mentioned but optional or undefined. | Some high-score paths require challenge tests; coverage incomplete. | High-score paths require defined adversarial tests with pass criteria. | Independent challenge execution validates test realism and scoring consequences. | Two cycles with no unsupported `90+` and consistently executed adversarial checks. |
| R7M-10 Exploitability weighting and severity calibration quality | Severity scoring ignores exploitability and blast radius. | Exploitability considered inconsistently and without defined tie-breakers. | Defined severity model exists but applied unevenly. | Exploitability and impact weighting are explicit and consistently applied. | Independent recompute confirms calibrated ordering and consistent severity outcomes. | Two cycles with stable calibration and no misprioritized critical exploitable conditions. |
| R7M-11 Exception governance and compensating-control testability | Exceptions are informal, expired, or ownerless. | Exception register exists but expiry/control tests are unreliable. | Governance exists; renewals and control-test quality inconsistent. | Exception lifecycle is enforced with tested compensating controls and expiry discipline. | Independent audit confirms no expired active exceptions and valid control-test evidence. | Two cycles with declining exception risk exposure and zero unauthorized renewal. |
| R7M-12 Temporal freshness and staleness resistance | Stale evidence is routinely used for non-zero scoring. | Freshness windows absent or not enforceable. | Freshness policy exists; stale evidence exceptions are frequent. | Freshness rules enforced with minimal stale usage and none on critical gates. | Independent audit verifies freshness compliance and proper stale-evidence exclusion. | Two cycles with zero stale-evidence use in critical scoring paths. |
| R7M-13 Anti-gaming protocol executability | Anti-gaming controls absent or non-operational. | Controls documented but execution evidence largely missing. | Some mandatory controls executed; gaps remain in required steps. | All mandatory anti-gaming steps executed and evidenced each cycle. | Independent observer verifies execution quality and timely closure of failures. | Two cycles with complete execution and demonstrated detection of attempted gaming. |
| R7M-14 Score inflation resistance and high-score proof thresholds | Unsupported high scores are common. | High-score guardrails exist on paper but are bypassed. | Guardrails partly enforced; unexplained high-score jumps persist. | Guardrails enforced with independent corroboration and jump review. | Distribution controls consistently detect and correct inflation attempts. | Two cycles with zero unsupported high-score outcomes and stable score integrity. |
| R7M-15 Cross-role security handoff operability | Handoffs are undefined or unusable. | Handoffs exist but acceptance criteria/SLA are missing. | Handoffs partially operational; return loops and silent acceptance occur. | Handoffs are explicit, SLA-backed, and mostly accepted first pass. | Independent sample confirms high first-pass acceptance and traceable return handling. | Two cycles with no silent acceptance and sustained high-quality adjudication handoffs. |
| R7M-16 Rubric change control and delta re-evaluation integrity | Security-relevant rubric changes are untracked and unapproved. | Version labels exist but no impact map or re-evaluation. | Change control exists with occasional missing delta re-score or gate re-test. | Approved diff, impact map, and delta re-evaluation are standard for all security changes. | Independent audit confirms no unauthorized edit and full impacted-row re-evaluation. | Two cycles with complete change lineage and deterministic post-delta outcomes. |

## 4) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Baseline-hash freeze: hash Rubric_0 version, anchor tables, and scoring template at cycle start; invalidate scoring against unapproved hashes.
2. High-anchor proof gate: block `90`/`100` unless independent reviewer and current-cycle adversarial challenge evidence are both present.
3. Evidence chronology check: enforce `capture -> score -> approve`; out-of-order timelines are inadmissible.
4. Backfill exclusion: evidence created after cycle cutoff cannot increase current-cycle score without formal cycle reopen record.
5. Raw-log recompute: recompute sampled security-relevant scores from raw evidence sources; dashboard-only summaries are insufficient.
6. Adversarial spot-check: run at least one surprise contradiction and one surprise exploitability-weighting challenge each cycle.
7. Denominator integrity check: detect score inflation via narrowed sampling populations or removed failed rows without approved rationale.
8. Exception laundering detection: flag repeated short renewals of the same exception and force executive re-approval.
9. Gate-bypass simulation: inject active security hard-gate conditions and verify scoring engine cannot produce pass outcome.
10. Provenance tamper scan: verify hash/signature integrity on sampled evidence and compare against immutable ledger.
11. Reviewer-independence enforcement: prohibit a reviewer from authoring evidence and validating its own high-anchor score.
12. Suppression detection: compare declared zero-defect or low-risk results to raw contradiction and exception registers for hidden issues.

## 5) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (caps, holds, mandatory remediation)
| ID | Trigger condition | Immediate effect |
| --- | --- | --- |
| R7M-TW-01 | Replay variance exceeds tolerance (anchor variance >1 or score variance >5 points) on >10% sampled rows | Cap R7M-07 at `50`; require replay root-cause and re-sample before publication |
| R7M-TW-02 | Any mandatory anti-gaming control in Section 4 is not executed in cycle | Cap R7M-13 at `25`; block any sub-dimension from scoring above `90` |
| R7M-TW-03 | Any `>75` score lacks independent corroboration evidence | Cap R7M-14 at `25`; re-score affected rows |
| R7M-TW-04 | First-pass cross-role security handoff acceptance drops below 80% | Cap R7M-15 at `50`; require handoff contract correction |
| R7M-TW-05 | Stale evidence used in any security-critical gate scoring decision | Cap R7M-12 at `25`; invalidate affected gate result until refreshed evidence provided |
| R7M-TW-06 | Cycle scoring publication is delayed by >2 business days due to unresolved security contradiction | Cap R7M-04 at `50`; escalate to R0 and R3 |

### Hard-fail conditions (Rubric_0 cycle score is invalid)
| ID | Hard-fail condition | Evidence test | Effect |
| --- | --- | --- | --- |
| R7M-HF-01 | Evidence fabrication, tampering, forged provenance, or backdated approval in rubric-evaluation package | Forensic integrity audit (hash/signature/timestamp mismatch) | Mark cycle `INVALID`; full forensic review required |
| R7M-HF-02 | Published score contradicts active security hard gate or security tripwire with blocking effect | Gate-state log vs published decision mismatch | `INVALID`; revoke published result and rerun cycle |
| R7M-HF-03 | Unresolved critical contradiction remains open at publication time | Contradiction register shows open critical item past SLA | `INVALID`; no publication until adjudication closure |
| R7M-HF-04 | Non-zero security-relevant scores lack required admissibility fields on >10% sampled rows | Admissibility audit extrapolation above threshold | `INVALID`; evidence remediation and full re-score required |
| R7M-HF-05 | Independent replay cannot reproduce security-critical gate outcomes | Replay gate-state mismatch on sampled critical rows | `INVALID`; replay remediation and full gate re-simulation required |
| R7M-HF-06 | Unauthorized rubric change to security anchors/weights/gates after cutoff affects scoring | Version-control diff without approved change record | `INVALID`; revert to approved baseline and re-score |
| R7M-HF-07 | Expired exception is used to justify continued non-zero score in a security-critical rubric row | Exception register and scoring linkage mismatch | `INVALID`; associated rows reset and cycle rerun |
| R7M-HF-08 | Reviewer independence breach on high anchors (`90+`) is confirmed | Role-separation audit shows same person authored, scored, and validated | `INVALID`; affected rows void and independent reassessment required |

## 6) Cross-role dependencies and adjudication handoffs

| Counterpart role | Dependency into R7 meta-evaluation | R7 handoff output | Acceptance criteria | SLA / escalation |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor / Business Owner | Risk appetite and governance authority for strictness of invalidation policy | Security meta-readiness verdict (`approve`, `conditional`, `reject`) with residual-risk statement | Decision is signed with explicit risk treatment and timeline | Escalate in 1 business day for unresolved blocking hard-fail |
| R2 Product Architect / Enterprise Architect | Structural contradiction patterns and boundary model changes in Rubric_0 | Contradiction severity classification and precedence correction requests | No unresolved critical architecture-security contradiction | Escalate in 2 business days if precedence conflict remains |
| R3 Engineering Manager | Cycle throughput constraints, adjudication latency data | Security gating operability feedback and required process corrections | Security controls remain enforceable without silent bypass | Escalate same day if release decision blocked by rubric ambiguity |
| R5 QA / Test Engineer | Calibration variance data and test harness support for replay/challenge runs | Security anchor calibration adjustments and reproducibility defects | Calibration variance within approved tolerance and gates reproducible | Escalate within cycle on failed reproducibility thresholds |
| R6 SRE / Platform Engineer | Operational logging/reliability evidence chain for replay and gate-state validation | Telemetry/evidence integrity requirements for scoring infrastructure | Critical evidence streams are complete and tamper-evident | Escalate immediately for missing critical evidence chain |
| R8 Privacy / Compliance / Legal | Legal admissibility and retention constraints for security evidence | Mapped security evidence controls and contradiction dispositions with legal impact | No unresolved legal conflict on evidence use or exception handling | Escalate within 1 business day for legal blocking issues |
| R12 DevOps / Release Manager | Scoring pipeline behavior, version promotion workflow, cutoff enforcement mechanics | Block/allow recommendation for rubric version promotion and publication controls | Promotion path automatically blocks on active hard-fail | Escalate immediately if pipeline allows blocked publication |
| R15 Internal Audit / Assurance | Independent replay, forensic validation, and score integrity assurance sampling | Final assurance-aligned adjudication package with closure obligations | Assurance replay passes and material integrity exceptions are zero unresolved | Escalate immediately on tampering or independence breach |

Adjudication handoff rule: every handoff outcome must be explicit `accepted` or `returned`; silent acceptance is invalid. Returned items must include defect class, owner, due date, and resubmission timestamp.

## 7) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle phase | Checklist item | Evidence artifact | Pass criterion |
| --- | --- | --- | --- |
| Pre-cycle baseline | Freeze approved Rubric_0 security-relevant version, anchors, weights, and gate logic. | Baseline hash manifest with approvals. | 100% of scoring uses frozen baseline artifacts. |
| Pre-cycle baseline | Refresh security decision-surface trace map and unresolved gap register. | Updated trace matrix and gap log. | No unresolved critical decision-coverage gap. |
| Pre-cycle baseline | Refresh contradiction taxonomy, owner assignment, and SLA clock rules. | Contradiction policy and current register snapshot. | Critical contradictions open at cycle start = 0. |
| Calibration prep | Run security-anchor lint for monotonicity, observability, and overlap. | Anchor lint report with resolved defects. | Zero unresolved high-severity anchor defects. |
| Calibration prep | Execute dual-rater calibration on representative security meta-evidence packet. | Calibration variance report and adjudication notes. | Gate-state agreement = 100%; variance within approved threshold. |
| Mid-cycle control | Perform independent replay and recompute on >=15% sampled rows including security-critical gates. | Replay transcript and variance summary. | Replay thresholds met; no gate-state mismatch. |
| Mid-cycle control | Execute mandatory anti-gaming controls (sampling, surprise challenge, recompute, cutoff, provenance checks). | Anti-gaming execution checklist and logs. | All mandatory controls completed with evidence. |
| Mid-cycle control | Audit high-anchor (`90+`) rows for independent corroboration and adversarial challenge proof. | High-anchor audit pack. | 100% high anchors satisfy proof requirements. |
| Pre-close | Recompute severity/exploitability calibration on sampled rows and verify ordering consistency. | Calibration recompute worksheet. | No misordered critical exploitability cases. |
| Pre-close | Apply tripwire/hard-fail checks before score publication. | Tripwire and hard-fail clearance report. | No active hard-fail; or cycle marked `INVALID`. |
| Delta implementation | For each approved Rubric_0 change, produce row-level impact map and targeted re-score plan. | Change dossier with impact mapping. | Every changed security-relevant row mapped to re-evaluation action. |
| Delta re-evaluation | Re-score impacted rows, rerun gate precedence simulations, and revalidate contradiction outcomes. | Delta re-score report and gate simulation outputs. | No new critical contradiction or gate bypass introduced. |
| Cycle close | Publish lessons learned and prioritized remediation backlog for Rubric_0 quality defects. | Retrospective report and remediation register. | 100% critical defects assigned owner, due date, and verification metric. |


---

## R8 Privacy / Compliance / Legal

- source_file: `swarm_outputs/meta_rubric_role_expansions/R8_privacy_compliance_legal_rubric1.md`
- words: 4769
- lines: 152

# R8 Privacy / Compliance / Legal Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 evaluates the quality, rigor, anti-gaming strength, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 1) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R8 evaluates whether Rubric_0 functions as an enforceable legal/privacy/compliance control system under release pressure, not a policy narrative. The role is accountable for validating obligation coverage, contradiction safety, evidence integrity, replayability, inflation resistance, and release-veto enforceability inside Rubric_0.

### Decision rights (R8 meta-evaluator)
| Decision domain | R8 authority | Non-delegable boundary | Escalation path |
| --- | --- | --- | --- |
| Rubric_0 legal/compliance readiness | Approve, conditionally approve, or reject Rubric_0 for cycle use from privacy/legal perspective | Cannot approve if any hard-fail condition in Section 6 is active | Escalate to R0 and R15 within 1 business day |
| Obligation-to-control coverage quality | Final R8 judgment on whether Rubric_0 covers applicable obligations with enforceable scoring consequences | Cannot accept any mandatory obligation family that is unmapped or non-actionable | Escalate to R2 and R1 for structural gap remediation |
| Lawful basis/consent/DSAR rule quality | Final R8 judgment on legal-rights governance adequacy in Rubric_0 criteria | Cannot permit non-zero scoring where lawful basis, consent, or DSAR evidence rules are non-replayable | Escalate to R5 and R12 for scoring pipeline correction |
| Contradiction precedence quality | Joint authority on legal/privacy contradiction protocol sufficiency | Cannot permit publication with unresolved Severity-1 legal/privacy contradiction | Escalate to R2, R7, and R15 immediately |
| Evidence admissibility and provenance quality | Final R8 decision on legal defensibility of evidence requirements | Cannot accept mutable, backfilled, or provenance-incomplete evidence for non-zero scores | Escalate to R15 forensic review on integrity signals |
| High-anchor authorization quality | Challenge or cap unjustified 90/100 assignments on compliance-relevant rows | No `90`/`100` without independent validation and same-cycle adversarial evidence | Escalate to R15 on independence breaches |
| Release-veto enforceability quality | Validate Rubric_0 blocks pass/publication under legal blockers without discretionary bypass | Cannot accept scoring logic that allows pass with active legal/compliance blocker | Escalate to R12 and R0 same cycle |
| Rubric delta promotion quality | Approve/return privacy/legal-impacting Rubric_0 deltas for next cycle | No promotion without impact map, targeted re-score, and gate replay evidence | Escalate to R11 and R15 for change-control breach |

### Meta-scoring admissibility rules
- Allowed anchors: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires explicit admissible `who/what/where` evidence.
- No sub-dimension may score above `50` without replayable raw evidence.
- No sub-dimension may score above `75` without independent reviewer validation (aligned with `RG2`).
- No sub-dimension may score above `90` without same-cycle adversarial challenge evidence.
- Evidence created after cycle cutoff is excluded unless a formally approved reopen record exists.

## 2) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R8M-01 Obligation-to-Control Coverage Completeness | Rubric_0 fully covers applicable legal, regulatory, contractual, and policy obligations with enforceable scoring consequences. | Build obligation catalog from `R8` role scope plus `A6 D4.1-D4.6`; pass if critical obligation-family coverage is 100%, unmapped critical family count = 0, and each mapped family has explicit cap/fail logic. | Who: R8 lead evaluator + legal counsel + R15 observer. What: obligation-to-rubric matrix, gap register, closure approvals. Where: Rubric_0 master, role expansion pack, legal/GRC obligation register. |
| R8M-02 Regulatory-Change Intake and Effective-Date Governance Quality | Rubric_0 defines auditable criteria for detecting legal changes, triaging applicability, implementing controls, and preventing effective-date misses. | Verify criteria require triage SLA, owner assignment, effective-date readiness evidence, and escalation for overdue implementation; replay two historical change scenarios and confirm deterministic scoring outcomes. | Who: legal ops lead + compliance manager + R8 evaluator. What: change-scenario replay sheet, triage-SLA mapping, scoring consequence log. Where: legal watchlist archive, Rubric_0 criteria tables, adjudication records. |
| R8M-03 Lawful-Basis and Purpose-Limitation Evaluability | Rubric_0 requires enforceable lawful-basis, purpose-tagging, and prohibited-use controls for non-zero scores. | Confirm scoring rows mandate lawful basis evidence, purpose boundaries, and runtime conformance tests; pass if no high-anchor path allows policy-only evidence without runtime validation. | Who: privacy counsel + data steward + R8 evaluator. What: lawful-basis rule audit, purpose-tag control crosswalk. Where: Rubric_0 rows, RoPA/purpose registry, scoring workbook samples. |
| R8M-04 Consent Versioning and Withdrawal Propagation Evaluability | Rubric_0 can reliably evaluate consent-state versioning, withdrawal handling, and downstream propagation SLAs. | Check that criteria include consent event lineage, withdrawal propagation SLA, and synthetic withdrawal testing for high anchors; verify deterministic penalty path when propagation evidence is missing. | Who: privacy engineer + QA reviewer + R8 evaluator. What: consent-governance criteria audit, synthetic-withdrawal requirement map. Where: Rubric_0 anchors, consent evidence schema, anti-gaming controls. |
| R8M-05 Notice-to-Practice and Disclosure Fidelity Evaluability | Rubric_0 can detect and penalize drift between disclosed data practices and actual behavior. | Validate explicit tests for notice-to-telemetry diff, mismatch severity thresholds, remediation SLA, and public-claim hold logic; run sample drift scenario to verify scoring consequence. | Who: legal writer + telemetry owner + R8 evaluator. What: drift-test scenario results, disclosure-control mapping. Where: Rubric_0 compliance rows, notice governance artifacts, adjudication notes. |
| R8M-06 Data Inventory, Classification, and Handling-Control Evaluability | Rubric_0 includes enforceable checks for regulated-data discovery, classification integrity, and handling controls. | Pass if rubric requires full regulated-store coverage, shadow-store detection checks, class-based control evidence, and sample-based validation criteria with explicit failure effects. | Who: data governance lead + platform owner + R8 evaluator. What: classification-control trace matrix, shadow-store challenge results. Where: Rubric_0 criteria, data catalog exports, control evidence index. |
| R8M-07 Processor/DPA/Subprocessor Governance Evaluability | Rubric_0 can evaluate third-party data processors using contractual, risk, and operational controls. | Verify rows require current DPA, risk tiering, reassessment cadence, subprocessor transparency, and blocking logic for missing critical vendor controls; simulate onboarding case with missing DPA and confirm cap/fail behavior. | Who: vendor risk lead + legal counsel + R8 evaluator. What: processor-governance test matrix, onboarding simulation output. Where: Rubric_0 role rows, vendor risk platform records, contract registry. |
| R8M-08 Cross-Border Transfer and Jurisdiction-Control Evaluability | Rubric_0 can evaluate legal transfer mechanisms, data-residency constraints, and jurisdictional control evidence. | Confirm criteria require transfer register completeness, mechanism validity/expiry checks, boundary testing, and explicit hard-fail consequence for unauthorized transfer or expired mechanism. | Who: privacy counsel + cloud/platform owner + regional compliance lead. What: transfer-control criteria audit and scenario replay. Where: Rubric_0 compliance rows, transfer register, boundary test logs. |
| R8M-09 Retention, Legal-Hold, and Deletion Governance Evaluability | Rubric_0 can evaluate retention enforcement, legal-hold discipline, and deletion verification across storage surfaces. | Verify rubric mandates retention schedule mapping, hold approval metadata, seeded deletion tests (primary/replica/analytics), and deterministic fail path for unjustified expired-data retention. | Who: records manager + legal reviewer + data platform owner. What: retention/deletion criteria audit, seeded-record challenge evidence. Where: Rubric_0 lifecycle/compliance rows, hold register, deletion reports. |
| R8M-10 DSAR Identity, Fulfillment, and Statutory-Clock Evaluability | Rubric_0 can evaluate rights-request intake, identity proofing, response quality, and deadline compliance. | Check criteria include statutory-clock calculation from raw timestamps, identity verification quality controls, fulfillment QA, and fail logic for missed deadlines without lawful extension. | Who: privacy operations lead + customer ops lead + legal reviewer. What: DSAR criteria test sheet, timestamp recomputation sample. Where: Rubric_0 compliance rows, DSAR tracker, case evidence archive. |
| R8M-11 Breach Reportability and Notification-Timeline Evaluability | Rubric_0 can evaluate incident legal triage, reportability decisions, and notification timeline governance by jurisdiction. | Confirm rubric requires decision-clock evidence, legal approval chain, multi-jurisdiction timeline controls, and drill evidence; simulate missed-clock scenario and verify non-bypassable fail impact. | Who: incident legal counsel + security lead + R8 evaluator. What: breach-timeline governance audit, drill scenario replay. Where: Rubric_0 D4.6-related rows, incident records, notification playbooks. |
| R8M-12 Evidence Admissibility, Provenance, and Audit Defensibility Rigor | Rubric_0 evidence rules are legally defensible, immutable, and sufficient for independent assurance. | Audit whether non-zero scoring requires `who/what/where/time/version/hash`, cutoff enforcement, retrieval SLA, and chain-of-custody checks; verify screenshot-only evidence cannot support anchors above `50`. | Who: R8 evaluator + R15 assurance reviewer + evidence custodian. What: admissibility schema audit, provenance-check report, retrieval test results. Where: Rubric_0 evidence rules, evidence vault, audit logs. |
| R8M-13 Contradiction-Handling and Legal-Precedence Determinism | Rubric_0 contradiction protocol resolves legal/privacy conflicts deterministically with severity, precedence, SLA, and score impact. | Validate presence and enforceability of `CR-01/CR-04/CR-09/CR-12`-class logic; run contradiction replay and confirm unresolved Severity-1 contradiction blocks publication. | Who: R8 adjudicator + R2 + R7 + R15. What: contradiction replay packet, SLA-aging report, closure evidence. Where: Rubric_0 contradiction protocol, adjudication register, cycle minutes. |
| R8M-14 Independent Replayability and Recomputation Fidelity | Rubric_0 supports independent re-scoring of privacy/compliance claims with stable outcomes. | Replay >=15% sampled rows (including lawful-basis, DSAR, transfer, notification rows); pass if score variance <=5 points, anchor drift <=1 level, and gate state parity = 100%. | Who: independent non-author scorer + R15 witness + R8 observer. What: replay transcripts, recompute worksheets, variance register. Where: immutable evidence store, scoring workbook, replay runbook. |
| R8M-15 Score Inflation Resistance and High-Anchor Guardrails | Rubric_0 prevents inflated privacy/compliance scores via weak evidence, denominator manipulation, or approval bias. | Verify `>75` requires independent corroboration, `>90` requires adversarial evidence, denominator freeze is enforced, and unexplained 90+ density jump >15 points triggers mandatory rescore. | Who: R8 scoring owner + R15 validator + R0 observer. What: high-score audit pack, denominator-drift report, distribution trend analysis. Where: historical score ledger, approval records, anti-gaming logs. |
| R8M-16 Cross-Role Handoff, Release-Veto Enforceability, and Operational Fit | Rubric_0 enables executable legal/compliance handoffs and enforces release vetoes without silent bypass or cycle paralysis. | Sample handoffs with R1/R2/R7/R12/R15; pass if first-pass acceptance >=90%, silent acceptance = 0, returned handoffs include defect class+owner+due date, release veto bypass count = 0, and cycle close <=5 business days after cutoff. | Who: R8 lead + counterpart role leads + R12 workflow owner. What: handoff SLA report, veto audit log, cycle-timing report. Where: adjudication tracker, release governance board records, cycle close package. |

## 3) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R8M-01 Obligation-to-Control Coverage Completeness | Obligation families are largely absent from Rubric_0. | Partial mapping exists with major mandatory-family gaps. | Most families mapped, but critical gaps or missing consequences remain. | All mandatory families mapped with enforceable scoring consequences. | Independent legal sample confirms complete critical-family coverage and accurate mappings. | Two consecutive cycles with zero critical mapping gaps and no material mapping defects. |
| R8M-02 Regulatory-Change Intake and Effective-Date Governance Quality | No legal-change intake/effective-date criteria are defined. | Intake exists but lacks SLA, ownership, or consequence logic. | Criteria exist with partial SLA and weak overdue escalation rules. | Intake, triage, effective-date readiness, and escalation are explicit and testable. | Independent replay of sampled change events confirms deterministic scoring outcomes. | Two cycles with zero overdue applicable-change handling defects in independent audit. |
| R8M-03 Lawful-Basis and Purpose-Limitation Evaluability | Rubric allows scoring without lawful-basis controls. | Lawful basis is mentioned but remains narrative and non-testable. | Core controls exist but edge-purpose enforcement is inconsistent. | Lawful-basis and purpose-limitation tests are explicit and enforceable. | Independent event-log sampling confirms Rubric_0 criteria detect misuse reliably. | Two cycles with no accepted non-zero lawful-basis score lacking runtime evidence. |
| R8M-04 Consent Versioning and Withdrawal Propagation Evaluability | Consent governance is absent from evaluable criteria. | Consent exists as policy text only; no propagation test expectations. | Core consent checks exist but downstream propagation proof is inconsistent. | Versioned consent and withdrawal-propagation criteria are explicit with penalties. | Independent synthetic-withdrawal challenge confirms criteria are operationally discriminative. | Two cycles with zero high-anchor consent scores lacking propagation proof. |
| R8M-05 Notice-to-Practice and Disclosure Fidelity Evaluability | Rubric cannot detect notice/practice drift. | Drift checks are optional or non-measurable. | Drift checks exist but mismatch severity and remediation rules are weak. | Drift detection, severity thresholds, and remediation SLA are enforceable. | Independent challenge confirms material mismatches are consistently penalized. | Two cycles with zero material drift escapes in sampled scoring outcomes. |
| R8M-06 Data Inventory, Classification, and Handling-Control Evaluability | Rubric omits classification and handling controls for regulated data. | Partial classification checks with major blind spots. | Most controls present but shadow-store or handling validation is weak. | Full regulated-store and handling-control evaluation criteria are operational. | Independent store sampling confirms criteria detect classification/control gaps reliably. | Two cycles with zero critical classification-control blind spots in audit samples. |
| R8M-07 Processor/DPA/Subprocessor Governance Evaluability | Third-party compliance governance is absent or non-scored. | DPA/risk checks are listed but unenforceable or optional. | Governance criteria exist but allow critical vendor gaps without deterministic penalty. | Critical vendor governance criteria are explicit with blocking consequences. | Independent onboarding simulation confirms missing DPA/risk evidence is penalized correctly. | Two cycles with no accepted critical-vendor score lacking required governance evidence. |
| R8M-08 Cross-Border Transfer and Jurisdiction-Control Evaluability | Transfer/jurisdiction controls are not evaluable in Rubric_0. | Controls listed without mechanism validity or expiry enforcement. | Major transfer controls exist but edge-jurisdiction handling is inconsistent. | Transfer register, mechanism validity, and jurisdiction tests are enforceable. | Independent boundary replay confirms unauthorized/expired transfers trigger expected fail path. | Two cycles with zero transfer-control scoring escapes on independent audit sample. |
| R8M-09 Retention, Legal-Hold, and Deletion Governance Evaluability | Retention/deletion governance criteria are absent. | Retention policy referenced but legal-hold/deletion verification is non-testable. | Core controls exist with partial multi-store verification expectations. | Retention, hold, and deletion verification rules are explicit and enforceable. | Independent seeded-record challenge confirms deterministic score outcomes for failures. | Two cycles with zero accepted high-anchor retention scores lacking deletion/hold proof. |
| R8M-10 DSAR Identity, Fulfillment, and Statutory-Clock Evaluability | Rubric cannot evaluate DSAR legal compliance. | DSAR criteria exist without identity-proofing or statutory clock logic. | Core DSAR checks exist but raw timestamp recomputation and QA requirements are weak. | DSAR criteria require identity, quality, and statutory-clock controls with fail consequences. | Independent synthetic DSAR replay confirms deterministic scoring and deadline handling. | Two cycles with zero accepted non-zero DSAR scores lacking statutory-clock evidence. |
| R8M-11 Breach Reportability and Notification-Timeline Evaluability | Rubric omits breach-notification governance criteria. | Criteria are narrative and lack timing/legal authority requirements. | Timing rules exist but jurisdiction handling and drill expectations are partial. | Reportability timing, approval chain, and jurisdictional controls are explicit. | Independent drill/incident replay confirms missed-clock scenarios trigger required fail effects. | Two cycles with zero accepted reportability scores that bypass notification-timeline controls. |
| R8M-12 Evidence Admissibility, Provenance, and Audit Defensibility Rigor | Non-zero scores can be assigned without auditable evidence chain. | Evidence fields are incomplete and provenance checks weak. | Most fields defined, but cutoff/immutability/retrieval enforcement is inconsistent. | Full admissibility schema is enforced with strong provenance and retrieval controls. | Independent assurance replay confirms sampled conclusions are reproducible from immutable evidence. | Two cycles with zero admissibility/provenance exceptions in independent assurance audits. |
| R8M-13 Contradiction-Handling and Legal-Precedence Determinism | Legal/privacy contradictions are unmanaged or non-blocking. | Contradictions logged ad hoc without precedence/SLA consequences. | Protocol exists but critical contradiction closure is inconsistent. | Deterministic protocol with legal precedence, SLA, and score-impact rules is operational. | Independent replay shows consistent outcomes and enforced blocking of unresolved Severity-1 items. | Two cycles with no unresolved Severity-1 legal/privacy contradiction at publication. |
| R8M-14 Independent Replayability and Recomputation Fidelity | Rubric outcomes cannot be replayed from evidence. | Replay works only with scorer interpretation and high variance. | Replay partially succeeds but variance/gate mismatches remain above tolerance. | Sampled replay meets variance tolerance and gate-state parity requirements. | Independent replay shows high fidelity across critical compliance rows. | Two independent teams reproduce sampled outcomes with no material variance. |
| R8M-15 Score Inflation Resistance and High-Anchor Guardrails | Unsupported high compliance scores are routinely accepted. | Guardrails are documented but bypassable. | Guardrails exist with inconsistent enforcement and unresolved jump anomalies. | High-anchor guardrails are consistently enforced with deterministic caps/rescores. | Independent inflation audit confirms detection and correction of manipulation patterns. | Two cycles with zero unsupported `90+` outcomes and stable score-distribution integrity. |
| R8M-16 Cross-Role Handoff, Release-Veto Enforceability, and Operational Fit | Handoffs/veto logic are undefined or unusable in practice. | Handoff templates exist but SLA/acceptance/veto enforcement are ambiguous. | Handoffs mostly defined; silent acceptance or occasional veto bypass still occurs. | Handoffs and veto logic are operational, SLA-bound, and non-bypassable. | Independent sample shows high first-pass handoff quality and zero improper veto bypasses. | Two cycles with sustained operational cadence, zero silent acceptance, and zero veto bypass events. |

## 4) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Baseline hash freeze: hash Rubric_0 version, anchor table, and scoring template at cycle start; invalidate scores produced from unapproved hashes.
2. Denominator freeze: freeze scoring populations at cycle start; require dual reporting (`before` and `after`) for any approved denominator change.
3. High-anchor gate: auto-cap any `>75` score without independent evidence and any `>90` score without same-cycle adversarial evidence.
4. Backfill exclusion: reject post-cutoff legal approvals/evidence from current-cycle scoring unless formal reopen is approved.
5. Chronology integrity check: verify `evidence capture -> scoring -> approval -> publication` ordering; out-of-order records are inadmissible.
6. DSAR clock recomputation: recompute statutory timelines from raw intake/closure timestamps rather than dashboard summaries.
7. Breach clock recomputation: recompute reportability and notification deadlines from raw incident timeline events.
8. Consent withdrawal challenge: run synthetic withdrawal and confirm downstream processing suppression evidence is required by scoring logic.
9. Notice drift challenge: compare declared disclosures against telemetry schemas/events to detect undeclared collection/use.
10. Shadow-store detection: independently enumerate data stores and compare to declared inventory to catch inventory theater.
11. Hidden-processor detection: reconcile payment/access/network logs against processor and subprocessor registers.
12. Contradiction suppression audit: reconcile contradiction register with adjudication minutes; hidden Severity-1 contradictions invalidate affected scores.
13. Manual override detection: diff computed scores against published scores and require signed rationale for every authorized override.
14. Reviewer independence check: prevent same actor from authoring evidence, scoring, and validating high anchors on the same row.

## 5) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (publication holds; unresolved tripwire at cutoff invalidates cycle)
| ID | Trigger condition | Detection method | Immediate effect | If unresolved at publication cutoff |
| --- | --- | --- | --- | --- |
| R8M-TW-01 | Any mandatory anti-gaming check in Section 4 is not executed | Control execution checklist audit | Cap `R8M-15` at `25`; block any sub-dimension from scoring above `90` | Cycle `INVALID` |
| R8M-TW-02 | Replay variance exceeds tolerance on >10% sampled rows | Independent replay variance analysis | Cap `R8M-14` at `50`; mandatory replay root-cause analysis | Cycle `INVALID` |
| R8M-TW-03 | Any `>75` score lacks independent validation evidence | High-anchor validation audit | Cap `R8M-15` at `25`; re-score affected rows | Cycle `INVALID` |
| R8M-TW-04 | First-pass handoff acceptance drops below 80% on critical privacy/legal handoffs | Handoff SLA dashboard review | Cap `R8M-16` at `50`; handoff protocol remediation required | Publication hold until corrected |
| R8M-TW-05 | Any unresolved Severity-1 legal/privacy contradiction exceeds SLA | Contradiction aging report | Cap `R8M-13` at `50`; publication blocked | Cycle `INVALID` |
| R8M-TW-06 | Any release-veto bypass attempt is not formally adjudicated with authority-chain record | Release governance/veto log audit | `R8M-16` set to `0`; emergency governance escalation | Cycle `INVALID` |

### Hard-fail conditions (immediate invalidation)
| ID | Hard-fail condition | Evidence test | Effect |
| --- | --- | --- | --- |
| R8M-HF-01 | Evidence fabrication, tampering, forged legal sign-off, or provenance mismatch in Rubric_0 scoring package (`G1`) | Hash/signature/timestamp forensic audit | Immediate cycle `INVALID`; mandatory forensic review |
| R8M-HF-02 | Published result ignores an active global gate (`G2`, `G3`, `G5`, or `G6`) tied to legal/privacy/compliance scope | Gate-state log vs published decision comparison | Immediate cycle `INVALID`; publication revoked |
| R8M-HF-03 | Personal/regulated-data processing is scored non-failing without lawful basis/required consent controls in Rubric_0 logic | Lawful-basis/consent row replay and gate simulation | Immediate cycle `INVALID` |
| R8M-HF-04 | Missed statutory DSAR deadline is not enforced as fail/cap by Rubric_0 scoring logic | DSAR clock recomputation and score-path simulation | Immediate cycle `INVALID` |
| R8M-HF-05 | Missed mandatory notification timeline is not enforced as fail by Rubric_0 logic | Incident timeline replay and scoring simulation | Immediate cycle `INVALID` |
| R8M-HF-06 | Unauthorized cross-border transfer or expired transfer mechanism can still produce pass outcome | Transfer control scenario replay | Immediate cycle `INVALID` |
| R8M-HF-07 | Critical processor without required DPA/risk assessment can score above `25` without approved exception path | Vendor-governance scenario replay | Immediate cycle `INVALID` |
| R8M-HF-08 | Unresolved Severity-1 legal/privacy contradiction exists at publication (`CR-12` class) | Contradiction register + SLA audit | Immediate cycle `INVALID` |
| R8M-HF-09 | Non-zero sampled rows are missing required admissibility fields above 10% defect rate | Evidence admissibility sample audit | Immediate cycle `INVALID`; full re-score required |
| R8M-HF-10 | Reviewer-independence breach on high-anchor rows is confirmed | Role-separation audit on scorer/reviewer/evidence author | Immediate cycle `INVALID`; affected rows voided |

## 6) Cross-role dependencies and adjudication handoffs

| Counterpart role | Required input to R8 meta-evaluation | R8 handoff output | Acceptance criteria | SLA / escalation |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor / Business Owner | Risk appetite, governance charter, and invalidation authority boundaries | Rubric_0 legal/compliance readiness verdict (`approve` / `conditional` / `reject`) with residual legal risk statement | Signed decision with explicit treatment for every open critical defect | Escalate within 1 business day on unresolved critical blocker |
| R1 Product Manager | Data-use purpose statements, launch claims, and disclosure intent for scoring-rule coverage tests | Required rubric clarifications for purpose/notice/consent/rights scoring criteria | No unresolved ambiguity in purpose/disclosure scoring tests | Escalate within 2 business days if ambiguity blocks scoring kickoff |
| R2 Product Architect / Enterprise Architect | Data-flow boundaries, residency assumptions, and control-mapping structure for contradiction testing | Architecture-linked legal precedence findings and required rubric rewrites | No unresolved architecture/legal precedence conflict | Escalate within 2 business days on unresolved Severity-1 conflict |
| R5 QA / Test Engineer | Replay protocol, sample-design support, and evidence quality checks | Replay/admissibility defect report and remediation requirements | Replay tolerance met and admissibility defects triaged with owners/dates | Escalate same cycle if replay variance exceeds threshold |
| R7 Security Engineer / Security Architect | Incident-control findings and shared security/privacy gate expectations | Joint contradiction dispositions and gate precedence corrections | No pass path with active shared legal/security blocker | Immediate escalation on bypass path discovery |
| R12 DevOps / Release Manager | Publication workflow logs, approval-chain evidence, and gate-state snapshots | Final legal/compliance publication authorization recommendation | Publication path automatically blocks on active hard-fail | Same-day escalation on approval-chain or cutoff integrity defect |
| R14 FinOps / Procurement / Vendor Mgmt | Processor onboarding/renewal records, contract obligations, and vendor risk statuses | Vendor-governance rubric corrections and mandatory contract-control criteria | Critical processor governance criteria are complete and testable | Escalate within 2 business days for ungoverned critical processor exposure |
| R15 Internal Audit / Assurance | Independent sampling, forensic validation, and assurance replay outcomes | Assurance-aligned adjudication memo with closure requirements | Independent assurance confirms reproducibility and integrity of sampled outcomes | Immediate escalation on integrity or independence breach |

Adjudication handoff rules:
1. Every handoff artifact must include `owner`, `timestamp`, `rubric_version`, `affected_sub_dimensions`, and immutable evidence links.
2. Handoff state is binary: `accepted` or `returned`; silent acceptance is invalid.
3. Returned handoffs must include defect class (`coverage`, `contradiction`, `evidence`, `replay`, `inflation`, `operability`) and resubmission due date.
4. Two consecutive returns in the same defect class trigger mandatory `R0 + R15` adjudication within 1 business day.

## 7) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle phase | Improvement checklist item | Owner(s) | Evidence artifact | Pass criterion | Delta re-evaluation rule |
| --- | --- | --- | --- | --- | --- |
| Pre-cycle baseline | Freeze Rubric_0 version hash, anchor model, gate logic, and scoring denominators. | R8 + R12 | Baseline hash manifest and denominator lock record | Zero uncontrolled baseline drift during cycle | Any unapproved drift forces cycle restart from frozen baseline. |
| Pre-cycle baseline | Refresh obligation catalog and map every mandatory family to Rubric_0 rows and fail/cap effects. | R8 + legal counsel | Obligation-to-rubric mapping diff and gap log | Critical-family gap count = 0 before scoring start | Any new mandatory-family gap blocks scoring kickoff. |
| Pre-cycle baseline | Reconfirm contradiction taxonomy and legal precedence rules (`CR-01/04/09/12` classes). | R8 + R2 + R7 | Contradiction protocol conformance report | Severity classes, owners, SLAs, and consequences are complete | Missing critical contradiction rule blocks publication readiness. |
| Calibration prep | Run anchor monotonicity/ambiguity lint on compliance-relevant rows. | R8 + R5 | Anchor lint report and defect closure log | No unresolved high-severity ambiguity defect | Unresolved defect caps impacted rows at `50` until fixed. |
| Calibration prep | Execute dual-rater calibration on representative privacy/legal evidence packet. | R8 + independent scorer | Calibration variance report and dispute log | Gate-state agreement = 100%; score variance within tolerance | Variance breach triggers immediate calibration rerun before live scoring. |
| Mid-cycle control | Execute full anti-gaming suite (Section 4) with evidence capture. | R8 + R15 observer | Anti-gaming execution log and challenge outputs | 100% mandatory checks executed | Any missed check triggers `R8M-TW-01`. |
| Mid-cycle control | Run independent replay/recomputation on >=15% sampled rows including DSAR/transfer/notification controls. | Independent scorer + R8 observer | Replay transcript and variance register | Replay tolerance met; gate-state parity = 100% | Tolerance breach triggers `R8M-TW-02` and targeted rescore. |
| Mid-cycle control | Audit high-anchor rows (`90+`) for independence, adversarial evidence, and denominator integrity. | R8 + R15 | High-anchor audit pack and denominator drift report | 100% of high-anchor rows pass proof requirements | Failed rows are downgraded and rescored before continuation. |
| Pre-close | Reconcile contradiction register with adjudication minutes and close all Severity-1 items. | R8 + R2 + R15 | Signed contradiction closure register | Open Severity-1 contradictions at close = 0 | Any open Severity-1 item triggers `R8M-HF-08`. |
| Pre-close | Recompute publication decision from raw gate states (`G*`, `RG*`, role hard-fails). | R8 + R12 | Gate-state recomputation worksheet | Published decision exactly matches computed gate state | Mismatch invalidates publication and requires full rerun. |
| Publication | Publish final scorecard, tripwire/hard-fail status, and immutable evidence index. | R8 owner | Final publication package with evidence manifest | Package is reproducible by independent reviewer without author assistance | Missing reproducibility proof blocks publication. |
| Post-cycle learning | Classify rubric defects (false pass, false fail, ambiguity, replay drift, inflation risk, latency). | R8 + R3 + R15 | Defect taxonomy report and prioritized backlog | Every critical defect has owner, due date, and verification metric | Unowned critical defect blocks next-cycle readiness sign-off. |
| Delta implementation | Apply approved Rubric_0 updates with row-level impact mapping and authority approvals. | R8 + R11 + R12 | Approved diff dossier and impact map | Unauthorized edits = 0 | Unauthorized edit triggers hard-fail and rollback to approved version. |
| Delta re-evaluation | Re-score all impacted rows and rerun contradiction, replay, and gate-coherence tests. | R8 + R5 + R15 | Delta re-score packet and control retest outputs | No new critical contradiction or bypass path introduced | Any unexplained impacted-row delta >1 anchor step requires rollback or redesign. |
| Next-cycle readiness | Approve next-cycle start only after closure evidence for prior critical issues is validated independently. | R8 + R0 + R15 | Readiness sign-off memo and closure evidence bundle | Prior-cycle critical issues have verified closure | Unverified closure keeps Rubric_0 in `hold` state for next cycle. |


---

## R9 Data / AI Engineer or Scientist

- source_file: `swarm_outputs/meta_rubric_role_expansions/R9_data_ai_engineer_scientist_rubric1.md`
- words: 4844
- lines: 165

# R9 Data / AI Engineer or Scientist Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 evaluates the quality, rigor, anti-gaming strength, contradiction safety, replayability, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 2) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R9 (Data / AI Engineer or Scientist) evaluates whether Rubric_0 can reliably govern data and AI quality decisions under adversarial review. The role is accountable for confirming that Rubric_0 is measurable, reproducible, contradiction-safe, inflation-resistant, and usable for release and risk decisions across A3/A4/A6 and the role layer.

### Decision rights
| Decision domain | R9 authority on Rubric_0 quality | Non-delegable boundary | Escalation boundary |
| --- | --- | --- | --- |
| Data/AI governance coverage fitness | Approve, conditionally approve, or return Rubric_0 coverage for data/AI decision classes | Cannot approve with any unmapped safety-critical data/AI decision class | Escalate to R0 and R2 within 1 business day |
| Data/AI anchor testability quality | Accept/reject anchor wording for measurability and monotonicity | Cannot accept subjective anchors for `75+` levels | Escalate to R5 and R15 in current cycle |
| Evidence admissibility sufficiency | Approve/reject data/AI evidence schema used for non-zero scores | No non-zero score without `who/what/where/time/version/provenance` | Escalate to R15 on any integrity defect |
| Replay and recomputation reliability | Block publication if replay of sampled rows fails tolerance | No publication if replay variance exceeds tolerance or gate outcomes diverge | Escalate to R15 and R12 same cycle |
| Contradiction protocol determinism | Require precedence/SLA fixes for conflicting rubric clauses | Cannot publish while Severity-1 contradiction is unresolved at cutoff | Escalate to R2, R7, R8 based on contradiction type |
| High-score guardrail enforcement | Enforce stricter proof for `>75` and `>90` | No `>75` without independent corroboration; no `>90` without challenge evidence | Escalate to R15 for inflation investigation |
| Tripwire and hard-gate coherence | Validate non-bypassable interaction of `G1..G6`, `RG1..RG4`, and role tripwires | Cannot approve if any hard-fail path is bypassable by averaging or override | Escalate to R0 governance forum immediately |
| Rubric delta governance | Approve or reject Rubric_0 deltas for next cycle | No retroactive score changes without versioned reopen and re-score trail | Escalate to R11 and R15 on change-control breach |

### Meta-scoring admissibility protocol
- Anchor scale: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires admissible evidence captured before cycle cutoff.
- Any hard-fail in Section 6 marks Rubric_0 cycle scoring `INVALID`.

## 3) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R9M-01 Data/AI Decision-Coverage Completeness | Rubric_0 covers all critical data/AI governance decisions from data intake to model retirement. | Build a decision catalog from `R9_data_ai_engineer_scientist.md` and map to Rubric_0 clauses. Pass if total mapping >=95% and safety-critical mapping =100%. | Who: R9 lead + R1 + R8 reviewers. What: decision-to-clause trace matrix and gap log. Where: meta-review workbook and governance evidence folder. |
| R9M-02 Data Contract and Lineage Clause Testability | Rubric_0 data/lineage clauses are measurable, explicit, and auditable. | Sample lineage-related clauses; each must state required fields, owner, threshold, and evidence source. Undefined clause rate in sample must be <=2%. | Who: R9 data platform reviewer + R2. What: clause testability audit and lineage criteria checklist. Where: Rubric_0 clause matrix and data-governance records. |
| R9M-03 Data Quality and Label Governance Rule Strength | Rubric_0 requires explicit quality/label controls, not narrative claims. | Check that rules require DQ thresholds, anomaly triage SLA, label audit cadence, and closure proof. Critical row omission tolerance = 0. | Who: R9 evaluator + R5 counterpart. What: DQ/label control crosswalk and omission report. Where: rubric mapping workbook and sampled score packets. |
| R9M-04 Leakage and Split-Integrity Rule Rigor | Rubric_0 enforces leakage prevention and valid split design criteria. | Verify mandatory leakage checks (temporal leakage, entity overlap, future-feature leakage). Pass if all critical model-evaluation rows require leakage evidence. | Who: R9 modeling reviewer + R15 witness. What: leakage-rule conformance scan and scenario replay notes. Where: rubric QA sheet and control test archive. |
| R9M-05 Train-Serve Parity Criteria Quality | Rubric_0 can evaluate feature and transformation parity across training and serving paths. | Simulate parity-fail and parity-pass scenarios. Pass if scoring consequences are deterministic and require parity evidence for `75+`. | Who: R9 feature owner + R6 partner. What: parity simulation sheet and scoring outcome log. Where: adjudication workspace and simulation artifacts. |
| R9M-06 Experiment Preregistration and Statistical-Power Governance | Rubric_0 evaluates experimental rigor with pre-registration and power criteria. | Sample experiment-related rows; each must require preregistration timestamp, power rationale, and guardrail definition. Missing any required field = row failure. | Who: R9 experiment reviewer + R5. What: prereg/power conformance audit. Where: rubric scorebook and experiment governance register. |
| R9M-07 Evaluation Slice and Failure-Mode Coverage | Rubric_0 requires segment-level evaluation and error taxonomy depth for high-impact decisions. | Check that rows require protected/high-risk segment slices and failure-cluster analysis. Pass if high-impact rows never allow aggregate-only scoring. | Who: R9 evaluator + R8 + R1. What: slice-coverage audit and failure-mode checklist. Where: model-governance review pack and rubric trace matrix. |
| R9M-08 Uncertainty Calibration and Threshold-Coupling Clarity | Rubric_0 ties uncertainty requirements to decision thresholds in auditable form. | Verify criteria require calibration evidence, uncertainty bounds, and threshold consequences. Pass if threshold rules are explicit and replayable. | Who: R9 reviewer + R15 observer. What: calibration/threshold policy audit and replay results. Where: scoring packet and calibration evidence index. |
| R9M-09 Fairness and Disparity Governance Enforceability | Rubric_0 provides enforceable fairness checks and mitigation/waiver logic. | Confirm disparity thresholds, mitigation deadlines, and waiver authority are explicit. Critical disparity with missing waiver path must force fail state. | Who: R9 + R8 + R7 reviewers. What: fairness-governance conformance and waiver audit. Where: governance board records and rubric gate map. |
| R9M-10 Reproducibility and Artifact Immutability Requirements | Rubric_0 requires immutable artifacts and reproducible claim replay for non-trivial scores. | Sample rows scored >50; verify required code/data/config/environment identifiers and replay procedure. Replay success in sample must be >=95%. | Who: non-author R9 reviewer + R15 witness. What: replay audit and artifact completeness report. Where: immutable artifact store and replay transcript folder. |
| R9M-11 Explainability and Decision-Trace Requirement Quality | Rubric_0 can evaluate explainability claims with case-level trace evidence. | Verify critical decision rows require explanation method limits, case traces, and reviewer acceptance criteria. Ambiguous explainability language in critical rows must be 0. | Who: R9 + domain reviewer + R11. What: explainability criteria lint and traceability audit. Where: rubric wording review log and evidence index. |
| R9M-12 Privacy/Access/Retention Control Coherence for Data/AI Scoring | Rubric_0 aligns data/AI scoring rules with privacy, access, and retention obligations. | Cross-check with legal/privacy controls. Pass if no contradiction between rubric evidence requirements and lawful retention/deletion constraints. | Who: R9 + R8 compliance reviewer. What: control-mapping matrix and contradiction register. Where: compliance repository and rubric adjudication tracker. |
| R9M-13 Drift Monitoring Rule Determinism | Rubric_0 drift criteria define measurable thresholds, ownership, and response SLAs. | Validate that drift rows include detection metric, breach threshold, response SLA, and escalation target. Missing field rate in sample must be <=2%. | Who: R9 on-call reviewer + R6. What: drift-rule completeness audit and SLA test logs. Where: observability governance binder and rubric score workbook. |
| R9M-14 Incident Response and Postmortem Closure Evaluability | Rubric_0 evaluates data/AI incident handling quality with closure effectiveness criteria. | Replay incident scenarios and score independently. Pass if scorers agree on severity, containment, and closure sufficiency for critical incidents. | Who: R9 incident reviewer + R13 + R15. What: incident replay transcript and disagreement log. Where: incident evidence packets and calibration notes. |
| R9M-15 Release Gate and Rollback/Kill-Switch Coherence | Rubric_0 enforces release-governance criteria for model promotion safety. | Simulate gate-fail, waiver, and rollback scenarios. Pass if hard gates always override average scores and rollback evidence is mandatory for release-quality claims. | Who: R9 + R12 + R6. What: release gate simulation matrix and precedence map. Where: release-governance test harness and score model workbook. |
| R9M-16 Contradiction Handling Determinism for Data/AI Tradeoffs | Rubric_0 includes explicit precedence and SLA for conflicts (accuracy vs fairness, latency vs safety, retention vs reproducibility). | Run contradiction scenarios and check deterministic outcomes, owner assignment, and closure timing. Severity-1 contradiction aging past SLA must be 0 at cutoff. | Who: R9 adjudicator + R2 + R8 + R15. What: contradiction scenario log and closure audit. Where: contradiction register and governance minutes. |
| R9M-17 Evidence Admissibility, Replayability, and Recomputation Fidelity | Rubric_0 evidence rules support independent replay and metric recomputation without author interpretation. | Replay >=15% sampled rows including gate-sensitive rows. Pass if score variance <=5 points and gate state agreement =100%. | Who: independent non-author scorer + R15 observer. What: replay workbook, recomputation sheets, variance report. Where: immutable evidence vault and replay runbook directory. |
| R9M-18 Score Inflation Resistance and High-Anchor Guardrails | Rubric_0 structurally resists inflated scoring and requires stronger proof at high anchors. | Validate rules: `>75` requires independent corroboration, `>90` requires challenge evidence, and unexplained jump >15 points triggers review. | Who: R9 scoring owner + R15 validator. What: high-score evidence audit and jump-analysis report. Where: score history dashboard and approvals ledger. |
| R9M-19 Aggregation Robustness and Operational Cadence Fit | Rubric_0 math is reproducible, non-masking for critical risk, and executable in decision windows. | Recompute formulas and run masking test by degrading critical rows. Pass if hard-gate outcomes still block pass and cycle completion meets SLA (<=5 business days after cutoff). | Who: R9 lead + R3 + R12 + R15. What: formula reconciliation, masking test report, cycle timing report. Where: scoring model workbook and cycle close records. |

## 4) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R9M-01 Data/AI Decision-Coverage Completeness | Critical data/AI decision classes are missing from Rubric_0. | Partial mapping exists; multiple safety-critical classes unmapped. | Most classes mapped; at least one safety-critical gap remains. | >=95% classes mapped and all safety-critical classes mapped. | Independent review confirms complete critical mapping and timely gap closure. | Two consecutive cycles with no safety-critical mapping gaps. |
| R9M-02 Data Contract and Lineage Clause Testability | Clauses are narrative-only and non-testable. | Some measurable language exists; owner/threshold fields often missing. | Most clauses testable, but sampling finds material ambiguity. | Clauses are measurable with explicit owner, threshold, and source. | Independent sample shows low ambiguity and consistent scoring decisions. | Two cycles with zero critical lineage-clause ambiguity defects. |
| R9M-03 Data Quality and Label Governance Rule Strength | Rubric_0 lacks DQ or label-governance requirements. | Rules exist but omit thresholds, triage SLA, or closure evidence. | Core rules present; enforcement gaps remain in critical rows. | Critical rows require explicit DQ/label thresholds and closure proof. | Independent audit confirms consistent enforcement and low omission rate. | Two cycles with no critical DQ/label rule omission in sampled scoring. |
| R9M-04 Leakage and Split-Integrity Rule Rigor | Leakage checks are absent. | Leakage mentioned but critical leakage classes are not required. | Leakage checks partially required; exceptions are loosely governed. | Mandatory temporal/entity/future leakage checks are enforced. | Independent replay confirms leakage evidence drives deterministic scoring. | Two cycles with zero critical row scored without leakage evidence. |
| R9M-05 Train-Serve Parity Criteria Quality | Rubric_0 cannot evaluate train-serve parity risk. | Parity is referenced but lacks measurable criteria and consequences. | Criteria exist; parity-fail consequences are inconsistently applied. | Parity criteria and consequences are explicit and deterministic. | Simulation replay shows consistent scoring and gate impact behavior. | Two cycles with no critical parity-rule interpretation disputes. |
| R9M-06 Experiment Preregistration and Statistical-Power Governance | Experimental rigor is not evaluated. | Experiment criteria exist without preregistration or power requirements. | Preregistration and power rules exist but have weak enforcement. | Decision-driving experiment rows require preregistration and power evidence. | Independent audit shows consistent enforcement and low defect rate. | Two cycles with zero high-impact row scored without prereg/power evidence. |
| R9M-07 Evaluation Slice and Failure-Mode Coverage | Aggregate-only evaluation is allowed for high-impact decisions. | Slice coverage is optional and failure taxonomy is shallow. | Slices required for some cases; high-impact exceptions remain. | High-impact rows require segment slices and failure-cluster analysis. | Independent reviewers confirm no aggregate-only scoring on critical rows. | Two cycles with zero critical omission of required slices/failure analysis. |
| R9M-08 Uncertainty Calibration and Threshold-Coupling Clarity | Uncertainty is not addressed in rubric decisions. | Uncertainty mentioned without calibration or threshold linkage. | Calibration rules exist but decision consequences are ambiguous. | Calibration and threshold consequences are explicit and replayable. | Independent recomputation confirms threshold behavior is deterministic. | Two cycles with no critical ambiguity in uncertainty-threshold decisions. |
| R9M-09 Fairness and Disparity Governance Enforceability | Fairness controls are absent or non-binding. | Fairness metrics listed but thresholds/waiver authority undefined. | Thresholds defined; mitigation and waiver governance inconsistent. | Thresholds, mitigation SLA, and waiver authority are enforceable. | Independent challenge confirms disparity breaches trigger correct outcomes. | Two cycles with zero unresolved critical disparity breach at publication. |
| R9M-10 Reproducibility and Artifact Immutability Requirements | Rubric allows non-reproducible claims for non-zero scores. | Artifact requirements are partial; replay often impossible. | Replay possible on some rows; missing immutable links remain. | Non-trivial scores require full artifact identifiers and replay path. | Independent non-author replay succeeds for sampled critical rows. | Two cycles with reproducible replay on all sampled critical rows. |
| R9M-11 Explainability and Decision-Trace Requirement Quality | Explainability claims are unbounded narrative. | Generic explanation requirement exists without case-level evidence. | Case traces required in limited scope; ambiguity remains. | Critical decision rows require method limits and case-level traces. | Cross-role review confirms explanation criteria are auditable and consistent. | Two cycles with zero critical explainability-admissibility disputes. |
| R9M-12 Privacy/Access/Retention Control Coherence for Data/AI Scoring | Rubric evidence rules conflict with privacy/access obligations. | Some controls mapped but contradictions and gaps are common. | Core controls mapped; unresolved contradictions remain in edge cases. | Privacy/access/retention controls align with scoring evidence rules. | Independent compliance sampling finds no unresolved critical contradiction. | Two cycles with zero legal/privacy contradiction caused by rubric design. |
| R9M-13 Drift Monitoring Rule Determinism | Drift criteria are undefined or non-operational. | Drift criteria exist but omit threshold, owner, or SLA fields. | Most fields defined; response behavior varies by scorer. | Drift criteria specify metric, threshold, owner, SLA, and escalation. | Independent scenario replay yields consistent breach-handling decisions. | Two cycles with no critical drift-rule ambiguity or missed SLA logic. |
| R9M-14 Incident Response and Postmortem Closure Evaluability | Incident quality cannot be evaluated consistently. | Incident criteria exist but severity and closure standards are vague. | Core criteria defined; scorer disagreement persists on critical cases. | Incident scoring is deterministic with clear closure-effectiveness rules. | Calibration replay shows high inter-rater agreement for critical incidents. | Two cycles with zero unresolved critical incident-scoring disputes. |
| R9M-15 Release Gate and Rollback/Kill-Switch Coherence | Release criteria are bypassable or rollback proof is optional. | Gates listed but precedence and rollback evidence rules are ambiguous. | Gate logic mostly works; edge-case bypass paths remain. | Hard gates are deterministic and require rollback/kill-switch evidence. | Adversarial simulation finds no practical bypass for critical gates. | Two cycles with zero gate-bypass finding in assurance tests. |
| R9M-16 Contradiction Handling Determinism for Data/AI Tradeoffs | Contradictions are unmanaged or ad hoc. | Contradictions logged but no precedence, owner, or SLA discipline. | Protocol exists; outcomes still vary in critical scenarios. | Precedence/SLA protocol is explicit and consistently enforced. | Independent replay confirms deterministic outcomes across reviewers. | Two cycles with no Severity-1 contradiction unresolved at cutoff. |
| R9M-17 Evidence Admissibility, Replayability, and Recomputation Fidelity | Scores cannot be replayed or recomputed independently. | Replay works only with scorer interpretation; high variance is common. | Partial replay succeeds; variance often exceeds tolerance. | Sample replay and recomputation meet tolerance and gate agreement rules. | Independent non-author replay is stable with near-zero unexplained variance. | Two cycles with no material replay/recompute discrepancy in sampled rows. |
| R9M-18 Score Inflation Resistance and High-Anchor Guardrails | Unsupported `90/100` scoring occurs without controls. | Controls exist on paper but are routinely bypassed. | Controls run inconsistently; inflation signals frequently unresolved. | High-anchor guardrails are enforced with mandatory corroboration/challenge evidence. | Distribution/jump analytics catch and correct inflation attempts quickly. | Two cycles with zero unsupported `>75` or `>90` outcomes. |
| R9M-19 Aggregation Robustness and Operational Cadence Fit | Score math is non-reproducible or process misses decision windows. | Formula exists but masking behavior or cycle timing is unverified. | Formula reconciles; masking test or SLA compliance remains inconsistent. | Formula is reproducible, critical-risk masking is blocked, and cycle SLA is usually met. | Independent recomputation matches outputs and cadence is stable in high-load cycles. | Two cycles with exact formula reconciliation, no masking defects, and zero rubric-induced decision delay. |

## 5) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Freeze Rubric_0 version hash, anchor text, weights, and gate logic at cycle start; reject scoring on non-frozen variants.
2. Freeze evaluation segment definitions and denominator populations at cycle start; any mid-cycle change requires approved reopen and dual reporting (`before` and `after`).
3. Require metric-dictionary freeze before scoring; new metrics introduced post-results are informational only for current cycle.
4. Require independent corroboration for any row scored `>75` and adversarial challenge evidence for any row scored `>90`.
5. Run non-author replay on at least 15% of scored rows including all gate-sensitive rows.
6. Recompute sampled metrics from raw evidence; dashboard-only screenshots are inadmissible for non-zero scoring.
7. Enforce cutoff integrity: post-cutoff evidence is excluded unless formal reopen approval exists.
8. Perform chronology audit (`capture -> score -> approve -> publish`); out-of-order records invalidate affected rows.
9. Detect anchor shopping by diffing draft and final anchor assignments; undocumented upward changes are auto-returned.
10. Detect contradiction suppression by reconciling contradiction register against final score packet.
11. Detect waiver laundering by flagging repeated short waivers for the same unresolved control gap.
12. Run high-score density analysis each cycle; unexplained `90+` spike >20% triggers full re-sample.
13. Require signer authority validation for approvals used as scoring evidence.
14. Require immutable provenance references for all sampled evidence (`hash`, `URI`, or immutable record id).
15. Require dual-scorer calibration on shared critical rows; unexplained divergence >1 anchor triggers adjudication replay.

## 6) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (caps, holds, and forced rework)
| ID | Trigger condition | Immediate effect | If unresolved by publication cutoff |
| --- | --- | --- | --- |
| R9M-TW-01 | Replay variance >5 points on >10% sampled rows | Cap `R9M-17` at `50`; mandatory replay root-cause analysis | Cycle marked `INVALID` |
| R9M-TW-02 | Any Severity-1 contradiction open past SLA | Cap `R9M-16` at `50`; publication hold | Cycle marked `INVALID` |
| R9M-TW-03 | Any mandatory anti-gaming check skipped | Cap `R9M-18` at `25`; no row may score above `90` | Cycle marked `INVALID` |
| R9M-TW-04 | Any score `>75` lacks independent corroboration | Cap affected row at `50`; re-score required | Cycle marked `INVALID` |
| R9M-TW-05 | Any score `>90` lacks challenge evidence | Cap affected row at `75`; inflation review required | Cycle marked `INVALID` |
| R9M-TW-06 | Gate simulation finds a bypass path for hard-gate logic | Cap `R9M-15` at `25`; immediate logic correction required | Cycle marked `INVALID` |
| R9M-TW-07 | Unauthorized rubric edit after cycle freeze | Stop scoring; revert to approved version and reopen protocol | Cycle marked `INVALID` |
| R9M-TW-08 | Cycle close delayed by >2 business days due to rubric defects | Cap `R9M-19` at `50`; remediation plan required | Publication blocked until corrected or cycle `INVALID` |

### Hard-fail conditions (Rubric_0 scoring invalid for the cycle)
| ID | Hard-fail condition | Evidence test | Effect |
| --- | --- | --- | --- |
| R9M-HF-01 | Evidence fabrication, tampering, or backdated approval in scoring package (`G1`) | Provenance hash/timestamp forensic mismatch | Cycle result `INVALID`; forensic review mandatory |
| R9M-HF-02 | Unresolved critical contradiction at cutoff (`G2`) | Contradiction register SLA aging audit | Cycle result `INVALID` |
| R9M-HF-03 | Unresolved mandatory legal/privacy/security control breach (`G3`) | R7/R8 blocker status and control evidence audit | Cycle result `INVALID` |
| R9M-HF-04 | Critical path operability/reliability fail published as pass (`G4`) | Gate log vs published decision audit | Cycle result `INVALID` |
| R9M-HF-05 | Independent replay/recompute cannot reproduce material claims (`G5`) | Non-author replay failure on critical sample | Cycle result `INVALID`; full re-score required |
| R9M-HF-06 | Publication without required authority-chain approvals (`G6`) | Signature/authority/timestamp audit | Cycle result `INVALID` |
| R9M-HF-07 | Critical role score <60 without enforced overall fail (`RG1`) | Role-layer score and decision audit | Cycle result `INVALID` |
| R9M-HF-08 | Unresolved critical cross-role contradiction on requirements/controls (`RG3`) | Cross-role contradiction audit | Cycle result `INVALID` |
| R9M-HF-09 | Role evidence package fails integrity/provenance checks (`RG4`) | Evidence-integrity audit for affected package | Affected role score = `0`; cycle `INVALID` pending remediation |
| R9M-HF-10 | High-impact data/AI rows allow aggregate-only scoring without required segment evaluation | Row-level rule and score decision audit | Cycle result `INVALID` |
| R9M-HF-11 | Non-zero scores assigned with >5% sampled evidence missing `who/what/where` | Admissibility sampling audit | Cycle result `INVALID` |
| R9M-HF-12 | Systemic score inflation: >20% of `90+` rows lack required corroboration/challenge evidence | High-anchor evidence audit | Cycle result `INVALID`; mandatory full re-sampling and re-score |

## 7) Cross-role dependencies and adjudication handoffs

| Counterpart role | Dependency into R9 meta-evaluation | R9 handoff output | Acceptance criteria | SLA / escalation |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor / Business Owner | Governance charter, risk appetite, and approval authority model | Rubric_0 readiness decision (`approve/conditional/hold`) with invalidation status | Decision state and residual-risk record signed by authorized owners | Escalate critical governance deadlock within 1 business day |
| R1 Product Manager | KPI hierarchy, segment criticality, and decision impact context | Coverage and ambiguity findings affecting rubric usability | No unresolved ambiguity on objective-to-metric mapping | Escalate within 2 business days |
| R2 Product Architect / Enterprise Architect | Data/feature contract boundaries and dependency architecture | Contradiction and coverage findings on architecture-linked rubric clauses | Critical architecture contradiction count = 0 at cutoff | Escalate within 2 business days |
| R5 QA / Test Engineer | Verification protocol quality and replay sample design | Replay variance and anchor-testability findings | Agreed replay tolerance met; unresolved critical testability defects = 0 | Escalate same cycle |
| R6 SRE / Platform Engineer | Runtime SLO/alert/rollback governance constraints | Drift/incident/release-gate coherence findings | No unresolved hard-gate bypass in shared controls | Immediate escalation for gate-bypass risk |
| R7 Security Engineer / Architect | Security control expectations and threat-path constraints | Security-linked contradiction disposition in rubric scoring logic | No pass path with active critical security control failure | Immediate escalation |
| R8 Privacy / Compliance / Legal | Lawful-basis, retention, and sensitive-data obligations | Privacy/retention control coherence findings and waiver-state audit | No unresolved legal contradiction at publication | Escalate within 1 business day |
| R12 DevOps / Release Manager | Release-control workflow, approval-chain rules, and gate state logs | Publication authorization recommendation for rubric score package | Gate-state consistency and approval-chain integrity validated | Same-day escalation on mismatch |
| R15 Internal Audit / Assurance | Independent assurance sampling and integrity testing | Final assurance memo with replay and inflation findings | Material assurance exceptions = 0 for publication | Immediate escalation on integrity breach |
| R3 Engineering Manager | Capacity and cadence data for evaluator workload | Operational-cadence fitness findings and simplification actions | Rubric execution meets cycle SLA without critical backlog | Escalate in-cycle on repeated SLA risk |
| R11 Technical Writer / DocOps | Controlled wording changes and version publication discipline | Approved wording deltas and change-impact notes | Versioned diff, approvers, and impact scope complete | Escalate on unapproved wording drift |

Adjudication rules:
1. Every handoff must be explicitly `accepted` or `returned`; silent acceptance is invalid.
2. Every returned handoff must include defect class, owner, due date, and resubmission timestamp.
3. Any defect returned twice in one cycle escalates to `R0 + R15` adjudication.
4. Any unresolved critical handoff at cutoff blocks publication.

## 8) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle point | Checklist item | Evidence artifact | Pass criterion | Delta re-evaluation rule |
| --- | --- | --- | --- | --- |
| Pre-cycle baseline | Freeze Rubric_0 version hash, anchor set, weights, and gate definitions. | Baseline manifest with signed approvals. | Zero unauthorized change during active scoring window. | Unauthorized change forces cycle restart on approved baseline. |
| Pre-cycle baseline | Refresh R9 decision-catalog-to-clause trace and unresolved gap log. | Updated trace matrix and gap register. | Safety-critical mapping =100% before scoring starts. | New critical gap blocks scoring kickoff. |
| Pre-cycle baseline | Reconfirm contradiction precedence rules and SLA timers. | Contradiction protocol sheet and owner roster. | No missing precedence path for known tradeoff classes. | Protocol change requires targeted re-score of affected rows. |
| Pre-cycle baseline | Reconfirm admissibility schema (`who/what/where/time/version/provenance`). | Admissibility schema version and cutoff notice. | Schema completeness approved by R9 and R15. | Mid-cycle schema change requires reopen approval and impacted-row re-score. |
| Calibration prep | Run anchor monotonicity and ambiguity lint for R9-relevant rubric rows. | Anchor lint report and defect log. | No unresolved critical ambiguity before scoring. | Unresolved critical ambiguity caps impacted rows at `50`. |
| Calibration prep | Run dual-scorer calibration on shared critical packet. | Calibration comparison and dispute register. | Unexplained divergence >1 anchor = 0 cases after adjudication. | Remaining divergence blocks publication. |
| Scoring execution | Score using admissible evidence only; reject narrative-only claims. | Row-level scorebook and admissibility sample log. | Non-zero rows with complete admissibility >=98% in sample. | Defective rows must be rescored before publication. |
| Replay assurance | Execute independent replay and recomputation on >=15% sampled rows. | Replay transcript, recomputation workbook, variance report. | Score variance <=5 points; gate agreement =100%. | Variance breach triggers `R9M-TW-01` and re-score. |
| Anti-gaming execution | Execute all mandatory anti-gaming checks and challenge scenarios. | Anti-gaming checklist and challenge outcomes. | Mandatory control execution rate =100%. | Any skipped mandatory control triggers `R9M-TW-03`. |
| Contradiction closure | Resolve all Severity-1 contradictions and apply score impacts. | Closure records and rescoring notes. | Severity-1 unresolved count = 0 at cutoff. | Any unresolved item triggers `R9M-TW-02` and invalidation. |
| High-score review | Audit all `>75` and `>90` rows for required corroboration/challenge evidence. | High-score evidence package and audit summary. | Missing required evidence count = 0. | Violations trigger `R9M-TW-04/05` and affected-row cap. |
| Gate coherence validation | Re-run hard-gate precedence simulation on final score draft. | Gate simulation report and sign-off. | No bypass path for hard-fail conditions. | Any bypass triggers `R9M-TW-06` and cycle invalidation if unresolved. |
| Publication gate | Apply tripwire and hard-fail checks before publishing cycle results. | Final invalidation check sheet and sign-offs. | Active hard-fail count = 0. | Any active hard-fail marks cycle `INVALID`. |
| Post-cycle remediation | Convert failed checks into dated corrective actions with verification tests. | Remediation register with owner/due date/test. | 100% critical actions owned and time-bound. | Unowned critical action blocks next-cycle readiness sign-off. |
| Delta implementation | Apply approved Rubric_0 wording/rule changes with versioned diffs and impact tags. | Change request, approved diff, impact matrix. | Unauthorized delta count = 0. | Unauthorized delta triggers `R9M-TW-07` and cycle reset. |
| Delta re-evaluation | Re-score impacted rows and rerun replay/gate/coherence tests for changed areas. | Delta re-score packet and focused replay report. | All impacted rows/gates retested with pass evidence. | Missing retest evidence blocks publication. |
| Cycle close | Publish retrospective with trend deltas, repeat defect classes, and carryover risks. | Cycle retrospective and carryover register. | Residual risks explicitly owned with review date. | Unowned carryover risk prevents cycle close. |


---

## R10 UX Researcher / Designer

- source_file: `swarm_outputs/meta_rubric_role_expansions/R10_ux_researcher_designer_rubric1.md`
- words: 4748
- lines: 154

# R10 UX Researcher / Designer Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 evaluates the quality, rigor, anti-gaming strength, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 2) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R10 evaluates whether Rubric_0 is an enforceable UX governance instrument rather than a style checklist. The role verifies that Rubric_0 can produce reproducible UX-related scoring outcomes, resist evidence and anchor gaming, resolve contradictions before publication, and operate inside real release cadence.

### Decision rights (R10 meta-evaluator)
| Decision area | R10 authority | Non-delegable boundary | Required co-signers | Escalation trigger |
| --- | --- | --- | --- | --- |
| UX meta-rubric fitness recommendation | Recommend `approve`, `conditional approve`, or `hold` for Rubric_0 usage | Cannot recommend approval if any hard-fail in Section 6 is active | R1, R12, R15 | Any hard-fail remains open at publication cutoff |
| UX criterion falsifiability quality | Final UX judgment on whether Rubric_0 UX-related criteria are testable and auditable | Cannot accept subjective high-anchor language without measurable tests | R5, R2 | Anchor ambiguity causes >1 step scoring divergence |
| Accessibility gate design sufficiency | Final UX judgment on whether Rubric_0 enforces accessibility critical-path blocking logic | Cannot approve scanner-only gate designs for critical workflows | R7, R8 | Manual AT evidence requirements missing or contradictory |
| UX evidence admissibility quality | Final UX judgment on evidence schema completeness for non-zero scoring | Cannot allow non-zero scores without `who/what/where/time/version/hash` fields | R15 | Evidence admissibility defects exceed threshold |
| Contradiction lifecycle adequacy | Joint authority on contradiction severity, SLA, and score impact | Cannot close cycle with unresolved critical contradiction affecting UX rows | R2, R8, R15 | Critical contradiction ages past SLA |
| Delta promotion readiness | Approve or reject Rubric_0 UX-related delta promotion | Cannot promote without impact map plus targeted replay/re-score | R1, R12, R15 | Unauthorized changes to anchors, gates, or weights |

### Meta-scoring admissibility rules
- Anchor scale: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires explicit `who/what/where` evidence.
- No sub-dimension may score above `50` without replayable evidence.
- No sub-dimension may score above `75` without independent reviewer validation.
- No sub-dimension may score above `90` without in-cycle adversarial challenge evidence.
- Evidence created after cycle cutoff is excluded from current-cycle scoring.

## 3) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R10-M01 UX concern coverage completeness | Rubric_0 fully covers UX-critical governance concerns across A5 and role layer expectations. | Build concern-to-row map from canonical R10 concerns (research validity, usability, IA, accessibility, inclusion, visual readability, design system, handoff, telemetry, harm prevention). Critical concern coverage must be 100%; total concern coverage >=95%. | Who: R10 meta lead + R1 reviewer. What: concern mapping matrix and gap register. Where: Rubric_0 master file, R10 role expansion, review workbook. |
| R10-M02 Decision usability and authority clarity | Rubric_0 UX criteria can drive deterministic decisions instead of narrative debate. | Run scenario replay (`go`, `hold`, `fail`) on 10 UX-relevant cases. Pass if evaluator decision agreement >=95% and authority path is explicit for each case. | Who: R10 + R12 + R15. What: scenario replay packet and adjudication outcome log. Where: governance simulation repository and cycle artifacts. |
| R10-M03 Research validity criteria rigor | Rubric_0 defines falsifiable standards for UX research question quality and method fit. | Lint UX research rows for measurable requirements (hypothesis, decision linkage, method rationale, success/failure threshold). Vague-language defect rate <=2% on sampled rows. | Who: R10 research owner + R5 verifier. What: criteria lint report and defect closure log. Where: Rubric_0 UX rows and scoring QA folder. |
| R10-M04 Sampling and bias-control criteria quality | Rubric_0 requires auditable participant representativeness and bias controls. | Verify criteria require segment quotas, exclusions rationale, attrition handling, and high-risk cohort coverage. Omission on launch-critical rows must be 0. | Who: R10 + R1 + analytics reviewer. What: sampling-control conformance audit. Where: Rubric_0 role rows and meta-review notes. |
| R10-M05 Critical task-flow usability threshold testability | Rubric_0 task-flow criteria are measurable with clear pass/fail thresholds. | Confirm criteria require explicit thresholds for success rate, critical error rate, and completion-effort boundary on critical journeys. Replay sample scoring for threshold determinism. | Who: R10 + R5. What: threshold audit sheet and replay transcript. Where: Rubric_0 A5/role criteria and replay workbook. |
| R10-M06 IA and findability criterion precision | Rubric_0 specifies how findability quality is measured and adjudicated. | Check for explicit first-click, tree-test, and backtracking expectations where applicable. Confirm critical journey definitions are required for non-zero scoring. | Who: UX architect + R10 reviewer. What: IA-criteria precision checklist. Where: Rubric_0 IA-related rows and adjudication tracker. |
| R10-M07 Content clarity and comprehension criterion precision | Rubric_0 content-quality rows are behaviorally testable, not stylistic opinion. | Verify criteria require comprehension checks, ambiguity thresholds, and decision-impact linkage. Reject rows lacking measurable comprehension expectations. | Who: content design reviewer + R10. What: content-criterion audit report. Where: Rubric_0 UX language rows and review pack. |
| R10-M08 Interaction feedback and recovery criterion quality | Rubric_0 includes measurable expectations for system-state clarity and error recovery behavior. | Confirm criteria include state visibility, consequence signaling, and recovery-path evidence requirements on critical flows. Test for explicit severity consequences when absent. | Who: interaction design lead + R5. What: interaction-criteria audit and consequence matrix. Where: Rubric_0 UX interaction rows and release governance notes. |
| R10-M09 Accessibility gate enforceability and AT evidence specificity | Rubric_0 accessibility rows enforce critical-path accessibility with manual AT evidence requirements. | Validate gate language requires keyboard and screen-reader evidence on critical journeys; scanner-only evidence cannot support >50. Simulate gate precedence under high average scores. | Who: accessibility lead + R7 + R8. What: accessibility gate simulation and evidence admissibility audit. Where: Rubric_0 gate sections, accessibility criteria rows, simulation logs. |
| R10-M10 Inclusive design parity criteria quality | Rubric_0 requires measurable parity checks across priority user cohorts and contexts. | Verify inclusion rows require cohort/context outcome comparisons, acceptable disparity thresholds, and timed remediation ownership. Critical cohort omission tolerance = 0. | Who: R10 + R13 + analytics partner. What: parity-criteria conformance review. Where: Rubric_0 inclusion criteria and adjudication workbook. |
| R10-M11 Visual hierarchy and readability criterion objectivity | Rubric_0 visual-quality anchors rely on auditable readability and hierarchy signals. | Confirm criteria include measurable readability signals (contrast, legibility, scan efficiency/comprehension) and prohibit purely aesthetic wording for high scores. | Who: visual designer + R10 + accessibility reviewer. What: visual-objectivity lint report. Where: Rubric_0 visual/readability sections and calibration notes. |
| R10-M12 Design-system governance criterion quality | Rubric_0 defines consistent component/token governance with enforceable exception control. | Verify criteria require component/token conformance checks, exception owner, expiry, and remediation path. Expired exception acceptance must be 0. | Who: design-system owner + R10 + R4. What: system-governance criteria audit. Where: Rubric_0 role rows and exception policy matrix. |
| R10-M13 Design-to-build fidelity and handoff testability | Rubric_0 criteria ensure UX specifications are testable and fidelity drift is auditable. | Check for explicit requirements on states, error cases, acceptance oracles, and implementation-fidelity review cadence. Validate deterministic score impacts for handoff incompleteness. | Who: R10 + R4 + R5 + R11. What: fidelity/handoff criteria conformance report. Where: Rubric_0 UX handoff rows and sampled adjudication packets. |
| R10-M14 Evidence traceability and provenance schema quality | Rubric_0 evidence policy supports traceable, admissible, tamper-evident UX scoring. | Audit non-zero UX-related rows for complete evidence fields and immutable provenance requirements. Required-field completeness >=98%; unresolved provenance anomalies = 0. | Who: R10 evidence owner + R15. What: admissibility/provenance audit log. Where: evidence index, scoring ledger, policy annex. |
| R10-M15 Independent replayability and recompute determinism | Independent reviewers can reproduce UX-related Rubric_0 scores from raw evidence. | Non-author replay on >=20% sampled UX rows including all triggered gate rows. Pass if anchor agreement >=95%, gate-state agreement = 100%, aggregate recompute variance = 0. | Who: independent reviewer + R15 observer + R10 witness. What: replay packet, recompute sheet, variance register. Where: immutable evidence store and replay workspace. |
| R10-M16 Contradiction handling and adjudication rigor | Rubric_0 defines contradiction classes, aging rules, SLA, and mandatory score recalculation behavior. | Verify contradiction schema includes type, severity, owner, due date, closure evidence, and recalculation rule. Unresolved critical contradiction at close must be 0. | Who: R10 + R2 + R8 + R15. What: contradiction conformance review and aging report. Where: contradiction register and adjudication minutes. |
| R10-M17 Score inflation resistance and high-anchor control strength | Rubric_0 prevents unjustified high UX-related scores through stronger proof and review controls. | Enforce high-anchor prerequisites (`>75` independent validation, `>90` adversarial challenge). Analyze score-distribution spikes; unexplained 90+ density increase triggers mandatory resampling. | Who: R10 + R15 + R1 observer. What: inflation analytics and cap-enforcement report. Where: scoring dashboard, high-anchor evidence samples, approval log. |
| R10-M18 Operational cadence fit and low-ambiguity usability | Rubric_0 can be run reliably within release/planning timelines with low interpretation drift. | Dry-run full evaluation workflow. Release-cycle completion <=3 business days, planning-cycle <=7 business days, ambiguity-driven rework <=10% of rows. | Who: R10 operations owner + R3 + R12. What: timing study, ambiguity log, handoff defect report. Where: governance tracker and cycle retrospective archive. |

## 4) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R10-M01 UX concern coverage completeness | UX governance concerns are largely missing. | Partial concern mapping exists; several critical concerns unmapped. | Most concerns mapped, but at least one critical concern remains unmapped. | All critical concerns mapped; minor non-critical gaps remain. | Independent review confirms near-complete mapping and no critical gaps. | Two cycles with full critical coverage and zero unresolved mapping defects. |
| R10-M02 Decision usability and authority clarity | UX criteria cannot produce a decision outcome. | Decisions depend on ad hoc interpretation and disputed authority. | Decision outcomes usually possible, but edge-case authority conflicts persist. | Decision outcomes and authority path are explicit for normal cases. | Scenario replay shows consistent outcomes across normal and edge cases. | Two cycles with no decision-authority ambiguity and high inter-rater agreement. |
| R10-M03 Research validity criteria rigor | Research criteria are non-falsifiable or absent. | Research quality language exists but is mostly subjective. | Basic falsifiable clauses exist, but high anchors remain vague. | Criteria are measurable with explicit hypothesis/method/threshold expectations. | Independent lint finds minimal ambiguity and clean high-anchor testability. | Two cycles with zero material ambiguity in research-row adjudication. |
| R10-M04 Sampling and bias-control criteria quality | Sampling/bias expectations are absent. | Sampling mentioned without enforceable cohort or bias controls. | Core sampling controls exist, but launch-critical cohort requirements are inconsistent. | Criteria enforce cohort quotas, exclusions rationale, and bias controls on critical rows. | Independent audit confirms consistent enforcement and low omission rate. | Two cycles with no critical cohort-coverage omission accepted for non-zero scores. |
| R10-M05 Critical task-flow usability threshold testability | No measurable task-flow thresholds exist. | Threshold intent exists but lacks specific pass/fail boundaries. | Thresholds exist for some flows; deterministic scoring still inconsistent. | Critical-flow thresholds are explicit and consistently scoreable. | Replay confirms threshold-driven scoring consistency across reviewers. | Two cycles with deterministic threshold scoring and zero critical-threshold ambiguity disputes. |
| R10-M06 IA and findability criterion precision | IA/findability criteria are absent or opinion-based. | IA language exists without measurable expectations. | Some measurable IA criteria exist; critical-path definitions are incomplete. | IA/findability criteria are explicit and tied to critical journeys. | Independent sample shows consistent IA scoring with low interpretation drift. | Two cycles with stable IA scoring and no unresolved critical findability criterion gaps. |
| R10-M07 Content clarity and comprehension criterion precision | Content quality cannot be objectively scored. | Criteria mention clarity but omit measurable comprehension tests. | Comprehension tests are partially specified; high-anchor differentiation is weak. | Criteria require measurable comprehension and ambiguity thresholds. | Independent review confirms reproducible scoring on sampled content rows. | Two cycles with no major adjudication disputes caused by content-criterion ambiguity. |
| R10-M08 Interaction feedback and recovery criterion quality | Interaction-state and recovery expectations are missing. | Interaction criteria exist but omit consequences for missing recovery behavior. | Most criteria measurable, but error-recovery requirements are inconsistently enforced. | Criteria define measurable state clarity and recovery expectations with explicit consequences. | Scenario tests show consistent score penalties when recovery evidence is absent. | Two cycles with no unresolved critical scoring contradiction on interaction/recovery criteria. |
| R10-M09 Accessibility gate enforceability and AT evidence specificity | Accessibility gates are absent or non-blocking. | Accessibility checks exist but scanner-only evidence can yield high scores. | Manual AT requirements exist but gate precedence is inconsistently enforced. | Accessibility gates are deterministic and require manual AT evidence on critical journeys. | Independent simulation confirms no bypass path under active accessibility gate failures. | Two cycles with zero gate-precedence disputes and no scanner-only high-anchor accessibility scores. |
| R10-M10 Inclusive design parity criteria quality | Inclusion/parity criteria are absent. | Inclusion criteria are narrative with no parity thresholds. | Parity checks exist but critical cohort/context requirements remain incomplete. | Criteria require cohort/context parity checks with explicit thresholds and owners. | Independent sample confirms parity criteria are actionable and consistently scored. | Two cycles with no unresolved high-impact inclusion-criteria omission. |
| R10-M11 Visual hierarchy and readability criterion objectivity | Visual criteria are purely aesthetic and non-auditable. | Some objective signals appear, but high anchors remain style-opinion based. | Readability/hierarchy metrics exist but are incomplete or inconsistently required. | Visual criteria rely on measurable readability/hierarchy signals for non-zero scoring. | Calibration shows low rater divergence and no major subjective disputes. | Two cycles with stable calibration and no unresolved objectivity defects in visual rows. |
| R10-M12 Design-system governance criterion quality | Design-system governance is absent in Rubric_0. | Governance is mentioned without enforceable exception controls. | Exception process exists but expiry/remediation enforcement is weak. | Criteria enforce component/token conformance and time-bound exception control. | Independent audit confirms low unauthorized overrides and timely exception closure rules. | Two cycles with no expired exception accepted as compliant in scored rows. |
| R10-M13 Design-to-build fidelity and handoff testability | Handoff/fidelity criteria are missing or unusable. | Handoff criteria exist but omit state/error completeness or testability. | Criteria mostly usable; recurring ambiguity remains for critical flows. | Criteria require testable handoffs and auditable fidelity checks. | Cross-role sample shows low rejection rate and deterministic scoring outcomes. | Two cycles with no critical handoff-criterion ambiguity causing score invalidation. |
| R10-M14 Evidence traceability and provenance schema quality | Rubric_0 allows non-zero scores without traceable provenance. | Evidence fields are partial and tamper detection is weak. | Most evidence requirements defined; cutoff/provenance enforcement inconsistent. | Complete admissibility schema with enforced provenance and cutoff rules. | Independent audit shows high completeness and no unresolved provenance anomalies. | Two cycles with zero inadmissible evidence accepted on sampled UX-related rows. |
| R10-M15 Independent replayability and recompute determinism | Independent replay cannot reproduce scores. | Replay works only with author interpretation and high variance. | Replay partially successful; gate states or aggregates mismatch occasionally. | Sampled replay is reliable with matching gate states and aggregates. | Independent replay shows high agreement and no unexplained variance. | Two cycles with full sampled replay parity and deterministic recomputation. |
| R10-M16 Contradiction handling and adjudication rigor | Contradictions are unmanaged and non-blocking. | Contradictions logged informally without SLA or score impact rules. | Process exists but critical contradictions can remain open at close. | Contradiction protocol is explicit, SLA-bound, and score-impacting. | Independent audit confirms critical contradictions resolved before publication. | Two cycles with zero unresolved critical contradiction at cycle close. |
| R10-M17 Score inflation resistance and high-anchor control strength | High scores are granted without stronger proof. | Inflation controls exist on paper but are inconsistently enforced. | High-anchor controls partly enforced; distribution spikes often unexplained. | Strong controls enforce higher proof thresholds and independent validation for high anchors. | Distribution and challenge audits detect and correct inflation attempts in-cycle. | Two cycles with no unsupported `90/100` outcomes on independent audit sample. |
| R10-M18 Operational cadence fit and low-ambiguity usability | Rubric_0 cannot be executed within decision timelines. | Execution is possible only with heavy delay and frequent interpretation conflicts. | Cadence is mostly achievable but ambiguity causes repeated rework. | Workflow fits cycle SLAs with manageable ambiguity and clear handoffs. | Multi-team dry-runs show predictable timing and low interpretation drift. | Two cycles with sustained SLA compliance and no decision delay caused by rubric design defects. |

## 5) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Version-hash freeze: lock Rubric_0 version, anchor table, and score template at cycle start; any unapproved hash change invalidates in-window scoring.
2. Chronology enforcement: require evidence sequence `capture -> adjudicate -> score -> approve`; out-of-order artifacts are inadmissible.
3. Quote cherry-pick control: any qualitative UX claim must include full session reference and disconfirming evidence summary; excerpt-only claims score `0`.
4. Denominator freeze: freeze cohort definitions and sample frame before scoring; in-cycle denominator changes require approved dual-run reporting (`before` and `after`).
5. Metric recompute challenge: recompute at least one critical UX metric set from raw logs each cycle; dashboard-only evidence cannot support `>75`.
6. Accessibility evidence integrity check: block `>50` accessibility scoring when only automated scan evidence is provided for critical journeys.
7. Severity-laundering detection: diff original vs final severity labels on sampled usability findings; unsupported downgrades invalidate related rows.
8. Exception-laundering detection: flag repeated short-term design-system/accessibility exception renewals for same issue; require executive re-approval.
9. High-anchor dual-proof rule: require independent reviewer plus in-cycle challenge evidence for every `90` or `100`.
10. Backfill exclusion rule: evidence created after cutoff cannot raise current-cycle scores.
11. Silent-override detection: compare computed vs published scores; undocumented manual overrides invalidate affected dimensions.
12. Contradiction suppression audit: reconcile contradiction register, adjudication minutes, and final score narrative; hidden critical contradictions invalidate cycle publication.
13. Cross-role consistency check: sample shared conditions across R10/R5/R7/R8/R12; unexplained divergence >1 anchor step triggers adjudication hold.

## 6) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (publication hold, caps, or forced re-score)
| ID | Tripwire condition | Detection method | Immediate effect | Minimum recovery proof |
| --- | --- | --- | --- | --- |
| R10-MTW-01 | Independent replay anchor agreement <95% on sampled UX rows or any gate-state mismatch | Non-author replay audit | Publication hold; impacted dimensions re-scored | Replay rerun meets thresholds and variance root-cause closed |
| R10-MTW-02 | Missing required evidence fields on >5% sampled non-zero UX rows | Evidence admissibility sampling audit | Affected dimensions capped at `50`; mandatory re-sampling | Field-complete evidence and resample defect rate <=2% |
| R10-MTW-03 | Any `>75` score lacks independent validation evidence | High-anchor audit | Affected rows downgraded to `50`; inflation review opened | Independent validation added and row-level re-adjudication completed |
| R10-MTW-04 | Accessibility critical-path row scored >50 with scanner-only evidence | Accessibility evidence audit | Accessibility-related dimensions capped at `25`; gate re-evaluation required | Manual keyboard + screen-reader evidence added and re-reviewed |
| R10-MTW-05 | Critical contradiction open beyond SLA at pre-close | Contradiction aging report | Cycle close blocked until contradiction adjudication completes | Signed closure record plus impacted score recalculation |
| R10-MTW-06 | First-pass cross-role handoff acceptance <80% on sampled UX adjudication packets | Handoff conformance audit | Operability dimension capped at `50`; handoff contract rewrite required | Updated handoff criteria and improved acceptance >=90% on re-sample |

### Hard-fail conditions (Rubric_0 cycle scoring becomes invalid)
| ID | Hard-fail condition | Evidence test | Immediate effect | Minimum recovery proof |
| --- | --- | --- | --- | --- |
| R10-MHF-01 | Evidence fabrication, tampering, forged provenance, or backdated approval in meta-evaluation package | Forensic hash/timestamp/signature audit | Entire cycle marked `INVALID` | Forensic closure, corrected immutable evidence chain, full independent re-score |
| R10-MHF-02 | Published result contradicts an active blocking UX/accessibility gate in Rubric_0 | Gate-state vs published outcome reconciliation | Cycle marked `INVALID`; publication revoked | Corrected gate enforcement logic and complete recomputation |
| R10-MHF-03 | Unresolved critical contradiction at publication cutoff | Contradiction register shows open critical item | Cycle marked `INVALID`; no publication allowed | Contradiction closure with score-impact update and co-signed adjudication |
| R10-MHF-04 | Independent replay cannot reproduce critical gate outcomes | Replay report shows gate-state mismatch on sampled critical rows | Cycle marked `INVALID` | Successful replay of required sample with gate-state parity |
| R10-MHF-05 | Unauthorized change to Rubric_0 anchors/weights/gates during active scoring window | Version-control and hash audit | In-window results marked `INVALID` | Re-run cycle on approved frozen version with signed change record |
| R10-MHF-06 | Post-cutoff evidence used to increase current-cycle scores | Cutoff timestamp reconciliation | Cycle marked `INVALID` | Cutoff-compliant rescoring with audit trail |
| R10-MHF-07 | Reviewer-independence breach for high anchors (`90+`) | Role-separation audit (`author=scorer=validator`) | Affected high-anchor results invalid; repeated pattern invalidates cycle | Independent reassignment and full re-adjudication of affected scope |
| R10-MHF-08 | Critical contradiction suppression (found in evidence/minutes but absent from register) | Cross-source contradiction reconciliation | Cycle marked `INVALID` | Register correction, root-cause analysis, and independent re-close |
| R10-MHF-09 | Manual score override without authorized rationale and co-signatures | Score ledger diff vs published score | Cycle marked `INVALID` for affected scope; systemic case invalidates full cycle | Authorized override record or score rollback + re-publication |

## 7) Cross-role dependencies and adjudication handoffs

| Counterpart role | Required inbound dependency for R10 meta-evaluation | R10 outbound handoff | Acceptance criteria | SLA / escalation |
| --- | --- | --- | --- | --- |
| R1 Product Manager | Decision priorities, risk appetite for UX tradeoffs, and planning cadence constraints | UX meta-readiness verdict and prioritized rubric rewrite requests | R1 accepts/returns with owner and due date for each rewrite | 3 business days; escalate to R0 if blocked |
| R2 Product/Enterprise Architect | Architecture constraints affecting IA/interaction criteria wording | Contradiction and feasibility defect log for Rubric_0 UX rows | Zero unresolved critical architecture-UX contradiction | 2 business days |
| R4 Software Engineer | Build-feasibility and fidelity ambiguity feedback from prior cycles | Handoff-criteria quality corrections and scoring impact rules | Critical handoff criteria are testable with no ambiguity on sampled rows | Weekly during active cycle |
| R5 QA/Test Engineer | Test-oracle and severity-policy alignment feedback | Deterministic UX threshold and severity-governance updates | QA confirms criterion testability and reproducibility | Pre-close + weekly calibration |
| R7 Security Engineer | Security-control UX interactions (auth, consent, recovery) for gate alignment | Updated gate precedence and abuse-resistant UX scoring clauses | No unresolved security-UX gate precedence conflict | 2 business days |
| R8 Privacy/Compliance/Legal | Legal/privacy interpretation for consent and rights flows | Compliance-safe UX criterion language and contradiction dispositions | Legal/privacy confirms enforceability on regulated flows | Before publication cutoff |
| R11 Technical Writer/DocOps | Terminology consistency and documentation traceability constraints | Content-clarity criterion updates and evidence schema clarifications | Terminology conflicts resolved and documented | 3 business days |
| R12 DevOps/Release Manager | Release timing windows and gate automation behavior | Operability fit findings and release-block conditions | Release governance confirms gate logic is executable in pipeline | Per release train |
| R13 Operations/Support/CS | Post-release user pain signals and incident taxonomy relevance for calibration | Inclusion/usability criterion delta proposals tied to escaped incidents | Incident-linked rubric changes accepted or returned with reasons | Weekly after major release |
| R15 Internal Audit/Assurance | Independent replay, provenance, and control-test findings | Final assurance-ready adjudication package and remediation obligations | Audit can reproduce sampled outcomes without author intervention | Per cycle close |

### Adjudication handoff rules
1. Every handoff artifact must include `owner`, `timestamp`, `rubric version hash`, `affected sub-dimensions`, and immutable evidence links.
2. Handoff state is binary: `accepted` or `returned`; silent acceptance is invalid.
3. Returned handoffs must include defect class (`coverage`, `ambiguity`, `evidence`, `contradiction`, `inflation`, `operability`) and a resubmission due date.
4. Two consecutive returns for the same defect class escalate to `R0 + R15` within 1 business day.

## 8) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle phase | Improvement checklist item | Owner(s) | Evidence artifact | Pass criterion | Delta re-evaluation rule |
| --- | --- | --- | --- | --- | --- |
| Cycle start | Freeze Rubric_0 version hash, scoring scope, and cutoff timestamp. | R10 + R12 | Baseline lock record | No in-cycle uncontrolled version/scope drift | Any drift forces cycle restart on approved baseline |
| Cycle start | Confirm reviewer-independence roster for high-anchor and replay checks. | R10 + R15 | Independence matrix | No conflict of interest in planned assignments | Any conflict requires reassignment before scoring |
| Design lint | Run UX-row falsifiability and ambiguity lint across all relevant Rubric_0 clauses. | R10 + R5 | Lint report and closure log | No unresolved critical ambiguity defects | Unresolved critical defect blocks scoring kickoff |
| Design lint | Validate contradiction protocol fields and mandatory score-impact rules. | R10 + R2 + R8 | Contradiction protocol conformance sheet | Required schema fields and score-impact rules complete | Missing field/rule blocks publication readiness |
| Data prep | Audit evidence schema completeness (`who/what/where/time/version/hash`) on sampled packets. | R10 + R15 | Evidence admissibility scan | Completeness >=98% and no unresolved tamper indicators | Failed scan triggers remediation and re-sampling |
| Calibration | Conduct dual-rater anchor calibration for sampled UX sub-dimensions. | R10 + cross-role raters | Calibration variance report | Variance within one anchor step; no inversion defects | Inversion requires anchor rewrite and recalibration |
| Scoring run | Execute independent replay on >=20% sampled UX rows including all triggered gates. | Independent reviewer + R10 witness | Replay transcript and variance register | Anchor agreement >=95%; gate-state agreement 100% | Failing threshold triggers impacted-dimension re-score |
| Scoring run | Recompute aggregate and dimension scores from row-level evidence using independent calculator. | R10 + R12 | Recompute parity report | Aggregate variance = 0 | Any mismatch blocks publication |
| Mid-cycle control | Execute anti-gaming challenge set (denominator, cherry-pick, backfill, override, suppression). | R10 + R15 | Challenge execution log | All mandatory controls executed with documented outcome | Any missed mandatory control applies defined cap/hold |
| Pre-close | Audit all `90+` rows for independent validation and in-cycle challenge proof. | R10 + R15 | High-anchor audit packet | 100% of `90+` rows satisfy proof gates | Missing proof downgrades rows and triggers re-score |
| Pre-close | Resolve all critical contradictions and apply score recalculations. | R10 + R2 + R8 + R15 | Signed contradiction closure bundle | Zero open critical contradictions at close | Any open critical contradiction invalidates close |
| Publication | Publish final meta-score, tripwire/hard-fail status, and immutable evidence index. | R10 owner | Final publication package | Package reproducible by non-author reviewer | Missing manifest/link integrity failure invalidates publication |
| Post-cycle analysis | Run calibration against downstream rubric-use outcomes (decision reversals, escaped UX risk). | R10 + R13 + R9 | Calibration study and drift memo | Directional calibration holds with explained drift | Unexplained inverse signal triggers threshold redesign |
| Post-cycle remediation | Classify rubric defects (false positive, false negative, ambiguity, latency, inflation) and assign owners. | R10 + R3 + R15 | Defect taxonomy and remediation tracker | All critical defects assigned owner and due date | Unowned critical defect blocks next-cycle readiness |
| Next-cycle readiness | Re-score impacted historical sample on updated Rubric_0 and document row-level deltas. | R10 + R1 + R12 + R15 | Delta re-score dossier | No unexplained delta >1 anchor step on sampled rows | Unexplained deltas require rollback or further revision |


---

## R11 Technical Writer / DocOps / PDF Owner

- source_file: `swarm_outputs/meta_rubric_role_expansions/R11_technical_writer_docops_pdf_owner_rubric1.md`
- words: 5001
- lines: 162

# R11 Technical Writer / DocOps / PDF Owner Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 evaluates the quality, rigor, anti-gaming strength, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 2) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R11 meta-evaluation determines whether Rubric_0 functions as a publishable-truth control system: criteria must be executable, evidence must be traceable and replayable, contradictions must resolve deterministically, and scoring outputs must remain audit-defensible across documentation and PDF governance workflows.

### Decision rights
| Decision domain | R11 authority | Non-delegable boundary | Escalation path |
| --- | --- | --- | --- |
| Rubric documentation-control fitness | Recommend `approve`, `conditional approve`, or `hold` for Rubric_0 use in doc/PDF-governed scoring cycles | Cannot approve if any hard-fail in Section 6 is active | Escalate to R0 and R15 within 1 business day |
| Evidence schema adequacy for doc/PDF-related rows | Final judgment on whether evidence rules are specific enough for replay and audit | Cannot allow non-zero scoring on narrative-only or non-replayable evidence | Escalate to R15 for admissibility breach |
| Citation and source-of-truth rule quality | Final judgment on citation traceability and canonical source determinism in Rubric_0 | Cannot accept unresolved dual-authority rule paths on critical rows | Escalate to R1/R2 for ownership conflict |
| PDF gate quality in Rubric_0 | Final judgment on accessibility/render/metadata gate enforceability in scoring logic | Cannot pass Rubric_0 if gate outcomes can be bypassed by averaging | Escalate to R12 and R7 immediately |
| Contradiction protocol operability | Joint authority on contradiction taxonomy, SLA, and blocking outcomes | Cannot permit publication with unresolved critical contradiction | Escalate to R2, R8, R15 same cycle |
| High-anchor documentation governance quality | Authorize or cap `90`/`100` assignments for R11-relevant rubric quality | No `90+` without independent evidence and replay proof | Escalate to R15 on independence breach |
| Rubric delta promotion readiness | Approve or reject Rubric_0 revisions affecting documentation/PDF scoring logic | No promotion without row-level impact map and delta re-evaluation | Escalate to R12 for promotion hold |

### Meta-scoring admissibility rules
- Allowed anchors: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires explicit `who/what/where` evidence.
- No sub-dimension may score above `50` without replayable raw evidence.
- No sub-dimension may score above `75` without independent reviewer evidence.
- No sub-dimension may score above `90` without same-cycle adversarial challenge evidence.
- Evidence created after cycle cutoff is excluded from current-cycle scoring.

## 3) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R11M-01 Documentation lifecycle coverage completeness | Rubric_0 covers all R11 governance decision classes from authoring through archival. | Map Rubric_0 clauses to lifecycle classes (procedure accuracy, source-of-truth, citation, structure/readability, links, PDF accessibility/render, publication pipeline, metadata/redaction, localization, deprecation, errata). Pass if all critical classes mapped and critical unmapped count = 0. | Who: R11 meta-lead + R2 reviewer. What: coverage matrix and gap register. Where: `rubrics/Rubric_0_Comprehensive_N6_Swarm.md`, `rubrics/Rubric_0_Role_Expansion_Pack_N16.md`, R11 analysis workbook. |
| R11M-02 Procedural executability criteria falsifiability | Rubric_0 defines testable criteria for whether procedural instructions are executable. | Sample procedure-related rows and verify explicit replay test rules, pass thresholds, and failure classification. Pass if critical rows include independent replay requirement and no subjective-only acceptance language. | Who: R11 + R4/R5 reviewers. What: row audit checklist and replay-rule validation log. Where: Rubric_0 role layer and R11 role expansion clauses. |
| R11M-03 Precondition, permission, rollback, and failure-path requirement quality | Rubric_0 enforces complete procedural safety constraints in scoring logic. | Verify critical procedure rows require prerequisites, permission model, rollback steps, and failure branches. Pass if omission tolerance on critical rows = 0. | Who: R11 + R6 reviewer. What: completeness conformance report and omission exceptions list. Where: Rubric_0 scoring clauses and adjudication records. |
| R11M-04 Canonical source and ownership determinism | Rubric_0 requires one authoritative source and owner per controlled instruction domain. | Perform dual-authority conflict simulation and check mandatory conflict-resolution SLA and block behavior. Pass if unresolved critical authority conflict always blocks non-zero scoring. | Who: R11 + R1/R2 owners. What: canonical-source rule test report and conflict register. Where: Rubric_0 role layer tables and contradiction protocol section. |
| R11M-05 Citation traceability and evidence admissibility specificity | Rubric_0 citation rules are precise enough to reject unverifiable or decayed claims. | Sample non-zero rows with factual claims. Pass if claim-to-citation mapping includes locator, revision context, and provenance fields; screenshot-only evidence rejected unless paired with source export. | Who: R11 + R15. What: citation admissibility audit and broken-locator report. Where: scoring evidence package and citation index. |
| R11M-06 Standards/legal reference currency and supersession control quality | Rubric_0 defines auditable freshness rules for standards/regulatory references. | Verify explicit freshness window, supersession handling, and blocking behavior for stale mandatory references. Pass if stale mandatory references cannot support non-zero critical rows. | Who: R11 + R8. What: freshness-policy conformance sheet and supersession decision log. Where: Rubric_0 legal/compliance sections and role-layer evidence rules. |
| R11M-07 Versioning, change rationale, and diff-audit quality | Rubric_0 change logic preserves traceability between rubric versions and scoring impact. | Verify required diff rationale, approver, effective date, and impacted-row mapping for rubric edits. Pass if unauthorized scoring-affecting edits = 0. | Who: R11 rubric owner + R12 + R15. What: change-control audit and row-level diff map. Where: rubric repo history and release governance records. |
| R11M-08 Rubric information architecture and navigation operability | Rubric_0 structure supports fast, consistent scorer navigation without interpretation drift. | Timebox finding of required rows for sampled scenarios by two independent reviewers. Pass if navigation success and section-discovery SLA meet targets with low divergence. | Who: R11 IA evaluator + independent scorers. What: navigation test report and ambiguity heatmap. Where: rubric document structure and calibration logs. |
| R11M-09 Language precision and audience-fit clarity for scorers | Rubric_0 language minimizes ambiguity and clarifies intended evaluator actions. | Run ambiguity lint for vague terms and unresolved pronouns in sampled rows. Pass if critical ambiguity defects = 0 and reviewer disagreement from wording stays within tolerance. | Who: R11 editor + R3 reviewer. What: language-lint report and calibration disagreement summary. Where: Rubric_0 row text and scoring QA packet. |
| R11M-10 Terminology governance and cross-artifact consistency quality | Rubric_0 uses controlled terminology consistently across sections and role layer. | Diff terminology across master rubric and role expansions for contradictory definitions. Pass if contradiction count on high-impact terms = 0 or resolved with approved glossary update. | Who: R11 + R10 + R4. What: glossary consistency audit and term-conflict closure log. Where: rubric files and terminology registry. |
| R11M-11 Link/anchor/cross-reference integrity gate quality | Rubric_0 references are stable and testable so scoring instructions do not break in execution. | Run reference lint and anchor resolution checks on rubric links/cross-references. Pass if critical link integrity failures = 0 and broken-reference threshold policy is explicit. | Who: R11 + DocOps owner. What: link/anchor audit report and threshold config evidence. Where: build artifacts and reference integrity logs. |
| R11M-12 Command/code sample reproducibility criteria quality | Rubric_0 requires executable validation for command/code examples used as scoring evidence. | Verify rows that accept sample-based evidence require environment declaration, replay harness, and pass criteria. Pass if local-only pass claims are disallowed for high anchors. | Who: R11 + R4/R5. What: sample replay policy conformance and matrix report. Where: rubric evidence protocol and replay transcripts. |
| R11M-13 PDF accessibility semantics gate quality | Rubric_0 defines explicit, enforceable accessibility criteria for PDF-related scoring logic. | Check presence of tag structure, reading order, alt text, heading hierarchy, and AT validation requirements with blocking thresholds. Pass if critical accessibility failures deterministically block non-zero critical scoring paths. | Who: R11 PDF owner + accessibility reviewer. What: gate conformance checklist and scenario replay results. Where: Rubric_0 R11 criteria and gate-precedence rules. |
| R11M-14 PDF render determinism and layout fidelity criteria quality | Rubric_0 requires deterministic PDF output and defined tolerance for layout drift claims. | Verify rubric requires renderer matrix, deterministic rerun criteria, and semantic/binary diff tolerances. Pass if renderer-dependent variability cannot be hidden behind averaged score. | Who: DocOps engineer + R11 approver. What: determinism policy audit and renderer-variance simulation log. Where: pipeline rules and scoring simulations. |
| R11M-15 Publication pipeline gate enforceability and provenance quality | Rubric_0 publication-control gates are executable, auditable, and bypass-resistant. | Simulate gate failure with otherwise high row scores. Pass if publication-related gating still blocks outcome and bypass requires explicit penalty and approval trace. | Who: R11 + R12 + R15. What: gate precedence simulation and bypass audit log. Where: Rubric_0 gate definitions and cycle execution ledger. |
| R11M-16 Metadata/classification/redaction/disclosure rule specificity | Rubric_0 explicitly controls disclosure risk in documentation/PDF scoring evidence. | Verify required checks for metadata sanitation, classification labels, redaction validation, and hidden-layer removal. Pass if evidence policy defines immediate invalidation path for confirmed disclosure events. | Who: R11 + R7 + R8. What: control mapping audit and incident-response linkage. Where: Rubric_0 control rows and hard-gate references. |
| R11M-17 Localization and semantic fidelity governance quality | Rubric_0 localization criteria detect and penalize meaning-changing translation defects. | Verify requirement for glossary conformance, locale risk review, and critical-semantics validation for supported locales. Pass if critical semantic mismatch triggers deterministic score consequence. | Who: localization lead + R11 + R13. What: localization-governance audit and mismatch severity register. Where: Rubric_0 localization rows and release adjudication package. |
| R11M-18 Deprecation, archival, and correction-loop governance quality | Rubric_0 defines enforceable controls for deprecation notices, archival retrieval, and errata closure. | Verify rows require migration path, timelines, owner, redirect/retention controls, and correction SLA with traceability. Pass if overdue critical correction cannot be scored as healthy governance. | Who: R11 + R1/R13 + records owner. What: lifecycle-control conformance report and SLA aging log. Where: Rubric_0 lifecycle rows and defect/correction tracker. |
| R11M-19 Contradiction handling and adjudication determinism | Rubric_0 contradiction process is explicit, SLA-bound, and outcome-deterministic. | Inject contradictory scoring conditions (for example, high readability score with failed citation admissibility). Pass if contradiction taxonomy, owner, SLA, and score-impact rules produce one deterministic outcome. | Who: R11 adjudicator + R2 + R8 + R15. What: contradiction simulation suite and aging report. Where: contradiction register and adjudication minutes. |
| R11M-20 Evidence replayability and recompute fidelity | Independent reviewers can reproduce R11-relevant rubric scores from source evidence. | Replay sampled rows including all critical gates and compare anchor outcomes. Pass if anchor variance <=1 level, gate-state parity = 100%, and aggregate recompute variance within policy. | Who: independent reviewer + R15 witness. What: replay transcript, recompute sheet, variance log. Where: immutable evidence package and scoring workbook. |
| R11M-21 Score inflation resistance and high-anchor proof threshold quality | Rubric_0 structurally prevents unjustified `90`/`100` scoring in doc/PDF governance areas. | Audit high-anchor rows for independent evidence, challenge tests, and trend anomalies. Pass if unsupported `90+` rate = 0 and unexplained high-anchor density spikes trigger forced resampling. | Who: R11 scorer + R15 + R0 observer. What: inflation analytics, high-anchor evidence pack, resample decisions. Where: historical scoring ledger and cycle audit records. |
| R11M-22 Rubric change control, delta re-evaluation, and cycle-latency fit | Rubric_0 changes are controlled and operationally re-evaluated without breaking cycle cadence. | Verify each scoring-affecting delta has impact map, targeted re-score, and comparability note. Pass if cycle SLA remains achievable and unexplained anchor deltas above policy threshold = 0. | Who: R11 rubric owner + R3 + R12 + R15. What: delta dossier, re-score report, cycle timing metrics. Where: change-control records and retrospective tracker. |

## 4) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R11M-01 Documentation lifecycle coverage completeness | Critical lifecycle classes missing. | Partial classes mapped; critical gaps remain. | Most classes mapped; at least one critical class unmapped. | All critical classes mapped with minor non-critical gaps only. | Independent review confirms complete critical mapping. | Two cycles with zero unresolved critical coverage gaps. |
| R11M-02 Procedural executability criteria falsifiability | Procedure quality judged by narrative only. | Some replay language exists but lacks measurable pass rules. | Replay rules exist for core paths; critical edge paths unclear. | Measurable replay criteria cover all critical procedure paths. | Independent sample confirms low ambiguity and consistent outcomes. | Two cycles with no critical procedure-criteria ambiguity findings. |
| R11M-03 Precondition, permission, rollback, and failure-path requirement quality | Safety prerequisites absent from rubric criteria. | Safety elements listed inconsistently and not enforced. | Most safety elements defined; critical omissions still occur. | Critical rows explicitly require all safety elements and enforce consequences. | Independent audit finds no unresolved critical omission. | Two cycles with zero critical safety-element omission in sampled rows. |
| R11M-04 Canonical source and ownership determinism | Rubric allows conflicting authorities with no resolution path. | Canonical-source intent exists but conflicts are unmanaged. | Conflict process exists but critical ownership ambiguity persists. | Deterministic authority rules with SLA-bound conflict handling. | Independent simulation shows unresolved critical conflict always blocks scoring. | Two cycles with zero unresolved critical authority conflicts at publication. |
| R11M-05 Citation traceability and evidence admissibility specificity | Uncited or unverifiable claims can score non-zero. | Citation fields exist but locator/revision data is often missing. | Most citations traceable; high-impact gaps still appear. | Material claims require resolvable citation and admissible evidence fields. | Independent sampling replays citations with minimal decay. | Two cycles with zero material citation-admissibility failures. |
| R11M-06 Standards/legal reference currency and supersession control quality | Stale mandatory references are accepted. | Currency checks are ad hoc and non-blocking. | Scheduled checks exist but supersession handling is inconsistent. | Freshness windows and supersession rules are explicit and enforceable. | Independent audit confirms no stale mandatory reference in critical scoring paths. | Two cycles with zero critical stale-reference defects. |
| R11M-07 Versioning, change rationale, and diff-audit quality | Rubric changes are untracked or unexplained. | Versions labeled but rationale/impact mapping missing. | Most edits tracked; some scoring-impact diffs undocumented. | Every scoring-affecting edit has rationale, approver, and impacted-row mapping. | Independent diff audit finds no unauthorized scoring-impact edit. | Two cycles with complete change lineage and clean audit replay. |
| R11M-08 Rubric information architecture and navigation operability | Scorers cannot reliably find required criteria. | Basic structure exists but navigation is slow and inconsistent. | Core criteria findable; edge scenarios trigger frequent lookup errors. | Structure supports reliable and timely navigation for critical scenarios. | Independent scorers meet navigation SLA with low drift. | Two cycles with no critical navigation-driven scoring delay. |
| R11M-09 Language precision and audience-fit clarity for scorers | Wording is vague and frequently misinterpreted. | Some precise language exists; ambiguity remains high. | Most rows clear; critical rows still include interpretation ambiguity. | Critical rows use precise, testable wording with low ambiguity. | Calibration results show strong inter-rater agreement. | Two cycles with no critical wording-driven contradiction. |
| R11M-10 Terminology governance and cross-artifact consistency quality | Key terms conflict across rubric sections. | Glossary exists but enforcement is weak and drift is common. | Core terms consistent; several high-impact conflicts persist. | Controlled vocabulary enforced for all high-impact terms. | Independent term audit confirms resolved high-impact conflicts. | Two cycles with zero unresolved high-impact terminology conflicts. |
| R11M-11 Link/anchor/cross-reference integrity gate quality | References are broken and ungoverned. | Reference checks exist but critical breakage is common. | Most references work; critical anchor failures still occur. | Reference integrity gates are explicit with critical-failure blocking behavior. | Monitoring and repair SLA prevent persistent critical breakage. | Two cycles with zero unresolved critical reference failures. |
| R11M-12 Command/code sample reproducibility criteria quality | Sample-based evidence accepted without replay controls. | Replay expected informally; environment constraints unspecified. | Core sample controls defined; cross-environment rigor incomplete. | Sample evidence requires environment declaration and replay criteria. | Independent matrix replay confirms reproducibility for critical sample types. | Two cycles with zero unsupported critical sample claims. |
| R11M-13 PDF accessibility semantics gate quality | Accessibility is not required in scoring logic. | Accessibility checks optional and non-blocking. | Accessibility gates defined but critical-path enforcement is inconsistent. | Accessibility requirements are explicit with deterministic blocking on critical failures. | Independent AT-focused simulation confirms gate reliability. | Two cycles with zero unresolved critical accessibility gate defects. |
| R11M-14 PDF render determinism and layout fidelity criteria quality | Render determinism not addressed. | Determinism mentioned but no measurable tolerance or matrix. | Partial tolerances defined; renderer variance decisions still subjective. | Determinism and fidelity tolerances are explicit and auditable. | Independent rerun tests confirm stable outcomes across approved renderers. | Two cycles with zero critical renderer-variance adjudication defects. |
| R11M-15 Publication pipeline gate enforceability and provenance quality | Pipeline gates are bypassable or undefined. | Gates exist but precedence/bypass penalties are ambiguous. | Gates mostly enforceable; edge-case bypass risks remain. | Mandatory gates are deterministic with auditable bypass controls. | Independent simulation finds no unauthorized bypass path. | Two cycles with zero unauthorized gate bypass in scoring workflow. |
| R11M-16 Metadata/classification/redaction/disclosure rule specificity | Disclosure-risk controls absent. | Controls listed but incomplete and weakly enforced. | Controls mostly defined; critical invalidation rules are unclear. | Explicit disclosure controls with deterministic invalidation on confirmed exposure. | Independent sampling confirms control specificity and enforceability. | Two cycles with zero unresolved critical disclosure-control design defect. |
| R11M-17 Localization and semantic fidelity governance quality | Localization governance missing from rubric logic. | Governance present but critical semantic-risk checks are optional. | Core controls exist; high-risk locale checks are inconsistently applied. | Semantic-risk controls and glossary conformance are enforced for critical locales. | Independent review confirms critical mismatch handling is deterministic. | Two cycles with zero unresolved critical localization-semantic governance defects. |
| R11M-18 Deprecation, archival, and correction-loop governance quality | Deprecation/errata governance absent. | Minimal lifecycle guidance without enforceable timelines or owners. | Lifecycle controls exist but SLA enforcement remains inconsistent. | Migration, archival, and correction controls are explicit and enforceable. | Independent sample shows overdue critical correction cannot pass unaffected. | Two cycles with zero unresolved critical lifecycle-governance failures. |
| R11M-19 Contradiction handling and adjudication determinism | Contradictions are unmanaged and non-blocking. | Contradictions tracked ad hoc without SLA or score impact. | Protocol exists but critical contradiction closure is inconsistent. | Severity, owner, SLA, and score-impact rules are explicit and enforced. | Independent simulation shows deterministic outcomes for critical contradictions. | Two cycles with zero unresolved critical contradiction at publication. |
| R11M-20 Evidence replayability and recompute fidelity | Scores cannot be replayed from evidence. | Replay requires author interpretation and large variance. | Partial replay succeeds but gate-state mismatches remain. | Independent replay and recompute meet defined variance thresholds. | High-fidelity replay shows stable gate-state parity across sampled critical rows. | Two cycles with deterministic replay/recompute parity on required samples. |
| R11M-21 Score inflation resistance and high-anchor proof threshold quality | High anchors granted without stronger evidence. | Guardrails exist on paper but are often bypassed. | Guardrails partly enforced; unexplained high-anchor spikes persist. | High anchors require independent proof and anomaly-triggered resampling. | Independent audits consistently detect and correct inflation attempts. | Two cycles with zero unsupported `90+` outcomes in sampled audits. |
| R11M-22 Rubric change control, delta re-evaluation, and cycle-latency fit | Rubric deltas are unmanaged and break cadence. | Versioning exists but delta impact and re-score process are missing. | Delta process exists; comparability and timing discipline are inconsistent. | Scoring-affecting deltas require impact map, re-score, and comparability note. | Independent review confirms explained deltas and on-time cycle execution. | Two cycles with stable comparability and SLA-compliant re-evaluation cadence. |

## 5) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Freeze rubric version hash, anchor tables, and scorer roster at cycle start; scoring on unapproved hash is invalid.
2. Require independent replay for at least 20% of R11-relevant scored rows, including all critical gate rows.
3. Enforce `capture -> score -> approve` chronology; backdated approval or reordered timeline artifacts are inadmissible.
4. Reject screenshot-only citation evidence unless source export and stable locator proof are attached.
5. Audit ignored-link patterns in checker configuration; new ignore patterns require owner, rationale, and expiry.
6. Compare changelog claims against raw rubric diffs; silent scoring-affecting edits trigger mandatory rescore.
7. Recompute sampled scores from raw evidence, not dashboards; mismatch beyond tolerance triggers hold.
8. Enforce reviewer independence for `90+` anchors; author-scored-author-approved paths are invalid.
9. Run contradiction suppression audit by reconciling contradiction register, meeting notes, and final scorecard.
10. Detect denominator manipulation by comparing cycle-start and cycle-close scored row populations.
11. Require binary PDF evidence checks (accessibility, metadata, redaction) for PDF-related high anchors; source-only review is insufficient.
12. Trigger mandatory anomaly review when 90+ density increases by more than 15 percentage points cycle-over-cycle.
13. Reject post-cutoff evidence for current-cycle score increase unless formal cycle reopen is approved by R0 and R15.
14. Require dual-tool recompute parity for final aggregation and gate precedence outcomes.

## 6) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (caps and mandatory remediation)
| ID | Trigger condition | Immediate effect |
| --- | --- | --- |
| R11M-TW-01 | Replay sample fails variance tolerance on >10% of sampled rows | Cap R11M-20 at `50`; rerun replay before publication |
| R11M-TW-02 | Any mandatory anti-gaming control in Section 5 is skipped | Cap R11M-21 at `25`; no row may score above `90` |
| R11M-TW-03 | Critical contradiction remains open past SLA but before publication | Cap R11M-19 at `50`; publication hold until closure |
| R11M-TW-04 | High-anchor density anomaly lacks approved explanation and resample | Cap R11M-21 at `50`; trigger forced independent resampling |
| R11M-TW-05 | First-pass cross-role handoff acceptance falls below 80% | Cap R11M-08 and R11M-22 at `50`; require handoff contract repair |
| R11M-TW-06 | Unauthorized reference-ignore or gate-waiver pattern repeats >2 times in cycle | Cap R11M-11 or R11M-15 at `25`; escalate to R12/R15 |

### Hard-fail conditions (Rubric_0 cycle score is invalid)
| ID | Hard-fail condition | Evidence test | Effect |
| --- | --- | --- | --- |
| R11M-HF-01 | Evidence fabrication, tampering, forged provenance, or backdated approval in rubric-evaluation package | Forensic hash/signature/timestamp audit | Mark cycle `INVALID`; full forensic review and rescore required |
| R11M-HF-02 | Published score contradicts active blocking gate/tripwire state | Gate-state log vs published result reconciliation | `INVALID`; revoke publication and rerun cycle |
| R11M-HF-03 | Unresolved critical contradiction exists at publication cutoff | Contradiction register aging audit | `INVALID`; no publication until closure and impacted-row rescoring |
| R11M-HF-04 | Non-zero scores without required admissibility fields exceed 10% in sampled audit | Evidence admissibility sampling and extrapolation | `INVALID`; evidence remediation and full-scope rescore |
| R11M-HF-05 | Independent replay cannot reproduce critical gate outcomes | Critical-row replay gate-state mismatch | `INVALID`; rerun scoring with corrected evidence/process |
| R11M-HF-06 | Unauthorized scoring-affecting rubric change during active scoring window | Version-hash and diff audit | `INVALID`; revert to approved baseline and rescore |
| R11M-HF-07 | Confirmed disclosure-risk control failure is scored as non-blocking in critical row | Control-outcome vs scoring-outcome conflict audit | `INVALID`; immediate governance escalation and score revocation |
| R11M-HF-08 | Reviewer independence breach on `90+` scoring is confirmed | Role-separation/IAM and approval-chain audit | `INVALID`; affected rows void, independent reassessment required |

## 7) Cross-role dependencies and adjudication handoffs

| Counterpart role | Dependency into R11 meta-evaluation | R11 handoff output | Acceptance criteria | SLA / escalation |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor / Business Owner | Risk appetite and invalidation strictness policy for rubric publication | Meta-readiness recommendation (`approve`/`conditional`/`hold`) with residual-risk statement | Decision signed with explicit risk treatment and due dates | Escalate within 1 business day for unresolved hard-fail |
| R1 Product Manager | Canonical policy ownership boundaries and deprecation/messaging governance expectations | Source-authority conflict findings and lifecycle-governance corrections | No unresolved critical policy-authority conflict | Escalate in 2 business days if conflict persists |
| R2 Product Architect / Enterprise Architect | Boundary/ownership definitions and contradiction precedence for technical-doc controls | Contradiction classification and ownership-boundary defect report | Critical ownership contradiction resolved with deterministic rule text | Escalate in 2 business days |
| R4 Software Engineer | Executability and sample-replay realism constraints for technical instructions | Procedure replay and sample-reproducibility criteria findings | No unresolved critical executability ambiguity on scored rows | Weekly during active cycle |
| R5 QA / Test Engineer | Replay protocol, sampling tolerance, and falsifiability calibration inputs | Replay variance findings and anchor-precision defect list | Replay tolerances and falsifiability criteria accepted | Escalate same cycle on failed tolerance |
| R6 SRE / Platform Engineer | Operational runbook and rollback-control criteria constraints | Failure-path and rollback criteria enforceability findings | Critical rollback and failure-path requirements are testable and deterministic | Weekly reliability sync |
| R7 Security Engineer / Security Architect | Disclosure-risk and hard-gate interpretation for doc/PDF security controls | Metadata/redaction control sufficiency and gating defect report | No unresolved critical disclosure-control contradiction | Escalate immediately on critical conflict |
| R8 Privacy / Compliance / Legal | Legal admissibility and standards-currency requirements | Citation/legal-reference governance findings and required rubric rewrites | Mandatory legal/reference rules unambiguous and enforceable | Escalate within 1 business day for blocking legal issue |
| R10 UX Researcher / Designer | Terminology, readability, and information-architecture consistency expectations | Terminology and rubric-structure consistency defects | Critical terminology/IA conflicts resolved with approved glossary/structure update | 3 business days |
| R12 DevOps / Release Manager | Gate-precedence implementation behavior and publication workflow constraints | Gate determinism results and promotion hold/release recommendation | No bypass path for blocking gates in operational workflow | Immediate escalation on bypass risk |
| R13 Operations / Support / Customer Success | Post-publication defect trend and correction-SLA feedback loops | Correction-loop effectiveness findings and SLA-risk report | Critical correction-loop gaps have owner and dated closure plan | Weekly operations governance |
| R15 Internal Audit / Assurance | Independent replay, provenance, and score-integrity assurance | Final assurance-aligned adjudication package with closure obligations | Auditor can replay sampled outcomes without author assistance | Immediate escalation on tamper/independence breach |

Handoff adjudication rule: every handoff must end as `accepted` or `returned`; silent acceptance is invalid. Returned handoffs must include defect class, owner, due date, and resubmission timestamp.

## 8) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle phase | Checklist item | Evidence artifact | Pass criterion |
| --- | --- | --- | --- |
| Pre-cycle baseline | Freeze approved Rubric_0 version hash, anchor definitions, and scored-row population. | Baseline lock manifest and signed approvals. | Zero uncontrolled in-cycle baseline drift. |
| Pre-cycle baseline | Refresh R11 lifecycle coverage map and unresolved gap register. | Updated coverage matrix and gap closure tracker. | No unresolved critical coverage gap at cycle start. |
| Pre-cycle baseline | Validate reviewer independence assignments for high-anchor evaluation. | Role-separation matrix and attestation log. | No scorer-author-approver conflict on planned `90+` rows. |
| Calibration prep | Run wording/ambiguity lint and terminology consistency lint across impacted rubric rows. | Lint reports and remediation commits. | Zero unresolved critical ambiguity or high-impact term conflict. |
| Calibration prep | Execute dual-rater pilot scoring for representative R11-relevant rows. | Calibration variance report and adjudication notes. | Anchor disagreement within approved tolerance. |
| Mid-cycle control | Execute independent replay on >=20% sample including all critical gate rows. | Replay transcripts and variance ledger. | Replay thresholds met and gate-state parity = 100%. |
| Mid-cycle control | Run anti-gaming control suite (chronology, denominator, bypass, contradiction suppression, high-anchor proof). | Anti-gaming execution checklist and findings log. | All mandatory controls executed and evidenced. |
| Mid-cycle control | Recompute sampled and aggregate scores from raw evidence using independent calculator. | Recompute worksheet and parity report. | No unexplained mismatch beyond policy tolerance. |
| Pre-close | Reconcile contradiction register status and enforce blocking logic on unresolved critical items. | Contradiction closure report and score-impact trace. | Critical contradictions open at close = 0. |
| Pre-close | Audit citation/source integrity and legal-reference freshness on critical rows. | Citation admissibility audit and freshness report. | Zero critical admissibility/freshness defects unresolved. |
| Pre-close | Verify gate precedence determinism with scenario replay (including failed mandatory gates). | Gate simulation outputs and approval notes. | No scenario yields publishable score with active blocking gate. |
| Delta implementation | For each Rubric_0 change, produce impacted-row map and expected anchor movement rationale. | Delta dossier with row-level impact mapping. | 100% of scoring-affecting deltas mapped before promotion. |
| Delta re-evaluation | Re-score impacted rows and document explained deltas versus prior cycle. | Delta re-score report and comparability note. | Unexplained delta >1 anchor step = 0. |
| Publication | Publish final score package with tripwire/hard-fail clearance and immutable evidence index. | Final scorecard, clearance report, evidence manifest. | Non-author reviewer can replay package end-to-end. |
| Post-cycle learning | Classify defects (ambiguity, replay failure, contradiction aging, inflation, gate bypass) and assign owners. | Retrospective defect taxonomy and action register. | 100% critical defects have owner, due date, verification metric. |
| Next-cycle readiness | Verify prior-cycle corrective actions closed and re-test affected rubric rows. | Closure proof log and targeted retest report. | >=90% on-time closure and no open critical corrective action. |


---

## R12 DevOps / Release Manager

- source_file: `swarm_outputs/meta_rubric_role_expansions/R12_devops_release_manager_rubric1.md`
- words: 4763
- lines: 157

# R12 DevOps / Release Manager Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 evaluates the quality, rigor, anti-gaming strength, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 1) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R12 meta-evaluation determines whether Rubric_0 can operate as a release-control governance system under real delivery pressure. The role evaluates whether Rubric_0 is release-decision complete, gate-deterministic, evidence-replayable, contradiction-safe, and resistant to score inflation or schedule-driven bypass behavior.

### Decision rights
| Decision domain | R12 authority on Rubric_0 quality | Non-delegable rule | Escalation boundary |
| --- | --- | --- | --- |
| Release-control decision coverage | Approve or return Rubric_0 coverage of release-governance decision classes before cycle start | Cannot approve when any safety-critical release decision class is unmapped | Escalate to R0 and R2 within 1 business day |
| Gate logic and release path determinism | Accept or reject whether Rubric_0 gates produce one deterministic outcome for each release scenario | No publication if mandatory gate precedence is ambiguous or bypassable | Escalate to R12+R15 same cycle |
| Evidence admissibility for non-zero scoring | Accept or reject evidence rule quality for release-related rows | No non-zero score without complete `who/what/where`, provenance, and cutoff eligibility | Escalate to R15 immediately on tamper indicators |
| Replay and recomputation readiness | Require rework when independent replay cannot reproduce release-related rows | No score publication when replay variance exceeds tolerance | Escalate to R15 and R3 in-cycle |
| Contradiction protocol operability | Require contradiction rule correction when release controls conflict with other rubric clauses | No pass outcome with unresolved Severity-1 contradiction at cutoff | Escalate to R2, R7, R8 within same cycle |
| High-score proof threshold enforcement | Cap or reject high-anchor outcomes lacking stronger independent proof | No score >75 without independent corroboration; no score >90 without challenge evidence | Escalate to R15 on repeated inflation pattern |
| Rubric delta promotion governance | Approve or reject Rubric_0 scoring-affecting changes for next cycle | No in-cycle scoring on unapproved rubric hash or undocumented delta | Escalate to R11 and R15 on change-control breach |
| Operational cadence suitability | Accept or return Rubric_0 execution model for release-train cadence | Cannot approve a model that repeatedly delays go/no-go windows | Escalate to R3 and R0 for workflow redesign |

### Meta-scoring admissibility rules
- Allowed anchors: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires admissible evidence captured before cycle cutoff.
- No sub-dimension may score above `50` without replayable evidence.
- No sub-dimension may score above `75` without independent reviewer evidence.
- No sub-dimension may score above `90` without same-cycle adversarial challenge evidence.
- Any hard-fail in Section 5 marks the Rubric_0 cycle result `INVALID`.

## 2) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R12M-01 Release-governance decision coverage completeness | Rubric_0 covers all critical DevOps/release decision classes needed to govern safe production changes. | Build a decision catalog from R12 role expansion and global gates (`G1..G6`, `RG1..RG4`). Pass if 100% safety-critical classes and >=95% all classes map to explicit rubric clauses with scoring consequences. | Who: R12 meta-lead + R2 reviewer. What: decision-to-clause trace matrix and gap register. Where: Rubric_0 master, role expansion pack, and cycle review workbook. |
| R12M-02 CI/CD gate determinism and enforceability quality | Rubric_0 defines gate conditions that are measurable, executable, and non-bypassable. | Run scenario replay (pass/fail/waiver/backfill). Pass if each scenario yields deterministic anchor impact and gate outcome, with zero ambiguous release-permit paths. | Who: R12 + R6 + R15. What: gate scenario suite and outcome log. Where: adjudication harness and scoring simulation records. |
| R12M-03 Promotion-path integrity and merge-control evaluability | Rubric_0 explicitly evaluates promotion-path integrity, protected branch behavior, and merge control quality. | Sample relevant rows and verify explicit checks for direct-push prohibition, required status checks, and reviewer quorum logic. Pass if critical control omissions = 0 in sample. | Who: R12 + repository admin reviewer. What: clause conformance audit and omission ledger. Where: Rubric_0 role rows and control mapping sheet. |
| R12M-04 Environment parity and drift-scoring precision | Rubric_0 can evaluate parity/drift claims using auditable thresholds and remediation timing rules. | Verify that parity/drift rows require measurable thresholds, drift severity, remediation SLAs, and exception handling. Pass if no high-anchor path allows threshold-free scoring. | Who: R12 + R6 platform reviewer. What: threshold and SLA conformance report. Where: Rubric_0 rows and parity-control crosswalk. |
| R12M-05 Reproducible build and dependency-pinning evaluability | Rubric_0 enforces deterministic build and pinning evidence requirements for high scores. | Check whether rows scoring >50 require independent rebuildability and lock/pinning proof. Pass if non-deterministic build claims cannot exceed anchor 50 without explicit waiver consequence. | Who: R12 build evaluator + independent reviewer. What: rebuild requirement audit and anchor-cap validation. Where: Rubric_0 role criteria and calibration workbook. |
| R12M-06 Artifact provenance, signing, and SBOM criteria strength | Rubric_0 scoring rules for artifact trust are specific enough to reject unverifiable supply-chain claims. | Validate that scoring rules require signature verification, provenance chain, SBOM quality, and policy outcome linkage. Pass if missing trust artifacts force deterministic score penalties. | Who: R12 + R7. What: trust-control clause audit and penalty-path matrix. Where: Rubric_0 release/security sections and governance simulation logs. |
| R12M-07 Approval-chain and separation-of-duties rule quality | Rubric_0 can consistently evaluate approval legitimacy and actor authority at decision time. | Replay sampled approval-related rows with IAM snapshot logic. Pass if rules demand approver eligibility, chronology integrity, and SoD checks before high anchors. | Who: R12 + R15. What: approval-rule replay log and authority-check worksheet. Where: scoring packet, IAM snapshots, and rubric clause map. |
| R12M-08 Change classification, window, and freeze-governance evaluability | Rubric_0 defines auditable criteria for change class discipline and schedule-window control. | Simulate normal/emergency/freeze scenarios. Pass if class misuse, out-of-window release, and freeze violations have deterministic scoring effects and escalation rules. | Who: R12 + R13 operations reviewer. What: change-control scenario results and consequence map. Where: rubric change-governance rows and adjudication records. |
| R12M-09 Progressive-delivery and blast-radius safeguard evaluability | Rubric_0 can evaluate staged rollout quality and blast-radius limits without subjective interpretation drift. | Verify requirement for risk-tiering, staged exposure limits, abort thresholds, and promotion criteria. Pass if high-risk full-blast deployment cannot score above defined cap. | Who: R12 + R6 SRE reviewer. What: rollout-control audit and cap-enforcement test. Where: rubric role rows and simulation outputs. |
| R12M-10 Rollback and emergency-path governance criteria quality | Rubric_0 evaluates rollback readiness and emergency route discipline with enforceable evidence rules. | Test whether drill cadence, latency targets, integrity checks, and emergency retrospective requirements are explicit. Pass if missing rollback proof deterministically reduces anchors. | Who: R12 + incident lead reviewer. What: rollback-governance conformance report. Where: Rubric_0 release/operability rows and gate logic workbook. |
| R12M-11 Schema/data migration safety evaluability | Rubric_0 captures migration risk with clear compatibility and fallback scoring rules. | Verify requirement for migration strategy class, compatibility evidence, and rollback/forward-fix logic. Pass if irreversible migration without approved exception cannot receive high anchor. | Who: R12 + R2 architecture + data owner reviewer. What: migration-rule audit and exception simulation log. Where: Rubric_0 technical/release rows and adjudication board records. |
| R12M-12 Pre-release evidence admissibility specificity | Rubric_0 release-readiness scoring rules define concrete admissibility constraints for every non-zero claim. | Sample non-zero release-related rows. Pass if >=98% include `who/what/where`, timestamp, provenance locator/hash, and cutoff eligibility; inadmissible evidence must be excluded. | Who: R12 scorer + R15 witness. What: admissibility sample report and exclusion list. Where: cycle evidence vault and scoring ledger. |
| R12M-13 Post-release verification and regression-response evaluability | Rubric_0 can evaluate whether post-release checks and response controls are actually governance-grade. | Verify that rows require check start SLA, hypercare conditions, trigger thresholds, and mitigation timelines. Pass if customer-reported-only detection path cannot score as mature control. | Who: R12 + R13 + R6. What: post-release control quality audit. Where: rubric release/operations clauses and replay tests. |
| R12M-14 Metrics recomputation and denominator-governance robustness | Rubric_0 metric clauses prevent denominator manipulation and allow independent recomputation. | Recompute sampled release metrics from raw immutable events. Pass if published and recomputed outcomes match policy tolerance and denominator exclusions are versioned and approved. | Who: R12 analytics owner + R15. What: recomputation workbook, denominator-change log audit. Where: metric methodology docs, score history, and governance log. |
| R12M-15 Waiver and exception lifecycle governance strength | Rubric_0 evaluates bypass behavior using explicit expiry, risk, and compensating-control requirements. | Check that waiver-related rows require owner, risk score, expiry, compensating controls, renewal logic, and closure evidence. Pass if expired waiver usage always incurs deterministic penalty. | Who: R12 + risk owner + R15. What: waiver-rule conformance report. Where: rubric governance rows and exception registry audit sample. |
| R12M-16 Contradiction-handling determinism for release controls | Rubric_0 resolves release-control conflicts with clear precedence, SLA, owner, and score consequence. | Run contradiction simulations (for example speed pressure vs failed gate; release request vs legal/security blocker). Pass if critical conflicts resolve deterministically and unresolved Severity-1 contradictions block publication. | Who: R12 adjudicator + R2 + R7 + R8. What: contradiction simulation suite and closure-aging report. Where: contradiction register, rubric precedence rules, governance minutes. |
| R12M-17 Evidence replayability and score recompute fidelity | Independent evaluators can reproduce release-related Rubric_0 row scores and aggregate outcomes. | Independent replay on >=15% sampled rows including all gate-sensitive rows. Pass if anchor variance <=1 level and gate-state parity = 100%. | Who: non-author evaluator + R15 witness. What: replay transcript, recompute sheet, variance report. Where: immutable evidence package and scoring workbook. |
| R12M-18 Score inflation resistance and anchor separability quality | Rubric_0 high anchors require materially stronger proof and cannot be assigned by narrative inflation. | Audit all >75 and >90 rows for independence/challenge requirements and abrupt score jumps. Pass if unsupported high-anchor count = 0 and unexplained >15-point jumps trigger forced resample. | Who: R12 scoring owner + R15. What: high-anchor audit, jump-analysis report, resample decisions. Where: cycle score ledger and calibration records. |

## 3) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R12M-01 Release-governance decision coverage completeness | Critical release decision classes are missing from Rubric_0. | Partial mapping exists but multiple safety-critical classes are unmapped. | Most classes mapped; at least one safety-critical class lacks deterministic scoring path. | All safety-critical classes and >=95% total classes are mapped with explicit consequences. | Independent reviewer validates complete critical mapping and timely gap closure. | Two cycles with zero unresolved critical coverage gaps. |
| R12M-02 CI/CD gate determinism and enforceability quality | Gate rules are absent or non-operational in rubric scoring logic. | Gates are described but trigger/effect rules are ambiguous. | Gates mostly defined but at least one bypassable or reviewer-dependent path remains. | Gate triggers, effects, and waiver penalties are deterministic for all critical scenarios. | Independent scenario replay reproduces gate outcomes without interpretation drift. | Two cycles with zero critical gate-logic ambiguity or bypass findings. |
| R12M-03 Promotion-path integrity and merge-control evaluability | Rubric_0 cannot evaluate promotion-path integrity. | Basic merge controls mentioned; direct push/quorum controls are weak or optional. | Core controls defined; critical omissions persist in high-risk paths. | Protected-path, status-check, and quorum controls are explicit and testable. | Independent audit confirms no critical control omission in sampled clauses. | Two cycles with no material promotion-path control design defects. |
| R12M-04 Environment parity and drift-scoring precision | Parity/drift claims are accepted without measurable criteria. | Threshold language exists but lacks severity tiers or remediation timing. | Measurable thresholds defined but high-anchor penalty logic remains inconsistent. | Threshold, severity, remediation SLA, and exception logic are explicit and enforceable. | Independent review confirms threshold use is deterministic in sampled rows. | Two cycles with no threshold-free high-anchor parity/drift scoring. |
| R12M-05 Reproducible build and dependency-pinning evaluability | Rubric_0 allows high scores without deterministic build proof. | Reproducibility is stated but no independent replay expectation exists. | Replay expectations exist but pinning and exception handling remain inconsistent. | High anchors require deterministic build replay and dependency pinning evidence. | Independent non-author rebuild challenge passes on sampled high-anchor rows. | Two cycles with zero accepted high-anchor nondeterministic-build claims. |
| R12M-06 Artifact provenance, signing, and SBOM criteria strength | Trust controls are missing from scoring logic. | Trust controls listed but non-binding for scoring outcomes. | Trust controls mostly present; penalty path for missing trust artifacts is weak. | Signature/provenance/SBOM requirements are explicit with deterministic score penalties. | Independent verification confirms trust-chain requirements are replayable and strict. | Two cycles with zero high-anchor trust claims lacking admissible proof. |
| R12M-07 Approval-chain and separation-of-duties rule quality | Approval legitimacy is not evaluated. | Approval checks exist but actor authority and SoD are weakly defined. | Authority/SoD checks partially enforceable; chronology conflicts remain. | Eligibility, chronology, and SoD requirements are explicit and deterministic. | Independent replay confirms correct decision-time authority interpretation. | Two cycles with no approval-rule ambiguity affecting anchor assignment. |
| R12M-08 Change classification, window, and freeze-governance evaluability | Change class/window controls are absent. | Controls are listed but class misuse and freeze breaches are not penalized predictably. | Most controls defined; edge-case consequences depend on scorer interpretation. | Class, window, freeze, and escalation outcomes are deterministic and auditable. | Independent scenario tests confirm consistent consequence assignment. | Two cycles with zero unresolved classification/window rule defects. |
| R12M-09 Progressive-delivery and blast-radius safeguard evaluability | Rubric_0 accepts high-risk full-blast behavior as acceptable. | Staged rollout is mentioned without enforceable risk-tier or threshold logic. | Staged control rules exist but abort or blast-radius criteria remain weak. | Risk-tiered staged rollout, exposure limits, and abort rules are explicit and enforceable. | Independent challenge validates cap on high anchors when staged controls are missing. | Two cycles with zero inflation of rollout maturity despite missing safeguards. |
| R12M-10 Rollback and emergency-path governance criteria quality | Rollback/emergency governance is non-testable prose. | Some rollback/emergency checks exist but drill and retrospective rules are unclear. | Drill and emergency requirements mostly defined; consequence rules are inconsistent. | Drill cadence, latency targets, emergency controls, and penalties are deterministic. | Independent replay confirms missing rollback proof cannot score above defined cap. | Two cycles with no high-anchor rollback governance claims lacking replayable proof. |
| R12M-11 Schema/data migration safety evaluability | Migration safety is omitted from scoring logic. | Migration rules exist but compatibility/fallback evidence is optional. | Compatibility checks present; irreversible-change handling is inconsistently governed. | Compatibility and rollback/forward-fix requirements are explicit with exception penalties. | Independent simulation confirms high-anchor migration scoring requires strong proof. | Two cycles with zero high-anchor unsafe-migration scoring paths. |
| R12M-12 Pre-release evidence admissibility specificity | Non-zero release-readiness scores are narrative-only. | Admissibility fields exist but missing-field tolerance is high. | Admissibility mostly enforced; material gaps still appear in sampled rows. | Non-zero scoring requires complete admissibility fields and cutoff compliance. | Independent sample shows near-zero admissibility defects and correct exclusion behavior. | Two cycles with zero material admissibility violations on release-related rows. |
| R12M-13 Post-release verification and regression-response evaluability | Rubric_0 cannot evaluate post-release control quality. | Post-release checks are generic and lack SLA/trigger rigor. | Check and response rules mostly defined; critical threshold behavior is inconsistent. | Post-release checks, hypercare, triggers, and response SLAs are explicit and testable. | Independent replay confirms deterministic scoring when threshold-response evidence is missing. | Two cycles with no high-anchor post-release maturity scoring without control proof. |
| R12M-14 Metrics recomputation and denominator-governance robustness | Metric clauses permit opaque or manipulated reporting. | Metrics are named but denominator and versioning rules are weak. | Recompute possible for some metrics; denominator drift checks are incomplete. | Metrics are recomputable from immutable events with controlled denominator governance. | Independent recomputation and denominator audit consistently match published outcomes. | Two cycles with zero unresolved denominator-manipulation findings. |
| R12M-15 Waiver and exception lifecycle governance strength | Rubric_0 ignores waiver hygiene. | Waivers acknowledged but expiry/risk/closure rules are weak. | Lifecycle rules mostly defined; recurrence and expiry enforcement remain inconsistent. | Owner/risk/expiry/compensating-control/closure rules are explicit and enforceable. | Independent sample confirms expired waivers always produce deterministic penalties. | Two cycles with no waiver-lifecycle governance blind spot in scoring logic. |
| R12M-16 Contradiction-handling determinism for release controls | Contradictions are unmanaged and non-blocking. | Contradictions are tracked but without deterministic precedence or SLA effects. | Protocol exists but critical conflict outcomes still vary by evaluator. | Precedence, owner, SLA, and score consequences are explicit and deterministic. | Independent conflict simulation yields consistent decisions across evaluators. | Two cycles with zero unresolved Severity-1 release-control contradiction at cutoff. |
| R12M-17 Evidence replayability and score recompute fidelity | Scores cannot be independently replayed from evidence package. | Replay succeeds only with author interpretation or missing raw evidence. | Partial replay succeeds; gate-state or anchor variance exceeds tolerance on critical rows. | Independent replay meets anchor/gate parity tolerance for required sample. | Non-author replay repeatedly reproduces high-impact rows with minimal variance. | Two cycles with full required replay parity and no material recomputation drift. |
| R12M-18 Score inflation resistance and anchor separability quality | High anchors are assignable without stronger evidence. | Anchor wording is weakly separated and easily inflated. | Some high-anchor guardrails exist but are inconsistently enforced. | Anchors are behaviorally distinct and high-anchor proof thresholds are enforced. | Inflation checks catch and remediate unsupported high-anchor assignments in-cycle. | Two cycles with zero unsupported >75 or >90 outcomes in audited sample. |

## 4) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Freeze Rubric_0 version hash, role-row population, and scoring formulas at cycle open; scoring on unapproved hash is invalid.
2. Run forced-fail gate simulations each cycle and confirm deterministic penalty outcomes for release-governance rows.
3. Recompute sampled release metrics directly from immutable event sources; dashboard-only evidence is inadmissible.
4. Reject post-cutoff evidence for current-cycle score increase unless formal reopen approval exists.
5. Audit chronology integrity (`capture -> score -> approve -> publish`); out-of-order records invalidate affected rows.
6. Validate approver authority against decision-time IAM/HR snapshots, not current role assignments.
7. Detect denominator drift by comparing cycle-start and cycle-close population definitions and exclusion logic.
8. Enforce independent review for all anchors >75 and adversarial challenge for anchors >90.
9. Trigger mandatory resampling when any sub-dimension increases by >15 points without approved delta rationale.
10. Compare contradiction register to final score packet; hidden unresolved contradictions force publication hold.
11. Audit waiver recurrence patterns for repeated short renewals on same control gap (waiver laundering).
12. Sample for narrative inflation: claims without `who/what/where` and provenance are auto-scored as zero.
13. Run cross-rater divergence checks on sampled rows; unexplained divergence >1 anchor level triggers adjudication replay.
14. Verify manual override controls by reconciling computed scores with published scores and signed rationale records.

## 5) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (caps, holds, and invalidation if unresolved by cutoff)
| ID | Trigger condition | Immediate effect | If unresolved at publication cutoff |
| --- | --- | --- | --- |
| R12M-TW-01 | Independent replay variance exceeds tolerance on >10% sampled release-related rows | Cap `R12M-17` at `50`; mandatory replay root-cause analysis | Cycle result `INVALID` |
| R12M-TW-02 | Any mandatory anti-gaming control in Section 4 is skipped | Cap `R12M-18` at `25`; no sub-dimension may exceed `90` | Cycle result `INVALID` |
| R12M-TW-03 | Severity-1 contradiction affecting release controls remains open past SLA | Cap `R12M-16` at `50`; publication hold | Cycle result `INVALID` |
| R12M-TW-04 | Any score >75 lacks independent evidence or any score >90 lacks challenge evidence | Cap `R12M-18` at `25`; forced re-score of affected rows | Cycle result `INVALID` |
| R12M-TW-05 | Denominator or formula changes occur after poor results without approved change record | Cap `R12M-14` and `R12M-18` at `25`; full recalculation required | Cycle result `INVALID` |
| R12M-TW-06 | Gate simulation identifies a publishable pass path with active blocking gate | Cap `R12M-02` at `25`; immediate gate-logic correction required | Cycle result `INVALID` |

### Hard-fail conditions (Rubric_0 cycle score invalid)
| ID | Hard-fail condition | Evidence test | Effect |
| --- | --- | --- | --- |
| R12M-HF-01 | Evidence fabrication, tampering, forged provenance, or backdated approval in rubric-evaluation package (`G1`) | Hash/signature/timestamp forensic audit | Cycle marked `INVALID`; forensic review and full re-score required |
| R12M-HF-02 | Unresolved critical contradiction at cutoff on release/spec/control interpretation (`G2` or `RG3`) | Contradiction register SLA-aging audit | Cycle marked `INVALID` until resolved and impacted rows rescored |
| R12M-HF-03 | Release-related legal/privacy/security mandatory control breach is active but scored as non-blocking (`G3`) | Cross-check R7/R8 blocker state against scoring outcome | Cycle marked `INVALID` |
| R12M-HF-04 | Critical operability path failure exists while rubric outcome is publishable pass (`G4`) | Operability evidence vs published outcome reconciliation | Cycle marked `INVALID` |
| R12M-HF-05 | Independent replay/recompute cannot reproduce material release-governance claims (`G5`) | Witness replay failure on critical sample | Cycle marked `INVALID`; full replay and re-score required |
| R12M-HF-06 | Score publication occurs without required authority-chain approvals (`G6`) | Approval-chain and decision-time authority audit | Cycle marked `INVALID`; governance breach escalation |
| R12M-HF-07 | Critical role score <60 without enforced fail behavior (`RG1`) | Role-layer calculation and decision-rule audit | Cycle marked `INVALID` |
| R12M-HF-08 | Role evidence package integrity/provenance failure is ignored (`RG4`) | Evidence integrity sampling and adjudication log audit | Affected role score = 0 and cycle marked `INVALID` |
| R12M-HF-09 | Out-of-band deployment-path evidence (manual/untracked path) is ignored in rubric evaluation of release controls | Deployment-path reconciliation against rubric scoring packet | Cycle marked `INVALID` pending corrected controls and re-score |
| R12M-HF-10 | Unauthorized Rubric_0 change during active scoring window alters anchors/weights/gates | Version diff and approval-record audit | Cycle marked `INVALID`; revert and re-run on approved baseline |

## 6) Cross-role dependencies and adjudication handoffs

| Counterpart role | Dependency into R12 meta-evaluation | R12 handoff output | Acceptance criteria | SLA / escalation trigger |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor / Business Owner | Governance appetite for invalidation strictness and publication risk posture | Rubric_0 release-governance readiness verdict (`approve`/`conditional`/`hold`) | Explicit decision state plus residual-risk treatment and due dates | Escalate critical deadlock within 1 business day |
| R1 Product Manager | Scope and release-goal decision classes that Rubric_0 must adjudicate under pressure | Contradiction disposition on scope-pressure vs gate-integrity conflicts | Deterministic precedence recorded; no unresolved Severity-1 conflict | Escalate within 2 business days |
| R2 Product Architect / Enterprise Architect | Architecture and migration constraints for release-governance scoring quality | Coverage-gap findings for architecture-dependent release controls | No unresolved critical architecture-control mismatch | Escalate same cycle on critical mismatch |
| R3 Engineering Manager | Cycle throughput constraints and staffing feasibility for rubric execution | Cadence-fit findings and required workflow adjustments | Scoring cycle SLA feasible without go/no-go delay | Escalate on repeated SLA miss risk |
| R5 QA / Test Engineer | Verification evidence schema and replay sample design inputs | Admissibility and replay variance findings for release-related rows | Replay tolerance met and evidence defects triaged | Immediate escalation for replay failure trend |
| R6 SRE / Platform Engineer | Runtime reliability and rollback expectations in gate logic | Joint gate determinism and contradiction-handling outcomes | No publishable pass with active reliability hard gate | Same-day escalation on bypass path |
| R7 Security Engineer / Security Architect | Supply-chain trust and security-gate interpretation requirements | Security-sensitive gate and trust-control adequacy findings | No unresolved security gating contradiction at cutoff | Immediate escalation on critical security blocker |
| R8 Privacy / Compliance / Legal | Compliance and legal blocker semantics for release-governance rows | Legal/privacy contradiction adjudication and required clause rewrites | Mandatory legal/privacy controls are deterministic and enforceable | Escalate within 1 business day |
| R11 Technical Writer / DocOps / PDF Owner | Change-control publication discipline and rubric version governance | Delta-impact and documentation-governance handoff for rubric revisions | Version/delta records complete and replay-ready | Escalate if scoring-affecting change lacks approved rationale |
| R13 Operations / Support / Customer Success | Post-release response expectations and incident communication criteria | Post-release evaluability findings and hypercare governance requirements | Post-release control quality criteria accepted and operational | Escalate if response-SLA criteria remain ambiguous |
| R15 Internal Audit / Assurance | Independent assurance of replay, provenance, and anti-gaming execution | Final assurance-aligned adjudication memo with open-risk list | Auditor replay succeeds and material exceptions are dispositioned | Immediate escalation on any integrity breach |

Adjudication rule: each handoff must end as `accepted` or `returned`. Silent acceptance is invalid. Returned handoffs must include defect class, owner, due date, and resubmission timestamp.

## 7) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle phase | Checklist item | Evidence artifact | Pass criterion |
| --- | --- | --- | --- |
| Pre-cycle baseline | Freeze Rubric_0 hash, anchor tables, score formulas, gate precedence, and role-row population. | Baseline manifest and approval record. | Zero uncontrolled baseline drift during cycle. |
| Pre-cycle baseline | Refresh release-governance decision coverage matrix against latest Rubric_0 and R12 role expansion. | Coverage matrix and gap register. | No unresolved safety-critical coverage gap at cycle start. |
| Pre-cycle baseline | Reconfirm contradiction taxonomy, precedence rules, severity thresholds, and SLA timers. | Contradiction protocol packet. | No ambiguity in Severity-1 ownership or closure effect. |
| Pre-cycle baseline | Confirm scorer independence assignments for >75 and >90 anchor candidates. | Independence roster and attestations. | No scorer-author-approver conflict in planned high-anchor sample. |
| Calibration prep | Execute anchor separability review on all R12 meta sub-dimensions. | Anchor calibration log and ambiguity findings. | Critical anchor ambiguity defects unresolved = 0. |
| Calibration prep | Run dual-rater dry run on representative gate-sensitive rows. | Dual-rater variance report. | Unexplained divergence >1 anchor level = 0. |
| Mid-cycle control | Execute full anti-gaming checklist (Section 4) and document outcomes. | Anti-gaming execution report and remediation tickets. | 100% mandatory controls executed with evidence. |
| Mid-cycle control | Perform independent replay on >=15% sampled rows including all gate-sensitive rows. | Replay transcripts and variance workbook. | Replay tolerance met and gate parity = 100%. |
| Mid-cycle control | Recompute release-related metric rows from immutable events and reconcile with published scores. | Recompute worksheet and reconciliation report. | No unexplained metric/denominator mismatch. |
| Mid-cycle control | Audit contradiction register aging and enforce blocking outcomes for open Severity-1 items. | Aging report and score-impact trace. | Open Severity-1 contradictions at pre-close = 0. |
| Pre-close | Verify all >75 and >90 row evidence meets independence/challenge proof thresholds. | High-anchor evidence audit and exception log. | Unsupported high-anchor count = 0. |
| Pre-close | Run gate-precedence simulation suite including fail, waiver, and conflicting-control scenarios. | Simulation output and sign-off log. | No publishable pass path when blocking gate is active. |
| Delta implementation | For each approved Rubric_0 delta, produce impacted-row map and expected anchor movement rationale. | Delta dossier with impact mapping. | 100% scoring-affecting deltas mapped before use. |
| Delta re-evaluation | Re-score only impacted rows and rerun contradiction/gate/replay tests on affected scope. | Delta re-score packet and targeted replay report. | Unexplained delta >1 anchor level in impacted rows = 0. |
| Publication gate | Apply tripwire and hard-fail checks before publishing cycle score. | Tripwire/hard-fail clearance report. | Active hard-fail count = 0. |
| Post-cycle learning | Classify defects (coverage gap, contradiction, replay failure, inflation, latency) and assign corrective actions. | Retrospective defect taxonomy and action register. | 100% critical defects have owner, due date, verification metric. |
| Next-cycle readiness | Verify closure of prior-cycle critical actions and retest affected rubric clauses. | Closure proof and retest results. | No open critical corrective action at next cycle start. |


---

## R13 Operations / Support / Customer Success

- source_file: `swarm_outputs/meta_rubric_role_expansions/R13_operations_support_customer_success_rubric1.md`
- words: 4797
- lines: 164

# R13 Operations / Support / Customer Success Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 evaluates the quality, rigor, anti-gaming strength, contradiction safety, evidence replayability, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 2) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R13 meta-evaluation verifies that Rubric_0 can govern support and customer-facing operations decisions under pressure without narrative drift. The role checks whether Rubric_0 is executable in real incident and ticket workflows, produces deterministic scoring outcomes, resists metric gaming, and remains audit-defensible for release and governance decisions.

### Decision rights (R13 meta-evaluator)
| Decision domain | R13 authority | Non-delegable boundary | Escalation path |
| --- | --- | --- | --- |
| Rubric_0 operations/support fitness recommendation | Recommend `approve`, `conditional approve`, or `hold` for Rubric_0 use in cycle scoring | Cannot approve if any hard-fail in Section 6 is active | Escalate to R0 and R15 within 1 business day |
| Operational criteria testability quality | Accept/reject whether Rubric_0 support-related rows are falsifiable and auditable | Cannot accept subjective-only criteria for `75+` anchors | Escalate to R5 and R2 in current cycle |
| Evidence admissibility sufficiency for support rows | Decide whether Rubric_0 evidence schema is adequate for non-zero operational scoring | Cannot allow non-zero score without explicit `who/what/where` evidence | Escalate to R15 on admissibility failure |
| Contradiction protocol operability for support conflicts | Joint authority on contradiction class, owner, SLA, and score consequences | Cannot permit publication with unresolved critical contradiction impacting support criteria | Escalate to R2, R8, and R15 immediately |
| High-anchor authorization quality | Authorize, cap, or return `90/100` assignments in support-relevant rubric rows | No `90+` without independent validation and same-cycle challenge evidence | Escalate to R15 for independence breach |
| SLA/entitlement scoring integrity | Validate that Rubric_0 metric definitions cannot be changed mid-cycle without score consequences | Cannot accept pass outcome when SLA definitions drift without approved restatement path | Escalate to R12 and R14 same cycle |
| Release-veto and incident-gate enforceability | Validate that active operational blockers in Rubric_0 cannot be averaged away | Cannot accept scoring logic that allows pass with active blocker gates | Escalate to R0 and R12 same day |
| Rubric delta promotion readiness | Approve or reject Rubric_0 changes affecting operations/support scoring logic | No promotion without impacted-row map and targeted re-evaluation | Escalate to R11 and R15 on change-control breach |

### Meta-scoring admissibility rules
- Anchor scale: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires explicit admissible `who/what/where` evidence.
- No sub-dimension may score above `50` without replayable raw evidence.
- No sub-dimension may score above `75` without independent reviewer validation.
- No sub-dimension may score above `90` without same-cycle adversarial challenge evidence.
- Evidence created after cycle cutoff is excluded unless formal reopen approval exists.

## 3) Sub-dimensions table

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R13M-01 Operations-support coverage completeness | Rubric_0 fully covers supportability, incident response, ticket quality, and customer-success governance decision classes. | Map canonical R13 concern set to Rubric_0 clauses; critical concern mapping must be 100% and overall mapping >=95%. | Who: R13 lead + R1 reviewer. What: concern-to-clause trace matrix and gap log. Where: Rubric_0 master, role expansion pack, meta-review workbook. |
| R13M-02 Intake and taxonomy criterion testability | Rubric_0 criteria for intake channels, metadata completeness, and deduplication are measurable and enforceable. | Sample intake-related rows for explicit thresholds, ownership, and consequence logic; subjective-only rows in critical paths must be 0. | Who: support operations owner + R5 verifier. What: row testability audit and defect register. Where: Rubric_0 role rows and scoring QA packet. |
| R13M-03 Severity calibration and escalation determinism | Rubric_0 defines deterministic severity and escalation scoring rules with low scorer drift. | Run blind replay on sampled severity/escalation scenarios; anchor agreement >=95% and escalation-path outcome agreement = 100%. | Who: R13 adjudicator + R6 counterpart + independent scorer. What: scenario replay outputs and variance report. Where: adjudication simulator and cycle evidence archive. |
| R13M-04 SLA and entitlement metric-definition integrity | Rubric_0 prevents SLA/entitlement scoring from denominator or definition manipulation. | Verify rows require metric dictionary freeze, tier mapping controls, and restatement protocol; simulate mid-cycle definition change and confirm forced cap/fail behavior. | Who: R13 analyst + R14 contract reviewer + R15 witness. What: metric-governance audit and simulation log. Where: Rubric_0 criteria tables, metric dictionary, scorebook tests. |
| R13M-05 Incident communication and status-governance enforceability | Rubric_0 includes auditable controls for customer incident communication timing, accuracy, and status posting discipline. | Confirm criteria require update start SLA, cadence adherence, correction logging, and status reconciliation checks with explicit scoring consequences. | Who: incident comms lead + R11 reviewer + R13 evaluator. What: communication-control conformance review. Where: Rubric_0 rows, status governance policy, replay notes. |
| R13M-06 Runbook/workaround/rollback evaluability | Rubric_0 can evaluate whether runbook criteria are executable and safe under failure conditions. | Check for required preconditions, stop criteria, rollback steps, and dry-run evidence; missing safety elements on critical rows must force non-pass anchors. | Who: runbook owner + R6 reviewer + R13 evaluator. What: runbook-criteria completeness audit. Where: Rubric_0 support/operability rows and gate simulations. |
| R13M-07 Case chronology and evidence-chain admissibility | Rubric_0 requires replayable, tamper-evident case chronology for non-zero scoring. | Audit sampled case-evidence requirements for timestamp, actor, action, rationale, and immutable references; screenshot-only evidence cannot support `>50`. | Who: QA analyst + R15 assurance reviewer. What: admissibility audit and tamper-control check. Where: evidence schema rules and sampled scoring packets. |
| R13M-08 Closure validation and reopen-control criterion quality | Rubric_0 closure-quality criteria are measurable and tied to reopen outcomes. | Verify closure rows require confirmation evidence, checklist completion, and reopen-window monitoring with deterministic penalty rules. | Who: case quality lead + R5 reviewer + R13 evaluator. What: closure-criteria audit and reopen-scenario replay. Where: Rubric_0 closure rows and adjudication test log. |
| R13M-09 Recurrence prevention and problem-management rigor | Rubric_0 converts repeated support failures into enforceable problem-management scoring logic. | Check RCA trigger conditions, action ownership, due-date controls, and effectiveness verification requirements; recurrence-without-owner must trigger cap/fail. | Who: problem manager + R3 reviewer + R13 evaluator. What: recurrence-control conformance report. Where: Rubric_0 rows, action-governance rules, simulation outputs. |
| R13M-10 User-impact quantification rule rigor | Rubric_0 requires explicit impact quantification method quality for incident and support scoring. | Validate criteria require affected users/accounts, duration, business impact method, and estimate true-up logic; aggregate-only impact claims must be ineligible for high anchors. | Who: incident analyst + finance partner + R13 evaluator. What: impact-method audit and replay comparison. Where: Rubric_0 impact rows and recompute workbook. |
| R13M-11 Engineering handoff and reproducibility packet quality | Rubric_0 enforces support-to-engineering handoff requirements that reduce bounce-back and ambiguity. | Verify criteria mandate reproducible steps, logs, scope, and urgency context; run sampled handoff adjudication for deterministic pass/fail outcomes. | Who: escalation lead + R4 counterpart + R13 evaluator. What: handoff-quality audit and acceptance-variance report. Where: Rubric_0 handoff criteria and sampled handoff packets. |
| R13M-12 Product feedback loop evaluability | Rubric_0 can evaluate whether customer pain is converted into tracked product decisions and closed-loop communication. | Confirm criteria require theme quantification, owner assignment, decision traceability, and customer follow-through evidence with score effects for missing closure. | Who: CS operations lead + R1 reviewer + R13 evaluator. What: feedback-loop criteria test report. Where: Rubric_0 R13 rows, decision logs, VOC evidence index. |
| R13M-13 Staffing/on-call/tooling operability-fit quality | Rubric_0 operations criteria are executable within real staffing and tooling constraints without ambiguity. | Dry-run scoring cycle for staffing/tooling-related rows and measure adjudication latency, exception clarity, and decision consistency under simulated surge conditions. | Who: workforce manager + support systems owner + R3 reviewer. What: operability dry-run report and timing metrics. Where: cycle rehearsal artifacts and governance tracker. |
| R13M-14 CSAT/CES signal-integrity evaluability | Rubric_0 can detect biased sampling and invalid satisfaction signal usage in scoring. | Verify criteria require response-rate thresholds, bias checks, suppression controls, and action closure evidence; cherry-picked cohorts must cap scoring. | Who: CS analyst + R9 reviewer + R13 evaluator. What: signal-integrity criteria audit and bias simulation results. Where: Rubric_0 customer signal rows and scoring simulation logs. |
| R13M-15 Contradiction-handling determinism for support governance | Rubric_0 contradiction protocol resolves support-critical conflicts deterministically (for example SLA pass vs unresolved critical incident evidence). | Inject contradiction scenarios and verify severity classification, owner assignment, SLA, and score-impact path produce one deterministic outcome; unresolved Severity-1 contradiction must block publication. | Who: R13 adjudicator + R2 + R8 + R15. What: contradiction simulation suite and aging report. Where: contradiction register and adjudication minutes. |
| R13M-16 Independent replayability and recompute fidelity | Independent reviewers can reproduce support-relevant Rubric_0 scores from raw evidence and rule definitions. | Replay >=20% sampled rows including all gate-sensitive rows; pass if anchor variance <=1 level, score variance <=5 points, and gate-state parity = 100%. | Who: independent non-author scorer + R15 witness + R13 observer. What: replay transcripts and recompute sheets. Where: immutable evidence store and replay workspace. |
| R13M-17 Score inflation resistance and high-anchor guardrails | Rubric_0 structurally resists inflated support-governance scoring. | Validate enforced prerequisites for `>75` and `>90`, anomaly detection for score-density spikes, and mandatory resampling for unexplained jumps. | Who: R13 scoring owner + R15 validator + R0 observer. What: inflation audit pack and distribution analysis. Where: scoring ledger, approval history, anti-gaming logs. |
| R13M-18 Delta change-control and cycle-cadence fit | Rubric_0 changes for support-related scoring logic are controlled, explainable, and operationally re-evaluable within cycle SLAs. | Verify every scoring-affecting delta has impacted-row map, comparability note, targeted re-score, and on-time execution; unexplained anchor deltas >1 step must be 0. | Who: R13 owner + R12 + R11 + R15. What: delta dossier, timing report, and re-score outputs. Where: change-control records and cycle retrospective package. |

## 4) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R13M-01 Operations-support coverage completeness | Critical R13 decision classes are missing. | Partial mapping exists; multiple critical gaps remain. | Most concerns mapped; at least one critical concern unmapped. | All critical concerns mapped with explicit scoring consequence paths. | Independent review confirms complete critical mapping and low ambiguity. | Two cycles with zero unresolved critical coverage gaps. |
| R13M-02 Intake and taxonomy criterion testability | Intake/taxonomy rows are narrative-only. | Criteria exist but omit thresholds or owners on critical paths. | Core thresholds present; consequence logic inconsistent. | Criteria are measurable with explicit owners, thresholds, and fail effects. | Independent sample shows consistent scoring outcomes with low drift. | Two cycles with zero critical intake-row ambiguity findings. |
| R13M-03 Severity calibration and escalation determinism | Severity/escalation scoring produces arbitrary outcomes. | Basic rules exist but high scorer disagreement persists. | Determinism for common cases only; critical edge cases remain ambiguous. | Deterministic severity/escalation outcomes for critical and edge cases. | Independent replay meets agreement targets and no unresolved critical disputes. | Two cycles with no critical severity/escalation adjudication variance beyond policy. |
| R13M-04 SLA and entitlement metric-definition integrity | Rubric allows ungoverned metric definition changes. | Definitions exist but denominator and tier controls are weak. | Freeze/restatement rules partly defined; manipulation risk remains. | Metric definitions, denominators, and restatement logic are enforceable. | Independent simulation confirms mid-cycle manipulation attempts are penalized. | Two cycles with zero unapproved metric-definition drift accepted in scoring. |
| R13M-05 Incident communication and status-governance enforceability | Communication/status discipline is absent from evaluable criteria. | Criteria are present but timing and correction rules are non-binding. | Timing/cadence rules exist; reconciliation and consequence paths are inconsistent. | Communication/status criteria are measurable with explicit consequence rules. | Independent replay confirms deterministic penalties for late/inaccurate updates. | Two cycles with zero critical communication-governance scoring contradictions. |
| R13M-06 Runbook/workaround/rollback evaluability | Runbook safety/executability is not evaluable. | Criteria mention runbooks without rollback or stop controls. | Most safety elements defined; critical omissions remain possible. | Full safety/executability criteria with deterministic score consequences. | Independent simulation confirms failed runbook safety evidence is penalized consistently. | Two cycles with zero critical runbook-criteria omission accepted for non-zero scoring. |
| R13M-07 Case chronology and evidence-chain admissibility | Non-zero scores allowed without replayable chronology evidence. | Evidence requirements are partial and tamper controls weak. | Most fields required; immutability/cutoff controls inconsistent. | Complete chronology and admissibility requirements enforced for non-zero scoring. | Independent audit shows high completeness and no unresolved tamper signals. | Two cycles with zero admissibility defects in sampled critical rows. |
| R13M-08 Closure validation and reopen-control criterion quality | Closure quality cannot be judged objectively. | Closure criteria exist but confirmation evidence is optional. | Confirmation and reopen checks exist with inconsistent consequences. | Closure and reopen controls are explicit, measurable, and enforced. | Independent scenario tests confirm deterministic score impact for weak closure evidence. | Two cycles with no critical closure-criteria contradiction at close. |
| R13M-09 Recurrence prevention and problem-management rigor | Rubric does not connect recurrence to control improvements. | RCA/action expectations exist but ownership and due-date enforcement weak. | Core recurrence controls exist; effectiveness checks are inconsistent. | Recurrence controls enforce RCA triggers, ownership, deadlines, and effectiveness testing. | Independent review confirms repeated failure without action cannot score above threshold. | Two cycles with zero accepted high anchors on unresolved recurring failure classes. |
| R13M-10 User-impact quantification rule rigor | Impact can be claimed without method or evidence. | Partial impact fields exist; method and true-up controls weak. | Method requirements defined for major cases only. | Impact criteria require method disclosure, baseline, and true-up with consequences. | Independent recomputation confirms claimed impact scores are reproducible. | Two cycles with zero unsupported high-anchor impact claims in sample audits. |
| R13M-11 Engineering handoff and reproducibility packet quality | Handoff quality is not enforceable in rubric scoring. | Handoff criteria exist without reproducibility minimums. | Reproducibility expectations partially specified; high drift remains. | Handoff criteria are explicit and produce consistent pass/fail outcomes. | Independent sample shows high agreement and low bounce-back ambiguity. | Two cycles with no critical handoff-criteria ambiguity defects. |
| R13M-12 Product feedback loop evaluability | Rubric does not evaluate feedback-to-decision closure. | Feedback criteria are narrative and ownerless. | Owner/decision fields exist; closure evidence requirements weak. | Criteria enforce quantified themes, decisions, owners, and customer loop closure. | Independent review confirms missing closure evidence is penalized consistently. | Two cycles with zero unresolved critical feedback-loop governance defects. |
| R13M-13 Staffing/on-call/tooling operability-fit quality | Rubric cannot be executed within operational realities. | Criteria are too abstract and create repeated adjudication delays. | Execution possible but ambiguity and timing defects persist. | Criteria are operationally executable within defined cycle timing. | Multi-team dry-run confirms low ambiguity and stable timing under stress. | Two cycles meeting SLA with no rubric-induced operational deadlock. |
| R13M-14 CSAT/CES signal-integrity evaluability | Rubric accepts biased satisfaction signals without controls. | Signal controls exist but sampling-bias requirements are weak. | Bias checks exist with partial enforceability and weak consequence paths. | Signal-integrity controls are explicit and enforceable for non-zero scoring. | Independent bias simulation confirms cherry-pick patterns are detected and penalized. | Two cycles with zero unsupported high-anchor CSAT/CES interpretations. |
| R13M-15 Contradiction-handling determinism for support governance | Contradictions are unmanaged or non-blocking. | Contradictions logged without SLA or score-impact logic. | Protocol exists but critical contradiction closure is inconsistent. | Deterministic contradiction protocol with severity, owner, SLA, and outcome rules. | Independent simulation shows unresolved critical contradictions always block publication. | Two cycles with zero unresolved critical contradiction at publication cutoff. |
| R13M-16 Independent replayability and recompute fidelity | Independent replay cannot reproduce support-related scores. | Replay depends on author interpretation and high variance. | Partial replay success; gate-state or anchor variance exceeds policy in sample. | Replay and recompute meet variance thresholds with full gate-state parity. | Independent replay is stable across critical sampled rows. | Two cycles with deterministic replay/recompute parity on required samples. |
| R13M-17 Score inflation resistance and high-anchor guardrails | High anchors are granted without stronger proof. | Guardrails exist on paper but are routinely bypassed. | Controls partly enforced; unexplained high-score density spikes persist. | High-anchor controls are enforced with mandatory independent/challenge evidence. | Independent inflation audits detect and correct manipulation attempts in-cycle. | Two cycles with zero unsupported `90+` outcomes in sampled audits. |
| R13M-18 Delta change-control and cycle-cadence fit | Support-related rubric deltas are unmanaged and break cycle comparability. | Versioning exists but impact mapping and re-score rules are missing. | Delta workflow exists; comparability and cadence discipline inconsistent. | Every scoring-affecting delta has impact map, targeted re-score, and cadence compliance. | Independent review confirms explained deltas and on-time cycle execution. | Two cycles with stable comparability and no unexplained impacted-row delta >1 anchor step. |

## 5) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Freeze Rubric_0 version hash, anchor table, and denominator population at cycle start; scoring on unfrozen artifacts is invalid.
2. Enforce chronology integrity: `capture -> score -> approve -> publish`; out-of-order records are inadmissible.
3. Recompute sampled SLA and entitlement metrics from raw ticket/event logs; dashboard-only screenshots cannot support non-zero scoring.
4. Require metric-dictionary freeze; mid-cycle metric definition changes trigger automatic cap and mandatory restatement.
5. Run independent re-grade on sampled severity decisions to detect intentional downgrade patterns.
6. Detect auto-ack inflation by validating first-response evidence includes meaningful diagnosis or next-step content.
7. Reject closure-quality claims without confirmation/reopen evidence inside the defined window.
8. Detect ticket-splitting and pause-state abuse that artificially improves SLA or MTTR metrics.
9. Reconcile incident register to status communication records to detect selective omission.
10. Validate CSAT/CES sampling integrity by segment, severity, and outcome; suppression pockets invalidate high anchors.
11. Enforce high-anchor proof thresholds: `>75` requires independent validation, `>90` requires same-cycle challenge evidence.
12. Run contradiction suppression audit by reconciling contradiction register, adjudication notes, and final score output.
13. Detect manual score overrides by diffing computed and published scores; undocumented overrides invalidate affected rows.
14. Exclude post-cutoff evidence from current-cycle score increases unless formal reopen approval exists.
15. Require at least 20% non-author replay sample including all gate-sensitive support rows each cycle.

## 6) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (caps, holds, or forced rescore)
| ID | Trigger condition | Immediate effect | If unresolved at publication cutoff |
| --- | --- | --- | --- |
| R13M-TW-01 | Any mandatory anti-gaming check in Section 5 is skipped | Cap `R13M-17` at `25`; no row may score above `90` | Cycle `INVALID` |
| R13M-TW-02 | Independent replay variance exceeds tolerance on >10% sampled rows | Cap `R13M-16` at `50`; targeted replay root-cause required | Cycle `INVALID` |
| R13M-TW-03 | Any `>75` score lacks independent evidence | Downgrade affected rows to `50`; open inflation review | Cycle `INVALID` |
| R13M-TW-04 | Any `>90` score lacks same-cycle challenge evidence | Downgrade affected rows to `75`; mandatory resampling | Cycle `INVALID` |
| R13M-TW-05 | First-pass cross-role handoff acceptance on critical support rows <80% | Cap `R13M-11` and `R13M-13` at `50`; handoff protocol repair required | Publication hold |
| R13M-TW-06 | Unresolved critical contradiction exceeds SLA | Cap `R13M-15` at `50`; publication blocked pending closure | Cycle `INVALID` |
| R13M-TW-07 | Unapproved mid-cycle SLA/entitlement metric definition change detected | Set `R13M-04` to `0`; restatement and rescoring required | Cycle `INVALID` |
| R13M-TW-08 | Unexplained 90+ density increase >15 percentage points cycle-over-cycle | Cap `R13M-17` at `50`; full high-anchor resample required | Cycle `INVALID` |

### Hard-fail conditions (immediate invalidation)
| ID | Hard-fail condition | Evidence test | Effect |
| --- | --- | --- | --- |
| R13M-HF-01 | Evidence fabrication, tampering, or backdated approvals in rubric-evaluation package (`G1` class) | Forensic hash/signature/timestamp audit | Immediate cycle `INVALID`; full forensic review |
| R13M-HF-02 | Published score contradicts active blocking gate/tripwire state | Gate-state and published-outcome reconciliation | Immediate cycle `INVALID`; publication revoked |
| R13M-HF-03 | Unresolved critical contradiction remains at publication cutoff (`G2`/`RG3` class) | Contradiction register aging audit | Immediate cycle `INVALID` |
| R13M-HF-04 | Independent replay cannot reproduce critical support-row gate outcomes (`G5` class) | Non-author replay with gate-state mismatch | Immediate cycle `INVALID`; full rescoring required |
| R13M-HF-05 | Publication occurs without required authority-chain approvals (`G6` class) | Approval identity and timestamp audit | Immediate cycle `INVALID` |
| R13M-HF-06 | Rubric logic allows pass with active operational blocker (for example unresolved customer-impacting critical communication failure) | Scenario replay of blocker conditions versus scoring outcomes | Immediate cycle `INVALID` |
| R13M-HF-07 | Non-zero sampled rows missing required `who/what/where` evidence exceed 10% defect rate | Evidence admissibility sampling audit | Immediate cycle `INVALID` |
| R13M-HF-08 | Reviewer independence breach confirmed for high-anchor rows | Role-separation audit on author/scorer/reviewer | Immediate cycle `INVALID`; affected rows void |
| R13M-HF-09 | Unauthorized scoring-affecting rubric change during frozen scoring window | Version hash and diff audit | Immediate cycle `INVALID`; revert and rerun on approved baseline |
| R13M-HF-10 | Manual score override without authorized rationale and signatures | Score ledger diff vs published package | Immediate cycle `INVALID` for affected scope; systemic pattern invalidates full cycle |

## 7) Cross-role dependencies and adjudication handoffs

| Counterpart role | Required inbound dependency for R13 meta-evaluation | R13 outbound handoff | Acceptance criteria | SLA / escalation |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor / Business Owner | Risk appetite and publication invalidation authority | R13 meta-readiness recommendation with residual-risk statement | Decision signed with explicit treatment of open critical risks | Escalate within 1 business day for unresolved critical blocker |
| R1 Product Manager | Product decision priorities for recurring support pain and customer-impact themes | Feedback-loop and decision-trace quality findings | No unresolved ambiguity on support-theme to product-decision linkage | Escalate within 2 business days |
| R2 Product/Enterprise Architect | Contradiction precedence and ownership boundaries for support versus architecture rules | Contradiction disposition package and required rubric text fixes | Critical ownership conflicts resolved with deterministic rule language | Escalate within 2 business days |
| R3 Engineering Manager | Operational cadence and staffing constraints for scoring execution | Operability-fit and cycle-latency findings | Cycle execution plan accepted with owner/due dates for defects | Weekly during active cycle |
| R4 Software Engineer | Engineering acceptance criteria for support handoff reproducibility | Handoff-quality scoring findings and remediation requirements | First-pass acceptance defects triaged with dated closure plan | Weekly or per release gate |
| R5 QA/Test Engineer | Replay protocol, sampling method, and anchor calibration support | Testability and replay variance findings | Agreement on replay tolerance and closure of critical testability defects | Same cycle escalation on replay failure |
| R6 SRE/Platform Engineer | Incident and escalation governance constraints for operational gates | Severity/escalation determinism and runbook-criteria findings | No unresolved critical support-SRE gate contradiction | Immediate escalation on blocker conflict |
| R8 Privacy/Compliance/Legal | Legal/privacy contradiction interpretation for support communications and entitlement evidence | Contradiction and admissibility findings affecting legal/privacy scope | Critical legal contradiction count at cutoff = 0 | Escalate within 1 business day |
| R11 Technical Writer / DocOps | Canonical communication and KB governance constraints in rubric wording | Communication/status and evidence wording corrections | Source-of-truth and wording conflicts closed with approved updates | 3 business days |
| R12 DevOps / Release Manager | Gate execution logs and publication workflow controls | Gate-coherence findings and publication recommendation | No bypass path for active blocking gates | Immediate escalation on bypass risk |
| R14 FinOps / Procurement / Vendor Management | Entitlement/SLA contract interpretation and override policy details | Metric-definition and entitlement-governance findings | Contract-tier scoring logic accepted and testable | 2 business days |
| R15 Internal Audit / Assurance | Independent replay, provenance testing, and integrity assurance | Assurance-ready adjudication package and closure obligations | Auditor can replay sampled results without author assistance | Immediate escalation on integrity breach |

Adjudication handoff rules:
1. Every handoff must be explicitly `accepted` or `returned`; silent acceptance is invalid.
2. Every returned handoff must include defect class, owner, due date, and resubmission timestamp.
3. Required defect classes: `coverage`, `evidence`, `contradiction`, `inflation`, `replay`, `operability`.
4. Two consecutive returns for the same defect class escalate to `R0 + R15` within 1 business day.

## 8) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle phase | Checklist item | Evidence artifact | Pass criterion | Delta re-evaluation rule |
| --- | --- | --- | --- | --- |
| Pre-cycle baseline | Freeze Rubric_0 version hash, anchor model, gate logic, and scoring denominator population. | Baseline lock manifest and signed approvals. | Zero uncontrolled baseline drift in cycle. | Any unauthorized drift forces cycle restart on approved baseline. |
| Pre-cycle baseline | Refresh R13 concern-to-clause trace and close critical mapping gaps before scoring starts. | Updated coverage matrix and gap closure log. | Critical coverage gap count = 0. | New critical gap blocks scoring kickoff. |
| Pre-cycle baseline | Reconfirm contradiction taxonomy, owners, SLAs, and score-impact rules for support-critical conflicts. | Contradiction protocol conformance report. | All required contradiction fields present and enforceable. | Missing critical rule blocks publication readiness. |
| Calibration prep | Run ambiguity/monotonicity lint on support-relevant rubric rows and anchors. | Lint report with defect closure evidence. | No unresolved high-severity wording defect. | Unresolved defect caps impacted rows at `50`. |
| Calibration prep | Conduct dual-rater calibration on representative support-row packet. | Calibration variance report and adjudication notes. | Anchor drift <=1 level and gate-state agreement = 100%. | Failed calibration triggers immediate recalibration before scoring. |
| Scoring execution | Score non-zero rows only with admissible `who/what/where` evidence and cutoff compliance. | Row-level scorebook and admissibility sample log. | Admissibility completeness >=98% in sample. | Defective rows must be rescored before close. |
| Replay assurance | Execute independent replay/recompute on >=20% sample including all gate-sensitive support rows. | Replay transcripts, recompute worksheet, variance register. | Replay and recompute tolerance met with gate-state parity. | Variance breach triggers `R13M-TW-02` and targeted rescore. |
| Anti-gaming control | Execute full anti-gaming suite in Section 5 and log outcomes. | Anti-gaming execution checklist and findings log. | Mandatory control execution rate = 100%. | Any skipped mandatory control triggers `R13M-TW-01`. |
| Pre-close | Audit all `90+` rows for independent validation and same-cycle challenge proof. | High-anchor audit packet and approval trail. | Missing proof count = 0. | Missing proof triggers row downgrade and resample. |
| Pre-close | Reconcile contradiction register with adjudication minutes and close all critical items. | Signed contradiction closure bundle. | Open critical contradictions at cutoff = 0. | Any open critical contradiction triggers `R13M-HF-03`. |
| Pre-close | Recompute final publication decision from gate/tripwire states and compare with draft score package. | Gate-state recomputation worksheet and parity report. | Computed and draft outcomes match exactly. | Mismatch invalidates publication package. |
| Delta implementation | For each scoring-affecting Rubric_0 change, produce impacted-row map and comparability note. | Approved delta dossier with row-level mapping. | 100% scoring-affecting deltas mapped before promotion. | Unmapped delta blocks promotion. |
| Delta re-evaluation | Re-score impacted rows and rerun replay, contradiction, and inflation checks on changed scope. | Delta rescore report and focused control retest results. | No unexplained impacted-row delta >1 anchor step. | Unexplained delta requires rollback or redesign. |
| Publication | Publish final meta-score package with tripwire/hard-fail status and immutable evidence index. | Final scorecard, invalidation report, evidence manifest. | Non-author reviewer can replay package end-to-end. | Missing reproducibility proof blocks publication. |
| Post-cycle learning | Classify defects (false pass, false fail, ambiguity, replay drift, inflation risk, latency) and assign owners. | Defect taxonomy and remediation tracker. | 100% critical defects have owner and due date. | Unowned critical defect blocks next-cycle readiness. |
| Next-cycle readiness | Verify closure evidence for prior critical defects and retest affected rubric rows. | Closure validation log and targeted retest report. | >=90% on-time closure and zero open critical carryover defects. | Open critical carryover defect keeps Rubric_0 in `hold` state. |


---

## R14 FinOps / Procurement / Vendor Management

- source_file: `swarm_outputs/meta_rubric_role_expansions/R14_finops_procurement_vendor_management_rubric1.md`
- words: 5089
- lines: 166

# R14 FinOps / Procurement / Vendor Management Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 evaluates the quality, rigor, anti-gaming strength, contradiction safety, replayability, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 2) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R14 evaluates whether Rubric_0 can govern spend, procurement, contracts, vendor risk, and commercial decisions under pressure without becoming narrative theater. The role is accountable for testing that Rubric_0 is measurable, contradiction-safe, evidence-replayable, inflation-resistant, and strong enough to block unsafe or uneconomic pass decisions.

### Decision rights (R14 meta-evaluator)
| Decision domain | R14 authority on Rubric_0 quality | Non-delegable boundary | Escalation boundary |
| --- | --- | --- | --- |
| FinOps/procurement coverage readiness | Approve, conditionally approve, or return Rubric_0 for cycle use from cost/procurement/vendor perspective | Cannot approve with any unmapped critical commercial control class | Escalate to R0 and R15 within 1 business day |
| Spend and unit-economics anchor quality | Accept/reject Rubric_0 anchor wording for measurability and denominator integrity | Cannot accept subjective anchors at `75+` | Escalate to R1 and R5 same cycle |
| Evidence admissibility for non-zero scores | Approve/reject admissibility schema used in commercial-control rows | No non-zero row without `who/what/where/time/version/provenance` | Escalate to R15 on integrity defects |
| Contradiction protocol sufficiency | Joint authority on cost-vs-risk/service/compliance precedence rules | Cannot publish with unresolved Severity-1 contradiction at cutoff | Escalate to R2, R7, R8, and R12 immediately |
| High-score authorization quality | Challenge/cap unjustified `90/100` assignments on R14-relevant rows | No `>75` without independent corroboration; no `>90` without adversarial challenge evidence | Escalate to R15 for inflation investigation |
| Gate and veto enforceability | Validate that hard gates and role tripwires cannot be bypassed by averaging or overrides | Cannot approve if any hard-fail path is bypassable | Escalate to R0 governance forum immediately |
| Rubric delta governance | Approve/reject Rubric_0 deltas impacting commercial controls | No retroactive score change without versioned reopen and re-score trail | Escalate to R11 and R15 on change-control breach |

### Meta-scoring admissibility rules
- Anchor scale: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires admissible evidence captured before cycle cutoff.
- Any hard-fail in Section 6 marks Rubric_0 cycle scoring `INVALID`.

## 3) Sub-dimensions table with evaluation tests and evidence requirements

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R14M-01 FinOps/Procurement Decision-Coverage Completeness | Rubric_0 covers all critical commercial decision classes from spend attribution through vendor exit. | Build decision catalog from `R14_finops_procurement_vendor_management.md` and map to Rubric_0 clauses. Pass if total mapping >=95% and critical control mapping =100%. | Who: R14 lead + R1 + R8 reviewers. What: decision-to-clause trace matrix and gap log. Where: meta-review workbook and governance evidence folder. |
| R14M-02 Spend Taxonomy and Attribution Rule Testability | Rubric_0 spend-attribution rows are measurable and auditable, not narrative-only. | Sample attribution-related rows; each must specify required fields, reconciliation tolerance, owner, and evidence source. Undefined field rate in sample must be <=2%. | Who: R14 FinOps reviewer + finance controller. What: clause testability audit and reconciliation criteria checklist. Where: Rubric_0 clause matrix and finance control records. |
| R14M-03 Unit-Economics and Denominator Integrity Rule Strength | Rubric_0 enforces stable formulas and denominator controls for unit-cost scoring. | Verify rows require formula definition, denominator source lock, change control, and variance-RCA trigger. Any high-anchor path without denominator lock fails. | Who: R14 analyst + R1 finance partner. What: unit-economics rule audit and denominator lineage map. Where: scoring packet and metric dictionary evidence set. |
| R14M-04 Forecast/Variance Governance Evaluability | Rubric_0 can evaluate forecast quality and corrective-action discipline deterministically. | Check that rows require forecast error metric, cadence, variance threshold, and response SLA. Run replay on two historical forecast-miss scenarios and verify deterministic anchor outcomes. | Who: R14 evaluator + finance planning owner. What: forecast-rule conformance audit and scenario replay sheet. Where: rubric test harness and planning artifacts. |
| R14M-05 Budget Guardrail and Exception Precedence Enforceability | Rubric_0 defines non-bypassable budget thresholds, exception authority, and expiry logic. | Validate budget rows include threshold classes, pre-approval requirement, exception expiry, and consequence for unauthorized overrun. Simulate overrun-without-approval and confirm fail/cap behavior. | Who: R14 owner + R0 delegate + R15 observer. What: guardrail rule review and overrun simulation log. Where: adjudication workspace and gate precedence map. |
| R14M-06 Purchase Intake and Approval-Chain Integrity Evaluability | Rubric_0 evaluates whether procurement workflow integrity can be audited and enforced. | Verify rows require workflow path evidence, approver authority validation, off-workflow exception handling, and SLA aging. Missing approval-chain requirements in critical rows must be 0. | Who: procurement operations lead + R14 evaluator. What: approval-chain criteria audit and sampled workflow checks. Where: procurement governance register and rubric scorebook. |
| R14M-07 Vendor Due-Diligence and Onboarding Gate Coherence | Rubric_0 aligns vendor onboarding scoring with security, privacy, legal, and financial-risk gates. | Cross-check rows against R7/R8 due-diligence minimums. Pass if critical-vendor rows enforce complete package and block non-compliant onboarding outcomes. | Who: R14 + R7 + R8 reviewers. What: due-diligence control crosswalk and gate coherence report. Where: vendor-risk governance records and rubric mapping workbook. |
| R14M-08 Contract Obligation Traceability and Notice-Window Control Quality | Rubric_0 can evaluate clause-to-control mapping and contractual notice discipline. | Verify rows require clause owner, notice dates, acknowledgement evidence, and missed-notice consequences. Simulate missed notice and confirm deterministic penalty path. | Who: contract manager + R14 evaluator. What: obligation-traceability audit and notice-window replay results. Where: CLM evidence pack and rubric adjudication log. |
| R14M-09 Invoice/PO/Receipt Matching and Payment-Control Determinism | Rubric_0 requires objective payment-control evidence and consequence logic for mismatches. | Confirm invoice-control rows require 3-way match metrics, duplicate detection controls, dispute SLA, and emergency waiver audit trail. Missing any field in sampled critical rows must be <=2%. | Who: AP lead + R14 reviewer + internal control analyst. What: payment-control rule audit and mismatch scenario tests. Where: finance controls repository and scoring packet. |
| R14M-10 Savings-Claim Validity and Baseline-Lock Rigor | Rubric_0 prevents inflated savings claims through baseline tampering or offset exclusion. | Verify rows require locked baseline, offset accounting, one-time vs recurring separation, and realized-spend reconciliation. Challenge with manipulated baseline scenario and ensure score cap/fail triggers. | Who: R14 program owner + finance assurance reviewer. What: savings-control conformance audit and challenge test output. Where: optimization governance folder and rubric simulation artifacts. |
| R14M-11 Commitment/License Utilization and Waste-Remediation Evaluability | Rubric_0 can evaluate commitment, reservation, and license utilization controls with enforceable remediation logic. | Check that rows require utilization denominator definition, idle-asset inclusion, remediation SLA, and reassessment cadence. Critical row omission tolerance = 0. | Who: cloud economics owner + license manager + R14 evaluator. What: utilization-rule audit and denominator integrity sheet. Where: FinOps policy evidence and rubric row map. |
| R14M-12 Cost Anomaly Detection and Response-SLA Determinism | Rubric_0 can score anomaly detection, triage ownership, and closure quality using objective criteria. | Verify rows include detection latency threshold, owner assignment SLA, RCA requirements, and recurrence checks. Replay anomaly case and confirm inter-rater agreement within one anchor level. | Who: R14 on-call reviewer + R6 counterpart. What: anomaly-rule conformance audit and replay transcript. Where: alerting governance records and calibration workbook. |
| R14M-13 Pricing/Benchmark/Negotiation Governance Quality | Rubric_0 includes enforceable criteria for benchmark-informed negotiation and term-quality decisions. | Confirm renewal/pricing rows require benchmark recency, alternatives analysis, concession log, and approval authority evidence. No high-anchor path if benchmark evidence missing. | Who: sourcing lead + R14 evaluator + R0 observer. What: negotiation-rule audit and benchmark evidence review. Where: sourcing governance repository and rubric score packet. |
| R14M-14 Renewal Readiness and BATNA Governance Evaluability | Rubric_0 can evaluate early renewal preparation and leverage posture, not just signature completion. | Validate rows require workback start threshold, BATNA documentation, scenario evaluation, and late-renew consequence. Replay late-start renewal scenario and verify deterministic penalty outcome. | Who: category manager + R14 reviewer. What: renewal-rule conformance test and scenario replay log. Where: renewal calendar records and adjudication workbook. |
| R14M-15 Vendor SLA-Credit Enforcement and Corrective-Action Evaluability | Rubric_0 enforces vendor-performance evidence, credit-claim discipline, and repeat-breach correction logic. | Check rows require SLA measurement source, claim eligibility test, claim submission timeline, and corrective-action closure criteria. Simulate unclaimed credit scenario and confirm non-bypassable downgrade. | Who: vendor manager + service owner + R14 evaluator. What: SLA-credit criteria audit and enforcement simulation results. Where: vendor-governance board records and rubric test artifacts. |
| R14M-16 Concentration/Lock-in/Exit-Readiness Rule Enforceability | Rubric_0 evaluates concentration risk, lock-in exposure, and tested exit readiness as enforceable controls. | Verify rows require parent-entity consolidation, concentration thresholds, mitigation owner, exit simulation evidence, and fail logic for unmitigated critical single-source exposure. | Who: procurement risk lead + R2 architect + R14 evaluator. What: lock-in/exit rule audit and concentration scenario replay. Where: risk register and rubric control matrix. |
| R14M-17 Contradiction Handling Determinism for Cost vs Risk/Service Tradeoffs | Rubric_0 includes deterministic precedence and SLA for conflicts like cost reduction vs reliability/security/privacy obligations. | Run contradiction scenarios and confirm owner assignment, precedence order, closure SLA, and score impact are deterministic. Severity-1 contradiction aging past SLA must be 0 at cutoff. | Who: R14 adjudicator + R2 + R7 + R8 + R12. What: contradiction scenario log and SLA-aging audit. Where: contradiction register and governance minutes. |
| R14M-18 Evidence Admissibility and Replay/Recomputation Fidelity | Rubric_0 evidence schema supports independent replay and metric recomputation without scorer interpretation. | Replay >=15% sampled R14-relevant rows including gate-sensitive rows. Pass if score variance <=5 points and gate-state agreement =100%. | Who: independent non-author scorer + R15 witness + R14 observer. What: replay workbook, recomputation sheets, variance report. Where: immutable evidence vault and replay runbook directory. |
| R14M-19 Score Inflation Resistance, High-Anchor Guardrails, and Operational Cadence Fit | Rubric_0 structurally resists inflated commercial-control scoring and remains executable in cycle time. | Validate rules: `>75` requires independent corroboration, `>90` requires adversarial challenge evidence, unexplained jump >15 points triggers review, and cycle close meets SLA (<=5 business days after cutoff). | Who: R14 scoring owner + R15 validator + R3 workflow owner. What: high-score audit, jump-analysis report, cycle timing report. Where: score history dashboard, approval ledger, cycle close records. |

## 4) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R14M-01 FinOps/Procurement Decision-Coverage Completeness | Critical commercial decision classes are missing from Rubric_0. | Partial mapping exists; multiple critical classes unmapped. | Most classes mapped, but at least one critical class lacks enforceable criteria. | >=95% decision classes mapped and all critical classes mapped. | Independent review confirms critical mapping and closure of sampled gaps. | Two consecutive cycles with zero critical mapping gaps. |
| R14M-02 Spend Taxonomy and Attribution Rule Testability | Attribution rows are narrative-only and non-testable. | Some measurable fields exist, but owner/tolerance/source fields are often missing. | Most fields exist; material ambiguity persists in sampled rows. | Rows are measurable with explicit fields, tolerances, owners, and evidence sources. | Independent sample shows consistent scoring and low ambiguity defect rate. | Two cycles with zero critical attribution-rule ambiguity findings. |
| R14M-03 Unit-Economics and Denominator Integrity Rule Strength | Rubric_0 allows unit-cost claims without formula or denominator controls. | Formula language exists but denominator source and change control are undefined. | Core controls exist; high-anchor conditions remain partially subjective. | Formula, denominator lock, and variance-RCA requirements are explicit and enforceable. | Independent recomputation confirms deterministic outcomes in sampled rows. | Two cycles with no critical unit-economics scoring dispute or denominator drift defect. |
| R14M-04 Forecast/Variance Governance Evaluability | Forecast governance is absent from evaluable criteria. | Forecast checks exist without cadence, threshold, or action SLA. | Criteria partially defined; scenario replay yields inconsistent scorer outcomes. | Forecast quality, thresholds, and response SLAs are explicit and replayable. | Independent replay confirms deterministic penalties/rewards on miss scenarios. | Two cycles with no critical forecast-rule interpretation defect. |
| R14M-05 Budget Guardrail and Exception Precedence Enforceability | Budget overruns can pass without enforceable consequence. | Guardrails are listed but exception authority/expiry rules are vague. | Core thresholds defined; overrun scenarios still permit scorer discretion. | Threshold, authority, expiry, and unauthorized-overrun consequence are deterministic. | Adversarial simulation finds no practical bypass in sampled cases. | Two cycles with zero guardrail-bypass finding in assurance tests. |
| R14M-06 Purchase Intake and Approval-Chain Integrity Evaluability | Procurement workflow integrity cannot be evaluated. | Workflow mentioned, but approver authority and off-workflow handling are non-operational. | Criteria exist with partial authority validation and SLA control. | Approval-chain integrity criteria are explicit, auditable, and enforceable. | Independent sample confirms low ambiguity and consistent outcomes. | Two cycles with zero critical off-workflow approval-control omission. |
| R14M-07 Vendor Due-Diligence and Onboarding Gate Coherence | Vendor onboarding rows do not enforce due-diligence gates. | Gates are referenced but allow critical onboarding without required package. | Most gate checks present; cross-role coherence gaps remain. | Critical-vendor onboarding requires full due-diligence package and blocking logic. | Joint R7/R8/R14 replay confirms deterministic block behavior for violations. | Two cycles with zero critical onboarding scored above threshold without required gates. |
| R14M-08 Contract Obligation Traceability and Notice-Window Control Quality | Contract obligations and notice windows are not evaluable. | Obligations listed without owner/date/consequence fields. | Traceability exists but notice-window enforcement is inconsistent. | Clause-to-owner/date/consequence requirements are explicit and auditable. | Independent missed-notice scenario replay yields consistent penalty outcomes. | Two cycles with no critical notice-window scoring escape. |
| R14M-09 Invoice/PO/Receipt Matching and Payment-Control Determinism | Payment controls are absent or non-binding in rubric scoring. | Controls exist but omit key fields (3-way match, duplicate control, dispute SLA). | Most fields present; emergency-waiver logic and consequences remain weak. | Payment-control criteria are complete with deterministic mismatch consequences. | Independent control replay confirms reproducible scoring outcomes. | Two cycles with zero critical payment-control ambiguity defect. |
| R14M-10 Savings-Claim Validity and Baseline-Lock Rigor | Rubric permits narrative savings claims without baseline discipline. | Baseline mentioned but lock, offsets, or realization checks are missing. | Core checks exist; manipulated-baseline challenge still yields inconsistent outcomes. | Baseline lock, offset accounting, and realization reconciliation are enforceable. | Adversarial baseline-manipulation tests are consistently detected and penalized. | Two cycles with zero high-anchor savings score lacking full control evidence. |
| R14M-11 Commitment/License Utilization and Waste-Remediation Evaluability | Commitment/license utilization controls are not evaluable. | Utilization referenced without denominator integrity or remediation deadlines. | Controls exist but idle-asset treatment and SLA enforcement are inconsistent. | Utilization denominator, idle inclusion, and remediation SLA are explicit. | Independent sample confirms deterministic handling of underutilization scenarios. | Two cycles with no critical underutilization-rule omission in sampled scoring. |
| R14M-12 Cost Anomaly Detection and Response-SLA Determinism | Rubric cannot evaluate anomaly detection and response quality. | Criteria are vague; detection latency and ownership rules are missing. | Core fields defined; scorer disagreement remains high on closure quality. | Detection, assignment, RCA, and recurrence criteria are deterministic. | Calibration replay shows high inter-rater consistency for critical anomaly cases. | Two cycles with zero unresolved critical anomaly-scoring dispute at cutoff. |
| R14M-13 Pricing/Benchmark/Negotiation Governance Quality | Pricing/negotiation quality is not governed by enforceable rubric criteria. | Benchmark or alternatives checks are optional and non-auditable. | Most criteria present; high-anchor outcomes can still occur without benchmark proof. | Benchmark recency, alternatives, concession logs, and approval evidence are mandatory. | Independent challenge confirms unsupported negotiation claims are downgraded. | Two cycles with zero `>75` pricing-governance score lacking benchmark evidence. |
| R14M-14 Renewal Readiness and BATNA Governance Evaluability | Renewal readiness is scored without lead-time or BATNA requirements. | Workback/BATNA language exists but is non-binding. | Rules partially defined; late-renew consequences vary across scorers. | Workback thresholds, BATNA proof, and late-renew penalties are deterministic. | Independent late-start scenario replay matches expected scoring path. | Two cycles with no critical renewal-readiness interpretation conflict. |
| R14M-15 Vendor SLA-Credit Enforcement and Corrective-Action Evaluability | SLA-credit enforcement is absent or non-operational in scoring. | SLA checks exist but claim eligibility/timeline requirements are missing. | Core checks present; repeat-breach corrective-action closure criteria are weak. | Measurement, claim submission, and corrective-action closure requirements are enforceable. | Independent replay shows unclaimed-credit scenario reliably downgrades scores. | Two cycles with zero critical SLA-credit enforcement omission. |
| R14M-16 Concentration/Lock-in/Exit-Readiness Rule Enforceability | Lock-in and exit-readiness controls are missing or non-binding. | Concentration checks exist without parent-entity consolidation or tested exit proof. | Core controls exist; fail consequences for unmitigated critical single-source risk are inconsistent. | Consolidation, thresholds, mitigation ownership, and exit-test evidence are enforceable. | Independent scenario testing confirms deterministic fail/cap behavior. | Two cycles with zero critical single-source exposure scored above allowed threshold without mitigation proof. |
| R14M-17 Contradiction Handling Determinism for Cost vs Risk/Service Tradeoffs | Cost/risk/service contradictions are unresolved or handled ad hoc. | Contradictions logged but no precedence order, owner, or SLA discipline. | Protocol exists; outcomes still vary in critical scenarios. | Precedence/SLA/owner/score-impact protocol is explicit and consistently enforced. | Independent replay confirms deterministic outcomes across reviewers. | Two cycles with no Severity-1 contradiction unresolved at cutoff. |
| R14M-18 Evidence Admissibility and Replay/Recomputation Fidelity | Scores cannot be replayed or recomputed independently. | Replay works only with scorer interpretation; variance frequently exceeds tolerance. | Partial replay succeeds; gate-state mismatches or unexplained variance remain. | Sample replay/recompute meets tolerance and gate-agreement requirements. | Independent non-author replay is stable with near-zero unexplained variance. | Two cycles with no material replay/recompute discrepancy in sampled rows. |
| R14M-19 Score Inflation Resistance, High-Anchor Guardrails, and Operational Cadence Fit | Unsupported high-anchor scores are common and cycle execution is unstable. | Guardrails exist on paper but are inconsistently enforced; cycle close often misses SLA. | Guardrails and cadence controls operate partially; inflation signals remain unresolved. | High-anchor guardrails are enforced and cycle close generally meets SLA. | Distribution/jump analytics detect and correct inflation attempts quickly; cadence stable under load. | Two cycles with zero unsupported `>75`/`>90` rows and zero rubric-induced decision delay. |

## 5) Role-specific anti-gaming checks for rubric-evaluation gaming risks

1. Freeze Rubric_0 version hash, anchor text, weights, and gate logic at cycle start; reject scores from non-frozen variants.
2. Freeze denominator populations used in spend, utilization, and savings-related rows; approved changes require dual reporting (`before` and `after`).
3. Freeze baseline snapshots for savings and unit-economics rows; baseline changes after first result require formal reopen approval.
4. Require independent corroboration for every row scored `>75` and adversarial challenge evidence for every row scored `>90`.
5. Run non-author replay on at least 15% sampled rows, including all gate-sensitive commercial-control rows.
6. Recompute sampled metrics from raw sources; screenshot-only evidence is inadmissible above anchor `50`.
7. Enforce chronology integrity (`capture -> score -> approve -> publish`); out-of-order evidence invalidates affected rows.
8. Detect reclassification gaming by diffing cost-center/account mappings versus prior cycle; undocumented shifts are auto-returned.
9. Detect savings inflation by re-running calculations with locked baseline and explicit offset inclusion.
10. Detect deferred-cost masking by reconciling service-period accrual timing against reported period outcomes.
11. Detect vendor-fragmentation gaming by consolidating reseller entities to beneficial parent in concentration analysis.
12. Detect hidden renewals by reconciling contract registry with PO/invoice activity for unregistered term extensions.
13. Detect SLA-credit suppression by recomputing breach eligibility from raw service measurements.
14. Validate signer authority and role separation for high-anchor approvals; same actor cannot author evidence, score, and validate the same high-anchor row.
15. Run high-score density and jump analysis each cycle; unexplained `90+` spike >20% triggers full re-sample and re-score.

## 6) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (caps, holds, and forced rework)
| ID | Trigger condition | Immediate effect | If unresolved by publication cutoff |
| --- | --- | --- | --- |
| R14M-TW-01 | Any mandatory anti-gaming check in Section 5 is skipped | Cap `R14M-19` at `25`; block any row from scoring above `90` | Cycle marked `INVALID` |
| R14M-TW-02 | Replay variance >5 points on >10% sampled rows | Cap `R14M-18` at `50`; require replay root-cause analysis | Cycle marked `INVALID` |
| R14M-TW-03 | Any score `>75` lacks independent corroboration evidence | Cap affected row at `50`; re-score required | Cycle marked `INVALID` |
| R14M-TW-04 | Any score `>90` lacks adversarial challenge evidence | Cap affected row at `75`; inflation review required | Cycle marked `INVALID` |
| R14M-TW-05 | Any Severity-1 contradiction open past SLA | Cap `R14M-17` at `50`; publication hold | Cycle marked `INVALID` |
| R14M-TW-06 | Gate simulation reveals bypass path for hard-fail logic | Cap `R14M-05` and `R14M-19` at `25`; immediate logic correction required | Cycle marked `INVALID` |
| R14M-TW-07 | Unauthorized rubric edit after cycle freeze | Stop scoring; revert to approved version and reopen protocol | Cycle marked `INVALID` |
| R14M-TW-08 | Cycle close delayed by >2 business days due to rubric design defects | Cap `R14M-19` at `50`; mandatory remediation plan | Publication blocked until corrected or cycle `INVALID` |
| R14M-TW-09 | Sampled non-zero rows missing admissibility fields exceed 5% | Cap `R14M-18` at `50`; resample and re-score required | Cycle marked `INVALID` |

### Hard-fail conditions (Rubric_0 scoring invalid for the cycle)
| ID | Hard-fail condition | Evidence test | Effect |
| --- | --- | --- | --- |
| R14M-HF-01 | Evidence fabrication, tampering, or backdated approval in scoring package (`G1`) | Provenance hash/timestamp forensic mismatch | Cycle result `INVALID`; forensic review mandatory |
| R14M-HF-02 | Unresolved critical contradiction at cutoff (`G2`) | Contradiction register SLA-aging audit | Cycle result `INVALID` |
| R14M-HF-03 | Unresolved mandatory legal/privacy/security control breach affecting commercial decision rows (`G3`) | R7/R8 blocker status and control evidence audit | Cycle result `INVALID` |
| R14M-HF-04 | Critical operability failure can still receive pass due to cost-weight masking (`G4`) | Gate simulation and decision audit | Cycle result `INVALID` |
| R14M-HF-05 | Independent replay/recompute cannot reproduce material claims (`G5`) | Non-author replay failure on critical sample | Cycle result `INVALID`; full re-score required |
| R14M-HF-06 | Publication without required authority-chain approvals (`G6`) | Signature/authority/timestamp audit | Cycle result `INVALID` |
| R14M-HF-07 | Critical vendor due-diligence gate missing but row scored above `25` | Vendor onboarding gate replay | Cycle result `INVALID` |
| R14M-HF-08 | Missed contractual notice window is not scored with mandated penalty path | Notice-window scenario replay and score-path audit | Cycle result `INVALID` |
| R14M-HF-09 | Payment-control bypass above policy threshold can still pass without emergency waiver path | Invoice-control scenario replay | Cycle result `INVALID` |
| R14M-HF-10 | Unmitigated critical single-source/lock-in exposure can score above allowed threshold | Concentration/exit scenario replay | Cycle result `INVALID` |
| R14M-HF-11 | Sampled non-zero rows missing required `who/what/where` exceed 10% | Admissibility sampling audit | Cycle result `INVALID`; full re-score required |
| R14M-HF-12 | Systemic score inflation: >20% of `90+` rows lack required corroboration/challenge evidence | High-anchor evidence audit | Cycle result `INVALID`; mandatory full re-sampling and re-score |

## 7) Cross-role dependencies and adjudication handoffs

| Counterpart role | Dependency into R14 meta-evaluation | R14 handoff output | Acceptance criteria | SLA / escalation |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor / Business Owner | Governance charter, risk appetite, and exception authority model | Rubric_0 commercial-control readiness decision (`approve/conditional/hold`) | Decision state and residual-risk record signed by authorized owners | Escalate governance deadlock within 1 business day |
| R1 Product Manager | KPI and value-model definitions that influence denominator and unit economics | Denominator integrity and unit-economics rubric findings | No unresolved ambiguity on metric ownership/formula boundaries | Escalate within 2 business days |
| R2 Product Architect / Enterprise Architect | Dependency topology and lock-in boundary definitions | Concentration/exit-control contradiction findings | Critical architecture-commercial contradiction count = 0 at cutoff | Escalate within 2 business days |
| R3 Engineering Manager | Delivery-cadence constraints and rubric execution capacity | Operational-cadence fitness findings for scoring process | Cycle workload supports close SLA without quality shortcuts | Escalate in-cycle on repeated SLA risk |
| R5 QA / Test Engineer | Replay protocol, sampling method, and calibration support | Replay variance findings and testability defects | Replay tolerance met; unresolved critical testability defects = 0 | Escalate same cycle |
| R6 SRE / Platform Engineer | Cost anomaly and reliability tradeoff constraints | Contradiction dispositions for cost-vs-reliability decisions | No pass path where cost optimization bypasses reliability hard gates | Immediate escalation for gate-bypass risk |
| R7 Security Engineer / Architect | Security due-diligence minimums for vendor gating | Security-linked gate coherence findings in Rubric_0 | No score path above threshold with active critical security blocker | Immediate escalation |
| R8 Privacy / Compliance / Legal | Legal/privacy due-diligence and contractual obligation expectations | Legal/privacy contradiction and control-coherence findings | No unresolved legal contradiction at publication | Escalate within 1 business day |
| R12 DevOps / Release Manager | Release workflow rules and approval-chain logs | Publication authorization recommendation for rubric score package | Gate-state consistency and approval-chain integrity validated | Same-day escalation on mismatch |
| R13 Operations / Support / Customer Success | SLA evidence patterns and service-credit claim operational data model | SLA-credit evaluability findings and missing-control defects | No unresolved critical ambiguity in SLA evidence admissibility | Escalate within 2 business days |
| R15 Internal Audit / Assurance | Independent assurance sampling and integrity testing | Final assurance-aligned memo with replay and inflation findings | Material assurance exceptions = 0 for publication | Immediate escalation on integrity breach |
| R11 Technical Writer / DocOps | Controlled wording changes and publication discipline | Approved wording deltas and impact notes for commercial-control rows | Versioned diff, approvers, and impact scope are complete | Escalate on unapproved wording drift |

Adjudication rules:
1. Every handoff must be explicitly `accepted` or `returned`; silent acceptance is invalid.
2. Every returned handoff must include defect class, owner, due date, and resubmission timestamp.
3. Any defect returned twice in one cycle escalates to `R0 + R15` adjudication.
4. Any unresolved critical handoff at cutoff blocks publication.

## 8) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle point | Checklist item | Evidence artifact | Pass criterion | Delta re-evaluation rule |
| --- | --- | --- | --- | --- |
| Pre-cycle baseline | Freeze Rubric_0 version hash, anchor set, weights, gates, and denominator definitions. | Baseline manifest with signed approvals. | Zero unauthorized change during scoring window. | Unauthorized change forces cycle restart on approved baseline. |
| Pre-cycle baseline | Refresh R14 decision-catalog-to-clause trace and unresolved gap register. | Updated trace matrix and gap log. | Critical decision-class mapping =100% before scoring starts. | New critical gap blocks scoring kickoff. |
| Pre-cycle baseline | Reconfirm contradiction precedence and SLA rules for cost/risk/service conflicts. | Contradiction protocol sheet and owner roster. | No missing precedence path for known conflict classes. | Protocol change requires targeted re-score of affected rows. |
| Pre-cycle baseline | Reconfirm admissibility schema (`who/what/where/time/version/provenance`) and cutoff policy. | Schema version record and cutoff notice. | Schema completeness approved by R14 and R15. | Mid-cycle schema change requires reopen approval and impacted-row re-score. |
| Calibration prep | Run anchor monotonicity and ambiguity lint for R14-relevant rows. | Anchor lint report and defect log. | No unresolved critical ambiguity before scoring. | Unresolved critical ambiguity caps impacted rows at `50`. |
| Calibration prep | Run dual-scorer calibration on shared critical packet. | Calibration comparison and dispute register. | Unexplained divergence >1 anchor level = 0 after adjudication. | Remaining divergence blocks publication. |
| Scoring execution | Score using admissible evidence only; reject narrative-only commercial claims. | Row-level scorebook and admissibility sample log. | Non-zero rows with complete admissibility >=98% in sample. | Defective rows must be rescored before publication. |
| Replay assurance | Execute independent replay/recompute on >=15% sampled rows including gate-sensitive rows. | Replay transcript, recomputation workbook, variance report. | Score variance <=5 points; gate-state agreement =100%. | Variance breach triggers `R14M-TW-02` and re-score. |
| Anti-gaming execution | Execute all mandatory anti-gaming checks and challenge scenarios in Section 5. | Anti-gaming checklist and challenge outputs. | Mandatory control execution rate =100%. | Any skipped mandatory control triggers `R14M-TW-01`. |
| Contradiction closure | Resolve all Severity-1 contradictions and apply score impacts before cutoff. | Closure records and rescoring notes. | Severity-1 unresolved count = 0 at cutoff. | Any unresolved item triggers `R14M-TW-05` and invalidation. |
| High-score review | Audit all `>75` and `>90` rows for required corroboration/challenge evidence. | High-score evidence package and audit summary. | Missing required evidence count = 0. | Violations trigger `R14M-TW-03/04` and affected-row cap. |
| Gate coherence validation | Re-run hard-gate precedence simulation on final score draft. | Gate simulation report and sign-off. | No bypass path for hard-fail conditions. | Any bypass triggers `R14M-TW-06` and invalidation if unresolved. |
| Publication gate | Apply all tripwire and hard-fail checks before publishing cycle results. | Final invalidation check sheet and sign-offs. | Active hard-fail count = 0. | Any active hard-fail marks cycle `INVALID`. |
| Post-cycle remediation | Convert failed checks into dated corrective actions with verification tests. | Remediation register with owner/due date/test. | 100% critical actions owned and time-bound. | Unowned critical action blocks next-cycle readiness sign-off. |
| Delta implementation | Apply approved Rubric_0 wording/rule changes with versioned diff and impact tags. | Change request, approved diff, impact matrix. | Unauthorized delta count = 0. | Unauthorized delta triggers `R14M-TW-07` and cycle reset. |
| Delta re-evaluation | Re-score impacted rows and rerun replay/gate/coherence tests for changed areas. | Delta re-score packet and focused replay report. | All impacted rows/gates retested with pass evidence. | Missing retest evidence blocks publication. |
| Cycle close | Publish retrospective with trend deltas, repeat defect classes, and carryover risks. | Cycle retrospective and carryover register. | Residual risks explicitly owned with review date. | Unowned carryover risk prevents cycle close. |


---

## R15 Internal Audit / Assurance

- source_file: `swarm_outputs/meta_rubric_role_expansions/R15_internal_audit_assurance_rubric1.md`
- words: 4908
- lines: 163

# R15 Internal Audit / Assurance Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

Scope guardrail: this Rubric_1 evaluates the quality, rigor, anti-gaming strength, contradiction safety, replayability, and operational usefulness of Rubric_0 itself. It does not score project artifact quality directly.

## 1) Title
R15 Internal Audit / Assurance Meta-Rubric Expansion (Rubric_1 scoring Rubric_0)

## 2) Role mission and decision rights for evaluating Rubric_0 quality

### Role mission
R15 evaluates whether Rubric_0 can withstand independent assurance, regulator scrutiny, and adversarial replay. The role is accountable for testing whether Rubric_0 is auditable, non-bypassable, evidence-disciplined, contradiction-safe, and resistant to score inflation under delivery pressure.

### Decision rights (R15 meta-evaluator)
| Decision domain | R15 authority on Rubric_0 quality | Non-delegable boundary | Escalation path |
| --- | --- | --- | --- |
| Assurance-readiness approval | Approve, conditionally approve, or reject Rubric_0 for cycle use from assurance perspective | Cannot approve if any hard-fail in Section 6 is active | Escalate to R0 and audit committee within 1 business day |
| Evidence admissibility standard | Set minimum admissibility fields and reject incomplete evidence for non-zero scoring | No non-zero score without admissible who/what/where evidence and provenance | Escalate to R12 and R11 on pipeline/evidence schema defects |
| Gate and precedence assurance | Validate `G1..G6` and `RG1..RG4` are non-bypassable in final decision logic | Cannot allow weighted averaging to override active hard gates | Escalate to R0 governance forum immediately |
| Replay/recompute assurance | Require independent replay and recomputation before publication | Cannot publish when replay variance or gate-state mismatch exceeds tolerance | Escalate to R15-led forensic review with R12 support |
| Contradiction adjudication sufficiency | Approve or return contradiction protocol quality and closure evidence | Cannot publish with unresolved Severity-1 contradiction at cutoff | Escalate to R2/R7/R8 with same-cycle adjudication |
| High-anchor authorization quality | Cap or void unsupported `>75` and `>90` assignments | No `>75` without independent validation; no `>90` without adversarial challenge evidence | Escalate to R0 and R15 QAIP owner |
| Delta governance and recertification | Approve or reject Rubric_0 deltas for next cycle | No delta promotion without impact map, targeted re-score, and gate replay | Escalate to R11 and R12 on change-control breach |
| Independence and COI integrity | Invalidate compromised scoring when assessor independence fails | No same-person evidence author + primary scorer + validator for same high-anchor row | Escalate to audit committee for unresolved independence impairment |

### Meta-scoring admissibility protocol
- Anchor set: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires explicit admissible `who/what/where` evidence.
- Any row scored above `50` requires replayable raw evidence.
- Any row scored above `75` requires independent reviewer confirmation.
- Any row scored above `90` requires same-cycle adversarial challenge evidence.
- Post-cutoff evidence is excluded unless formal reopen approval is recorded.

## 3) Sub-dimensions table with at least 16 sub-dimensions

| Sub-dimension | Definition | Evaluation tests (how to judge Rubric_0 quality) | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R15M-01 Assurance-scope coverage completeness | Rubric_0 covers all assurance-critical decision classes across A3/A4/A6 and role layer controls. | Build coverage map from `Rubric_0_Comprehensive_N6_Swarm.md` and `Rubric_0_Role_Expansion_Pack_N16.md`; pass if critical decision-class mapping = 100% and total mapping >= 95%. | Who: R15 lead evaluator + R0 governance analyst. What: decision-class-to-rubric trace matrix and gap log. Where: meta-evaluation workbook and governance evidence folder. |
| R15M-02 Hard-gate precedence and non-bypassability | Rubric_0 enforces hard gates before arithmetic scoring and prevents bypass by overrides or averaging. | Replay gate truth table for `G1..G6` and `RG1..RG4`; pass if simulated gate-triggered cases produce deterministic fail outcomes 100% of runs. | Who: R15 assurance engineer + R12 workflow owner. What: gate truth-table replay report and bypass test logs. Where: scoring engine workbook and release-governance records. |
| R15M-03 Contradiction-handling determinism and aging control | Rubric_0 contradiction protocol defines precedence, severity, owner, SLA, and score impact. | Run contradiction scenarios; pass if Severity-1 contradictions always block publication and unresolved Severity-1 count at cutoff = 0. | Who: R15 adjudicator + R2 + R7 + R8 counterparts. What: contradiction scenario packet, SLA-aging dashboard, closure records. Where: contradiction register and adjudication minutes. |
| R15M-04 Evidence admissibility schema rigor | Rubric_0 evidence requirements are explicit, auditable, and sufficient for non-zero scoring. | Sample non-zero rows; pass if required evidence fields (`who/what/where/time/version`) completeness >= 98% and inadmissible evidence is consistently rejected. | Who: R15 evidence reviewer + R11 doc owner. What: admissibility audit sheet and rejection log. Where: evidence catalog and scoring package archive. |
| R15M-05 Chain-of-custody and provenance enforceability | Rubric_0 requires immutable evidence lineage from source extraction to score publication. | Verify provenance requirements include source ID, extraction timestamp, and integrity check; pass if sampled broken lineage events = 0. | Who: R15 evaluator + evidence custodian. What: provenance manifest, hash/integrity logs, exception report. Where: evidence vault and audit log system. |
| R15M-06 Independent replayability and recomputation fidelity | Rubric_0 outcomes can be reproduced by non-authors without hidden context. | Independent replay of >= 15% sampled rows (including gate-sensitive rows); pass if score variance <= 5 points, anchor drift <= 1 step, and gate-state parity = 100%. | Who: independent non-author scorer + R15 witness. What: replay transcript, recomputation workbook, variance register. Where: immutable evidence store and replay runbook. |
| R15M-07 Sampling-method rigor for rubric evaluation | Rubric_0 requires valid population definition, sampling logic, exclusions, and reselection reproducibility. | Rebuild sample from source population; pass if population reconciliation variance <= 1%, undocumented exclusions = 0, and reselection reproducibility = 100%. | Who: R15 sampling reviewer + data owner. What: population extract, reconciliation workbook, sampling seed and exclusion approvals. Where: source systems and sampling evidence folder. |
| R15M-08 Anchor falsifiability and monotonic specificity | Rubric_0 anchors are measurable, non-ambiguous, and progressively stricter from 0 to 100. | Run anchor lint on sampled rows; pass if monotonicity violations = 0 and undefined subjective terms in high-stakes rows = 0. | Who: R15 rubric QA reviewer + R5 test reviewer. What: anchor lint report and ambiguity defect log. Where: rubric text repository and QA findings tracker. |
| R15M-09 Severity calibration consistency for rubric defects | Defect severities in Rubric_0 quality review follow consistent materiality rules. | Monthly blind recalibration on sampled defects; pass if drift > 1 severity band <= 10% and undocumented overrides = 0. | Who: R15 calibration panel lead. What: severity matrix, calibration minutes, override register. Where: assurance governance workspace. |
| R15M-10 Score inflation resistance and high-anchor guardrails | Rubric_0 structurally resists unjustified high scoring. | Validate enforced rules for `>75` and `>90`, denominator-freeze checks, and high-score distribution jumps; pass if unsupported `90+` rows = 0. | Who: R15 scoring integrity reviewer + R0 observer. What: high-anchor audit pack, denominator drift analysis, score-distribution trend. Where: score ledger and approval logs. |
| R15M-11 Independence and conflict-of-interest control quality | Rubric_0 evaluation process preserves assessor independence and prevents role-concentration bias. | Pass if COI declarations complete before scoring = 100%, unmitigated COI = 0, and scorer-author-validator overlap on sampled high rows = 0. | Who: R15 QAIP lead + HR/compliance partner. What: COI roster, recusal decisions, role-separation audit. Where: staffing records and evaluation workflow logs. |
| R15M-12 Decision-log chronology and audit-trail completeness | Rubric_0 scoring decisions are chronologically valid and fully traceable. | Chronology test (`evidence capture -> score -> approval -> publication`) on sample; pass if out-of-order events = 0 and critical decision logging coverage = 100%. | Who: R15 process auditor + R12 release governance lead. What: decision ledger, timestamp audit report, missing-log exceptions. Where: governance tracker and publication workflow logs. |
| R15M-13 Remediation action design quality for Rubric_0 defects | Rubric_0 defects are corrected via specific, owned, testable plans. | Pass if critical defects have SMART remediation plans with single accountable owner and verification test = 100%. | Who: remediation owner + R15 follow-up reviewer. What: remediation plan QA checklist and owner sign-offs. Where: corrective-action tracker. |
| R15M-14 Remediation verification and closure independence | Rubric_0 defects close only after independent verification confirms effectiveness. | Pass if closure without independent retest = 0, and reopened critical defects within 90 days <= 5%. | Who: independent follow-up reviewer (not original scorer). What: retest artifacts, closure decisions, reopen log. Where: follow-up evidence pack and issue register. |
| R15M-15 Recurrence detection and strengthened-control discipline | Repeat Rubric_0 quality failures are detected early and trigger stronger controls. | Pass if repeat-finding detection latency <= 5 business days, repeat critical findings escalated = 100%, and strengthened-control plan exists for each repeat critical issue. | Who: R15 analytics owner + governance chair. What: recurrence dashboard, escalation notices, strengthened-control plans. Where: BI recurrence model and governance minutes. |
| R15M-16 Assurance-report traceability and defensibility | Rubric_0 quality verdicts are statement-to-evidence traceable and challenge-ready. | Pass if statement-to-evidence traceability = 100%, unresolved material contradiction at publication = 0, and QA signoff completeness = 100%. | Who: report author + QA reviewer + R15 approver. What: final assurance memo, evidence index, contradiction closure register. Where: report repository and evidence manifest. |
| R15M-17 Cross-role handoff executability and adjudication SLA discipline | Rubric_0 supports enforceable handoffs with clear acceptance, return, and escalation states. | Sample critical handoffs (R0/R2/R7/R8/R12); pass if first-pass acceptance >= 90%, silent acceptance = 0, and returned handoffs include defect class/owner/due date = 100%. | Who: R15 handoff coordinator + counterpart role leads. What: handoff SLA report, return-reason log, escalation records. Where: adjudication tracker and release board records. |
| R15M-18 Version freeze, cutoff integrity, and delta re-evaluation discipline | Rubric_0 versioning prevents retroactive manipulation and enforces impact-based re-evaluation of deltas. | Pass if unauthorized post-freeze edits = 0 and impacted-row re-score + gate replay coverage = 100% for approved deltas. | Who: R11 doc owner + R12 release owner + R15 validator. What: version manifest, approved diff dossier, delta retest report. Where: version control history and cycle-close package. |

## 4) Anchor table that defines explicit behavioral anchors at 0/25/50/75/90/100 for every sub-dimension

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R15M-01 Assurance-scope coverage completeness | Critical assurance classes are missing from Rubric_0. | Partial mapping exists with major blind spots. | Most classes mapped but at least one critical gap remains. | Critical classes fully mapped and total coverage >=95%. | Independent review confirms mapping completeness and gap closure quality. | Two consecutive cycles with zero critical coverage gaps. |
| R15M-02 Hard-gate precedence and non-bypassability | Gate logic absent or routinely bypassed. | Gates exist but precedence conflicts permit pass outcomes. | Gates mostly work but edge-case bypass path remains. | Gate precedence is deterministic; no tested bypass path. | Independent adversarial replay confirms non-bypassable behavior. | Two cycles with zero gate-precedence defects in assurance sampling. |
| R15M-03 Contradiction-handling determinism and aging control | Contradictions are unmanaged and non-blocking. | Contradictions logged ad hoc without enforceable SLA. | Severity/owner/SLA model exists but closure behavior is inconsistent. | Deterministic contradiction handling with enforced SLA and score impact. | Independent replay confirms Severity-1 contradictions block publication every time. | Two cycles with no unresolved Severity-1 contradiction at cutoff. |
| R15M-04 Evidence admissibility schema rigor | Non-zero scoring is possible without admissible evidence. | Evidence requirements are partial and inconsistently applied. | Admissibility fields mostly defined; rejection behavior still inconsistent. | Admissibility schema is complete and consistently enforced. | Independent sample audit shows near-zero admissibility defects. | Two cycles with zero accepted non-zero rows missing mandatory fields. |
| R15M-05 Chain-of-custody and provenance enforceability | Evidence lineage is missing or mutable. | Some provenance exists but integrity checks are weak. | Lineage mostly present; occasional chain-of-custody gaps remain. | Immutable provenance requirements enforced for material evidence. | Independent forensic check confirms integrity on sampled evidence packages. | Two cycles with no material provenance exception. |
| R15M-06 Independent replayability and recomputation fidelity | Outcomes cannot be replayed by non-authors. | Replay works only with scorer interpretation and high variance. | Partial replay succeeds but exceeds tolerance on material rows. | Replay/recompute meet variance tolerance and gate-state parity. | Independent teams reproduce sampled outcomes with minimal variance. | Two cycles with stable replay and no material recomputation mismatch. |
| R15M-07 Sampling-method rigor for rubric evaluation | Sampling is ad hoc or non-reproducible. | Sample exists but population/exclusion logic is opaque. | Method documented but reconciliation or reselection defects remain. | Sampling is population-complete, justified, and reproducible. | Independent reselection matches issued sample and conclusions. | Two cycles with zero material sampling defect. |
| R15M-08 Anchor falsifiability and monotonic specificity | Anchor language is vague and non-testable. | Some anchors testable; monotonic progression frequently breaks. | Most anchors measurable but ambiguity exists in high-stakes rows. | Anchors are falsifiable, measurable, and monotonic. | Independent lint confirms no critical ambiguity in sampled rows. | Two cycles with zero high-severity anchor-lint defects. |
| R15M-09 Severity calibration consistency for rubric defects | Severity assignments are arbitrary or politicized. | Matrix exists but calibrations are sporadic and weakly documented. | Calibration routine exists; drift and undocumented overrides still significant. | Severity ratings are consistent with low drift and documented overrides. | Blind calibration confirms stable severity behavior across reviewers. | Two cycles with no unjustified severity downgrade. |
| R15M-10 Score inflation resistance and high-anchor guardrails | Unsupported high scores are common and unchecked. | Guardrails are documented but bypassable in practice. | Guardrails partially enforced; high-score anomalies unresolved. | High-anchor controls enforced with deterministic caps and rescore rules. | Independent inflation testing confirms manipulation attempts are detected and blocked. | Two cycles with zero unsupported `>75` or `>90` rows. |
| R15M-11 Independence and conflict-of-interest control quality | COI controls absent; independence compromised. | COI checks exist but late/incomplete; conflicts persist. | COI process exists; role-separation defects occur intermittently. | COI and role separation controls are complete and enforced. | Independent audit confirms no unmitigated COI in sampled high-stakes scoring. | Two cycles with zero independence breach on sampled high-anchor rows. |
| R15M-12 Decision-log chronology and audit-trail completeness | Scoring chronology is unverifiable or backfilled. | Logs exist but chronology breaks and missing records are frequent. | Core logs present; some ordering or completeness defects remain. | Chronology is valid and critical decision logging is complete. | Independent chronology replay confirms end-to-end traceability. | Two cycles with zero material chronology violation. |
| R15M-13 Remediation action design quality for Rubric_0 defects | Defects lack owners or credible fixes. | Plans exist but are vague, ownerless, or non-testable. | Most plans are actionable; some critical plans miss verification design. | All critical defects have SMART, owned, testable remediation plans. | Independent challenge confirms remediation plans are feasible and risk-reducing. | Two cycles with zero critical defect lacking acceptable remediation plan. |
| R15M-14 Remediation verification and closure independence | Defects are closed without independent verification. | Closure relies mostly on self-attestation with limited retesting. | Retesting occurs but independence and evidence quality vary. | Independent retest is mandatory and closure evidence is complete. | Reopen rate is low and closure decisions withstand assurance sampling. | Two cycles with zero improper closure in independent follow-up audits. |
| R15M-15 Recurrence detection and strengthened-control discipline | Repeat failures are not tracked or escalated. | Recurrence tracking is manual and escalation is inconsistent. | Recurrence analytics exist but strengthened-control responses are weak. | Repeat failures are quickly detected, escalated, and control-strengthened. | Trend evidence shows recurrence reduction in high-risk defect classes. | Two cycles with sustained decline of repeat critical defects. |
| R15M-16 Assurance-report traceability and defensibility | Final meta-evaluation cannot be defended from evidence. | Report has partial evidence links and unresolved contradictions. | Report mostly traceable but challenge responses are slow or incomplete. | Report is fully traceable, contradiction-closed, and QA approved. | Independent challenge reproduces key conclusions without author intervention. | Two cycles with no material restatement after assurance challenge. |
| R15M-17 Cross-role handoff executability and adjudication SLA discipline | Handoffs are ambiguous, silent, or routinely late. | Handoff forms exist but acceptance criteria and ownership are unclear. | Handoffs are mostly structured; repeated SLA misses persist. | Binary accept/return workflow is enforced and SLA performance is stable. | Independent sample shows high first-pass quality and low repeat returns. | Two cycles with no silent acceptance and sustained SLA adherence. |
| R15M-18 Version freeze, cutoff integrity, and delta re-evaluation discipline | Rubric version drift or retroactive edits alter cycle outcomes. | Freeze exists but post-cutoff edits leak into scoring. | Versioning mostly controlled; delta retesting is inconsistent. | Version freeze and cutoff controls enforced; delta impact retests complete. | Independent diff and retest audits confirm no unauthorized score-impacting edit. | Two cycles with full version integrity and complete delta re-evaluation coverage. |

## 5) Role-specific anti-gaming checks for rubric-evaluation gaming risks

| Gaming pattern to detect | Adversarial check | Required control response | Scoring consequence |
| --- | --- | --- | --- |
| Cherry-picked sampled rows that avoid hard cases | Rebuild sample from frozen full population using locked seed and compare defect rates. | Population snapshot hash and selection log must be immutable. | Material mismatch caps `R15M-07` at `25`; unresolved mismatch invalidates cycle. |
| Denominator drift to inflate pass rates | Compare cycle-start denominator vs reported denominator and require approved change ticket. | Dual reporting (`before`/`after`) and authority sign-off required for denominator changes. | Unapproved drift caps `R15M-10` at `25`; critical drift triggers hard-fail review. |
| Backfilled evidence after cutoff | Audit evidence creation/extraction timestamps against cycle cutoff. | Post-cutoff evidence excluded unless reopen approval exists. | Affected rows capped at `50`; repeated pattern triggers invalidation. |
| Replay performed by non-independent actors | Validate non-author status and access/activity logs for replay reviewers. | Independence attestation required for all replay reviewers. | Rows above `75` are voided for affected scopes. |
| Contradiction suppression | Reconcile contradiction register against meeting minutes and score packet notes. | Every contradiction must have owner, severity, and closure state. | Hidden Severity-1 contradiction sets `R15M-03` to `0` and publication hold. |
| Severity downgrade pressure | Blind recalibration of sampled downgraded findings. | Downgrades require panel record with evidence-based rationale. | Unjustified downgrade sets `R15M-09` to `0` for cycle. |
| High-anchor inflation without proof | Audit all `>75` and `>90` rows for mandatory corroboration/challenge evidence. | Enforced cap rules with automated block on missing proofs. | Unsupported `>75` or `>90` rows are downgraded and rescored; systemic failure invalidates cycle. |
| Post-signoff report softening edits | Diff signed report hash vs published report hash. | Immutable signoff package and controlled amendment process required. | Unauthorized edits set `R15M-16` to `0`. |
| Role concentration (same person authors, scores, validates) | Perform row-level role-separation audit on high-impact rows. | Enforce separation of duties for evidence author, scorer, and validator. | Breach caps affected rows at `50`; repeated breach triggers hard-fail. |
| Waiver laundering through rolling short renewals | Analyze exception renewals for repeated extensions of same unresolved defect. | Renewal requires new evidence and strengthened compensating control test. | Related controls capped at `25` until corrected. |
| Selective replay only on easy rows | Independently select replay sample including mandatory gate-sensitive rows. | Surprise sample quota is mandatory each cycle. | Missing mandatory replay coverage caps `R15M-06` at `50`. |
| Unauthorized rubric delta insertion mid-cycle | Compare active scoring rubric hash against approved baseline hash. | Cycle freeze with change-control gate and reopen protocol. | Cycle marked invalid if unapproved delta affects scored rows. |

## 6) Tripwires and hard-fail conditions that invalidate Rubric_0 scoring if triggered

### Tripwires (forced caps, holds, and rework)
| ID | Trigger condition | Immediate effect | If unresolved at publication cutoff |
| --- | --- | --- | --- |
| R15M-TW-01 | Any mandatory anti-gaming check in Section 5 not executed | Cap `R15M-10` at `25` and block `90+` scoring | Cycle status `INVALID` |
| R15M-TW-02 | Replay variance tolerance breached on >10% sampled rows | Cap `R15M-06` at `50` and require replay root-cause analysis | Cycle status `INVALID` |
| R15M-TW-03 | Any `>75` row lacks independent corroboration | Cap affected rows at `50` and force rescore | Cycle status `INVALID` |
| R15M-TW-04 | Any `>90` row lacks adversarial challenge evidence | Cap affected rows at `75` and trigger inflation review | Cycle status `INVALID` |
| R15M-TW-05 | Any unresolved Severity-1 contradiction exceeds SLA | Cap `R15M-03` at `50` and publication hold | Cycle status `INVALID` |
| R15M-TW-06 | Handoff silent acceptance detected on critical path | Cap `R15M-17` at `50` and require explicit re-adjudication | Publication hold until corrected |
| R15M-TW-07 | Unauthorized post-freeze rubric change detected | Stop scoring and revert to approved baseline | Cycle status `INVALID` |
| R15M-TW-08 | Decision chronology violation on critical rows | Cap `R15M-12` at `25` and require forensic timeline review | Cycle status `INVALID` |

### Hard-fail conditions (immediate invalidation of Rubric_0 scoring)
| ID | Hard-fail condition | Evidence test | Effect |
| --- | --- | --- | --- |
| R15M-HF-01 | Evidence fabrication, tampering, or forged approval in Rubric_0 scoring package (`G1`) | Provenance hash/signature forensic mismatch | Immediate cycle `INVALID`; forensic investigation required |
| R15M-HF-02 | Published decision bypasses an active global hard gate (`G2`, `G3`, `G5`, or `G6`) | Gate-state log vs published outcome comparison | Immediate cycle `INVALID`; publication revoked |
| R15M-HF-03 | Active critical role score <60 is not enforced as fail (`RG1`) | Role-layer outcome audit | Immediate cycle `INVALID` |
| R15M-HF-04 | Unresolved critical cross-role contradiction at cutoff (`RG3`) | Contradiction aging and closure audit | Immediate cycle `INVALID` |
| R15M-HF-05 | Material claims cannot be independently replayed/recomputed from retained evidence | Non-author replay failure on critical sample | Immediate cycle `INVALID`; full rescore required |
| R15M-HF-06 | Evidence package fails integrity/provenance checks (`RG4`) | Admissibility and chain-of-custody audit | Affected role score = `0`; cycle `INVALID` pending remediation |
| R15M-HF-07 | Reviewer independence breach on high-anchor rows is confirmed | Role-separation and COI audit | Immediate cycle `INVALID`; affected rows voided |
| R15M-HF-08 | Post-cutoff edits materially improve same-cycle scores without approved reopen | Version history and approval-chain audit | Immediate cycle `INVALID`; restart from frozen baseline |
| R15M-HF-09 | Missing mandatory `who/what/where` evidence in >10% sampled non-zero rows | Evidence completeness sampling audit | Immediate cycle `INVALID` |
| R15M-HF-10 | Systemic score inflation: >20% of `90+` rows lack required corroboration/challenge evidence | High-anchor evidence audit | Immediate cycle `INVALID`; mandatory full-scope inflation review |

## 7) Cross-role dependencies and adjudication handoffs

| Counterpart role | Required input to R15 meta-evaluation | R15 handoff output | Acceptance criteria | SLA / escalation |
| --- | --- | --- | --- | --- |
| R0 Executive Sponsor / Business Owner | Governance charter, risk appetite, and invalidation authority boundaries | Rubric_0 assurance-readiness verdict and hard-fail status | Signed decision with explicit treatment of all open critical defects | Escalate unresolved critical deadlock within 1 business day |
| R1 Product Manager | Scope intent, requirement criticality, and decision-use context for rubric tests | Coverage and operational-usability defects impacting adjudication flow | No unresolved ambiguity on decision-use intent for critical rows | Escalate within 2 business days |
| R2 Product Architect / Enterprise Architect | Gate logic structure, precedence assumptions, and contradiction pathways | Contradiction and gate-coherence remediation requirements | No unresolved architecture-driven gate contradiction at cutoff | Escalate same cycle for Severity-1 conflicts |
| R5 QA / Test Engineer | Testability review methods, replay sample strategy, and variance thresholds | Anchor testability defects, replay variance report, and correction actions | Replay tolerance and testability acceptance reached | Escalate in-cycle if tolerance is breached |
| R7 Security Engineer / Architect | Integrity-control requirements and shared blocker states | Security-linked gate and contradiction adjudication outcomes | No pass path with active critical integrity/security blocker | Immediate escalation on bypass discovery |
| R8 Privacy / Compliance / Legal | Legal precedence rules, obligation constraints, and contradiction evidence | Privacy/legal contradiction disposition and required rubric changes | Severity-1 legal/privacy contradiction count = 0 at cutoff | Escalate within 1 business day |
| R12 DevOps / Release Manager | Publication workflow logs, approval-chain data, and version-freeze records | Publication authorization recommendation with cutoff/version audit status | Approval chain valid and no unauthorized post-freeze change | Same-day escalation on workflow integrity defect |
| R11 Technical Writer / DocOps | Controlled wording changes, diff metadata, and rubric publication packaging | Accepted or returned rubric-text delta with impact scope | Every accepted wording change has approved impact map | Escalate on undocumented wording drift |
| R15 Internal Audit QAIP / External assessor | Independent quality sampling results and methodology conformance findings | Final assurance memo with QAIP closure obligations | Material QAIP exceptions closed or risk-accepted by authority | Escalate to audit committee for unresolved critical QAIP issues |

Adjudication handoff rules:
1. Every handoff artifact must include `owner`, `timestamp`, `rubric_version`, `affected_sub_dimensions`, and immutable evidence links.
2. Handoff state is binary: `accepted` or `returned`; silent acceptance is invalid.
3. Returned handoffs must include defect class, accountable owner, due date, and re-submission timestamp.
4. Two consecutive returns in the same defect class trigger mandatory `R0 + R15` adjudication within 1 business day.

## 8) Cycle improvement checklist focused on improving Rubric_0 and re-evaluating deltas

| Cycle phase | Checklist item | Evidence artifact | Pass criterion | Delta re-evaluation rule |
| --- | --- | --- | --- | --- |
| Pre-cycle baseline | Freeze Rubric_0 version hash, anchor set, gate logic, and denominator definitions. | Baseline manifest with signed approvals. | Zero unauthorized drift during scoring window. | Any unauthorized drift forces cycle restart on frozen baseline. |
| Pre-cycle baseline | Refresh assurance decision-class coverage map against current Rubric_0 sections and role layer. | Updated trace matrix and gap log. | Critical decision-class coverage = 100%. | New critical gap blocks scoring kickoff. |
| Pre-cycle baseline | Reconfirm contradiction taxonomy, precedence rules, and SLA timers. | Contradiction protocol conformance report. | No missing Severity-1 closure path. | Protocol change requires targeted re-score of impacted rows. |
| Calibration prep | Run anchor monotonicity and ambiguity lint for high-stakes rows. | Anchor lint report and defect tracker. | No open high-severity anchor ambiguity. | Unresolved ambiguity caps impacted rows at `50`. |
| Calibration prep | Run dual-rater calibration on representative rubric-evaluation packet. | Calibration variance report and dispute log. | Gate-state agreement = 100%; score variance within tolerance. | Variance breach requires calibration rerun before scoring continues. |
| Mid-cycle control | Execute mandatory anti-gaming checks from Section 5 and record outcomes. | Anti-gaming execution log and challenge outputs. | Mandatory checks executed = 100%. | Any miss triggers `R15M-TW-01`. |
| Mid-cycle control | Execute independent replay/recompute on >=15% sampled rows including gate-sensitive rows. | Replay transcript and variance register. | Variance and gate parity tolerances met. | Breach triggers `R15M-TW-02` and targeted rescore. |
| Mid-cycle control | Audit all `>75` and `>90` rows for required evidence and independence. | High-anchor evidence audit pack. | Unsupported high-anchor rows = 0. | Violations trigger caps/downgrades and possible invalidation. |
| Mid-cycle control | Verify decision chronology (`capture -> score -> approve -> publish`) for critical rows. | Chronology audit report and exception log. | Critical chronology violations = 0. | Violations trigger `R15M-TW-08` and forensic review. |
| Pre-close | Reconcile contradiction register with adjudication minutes and close all Severity-1 items. | Signed contradiction closure register. | Open Severity-1 contradictions at cutoff = 0. | Any open Severity-1 item triggers `R15M-TW-05`. |
| Pre-close | Recompute publication decision from raw gate states and hard-fail flags. | Gate-state recomputation worksheet. | Published decision exactly matches computed state. | Mismatch invalidates publication and requires rerun. |
| Publication | Publish final rubric assurance package with immutable evidence index. | Final package, evidence manifest, and signoffs. | Independent reviewer can replay sampled conclusions without author help. | Missing replayability proof blocks publication. |
| Post-cycle learning | Classify defects (false pass, false fail, ambiguity, replay drift, inflation, latency) and prioritize fixes. | Defect taxonomy report and prioritized backlog. | Every critical defect has owner, due date, and verification metric. | Unowned critical defect blocks next-cycle readiness. |
| Delta implementation | Apply only approved Rubric_0 deltas with row-level impact mapping. | Approved diff dossier and impact matrix. | Unauthorized delta count = 0. | Unauthorized delta triggers immediate hard-fail review. |
| Delta re-evaluation | Re-score impacted rows and rerun contradiction, replay, and gate-coherence tests. | Delta rescore packet and focused retest outputs. | Impacted-row retest coverage = 100%. | Any unexplained impacted-row shift >1 anchor requires rollback or redesign. |
| Next-cycle readiness | Validate closure effectiveness for prior critical defects through independent follow-up sampling. | Readiness signoff memo and closure evidence bundle. | Prior-cycle critical defects independently verified closed. | Unverified closure keeps Rubric_0 in hold state for next cycle. |

## Rubric_2 Cross-Role Minimum Sub-Dimension Normalization (R0..R15)

This section is normative for interoperability with `Rubric_2`.

For every role section (`R0..R15`), scoring must explicitly cover these six minimum
sub-dimensions in addition to role-specific dimensions:

1. `Coverage Sufficiency`
2. `Discriminative Anchors`
3. `Evidence Admissibility`
4. `Anti-Gaming Strength`
5. `Delta Efficacy`
6. `Contradiction Closure`

Normalization rules:

1. Any role section missing one or more of the six minimum sub-dimensions is capped
   at `90` until corrected.
2. Non-zero scoring for any minimum sub-dimension requires explicit
   `who/what/where` evidence and manifest-resolved `collateral_refs`.
3. Recheck must be executed by non-author judges with adversarial spot checks across
   all six minimum sub-dimensions.
4. `PERFECT PASS` for `Rubric_1` requires all six minimum sub-dimensions to be
   satisfied for every role (`R0..R15`) with replayable evidence.
