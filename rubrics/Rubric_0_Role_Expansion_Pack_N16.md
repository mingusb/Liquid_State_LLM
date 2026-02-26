# Rubric 0 Role Expansion Pack (N=16)

- generated_utc: 2026-02-24T01:53:24Z
- purpose: Consolidated role-wise sub-dimension expansions for the top-level role layer in Rubric 0.
- source_dir: `swarm_outputs/role_expansions/`

## Index

| Role ID | Role | File | Words | Lines |
| --- | --- | --- | ---: | ---: |
| R0 | Executive Sponsor / Business Owner | `swarm_outputs/role_expansions/R0_executive_sponsor_business_owner.md` | 4580 | 175 |
| R1 | Product Manager | `swarm_outputs/role_expansions/R1_product_manager.md` | 4305 | 169 |
| R2 | Product Architect / Enterprise Architect | `swarm_outputs/role_expansions/R2_product_architect_enterprise_architect.md` | 4974 | 180 |
| R3 | Engineering Manager | `swarm_outputs/role_expansions/R3_engineering_manager.md` | 3924 | 180 |
| R4 | Software Engineer | `swarm_outputs/role_expansions/R4_software_engineer.md` | 4214 | 182 |
| R5 | QA / Test Engineer | `swarm_outputs/role_expansions/R5_qa_test_engineer.md` | 4530 | 190 |
| R6 | SRE / Platform Engineer | `swarm_outputs/role_expansions/R6_sre_platform_engineer.md` | 4599 | 184 |
| R7 | Security Engineer / Security Architect | `swarm_outputs/role_expansions/R7_security_engineer_security_architect.md` | 5006 | 179 |
| R8 | Privacy / Compliance / Legal | `swarm_outputs/role_expansions/R8_privacy_compliance_legal.md` | 5082 | 180 |
| R9 | Data / AI Engineer or Scientist | `swarm_outputs/role_expansions/R9_data_ai_engineer_scientist.md` | 4509 | 201 |
| R10 | UX Researcher / Designer | `swarm_outputs/role_expansions/R10_ux_researcher_designer.md` | 4957 | 208 |
| R11 | Technical Writer / DocOps / PDF Owner | `swarm_outputs/role_expansions/R11_technical_writer_docops_pdf_owner.md` | 4966 | 207 |
| R12 | DevOps / Release Manager | `swarm_outputs/role_expansions/R12_devops_release_manager.md` | 5505 | 195 |
| R13 | Operations / Support / Customer Success | `swarm_outputs/role_expansions/R13_operations_support_customer_success.md` | 5592 | 197 |
| R14 | FinOps / Procurement / Vendor Management | `swarm_outputs/role_expansions/R14_finops_procurement_vendor_management.md` | 6002 | 206 |
| R15 | Internal Audit / Assurance | `swarm_outputs/role_expansions/R15_internal_audit_assurance.md` | 6371 | 223 |

---

## Pack-wide canonical contracts

### Canonical evidence field names and normalization
The canonical evidence schema for this role-pack is:

| Canonical field | Accepted aliases in role sections | Normalization rule |
| --- | --- | --- |
| `who` | none | keep as `who` |
| `what` | none | keep as `what` |
| `where` | none | keep as `where` |
| `time_utc` | none | keep as `time_utc` |
| `rubric_snapshot_id` | `iteration_snapshot_id` | keep as `rubric_snapshot_id` |
| `version` | `artifact_version`, `version_id` | normalize to `version` in scoring manifests |
| `hash` | `artifact_hash_sha256`, `evidence_hash`, `evidence_hash_sha256` | normalize to `hash` in scoring manifests |
| `provenance_chain` | `provenance_source` | normalize to `provenance_chain` in scoring manifests |

All role sections in this file may use aliases for readability, but scoring, publication, and replay outputs must emit canonical names only after normalization.

Normalization enforcement:

| Condition | Deterministic effect |
| --- | --- |
| Any published scoring packet row uses aliases instead of canonical field names | Publication blocked until normalization pass is rerun |
| Sampled non-zero rows with unnormalized alias fields exceed `2%` | Iteration packet marked `INVALID` for publication; targeted rescore required |
| Sampled non-zero rows missing canonical `provenance_chain` after normalization | Affected rows set to `0` and replay required |
| Normalization run lacks immutable ledger metadata and reviewer signoff | Publication blocked until normalized packet is regenerated and signed |
| Alias-map change occurs after snapshot without approved reopen | Iteration packet marked `INVALID` until approved reopen and targeted rescore complete |
| Normalization toolchain version drifts after snapshot without approved reopen | Iteration packet marked `INVALID`; normalization and scoring must rerun on approved toolchain snapshot |
| Normalization rerun on identical input yields non-idempotent output hash | Iteration packet marked `INVALID`; normalization path is non-deterministic until fixed |
| Dual-run normalization outputs disagree and no adjudication record exists | Publication blocked until deterministic normalization adjudication is signed |
| Dual-run mismatch has adjudication record but missing adjudication hash linkage in ledger | Publication blocked until ledger/adjudication linkage is complete |

Normalization run ledger (mandatory fields): `normalization_run_id`, `input_packet_hash`, `output_packet_hash`, `second_run_output_hash`, `alias_field_count`, `normalized_field_count`, `alias_map_version`, `normalization_rules_hash`, `normalizer_tool_version`, `normalizer_image_hash`, `rules_commit_hash`, `idempotence_check_hash`, `adjudication_record_hash`, `reviewer`, `secondary_reviewer`, `time_utc`, `snapshot_id`, `ledger_hash`.

### Canonical handoff defect-class lexicon
The authoritative `defect_class` vocabulary for this entire file is:
`coverage`, `evidence`, `contradiction`, `replay`, `inflation`, `operability`, `governance`.

No section may introduce alternate defect-class taxonomies for returned handoffs.

Canonical severity and SLA map:

| defect_class | Default severity | Default SLA to close |
| --- | --- | --- |
| `coverage` | Medium | 3 business days |
| `evidence` | High | 2 business days |
| `contradiction` | Critical | 1 business day |
| `replay` | High | 2 business days |
| `inflation` | Critical | 1 business day |
| `operability` | High | 2 business days |
| `governance` | Medium | 3 business days |

SLA breach escalation semantics:

| Condition | Deterministic effect |
| --- | --- |
| Returned defect passes `due_utc` without closure | Escalate to R0 + R15 within 4 business hours; keep handoff `returned` |
| `contradiction` or `inflation` defect class breaches SLA | Force critical escalation and publication hold until closure evidence is signed |
| Same `defect_class` breaches SLA in two consecutive iterations | Raise severity one level for next iteration and require corrective-action owner attestation |

Defect-class downgrade controls:

| Condition | Deterministic effect |
| --- | --- |
| Returned defect severity is downgraded vs prior open return on same issue without signed rationale | Downgrade is invalid; retain prior severity and keep handoff `returned` |
| Returned defect class changed to a lower-severity class without replay evidence | Publication hold until R15-signed downgrade packet is attached |

Defect lifecycle continuity controls:

| Condition | Deterministic effect |
| --- | --- |
| Returned handoff does not carry stable issue identity across iterations | Handoff is invalid; must be reissued with linked issue continuity metadata |
| State transition skips required prior state evidence (`returned` -> `accepted` without closure proof) | Transition invalid; handoff remains `returned` and publication hold stays active |
| Closed issue reopens without explicit reopen reason and authority | Reopen invalid; issue remains in prior terminal state until compliant reopen record is attached |
| Transition sequence is non-monotonic for the same `issue_id` | Transition invalid; issue history must be repaired before publication |
| Transition lacks accountable actor identity or transition reason metadata | Transition invalid; handoff remains at prior valid state until corrected |

### Bilateral handoff symmetry lint (critical pairs)
Before publication, a deterministic symmetry lint must validate every critical bilateral handoff pair listed in this file. For each pair, both directions must exist and must use parity-complete metadata:
`handoff_state`, `defect_class` (if `returned`), `owner`, `due_utc`, `resubmission_utc`, `snapshot_id`, `decision_hash`.

Any symmetry-lint failure blocks publication until corrected and replayed.

Authoritative critical bilateral pair registry:

| Pair ID | Endpoint A | Endpoint B |
| --- | --- | --- |
| BP-01 | R0 Executive Sponsor | R1 Product Manager |
| BP-02 | R0 Executive Sponsor | R2 Product Architect |
| BP-03 | R0 Executive Sponsor | R3 Engineering Manager |
| BP-04 | R0 Executive Sponsor | R5 QA/Test Engineer |
| BP-05 | R0 Executive Sponsor | R6 SRE/Platform |
| BP-06 | R0 Executive Sponsor | R7 Security |
| BP-07 | R0 Executive Sponsor | R8 Privacy/Compliance/Legal |
| BP-08 | R0 Executive Sponsor | R12 DevOps/Release |
| BP-09 | R0 Executive Sponsor | R14 FinOps/Procurement/Vendor |
| BP-10 | R0 Executive Sponsor | R15 Internal Audit/Assurance |
| BP-11 | R1 Product Manager | R15 Internal Audit/Assurance |
| BP-12 | R3 Engineering Manager | R8 Privacy/Compliance/Legal |
| BP-13 | R3 Engineering Manager | R15 Internal Audit/Assurance |
| BP-14 | R4 Software Engineer | R15 Internal Audit/Assurance |
| BP-15 | R6 SRE/Platform | R8 Privacy/Compliance/Legal |
| BP-16 | R6 SRE/Platform | R15 Internal Audit/Assurance |
| BP-17 | R7 Security | R15 Internal Audit/Assurance |

Mandatory symmetry-lint report fields:
`pair_id`, `endpoint_a_state`, `endpoint_b_state`, `metadata_parity_pass`, `defect_class_canonical_pass`, `reviewer`, `time_utc`, `snapshot_id`, `report_hash`.

Registry completeness constraints:
1. Every critical bilateral handoff pair observed in role sections must be represented in this registry.
2. No registry pair may remain unobserved for two consecutive iterations without signed waiver and rationale.
3. Registry lint output must include `observed_pair_count`, `missing_pair_count`, and `stale_pair_count`.

## R0 Executive Sponsor / Business Owner

- source_file: `swarm_outputs/role_expansions/R0_executive_sponsor_business_owner.md`
- words: 4580
- lines: 175

# R0 Executive Sponsor / Business Owner Rubric Expansion

## Role mission and decision rights

### Mission
The Executive Sponsor / Business Owner (R0) is the accountable owner of business outcomes, capital exposure, and enterprise risk acceptance for an initiative or portfolio slice. R0 is responsible for converting strategic intent into funded, governed delivery that produces measurable net benefits without violating legal, fiduciary, security, privacy, or reputational guardrails.

R0 is scored on verified outcomes and governance behavior, not intent, effort, or presentation quality.

### Decision rights (non-delegable accountability)
1. Approve or reject initiative start based on strategic fit, value hypothesis quality, and control readiness.
2. Set target outcomes, acceptable downside, and decision thresholds for continue/pivot/stop.
3. Commit and reallocate budget across stage gates, including freezing spend when controls fail.
4. Define risk appetite and tolerance bands for financial, compliance, operational, and reputational exposure.
5. Approve exceptions only with documented rationale, compensating controls, named owner, and expiry date.
6. Assign and replace accountable owners for value, risk, and remediation obligations.
7. Escalate cross-role deadlocks and unresolved critical risks within defined SLA.
8. Authorize launch/scale/retire decisions only when gate evidence meets policy standards.
9. Commission independent assurance when evidence integrity or reporting candor is uncertain.
10. Enforce post-release benefit realization reviews and corrective action closure.

### Scoring and evidence admissibility
- Anchor scale: `0`, `25`, `50`, `75`, `90`, `100`.
- Any non-zero score requires explicit `who/what/where/time/version/hash` evidence.
- Required non-zero evidence fields for every scored row: `who`, `what`, `where`, `time_utc`, `rubric_snapshot_id` (`iteration_snapshot_id` alias), `version` (`artifact_version`), `hash` (`artifact_hash_sha256`), and `provenance_chain`.
- Any non-zero row missing one or more required fields is deterministically set to `0` for the iteration.
- Evidence entered after the iteration cutoff is admissible only for the next iteration, unless a formally approved iteration reopen record exists.
- Claimed metrics must reconcile to source systems (finance, risk, audit, telemetry); unreconciled claims are scored as missing.
- High-anchor controls: scores `>75` require independent reviewer attestation; scores `>90` additionally require same-iteration replay and adversarial challenge evidence.

### Iteration snapshot/version governance and delta re-evaluation controls

| Control ID | Control requirement | Required record fields | Deterministic enforcement |
| --- | --- | --- | --- |
| R0-SV1 | Snapshot Rubric_0 and role-pack state before scoring starts. | `rubric_snapshot_id` (`iteration_snapshot_id` alias), `rubric_version`, `git_commit`, `rubric_hash_sha256`, `captured_time_utc`, approver signatures. | Scoring cannot start until snapshot record is complete and signed. |
| R0-SV2 | Lock scoring inputs to the approved snapshot. | `rubric_snapshot_id` (`iteration_snapshot_id` alias) on every scorecard row and evidence manifest. | Rows without matching snapshot ID are rejected and set to `0`. |
| R0-SV3 | Handle post-snapshot rubric edits through formal reopen only. | `reopen_request_id`, change rationale, impacted rows list, approving authority, effective time. | Any unapproved post-snapshot change invalidates the iteration result. |
| R0-SV4 | Re-evaluate only impacted rows, then re-run all gate checks after approved change. | Delta map (`old_row_id`, `new_row_id`, impact reason), re-score log, gate replay log. | Publication blocked until impacted-row re-score and gate replay both pass. |
| R0-SV5 | Maintain immutable change ledger for each iteration. | Sequential ledger ID, editor, timestamp, before/after hash, approval reference. | Missing ledger entries invalidate comparability claims for the iteration. |
| R0-SV6 | Prohibit retroactive score inflation. | Pre/post change score diff report with rationale and approvals. | Upward score deltas without approved reopen and replay evidence are voided. |

### Deterministic gate and contradiction precedence contract

| Precedence rank | Condition | Deterministic outcome |
| ---: | --- | --- |
| 1 | Non-zero row fails admissibility (`who/what/where/time/version/hash`). | Row score forced to `0`. |
| 2 | Any R0 hard-fail tripwire is active. | R0 role result set to `FAIL` and specified hard-fail effect applied. |
| 3 | Any unresolved `critical` contradiction remains open at decision time. | Overall result forced to `FAIL`; arithmetic result suppressed. |
| 4 | Any fail-state role gate (`RG1`/`RG3`) is active, or `RG4` causes role-zero effects that trigger `RG1` on recompute. | Overall result forced to `FAIL` regardless of weighted average. |
| 5 | Only cap-only role gates (`RG2`/`RG5`) are active. | Apply caps, recompute arithmetic, and continue to global-gate evaluation (no automatic `FAIL`). |
| 6 | Any global hard gate (`G1..G6`) is active after role-layer effects are applied. | Overall result forced to `FAIL` regardless of weighted average. |
| 7 | No active fail-state gates and no unresolved critical contradictions. | Compute weighted score using snapshot-locked inputs only. |

| Simulation case | Input state | Expected result |
| --- | --- | --- |
| R0-PR-01 | One row scored `90` with missing `artifact_hash_sha256`. | Row becomes `0`; role score recomputed from remaining admissible rows. |
| R0-PR-02 | Weighted aggregate computes to `88`, but `RG1` is active. | Final decision is `FAIL`; `88` is non-authoritative. |
| R0-PR-03 | Weighted aggregate computes to `92`, but one critical contradiction is unresolved. | Final decision is `FAIL`; contradiction closure required before publication. |
| R0-PR-04 | Weighted aggregate computes to `95`, but global gate `G5` is active. | Final decision is `FAIL`; replay/recompute issue must be closed first. |
| R0-PR-05 | No hard gates active, no unresolved critical contradictions, all evidence admissible. | Final decision determined by weighted score bands. |

## Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| R0.1 Strategic objective clarity and testability | Strategic goals are specific, measurable, time-bound, and directly traceable to funded work. | >=95% of active spend mapped to approved objectives; objective statements contain metric, baseline, target, date, owner; quarterly traceability refresh completed on time. | Who: R0 + PMO lead. What: strategy-to-initiative map with version history. Where: board packet and portfolio system record. |
| R0.2 Value hypothesis rigor | Each initiative has an auditable value hypothesis with baseline, benefit formula, assumptions, and confidence range. | 100% of approved initiatives include baseline + target + formula + owner; sensitivity analysis includes base/worst case; assumption register has review timestamps. | Who: R0 + finance partner + product manager. What: value case, assumptions log, confidence model. Where: investment memo repository and finance planning workbook. |
| R0.3 Portfolio prioritization integrity | Priority order is driven by agreed value/risk/capacity model, not influence or noise. | Off-model override rate <=15% per cycle; all overrides include rationale + impact; top quartile value items receive planned capacity >=85%. | Who: R0 + portfolio council chair. What: ranked backlog snapshots, override log, capacity allocation report. Where: portfolio tool and governance minutes. |
| R0.4 Investment adequacy and phasing | Funding is sufficient for promised outcomes and released by stage-gate evidence. | 100% tranche releases tied to gate criteria; unfunded mandated scope = 0; reforecast variance explained within 10 business days. | Who: R0 + finance controller. What: tranche approvals, gate checklists, reforecast notes. Where: finance ERP extracts and gate decision archive. |
| R0.5 Risk appetite and tolerance setting | Quantified risk tolerances are declared, communicated, and enforced in decisions. | Current risk appetite statement published; threshold breaches escalated within SLA (<=48h for critical); expired exceptions operating = 0. | Who: R0 + risk/compliance owner. What: risk appetite doc, breach log, exception register. Where: risk system and governance portal. |
| R0.6 Decision timeliness and governance cadence | Critical decisions are made within agreed SLAs with documented rationale. | >=90% critical decisions within SLA; meeting quorum met in >=95% decisions; decision aging dashboard has no critical item > SLA by >5 business days without escalation. | Who: R0 office + governance secretary. What: decision register with timestamps, quorum records, aging report. Where: governance tracker and committee minutes. |
| R0.7 Escalation and unblock effectiveness | R0 removes blockers quickly and decisively when teams cannot resolve them. | Critical cross-role blockers median time-to-resolution <=7 days; unresolved Sev-1 governance conflicts at cycle close = 0. | Who: R0 + EM + PM. What: escalation tickets, resolution decision logs, dependency burn-down. Where: issue tracker and weekly risk review notes. |
| R0.8 Exception approval discipline | Exceptions are rare, justified, controlled, time-limited, and independently reviewed. | Exception volume trend stable/decreasing; 100% exceptions include compensating control + expiry + owner; post-expiry renewal without review = 0. | Who: R0 + control owner + internal audit observer. What: signed exception forms, compensating control evidence, expiry actions. Where: GRC system and approval ledger. |
| R0.9 Accountable ownership continuity | Named accountable owners remain in role or are formally transitioned without control gaps. | Critical ownership vacancies >10 business days = 0; transition packets completed before owner change in >=95% cases; RACI drift reviewed monthly. | Who: R0 + HRBP + PMO. What: accountability roster, transition packets, RACI revisions. Where: portfolio governance repository and HR change log. |
| R0.10 Benefit realization governance | Benefits are measured after launch, variance is acted on, and value leakage is controlled. | >=95% launched initiatives tracked for benefits through committed horizon; major negative variance actioned within 15 business days; no benefit claim without baseline evidence. | Who: R0 + finance + product owner. What: benefits register, baseline-vs-actual reports, variance action plans. Where: finance BI dashboards and quarterly value review deck. |
| R0.11 Financial variance and reallocation discipline | R0 controls budget drift and reallocates capital based on evidence. | Forecast error within agreed tolerance; low-performing initiatives re-scoped/stopped within one cycle; discretionary spend freeze triggered when variance thresholds breached. | Who: R0 + finance controller. What: variance reports, reallocation decisions, stop/go memos. Where: monthly close package and investment committee records. |
| R0.12 Regulatory, legal, and fiduciary oversight | Mandatory obligations are reflected in decisions before commitment and release. | 100% required legal/compliance sign-offs captured pre-gate; open high-severity audit findings past due = 0; fiduciary conflicts disclosed in all applicable decisions. | Who: R0 + legal counsel + compliance lead. What: obligation checklist, sign-offs, conflict disclosures, audit aging. Where: legal hold system, audit tracker, board records. |
| R0.13 Stakeholder alignment and conflict arbitration | R0 aligns executive stakeholders and resolves conflicts with explicit trade-offs. | Major conflicts resolved or escalated within SLA; decision reversals due to unaddressed stakeholder conflict trend downward; dissent logged with closure actions. | Who: R0 + PM + architecture + operations leaders. What: stakeholder decision memos, dissent log, arbitration outcomes. Where: steering committee minutes and decision tracker. |
| R0.14 Kill/pivot discipline | R0 stops or pivots failing initiatives before avoidable sunk-cost expansion. | Continue decisions require updated evidence each gate; initiatives breaching downside threshold for 2 cycles are stopped/pivoted unless board-waived; zombie initiatives = 0. | Who: R0 + finance + PMO. What: gate outcomes, pivot/termination memos, downside threshold dashboard. Where: portfolio review artifacts and capital governance log. |
| R0.15 Evidence integrity and reporting candor | Executive reporting is complete, balanced, and consistent with source data. | No material mismatch between board report and source systems; red/amber issues not suppressed; reconciliation exceptions closed within 10 business days. | Who: R0 chief of staff + finance/risk data stewards. What: report-source reconciliations, issue disclosures, correction logs. Where: board pack archive and source-of-truth datasets. |
| R0.16 Corrective action closure and learning loop | Failures produce owned corrective actions that close on time and reduce recurrence. | >=90% corrective actions closed by due date; repeat findings trend down quarter-over-quarter; lessons integrated into next planning cycle artifacts. | Who: R0 + control owners + internal audit liaison. What: remediation tracker, effectiveness tests, updated policies/templates. Where: action register, retrospective records, policy repo. |

## Scoring anchors table (0/25/50/75/90/100)

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R0.1 Strategic objective clarity and testability | Funding has no objective mapping; goals are slogans. | Partial mapping exists but not measurable or current. | Most work mapped; several objectives lack baseline/target/owner. | >=90% mapped with measurable goals; periodic refresh performed. | >=95% mapped; traceability drives reprioritization decisions. | Full traceability independently verified; sustained objective attainment across cycles. |
| R0.2 Value hypothesis rigor | No quantifiable value case before approval. | Value cases exist but omit baseline/formula/confidence. | Baseline and target present; assumptions weak or untested. | Complete value hypotheses with sensitivity and review cadence. | Hypotheses are challenged with external benchmarks and adjusted early. | Forecast quality is consistently high; independent audit confirms rigor. |
| R0.3 Portfolio prioritization integrity | Priorities set by escalation power only. | Model exists but routinely bypassed without documentation. | Model used, but override rate high and capacity misaligned. | Prioritization mostly model-driven; overrides controlled and explained. | Overrides rare, impact-tested, and transparent; value-ranked delivery stable. | Multi-cycle evidence shows superior return from selection discipline. |
| R0.4 Investment adequacy and phasing | Funds released indiscriminately; no gate logic. | Gates documented but funding not contingent on evidence. | Gate-linked funding is inconsistent; reforecasts often late. | Tranche funding tied to gate outcomes with timely reforecasting. | Funding adequacy tested proactively; underfunded scope corrected early. | Capital deployment optimization proven by independent assurance. |
| R0.5 Risk appetite and tolerance setting | No explicit risk limits; breaches handled ad hoc. | Limits stated qualitatively, rarely used in decisions. | Some quantified thresholds; enforcement inconsistent. | Quantified limits used in approvals; breaches escalated on time. | Risk trends actively managed; exception hygiene strong. | Control behavior is resilient under stress and externally validated. |
| R0.6 Decision timeliness and governance cadence | Critical decisions stall without ownership. | Decisions occur, often late, with weak rationale capture. | SLA tracked but frequently missed; quorum discipline uneven. | Decision SLAs mostly met; rationale and quorum reliably documented. | Timely decisions under pressure with low avoidable rework. | Decision system is predictably fast, well-documented, and benchmark-grade. |
| R0.7 Escalation and unblock effectiveness | Blockers linger; no executive intervention. | Escalations acknowledged but rarely resolved in time. | Some blockers resolved; critical ones often age past SLA. | Most critical blockers resolved within SLA with clear owners. | Cross-role deadlocks resolved quickly with minimal delivery impact. | Escalation system prevents recurrence through structural fixes. |
| R0.8 Exception approval discipline | Exceptions are informal or undocumented. | Exceptions logged but missing controls/expiry. | Basic controls present; renewals poorly governed. | Exceptions include owner, control, expiry; reviews are timely. | Exception volume constrained; compensating controls tested. | Exception use is rare, high-quality, and independently challenged. |
| R0.9 Accountable ownership continuity | Critical initiatives lack named accountable owner. | Owners named but turnover causes unmanaged gaps. | Ownership tracked; transitions incomplete or delayed. | Continuity maintained with formal transitions and minimal gaps. | Succession risk managed proactively with no critical coverage loss. | Ownership continuity remains stable through organizational churn. |
| R0.10 Benefit realization governance | No post-launch benefit tracking. | Tracking is anecdotal or stops after go-live. | Benefits measured inconsistently; variance actions lag. | Benefits tracked through horizon; variance actions are timely. | Value leakage monitored and reduced with targeted interventions. | Realized benefits consistently meet/exceed commitments and are auditable. |
| R0.11 Financial variance and reallocation discipline | Budget drift unmanaged; no reallocation logic. | Variance reported late; weak corrective decisions. | Variance monitored; reallocations slow or politically constrained. | Variance controlled within thresholds; reallocations evidence-based. | Rapid reallocation away from underperformance preserves portfolio value. | Financial stewardship shows sustained efficiency gains verified by finance. |
| R0.12 Regulatory, legal, and fiduciary oversight | Mandatory sign-offs bypassed; duty-of-care breaches present. | Reviews occur after key decisions; conflicts poorly disclosed. | Compliance checks exist; closure of issues inconsistent. | Pre-gate sign-offs and fiduciary disclosures consistently enforced. | High-severity findings are prevented or closed rapidly. | Clean multi-cycle assurance outcome with strong defensibility. |
| R0.13 Stakeholder alignment and conflict arbitration | Executive conflicts unresolved; decisions repeatedly reversed. | Conflicts handled informally with unclear trade-offs. | Arbitration occurs but outcomes are slow/fragile. | Material conflicts resolved with documented trade-offs and owners. | Alignment durable; dissent captured and converted into action. | Stakeholder governance consistently prevents destabilizing reversals. |
| R0.14 Kill/pivot discipline | Failing initiatives continue indefinitely. | Stop criteria exist but are ignored. | Some pivots/stops occur, usually late after excess burn. | Downside thresholds trigger timely pivot/stop decisions. | Poor bets terminated early; capital redirected productively. | Portfolio shows institutionalized anti-sunk-cost behavior. |
| R0.15 Evidence integrity and reporting candor | Reporting is misleading, contradictory, or fabricated. | Selective reporting hides material risk signals. | Reporting mostly accurate; reconciliation breaks are frequent. | Balanced reporting with regular reconciliation and issue disclosure. | High candor culture: bad news surfaced early with corrective plan. | Reporting integrity is independently validated with zero material restatements. |
| R0.16 Corrective action closure and learning loop | Findings recur; actions unowned or never closed. | Action plans exist but miss deadlines with little consequence. | Majority closed, but effectiveness checks are weak. | Actions close mostly on time with effectiveness verification. | Recurrence declines and lessons update standards each cycle. | Learning loop is institutionalized, measurable, and resilient to leadership change. |

## Anti-gaming checks specific to this role

1. Freeze scoring credit for any metric redefinition introduced after variance appears unless backward comparability is demonstrated and approved by finance and audit.
2. Reject benefits claims that cannot be reconciled to finance-controlled source data; narrative-only claims score as `0` for related rows.
3. Sample at least 20% of “green” board-report items against raw source systems each cycle; any material mismatch forces full-scope reconciliation.
4. Flag and investigate “objective relabeling” where initiatives are remapped to broader goals after underperformance.
5. Treat backdated approvals, signatures, or decision timestamps as evidence-integrity violations.
6. Require explicit downside scenario in every continue decision; missing downside analysis voids approval quality credit.
7. Detect exception laundering by tracking repeated short-term renewals for the same control gap.
8. Compare promised capacity allocation to actual staffing/spend to catch priority theater.
9. Audit for “survivorship reporting”: verify terminated initiatives remain in performance denominator for portfolio learning.
10. Require minority/dissent opinions in arbitration records for major conflicts; absent dissent capture triggers governance-quality downgrade.
11. Verify that “on-time decision” metrics are not gamed by splitting one decision into serial low-value micro-decisions.
12. Apply conflict-of-interest checks to funding decisions involving sponsor-owned cost centers or incentives.

## Tripwires and hard-fail conditions

| ID | Hard-fail condition | Detection method | Immediate effect | Control owner | Minimum recovery proof |
| --- | --- | --- | --- | --- | --- |
| R0-HF1 | >10% of active portfolio spend has no mapped strategic objective and no approved waiver. | Portfolio objective-map audit against spend ledger snapshot. | R0 iteration score capped at `25`; new funding approvals blocked. | R0 + PMO lead | Corrected mapping with governance sign-off and independent sample validation. |
| R0-HF2 | Mandatory legal/compliance sign-off missing for any launched or scaled initiative. | Launch packet sign-off completeness check. | Automatic `FAIL` for R0 iteration; launch authority suspended pending review. | R0 + legal/compliance lead | Retroactive risk assessment, formal remediation plan, and control redesign approval. |
| R0-HF3 | Material evidence fabrication, tampering, or backdating in executive decisions/reports. | Hash/timestamp forensic audit on submitted evidence. | R0 score set to `0`; forensic audit triggered. | R0 + R15 | Forensic closure report, accountable action, and re-baselined evidence controls. |
| R0-HF4 | Critical risk threshold breached and left un-escalated beyond SLA (>48h). | Risk register timestamp vs escalation log comparison. | `FAIL` until escalation control is restored and retested. | R0 + risk owner | Timestamped escalation trail, accountable owner assignment, and repeat test pass. |
| R0-HF5 | Exception used without compensating control or with expired approval in production. | Exception register expiry and control-evidence audit. | Exception invalid; associated control area scored `0`. | R0 + control owner | Active compensating controls, renewed approval with expiry, and audit verification. |
| R0-HF6 | Benefit claims reported to governance forum without baseline or formula traceability. | Benefit claim audit against baseline/formula manifest. | Benefit-governance score capped at `25`; value claims excluded from decisions. | R0 + finance controller | Baseline reconstruction, formula documentation, and finance reconciliation sign-off. |
| R0-HF7 | Two consecutive iterations with unresolved high-severity audit findings owned by R0. | Iteration-over-iteration audit finding aging report. | `FAIL` for fiduciary oversight row and conditional portfolio freeze. | R0 + audit liaison | Closure evidence and effectiveness test passed by internal audit. |
| R0-HF8 | Failing initiative exceeds downside tolerance for 2 iterations without pivot/stop and without board waiver. | Downside-threshold dashboard and waiver audit. | Kill/pivot discipline scored `0`; portfolio governance exception review mandatory. | R0 + PMO | Formal pivot/terminate decision and capital reallocation evidence. |
| R0-HF9 | Board/executive report materially contradicts source systems on risk or financial status. | Report reconciliation test against source extracts. | Reporting integrity scored `0`; resubmission required before next decision meeting. | R0 chief of staff + finance/risk stewards | Corrected report, reconciled data pack, and independent reviewer attestation. |
| R0-HF10 | Critical accountability vacancy (>10 business days) for an in-flight high-risk initiative. | Ownership roster aging audit. | Ownership continuity row scored `0`; gate decisions paused for affected initiative. | R0 + HRBP | Named accountable replacement and completed transition packet with acceptance. |
| R0-HF11 | Post-snapshot rubric edits used in scoring without approved iteration reopen. | Snapshot hash diff against scoring version and reopen ledger. | Entire iteration result marked `INVALID`; publication blocked. | R0 + R12 + R15 | Approved reopen record, impacted-row re-score log, and successful gate replay. |
| R0-HF12 | Any score `>90` lacks same-iteration independent replay plus adversarial challenge evidence. | High-anchor audit of replay/challenge artifacts. | Affected rows downgraded to max `75`; if systemic (>3 rows), iteration marked `INVALID`. | R0 + independent reviewer + R15 | Complete replay/challenge package and rescored output with updated ledger. |

## Cross-role dependency and handoff criteria

| Partner role | What R0 must hand off | Acceptance criteria (receiver) | Return/escalation trigger |
| --- | --- | --- | --- |
| R1 Product Manager | Strategic objective priorities, value targets, non-goals, and decision thresholds. | R1 confirms PRD/roadmap traceability to objective map and measurable KPIs. | Ambiguous value target, conflicting priorities, or missing owner. |
| R2 Product Architect / Enterprise Architect | Risk tolerance bands, mandatory NFR priorities, approved trade-off envelope. | R2 returns architecture options with explicit fit to tolerance envelope and constraints. | Architecture requires unapproved risk posture shift or hidden dependency risk. |
| R3 Engineering Manager | Funding envelope by phase, staffing constraints, delivery governance cadence. | R3 provides feasible delivery plan with capacity realism and gate-ready milestones. | Delivery plan exceeds envelope or lacks critical capability coverage. |
| R5 QA / Test Engineer | Release decision criteria, quality guardrails, and acceptable residual defect risk. | R5 provides traceable verification evidence against release criteria and risk posture. | Critical coverage gaps or defect risk above approved threshold. |
| R6 SRE / Platform Engineer | SLO/availability targets, incident tolerance, rollback authority boundaries. | R6 confirms operability readiness, rollback tests, and on-call capability alignment. | SLO infeasible under current budget or rollback path unproven. |
| R7 Security Engineer | Security risk appetite, mandatory controls, exception policy boundaries. | R7 delivers threat/control status with explicit pass/fail against required controls. | Control failure requires waiver outside approved exception policy. |
| R8 Privacy / Compliance / Legal | Applicable obligations, approval gates, and non-negotiable legal constraints. | R8 attests obligation-to-control mapping and pre-release compliance status. | Missing legal basis, unresolved regulatory conflict, or unowned compliance gap. |
| R12 DevOps / Release Manager | Stage-gate release authority, freeze criteria, rollback decision protocol. | R12 confirms release checklist completion and evidence integrity before cutover. | Incomplete approvals, unsigned artifacts, or unresolved rollback prerequisites. |
| R14 FinOps / Procurement / Vendor Mgmt | Budget limits, unit economics targets, vendor risk tolerance, renewal guardrails. | R14 validates spend-to-value trajectory and contract controls against guardrails. | Vendor/commercial exposure exceeds tolerance or forecast drift unresolved. |
| R15 Internal Audit / Assurance | Control claims, sampling scope, evidence locations, remediation commitments. | R15 confirms testability and independently verifies control effectiveness claims. | Evidence not reproducible, remediation overdue, or independence conflict detected. |

### Cross-role handoff quality gates
1. Every handoff includes `decision date`, `accountable owner`, `expiry/next review date`, and `source-of-truth link`.
2. No downstream role may inherit contradictory targets (for example, reduced budget with unchanged scope and timeline) without explicit R0 arbitration record.
3. Handoff acceptance is binary (`accepted` or `returned`) within SLA; silent acceptance is invalid.
4. Returned handoffs require `defect_class` from the pack-wide canonical lexicon, plus `owner`, `due_utc`, and corrected `resubmission_utc`.
5. Repeated return of the same canonical `defect_class` in two iterations triggers R0 corrective-action ownership.
6. Bilateral critical-pair handoff symmetry lint must pass with metadata parity before publication.
7. Returned-handoff severity and closure SLA must follow the canonical `defect_class` severity/SLA map unless a signed exception is attached.
8. Any SLA-breached returned handoff must include escalation evidence and updated `due_utc` before closure can proceed.
9. Any severity downgrade on an open returned defect requires R15 co-sign and immutable downgrade-justification evidence.
10. Returned defect lifecycle transitions must preserve issue identity and prior-state linkage across iterations.
11. Any post-closure reopen transition must include approved reopen reason and authority-chain evidence.
12. Lifecycle transition sequence for each `issue_id` must be strictly monotonic and audit-replayable.
13. Every lifecycle transition must record accountable actor and transition reason evidence.

## Cycle-level improvement checklist

| Cycle point | Checklist item | Evidence artifact | Pass criterion |
| --- | --- | --- | --- |
| Pre-iteration planning | Create signed iteration snapshot (version + hash + cutoff + owner roster). | Snapshot manifest with `rubric_snapshot_id` (`iteration_snapshot_id` alias), hash set, and signatures. | No scoring starts without a complete snapshot manifest. |
| Pre-cycle planning | Reconfirm objective map and measurable targets for all funded initiatives. | Updated objective map with version tag and approver list. | 100% funded work mapped; no stale owner/date fields. |
| Pre-cycle planning | Revalidate value hypotheses and downside thresholds. | Value-case refresh pack with sensitivity deltas. | All initiatives have current base/worst-case assumptions. |
| Pre-cycle planning | Reapprove risk appetite and exception boundaries. | Signed risk posture memo and exception policy snapshot. | No ambiguity in critical thresholds or escalation SLA. |
| Pre-cycle planning | Confirm accountability roster and succession coverage. | Current RACI + transition readiness list. | No critical ownership vacancies at cycle start. |
| Mid-cycle control | Review decision aging and unblock queue. | Decision SLA dashboard and escalation log. | No critical decision >SLA without active escalation. |
| Mid-cycle control | Reconcile reported benefits/costs with source systems. | Finance reconciliation report and discrepancy log. | Material discrepancies resolved or formally escalated. |
| Mid-cycle control | Audit exception hygiene and expiry compliance. | Exception aging report with compensating-control evidence. | Zero expired exceptions operating in production. |
| Mid-cycle control | Test cross-role handoff quality on sampled items. | Handoff sample audit sheet and defect findings. | Sample pass rate >=90%; corrective owners assigned for failures. |
| End-cycle review | Execute continue/pivot/stop decisions using current evidence. | Gate decision pack with downside and trade-off record. | No initiative continues without evidence-backed decision. |
| End-cycle review | Run benefit realization and leakage review. | Benefits register with variance actions and due dates. | Major negative variances have owned, dated recovery plans. |
| End-cycle review | Verify corrective action closure effectiveness. | Remediation closure report with recurrence metrics. | >=90% on-time closure and decreasing recurrence trend. |
| End-iteration review | Execute deterministic gate/contradiction replay and high-anchor challenge audit. | Gate replay matrix + `>90` challenge/replay evidence pack. | 100% replay parity and 100% compliant high-anchor rows. |
| End-iteration review | If rubric deltas were approved, re-score impacted rows and rerun gate stack before publication. | Delta impact map, impacted-row re-score log, updated gate replay log. | No unresolved critical contradiction and no active hard-fail before publication. |
| End-cycle review | Publish candid executive report with reconciliation appendix. | Final governance report plus source reconciliation appendix. | No material contradiction between summary and source data. |

---

## R1 Product Manager

- source_file: `swarm_outputs/role_expansions/R1_product_manager.md`
- words: 4305
- lines: 169

# R1 Product Manager Rubric Expansion

## 1) Role mission and decision rights

**Role mission**
The Product Manager (R1) is accountable for turning business intent and user needs into evidence-backed product decisions that can survive adversarial review. R1 owns problem framing, outcome definition, scope discipline, cross-functional decision integrity, and value realization follow-through. R1 is not evaluated on narrative quality; R1 is evaluated on decision quality, evidence integrity, and measurable outcomes.

**Decision rights**

| Decision domain | R1 authority | Non-delegable decisions | Mandatory co-signers | Escalation trigger |
| --- | --- | --- | --- | --- |
| Problem selection | Accountable | Final problem statement, target segment, success window | R0 Executive Sponsor, Data Lead | Conflicting problem statements > 5 business days |
| KPI/OKR framework | Accountable | North-star KPI, guardrails, target thresholds | Data Lead, Engineering Manager | KPI has no reproducible baseline |
| Prioritization and sequencing | Accountable | Quarterly rank order and tradeoff rationale | Engineering Manager, Design Lead | Capacity overrun risk > 15% |
| Requirements baseline | Accountable | Acceptance criteria, non-goals, out-of-scope boundaries | Tech Lead, QA Lead | Critical requirement non-testable |
| Scope change control | Accountable | Approve/reject change requests affecting release objective | Engineering Manager, Release Manager | Scope delta > 10% without approved tradeoff |
| Launch recommendation | Recommend (not sole approver) | Residual risk statement and evidence package completeness | Security, SRE, Release Manager, R0 | Any unresolved Severity-1 risk |
| Post-launch correction | Accountable | Corrective backlog ranking and target recovery plan | Engineering Manager, Support Lead, Data Lead | KPI miss persists for 2 review cycles |

## 1A) Iteration snapshot, admissibility, and deterministic precedence contract

| Control ID | Control rule | Deterministic enforcement |
| --- | --- | --- |
| R1-SV1 | Each iteration must start with an approved snapshot containing rubric/process version and evidence cutoff metadata. | Scoring kickoff blocked until snapshot record is complete. |
| R1-SV2 | Every scored row must reference `rubric_snapshot_id` (`iteration_snapshot_id` alias) and `artifact_hash_sha256`. | Rows without matching snapshot ID/hash are scored `0`. |
| R1-SV3 | Post-snapshot rubric/process edits require approved iteration reopen and impacted-row map. | Any unapproved post-snapshot change invalidates the iteration result. |
| R1-SV4 | Approved delta changes require impacted-row re-score plus full gate replay before publication. | Publication blocked until re-score and gate replay logs are complete. |
| R1-SV5 | Retroactive score inflation is prohibited. | Upward deltas without reopen + replay evidence are voided. |

| Admissibility field | Requirement for non-zero claims | Enforcement |
| --- | --- | --- |
| `who` | Accountable scorer and evidence producer identity. | Missing field -> row score `0`. |
| `what` | Precise artifact or metric claim being scored. | Missing field -> row score `0`. |
| `where` | Immutable storage location or system-of-record reference. | Missing field -> row score `0`. |
| `time_utc` | Evidence capture timestamp in UTC. | Missing field -> row score `0`. |
| `artifact_version` | Version or revision ID of the evidence artifact. | Missing field -> row score `0`. |
| `artifact_hash_sha256` | Integrity hash for replay/recompute integrity. | Missing field -> row score `0`. |
| `rubric_snapshot_id` (`iteration_snapshot_id` alias) | Snapshot identifier linking evidence to current iteration. | Mismatch -> row score `0`. |

| Precedence rank | Condition | Deterministic outcome |
| ---: | --- | --- |
| 1 | Row admissibility failure. | Row score forced to `0`. |
| 2 | Active R1 tripwire/hard-fail in Section 5. | Apply defined cap/fail effect immediately. |
| 3 | Unresolved critical contradiction at decision close. | Publication blocked; role outcome is `FAIL`. |
| 4 | Active fail-state role/global gate (`RG1`,`RG3`,`G1..G6`) after cap-only effects are applied. | Final outcome is `FAIL`, regardless of arithmetic score. |
| 5 | Active cap-only gates only (`RG2`/`RG5`) with no fail-state gates. | Apply cap/rescore effects; publication remains eligible. |
| 6 | No active gates and no unresolved critical contradictions. | Publish arithmetic score with evidence manifest. |

| Determinism test case | Input state | Expected output |
| --- | --- | --- |
| R1-PR-01 | Row scored `90` with missing `artifact_hash_sha256`. | Row downgraded to `0`; role score recomputed. |
| R1-PR-02 | Arithmetic role score `84`, unresolved critical contradiction exists. | Publication blocked and role status `FAIL`. |
| R1-PR-03 | Arithmetic role score `93`, but no adversarial challenge evidence. | Affected row(s) capped at `75`; re-score required. |
| R1-PR-04 | Arithmetic role score `88`, global hard gate active. | Final decision `FAIL`; arithmetic score non-authoritative. |

## 2) Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| Problem framing falsifiability | Problem statement is explicit, bounded, and falsifiable. | Test: statement includes actor, blocked outcome, measurable impact, deadline. Test: at least one falsification condition exists. | Who: PM owner + Data Lead reviewer. What: versioned problem brief and falsification criteria. Where: PRD repository and decision log entry. |
| Baseline and causality integrity | Baseline state and causal assumptions are reproducible and not conflated with symptoms. | Test: baseline query reproduces reported value within 2%. Test: top 3 causal assumptions ranked by confidence and risk. | Who: PM + Analytics engineer. What: baseline SQL/query, causal map, assumption register. Where: analytics repo, experiment folder, PRD appendix. |
| Outcome and KPI architecture quality | KPI tree links user outcomes, business outcomes, and guardrails with clear ownership. | Test: every KPI has formula, owner, refresh cadence. Test: guardrail breach triggers alert and action owner. | Who: PM + Data Lead + Engineering Manager. What: KPI dictionary, alert thresholds, owner map. Where: metrics catalog and governance dashboard. |
| Prioritization model integrity | Backlog ranking uses explicit value, effort, risk, and urgency criteria. | Test: top 10 items scored with same model. Test: override decisions include documented rationale and approver. | Who: PM + Engineering Manager. What: scoring sheet, override log, ranking snapshots. Where: portfolio board and sprint planning archive. |
| Roadmap coherence and tradeoff integrity | Roadmap sequencing respects dependencies, capacity, and stated strategy. | Test: each roadmap item ties to objective and KPI. Test: dependency conflicts resolved before commitment. | Who: PM + Architect + Engineering Manager. What: roadmap baseline, dependency map, tradeoff records. Where: quarterly planning deck and dependency tracker. |
| Requirements quality and traceability | Requirements are atomic, testable, and traceable to problem and KPI hypotheses. | Test: critical requirements have objective acceptance criteria. Test: no orphan requirements in release scope. | Who: PM + QA Lead + Tech Lead. What: requirement catalog, acceptance matrix, traceability matrix. Where: PRD system and test management tool. |
| Release scope governance | Scope is locked and controlled with explicit change criteria and impact analysis. | Test: all change requests include impact on date, risk, KPI, and cost. Test: unauthorized scope additions = 0. | Who: PM + Release Manager. What: scope baseline, change requests, approval chain. Where: release board and change-control log. |
| Stakeholder alignment and conflict resolution | Material stakeholder conflicts are surfaced, adjudicated, and resolved with traceable decisions. | Test: unresolved critical conflicts aging < 10 business days. Test: all veto decisions have rationale and owner. | Who: PM + R0 + functional leads. What: conflict register, decision memos, escalation records. Where: governance meeting notes and decision registry. |
| Discovery and experiment rigor | Discovery work reduces uncertainty through pre-registered hypotheses and valid methods. | Test: hypothesis and success threshold defined before data collection. Test: discovery outcomes cause documented backlog changes. | Who: PM + UX Research + Data Lead. What: experiment plans, raw findings, decision delta notes. Where: research repo and backlog change history. |
| Dependency and delivery risk governance | External and internal dependencies have owners, contingency plans, and monitored risk aging. | Test: critical dependencies each have owner, SLA, and fallback. Test: overdue high-risk mitigations < 5%. | Who: PM + Engineering Manager + Partner owner. What: dependency register, risk log, mitigation tracker. Where: program risk board. |
| Go/no-go recommendation quality | Launch recommendation is evidence-backed, risk-explicit, and gate-compliant. | Test: gate checklist completion = 100% for mandatory controls. Test: residual risk acceptance signed by authorized roles only. | Who: PM + Security + SRE + Release Manager. What: launch packet, gate evidence, residual risk memo. Where: release approval workspace. |
| GTM and enablement alignment | Market messaging, sales enablement, and support readiness accurately reflect product behavior. | Test: top 5 externally stated claims map to implemented behavior. Test: support runbooks cover top incident classes. | Who: PM + GTM Lead + Support Lead. What: claim substantiation sheet, enablement artifacts, runbooks. Where: GTM launch folder and support KB. |
| Post-launch value realization follow-through | Outcome tracking verifies whether promised value is achieved and sustained. | Test: KPI review cadence met 100% of scheduled sessions. Test: value leakage root causes assigned within 5 business days. | Who: PM + Data Lead + Support Lead. What: KPI trend reports, leakage analysis, corrective backlog. Where: weekly business review and analytics dashboards. |
| Decision log hygiene and latency | High-impact decisions are documented with options, rationale, authority, and timestamp. | Test: decision logging coverage for material decisions >= 95%. Test: decision SLA breaches tracked and escalated. | Who: PM + PMO or Chief of Staff. What: decision ledger, SLA dashboard, escalation records. Where: governance log and planning workspace. |
| Compliance, privacy, and trust integration | Legal/privacy/trust constraints are integrated before release decisions, not post hoc. | Test: all high-risk features have legal/security review artifacts pre-launch. Test: user-facing disclosures match implemented behavior. | Who: PM + Legal/Privacy + Security. What: control mapping, approvals, disclosure text, validation checks. Where: compliance repository and release packet. |
| Portfolio opportunity-cost management | PM evaluates what not to build and quantifies opportunity cost of current roadmap choices. | Test: top alternatives (including do-nothing) evaluated each planning cycle. Test: stop/pivot criteria defined for underperforming bets. | Who: PM + Finance + R0 Sponsor. What: alternatives analysis, opportunity-cost model, stop/pivot decisions. Where: portfolio review pack and investment log. |

## 3) Scoring anchors table (0/25/50/75/90/100)

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| Problem framing falsifiability | No measurable problem statement; solution-led narrative only. | Problem statement exists but lacks measurable impact or deadline. | Measurable statement exists but falsification condition missing or weak. | Bounded, measurable, falsifiable statement with named owner/date. | Includes tested alternative hypotheses and explicit disconfirmation checks. | 90 plus assumptions stable across 2 cycles with logged corrections. |
| Baseline and causality integrity | Baseline not reproducible or contradicts source data. | Baseline exists but no query lineage or confidence level. | Reproducible baseline, but causality assumptions are implicit. | Reproducible baseline and ranked causal assumptions with evidence grades. | Includes sensitivity analysis and competing causal explanations. | 90 plus independent replay reproduces all baseline and assumption claims. |
| Outcome and KPI architecture quality | No coherent KPI tree or ownerless metrics. | KPI list exists; formulas/owners incomplete. | KPI tree defined; guardrails weak or unused in decisions. | KPI tree complete with formulas, owners, thresholds, review cadence. | Demonstrates at least one prevented harmful optimization via guardrail. | 90 plus KPI-driven decisions consistently predict directional outcomes across 2 cycles. |
| Prioritization model integrity | Priorities set ad hoc or by status only. | Criteria named but inconsistently applied. | Model applied, but overrides undocumented or frequent. | Consistent weighted model; overrides logged with approver and rationale. | Includes scenario-based reprioritization under realistic constraints. | 90 plus forecast-vs-realized value error stays within defined band for 2 cycles. |
| Roadmap coherence and tradeoff integrity | Roadmap disconnected from strategy and dependency reality. | Strategy linkage partial; tradeoffs undocumented. | Strategy linkage present; dependency/capacity checks inconsistent. | Sequence tied to objectives, capacity, dependencies, and tradeoffs. | Explicitly quantifies sacrificed outcomes and accepted risks. | 90 plus roadmap change decisions show measurable improvement in objective attainment across 2 cycles. |
| Requirements quality and traceability | Critical requirements missing or untestable. | Requirements present but ambiguous and weakly traceable. | Most requirements testable; trace gaps remain in critical paths. | Atomic, testable requirements fully traced to problem/KPI hypotheses. | Edge cases/non-goals quantified; QA challenge resolves major ambiguities pre-build. | 90 plus independent audit finds zero material ambiguity in sampled critical requirements. |
| Release scope governance | Scope drift unmanaged; unauthorized additions common. | Scope baseline exists but changes bypass governance. | Change governance exists; impact analysis incomplete. | All scope changes logged with approved impact analysis. | Scope control prevents at least one high-risk late addition. | 90 plus unauthorized scope additions remain zero across 2 release cycles. |
| Stakeholder alignment and conflict resolution | Critical conflicts hidden or unresolved. | Conflicts logged but no owners or deadlines. | Owners assigned; escalations slow or inconsistent. | Critical conflicts resolved within SLA with decision trace. | Uses structured conflict protocol reducing repeat escalations. | 90 plus zero aged critical conflicts beyond SLA across 2 cycles. |
| Discovery and experiment rigor | Discovery absent or purely confirmatory. | Experiments run without preregistered thresholds. | Thresholds exist; method/sample validity weak for decision risk. | Preregistered hypotheses, valid method, decision-linked outcomes. | Negative findings drive documented de-scope/pivot decisions. | 90 plus experiment accuracy and cycle time improve together across 2 cycles. |
| Dependency and delivery risk governance | Critical dependencies ownerless; no contingency plans. | Dependency list exists but stale and incomplete. | Owners assigned; mitigation closure poor or delayed. | Critical dependencies owned, monitored, and mitigated within SLA. | Tabletop or scenario drills validate contingency viability. | 90 plus no unflagged critical dependency failures across 2 cycles. |
| Go/no-go recommendation quality | Launch recommendation made without gate evidence. | Gate checklist partial; residual risk unquantified. | Gate evidence mostly present; approval authority gaps remain. | Full mandatory gate evidence with authorized residual risk acceptance. | Recommendation quality predicts launch risk profile accurately. | 90 plus no avoidable Severity-1 launch incidents attributable to missing PM evidence for 2 cycles. |
| GTM and enablement alignment | External claims materially misrepresent product behavior. | Claims and enablement artifacts exist but not validated. | Claims partially substantiated; support readiness uneven. | Claims substantiated; sales/support enablement aligned to behavior and limits. | Launch communications include clear limitation and mitigation guidance. | 90 plus claim accuracy and support readiness validated by first-30-day incident data across 2 launches. |
| Post-launch value realization follow-through | No post-launch value tracking or corrective ownership. | Tracking exists but irregular and reactive only. | Regular tracking with slow or weak corrective closure. | Scheduled reviews with owned corrective actions and recovery targets. | Value leakage root causes are prioritized and reduced quarter-over-quarter. | 90 plus promised value realization within agreed tolerance sustained across 2 quarters. |
| Decision log hygiene and latency | Material decisions undocumented or backfilled. | Partial logging; ownership and rationale missing often. | Logging mostly complete; SLA breach response inconsistent. | High-impact decision coverage >=95% with owner/rationale/timestamp. | Contradiction aging actively managed with escalation outcomes. | 90 plus independent audit reproduces complete decision trail for sampled releases. |
| Compliance, privacy, and trust integration | Known compliance/trust risk shipped without mitigation. | Risks listed but controls not mapped or owned. | Controls mapped; evidence incomplete or late in cycle. | Required control evidence complete before release decision. | Continuous trust/compliance monitoring with action thresholds active. | 90 plus zero material compliance/trust breaches attributable to PM governance across 2 cycles. |
| Portfolio opportunity-cost management | No alternatives analysis; sunk-cost bias dominates. | Alternatives named but not quantified. | Alternatives quantified once; stop/pivot criteria unclear. | Alternatives and do-nothing compared with explicit opportunity-cost model. | Underperforming bets are stopped/pivoted by predefined rules. | 90 plus portfolio reallocation improves aggregate objective yield over 2 planning cycles. |

## 4) Anti-gaming checks specific to Product Manager role

1. Baseline replay check: Independent reviewer reruns baseline query and compares against PM-reported baseline (tolerance <= 2%).
2. Pre-registration integrity check: Experiment hypothesis timestamp must predate first data collection event.
3. Metric freeze window: KPI formula and denominator changes are blocked inside each release freeze window unless governance exception is approved.
4. Scope laundering detection: Compare shipped artifacts to approved scope baseline; any unapproved high-impact item is auto-flagged.
5. Quote cherry-pick control: User research claims require full sample distribution and negative finding summary, not only positive excerpts.
6. Roadmap override audit: Every priority override must have approver identity, rationale, and displaced item impact.
7. Decision chronology check: Decision log timestamps must precede implementation merge/deploy timestamps for sampled items.
8. Sign-off authority validation: Launch and risk approvals are valid only if signed by authorized role holders at decision time.
9. Backfill exclusion rule: Evidence created after decision cutoff does not count for that cycle’s score.
10. Claim substantiation sweep: Top external claims are tested against real product behavior in staging and production.

## 5) Tripwires and hard-fail conditions

| ID | Trigger condition | Detection method | Immediate effect | Control owner | Minimum recovery proof |
| --- | --- | --- | --- | --- | --- |
| R1-TW1 | Non-zero claims fail admissibility (`who/what/where/time/version/hash`) in >5% sampled rows. | Independent evidence schema sample audit. | Affected rows forced to `0`; role score capped at `50` for the iteration. | R1 + R15 | Completed evidence remediation and resample below threshold. |
| R1-HF1 | Fabricated, altered, or backdated decision/evidence artifact. | Hash/timestamp forensic check and source-system comparison. | Entire R1 iteration marked `INVALID`; publication blocked. | R1 + R15 | Forensic closure report, corrected evidence chain, and independent re-score. |
| R1-HF2 | Launch recommendation submitted with unresolved Severity-1 user harm, legal, privacy, or security risk. | Launch packet contradiction check vs risk register. | Immediate `FAIL`; launch recommendation voided. | R1 + Security + Legal | Closed Sev-1 risks, updated launch packet, and re-approved decision. |
| R1-HF3 | Critical requirement in release scope lacks objective acceptance criteria. | Requirements traceability and testability audit. | Immediate `FAIL` for requirements governance. | R1 + QA lead | Corrected testable criteria and QA acceptance evidence. |
| R1-HF4 | KPI success claimed from non-reproducible metrics or unapproved formula/denominator changes. | Independent metric recompute + formula change log diff. | KPI-related rows set to `0`; role cannot exceed `50`. | R1 + Data lead | Reproducible recompute pack and approved metric-change record. |
| R1-HF5 | Scope increase >10% on committed objective without approved tradeoff decision and re-baseline. | Scope baseline diff against approved change-control ledger. | Scope-governance row set to `0`; release recommendation blocked. | R1 + Release manager | Approved tradeoff record, updated baseline, and impacted-row re-score. |
| R1-HF6 | Material stakeholder veto ignored and release proceeds without escalation record. | Decision log audit against veto register. | Immediate `FAIL`; decision packet revoked. | R1 + R0 | Escalation record with adjudication outcome and updated decision rationale. |
| R1-HF7 | Any high-risk dependency has no owner and no contingency at commitment point. | Dependency register completeness audit at commitment checkpoint. | Dependency-governance row set to `0`; commitment invalidated. | R1 + R3 | Owner assignment, contingency plan, and signed dependency acceptance. |
| R1-HF8 | PM-approved external claim is knowingly inconsistent with implemented behavior. | Claim substantiation replay in staging/production. | Immediate `FAIL`; external claim withdrawn. | R1 + GTM lead + Engineering | Corrected claim set, behavior validation evidence, and approval reissue. |
| R1-HF9 | Post-snapshot rubric/process edit used in scoring without approved iteration reopen. | Snapshot hash diff and reopen-ledger audit. | Entire iteration marked `INVALID`; full rescoring required. | R1 + R12 + R15 | Approved reopen record, impacted-row map, and complete re-score log. |
| R1-HF10 | Any score `>90` lacks same-iteration independent replay and adversarial challenge evidence. | High-anchor evidence audit. | Affected row(s) capped at `75`; if repeated (>3 rows), iteration `INVALID`. | R1 + independent reviewer + R15 | Replay transcript, challenge results, and rescored publication packet. |
| R1-HF11 | Mandatory anti-gaming challenge suite not executed in the iteration. | Anti-gaming execution ledger completeness check. | No score above `50` for affected scope; publication blocked until rerun. | R1 + R15 | Completed challenge suite evidence and rerun scoring results. |

## 6) Cross-role dependency and handoff criteria

| Handoff pair | PM must provide (outbound) | PM must receive (inbound) | Entry criteria | Exit/acceptance criteria | SLA |
| --- | --- | --- | --- | --- | --- |
| R1 -> R0 Executive Sponsor | Problem frame, opportunity-cost analysis, risk-adjusted recommendation | Strategic constraints, risk appetite, funding boundary | Problem and KPI baseline complete | Signed strategic decision with explicit constraints | 5 business days |
| R1 <-> R2 Architect | Prioritized capability outcomes, non-goals, NFR priorities | Feasibility constraints, architecture risks, dependency map | Objective and scope draft complete | Architecture risks reflected in roadmap and scope baseline | 4 business days |
| R1 <-> R3 Engineering Manager | Ranked backlog, acceptance criteria, release scope | Capacity forecast, delivery risk assessment, staffing constraints | Requirements v1 approved | Plan reflects realistic capacity and risk mitigation owners | Weekly planning cadence |
| R1 <-> R4 Software Engineer | Testable stories and decision rationale for edge cases | Implementation feedback, technical unknowns, effort signals | Story ready for development | Story accepted with clear acceptance test mapping | Per sprint |
| R1 <-> R5 QA/Test | Requirement trace matrix and release test intent | Coverage gaps, defect risk profile, pass/fail evidence | Acceptance criteria finalized | Critical-path test coverage and defect triage signed | Per release gate |
| R1 <-> R6 SRE/Platform | Launch behavior expectations, rollback criteria, SLO priorities | Operational readiness, capacity risk, incident readiness | Launch candidate identified | Go/no-go packet includes ops sign-off and rollback viability | 3 business days before launch |
| R1 <-> R7 Security | Feature intent, abuse cases, user flow changes | Threat findings, required controls, residual risk status | Feature design stable | Mandatory security controls accepted or release blocked | Before release decision |
| R1 <-> R8 Privacy/Legal | Data-use purpose, consent behavior, user disclosure text | Legal obligations, policy constraints, approval status | Data flow and UX copy drafted | Legal/privacy approvals recorded and traceable | Before release decision |
| R1 <-> R10 UX Research/Design | Priority questions, target segments, success thresholds | Research findings, usability risks, design alternatives | Discovery plan approved | Findings incorporated into prioritized backlog decisions | Within discovery cycle |
| R1 <-> R12 DevOps/Release Manager | Final scope baseline, launch risk memo, gate evidence map | CI/CD gate status, artifact provenance, rollback path status | Release candidate ready | All mandatory release gates pass with authorized approvals | Release cutoff |
| R1 <-> R13 Support/Operations | Known limitations, issue taxonomy, customer communication plan | Early incident trends, support burden data, KB gaps | Launch date set | First-30-day support plan active with owners and thresholds | 2 business days before launch |
| R1 <-> R14 FinOps/Procurement | Demand forecast, packaging assumptions, feature value thesis | Unit cost model, vendor constraints, budget guardrails | Pricing/roadmap proposal prepared | Approved economic model ties scope to budget and margin floor | Monthly portfolio review |
| R1 <-> R15 Internal Audit/Assurance | Decision logs, evidence manifest, contradiction closures, and gate replay artifacts for scored PM claims | Admissibility findings, replay variance report, and return metadata (`accepted`/`returned`, defect class, owner, due date) | Release/planning packet assembled and snapshot locked | R15 confirms reproducibility and either accepts or returns with explicit defect metadata | 3 business days |

## 7) Cycle-level improvement checklist

Use this checklist each planning/release cycle. Any unchecked item requires explicit risk acceptance.

| Cycle phase | Checklist item | Evidence artifact |
| --- | --- | --- |
| Intake | Create iteration snapshot record (`version`, `hash`, `cutoff`, reviewer roster). | Snapshot manifest and approvals |
| Intake | Problem statement includes actor, impact metric, and deadline | Versioned problem brief |
| Intake | Baseline reproducibility verified by non-author reviewer | Baseline replay record |
| Planning | KPI tree and guardrails approved with owners | KPI dictionary and owner map |
| Planning | Top-priority items scored with standard model; overrides justified | Prioritization sheet and override log |
| Planning | Opportunity-cost alternatives reviewed (including do-nothing) | Portfolio alternatives memo |
| Design/Discovery | High-uncertainty assumptions assigned validation experiments | Assumption register + experiment plan |
| Design/Discovery | Stakeholder conflicts logged with owners and due dates | Conflict log |
| Build readiness | Requirements are testable and fully traced to outcomes | Traceability matrix |
| Build readiness | Scope baseline locked; change-control protocol active | Release scope baseline |
| Pre-launch | Mandatory security/privacy/legal/ops gates completed | Signed gate checklist |
| Pre-launch | Validate deterministic precedence replay on sampled contradictions and gate triggers. | Precedence replay matrix |
| Pre-launch | External claims substantiated against implemented behavior | Claim substantiation sheet |
| Launch | Residual risks accepted by authorized roles only | Residual risk memo |
| Post-launch (week 1-2) | KPI and incident review cadence met | Review minutes and dashboard snapshots |
| Post-launch (week 3-6) | Value leakage root causes assigned and corrective actions started | Leakage analysis + corrective backlog |
| Retrospective | Forecast vs realized value error quantified and explained | Quarterly value realization report |
| Retrospective | Audit all `>90` scores for replay plus adversarial challenge evidence. | High-anchor audit log and reviewer attestations |
| Retrospective | If approved deltas occurred, re-score impacted rows and rerun gate checks before carry-forward. | Delta impact map, impacted-row re-score, gate replay report |
| Retrospective | Template/process updates merged to prevent repeated failure modes | Updated rubric/checklist changelog |

---

## R2 Product Architect / Enterprise Architect

- source_file: `swarm_outputs/role_expansions/R2_product_architect_enterprise_architect.md`
- words: 4974
- lines: 180

# R2 Product Architect / Enterprise Architect Rubric Expansion

## 1) Role mission and decision rights

### Role mission
R2 is the accountable architecture authority for converting product strategy into an implementable, governed system design across business capabilities, application boundaries, data semantics, integration contracts, and non-functional controls. R2 is judged on decision quality and control effectiveness, not on document volume. A non-traceable architecture claim is treated as unproven.

R2 must ensure:
- Strategic goals are translated into auditable architecture decisions.
- Target and transition architectures are executable by delivery teams.
- Risk controls (security, privacy, resilience, compliance) are designed in before release.
- Architecture tradeoffs are explicit, approved, and reversible where feasible.
- Technical debt trajectory is managed with measurable closure, not deferred indefinitely.

### Decision rights
| Decision area | R2 authority | Non-delegable boundary | Required co-signers | Evidence required for valid decision |
| --- | --- | --- | --- | --- |
| Capability and domain decomposition | Final decision authority | Cannot violate mandated legal segregation of duties | Product Manager, Engineering Manager | Domain map revision, impacted service list, signed decision record |
| Target-state architecture baseline | Final decision authority | Cannot waive mandatory security/privacy/compliance controls | Security Architect, Privacy/Compliance | Baseline package, unresolved contradiction log = 0 critical |
| Transition-state sequencing | Final for architecture-critical dependencies | Cannot commit delivery date when critical dependency is unresolved | Program/Delivery lead | Dependency critical path, gate results, approved mitigation for each high risk |
| NFR budgets (availability, latency, recovery) | Final architecture budget setter | Cannot set below contractual/regulatory minimums | SRE lead, Product Manager | NFR budget sheet, validation test plan, waiver register |
| Integration contract standards | Final authority on contract/version policy | Cannot allow unannounced breaking change | API lead, QA lead | Versioning policy, compatibility test evidence, migration plan |
| Data canonical model arbitration | Final arbiter on semantic conflicts | Cannot bypass privacy classification or retention obligations | Data lead, Privacy/Compliance | Canonical model change set, lineage impact assessment, sign-off |
| Build-vs-buy architecture recommendation | Technical veto on non-viable options | Cannot approve spend without finance authority | Finance/Procurement, Product leadership | Options analysis with TCO/risk, lock-in/exit plan |
| Architecture exceptions and waivers | Joint approval with control owners | Cannot approve expired or unbounded high-risk waiver | Security, SRE, Compliance | Exception record with expiry, compensating controls, owner |
| Architecture conformance gate | Final pass/fail on architecture readiness | Cannot bypass evidence requirements for critical services | Engineering Manager, Release Manager | Conformance report, exception count by severity, release gate minutes |

## 1A) Iteration snapshot governance, admissibility, and scoring arithmetic contract

### Authoritative scoring arithmetic contract

| Step | Rule | Deterministic specification |
| ---: | --- | --- |
| 1 | Input validation | Allowed anchors per row are only `0/25/50/75/90/100`; any other value is invalid. |
| 2 | Admissibility gate | Non-zero rows must include `who/what/where/time/version/hash`; missing field forces row to `0`. |
| 3 | Row-level controls | Apply row-level tripwires/caps before any averaging. |
| 4 | Role raw mean | `role_raw = mean(all row scores after Step 1-3)` computed to 4 decimal places. |
| 5 | High-anchor control | Any row `>90` without same-iteration replay + adversarial challenge evidence is capped to `75` before recomputing `role_raw`. |
| 6 | Role-level caps/fails | Apply role tripwires and hard-fails from Section 5. |
| 7 | Gate precedence | `FAIL` only when unresolved critical contradiction exists, any global gate (`G1..G6`) is active, or fail-state role gates (`RG1`/`RG3`) are active after cap-only effects. `RG2`/`RG5` are cap-only and do not independently force `FAIL`. |
| 8 | Rounding and publication | Publish role score rounded to 1 decimal place after all caps/fails/gates are applied. |

| Precedence rank | Condition | Outcome |
| ---: | --- | --- |
| 1 | Admissibility failure on non-zero claim. | Row score `0`. |
| 2 | Row-level cap/hard-fail trigger. | Row-level effect applied. |
| 3 | Role-level hard-fail trigger. | Role outcome `FAIL`. |
| 4 | Unresolved critical contradiction. | Publication blocked; role `FAIL`. |
| 5 | Active fail-state gate (`RG1`,`RG3`,`G1..G6`) after cap-only effects. | Role/final outcome `FAIL` regardless of arithmetic score. |
| 6 | Active cap-only gates only (`RG2`/`RG5`) with no fail-state gates. | Apply caps and publish recomputed rounded arithmetic score. |
| 7 | No active fails/gates. | Publish rounded arithmetic score. |

| Parity test ID | Test case | Required result |
| --- | --- | --- |
| R2-CALC-01 | Independent calculator A and B compute same dataset. | Exact parity at 1 decimal place and matching gate state. |
| R2-CALC-02 | Inject missing `artifact_hash_sha256` in one non-zero row. | Row becomes `0`; recomputed score parity preserved. |
| R2-CALC-03 | Inject unresolved critical contradiction with high arithmetic score. | Final outcome must be `FAIL` in both calculators. |
| R2-CALC-04 | Inject `>90` row without challenge evidence. | Row capped at `75`; recomputed score parity preserved. |

### Iteration snapshot/version and delta re-evaluation controls

| Control ID | Requirement | Enforcement |
| --- | --- | --- |
| R2-SV1 | Record `rubric_snapshot_id` (`iteration_snapshot_id` alias), rubric version, commit, and hash before scoring. | No scoring until snapshot record is approved. |
| R2-SV2 | Bind every scored row to `rubric_snapshot_id` (`iteration_snapshot_id` alias). | Snapshot mismatch -> row rejected and scored `0`. |
| R2-SV3 | Require formal iteration reopen for any post-snapshot rubric/process change. | Unapproved post-snapshot edits invalidate the iteration result. |
| R2-SV4 | Re-score impacted rows and rerun gate/precedence tests after approved delta. | Publication blocked until delta re-evaluation artifacts are complete. |
| R2-SV5 | Maintain immutable change ledger with before/after hash and approver IDs. | Missing ledger entry voids delta and comparability claims. |

## 2) Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| R2-01 Strategy-to-capability traceability | Architecture decisions are bidirectionally linked from strategic objective to capability to implementation scope. | `% in-scope epics with strategy objective ID`; `% capabilities with owner + KPI baseline`; `orphan architecture decisions count`. | Who: Product Architect + Product Manager. What: trace matrix, capability map, KPI baseline sheet. Where: version-controlled architecture repository, roadmap system, governance minutes. |
| R2-02 Domain boundary and ownership integrity | Domain boundaries are explicit, stable, and mapped to a single accountable owner per critical component. | `% Tier-1 services with named owner`; `cross-domain change conflicts per cycle`; `boundary violation incidents`. | Who: Product Architect + Engineering Manager. What: domain map, service ownership register, conflict log. Where: service catalog, architecture repo, incident tracker. |
| R2-03 Target-state architecture completeness | Required architecture viewpoints are current, consistent, and approved for release scope. | `% required viewpoints present`; `critical contradictions unresolved`; `% constraints quantified (capacity, latency, security)`. | Who: Product Architect + Security + SRE. What: target-state package, contradiction register, approval record. Where: architecture repository, review board records. |
| R2-04 Transition architecture and dependency sequencing | Current-to-target transition plan is dependency-aware with enforceable gates and rollback-safe sequencing. | `% critical dependencies with owner + mitigation`; `milestones passed with gate evidence`; `sequence violations after commitment`. | Who: Product Architect + Program lead. What: transition diagrams, dependency critical path, gate checklist. Where: delivery planning tool, architecture governance log. |
| R2-05 NFR architecture budget quality | Critical journeys have explicit performance, reliability, and recovery budgets with validation evidence. | `% critical journeys with quantified NFR budgets`; `% budgets validated by test`; `expired NFR waivers`. | Who: Product Architect + SRE + QA. What: NFR catalog, load/failure test reports, waiver log. Where: architecture repo, CI artifact store, release evidence pack. |
| R2-06 Integration contract and version governance | Interfaces are versioned, compatibility-tested, and changed through controlled migration paths. | `% interfaces with versioned contract`; `unapproved breaking changes`; `% releases with passing contract tests`. | Who: Product Architect + API lead + QA. What: schema registry export, compatibility test results, migration notices. Where: contract registry, CI pipeline logs, release notes. |
| R2-07 Data architecture semantics and lineage | Canonical entities, classification, and end-to-end lineage are controlled for critical data flows. | `% critical entities aligned to canonical model`; `% regulated elements with lineage complete`; `semantic conflict aging`. | Who: Product Architect + Data lead + Privacy. What: canonical model, lineage map, classification matrix, conflict decisions. Where: data catalog, architecture repository, governance tracker. |
| R2-08 Security and privacy-by-design architecture | Threat and privacy controls are mapped to architecture components before implementation. | `% mandatory controls mapped to components`; `% high-risk threats with mitigation design`; `overdue security/privacy architecture findings`. | Who: Product Architect + Security Architect + Privacy officer. What: threat model, control mapping, design review closure evidence. Where: risk register, security review system, architecture repo. |
| R2-09 Resilience and failure-mode design | Failure modes are explicitly designed with containment, degradation, and recovery behaviors. | `% critical failure modes with tested response`; `single points of failure unresolved`; `RTO/RPO design violations`. | Who: Product Architect + SRE + Engineering lead. What: failure mode analysis, chaos/tabletop outcomes, recovery design docs. Where: reliability workspace, runbook repository, incident records. |
| R2-10 Operability and observability-by-design | Logging, metrics, traces, and runbook hooks are part of architecture acceptance criteria. | `% critical services meeting observability minimum`; `% alerts mapped to business/user impact`; `mean detection gap for major incidents`. | Who: Product Architect + SRE + Operations. What: observability standard checklist, telemetry coverage report, runbook completeness audit. Where: monitoring platform, runbook system, architecture acceptance record. |
| R2-11 Technical debt trajectory governance | Debt is inventoried, risk-ranked, and actively reduced according to policy and impact. | `% high-risk debt items with owner + due date`; `debt backlog aging`; `incident recurrence linked to known debt`. | Who: Product Architect + Engineering Manager. What: debt register, risk scoring, retirement plan, closure evidence. Where: issue tracker, architecture debt board, incident RCA archive. |
| R2-12 ADR quality and decision latency | Material architecture decisions are documented with alternatives, rationale, and timely approval. | `% material changes with ADR`; `median decision latency vs SLA`; `% ADRs with rejected alternatives and consequences`. | Who: Product Architect + Architecture review board. What: ADR set, decision timestamps, alternative analysis artifacts. Where: ADR repository, review board minutes. |
| R2-13 Build-vs-buy and platform fit economics | Platform and sourcing choices are justified by technical fit, lifecycle economics, and exit viability. | `% major platform decisions with option analysis`; `% analyses including lock-in + exit cost`; `actual vs forecast variance post-decision`. | Who: Product Architect + Finance + Procurement. What: option scorecards, TCO model, sensitivity analysis, post-implementation review. Where: decision repository, finance model store, procurement records. |
| R2-14 Compliance and control-by-design traceability | Regulatory and policy obligations are traced to concrete architecture controls and test evidence. | `% obligations mapped to controls`; `% mapped controls with verification evidence`; `expired compliance exceptions`. | Who: Product Architect + Compliance + Security. What: obligation-control matrix, control test evidence, exception approvals. Where: GRC system, architecture repository, audit evidence store. |
| R2-15 Architecture conformance and exception governance | Delivery artifacts are checked for conformance and exceptions are governed with expiry and closure. | `% release candidates passing conformance checks`; `critical exceptions open past expiry`; `repeat exception rate by team`. | Who: Product Architect + Engineering Manager + Release Manager. What: conformance scan reports, exception register, closure proofs. Where: CI gate output, architecture governance tracker, release logs. |
| R2-16 Cost-performance efficiency architecture | Architecture choices achieve required service levels within approved unit-cost envelopes. | `cost per transaction/user vs target`; `resource saturation at p95 load`; `efficiency regression count after architecture changes`. | Who: Product Architect + SRE + FinOps. What: unit-economics dashboard, performance profiles, capacity model deltas. Where: observability platform, FinOps dashboard, architecture change log. |

## 3) Scoring anchors (explicit behavioral anchors for every sub-dimension)

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R2-01 Strategy-to-capability traceability | No maintained map; architecture work cannot be tied to strategic objectives. | Map exists as slides only; <60% in-scope work traceable; owners missing. | 60-79% traceability; forward links exist but reverse links to outcomes are incomplete. | >=80% bidirectional traceability; owners and KPIs assigned for most capabilities. | >=95% traceability; independent sample confirms no material orphan items. | 100% in-scope traceability sustained for 2 cycles; zero orphan decisions and audited outcome linkage. |
| R2-02 Domain boundary and ownership integrity | Tier-1 domains/services have no accountable owner; boundaries undefined. | Partial boundary map; frequent ownership disputes; >20% Tier-1 assets unowned. | Boundary map mostly present; conflicts recurring; ownership incomplete in critical areas. | Boundaries explicit for major domains; >=80% Tier-1 ownership complete; disputes resolved within SLA. | >=95% Tier-1 ownership complete; boundary violations rare and time-bounded. | 100% Tier-1 ownership with zero unresolved boundary conflicts across 2 cycles. |
| R2-03 Target-state architecture completeness | Target-state baseline absent or obsolete for release scope. | Fragments exist; critical viewpoints missing; contradictions unmanaged. | Most viewpoints present but with unresolved critical contradictions or unquantified constraints. | Required viewpoints complete for core scope; contradictions tracked and mostly closed. | Viewpoints >=95% complete and internally consistent; critical contradictions = 0. | Full approved package for all in-scope domains, no contradictions, and downstream specs synchronized. |
| R2-04 Transition architecture and dependency sequencing | Transition plan absent; delivery sequence ignores architecture dependencies. | Basic timeline with no dependency critical path; gates not enforced. | Dependency map exists but stale/incomplete; repeated sequence violations. | Dependency-critical path maintained; gates used for most critical milestones. | >=95% critical dependencies have owner+mitigation; sequence violations exceptional. | 100% critical dependencies governed; no unauthorized sequence violations for 2 cycles. |
| R2-05 NFR architecture budget quality | No quantified NFR budgets for critical journeys. | Budgets stated qualitatively; validation absent; waivers unmanaged. | Quantified budgets for some journeys; partial validation; waiver aging uncontrolled. | >=80% critical journeys have quantified budgets and testable acceptance criteria. | >=95% budget coverage validated by tests; no overdue critical waivers. | 100% critical journeys budgeted and validated; sustained compliance with no critical waiver debt. |
| R2-06 Integration contract and version governance | Interfaces changed ad hoc; no versioning or compatibility policy. | Contract docs partial; tests optional; breaking changes occur without process. | Versioning policy exists; enforcement inconsistent; migration planning weak. | >=80% interfaces versioned with compatibility tests in release path. | >=95% interfaces versioned; zero unapproved breaking changes in cycle. | 100% governed interfaces plus proven migration discipline and partner notification compliance. |
| R2-07 Data architecture semantics and lineage | No canonical semantics for critical entities; lineage unknown. | Canonical model partial; regulated data classification/lineage missing in many cases. | Canonical mapping moderate; semantic conflicts unresolved beyond SLA. | Critical entities mostly mapped; lineage present for major regulated flows. | >=95% regulated critical flows have complete lineage and approved semantic model. | 100% critical entity alignment and lineage, with zero unresolved semantic conflicts. |
| R2-08 Security and privacy-by-design architecture | Mandatory controls not mapped; threat/privacy design absent. | Control mapping started but <60% complete; high-risk findings stale. | Control mapping moderate; mitigations partly designed; closure inconsistent. | Most mandatory controls mapped and reviewed before build; findings tracked to closure. | >=95% mandatory controls mapped with verification path; no overdue critical finding. | 100% mapped and verified for scope; zero critical overdue findings and no control bypasses. |
| R2-09 Resilience and failure-mode design | Critical failure modes unidentified; no containment/recovery design. | Failure list exists but not actionable; SPOFs accepted without owner. | Major failure modes identified; response patterns partially tested. | Core failure modes designed with tested detection/containment paths. | >=95% critical failure modes have tested responses; RTO/RPO design meets policy. | Full failure-mode coverage with verified recovery behavior and no unresolved critical SPOF. |
| R2-10 Operability and observability-by-design | Architecture omits telemetry/runbook requirements for critical services. | Minimum standards written but not enforced; incident detection mostly reactive. | Telemetry coverage partial; runbook quality inconsistent. | Observability minimums enforced for major services; detection and runbook quality acceptable. | >=95% critical services meet observability standard; alert-to-impact mapping validated. | 100% critical coverage with demonstrated fast detection and actionable runbooks across incidents. |
| R2-11 Technical debt trajectory governance | No debt inventory or ownership; debt decisions are implicit. | Debt list exists but unranked/unfunded; aging uncontrolled. | Inventory and scoring present; closure sporadic; high-risk items persist. | High-risk debt has owner+date for most items; retirement plan active. | >=95% high-risk items governed to SLA; debt-related incident recurrence declining. | High-risk debt controlled with sustained downward trend and verified value/risk improvement. |
| R2-12 ADR quality and decision latency | Material architecture decisions undocumented or backfilled. | ADR template exists but adoption <60%; alternatives/rationale weak. | ADR coverage moderate; timestamps or consequences incomplete. | >=80% material decisions have timely ADRs with alternatives and tradeoffs. | >=95% material decisions captured within SLA; implementation traceability strong. | 100% material decisions captured pre-implementation, with auditable rationale and reversal criteria. |
| R2-13 Build-vs-buy and platform fit economics | Selection made by opinion or vendor pressure; no comparative analysis. | Options listed without lifecycle cost/risk quantification. | Comparative analysis present for some decisions; lock-in/exit analysis incomplete. | Most major decisions include fit/risk/TCO analysis and decision record. | >=95% major decisions include sensitivity analysis and explicit exit path. | 100% major decisions evidenced with post-implementation variance within approved tolerance. |
| R2-14 Compliance and control-by-design traceability | Obligations not mapped to architecture controls for release scope. | Mapping exists but incomplete and unverified; exceptions poorly governed. | Mapping moderate; evidence fragmented; exception aging high. | Most obligations mapped with test evidence and accountable control owner. | >=95% mapping + verification complete; no overdue critical compliance exception. | Full obligation-control traceability and verification with zero critical exception debt. |
| R2-15 Architecture conformance and exception governance | No conformance gate; releases ship without architecture checks. | Conformance checks optional; exceptions open-ended and untracked. | Checks run for some teams; exception process inconsistent. | Conformance gate applied to major releases; exceptions time-bounded and owned. | >=95% release candidates pass gate or have approved bounded exceptions. | 100% conformance coverage, zero critical expired exceptions, and repeat exceptions reduced cycle-over-cycle. |
| R2-16 Cost-performance efficiency architecture | Architecture drives cost overruns or misses service targets with no corrective path. | Cost/performance tracked informally; no unit-cost target governance. | Unit-cost and performance tracked but tradeoffs unresolved. | Cost/performance targets set and reviewed; corrective actions executed on breach. | >=95% critical services stay within target envelope with evidence-backed tuning. | Sustained target compliance with documented architecture optimizations and no unmanaged regressions. |

## 4) Anti-gaming checks specific to R2

1. Reject any non-zero score when evidence is presentation-only and has no source-controlled artifact link.
2. Recompute a random 15% sample of claimed metrics from raw logs or source systems; scoring uses recomputed values.
3. Invalidate architecture approvals created after release cutoff for that cycle (no retroactive credit).
4. Detect denominator manipulation by comparing current and prior-cycle population definitions for each percentage metric.
5. Require independent reviewer sign-off for any `90` or `100` anchor claim.
6. Cap sub-dimension at `50` when contradiction logs exist but are hidden from review packet.
7. Treat “temporary” exceptions without expiry date, owner, and compensating control as unapproved exceptions.
8. Compare ADR timestamps against merge/deploy timestamps; post-hoc ADR creation cannot score above `25`.
9. Cross-check contract version numbers in code artifacts against published interface registry to detect silent breaking changes.
10. Verify that “closed” technical debt items show production validation evidence, not just ticket closure state.
11. For conformance scores, sample excluded teams/services; any unjustified exclusion invalidates the score.
12. Mark evidence tampering, log deletion, or provenance mismatch as integrity failure and force role-cycle fail.

## 5) Tripwires and hard-fail conditions

| ID | Condition | Detection method | Immediate effect | Control owner | Minimum recovery proof |
| --- | --- | --- | --- | --- | --- |
| HF-01 | Critical release scope has no approved target-state architecture package. | Release gate audit shows missing baseline or missing required viewpoints. | Hard fail: block release and set R2 iteration status to `FAIL`. | R2 + Release manager | Approved target-state package and repeated gate pass evidence. |
| HF-02 | Mandatory security, privacy, or regulatory control is absent from architecture mapping. | Obligation-to-control matrix diff against policy baseline. | Hard fail until mapping and verification evidence are complete. | R2 + R7 + R8 | Completed mapping, verification artifacts, and independent review sign-off. |
| HF-03 | Breaking interface change deployed without approved migration and communication plan. | Contract registry/version diff and release notes review. | Hard fail plus rollback/hotfix requirement. | R2 + API lead | Approved migration plan, partner notification evidence, and compatibility retest pass. |
| HF-04 | Tier-1 domain or service has no accountable owner for more than 5 business days. | Service catalog ownership audit with timestamp aging. | Hard fail on R2-02 and release hold for affected scope. | R2 + R3 | Named owner assignment and ownership acceptance evidence. |
| HF-05 | Contractual or customer-committed NFR is unquantified at commitment point. | Commitment packet review vs NFR budget table. | Hard fail on R2-05 and mandatory re-commitment process. | R2 + R6 | Quantified NFR budget, validation plan, and approved recommitment record. |
| HF-06 | Regulated critical data element lacks lineage or classification in release scope. | Data catalog lineage completeness check for scoped entities. | Hard fail until lineage/classification is corrected and re-audited. | R2 + Data lead + Privacy | Completed lineage/classification records and privacy sign-off. |
| HF-07 | Material architecture change implemented without ADR or emergency decision record. | Change log to ADR cross-reference. | Hard fail on R2-12; block further changes in impacted domain. | R2 + Architecture board | Backfilled decision record with approved emergency rationale and independent review. |
| HF-08 | Critical architecture exception is expired but still active in production. | Exception register expiry audit plus runtime dependency scan. | Hard fail on R2-15 and immediate escalation to governance board. | R2 + control owner | Renewed exception with fresh evidence or verified exception closure. |
| HF-09 | Conformance gate bypassed for critical service release. | CI/release pipeline gate event audit. | Hard fail and release invalidation for that artifact. | R2 + R12 | Re-executed conformance gate with complete evidence chain and approvals. |
| HF-10 | Evidence fabrication, tampering, or provenance mismatch confirmed. | Forensic integrity check and immutable-log verification. | Hard fail: R2 score = `0` for iteration; mandatory investigation. | R2 + R15 | Forensic closure report and clean independent replay on remediated evidence pack. |
| HF-11 | Post-snapshot rubric/process edit used in scoring without approved iteration reopen. | Snapshot hash diff against scoring artifacts and reopen ledger audit. | Iteration marked `INVALID`; publication blocked. | R2 + R12 + R15 | Approved reopen record, impacted-row re-score log, and parity replay pass. |
| HF-12 | Any score `>90` lacks same-iteration replay and adversarial challenge evidence. | High-anchor evidence audit. | Affected rows capped to `75`; if repeated (>3 rows), iteration marked `INVALID`. | R2 + independent reviewer + R15 | Replay/challenge evidence pack and rescored publication packet. |

## 6) Cross-role dependency and handoff criteria

| Counterparty role | Required input to R2 | R2 handoff output | Acceptance criteria for handoff completion | SLA / cadence |
| --- | --- | --- | --- | --- |
| R1 Product Manager | Prioritized outcomes, constraints, KPI definitions, committed dates | Capability map, architecture feasibility decision, scope boundary constraints | Every committed epic has objective link, architecture risk grade, and explicit accept/reject rationale | Weekly planning; 4 business days for priority/scope changes |
| R0 Executive Sponsor / Business Owner | Strategic constraints, risk appetite, investment guardrails, and exception boundaries | Architecture decision package with risk-adjusted tradeoffs, residual-risk statement, and funding-impact notes | Sponsor-level constraints are explicitly mapped to accepted architecture decisions with no unresolved severity-1 contradiction | 5 business days for material architecture risk or funding-impact changes |
| R3 Engineering Manager | Team capacity, delivery risks, current system constraints | Domain ownership decisions, conformance requirements, transition gates | Engineering plan references approved architecture IDs and no unresolved critical contradiction | Weekly architecture-delivery sync |
| R4 Software Engineer / Tech Lead | Design proposals, implementation alternatives, estimated impacts | Approved patterns, ADR decisions, interface and NFR requirements | Proposed design passes pattern checklist and maps to an approved ADR | Per material design change; response SLA 2 business days |
| R5 QA / Test Engineer | Validation strategy, coverage gaps, defect trends | Architecture acceptance test criteria, contract/NFR test obligations | Test plan traces every architecture-critical requirement to executable checks | Per release and at design freeze |
| R6 SRE / Platform | SLO history, capacity/saturation trends, incident learnings | NFR budgets, resilience patterns, observability requirements | SLO budgets are measurable and test plan exists for each critical journey | Weekly reliability review |
| R7 Security Architect | Threat model updates, control requirements, risk findings | Security-by-design architecture decisions and exception dispositions | All high-risk threats in scope have mapped architecture mitigation and owner | At each major architecture review |
| R8 Privacy/Compliance/Legal | Regulatory obligations, policy changes, audit findings | Obligation-to-control architecture mapping and remediation plan | No high-severity obligation gap remains unresolved at release gate | Monthly governance plus release gate |
| R9 Data/AI Engineer | Data model proposals, pipeline dependencies, lineage status | Canonical semantics rulings, data contract and lineage requirements | Canonical entities and lineage expectations accepted and versioned | Bi-weekly data architecture board |
| R12 DevOps / Release Manager | Release plan, environment constraints, gate results | Architecture conformance gate decision and approved exceptions | Release candidate has pass status or bounded exception with expiry and owner | Per release train |
| R14 FinOps / Procurement | Cost baselines, vendor terms, budget guardrails | Build-vs-buy architecture recommendation and risk-adjusted TCO rationale | Decision includes exit path, lock-in score, and variance monitoring plan | Per sourcing decision; response SLA 5 business days |
| R15 Internal Audit / Assurance | Control testing scope, sampling protocol, prior findings | Evidence package with provenance and remediation closure records | Independent audit can reproduce sampled claims without manual reinterpretation | Quarterly or on-demand audit windows |

## 7) Cycle-level improvement checklist

Use this checklist each scoring cycle; an unchecked item requires explicit exception approval.

| Phase | Checklist item | Owner | Done criteria | Evidence artifact |
| --- | --- | --- | --- | --- |
| Iteration start | Record approved snapshot (`rubric_snapshot_id`, version, commit, hash, cutoff; `iteration_snapshot_id` accepted as alias). | R2 + R12 + R15 | Snapshot fields complete and signed before scoring. | Snapshot manifest and approval record |
| Cycle start | Re-baseline scope and mark architecture-critical items. | R2 + R1 | 100% scoped items classified by architecture criticality. | Scope baseline snapshot + criticality tag export |
| Cycle start | Refresh domain map and Tier-1 ownership roster. | R2 + R3 | No Tier-1 owner gaps older than 5 business days. | Domain map diff + service owner audit |
| Cycle start | Confirm mandatory control catalog version for security/privacy/compliance. | R2 + R7 + R8 | Control catalog version pinned for cycle with no unresolved critical mapping gaps. | Control baseline record + mapping report |
| Design phase | Enforce ADR creation before implementation for material changes. | R2 + R4 | 100% material changes linked to ADR ID before merge. | ADR index + change-to-ADR trace report |
| Design phase | Quantify NFR budgets for all newly committed critical journeys. | R2 + R6 | Every critical journey has latency/availability/recovery target and test method. | NFR budget table + planned validation matrix |
| Design phase | Verify integration contracts and migration paths for changed interfaces. | R2 + R5 | No interface change without version strategy and compatibility test plan. | Contract diff report + migration checklist |
| Mid-cycle | Run independent contradiction sweep across architecture viewpoints. | R2 reviewer not author | Critical contradictions = 0 or escalated with dated closure plan. | Contradiction register with owner and due date |
| Mid-cycle | Run dual-calculator parity test on sampled scoring data and gate states. | R2 + R12 | Exact parity at 1 decimal place and identical gate outcomes. | Parity report and mismatch log |
| Mid-cycle | Audit exception register for expiry, owner, and compensating controls. | R2 + control owners | 0 critical expired exceptions; all others explicitly time-bounded. | Exception aging report |
| Pre-release | Execute architecture conformance gate on release candidate. | R2 + R12 | Pass status or formally approved bounded exceptions only. | Conformance gate report + release minutes |
| Pre-release | Reconcile promised NFRs and control mappings with final build artifacts. | R2 + R6 + R7 + R8 | No missing contractual NFR or mandatory control in final scope. | Final traceability packet |
| Pre-release | Validate every `>90` row has same-iteration replay and adversarial challenge evidence. | R2 + independent reviewer + R15 | 100% high-anchor rows have compliant evidence. | High-anchor audit checklist and reviewer signatures |
| Post-release | Compare predicted vs actual cost-performance and reliability outcomes. | R2 + R6 + R14 | Variance explained; corrective actions opened for out-of-tolerance deltas. | Post-implementation review |
| Post-release | Update debt trajectory and architecture standards based on incidents/findings. | R2 + R3 + R15 | All material learnings converted into dated backlog items or standard updates. | Debt board update + standard revision log |
| Post-release | If approved deltas occurred, re-score impacted rows and rerun precedence/gate replay before carry-forward. | R2 + R12 + R15 | Re-score and gate replay completed with no active hard-fail. | Delta impact map, impacted-row re-score log, replay report |

---

## R3 Engineering Manager

- source_file: `swarm_outputs/role_expansions/R3_engineering_manager.md`
- words: 3924
- lines: 180

# R3 Engineering Manager Rubric Expansion

## 1) Role mission and decision rights

### Role mission
Own engineering execution integrity: convert approved product and architecture intent into predictable, safe, and maintainable delivery outcomes. The Engineering Manager (EM) is accountable for schedule realism, quality gate enforcement, incident-learning closure, staffing effectiveness, and truthful risk disclosure.

### Decision rights
1. Accept, reject, or re-sequence engineering commitments based on capacity and risk evidence.
2. Enforce release-quality gates; block release when mandatory controls are unmet.
3. Allocate team capacity across feature work, reliability work, and technical debt retirement.
4. Escalate cross-team dependency risk and trigger executive decisions when blocked beyond SLA.
5. Set staffing plans, hiring priorities, and backfill ordering within approved budget.
6. Initiate corrective actions for performance, skill gaps, and ownership gaps.
7. Approve operational readiness for services owned by the team.
8. Own post-incident corrective action closure and recurrence prevention for team-owned systems.

### Non-delegable accountabilities
1. No optimistic status reporting without evidence.
2. No hidden risk carry-over across cycles.
3. No waiver of security/compliance gates without explicit authority trace.
4. No closure of corrective actions without objective verification.

## 1A) Iteration snapshot, critical-role gate policy, and deterministic precedence

### Critical-role gate policy
- `RG1` critical-role set for role-layer enforcement is: `R1`, `R2`, `R3`, `R4`, `R6`, `R7`, `R8`, `R12`.
- Any role in this set with score `<60` forces overall `FAIL`, regardless of arithmetic aggregate.
- R3 is mandatory in this set for every iteration; omission is a governance defect and blocks publication.

### Non-zero admissibility schema

| Field | Requirement | Enforcement |
| --- | --- | --- |
| `who` | Scorer and evidence owner identity. | Missing field -> row score `0`. |
| `what` | Specific claim/artifact being scored. | Missing field -> row score `0`. |
| `where` | Immutable evidence location/system reference. | Missing field -> row score `0`. |
| `time_utc` | Evidence timestamp in UTC. | Missing field -> row score `0`. |
| `artifact_version` | Artifact or dataset version ID. | Missing field -> row score `0`. |
| `artifact_hash_sha256` | Integrity hash for replay/recompute checks. | Missing field -> row score `0`. |
| `rubric_snapshot_id` (`iteration_snapshot_id` alias) | Snapshot link for current iteration. | Snapshot mismatch -> row score `0`. |

### Iteration snapshot/version and delta re-evaluation controls

| Control ID | Control rule | Deterministic enforcement |
| --- | --- | --- |
| R3-SV1 | Capture approved iteration snapshot before scoring (`version`, `commit`, `hash`, `cutoff`). | Scoring cannot start without snapshot record. |
| R3-SV2 | Bind all scored rows and evidence to `rubric_snapshot_id` (`iteration_snapshot_id` alias). | Snapshot mismatch rows are rejected (`0`). |
| R3-SV3 | Require approved iteration reopen for any post-snapshot rubric/process edit. | Unapproved edit invalidates the iteration result. |
| R3-SV4 | Re-score impacted rows and replay gate stack after approved deltas. | Publication blocked until delta re-evaluation is complete. |
| R3-SV5 | Prohibit retroactive score inflation. | Upward deltas without reopen + replay evidence are voided. |

### Deterministic precedence truth table

| Precedence rank | Condition | Outcome |
| ---: | --- | --- |
| 1 | Row admissibility failure. | Row score `0`. |
| 2 | Active tripwire/hard-fail in Section 5. | Apply specified cap/fail immediately. |
| 3 | Unresolved critical contradiction at decision close. | Role/final status `FAIL`; publication blocked. |
| 4 | `RG1` breach in critical-role set (including `R3`). | Overall status `FAIL`, arithmetic suppressed. |
| 5 | Active fail-state gate (`RG3` or any `G1..G6`) after cap-only effects. | Overall status `FAIL`, arithmetic suppressed. |
| 6 | Active cap-only gates only (`RG2`/`RG5`) with no fail-state gates. | Apply caps and publish recomputed arithmetic score with evidence manifest. |
| 7 | No active fails/gates. | Publish arithmetic score with full evidence manifest. |

| Determinism case | Input state | Expected result |
| --- | --- | --- |
| R3-PR-01 | R3 arithmetic score `59.9`, no other gate active. | RG1 breach -> overall `FAIL`. |
| R3-PR-02 | R3 arithmetic score `91`, but no challenge/replay evidence. | Affected row(s) capped to `75`; recompute required. |
| R3-PR-03 | High arithmetic score and unresolved critical contradiction. | Publication blocked and status `FAIL`. |
| R3-PR-04 | No contradictions, all gates clear, full admissibility fields present. | Publish arithmetic score. |

## 2) Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| Commitment Reliability | Degree to which promised scope and dates are met without late surprises. | Sprint commitment hit rate; forecast error by milestone; % slips pre-flagged >=1 cycle earlier. | Who: EM, PM. What: locked commitment baseline, delivered scope report, variance analysis. Where: sprint board snapshots, planning docs, release notes repository. |
| Flow Health and WIP Control | Stability of engineering flow and control of queue aging. | p50/p85 cycle time trend; aged WIP > SLA count; blocked-days ratio. | Who: EM, Tech Lead. What: cycle-time dashboard, blocker log with owner/time-to-clear. Where: issue tracker analytics, weekly ops review notes. |
| Scope Change Governance | Discipline for mid-cycle scope adds/removals and tradeoff documentation. | Mid-cycle scope-change count; % changes with explicit tradeoff memo; interrupt budget usage. | Who: EM, PM. What: change log, tradeoff decisions, interrupt budget ledger. Where: planning changelog, decision record folder. |
| Quality Gate Enforcement | Adherence to pre-release criteria (tests, reviews, risk signoffs). | % releases passing all mandatory gates (`MG-01..MG-06`) first attempt; gate waiver count; waiver approval validity. | Who: EM, QA Lead, Release Manager. What: gate checklist, waiver approvals, failed gate incidents. Where: CI/CD pipeline records, release governance docs. |
| Defect Escape Control | Prevention of high-severity defects escaping to production. | Sev1/Sev2 escape rate; regression reopen rate; change failure rate. | Who: EM, QA Lead. What: defect trend by severity, RCA links, reopen audit. Where: incident tracker, defect system, PIR archive. |
| Reliability and SLO Stewardship | Management of service reliability against agreed SLO/error-budget policy. | Error-budget burn; SLO attainment; repeat incident ratio. | Who: EM, SRE Lead. What: SLO dashboards, burn-rate logs, recurrence report. Where: observability platform, reliability review records. |
| Incident Learning Closure | Quality and timeliness of post-incident corrective actions. | PIR completion SLA; corrective action closure SLA; recurrence within 60 days. | Who: EM, Incident Commander. What: PIR documents, action tracker, closure verification evidence. Where: incident knowledge base, action tracker system. |
| Risk Escalation Timeliness | Speed and quality of raising risks before deadline or quality breach. | % high risks escalated before breach; risk age by severity; escalation latency. | Who: EM. What: risk register with timestamps, escalation records, mitigation owners. Where: risk system, leadership escalation channel logs. |
| Cross-team Dependency Governance | Control of external dependencies required for delivery. | Dependency SLA attainment; overdue external blockers; blocked critical-path days. | Who: EM, partner EM/Lead. What: dependency contract, weekly dependency review, unblock decisions. Where: program board, dependency tracker, meeting minutes. |
| Maintainability and Technical Debt Allocation | Allocation and execution of debt reduction to sustain development speed and safety. | % capacity reserved for debt/reliability; debt aging; hotspots with rising change failure. | Who: EM, Tech Lead. What: debt backlog with priority rationale, completed debt outcomes. Where: engineering roadmap, architecture debt register. |
| Staffing Capacity Adequacy | Match between workload demand and available role/skill capacity. | Capacity vs demand gap; single-owner critical components; on-call load concentration. | Who: EM. What: capacity model, skills matrix, ownership map. Where: workforce planning docs, service ownership registry. |
| Hiring and Onboarding Throughput | Efficiency and quality of filling roles and integrating hires to productivity. | Time-to-fill; offer acceptance rate; time-to-first-independent delivery. | Who: EM, Recruiting Partner. What: hiring funnel metrics, interview scorecards, onboarding milestones. Where: ATS reports, onboarding tracker, team wiki. |
| Performance Management and Coaching | Consistency and effectiveness of expectations, feedback, and corrective action. | Goal completion quality; coaching cadence adherence; unresolved low-performance cases. | Who: EM, HR Partner. What: goal records, feedback artifacts, performance plans and outcomes. Where: performance system, manager 1:1 logs, HR case records. |
| Security and Compliance Execution | Delivery compliance with security remediations and mandated controls. | Critical vuln remediation SLA; overdue controls; audit finding recurrence. | Who: EM, Security Lead. What: vuln backlog status, control evidence pack, audit closure proofs. Where: security tracker, compliance repository, audit portal. |
| Cost and Productivity Stewardship | Control of engineering spend relative to delivered outcomes. | Budget variance; cloud/tool unit-cost trend; output per engineer trend adjusted for severity mix. | Who: EM, Finance Partner. What: monthly budget actuals, cost attribution, productivity trend analysis. Where: finance dashboards, FinOps reports, portfolio review deck. |
| Stakeholder Communication Integrity | Accuracy, timeliness, and completeness of status/risk communication. | Status-report correction rate; missed escalation incidents; decision latency due to unclear reporting. | Who: EM, PM, Sponsor. What: weekly status reports, risk disclosures, decision logs. Where: leadership updates, program review notes, decision register. |

### R3 mandatory gate registry (`MG-01..MG-06`)

| Gate ID | Mandatory gate | Pass condition | Fail consequence |
| --- | --- | --- | --- |
| MG-01 | Test integrity gate | Unit/integration/regression suites pass on release candidate; no unresolved critical test failures. | Release blocked; affected quality rows capped at `50` until closure evidence exists. |
| MG-02 | Review and approval gate | Required reviewer quorum satisfied and approvals captured in immutable record. | Release blocked; quality-gate rows capped at `50`; escalation to R3 + R12. |
| MG-03 | Security and compliance gate | No unresolved high/critical security finding unless approved time-boxed exception exists. | Release blocked; security/compliance rows capped at `25`; tripwire review required. |
| MG-04 | Performance and reliability gate | Performance budgets and SLO pre-release checks pass with evidence attached. | Release blocked; reliability rows capped at `50` until replay confirms pass. |
| MG-05 | Rollback and recovery gate | Rollback rehearsal passed for scope with data/state changes. | Release blocked; operability rows capped at `25` until rehearsal passes. |
| MG-06 | Tripwire and contradiction gate | No active hard-fail tripwire; no unresolved critical contradiction at cutoff. | Overall status `FAIL`; arithmetic suppressed until closure evidence is accepted. |

## 3) Scoring anchors table (0/25/50/75/90/100)

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| Commitment Reliability | Commitments are made without capacity model; misses are routine and unexplained. | Commitments exist but are frequently redefined late; variance cause is undocumented. | Baselines exist; delivery is mixed; misses often identified too late for mitigation. | Most commitments are met; misses are pre-signaled with documented tradeoffs. | Commitments are consistently reliable; forecast error is low and explained with evidence. | Reliability remains high across volatile conditions using validated predictive controls. |
| Flow Health and WIP Control | No flow metrics; queue aging and blocking are unmanaged. | Metrics are reported but not used to change behavior. | WIP limits exist inconsistently; blocker aging remains high. | Flow controls are enforced; stale work and blocking are actively reduced. | Stable cycle-time bands with rapid blocker resolution and low queue age. | Flow is continuously optimized with proven throughput gains and no quality regression. |
| Scope Change Governance | Mid-cycle scope changes are ad hoc and unlogged. | Changes are logged inconsistently; tradeoffs rarely explicit. | Most changes are logged; interruption cost is weakly quantified. | Scope changes require explicit tradeoff and owner signoff. | Change control prevents churn; interrupts stay within declared budget. | Governance absorbs high-priority change without commitment instability. |
| Quality Gate Enforcement | Releases bypass mandatory gates with no traceable authority. | Gates exist but waivers are common and weakly justified. | Gates usually run; exceptions frequently discovered late. | Mandatory gates are enforced with valid waiver chain and documented risk. | Gate pass rate is high first-attempt; waiver usage is rare and defensible. | Gate system predicts failure early and prevents materially risky releases. |
| Defect Escape Control | Severe escapes are common; root causes are not closed. | Escape tracking exists but severity classification is inconsistent. | Escapes decline slowly; recurrence indicates partial fixes. | Severe escape trend is controlled with verified corrective actions. | Escapes are rare; reopen/regression rates are low and stable. | Preventive controls materially reduce defect injection quarter over quarter. |
| Reliability and SLO Stewardship | SLOs are absent or ignored; budget burn unmanaged. | SLOs defined but routinely breached without response discipline. | SLO reviews occur; breaches trigger inconsistent prioritization. | Error-budget policy drives tradeoffs and reliability work allocation. | SLO attainment is stable with low unplanned burn volatility. | Reliability remains within policy even under load/change spikes. |
| Incident Learning Closure | PIRs missing; the same incidents recur unaddressed. | PIRs produced late; actions are vague or ownerless. | PIR cadence exists; closure quality is inconsistent. | PIRs are on time; actions have owners, deadlines, and verification. | Recurrence is low due to high closure quality and evidence checks. | Incident learning system demonstrably prevents repeat failure classes. |
| Risk Escalation Timeliness | Risks are hidden until failure is unavoidable. | Risks are listed but escalated only after deadlines slip. | High risks usually escalated, but latency often exceeds policy. | Escalations are timely with clear impact and decision ask. | Early escalation consistently enables mitigation before breach. | Risk sensing is proactive, producing near-zero unanticipated critical breaches. |
| Cross-team Dependency Governance | External blockers are unmanaged and discovered late. | Dependencies tracked informally; accountability is unclear. | Dependencies mapped; missed SLAs are frequent and under-escalated. | Dependency owners, SLAs, and escalation paths are enforced. | Critical-path dependencies are resolved before blocking delivery. | Cross-team dependency system is predictive and resilient under contention. |
| Maintainability and Technical Debt Allocation | No debt plan; maintainability declines unchecked. | Debt backlog exists but receives negligible capacity. | Some debt work delivered; hotspots and aging continue to grow. | Debt allocation is protected; high-risk debt is retired on schedule. | Maintainability metrics improve with reduced rework and incident linkage. | Debt governance sustains long-term velocity and reliability without drift. |
| Staffing Capacity Adequacy | Staffing shortfalls are unmeasured; key work has no owners. | Basic headcount view exists; skill coverage gaps persist unaddressed. | Capacity model exists; corrective staffing actions are slow. | Capacity and skills are matched to roadmap with manageable gaps. | Critical ownership concentration is low; coverage remains robust. | Capacity planning anticipates demand shifts with minimal disruption. |
| Hiring and Onboarding Throughput | Roles remain open indefinitely; onboarding is unstructured. | Hiring funnel exists with chronic delays and weak quality control. | Time-to-fill improves, but onboarding-to-productivity is inconsistent. | Hiring and onboarding meet SLA for most roles. | High role-fill quality with fast, repeatable onboarding outcomes. | Recruiting/onboarding system reliably delivers high-performing hires at scale. |
| Performance Management and Coaching | Expectations unclear; poor performance is ignored. | Feedback is sporadic; documentation fails policy standards. | Process runs but differentiation and follow-through are uneven. | Goals, feedback, and corrective plans are timely and policy-compliant. | Coaching quality is high; performance issues are resolved quickly. | Team performance system produces sustained high capability and low regret attrition. |
| Security and Compliance Execution | Critical security/compliance obligations are missed. | Obligations known but frequently overdue; evidence incomplete. | Most obligations met; recurring overdue items persist. | Security and compliance SLAs are met with complete evidence packs. | Minimal overdue criticals; audit findings close without recurrence. | Controls are consistently ahead of SLA with strong independent audit confidence. |
| Cost and Productivity Stewardship | Spend overruns are unmanaged and unexplained. | Budget tracking exists; productivity/cost link is absent. | Variance controlled intermittently; unit economics unstable. | Spend stays within tolerance; productivity and cost are reviewed together. | Unit-cost trend improves while delivery quality is maintained. | Cost governance delivers sustained efficiency gains with no hidden risk transfer. |
| Stakeholder Communication Integrity | Status reporting is misleading or materially late. | Reports are frequent but omit key risks and assumptions. | Core updates are accurate; risk escalation is sometimes delayed. | Reporting is timely, complete, and decision-oriented. | Stakeholders receive early, evidence-backed risk and option framing. | Communication enables consistently fast, high-quality cross-functional decisions. |

## 4) Anti-gaming checks specific to Engineering Manager role

1. Commitment laundering check: compare locked sprint baseline to end-of-cycle scope; moved-out items count as misses unless approved exception exists pre-cutoff.
2. Story-splitting inflation check: recalculate delivery using normalized value units and acceptance criteria completion, not ticket count.
3. Severity laundering check: sample Sev2/Sev3 downgrades; require independent QA/SRE concurrence and incident evidence.
4. Waiver abuse check: all gate waivers require approver identity, risk statement, expiry, and mitigation owner; expired waivers auto-fail.
5. Backdated escalation check: reject risk entries created after breach timestamp as valid pre-escalation evidence.
6. Corrective-action theater check: closure requires measurable before/after metric change; checklist-only closure is invalid.
7. Dependency blame-shift check: blocked-day attribution must be jointly signed by both teams; unilateral attribution is inadmissible.
8. Meeting theater check: status claims without artifact link (dashboard, log, ticket, decision record) are scored as unsupported.

## 5) Tripwires and hard-fail conditions

### Tripwires (score caps and mandatory remediation)
| ID | Trigger | Detection method | Immediate effect | Control owner | Minimum recovery proof |
| --- | --- | --- | --- | --- | --- |
| R3-TW1 | Commitment instability: commitment hit rate <70% for two consecutive iterations. | Iteration commitment baseline vs delivery reconciliation audit. | Cap `Commitment Reliability` at `50`; mandatory recovery plan. | R3 + PM | Approved recovery plan and next-iteration stability improvement evidence. |
| R3-TW2 | Flow collapse: p85 cycle time worsens >30% over trailing 3 iterations without approved cause. | Flow telemetry trend audit with change log correlation. | Cap `Flow Health and WIP Control` at `50`. | R3 + Tech lead | Root-cause analysis and verified flow recovery trend. |
| R3-TW3 | Dependency stagnation: critical external dependency blocked >10 business days without escalation. | Dependency SLA log and escalation timestamp audit. | Cap `Cross-team Dependency Governance` at `50`. | R3 + counterpart owner | Escalation record and resolved dependency evidence. |
| R3-TW4 | Debt starvation: <10% capacity to reliability/debt for two consecutive quarters in high-incident system. | Capacity allocation audit and incident trend review. | Cap `Maintainability and Technical Debt Allocation` at `50`. | R3 + R2 | Updated allocation plan and evidence of executed debt work. |
| R3-TW5 | Coaching neglect: low-performance case without action plan within 30 days. | Performance case management audit. | Cap `Performance Management and Coaching` at `50`. | R3 + HR partner | Action plan and follow-up outcome evidence. |
| R3-TW6 | Any score `>90` missing same-iteration replay + adversarial challenge evidence. | High-anchor evidence audit. | Affected rows capped to `75`; if repeated (>3 rows), escalate to hard-fail review. | R3 + independent reviewer + R15 | Completed replay/challenge package and rescored output. |
| R3-TW7 | Mandatory anti-gaming suite skipped in iteration. | Anti-gaming execution ledger completeness check. | No score above `50` for affected scope; publication blocked until rerun. | R3 + R15 | Full anti-gaming rerun evidence and updated scoring packet. |

### Hard-fail conditions (iteration score forced to FAIL or INVALID)
| ID | Condition | Evidence test | Immediate effect | Control owner | Minimum recovery proof |
| --- | --- | --- | --- | --- | --- |
| R3-HF1 | Release executed with failed mandatory quality/security gate and no authorized waiver chain. | CI/CD gate logs + approval trail mismatch. | Immediate `FAIL`; release decision revoked. | R3 + R12 + R7 | Corrected gate execution and approved release decision reissue. |
| R3-HF2 | Critical risk withheld or materially misreported before milestone/release decision. | Timestamped status reports contradict risk register/incident data. | Immediate `FAIL`; decision packet invalidated. | R3 + R0 | Corrected risk disclosure package and signed escalation disposition. |
| R3-HF3 | Repeat Sev1 incident from previously identified unresolved root cause. | PIR history links repeat cause to unclosed action. | Immediate `FAIL`; remediation escalation mandatory. | R3 + Incident commander | Verified corrective closure and recurrence control validation. |
| R3-HF4 | Evidence tampering/backdating for commitments, risks, or controls. | Immutable log/audit trail conflict. | Iteration marked `INVALID`; forensic review required. | R3 + R15 | Forensic closure report and independent replay on clean evidence set. |
| R3-HF5 | Audit-critical security/compliance item overdue beyond policy grace without approved exception. | Security tracker and policy SLA breach. | Immediate `FAIL`; affected release path blocked. | R3 + Security lead | Approved exception or closed finding with verification evidence. |
| R3-HF6 | Post-snapshot rubric/process edit used in scoring without approved iteration reopen. | Snapshot hash diff and reopen ledger audit. | Iteration marked `INVALID`; full rescoring required. | R3 + R12 + R15 | Approved reopen record, impacted-row re-score log, and gate replay pass. |
| R3-HF7 | `RG1` critical-role set executed without `R3` included. | Gate-configuration audit against approved role set. | Iteration marked `INVALID`; publication blocked. | R3 + R0 + R15 | Corrected gate config and replay showing deterministic outcomes. |

## 6) Cross-role dependency and handoff criteria

| Counterpart role | Handoff from EM (what must be provided) | Acceptance criteria by counterpart | SLA / cadence | Escalation rule |
| --- | --- | --- | --- | --- |
| R1 Product Manager | Capacity-backed delivery plan, scope tradeoff memo, risk-adjusted dates | PM confirms priority alignment and acceptance criteria completeness | Weekly planning; release freeze -5 business days | If priority changes after freeze, escalate to sponsor within 1 business day |
| R2 Product Architect | Implementation sequencing, debt budget, architecture risk list | Architect confirms no unresolved critical design conflicts | Weekly design-risk review | Unresolved critical architecture risk >5 business days escalates to R0 |
| R4 Software Engineer | Clear ownership map, DoD, quality expectations, incident follow-ups | Engineers acknowledge ownership and test/observability obligations | Daily execution; weekly health check | Ownership gaps on tier-1 service escalate within 24 hours |
| R5 QA/Test Engineer | Release candidate readiness packet, test evidence links, known-risk statement | QA signs pass/fail disposition with residual risk statement | Per release + weekly quality sync | Missing critical test evidence blocks release automatically |
| R6 SRE/Platform Engineer | SLO change requests, reliability backlog priorities, runbook readiness | SRE accepts error-budget posture and operational readiness | Weekly reliability review | Error-budget breach unresolved in 48 hours escalates to R0/R12 |
| R7 Security Engineer | Remediation schedule, control implementation evidence, exception requests | Security validates SLA compliance and control sufficiency | Weekly vuln triage; monthly control review | Critical vuln overdue triggers release block and executive notice |
| R8 Privacy/Compliance/Legal | Data-handling decisions, exception requests, and control ownership for regulated flows | R8 confirms legal/privacy constraints are met or returns with explicit defect class and owner | At design freeze and pre-release | Any unresolved statutory/privacy conflict escalates to R0 within 24 hours |
| R12 DevOps/Release Manager | Release go/no-go decision pack, rollback plan, gate artifacts | Release manager verifies reproducible build and approval chain integrity | Per release window | Approval-chain gap stops release and opens incident review |
| R0 Executive Sponsor | Monthly engineering risk posture, forecast confidence, asks needing authority | Sponsor records explicit decision on tradeoffs beyond EM authority | Monthly business review | Unresolved high-impact risk >7 days escalates immediately |
| R15 Internal Audit/Assurance | Snapshot manifest, gate replay artifacts, contradiction log, and scored-row evidence index | R15 confirms reproducibility and returns explicit `accepted`/`returned` handoff state with defect metadata when needed | Per iteration close | Missing replay/admissibility evidence escalates immediately; publication blocked until resolved |

## 7) Cycle-level improvement checklist

Use once per delivery cycle (sprint or release train). All items require artifact links.

1. Record approved iteration snapshot by iteration day 1 with `rubric_snapshot_id` (`iteration_snapshot_id` alias), version, commit, hash, and cutoff.
2. Lock commitment baseline by iteration day 1; record assumptions and dependency owners.
3. Validate WIP limits and aging thresholds; publish current blocker top-5 with owners.
4. Run mid-iteration risk review; escalate any high risk with breach probability >30%.
5. Audit gate readiness 48 hours before release cut; resolve or formally waive all gaps.
6. Reconcile delivered vs committed scope; classify misses by controllable vs external cause.
7. Review incident and defect escapes; verify corrective actions with measurable outcome tests.
8. Confirm debt/reliability allocation met planned floor; if missed, schedule recovery allocation for next iteration.
9. Verify staffing/ownership coverage for tier-1 services and on-call fairness.
10. Publish stakeholder status report with evidence links and explicit unresolved decisions.
11. Perform anti-gaming sample audit on at least 15% of scored evidence rows.
12. Validate `RG1` critical-role set contains `R3` before gate execution and publication.
13. Audit all `>90` rows for same-iteration replay + adversarial challenge evidence.
14. If approved deltas occurred, re-score impacted rows and rerun precedence/gate replay before publication.
15. Close iteration with retrospective actions, owners, due dates, and verification metric per action.
16. Re-score all 16 sub-dimensions; apply tripwires/hard-fail logic before publishing iteration result.

---

## R4 Software Engineer

- source_file: `swarm_outputs/role_expansions/R4_software_engineer.md`
- words: 4214
- lines: 182

# R4 Software Engineer Rubric Expansion

## 1) Role mission and decision rights

### Role mission
R4 (Software Engineer) is accountable for turning approved requirements and architecture into production behavior that is correct, secure, observable, maintainable, and safe to change. R4 is scored on reproducible engineering outcomes, not narrative intent.

### Decision rights
| Decision area | R4 may decide | R4 must escalate | Audit evidence required |
| --- | --- | --- | --- |
| Implementation design | Internal algorithm, data structures, module layout, refactor shape | Any change that alters externally committed behavior, compliance scope, or architecture boundary | ADR/PR discussion, linked requirement IDs, reviewer sign-off |
| Test design | Test types, fixtures, assertion strategy, failure oracles | Any proposed gap for critical-path testing | Risk-to-test matrix, CI run artifacts |
| Error handling | Retry/backoff, timeout defaults, fallback path design | User-visible policy changes, legal/compliance exposure, irreversible side effects | Error policy doc, chaos/failure test evidence |
| Dependency usage | Version selection and non-critical library introduction | New critical dependency, license risk, unresolved high/critical CVE | Dependency review record, SBOM diff, security scan output |
| Performance tuning | Query/index strategy, caching strategy, code-path optimizations | Any optimization that weakens correctness/security/traceability controls | Before/after benchmark with guardrail checks |
| Release recommendation | Engineering go/no-go recommendation | Final release authorization, risk acceptance exceptions | Release checklist, tripwire status, owner sign-off |

## 2) Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| Requirements-to-Code Traceability | Every shipped behavior maps to an approved requirement and verification artifact. | Critical requirement trace coverage >= 98%; orphan behavior rate < 2%; reverse-trace sample pass rate >= 95%. | Who: feature engineer + reviewer. What: trace matrix with requirement IDs, PR IDs, test IDs. Where: repo docs folder + PR links + CI artifact store. |
| Functional Correctness | Business logic produces specified outputs for nominal and edge conditions. | Escaped Sev1/Sev2 functional defects per release; deterministic replay pass; boundary-case test pass rate. | Who: engineer + QA counterpart. What: defect reports, replay harness output, acceptance test logs. Where: issue tracker + CI runs + test report storage. |
| Modularity and Separation of Concerns | Code boundaries isolate responsibilities and prevent cross-layer leakage. | Static boundary rule violations; cyclic dependency count; module churn concentration trend. | Who: engineer + architect reviewer. What: architecture lint report, dependency graph diff, ADR reference. Where: CI static analysis + architecture docs. |
| Readability and Maintainability | Code is understandable, consistent, and safe for non-authors to modify. | Review rework ratio; time-to-first-correct-fix by non-author; lint/style debt trend. | Who: author + non-author maintainer. What: review logs, readability checklist, fix lead-time report. Where: PR system + engineering metrics dashboard. |
| Test Strategy by Risk | Test depth matches failure impact and likelihood. | Risk items with mapped automated tests >= 95%; critical-path mutation score threshold met; flaky rate < agreed cap. | Who: engineer + QA. What: risk-to-test matrix, mutation report, flake triage log. Where: test plan repo + CI quality dashboard. |
| Assertion and Oracle Quality | Tests verify correct semantics, not just execution. | Assertion density in critical tests; false-pass findings from seeded defects; oracle ambiguity defects. | Who: engineer + reviewer. What: seeded-defect experiment results, test code review checklist. Where: CI experiment job + PR comments. |
| Error Handling and Recovery Semantics | Failures are explicit, bounded, and recoverable without silent corruption. | Unhandled exception rate; timeout/backoff policy coverage; recovery path integration test pass. | Who: engineer + SRE reviewer. What: failure-mode test results, exception classification logs. Where: CI failure tests + runtime logs dashboard. |
| Defensive Input and State Validation | Invalid input/state is rejected or normalized safely at trust boundaries. | Input validation coverage at API boundaries; invalid-input fuzz pass rate; invariant breach count. | Who: engineer + security reviewer. What: fuzz report, invariant check logs, validation checklist. Where: security CI job + service telemetry store. |
| Performance Budget Compliance | Service behavior stays within agreed latency/throughput SLO budgets. | p95/p99 latency vs budget; throughput under expected load; regression delta against baseline. | Who: engineer + perf owner. What: benchmark suite output, load-test report, budget exception records. Where: perf pipeline + observability dashboard. |
| Resource Efficiency | Compute, memory, I/O, and storage usage are efficient for expected workload and cost profile. | CPU/memory per request; DB query efficiency; cost per transaction trend. | Who: engineer + platform/FinOps partner. What: profiler snapshots, query plans, unit cost report. Where: profiler artifacts + DB telemetry + cost dashboard. |
| Secure Coding Hygiene | Code enforces authz, input safety, secret handling, and secure defaults. | Open high/critical code-level findings count; policy-as-code pass rate; secret leak incidents. | Who: engineer + security engineer. What: SAST/DAST results, secret scan output, fix verification evidence. Where: security pipeline + vuln tracker. |
| Dependency and Supply-Chain Hygiene | Third-party components are versioned, reviewed, and policy compliant. | SBOM freshness; time-to-remediate high CVEs; unsigned artifact rate. | Who: engineer + security/release manager. What: SBOM, dependency diff approvals, signature verification log. Where: artifact registry + dependency management system. |
| Observability Coverage | Code emits actionable logs/metrics/traces for critical paths and failure states. | Critical-path telemetry coverage >= 95%; alert precision/recall; missing-signal incidents. | Who: engineer + SRE. What: instrumentation map, alert test results, trace coverage report. Where: observability repo + monitoring system. |
| Runtime Diagnostics and Operability Hooks | Operators can diagnose and mitigate incidents quickly using built-in diagnostics. | Mean time to isolate fault in game days; availability of correlation IDs; health endpoint fidelity. | Who: engineer + on-call owner. What: incident drill reports, runbook-linked diagnostic outputs. Where: incident platform + runbook repository. |
| Data Integrity and Migration Safety | Data changes preserve correctness, lineage, and rollback safety. | Migration dry-run success; checksum/reconciliation pass; rollback rehearsal success rate. | Who: engineer + DBA/data engineer. What: migration plan, reconciliation report, rollback evidence. Where: migration repo + database ops logs. |
| CI/CD Change Safety | Changes are merged and released through enforced gates with rollback readiness. | Gate bypass count (target 0); change failure rate; rollback success time. | Who: engineer + release manager. What: pipeline audit logs, deployment records, rollback drill output. Where: CI/CD platform + release tracker. |
| Code Review Rigor | Reviews detect defects and enforce standards before merge. | Critical defect catch rate in review; review depth checklist completion; rubber-stamp rate. | Who: author + qualified reviewer. What: PR review transcript, checklist, sampled audit outcomes. Where: code hosting platform + engineering audit log. |
| Documentation and Knowledge Continuity | Implementation intent and operational behavior remain understandable beyond original author. | ADR/runbook freshness; onboarding task completion by non-author; stale-doc defect count. | Who: engineer + team lead. What: ADR updates, runbook revision history, onboarding verification notes. Where: docs repository + team wiki + onboarding tracker. |

## 3) Scoring anchors table (0/25/50/75/90/100)

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| Requirements-to-Code Traceability | Critical behavior cannot be traced; evidence missing or fabricated. | Partial trace exists; large critical gaps or stale mappings. | Most critical items traced, but test linkage or freshness inconsistent. | Critical scope trace complete; independent sample finds only minor issues. | Automated trace checks block drift; independent audit passes with no critical gaps. | Two consecutive cycles with full trace integrity and zero unresolved critical trace defects. |
| Functional Correctness | Core flows fail reproducibly; Sev1 defects open in release candidate. | Frequent logic defects; edge behavior undefined in multiple critical paths. | Nominal behavior stable, but boundary correctness still causes recurring Sev2 issues. | Critical flows correct with broad edge-case coverage and controlled defect escape. | Adversarial replay and seeded tests show high detection and near-zero serious escapes. | Two cycles with zero Sev1/Sev2 escaped functional defects in owned scope. |
| Modularity and Separation of Concerns | Architecture boundaries ignored; high coupling blocks safe change. | Repeated boundary violations and circular dependencies with weak remediation. | Basic separation present, but hotspots repeatedly violate layer rules. | Boundaries largely enforced; violations are rare and corrected quickly. | Automated boundary checks with policy gating; no unresolved critical violations. | Two cycles with zero unauthorized cross-layer access in critical components. |
| Readability and Maintainability | Code is opaque, inconsistent, and effectively single-author maintainable. | Reviews repeatedly flag readability issues; changes risky for non-authors. | Style consistent in most areas, but complexity hotspots remain unaddressed. | Most modules understandable by peers; non-author fixes succeed without major rework. | Maintainability metrics trend positive; review rework and comprehension defects are low. | Two cycles where non-authors deliver correct fixes quickly across critical modules. |
| Test Strategy by Risk | Critical risks untested or tested only manually. | Happy-path automation exists; risk-based depth absent for major failure modes. | Risk mapping partial; some critical areas lack robust automation or flaky tests. | Risk-driven coverage complete for critical paths; flake rate controlled. | Mutation and adversarial tests demonstrate strong detection power across high-risk areas. | Two cycles with no critical risk class lacking deterministic automated tests. |
| Assertion and Oracle Quality | Tests mostly check status codes/execution; defects pass unnoticed. | Assertions weak or ambiguous in many critical tests. | Reasonable assertions in main flows, but semantic oracles missing for complex logic. | Strong assertions for critical paths; seeded defects usually caught. | Oracle quality proven by repeated seeded-defect detection and low false-pass rate. | Two cycles with seeded critical defects consistently detected before merge. |
| Error Handling and Recovery Semantics | Failures crash services or silently corrupt outcomes. | Error paths inconsistent; retries/timeouts unsafe or unbounded. | Basic handling in place; some recovery paths undocumented or untested. | Failures are explicit and bounded; recovery behavior tested for critical dependencies. | Fault-injection evidence shows graceful degradation and deterministic recovery. | Two cycles with no Sev1 incident caused by unhandled/unsafe error path in owned code. |
| Defensive Input and State Validation | Trust boundaries accept malformed input without controls. | Validation exists in scattered points; bypasses common. | Most boundaries validated, but invariant checks incomplete for sensitive state. | Consistent validation and invariant enforcement on critical boundaries. | Fuzz and adversarial input tests pass with no critical bypasses. | Two cycles with zero critical validation bypasses and verified invariant coverage. |
| Performance Budget Compliance | Latency/throughput budgets materially violated with no containment. | Frequent regressions; performance testing absent on critical paths. | Budgets usually met but periodic regressions recur in peak scenarios. | Budgets met for normal and expected peak loads; regressions caught pre-release. | Continuous performance gates and benchmark baselines prevent material drift. | Two cycles with no material budget breach in owned services under agreed workloads. |
| Resource Efficiency | Resource usage is wasteful and causes capacity/cost instability. | High CPU/memory/I/O overhead known but not prioritized. | Major inefficiencies identified; only partial remediation delivered. | Resource profile stable and acceptable for target workload/cost envelope. | Profiling-informed improvements reduce cost/unit while preserving quality constraints. | Two cycles of sustained efficient resource usage with no uncontrolled cost spike from owned changes. |
| Secure Coding Hygiene | Exploitable high/critical code vulnerabilities remain unresolved. | Multiple serious findings recur; security controls inconsistently applied. | Core controls present but residual high findings or weak remediation timeliness. | No unresolved critical findings; high findings remediated within policy SLA. | Security tests integrated into CI with low recurrence and verified fixes. | Two cycles with zero unresolved high/critical code-level findings in owned scope. |
| Dependency and Supply-Chain Hygiene | Unreviewed or tampered dependencies/artifacts in release path. | Dependency inventory incomplete; critical CVEs linger beyond SLA. | SBOM present, but remediation and signature enforcement inconsistent. | Dependency and artifact controls enforced with timely remediation. | Signed artifacts, current SBOM, and policy gating block risky components. | Two cycles with zero policy violations and zero overdue high/critical dependency CVEs. |
| Observability Coverage | Critical failures cannot be detected from telemetry. | Basic logs exist; missing metrics/traces for key transactions. | Most critical flows instrumented, but blind spots remain in failure states. | Instrumentation covers critical flows and major fault modes; alerts actionable. | Telemetry quality verified by drills; low false-positive and false-negative alert rates. | Two cycles where all Sev1/Sev2 incidents had sufficient first-hour telemetry for diagnosis. |
| Runtime Diagnostics and Operability Hooks | On-call cannot isolate faults without ad hoc code changes. | Diagnostics incomplete; correlation and debug context often missing. | Standard hooks exist, but incident drills show inconsistent usefulness. | Operators can isolate most critical faults quickly using built-in diagnostics. | Game-day evidence shows fast fault isolation and safe mitigation using existing hooks. | Two cycles with no Sev1 incident extended by missing diagnostics in owned components. |
| Data Integrity and Migration Safety | Data corruption or irreversible migration failure occurs. | Migration process ad hoc; rollback/reconciliation largely untested. | Migration controls partially implemented; reconciliation gaps remain. | Migrations rehearsed with rollback and reconciliation for critical datasets. | Integrity checks and staged rollouts prevent corruption and enable confident rollback. | Two cycles with zero integrity incidents from schema/data changes in owned scope. |
| CI/CD Change Safety | Mandatory gates bypassed or unverifiable deployment path used. | Gate coverage weak; rollbacks unreliable; frequent failed changes. | Standard pipeline present, but exceptions and manual steps cause avoidable risk. | Enforced gates with tested rollback for critical services. | Change safety metrics stable; near-zero unauthorized exceptions; fast rollback validation. | Two cycles with zero unauthorized gate bypass and consistent successful rollback drills. |
| Code Review Rigor | Reviews are absent or perfunctory; defects regularly merge unchecked. | Reviews occur but quality inconsistent; checklist rarely enforced. | Reviews catch common issues, but critical logic/security defects still slip. | Structured, accountable reviews catch most serious issues pre-merge. | Review effectiveness measured and improved through sampled audits and feedback loops. | Two cycles with high critical-defect catch rate and low rubber-stamp incidence. |
| Documentation and Knowledge Continuity | No reliable docs/runbooks; ownership knowledge trapped in one person. | Docs stale or incomplete for critical components. | Basic documentation exists but frequently lags implementation changes. | Docs and runbooks current for critical systems; non-author onboarding is viable. | Documentation quality validated through drills and onboarding evidence. | Two cycles where non-authors independently handle incidents/changes using current docs. |

## 4) Anti-gaming checks specific to Software Engineer role

1. Reverse-trace audit: sample 15% of production behaviors and require mapping back to requirement, code, test, and approving review; any broken chain voids that row score.
2. Hidden defect seeding: inject controlled defects in staging branches; if tests fail to detect, cap related test sub-dimension at 50.
3. Replay challenge: independent reviewer reruns benchmark and critical tests from raw commit hash; screenshot summaries are inadmissible without raw artifacts.
4. Post-hoc approval detection: any ADR/review/exception created after merge timestamp is marked non-compliant for that cycle unless pre-approved emergency protocol exists.
5. Suppression audit: inspect linter/security/test exclusions; exclusions without dated rationale and owner sign-off are treated as failed controls.
6. Metric inflation check: reject superficial test additions that do not increase risk coverage or oracle quality.
7. Incident-memory check: compare incident causes against prior “fixed” claims; repeated class without systemic correction triggers scoring cap.
8. Ownership laundering check: “shared ownership” claims are invalid unless one accountable engineer is named per critical change.
9. Flake masking check: quarantine is allowed only with linked root-cause ticket and due date; indefinite quarantine is scored as missing verification.
10. Branch hygiene check: force-push rewrites that remove failed test history from reviewed branches invalidate evidence for that change set.

## 5) Tripwires and hard-fail conditions

| ID | Hard-fail condition | Immediate scoring consequence | Minimum closure evidence |
| --- | --- | --- | --- |
| HF-1 | Confirmed evidence fabrication or tampering in code/test/review artifacts | Overall R4 score = 0 for cycle | Forensic report, corrected evidence chain, governance approval to resume scoring |
| HF-2 | Release includes unresolved exploitable high/critical vulnerability in owned code path without approved exception | Overall cap = 25 and release recommendation = fail | Verified fix in production candidate, retest evidence, security sign-off |
| HF-3 | Critical behavior in production has no requirement and test lineage | Traceability and correctness rows = 0; overall cap = 50 | Completed trace chain, independent audit pass |
| HF-4 | Mandatory CI/CD gate bypassed for production deployment without emergency protocol | Change-safety row = 0; overall cap = 50 | Incident record, approved emergency waiver, preventive control added |
| HF-5 | Irreversible data corruption caused by migration/change in owned component | Data-integrity row = 0; overall cap = 25 | RCA, restore/reconciliation proof, migration guardrails added |
| HF-6 | Sev1 incident prolonged due to absent telemetry/diagnostics in owned critical path | Observability/diagnostics rows capped at 25 | Added instrumentation, validated drill, SRE sign-off |
| HF-7 | Repeated critical defect class escapes in two consecutive releases with no systemic corrective action | Correctness/testing rows capped at 50 | Systemic fix plan executed and verified over one clean release |

## 6) Cross-role dependency and handoff criteria

| Counterpart role | Handoff trigger | R4 must provide | Counterpart acceptance criteria | Escalation SLA |
| --- | --- | --- | --- | --- |
| R1 Product Manager | Requirement ambiguity or acceptance mismatch | Concrete scenario list, impacted code paths, proposed interpretation, risk statement | Written acceptance criteria update or explicit deferral decision | 2 business days |
| R2 Architect | Boundary exception, major refactor, or NFR conflict | ADR draft, boundary impact diff, fitness-test results | Approved ADR/exception with expiration and owner | Before merge to default branch |
| R5 QA/Test Engineer | Critical risk mapping and release test readiness | Risk-to-test matrix, oracle definitions, known limits | Critical risk coverage confirmed; unresolved high-risk gaps explicitly waived by authority | Before release candidate cut |
| R6 SRE/Platform | New service behavior, scaling change, or incident-prone component | SLO impact note, observability map, rollback steps, runbook updates | On-call readiness confirmed; alert/runbook validation completed | 24 hours before prod rollout |
| R7 Security Engineer | New trust boundary, authz change, dependency risk | Threat delta summary, control implementation evidence, scan outputs | No unresolved blocking findings or approved exception recorded | Before merge for internet-facing changes |
| R8 Privacy/Compliance | Data collection, retention, deletion, or residency logic changes | Data-flow delta, field classification, retention/deletion tests | Control mapping approved and auditable | Before release for regulated data changes |
| R12 Release Manager | Go/no-go decision point | Tripwire status, gate report, rollback rehearsal evidence | All mandatory gates pass and unresolved risks explicitly accepted by authority | At go/no-go meeting |
| R13 Operations/Support | Incident handoff and recurring ticket class | Reproducer, fix diff, diagnostic guidance, KB update | Reproducer closed and support playbook updated | 1 business day after fix merge |
| R15 Internal Audit/Assurance | Audit sampling, score challenge, or high-anchor verification request | Replay-ready evidence pack (who/what/where/time/version/hash), gate-state logs, and change-control trace | R15 can independently reproduce sampled claims and gate outcomes; explicit `accepted`/`returned` result captured | 3 business days or before release cutoff, whichever is sooner |

## 7) Cycle-level improvement checklist

### Planning (before implementation)
- [ ] Confirm requirement IDs, acceptance criteria, and non-functional budgets are explicit and testable.
- [ ] Identify top failure modes (correctness, security, reliability, data) and map tests before coding.
- [ ] Define observability changes (logs/metrics/traces) required for new/changed critical paths.
- [ ] Validate dependency impact (license, CVE posture, maintenance risk) for any new package.

### Build and review (during implementation)
- [ ] Keep each PR traceable: requirement ID, risk note, test evidence, rollback note.
- [ ] Enforce boundary and static checks; do not merge with unresolved blocking findings.
- [ ] Include adversarial and negative tests for trust boundaries and high-impact logic.
- [ ] Update ADR/runbook/docs in the same change when behavior or operation changes.

### Pre-release (before production)
- [ ] Verify all mandatory CI/CD gates (`MG-01..MG-06`) passed without unauthorized bypass.
- [ ] Run performance regression suite against agreed budgets and record deltas.
- [ ] Execute migration dry-run, reconciliation checks, and rollback rehearsal when data changes exist.
- [ ] Confirm security scan closure for high/critical findings or formal, time-boxed exception.
- [ ] Recheck tripwire table and contradiction register; any active hard-fail condition blocks R3 go recommendation.

### Post-release (learning and correction)
- [ ] Compare incidents/defects against pre-release risks; log misses and control gaps.
- [ ] Close corrective actions with objective evidence, owner, and due date.
- [ ] Audit one random shipped feature end-to-end (requirement -> code -> test -> telemetry -> support).
- [ ] Track trend metrics per sub-dimension and prioritize next-cycle engineering debt accordingly.

## 8) Iteration snapshot governance and deterministic rescore controls

These controls are mandatory and override weaker language elsewhere in this file.

### 8.1 Non-zero admissibility contract (row level)

| Field | Required value for any non-zero row | Rejection rule |
| --- | --- | --- |
| `who` | Named scorer and independent reviewer IDs | Missing field sets row anchor to `0` |
| `what` | Concrete artifact IDs (requirement, PR, test run, incident, or benchmark IDs) | Missing field sets row anchor to `0` |
| `where` | Immutable artifact location (repo path, CI job URL, ticket URL, log index) | Missing field sets row anchor to `0` |
| `time` | Evidence capture timestamp and scoring timestamp in UTC | Missing field sets row anchor to `0` |
| `version` | Rubric revision tag and service/build version under test | Missing field sets row anchor to `0` |
| `hash` | SHA-256 (or signed digest) for the primary evidence bundle | Missing field sets row anchor to `0` |

Sampling rule: if missing-field defects exceed 5% of sampled non-zero rows, publication is blocked and R4 is marked `FAIL` for the iteration snapshot.

### 8.2 Iteration snapshot lock and approved reopen protocol

| Control | Mandatory record | Verification | Consequence if violated |
| --- | --- | --- | --- |
| Snapshot lock before scoring | `iteration_id`, `snapshot_id`, rubric file hash, anchor table hash, denominator hash, cutoff timestamp, approvers (`R4`,`R1`,`R15`) | Hash check at scoring start and pre-publication | Unlocked scoring is invalid |
| Approved reopen for rubric edits | Change ticket with reason, impacted row IDs, approvers, reopen timestamp | Change log diff must match approved ticket scope | Out-of-scope edits invalidate scores produced after edit |
| Unauthorized in-iteration change detection | Diff against locked snapshot hashes | Automated hash verification on each scoring run | Publication blocked; full impacted-row rescore required |

### 8.3 Deterministic precedence and contradiction truth table

| Precedence rank | Condition | Deterministic outcome |
| --- | --- | --- |
| 1 | Any hard-fail condition active | R4 verdict = `FAIL`; no arithmetic override allowed |
| 2 | Severity-1 contradiction unresolved past SLA | Publication blocked; rows in affected scope set to `0` until closure |
| 3 | Mandatory anti-gaming control skipped | Affected scope capped at `50`; unresolved at publication => `FAIL` |
| 4 | High-anchor proof missing (`90`/`100`) | Row capped at `75` (missing independence) or `50` (missing replay/challenge) |
| 5 | No blocking condition active | Compute weighted score from admissible rows only |

### 8.4 Mandatory anti-gaming execution set and tripwires

Required controls per iteration snapshot: reverse-trace audit, hidden-defect seeding, non-author replay, post-hoc approval detection, suppression audit, metric inflation check, branch-history integrity check.

| ID | Trigger | Immediate effect | Recovery proof |
| --- | --- | --- | --- |
| `R4-ITW-01` | Any mandatory anti-gaming control not executed | All affected rows capped at `50`; publication blocked | Missing control run evidence + rescored impacted rows |
| `R4-ITW-02` | Same person authored evidence and approved a `90` or `100` row | Affected row downgraded to `50` | Independent re-review and replay transcript |
| `R4-ITW-03` | Dual-calculator final totals do not match exactly | Determinism failure; iteration snapshot invalid for R4 | Corrected arithmetic spec and parity pass logs |

### 8.5 Delta re-evaluation, replay, and high-anchor challenge

| Control | Minimum requirement | Block condition |
| --- | --- | --- |
| Impacted-row map | Every approved rubric delta must list impacted row IDs, expected anchor movement, and gate impact | Missing impacted-row map blocks publication |
| Targeted rescore | 100% of impacted rows must be rescored on the new snapshot hash | Any impacted row not rescored blocks publication |
| Replay coverage | Non-author replay on `>=20%` of R4 rows and all gate-sensitive rows | Coverage miss invalidates high-anchor rows |
| High-anchor challenge gate | Any row scored `100` requires same-iteration adversarial challenge plus replay parity | Missing challenge proof caps row at `50` |
| Aggregate parity | Two independent calculators must produce identical row anchors and identical final role score | Any mismatch marks iteration snapshot `FAIL` for R4 |

---

## R5 QA / Test Engineer

- source_file: `swarm_outputs/role_expansions/R5_qa_test_engineer.md`
- words: 4530
- lines: 190

# R5 QA / Test Engineer Rubric Expansion

## 1) Role mission and decision rights
R5 owns empirical release confidence. The role validates whether shipped behavior matches approved requirements, declared risk tolerance, and non-functional commitments. R5 treats all quality claims as unproven until verified by reproducible tests with falsifiable oracles and tamper-evident evidence.

R5 has binding authority to block release when tripwires are triggered, evidence is incomplete, or critical risk is untested. R5 does not approve business priority, architecture direction, or staffing plans, but can require testability, observability, and evidence conditions before sign-off.

| Decision right | R5 authority boundary | Mandatory evidence before decision | Override path |
|---|---|---|---|
| Test strategy approval | Approve or reject strategy for critical flows, abuse cases, and NFRs | Versioned test strategy, risk map, requirement baseline, gap list | Program risk board with written residual-risk acceptance and expiry date |
| Release quality gate | Approve/hold release based on objective gate outcomes | CI gate report, defect snapshot, waiver ledger, evidence manifest | Executive risk board only; no single-role override |
| Defect severity calibration | Final severity call for disputed Sev1/Sev2 defects | Impact proof (user/business/security), repro steps, logs, RCA draft | Cross-functional incident council with written rationale |
| Evidence admissibility | Accept/reject evidence used for scores above 75 | Raw logs, immutable timestamps, artifact hashes, replay instructions | Internal audit plus QA lead joint approval |
| Waiver recommendation | Recommend conditional waiver with mitigation plan | Time-boxed waiver, owner, rollback trigger, closure criteria | Product owner and risk owner co-sign; QA cannot self-approve |
| Regression scope sufficiency | Require additional regression before go-live | Change-impact map, touched components, historical escape map | Engineering manager + release manager + risk owner |
| Post-release quality reopening | Reopen release decision on new severe evidence | Incident timeline, failed controls, reproduction in production-like env | Same authority that approved original release |

## 2) Sub-dimensions table
| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where) |
|---|---|---|---|
| 1. Risk-Coverage Strategy Completeness | Test plan covers highest-impact failure modes first and is updated when risk profile changes. | Critical risk-to-test mapping rate; update latency after requirement/architecture change; uncovered Sev1 risk count. | Who: QA Lead, Product Manager, Architect. What: risk register, risk-to-test matrix, residual risk sign-off. Where: repo `qa/risk/`, issue board `QA-RISK`, release folder `evidence/r5/`. |
| 2. Requirement-to-Test Traceability Integrity | Every normative requirement is mapped bidirectionally to executable tests and release evidence. | Traceability coverage; broken link count; critical requirement positive/negative/error-path coverage. | Who: QA Lead, Product Owner, Engineering Lead. What: requirement catalog, trace matrix export, test run report with requirement IDs. Where: `qa/traceability/`, requirements system, CI artifacts for release branch. |
| 3. Acceptance Criteria Testability Gate | Acceptance criteria are measurable, unambiguous, and machine-verifiable for critical scope. | Percent of criteria with numeric/binary pass conditions; ambiguity rate; contradiction backlog age. | Who: QA, Product, Business Analyst. What: acceptance criteria ledger, ambiguity lint report, contradiction tickets. Where: `product/acceptance/`, `qa/lint/`, tracker `QA-CONTRA`. |
| 4. Oracle Precision and Falsifiability | Tests use explicit expected outcomes that can fail objectively and detect wrong behavior. | Deterministic oracle ratio; tolerance-band violations; seeded defect detection rate. | Who: QA, domain SME, engineering reviewer. What: oracle catalog, expected-value source, seeded-defect results. Where: `qa/oracles/`, `qa/mutation/`, CI test artifacts. |
| 5. Negative, Boundary, and State Transition Coverage | Test design covers invalid input, limits, state-machine transitions, and failure paths. | Coverage of boundary classes; negative test execution rate; state transition matrix completeness. | Who: QA engineer, component owner. What: test design spec, boundary matrix, transition test results. Where: `qa/design/`, `qa/cases/`, CI reports for integration suite. |
| 6. Test Data Fidelity and Compliance | Test data reflects production-relevant distributions without violating privacy/compliance controls. | Dataset freshness age; masked/synthetic data coverage; data policy violations. | Who: QA data owner, privacy officer, data engineer. What: test data catalog, masking evidence, refresh logs. Where: `qa/test-data/`, privacy control repository, pipeline logs. |
| 7. Environment Parity and Deterministic Reproducibility | Test outcomes are repeatable across controlled environments with known configuration parity. | Infra parity drift score; cold-start replay success rate; env bootstrap time. | Who: QA, platform engineer, release manager. What: environment manifests, IaC revision, replay outcomes. Where: `infra/test-env/`, `qa/replay/`, CI environment metadata. |
| 8. Automation Stability and Flake Control | Automated tests provide reliable signal and flake is measured, triaged, and reduced. | 30-day flake rate; muted/quarantined test count; retry masking incidents. | Who: QA automation owner, engineering manager. What: flake dashboard export, quarantine log, retry policy audit. Where: `qa/automation/metrics/`, CI analytics, tracker `QA-FLAKE`. |
| 9. CI/CD Quality Gate Enforcement | Merge and release gates enforce mandatory test/security/performance checks without silent bypass. | Unauthorized bypass count; gate pass/fail integrity; failed-critical-test merge attempts blocked. | Who: QA lead, DevOps lead, release manager. What: gate policy, branch protection config, gate audit log. Where: CI config repo, release governance log, protected branch settings export. |
| 10. Non-Functional Performance and Capacity Verification | Performance, scalability, and resource behavior are proven for real workloads and stress conditions. | P95/P99 latency compliance; peak-load pass rate; saturation and backpressure test coverage. | Who: QA performance engineer, SRE, architect. What: workload model, benchmark raw telemetry, pass/fail assertions. Where: `qa/perf/`, observability platform export, load-test pipeline artifacts. |
| 11. Security, Privacy, and Abuse Verification Depth | Threat and misuse paths are tested beyond scanner checks, including privacy control behavior. | Threat-model scenario coverage; unresolved critical findings; abuse-path detection rate. | Who: QA security tester, security engineer, privacy lead. What: abuse-case suite, pentest findings, remediation verification. Where: `qa/security/`, vuln tracker, privacy evidence pack. |
| 12. Reliability, Failover, and Recovery Validation | Service behavior under dependency failure, failover, backup/restore, and degraded mode is verified. | Fault-injection coverage; restore success; measured RTO/RPO adherence; data integrity checks. | Who: QA reliability owner, SRE, platform team. What: drill run logs, recovery verification, integrity check report. Where: `qa/resilience/`, DR drill records, incident simulation logs. |
| 13. Defect Severity Calibration and Triage Discipline | Defects are classified by objective impact and closed with reproducible verification and RCA. | Severity misclassification rate; Sev1/Sev2 RCA completion; reopen rate after close. | Who: QA triage lead, engineering lead, support lead. What: defect register, severity rationale, closure evidence with retest. Where: tracker `QA-DEFECT`, RCA repository, release notes. |
| 14. Regression Impact Analysis and Suite Freshness | Regression scope is selected from actual change impact and suites are kept current and relevant. | Changed-component regression coverage; stale-test ratio; escaped-regression recurrence. | Who: QA lead, module owners, release manager. What: change-impact map, regression suite index, stale-test cleanup log. Where: `qa/regression/`, code diff reports, CI trend history. |
| 15. Evidence Integrity and Independent Replayability | Quality claims are supported by immutable artifacts that independent reviewers can replay. | Evidence completeness ratio; hash verification pass rate; independent replay success rate. | Who: QA evidence owner, internal audit, independent reviewer. What: evidence manifest, signed hashes, replay transcript. Where: immutable artifact store, `qa/evidence/`, audit archive. |
| 16. Escaped Defect Detection and Feedback Closure | Production escapes are detected quickly and translated into preventive tests and controls. | Sev1/Sev2 escape MTTD; % escapes mapped to new tests; recurrence by defect family. | Who: QA lead, SRE incident lead, support manager. What: escape ledger, postmortem actions, new-test linkage report. Where: incident tracker, `qa/escape-analysis/`, monitoring alert history. |
| 17. Accessibility and Cross-Platform Verification | Critical workflows are validated for accessibility and consistent behavior across supported platforms. | WCAG critical-check pass rate; browser/device matrix coverage; assistive-tech defect backlog age. | Who: QA accessibility owner, UX lead, frontend lead. What: accessibility test runs, manual AT checks, platform matrix results. Where: `qa/accessibility/`, visual regression store, browser farm artifacts. |
| 18. Waiver Governance and Residual Risk Accounting | Exceptions are explicit, temporary, and tied to accountable mitigation with expiry enforcement. | Overdue waiver count; waivers without mitigation tasks; expired-waiver release attempts. | Who: QA lead, product owner, risk owner. What: waiver ledger, mitigation tickets, closure attestations. Where: release governance board records, `qa/waivers/`, risk register. |

## 3) Scoring anchors table (0/25/50/75/90/100) for every sub-dimension
| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
|---|---|---|---|---|---|---|
| 1. Risk-Coverage Strategy Completeness | No risk-to-test mapping; critical risks unknown. | Static risk list exists; mapped critical risks <60%. | Critical risks partially mapped (60-84%); updates lag major changes. | Critical risks mapped >=95%; strategy updated within 5 business days of major change. | Critical risks mapped >=98%; independent audit finds zero missing Sev1 risk scenarios. | Two consecutive cycles with 100% critical risk mapping and zero Sev1 escapes from unmapped risk. |
| 2. Requirement-to-Test Traceability Integrity | Critical requirements untraced or no canonical requirement baseline. | Trace matrix exists but coverage <60% or one-way links only. | Coverage 60-84%; critical requirements missing negative/error-path tests. | Coverage >=95% with bidirectional links; all critical requirements have positive and negative tests. | Coverage >=99%; automated validator reports zero broken critical links in release branch. | 100% bidirectional traceability; independent replay confirms every critical test links to requirement and release artifact. |
| 3. Acceptance Criteria Testability Gate | Acceptance criteria absent or subjective ("fast", "easy", "good"). | <50% criteria measurable; ambiguity unresolved near release. | 50-79% measurable; numeric tolerance missing for several critical criteria. | >=95% measurable criteria with explicit bounds and fail conditions for critical scope. | 100% measurable; contradiction backlog for critical criteria is zero before gate decision. | Two cycles with fully machine-assertable critical criteria and zero escaped ambiguity defects. |
| 4. Oracle Precision and Falsifiability | Pass/fail based on human interpretation only. | Expected outcomes partially documented; inconsistent oracle sources. | Deterministic oracles for most nominal paths; tolerance bands too broad on some critical checks. | Deterministic, falsifiable oracles for all critical scenarios; oracle sources versioned. | Seeded defect and mutation runs show >=80% detection on critical components. | Dual independent oracle derivation matches expected outcomes and mutation kill >=90% for two cycles. |
| 5. Negative, Boundary, and State Transition Coverage | Only happy-path tests exist. | Negative/boundary coverage <30%; state transitions mostly untested. | Boundary and negative tests exist for core APIs only. | >=95% critical workflow coverage across negative, boundary, and state-transition scenarios. | Includes combinatorial and concurrency edge tests; no unresolved critical edge-case defects. | Two cycles with zero Sev1/Sev2 escapes attributable to missing edge/state coverage. |
| 6. Test Data Fidelity and Compliance | Uncontrolled or prohibited production data used in testing. | Synthetic/masked data coverage <50%; data ownership unclear. | Controlled datasets for nominal flows; edge distributions and privacy controls incomplete. | Data catalog complete for critical suites; masking/minimization controls enforced and audited. | Automated drift and policy checks on every critical pipeline run; zero unresolved policy violations. | Independent privacy/compliance audit passes for two cycles; deterministic replay datasets retained for critical flows. |
| 7. Environment Parity and Deterministic Reproducibility | Test results depend on undocumented local setup. | Environment documented but drift high; reproducibility unreliable. | Reproducible setup in one environment only; parity gaps remain. | IaC-managed parity across test and staging; cold-start reproduction works for critical suites. | Cross-environment replay produces equivalent results within declared tolerance. | Two cycles of non-author cold-start replay with zero critical environment drift incidents. |
| 8. Automation Stability and Flake Control | Automation absent or nonfunctional for release scope. | Flake rate >15% and retries routinely mask first-fail outcomes. | Flake rate 5-15%; quarantine process exists but backlog persists. | Flake rate <=3% (30-day rolling); quarantine entries have owners and due dates. | Flake rate <=1%; first-failure retention and triage SLA consistently met. | Two cycles with flake <=0.5% and zero muted failing critical tests at release gate. |
| 9. CI/CD Quality Gate Enforcement | Critical failures do not block merge/release. | Gate exists but bypasses are frequent or undocumented. | Mandatory gates active, but >5% of releases use exception path with weak controls. | Mandatory gates enforced with zero unauthorized bypass in cycle. | Gate decisions are immutable, fully attributable, and independently auditable. | Two cycles of zero unauthorized bypass and zero Sev1 post-release defects linked to gate omission. |
| 10. Non-Functional Performance and Capacity Verification | No repeatable performance or capacity tests for critical journeys. | Single nominal load test only; no tail metrics or stress behavior. | Baseline load tests exist; burst/saturation/failover coverage incomplete. | P95/P99 and saturation tests executed every release for critical paths with explicit thresholds. | Peak+20% and cold-cache/failover scenarios pass with bounded degradation. | Two cycles with independent rerun confirming performance claims and SLO compliance on critical journeys. |
| 11. Security, Privacy, and Abuse Verification Depth | No executable security/privacy/abuse tests. | Scanner-only checks; no adversarial misuse validation. | Top vulnerability tests plus partial abuse/privacy scenario coverage. | Threat-model-mapped tests for all critical assets; consent/deletion/access controls verified. | Independent adversarial exercise completed; unresolved Sev1 findings = 0 at release decision. | Two cycles with zero unresolved critical exploit/privacy findings and successful independent exploit replay prevention. |
| 12. Reliability, Failover, and Recovery Validation | Failover/restore claims untested. | Runbooks exist but no executed drills. | Planned drills run occasionally; integrity verification incomplete. | Fault injection + restore testing each release; measured RTO/RPO reported. | Blind drill passes with end-to-end data integrity verification for critical datasets. | Two consecutive blind drills pass within target RTO/RPO with zero critical data loss. |
| 13. Defect Severity Calibration and Triage Discipline | Defect process absent or severity arbitrary. | Defects logged but severity policy inconsistent; severe misclassification common. | Severity rubric used; misclassification remains >20% or RCA quality weak. | Misclassification <=10%; all Sev1/Sev2 defects include reproducible RCA and verified closure. | Misclassification <=5%; reopen trend and recurrence tracked with corrective actions. | Two cycles with no severity laundering incidents and >=50% reduction in repeat Sev1/Sev2 classes. |
| 14. Regression Impact Analysis and Suite Freshness | Regression suite missing or obsolete. | Suite exists but not linked to changed components. | Partial impact-based selection; stale tests materially reduce signal. | >=95% changed critical components covered by impact-selected regression tests. | Stale-test ratio <5%; monthly curation removes redundant/non-diagnostic cases. | Two cycles with zero severe escapes from previously fixed defects and proven suite relevance. |
| 15. Evidence Integrity and Independent Replayability | Evidence missing, unverifiable, or tampered. | Evidence is screenshot-heavy with incomplete raw artifacts/provenance. | Raw artifacts available but manifest incomplete; replay succeeds inconsistently. | Complete manifest, hash chain, and replay instructions for all critical claims. | Independent reviewer replays >=95% of sampled critical claims successfully. | Two independent teams replay 100% critical claims from cold start with matching conclusions. |
| 16. Escaped Defect Detection and Feedback Closure | Escapes are not tracked or analyzed. | Escapes tracked but not connected to prevention actions. | RCA exists, but <60% of severe escapes produce new preventive tests. | 100% Sev1/Sev2 escapes mapped to preventive tests and monitoring rules. | Detection and closure trends improve quarter over quarter with low severe recurrence. | Two cycles with zero repeated Sev1 defect families and 100% closure SLA compliance for severe escapes. |
| 17. Accessibility and Cross-Platform Verification | No accessibility or platform compatibility verification. | Manual spot-checks on limited platform set only. | Baseline automated WCAG checks plus limited browser/device testing. | Critical flows validated against WCAG 2.2 AA and supported browser/device matrix each release. | Includes assistive technology and localization rendering tests; critical a11y backlog is zero. | Two cycles with no critical production accessibility defects and independent re-validation pass. |
| 18. Waiver Governance and Residual Risk Accounting | Waivers informal, ownerless, or timeless. | Waivers logged but often missing mitigation tasks or expiry. | Owner and expiry present; follow-through inconsistent and overdue waivers exist. | All waivers time-boxed, risk-scored, and linked to mitigation tickets before release approval. | Overdue waiver rate is zero; closure evidence audited before next release. | Two cycles with no evergreen waivers and all expired waivers closed before release cut. |

## 4) Anti-gaming checks specific to this role
1. Recompute reported pass rates from raw test results; reject rollup screenshots as sole evidence.
2. Run seeded-defect tests each cycle; if seeded Sev1 defect is not detected, cap related scoring at 50.
3. Compare first-fail and post-retry outcomes; any retry-masked critical failure is treated as gate failure.
4. Sample trace links and verify semantic validity, not just matching IDs.
5. Re-run a random 10% of critical tests from a clean environment with non-author operator.
6. Cross-check defect severity against user impact and incident metrics to detect severity laundering.
7. Detect quiet scope drops by diffing requirement baseline against release evidence.
8. Audit quarantined/muted tests weekly; expired quarantine automatically blocks release.
9. Validate timestamp sequence (requirement approval -> code change -> test run -> release decision); out-of-order evidence is inadmissible.
10. Compare waiver volume and aging near release cutoffs; spikes trigger mandatory independent review.
11. Perform independent percentile recomputation for performance claims from raw telemetry.
12. Require proof that every critical postmortem action produced a changed test, monitor, or gate rule.

## 5) Tripwires and hard-fail conditions
| ID | Trigger condition | Detection rule | Consequence |
|---|---|---|---|
| R5-TW-01 | Evidence fabrication or tampering | Hash mismatch, forged timestamp, or altered raw artifact | Immediate hard fail; R5 score set to 0; release blocked |
| R5-TW-02 | Critical requirement has no validating test | Traceability audit finds any unmapped critical requirement | Release blocked until mapping and passing test evidence exist |
| R5-TW-03 | Unauthorized gate bypass | Merge/release occurred with failed mandatory gate and no approved waiver | Hard fail for cycle; release rollback review required |
| R5-TW-04 | Unresolved Sev1 defect at release decision | Sev1 status open without time-boxed approved waiver | Release blocked |
| R5-TW-05 | Critical abuse/security/privacy path untested | Threat model marks critical path without executed test result | Release blocked; sub-dimension 11 capped at 25 |
| R5-TW-06 | Recovery claim cannot be reproduced | Blind restore/failover drill fails RTO/RPO or integrity checks | Release blocked for affected service until successful rerun |
| R5-TW-07 | Flake masking of critical failures | Critical test passed only after retries while first-fail ignored | Sub-dimensions 8 and 9 capped at 50; gate rerun mandatory |
| R5-TW-08 | Waiver governance breach | Expired waiver used to justify release or waiver missing owner | Release blocked; sub-dimension 18 capped at 25 |
| R5-TW-09 | Independent replay failure for critical claim | Non-author cannot reproduce claim with provided evidence | Sub-dimension 15 capped at 25; score above 75 disallowed |
| R5-TW-10 | Recurrent severe escape with no prevention closure | Same Sev1/Sev2 defect family recurs without linked new controls | Cycle marked conditional fail; corrective plan due before next release |
| R5-HF-11 | `R5-ITW-01` remains unresolved at publication close | Mandatory anti-gaming control skipped and not remediated before publication | Immediate hard fail; iteration snapshot `FAIL` for R5 |
| R5-HF-12 | `R5-ITW-02` remains unresolved at publication close | Required replay sample not executed or below Section 8.3 minimums at publication | Immediate hard fail; iteration snapshot `FAIL` for R5 |

Hard-fail rule: triggering `R5-TW-01`, `R5-TW-02`, `R5-TW-03`, `R5-TW-04`, `R5-HF-11`, or `R5-HF-12` is an automatic release fail regardless of weighted average.

## 6) Cross-role dependency and handoff criteria
| Counterpart role | Input required by R5 | R5 output/handoff | Acceptance criteria for handoff | SLA |
|---|---|---|---|---|
| R1 Product Manager | Approved requirement baseline, acceptance criteria, priority and criticality tags | Testability review, traceability gaps, release quality recommendation | 100% critical requirements are testable and traceable before code freeze | Within 2 business days of baseline change |
| R2 Product Architect / Enterprise Architect | Architecture decisions, dependency map, NFR targets, failure modes | Risk-driven test strategy and resilience/performance test scope | All critical architecture risks mapped to executable tests | Within 3 business days of architecture revision |
| R3 Engineering Manager | Delivery plan, code-freeze policy, ownership map | Quality gate readiness report and defect risk forecast | No unresolved ownership for critical failing tests/defects | Weekly during active release window |
| R4 Software Engineer | Implemented features, test hooks, logs, fix PRs | Defect verification results, oracle updates, regression requirements | Every Sev1/Sev2 fix includes reproducer and regression proof | Same day for critical fixes; 2 business days otherwise |
| R6 SRE / Platform Engineer | SLO targets, incident history, drill schedule, observability data | Reliability validation findings and production feedback loop actions | Recovery and detection claims supported by executed drills and telemetry | Before release approval and after each Sev1 incident |
| R7 Security Engineer / Security Architect | Threat model, control requirements, vulnerability findings | Security/abuse test evidence and residual risk statement | Critical threats have executed tests and closure evidence | Before release candidate sign-off |
| R8 Privacy / Compliance / Legal | Regulatory obligations, data handling controls, consent/retention policies | Privacy test coverage report and exceptions with expiry | No mandatory privacy control missing test evidence | Before release and policy updates |
| R12 DevOps / Release Manager | Pipeline config, gate policy, promotion records | Go/no-go QA gate decision with auditable evidence bundle | Mandatory gates pass or have approved, time-boxed waivers | At each promotion decision |
| R13 Operations / Support / Customer Success | Escalation records, customer-impact defects, support trends | Escape analysis and preventive test/control backlog | All Sev1/Sev2 escapes mapped to preventive action owners | Weekly and after major incidents |
| R15 Internal Audit / Assurance | Audit criteria, sampling plan, evidence retention requirements | Replay package, hash manifest, adjudication log | Audit can reproduce sampled critical claims without author assistance | Per audit cycle and pre-release for high-risk launches |

## 7) Cycle-level improvement checklist
Use this checklist every release cycle; unchecked critical items block sign-off.

### Planning (before implementation)
- [ ] Recalculate risk ranking using latest incident and change history.
- [ ] Confirm critical requirement baseline is frozen and uniquely versioned.
- [ ] Confirm testability review completed for all new/changed critical requirements.
- [ ] Approve threat/abuse/performance/resilience scope for this cycle.

### Build and test execution
- [ ] Enforce bidirectional requirement-to-test traceability checks in CI.
- [ ] Run deterministic oracle validation and seeded-defect detection for critical components.
- [ ] Monitor flake rate daily; triage or quarantine with owner and due date.
- [ ] Run boundary/negative/state-transition suites for all critical workflows.
- [ ] Run performance, security/privacy, and resilience suites with raw artifact retention.

### Pre-release gate
- [ ] Verify zero unauthorized gate bypasses and zero unresolved Sev1 defects.
- [ ] Validate waiver ledger: all waivers have owner, mitigation, and expiry before release cut.
- [ ] Recompute key quality metrics from raw evidence (traceability, defect severity, flake, SLO tests).
- [ ] Complete independent replay for sampled critical claims.

### Post-release learning and closure
- [ ] Log every Sev1/Sev2 escape within 1 business day and assign RCA owner.
- [ ] Link each severe escape to at least one preventive test/gate/monitoring change.
- [ ] Measure recurrence by defect family and review trend with engineering and product.
- [ ] Close or renew waivers with explicit decision and updated risk statement.
- [ ] Publish cycle-end QA assurance report with auditable evidence links.

## 8) Iteration snapshot governance, admissibility schema, and replay determinism

These controls are mandatory and override weaker language elsewhere in this file.

### 8.1 Mandatory non-zero evidence schema (row level)

| Field | Required value | Enforcement |
| --- | --- | --- |
| `who` | Scorer ID, evidence author ID, independent validator ID | Missing field sets row anchor to `0` |
| `what` | Requirement ID, test case ID, run ID, defect ID, gate ID | Missing field sets row anchor to `0` |
| `where` | Immutable evidence location (artifact URI, log index, ticket URI) | Missing field sets row anchor to `0` |
| `time` | Evidence capture UTC timestamp and decision UTC timestamp | Missing field sets row anchor to `0` |
| `version` | Requirement baseline version, code revision, test suite revision | Missing field sets row anchor to `0` |
| `hash` | SHA-256 (or signed digest) for primary evidence payload | Missing field sets row anchor to `0` |

Completeness thresholds:
- sampled completeness for non-zero rows must be `>=95%`;
- sampled completeness for rows scored `>75` must be `>=98%`.

If sampled missing-field defects exceed 5% for non-zero rows, R5 publication is blocked and the iteration snapshot is `FAIL` for R5.

### 8.2 Iteration snapshot lock and delta reopen controls

| Control | Mandatory record | Consequence if missing |
| --- | --- | --- |
| Snapshot lock before scoring | `iteration_id`, `snapshot_id`, rubric hash, denominator hash, cutoff UTC, approvers (`R5`,`R12`,`R15`) | Scoring on unlocked baseline is invalid |
| Approved delta reopen | Change ticket, impacted row IDs, rationale, approvers, reopen timestamp | Out-of-process edits invalidate all post-edit scores |
| Delta rescore log | Prior anchor, new anchor, evidence delta, reviewer IDs for each impacted row | Publication blocked until completed |

### 8.3 Deterministic replay and recompute contract

| Control | Minimum requirement | Hard-fail trigger |
| --- | --- | --- |
| Non-author replay sample | Replay `>=20%` of scored rows (minimum 12), including all gate-sensitive rows and all rows scored `90` or `100` | Coverage shortfall blocks publication |
| Row replay parity | Replayed row anchor must match published anchor exactly unless signed adjudication exception exists | >5% unmatched sampled rows => `FAIL` for R5 |
| Aggregate recompute parity | Independent recompute of final R5 score must equal published score exactly (`delta = 0.00`) | Any non-zero delta blocks publication and marks iteration snapshot invalid for R5 |

### 8.4 Mandatory anti-gaming suite and hard-fail behavior

Required suite per iteration snapshot: denominator drift check, seeded-defect detection, retry-masking audit, trace-link semantic audit, cutoff chronology audit, independent percentile recompute, waiver spike audit, postmortem-action proof audit.

| ID | Trigger | Immediate effect | Recovery proof | If unresolved at publication |
| --- | --- | --- | --- | --- |
| `R5-ITW-01` | Any mandatory anti-gaming control skipped | Affected scope capped at `50`; publication blocked | Completed control execution logs plus impacted-row rescoring evidence | `R5-HF-11`: iteration snapshot `FAIL` for R5 |
| `R5-ITW-02` | Required replay sample not executed | No row in affected scope may exceed `75` | Replay transcript meeting Section 8.3 coverage and parity thresholds | `R5-HF-12`: iteration snapshot `FAIL` for R5 |
| `R5-ITW-03` | Any `100` row lacks same-iteration adversarial challenge evidence | Row downgraded to `50` | Challenge execution log, independent validator sign-off, and corrected row rescore | Publication blocked until corrected rescore |

### 8.5 Deterministic precedence order

| Rank | Condition | Outcome |
| --- | --- | --- |
| 1 | Hard-fail active (`R5-TW-01`, `R5-TW-02`, `R5-TW-03`, `R5-TW-04`, `R5-HF-11`, `R5-HF-12`) | Immediate `FAIL` |
| 2 | Severity-1 contradiction unresolved past SLA | Publication blocked |
| 3 | Anti-gaming tripwire active | Apply caps and holds from Section 8.4 |
| 4 | High-anchor evidence missing | Cap rows per Sections 8.3-8.4 |
| 5 | No blocking condition active | Compute weighted role score from admissible rows only |

---

## R6 SRE / Platform Engineer

- source_file: `swarm_outputs/role_expansions/R6_sre_platform_engineer.md`
- words: 4599
- lines: 184

# R6 SRE / Platform Engineer Rubric Expansion

## 1) Role mission and decision rights
R6 exists to keep production services within agreed reliability, availability, performance, and recoverability bounds under normal, degraded, and adversarial conditions. R6 is accountable for operating signals, safe change delivery, incident command quality, and proof of recovery capability. Narrative claims do not count; only replayable operational evidence counts.

R6 decision rights are binding for runtime safety controls and reliability gates.

| Decision domain | R6 authority | Non-delegable constraint | Required decision record |
| --- | --- | --- | --- |
| SLI/SLO policy and error budgets | Set and enforce SLI definitions, SLO targets, and burn-rate actions for production services | Cannot weaken SLO policy after breach without formal exception approval | SLO policy version, approver list, dated exception ticket |
| Release reliability gate | Block rollout when reliability tripwires or burn-rate thresholds are active | No schedule-based override by delivery team alone | Gate decision log with active alerts and budget state |
| Incident command model | Appoint IC, declare severity, set escalation path, and close incident timeline | Must preserve timeline integrity; no retroactive timeline edits | Incident record with timestamps, participants, escalation chain |
| Capacity and saturation controls | Set autoscaling thresholds, headroom targets, and saturation alarms | Cannot accept sustained saturation beyond policy without mitigation plan | Capacity review report and approved mitigation ticket |
| Backup/restore and DR testing | Define test cadence and pass criteria for restores and failovers | No “backup healthy” claim without successful restore proof | Restore drill output, RTO/RPO result report |
| Operational automation | Approve automation that mutates production state | Automation requires rollback path, idempotency, and audit trail | Automation runbook, change approval, execution log |
| Dependency reliability policy | Enforce reliability controls for upstream/downstream dependencies | Cannot onboard critical dependency without SLI and fallback path | Dependency assessment record and fallback test evidence |

## 2) Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R6-01 Service criticality inventory and ownership | All production services, jobs, queues, and data stores are tiered by business impact and mapped to accountable owners. | 100% of Tier-0/Tier-1 assets have primary and secondary owner; ownership review age <= 30 days; orphaned critical assets = 0. | Who: platform lead + service owner. What: service catalog export and on-call mapping. Where: versioned catalog file, pager schedule, incident system service registry. |
| R6-02 SLI design and measurement fidelity | SLIs measure user-visible reliability and are computed from trustworthy telemetry paths. | Each Tier-1 service has latency, availability, and correctness/error SLIs; telemetry completeness >= 99.5%; SLI query reproducibility check passes. | Who: observability owner + independent reviewer. What: SLI spec, query definitions, recomputation notes. Where: `observability/` repo folder, metrics backend query links, dashboard URLs. |
| R6-03 SLO governance and error-budget policy | SLO targets and burn-rate responses are explicit, enforced, and tied to release decisions. | 100% Tier-1 services have approved SLOs; fast/slow burn alerts active; budget breach response initiated within policy SLA. | Who: SRE manager + engineering manager. What: SLO policy, exception approvals, breach response tickets. Where: policy docs repo, ticketing system, release gate records. |
| R6-04 Alert quality and paging hygiene | Alerts are actionable, low-noise, and routed to the correct responder at the right severity. | Actionable alert ratio >= 80%; false-positive paging rate <= 20%; duplicate-page suppression works; page-to-ack median within target. | Who: on-call engineer + incident manager. What: alert tuning report and page analytics. Where: alert configuration repo, paging platform analytics dashboard. |
| R6-05 Incident detection and triage latency | Critical incidents are detected quickly and classified correctly before customer impact expands. | MTTD for Sev1/Sev2 meets target; initial severity accuracy >= 90%; customer-reported-first Sev1 rate trends down. | Who: incident commander + duty engineer. What: incident timeline and detection source analysis. Where: incident management records, monitoring alert history. |
| R6-06 Incident command and escalation discipline | Incident response follows a reproducible command model with clear ownership, communications, and escalation timing. | IC assigned within 5 minutes for Sev1; stakeholder updates at policy cadence; escalation steps executed within SLA. | Who: IC + communications lead. What: chat transcript, timeline, escalation logs. Where: incident channel archive, incident ticket, status page history. |
| R6-07 Post-incident RCA and corrective closure | Root cause analysis identifies systemic causes and drives verified corrective actions to closure. | RCA published within policy window; corrective actions have owner and due date; overdue high-risk actions = 0; recurrence rate declines. | Who: service owner + SRE reviewer. What: RCA doc and action tracker. Where: postmortem repository, work-item tracker, recurrence report. |
| R6-08 Deployment safety and progressive delivery controls | Production changes are released through controlled blast-radius reduction and automatic abort criteria. | Canary/gradual rollout used for Tier-1 changes; health checks gate promotion; automatic rollback/abort triggers validated. | Who: release engineer + service owner. What: rollout plan, gate config, canary verdict. Where: CI/CD pipeline config, deployment logs, release records. |
| R6-09 Rollback and forward-fix readiness | Teams can rapidly recover from bad releases using tested rollback and forward-fix playbooks. | Rollback rehearsal success >= 95%; rollback decision latency within target; config and schema rollback compatibility verified pre-release. | Who: deployment owner + database/platform owner. What: rollback drill results and compatibility checklist. Where: runbooks repo, deployment system logs, change tickets. |
| R6-10 Capacity forecasting and saturation control | Forecasting and scaling controls keep services below dangerous saturation under expected and burst load. | 30/60/90-day forecasts maintained; CPU/memory/IO saturation alerts active; Tier-1 headroom policy met at peak windows. | Who: capacity owner + finance partner. What: forecast model and saturation trend report. Where: capacity planning docs, telemetry dashboards, scaling policy configs. |
| R6-11 Resilience engineering and failure-mode validation | Critical failure modes are tested through controlled fault injection and degraded-mode validation. | Quarterly failure-injection for Tier-1 paths; graceful degradation tests pass; single-point dependency failures have validated fallback behavior. | Who: resilience lead + service owner. What: experiment plan, blast-radius guardrails, test results. Where: game day records, experiment scripts, incident knowledge base. |
| R6-12 Backup integrity and restore performance | Backup claims are verified by successful restore tests that meet integrity and timing objectives. | Backup success telemetry monitored; restore test cadence met; checksum/data validation passes after restore; RTO/RPO targets met in drills. | Who: database/storage owner + auditor witness. What: restore test report and integrity validation output. Where: backup platform logs, restore runbooks, drill artifacts. |
| R6-13 Disaster recovery readiness and regional failover | Disaster scenarios have tested failover procedures that meet business continuity requirements. | DR drill cadence met; regional failover success rate >= target; dependency failover sequence validated; DNS/traffic shift timing within objective. | Who: DR coordinator + network/platform owner. What: DR plan, drill timeline, failback report. Where: DR documentation repo, traffic management logs, status records. |
| R6-14 Platform dependency and supply-path hygiene | Runtime dependencies are monitored, version-governed, and protected against reliability regressions. | Critical dependency inventory complete; dependency SLO/SLA tracked; unsupported/EOL dependency count trends to zero; fallback tested. | Who: platform owner + security owner. What: dependency register and risk assessments. Where: CMDB/dependency manifest, vendor status pages, risk register. |
| R6-15 Operational automation robustness and toil reduction | Automation reduces manual risk and toil without creating opaque or unsafe control paths. | Toil hours per engineer trend downward; automation failure rate below threshold; scripts are idempotent and auditable; manual break-glass usage monitored. | Who: automation owner + team lead. What: toil baseline, automation test evidence, run logs. Where: automation repo, scheduler/orchestrator logs, ops metrics dashboard. |
| R6-16 Runbook quality and on-call readiness | Responders can execute critical operations without tribal knowledge and with regular readiness validation. | Tier-1 runbook coverage = 100%; runbook drill pass rate >= 90%; on-call training completion = 100%; role handover checklist compliance >= 95%. | Who: on-call manager + service owner. What: runbook audit, drill scorecards, training records. Where: runbook repository, LMS/training tracker, shift handover logs. |

## 3) Scoring anchors table (0/25/50/75/90/100)
Use only `0`, `25`, `50`, `75`, `90`, `100`. A sub-dimension cannot exceed `50` without complete required evidence, cannot exceed `75` without independent review, and cannot exceed `90` without at least one successful challenge test in-cycle.

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R6-01 Service criticality inventory and ownership | Critical assets are not inventoried; ownership missing or fabricated. | Partial inventory; >20% Tier-1 assets lack named backup owner. | Most assets cataloged, but stale records and ownership drift persist. | Full Tier-1 inventory with current primary/secondary owners and monthly attestation. | Independent audit sample confirms <=2% catalog drift and valid pager mapping. | Two consecutive quarters with zero orphan critical assets and clean audit outcomes. |
| R6-02 SLI design and measurement fidelity | No reliable SLI definitions or telemetry path. | SLIs defined narratively, but not reproducible from raw telemetry. | Core SLIs exist with partial query reproducibility; known measurement gaps remain. | Tier-1 SLIs are user-centered, versioned, and reproducible from source telemetry. | Independent recomputation matches dashboard values within agreed tolerance. | Two cycles of stable SLI definitions with no material measurement dispute. |
| R6-03 SLO governance and error-budget policy | No enforced SLO policy; breaches ignored. | SLOs documented but not tied to release/change decisions. | SLO policy active for core services, but breach response is inconsistent. | Error-budget policy consistently triggers feature freeze/reliability actions per rule. | Exceptions are rare, approved, time-bound, and independently reviewed. | Two cycles with disciplined budget governance and no undocumented override. |
| R6-04 Alert quality and paging hygiene | Paging is unreliable or unusable; major incidents missed or noisy spam dominates. | Alerts exist but are mostly non-actionable; false pages routinely exceed policy. | Baseline routing works; actionable ratio and duplicate suppression are inconsistent. | Alerts are actionable, ownership-correct, and tuned to policy thresholds. | Noise, duplicate pages, and misroutes remain low under independent sampling. | Sustained low-noise paging quality across two cycles including peak event periods. |
| R6-05 Incident detection and triage latency | Sev1/Sev2 detection fails or depends on customer reports. | Detection exists but MTTD is far beyond target; severity assignment frequently wrong. | Monitoring detects most incidents; triage speed/accuracy meets minimum baseline only. | Detection and triage targets are met consistently for critical services. | Independent review confirms high severity accuracy and timely escalation initiation. | Two cycles with target MTTD and near-zero customer-reported-first critical incidents. |
| R6-06 Incident command and escalation discipline | No defined IC model; escalations ad hoc and delayed. | IC role informal; timeline and communications often incomplete. | IC process defined and used, but cadence and escalation SLAs are uneven. | IC assignment, communication cadence, and escalation path are consistently executed. | Cross-functional participants confirm command quality and decision traceability. | Two cycles of critical incidents handled within policy with no command breakdowns. |
| R6-07 Post-incident RCA and corrective closure | No RCAs, or RCAs are blame-based and non-actionable. | RCAs produced sporadically; actions unowned or routinely overdue. | RCAs generally timely; corrective actions tracked but closure quality varies. | RCAs identify systemic causes and drive owned, timely corrective closure. | Independent reviewer verifies causal logic and effectiveness of closed actions. | Two cycles show reduced repeat incidents from previously identified causal classes. |
| R6-08 Deployment safety and progressive delivery controls | Direct-to-prod changes bypass safety controls. | Basic pipeline exists, but canary/abort controls are absent or disabled. | Progressive delivery used on some services; gate adherence is inconsistent. | Tier-1 releases use enforced canary/progressive gates with clear abort criteria. | Independent replay of releases confirms gate decisions match runtime health evidence. | Two cycles with no critical incidents from gate bypass or uncontrolled rollout blast radius. |
| R6-09 Rollback and forward-fix readiness | Rollback path unknown or repeatedly fails when needed. | Rollback documented but untested; recovery depends on specific individuals. | Rollback tested occasionally; schema/config constraints still create recovery delays. | Rollback and forward-fix playbooks tested and executable within target latency. | Independent drill validates recovery path across app, config, and data layers. | Two cycles with all high-risk changes meeting recovery-time objectives during drills or events. |
| R6-10 Capacity forecasting and saturation control | Capacity managed reactively; frequent saturation and resource exhaustion. | Forecasting ad hoc; headroom targets undefined or ignored. | Forecast and scaling policy exist but miss seasonal/burst demand patterns. | Forecasting is maintained and saturation controls keep Tier-1 services within policy. | Independent stress checks confirm headroom assumptions and alarm thresholds are valid. | Two cycles with no avoidable saturation incidents and forecast error within target band. |
| R6-11 Resilience engineering and failure-mode validation | No fault-injection or degraded-mode testing for critical paths. | Experiments are one-off demos without operational follow-through. | Some failure modes tested; coverage and remediation depth are incomplete. | Critical failure modes are regularly tested with explicit fallback validation. | Independent observers verify experiment safety, learning quality, and control updates. | Two cycles show measurable resilience gains and reduced incident impact from tested modes. |
| R6-12 Backup integrity and restore performance | Backups unverified; restore attempts fail or are untested. | Backup jobs run, but restore proof is outdated or partial. | Restore tests pass for some critical stores; integrity/time targets not consistently met. | Restore tests meet policy cadence with integrity checks and RTO/RPO evidence. | Independent witness reproduces restore on sampled critical systems successfully. | Two cycles with full critical restore coverage and zero unresolved restore-control gaps. |
| R6-13 Disaster recovery readiness and regional failover | DR plan absent or purely theoretical. | DR documentation exists, but failover path untested in realistic conditions. | Limited DR drills run; critical dependencies and failback steps remain weak. | DR and regional failover drills executed on schedule with target outcomes. | Independent cross-team drill confirms dependency sequencing and communications readiness. | Two cycles with successful end-to-end failover/failback for all Tier-0/Tier-1 services. |
| R6-14 Platform dependency and supply-path hygiene | Critical dependencies unknown or unmanaged. | Dependency list incomplete; reliability or EOL risk not actively governed. | Dependency tracking exists; fallback and lifecycle hygiene partially implemented. | Critical dependencies have owners, reliability metrics, lifecycle plans, and tested fallback. | Independent review confirms no hidden critical dependency without risk treatment. | Two cycles with zero unmanaged critical dependency exposure and clean lifecycle compliance. |
| R6-15 Operational automation robustness and toil reduction | Manual operations dominate; automation causes uncontrolled side effects. | Scripts exist but are fragile, non-idempotent, and weakly audited. | Core automations work; failure handling and observability are inconsistent. | Automation is idempotent, monitored, audited, and materially reduces toil. | Independent challenge runs confirm safe behavior under retries and partial failures. | Two cycles with sustained toil reduction and no major incident from automation defects. |
| R6-16 Runbook quality and on-call readiness | No usable runbooks; responders rely on tribal knowledge. | Runbooks incomplete/outdated; drills rarely executed. | Runbooks cover core paths, but drill pass rate and training coverage are uneven. | Full Tier-1 runbook coverage with regular drills and complete on-call training. | Independent responder executes sampled runbooks successfully without author assistance. | Two cycles with high drill pass rates and no critical delay attributable to documentation gaps. |

## 4) Anti-gaming checks specific to this role
1. Recompute sampled SLI/SLO values from raw telemetry for at least 7 random days per cycle; reject dashboard-only evidence.
2. Validate incident timelines against immutable chat/page timestamps; reject post-hoc timeline edits without correction note.
3. Detect alert suppression abuse by auditing silences, maintenance windows, and mute durations against approved change windows.
4. Compare canary verdict logs with final rollout decisions; flag manual override without approved exception ticket.
5. Run blind restore challenge on randomly selected critical data stores; do not pre-announce target system.
6. Compare pager false-positive claims with actual ack/resolution dispositions; reject hand-edited statistics.
7. Sample dependency register entries and verify owner acknowledgement plus fallback test proof.
8. Verify RCA closure claims by checking merged remediation code/config against incident causal chain.
9. Audit “automation success” by replaying failed runs; reject success rates that exclude retries and partial failures.
10. Validate runbook freshness by executing steps from current docs on a non-author operator.
11. Compare capacity forecast assumptions with actual peak load windows; flag retrospective model edits.
12. Enforce evidence cut-off timestamp; exclude evidence created after gate decision unless re-evaluation is formally reopened.

## 5) Tripwires and hard-fail conditions

| ID | Tripwire / hard-fail condition | Effect |
| --- | --- | --- |
| R6-HF1 | Any Sev1 incident caused by known unresolved reliability risk past due date. | Immediate role-level FAIL for cycle; executive risk acceptance required before release continuation. |
| R6-HF2 | Production release bypasses mandatory reliability gate (canary, health gate, or error-budget block). | R6 score capped at 25 for cycle; release governance incident opened. |
| R6-HF3 | Backup success is claimed but latest required restore test failed or was not executed. | Sub-dimensions R6-12 and R6-13 scored 0; release block for affected services. |
| R6-HF4 | Tier-0/Tier-1 service without accountable primary and secondary on-call owner. | R6-01 scored 0; no new production changes allowed for that service. |
| R6-HF5 | Monitoring misses a Sev1 that is first detected by customers for a repeat failure mode. | R6-04 and R6-05 capped at 25 until detection gap remediation validated. |
| R6-HF6 | Evidence tampering, fabricated uptime/latency numbers, or altered incident timelines. | Entire R6 score set to 0 for cycle; forensic review mandatory. |
| R6-HF7 | DR drill misses contractual RTO/RPO for critical service without approved exception and dated mitigation plan. | R6-13 scored 0; critical-service release freeze until mitigation re-test passes. |
| R6-HF8 | Error budget exhausted and high-risk feature rollout proceeds without formal waiver. | R6-03 and R6-08 capped at 25; waiver process violation logged as control breach. |
| R6-HF9 | Automation performing production mutation has no rollback path or audit log. | R6-15 scored 0; automation disabled until controls are implemented and retested. |
| R6-HF10 | Repeated incident recurrence with previously “closed” corrective actions from RCA. | R6-07 capped at 25; corrective-action governance review required. |

## 6) Cross-role dependency and handoff criteria

| Counterpart role | R6 receives (entry criteria) | R6 hands off (exit criteria) | SLA / escalation trigger |
| --- | --- | --- | --- |
| R4 Software Engineer | Change risk classification, rollback compatibility notes, observability instrumentation updates included in PR. | Runtime readiness verdict, deployment gate status, rollback drill confirmation for high-risk changes. | Escalate if PR lacks rollback or telemetry evidence within 1 business day. |
| R12 DevOps / Release Manager | Approved release plan with window, blast-radius strategy, and freeze constraints. | Go/no-go reliability signoff with canary criteria and abort thresholds. | Escalate if release proceeds without signed reliability gate evidence. |
| R5 QA / Test Engineer | Performance/resilience test outcomes and known defect risk register. | Production telemetry deltas, incident observations, and escaped-failure patterns for regression updates. | Escalate if Sev2+ defect risk lacks runtime mitigation before cutover. |
| R7 Security Engineer | Current threat advisories and required runtime hardening controls. | Runtime control verification, suspicious activity signals, and incident artifacts for security cases. | Escalate within 30 minutes for active exploit indicators on internet-facing services. |
| R2 Product Architect / Enterprise Architect | NFR targets, dependency topology, and approved resilience patterns. | Capacity and failure-mode findings that require architecture changes or exception decisions. | Escalate if architecture constraints block reliability objectives for next release cycle. |
| R1 Product Manager | Business criticality tiers, customer impact thresholds, and availability commitments. | Error-budget status, reliability tradeoff decisions, and feature-freeze recommendations. | Escalate when product scope conflicts with active error-budget policy. |
| R13 Operations / Support / Customer Success | Customer-impact signals, ticket trends, and communication requirements during incidents. | Incident status cadence, mitigation ETA, workaround/runbook updates for frontline teams. | Escalate if customer comms SLA is missed during Sev1/Sev2 events. |
| R14 FinOps / Procurement / Vendor Management | Cost guardrails, vendor SLA terms, and renewal/exit risk timelines. | Capacity spend justification, reliability-vs-cost tradeoff evidence, and vendor risk escalations. | Escalate if cost pressure requests violate minimum reliability control baselines. |
| R8 Privacy / Compliance / Legal | Regulatory control obligations, data-handling constraints, and notification SLAs for operational incidents. | Incident evidence package with privacy-impact classification, timeline, and containment proof for legal/compliance review. | Escalate within 1 hour when incident facts indicate potential statutory/privacy notification trigger. |
| R15 Internal Audit / Assurance | Audit sampling request, replay scope, and admissibility criteria for scored reliability claims. | Replay bundle (evidence manifest, hash set, gate outcomes, contradiction closure log) sufficient for independent audit reproduction. | Escalate immediately if requested critical evidence cannot be reproduced before publication cutoff. |

## 7) Cycle-level improvement checklist
Use this checklist each scoring cycle (for example: sprint, biweekly ops cycle, or monthly reliability review).

| Checklist item | Pass criterion | Evidence artifact |
| --- | --- | --- |
| Re-validate service tiering and ownership | 100% Tier-0/Tier-1 assets have current primary/secondary ownership and escalation path. | Service catalog diff + on-call roster snapshot. |
| Recompute sampled SLIs from source data | Sample recomputation matches published SLI/SLO values within tolerance. | Recompute worksheet and query references. |
| Review error-budget policy actions | Every breach has documented action (freeze, mitigation, or approved waiver). | Budget review minutes and linked tickets. |
| Tune noisy or low-value alerts | False-positive pages reduced and alert runbooks attached to high-severity alerts. | Alert quality report and config diffs. |
| Audit incident response timelines | IC assignment, communications cadence, and escalation SLA adherence verified. | Incident audit log and timestamp report. |
| Close overdue postmortem actions | No overdue high-risk corrective actions from prior incidents. | Action tracker export with closure proof. |
| Execute release safety drill | Canary abort and rollback exercises pass on representative high-risk service. | Drill run output and release gate checklist. |
| Update capacity forecast with actuals | Forecast error measured, corrected assumptions committed, and headroom checked. | Forecast model revision note and dashboard links. |
| Run resilience experiment | At least one critical failure mode tested with validated mitigation behavior. | Game day report and remediation ticket set. |
| Perform backup restore challenge | Random critical system restore succeeds with integrity verification and timing targets. | Restore challenge report and checksum output. |
| Execute DR or failover component drill | Planned DR milestone completed with documented lessons and owner actions. | DR drill log, failover timeline, failback notes. |
| Review dependency risk and lifecycle | Critical dependency owner, SLA health, fallback status, and EOL plans updated. | Dependency register diff and risk review record. |
| Measure toil and automation safety | Toil trend reviewed and unsafe automation paths remediated. | Toil metrics dashboard and automation audit log. |
| Validate runbook freshness and training | Sampled non-author responders execute runbooks successfully; training completion current. | Drill scorecards, runbook update log, training completion export. |

## 8) Iteration snapshot governance, anti-gaming tripwires, and latency SLA controls

These controls are mandatory and override weaker language elsewhere in this file.

### 8.0 Non-zero admissibility contract (row level)

| Field | Required value for any non-zero row | Rejection rule |
| --- | --- | --- |
| `who` | Scorer ID and independent validator ID | Missing field sets row anchor to `0` |
| `what` | Operational claim ID (SLO, incident, release gate, drill, dependency, or automation run) | Missing field sets row anchor to `0` |
| `where` | Immutable evidence location (log query URI, ticket URI, run artifact URI) | Missing field sets row anchor to `0` |
| `time` | Evidence capture UTC and decision UTC | Missing field sets row anchor to `0` |
| `version` | Rubric revision, service version, and policy revision under evaluation | Missing field sets row anchor to `0` |
| `hash` | SHA-256 (or signed digest) for the primary evidence bundle | Missing field sets row anchor to `0` |

If sampled missing-field defects exceed 5% for non-zero rows, publication is blocked and the iteration snapshot is marked `INVALID` for R6.

### 8.1 Iteration snapshot lock and version-hash governance

| Control | Mandatory fields | Verification | Consequence if violated |
| --- | --- | --- | --- |
| Snapshot lock before scoring | `iteration_id`, `snapshot_id`, rubric hash, anchor hash, weight-model hash, denominator hash, cutoff UTC, approvers (`R6`,`R12`,`R15`) | Hash check at scoring start and pre-publication | Scoring result is invalid |
| Approved delta reopen record | Change ticket ID, scope, impacted rows/gates, approvers, reopen UTC | Diff must match approved scope | Out-of-scope edits invalidate post-edit scores |
| Unauthorized edit tripwire | Any hash drift without approved reopen record | Automated hash-drift monitor | Publication blocked; affected iteration snapshot marked `INVALID` |

### 8.2 Delta re-evaluation requirements

| Requirement | Minimum evidence | Block condition |
| --- | --- | --- |
| Impact map | Row IDs, gate IDs, contradiction IDs impacted by each approved delta | Missing map blocks publication |
| Targeted retest | Re-score all impacted rows and re-simulate all impacted gates | Any impacted row/gate not re-tested blocks publication |
| Comparability note | Explain anchor deltas >1 step with evidence references | Unexplained >1-step delta blocks publication |

### 8.3 Mandatory anti-gaming controls and skipped-control invalidation

Required controls per iteration snapshot: baseline hash check, denominator drift check, cutoff integrity check, provenance check, contradiction suppression check, replay witness rotation, gate-bypass simulation.

| ID | Trigger | Immediate effect | Recovery proof | If unresolved at publication |
| --- | --- | --- | --- | --- |
| `R6-ITW-01` | Any mandatory anti-gaming control skipped | Affected sub-dimensions capped at `50`; publication hold | Completed control logs, independent witness attestations, and impacted-row rescoring packet | Iteration snapshot marked `INVALID` |
| `R6-ITW-02` | Gate-bypass simulation finds pass path with active hard gate | `R6` scoring halted; gate logic remediation required | Updated precedence rules, rerun simulation logs, and parity verification report | Iteration snapshot marked `INVALID` |
| `R6-ITW-03` | Replay witness is not independent non-author | All rows scored `>75` capped at `50` | Independent non-author replay transcript meeting coverage target | Iteration snapshot marked `INVALID` |

### 8.4 Deterministic precedence and contradiction handling order

| Rank | Condition | Outcome |
| --- | --- | --- |
| 1 | Any hard-fail condition active (`R6-HF1..R6-HF10`) | Immediate `FAIL` |
| 2 | Severity-1 contradiction unresolved past SLA | Publication blocked; impacted scope anchor set to `0` |
| 3 | Anti-gaming tripwire active (`R6-ITW-01..03`) | Apply cap/hold and require rerun evidence |
| 4 | High-anchor proof missing (`90` or `100`) | Cap row at `75` (missing independence) or `50` (missing challenge/replay) |
| 5 | No blocking condition active | Compute weighted role score from admissible rows only |

### 8.5 Operational scoring-latency SLA (enforceable)

| SLA metric | Target | Enforcement |
| --- | --- | --- |
| Snapshot close latency | Final R6 publication within 5 business days after cutoff UTC | If exceeded due to rubric process, cap `R6-16` at `50` and hold publication |
| First-pass completion | `>=90%` rows adjudicated without return/rework | If below target, mandatory corrective plan and rerun of returned rows |
| Critical adjudication backlog | `0` unresolved critical returns at publication | Any unresolved critical return blocks publication |

If latency SLA breach persists after one corrective rerun, the iteration snapshot is `INVALID` for R6.

---

## R7 Security Engineer / Security Architect

- source_file: `swarm_outputs/role_expansions/R7_security_engineer_security_architect.md`
- words: 5006
- lines: 179

# R7 Security Engineer / Security Architect Rubric Expansion

## 1) Role mission and decision rights
R7 exists to prevent, detect, and contain security failures before they become material business impact. R7 is accountable for turning threat assumptions into enforced controls, proving those controls work under adversarial testing, and stopping releases when risk exceeds approved tolerance.

R7 decision rights are binding for security control gates and high-risk exceptions.

| Decision domain | R7 authority | Non-delegable constraint | Required decision record |
| --- | --- | --- | --- |
| Threat model and security architecture sign-off | Approve or block high-risk designs and releases based on threat model completeness and residual risk | No production launch of high-risk scope without a current threat model and owner-signed mitigation plan | Threat model version, unresolved risk register, sign-off ticket with approvers and date |
| Authentication control policy | Set MFA, session, credential, and workload identity requirements | Privileged or production access without required MFA/workload identity is prohibited | Auth policy version, exception record, identity provider control report |
| Authorization and privilege boundaries | Define least-privilege baseline, separation-of-duties rules, and privileged path controls | Cannot waive segregation-of-duty conflicts without formal exception and compensating control test | Access model spec, entitlement review logs, approved exception with expiry |
| Vulnerability remediation SLA and risk acceptance | Set remediation SLAs by severity/exploitability and enforce overdue escalation | Critical exploitable findings cannot remain open past SLA without executive risk acceptance | Vulnerability backlog export, SLA aging report, risk acceptance artifact |
| Secrets, certificate, and key lifecycle | Approve issuance, rotation, revocation, and storage controls for secrets and keys | Shared static secrets and unmanaged key material are prohibited in production | KMS/HSM policy, rotation logs, revocation records, secret scanning results |
| Detection and logging minimums | Set required telemetry, detection rules, and retention for critical systems | Systems cannot be promoted to production without required security telemetry | Logging standard, rule catalog, onboarding checklist, SIEM coverage report |
| Supply-chain trust controls | Require provenance, signing, and dependency governance for build and deploy pipelines | Unsigned or unprovenance artifacts are blocked from production | SBOM record, attestation verification logs, artifact signature verification report |
| Incident containment authority | Declare security severity and require emergency containment actions | Containment actions must preserve forensic integrity and chain of custody | Incident declaration record, containment timeline, forensic evidence log |

## 2) Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where) |
| --- | --- | --- | --- |
| R7-01 Threat model completeness and freshness | Critical systems have current threat models covering assets, trust boundaries, abuse cases, and mitigation ownership. | 100% internet-facing and Tier-0/Tier-1 systems have threat model age <= 90 days; unresolved high-risk threat actions = 0 past due; abuse-case coverage includes auth, privilege escalation, data exfiltration. | Who: security architect + service owner. What: signed threat model and mitigation tracker. Where: versioned security architecture repo and linked work-item system. |
| R7-02 Attack surface inventory and exposure drift control | All externally and internally reachable assets are inventoried, classified, and monitored for unauthorized exposure changes. | Independent ASM scan-to-inventory match >= 98%; unknown internet-facing endpoints = 0 older than 24 hours; DNS/certificate drift reviewed weekly. | Who: security engineering + platform owner. What: asset inventory export, ASM diff report, closure tickets. Where: CMDB/asset register, ASM platform, ticketing system. |
| R7-03 Identity and authentication robustness | Human and machine identities use strong authentication with resistant controls against credential theft and replay. | Phishing-resistant MFA coverage = 100% for privileged users and >= 98% for workforce users; shared accounts = 0; service-to-service auth uses workload identity or mTLS for Tier-1 paths. | Who: IAM owner + security reviewer. What: MFA enrollment report, account hygiene report, workload identity config evidence. Where: IdP admin console export, IAM repo, service mesh or PKI logs. |
| R7-04 Authorization and least-privilege integrity | Access decisions enforce deny-by-default, minimum necessary permissions, and periodic entitlement review. | 100% critical APIs/services have policy tests for allow/deny paths; privileged entitlement recertification completed monthly; dormant privileged roles removed within 24 hours of inactivity threshold breach. | Who: IAM engineer + application owner. What: policy-as-code tests, entitlement review attestations, revocation logs. Where: policy repository, access governance system, IAM audit logs. |
| R7-05 Privileged access and break-glass control discipline | Administrative access is tightly controlled, time-bound, and fully auditable with emergency access safeguards. | Just-in-time access for admin roles >= 95%; persistent admin accounts trend to 0; break-glass use reviewed within 1 business day with approved justification. | Who: PAM owner + security operations lead. What: JIT access logs, session recording evidence, break-glass review records. Where: PAM platform, SIEM, incident/change records. |
| R7-06 Secrets, certificates, and key lifecycle controls | Secrets and cryptographic keys are generated, stored, rotated, and revoked through managed systems with exposure prevention. | Plaintext secrets in code/artifacts = 0 open findings; rotation SLA adherence >= 98%; certificate expiry incidents = 0; key revocation tests pass quarterly. | Who: platform security + service owner. What: secret scan reports, rotation logs, cert inventory and expiry report, revocation drill output. Where: secret manager/KMS logs, CI scan output, certificate management dashboard. |
| R7-07 Cryptographic posture and data protection enforcement | Approved algorithms and protocol configurations protect data in transit and at rest with strong key management boundaries. | Deprecated algorithms/ciphers = 0 in production scans; TLS policy compliance >= 99%; encryption-at-rest enabled for all restricted data stores; key separation by environment enforced. | Who: security architect + infra owner. What: crypto baseline policy, config scan results, datastore encryption attestation. Where: IaC repo, runtime scanner outputs, cloud security posture tool. |
| R7-08 Vulnerability discovery and triage quality | Vulnerabilities are discovered comprehensively, deduplicated, and triaged by exploitability and business impact. | Scanner coverage = 100% for supported assets; KEV-mapped findings triaged within 24 hours; false-positive dispute resolution within SLA; duplicate finding rate controlled. | Who: AppSec lead + asset owner. What: scan coverage report, triage rubric output, KEV prioritization log. Where: vuln management platform, scanner configs, triage tickets. |
| R7-09 Patch and remediation governance | Security patches and code fixes are deployed within policy windows with verification that risk is materially reduced. | Critical internet-facing remediation within 7 days (or stricter policy); KEV remediation within 48 hours unless approved exception; overdue critical vulnerabilities = 0 without active risk acceptance. | Who: security engineering + service owner + release manager. What: remediation SLA report, patch deployment logs, exception approvals. Where: vuln platform, deployment system, governance records. |
| R7-10 Secure SDLC and adversarial testing depth | Security checks are embedded in SDLC and validated by adversarial tests before release of high-risk changes. | 100% repos enforce SAST/dependency/secret scanning gates; DAST/API tests for internet-facing apps each release; manual penetration test or targeted adversarial review for high-risk changes. | Who: AppSec engineer + QA/security tester + dev lead. What: pipeline gate configs, test reports, remediation proof. Where: CI/CD configs, security test repositories, release evidence package. |
| R7-11 Cloud and infrastructure hardening with drift control | Infrastructure baselines enforce hardened configuration and detect/remediate security drift rapidly. | High-risk misconfiguration MTTR within policy (for example <= 24 hours); CIS or equivalent benchmark compliance >= target; public storage/database exposure findings = 0 unresolved. | Who: cloud security engineer + platform team. What: policy compliance report, drift alerts, remediation tickets. Where: CSPM/CNAPP dashboards, IaC policy repo, change records. |
| R7-12 Supply-chain integrity and artifact provenance | Build and deploy chains prove component origin and integrity from source to production artifact. | SBOM coverage = 100% for production artifacts; artifact signing verification at deploy = 100%; provenance attestations present and validated; blocked malicious/typosquat dependency attempts tracked. | Who: supply-chain security owner + DevOps lead. What: SBOMs, signature verification logs, attestation records, dependency policy exceptions. Where: artifact registry, CI/CD attestations store, dependency firewall logs. |
| R7-13 Security telemetry coverage and log integrity | Required security events are captured with integrity controls and sufficient retention for investigation and detection. | 100% critical systems emit auth, admin, and sensitive-data access logs; log loss rate below threshold; immutable/tamper-evident storage enabled; retention meets policy. | Who: security operations + observability owner. What: telemetry coverage matrix, ingest health report, retention configuration evidence. Where: SIEM/data lake configs, log pipeline dashboards, policy repository. |
| R7-14 Detection engineering efficacy and containment speed | Detection content covers priority attacker techniques and drives rapid, accurate containment actions. | MITRE ATT&CK coverage for top threat scenarios >= target; mean time to detect and contain meets policy for Sev1/Sev2 security events; true-positive ratio improving cycle-over-cycle. | Who: detection engineer + incident commander. What: rule catalog, detection test results, incident response timing report. Where: SIEM/SOAR platform, purple-team exercise logs, incident tracker. |
| R7-15 Security incident command, forensics, and corrective closure | Security incidents follow disciplined command, evidence handling, root-cause analysis, and verified corrective action closure. | Severity declaration within policy window; chain-of-custody completeness = 100% for forensics artifacts; post-incident corrective actions have owners/dates and no overdue critical closures. | Who: security incident lead + forensic analyst + service owner. What: incident timeline, evidence ledger, post-incident report, closure tracker. Where: incident management system, evidence vault, corrective action board. |
| R7-16 Exception governance and compensating control validity | Security exceptions are time-bound, risk-ranked, and backed by tested compensating controls. | Exception inventory completeness = 100%; expired exceptions = 0; compensating controls tested at approved cadence with pass rate >= 95%; renewal requires updated risk rationale. | Who: security governance lead + risk owner + control owner. What: exception register, compensating control test report, renewal/closure decisions. Where: GRC system, control testing repository, approval records. |

## 3) Scoring anchors table (0/25/50/75/90/100)
Use only `0`, `25`, `50`, `75`, `90`, `100`. No sub-dimension may score above `50` without complete who/what/where evidence, above `75` without independent reviewer validation, or above `90` without successful adversarial challenge evidence from the current cycle.

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R7-01 Threat model completeness and freshness | No usable threat model for critical systems. | Threat model exists for some systems but is stale, missing abuse cases, or lacks owners. | Most critical systems modeled, but mitigation ownership or freshness SLAs are inconsistently met. | All critical systems have current threat models with owned mitigations and no overdue critical actions. | Independent challenge review confirms model assumptions, attack paths, and controls are accurate. | Two consecutive cycles with full coverage, timely refresh, and zero material threat-model gaps discovered post-release. |
| R7-02 Attack surface inventory and exposure drift control | External/internal exposure is unknown; shadow assets unmanaged. | Partial inventory exists but independent scanning regularly finds unmanaged exposure. | Inventory mostly complete; drift detection works but closure discipline is inconsistent. | Inventory is continuously reconciled with ASM; unauthorized exposures are detected and closed within SLA. | Independent recon (DNS, CT logs, cloud account checks) finds negligible unexplained assets. | Two consecutive cycles with no unmanaged exposure lasting beyond policy thresholds. |
| R7-03 Identity and authentication robustness | Privileged access lacks required MFA or strong identity assurance. | MFA and auth controls exist but major privileged/user/service gaps remain. | Baseline auth controls implemented; high-risk identity gaps are known and tracked but not fully closed. | Phishing-resistant MFA and workload identity controls meet policy for critical populations and paths. | Independent adversarial tests (credential theft/replay simulation) show controls resist expected attacks. | Two cycles with sustained policy compliance and no auth-control bypass causing incident impact. |
| R7-04 Authorization and least-privilege integrity | Access is broad/default-allow; entitlement governance absent. | Access policy documented but enforcement and recertification are sporadic. | Core services enforce authorization, but least-privilege drift and stale entitlements persist. | Deny-by-default and periodic entitlement reviews are consistently enforced with timely privilege revocation. | Independent access simulation confirms separation-of-duty and least-privilege boundaries hold under test. | Two cycles with no material privilege creep and clean independent entitlement audits. |
| R7-05 Privileged access and break-glass control discipline | Persistent shared admin access and untracked emergency access are common. | PAM exists but JIT/session audit controls are incomplete or bypassed. | Privileged access is mostly controlled; break-glass review or session traceability is inconsistent. | JIT privileged access, session auditability, and prompt break-glass review are consistently executed. | Independent spot checks confirm no unapproved persistent admin paths and justified break-glass use only. | Two cycles with zero policy-breaking privileged access events and full review completion. |
| R7-06 Secrets, certificates, and key lifecycle controls | Secrets/keys are unmanaged or exposed in code/artifacts. | Managed secret tooling exists but rotation, revocation, or leak response is weak. | Most secrets and certs managed; some rotation SLA misses or legacy unmanaged items remain. | Managed lifecycle controls meet policy with effective leak scanning and expiry prevention. | Independent rotation/revocation challenge demonstrates old credentials no longer grant access. | Two cycles with zero production secret leakage and complete lifecycle SLA adherence. |
| R7-07 Cryptographic posture and data protection enforcement | Deprecated or weak crypto is actively used for sensitive data paths. | Crypto baseline exists but non-compliant protocols/ciphers remain widespread. | Critical paths largely compliant, but exceptions and configuration drift are not consistently controlled. | Approved crypto posture is enforced across critical paths with strong key boundary controls. | Independent protocol and configuration testing confirms absence of weak/deprecated settings. | Two cycles with full compliance and no significant crypto-related finding in audits or tests. |
| R7-08 Vulnerability discovery and triage quality | Vulnerability process is absent or non-functional. | Scanning is incomplete and triage is ad hoc; exploitability not reflected in priority. | Coverage is broad, triage works for major findings, but backlog quality/aging control is inconsistent. | Comprehensive scanning and risk-based triage consistently prioritize exploitable business-critical findings. | Independent sampling confirms low false triage rates and accurate risk ranking decisions. | Two cycles with stable high coverage, timely triage, and no critical blind spots discovered. |
| R7-09 Patch and remediation governance | Critical vulnerabilities remain open without control or escalation. | Remediation SLAs exist but are regularly missed with weak accountability. | Remediation meets minimum baseline for many assets, but high-risk overdue items persist. | Critical and KEV remediation SLAs are met or formally risk-accepted with compensating controls. | Independent re-scan and runtime verification confirm closed findings are actually remediated. | Two cycles with zero unapproved overdue critical findings and consistent remediation proof quality. |
| R7-10 Secure SDLC and adversarial testing depth | Releases bypass security gates and high-risk changes lack security testing. | Some tools run, but they are optional or easily bypassed; test depth is shallow. | Mandatory baseline gates exist; high-risk adversarial testing is inconsistent across teams. | Security gates are enforced and high-risk changes receive targeted adversarial testing before release. | Independent red/purple-team or specialist review validates gate efficacy and test realism. | Two cycles with no critical release lacking required security test evidence. |
| R7-11 Cloud and infrastructure hardening with drift control | Production infrastructure lacks hardening baseline and drift detection. | Hardening standards exist but major misconfigurations persist unresolved. | Baseline controls applied to most environments; remediation timeliness varies. | Hardened baseline and drift controls are enforced with timely closure of high-risk misconfigurations. | Independent cloud posture review confirms policy compliance and effective drift response. | Two cycles with no unresolved critical exposure from infrastructure misconfiguration. |
| R7-12 Supply-chain integrity and artifact provenance | Build/deploy artifacts are unsigned and origin cannot be proven. | Partial signing/SBOM adoption; critical paths still lack provenance guarantees. | Most production artifacts include provenance; enforcement gaps remain in some pipelines. | Provenance, SBOM, and signature verification are enforced end-to-end for production artifacts. | Independent replay verifies policy blocks unsigned/untrusted artifacts and risky dependencies. | Two cycles with complete provenance enforcement and no unauthorized artifact promotion. |
| R7-13 Security telemetry coverage and log integrity | Critical security events are not logged or logs are easily altered. | Logging exists but coverage gaps, ingestion loss, or retention violations are common. | Core telemetry is available, but integrity guarantees and gap monitoring are inconsistent. | Critical event telemetry coverage, integrity controls, and retention requirements are consistently met. | Independent forensic readiness test reconstructs sampled events without material gaps. | Two cycles with sustained coverage/integrity targets and no investigation blocked by telemetry gaps. |
| R7-14 Detection engineering efficacy and containment speed | Security detections are ineffective; major events are discovered late by external parties. | Rule set exists but high false positives/negatives and slow containment persist. | Detection and containment operate at baseline, but ATT&CK coverage and tuning are uneven. | Priority threat detections are tuned and containment SLAs are consistently achieved. | Independent simulation/purple-team exercises confirm reliable detection and timely containment. | Two cycles with strong true-positive quality and no repeat major detection blind spot. |
| R7-15 Security incident command, forensics, and corrective closure | Security incidents are handled ad hoc with broken evidence handling. | Incident process exists, but command discipline or chain-of-custody is frequently incomplete. | Incident records and postmortems are mostly present; corrective closure is uneven and late. | Incident command, forensic integrity, and corrective-action governance are consistently executed. | Independent case review confirms timeline integrity, evidence handling, and corrective effectiveness. | Two cycles with no overdue critical corrective actions and no forensic integrity breach. |
| R7-16 Exception governance and compensating control validity | Exceptions are uncontrolled, indefinite, or undocumented. | Exception register exists but expiries, risk rationale, or control tests are unreliable. | Most exceptions are tracked and time-bound, but compensating control evidence is inconsistent. | All exceptions are current, approved, risk-ranked, and backed by tested compensating controls. | Independent testing validates compensating controls materially reduce accepted risk. | Two cycles with zero expired exceptions and consistent compensation test pass outcomes. |

## 4) Anti-gaming checks specific to this role
1. Recompute vulnerability aging from raw scanner timestamps; reject hand-curated backlog exports that hide reopen dates.
2. Reconcile attack surface inventory against independent DNS zone data, certificate transparency logs, and cloud account enumerations.
3. Verify remediation closure by forced re-scan and runtime validation; reject ticket-only "closed" status.
4. Sample privileged access approvals and compare requested scope vs actual granted permissions in audit logs.
5. Cross-check MFA compliance claims against identity-provider sign-in logs, not dashboard screenshots.
6. Run secret-rotation challenge by attempting access with pre-rotation credentials; failure to revoke means control failure.
7. Validate artifact provenance by replaying verification from source commit to deployed digest on a random production artifact.
8. Audit exception inventory for silently renewed entries and backdated approvals; reject auto-renew without renewed risk decision.
9. Compare detection performance metrics with raw alert/event stream to detect suppression of false positives.
10. Check for rule-disable windows around incidents; require documented approval and post-window re-enable proof.
11. Verify threat-model freshness using commit history timestamps; reject undated documents or bulk timestamp edits.
12. Freeze evidence cut-off at scoring time; any post-cutoff edits require explicit re-review and version diff.

## 5) Tripwires and hard-fail conditions

| ID | Tripwire / hard-fail condition | Effect |
| --- | --- | --- |
| R7-HF1 | Internet-facing critical vulnerability in known-exploited catalog remains unmitigated past policy SLA without approved risk acceptance. | Immediate R7 role FAIL for cycle and release freeze for affected service. |
| R7-HF2 | Privileged production access is possible without required MFA or approved emergency exception. | R7-03 and R7-05 set to 0; emergency access review triggered within 24 hours. |
| R7-HF3 | Confirmed secret/key exposure in production with no completed revocation and rotation containment. | R7-06 set to 0 and affected systems blocked from further release until containment proof. |
| R7-HF4 | Unsigned or unprovenance artifact deployed to production critical path. | R7-12 set to 0; pipeline trust incident opened and promotion permissions suspended. |
| R7-HF5 | Security telemetry for critical auth/admin/data-access events is missing or tampered during an active incident window. | R7-13 capped at 25 and incident handling considered control failure pending forensic review. |
| R7-HF6 | Evidence tampering (altered incident timelines, fabricated scan results, or falsified control tests). | Entire R7 score set to 0 for cycle; formal investigation required. |
| R7-HF7 | High-risk release ships without current threat model and approved mitigation ownership. | R7-01 and R7-10 capped at 25; release governance breach recorded. |
| R7-HF8 | Critical cloud misconfiguration creates public exposure of restricted data and remains open beyond emergency SLA. | R7-11 set to 0 for cycle until verified closure and retrospective control update. |
| R7-HF9 | Expired security exception remains active in production beyond expiry date. | R7-16 set to 0 and associated system risk accepted only by executive override. |
| R7-HF10 | Repeat security incident occurs from previously closed corrective action without evidence of effectiveness test. | R7-15 capped at 25 and corrective-action governance audit mandated. |

## 6) Cross-role dependency and handoff criteria

| Counterpart role | R7 receives (entry criteria) | R7 hands off (exit criteria) | SLA / escalation trigger |
| --- | --- | --- | --- |
| R2 Product Architect / Enterprise Architect | Current system boundary diagrams, data-flow classification, and NFR/security assumptions for new or changed architecture. | Threat model verdict, required control set, and accepted residual-risk record linked to architecture decision. | Escalate if architecture proposal lacks data-flow or trust-boundary detail before design sign-off. |
| R4 Software Engineer | PRs with security-relevant code changes, test artifacts, dependency updates, and endpoint inventory changes. | Actionable remediation findings, secure coding requirements, and pass/fail security gate decision per release. | Escalate within 1 business day for critical exploitable code finding without owner acknowledgement. |
| R6 SRE / Platform Engineer | Runtime telemetry mappings, deployment topology, and incident routing for production services. | Detection onboarding requirements, hardening controls, and incident containment playbooks verified for runtime use. | Escalate immediately for internet-facing exploit indicators or missing critical telemetry at go-live. |
| R12 DevOps / Release Manager | Build provenance metadata, artifact signatures, SBOM, and release candidate manifest. | Security release gate approval/block with explicit failed controls and required fixes. | Escalate if deployment proceeds without successful artifact trust verification evidence. |
| R5 QA / Test Engineer | Functional/non-functional test scope and risk-based release test plans for critical workflows. | Adversarial test scenarios, abuse-case checks, and defect severity classification for security issues. | Escalate when high-risk abuse-case tests are omitted from release test scope. |
| R8 Privacy / Compliance / Legal | Regulatory control obligations, breach-reporting timelines, and data-handling constraints. | Implemented technical control evidence, incident facts, and exception/risk decisions mapped to obligations. | Escalate within 4 hours when incident facts indicate potential statutory notification trigger. |
| R1 Product Manager | Business criticality tiers, launch timelines, and explicit risk tolerance for feature scope. | Security tradeoff decision package: blocked risks, accepted risks, and required launch conditions. | Escalate when delivery date pressure conflicts with unresolved critical security controls. |
| R14 FinOps / Procurement / Vendor Management | Vendor risk assessments, contract security clauses, and third-party dependency criticality. | Technical due-diligence findings, required contractual remediations, and onboarding/no-go recommendation. | Escalate before renewal when critical vendor control gaps remain unresolved past agreed deadline. |
| R15 Internal Audit / Assurance | Audit scope, sampling requirements, and independence criteria for security-scored claims. | Independent-replay package with evidence lineage, gate-state outputs, contradiction closure artifacts, and explicit return metadata. | Escalate immediately when replay/admissibility defects are found in critical security claims; publication blocked until closure. |

## 7) Cycle-level improvement checklist
Use this checklist each scoring cycle (for example: sprint, biweekly security cycle, or monthly governance review).

| Checklist item | Pass criterion | Evidence artifact |
| --- | --- | --- |
| Refresh threat models for changed high-risk systems | All high-risk architecture changes have updated threat models and owned mitigations before release. | Threat-model diff report and mitigation ownership log. |
| Reconcile attack surface inventory | No unmanaged internet-facing asset older than policy threshold. | ASM vs inventory reconciliation export with closure tickets. |
| Validate identity and MFA posture | MFA and workload identity coverage meets policy for privileged and critical service paths. | IdP compliance export and service identity audit. |
| Run entitlement recertification | Monthly privileged entitlement review complete with revocations executed on time. | Recertification attestation pack and IAM revocation log. |
| Test secrets/key rotation and revocation | Rotation schedule met and challenge test proves old credentials are invalid. | Rotation report, revocation test output, cert expiry dashboard snapshot. |
| Verify cryptographic baseline compliance | Runtime and IaC scans show no deprecated crypto configuration on critical paths. | Crypto scan report and approved exception list. |
| Triage and burn down vulnerability backlog | KEV and critical findings triaged/remediated within SLA or formally risk-accepted. | Vulnerability aging dashboard export and acceptance records. |
| Confirm patch deployment effectiveness | Closed patch tickets are validated by re-scan and version verification in production. | Patch verification report and deployment evidence bundle. |
| Validate secure SDLC gates | Required security scanners/tests are enforced and cannot be bypassed in release pipelines. | CI policy config snapshots and failed-gate audit sample. |
| Audit cloud hardening and drift remediation | Critical misconfigurations are remediated within emergency SLA with root-cause prevention ticket. | CSPM findings report, closure times, IaC remediation PR links. |
| Verify supply-chain provenance controls | Production artifacts include SBOM, signature, and attestation with successful verification at deploy. | Artifact trust verification logs and SBOM archive. |
| Exercise detection and containment playbooks | Priority attack simulations trigger detections and containment within target times. | Purple-team exercise results and incident timing metrics. |
| Audit incident forensics and action closure | Security incidents have complete chain-of-custody records and no overdue critical corrective actions. | Incident evidence ledger and corrective action tracker export. |
| Review exception expiries and compensating controls | No expired exceptions; all active exceptions have current compensating control test results. | Exception register diff and control test report. |

## 8) Iteration snapshot admissibility, change control, and anti-gaming enforcement

These controls are mandatory and override weaker language elsewhere in this file.

### 8.1 Mandatory row-level admissibility schema for non-zero security scores

| Field | Required value | Rejection rule |
| --- | --- | --- |
| `who` | Scorer ID, evidence author ID, independent validator ID | Missing field sets row anchor to `0` |
| `what` | Security control/test ID, finding ID, incident ID, exception ID | Missing field sets row anchor to `0` |
| `where` | Immutable evidence location (SIEM query URI, scan artifact URI, ticket URI, repo path) | Missing field sets row anchor to `0` |
| `time` | Evidence capture UTC and scoring UTC | Missing field sets row anchor to `0` |
| `version` | Rubric revision, policy revision, pipeline revision under evaluation | Missing field sets row anchor to `0` |
| `hash` | SHA-256 (or signed digest) for the evidence bundle | Missing field sets row anchor to `0` |

Thresholds:
- completeness for sampled non-zero rows must be `>=95%`;
- completeness for sampled rows scored `>75` must be `>=98%`.

If sampled missing-field defects exceed 10% for non-zero rows, the iteration snapshot is `INVALID` for R7.

### 8.2 Iteration snapshot lock and security delta re-evaluation controls

| Control | Mandatory record | Consequence if violated |
| --- | --- | --- |
| Snapshot lock before scoring | `iteration_id`, `snapshot_id`, security-row hash set, anchor hash, gate hash, cutoff UTC, approvers (`R7`,`R12`,`R15`) | Unlocked scoring is invalid |
| Approved security delta dossier | Change ticket, approved diff, impacted rows, impacted gates, impacted contradiction IDs, approvers | Out-of-process edits invalidate all post-edit scores |
| Targeted security re-evaluation | Re-score all impacted rows and re-simulate impacted gate precedence paths | Publication blocked until complete |
| Unauthorized edit detection | Hash drift without approved dossier | Iteration snapshot marked `INVALID` |

### 8.3 Deterministic precedence and contradiction order

| Rank | Condition | Deterministic outcome |
| --- | --- | --- |
| 1 | Any hard-fail active (`R7-HF1..R7-HF10`) | Immediate `FAIL` |
| 2 | Critical contradiction unresolved past SLA | Publication blocked and affected rows set to `0` |
| 3 | Mandatory anti-gaming step skipped | Affected scope capped at `50`; unresolved at publication => `INVALID` |
| 4 | High-anchor proof missing (`90` or `100`) | Row capped at `75` or `50` based on missing control |
| 5 | No blocking condition active | Compute weighted role score from admissible rows only |

### 8.4 High-anchor challenge and replay gate

| Anchor band | Required proof | Consequence if missing |
| --- | --- | --- |
| `90` | Independent validator + non-author replay parity + same-iteration adversarial challenge evidence | Cap row at `75` and require targeted rescore |
| `100` | Independent validator + non-author replay parity + same-iteration adversarial challenge evidence | Cap row at `50` and reopen adjudication |

### 8.5 Mandatory anti-gaming suite and tripwires

Required controls per iteration snapshot: baseline hash lock check, evidence chronology check, raw-log recompute, adversarial spot check, denominator integrity check, provenance tamper scan, reviewer-independence check, suppression detection check.

| ID | Trigger | Immediate effect | Recovery proof | If unresolved at publication |
| --- | --- | --- | --- | --- |
| `R7-ITW-01` | Any mandatory anti-gaming control skipped | Affected scope capped at `50`; publication blocked | Completed control execution logs plus impacted-row rescoring evidence | Iteration snapshot marked `INVALID` |
| `R7-ITW-02` | Gate-bypass simulation passes despite active security hard gate | R7 scoring halted | Corrected gate logic, rerun simulation evidence, and independent parity confirmation | Iteration snapshot marked `INVALID` |
| `R7-ITW-03` | Reviewer-independence breach on `90`/`100` row | Affected row set to `0` | Reassigned reviewer, independent replay transcript, and corrected score record | Iteration snapshot marked `INVALID` if repeated in sample |

---

## R8 Privacy / Compliance / Legal

- source_file: `swarm_outputs/role_expansions/R8_privacy_compliance_legal.md`
- words: 5082
- lines: 180

# R8 Privacy / Compliance / Legal Rubric Expansion

## 1) Role mission and decision rights
R8 exists to convert privacy, compliance, and legal obligations into enforceable operational controls and binding release decisions. R8 is accountable for preventing unlawful processing, proving compliance under independent audit, and stopping delivery when legal risk exceeds approved tolerance.

R8 decision rights are binding for legal/compliance gates and high-risk exceptions.

| Decision domain | R8 authority | Non-delegable constraint | Required decision record |
| --- | --- | --- | --- |
| Obligation applicability and control scope | Determine which statutes, regulations, contractual clauses, and policy obligations apply; require control owner assignment | No applicable obligation may remain unmapped to a control and owner past SLA | Obligation register version, mapping matrix, owner list, approval timestamp |
| Lawful basis and purpose approval | Approve or block processing purpose, lawful basis model, and prohibited-use boundaries | No production processing of personal data without documented lawful basis/purpose mapping | Purpose register, lawful basis memo, legal sign-off ticket |
| Consent and notice operating model | Approve consent states, withdrawal behavior, and notice text-to-system mapping | No consent-gated processing before valid consent event is recorded and retrievable | Consent state model, notice version, propagation test evidence |
| Retention and legal hold policy | Set retention clocks, destruction obligations, and legal hold exception handling | No expired regulated data may persist without documented legal hold | Retention schedule, hold register, deletion verification report |
| Transfer and localization controls | Approve cross-border transfer mechanism, residency boundaries, and processor conditions | No restricted data transfer without approved mechanism and jurisdiction check | Transfer impact assessment, contract clause evidence, approval record |
| DSAR response model | Define intake, identity proofing, response package, and SLA clocks | No verified rights request may miss statutory deadline without approved legal extension basis | DSAR tracker, identity verification log, fulfillment package |
| Breach reportability and notification decision | Declare reportability path and mandatory internal/external notifications | No confirmed reportable incident may pass notification deadline | Incident legal assessment, clock log, notification approvals |
| Compliance exception acceptance | Approve, reject, or expire compliance exceptions and compensating controls | No indefinite exception; all exceptions must be time-bound and tested | Exception register entry, compensating control test, expiry decision |
| Release veto for legal/compliance blockers | Block release where unresolved legal/compliance tripwire exists | Release cannot proceed on executive pressure alone when hard-fail criteria are met | Gate decision artifact, blocker list, escalation thread |

### Iteration snapshot governance and admissibility controls

| Control | Requirement | Deterministic enforcement |
| --- | --- | --- |
| Iteration snapshot lock | Before scoring begins, record `iteration_id`, rubric snapshot hash, role file hash, and scorer roster. | Any score computed on an unapproved snapshot hash is invalid for the iteration. |
| Scoring denominator lock | Record the row population denominator at snapshot time. | Any denominator change requires approved delta dossier and dual reporting (`before`/`after`) in the same iteration. |
| Delta dossier and targeted re-evaluation | Any in-iteration scoring logic or evidence-rule change must include impacted rows, impacted gates, owner, approvers, and rationale. | Impacted rows are rescored and impacted gates/contradictions are replayed before publication. |
| Unauthorized drift tripwire | Detect edits to rubric/anchors/gates after snapshot without approval chain. | Role output is marked invalid for publication until rollback or approved delta re-evaluation is complete. |

### Non-zero evidence admissibility contract (mandatory fields)

| Field | Requirement for non-zero scoring | Rejection behavior when missing/invalid |
| --- | --- | --- |
| `who` | Named accountable actor and reviewer identity | Row ineligible for score above `0` |
| `what` | Concrete claim or control test outcome | Row ineligible for score above `0` |
| `where` | Immutable locator for evidence artifact | Row ineligible for score above `0` |
| `time_utc` | Capture timestamp in UTC | Row ineligible for score above `0` |
| `version` | Version/snapshot identifier of control, policy, or artifact | Row ineligible for score above `0` |
| `hash` | Integrity hash for evidence or source bundle | Row ineligible for score above `0` |
| `provenance_chain` | Source lineage showing system-of-record to scored claim linkage | Row ineligible for score above `0` |

| Admissibility sampling rule | Threshold | Deterministic effect |
| --- | --- | --- |
| Sampled non-zero rows missing any required field | `>5%` | Cap affected sub-dimension at `50` and require targeted re-score |
| Sampled non-zero rows missing `time_utc`/`version`/`hash`/`provenance_chain` | `>10%` | Set R8 role score to `0` for the iteration pending full evidence remediation |

### Contradiction precedence protocol (deterministic)

| Contradiction class | Precedence order | Owner | SLA | Score and gate consequence |
| --- | --- | --- | --- | --- |
| Legal/privacy mandatory-control conflict | Highest | R8 with R8+R7 co-sign | 1 business day | Publication blocked; unresolved state forces overall FAIL via `G3` |
| Statutory timeline conflict (DSAR/notification) | High | R8 legal owner | 24 hours | Related row set to `0`; unresolved state blocks publication |
| Contract claim vs runtime behavior conflict | Medium | R8 + R1 | 2 business days | Claim-related rows capped at `25` until contradiction closure evidence is attached |
| Exception expiry vs delivery deadline conflict | Medium | R8 + R12 | 1 business day | Expired-exception rows set to `0`; release veto remains active |

## 2) Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| R8-01 Obligation-to-Control Mapping Integrity | All applicable privacy/compliance/legal obligations are mapped to preventive and detective controls with accountable owners. | Applicable obligation coverage = 100%; critical unmapped obligations older than 5 business days = 0; monthly independent sample re-performance mismatch rate < 2%. | Who: compliance lead, legal counsel, control owner. What: obligation register, control mapping, sampled re-performance notes. Where: GRC system, control library repo, ticketing system. |
| R8-02 Regulatory Change Intake and Impact Assessment | Legal/regulatory changes are detected, triaged, translated into implementation actions, and closed before effective dates. | New applicable changes triaged within 5 business days; overdue legal-change implementation tasks = 0; effective-date readiness attestations complete for 100% applicable changes. | Who: legal ops analyst, compliance manager, product/control owner. What: change bulletin log, impact memo, implementation plan. Where: legal watchlist feed, GRC change module, planning board. |
| R8-03 Lawful Basis and Purpose Limitation Governance | Each processing activity has explicit lawful basis, purpose boundaries, and prohibited secondary uses enforced in design and runtime. | Processing activities with approved lawful basis = 100%; unauthorized purpose use findings = 0; quarterly sample of events shows purpose tag consistency >= 98%. | Who: privacy counsel, data steward, engineering owner. What: processing register, lawful basis rationale, purpose-tag audit results. Where: RoPA repository, schema registry, audit log store. |
| R8-04 Consent Capture, Versioning, and Withdrawal Propagation | Consent states are granular, versioned, and propagated to all processing systems within policy SLA after grant/withdrawal. | Consent event completeness for consent-required processing = 100%; withdrawal propagation SLA success >= 99%; synthetic withdrawal unauthorized-processing findings = 0. | Who: consent product owner, privacy engineer, QA auditor. What: consent ledger, version history, propagation test logs. Where: consent service DB, event bus logs, downstream processor logs. |
| R8-05 Notice-to-Practice Fidelity | Public/internal notices accurately reflect real data collection, use, sharing, retention, and rights handling behavior. | Notice drift findings older than 10 business days = 0; quarterly notice-vs-telemetry diff run completion = 100%; material mismatch recurrence trend decreases cycle-over-cycle. | Who: legal writer, privacy counsel, telemetry owner. What: notice diff report, remediation tickets, approved notice versions. Where: policy repo, telemetry catalog, publishing CMS. |
| R8-06 Data Inventory, Classification, and Processing Records | Personal and regulated data assets are fully inventoried, classified, and linked to processing context, owners, and controls. | Classified regulated stores coverage = 100%; unknown personal-data store findings older than 7 days = 0; sampled field classification accuracy >= 98%. | Who: data governance lead, platform owner, compliance reviewer. What: data inventory export, classification tags, sampling report. Where: CMDB/data catalog, schema registry, warehouse metadata store. |
| R8-07 Processor / Vendor DPA and Subprocessor Governance | Third parties processing regulated data are contractually and operationally controlled through DPAs, risk reviews, and subprocessor transparency. | Critical processors with current DPA/risk review = 100%; unapproved subprocessors = 0; overdue vendor reassessments = 0. | Who: vendor manager, legal counsel, security/compliance assessor. What: DPA records, risk assessments, subprocessor list approvals. Where: contract lifecycle tool, vendor risk platform, procurement system. |
| R8-08 Cross-Border Transfer and Jurisdiction Control | Data movement across jurisdictions follows approved legal mechanisms, residency constraints, and transfer-impact safeguards. | Transfer inventory completeness = 100%; unauthorized cross-border transfers = 0; transfer mechanism renewal before expiry = 100%. | Who: privacy counsel, cloud/platform owner, regional compliance lead. What: transfer register, mechanism approvals, boundary test logs. Where: data-flow maps, cloud region policy configs, legal repository. |
| R8-09 Retention Schedule Enforcement and Legal Hold Discipline | Retention clocks and destruction controls are enforced across stores; legal holds are explicit, approved, and reversible. | Expired records without legal hold = 0 in sampled systems; legal hold approvals include scope/date/reviewer = 100%; deletion verification across primary+replica+analytic stores success >= 98%. | Who: records manager, legal counsel, data platform owner. What: retention matrix, hold register, deletion evidence. Where: records policy system, storage logs, deletion job reports. |
| R8-10 DSAR Intake, Identity Verification, and Fulfillment Quality | Rights requests are received, identity-verified, fulfilled accurately, and completed within statutory timelines. | Statutory deadline compliance >= 99%; identity verification failure escape rate = 0; fulfillment quality audit defect rate < 2%. | Who: privacy operations lead, customer operations, legal reviewer. What: DSAR tracker, ID verification logs, response package QA audits. Where: DSAR platform, CRM/case system, evidence archive. |
| R8-11 Breach Triage, Materiality Determination, and Notification Timeliness | Incident facts are rapidly assessed for legal reportability, with jurisdictional clock control and documented notification decisions. | Reportability decision within 24 hours of confirmation for 100% qualifying incidents; missed notification deadlines = 0; semiannual notification drill completion = 100%. | Who: incident commander, privacy/legal counsel, security lead. What: incident timeline, materiality worksheet, notification approval chain. Where: incident response platform, legal decision log, regulator notice archive. |
| R8-12 Contractual, Sectoral, and Marketing Claims Compliance | Product commitments and external claims comply with contracts, sector rules, and advertising/privacy representations. | Material claim-to-control mismatches = 0; contract obligation test pass rate >= 98%; blocked non-compliant launch claims tracked to closure. | Who: commercial counsel, product marketing owner, compliance reviewer. What: claims register, contract control tests, launch approval notes. Where: contract repository, release checklist system, marketing CMS. |
| R8-13 Audit Defensibility and Evidence Integrity | Compliance conclusions are reproducible from immutable, timestamped evidence with clear chain-of-custody. | Evidence integrity verification pass rate = 100%; unsupported non-zero scores = 0; requested audit evidence retrieval within SLA (for example 2 business days) >= 98%. | Who: compliance assurance lead, internal audit liaison, evidence custodian. What: evidence manifest, hash/signature records, retrieval logs. Where: evidence vault, version-controlled repo, audit ticket system. |
| R8-14 Exception Governance and Compensating Controls | Exceptions are risk-ranked, time-bound, narrowly scoped, and backed by tested compensating controls. | Expired exceptions = 0; exceptions lacking compensating control test in current cycle = 0; extension approvals with updated rationale = 100%. | Who: compliance governance lead, risk owner, control tester. What: exception register, test reports, extension decisions. Where: GRC exceptions module, control testing repo, approval workflow system. |
| R8-15 Privacy/Compliance Training and Delegated Authority Competence | Role-specific training, certification, and decision authority boundaries are current for staff making compliance-impacting decisions. | Required training completion = 100% for privileged decision roles; failed certification retake closure within SLA >= 95%; unauthorized approver actions = 0. | Who: training owner, line manager, compliance lead. What: completion reports, certification results, authority matrix attestations. Where: LMS, HRIS, approval audit logs. |
| R8-16 Enforcement Escalation and Release Veto Effectiveness | Escalation paths are used promptly, and legal/compliance veto decisions are enforced without bypass. | Compliance hard-block bypasses = 0; escalation acknowledgment within 4 business hours for critical blockers >= 99%; repeat blocker recurrence declines cycle-over-cycle. | Who: compliance lead, release manager, executive sponsor. What: gate decisions, escalation timeline, recurrence analysis. Where: release governance board records, incident/escalation tracker, decision log. |

## 3) Scoring anchors table (0/25/50/75/90/100)
No sub-dimension may score above `50` without complete who/what/where/time/version/hash evidence, above `75` without independent reviewer validation, or above `90` without both same-iteration adversarial challenge evidence and non-author replay of affected rows.

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R8-01 Obligation-to-Control Mapping Integrity | No maintained obligation map; ownership absent. | Partial map exists, but critical obligations are missing or stale. | Core obligations mapped with named owners; repeated sample mismatches remain. | All applicable obligations mapped to active controls; critical gaps closed within SLA. | Independent legal/audit re-performance confirms mapping accuracy and owner accountability. | Two consecutive cycles with zero critical unmapped obligations and no material mapping finding. |
| R8-02 Regulatory Change Intake and Impact Assessment | No structured legal-change intake process. | Intake exists but changes are triaged late and effective dates are missed. | Applicable changes usually tracked, but implementation closure is inconsistent. | Applicable changes are triaged on time and implemented before effective date. | Independent sample verifies correct applicability decisions and timely implementation closure. | Two cycles with zero overdue applicable legal changes and no emergency retrofits. |
| R8-03 Lawful Basis and Purpose Limitation Governance | Processing occurs without documented lawful basis/purpose control. | Lawful basis documented for some flows; major gaps or prohibited secondary use findings persist. | Primary flows have basis/purpose mapping; edge flows and enforcement are inconsistent. | All processing activities have approved basis/purpose and prohibited-use enforcement. | Independent event-log sample confirms purpose tags and runtime behavior alignment. | Two cycles with no unauthorized purpose use and no material lawful-basis defect. |
| R8-04 Consent Capture, Versioning, and Withdrawal Propagation | Consent-required processing occurs without retrievable consent evidence. | Consent capture exists but versioning or withdrawal propagation often fails SLA. | Core consent flows work; downstream propagation gaps still appear in edge systems. | Granular consent states are versioned and withdrawals propagate within SLA across systems. | Independent synthetic withdrawal tests confirm no unauthorized post-withdrawal processing. | Two cycles with sustained withdrawal SLA performance and zero critical consent-control escapes. |
| R8-05 Notice-to-Practice Fidelity | Notices materially misrepresent actual collection/use/sharing behavior. | Notice updates happen reactively; significant drift remains unresolved. | Core notices align, but periodic drift findings recur in some surfaces. | Notice-to-practice comparisons run regularly and material mismatches are resolved promptly. | Independent reviewer validates notice text against telemetry and product behavior samples. | Two cycles with no material notice drift and no regulator/customer correction event. |
| R8-06 Data Inventory, Classification, and Processing Records | Regulated data stores are unknown or unclassified. | Inventory exists but coverage is partial with recurring shadow stores. | Most regulated stores are classified; field-level accuracy and ownership are inconsistent. | Full regulated-store coverage with high classification accuracy and owned records. | Independent sampling confirms classification integrity and accurate processing records. | Two cycles with sustained 100% regulated-store classification and no unknown-store finding older than SLA. |
| R8-07 Processor / Vendor DPA and Subprocessor Governance | Critical processors operate without DPA or risk review. | DPA/risk process exists but coverage gaps and expired reviews persist. | Most critical vendors are governed; subprocessor transparency and refresh cadence are uneven. | Critical processors have current DPA/risk evidence and subprocessor approvals. | Independent contract/risk sample confirms governance completeness and control follow-through. | Two cycles with zero critical vendor governance lapses and no unauthorized subprocessor. |
| R8-08 Cross-Border Transfer and Jurisdiction Control | Cross-border transfers occur without approved legal mechanism. | Transfer controls exist on paper; inventory and boundary enforcement are incomplete. | Major transfers are controlled; edge transfers and expiry renewals are inconsistently handled. | Transfer inventory is complete and all transfers use current approved mechanisms. | Independent boundary test and contract sample confirm jurisdiction control effectiveness. | Two cycles with zero unauthorized transfers and no expired transfer mechanism in use. |
| R8-09 Retention Schedule Enforcement and Legal Hold Discipline | Expired regulated data persists with no lawful hold rationale. | Retention schedule exists but deletion execution and hold governance are unreliable. | Core stores enforce retention; replica/analytic deletion and hold metadata are inconsistent. | Retention and deletion work across stores; legal holds are explicit, approved, and reviewed. | Independent seeded-record test confirms deterministic deletion/hold behavior across systems. | Two cycles with no unjustified expired regulated data and complete hold audit trails. |
| R8-10 DSAR Intake, Identity Verification, and Fulfillment Quality | Verified rights requests are not handled or routinely miss legal deadlines. | DSAR process exists but deadline misses and identity-verification defects are common. | Core DSAR workflows function; surge handling and response accuracy are inconsistent. | Statutory deadlines are met and fulfillment packages are accurate and complete. | Independent synthetic DSAR sample confirms identity proofing and response fidelity. | Two cycles with sustained deadline compliance and zero material DSAR quality finding. |
| R8-11 Breach Triage, Materiality Determination, and Notification Timeliness | Reportable incidents lack legal triage and notification clock control. | Triage occurs inconsistently; reportability decisions are late or weakly documented. | Core incident triage works; multi-jurisdiction timing and drill performance vary. | Reportability and notifications are timely, documented, and exercised through drills. | Independent drill and incident sample confirm timeline accuracy and legal decision quality. | Two cycles with zero missed mandatory notifications and no unresolved materiality dispute. |
| R8-12 Contractual, Sectoral, and Marketing Claims Compliance | Product/marketing claims contradict contractual or sector legal obligations. | Claim review exists but high-risk claims launch without verified compliance evidence. | Major claims are reviewed; edge claims and contract test coverage are incomplete. | Claims and contractual obligations are tested and enforced before launch approval. | Independent counsel/compliance sample validates claim-to-control traceability. | Two cycles with no material claim-compliance incident and full high-risk claim pre-clearance. |
| R8-13 Audit Defensibility and Evidence Integrity | Evidence is missing, mutable, or cannot support conclusions. | Evidence exists but provenance, completeness, or retrieval timeliness is poor. | Most evidence is reproducible; some chain-of-custody or retrieval gaps remain. | Evidence is immutable, indexed, and sufficient for independent re-performance. | Independent audit replay reproduces scores/decisions from evidence without discrepancy. | Two cycles with zero evidence-integrity exceptions and clean independent assurance outcome. |
| R8-14 Exception Governance and Compensating Controls | Exceptions are undocumented, indefinite, or untested. | Exceptions are tracked but expiries, rationale, or compensating tests are inconsistent. | Most exceptions are time-bound; some stale extensions or weak compensating evidence remain. | All exceptions are current, risk-ranked, and backed by passing compensating tests. | Independent challenge confirms compensating controls materially reduce accepted risk. | Two cycles with zero expired active exceptions and no untested compensating control. |
| R8-15 Privacy/Compliance Training and Delegated Authority Competence | Decision-makers lack required training/certification and authority boundaries. | Training program exists but completion gaps and unauthorized approvals occur. | Required roles mostly trained; recertification lag and decision-quality drift remain. | Role-based training/certification and authority matrix are current and enforced. | Independent sample confirms approvers are authorized and decisions meet policy quality bar. | Two cycles with full completion, zero unauthorized approvals, and stable decision quality. |
| R8-16 Enforcement Escalation and Release Veto Effectiveness | Legal/compliance blockers are bypassed and release vetoes are not enforceable. | Escalation path exists but critical issues are delayed or overridden without process. | Vetoes usually hold; occasional late escalation or recurrence weakens control. | Critical blockers escalate on time and release vetoes are enforced until closure. | Independent governance review confirms no improper bypass and strong recurrence control. | Two cycles with zero hard-block bypasses and measurable reduction in repeat blocker classes. |

## 4) Anti-gaming checks specific to this role
1. Recompute DSAR SLA from raw intake and completion timestamps; reject manually edited status fields.
2. Run synthetic consent withdrawal events and inspect downstream logs for any post-withdrawal processing.
3. Compare published notices to actual telemetry schemas and event payloads; flag undeclared data elements.
4. Independently enumerate storage systems and compare to declared data inventory to detect shadow stores.
5. Rebuild obligation-to-control mapping from primary legal text samples; compare with GRC map for omissions.
6. Sample vendor payments and data-access logs to detect processors absent from DPA/subprocessor registers.
7. Replay cross-border flows using network and cloud region logs; verify claimed residency boundaries.
8. Seed expiring records and test deletion across primary, replica, cache, and analytics surfaces.
9. Validate legal hold scope by checking hold IDs against actual excluded deletion records.
10. Reconstruct breach-notification clocks from incident raw timestamps, not post-incident summaries.
11. Audit exception renewals for backdated approvals and unchanged risk rationale across cycles.
12. Verify evidence immutability by checking hash/signature chain and edit history against manifest timestamps.
13. Lock iteration snapshot hash and denominator before scoring; reject unapproved in-iteration drift.
14. Require approved delta dossier for any scoring-rule update and rerun impacted-row replay before publication.
15. For every proposed `90` or `100`, run an adversarial challenge and a non-author replay on the same row set.

## 5) Tripwires and hard-fail conditions

| ID | Tripwire / hard-fail condition | Effect |
| --- | --- | --- |
| R8-HF1 | Personal/regulated data processing in production without documented lawful basis or required consent. | Immediate R8 FAIL; affected processing must be stopped or isolated before release continues. |
| R8-HF2 | Verified statutory DSAR deadline missed without lawful extension basis and legal approval. | R8-10 set to `0`; release/change freeze for implicated workflow until corrective controls are proven. |
| R8-HF3 | Unauthorized cross-border transfer of restricted data or use of expired transfer mechanism. | R8-08 set to `0`; mandatory incident and regulator-readiness review triggered. |
| R8-HF4 | Missed mandatory legal/regulatory breach notification deadline. | R8-11 set to `0`; cycle marked fail regardless of other sub-dimension scores. |
| R8-HF5 | Critical processor handles regulated data without executed DPA or required risk assessment. | R8-07 capped at `25`; new data sharing with that processor blocked until closure. |
| R8-HF6 | Expired regulated data retained without approved legal hold justification in sampled critical system. | R8-09 set to `0`; deletion/hold controls require emergency remediation and re-test. |
| R8-HF7 | Material notice-to-practice mismatch persists beyond remediation SLA. | R8-05 capped at `25`; public claims freeze until corrected notice and control evidence exist. |
| R8-HF8 | Evidence tampering, fabricated legal sign-off, or unverifiable compliance artifact discovered. | Entire R8 role score set to `0`; formal investigation and re-audit required. |
| R8-HF9 | Compliance hard-block release veto bypassed without documented governance override authority. | R8-16 set to `0`; release governance nonconformance escalated to executive sponsor and audit. |
| R8-HF10 | Applicable new legal requirement reaches effective date with no implemented control or approved temporary measure. | R8-02 and R8-01 capped at `25`; affected scope cannot be promoted. |

### Tripwire detection and minimum recovery proof

| ID | Detection rule | Minimum recovery proof before publication |
| --- | --- | --- |
| R8-HF1 | Runtime audit shows production processing without lawful basis/consent artifact set | Verified processing stop or lawful-basis/consent remediation evidence plus independent replay of affected rows |
| R8-HF2 | DSAR raw timestamp recomputation confirms missed statutory deadline without lawful extension | Corrected DSAR workflow controls, legal extension policy proof, and sampled replay passing statutory-clock checks |
| R8-HF3 | Transfer logs show unauthorized transfer or expired mechanism usage | Transfer containment evidence, mechanism renewal/approval record, and boundary-test replay |
| R8-HF4 | Incident timeline confirms missed mandatory notification deadline | Corrected notification clock controls, drill evidence, and legal approval-chain replay |
| R8-HF5 | Vendor register and payment/access logs show critical processor missing DPA/risk review | Executed DPA/risk review artifacts and independent onboarding-governance recheck |
| R8-HF6 | Seeded-record deletion test finds expired regulated data without legal hold basis | Verified deletion/hold remediation across primary+replica+analytics and reseeded test pass report |
| R8-HF7 | Notice-to-telemetry diff shows material mismatch beyond SLA | Published corrected notice, remediation closure records, and telemetry-diff rerun pass |
| R8-HF8 | Forensic hash/signature audit finds evidence tamper/fabrication | Forensic closure memo, rebuilt immutable evidence chain, and full independent re-score of impacted rows |
| R8-HF9 | Gate logs show release veto bypass without authority chain | Governance correction record, restored veto enforcement control, and gate-state recomputation parity |
| R8-HF10 | Legal change reached effective date without implemented control or temporary measure | Implemented control evidence or approved temporary measure with expiry plus targeted re-score of affected obligations |

## 6) Cross-role dependency and handoff criteria

| Counterpart role | R8 receives (entry criteria) | R8 hands off (exit criteria) | SLA / escalation trigger |
| --- | --- | --- | --- |
| R1 Product Manager | Feature intent, user segment, data-use objectives, and launch date with jurisdiction list. | Approved lawful-basis/purpose constraints, notice/consent requirements, and legal launch conditions. | Escalate within 1 business day if launch scope lacks data-use purpose clarity. |
| R2 Product Architect / Enterprise Architect | Current data-flow diagrams, system boundaries, and storage/transfer architecture for changed scope. | Compliance control requirements mapped to architecture decisions and residual legal risk statements. | Escalate before design sign-off if data-flow lineage or residency assumptions are missing. |
| R4 Software Engineer | Implementation design and telemetry schema for data collection, consent checks, and deletion routines. | Control acceptance criteria, legal test cases, and pass/fail compliance gate decision for release. | Escalate immediately for code paths enabling collection/processing outside approved purpose. |
| R6 SRE / Platform Engineer | Runtime topology, region deployment model, backup/restore behavior, and log retention configs. | Retention/hold/deletion operational requirements, residency guardrails, and evidence logging requirements. | Escalate within 4 business hours if platform settings conflict with retention or residency mandates. |
| R7 Security Engineer / Security Architect | Incident facts, threat model outputs, and technical control status for privacy-impacting events. | Reportability decisions, breach notification obligations, and legal clock milestones. | Escalate within 2 hours for incident signals likely to trigger statutory notifications. |
| R12 DevOps / Release Manager | Release candidate manifest, gate results, and exception list with approvers and expiries. | Final legal/compliance go/no-go decision and blocker closure evidence requirements. | Escalate if promotion is attempted with unresolved R8 hard-fail item. |
| R14 FinOps / Procurement / Vendor Management | New/renewing vendor list with data-access scope, contract drafts, and risk tiering. | DPA/contract clause requirements, approved processor status, and restricted-use conditions. | Escalate before purchase order execution when regulated data processor lacks required terms. |
| R15 Internal Audit / Assurance | Audit plan, sample requests, prior findings, and remediation status baseline. | Evidence manifest, reproducible scoring basis, and closed-loop remediation proof. | Escalate if requested critical evidence cannot be produced within agreed audit SLA. |

## 7) Iteration-level improvement checklist
Use each scoring iteration (sprint/month/quarter per governance cadence).

| Checklist item | Pass criterion | Evidence artifact |
| --- | --- | --- |
| Lock iteration snapshot hash and denominator | Snapshot hash, denominator, and scorer roster are recorded before first score. | Snapshot lock manifest and approval record. |
| Process approved delta dossier before any re-score | Every scoring-affecting change has impacted-row map and approver chain. | Delta dossier with impacted rows/gates and approvals. |
| Rerun targeted re-evaluation after approved delta | All impacted rows plus gate/contradiction outcomes are replayed before publication. | Targeted re-score and gate replay report. |
| Refresh obligation register and mappings | All new/changed obligations mapped with control owner and due dates. | Obligation diff report and approved mapping updates. |
| Run regulatory horizon scan and triage | Applicable legal changes triaged within SLA with impact owner assigned. | Change intake log with timestamps and assignments. |
| Re-validate lawful basis and purpose tags | No new processing activity lacks approved basis/purpose link. | RoPA/purpose register diff and approval tickets. |
| Execute consent withdrawal propagation test | Synthetic withdrawals block downstream processing within policy SLA. | Test run logs and downstream processor verification report. |
| Perform notice-to-telemetry drift review | All material notice mismatches have remediation owner/date. | Drift report and closure tracker. |
| Reconcile data inventory/classification coverage | Regulated stores remain fully classified; shadow-store backlog at zero past SLA. | Catalog reconciliation export and closure evidence. |
| Verify processor DPA and subprocessor status | Critical processors have current DPA/risk assessment and approved subprocessors. | Vendor compliance dashboard export and contract records. |
| Validate cross-border transfer controls | No transfer occurs without current mechanism and approved jurisdictional conditions. | Transfer registry, mechanism validity check, boundary test output. |
| Test retention/deletion with legal hold exceptions | Seeded expired records deleted correctly except approved holds. | Deletion verification report and hold exception log. |
| Audit DSAR throughput and quality | Deadline compliance and response accuracy meet targets for sampled cases. | DSAR KPI report and response QA sample file. |
| Rehearse breach reportability workflow | Drill meets decision and notification timing requirements by jurisdiction. | Drill timeline report and legal approval trail. |
| Review external claims and contractual obligations | High-risk claims/contracts pass compliance checks before launch/renewal. | Claims-control checklist and contract compliance test records. |
| Verify evidence integrity and retrieval readiness | Evidence hashes/signatures validate; retrieval SLA met for sampled requests. | Evidence manifest verification log and retrieval audit report. |
| Clean up exceptions and retest compensating controls | No expired exceptions; all active exceptions have current passing test evidence. | Exception register diff and compensating control test pack. |
| Validate authority matrix and training completion | All required approvers are authorized and current on role-specific training. | LMS completion export and authority attestation log. |
| Review veto/escalation outcomes and recurrence | No hard-block bypass; repeat blocker classes have corrective actions with owners. | Gate decision summary and recurrence analysis report. |

---

## R9 Data / AI Engineer or Scientist

- source_file: `swarm_outputs/role_expansions/R9_data_ai_engineer_scientist.md`
- words: 4509
- lines: 201

# R9 Data / AI Engineer or Scientist Rubric Expansion

## Role mission and decision rights

**Role mission**
R9 is accountable for producing data and model outputs that are statistically valid, operationally reliable, reproducible, and safe for real-world decisions. The role owns technical truthfulness of data and model claims across development, evaluation, deployment, and post-release monitoring.

**Decision rights**

| Decision area | R9 authority | Required co-approval | Escalation trigger |
| --- | --- | --- | --- |
| Training data inclusion/exclusion | Final decision on dataset fitness and exclusion rules | R8 for regulated/sensitive attributes | Any unresolved legal/privacy objection or unknown data origin |
| Feature definitions and transformations | Final decision on feature logic, leakage controls, and lineage links | R2 when feature affects shared architecture contracts | Feature breaks contract or creates cross-system schema drift |
| Model family and objective function selection | Final decision on model class and optimization target | R1 when objective changes business KPI definition | Objective conflicts with approved KPI/OKR or policy constraints |
| Offline evaluation thresholds | Final decision on metric suite and minimum pass thresholds | R5 for test protocol integrity | Thresholds weakened after poor results without approved rationale |
| Promotion to staging/production recommendation | Can recommend go/no-go with evidence package | R12 for release execution, R6 for runtime readiness | Missing rollback proof, missing monitoring, or unresolved Sev-1 risks |
| Drift/bias incident mitigation | Can trigger model rollback, traffic reduction, or kill-switch | R6 for operational execution, R7/R8 when risk has security/privacy dimension | Harmful drift, discriminatory impact, or unexplained severe degradation |
| Experiment design and readout | Final decision on experiment method, power, and guardrails | R1 for user/business impact interpretation | Experiment materially impacts users without pre-registered safeguards |
| Retention of model/data artifacts | Final decision on technical retention for reproducibility | R8 for policy and statutory retention requirements | Conflict between reproducibility need and legal retention limits |

### Iteration snapshot governance and delta re-evaluation controls

| Control | Requirement | Deterministic enforcement |
| --- | --- | --- |
| Iteration snapshot lock | Record `iteration_id`, rubric snapshot hash, role file hash, and scorer roster before first score. | Scores produced on an unapproved snapshot hash are invalid for publication. |
| Denominator lock | Lock scored-row population and critical segment list at snapshot time. | Any denominator/segment change requires approved delta dossier and dual reporting (`before`/`after`). |
| Approved delta dossier | Any in-iteration scoring-rule or anchor change must include impacted rows, impacted gates, owner, approvers, and rationale. | All impacted rows and gates are rescored/replayed before publication. |
| Unauthorized drift tripwire | Detect anchor/weight/gate edits without authority chain. | Role result is held invalid until rollback to snapshot or approved delta re-evaluation completes. |

### Non-zero evidence admissibility contract (mandatory fields)

| Field | Requirement for non-zero scoring | Rejection behavior when missing/invalid |
| --- | --- | --- |
| `who` | Named accountable actor and reviewer | Row ineligible for score above `0` |
| `what` | Specific model/data claim or control test result | Row ineligible for score above `0` |
| `where` | Immutable evidence locator | Row ineligible for score above `0` |
| `time_utc` | UTC capture timestamp | Row ineligible for score above `0` |
| `version` | Model/data/code snapshot version ID | Row ineligible for score above `0` |
| `hash` | Integrity hash for evidence bundle | Row ineligible for score above `0` |
| `provenance_chain` | Source lineage showing raw data/model artifacts to scored claim linkage | Row ineligible for score above `0` |

| Admissibility sampling rule | Threshold | Deterministic effect |
| --- | --- | --- |
| Sampled non-zero rows missing any required field | `>5%` | Cap affected sub-dimensions at `50` and require targeted re-score |
| Sampled non-zero rows missing `time_utc`/`version`/`hash`/`provenance_chain` | `>10%` | Set R9 role score to `0` for the iteration pending full remediation |

### Contradiction precedence protocol for data/AI tradeoffs

| Contradiction class | Precedence order | Owner | SLA | Score and gate consequence |
| --- | --- | --- | --- | --- |
| Safety/privacy/security/legal vs model performance | Highest | R9 + R7/R8 co-sign | 1 business day | Publication blocked; unresolved state forces FAIL via `G3` |
| Fairness disparity vs aggregate accuracy gain | High | R9 + R8 | 1 business day | Related fairness/performance rows capped at `50` until mitigation or formal waiver closes |
| Reproducibility requirements vs retention constraints | High | R9 + R8 | 2 business days | Claims above `75` blocked until admissible reproducibility path is documented |
| Latency/cost optimization vs reliability/safety thresholds | Medium | R9 + R6/R12 | 2 business days | Release-gating row set to `0` when thresholds are breached without approved exception |

### High-anchor (`90`/`100`) authorization gate

| Requirement for any `90` or `100` | Mandatory evidence | Deterministic consequence if missing |
| --- | --- | --- |
| Independent validator (non-author) | Independent review record tied to row evidence IDs | Row capped at `75` |
| Same-iteration adversarial challenge | Challenge design, execution log, and outcome for the claimed row set | Row capped at `75` and targeted re-score required |
| Non-author replay parity | Replay shows anchor parity and gate-state parity on affected rows | Row capped at `75`; release recommendation for affected scope is void until replay passes |

## Sub-dimensions

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| 1. Data source contract integrity | Upstream sources have explicit, versioned schemas and ownership; breaking changes are controlled. | Contract test pass rate; unannounced schema-break count; source owner acknowledgment latency. | Who: source owner + R9 reviewer. What: signed schema contract, change log, contract test results. Where: data catalog, repo CI logs, ticket system. |
| 2. Ingestion completeness and freshness | Pipelines ingest required records on time with bounded lag and loss. | Freshness SLA attainment; missing-partition rate; late-arrival reconciliation success. | Who: pipeline owner. What: ingestion dashboard exports, reconciled counts, SLA report. Where: orchestration logs, warehouse audit tables. |
| 3. Data quality validation and anomaly triage | Data quality checks detect null spikes, distribution shifts, and rule violations; anomalies are triaged to closure. | Critical rule failure rate; mean time to triage; repeat defect rate by rule. | Who: on-call analyst/engineer. What: rule definitions, failing samples, triage decisions and closure notes. Where: DQ framework repo, incident tracker, observability platform. |
| 4. Lineage and provenance traceability | Every feature and model artifact is traceable to exact source data, code version, and run context. | Lineage coverage ratio; orphan artifact count; reproducibility replay success. | Who: R9 owner + independent reviewer. What: lineage graph snapshot, run manifest, commit hash mapping. Where: metadata store, experiment tracker, artifact registry. |
| 5. Label quality and ground-truth governance | Labels/targets are accurate, policy-compliant, and measured for noise and drift. | Inter-annotator agreement; label error audit rate; stale-label rate. | Who: labeling lead + R9 validator. What: annotation guidelines, audit sample results, adjudication records. Where: labeling platform, QA audit docs. |
| 6. Feature pipeline consistency (train/serve parity) | Features used in training match online/offline serving semantics and transformations. | Train-serve skew tests; feature parity test coverage; skew incident count. | Who: feature pipeline owner. What: parity test suite, skew reports, transformation specs. Where: CI pipeline, feature store, serving logs. |
| 7. Experiment design and statistical power | Experiments are pre-registered with hypotheses, power rationale, and guardrails. | Pre-registration compliance; underpowered experiment rate; guardrail breach frequency. | Who: experiment owner + reviewer. What: prereg doc, power calculation, analysis plan. Where: experiment registry, analytics repo. |
| 8. Evaluation coverage and error analysis | Evaluation spans relevant segments, failure modes, and operational edge cases. | Segment coverage ratio; severe-error discovery rate; unresolved high-impact error clusters. | Who: model evaluator. What: eval matrix by segment, confusion/error slices, remediation backlog. Where: model card repo, dashboard, issue tracker. |
| 9. Uncertainty calibration and reporting | Probabilities/scores are calibrated and uncertainty is communicated for decisions. | Calibration error (ECE/Brier); confidence interval availability; overconfidence incident count. | Who: R9 evaluator. What: calibration plots, reliability tests, uncertainty documentation. Where: notebook/report repo, model registry attachments. |
| 10. Bias/fairness measurement and mitigation | Group-level performance disparities are measured, reviewed, and mitigated when outside thresholds. | Disparity metric trend; mitigation completion rate; fairness waiver count. | Who: R9 + R8 reviewer. What: fairness report, threshold decisions, mitigation experiment results. Where: governance folder, risk register, experiment tracker. |
| 11. Model reproducibility and artifact versioning | Any reported model result can be recreated from immutable code/data/config artifacts. | End-to-end replay success rate; missing artifact count; mutable dependency violations. | Who: model owner + independent reproducer. What: lockfiles, environment spec, dataset snapshot ID, replay logs. Where: artifact registry, SCM, build pipeline logs. |
| 12. Explainability and decision trace generation | Model behavior and key decisions are explainable to technical and risk reviewers. | Explanation coverage for critical decisions; contradiction rate between explanation and behavior. | Who: model owner + domain reviewer. What: explanation method docs, case-level traces, reviewer sign-off notes. Where: model card, audit workspace, decision logs. |
| 13. Privacy and sensitive-data handling in ML workflow | Sensitive attributes and personal data are minimized, protected, and policy-compliant across the ML lifecycle. | Unauthorized attribute usage count; masking/tokenization control pass rate; retention-policy violations. | Who: R9 owner + R8 control owner. What: data classification map, access logs, retention/deletion evidence. Where: IAM logs, data governance tools, compliance tracker. |
| 14. Release gating and rollback readiness | Promotion requires passing quality/risk gates with tested rollback and kill-switch paths. | Gate pass completeness; rollback drill success; time-to-safe-state in drills. | Who: R9 + R12 + R6 approvers. What: release checklist, gate report, rollback test artifacts. Where: release pipeline, change record, runbook repo. |
| 15. Production monitoring and drift response | Live performance, data drift, and concept drift are monitored with actionable thresholds. | Drift alert precision/recall; mean time to detect; threshold breach aging. | Who: R9 on-call + SRE partner. What: monitoring config, alert history, drift investigation reports. Where: observability stack, incident system. |
| 16. Incident response and postmortem closure | Model/data incidents are contained quickly and converted to preventive actions. | MTTR for model incidents; corrective action closure rate; repeat incident rate. | Who: incident commander + R9 owner. What: timeline, impact assessment, corrective actions with owners/dates. Where: incident reports, postmortem tracker. |
| 17. Compute/cost efficiency with quality safeguards | Training/inference cost is controlled without degrading validated quality or safety thresholds. | Cost per training run/inference; efficiency gain with no quality regression; waste rate of failed runs. | Who: R9 owner + FinOps liaison. What: cost dashboard, quality-vs-cost tradeoff analysis, optimization records. Where: cloud billing exports, experiment tracker. |
| 18. Documentation, handoff, and runbook quality | R9 artifacts are complete enough for independent operation, review, and audit. | Documentation completeness score; handoff rejection count; stale runbook rate. | Who: R9 author + receiving team reviewer. What: model card, runbook, ownership matrix, handoff sign-off. Where: docs repo, ops wiki, ticket approvals. |

## Scoring anchors by sub-dimension (0/25/50/75/90/100)
No sub-dimension may score above `50` without complete who/what/where/time/version/hash evidence, above `75` without independent reviewer validation, or above `90` without same-iteration adversarial challenge plus non-author replay parity.

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Data source contract integrity | No formal schema contracts; source changes break pipelines unnoticed. | Partial contracts exist but many sources unowned; frequent undocumented breaks. | Most critical sources contracted; breakage detected but often after downstream impact. | Contracts cover critical feeds; pre-merge checks catch most breaking changes. | Near-complete contract coverage; documented exceptions time-bound and approved. | Full contract coverage with versioned approvals; zero unannounced breaks for two consecutive cycles. |
| 2. Ingestion completeness and freshness | Ingestion lag/loss unknown; no reconciliation. | Basic schedule exists; frequent missing partitions and no root-cause closure. | Freshness tracked for key pipelines; recurring misses remain unresolved. | SLA and reconciliation in place for critical pipelines; misses triaged with owners. | High SLA attainment with rapid correction; lag budgets actively managed. | Sustained SLA compliance with automatic reconciliation and verified late-data recovery. |
| 3. Data quality validation and anomaly triage | No data quality rules or triage process. | Sparse checks; anomalies manually noticed and inconsistently handled. | Core checks exist; triage happens but closure evidence weak. | Rule suite covers major failure modes; triage and closure are tracked. | High-signal checks with low false positives; repeat defects declining. | Comprehensive rule governance with rapid triage, documented prevention, and no repeated critical rule failures in cycle. |
| 4. Lineage and provenance traceability | Cannot trace model outputs to source data/code versions. | Lineage exists only for parts of pipeline; frequent orphan artifacts. | Traceability available for most training runs but not all deployed artifacts. | Deployed models and critical features have end-to-end lineage. | Lineage includes transformations, owners, and environment context with periodic verification. | Full immutable provenance chain for all production artifacts; independent replay validates lineage claims. |
| 5. Label quality and ground-truth governance | Labels unmanaged; quality unknown; no policy controls. | Annotation guidance minimal; disagreement and error rates unmeasured. | Label QA on sample basis; known noise issues remain open. | Systematic label audits and adjudication process for high-impact tasks. | Strong agreement and low audited error rate with drift monitoring. | Continuous label governance with controlled refresh strategy and independently verified label quality targets met. |
| 6. Feature pipeline consistency (train/serve parity) | Train and serve features differ materially; skew undetected. | Ad hoc parity checks; skew incidents common. | Parity tests for major features; residual skew appears in edge cases. | Automated parity checks for critical features; skew incidents triaged quickly. | Broad parity coverage including edge transformations and time windows. | Full parity enforcement in CI/CD with no unresolved critical skew incidents in cycle. |
| 7. Experiment design and statistical power | Experiments run without hypotheses or design discipline. | Hypotheses recorded inconsistently; no power rationale. | Basic preregistration; underpowered tests still used for decisions. | Most decisions rely on preregistered and adequately powered experiments. | Strong adherence to preregistration and guardrails; exceptions approved before execution. | All decision-driving experiments preregistered, powered, and independently reviewable with no post-hoc metric switching. |
| 8. Evaluation coverage and error analysis | Evaluation limited to aggregate metric only. | Minimal slicing; major segments omitted. | Important segments tested but failure-mode depth is shallow. | Broad segment and edge-case evaluation with tracked error taxonomy. | High-impact failure clusters prioritized and mitigations validated. | Exhaustive risk-based coverage with closed-loop error reduction demonstrated across cycles. |
| 9. Uncertainty calibration and reporting | Confidence scores absent or misleading. | Uncertainty reported inconsistently and not validated. | Calibration checked once; poor alignment persists in deployment. | Calibration validated on release candidates; uncertainty shown in reviewer artifacts. | Calibration maintained in production with periodic recalibration triggers. | Robust calibrated outputs with decision thresholds explicitly tied to uncertainty bounds and validated post-release. |
| 10. Bias/fairness measurement and mitigation | No fairness measurement or thresholds. | Fairness metrics run ad hoc after complaints. | Core group metrics tracked, but mitigations slow or incomplete. | Fairness thresholds defined and enforced for release candidates. | Disparities monitored continuously with timely mitigations and documented tradeoffs. | Fairness governance is proactive, independently reviewed, and no unresolved high-severity disparity breaches in cycle. |
| 11. Model reproducibility and artifact versioning | Results cannot be recreated from stored artifacts. | Some artifacts versioned; environment/data snapshots missing. | Reproduction possible for selected runs only. | Most key results reproducible using versioned code/data/config bundles. | Independent reproduction succeeds for release candidates with minor gaps. | Deterministic or bounded-stochastic replay succeeds for all release claims with immutable artifact chain. |
| 12. Explainability and decision trace generation | No explanation artifacts for model decisions. | Generic explanations produced but not tied to real decisions. | Case-level traces exist for limited workflows only. | Explanations cover critical decisions and are reviewed for consistency. | Explanation artifacts are usable by technical and risk reviewers with low contradiction rate. | Full decision-trace capability for critical paths, with reviewer acceptance and auditable explanation-method limits documented. |
| 13. Privacy and sensitive-data handling in ML workflow | Sensitive data used without classification or access controls. | Basic controls exist but unauthorized usage or retention breaches occur. | Classification and access policies partially enforced; gaps remain. | Sensitive data controls enforced on critical workflows with periodic audits. | Strong minimization, access, and retention compliance with quick remediation of findings. | End-to-end compliant handling with verified minimization and zero unresolved high-severity privacy violations in cycle. |
| 14. Release gating and rollback readiness | Models promoted without formal gates or rollback capability. | Checklist exists but can be bypassed; rollback untested. | Core gates enforced; rollback plan documented but rarely drilled. | Gate evidence required for promotion; rollback tested on schedule. | Reliable rollback/kill-switch drills meet target safe-state times. | Release and rollback are fully rehearsed, evidence-complete, and independently approved for every production promotion. |
| 15. Production monitoring and drift response | No production drift monitoring. | Basic alerts generate noise; drift investigations inconsistent. | Key drift signals monitored; response often delayed. | Monitors cover major data/performance drift with documented response playbooks. | Alert quality high; response SLAs usually met with root-cause closure. | Comprehensive monitoring with low-noise alerts, rapid containment, and demonstrated prevention of repeat drift incidents. |
| 16. Incident response and postmortem closure | Model incidents unmanaged; no postmortems. | Incidents logged inconsistently; corrective actions rarely completed. | Postmortems produced but actions stale. | Incident process reliable with owned corrective actions and due dates. | High closure discipline and measurable reduction in repeat incidents. | Incident learning is institutionalized; all high-severity actions closed on time and verified effective. |
| 17. Compute/cost efficiency with quality safeguards | Spend untracked; optimization decisions harm quality. | Cost tracked manually; optimization ad hoc with weak safeguards. | Basic cost controls; some regressions from aggressive savings. | Cost/quality tradeoffs quantified before major changes. | Efficient resource usage with regression guards and waste reduction trend. | Cost is continuously optimized under enforced quality/safety floors with independently validated no-regression evidence. |
| 18. Documentation, handoff, and runbook quality | No usable model cards or runbooks. | Documentation incomplete and stale; receivers cannot operate independently. | Core docs exist but missing ownership or recovery detail. | Handoff packages complete for critical systems and accepted by receiving teams. | Documentation freshness and ownership routinely verified with low rejection rates. | Independent team can operate, audit, and recover service using docs alone; handoff acceptance is sustained across cycles. |

## Anti-gaming checks specific to this role

1. Freeze evaluation dataset hashes and segment definitions before model training; any post-hoc changes invalidate reported scores for that cycle.
2. Require metric registry approval before experiment launch; new "better-looking" metrics introduced after seeing results are informational only.
3. Recompute reported offline metrics from raw predictions for a random 20% sample of model runs each cycle.
4. Enforce slice completeness rule: no release decision may be based only on global metrics when protected or high-risk segments exist.
5. Compare shadow and live data distributions weekly; suppressing drift alerts without incident ticket and rationale is scored as control failure.
6. Require independent reproduction by a non-author engineer for all release-candidate claims above score 75.
7. Detect label leakage by mandatory temporal and feature-leak tests; failed leakage test caps related sub-dimensions at 25.
8. Cross-check cost-efficiency claims against quality guardrails; any improvement claim without paired quality evidence is null.
9. Lock model-card sign-off timestamps; backfilled justifications after go-live count only for next cycle.
10. Maintain an exceptions ledger with expiry dates; expired exceptions automatically convert to open defects.
11. Lock iteration snapshot hash and denominator before scoring; reject unapproved in-iteration edits.
12. Require approved delta dossier and targeted re-evaluation for any scoring-rule update.
13. Require independent validation plus same-iteration adversarial challenge for every `90`/`100` row.
14. Recompute at least one reported `90+` claim end-to-end from raw evidence and compare to published outcome.
15. Reconcile contradiction register with release decision packet; hidden open contradictions invalidate publication.

## Tripwires and hard-fail conditions

| ID | Hard-fail condition | Immediate consequence |
| --- | --- | --- |
| R9-HF1 | Fabricated, tampered, or non-reproducible evaluation evidence for release decision | R9 score set to 0; release blocked pending forensic review |
| R9-HF2 | Production model deployed without documented rollback or kill-switch path | Immediate release freeze and rollback |
| R9-HF3 | Known high-severity data leakage (train-test contamination or feature leakage) left unresolved at decision point | Evaluation invalidated; model ineligible for promotion |
| R9-HF4 | Unresolved critical disparity breach against approved fairness thresholds in a protected/high-risk segment | Release blocked until mitigated or formally waived by governance board |
| R9-HF5 | Sensitive data processed outside approved classification/access controls | Incident escalation to R8/R7; release blocked |
| R9-HF6 | Inability to reproduce primary model claim from versioned artifacts within agreed replay window | All claim-based scores capped at 25 until fixed |
| R9-HF7 | Drift alarm above critical threshold not triaged within SLA and user-impact risk present | Automatic traffic reduction/rollback trigger |
| R9-HF8 | Metric thresholds weakened after failed results without pre-approved change control | Current-cycle evaluation deemed invalid |
| R9-HF9 | Required segment-level evaluation omitted for high-impact population | Release decision void; mandatory re-evaluation |
| R9-HF10 | Repeated Sev-1 model incident with previously promised corrective action not implemented | Mandatory executive review; R9 cannot approve new promotions |

### Hard-fail detection and minimum recovery proof

| ID | Detection rule | Minimum recovery proof before publication |
| --- | --- | --- |
| R9-HF1 | Forensic integrity audit finds fabricated/tampered/non-reproducible evaluation evidence | Forensic closure memo, rebuilt immutable evidence chain, and full independent re-score of affected rows |
| R9-HF2 | Release record shows no rollback/kill-switch path in production | Tested rollback/kill-switch drill evidence and updated release-gate replay pass |
| R9-HF3 | Leakage tests or incident evidence show unresolved train-test/feature leakage | Leakage remediation proof, retraining evidence, and independent evaluation replay |
| R9-HF4 | Fairness dashboard or audit shows unresolved critical disparity breach | Mitigation evidence or formal governance waiver with expiry plus re-evaluation packet |
| R9-HF5 | Access/classification audit shows sensitive data outside approved controls | Containment and control remediation evidence plus R8/R7 closure sign-off |
| R9-HF6 | Non-author replay cannot reproduce primary model claim in replay window | Complete artifact bundle with successful non-author replay transcript and parity check |
| R9-HF7 | Critical drift breach not triaged within SLA while impact risk exists | Drift triage closure record, containment action evidence, and monitoring-threshold retest |
| R9-HF8 | Threshold changes occurred post-failure without approved change control | Approved delta dossier, impacted-row re-score, and change chronology audit pass |
| R9-HF9 | Required segment-level evaluation missing for high-impact population | Completed segment evaluation evidence with updated decision and gate recomputation |
| R9-HF10 | Repeat Sev-1 incident with unimplemented prior corrective action | Implemented corrective action verification and independent incident-postmortem closure review |

## Cross-role dependency and handoff criteria

| Counterparty role | Dependency into R9 | Handoff from R9 | Acceptance criteria |
| --- | --- | --- | --- |
| R1 Product Manager | Outcome definitions, guardrails, segment priorities | Metric design brief, experiment readouts, model impact narrative | KPI mapping approved; tradeoffs and segment impacts explicitly signed off |
| R2 Product/Enterprise Architect | Data platform and interface constraints | Feature contracts, lineage design, serving architecture assumptions | Contract compatibility verified; no unresolved architecture exceptions |
| R5 QA/Test Engineer | Test strategy and release verification policy | Evaluation test suite, parity tests, failure-mode test cases | QA confirms coverage across critical paths and non-functional gates |
| R6 SRE/Platform Engineer | Runtime SLOs, monitoring stack, incident process | Drift monitors, alert thresholds, rollback runbooks | SLO and alert integration validated in staging and drill logs |
| R7 Security Engineer | Threat model controls, secrets and supply-chain policies | Model artifact integrity plan, dependency inventory, access patterns | Security controls pass; critical vulnerabilities resolved or waived formally |
| R8 Privacy/Compliance/Legal | Data-use constraints, lawful basis, retention requirements | Data classification map, fairness/impact reports, deletion/retention evidence | Compliance sign-off recorded; open obligations tracked with due dates |
| R12 DevOps/Release Manager | Promotion workflow and change governance | Release gate evidence package and go/no-go recommendation | Gate checklist complete; rollback rehearsal evidence attached |
| R15 Internal Audit/Assurance | Independent control testing schedule | Reproducibility bundle, decision trace logs, exception ledger | Audit sample replay succeeds; evidence provenance passes integrity checks |

## Iteration-level improvement checklist

### Pre-iteration (planning)
- [ ] Confirm current decision rights and approver roster (R9, R1, R6, R8, R12) with named backups.
- [ ] Lock iteration snapshot hash, scored-row denominator, and critical segment list before experimentation.
- [ ] Validate source contracts and data retention constraints for all planned datasets.
- [ ] Define experiment preregistration template and minimum power requirements.
- [ ] Publish admissibility schema requiring who/what/where/time/version/hash for non-zero rows.

### Build iteration (data + model development)
- [ ] Run ingestion freshness/completeness reconciliation at agreed cadence.
- [ ] Execute data quality and leakage tests on every training snapshot.
- [ ] Record immutable lineage for data, code, configuration, and environment.
- [ ] Require train-serve parity checks for all newly introduced or changed features.
- [ ] Update model card draft with evaluation slices, uncertainty, and known limitations.
- [ ] Log contradiction cases by class, owner, SLA, and expected score consequence.

### Release iteration (promotion readiness)
- [ ] Complete segment-level evaluation, fairness review, and uncertainty calibration checks.
- [ ] Verify independent reproduction of primary claims from registry artifacts.
- [ ] Run same-iteration adversarial challenge for every proposed `90`/`100` row.
- [ ] Confirm release gates, rollback drills, and kill-switch verification are current.
- [ ] Publish handoff packet to R6/R12 including runbooks and alert thresholds.
- [ ] Apply targeted re-evaluation for every approved delta before publication.

### Post-release iteration (operations and learning)
- [ ] Review drift and incident trends against SLA, with action aging dashboard.
- [ ] Audit one random decision trace end-to-end for explainability and evidence integrity.
- [ ] Close corrective actions from postmortems and verify effectiveness.
- [ ] Run cost-quality review to identify optimization opportunities without threshold erosion.
- [ ] Carry forward unresolved exceptions with explicit expiry dates and owners.

---

## R10 UX Researcher / Designer

- source_file: `swarm_outputs/role_expansions/R10_ux_researcher_designer.md`
- words: 4957
- lines: 208

# R10 UX Researcher / Designer Rubric Expansion

## 1) Role mission and decision rights

**Role mission**
R10 is accountable for ensuring product behavior is understandable, usable, inclusive, and evidence-backed for real users in real contexts. R10 owns the validity of UX findings, the quality of interaction and information design decisions, and the traceability from research evidence to released experience outcomes.

R10 has authority to block UX sign-off when critical usability/accessibility risks are unresolved or when evidence quality is insufficient. R10 does not unilaterally approve business launch risk, legal interpretation, or infrastructure readiness, but can require UX and accessibility gates before release recommendation.

| Decision area | R10 authority boundary | Required co-approval | Escalation trigger |
| --- | --- | --- | --- |
| Research plan and method selection | Final call on study method, protocol, and success criteria for UX questions | R1 for decision relevance; R8 for regulated populations | Study method cannot answer launch-critical question or introduces compliance risk |
| Participant inclusion/exclusion | Final call on recruitment criteria and segment quotas | R1 for target segment priorities | Critical segment underrepresented beyond approved tolerance |
| Usability severity classification | Final severity rating for UX defects affecting task completion | R5 for release gate alignment | Severity dispute on critical path defect remains unresolved > 2 business days |
| Accessibility readiness recommendation | Can approve/withhold UX accessibility readiness for critical journeys | R7 and R8 for security/privacy/legal control surfaces | Any critical WCAG or assistive-tech blocker on a release-critical workflow |
| IA and interaction pattern choice | Final call on navigation model and interaction patterns within approved scope | R2 when pattern affects architecture constraints | Pattern conflicts with platform constraints or cross-product standards |
| Design-system exception approval | Can approve temporary exceptions with expiry and mitigation | R3 for team capacity impact; R12 for release impact | Exception lacks owner, expiry date, or rollback path |
| Prototype-to-build handoff readiness | Can approve/reject handoff package quality | R4 and R5 for implementation/testability readiness | Handoff ambiguity causes repeated implementation defects |
| Post-release UX remediation priority | Can require remediation ranking for UX incidents and regressions | R1 for roadmap tradeoffs; R13 for support impact | Recurring high-severity usability incident with no dated owner |

### Iteration snapshot governance, admissibility, and precedence controls

| Control | Requirement | Deterministic enforcement |
| --- | --- | --- |
| Iteration snapshot lock | Record `iteration_id`, rubric snapshot hash, role file hash, and scorer roster before first score. | Scores produced on an unapproved snapshot hash are invalid. |
| Denominator and cohort lock | Lock studied cohort definitions and scored-row denominator at snapshot time. | Any in-iteration denominator/candidate change requires approved delta dossier and dual reporting (`before`/`after`). |
| Delta dossier and targeted re-evaluation | Any scoring-affecting criteria update must include impacted rows/gates, owner, approvers, and rationale. | Impacted rows are rescored and impacted gates are replayed before publication. |

### Non-zero evidence admissibility contract (mandatory fields)

| Field | Requirement for non-zero scoring | Rejection behavior when missing/invalid |
| --- | --- | --- |
| `who` | Named study owner/reviewer identity | Row ineligible for score above `0` |
| `what` | Explicit UX claim, finding, or control test | Row ineligible for score above `0` |
| `where` | Immutable evidence locator (raw sessions/logs/artifacts) | Row ineligible for score above `0` |
| `time_utc` | UTC timestamp of evidence capture | Row ineligible for score above `0` |
| `version` | Study protocol/spec/release snapshot version | Row ineligible for score above `0` |
| `hash` | Integrity hash for evidence bundle | Row ineligible for score above `0` |
| `provenance_chain` | Source lineage from raw UX evidence to scored claim | Row ineligible for score above `0` |

| Admissibility sampling rule | Threshold | Deterministic effect |
| --- | --- | --- |
| Sampled non-zero rows missing any required field | `>5%` | Cap affected sub-dimensions at `50` and require targeted re-score |
| Sampled non-zero rows missing `time_utc`/`version`/`hash`/`provenance_chain` | `>10%` | Set R10 role score to `0` for the iteration pending remediation |

### High-anchor (`90`/`100`) dual-proof gate

| Requirement | Mandatory evidence | Deterministic consequence if missing |
| --- | --- | --- |
| Independent validator (non-author) | Independent review bound to row evidence IDs | Row capped at `75` |
| Same-iteration adversarial challenge | Challenge script, execution evidence, and outcome | Row capped at `75` and targeted re-score required |
| Non-author replay parity | Replay confirms anchor and gate-state parity for affected rows | Row capped at `75`; release recommendation for affected flow is void |

### Contradiction precedence protocol (deterministic)

| Contradiction class | Precedence order | Owner | SLA | Score and gate consequence |
| --- | --- | --- | --- | --- |
| Accessibility/safety/legal conflict vs positive usability results | Highest | R10 + R8/R7 | 1 business day | Publication blocked; unresolved state forces FAIL via `G4`/`G3` |
| Critical cohort exclusion vs favorable aggregate metrics | High | R10 + R1 | 1 business day | Sampling-related rows set to `0` until cohort evidence is complete |
| Handoff feasibility vs UX fidelity claims | Medium | R10 + R4/R5 | 2 business days | Fidelity/handoff rows capped at `50` until contradiction closure evidence is attached |
| UX optimization vs support/operations risk | Medium | R10 + R13/R12 | 2 business days | Post-release readiness rows capped at `50` and release packet marked incomplete |

## 2) Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| 1. Research objective and hypothesis validity | Research goals are decision-linked, falsifiable, and time-bounded. | Pre-registered hypothesis rate; percent of studies mapped to explicit product decision; post-hoc hypothesis introduction count. | Who: R10 lead + R1 reviewer. What: research brief, hypothesis registry, decision linkage map. Where: research repo, decision log, planning board. |
| 2. Participant sampling and recruitment integrity | Participant sample represents target and high-risk segments with controlled bias. | Segment quota attainment; screener false-positive rate; replacement bias rate after no-shows. | Who: researcher + recruiting owner. What: screener, quota sheet, recruitment audit. Where: participant ops folder, research CRM, study packet. |
| 3. Method-task fit and protocol rigor | Chosen method is appropriate for risk level and task type; protocol is consistently executed. | Pilot failure rate; protocol deviation count per session; method justification coverage. | Who: R10 owner + peer reviewer. What: method rationale, moderator script, protocol checklist. Where: research plan archive, session docs. |
| 4. Moderator bias control and session integrity | Session conduct minimizes leading behavior and preserves raw evidence integrity. | Leading-question incidence; recording completeness rate; inter-rater agreement on coded findings. | Who: moderator + independent note reviewer. What: session recordings, transcript excerpts, coding rubric and agreement report. Where: secure research storage, analysis workspace. |
| 5. Task-flow usability on critical journeys | Users can complete critical tasks accurately and within acceptable effort. | Task success rate by segment; critical error rate; median time-on-task delta vs baseline. | Who: R10 + R5 observer. What: usability run results, error taxonomy, benchmark comparison. Where: usability dashboard, evidence package, test logs. |
| 6. Information architecture and findability coherence | Navigation structure and labels let users find targets without excessive detours. | First-click success; tree-test pass rate; backtrack depth for primary tasks. | Who: IA designer + UX researcher. What: IA map, tree-test results, click-path analysis. Where: IA repository, analytics export, study report. |
| 7. Content clarity and comprehension quality | Interface and support copy is clear, unambiguous, and decision-enabling. | Comprehension check score; ambiguous-term defect count; help-seeking rate caused by wording confusion. | Who: content designer + R10 reviewer. What: content inventory, comprehension test outcomes, issue log linkage. Where: content repo, support taxonomy, study artifacts. |
| 8. Interaction feedback and affordance clarity | Controls communicate state, consequence, and recovery options clearly. | Misclick rate; undo/cancel successful recovery rate; state ambiguity defect aging. | Who: interaction designer + QA counterpart. What: interaction specs, event logs, defect records. Where: design files, telemetry dashboards, defect tracker. |
| 9. Accessibility conformance on critical paths | Critical workflows satisfy WCAG 2.2 AA and assistive-technology usability expectations. | Critical WCAG violation count; keyboard-only task success; screen-reader completion rate on critical journeys. | Who: accessibility owner + independent auditor. What: automated and manual audit reports, AT test videos, issue remediation proof. Where: a11y audit folder, CI reports, tracker. |
| 10. Inclusive design across contexts and populations | Experience works for diverse abilities, languages, devices, and constraints. | Outcome parity across priority cohorts; localization defect rate; low-bandwidth completion gap. | Who: R10 + localization + support analyst. What: cohort analysis, localization QA results, constrained-network test report. Where: analytics workspace, localization tracker, test lab artifacts. |
| 11. Visual hierarchy and readability effectiveness | Visual emphasis, typography, spacing, and contrast support fast, accurate scanning and comprehension. | Contrast pass rate; key-message recall after scan test; visual clutter defect count. | Who: visual designer + UX researcher. What: hierarchy review, readability test report, contrast audit output. Where: design review notes, research folder, accessibility tooling exports. |
| 12. Design-system consistency and exception governance | Production UI uses approved components/tokens; deviations are controlled and time-bound. | Token/component reuse ratio; unapproved override count; exception closure latency. | Who: design-system owner + R10 reviewer. What: component usage audit, exception ledger, remediation tickets. Where: design-system repo, code audit reports, governance board records. |
| 13. Prototype-to-production fidelity and spec quality | Implementation reflects approved UX behavior with sufficiently precise handoff artifacts. | Design-dev fidelity defect rate; spec ambiguity ticket volume; redline completeness score. | Who: R10 + R4 + R5. What: annotated specs, fidelity review report, implementation diff evidence. Where: handoff package, QA results, PR review artifacts. |
| 14. UX evidence traceability and decision ledger hygiene | Every major UX decision links to raw evidence, alternatives considered, and final rationale. | Trace link completeness; orphan insight count; decision logging latency. | Who: R10 owner + audit reviewer. What: decision ledger, evidence index, alternatives matrix. Where: governance log, research archive, release packet. |
| 15. Iterative validation and experiment discipline | UX changes are validated through controlled iteration, not one-off opinion. | Experiment preregistration rate; iteration cycle time; rollback or redesign trigger usage after failed result. | Who: R10 + data analyst + PM. What: experiment plans, readouts, decision outcomes. Where: experiment registry, analytics repo, backlog history. |
| 16. Handoff quality to engineering, QA, and documentation | Handoffs are complete, testable, and reduce rework across build/verify/document workflows. | Handoff rejection count; clarification turnaround time; defect origin tagged "spec gap". | Who: R10 + R4 + R5 + R11 recipients. What: handoff checklist, clarification log, defect root-cause tags. Where: delivery board, handoff package, defect tracker. |
| 17. Post-release UX telemetry and remediation closure | Live UX health is monitored and converted into prioritized, closed corrective actions. | UX KPI breach MTTD; time to triage high-severity usability incidents; corrective action closure rate. | Who: R10 + R13 + R1. What: UX telemetry dashboard, incident reviews, remediation backlog report. Where: analytics platform, incident tracker, planning board. |
| 18. Dark-pattern and user-harm prevention | Design avoids deceptive, coercive, or manipulative patterns that undermine user agency. | Dark-pattern checklist pass rate; complaint rate on consent/cancel flows; regulator/escalation flag count. | Who: R10 + R8 + legal reviewer. What: pattern risk assessment, complaint analysis, compliance review notes. Where: trust review archive, support system, governance records. |

## 3) Scoring anchors table (0/25/50/75/90/100)
No sub-dimension may score above `50` without complete who/what/where/time/version/hash evidence, above `75` without independent reviewer validation, or above `90` without same-iteration adversarial challenge and non-author replay parity.

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Research objective and hypothesis validity | No explicit research objective or falsifiable hypothesis. | Objective exists but is solution-biased and not tied to a decision. | Decision linkage exists for most studies; hypotheses are partially testable. | All launch-relevant studies have pre-registered, falsifiable hypotheses tied to named decisions. | Hypotheses, success/failure thresholds, and decision owners are complete with minimal late changes. | Two consecutive cycles show zero post-hoc hypothesis insertion and full decision-to-study traceability. |
| 2. Participant sampling and recruitment integrity | Participants are ad hoc; target segments are unknown or ignored. | Basic screener exists but critical cohorts are routinely missing. | Core cohorts represented; high-risk or edge cohorts under-sampled. | Segment quotas for critical cohorts met with documented sampling rationale. | Recruitment bias monitored; replacement rules and exclusions are consistently enforced. | Two cycles with full critical cohort coverage and independent audit confirms no material sampling bias. |
| 3. Method-task fit and protocol rigor | Method is inappropriate for question risk; protocol absent. | Method chosen by convenience; protocol frequently skipped. | Method mostly appropriate; protocol deviations are common and weakly logged. | Method rationale and protocol are consistent, with deviations recorded and justified. | Pilot and execution quality checks prevent most protocol failures before full study run. | Two cycles with zero unapproved protocol deviations on launch-critical studies. |
| 4. Moderator bias control and session integrity | Sessions are unrecorded or heavily leading; evidence unusable. | Some recordings exist; leading prompts materially distort outcomes. | Bias controls exist but inter-rater consistency is weak. | Recorded sessions, neutral prompts, and reproducible coding for critical findings. | Independent reviewer confirms low leading-question rate and high coding agreement. | Two cycles with complete recording integrity and independently replicated findings on sampled sessions. |
| 5. Task-flow usability on critical journeys | Critical tasks fail frequently; no severity framework used. | Task success low and issues are described narratively only. | Task metrics exist, but major errors persist on key flows. | Critical task success and error thresholds are met for primary segments. | Thresholds met across primary and high-risk segments with verified remediation of critical failures. | Sustained high performance across two cycles with no unresolved high-severity critical-flow defects. |
| 6. Information architecture and findability coherence | Users cannot reliably locate key destinations. | Navigation structure exists but label confusion causes frequent dead ends. | Findability acceptable for common tasks but weak on secondary critical routes. | IA supports reliable first-click outcomes and low backtracking on critical paths. | Tree and click tests pass across priority cohorts with documented exceptions only. | Two cycles of stable findability performance with no critical navigation regressions. |
| 7. Content clarity and comprehension quality | Copy is ambiguous; users misinterpret required actions. | Major terminology confusion persists with no measurement plan. | Comprehension tests run; wording issues remain in critical screens. | Critical copy is plain, test-validated, and aligned to user decision points. | Comprehension outcomes strong across priority cohorts, including non-expert users. | Two cycles with zero Sev1/Sev2 incidents attributable to copy ambiguity on critical flows. |
| 8. Interaction feedback and affordance clarity | Users cannot tell system state or consequence of actions. | Basic states exist but recovery and confirmation cues are inconsistent. | Most controls have clear feedback; some high-risk ambiguities remain. | Interaction states, confirmations, and recovery paths are clear on critical workflows. | Error prevention and recovery behavior are validated with low ambiguity defect rates. | Two cycles with no unresolved critical state/affordance defects and verified recovery success. |
| 9. Accessibility conformance on critical paths | Critical flows fail basic keyboard/screen-reader access. | Automated scans run, but critical manual issues remain unresolved. | Most WCAG checks pass; assistive-tech task completion is inconsistent. | Critical journeys pass WCAG and manual AT checks with tracked fixes. | Accessibility outcomes meet thresholds across release-critical surfaces with timely closure. | Two cycles with zero unresolved critical accessibility blockers and independent audit pass. |
| 10. Inclusive design across contexts and populations | Design excludes key user contexts (language/device/connectivity/ability). | Inclusion concerns are listed but not tested. | Partial cohort/context testing; gaps remain on high-impact populations. | Inclusive tests cover priority cohorts and constrained contexts with mitigations. | Performance and completion gaps are measured and reduced with owner-backed actions. | Two cycles with no unresolved high-impact inclusion gap and parity targets met for priority cohorts. |
| 11. Visual hierarchy and readability effectiveness | Visual layout obscures primary actions and messages. | Basic visual order exists but contrast/readability defects are common. | Most screens readable; clutter and hierarchy issues persist on key views. | Hierarchy/readability standards met on critical views with measurable scan efficiency. | Strong recall and fast scan performance validated across target cohorts. | Two cycles with no critical readability/hierarchy defects and sustained objective scan-test performance. |
| 12. Design-system consistency and exception governance | UI is inconsistent; ad hoc styles dominate. | Some system components used; untracked overrides are frequent. | System usage is moderate; exception process exists but weakly enforced. | Critical surfaces use approved components/tokens; exceptions are logged and time-bound. | High consistency with low unauthorized overrides and active exception closure. | Two cycles with full critical-surface compliance and zero expired design-system exceptions. |
| 13. Prototype-to-production fidelity and spec quality | Build diverges materially from approved UX behavior; specs unusable. | Handoff artifacts incomplete; frequent interpretation errors. | Core behavior implemented; fidelity gaps and spec ambiguities still common. | Handoff artifacts are precise; critical fidelity defects are rare and quickly corrected. | Fidelity checks and spec quality prevent most build-time UX regressions. | Two cycles with near-zero critical fidelity gaps and no release delays caused by ambiguous UX specs. |
| 14. UX evidence traceability and decision ledger hygiene | UX decisions cannot be tied to evidence or decision rationale. | Evidence exists but is fragmented and backfilled after decisions. | Most decisions have references; alternatives/rationales are inconsistently captured. | Major UX decisions have complete evidence links, alternatives, and timestamps. | Independent reviewer can replay sampled decisions end-to-end with minimal gaps. | Two cycles with full traceability on decision-critical UX changes and zero inadmissible evidence events. |
| 15. Iterative validation and experiment discipline | Design changes ship without validation loop. | Validation occurs sporadically with moving success criteria. | Iteration exists, but preregistration and rollback triggers are inconsistent. | Controlled iteration with preregistered thresholds drives acceptance/rework decisions. | Experiments are timely, decision-linked, and include explicit fail/rollback criteria. | Two cycles with no decision-critical UX changes accepted without preregistered validation evidence. |
| 16. Handoff quality to engineering, QA, and documentation | Downstream teams cannot implement/test/document without repeated rework. | Handoff packages often missing states, edge cases, or acceptance details. | Handoffs mostly usable; high clarification load persists on critical stories. | Handoffs are complete and testable; critical clarification latency stays within SLA. | Cross-role recipients report low rejection and low defect origination from spec gaps. | Two cycles with zero critical release defects attributed to handoff incompleteness. |
| 17. Post-release UX telemetry and remediation closure | UX regressions in production are not monitored or owned. | Basic UX metrics exist but incident triage is slow and inconsistent. | Monitoring covers core metrics; corrective actions close slowly. | Critical UX metrics are monitored with SLA-based triage and owned remediation plans. | Remediation closure is timely and reduces repeated high-severity usability incidents. | Two cycles with zero overdue critical UX remediations and demonstrated reduction in repeat incident classes. |
| 18. Dark-pattern and user-harm prevention | Deceptive or coercive patterns are present and unaddressed. | Risks are discussed but no enforceable detection or prevention controls exist. | Checklist exists; some high-risk patterns remain unresolved. | High-risk flows pass dark-pattern review with explicit user-agency safeguards. | Complaints and compliance signals are monitored, with rapid corrective action on breaches. | Two cycles with zero substantiated dark-pattern violations on release-critical flows. |

## 4) Anti-gaming checks specific to this role

1. Require pre-registered study objectives, hypotheses, and success thresholds before first participant session; post-session edits are marked inadmissible for current-cycle scoring.
2. Freeze participant quota targets and exclusion criteria at study start; any quota changes require timestamped approval from R1 and R10.
3. Random-audit at least 20% of study sessions by comparing transcript snippets to full recordings to detect quote cherry-picking.
4. Enforce negative-finding inclusion: each research readout must include top disconfirming evidence and unresolved contradictions.
5. Recompute reported task success/error/time metrics from raw event logs for at least one critical flow per cycle.
6. Reject screenshot-only accessibility claims; require keyboard and screen-reader execution evidence on critical journeys.
7. Audit design-system exception ledger for expired waivers each release; expired exceptions count as open defects.
8. Compare prototype claims to production behavior on sampled stories; unmatched claims invalidate associated high scores.
9. Detect severity laundering by diffing original versus final usability severity labels; unresolved downgrades require independent R5 review.
10. Lock decision ledger timestamps at release cutoff; backfilled rationale counts only for next cycle.
11. Validate cohort coverage claims against recruitment source logs; unverifiable participant provenance invalidates sampling scores.
12. Require at least one independent reviewer (non-author) for any sub-dimension scored above 75.
13. Lock iteration snapshot hash and denominator before scoring; reject unapproved in-iteration changes.
14. Require approved delta dossier and targeted re-evaluation for any scoring-rule update.
15. Require independent validator plus same-iteration adversarial challenge for each proposed `90`/`100` row.

## 5) Tripwires and hard-fail conditions

| ID | Hard-fail condition | Detection rule | Immediate consequence |
| --- | --- | --- | --- |
| R10-HF1 | Fabricated, altered, or non-verifiable UX research evidence | Hash mismatch, missing raw session artifacts, or inconsistent timestamps | R10 score set to 0 for cycle; release recommendation blocked pending investigation |
| R10-HF2 | Release-critical workflow has unresolved accessibility blocker | Open critical WCAG/AT defect at launch decision time | Release blocked until verified remediation |
| R10-HF3 | Deceptive/dark-pattern behavior confirmed on consent, billing, cancellation, or privacy controls | Independent review substantiates coercive flow with no approved mitigation | Release blocked; mandatory trust/legal escalation |
| R10-HF4 | Critical task-flow usability below approved threshold without approved exception | Task success/error metrics miss threshold for primary segment and no signed waiver | Release blocked; mandatory redesign/retest |
| R10-HF5 | Critical target cohort missing from study evidence with no approved risk acceptance | Sampling audit shows missing launch-critical segment | Decision invalidated; re-study required |
| R10-HF6 | UX decision traceability failure on material release decision | Evidence-to-decision link absent for any launch-critical UX choice | Related sub-dimensions capped at 25; release gate re-review required |
| R10-HF7 | High-severity usability defect known pre-launch but severity downgraded without independent review | Severity history shows unsupported downgrade | Release blocked; severity adjudication reopened with R5 |
| R10-HF8 | Handoff incompleteness causes repeated critical implementation defects in same flow | Two or more critical defects tagged to missing UX spec details in cycle | R10 cannot approve handoff readiness until corrected and re-verified |
| R10-HF9 | Accessibility or inclusion claims rely only on automated scans where manual AT testing is required | Evidence package lacks required manual testing on critical journeys | Accessibility-related scores capped at 25; launch blocked for affected flow |
| R10-HF10 | Repeated post-release critical UX incident with overdue corrective actions | Same incident class recurs with past-due mitigation actions | Mandatory executive review; no new UX sign-off authority until closure plan approved |

Hard-fail rule: triggering `R10-HF1`, `R10-HF2`, `R10-HF3`, or `R10-HF4` is automatic release fail regardless of weighted score.

### Minimum recovery proof requirements

| ID | Minimum recovery proof before publication |
| --- | --- |
| R10-HF1 | Forensic closure memo, rebuilt immutable evidence chain, and full independent re-score of impacted rows |
| R10-HF2 | Verified remediation of blocker plus manual keyboard/screen-reader retest evidence on affected critical workflow |
| R10-HF3 | Corrected flow implementation evidence, legal/trust re-review, and follow-up user validation showing risk removed |
| R10-HF4 | Redesigned flow with threshold retest evidence and independent reviewer sign-off |
| R10-HF5 | Completed launch-critical cohort study evidence plus updated decision replay |
| R10-HF6 | Complete evidence-to-decision linkage map with immutable references and replay pass |
| R10-HF7 | Restored severity classification with independent R5 adjudication and updated release gate outcome |
| R10-HF8 | Corrected handoff package, reimplementation verification, and repeated-defect class closure proof |
| R10-HF9 | Manual accessibility/inclusion evidence for affected journeys and re-scored accessibility rows |
| R10-HF10 | Approved closure plan with dated owners plus verification that overdue corrective actions are completed |

## 6) Cross-role dependency and handoff criteria

| Counterparty role | Dependency into R10 | Handoff from R10 | Acceptance criteria | SLA |
| --- | --- | --- | --- | --- |
| R1 Product Manager | Priority questions, target segments, decision deadlines | Research findings, UX risk register, design recommendation set | Findings map to explicit decisions with owner and due date | Within 3 business days of study close |
| R2 Product/Enterprise Architect | Platform constraints, IA/interaction technical limits | IA model, interaction patterns, component behavior requirements | No unresolved architecture conflicts on critical patterns | Before build kickoff for affected epic |
| R3 Engineering Manager | Delivery capacity, staffing constraints, implementation sequencing | UX scope tiers, phased fidelity targets, exception requests | Plan reflects feasible capacity and preserves critical UX outcomes | Weekly planning cadence |
| R4 Software Engineer | Feasibility feedback, implementation edge cases, telemetry hooks | Annotated specs, state definitions, error/recovery behavior, instrumentation requirements | Handoff package supports implementation with zero critical ambiguities | Prior to story `Ready for Dev` |
| R5 QA/Test Engineer | Test strategy constraints, severity policy, release gate criteria | Usability acceptance criteria, accessibility test matrix, expected behavior oracles | QA confirms testable acceptance and complete critical-flow coverage | Before feature test plan freeze |
| R6 SRE/Platform Engineer | Runtime constraints, observability standards, incident process | UX telemetry KPI definitions, alert thresholds, incident triage cues | UX alerts integrated and validated in staging | Before release candidate cut |
| R7 Security Engineer | Security-control UX requirements, abuse cases | Secure interaction patterns for auth/consent/recovery flows | Security UX controls pass threat-informed UX review | Before release approval |
| R8 Privacy/Compliance/Legal | Legal obligations for consent, disclosures, retention, user rights flows | Compliance-aware UX copy/flow designs and validation evidence | Legal/privacy sign-off recorded on regulated/high-risk flows | Before launch decision |
| R11 Technical Writer/DocOps | Documentation standards, terminology governance | Finalized UX terminology, state/change explanations, user-facing flow deltas | Docs reflect released behavior and limitation language accurately | Before documentation freeze |
| R12 DevOps/Release Manager | Release timeline, gate enforcement rules, rollback windows | UX gate evidence pack and unresolved UX risk statement | Mandatory UX/a11y gates complete; residual risk explicitly approved | At each release go/no-go |
| R13 Operations/Support/Customer Success | Ticket taxonomy, top user pain themes, escalation data | Prioritized UX remediation backlog and support-facing behavior notes | High-volume support pain points mapped to owned UX actions | Weekly after launch for 30 days |
| R15 Internal Audit/Assurance | Sampling plan and evidence integrity requirements | Replayable UX evidence bundle and decision ledger extracts | Auditor can reproduce sampled UX claims without author intervention | Per audit cycle or high-risk release |

## 7) Iteration-level improvement checklist

### Planning and framing
- [ ] Define release-critical journeys and decision questions with R1, including explicit success/failure thresholds.
- [ ] Lock iteration snapshot hash, study hypotheses, sampling quotas, and exclusion criteria before participant recruitment.
- [ ] Confirm legal/privacy/security constraints for consent, billing, and sensitive flows with R8/R7.
- [ ] Publish UX evidence schema (required artifacts, ownership, storage paths) for the iteration with who/what/where/time/version/hash fields.

### Research and design execution
- [ ] Run pilot sessions and log protocol deviations before full study launch.
- [ ] Achieve cohort quotas for primary and high-risk segments or escalate exceptions before analysis.
- [ ] Record and archive all critical sessions with auditable transcript linkage.
- [ ] Quantify task success, critical error rates, and time-on-task for release-critical workflows.
- [ ] Execute IA findability tests and content comprehension checks on prioritized tasks.
- [ ] Complete manual accessibility checks (keyboard + screen reader) on all release-critical paths.
- [ ] Log design-system exceptions with owner, expiry, and remediation task.
- [ ] Track contradiction cases with class, owner, SLA, and deterministic score consequence.

### Handoff and release readiness
- [ ] Deliver annotated specs with states, errors, and recovery behavior for each critical flow.
- [ ] Validate implementation fidelity on sampled high-risk stories before code freeze.
- [ ] Recompute one critical UX metric set from raw telemetry to validate report integrity.
- [ ] Confirm QA acceptance criteria and accessibility test matrix are complete and executable.
- [ ] Publish a single UX release packet: evidence index, unresolved risks, approved exceptions, and sign-offs.
- [ ] Execute same-iteration adversarial challenge for every proposed `90`/`100` row and attach evidence.
- [ ] Apply targeted re-evaluation for every approved delta before publication.

### Post-release learning and closure
- [ ] Monitor UX KPIs and support pain signals daily during first 14 days post-launch.
- [ ] Triage all high-severity UX incidents within SLA and assign corrective owners/dates.
- [ ] Verify closure effectiveness for critical remediations with follow-up user validation.
- [ ] Run anti-gaming audit sample (sessions, metrics recompute, decision ledger chronology).
- [ ] Roll unresolved exceptions forward only with renewed approval and new expiry date.

---

## R11 Technical Writer / DocOps / PDF Owner

- source_file: `swarm_outputs/role_expansions/R11_technical_writer_docops_pdf_owner.md`
- words: 4966
- lines: 207

# R11 Technical Writer / DocOps / PDF Owner Rubric Expansion

## 1) Role mission and decision rights

**Role mission**
R11 is accountable for publishable truth in documentation and PDFs: procedures must execute as written, claims must be traceable to approved sources, and published outputs must remain accessible, reproducible, and governable through their lifecycle. R11 owns documentation and PDF operational quality from draft intake through release, correction, localization, and archival.

R11 can block documentation/PDF release when evidence integrity, procedural correctness, accessibility, or publication controls fail. R11 does not unilaterally approve product scope, legal interpretation, or runtime production readiness, but can require documentation and PDF gates before release recommendation.

| Decision area | R11 authority boundary | Required co-approval | Escalation trigger |
| --- | --- | --- | --- |
| Procedure publication readiness | Final call on whether user/operator procedures are executable and complete | R4 for technical behavior; R5 for testability | Critical step cannot be executed from current artifact set |
| Canonical source designation | Final call on doc source-of-truth pointer and duplicate suppression | R1 for product policy docs; R2 for architecture docs | Two active artifacts claim authority for same requirement > 1 business day |
| Claim and citation admissibility | Can reject factual claims lacking resolvable citation and evidence | R8 for regulated/legal claims; R15 for audit disputes | Material claim used in release/public content without admissible source |
| PDF production acceptance | Can approve/reject PDF output based on accessibility, fidelity, and metadata checks | R12 for release gate timing | Tagged structure, reading order, or metadata controls fail on release-critical PDF |
| Link/reference gate criteria | Final call on link-check thresholds and blocker severity in docs/PDFs | R12 for go/no-go policy | Broken critical reference exceeds threshold at release cutoff |
| Localization freeze and release | Can hold localized docs when glossary/translation QA gates fail | R13 for support-language priorities | Target-locale critical safety or legal wording mismatch remains unresolved |
| Deprecation and archival notice quality | Final call on migration/deprecation notice completeness | R1 for policy impact; R13 for customer comms | End-of-life artifact lacks migration path, timeline, or owner |
| Correction notice publication | Can require errata/advisory publication and page-level correction map | R7/R8 when security/privacy/legal impact exists | Material inaccuracy persists past correction SLA |

### Iteration snapshot governance and delta re-evaluation controls

| Control | Requirement | Deterministic enforcement |
| --- | --- | --- |
| Iteration snapshot lock | Record `iteration_id`, rubric snapshot hash, role file hash, and scorer roster before first score. | Scores produced on an unapproved snapshot hash are invalid. |
| Denominator lock | Lock scored-row population and release-critical artifact set at snapshot time. | In-iteration denominator changes require approved delta dossier and dual reporting (`before`/`after`). |
| Delta dossier and targeted re-score | Any scoring-affecting update must include impacted rows, impacted gates, owner, approvers, and comparability note. | All impacted rows are rescored and impacted gate outcomes are replayed before publication. |
| Unauthorized drift tripwire | Detect anchor/gate/evidence-rule edits without authority-chain record. | Role output is held invalid until rollback or approved delta re-evaluation completes. |

### Non-zero evidence admissibility contract (mandatory fields)

| Field | Requirement for non-zero scoring | Rejection behavior when missing/invalid |
| --- | --- | --- |
| `who` | Named accountable author/reviewer | Row ineligible for score above `0` |
| `what` | Specific claim, procedure test, or gate outcome | Row ineligible for score above `0` |
| `where` | Immutable locator to evidence source | Row ineligible for score above `0` |
| `time_utc` | UTC capture timestamp | Row ineligible for score above `0` |
| `version` | Document/PDF/rubric snapshot version | Row ineligible for score above `0` |
| `hash` | Integrity hash for evidence artifact bundle | Row ineligible for score above `0` |
| `provenance_chain` | Source lineage from canonical source to rendered/scored artifact | Row ineligible for score above `0` |

| Admissibility sampling rule | Threshold | Deterministic effect |
| --- | --- | --- |
| Sampled non-zero rows missing any required field | `>5%` | Cap affected sub-dimensions at `50` and require targeted re-score |
| Sampled non-zero rows missing `time_utc`/`version`/`hash`/`provenance_chain` | `>10%` | Set R11 role score to `0` for the iteration pending remediation |

### High-anchor (`90`/`100`) dual-proof gate

| Requirement | Mandatory evidence | Deterministic consequence if missing |
| --- | --- | --- |
| Independent validator (non-author) | Independent review linked to row-level evidence IDs | Row capped at `75` |
| Same-iteration adversarial challenge | Challenge run (for example replay, contradiction injection, or gate-bypass attempt) with results | Row capped at `75` and targeted re-score required |
| Non-author replay parity | Replay confirms anchor and gate-state parity on affected rows | Row capped at `75`; publication package remains blocked for affected scope |

### Contradiction precedence protocol (deterministic)

| Contradiction class | Precedence order | Owner | SLA | Score and gate consequence |
| --- | --- | --- | --- | --- |
| Safety/legal/accessibility conflict vs publish-readiness claims | Highest | R11 + R8/R7 | 1 business day | Publication blocked; unresolved state forces FAIL via `G3`/`G4` |
| Canonical-source conflict across active artifacts | High | R11 + R1/R2 | 1 business day | Source-of-truth rows set to `0` until conflict closure evidence is attached |
| Citation admissibility conflict vs content quality claim | High | R11 + R15 | 1 business day | Citation and dependent rows capped at `50` until admissibility passes |
| Localization semantic conflict vs release timeline | Medium | R11 + R13 | 2 business days | Locale publication blocked and localization-governance rows capped at `50` |

## 2) Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| 1. Procedural accuracy and step executability | Procedures produce intended outcomes when followed exactly in declared environments. | Independent cold-run pass rate on critical procedures; step failure rate; undocumented prerequisite count per procedure. | Who: R11 owner + independent executor (not author). What: step replay logs, environment manifest, failure notes. Where: docs CI artifacts, runbook validation folder, issue tracker. |
| 2. Procedure completeness and precondition coverage | Procedures state prerequisites, permissions, rollback, and failure paths required for safe execution. | Missing-precondition defects; percent procedures with rollback steps; failure-mode branch coverage. | Who: R11 + R6/R4 reviewer. What: prerequisite checklist, rollback sections, failure branch tests. Where: source docs repo, review records, validation logs. |
| 3. Source-of-truth mapping and ownership integrity | Every controlled topic has one canonical owner artifact and authoritative version pointer. | Duplicate-authority conflict count; orphan page count; canonical mapping completeness. | Who: R11 + R1/R2 topic owners. What: canonical map, ownership matrix, conflict register. Where: docs governance registry, repo metadata, release packet. |
| 4. Citation and factual traceability | Non-trivial factual claims are linked to verifiable evidence with durable locators and revision context. | Claim-to-citation coverage; unresolved citation count; citation rot rate on sampled claims. | Who: author + reviewer + evidence custodian. What: claim map, citation index, source snapshots/hashes. Where: document source, evidence vault, audit trail. |
| 5. Standards/legal reference currency management | External standards, regulatory references, and policy citations are version-current or explicitly time-scoped. | Stale reference count; days since last standards sweep; unresolved superseded-reference alerts. | Who: R11 + R8 reviewer. What: standards register, freshness report, supersession decisions. Where: compliance reference ledger, doc repo, change log. |
| 6. Versioning, revision history, and change rationale | Each published change has semantic versioning, dated rationale, approver, and impact scope. | Unexplained diff rate; revision entry completeness; publish-without-rationale incidents. | Who: R11 release editor. What: changelog entries, approval records, diff summaries. Where: git history, release notes store, document front-matter metadata. |
| 7. Information architecture and document structure quality | Content organization supports task completion, accurate navigation, and predictable section semantics. | Navigation success in tree tests; misfiled-topic defect rate; section template conformance. | Who: R11 IA owner + sampled readers. What: IA map, navigation test results, template audit. Where: docs site config, usability notes, structure lint outputs. |
| 8. Readability and audience-fit language quality | Language matches target audience literacy/domain level without ambiguity or unnecessary cognitive load. | Reading-level threshold pass rate by doc class; ambiguity defect count; support ticket deflection quality. | Who: R11 editor + R13 support analyst. What: readability reports, ambiguity review comments, ticket linkage analysis. Where: content QA reports, support system, editorial reviews. |
| 9. Terminology governance and naming consistency | Controlled vocabulary is used consistently across docs, UI labels, API terms, and PDFs. | Glossary term drift count; prohibited-term usage; cross-artifact term mismatch rate. | Who: R11 terminology owner + R10/R4 contributors. What: glossary, term-lint reports, mismatch diff list. Where: terminology registry, CI lint outputs, design/dev handoff artifacts. |
| 10. Link, anchor, and cross-reference integrity | Internal/external links, anchors, references, and page citations resolve correctly after build and publish. | Broken-link rate; anchor-shift failures after build; unresolved cross-reference checks. | Who: R11 + DocOps pipeline owner. What: link checker output, anchor map, publish validation report. Where: CI pipeline logs, built artifact reports, monitoring dashboard. |
| 11. Command/code sample validity and environmental reproducibility | Commands and code snippets execute successfully in declared supported environments. | Snippet execution pass rate; environment-specific failure count; sample drift against product versions. | Who: R11 + R4/R5 validator. What: snippet test harness results, supported-environment matrix, failure reproductions. Where: docs test suite, CI jobs, sample repository. |
| 12. PDF accessibility semantics and reading-order correctness | PDF outputs preserve tags, logical reading order, alt text, heading hierarchy, and keyboard/screen-reader usability. | PDF/UA and WCAG check pass rate; reading-order defect count; AT critical-path completion rate. | Who: R11 PDF owner + accessibility reviewer. What: preflight reports, AT test evidence, tagged-structure inspection logs. Where: PDF QA artifacts, accessibility audit folder, release packet. |
| 13. PDF render determinism and layout fidelity | PDF generation is reproducible and layout-stable across approved renderer versions and platforms. | Hash/semantic diff stability across reruns; renderer compatibility defect rate; figure/table layout drift incidents. | Who: DocOps engineer + R11 approver. What: deterministic build logs, binary/text hash comparisons, renderer matrix report. Where: build pipeline artifacts, release provenance store, QA reports. |
| 14. Publication pipeline reliability and gate enforcement | Documentation/PDF publish pipeline enforces required quality gates and produces auditable release artifacts. | Gate bypass count; pipeline success rate for release branch; mean time to recover failed doc build. | Who: DocOps owner + R12 reviewer. What: pipeline configs, gate logs, bypass approvals. Where: CI/CD system, branch protection settings, incident records. |
| 15. Metadata, classification, redaction, and disclosure hygiene | Published files contain correct metadata and prevent unintended disclosure of sensitive/internal information. | Metadata policy pass rate; redaction failure count; accidental exposure incidents. | Who: R11 + R7/R8 reviewers. What: metadata scan outputs, redaction validation logs, disclosure incident postmortems. Where: preflight reports, security scan system, compliance tracker. |
| 16. Localization workflow and translation quality governance | Localization uses approved glossary/style guides, with tracked review and locale-specific risk checks. | Locale QA pass rate; critical mistranslation count; translation memory reuse with approved glossary compliance. | Who: localization lead + R11 reviewer + regional approver. What: localization QA reports, glossary conformance checks, sign-off records. Where: localization platform, docs repo, release checklist. |
| 17. Deprecation, migration notice, and archival governance | Deprecated content has clear migration path, timelines, redirects, and retention/legal-hold handling. | Missing migration notice count; stale deprecated-page traffic rate; archive retrievability pass rate. | Who: R11 + R1/R13 + records owner. What: deprecation notices, redirect map, archive validation logs. Where: docs portal, redirect config, records archive system. |
| 18. Post-publication defect triage and correction closure | Documentation/PDF defects are triaged by severity and corrected within SLA with transparent errata traceability. | Mean time to acknowledge doc defects; SLA breach rate by severity; recurrence rate of corrected defect class. | Who: R11 incident owner + support liaison. What: defect queue, errata notices, closure verification tests. Where: issue tracker, public changelog/errata page, support analytics. |

## 3) Scoring anchors table (0/25/50/75/90/100)
No sub-dimension may score above `50` without complete who/what/where/time/version/hash evidence, above `75` without independent reviewer validation, or above `90` without same-iteration adversarial challenge and non-author replay parity.

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Procedural accuracy and step executability | Procedures fail on basic replay; no verified execution evidence. | A few procedures replay, but critical procedures frequently fail or require tribal knowledge. | Most core procedures replay with intermittent failures and incomplete failure capture. | All release-critical procedures pass independent replay in declared environments. | Passes include edge-condition and rollback paths with low failure recurrence. | Two consecutive cycles with zero unresolved critical replay failures and reproducible logs for sampled procedures. |
| 2. Procedure completeness and precondition coverage | Prerequisites/rollback/failure paths absent. | Prerequisites listed inconsistently; rollback frequently missing. | Core prerequisites documented, but failure branches or permissions are incomplete. | Critical procedures include prerequisites, permissions, rollback, and failure handling. | Coverage includes common edge cases with verified branch execution evidence. | Two cycles with no Sev1/Sev2 incidents attributed to missing procedure preconditions or rollback guidance. |
| 3. Source-of-truth mapping and ownership integrity | No canonical mapping; conflicting documents coexist. | Canonical intent exists but many topics have competing authorities. | Most topics mapped, but conflicts/orphans remain unresolved. | Single authoritative source per controlled topic with named owner and version pointer. | Conflict detection and resolution SLA consistently met with low orphan rate. | Two cycles with zero unresolved authority conflicts on release-critical topics. |
| 4. Citation and factual traceability | Claims are uncited or cite unverifiable sources. | Some citations exist, but many claims cannot be replayed to source. | Majority of material claims cited; gaps remain on high-impact statements. | All material claims have resolvable citations with revision context. | Independent sampling replays citations with minimal locator decay. | Two cycles with full claim traceability and no material claim retractions from citation failure. |
| 5. Standards/legal reference currency management | Standards/legal references are stale or unknown. | Ad hoc updates occur after external challenge only. | Periodic refresh exists, but superseded references persist in critical docs. | Scheduled freshness sweep and explicit supersession handling for all regulated references. | Staleness alerts are proactive and closure SLA is consistently met. | Two cycles with zero release-critical docs containing superseded mandatory references. |
| 6. Versioning, revision history, and change rationale | Published changes have no version/rationale trail. | Version labels exist but rationale/approvals are often missing. | Most changes versioned; impact rationale inconsistently recorded. | Every publish includes semantic version, dated rationale, approver, and impact scope. | Diff-to-rationale quality supports fast audit replay with low ambiguity. | Two cycles with no undocumented release deltas and full audit replay success on sampled changes. |
| 7. Information architecture and document structure quality | Structure is inconsistent; users cannot locate key guidance. | Basic hierarchy exists but critical tasks require excessive navigation. | Core sections are findable; important edge topics are misplaced. | Critical task content is predictably structured and discoverable with template conformance. | Navigation tests show high first-attempt success across priority audiences. | Two cycles with no critical misrouting defects and sustained navigation test performance. |
| 8. Readability and audience-fit language quality | Content is confusing, jargon-heavy, or misaligned to audience. | Readability checks sporadic; ambiguity defects repeatedly escape. | Most content readable; complex sections still generate high clarification load. | Critical docs meet audience-fit language targets and pass ambiguity review. | Support/contact clarifications attributable to wording are low and trending down. | Two cycles with no critical incidents caused by ambiguous or audience-misaligned language. |
| 9. Terminology governance and naming consistency | Terms conflict across docs/UI/PDF; glossary absent or ignored. | Glossary exists but enforcement is weak and drift is common. | Common terms consistent, but high-impact mismatches still occur. | Controlled vocabulary enforced on release-critical content with low mismatch rate. | Cross-artifact term linting prevents most drift before merge. | Two cycles with zero critical term contradictions across docs, product UI, and PDFs. |
| 10. Link, anchor, and cross-reference integrity | Critical links/anchors are broken and unmonitored. | Link checks run irregularly; breakage is common at release. | Most links resolve; anchor/cross-reference failures still appear in key sections. | Release gates enforce low breakage thresholds and critical references resolve. | Monitoring catches post-publish regressions quickly with timely repair. | Two cycles with no unresolved critical broken references and stable link integrity trend. |
| 11. Command/code sample validity and environmental reproducibility | Samples are untested and fail when executed. | Manual spot-checking only; many samples fail in supported environments. | Core samples tested; environment-specific failures remain. | All critical samples tested automatically against declared environment matrix. | Drift detection catches version mismatches before publication. | Two cycles with zero unresolved critical sample failures on supported environments. |
| 12. PDF accessibility semantics and reading-order correctness | PDFs are untagged/misordered and unusable with assistive tech. | Automated checks run, but critical manual AT issues remain unresolved. | Most accessibility criteria pass; some critical-path AT gaps persist. | Release-critical PDFs pass tag/order/manual AT checks with tracked closure evidence. | Accessibility defects are rare, triaged fast, and verified before release. | Two cycles with zero unresolved critical PDF accessibility blockers and independent audit pass. |
| 13. PDF render determinism and layout fidelity | PDF builds are non-deterministic and layout drifts unpredictably. | Determinism not enforced; frequent renderer-dependent defects. | Deterministic builds for common path only; cross-renderer issues remain. | Rebuilds are deterministic within defined tolerance across approved renderers. | Compatibility matrix is routinely validated with low drift incident rate. | Two cycles with stable deterministic output and no material figure/table/layout regressions. |
| 14. Publication pipeline reliability and gate enforcement | Manual publishing bypasses controls; evidence not auditable. | Some automation exists but gate bypass is common and weakly approved. | Pipeline generally works; occasional gate failures/bypasses on critical releases. | Mandatory gates enforced on release branch with auditable logs and approvals. | Failure recovery is fast and bypasses are exceptional, justified, and time-bounded. | Two cycles with zero unauthorized gate bypasses and high pipeline reliability for release docs. |
| 15. Metadata, classification, redaction, and disclosure hygiene | Sensitive metadata/disclosure issues are present in published artifacts. | Policy exists but scans are inconsistent; leaks/misclassifications recur. | Scans catch most issues; occasional high-impact misses remain. | Metadata/redaction/disclosure checks are required and pass for critical releases. | Independent sampling confirms low residual leakage risk and timely correction. | Two cycles with zero material disclosure incidents from docs/PDF metadata or redaction failure. |
| 16. Localization workflow and translation quality governance | Localized content is uncontrolled; critical mistranslations untracked. | Translation performed without enforced glossary/style governance. | Process exists for major locales; QA gaps remain on critical terminology. | Priority locales pass QA with glossary conformance and named approvers. | Locale-specific risk checks and feedback loops keep severe mistranslations rare. | Two cycles with zero unresolved critical mistranslations in supported release locales. |
| 17. Deprecation, migration notice, and archival governance | Deprecated content removed/changed without migration guidance or retention control. | Notices appear late and lack owner/timeline. | Basic notices exist; redirects/archive retrieval inconsistent. | Deprecation includes migration path, date, owner, redirects, and retention handling. | Archive retrieval and redirect tests pass with low stale-traffic impact. | Two cycles with no critical customer/operational impact from deprecation or archival failures. |
| 18. Post-publication defect triage and correction closure | Doc/PDF defects are unowned and remain unresolved. | Defects logged but triage and correction SLAs are routinely missed. | Core triage works; recurring defect classes remain high. | Severity-based triage and correction SLAs are met for critical defects. | Root-cause actions reduce recurrence and errata are transparent. | Two cycles with no overdue critical doc defects and measurable recurrence reduction in top defect classes. |

## 4) Anti-gaming checks specific to this role

1. Enforce pre-publish evidence freeze: claims, citations, link-check reports, and replay logs are timestamped before release decision; post-freeze edits are inadmissible for current-cycle scoring.
2. Require blind replay sampling: at least 20% of release-critical procedures are executed by a non-author reviewer using only published docs.
3. Recompute citation validity independently on a sampled claim set; screenshot-only citation evidence is rejected.
4. Compare changelog entries against raw diffs; missing impact rationale or silent removals are scored as governance defects.
5. Detect link-check suppression by auditing ignore lists; new ignored patterns require explicit approval and expiry date.
6. Require binary-output PDF audits, not source-only reviews, for accessibility/metadata/redaction claims.
7. Validate snippet tests against supported-environment matrix; local-only pass claims do not count.
8. Run terminology drift diff across docs/UI/API strings each release; unresolved contradictions invalidate high terminology scores.
9. Audit localization claims against source/target segment and glossary conformance reports; vendor self-attestation alone is insufficient.
10. Require errata transparency: resolved critical defects must link old claim, corrected claim, and correction timestamp.
11. Enforce reviewer independence for any sub-dimension scored above 75; author-only approvals cap score at 75.
12. Track repeated waiver patterns (same gate waived more than twice per quarter); recurring waivers trigger automatic score cap at 50 for affected sub-dimensions until root cause closure.
13. Lock iteration snapshot hash and denominator before scoring; reject unapproved in-iteration drift.
14. Require approved delta dossier, impacted-row map, and targeted re-score for scoring-affecting updates.
15. Require independent validator plus same-iteration adversarial challenge for every proposed `90`/`100` row.

## 5) Tripwires and hard-fail conditions

| ID | Hard-fail condition | Detection rule | Immediate consequence |
| --- | --- | --- | --- |
| R11-HF1 | Fabricated or non-verifiable citation/evidence in released docs/PDF | Source locator cannot be resolved or evidence hash/timestamp mismatch on material claim | R11 score set to 0 for cycle; release/continued distribution blocked pending investigation |
| R11-HF2 | Release-critical procedure cannot be executed as published | Independent replay fails on critical path without approved emergency waiver | Release blocked until corrected and replay-pass evidence is attached |
| R11-HF3 | Critical PDF accessibility failure on mandatory distribution artifact | Tagged order/AT critical-path test fails at release cutoff | Release blocked for affected artifact |
| R11-HF4 | Sensitive data disclosure via metadata, redaction failure, or hidden layers | Preflight/security scan confirms exposure in distributable file | Immediate takedown/revocation; security/compliance escalation |
| R11-HF5 | Canonical source conflict on regulated/safety-critical instruction | Two authoritative docs conflict on required behavior and remain unresolved at decision time | Overall decision invalid; mandatory contradiction resolution before release |
| R11-HF6 | Unauthorized publish gate bypass on release branch | Pipeline/branch logs show bypass without approved emergency record | Release governance failure; affected release requires re-approval |
| R11-HF7 | Superseded legal/standards requirement published as current in regulated content | Freshness audit finds outdated mandatory reference on release-critical doc | Release blocked; compliance escalation to R8 |
| R11-HF8 | Localization error changes safety, financial, or legal meaning in supported locale | Locale QA or incident confirms semantic distortion in critical instruction | Locale-specific release halted; corrective notice and revalidation required |
| R11-HF9 | Broken critical links/references exceed approved threshold at launch | Link integrity gate fails threshold for critical references | Release blocked until link integrity gate passes |
| R11-HF10 | Critical doc defect remains uncorrected beyond SLA with known user harm | Defect tracker shows overdue Sev1/Sev2 doc issue with no approved risk acceptance | Executive escalation; no new doc approval authority until recovery plan is accepted |

Hard-fail rule: triggering `R11-HF1`, `R11-HF2`, `R11-HF3`, or `R11-HF4` is automatic release fail regardless of weighted score.

### Minimum recovery proof requirements

| ID | Minimum recovery proof before publication |
| --- | --- |
| R11-HF1 | Forensic closure memo, rebuilt immutable citation/evidence chain, and independent re-score of impacted rows |
| R11-HF2 | Corrected procedure plus independent cold replay pass in declared environment with logs |
| R11-HF3 | Corrected PDF artifact with manual AT retest evidence and accessibility gate replay pass |
| R11-HF4 | Confirmed takedown/remediation, metadata-redaction verification report, and security/compliance closure sign-off |
| R11-HF5 | Canonical source conflict resolution record with owner approvals and row-level rescoring |
| R11-HF6 | Restored gate enforcement controls, authorized approval-chain evidence, and publication gate recomputation parity |
| R11-HF7 | Updated current legal/standards references with freshness audit pass and compliance reviewer approval |
| R11-HF8 | Corrected locale content, semantic QA rerun pass, and locale-specific release validation evidence |
| R11-HF9 | Link-integrity rerun pass for critical references and updated release packet |
| R11-HF10 | Completed correction actions with effectiveness verification and accepted recovery plan for recurrence control |

## 6) Cross-role dependency and handoff criteria

| Counterparty role | Dependency into R11 | Handoff from R11 | Acceptance criteria | SLA |
| --- | --- | --- | --- | --- |
| R1 Product Manager | Product policy, audience priority, and release messaging scope | User-facing doc set, release notes, deprecation notices, unresolved-doc risk statement | All release-critical claims map to approved product decisions and owners | Before go/no-go meeting |
| R2 Product/Enterprise Architect | Canonical architecture constraints, interface boundaries, and topology changes | Updated architecture-facing docs and canonical source pointers | No unresolved contradiction between architecture records and published procedures | Within 2 business days of architecture approval |
| R4 Software Engineer | Actual implemented behavior, flags, and version compatibility details | Executable procedures, command samples, troubleshooting guidance | Sampled procedures run successfully against implemented behavior | Before code freeze for release docs |
| R5 QA/Test Engineer | Test outcomes, known defects, severity decisions | Test-oracle-aligned docs, known limitations section, validation references | QA confirms doc assertions match verified system behavior | Before release candidate sign-off |
| R6 SRE/Platform Engineer | Operational constraints, runbook inputs, incident learnings | Operations runbooks, rollback docs, incident update notes | On-call can execute runbooks without author intervention | Before production readiness review |
| R7 Security Engineer | Security controls, hardening instructions, disclosure requirements | Security guidance docs and secure configuration instructions | Security review confirms no unsafe defaults or missing critical warnings | Before security gate closure |
| R8 Privacy/Compliance/Legal | Regulatory wording, consent/disclosure obligations, retention rules | Compliance-sensitive content package with citation map and review history | Legal/compliance sign-off recorded for regulated claims | Before public/regional publication |
| R10 UX Researcher/Designer | UI terminology, flow semantics, accessibility intent | Consistent UI-help-doc terminology, task flow documentation, alt text conventions | Terminology and flow descriptions match released UX behavior | Before documentation freeze |
| R12 DevOps/Release Manager | Release schedule, gate policy, and deployment windows | Publish-ready artifact bundle with gate evidence and provenance | Required doc/PDF gates pass and are attached to release evidence bundle | At each release cut |
| R13 Operations/Support/Customer Success | Top support pain points, field workaround signals, locale escalations | Corrected KB articles, advisories, errata, and triage status | High-volume support issues have mapped corrective doc action and owner | Weekly, plus incident-driven |
| R15 Internal Audit/Assurance | Evidence admissibility criteria and sampling scope | Replayable evidence package: citations, diffs, logs, approvals, PDF preflight outputs | Auditor can reproduce sampled claims and gate decisions without author-only context | Per audit cycle or high-risk release |

## 7) Iteration-level improvement checklist

### Planning and control setup
- [ ] Confirm release-critical doc/PDF artifact inventory with named owners and canonical source pointers.
- [ ] Lock iteration snapshot hash and denominator; publish admissibility schema requiring who/what/where/time/version/hash for non-zero rows.
- [ ] Define quality thresholds for procedure replay, link integrity, snippet pass rate, and correction SLA.
- [ ] Publish reviewer independence plan for sub-dimensions expected to score above 75.
- [ ] Publish delta dossier template with impacted-row map and targeted re-score workflow.

### Authoring and validation execution
- [ ] Run independent cold replay on sampled critical procedures and capture environment manifests.
- [ ] Complete claim-to-citation mapping for all material claims and verify locator durability.
- [ ] Execute terminology drift checks across docs, UI strings, and API references.
- [ ] Run link/anchor/cross-reference checks on built artifacts, including PDF internal references.
- [ ] Execute snippet/command harness tests on declared supported environment matrix.
- [ ] Run PDF accessibility and metadata/redaction preflight on final distributable binaries.

### Release and handoff readiness
- [ ] Verify changelog completeness: rationale, owner, date, impact scope, and approver for each release delta.
- [ ] Confirm localization QA and glossary conformance for all in-scope locales.
- [ ] Attach full gate evidence bundle to release packet (no screenshot-only claims).
- [ ] Confirm no unresolved canonical-source conflicts for release-critical topics.
- [ ] Publish deprecation/migration notices and redirect plan for changed/retired docs.
- [ ] Execute same-iteration adversarial challenge for every proposed `90`/`100` row and attach proof.
- [ ] Apply targeted re-score and gate replay for every approved scoring-affecting delta before publication.

### Post-release governance and learning
- [ ] Monitor doc/PDF defect intake daily for first 14 days; enforce severity-based triage SLA.
- [ ] Publish errata with old/new claim linkage and correction timestamps for material fixes.
- [ ] Run anti-gaming audit sample: replay reproducibility, citation validity, gate bypass, reviewer independence.
- [ ] Review repeated waivers and unresolved exceptions; assign root-cause actions with due dates.
- [ ] Update next-cycle control thresholds using measured recurrence, SLA breaches, and near-miss findings.

---

## R12 DevOps / Release Manager

- source_file: `swarm_outputs/role_expansions/R12_devops_release_manager.md`
- words: 5505
- lines: 195

# R12 DevOps / Release Manager Rubric Expansion

## 1) Role mission and decision rights
R12 exists to ensure every production release is controlled, reproducible, authorized, reversible, and verifiable. The role is accountable for release control-plane integrity: gate enforcement, promotion discipline, approval legitimacy, evidence integrity, and rapid containment when change risk materializes. Delivery speed is not accepted as justification for bypassing control evidence.

R12 decision rights are binding for release authorization, pipeline governance, and emergency-path controls.

| Decision domain | R12 authority | Non-delegable constraint | Required decision record |
| --- | --- | --- | --- |
| CI/CD gate policy | Define and enforce mandatory release gates for protected branches and production promotion paths | No production promotion after failed mandatory check without approved time-bound waiver | Policy-as-code version, failed-check log, waiver ticket with expiry |
| Release go/no-go | Approve or block release after verifying gate outcomes, risk state, and evidence completeness | Schedule pressure cannot override missing critical evidence | Go/no-go record with approvers, timestamp, linked evidence packet |
| Approval chain and separation of duties | Enforce dual approval and approver eligibility for normal releases | No self-approval, no unauthorized approver delegation | Approval ledger with actor IDs, role mapping, and decision order |
| Artifact trust controls | Require artifact signing, provenance attestations, and SBOM before promotion | Unsigned or provenance-broken artifact cannot enter production | Signature verification logs, provenance attestations, SBOM report |
| Emergency release path | Allow emergency deployment under documented incident context and constrained blast radius | Emergency path requires retrospective review and cannot become default route | Emergency change record, incident link, retrospective report |
| Change window and freeze controls | Define release windows/freezes and enforce exception protocol | Out-of-window normal change is blocked unless approved as emergency | Change calendar, deployment timestamps, freeze exception approvals |
| Rollback control | Set rollback trigger criteria and drill cadence; block releases without viable recovery path | No high-risk release without tested rollback or accepted forward-fix fallback | Rollback drill outputs, trigger thresholds, recovery checklist |
| Release evidence retention | Define release packet minimum and retention controls | Missing or tampered packet invalidates release assurance for cycle | Immutable archive ID, checksum manifest, retrieval test log |

## 2) Sub-dimensions table

| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| R12-01 CI/CD gate policy integrity | Mandatory checks are codified and enforced uniformly across all production promotion paths. | 100% protected release pipelines include required checks; sampled bypass attempts are blocked; gate-definition drift alerts resolved within 5 business days. | Who: release manager + platform owner. What: policy-as-code files, gate execution logs, drift tickets. Where: VCS repo, CI system audit trail, ticket system. |
| R12-02 Branch protection and merge control enforcement | Production-bound code enters only through controlled merge paths with required review and status checks. | Direct push to protected branches = 0; required reviewer quorum met; status checks required and passing before merge. | Who: release manager + repo admin. What: branch protection config and merge audit logs. Where: Git hosting admin settings, audit export, PR records. |
| R12-03 Environment parity and drift control | Build/deploy environments are materially equivalent and configuration drift is monitored and corrected. | Stage-prod parity >= 95% for Tier-1 controls; drift detection runs weekly; unresolved critical drift older than 14 days = 0. | Who: DevOps engineer + service owner. What: IaC manifests, parity report, drift remediation evidence. Where: IaC repo, drift scanner output, change tickets. |
| R12-04 Reproducible build and dependency pinning | Release artifacts are reproducible from source with pinned dependencies and deterministic build inputs. | Independent rebuild hash match for sampled releases; unpinned critical dependency count = 0; reproducibility test executed every release cycle. | Who: build engineer + independent reviewer. What: build manifest, lockfiles, rebuild result log. Where: build system records, artifact registry metadata, CI job history. |
| R12-05 Artifact provenance, signing, and SBOM integrity | Every promoted artifact has verifiable provenance, cryptographic signature, and valid SBOM/license posture. | Signed artifact coverage = 100%; provenance attestation chain verifies; prohibited/unknown license release count = 0. | Who: release manager + security reviewer. What: signature verification report, provenance attestations, SBOM scan output. Where: artifact registry, signing service logs, compliance report store. |
| R12-06 Release approval chain integrity | Go/no-go decisions are attributable, ordered, and performed by authorized roles with separation of duties. | Dual approval compliance >= 99%; approval timestamps precede deploy start; unauthorized approver rate = 0. | Who: release manager + control owner. What: approval records, role-authority mapping, deploy timeline. Where: release management tool, IAM/HR role map, deployment logs. |
| R12-07 Change classification and CAB discipline | Changes are correctly classified (standard/normal/emergency) and governed by the required CAB workflow. | Classification completeness = 100%; CAB record exists for normal/emergency changes; emergency retrospective completed <= 2 business days. | Who: CAB chair + change owner. What: change records, CAB minutes, retrospective reports. Where: ITSM platform, CAB archive, PIR repository. |
| R12-08 Change window and freeze discipline | Changes are executed within approved windows and freeze policy exceptions are controlled and auditable. | Out-of-window normal changes = 0; freeze exception approvals are time-bound; repeated window violations trend to zero. | Who: release manager + operations lead. What: change calendar, deployment timestamp report, exception register. Where: release calendar system, CI/CD logs, governance tracker. |
| R12-09 Progressive delivery and blast-radius safeguards | High-risk releases use staged rollout controls with defined abort thresholds and blast-radius limits. | Canary/staged rollout usage for high-risk changes >= 95%; abort thresholds configured and tested; initial exposure within policy limit. | Who: release engineer + SRE reviewer. What: rollout plan, canary verdict logs, abort configuration evidence. Where: deployment orchestrator, observability dashboards, release runbook. |
| R12-10 Rollback readiness and emergency-path governance | Recovery paths are tested, executable, and governed to prevent uncontrolled emergency behavior. | Monthly rollback drill pass rate >= 90%; rollback p95 <= 10 minutes for scoped tier; emergency change rate monitored with corrective actions. | Who: release manager + incident lead. What: rollback drill results, emergency change trend report, mitigation actions. Where: drill tickets, deployment logs, change analytics dashboard. |
| R12-11 Schema/data migration safety control | Data and schema changes are compatibility-tested with explicit rollback/forward-fix strategy before release. | Expand/contract pattern used for incompatible changes; migration replay and rollback tests pass on prod-like data; irreversible migration waivers are approved pre-release. | Who: DB owner + release manager. What: migration plan, compatibility matrix, drill output. Where: migration repo, staging test logs, CAB waiver register. |
| R12-12 Pre-release verification evidence completeness | Release readiness requires complete verification package across functional, resilience, security, and compliance controls. | Readiness checklist completion = 100%; unresolved Sev1/Sev2 release blockers = 0; evidence packet assembled before approval. | Who: release manager + QA + security. What: checklist, test reports, risk acceptances. Where: release ticket, test management system, compliance evidence vault. |
| R12-13 Post-release verification and regression response | Post-deploy health checks, hypercare monitoring, and rollback triggers are executed within defined SLA. | Critical synthetic checks start <= 5 minutes after deploy; hypercare window executed for high-risk releases; threshold breach response within SLA. | Who: release manager + SRE on-call. What: post-release verification log, hypercare report, incident/rollback timeline. Where: monitoring platform, release record, incident system. |
| R12-14 Release metrics integrity and denominator governance | Delivery metrics (lead time, deployment frequency, change failure rate, MTTR) are computed from immutable event streams with stable definitions. | Independent metric recomputation matches published values; denominator exclusions are documented and approved; metric-definition changes are versioned and backfilled. | Who: release analytics owner + internal reviewer. What: metric methodology, recomputation worksheet, change log. Where: analytics pipeline repo, BI dashboard history, governance notes. |
| R12-15 Waiver and exception lifecycle governance | Control bypasses are explicit, time-bound, risk-scored, and tracked to closure with compensating controls. | Active expired waivers = 0; waiver renewal requires fresh approval; repeated waiver use on same control trends down. | Who: release manager + risk owner. What: waiver register, expiry report, compensating control evidence. Where: GRC/ITSM register, approval workflow log, control validation records. |
| R12-16 Release evidence retention and audit reproducibility | Release decisions and execution evidence are immutable, retrievable, and sufficient for independent reconstruction. | Release packet retrieval <= 2 business days; packet integrity check passes; sampled release can be reconstructed end-to-end by independent reviewer. | Who: release manager + audit reviewer. What: packet index, checksum/signature proofs, reconstruction test report. Where: evidence archive, immutable storage, audit workpapers. |
| R12-17 Release contradiction precedence determinism | Conflicts between release controls and delivery pressure are resolved by one precedence path with owner, SLA, and deterministic score effect. | Severity-1 contradiction register completeness = 100%; unresolved Severity-1 contradictions past SLA = 0; precedence decision timestamped <= 30 minutes for active release blockers. | Who: release manager + contradiction owner. What: contradiction register entry with class/severity, precedence decision, disposition, and score impact. Where: release governance tracker, CAB record, adjudication log. |
| R12-18 Independent replay and recompute determinism | R12 scoring outputs are reproducible by non-authors using the same snapshot and admissible evidence package. | Replay sample size >= max(15 rows, 20% of scored R12 rows) each iteration including all gate-sensitive rows; anchor variance <= 1 level; aggregate variance <= 5 points; gate-state parity = 100%. | Who: independent non-author reviewer + R15 witness. What: replay worksheet, recompute output, variance report, parity verdict. Where: scoring workbook, immutable evidence vault, replay run log. |
| R12-19 Iteration snapshot and delta re-evaluation governance | R12 scoring runs only on an approved iteration snapshot; scoring-affecting deltas require targeted re-evaluation before publication. | Iteration snapshot manifest approved before scoring = 100%; unauthorized scoring-affecting deltas = 0; approved deltas with impacted-row map + targeted rescore + parity check = 100%. | Who: release manager + R11/R15 approvers. What: snapshot manifest, approved delta dossier, impacted-row map, targeted rescore evidence. Where: version control history, governance approvals, scoring packet archive. |

## 2A) Non-zero evidence admissibility ledger (mandatory)

Every non-zero R12 claim must include all fields below in the iteration evidence ledger.

| Field | Requirement | Rejection rule |
| --- | --- | --- |
| `claim_id` | Unique row/claim identifier. | Missing ID -> claim scored `0`. |
| `who` | Named actor identity and role at decision time. | Missing/alias-only identity -> claim scored `0`. |
| `what` | Specific control/test/assertion being scored. | Narrative-only claim with no control reference -> claim scored `0`. |
| `where` | Immutable locator (repo path, ticket ID, log URI, artifact digest path). | Non-resolvable locator -> claim scored `0`. |
| `when_utc` | Capture timestamp in UTC. | Missing timestamp -> claim scored `0`. |
| `rubric_version` | Rubric semantic version used for this score. | Version mismatch with approved snapshot -> claim inadmissible. |
| `snapshot_id` | Iteration snapshot identifier/hash bundle. | Missing snapshot reference -> claim inadmissible. |
| `evidence_hash_sha256` | Integrity hash for artifact or canonical export. | Hash mismatch -> trigger `R12-HF5`. |
| `source_system` | System-of-record name. | Unattributed source -> claim scored `0`. |
| `cutoff_status` | `in_cutoff_window` or approved `reopen_id`. | Post-cutoff evidence without reopen ID -> excluded. |

Admissibility enforcement:
1. Any non-zero row missing any required field is scored `0` before aggregation.
2. If missing-field rate in the independent sample is `>5%`, cap R12 at `50` and force targeted rescore before publication.
3. Evidence added after cutoff is excluded from the current iteration unless approved reopen metadata exists.

## 2B) Deterministic contradiction precedence and publication effects

| Precedence rank | Contradiction class | Owner | SLA | Deterministic resolution | Deterministic score/publication effect |
| --- | --- | --- | --- | --- | --- |
| 1 | Failed mandatory gate vs delivery-date pressure | R12 | Immediate | Gate outcome wins. | Trigger `R12-HF1`; publication hold. |
| 2 | Active legal/privacy/security blocker vs release request | R8/R7 with R12 | Immediate | Compliance/security blocker wins. | Release blocked; unresolved state maps to global fail gates. |
| 3 | Reliability blocker (error budget exhausted, rollback readiness failed) vs release request | R6 with R12 | <= 30 minutes | Reliability blocker wins unless approved exception exists in snapshot. | Release blocked; score cannot exceed `50` for affected rows until closed. |
| 4 | Change-window or snapshot-policy breach vs schedule commitment | R12 | <= 30 minutes | Policy breach blocks normal release path. | Trigger `R12-HF8` or `R12-HF15`; publication hold. |
| 5 | Admissibility defect vs requested non-zero anchor | R12 scorer + R15 witness | <= 1 hour | Evidence rule wins; inadmissible claim removed. | Affected row forced to `0`; rescore required. |
| 6 | Severity-1 contradiction unresolved past SLA | Assigned contradiction owner | SLA expiry | Unresolved contradiction cannot be waived silently. | `R12-17` capped at `50`; publication blocked until closure evidence is attached. |

## 3) Scoring anchors table (0/25/50/75/90/100)
Use only `0`, `25`, `50`, `75`, `90`, `100`. No sub-dimension may score above `50` without complete evidence, above `75` without independent review, or above `90` without at least one successful in-cycle challenge test.

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R12-01 CI/CD gate policy integrity | Gate policy absent or unenforced on production path. | Policy exists but key gates are optional or routinely bypassed. | Mandatory gates enforced on some pipelines; exceptions and drift unmanaged. | Mandatory gates enforced across all protected promotion paths with documented exceptions. | Independent bypass attempt fails and sampled gate logs reconcile with policy. | Two consecutive quarters with zero unauthorized bypass and stable policy coverage. |
| R12-02 Branch protection and merge control enforcement | Direct pushes or unreviewed merges reach production branches. | Branch protections configured but frequently overridden. | Protections active for core repos; inconsistent reviewer/quorum enforcement remains. | Protected branches consistently enforce review quorum and required status checks. | Independent audit confirms no unauthorized merges in sample period. | Two quarters of full enforcement across all production-bound repositories. |
| R12-03 Environment parity and drift control | Environment state unknown; critical drift unmanaged. | Parity documented manually; drift checks sporadic and unverifiable. | Parity checks run with partial remediation; critical drift aging breaches occur. | Stage-prod parity and drift checks are routine; critical drift is timely remediated. | Independent parity/drift sample validates reported conformance. | Two quarters with sustained parity target and no overdue critical drift. |
| R12-04 Reproducible build and dependency pinning | Builds are non-deterministic and critical dependencies are unpinned. | Reproducibility claimed but no independent rebuild evidence. | Deterministic build controls exist for some release lines; pinning exceptions remain. | Independent rebuilds pass for release samples; critical dependencies are pinned. | Challenge rebuild by non-author reproduces artifact hash and metadata chain. | Two quarters of repeatable rebuild success without critical pinning violations. |
| R12-05 Artifact provenance, signing, and SBOM integrity | Production artifacts lack signatures/provenance or SBOM evidence. | Signing/SBOM exists but incomplete, unverifiable, or post-facto generated. | Most artifacts signed and scanned; occasional gaps or unresolved findings remain. | All promoted artifacts have verified signatures, provenance, and policy-compliant SBOM. | Independent verifier confirms provenance chain and transitive license checks on sample. | Two quarters with zero unsigned promotions and zero prohibited-license releases. |
| R12-06 Release approval chain integrity | Releases occur without authorized approval records. | Approval process exists but self-approval/role conflicts occur. | Dual approvals usually present; ordering or authority checks are inconsistent. | All normal releases have valid dual approvals with separation of duties and correct ordering. | Independent audit confirms approver authority and timestamp integrity on sampled releases. | Two quarters with no approval-chain violations across all production releases. |
| R12-07 Change classification and CAB discipline | Changes unclassified or intentionally misclassified to bypass governance. | Classification exists but CAB workflow is inconsistently applied. | Classes recorded reliably; emergency retrospective and risk capture are uneven. | Classification, CAB decisions, and emergency retrospectives are consistently complete. | Independent reclassification sample matches recorded class with only minor variance. | Two quarters with low emergency-path abuse and no material misclassification. |
| R12-08 Change window and freeze discipline | Normal changes routinely occur out of window or during freeze without authority. | Windows defined but not enforced; exception logging is incomplete. | Most releases respect windows; freeze exception controls are weak. | Window/freeze policy is enforced with approved, time-bound exceptions only. | Independent check of deployment timestamps confirms policy compliance. | Two quarters with zero unauthorized out-of-window normal releases. |
| R12-09 Progressive delivery and blast-radius safeguards | High-risk releases deploy full-blast with no staged controls. | Canary/staged rollout documented but often disabled at release time. | Progressive rollout used inconsistently; abort criteria not always enforced. | High-risk changes use staged rollout with enforced abort thresholds and blast-radius limits. | Independent replay confirms abort and promotion decisions align to observed health signals. | Two quarters with no Sev1 caused by missing staged-release controls. |
| R12-10 Rollback readiness and emergency-path governance | Rollback path absent or emergency changes uncontrolled. | Rollback documented but rarely tested; emergency path lacks governance closure. | Rollback drills happen but miss cadence/latency targets; emergency trend unmanaged. | Rollback drills and emergency controls meet policy cadence and performance targets. | Independent live drill validates recovery latency and governance records. | Two quarters with sustained rollback readiness and declining unjustified emergency usage. |
| R12-11 Schema/data migration safety control | Migration approach risks irreversible breakage without controls. | Migration steps documented but compatibility/rollback tests are missing. | Migration controls exist for common cases; edge compatibility gaps remain. | Compatibility and rollback/forward-fix strategy are validated pre-release for material migrations. | Independent adversarial migration rehearsal on prod-like data succeeds without corruption. | Two quarters of high-risk migrations with zero unplanned data-loss events. |
| R12-12 Pre-release verification evidence completeness | Release approved without required verification evidence. | Checklist exists but critical sections routinely incomplete. | Verification package assembled inconsistently; blocker handling is weak. | Complete evidence packet required and used for every release decision. | Independent reviewer verifies checklist truthfulness against raw test/control outputs. | Two quarters with zero releases approved on incomplete critical evidence. |
| R12-13 Post-release verification and regression response | Post-release checks absent; regressions detected only by customers. | Checks exist but start late or do not trigger timely response. | Hypercare used for some high-risk releases; response SLA misses persist. | Post-release checks and hypercare consistently execute with SLA-bound response. | Independent sampling confirms threshold breaches trigger rollback/mitigation on time. | Two quarters with no unmitigated critical regression escaping hypercare controls. |
| R12-14 Release metrics integrity and denominator governance | Metrics missing, fabricated, or methodologically invalid. | Metrics published but denominator rules are opaque or manipulated. | Core metrics exist with partial method documentation; recalculation gaps remain. | Metrics are reproducible from immutable events with versioned definitions and approved exclusions. | Independent recomputation matches published metrics and confirms denominator integrity. | Two quarters of stable, independently validated metrics with no manipulation findings. |
| R12-15 Waiver and exception lifecycle governance | Gate bypasses occur without approved waivers or expiry controls. | Waivers exist but lack risk rationale, expiry, or compensating controls. | Waiver process active; expiry enforcement and recurrence control inconsistent. | Waivers are approved, time-bound, risk-scored, and tracked to closure. | Independent sample shows no active expired waiver and valid compensating controls. | Two quarters with low waiver recurrence and zero unauthorized bypass events. |
| R12-16 Release evidence retention and audit reproducibility | Release evidence missing, mutable, or irretrievable. | Evidence retained inconsistently; packet reconstruction frequently fails. | Core packet retained for most releases; integrity checks/retrieval SLA inconsistent. | Immutable evidence packets are complete, retrievable, and sufficient for independent replay. | Independent auditor reconstructs sampled release decisions end-to-end within SLA. | Two quarters with zero integrity breaches and 100% successful reconstruction samples. |
| R12-17 Release contradiction precedence determinism | Contradictions are ad hoc, ownerless, or silently waived. | Contradictions logged but precedence/SLA/score effects are ambiguous. | Core protocol exists but unresolved Severity-1 handling is inconsistent. | Precedence, owner, SLA, and score effects are explicit and consistently applied. | Independent simulation reproduces identical outcomes on sampled contradiction cases. | Two iterations with zero unresolved Severity-1 contradiction at cutoff and zero precedence drift. |
| R12-18 Independent replay and recompute determinism | Non-author replay fails or cannot run from provided evidence. | Replay possible only with author intervention; variance exceeds policy. | Partial replay succeeds; sample size/tolerance rules are inconsistently met. | Required non-author replay sample and tolerance thresholds are met. | Replay includes all gate-sensitive rows and demonstrates full gate-state parity. | Two iterations with stable replay parity and no unexplained variance breaches. |
| R12-19 Iteration snapshot and delta re-evaluation governance | Scoring runs on uncontrolled versions; deltas are untracked. | Snapshot exists but scoring-affecting deltas bypass approval. | Snapshot control works for most changes; impacted-row retest is inconsistent. | Approved snapshot is enforced; every scoring-affecting delta has impacted-row rescore evidence. | Independent review confirms no unauthorized delta in scored scope. | Two iterations with full snapshot integrity and 100% targeted delta re-evaluation coverage. |

## 4) Anti-gaming checks specific to this role
1. Execute controlled failing checks on sampled pipelines each cycle; verify promotion is blocked and alert is emitted.
2. Reconcile CI summary dashboards against raw job logs and artifact metadata for sampled releases.
3. Compare deployment events in runtime platforms against CI/CD promotion records to detect out-of-band deploy paths.
4. Recompute lead time, CFR, and MTTR from raw immutable events; reject hand-edited spreadsheet metrics.
5. Validate approver authority by joining approval logs with IAM/HR role snapshots at decision timestamp.
6. Audit approval chronology; reject approvals created or edited after deployment start unless formal incident reopening exists.
7. Rebuild sampled artifacts from tagged commits using locked dependencies; verify hash and provenance equivalence.
8. Reclassify a random sample of emergency changes against policy; flag classification drift or intentional downgrade.
9. Inspect freeze-window exceptions for expiry, compensating controls, and explicit business-risk owner signoff.
10. Perform unannounced rollback drill on a selected high-risk service and compare actual execution to runbook claims.
11. Validate SBOM completeness against actual shipped transitive dependencies from registry manifests.
12. Attempt retrieval of randomly chosen historical release packets; failure to retrieve within SLA invalidates claimed readiness.

## 4A) Independent replay and >90 high-anchor challenge protocol

| Control | Requirement | Failure effect |
| --- | --- | --- |
| Replay sample coverage | Non-author replay on `max(15 rows, 20% of scored R12 rows)` each iteration. | Trigger `R12-HF14` until rerun meets coverage. |
| Gate-sensitive inclusion | Every row that can trigger/clear a gate must be in the replay sample. | Publication hold; targeted replay required. |
| Replay tolerance | Anchor variance `<=1`, aggregate variance `<=5 points`, gate-state parity `100%`. | Trigger `R12-HF14`; affected rows rescored. |
| `>75` proof | Independent reviewer evidence required in same iteration. | Cap affected row at `75`. |
| `>90` proof | Both independent replay pass and same-iteration adversarial challenge evidence are required. | Cap affected row at `75`; trigger `R12-HF16` if unresolved at cutoff. |
| Author separation | Evidence author cannot be sole scorer and sole validator on the same high-anchor row. | High-anchor claim invalidated; row rescored. |

## 5) Tripwires and hard-fail conditions

| ID | Tripwire / hard-fail condition | Effect |
| --- | --- | --- |
| R12-HF1 | Production promotion occurs after a failed mandatory gate without approved waiver. | Immediate role-level FAIL for cycle; affected release requires executive remediation review. |
| R12-HF2 | Manual or out-of-band production deployment has no authorized emergency record. | R12 score capped at 25; 100% deployment-path audit required next cycle. |
| R12-HF3 | Unsigned artifact or broken provenance chain is promoted to production. | R12-05 scored 0; release freeze on affected pipeline until trust controls revalidated. |
| R12-HF4 | Release approved by unauthorized actor or with self-approval violating separation of duties. | R12-06 scored 0; all approvals in cycle re-audited before next release. |
| R12-HF5 | Evidence tampering, backdated approvals, or altered release logs are detected. | Entire R12 score set to 0 for cycle; forensic audit and control-owner escalation mandatory. |
| R12-HF6 | Required rollback drill fails and remains unresolved past policy SLA. | R12-10 capped at 25; high-risk releases blocked until re-test passes. |
| R12-HF7 | Emergency change lacks retrospective review within 2 business days. | R12-07 and R12-10 capped at 25 until retrospective and corrective actions are verified. |
| R12-HF8 | Normal release executed during freeze window without approved exception. | R12-08 scored 0 for cycle; change-governance incident opened. |
| R12-HF9 | High-risk schema migration deployed without tested rollback/forward-fix strategy or approved exception. | R12-11 scored 0; migration path frozen pending independent validation. |
| R12-HF10 | Critical post-release verification checks are disabled or skipped for a high-risk release. | R12-13 capped at 25; release reliability review required before next cutover. |
| R12-HF11 | Active expired waiver permits continued bypass of mandatory control. | R12-15 scored 0; all active waivers re-certified within 5 business days. |
| R12-HF12 | Release evidence packet cannot be retrieved or reconstructed within required SLA. | R12-16 capped at 25; no anchor above 50 for audit-related sub-dimensions that cycle. |
| R12-HF13 | Severity-1 release contradiction remains unresolved past SLA. | R12-17 capped at 50 and publication blocked until contradiction closure evidence is approved. |
| R12-HF14 | Independent replay coverage or tolerance requirements are not met. | R12-18 capped at 25; no score publication until replay rerun passes tolerance. |
| R12-HF15 | Scoring-affecting rubric/evidence delta is applied after approved iteration snapshot without approved delta dossier. | R12-19 scored 0; iteration scoring packet marked invalid and rerun on approved snapshot. |
| R12-HF16 | Any proposed `>90` anchor lacks same-iteration adversarial challenge evidence. | Affected rows downgraded to `75`; publication blocked until challenge proof or rescore is complete. |

### Tripwire recovery proof requirements

| ID set | Minimum recovery proof | Verification authority | Reopen rule |
| --- | --- | --- | --- |
| R12-HF1, R12-HF8, R12-HF15 | Corrected control state, approved incident/change record, and full impacted-row rescore on approved snapshot. | R12 + R15 | Any recurrence in same iteration reopens incident and blocks publication. |
| R12-HF3, R12-HF5, R12-HF12 | Integrity forensics, corrected evidence pack with matching hashes, and independent reconstruction pass. | R15 + R7 (for provenance) | Any new hash mismatch reopens forensic review. |
| R12-HF13 | Contradiction closure record with owner, disposition, SLA compliance note, and score-impact trace. | R12 + counterpart owner + R15 witness | Reopened contradiction automatically reapplies publication hold. |
| R12-HF14, R12-HF16 | Replay/challenge rerun artifacts meeting coverage and tolerance rules with non-author signoff. | R15 witness + R12 owner | Later variance breach in same iteration reopens all impacted rows. |

## 6) Cross-role dependency and handoff criteria

| Counterpart role | R12 receives (entry criteria) | R12 hands off (exit criteria) | SLA / escalation trigger |
| --- | --- | --- | --- |
| R1 Product Manager | Approved scope, business risk acceptance, release readiness criteria, and freeze constraints. | Release decision with scope confirmation, deferred items list, and business-risk exceptions. | Escalate if scope changes after code freeze without approved risk update. |
| R2 Product Architect / Enterprise Architect | Architecture constraints, compatibility requirements, and migration strategy decisions. | Promotion plan confirming architecture guardrails and migration safety checks. | Escalate same day if architecture-required gate is missing from release plan. |
| R3 Engineering Manager | Team readiness, staffing coverage for release/hypercare, and dependency ownership confirmation. | Cutover schedule, support roster, and unresolved risk register with owners. | Escalate if no accountable owner for a critical release dependency within 1 business day. |
| R4 Software Engineer | Release candidate build, rollback notes, feature-flag strategy, and known-risk annotations. | Gate outcomes, promotion status, and rollback decision artifacts. | Escalate if candidate lacks rollback notes or required config manifest. |
| R5 QA / Test Engineer | Signed test verdict, coverage summary, open-defect risk assessment, and regression status. | Go/no-go record with linked quality evidence and accepted residual risk. | Escalate immediately for unresolved Sev1/Sev2 defects marked release-blocking. |
| R6 SRE / Platform Engineer | SLO/error-budget state, canary thresholds, observability readiness, and incident routing readiness. | Final release window, blast-radius plan, and rollback trigger thresholds. | Escalate if release requested while error budget is exhausted without waiver. |
| R7 Security Engineer / Security Architect | Security scan verdict, vulnerability waiver decisions, signing key status, and threat advisories. | Signed artifact/provenance confirmation and security gate pass/fail record. | Escalate within 30 minutes on active exploit or critical unpatched finding in release scope. |
| R8 Privacy / Compliance / Legal | Compliance obligations, required approvals, data-handling constraints, and notification obligations. | Release evidence packet mapping obligations to controls and approval chain records. | Escalate before go/no-go if any required legal/compliance signoff is missing. |
| R11 Technical Writer / DocOps / PDF Owner | Release notes draft, operator/user documentation deltas, and publication rollback plan. | Finalized release notes, publication timestamp, and documentation parity confirmation. | Escalate if user-impacting change lacks documentation update by release cutoff. |
| R13 Operations / Support / Customer Success | Support readiness checklist, incident comms templates, and customer-impact playbooks. | Release comms packet, hypercare status cadence, and known-issues/workaround list. | Escalate if frontline readiness is incomplete at T-4 hours to release window. |

## 7) Cycle-level improvement checklist
Use this checklist each scoring cycle (sprint, release train, or monthly governance review).

| Checklist item | Pass criterion | Evidence artifact |
| --- | --- | --- |
| Validate mandatory gate coverage | 100% production promotion paths include current mandatory controls. | Gate coverage report and policy diff review. |
| Lock approved iteration snapshot | Snapshot manifest includes rubric hash, scoring formula version, row population, and gate-order checksum before scoring. | Signed snapshot manifest and checksum ledger. |
| Audit protected branch controls | No unauthorized direct pushes/merges to protected production branches. | Branch protection audit export and exception log. |
| Re-run environment parity/drift scan | Parity target met and no overdue critical drift remediation. | Parity report, drift findings, closure tickets. |
| Execute reproducibility challenge build | Independent rebuild reproduces sampled artifact hash and metadata. | Rebuild job logs and hash comparison sheet. |
| Verify signatures/provenance/SBOM | Sampled releases pass signature, provenance, and license policy checks. | Verification report and scanner outputs. |
| Run contradiction precedence drill | All Severity-1 contradiction classes produce one deterministic resolution and score effect. | Contradiction simulation log and closure report. |
| Sample approval chain integrity | Sampled go/no-go decisions show valid approvers and correct chronology. | Approval audit worksheet with IAM role snapshot links. |
| Review change classification quality | Sample classification recheck shows low variance and complete retrospectives. | Classification audit results and CAB evidence links. |
| Validate change window/freeze compliance | No unauthorized out-of-window normal changes. | Deployment timestamp reconciliation report. |
| Drill staged rollout abort path | Canary abort works and promotion is blocked when threshold is breached. | Drill execution timeline and gate decision log. |
| Run rollback drill on high-risk path | Rollback/forward-fix recovery meets time and integrity targets. | Rollback drill ticket, timing metrics, integrity checks. |
| Re-verify migration safety controls | Material schema changes include tested compatibility and fallback strategy. | Migration checklist, replay results, waiver approvals if any. |
| Confirm pre-release evidence completeness | No release ticket closed without complete required evidence packet. | Checklist compliance report and missing-evidence exceptions. |
| Audit post-release hypercare response | High-risk releases have timely checks and threshold-driven response actions. | Hypercare report, alert timelines, mitigation records. |
| Recompute DORA metrics from raw events | Published metrics match independently recomputed values and denominators. | Recalculation workbook and methodology changelog. |
| Execute independent replay/recompute sample | Replay sample meets `max(15 rows, 20%)`, variance, and gate-parity requirements. | Replay transcript, variance report, gate-parity evidence. |
| Re-evaluate approved deltas | Every approved scoring-affecting delta has impacted-row mapping, targeted rescore, and parity check before publication. | Delta dossier, impacted-row map, and targeted replay output. |
| Expire and close waivers on time | Active expired waiver count is zero and recurrence is tracked. | Waiver expiry report and closure evidence. |
| Test release packet retrieval/reconstruction | Sampled historical releases reconstruct successfully within SLA. | Retrieval test log and reconstruction report. |

---

## R13 Operations / Support / Customer Success

- source_file: `swarm_outputs/role_expansions/R13_operations_support_customer_success.md`
- words: 5592
- lines: 197

# R13 Operations / Support / Customer Success Rubric Expansion

## 1) Role mission and decision rights
**Role mission**
Operate customer-facing support as a controlled production function: restore service quickly, communicate truthfully under uncertainty, preserve evidence quality, and convert incidents and tickets into durable product and reliability improvements.

**Decision rights**
| Decision area | R13 decision rights | Escalation boundary |
| --- | --- | --- |
| Ticket intake and routing policy | Owns channel rules, form schema, queue taxonomy, and routing automation. | Escalate to R3/R6 when routing policy materially changes pager load or incident command structure. |
| Severity assignment at intake | Can assign provisional severity using approved matrix and available evidence. | Escalate to R6 incident commander for disputed P1/P2 classification within 15 minutes. |
| Customer communication during incidents | Owns external wording, cadence, and channel selection for operational incidents. | Escalate to R7/R8 for security, privacy, legal, or regulatory-impact language. |
| Runbook execution for known issues | Can execute approved runbooks, mitigations, and workarounds. | Escalate to R4/R6 when runbook step fails, side effects appear, or rollback criteria trigger. |
| SLA and entitlement enforcement | Can prioritize work based on contractual tiers and support policy. | Escalate to R14/R8 when entitlement is ambiguous or contractual conflict exists. |
| Case closure authority | Can close only after evidence-backed validation checklist passes. | Escalate to R1/R3 when customer disputes root cause, scope, or fix ownership. |
| Problem management intake | Can open recurring-issue problem records and require RCA owners. | Escalate to R3 if owners are missing or action deadlines slip twice. |
| Knowledge base governance | Owns article lifecycle, validation cadence, and deprecation rules. | Escalate to R11 when source-of-truth conflict exists across docs. |

## 2) Sub-dimensions table
| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| R13.1 Intake channel integrity | Customer requests enter controlled channels with required metadata and deduplication. | Weekly sample of 50 tickets; intake schema completeness >= 95%; duplicate rate trend reviewed weekly; off-channel requests auto-redirect tested monthly. | Who: Support operations lead. What: queue export with completeness and duplicate flags, redirect logs. Where: ticketing system `ops-support` project and intake automation dashboard. |
| R13.2 Severity calibration accuracy | Priority reflects customer impact and urgency according to published matrix. | Biweekly blind re-grade of 30 tickets by independent reviewer; mismatch <= 10%; every P1/P2 has explicit severity rationale. | Who: Support manager plus R6 reviewer. What: severity matrix, sampled tickets, calibration report. Where: severity audit notebook and ticket links. |
| R13.3 First-response SLA compliance | Time-to-first-meaningful-response meets contracted targets by tier and channel. | Daily SLA dashboard by tier; meaningful-response quality spot-check on 20 tickets/week; breach RCA opened within 2 business days. | Who: Queue owner. What: SLA report, response transcripts, breach RCAs. Where: support BI dashboard and incident tracker. |
| R13.4 Escalation timeliness and path fidelity | High-risk or blocked cases reach the correct resolver group quickly with full context. | Escalation latency tracked for P1/P2 and blocked P3; >= 90% within target; misroute rate <= 8%; monthly escalation drill. | Who: Incident duty manager. What: escalation timestamps, route history, drill logs. Where: paging tool, ticket history, drill records repo. |
| R13.5 Runbook executability and coverage | Common failure modes have current, executable runbooks with rollback and stop conditions. | Top-incident classes mapped to runbooks; coverage >= 85%; monthly dry-run pass rate >= 90%; stale runbooks flagged if > 90 days unvalidated. | Who: Runbook owner roster. What: runbook index, dry-run outcomes, validation timestamps. Where: ops runbook repository and drill tracker. |
| R13.6 Customer incident communication quality | External updates are accurate, plain-language, and aligned with known facts and uncertainty. | P1 updates start <= 30 minutes; promised cadence adherence >= 95%; communication QA sample each major incident. | Who: Incident communications lead. What: outbound messages, QA checklist, correction log. Where: status communication archive and incident timeline. |
| R13.7 Status-page and broadcast cadence discipline | Qualifying incidents are posted and updated on public/internal channels on time with correct component scope. | >= 90% qualifying incidents posted <= 15 minutes; closure note within 24 hours; monthly reconciliation against incident register. | Who: Status manager. What: status page event logs, incident register, reconciliation report. Where: status platform export and incident system. |
| R13.8 Knowledge base accuracy and freshness | Support articles remain factual, reproducible, and current with product behavior. | Top 100 articles reviewed <= 90 days; broken link rate < 3%; random reproduction test of 20 articles/month. | Who: KB editor plus domain reviewer. What: article revision history, reproduction test results, link check report. Where: KB platform and doc QA records. |
| R13.9 Case chronology and evidence quality | Every case preserves a timestamped, replayable record of decisions and actions. | Weekly audit of 40 resolved tickets; >= 90% include timeline, actor, decision rationale, and evidence link; tamper anomalies = 0. | Who: Quality analyst. What: sampled case audits, evidence attachments, audit exceptions. Where: ticket comments, attachments, and QA workbook. |
| R13.10 Resolution validation before closure | Cases close only after outcome verification confirms issue is resolved for customer or monitored system. | Closure checklist completion >= 95%; 14-day reopen rate <= 8%; failed validations tracked as defects. | Who: Case owner and QA reviewer. What: closure checklist, confirmation artifact, reopen report. Where: ticket closure form and QA dashboard. |
| R13.11 Recurrence prevention and problem management | Repeated incidents convert into root-cause actions with tracked effectiveness. | RCA required for all P1/P2 and repeat P3; corrective-action on-time rate >= 80%; recurrence trend reviewed monthly. | Who: Problem manager. What: RCA docs, action tracker, recurrence dashboard. Where: problem management system and engineering backlog links. |
| R13.12 User-impact quantification quality | Incident and case impact is measured in affected users/accounts, duration, and business consequence. | Every P1/P2 includes impact estimate method; variance between early and final estimate <= 15% median; finance-impact fields complete >= 90%. | Who: Incident analyst. What: impact worksheets, telemetry extracts, post-incident true-up. Where: incident records and analytics warehouse. |
| R13.13 Entitlement and SLA-tier governance | Priority handling follows contractual support tiers without unauthorized overrides. | Tier mapping accuracy >= 95%; override approvals logged 100%; monthly contract-compliance audit with zero unexplained exceptions. | Who: Support operations manager. What: entitlement map, override log, compliance audit output. Where: CRM contract data and ticketing priority history. |
| R13.14 Engineering handoff quality | Escalations to engineering contain reproducible context and minimize bounce-back. | First-pass acceptance >= 90%; bounce-back <= 10%; handoff packet completeness scored weekly on 30 escalations. | Who: Support escalation lead and R4 counterpart. What: handoff template scores, bounce-back reasons, acceptance timestamps. Where: escalation queue and engineering issue tracker. |
| R13.15 Product feedback loop closure | High-frequency customer pain and feature gaps are converted into prioritized product actions with outcomes reported back. | Monthly top-issue digest linked to backlog; >= 80% of top recurring themes have owner and decision; closure notice sent to impacted accounts. | Who: CS operations lead and R1 PM. What: VOC digest, backlog links, customer follow-up logs. Where: product planning board and CRM activity history. |
| R13.16 Staffing and on-call resilience | Coverage model sustains committed service levels across peak load and absences. | Unfilled critical shifts < 2%; handoff checklist compliance >= 95%; fatigue threshold breaches tracked and corrected weekly; quarterly surge simulation. | Who: Support workforce manager. What: rota, attendance logs, handoff forms, simulation report. Where: scheduling tool and ops review folder. |
| R13.17 Tooling and automation reliability | Core support tooling and automations are observable, reliable, and safely changed. | Ticket platform uptime >= 99.5%; routing automation success >= 70%; failed automation alert MTTA <= 10 minutes; monthly rollback drill for automation changes. | Who: Support systems owner. What: uptime reports, automation run logs, alert and drill records. Where: observability stack and automation CI logs. |
| R13.18 CSAT/CES signal integrity and actionability | Satisfaction/effort signals are representative, resistant to manipulation, and tied to corrective action. | Survey response rate >= 12%; non-response bias review monthly; low-score action closure >= 80% within 30 days; trend segmented by tier. | Who: Customer success analyst. What: survey dataset, bias analysis, action tracker. Where: CS platform, BI model, and review minutes. |
| R13.19 Support contradiction handling and publication-block determinism | Support-critical contradictions are classified, owned, time-bound, and resolved through one deterministic precedence path. | Contradiction records include severity class/owner/SLA/precedence decision at 100%; unresolved Severity-1 contradictions past SLA = 0; publication-block decision issued <= 15 minutes for active Severity-1 support contradictions. | Who: support incident manager + contradiction owner. What: contradiction register entry, precedence decision log, disposition and score-impact record. Where: incident governance tracker, adjudication notes, scoring packet. |
| R13.20 Independent replay and recompute determinism | Support scoring outcomes can be reproduced by non-authors from the same snapshot and admissible evidence package. | Replay sample size >= max(20 rows, 20% of scored R13 rows) per iteration including all gate-sensitive rows; anchor variance <= 1 level; aggregate variance <= 5 points; gate-state parity = 100%. | Who: independent non-author scorer + R15 witness. What: replay transcript, recompute worksheet, variance report, gate-parity verdict. Where: immutable evidence store, scoring workbook, replay logs. |
| R13.21 Iteration snapshot and delta re-evaluation governance | Support scoring uses one approved iteration snapshot; scoring-affecting deltas require targeted re-evaluation before publication. | Snapshot manifest approved before scoring = 100%; unauthorized scoring-affecting deltas = 0; approved deltas with impacted-row map + targeted rescore + parity check = 100%. | Who: R13 owner + R11/R15 approvers. What: snapshot manifest, approved delta dossier, impacted-row mapping, targeted replay outputs. Where: version control history, governance approvals, scoring archive. |

## 2A) Non-zero evidence admissibility ledger (mandatory)

Every non-zero R13 claim must include all fields below in the iteration evidence ledger.

| Field | Requirement | Rejection rule |
| --- | --- | --- |
| `claim_id` | Unique row and claim identifier. | Missing ID -> claim scored `0`. |
| `who` | Named actor identity and role at event time. | Missing/alias-only identity -> claim scored `0`. |
| `what` | Specific support control or test asserted. | Narrative-only assertion -> claim scored `0`. |
| `where` | Immutable locator (ticket ID, incident ID, log URI, dashboard query ref). | Non-resolvable locator -> claim scored `0`. |
| `when_utc` | UTC event/capture timestamp. | Missing timestamp -> claim scored `0`. |
| `rubric_version` | Rubric version used for scoring. | Version mismatch with approved snapshot -> inadmissible. |
| `snapshot_id` | Iteration snapshot identifier/hash bundle. | Missing snapshot reference -> inadmissible. |
| `evidence_hash_sha256` | Integrity hash for attached evidence export/artifact. | Hash mismatch -> hard-fail review. |
| `source_system` | System-of-record for the evidence. | Unattributed source -> claim scored `0`. |
| `cutoff_status` | `in_cutoff_window` or approved `reopen_id`. | Post-cutoff evidence without reopen ID -> excluded. |

Admissibility enforcement:
1. Any non-zero row missing a required field is forced to `0` before aggregation.
2. If missing-field rate in independent sample exceeds `5%`, cap R13 at `50` and force targeted rescore.
3. Post-cutoff evidence is excluded from the current iteration unless approved reopen metadata exists.

## 2B) Deterministic contradiction precedence protocol

| Precedence rank | Contradiction class | Owner | SLA | Deterministic resolution | Deterministic score/publication effect |
| --- | --- | --- | --- | --- | --- |
| 1 | Active customer-impacting Severity-1 incident vs favorable SLA claim | R13 incident owner | Immediate | Incident state wins over aggregate SLA trend. | Publication blocked until Severity-1 contradiction is closed. |
| 2 | Security/privacy communication hold vs normal incident comms cadence | R7/R8 with R13 | Immediate | Security/privacy hold wins until approved message path exists. | Any bypass triggers role fail condition. |
| 3 | Entitlement contract tier vs manual priority override | R14/R8 with R13 | <= 2 hours | Contract tier and approved exception rules win. | Unauthorized override forces entitlement rows to `0` pending restatement. |
| 4 | Resolver acceptance missing vs escalation clock pause | R13 escalation owner | <= 30 minutes | Clock does not pause until accepted by correct resolver group. | Misreported SLA evidence invalidated for affected rows. |
| 5 | Admissibility defect vs requested non-zero anchor | R13 scorer + R15 witness | <= 1 hour | Evidence rule wins; inadmissible claim removed. | Affected row forced to `0`; targeted rescore required. |
| 6 | Severity-1 contradiction unresolved past SLA | Assigned contradiction owner | SLA expiry | Unresolved contradiction cannot be waived silently. | `R13.19` capped at `50`; publication blocked until closure evidence is approved. |

## 3) Scoring anchors table (0/25/50/75/90/100)
| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R13.1 Intake channel integrity | Requests are lost or unmanaged; no controlled intake path. | Channels exist but > 40% tickets miss mandatory fields; duplicates unmanaged. | Official intake exists; >= 70% schema completeness; dedupe is manual and inconsistent. | >= 90% controlled intake; >= 90% required fields complete; weekly dedupe review active. | >= 97% controlled intake; same-day dedupe; off-channel requests redirected automatically. | >= 99% controlled intake across two quarters; quarterly loss-injection tests and independent audit pass. |
| R13.2 Severity calibration accuracy | No severity matrix; prioritization is arbitrary. | Matrix exists but mismatch > 40% in sampled tickets. | Matrix used; mismatch <= 25%; rationale missing in many high-severity tickets. | Mismatch <= 10%; >= 95% P1/P2 have explicit rationale and evidence. | Mismatch <= 5%; monthly cross-team calibration with documented disputes resolved. | Mismatch <= 2% for two quarters; audits show no intentional downgrading behavior. |
| R13.3 First-response SLA compliance | SLA commitments undefined or unmeasured. | SLA measured but <= 60% met; responses are often non-meaningful. | 70% to 84% SLA attainment; quality checks are sporadic. | >= 90% attainment by tier; breach RCAs opened on time. | >= 95% attainment by tier and channel; meaningful-response QA pass >= 95%. | >= 98% attainment for two quarters with proactive breach prevention alerts. |
| R13.4 Escalation timeliness and path fidelity | No reliable escalation route; high-severity tickets stall. | Route exists but misroute > 30%; escalations frequently exceed targets. | Documented path; >= 70% escalations on time; misroute <= 20%. | >= 90% on-time escalation; misroute <= 8%; resolver acknowledgement tracked. | >= 95% on-time; misroute <= 3%; paging and ownership are automated. | >= 98% on-time plus quarterly drill pass and zero unowned P1 escalation. |
| R13.5 Runbook executability and coverage | No usable runbooks for common incidents. | Runbooks exist but stale; < 40% top issue classes covered. | >= 60% coverage; steps incomplete or non-reproducible in dry-runs. | >= 85% coverage; monthly dry-run pass >= 90%; rollback steps present. | >= 95% coverage; updates applied within 7 days of major behavior change. | >= 98% coverage; non-author operators succeed in simulations >= 95%. |
| R13.6 Customer incident communication quality | No customer updates or materially inaccurate updates. | Irregular updates; jargon-heavy; missing scope and next-update commitment. | Template-based updates but key fields missing in > 20% major incidents. | Updates start <= 30 minutes for P1 and include impact, scope, workaround, next update. | Promised cadence met >= 95%; corrections are transparent and timestamped. | >= 90% affected accounts rate updates useful; zero contradictory major-incident statements. |
| R13.7 Status-page and broadcast cadence discipline | Status page absent or never used for incidents. | Status page exists but > 30% qualifying incidents are not posted. | Major incidents posted with median delay > 45 minutes. | >= 90% qualifying incidents posted <= 15 minutes; closure notes within 24 hours. | >= 97% posted <= 10 minutes; component scope validated in review. | 99% timely postings with automated trigger evidence and monthly reconciliation clean. |
| R13.8 Knowledge base accuracy and freshness | KB missing or unusable for frontline support. | > 40% key articles stale or incorrect; no owner accountability. | Ownership defined; <= 70% top articles current; reproduction tests rare. | >= 90% top articles reviewed <= 90 days; broken links < 3%. | >= 97% articles current with reproducible steps and named validator. | >= 99% current for two quarters; spot audits show < 1% factual defects. |
| R13.9 Case chronology and evidence quality | Case history cannot reconstruct what happened. | Partial notes with missing timestamps, actors, and decision rationale. | >= 70% cases have timeline, but evidence links are inconsistent. | >= 90% cases have timestamped chronology and supporting artifacts. | >= 97% cases have replayable evidence chain and no tamper exceptions. | >= 99% forensic-grade records; independent reviewer can replay sampled cases end-to-end. |
| R13.10 Resolution validation before closure | Tickets close without verification; reopen rate uncontrolled. | Validation optional; reopen > 20% within 14 days. | Checklist exists; reopen <= 15%; confirmation evidence inconsistent. | Required validation evidence on >= 90% closures; reopen <= 8%. | Validation evidence on >= 95% closures; reopen <= 4%. | Reopen <= 2% for two quarters; random audit confirms closure rigor. |
| R13.11 Recurrence prevention and problem management | Repeat incidents accepted with no RCA or action tracking. | RCAs sporadic and blame-focused; actions lack owners and due dates. | RCA for P1 only; corrective-action on-time rate < 60%. | RCA for P1/P2 and repeat P3; >= 80% actions on time. | >= 90% on-time actions plus effectiveness checks after release. | Class-A recurrence reduced >= 50% year-over-year with verified causal controls. |
| R13.12 User-impact quantification quality | Impact is not measured or documented. | Impact estimates are anecdotal with no method statement. | Accounts and duration tracked but confidence and variance unknown. | Users/accounts, duration, and business impact quantified with documented method. | Median early-to-final estimate variance <= 15%; telemetry and CRM reconciled. | Variance <= 5% for major incidents; finance and ops independent sign-off present. |
| R13.13 Entitlement and SLA-tier governance | Contract tiers ignored; prioritization is arbitrary. | Tier rules exist but overrides are undocumented and frequent. | Tier mapping correctness around 70%; exception handling inconsistent. | >= 95% correct tier mapping; all overrides require named approver and reason. | >= 98% correct mapping; automated contract checks and monthly compliance review. | Zero unauthorized priority elevation in quarter; compliance audit has no material findings. |
| R13.14 Engineering handoff quality | Escalations are rejected for missing context. | Bounce-back > 30%; reproduction details often absent. | Template used; bounce-back <= 20%; key fields still missing frequently. | >= 90% first-pass acceptance; bounce-back <= 10%; reproducible packet standard met. | >= 95% first-pass acceptance; time-to-engineering-engage within target. | >= 98% acceptance for two quarters; no critical incident delayed by handoff quality. |
| R13.15 Product feedback loop closure | No systematic channel from support pain to product backlog. | Anecdotal escalation only; trends not quantified. | Monthly issue list exists but lacks owner decisions and traceability. | Top themes linked to backlog with owners, decisions, and target dates. | >= 85% top themes receive closed-loop update to affected customers/accounts. | Quantified churn/deflection improvement tied to closed-loop items and PM sign-off. |
| R13.16 Staffing and on-call resilience | Coverage gaps leave critical queues unowned. | Single points of failure common; > 20% critical shifts unfilled. | Rota exists; backup coverage weak; fatigue breaches unmanaged. | 24x7 committed-tier coverage; unfilled critical shifts < 5%; handoff discipline enforced. | Unfilled critical shifts < 2%; quarterly surge drills pass >= 90%. | Peak-load events handled without missed critical page due to staffing over two quarters. |
| R13.17 Tooling and automation reliability | Core support systems frequently fail without detection. | Tool outages and automation failures common; manual workarounds dominate. | Key tooling monitored; automation handles >= 40% routing. | Platform uptime >= 99.5%; automation >= 70%; failure alerts routed on-call. | Uptime >= 99.9%; automation >= 85%; false-route rate <= 3%. | Failover and rollback drills pass quarterly; change controls prevent silent automation regressions. |
| R13.18 CSAT/CES signal integrity and actionability | No satisfaction/effort signal captured. | Response rate < 5% or sampling is clearly biased and non-actionable. | Response >= 8%; segmentation partial; actions not consistently tracked. | Response >= 12%; monthly bias checks; low-score action plans logged. | Response >= 18% with statistically stable segment views; >= 85% action closure. | Signal predicts churn/escalation risk and interventions materially reduce negative outcomes. |
| R13.19 Support contradiction handling and publication-block determinism | Contradictions are ad hoc, ownerless, or non-blocking. | Contradictions tracked inconsistently; precedence or SLA effects are ambiguous. | Protocol exists for common cases only; Severity-1 handling still varies by reviewer. | Severity class, owner, SLA, precedence order, and score effect are explicit and enforced. | Independent simulation reproduces same contradiction outcomes across reviewers. | Two iterations with zero unresolved Severity-1 support contradiction at cutoff. |
| R13.20 Independent replay and recompute determinism | Non-author replay fails or cannot run from provided evidence. | Replay possible only with author intervention; variance breaches policy. | Partial replay succeeds but required sample coverage is inconsistent. | Required replay sample and tolerance thresholds are met each iteration. | Replay includes all gate-sensitive rows with full gate-state parity. | Two iterations with stable replay parity and zero unexplained variance breaches. |
| R13.21 Iteration snapshot and delta re-evaluation governance | Scoring runs on uncontrolled versions or undocumented deltas. | Snapshot exists but scoring-affecting deltas bypass approval. | Snapshot mostly enforced; impacted-row retesting is inconsistent. | Approved snapshot enforced; every scoring-affecting delta has impacted-row rescore evidence. | Independent review confirms no unauthorized delta in scored scope. | Two iterations with complete snapshot integrity and targeted retest coverage. |

## 3A) High-anchor proof thresholds (mandatory)

| Proposed anchor | Required proof set | Automatic downgrade when missing |
| --- | --- | --- |
| `>75` | Independent reviewer evidence from same iteration. | Downgrade to `75`. |
| `>90` | Independent reviewer evidence plus same-iteration adversarial challenge evidence and non-author replay pass. | Downgrade to `75` and publication hold until resolved or rescored. |
| `100` | `>90` requirements plus sustained control evidence across two consecutive iterations. | Downgrade to `90`. |

## 4) Anti-gaming checks specific to this role
| Gaming pattern to detect | Adversarial check | Control response | Scoring consequence |
| --- | --- | --- | --- |
| Severity downgrading to protect SLA | Re-grade random closed P1/P2 candidates using telemetry and customer impact facts. | Require independent R6 sign-off on disputed downgrades. | If intentional pattern confirmed, cap R13.2 and R13.3 at 50 for cycle. |
| Auto-acknowledgement counted as first response | NLP/keyword check flags empty or template-only responses lacking diagnosis or next step. | Redefine SLA metric to first meaningful response only. | Invalid responses removed from numerator; repeated abuse triggers hard-fail review. |
| Premature closure to suppress backlog | Compare closure timestamps to customer confirmations and reopen rates within 14 days. | Enforce closure checklist with mandatory confirmation evidence. | If > 5% sampled closures invalid, cap R13.10 at 25. |
| Ticket splitting to mask MTTR | Detect linked tickets with same root incident and fragmented durations. | Require parent-child incident linkage and aggregate resolution metric. | Manipulated cohorts excluded; R13.9 and R13.11 capped at 50. |
| Selective status-page omission | Reconcile incident register against status posts by component and severity. | Mandatory postmortem question: "Why not status-posted?" with approver name. | Unjustified omissions > 2 in cycle cap R13.7 at 25. |
| CSAT cherry-picking | Compare survey send rate by severity, tier, and outcome; flag suppression pockets. | Automated survey trigger at closure with limited manual suppression codes. | Biased sampling invalidates R13.18 score above 50. |
| KB inflation by low-value edits | Track semantic change size and reproducibility outcomes, not edit counts. | Score freshness on validated accuracy, not raw update volume. | Cosmetic update spikes ignored; no score lift without validation proof. |
| Escalation ping-pong to stop SLA clock | Audit ownership transitions and paused-state abuse. | Clock continues until accepted by correct resolver group. | Excess abusive pauses cap R13.4 at 50. |
| Off-tool support via private chats | Compare chat/email exports to ticket IDs; identify untracked work. | Require case ID for all customer-impacting support actions. | Untracked support > 3% sampled interactions caps R13.1 at 25. |
| Backdated notes or timestamp tampering | Immutable audit-log diff between created_at and edited_at plus actor trail review. | Lock critical fields post-closure; escalate anomalies to assurance role. | Any confirmed tampering sets R13.9 = 0 for cycle. |

## 4A) Independent replay and recompute protocol

| Control | Requirement | Failure effect |
| --- | --- | --- |
| Replay sample coverage | Non-author replay on `max(20 rows, 20% of scored R13 rows)` each iteration. | Trigger replay failure tripwire; publication hold until rerun passes. |
| Gate-sensitive inclusion | Every support row that can trigger/clear a gate must be sampled. | Publication hold and targeted replay required. |
| Replay tolerance | Anchor variance `<=1`, aggregate variance `<=5 points`, gate-state parity `100%`. | Affected rows rescored; role capped at `50` until corrected. |
| Recompute integrity | SLA and entitlement metrics recomputed from raw ticket/event data, not dashboards alone. | SLA/entitlement rows forced to `0` pending restatement. |
| Author separation | Replay reviewer cannot be the primary scorer for the same sampled row. | High-anchor evidence invalidated for affected rows. |

## 5) Tripwires and hard-fail conditions
| Tripwire condition | Hard-fail effect |
| --- | --- |
| Customer-impacting P1 lasts > 30 minutes without external acknowledgement. | Overall R13 cycle FAIL. |
| No named owner for active P1/P2 for any interval > 15 minutes. | Overall R13 cycle FAIL. |
| Confirmed falsification or tampering of case evidence, timestamps, or incident notes. | Overall R13 cycle FAIL and R13.9 forced to 0. |
| Contractual support entitlement violated for priority handling in regulated or top-tier accounts without approved exception. | Overall R13 cycle FAIL. |
| Security/privacy incident customer communication sent without required R7/R8 review where policy requires it. | Overall R13 cycle FAIL pending corrective control verification. |
| Repeated incident class recurs 3 times in 90 days with no accepted problem record or corrective owner. | Overall R13 score capped at 50. |
| Status-page suppression on major incidents to avoid reputational impact is evidenced. | Overall R13 cycle FAIL. |
| SLA reporting metric definitions changed mid-cycle without governance approval. | All SLA-related sub-dimension scores (R13.3, R13.4, R13.13) invalidated to 0 until restated. |

### Additional deterministic tripwires for contradiction, replay, and snapshot control

| ID | Tripwire condition | Immediate effect |
| --- | --- | --- |
| R13-HF9 | Severity-1 support contradiction unresolved past SLA. | `R13.19` capped at `50`; publication blocked until approved closure evidence is attached. |
| R13-HF10 | Independent replay coverage or tolerance requirements not met. | `R13.20` capped at `25`; no publication until replay rerun passes tolerance. |
| R13-HF11 | Any proposed `>90` anchor lacks same-iteration adversarial challenge evidence. | Affected rows downgraded to `75`; high-anchor publication blocked until resolved or rescored. |
| R13-HF12 | Scoring-affecting rubric/evidence delta applied after approved iteration snapshot without approved delta dossier. | `R13.21` set to `0`; iteration scoring packet marked invalid and rerun on approved snapshot. |

### Tripwire recovery proof requirements

| ID set | Minimum recovery proof | Verification authority | Reopen rule |
| --- | --- | --- | --- |
| R13-HF9 | Contradiction closure record with severity, owner, SLA compliance, disposition, and score-impact trace. | R13 + contradiction owner + R15 witness | Any recurrence of same unresolved contradiction class reopens publication hold. |
| R13-HF10 | Replay rerun artifacts meeting sample, tolerance, and gate-parity requirements. | R15 witness + R13 owner | New variance breach in same iteration reopens all impacted rows. |
| R13-HF11 | Same-iteration adversarial challenge evidence or approved rescore package at allowed anchor. | R13 owner + independent reviewer | Missing proof at any later publication check reopens hold. |
| R13-HF12 | Approved delta dossier, impacted-row map, targeted rescore, and parity report on approved snapshot. | R11 + R15 + R13 | Any unauthorized additional delta forces another invalidation review. |

## 6) Cross-role dependency and handoff criteria
| Dependency/handoff | Entry criteria from partner role | R13 handoff package requirements | Acceptance SLA and exit criteria |
| --- | --- | --- | --- |
| R13 -> R4 Software Engineer (defect escalation) | Reproducible issue suspected, customer/business impact quantified, severity assigned. | Steps to reproduce, expected vs actual behavior, logs/traces, account scope, workaround status, urgency rationale. | R4 acknowledges <= 30 minutes for P1/P2 and <= 4 hours for P3; exit when fix/mitigation committed and linked. |
| R13 -> R6 SRE/Platform (operational incident) | Service degradation/outage indicators observed or threshold alerts breached. | Incident timeline start, affected components, blast radius estimate, current mitigations, customer comms draft. | R6 incident command acceptance <= 15 minutes for P1; exit when incident state and command owner recorded. |
| R13 -> R7 Security (suspected abuse/breach) | Indicators of compromise, abuse pattern, or security-control failure. | Evidence chain, impacted identities/assets, containment actions taken, communication hold flags. | R7 ack <= 15 minutes for critical, <= 1 hour for high; exit when case triaged and legal/forensic path assigned. |
| R13 -> R8 Privacy/Compliance/Legal (regulated exposure) | Potential personal-data impact or contractual reporting obligation. | Data categories, affected jurisdictions/accounts, timeline, known disclosures, draft customer/regulator statements. | R8 decision <= 2 hours for reportable risk; exit when communication and reporting obligations explicitly approved. |
| R13 -> R1 Product Manager (recurring pain/theme) | Recurrence threshold exceeded or high-value feature gap confirmed by evidence. | Theme quantification, account impact, revenue/churn risk, failed workarounds, candidate requirement language. | R1 triage decision <= 10 business days; exit when backlog item decision and owner are recorded. |
| R12 Release Manager -> R13 (release readiness) | Upcoming release introduces support-impacting change. | Runbook deltas, known issues, rollback conditions, customer-facing notes, monitoring expectations. | R13 readiness sign-off before release window; exit when support playbook published and staffed. |
| R11 Technical Writer <-> R13 (KB/source-of-truth sync) | KB or product docs disagree or major process changed. | Conflict ticket with evidence, proposed canonical text, validation owner, publish deadline. | Joint resolution <= 5 business days; exit when source-of-truth location and redirects are updated. |
| R14 FinOps/Procurement -> R13 (entitlement changes) | Contract tier, SLA terms, or support scope changed. | Effective date, impacted accounts, priority/response obligations, exception rules, communication plan. | R13 operational policy updated before effective date; exit when entitlement mapping test passes. |

## 7) Cycle-level improvement checklist
Use this checklist each operating cycle (weekly ops review plus monthly governance review). A checked item requires linked evidence.

| Checklist item | Evidence required |
| --- | --- |
| [ ] Re-ran severity calibration sample and logged mismatch rate with named reviewer. | Calibration report with sampled ticket IDs and decisions. |
| [ ] Locked approved iteration snapshot before scoring. | Signed snapshot manifest with rubric hash, scorebook version, and row-population checksum. |
| [ ] Reviewed SLA misses by tier/channel and opened RCAs for material breaches. | SLA breach list and RCA issue links. |
| [ ] Replayed contradiction precedence scenarios for active Severity-1 support contradictions. | Contradiction simulation log and closure record. |
| [ ] Executed at least one escalation-path drill and documented timing defects. | Drill record with participants, timings, and actions. |
| [ ] Validated runbook freshness for top incident classes and updated stale items. | Runbook index with validation dates and commit links. |
| [ ] Reconciled status-page posts with incident register and resolved any gaps. | Reconciliation sheet and exception decisions. |
| [ ] Audited closure quality and reopen causes; corrected checklist defects. | Closure audit sample and reopen analysis. |
| [ ] Reviewed recurrence dashboard and verified problem-action effectiveness. | Problem tracker export with effectiveness field completion. |
| [ ] Performed entitlement override audit and approved exceptions explicitly. | Override log with approver identity and rationale. |
| [ ] Checked CSAT/CES sampling bias and closed low-score actions on schedule. | Survey bias analysis and action tracker status. |
| [ ] Executed independent replay/recompute sample for support scoring. | Replay transcript, recompute worksheet, and variance report. |
| [ ] Audited all proposed `>90` anchors for independent and challenge evidence. | High-anchor proof audit pack and downgrade/rescore decisions. |
| [ ] Delivered cross-role VOC digest to R1/R3/R6 with acknowledged owners. | Digest artifact, meeting notes, and owner assignments. |
| [ ] Confirmed on-call staffing resilience for upcoming cycle including backup coverage. | Published rota, handoff checklist, and absence contingency plan. |
| [ ] Verified support tooling alerting and automation rollback readiness. | Monitoring health report and latest rollback drill output. |
| [ ] Re-evaluated every approved scoring-affecting delta before publication. | Delta dossier, impacted-row map, and targeted rescore output. |

---

## R14 FinOps / Procurement / Vendor Management

- source_file: `swarm_outputs/role_expansions/R14_finops_procurement_vendor_management.md`
- words: 6002
- lines: 206

# R14 FinOps / Procurement / Vendor Management Rubric Expansion

## 1) Role mission and decision rights
**Role mission**
Control total third-party and platform spend as an evidence-driven operating system: make cost transparent, keep commercial commitments enforceable, reduce waste without harming reliability or compliance, and preserve credible exit options for every material vendor dependency.

**Decision rights**
| Decision area | R14 decision rights | Escalation boundary |
| --- | --- | --- |
| Cost policy and allocation model | Owns cost taxonomy, tagging/account-coding standards, and showback/chargeback rules. | Escalate to R0/R1 when reallocation changes product P&L or customer pricing. |
| Budget guardrails and spend thresholds | Sets warning and hard-stop thresholds for categories/accounts/vendors within approved budgets. | Escalate to R0/CFO delegate for any forecasted overrun above approved tolerance. |
| Purchase intake and commercial routing | Owns procurement workflow, required approvers, and sourcing path by spend/risk tier. | Escalate to R8 when legal/regulatory obligations conflict with purchase urgency. |
| Vendor onboarding controls | Can block onboarding until due diligence artifacts are complete and verified. | Escalate to R7/R8 for unresolved security/privacy/legal findings. |
| Contract and renewal governance | Owns obligation register, renewal calendar, and negotiation workback schedule. | Escalate to R0 for term, liability, or strategic lock-in decisions outside policy. |
| Invoice/payment controls | Can hold payment when PO/receipt/invoice mismatch exceeds tolerance or evidence is incomplete. | Escalate to finance controller for emergency release or disputed contractual interpretation. |
| Savings program portfolio | Prioritizes optimization initiatives (rightsizing, commitment plans, license rationalization) and savings verification rules. | Escalate to R3/R6 if optimization plan creates reliability or delivery risk. |
| Vendor performance enforcement | Can issue service-credit notices and corrective-action demands based on SLA evidence. | Escalate to R8 for formal notice, breach remediation, or termination path. |

## 2) Sub-dimensions table
| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash/provenance) |
| --- | --- | --- | --- |
| R14.1 Spend data completeness and tagging fidelity | All material spend records are attributable to owner, cost center, product/service, environment, and contract vehicle. | Monthly full-population completeness check; mandatory field completeness >= 98%; unallocated spend <= 2%; cloud-bill to AP-ledger variance <= 0.5%. | Who: FinOps lead and AP analyst. What: billing exports, ERP ledger extract, tag coverage report, reconciliation workbook. Where: `finops_spend_mart`, ERP AP module, monthly evidence folder. |
| R14.2 Unit economics model integrity | Unit-cost models use stable formulas, controlled denominators, and versioned assumptions tied to real usage. | Formula review each cycle; denominator source traceability = 100%; unexplained unit-cost variance > 10% gets RCA within 5 business days. | Who: FinOps analyst with R1 finance partner. What: metric dictionary, formula changelog, variance RCA tickets. Where: BI semantic model, rubric evidence repo. |
| R14.3 Forecast accuracy and variance response discipline | Forecasts are evidence-based, refreshed on cadence, and trigger timely corrective actions when variance breaches tolerance. | Rolling 90-day forecast MAPE <= 10% for top spend categories; weekly reforecast cadence met >= 95%; variance breach response started <= 3 business days. | Who: Procurement finance manager. What: forecast snapshots, actual-vs-forecast trend, variance action log. Where: planning workbook, finance dashboard, issue tracker. |
| R14.4 Budget guardrail and commitment governance | Approved budgets and commitment envelopes are enforced with explicit pre-approval paths and exception controls. | Budget overrun without approved exception = 0; alert coverage on budget owners = 100%; commitment utilization reviewed weekly for top contracts. | Who: Budget owner plus R14 controller. What: threshold policies, alert logs, exception approvals, commitment reports. Where: budget system, notification logs, governance minutes. |
| R14.5 Purchase intake and approval discipline | Every purchase request follows the approved workflow with risk tiering, approver traceability, and policy checks. | Off-workflow purchases <= 1%; approval SLA met >= 90% by tier; sampled requests show policy checklist completion >= 95%. | Who: Procurement operations manager. What: intake tickets, approval chain logs, policy checklist audits. Where: procurement tool workflow records, audit workbook. |
| R14.6 Vendor due diligence and onboarding risk controls | New or materially changed vendors pass security, privacy, legal, and financial-risk checks before production use. | Due-diligence package completeness = 100% for critical vendors; unresolved high-risk findings at go-live = 0; reassessment cadence adherence >= 95%. | Who: Vendor risk owner with R7/R8 reviewers. What: diligence questionnaires, control attestations, risk register decisions. Where: vendor risk register, GRC system, contract folder. |
| R14.7 Contract obligation traceability and calendar discipline | Commercial terms, obligations, and milestones are fully traceable from clause to control owner and due date. | Clause-to-control mapping completeness >= 95%; upcoming obligations (60/30/15 days) acknowledged by owners = 100%; missed contractual notice dates = 0. | Who: Contract manager. What: clause matrix, obligation calendar, owner acknowledgements. Where: CLM system, shared obligations tracker, meeting records. |
| R14.8 Invoice validation and payment accuracy controls | Invoices are paid only after amount, quantity, rate, and service period are validated against contract/PO/receipt evidence. | 3-way match pass rate >= 97%; duplicate payment rate = 0; disputed invoice resolution median <= 15 business days. | Who: AP lead and procurement analyst. What: invoice match logs, dispute register, payment hold releases. Where: ERP AP workflow, AP controls dashboard. |
| R14.9 Savings claim validity and realization tracking | Claimed savings are calculated from approved baselines, net of offsets, and validated in realized spend. | Savings with baseline and counterfactual evidence = 100%; realized-vs-claimed delta within +/-10%; one-time vs recurring savings separated in all reports. | Who: FinOps program manager. What: savings ledger, baseline snapshots, offset adjustments, realization reports. Where: optimization portfolio tracker, finance close package. |
| R14.10 Commitment utilization and waste remediation | Reserved/committed spend instruments and enterprise agreements are actively managed to avoid underutilization and waste. | Commitment utilization >= 85% for material plans; idle/unused committed assets remediated <= 30 days; burn-down reviewed weekly. | Who: Cloud economics owner. What: commitment utilization reports, remediation tickets, burn-down dashboard. Where: cloud provider consoles, FinOps dashboard, backlog board. |
| R14.11 License entitlement and commercial compliance | Software usage aligns with purchased entitlements and contract terms, avoiding under-licensing and paid shelfware. | True-up surprises at audit = 0; shelfware ratio <= 10% for top license pools; access-to-license reconciliation coverage = 100% monthly. | Who: License manager. What: entitlement positions, user assignment extracts, vendor audit correspondence. Where: SAM tool, identity system exports, contract archive. |
| R14.12 Cost anomaly detection and response quality | Material spend anomalies are detected quickly, triaged to owner, and resolved with root-cause prevention actions. | P1 anomaly detection latency <= 24h; owner assignment <= 4h from alert; anomaly recurrence after closure <= 10% quarterly. | Who: FinOps on-call owner. What: anomaly alerts, triage timelines, RCA and prevention tasks. Where: observability/FinOps alerting stack, incident tracker. |
| R14.13 Pricing model optimization and negotiation quality | Pricing structure and negotiated terms reflect usage profile, volume leverage, and risk-adjusted alternatives. | Competitive benchmark refreshed <= 180 days; negotiated effective-rate improvement documented for each major renewal; concession tracking completeness = 100%. | Who: Sourcing lead. What: benchmark packs, negotiation issue log, final term sheets. Where: sourcing workspace, CLM attachments, executive review deck. |
| R14.14 Renewal readiness and leverage posture | Renewal strategy is started early with BATNA options, consumption truths, and approval-ready scenarios. | Renewal workback starts >= 120 days pre-expiry for critical vendors; decision packet completeness >= 95%; late/auto-renew events = 0. | Who: Category manager. What: renewal calendar, BATNA analysis, scenario packets, approvals. Where: renewal tracker, decision memo repository. |
| R14.15 Vendor performance and SLA credit enforcement | Vendor performance is measured against contract SLAs and credits/penalties are pursued with evidence-backed claims. | Monthly SLA compliance pack produced 100%; unclaimed eligible service credits <= 5%; corrective-action plans opened for repeated breaches. | Who: Vendor manager with service owner. What: SLA measurements, credit claim submissions, corrective-action logs. Where: vendor governance portal, contract evidence folder. |
| R14.16 Concentration and lock-in risk management | Dependency concentration and lock-in risk are quantified, reviewed, and mitigated for critical capabilities/vendors. | Top-5 vendor concentration ratio tracked monthly; single-vendor critical capability without mitigation <= 10%; dual-source or contingency plans validated annually. | Who: Procurement risk lead. What: concentration analysis, lock-in heatmap, mitigation plans. Where: risk dashboard, architecture dependency register. |
| R14.17 Exit and transition readiness | For critical vendors, a tested exit path exists with data portability, runbook, timeline, and accountable owner. | Exit plan coverage = 100% for critical vendors; annual tabletop or simulation pass >= 90%; data export test success = 100% for sampled systems. | Who: Vendor transition owner. What: exit playbooks, simulation reports, portability test artifacts. Where: BCM repository, vendor transition workspace. |
| R14.18 Chargeback/showback trust and stakeholder alignment | Cost allocation outputs are explainable, dispute-managed, and trusted by product/engineering/finance stakeholders. | Billing dispute rate <= 5%; dispute closure median <= 10 business days; independent recomputation of sampled bills matches >= 99%. | Who: FinOps business partner. What: chargeback statements, dispute logs, recomputation worksheets, sign-off minutes. Where: cost allocation platform, finance governance archive. |
| R14.19 Cost-vs-risk contradiction precedence determinism | Commercial tradeoff contradictions (cost vs reliability/security/privacy/service commitments) are resolved through one precedence path with owner and SLA. | Contradiction records with severity/owner/SLA/precedence decision = 100%; unresolved Severity-1 contradictions past SLA = 0; precedence decision for Severity-1 issued <= 4 business hours. | Who: FinOps lead + contradiction owner. What: contradiction register, precedence decision log, score-impact disposition. Where: governance tracker, CAB/commercial review minutes, scoring packet. |
| R14.20 Independent replay and recompute determinism | R14 scores are reproducible by non-authors from admissible evidence and stable formulas. | Replay sample size >= max(15 rows, 15% of scored R14 rows) each iteration including all gate-sensitive rows; anchor variance <= 1 level; aggregate variance <= 5 points; gate-state parity = 100%. | Who: independent non-author scorer + R15 witness. What: replay transcript, recompute workbook, variance report, parity verdict. Where: immutable evidence vault, scoring workbook, replay logs. |
| R14.21 Iteration snapshot and delta re-evaluation governance | R14 scoring runs only on an approved iteration snapshot and approved deltas with targeted re-evaluation. | Snapshot manifest approved before scoring = 100%; unauthorized scoring-affecting delta count = 0; approved deltas with impacted-row map + targeted rescore + parity check = 100%. | Who: R14 owner + R11/R15 approvers. What: snapshot manifest, approved delta dossier, impacted-row mapping, targeted replay evidence. Where: version control history, governance approvals, scoring archive. |

## 2A) Non-zero evidence admissibility ledger (mandatory)

Every non-zero R14 claim must include all fields below in the iteration evidence ledger.

| Field | Requirement | Rejection rule |
| --- | --- | --- |
| `claim_id` | Unique row/claim identifier. | Missing ID -> claim scored `0`. |
| `who` | Named actor identity and decision-time role. | Missing/alias-only identity -> claim scored `0`. |
| `what` | Specific commercial control or computation asserted. | Narrative-only claim -> claim scored `0`. |
| `where` | Immutable locator (CLM clause ID, ERP voucher ID, dashboard query ref, workbook cell mapping). | Non-resolvable locator -> claim scored `0`. |
| `when_utc` | UTC capture timestamp. | Missing timestamp -> claim scored `0`. |
| `rubric_version` | Rubric version used for scoring. | Version mismatch with approved snapshot -> inadmissible. |
| `snapshot_id` | Iteration snapshot identifier/hash bundle. | Missing snapshot reference -> inadmissible. |
| `evidence_hash_sha256` | Integrity hash for source extract/artifact. | Hash mismatch -> hard-fail review. |
| `source_system` | System-of-record for evidence. | Unattributed source -> claim scored `0`. |
| `provenance_chain` | Extract method and transformation lineage from source to score input. | Missing lineage -> claim scored `0`. |
| `cutoff_status` | `in_cutoff_window` or approved `reopen_id`. | Post-cutoff evidence without reopen ID -> excluded. |

Admissibility enforcement:
1. Any non-zero row missing a required field is forced to `0` before aggregation.
2. If missing-field rate in independent sample exceeds `5%`, cap R14 at `50` and force targeted rescore.
3. Post-cutoff evidence is excluded from the current iteration unless approved reopen metadata exists.

## 2B) Deterministic contradiction precedence protocol (cost vs risk/service)

| Precedence rank | Contradiction class | Owner | SLA | Deterministic resolution | Deterministic score/publication effect |
| --- | --- | --- | --- | --- | --- |
| 1 | Legal/privacy/security blocker vs cost-optimization recommendation | R8/R7 with R14 | Immediate | Mandatory control blocker wins. | Publication blocked; unresolved state maps to fail gates. |
| 2 | Reliability/service SLO blocker vs savings action | R6 with R14 | <= 4 business hours | Service/reliability blocker wins unless approved exception exists in snapshot. | Cost-optimization rows capped at `50` until resolved. |
| 3 | Contractual entitlement/notice duty vs budget shortfall pressure | R8/R14 | <= 1 business day | Contractual obligation wins over spend deferral pressure. | Notice/entitlement violation triggers hard-fail path. |
| 4 | Invoice mismatch evidence vs end-period payment acceleration | AP controller + R14 | <= 1 business day | Payment-control evidence wins; mismatched payment remains blocked absent approved emergency waiver. | Payment-control rows forced to fail path if bypassed. |
| 5 | Admissibility defect vs requested non-zero anchor | R14 scorer + R15 witness | <= 1 business day | Evidence rule wins; inadmissible claim removed. | Affected row forced to `0`; targeted rescore required. |
| 6 | Severity-1 contradiction unresolved past SLA | Assigned contradiction owner | SLA expiry | Unresolved contradiction cannot be waived silently. | `R14.19` capped at `50`; publication blocked until closure evidence is approved. |

## 3) Scoring anchors table (0/25/50/75/90/100)
| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R14.1 Spend data completeness and tagging fidelity | Majority of spend cannot be attributed to owner/use case; reconciliations absent. | Basic tags exist but > 30% spend is unmapped; reconciliation is ad hoc. | Attribution model defined; unmapped spend <= 15%; monthly reconciliation exists with recurring exceptions. | Mandatory fields >= 95%; unmapped spend <= 5%; ledger/bill variance <= 1% with documented remediation. | Mandatory fields >= 98%; unmapped <= 2%; automated exception routing with owner SLA. | Mandatory fields >= 99.5% for two quarters; independent audit reproduces attribution end-to-end. |
| R14.2 Unit economics model integrity | No unit-cost model or formulas are opaque/non-reproducible. | Model exists but denominators are unstable and assumption changes are undocumented. | Core formulas documented for major services; variance interpretation inconsistent. | Formula dictionary complete for material services; versioned assumptions; variance RCA on breaches. | Denominator lineage and assumptions independently traceable; decisions tied to unit-cost thresholds. | Unit-cost model is decision-grade across all critical services with quarterly independent validation pass. |
| R14.3 Forecast accuracy and variance response discipline | Forecasting absent; spend surprises are discovered after close. | Forecast exists but error is frequently > 30%; no timely action on misses. | Regular forecast produced; error around 15-25%; actions start late or inconsistently. | Rolling forecasts within agreed tolerance for major categories; variance actions initiated on schedule. | Forecast accuracy high (MAPE <= 10%) with clear driver decomposition and rapid reforecasting. | Forecast error <= 5% on top categories for two quarters and corrective actions prevent repeat misses. |
| R14.4 Budget guardrail and commitment governance | Budgets are not enforced; material overruns occur without approval trail. | Thresholds defined but alerts or exceptions are unreliable. | Alerting works for most categories; exceptions documented inconsistently. | Approved guardrails enforced; unauthorized overruns are rare and corrected quickly. | No unauthorized overrun events; exception approvals are complete and time-bounded. | Guardrail system prevents overrun pre-commitment and withstands surprise audit with zero material findings. |
| R14.5 Purchase intake and approval discipline | Purchases routinely bypass procurement workflow. | Workflow exists but > 20% spend is off-process or missing approvals. | Most requests route correctly; policy checks are partial; approval latency unpredictable. | >= 95% requests follow workflow with required approvers and risk checks. | >= 99% compliant intake with tier-based SLA and escalation for bottlenecks. | Full workflow integrity for two quarters; zero retroactive approvals accepted in sample audit. |
| R14.6 Vendor due diligence and onboarding risk controls | Critical vendors onboard without security/privacy/legal risk review. | Checklist exists but high-risk findings are waived informally. | Due diligence completed for many vendors; evidence quality uneven. | Critical vendor diligence complete before go-live; unresolved high risk blocks launch. | Reassessments happen on cadence with closed-loop remediation and signed risk acceptance only when justified. | No production use for critical vendors without complete validated package and independent reviewer concurrence. |
| R14.7 Contract obligation traceability and calendar discipline | Contract obligations are unknown or unmanaged. | Some obligations tracked, but owners/dates are missing and deadlines are missed. | Obligation register exists; notice windows occasionally missed. | Clause-to-owner mapping mostly complete; notice obligations met on time. | Full obligation calendar with automated reminders and confirmed owner acknowledgment. | Zero missed notices for two quarters; sampled clauses fully trace to controls and evidence. |
| R14.8 Invoice validation and payment accuracy controls | Payments made without contract/PO validation; duplicate or erroneous payments are common. | Partial matching with many manual overrides and weak justification trails. | 3-way match applied to major categories; disputes and corrections are reactive. | Strong match controls with low exception rate and documented dispute handling. | Duplicate payments eliminated; mismatch exceptions resolved within SLA and root causes tracked. | Independent control test shows near-perfect match integrity and no material payment leakage. |
| R14.9 Savings claim validity and realization tracking | Savings claims are narrative only, with no baseline or verification. | Baselines are cherry-picked; offsets ignored; claimed savings are inflated. | Baseline method documented but realization tracking inconsistent. | Claimed savings tied to approved baseline and reflected in realized spend with tolerable variance. | Realization reporting net of offsets and timing effects; recurring vs one-time clearly separated. | Third-party recheck reproduces savings figures with no material adjustment over two quarters. |
| R14.10 Commitment utilization and waste remediation | Commitment instruments unmanaged; material idle commitments persist. | Utilization tracked sporadically; waste known but no accountable remediation. | Utilization monitored; remediation backlogs exist and age out. | Utilization within target bands; waste tickets owned and closed within policy window. | Proactive rebalancing minimizes idle commitments and avoids emergency purchases. | Utilization and waste controls sustain optimized levels through demand swings with evidence-backed governance. |
| R14.11 License entitlement and commercial compliance | License position unknown; audit exposure is high. | Inventory exists but assignment/usage reconciliation is unreliable. | Compliance tracked for major products; shelfware and audit readiness moderate. | Monthly entitlement reconciliation complete; under-licensing and shelfware controlled. | True-up surprises avoided; reclaim and reallocation workflows reduce waste continuously. | Audit-ready license position maintained continuously with zero material findings and low shelfware. |
| R14.12 Cost anomaly detection and response quality | Anomalies discovered only after invoices post; no clear ownership. | Alerts exist but noisy/late; response often misses material events. | Detection and triage functioning for high spend areas; closure quality inconsistent. | Material anomalies detected quickly, assigned rapidly, and closed with RCA. | Recurrence reduced by preventive controls; response SLAs consistently met. | End-to-end anomaly program catches high-impact events early with repeatable forensic evidence. |
| R14.13 Pricing model optimization and negotiation quality | Pricing accepted without benchmark or leverage analysis. | Negotiation is tactical only; concessions poorly documented. | Benchmarking and negotiations occur, but scenario rigor is limited. | Negotiation packs include usage truths, alternatives, and quantified concession impact. | Effective rates improve cycle-over-cycle on comparable demand; risk terms also improved. | Negotiations consistently deliver top-quartile commercial outcomes validated against external benchmarks. |
| R14.14 Renewal readiness and leverage posture | Renewals are reactive; auto-renew events create locked-in unfavorable terms. | Calendar exists but key renewals start too late for leverage. | Some renewals planned early; BATNA quality varies. | Critical renewals launched >= 120 days out with complete decision packets. | Decision options are financially and operationally stress-tested before commitment. | Zero late renewals for two quarters; leverage strategy repeatedly captures favorable terms and flexibility. |
| R14.15 Vendor performance and SLA credit enforcement | SLA performance not measured; credits are never claimed. | Basic SLA reporting with low trust and infrequent enforcement. | Performance tracked; credits claimed inconsistently; recurring breaches under-managed. | Reliable SLA packs with regular breach challenge and credit recovery. | Credit capture near complete and linked to corrective-action governance. | Full enforcement discipline: eligible credits consistently recovered and breach recurrence materially reduced. |
| R14.16 Concentration and lock-in risk management | Critical capability relies on single vendor with no mitigation visibility. | Risks recognized but unquantified; mitigation plans are aspirational. | Concentration metrics exist; mitigation coverage partial. | Top concentration and lock-in risks quantified with owned mitigation plans. | Contingency patterns (dual source/portable architecture/escrow) validated for critical domains. | Concentration and lock-in risk kept within approved appetite with periodic adversarial testing. |
| R14.17 Exit and transition readiness | No feasible exit path for critical vendor dependencies. | Exit plan is template-only and untested. | Partial plans exist; portability assumptions unproven. | Critical vendors have documented exit runbooks with owners and timeline. | Tabletop and data portability tests executed with action closure on gaps. | Exit execution is demonstrably viable under timed simulation for all critical vendors. |
| R14.18 Chargeback/showback trust and stakeholder alignment | Allocation outputs are opaque and broadly disputed. | Reports exist but methodology unclear; disputes linger unresolved. | Method published; dispute management inconsistent and slow. | Stakeholders can trace charges; disputes are resolved within policy. | Independent recomputation and finance review show high accuracy and fairness. | Chargeback/showback is trusted as decision-grade by engineering/product/finance with persistent low dispute rate. |
| R14.19 Cost-vs-risk contradiction precedence determinism | Contradictions are ad hoc, ownerless, or silently waived. | Contradictions logged inconsistently; precedence/SLA effects are ambiguous. | Protocol exists but Severity-1 contradiction handling varies by reviewer. | Precedence, owner, SLA, and score effects are explicit and enforced. | Independent simulation reproduces contradiction outcomes across reviewers. | Two iterations with zero unresolved Severity-1 cost-vs-risk contradiction at cutoff. |
| R14.20 Independent replay and recompute determinism | Non-author replay fails or cannot run from provided evidence. | Replay possible only with author intervention; variance exceeds policy. | Partial replay succeeds but required sample coverage/tolerance are inconsistent. | Required replay sample and tolerance thresholds are met each iteration. | Replay includes all gate-sensitive rows and demonstrates full gate-state parity. | Two iterations with stable replay parity and no unexplained variance breaches. |
| R14.21 Iteration snapshot and delta re-evaluation governance | Scoring runs on uncontrolled versions; deltas are undocumented. | Snapshot exists but scoring-affecting deltas bypass approval. | Snapshot mostly enforced; impacted-row retesting is inconsistent. | Approved snapshot is enforced; every scoring-affecting delta has impacted-row rescore evidence. | Independent review confirms no unauthorized delta in scored scope. | Two iterations with complete snapshot integrity and targeted retest coverage. |

## 3A) High-anchor proof thresholds (mandatory)

| Proposed anchor | Required proof set | Automatic downgrade when missing |
| --- | --- | --- |
| `>75` | Independent reviewer corroboration in the same iteration. | Downgrade to `75`. |
| `>90` | Independent corroboration plus same-iteration adversarial challenge evidence and non-author replay pass. | Downgrade to `75` and publication hold until resolved or rescored. |
| `100` | `>90` requirements plus sustained control evidence across two consecutive iterations. | Downgrade to `90`. |

## 4) Anti-gaming checks specific to this role
| Gaming pattern to detect | Adversarial check | Control response | Scoring consequence |
| --- | --- | --- | --- |
| Reclassifying spend to lower-visibility cost centers | Compare invoice vendor strings, GL account movement, and historical routing for sudden classification shifts. | Require controller-approved mapping change ticket with rationale and effective date. | Unsupported reclassification invalidates affected savings and caps R14.1/R14.9 at 50. |
| Inflated savings via baseline manipulation | Recompute savings using prior locked baseline and net offsets (migrations, rebates, deferred charges). | Baseline lock before execution; any change requires governance approval. | If baseline tampering confirmed, set R14.9 = 0 for cycle. |
| Deferring invoice recognition to mask overrun | Match service period to accrual and payment timing; flag end-of-period hold spikes. | Enforce accrual policy with AP-controller review on hold/release events. | Material misstatement forces R14.3/R14.4 score cap at 25. |
| Overstating commitment utilization by excluding idle inventory | Reconcile commitment dashboards against raw reservation/license assignment states. | Include idle assets in utilization denominator by policy. | Exclusion behavior detected in sample caps R14.10 at 50. |
| Closing anomalies without root-cause correction | Sample anomaly closures for true fix evidence and recurrence within 30/60 days. | Mandatory closure checklist: cause, control, owner, verification window. | False closures > 10% sampled cap R14.12 at 50. |
| Auto-renew accepted without market test | Audit renewals for benchmark evidence, BATNA documentation, and approval trail. | Renewal gate requires benchmark packet before signature authority. | Missing packet on critical renewal caps R14.13/R14.14 at 25. |
| Suppressing SLA breach evidence to avoid vendor dispute | Recompute SLA attainment from raw telemetry and compare to vendor scorecards. | Joint signed monthly SLA reconciliation with immutable evidence links. | Proven suppression sets R14.15 = 0 for cycle. |
| License compliance cosmetically improved by disabling usage telemetry | Compare entitlement counts with identity access and endpoint telemetry continuity. | Telemetry outage > policy threshold triggers compliance hold and review. | Telemetry manipulation caps R14.11 at 25 until independent recompute passes. |
| Chargeback fairness inflated by excluding disputed invoices from denominator | Rebuild dispute rate including reopened and partially credited items. | Dispute KPI definition fixed in governance charter; change control required. | Metric-definition manipulation invalidates R14.18 score above 50. |
| Vendor concentration risk hidden through reseller fragmentation | Consolidate beneficial vendor ownership and platform dependency across reseller entities. | Maintain parent-entity mapping in supplier master and risk model. | Hidden concentration > threshold caps R14.16 at 50. |

## 4A) Independent replay and recompute protocol

| Control | Requirement | Failure effect |
| --- | --- | --- |
| Replay sample coverage | Non-author replay on `max(15 rows, 15% of scored R14 rows)` each iteration. | Trigger replay failure tripwire; publication hold until rerun passes. |
| Gate-sensitive inclusion | Every row that can trigger/clear a gate must be in replay sample. | Publication hold and targeted replay required. |
| Replay tolerance | Anchor variance `<=1`, aggregate variance `<=5 points`, gate-state parity `100%`. | `R14.20` capped at `25`; affected rows rescored. |
| Recompute integrity | Unit-cost, forecast, savings, and SLA-credit claims recomputed from raw sources. | Affected metric rows forced to `0` pending restatement. |
| Author separation | Replay reviewer cannot be the primary scorer for the same sampled row. | High-anchor evidence invalidated for affected rows. |

## 5) Tripwires and hard-fail conditions
| Tripwire condition | Hard-fail effect |
| --- | --- |
| Confirmed falsification of savings, forecast, or spend attribution evidence. | Overall R14 cycle FAIL; affected sub-dimensions forced to 0 pending forensic review. |
| Critical vendor onboarded to production with unresolved high-risk security/privacy/legal finding and no approved exception. | Overall R14 cycle FAIL until control owner certifies remediation. |
| Material contract notice deadline missed causing automatic renewal, penalty, or lost termination right. | Overall R14 cycle FAIL for the cycle of occurrence. |
| Payment released on known mismatched invoice above policy threshold without approved emergency waiver. | Overall R14 cycle FAIL and R14.8 forced to 0 for cycle. |
| Budget overrun beyond approved tolerance with no pre-approved exception chain. | Overall R14 score capped at 50 for cycle. |
| Eligible vendor service credits repeatedly unclaimed for two consecutive cycles despite measured breaches. | R14.15 capped at 25 and mandatory corrective action before next cycle close. |
| No tested exit plan for any critical single-source vendor dependency. | R14.17 forced to 25 maximum until simulation evidence exists. |
| Cost anomaly above materiality threshold remains unowned for > 24 hours. | Overall R14 cycle FAIL for operational control breakdown. |
| License audit or regulator finds willful non-compliance not self-reported internally. | Overall R14 cycle FAIL with executive escalation. |
| Chargeback statements issued with known recomputation errors affecting cross-team billing. | R14.18 forced to 0 for cycle and rebill required. |

### Additional deterministic tripwires for contradiction, replay, and snapshot control

| ID | Tripwire condition | Immediate effect |
| --- | --- | --- |
| R14-HF11 | Severity-1 cost-vs-risk contradiction unresolved past SLA. | `R14.19` capped at `50`; publication blocked until approved closure evidence is attached. |
| R14-HF12 | Independent replay coverage or tolerance requirements not met. | `R14.20` capped at `25`; no publication until replay rerun passes tolerance. |
| R14-HF13 | Any proposed `>90` anchor lacks same-iteration adversarial challenge evidence. | Affected rows downgraded to `75`; high-anchor publication blocked until resolved or rescored. |
| R14-HF14 | Scoring-affecting rubric/evidence delta applied after approved iteration snapshot without approved delta dossier. | `R14.21` set to `0`; iteration scoring packet marked invalid and rerun on approved snapshot. |
| R14-HF15 | Sampled non-zero rows with missing admissibility fields exceed `5%`. | Affected rows forced to `0`; role capped at `50` pending targeted rescore. |

### Tripwire recovery proof requirements

| ID set | Minimum recovery proof | Verification authority | Reopen rule |
| --- | --- | --- | --- |
| R14-HF11 | Contradiction closure record with owner, SLA compliance, disposition, and score-impact trace. | R14 + contradiction owner + R15 witness | Recurrence of unresolved Severity-1 contradiction reopens publication hold. |
| R14-HF12 | Replay rerun artifacts meeting coverage, tolerance, and gate-parity requirements. | R15 witness + R14 owner | New variance breach in same iteration reopens impacted rows. |
| R14-HF13 | Same-iteration adversarial challenge evidence or approved rescore package at allowed anchor. | R14 owner + independent reviewer | Missing proof at later publication checks reopens hold. |
| R14-HF14 | Approved delta dossier, impacted-row map, targeted rescore, and parity evidence on approved snapshot. | R11 + R15 + R14 | Any additional unauthorized delta forces another invalidation review. |
| R14-HF15 | Corrected admissibility ledger, rescore output, and independent sample under defect threshold. | R14 + R15 | Subsequent threshold breach in same iteration reopens cap. |

## 6) Cross-role dependency and handoff criteria
| Dependency/handoff | Entry criteria from partner role | R14 handoff package requirements | Acceptance SLA and exit criteria |
| --- | --- | --- | --- |
| R1 Product Manager -> R14 (feature/business-case costing) | Proposed initiative has scope, usage assumptions, and target KPIs. | Cost model by scenario, vendor options, unit economics sensitivity, budget impact summary. | Initial R14 assessment <= 5 business days; exit when cost envelope and guardrails are signed off. |
| R3 Engineering Manager / R6 SRE -> R14 (optimization change) | Reliability-safe optimization candidate identified with expected usage impact. | Before/after cost baseline, risk statement, rollback plan, ownership and validation window. | Decision <= 3 business days for non-critical changes; exit when savings and reliability checks pass. |
| R7 Security / R8 Privacy -> R14 (vendor onboarding gate) | Vendor requires production data/system access. | Completed diligence packet, unresolved findings list, risk acceptance or remediation deadlines, contract control clauses. | Critical-vendor decision <= 10 business days; exit when all blocking findings are cleared or formally accepted. |
| R8 Legal -> R14 (contract negotiation and signature) | Redlines stabilize and commercial deltas identified. | Negotiation ledger, fallback positions, obligation matrix, financial risk summary, approval chain. | Final commercial sign-off <= 2 business days after legal readiness; exit on approved signature package. |
| R12 Release Manager -> R14 (new third-party dependency in release) | Release candidate introduces new billable dependency or pricing dimension. | Cost impact forecast, commitment/entitlement plan, budget owner approval, anomaly monitors enabled. | Go/no-go response before release CAB cutoff; exit when monitors and controls verified live. |
| R13 Operations/Support -> R14 (SLA breach and service credit claim) | Incident or monthly SLA report indicates credit eligibility. | Breach evidence pack, impacted service period, contract clause reference, claim draft and timeline. | Claim decision <= 5 business days; exit when credit filed/recovered or justified rejection approved. |
| R0 Executive Sponsor -> R14 (major renewal/termination decision) | Strategic vendor decision required (renew, re-compete, or exit). | Multi-option decision memo: TCO, risk, lock-in exposure, transition feasibility, recommended path. | Executive decision at scheduled governance meeting; exit when decision and conditions are documented. |
| R14 -> R2 Architect (lock-in mitigation plan) | Concentration/lock-in risk crosses approved threshold. | Dependency map, portability gaps, mitigation investment estimate, timeline and risk reduction target. | R2 acceptance <= 10 business days; exit when architecture mitigation work is planned with owners. |

## 7) Cycle-level improvement checklist
Use this checklist every cycle (weekly operational review and monthly governance review). A checked item requires linked evidence.

| Checklist item | Evidence required |
| --- | --- |
| [ ] Reconciled cloud/SaaS/vendor spend to AP ledger and resolved all material exceptions. | Signed reconciliation workbook with exception ticket links. |
| [ ] Locked approved iteration snapshot before scoring. | Signed snapshot manifest with rubric hash, scorebook version, denominator snapshot, and gate-order checksum. |
| [ ] Recomputed top unit economics metrics and documented assumption changes. | Updated metric dictionary and formula changelog with approver names. |
| [ ] Reviewed forecast error drivers and opened corrective actions for tolerance breaches. | Forecast variance report and action tracker export. |
| [ ] Audited purchase workflow bypasses and remediated root causes. | Off-workflow audit sample, corrective actions, and owner acknowledgements. |
| [ ] Verified due-diligence completeness for new/changed critical vendors. | Vendor risk checklist pack with R7/R8 disposition. |
| [ ] Refreshed obligation calendar and confirmed 60/30/15 day notice actions. | Obligation tracker snapshot with owner confirmations. |
| [ ] Completed invoice control sample and validated duplicate-payment prevention controls. | AP control test result set and dispute-resolution log. |
| [ ] Revalidated claimed savings against realized spend (net of offsets). | Savings recomputation workbook and finance sign-off. |
| [ ] Reviewed commitment utilization and closed aged waste-remediation tickets. | Utilization dashboard and remediation ticket aging report. |
| [ ] Performed license entitlement reconciliation with identity data. | SAM reconciliation output and exception closure evidence. |
| [ ] Ran anomaly postmortem review for all material alerts closed this cycle. | Alert timeline, RCA records, and preventive control updates. |
| [ ] Replayed contradiction precedence scenarios for active Severity-1 commercial conflicts. | Contradiction simulation log and closure evidence. |
| [ ] Advanced renewal workbacks for critical vendors and refreshed BATNA benchmarks. | Renewal plan tracker and benchmark evidence pack. |
| [ ] Reconciled SLA breaches with service-credit submissions and recovery status. | SLA evidence bundle and claim register. |
| [ ] Recomputed chargeback sample and resolved billing disputes within SLA. | Independent recomputation sheet, dispute log, stakeholder sign-off. |
| [ ] Executed independent replay/recompute sample for R14 scoring. | Replay transcript, recompute workbook, and variance report. |
| [ ] Audited all proposed `>90` anchors for independent and challenge evidence. | High-anchor proof audit pack and downgrade/rescore decisions. |
| [ ] Reviewed concentration and lock-in heatmap; updated mitigation owners and dates. | Risk dashboard export and architecture/procurement action log. |
| [ ] Ran one exit-readiness simulation for a critical vendor and captured gaps. | Tabletop/simulation report with closed-loop remediation tasks. |
| [ ] Re-evaluated every approved scoring-affecting delta before publication. | Delta dossier, impacted-row map, and targeted rescore/replay output. |

---

## R15 Internal Audit / Assurance

- source_file: `swarm_outputs/role_expansions/R15_internal_audit_assurance.md`
- words: 6371
- lines: 223

# R15 Internal Audit / Assurance Rubric Expansion

## 1) Title
R15 Internal Audit / Assurance Rubric Expansion

## 2) Role mission and decision rights
Internal Audit / Assurance exists to provide independent, evidence-backed judgment on whether controls are designed effectively, operating as intended, and remediated durably when they fail. The role is accountable for surfacing control truth early, resisting managerial pressure, and issuing defensible assurance conclusions that can withstand regulator, board, and forensic scrutiny.

| Decision area | R15 decision rights | Escalation boundary |
| --- | --- | --- |
| Audit universe and annual plan | Owns risk-based prioritization, scope depth, and cycle cadence for assurance work. | Escalate to audit committee when management requests removal/deferment of high-risk scope. |
| Methodology and test standards | Sets mandatory test design, sampling, evidence, and documentation standards. | Escalate to R0 and audit committee for any request to weaken required methodology controls. |
| Sample design and population cut | Approves population definition, sample method, and exclusions before fieldwork. | Escalate to R8 if legal limits constrain access to needed records. |
| Finding acceptance and severity rating | Has final authority on finding validity and severity after calibration and challenge process. | Escalate to audit committee on unresolved severity disputes for high/critical findings. |
| Report issuance and wording control | Owns final assurance language, confidence statements, and limitation disclosures. | Escalate to audit committee if management attempts post-signoff edits to factual conclusions. |
| Remediation closure acceptance | Can reject closure until independent retest evidence meets closure standard. | Escalate to R0 for chronic closure pressure or repeated evidence insufficiency. |
| Immediate risk notification | Can issue immediate escalation notice for critical control breakdowns without management pre-clearance. | Escalate to R12/R7/R8 immediately when release, security, or legal exposure is active. |
| Independence and conflict controls | Can recuse auditors, reassign work, and invalidate compromised workpapers. | Escalate to audit committee if staffing model prevents independence requirements from being met. |

## 3) Sub-dimensions table
| Sub-dimension | Definition | Leading indicators / tests | Required evidence (who/what/where/time/version/hash) |
| --- | --- | --- | --- |
| R15.1 Audit universe completeness and risk-based plan quality | Assurance scope covers all material processes, systems, vendors, and regulatory obligations, ranked by current risk. | High-risk domain annual coverage >= 95%; plan completion >= 90%; out-of-cycle risk events inserted into plan <= 10 business days. | Who: Head of Internal Audit, ERM owner. What: audit universe inventory, risk scoring model, approved annual plan, mid-cycle replan log. Where: GRC platform, audit planning workspace, committee minutes. |
| R15.2 Charter authority and organizational independence | Audit mandate, unrestricted access rights, and functional reporting lines preserve assessor independence. | Charter board approval age <= 12 months; access-denial incidents unresolved > 5 business days = 0; direct committee sessions held each cycle. | Who: Chief Audit Executive, audit committee chair. What: signed charter, reporting line attestation, access exception log. Where: governance repository, HR org records, committee agenda pack. |
| R15.3 Conflict-of-interest screening and assessor rotation | Assignments are screened for financial, managerial, or prior operational conflicts and rotated where required. | COI declarations completed before fieldwork = 100%; unmitigated conflicts = 0; high-risk area lead rotation at least every 2 cycles. | Who: Audit operations manager, assigned auditors. What: COI forms, recusal decisions, assignment roster history. Where: audit workflow tool, HR role history export, evidence vault. |
| R15.4 Control objective-to-test traceability integrity | Every in-scope control objective maps to explicit tests, and every test maps back to an approved control objective. | Trace matrix completeness for material controls = 100%; orphan tests = 0; unmapped objectives older than 5 business days = 0. | Who: Audit lead, control owner reviewer. What: control catalog, test trace matrix, mapping exception tickets. Where: control library, workpaper repository, issue tracker. |
| R15.5 Test procedure design rigor and falsifiability | Test scripts define data sources, steps, pass/fail thresholds, and failure interpretation before execution. | Pre-fieldwork peer review completion = 100%; high-risk controls with both positive and negative test paths >= 90%; ambiguous pass/fail criteria findings = 0. | Who: Test designer, methodology reviewer. What: signed test scripts, peer review checklists, method deviation log. Where: audit methodology repo, workpaper system, QA board. |
| R15.6 Population completeness and sample-method validity | Sampling uses complete populations, justified methods, reproducible selection logic, and controlled exclusions. | Population-to-source reconciliation variance <= 1%; undocumented sample exclusions = 0; sample reselection reproducibility pass = 100% for audited sample. | Who: Audit analyst, data owner. What: population extracts, reconciliation workbook, sampling seed/code, exclusion approvals. Where: source systems, analytics notebook repo, audit evidence folder. |
| R15.7 Evidence admissibility and chain-of-custody integrity | Evidence is authoritative, timestamped, immutable, and attributable from source extraction through report issuance. | Evidence with source owner and extraction timestamp = 100%; broken hash/immutability checks = 0; screenshot-only critical evidence items = 0. | Who: Auditor, evidence custodian. What: evidence manifest, source export metadata, hash/signature verification logs. Where: evidence vault, source system exports, integrity audit log store. |
| R15.8 Fieldwork execution discipline and supervisory review quality | Fieldwork follows approved scope and procedures, with documented deviations and timely supervisory sign-off. | Required workpaper sections complete >= 95%; supervisory review before preliminary conclusion = 100%; unauthorized procedure deviations = 0. | Who: Engagement lead, supervising manager. What: workpaper checklist, review comments, deviation approvals, rework records. Where: audit management system, review workflow logs. |
| R15.9 Finding articulation quality and replayability | Findings are written with condition, criteria, cause, effect, and quantified risk so an independent reviewer can reproduce the result. | CCRE completeness for high/critical findings = 100%; reproduction success >= 95% on sampled findings; unsupported assertion count = 0. | Who: Auditor, independent reviewer. What: finding narratives, reproduction notes, evidence links, quantification worksheets. Where: finding register, workpaper system, assurance review notebook. |
| R15.10 Severity calibration and materiality consistency | Severity ratings are consistent across audits and aligned to approved impact/likelihood/materiality rules. | Calibration session cadence met monthly; sampled rating drift > 1 band <= 10%; severity override without panel record = 0. | Who: Calibration panel, Chief Audit Executive delegate. What: severity matrix, panel minutes, rating challenge log, override approvals. Where: governance wiki, calibration tracker, issue system. |
| R15.11 Root-cause validation and control-failure attribution | Root causes are evidence-backed, system-level, and distinguish design failure from operating failure. | Findings with causal evidence chain >= 95%; "human error only" root-cause usage for high findings <= 5%; alternative-cause review performed for critical findings = 100%. | Who: Auditor, process/control owner, challenge reviewer. What: root-cause analysis artifacts, failure-mode mapping, challenge outcomes. Where: RCA repository, finding record, process map library. |
| R15.12 Remediation action design and accountable ownership quality | Corrective actions are specific, feasible, time-bound, and assigned to one accountable owner with success criteria. | Findings with SMART action plans = 100%; high/critical actions with interim compensating controls where needed = 100%; owner acceptance documented = 100%. | Who: Management action owner, audit follow-up lead. What: remediation plan, dependency map, milestone schedule, owner signoff. Where: remediation tracker, project board, governance minutes. |
| R15.13 Remediation verification and closure-testing independence | Findings close only after independent retest demonstrates sustained control effectiveness. | Closures without independent retest = 0; reopened findings within 90 days <= 5%; closure package completeness for sampled items = 100%. | Who: Follow-up auditor independent of original tester. What: retest scripts, closure evidence pack, reopen log, closure decision notes. Where: follow-up workpapers, issue register, evidence vault. |
| R15.14 Recurrence analytics and repeat-finding escalation discipline | Repeat control failures are detected, trended, and escalated with strengthened corrective requirements. | Repeat finding identification latency <= 5 business days; repeat high findings with executive escalation = 100%; recurrence trend reviewed each cycle. | Who: Assurance analytics owner, audit leadership. What: recurrence dashboard, clustering logic, escalation notices, trend review minutes. Where: BI model, finding history store, committee deck archive. |
| R15.15 Assurance report traceability and defensibility | Final report conclusions are fully traceable to evidence and disclose scope limits, confidence bounds, and unresolved uncertainty. | Statement-to-evidence traceability coverage = 100%; unresolved contradiction count at publication = 0; report QA signoff completion = 100%. | Who: Report author, QA reviewer, CAE approver. What: final report, evidence index, contradiction resolution log, signoff record. Where: report repository, evidence manifest, governance approval system. |
| R15.16 Issue aging governance and escalation timeliness | Open findings are managed against severity-based SLAs with deterministic escalation for overdue risk. | Overdue critical findings without same-day escalation = 0; overdue high findings without weekly escalation = 0; aging trend improves quarter-over-quarter. | Who: Audit follow-up manager, accountable executive. What: aging register, escalation emails/tickets, SLA breach log. Where: issue tracker, executive dashboard, committee reporting pack. |
| R15.17 Audit quality assurance and improvement program (QAIP) effectiveness | Internal quality reviews and periodic external assessments verify methodology conformance and drive measurable improvement. | QA review coverage of completed audits = 100%; critical QA findings open > 30 days = 0; external quality assessment currency <= 5 years. | Who: QAIP lead, external assessor. What: QA checklist results, methodology deviation reports, external assessment report, corrective-action tracker. Where: QAIP repository, audit tool QA module, governance archive. |
| R15.18 Management override resistance and retaliation-safe escalation | The assurance function detects and resists inappropriate influence and protects staff/reporters from retaliation for adverse findings. | Override attempts logged with disposition = 100%; anonymous escalation channel test run quarterly = 100%; substantiated retaliation cases unresolved > 10 business days = 0. | Who: CAE, ethics/compliance partner. What: override register, whistleblower/escalation logs, retaliation investigation outcomes. Where: governance case system, ethics hotline records, committee minutes. |
| R15.19 Gate truth-table replay determinism (G1-G6/RG1-RG4) | Global and role gates are replayed from raw gate states using one precedence order before publication. | Truth-table replay executed each iteration for all `G1..G6` and `RG1..RG4`; gate-state parity between computed and published outcomes = 100%; unresolved mismatch count at cutoff = 0. | Who: assurance lead + independent replay reviewer. What: gate-state extract, truth-table replay worksheet, parity report, mismatch disposition. Where: scoring engine output, gate register, publication packet. |
| R15.20 Iteration snapshot and delta re-evaluation governance | Assurance scoring runs only on approved iteration snapshots; scoring-affecting deltas require targeted retest and replay. | Snapshot manifest approved before scoring = 100%; unauthorized scoring-affecting deltas = 0; approved deltas with impacted-row map + targeted rescore + gate replay = 100%. | Who: R15 owner + R11/R12 approvers. What: snapshot manifest, approved delta dossier, impacted-row map, targeted retest/replay evidence. Where: version control history, approval records, scoring archive. |

## 3A) Non-zero evidence admissibility ledger (mandatory)

Every non-zero R15 claim must include all fields below in the iteration evidence ledger.

| Field | Requirement | Rejection rule |
| --- | --- | --- |
| `claim_id` | Unique row and claim identifier. | Missing ID -> claim scored `0`. |
| `who` | Named actor identity and role at event time. | Missing/alias-only identity -> claim scored `0`. |
| `what` | Specific assurance control/test/assertion. | Narrative-only claim -> claim scored `0`. |
| `where` | Immutable locator (workpaper ID, finding ID, query reference, artifact URI). | Non-resolvable locator -> claim scored `0`. |
| `when_utc` | UTC capture timestamp. | Missing timestamp -> claim scored `0`. |
| `rubric_version` | Rubric version used for scoring. | Version mismatch with approved snapshot -> inadmissible. |
| `snapshot_id` | Iteration snapshot identifier/hash bundle. | Missing snapshot reference -> inadmissible. |
| `evidence_hash_sha256` | Integrity hash for source extract/artifact. | Hash mismatch -> hard-fail review. |
| `source_system` | System-of-record for evidence. | Unattributed source -> claim scored `0`. |
| `cutoff_status` | `in_cutoff_window` or approved `reopen_id`. | Post-cutoff evidence without reopen ID -> excluded. |

Admissibility enforcement:
1. Any non-zero row missing any required field is forced to `0` before aggregation.
2. If missing-field rate in independent sample exceeds `5%`, cap R15 at `50` and force targeted rescore.
3. Post-cutoff evidence is excluded from the current iteration unless approved reopen metadata exists.

## 3B) Gate truth-table replay protocol (deterministic precedence)

Gate precedence order for replay: `RG1 -> RG2 -> RG3 -> RG4 -> G1 -> G2 -> G3 -> G4 -> G5 -> G6 -> arithmetic scoring`.

| Replay case | Required input state | Expected deterministic output | Publication rule |
| --- | --- | --- | --- |
| Evidence integrity breach | `G1=true` | Overall invalid/zero path; no arithmetic override allowed. | Publication blocked. |
| Critical contradiction unresolved | `G2=true` or `RG3=true` | Overall fail path regardless of mean score. | Publication blocked until closure evidence approved. |
| Mandatory legal/privacy/security blocker | `G3=true` | Overall fail path. | Publication blocked. |
| Non-operable critical path | `G4=true` | Overall fail path. | Publication blocked. |
| Replay failure on material claims | `G5=true` | Overall fail path and forced full replay/rescore. | Publication blocked. |
| Missing authority-chain approvals | `G6=true` | Overall fail path. | Publication blocked. |
| Critical role floor breach | `RG1=true` | Overall fail path. | Publication blocked. |
| High-anchor independence breach | `RG2=true` | Role cap at `75` before aggregate. | Publication blocked until cap/rescore applied. |
| Role evidence provenance failure | `RG4=true` | Affected role set to `0` before aggregate. | Publication blocked until corrected packet is verified. |

## 4) Scoring anchors table (0/25/50/75/90/100)
No sub-dimension may score above `50` without complete who/what/where evidence, above `75` without independent reviewer confirmation, or above `90` without current-cycle adversarial re-test evidence.

| Sub-dimension | 0 | 25 | 50 | 75 | 90 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| R15.1 Audit universe completeness and risk-based plan quality | No maintained audit universe; major risk areas unscoped. | Universe exists but materially incomplete or stale; planning is calendar-driven only. | Most core domains listed, but risk ranking and reprioritization are inconsistent. | Material domains covered with risk-based annual plan and documented update triggers. | High-risk coverage >= 95% with in-cycle reprioritization and committee visibility. | Two consecutive cycles with independent validation showing no material scope omissions. |
| R15.2 Charter authority and organizational independence | No effective charter or management controls audit scope/reporting. | Charter is outdated or weak; access denials materially constrain work. | Charter exists and mostly followed, but reporting lines dilute independence. | Current charter, direct committee access, and unrestricted evidence rights are operational. | Independence exceptions are rare, logged, and resolved quickly with committee support. | No unresolved independence impairments across two cycles; challenge rights proven in live escalations. |
| R15.3 Conflict-of-interest screening and assessor rotation | No COI screening; conflicted auditors evaluate owned areas. | COI forms exist but are optional or completed after fieldwork starts. | COI checks are performed, but recusals/rotation are inconsistently enforced. | Mandatory pre-assignment COI screening and recusal/rotation controls for high-risk areas. | Independent checks confirm COI controls are effective and timely for all sampled audits. | Two cycles with zero unmitigated conflicts and full rotation policy adherence. |
| R15.4 Control objective-to-test traceability integrity | Objectives and tests are disconnected; coverage cannot be demonstrated. | Partial mapping with many orphan tests or unmapped objectives. | Mapping covers core controls but has unresolved gaps and version drift. | Complete bidirectional traceability for material controls with managed exceptions. | Traceability is version-controlled and independently re-performed without material mismatch. | Two cycles with zero orphan tests/unmapped objectives in sampled engagements. |
| R15.5 Test procedure design rigor and falsifiability | Tests are ad hoc and subjective; pass/fail cannot be defended. | Scripts exist but lack thresholds, data sources, or negative paths. | Core scripts are defined; ambiguity remains in edge/high-risk scenarios. | Scripts are explicit, falsifiable, peer-reviewed, and include required negative testing. | Re-performance by independent reviewer reproduces decisions with minimal interpretation variance. | Two cycles of defect-free method reviews and repeatable outcomes across sampled tests. |
| R15.6 Population completeness and sample-method validity | Sample frame is unknown or cherry-picked. | Population is partial/unreconciled; sample exclusions are undocumented. | Reconciliation exists for some scopes; selection bias controls are weak. | Population completeness is validated and sample method rationale is documented and reproducible. | Independent reselection reproduces sample logic and conclusions for sampled audits. | Two cycles with zero material sampling defects and clean adversarial sampling challenge results. |
| R15.7 Evidence admissibility and chain-of-custody integrity | Findings rely on missing, unverifiable, or mutable evidence. | Evidence repository exists but provenance and immutability are inconsistent. | Most evidence is attributable, but chain-of-custody gaps persist in some files. | Material findings use authoritative, timestamped, immutable evidence with clear ownership. | Integrity checks and access logs pass independent review for sampled evidence sets. | Forensic replay of sampled findings succeeds end-to-end with no provenance exceptions. |
| R15.8 Fieldwork execution discipline and supervisory review quality | Fieldwork is unsupervised and procedurally inconsistent. | Plan exists but deviation control and supervisory review are unreliable. | Workpapers are mostly complete; review timing/quality is uneven. | Fieldwork follows approved methods; supervisory signoff and deviation controls are reliable. | Quality defects are low and corrected in-cycle with documented root-cause actions. | Two cycles with no critical workpaper defects in independent QA sampling. |
| R15.9 Finding articulation quality and replayability | Findings are opinion statements without reproducible proof. | Findings include some facts but miss criteria/cause/effect or quantification. | Structured writing is used inconsistently; replayability varies by auditor. | Findings consistently include CCRE structure and reproducible evidence links. | Independent reviewer reproduces >= 95% sampled findings without material rewrite. | Two cycles with board-ready findings requiring no material factual correction. |
| R15.10 Severity calibration and materiality consistency | Severity assignment is arbitrary or politically influenced. | Matrix exists but ratings frequently deviate without documented rationale. | Matrix is used with moderate consistency; cross-team drift remains significant. | Severity ratings align to approved thresholds with documented challenge decisions. | Blind recalibration shows low drift and overrides are rare and fully justified. | Two cycles with no unjustified downgrades and consistent internal/external assurance alignment. |
| R15.11 Root-cause validation and control-failure attribution | Root cause is absent or purely blame-oriented. | Root-cause statements are superficial and weakly supported by evidence. | Root causes are identified for many findings but systemic attribution is inconsistent. | Root-cause analysis is evidence-backed, distinguishes design vs operation failure, and is actionable. | Alternative-cause challenge is routine and materially improves corrective-action quality. | Root-cause accuracy is demonstrated by sustained non-recurrence after remediation across cycles. |
| R15.12 Remediation action design and accountable ownership quality | No credible remediation plans or owners. | Plans are vague, non-time-bound, or owner accountability is unclear. | Most findings have plans; dependency and feasibility treatment is uneven. | All findings have SMART actions, named owners, and realistic due dates. | Plans include interim controls for high-risk gaps and withstand independent challenge. | Two cycles with high on-time completion and no scope-dilution closures. |
| R15.13 Remediation verification and closure-testing independence | Findings are closed without testing. | Closure depends on management attestation; retesting is rare or non-independent. | Retesting occurs but independence or evidence quality is inconsistent. | Independent retest is mandatory and closure evidence is complete and reproducible. | Reopen rate is low and closure decisions withstand sample-based assurance challenge. | Two cycles with zero improper closures in independent closure audits. |
| R15.14 Recurrence analytics and repeat-finding escalation discipline | Repeat failures are not tracked or escalated. | Recurrence is noted manually with no systematic detection or ownership. | Recurrence metrics exist but escalation and response are inconsistent. | Repeat findings are detected quickly and escalated by severity with required action. | Trend analytics drive strengthened controls and reduction actions across shared root causes. | Multi-cycle evidence shows durable decline in repeat high-risk findings with enforced escalation. |
| R15.15 Assurance report traceability and defensibility | Final report cannot be tied back to evidence or scope boundaries. | Report is partially supported but contains unresolved contradictions or omissions. | Report is mostly traceable; confidence limits and assumptions are weakly stated. | Report conclusions are fully traceable, balanced, and QA-approved before release. | Committee/regulator challenge can be answered quickly from indexed evidence links. | Independent external challenge confirms full defensibility and factual integrity of conclusions. |
| R15.16 Issue aging governance and escalation timeliness | Aging is unmanaged; overdue risk accumulates without escalation. | Aging tracked manually; escalations are late or inconsistently applied. | SLA model exists but breach handling is reactive and often delayed. | Severity-based SLAs and escalation paths are consistently executed. | No un-escalated overdue critical/high findings; aging trend is demonstrably improving. | Two cycles with proactive escalation preventing material overdue exposure. |
| R15.17 Audit quality assurance and improvement program (QAIP) effectiveness | No QAIP or methodology conformance checks. | QAIP documented but not executed, and defects remain open. | QA reviews happen on part of portfolio; closure discipline is inconsistent. | Full QA coverage with timely closure of methodology deviations and tracked improvements. | External assessment current and confirms strong conformance with low residual risk. | QAIP continuously improves audit quality with measurable defect reduction across cycles. |
| R15.18 Management override resistance and retaliation-safe escalation | Assurance is suppressed by management influence; no safe escalation path. | Override pressure occurs with incomplete logging and weak response. | Override events are logged, but challenge/retaliation handling is inconsistent. | All override attempts are logged, challenged, and escalated per policy; retaliation protocol active. | Anonymous escalation channel is tested and response SLAs are met with committee oversight. | Two cycles with transparent override governance and no substantiated unresolved retaliation cases. |
| R15.19 Gate truth-table replay determinism (G1-G6/RG1-RG4) | Gate outcomes are not replayed or are overridden by arithmetic scoring. | Partial replay exists, but precedence or parity defects remain. | Replay runs for common gates only; edge-case mismatches still occur. | Full truth-table replay runs with deterministic precedence and no unresolved mismatches. | Independent replay confirms computed and published gate outcomes match exactly. | Two iterations with 100% gate-state parity and zero bypass findings. |
| R15.20 Iteration snapshot and delta re-evaluation governance | Scoring runs on uncontrolled versions; deltas are undocumented. | Snapshot exists but scoring-affecting deltas bypass approval/retest. | Snapshot mostly enforced; impacted-row retesting is inconsistent. | Approved snapshot is enforced; all scoring-affecting deltas have impacted-row retest and gate replay evidence. | Independent review confirms no unauthorized delta in scored scope. | Two iterations with full snapshot integrity and complete targeted delta re-evaluation coverage. |

## 4A) High-anchor proof thresholds (mandatory)

| Proposed anchor | Required proof set | Automatic downgrade when missing |
| --- | --- | --- |
| `>75` | Independent reviewer confirmation in same iteration. | Downgrade to `75`. |
| `>90` | Independent reviewer confirmation plus same-iteration adversarial challenge evidence and non-author replay pass. | Downgrade to `75` and publication hold until resolved or rescored. |
| `100` | `>90` requirements plus sustained control evidence across two consecutive iterations. | Downgrade to `90`. |

## 5) Anti-gaming checks specific to this role
| Gaming pattern to detect | Adversarial check | Control response | Scoring consequence |
| --- | --- | --- | --- |
| Cherry-picked low-risk samples presented as representative | Rebuild sample from full source population using locked selection seed and compare fail rates. | Require pre-fieldwork signed population snapshot and selection log immutability. | If mismatch is material, cap R15.6 at 25 for cycle. |
| Population tampering after exception discovery | Compare population hash at sample selection vs close; inspect added/removed records. | Freeze sampled population at selection timestamp; require approved change ticket for any adjustment. | Unapproved tampering sets R15.6 = 0 for cycle. |
| Backfilled evidence uploaded after challenge request | Compare evidence file creation/source extraction times against audit cutoff timestamps. | Disallow post-cutoff evidence for current cycle conclusions unless explicitly flagged as supplemental. | Unsupported backfill invalidates affected findings and caps R15.7/R15.9 at 50. |
| Severity downgrades under management pressure | Re-rate sampled findings in blind calibration panel and compare to issued ratings. | Enforce mandatory panel record for any downgrade from initial recommendation. | Unjustified downgrades force R15.10 = 0 for cycle. |
| Control demonstration in test environment only | Trace every control test artifact to production-equivalent logs/config IDs and execution windows. | Require production (or approved mirrored environment) provenance fields in test scripts. | Non-equivalent evidence caps R15.5/R15.7 at 25. |
| Finding splitting to avoid critical classification | Cluster related findings by root cause/process and recompute aggregate impact. | Add aggregation rule in severity policy for same-root-cause multi-point failures. | If split inflation is confirmed, recalculate severity and cap R15.10 at 50. |
| Premature closure based on promises, not retest | Sample "closed" findings and demand independent retest artifacts and sustained-window evidence. | Closure gate requires independent retest checklist with named reviewer and replay artifacts. | Invalid closures > 5% sample cap R15.13 at 25. |
| Reclassifying repeat findings as "new issue" to hide recurrence | Match control IDs/root causes across cycles using normalized taxonomy and text similarity. | Enforce persistent control ID and recurrence tagging policy. | Misclassification forces R15.14 score to 0 for cycle. |
| Methodology nonconformance hidden by selective QA sampling | Independently select QA sample from full completed audit population. | QAIP sampling plan approved by committee and includes surprise sample quota. | Nonconformance concealment caps R15.17 at 25. |
| Post-signoff report edits softening conclusions | Diff signed report hash against published version and validate change-author approvals. | Immutable signoff artifact and controlled post-signoff amendment process. | Unauthorized edits set R15.15 = 0 for cycle. |
| Interview coaching and staged walkthroughs | Run surprise walkthrough with different operators and compare operational variance. | Require at least one unannounced control walkthrough per high-risk audit. | Material discrepancy caps R15.8 and R15.11 at 50. |
| Retaliation risk suppressing adverse evidence | Compare anonymous hotline/control challenge volume with observed incident/finding signals for divergence. | Quarterly retaliation climate check and direct committee access for auditors/reporters. | If suppression pattern is substantiated, R15.18 = 0 and role-level hard fail review. |

## 5A) Independent replay and recompute protocol

| Control | Requirement | Failure effect |
| --- | --- | --- |
| Replay sample coverage | Non-author replay on `max(20 rows, 20% of scored R15 rows)` each iteration. | Replay failure tripwire; publication hold until rerun passes. |
| Gate-sensitive inclusion | All rows that can trigger/clear `G1..G6` or `RG1..RG4` must be replayed. | Publication hold and targeted replay required. |
| Replay tolerance | Anchor variance `<=1`, aggregate variance `<=5 points`, gate-state parity `100%`. | `R15.19` capped at `25`; affected rows rescored. |
| Recompute integrity | Final publication decision recomputed directly from gate states and row scores before publication. | Publication blocked until parity is restored. |
| Author separation | Replay reviewer cannot be the primary scorer for the same sampled row. | High-anchor evidence invalidated for affected rows. |

## 6) Tripwires and hard-fail conditions
| ID | Tripwire / hard-fail condition | Effect |
| --- | --- | --- |
| R15-HF1 | Confirmed evidence fabrication, falsification, or chain-of-custody tampering in any material finding. | Immediate overall R15 cycle FAIL; affected work invalidated and forensic review required. |
| R15-HF2 | Active conflict of interest in audit assignment for scoped critical area without documented recusal/mitigation. | Overall R15 cycle FAIL until reassignment and re-performance are completed. |
| R15-HF3 | Critical finding severity lowered without calibration panel record and evidence-backed rationale. | R15.10 set to 0; cycle cannot pass pending committee adjudication. |
| R15-HF4 | Any critical finding closed without independent retest evidence. | R15.13 set to 0 and overall R15 score capped at 50 for cycle. |
| R15-HF5 | Sampled high/critical finding cannot be independently reproduced from retained evidence. | R15.7 and R15.9 set to 0 for affected scope; cycle fail for that engagement. |
| R15-HF6 | Management override blocks issuance or materially edits final conclusions after signoff without committee authorization. | Overall R15 cycle FAIL and mandatory governance escalation. |
| R15-HF7 | Overdue critical finding remains un-escalated beyond one business day. | R15.16 set to 0 for cycle; release/go-live assurance signoff suspended. |
| R15-HF8 | Repeat high/critical control failure occurs in two consecutive cycles with no approved strengthened remediation plan. | R15.14 capped at 25 and conditional fail until plan acceptance. |
| R15-HF9 | External regulator or external auditor identifies material issue previously scored as closed/low without disclosure in assurance report. | R15.15 set to 0 and full retrospective recalibration required. |
| R15-HF10 | QAIP external assessment overdue beyond 5-year limit or critical QA deficiency left open > 90 days. | R15.17 capped at 25 and overall role cannot exceed conditional pass. |
| R15-HF11 | Gate truth-table replay for `G1..G6` and `RG1..RG4` is missing or computed/published outcomes mismatch. | R15.19 set to 0; publication blocked until replay parity is restored and verified. |
| R15-HF12 | Scoring-affecting rubric/evidence delta applied after approved iteration snapshot without approved delta dossier and retest evidence. | R15.20 set to 0; iteration packet marked invalid and rerun on approved snapshot. |
| R15-HF13 | Critical cross-role handoff lacks explicit `accepted`/`returned` state or required return metadata. | Publication blocked; affected adjudication path must be re-run with compliant metadata. |
| R15-HF14 | Any proposed `>90` anchor lacks same-iteration adversarial challenge evidence. | Affected rows downgraded to `75`; high-anchor publication blocked until resolved or rescored. |

### Tripwire recovery proof requirements

| ID set | Minimum recovery proof | Verification authority | Reopen rule |
| --- | --- | --- | --- |
| R15-HF11 | Full truth-table replay report, parity evidence, and mismatch disposition for each affected gate. | R15 + independent replay reviewer | Any later gate-parity mismatch in same iteration reopens hold. |
| R15-HF12 | Approved delta dossier, impacted-row map, targeted rescore, and gate replay evidence on approved snapshot. | R11 + R12 + R15 | Additional unauthorized delta in same iteration reopens invalidation review. |
| R15-HF13 | Reissued handoff artifacts with explicit state and complete return metadata, plus updated adjudication decision log. | R15 + counterpart owner | Missing metadata on a subsequent critical handoff reopens hold. |
| R15-HF14 | Same-iteration adversarial challenge evidence or approved rescore at allowed anchor. | R15 owner + independent reviewer | Missing proof in later publication checks reopens hold. |

## 7) Cross-role dependency and handoff criteria
| Dependency/handoff | Entry criteria from partner role | R15 handoff package requirements | Acceptance SLA and exit criteria |
| --- | --- | --- | --- |
| R0 Executive Sponsor / Audit Committee -> R15 (annual assurance mandate) | Risk appetite, strategic priorities, and mandatory assurance themes are published for the cycle. | Risk-based audit plan, coverage rationale, exclusions with justification, and committee approval record. | Initial plan acceptance <= 10 business days from mandate issue; exit when committee signoff is recorded. |
| R1 Product Manager -> R15 (new process/control introduction) | New or changed product workflow with control impact and launch timeline is documented. | Control objective map, planned test scope, risk ranking, and pre-launch assurance test schedule. | Triage <= 5 business days; exit when control coverage and testability are accepted. |
| R3 Engineering Manager / R4 Software Engineer -> R15 (technical control testing) | Control implementation details, logs, and environment metadata are available for sampling. | Test scripts, sample population extracts, evidence pull protocol, and replay instructions. | Evidence package completeness check <= 3 business days; exit when replay succeeds in sample test. |
| R5 QA / Test Engineer -> R15 (verification evidence reuse) | Test suites and defect history for scoped controls are current and versioned. | Independent assurance crosswalk of QA tests vs control objectives and identified gaps. | Crosswalk decision <= 4 business days; exit when gap ownership is assigned and dated. |
| R6 SRE / Platform -> R15 (operational control assurance) | SLO/incident, backup, and change-control telemetry for audit window is accessible. | Sampling plan for operational controls, incident replay set, and exception interpretation rules. | Operational evidence acceptance <= 5 business days; exit when sampled operational controls are independently verified. |
| R7 Security -> R15 (security-control findings alignment) | Vulnerability, IAM, and monitoring findings with severity and remediation status are available. | Consolidated control-failure view, severity reconciliation notes, and follow-up retest schedule. | Severity alignment <= 2 business days for criticals; exit when discrepancies are adjudicated with records. |
| R8 Privacy / Compliance / Legal -> R15 (obligation assurance traceability) | Applicable obligations and required controls are mapped and signed by legal/compliance. | Obligation-to-test trace matrix, legal interpretation notes, and evidentiary sufficiency conclusion. | Mapping validation <= 5 business days; exit when no unmapped mandatory obligation remains. |
| R12 DevOps / Release Manager -> R15 (release gate assurance) | Release candidate has control-impact list and unresolved findings list by severity. | Go/no-go assurance memo, open-risk exceptions, and required post-release verification checkpoints. | Gate response before CAB cutoff; exit when decision and residual-risk owner are documented. |
| R13 Operations / Support -> R15 (recurrence and closure quality) | Incident recurrence and ticket-based control failures are linked to control IDs. | Repeat-finding analysis, recurrence trend, and escalation recommendations with due dates. | Monthly review closure <= 3 business days after data cut; exit when repeat risks are assigned and tracked. |
| R14 FinOps / Procurement / Vendor Mgmt -> R15 (third-party control assurance) | Vendor obligations, SLA breaches, and control attestations for scoped vendors are current. | Third-party control test pack, evidence provenance links, and vendor-risk finding ratings. | Review <= 7 business days; exit when high-risk third-party findings have owners and closure dates. |

## 7A) Handoff state contract (mandatory)

Every critical handoff in Section 7 must include explicit state and metadata:
The `defect_class` vocabulary in this section is authoritative for all returned handoffs in this file.

| Field | Requirement | Enforcement |
| --- | --- | --- |
| `handoff_state` | Must be exactly `accepted` or `returned`. | Missing/implicit state triggers `R15-HF13`. |
| `defect_class` (required for `returned`) | One of `coverage`, `evidence`, `contradiction`, `replay`, `inflation`, `operability`, `governance` (authoritative pack-wide lexicon). | Missing or non-canonical class invalidates return and triggers reissue. |
| `severity_level` (required for `returned`) | One of `Medium`, `High`, `Critical`, mapped to canonical `defect_class` unless signed exception exists. | Missing/severity mismatch blocks closure. |
| `sla_hours` (required for `returned`) | Positive integer SLA in hours consistent with canonical severity map unless signed exception exists. | Missing/SLA mismatch blocks closure. |
| `downgrade_justification_hash` (required when severity is lowered for same open issue) | Immutable hash of R15-signed downgrade rationale packet. | Missing downgrade justification blocks acceptance. |
| `issue_id` (required for `returned`) | Stable issue identifier preserved across iterations for the same defect lifecycle. | Missing issue identity blocks acceptance. |
| `prior_state_hash` (required when transitioning `returned` -> `accepted`) | Immutable hash linking to prior returned-state decision artifact. | Missing prior-state linkage blocks closure transition. |
| `issue_state` | One of `new`, `returned`, `accepted`, `closed`, `reopened`. | Missing/invalid state blocks transition processing. |
| `reopen_reason_code` (required for `reopened`) | One of `new_evidence`, `replay_mismatch`, `policy_change`, `audit_finding`. | Missing reopen reason blocks reopen transition. |
| `reopen_authority_chain` (required for `reopened`) | Signed approver chain for reopen decision. | Missing reopen authority evidence blocks reopen transition. |
| `reopen_event_id` (required for `reopened`) | Immutable identifier for reopen event record. | Missing reopen event ID blocks reopen transition. |
| `transition_sequence` | Strictly increasing integer sequence per `issue_id`. | Non-monotonic transition sequence blocks publication. |
| `transition_actor` | Identity of accountable actor executing the state transition. | Missing transition actor blocks transition processing. |
| `transition_reason_code` | One of `new_finding`, `retest_passed`, `evidence_update`, `policy_enforcement`, `appeal_decision`. | Missing/invalid transition reason blocks transition processing. |
| `transition_proof_hash` | Immutable hash of transition evidence record for this state change. | Missing transition proof hash blocks transition processing. |
| `owner` | Single accountable owner identity. | Missing owner blocks closure. |
| `due_utc` | ISO 8601 UTC due timestamp (`YYYY-MM-DDTHH:MM:SSZ`) for returned defects. | Missing or non-UTC due date blocks closure. |
| `resubmission_utc` | ISO 8601 UTC resubmission timestamp (`YYYY-MM-DDTHH:MM:SSZ`) for returned handoffs. | Missing or non-UTC resubmission stamp blocks acceptance. |
| `escalated_utc` (required if SLA breached) | ISO 8601 UTC escalation timestamp for overdue returned handoffs. | Missing escalation timestamp after SLA breach blocks closure. |
| `snapshot_id` | Iteration snapshot identifier for the decision. | Missing snapshot reference blocks publication. |
| `decision_hash` | Hash of final handoff decision artifact. | Hash mismatch triggers integrity review. |

## 8) Cycle-level improvement checklist
Use this checklist each cycle (weekly for active audits, monthly for governance close). Every checked item must include linked evidence.

| Checklist item | Evidence required |
| --- | --- |
| [ ] Re-baselined audit universe against current systems/process/vendor inventory and updated risk scores. | Audit universe diff report, risk model output, approval ticket. |
| [ ] Locked approved iteration snapshot before scoring. | Signed snapshot manifest with rubric hash, gate-order checksum, scorebook version, and denominator snapshot. |
| [ ] Confirmed charter currency and independence attestations for current reporting lines. | Signed charter copy, independence attestation, committee acknowledgement. |
| [ ] Collected and reviewed COI declarations for all assigned auditors before fieldwork start. | COI roster, recusal decisions, assignment history log. |
| [ ] Revalidated objective-to-test traceability for all in-scope critical controls. | Trace matrix export with zero unresolved unmapped rows. |
| [ ] Peer-reviewed all new/changed test scripts for explicit pass/fail and negative-path coverage. | Test design review checklist and approvals. |
| [ ] Reconciled each sample population to source systems and locked sample-selection artifacts. | Population reconciliation workbook, sampling seed/hash record, exclusion approvals. |
| [ ] Verified evidence chain-of-custody integrity (timestamps, ownership, hashes) for sampled findings. | Evidence manifest, integrity verification logs, exception report. |
| [ ] Completed supervisory review of fieldwork workpapers and closed review comments. | Workpaper review queue snapshot and comment closure log. |
| [ ] Ran finding replay test on a sample of closed and draft findings. | Reproduction notes, replay success/failure register, corrective actions. |
| [ ] Executed severity calibration session for new high/critical findings with panel minutes. | Calibration packet, rating deltas, override approvals. |
| [ ] Replayed full gate truth table (`G1..G6`, `RG1..RG4`) and verified computed/published parity. | Gate replay worksheet, parity report, mismatch dispositions. |
| [ ] Challenged root-cause statements for top findings using alternative-cause review. | RCA challenge worksheet and accepted cause decision records. |
| [ ] Validated remediation plans for SMART quality, owner accountability, and interim controls. | Remediation plan QA checklist and owner signoffs. |
| [ ] Performed independent retest before closure on findings marked ready to close. | Retest artifacts, closure decision records, reopen watchlist. |
| [ ] Published recurrence trend and escalated repeat high/critical failures to governance forum. | Recurrence dashboard snapshot, escalation notices, meeting minutes. |
| [ ] QA-reviewed draft assurance report for statement-to-evidence traceability and contradiction closure. | Report QA checklist, evidence index, contradiction resolution log. |
| [ ] Audited all proposed `>90` anchors for independent and challenge evidence. | High-anchor proof audit pack and downgrade/rescore decisions. |
| [ ] Reviewed overdue finding aging and executed severity-based escalation SLAs. | Aging register, escalation timestamps, executive acknowledgements. |
| [ ] Completed QAIP sampling of finished audits and assigned owners for any methodology defects. | QAIP review results, defect tracker, closure plan. |
| [ ] Audited management override/retaliation logs and confirmed committee visibility for sensitive cases. | Override register, hotline case summary, committee briefing record. |
| [ ] Re-evaluated every approved scoring-affecting delta before publication. | Delta dossier, impacted-row map, targeted rescore, and gate replay outputs. |
| [ ] Ran bilateral handoff symmetry and defect-lexicon lint across all critical role pairs. | Symmetry-lint report with pair coverage, metadata parity results, and defect-class conformance summary. |
