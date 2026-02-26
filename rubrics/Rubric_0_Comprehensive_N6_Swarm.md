# Rubric 0 Master Instrument (N=6 Swarm-Drafted)

## Intent
This is a full-scale, enforcement-grade Rubric 0 for comprehensive artifact quality.
It is intentionally strict and anti-gaming by construction.

## Drafting Provenance
- method: six independent rubric-specialist agents (A1..A6)
- merge mode: section-preserving integration with a unified governance layer
- generated_utc: `2026-02-23T23:56:00Z`
- total_word_count: `36300`
- estimated_pages_at_500_words_per_page: `72.6`

## Coverage Model (Master)
| Section | Coverage Scope | Source File | Words | Lines |
| --- | --- | --- | ---: | ---: |
| A1 | Value Realization, Stakeholder Fit, Problem Framing | `A1_value_stakeholder.md` | 5633 | 463 |
| A2 | Requirements Fidelity, Specification Integrity, Scope Governance | `A2_requirements_spec.md` | 4823 | 177 |
| A3 | Technical/Domain Correctness, Verification Rigor | `A3_correctness_verification.md` | 4786 | 360 |
| A4 | Reliability, Security, Privacy, Abuse Resistance, Performance | `A4_reliability_security.md` | 5854 | 271 |
| A5 | UX, Accessibility, Information Design, Visual/Document Quality | `A5_ux_accessibility_visual.md` | 7413 | 1237 |
| A6 | Operability, Maintainability, Auditability, Compliance, Lifecycle Governance | `A6_operability_governance.md` | 5748 | 352 |

### Domain Boundary Contract (Non-overlap)
- `A1` owns upstream decision framing quality: problem definition, value model, stakeholder fit, tradeoff intent, and adoption/learning framing.
- `A2` owns requirement/specification execution quality: requirement fidelity, traceability, scope/change control, and verification readiness.
- `A3..A6` own downstream execution and production-readiness qualities.
- Any repeated concept across sections must use explicit cross-reference and single authoritative owner; duplicate normative requirements are prohibited.

## Master Scoring Aggregation
This master Rubric 0 uses a two-part score:
- Domain score from A1..A6.
- Role-layer score from R0..R15.
- Master final score = `(Domain score * 0.70) + (Role-layer score * 0.30)`, unless a governance charter override is approved before iteration snapshot lock and recorded with `override_id`, `effective_from_utc`, `expires_utc`, and `auto_revert=true`.

Authoritative controls:
- The sections `Iteration Snapshot Governance`, `Deterministic Gate and Contradiction Precedence`, `Role scoring protocol`, and `Role-layer hard gates` are authoritative for scoring execution.
- If any later text conflicts with these sections, these sections take precedence.

### Override Validity Contract
Any scoring-model or weighting override is valid only when all fields are present:
1. `override_id` (unique immutable identifier)
2. `authority_chain` (approvers by role)
3. `effective_from_utc`
4. `expires_utc`
5. `auto_revert=true`
6. `reason_code` in `{regulatory_change, incident_emergency, model_correction, scoring_bug_fix}`
7. `max_duration_hours` where `max_duration_hours <= 336`
8. `renewal_count` where `renewal_count <= 1` in a rolling two-iteration window
9. `control_ticket_id` linked to the approved change record
10. `override_owner` with accountable role identity
11. `reversion_verification_due_utc` where `reversion_verification_due_utc <= expires_utc + 24h`
12. `scope_selector` identifying the exact score components affected
13. `conflict_strategy` in `{forbid_overlap, supersede, merge_with_dual_report}`
14. `supersedes_override_id` (required when `conflict_strategy=supersede`)
15. `preflight_impact_hash` for approved before/after score simulation on affected scope
16. `blast_radius_estimate` describing impacted sections/roles and expected gate effects
17. `preflight_reviewer` (non-author) for independent impact validation
18. `preflight_tolerance_pct` where realized drift beyond tolerance requires override invalidation
19. `preflight_dataset_hash` for the exact evidence set used during preflight simulation
20. `realized_effect_hash` for published post-execution impact record on affected scope
21. `gate_diff_hash` capturing preflight-vs-realized gate-state delta artifact
22. `independent_recompute_hash` from non-author recomputation of realized override effects

Expired overrides are automatically invalid and must not be used in scoring.
Overrides exceeding duration or renewal limits are invalid and trigger override-abuse tripwire handling.
Overrides missing post-expiry reversion verification evidence within 24 hours are treated as override-control failures and block publication.
Overlapping active overrides on the same `scope_selector` are invalid unless governed by explicit `supersede` or signed `merge_with_dual_report` evidence.
Any override record with non-monotonic timestamps (`effective_from_utc > expires_utc`) is invalid and blocks publication.
Overrides with missing preflight impact simulation evidence are invalid for publication.
Supersede chains containing broken references or cycles are invalid and block publication.
Realized score/gate effects that materially deviate from approved preflight simulation beyond `preflight_tolerance_pct` invalidate the override for publication.
Preflight and realized impact hashes must reference the same snapshot and compatible denominator manifest.
Any override finalized without `realized_effect_hash` is invalid for publication closeout.
Any override with missing `gate_diff_hash` or `independent_recompute_hash` is invalid for publication closeout.
Independent recompute mismatch on override-affected scope blocks publication until parity is restored.

### Mode 1: Equal Domain Authority (default)
- Domain score = `mean(A1..A6 section scores)`.
- Master final score = `(Domain score * 0.70) + (Role-layer score * 0.30)`.

### Mode 2: Risk-Weighted Domain Authority (for regulated/high-impact contexts)
- Domain score = `(A1*0.12) + (A2*0.16) + (A3*0.18) + (A4*0.22) + (A5*0.14) + (A6*0.18)`.
- Master final score = `(Domain score * 0.70) + (Role-layer score * 0.30)`.

### Deterministic Calculation Contract
1. Scorable rows use anchors `0/25/50/75/90/100` only.
2. Row-level admissibility failures and row-level caps apply before any row aggregation.
3. Section and role scores are computed as weighted means of their post-cap rows.
4. Role-layer hard gates (`RG*`) are applied before global hard gates (`G*`).
5. If any blocking gate is active, no arithmetic pass outcome may be published.
6. Final numeric score is computed only after all caps and gate effects are applied.

### Rounding and Cap-Order Specification
| Step | Operation | Deterministic rule |
| --- | --- | --- |
| 1 | Row anchor assignment | One of `0/25/50/75/90/100` only |
| 2 | Row caps and row invalidation | Apply admissibility caps and tripwires first |
| 3 | Section and role arithmetic | Use weighted mean with full precision |
| 4 | Role-layer gate effects | Apply `RG1..RG6` outcomes |
| 5 | Global gate effects | Apply `G1..G6` outcomes |
| 6 | Master score calculation | `0.70*Domain + 0.30*Role` only when no blocking gate is active |
| 7 | Numeric rounding | Round half-up to nearest whole number for decision band assignment |

## Iteration Snapshot Governance
All scoring in an iteration must reference one immutable snapshot.

| Snapshot field | Required value |
| --- | --- |
| `iteration_id` | Unique iteration identifier |
| `snapshot_id` | Unique immutable snapshot identifier for the iteration |
| `rubric0_hash` | Hash of this file used for scoring |
| `role_pack_hash` | Hash of `rubrics/Rubric_0_Role_Expansion_Pack_N16.md` used for scoring |
| `scoring_template_hash` | Hash of score workbook/schema template |
| `denominator_manifest_hash` | Hash of row-population manifest used for sampling and rates |
| `cutoff_utc` | Evidence cutoff timestamp for current iteration |
| `owner_roster_hash` | Hash of scorer/reviewer ownership and independence roster |
| `approval_chain_record` | Signed authority-chain approvals for publication |

### Snapshot State Machine
| State | Entry condition | Allowed actions | Mandatory evidence | Failure effect |
| --- | --- | --- | --- | --- |
| `SNAPSHOT_LOCKED` | All snapshot fields populated and signed | Scoring, replay, adjudication | Snapshot manifest + signatures | Missing fields -> scoring blocked |
| `REOPEN_REQUESTED` | Scoring-affecting delta identified after lock | Impact analysis only | Reopen request with rationale and impacted rows | No request -> unauthorized change |
| `REOPEN_APPROVED` | R0 + R15 approve reopen | Targeted re-score and gate replay on impacted scope | Approved reopen record | Missing approval -> snapshot `INVALID` |
| `CLOSE_READY` | All blocking defects closed and gate replay passed | Publication package assembly | Gate replay log + contradiction closure log | Any active blocking defect -> publication blocked |
| `CLOSED` | Publication approved with immutable evidence index | Read-only archival | Final signed package | Post-close score change without reopen -> snapshot `INVALID` |

### Delta and Re-evaluation Rules
| Rule ID | Trigger | Required action | Score consequence if missing |
| --- | --- | --- | --- |
| SG-01 | Any scoring-affecting rubric delta after snapshot lock | Open `REOPEN_REQUESTED`; produce impacted-row map; rerun targeted re-score and gate replay | Snapshot `INVALID` |
| SG-02 | Denominator or metric-definition change after snapshot lock | Dual-report (`before` and `after`) plus approved reopen | Affected scope capped at `50`; unresolved at cutoff -> snapshot `INVALID` |
| SG-03 | Unauthorized edit to anchors, weights, or gates | Revert and restart from approved snapshot | Snapshot `INVALID` |
| SG-04 | Approved delta lacks impacted-row retest evidence | Block publication until retest complete | Publication blocked |

## Cross-Section Hard Gates (Global Tripwires)
Any triggered gate below blocks overall pass regardless of section averages.

| Gate ID | Global Condition | Effect |
| --- | --- | --- |
| G1 | Any evidence fabrication/tamper event confirmed in any section | overall score = 0; snapshot `INVALID`; mandatory forensic review |
| G2 | Any unresolved Severity-1 contradiction at iteration cutoff | overall FAIL; publication blocked |
| G3 | Any unresolved legal/privacy/security mandatory-control breach at release point | overall FAIL; publication blocked |
| G4 | Any critical path is non-operable for intended users (including accessibility-critical path) | overall FAIL; publication blocked |
| G5 | Independent replay/recompute cannot reproduce material claims | overall FAIL; snapshot `INVALID` until replay passes |
| G6 | Release/publish executed without required authority chain approvals | overall FAIL; snapshot `INVALID` |

## Deterministic Gate and Contradiction Precedence
Execution precedence is fixed and mandatory:
1. Evidence admissibility validation.
2. Row-level tripwires and caps.
3. Role-layer gate evaluation (`RG1..RG6`).
4. Global gate evaluation (`G1..G6`).
5. Arithmetic score publication and decision band assignment (only if no blocking gate is active).

Contradiction precedence classes:
1. Legal/privacy/security mandatory-control contradictions.
2. Release/operability blocker contradictions.
3. Data/AI safety/fairness contradictions.
4. Cost/schedule/performance tradeoff contradictions.

Severity rule:
- Any unresolved Severity-1 contradiction at iteration cutoff automatically activates `G2` and `RG3`.

### Required Gate Truth-Table Replay Set
These cases must be replayed and signed by R15 before publication.

| Replay ID | Simulated inputs | Expected outcome |
| --- | --- | --- |
| GT-01 | No active `G*` or `RG*` | Arithmetic outcome allowed |
| GT-02 | `RG2` active only | Affected role/rows capped; no fail unless another fail gate is active |
| GT-03 | `RG1` active | overall FAIL |
| GT-04 | `RG4` active on a critical role | affected role = `0`; re-evaluate `RG1`; fail if threshold violated |
| GT-05 | `G2` active | overall FAIL |
| GT-06 | `G1` active with any other states | overall score = `0`; snapshot `INVALID` |
| GT-07 | `G5` active with high arithmetic score | overall FAIL; snapshot `INVALID` until replay passes |
| GT-08 | `G6` active | overall FAIL; snapshot `INVALID` |
| GT-09 | R12 Severity-1 contradiction unresolved at cutoff | `G2` + `RG3` active -> overall FAIL |
| GT-10 | R13 Severity-1 contradiction unresolved at cutoff | `G2` + `RG3` active -> overall FAIL |
| GT-11 | R14 Severity-1 cost-vs-risk contradiction unresolved at cutoff | `G2` + `RG3` active -> overall FAIL |
| GT-12 | Unauthorized post-lock rubric edit | snapshot `INVALID` |

## Anti-Gaming Meta-Protocol (Applies to Every Section)
| Control | Minimum execution rule | Failure consequence |
| --- | --- | --- |
| Independent sampling | `max(15% of scored rows, 10 rows)` per section | Missing sample invalidates affected section score publication |
| Surprise challenge | At least one adversarial challenge per section per iteration | Affected section capped at `50` until challenge evidence exists |
| Raw recompute | Recompute sampled metrics from raw evidence artifacts | Mismatch beyond tolerance triggers replay hold |
| Backfill exclusion | Evidence created after `cutoff_utc` excluded unless reopen approved | Ineligible evidence auto-removed; impacted rows rescored |
| Contradiction aging | Severity-1 contradiction aging beyond SLA is blocking | Activates `G2`/`RG3` fail behavior |
| Provenance integrity | Non-immutable evidence cannot support non-zero claims | Claim scored `0` |

## Adjudication Sequence
1. Confirm `SNAPSHOT_LOCKED` state and validate manifest hashes.
2. Validate evidence admissibility and cutoff eligibility.
3. Score domain sections (A1..A6) and role layer (R0..R15).
4. Apply row-level caps and tripwires.
5. Apply role-layer hard gates (`RG*`), then global hard gates (`G*`).
6. Execute required gate truth-table replay set (`GT-01..GT-12`) and capture R15 sign-off.
7. Compute final score only if no blocking gate is active.
8. Publish one of: `FAIL`, `CONDITIONAL FAIL`, `CONDITIONAL PASS`, `PASS`, `HIGH-ASSURANCE PASS`.
9. Mark snapshot status: `CLOSED` or `INVALID`.

### Decision Bands
| Final Score | Decision | Required Action |
| ---: | --- | --- |
| 0-59 | FAIL | block release; full remediation plan |
| 60-74 | CONDITIONAL FAIL | limited pilot only with executive waiver |
| 75-84 | CONDITIONAL PASS | release allowed with dated remediation contract |
| 85-94 | PASS | release approved under normal controls |
| 95-100 | HIGH-ASSURANCE PASS | release approved; candidate benchmark artifact |

## Section Index
- A1: Value and stakeholder legitimacy.
- A2: Requirement/spec rigor and scope governance.
- A3: Correctness, factual integrity, and reproducible verification.
- A4: Reliability/security/privacy/abuse/performance resilience.
- A5: UX/accessibility/information/visual quality.
- A6: Operability/audit/compliance/lifecycle control.

## Role-Centric Dimension Layer (Deloitte-Style Operating Model)
This master rubric now includes a role-centric overlay where each major role is a top-level accountability dimension and each role concern is scored as a sub-dimension.

### Design intent
1. Keep domain quality (A1..A6) and role accountability orthogonal.
2. Prevent diffusion of responsibility by forcing named role-level scores.
3. Align strategy, architecture, engineering, risk/control, operations, and value realization.

### Role dimension catalog
| Role Dimension | Core sub-dimensions (role concerns) |
| --- | --- |
| R0 Executive Sponsor / Business Owner | strategic objective clarity; risk appetite and tolerance setting; investment and resourcing adequacy; decision timeliness and escalation behavior; accountable ownership continuity; benefit-realization governance; exception approval discipline |
| R1 Product Manager | problem-value framing quality; requirement quality and prioritization discipline; roadmap coherence and tradeoff integrity; stakeholder alignment and conflict handling; KPI/OKR definition quality; release-scope governance; value realization follow-through |
| R2 Product Architect / Enterprise Architect | architecture boundary clarity; NFR architecture quality; integration and contract topology rigor; data architecture and lineage design; resilience and failure-mode design; security/privacy-by-design architecture; technical debt trajectory governance |
| R3 Engineering Manager | delivery predictability and flow health; engineering quality gate enforcement; team capability and staffing adequacy; cross-team dependency governance; incident learning closure discipline; risk escalation quality; maintainability and debt allocation |
| R4 Software Engineer | implementation correctness; modularity/readability and maintainability; test design quality and assertion rigor; error handling and defensive coding; performance and efficiency discipline; secure coding hygiene; observability hooks and runtime diagnostics |
| R5 QA / Test Engineer | verification strategy completeness; requirement-to-test traceability integrity; oracle quality and falsifiability; automation stability and flake control; non-functional test depth; defect severity calibration; regression gate reliability |
| R6 SRE / Platform Engineer | SLI/SLO design and governance; capacity and saturation control; deployment/rollback safety; incident detection and response quality; backup/restore and DR readiness; platform dependency hygiene; operational automation robustness |
| R7 Security Engineer / Security Architect | threat model completeness and freshness; identity/authentication robustness; authorization and least-privilege integrity; vulnerability and patch governance; secrets/crypto/key lifecycle controls; detection/response efficacy; supply-chain security controls |
| R8 Privacy / Compliance / Legal | obligation-to-control mapping integrity; lawful basis and consent governance; data classification and handling controls; retention/DSAR process quality; transfer and jurisdiction control discipline; regulatory reporting readiness; audit defensibility |
| R9 Data / AI Engineer or Scientist | data quality and lineage integrity; feature/ETL pipeline reliability; statistical validity and uncertainty reporting; model evaluation and drift governance; reproducibility of data/model outputs; bias/fairness control discipline; explainability and provenance quality |
| R10 UX Researcher / Designer | research validity and sample quality; task-flow usability quality; information architecture coherence; accessibility and inclusive design quality; visual hierarchy and readability quality; design-system consistency; UX evidence traceability |
| R11 Technical Writer / DocOps / PDF Owner | procedural accuracy and completeness; source-of-truth integrity; citation and factual traceability; structure/readability quality; publication pipeline reliability; link/reference integrity; localization and revision governance |
| R12 DevOps / Release Manager | CI/CD gate integrity; environment parity and reproducibility; release approval chain integrity; artifact provenance/signing; rollback and emergency-path governance; change window discipline; post-release verification rigor |
| R13 Operations / Support / Customer Success | supportability and runbook quality; ticket triage and escalation fidelity; customer-facing incident communication quality; KB accuracy and freshness; closure quality and recurrence prevention; service-level adherence; user-impact quantification |
| R14 FinOps / Procurement / Vendor Management | unit economics and cost transparency; budget adherence and forecast discipline; third-party/vendor risk controls; license/commercial compliance; contract obligation traceability; spend-to-value optimization; renewal/exit governance |
| R15 Internal Audit / Assurance | control test design integrity; sample-method validity; independence and conflict-of-interest controls; finding severity calibration; remediation verification quality; recurrence detection discipline; assurance-report traceability and defensibility |

### Role scoring protocol
1. Score each role sub-dimension using anchors `0/25/50/75/90/100`.
2. Require explicit `who/what/where/time/version/hash` evidence for every non-zero role score.
3. Role score = weighted mean of that role's sub-dimensions (equal weights unless pre-approved override).
4. Role-layer score = weighted mean across R0..R15.
5. Role-layer default weight in master score = 30% (A1..A6 remain 70% combined), configurable by governance charter.

### Role-layer Evidence Admissibility Schema (Mandatory for Non-zero Scores)
| Field | Requirement |
| --- | --- |
| `who` | Identity and role of evidence producer or reviewer |
| `what` | Specific claim/test/control event being scored |
| `where` | Immutable locator to source artifact or system record |
| `time_utc` | Event/evidence timestamp in UTC |
| `rubric_snapshot_id` | Snapshot identifier used for scoring |
| `rubric_snapshot_hash` | Hash of rubric snapshot used for scoring |
| `version` (`version_id`) | Artifact or dataset version used by the claim |
| `hash` (`evidence_hash`) | Hash of evidence payload or source export |
| `provenance_chain` (`provenance_source`) | Source-to-claim lineage with transformation steps |

Sampling and enforcement:
- Replay sampling minimum is `max(15% of scored rows, 10 rows)` per role and must include all gate-sensitive rows and all `>90` rows.
- Replay samples must be stratified: at least one sampled row from each active domain section and each active gate class touched in the iteration.
- Replay tolerance is `<=1` anchor drift, `<=5` numeric points variance, and `100%` gate-state parity on sampled rows.
- If replay tolerance is breached on more than `10%` of sampled rows for a role, cap that role at `50` and block publication until replay root cause is closed.
- Missing any required field in a sampled non-zero row sets that row score to `0`.
- If sampled missing-field rate for a role exceeds `5%`, that role score is set to `0` for the iteration.
- If sampled missing-field rate across all non-zero rows exceeds `10%`, snapshot status is `INVALID`.

### Role-layer hard gates
| Gate ID | Condition | Effect |
| --- | --- | --- |
| RG1 | Any critical role (R1, R2, R3, R4, R6, R7, R8, R12) has score < 60 | overall FAIL |
| RG2 | Any role score above 75 without independent reviewer evidence | role score capped at 75 |
| RG3 | Any unresolved cross-role contradiction on critical requirement/spec/control | overall FAIL until resolved |
| RG4 | Any role evidence package fails integrity/provenance checks | affected role score = 0 for iteration |
| RG5 | Any row scored above 90 without mandatory challenge/replay proof | affected row capped at 75; systemic breach triggers snapshot `INVALID` |
| RG6 | Any high-impact fairness disparity breach remains open past SLA without approved waiver | overall FAIL until mitigation closes or waiver is approved by `R8 + R15 + R0` |

### R9 Fairness and Disparity Governance Contract (Mandatory)
| Control | Requirement | Deterministic consequence if unmet |
| --- | --- | --- |
| F1 Threshold definition | For each in-scope high-impact segment, define one primary disparity metric and threshold in the snapshot package (for example: max TPR/FNR gap, calibration error gap, or parity ratio floor). | If threshold is missing, any fairness-related row in R9 cannot score above `50`. |
| F2 Breach triage SLA | Any threshold breach must be logged and assigned within `1 business day`. | Unassigned or unlogged breach at cutoff forces `RG6` and publication hold. |
| F3 Mitigation closure SLA | Breach must be mitigated or formally waived within `3 business days`. | Unresolved breach past SLA sets affected R9 rows to `0` and triggers `RG6`. |
| F4 Waiver authority and expiry | Waiver requires explicit approval by `R8 + R15 + R0`, with rationale, compensating controls, and `expires_utc`. | Missing authority chain or expiry makes waiver invalid; breach is treated as unresolved and `RG6` applies. |
| F5 Replayable evidence | Non-zero fairness claims require `who/what/where/time/version/hash` plus reproducible slice outputs and mitigation evidence. | Missing replayable evidence caps related rows at `50`; repeated failures mark snapshot `INVALID`. |
| F6 Contradiction precedence | When accuracy/cost claims conflict with fairness obligations, fairness contract controls unless a valid waiver exists. | Contradiction remains pass-blocking under `RC-R9` and cannot be bypassed by arithmetic averages. |

### High-Anchor Proof Gates
| Requested score band | Mandatory evidence | Missing-proof effect |
| --- | --- | --- |
| `>75` | Independent corroboration by non-author reviewer | Cap affected row at `75` |
| `>90` | Independent corroboration + same-iteration adversarial challenge + replay + recompute parity | Cap affected row at `75`; open inflation defect |
| `100` | All `>90` proof plus two non-author independent witness replays in distinct environments | Downgrade to `90` unless all proofs are present |

### Role Contradiction Precedence and SLA (Pass-Blocking Classes)
| Class ID | Contradiction example | Owner | SLA | Unresolved effect |
| --- | --- | --- | --- | --- |
| RC-R9 | Accuracy/latency claim conflicts with fairness/safety or retention obligations | R9 + R8 | Classify 1 business day, resolve 3 business days | Activate `RG3` and `G2` |
| RC-R12 | Release speed pressure conflicts with failed mandatory gate | R12 + R7/R8 | Classify same day, resolve before publish cutoff | Activate `RG3` and `G2` |
| RC-R13 | SLA success claim conflicts with unresolved critical incident evidence | R13 + R12 | Classify same day, resolve 2 business days | Activate `RG3` and `G2` |
| RC-R14 | Cost-saving claim conflicts with legal/security/reliability blockers | R14 + R7/R8/R12 | Classify 1 business day, resolve 3 business days | Activate `RG3` and `G2` |

### Operational Tripwire Catalog (Pass-Blocking)
| Tripwire ID | Trigger | Detection method | Immediate effect | Owner | Minimum recovery proof |
| --- | --- | --- | --- | --- | --- |
| RT-R0-01 | Missing snapshot manifest fields or missing authority-chain signatures | Snapshot manifest audit | Publication blocked | R0 + R15 | Complete signed snapshot manifest |
| RT-R0-02 | Override record exceeds `max_duration_hours`, exceeds `renewal_count`, or uses non-canonical `reason_code` | Override ledger lint | Snapshot `INVALID`; publication blocked | R0 + R15 | Corrected override ledger and full gate replay on approved snapshot |
| RT-R0-03 | Override expires without signed reversion verification evidence by `reversion_verification_due_utc` | Override reversion audit | Snapshot `INVALID`; publication blocked | R0 + R12 + R15 | Reversion verification report plus full gate replay on approved snapshot |
| RT-R0-04 | Overlapping active overrides affect the same `scope_selector` without valid `conflict_strategy` resolution | Override conflict-matrix lint | Snapshot `INVALID`; publication blocked | R0 + R15 | Conflict-resolution record and full gate replay on approved snapshot |
| RT-R0-05 | Override record contains non-monotonic or malformed effective/expiry timestamps | Override timeline lint | Snapshot `INVALID`; publication blocked | R0 + R12 + R15 | Corrected override timeline evidence and replay-parity proof |
| RT-R0-06 | Override lacks approved preflight impact simulation for affected scope/gates | Override preflight audit | Publication blocked; override invalid for scoring | R0 + R2 + R15 | Signed preflight simulation record and replay parity evidence |
| RT-R0-07 | `supersedes_override_id` chain contains missing references or cyclic dependency | Override chain-integrity lint | Snapshot `INVALID`; publication blocked | R0 + R15 | Corrected acyclic supersede chain and full gate replay |
| RT-R0-08 | Realized override effect exceeds approved `preflight_tolerance_pct` on score/gate outcomes | Preflight-vs-realized drift audit | Override invalid for publication; snapshot `INVALID` until rescore on approved configuration | R0 + R2 + R15 | Drift analysis, corrected preflight, and full gate replay parity |
| RT-R0-09 | `preflight_dataset_hash` and `realized_effect_hash` reference different snapshot/denominator contexts | Override context-consistency lint | Snapshot `INVALID`; publication blocked | R0 + R2 + R15 | Context-aligned preflight/realized records with replay parity |
| RT-R0-10 | Override reaches publication closeout without `realized_effect_hash` record | Override closeout completeness audit | Publication blocked until closeout evidence is complete | R0 + R12 + R15 | Signed realized-effect record and gate replay confirmation |
| RT-R0-11 | Override closeout is missing `gate_diff_hash` or `independent_recompute_hash` | Override closeout integrity audit | Publication blocked; override closeout invalid | R0 + R11 + R15 | Completed closeout integrity bundle and replay parity evidence |
| RT-R0-12 | Independent recompute hash mismatches published override-affected outputs | Override recompute parity audit | Snapshot `INVALID`; publication blocked | R0 + R11 + R15 | Recompute parity restoration and corrected publication package |
| RT-R1-01 | Critical handoff lacks explicit `accepted`/`returned` state or missing defect metadata | Handoff ledger audit | R1 capped at `50`; publication hold | R1 + R15 | Corrected handoff records and impacted-row re-score |
| RT-R1-02 | Critical bilateral handoff pair missing on one side or using non-canonical `defect_class` lexicon | Handoff symmetry and lexicon lint | Publication hold until parity is restored | R0 + R15 | Passing symmetry-lint report and updated handoff artifacts |
| RT-R2-01 | Calculator parity failure or ambiguous cap-order outcome | Dual-calculator parity test | Snapshot `INVALID` until fixed | R2 + R12 | Parity pass evidence and recomputed outputs |
| RT-R3-01 | Scoring close misses SLA by >2 business days due to rubric logic defects | Iteration timing report | R3 capped at `50`; remediation required | R3 | Signed remediation plan and on-time rerun |
| RT-R4-01 | Unapproved scoring-affecting rubric edit after snapshot lock | Hash diff audit | Snapshot `INVALID` | R4 + R15 | Revert to approved hash and full impacted-scope re-score |
| RT-R4-02 | Mandatory engineering anti-gaming controls skipped in current iteration | Control checklist audit | R4-relevant scope capped at `50`; publication hold | R4 + R15 | Completed controls, challenge evidence, and rescored rows |
| RT-R5-01 | Mandatory anti-gaming challenge suite not executed | Control checklist audit | Affected scope capped at `50`; publication hold | R5 | Completed challenge suite and replay evidence |
| RT-R6-01 | Baseline hash or denominator drift without approved reopen | Snapshot/denominator diff audit | Snapshot `INVALID` | R6 + R15 | Approved reopen and dual-report reconciliation |
| RT-R6-02 | Mandatory runtime anti-gaming controls skipped in current iteration | Control checklist audit | R6-relevant scope capped at `25`; unresolved at cutoff -> snapshot `INVALID` | R6 + R15 | Completed controls, replay proof, and rescored rows |
| RT-R7-01 | Security gate bypass path found in simulation | Gate simulation replay | Affected security scopes capped at `25`; publication hold | R7 | Corrected gate logic and successful replay |
| RT-R7-02 | Mandatory security anti-gaming controls skipped in current iteration | Control checklist audit | R7-relevant scope capped at `25`; unresolved at cutoff -> snapshot `INVALID` | R7 + R15 | Completed controls, adversarial challenge evidence, and rescored rows |
| RT-R8-01 | Sampled non-zero rows missing admissibility fields exceed threshold | Admissibility sample audit | R8 score set to `0` for iteration | R8 + R15 | Defect-rate below threshold and rescore |
| RT-R9-01 | Any `>90` row lacks challenge evidence | High-anchor audit | Affected rows capped at `75` | R9 + R15 | Added challenge evidence and row-level re-adjudication |
| RT-R9-02 | Fairness disparity threshold breach lacks mitigation closure by SLA or valid waiver | Fairness governance audit | overall FAIL; publication hold; affected R9 rows set to `0` | R9 + R8 + R15 | Mitigation closure evidence or signed waiver with authority chain, compensating controls, and expiry |
| RT-R10-01 | UX/accessibility critical-path row scored `>50` with scanner-only evidence | Accessibility evidence audit | Affected UX scope capped at `25`; hold | R10 + R8 | Manual AT evidence and rescoring |
| RT-R11-01 | Final publication outcome differs from independent recompute | Score ledger parity audit | Snapshot `INVALID` | R11 + R12 | Recomputation parity and corrected publication package |
| RT-R12-01 | Severity-1 release contradiction unresolved past SLA | Contradiction aging audit | overall FAIL; publication hold | R12 | Closed contradiction record and impacted-row rescore |
| RT-R13-01 | Replay variance threshold breached on support sample | Independent replay audit | R13 capped at `50`; unresolved breach -> snapshot `INVALID` | R13 + R15 | Replay pass report and root-cause closure |
| RT-R14-01 | Severity-1 cost-vs-risk contradiction unresolved at cutoff | Contradiction aging audit | overall FAIL | R14 + R15 | Closure evidence with deterministic rescore |
| RT-R15-01 | Required gate truth-table replay set missing or unsigned | Replay packet audit | Snapshot `INVALID` | R15 | Signed `GT-01..GT-12` replay package |

### Crosswalk: roles to domain sections
| Role | A1 | A2 | A3 | A4 | A5 | A6 |
| --- | --- | --- | --- | --- | --- | --- |
| R0 Executive Sponsor | primary | primary | supporting | supporting | supporting | primary |
| R1 Product Manager | primary | primary | supporting | supporting | supporting | primary |
| R2 Product Architect | supporting | primary | primary | primary | supporting | primary |
| R3 Engineering Manager | supporting | supporting | primary | primary | supporting | primary |
| R4 Software Engineer | supporting | supporting | primary | primary | supporting | supporting |
| R5 QA/Test Engineer | supporting | primary | primary | primary | supporting | supporting |
| R6 SRE/Platform Engineer | supporting | supporting | supporting | primary | supporting | primary |
| R7 Security Engineer | supporting | supporting | supporting | primary | supporting | primary |
| R8 Privacy/Compliance/Legal | supporting | primary | supporting | primary | supporting | primary |
| R9 Data/AI Engineer | supporting | supporting | primary | supporting | supporting | supporting |
| R10 UX Researcher/Designer | supporting | supporting | supporting | supporting | primary | supporting |
| R11 Technical Writer/DocOps | supporting | primary | primary | supporting | primary | supporting |
| R12 DevOps/Release Manager | supporting | supporting | supporting | primary | supporting | primary |
| R13 Operations/Support | supporting | supporting | supporting | primary | supporting | primary |
| R14 FinOps/Procurement/Vendor | primary | supporting | supporting | supporting | supporting | primary |
| R15 Internal Audit/Assurance | supporting | supporting | primary | primary | supporting | primary |

### Role expansion pack (N=16)
The detailed role-wise sub-dimension expansions are maintained in:
- `rubrics/Rubric_0_Role_Expansion_Pack_N16.md`
- `rubrics/Rubric_1_Comprehensive_N6_Swarm.md` (meta-rubric that scores this Rubric_0)
- `rubrics/Rubric_1_Role_Expansion_Pack_N16.md` (role-wise rubric-for-rubric expansions)

Canonical role files:
- `swarm_outputs/role_expansions/R0_executive_sponsor_business_owner.md`
- `swarm_outputs/role_expansions/R1_product_manager.md`
- `swarm_outputs/role_expansions/R2_product_architect_enterprise_architect.md`
- `swarm_outputs/role_expansions/R3_engineering_manager.md`
- `swarm_outputs/role_expansions/R4_software_engineer.md`
- `swarm_outputs/role_expansions/R5_qa_test_engineer.md`
- `swarm_outputs/role_expansions/R6_sre_platform_engineer.md`
- `swarm_outputs/role_expansions/R7_security_engineer_security_architect.md`
- `swarm_outputs/role_expansions/R8_privacy_compliance_legal.md`
- `swarm_outputs/role_expansions/R9_data_ai_engineer_scientist.md`
- `swarm_outputs/role_expansions/R10_ux_researcher_designer.md`
- `swarm_outputs/role_expansions/R11_technical_writer_docops_pdf_owner.md`
- `swarm_outputs/role_expansions/R12_devops_release_manager.md`
- `swarm_outputs/role_expansions/R13_operations_support_customer_success.md`
- `swarm_outputs/role_expansions/R14_finops_procurement_vendor_management.md`
- `swarm_outputs/role_expansions/R15_internal_audit_assurance.md`

---

# Section 1: A1
- source_file: `A1_value_stakeholder.md`
- scope: Value Realization, Stakeholder Fit, Problem Framing
- word_count: 5633
- line_count: 463

# A1 Value & Stakeholder Rubric Section

## Purpose and enforcement posture

This A1 section is the strict evaluation block for **Value Realization**, **Stakeholder Fit**, and **Problem Framing** inside Master Rubric 0.

This rubric is designed for high-integrity artifact review across software products, technical documents, PDFs, and web deliverables. It is written to prevent narrative inflation, metric gaming, and shallow stakeholder claims.

Evaluation stance is adversarial by default:
1. Claims are treated as false until evidence proves otherwise.
2. Missing evidence is scored as failure, not partial credit.
3. Unowned risks are treated as unresolved risks.
4. Polished presentation is not a substitute for traceability.

This section must be applied before approval, major investment, scaling decisions, or public release when value and stakeholder impact are central claims.

## Applicability

Use this section for:
1. Product strategy memos and investment proposals.
2. PRDs, architecture decision records, and scope docs.
3. Pilot reports and post-launch value assessments.
4. Policy, compliance, and operational change artifacts.
5. Public-facing web pages and PDFs claiming outcomes.

## Core evaluation model

### Top-level dimensions and weights

| Code | Top-level dimension | Weight |
|---|---|---:|
| D1 | Problem Framing Integrity | 18% |
| D2 | Value Realization Model Quality | 20% |
| D3 | Stakeholder Fit and Segment Alignment | 20% |
| D4 | Solution-Need Alignment and Tradeoff Discipline | 16% |
| D5 | Adoption and Realization Feasibility | 16% |
| D6 | Measurement, Learning, and Governance Discipline | 10% |

### Scoring math

```text
Sub-dimension score ∈ {0, 25, 50, 75, 90, 100}
Dimension score = mean of its sub-dimensions
A1 overall score = Σ (dimension score × dimension weight)
```

### Gate conditions required before passing

All gates are mandatory:
1. Evidence completeness ratio >= 90% for required evidence list.
2. No pass/fail tripwire triggered.
3. No top-level dimension score < 60.
4. Overall weighted A1 score >= 75.
5. No fabricated, contradictory, or unverifiable evidence.

If any gate fails, the A1 result is fail regardless of calculated score.

## Dimension architecture (3 levels)

The architecture uses three levels:
1. Dimension
2. Sub-dimension
3. Indicators (operational tests)

Each indicator must be demonstrably testable and traceable.

| Dimension | Sub-dimension | Indicators (operational tests) |
|---|---|---|
| D1 Problem Framing Integrity | D1.1 Problem statement precision | I1: Statement identifies actor, blocked job, measurable impact, and time horizon. I2: Root-cause hypothesis is separate from symptom description. I3: Single accountable owner and decision date are explicit. |
| D1 Problem Framing Integrity | D1.2 Boundary and context integrity | I1: Start/end process boundaries are explicit. I2: Regulatory, policy, technical constraints are listed with source references. I3: Upstream and downstream dependencies have named owners. |
| D1 Problem Framing Integrity | D1.3 Baseline quantification fidelity | I1: Baseline metric formula and units are explicit. I2: Data provenance and sampling method are reproducible. I3: Baseline window is representative (minimum 4 weeks or justified exception). |
| D1 Problem Framing Integrity | D1.4 Causal model rigor | I1: Causal chain from intervention to outcome is explicit. I2: At least two plausible alternative explanations are evaluated. I3: High-uncertainty assumptions are ranked and test plans exist. |
| D1 Problem Framing Integrity | D1.5 Risk and harm framing | I1: Harm pathways are identified by affected stakeholder class. I2: Severity and likelihood are rated with thresholds. I3: Rollback or halt criteria are pre-defined before launch. |
| D1 Problem Framing Integrity | D1.6 Non-goals and anti-requirements | I1: Non-goals prevent scope laundering. I2: Explicit unacceptable tradeoffs are documented. I3: Any exception requires formal sign-off from accountable sponsor. |
| D2 Value Realization Model Quality | D2.1 Outcome hierarchy completeness | I1: North-star outcome maps to objective. I2: Leading and lagging indicators are linked to shared outcome chain. I3: Outcomes cover user value, business value, and operational value. |
| D2 Value Realization Model Quality | D2.2 Metric definition quality | I1: KPI dictionary includes formulas, units, and owners. I2: Guardrail metrics block local optimization damage. I3: Targets and alert thresholds are time-bound. |
| D2 Value Realization Model Quality | D2.3 Benefit-cost model credibility | I1: Benefit estimates include range and confidence assumptions. I2: Full lifecycle costs are included (build, run, support, compliance, migration). I3: Sensitivity analysis includes best/base/worst. |
| D2 Value Realization Model Quality | D2.4 Time-to-value and ramp logic | I1: Value accrual curve is phased by milestone. I2: Dependencies and lead times are reflected in plan. I3: Delay-triggered replan threshold is explicit. |
| D2 Value Realization Model Quality | D2.5 Distributional value equity | I1: Benefits and burdens are segmented. I2: Net-negative segments are identified. I3: Mitigations exist for adversely impacted groups. |
| D2 Value Realization Model Quality | D2.6 Externalities and opportunity cost accounting | I1: Externalities are quantified (risk transfer, burden shift, compliance load). I2: Opportunity cost versus alternatives is estimated. I3: Stop criterion exists if realized value trails alternatives. |
| D3 Stakeholder Fit and Segment Alignment | D3.1 Stakeholder coverage completeness | I1: Stakeholder map includes users, buyers, operators, approvers, affected non-users. I2: Influence and impact ratings are assigned. I3: Critical roles have named representation in review loop. |
| D3 Stakeholder Fit and Segment Alignment | D3.2 Segmentation and priority accuracy | I1: Segments are need and behavior based, not only demographic. I2: Segment size, value potential, and risk are quantified. I3: Priority tiering has explicit criteria. |
| D3 Stakeholder Fit and Segment Alignment | D3.3 Job/workflow fit validity | I1: Core jobs/pains validated with direct evidence. I2: Current versus target workflow map exists with delta severity. I3: High-severity mismatches have mitigation owners and due dates. |
| D3 Stakeholder Fit and Segment Alignment | D3.4 Adoption friction and burden analysis | I1: Switching and learning burden estimated per segment. I2: Burden mitigation actions are scheduled and owned. I3: Pilot tracks burden outcomes, not only activity. |
| D3 Stakeholder Fit and Segment Alignment | D3.5 Accessibility, inclusion, and compliance fit | I1: Accessibility criteria tested against artifact type (web/PDF/doc/software surface). I2: Language/readability/legal obligations are verified for target audience. I3: Exceptions include approval and remediation date. |
| D3 Stakeholder Fit and Segment Alignment | D3.6 Trust and decision-governance fit | I1: Decision authorities, blockers, and veto points are mapped. I2: Privacy/security/explainability trust risks are controlled. I3: Communication cadence exists by stakeholder class. |
| D4 Solution-Need Alignment and Tradeoff Discipline | D4.1 Requirement-to-problem traceability | I1: Every requirement traces to problem frame element. I2: Orphan requirements are removed or justified. I3: Traceability matrix is version controlled. |
| D4 Solution-Need Alignment and Tradeoff Discipline | D4.2 Alternatives breadth and depth | I1: At least three distinct alternatives evaluated including do-nothing. I2: Common criteria used for all alternatives. I3: Rejection rationale is evidence-based. |
| D4 Solution-Need Alignment and Tradeoff Discipline | D4.3 Tradeoff explicitness | I1: Cost-quality-speed-risk-usability tradeoffs quantified. I2: Chosen operating point justified against thresholds. I3: Sacrificed metrics acknowledged with sign-off. |
| D4 Solution-Need Alignment and Tradeoff Discipline | D4.4 Prioritization discipline | I1: Prioritization includes value, effort, risk, urgency. I2: Top priorities explain majority of expected value. I3: Deferred items have re-entry triggers. |
| D4 Solution-Need Alignment and Tradeoff Discipline | D4.5 Dependency and ecosystem fit | I1: Critical dependencies have owner and health status. I2: Vendor/partner assumptions are validated. I3: Contingency plans exist for high-risk dependencies. |
| D4 Solution-Need Alignment and Tradeoff Discipline | D4.6 Failure mode and recovery readiness | I1: Pre-mortem identifies major failure modes. I2: Detection and recovery playbooks exist. I3: Simulation or tabletop evidence includes remediation actions. |
| D5 Adoption and Realization Feasibility | D5.1 Rollout strategy realism | I1: Pilot/scale/steady phases have entry and exit criteria. I2: Capacity assumptions by phase are quantified. I3: Rollback path is defined and tested. |
| D5 Adoption and Realization Feasibility | D5.2 Change management adequacy | I1: Sponsors, change agents, resistance map are explicit. I2: Training and communication are aligned to phase plan. I3: Adoption KPIs are defined pre-launch. |
| D5 Adoption and Realization Feasibility | D5.3 Operational capability readiness | I1: Staffing and tooling plans match expected load. I2: SOPs/runbooks complete critical paths. I3: Build-to-run handoff has acceptance sign-off. |
| D5 Adoption and Realization Feasibility | D5.4 Economic sustainability | I1: Ongoing run costs compared to realized value monthly. I2: Budget variance thresholds and owner are defined. I3: Sustainability plan exists beyond initial funding. |
| D5 Adoption and Realization Feasibility | D5.5 Support and incident response fit | I1: Support channels and SLAs are published. I2: Known-issues and workaround base is prepared. I3: Incident review cadence and owner defined. |
| D5 Adoption and Realization Feasibility | D5.6 Value capture enforcement | I1: Mechanism translating use to realized value is instrumented. I2: Value leakage points identified with controls. I3: Accountability for value capture is assigned. |
| D6 Measurement, Learning, and Governance Discipline | D6.1 Instrumentation completeness | I1: Instrumentation spans full value chain. I2: Data quality checks detect missingness and drift. I3: Collection complies with privacy/legal constraints. |
| D6 Measurement, Learning, and Governance Discipline | D6.2 Validation experiment quality | I1: Hypotheses and success thresholds pre-registered. I2: Baseline/control method explicit. I3: Sample size or power rationale documented. |
| D6 Measurement, Learning, and Governance Discipline | D6.3 Review cadence and decision latency | I1: Fixed review cadence is observed. I2: Decision lead time measured against SLA. I3: Action aging tracked and escalated. |
| D6 Measurement, Learning, and Governance Discipline | D6.4 Accountability and ownership clarity | I1: Each KPI has one accountable owner. I2: Decision rights matrix approved and current. I3: Escalation path response time tested. |
| D6 Measurement, Learning, and Governance Discipline | D6.5 Threshold-triggered governance | I1: Scale/pivot/stop thresholds explicit. I2: Threshold breach alerts are enforceable. I3: Governance response SLA monitored. |
| D6 Measurement, Learning, and Governance Discipline | D6.6 Retrospective correction discipline | I1: Post-launch reviews occur on schedule. I2: Corrective actions are prioritized and closed with evidence. I3: Lessons integrated into next planning artifacts. |

## Universal percent anchors with explicit tests

These anchors are mandatory and apply to every sub-dimension.

| Score anchor | Assignment tests |
|---|---|
| 0% | Zero indicators pass, or evidence absent, or evidence is contradictory or unverifiable. Any confirmed fabrication or backdated falsification yields 0 immediately. |
| 25% | Exactly one indicator passes with weak evidence quality. Evidence is mostly declarative and not reproducible. |
| 50% | Two indicators pass with traceability. Data exists but has weaknesses (single-source, narrow sample, stale evidence, or partial stakeholder validation). |
| 75% | All indicators pass with current and traceable evidence. At least two evidence modalities triangulate key claims (for example telemetry + interview, incident log + survey). |
| 90% | All indicators pass with independent reviewability, explicit falsification attempt, and demonstrated decision utility under real or realistic pilot conditions. |
| 100% | Meets 90% standard and remains stable across two review cycles. Independent reproduction of major claims has <= 5% unexplained variance. Corrective loop evidence is present when variance occurs. |

### Score cap and downgrade rules

1. Missing mandatory evidence caps sub-dimension at 25.
2. Evidence older than 180 days without approved rationale caps sub-dimension at 50.
3. Any unresolved high-severity risk in that sub-dimension caps at 50.
4. Any indicator with no single accountable owner caps that sub-dimension at 75.
5. If anti-gaming checks fail for that sub-dimension, cap according to anti-gaming table.

## Dimension-level strict scoring criteria

### D1 Problem Framing Integrity

| Anchor | D1 assignment criteria |
|---|---|
| 0% | Problem statement absent or conflicting without arbitration. Baseline missing or irreproducible. No accountable owner. |
| 25% | Problem statement exists but lacks measurable impact and operational boundary. Non-goals absent or cosmetic. |
| 50% | At least four D1 sub-dimensions reach >= 50. Baseline formula and source exist, but causal alternatives and harm modeling remain weak. |
| 75% | All six D1 sub-dimensions >= 50 and at least four >= 75. Boundaries, baseline, non-goals, and rollback triggers are explicit and owned. |
| 90% | All six D1 sub-dimensions >= 75 and at least three >= 90. Alternative causal explanations are tested and rejected with auditable evidence. |
| 100% | All six D1 sub-dimensions >= 90 across two cycles. Independent reviewer reproduces framing logic and baseline with <= 5% variance. |

### D2 Value Realization Model Quality

| Anchor | D2 assignment criteria |
|---|---|
| 0% | No valid value model. Claimed outcomes are not measurable or not linked to intervention. |
| 25% | Target outcomes are narrative only. KPI definitions incomplete. Lifecycle costs or guardrails omitted. |
| 50% | At least four D2 sub-dimensions >= 50. Core KPI formulas exist, but sensitivity, distributional analysis, or opportunity cost is weak. |
| 75% | All six D2 sub-dimensions >= 50 and at least four >= 75. Outcome hierarchy, cost model, and time-to-value logic are decision-ready. |
| 90% | All six D2 sub-dimensions >= 75 and at least three >= 90. Externalities and segment-level distributional effects are quantified and mitigated. |
| 100% | All six D2 sub-dimensions >= 90 across two cycles. Forecast versus realized value error remains inside pre-committed tolerance or is corrected via governed replanning. |

### D3 Stakeholder Fit and Segment Alignment

| Anchor | D3 assignment criteria |
|---|---|
| 0% | Stakeholder map absent or materially incomplete. Accessibility/compliance fit not assessed. |
| 25% | Stakeholders listed but unprioritized and weakly validated. Burden and trust dynamics unmeasured. |
| 50% | At least four D3 sub-dimensions >= 50. Segment and workflow evidence exists but is uneven and partly proxy-based. |
| 75% | All six D3 sub-dimensions >= 50 and at least four >= 75. Friction and burden are measured per segment; compliance checks are operational. |
| 90% | All six D3 sub-dimensions >= 75 and at least three >= 90. Stakeholder fit validated in realistic conditions; trust risks actively managed. |
| 100% | All six D3 sub-dimensions >= 90 across two cycles. Behavior-based adoption quality confirms fit without net-negative blind spots in critical segments. |

### D4 Solution-Need Alignment and Tradeoff Discipline

| Anchor | D4 assignment criteria |
|---|---|
| 0% | Requirements do not trace to problem frame. Alternatives absent or sham. Tradeoffs hidden. |
| 25% | Partial traceability with significant orphan scope. Prioritization is preference-driven. |
| 50% | At least four D4 sub-dimensions >= 50. Alternatives exist and are scored, but tradeoff quantification and dependency realism are weak. |
| 75% | All six D4 sub-dimensions >= 50 and at least four >= 75. Tradeoffs explicit, priorities criteria-based, failure modes and recovery paths tested. |
| 90% | All six D4 sub-dimensions >= 75 and at least three >= 90. Chosen option remains robust under sensitivity and dependency stress testing. |
| 100% | All six D4 sub-dimensions >= 90 across two cycles. Decision updates follow evidence and controlled change logs, not sponsor preference shifts. |

### D5 Adoption and Realization Feasibility

| Anchor | D5 assignment criteria |
|---|---|
| 0% | No credible rollout or operations plan. Value capture mechanism undefined. |
| 25% | Timeline exists without gate criteria, capacity assumptions, or rollback. Change plan generic. |
| 50% | At least four D5 sub-dimensions >= 50. Pilot and readiness evidence exists, but sustainability or support design remains weak. |
| 75% | All six D5 sub-dimensions >= 50 and at least four >= 75. Rollout gates, change, operations, support, and value capture are credible and owned. |
| 90% | All six D5 sub-dimensions >= 75 and at least three >= 90. Pilot demonstrates adoption quality and controlled burden with viable economics. |
| 100% | All six D5 sub-dimensions >= 90 across two cycles. Scale progression sustains value without unresolved severe operational regressions. |

### D6 Measurement, Learning, and Governance Discipline

| Anchor | D6 assignment criteria |
|---|---|
| 0% | No reliable instrumentation-governance path for decision making. |
| 25% | Metrics exist but do not represent the value chain. Review rhythm is inconsistent. |
| 50% | At least four D6 sub-dimensions >= 50. Governance structure exists but thresholds, ownership, or corrective closure are incomplete. |
| 75% | All six D6 sub-dimensions >= 50 and at least four >= 75. Cadence, thresholds, accountability, and corrective tracking are operational. |
| 90% | All six D6 sub-dimensions >= 75 and at least three >= 90. Threshold breaches trigger timely and documented action. |
| 100% | All six D6 sub-dimensions >= 90 across two cycles. Governance latency remains within SLA and retrospectives produce measurable improvement. |

## Required evidence package

No partial-credit narrative substitutions are allowed for mandatory evidence.

| Evidence ID | Required artifact | Valid evidence forms across software/doc/PDF/web | Acceptance test |
|---|---|---|---|
| E01 | Problem framing dossier | PRD section, ADR, strategy memo, product brief, PDF appendix | Contains actor, job, impact metric, baseline period, owner, version/date |
| E02 | Baseline data and lineage | Queries, telemetry extracts, logs, analytics export | Reproducible extraction and source path documented |
| E03 | Boundary and context map | Process diagram, dependency map, policy matrix | Start/end, constraints, and dependency ownership explicit |
| E04 | Stakeholder map | RACI, stakeholder register, influence-impact matrix | Includes users, approvers, operators, and affected non-users |
| E05 | Segment validation log | Interview notes, transcripts, observation artifacts, support data | Evidence per priority segment with method and timestamp |
| E06 | KPI dictionary | Metrics spec, dashboard schema, glossary | Formula, unit, cadence, owner, guardrail for each KPI |
| E07 | Benefit-cost model | Workbook, financial model, scenario model | Includes lifecycle costs and best/base/worst cases |
| E08 | Alternatives and tradeoffs | Option memo, scoring matrix, ADR chain | Includes do-nothing baseline and explicit rejection rationale |
| E09 | Prioritization ledger | Backlog scoring model, roadmap rationale | Value/effort/risk criteria with re-entry triggers for deferred scope |
| E10 | Risk and harm register | Risk matrix, harm analysis, mitigation plan | Severity, likelihood, trigger, owner, mitigation, status |
| E11 | Rollout and change plan | Phase plan, training/comms plan, readiness checklist | Entry/exit criteria, capacity assumptions, rollback route |
| E12 | Operational readiness pack | SOPs, runbooks, support model, staffing plan | Critical path runbooks and signed handoff criteria |
| E13 | Instrumentation and experiment design | Event spec, validation plan, preregistration | Hypothesis, thresholds, control/baseline method |
| E14 | Governance decision log | Meeting records, action tracker, decision register | Dated decision, accountable owner, due date, closure evidence |
| E15 | Accessibility and compliance audit | WCAG report, readability analysis, legal/privacy review | Findings severity, owner, remediation timeline, exceptions approval |
| E16 | Post-launch or pilot realization evidence | Pilot report, adoption trend, incident summaries, value report | Realized outcome versus forecast and corrective action status |

### Evidence quality thresholds

1. Freshness: <= 90 days for dynamic metrics; <= 180 days for structural artifacts.
2. Traceability: major claim must reference evidence ID and retrieval timestamp.
3. Reproducibility: at least one independent reviewer can reconstruct one primary value KPI.
4. Integrity: screenshots alone are inadmissible unless paired with source query/export.
5. Completeness: missing > 20% of required evidence is automatic fail.

## Anti-gaming controls

These checks are mandatory and scored during review. They are designed to expose inflated claims and selective evidence use.

| Control ID | Common gaming behavior | Evaluator test | Consequence if failed |
|---|---|---|---|
| AG01 | Baseline cherry-picking | Recompute baseline using alternate windows including unfavorable periods | Related sub-dimensions capped at 50 unless justified |
| AG02 | Vanity metric substitution | Map claimed KPI to actual outcome chain and verify causality | D2.2 and D6.1 capped at 25 |
| AG03 | Proxy-only stakeholder evidence | Verify direct evidence from affected roles | D3.1 and D3.3 capped at 50 |
| AG04 | Strawman alternatives | Validate realism and comparability of rejected options | D4.2 capped at 25 |
| AG05 | Burden transfer masking | Quantify shifted burden to support/ops/downstream teams | D2.6 and D5.3 capped at 50 |
| AG06 | Post-hoc threshold lowering | Compare original thresholds to reported thresholds | Invalidates period claims; cap related metrics at 25 |
| AG07 | Selective segment sampling | Inspect whether dissenting or high-friction cohorts were excluded | D3 cannot exceed 50 |
| AG08 | Evidence laundering via polished docs | Trace every major claim to raw source evidence | Untraceable claim treated as absent |
| AG09 | Survivorship bias in pilot reporting | Include churned, dropped, or failed cohorts in outcome computation | D5.1 and D5.6 capped at 50 |
| AG10 | Ownership diffusion | Check KPI ownership for single accountable owner | D6.4 indicator fails when multiple/no owners |
| AG11 | Compliance checkbox theater | Verify remediation closure beyond audit completion | Unresolved severe items trigger fail tripwire |
| AG12 | Metric reconstruction mismatch | Independently rebuild one major KPI from source logs | > 5% unexplained variance blocks 90/100 anchors |
| AG13 | Narrative objective drift | Compare initial objective to final claims and detect silent redefinition | Silent drift caps D1 and D2 at 50 |
| AG14 | Unstated denominator changes | Verify denominator consistency across reporting periods | Inconsistent denominator invalidates trend claims |
| AG15 | Delay concealment | Compare planned milestone dates to actual dates and decision logs | Hidden delays cap D2.4 and D5.1 at 50 |

## Adversarial test matrix (mandatory for rigorous evaluation)

This matrix must be executed for medium/high impact artifacts and any artifact claiming substantial value.

| Test ID | Adversarial scenario | Red-team method | Pass condition | Failure effect |
|---|---|---|---|---|
| AT01 | Baseline inflation | Recompute baseline using three alternate windows and compare effect size | Claimed uplift remains directionally valid within tolerance | D1.3 and D2.3 capped at 25 |
| AT02 | Causality illusion | Test confounders and seasonality against claimed intervention effect | Confounders addressed and causal claim remains plausible | D1.4 capped at 50 |
| AT03 | Segment cherry-pick | Include low-performance and hard-to-serve segments in value distribution | Claim includes full distribution and mitigation plan | D3 capped at 50 |
| AT04 | Alternative suppression | Add do-nothing and one external viable option into scoring | Selected option remains preferred under stated criteria | D4.2 and D4.3 capped at 50 |
| AT05 | Hidden cost exposure | Insert omitted costs (support, compliance, migration, training) | Net value remains non-negative under base case | D2.3 fail and tripwire TW06 |
| AT06 | Burden transfer reveal | Quantify externalized burden on operations and support teams | Burden acknowledged and controlled with owners | D2.6 and D5.3 capped at 50 |
| AT07 | Adoption over-forecast | Stress adoption curve to 50% of expected trajectory | Time-to-value remains viable with contingency plan | D5.1 and D5.4 capped at 50 |
| AT08 | Instrumentation blind spot | Map critical journey events to telemetry and locate gaps | Gaps are non-critical or remediated before decision use | D6.1 capped at 25 |
| AT09 | Governance latency | Simulate threshold breach and measure response against SLA | Decision and action within SLA with recorded owner | D6.3 and D6.5 capped at 50 |
| AT10 | Compliance friction test | Validate accessibility/legal requirements on actual artifact surfaces | Severe issues closed or formally excepted with dates | TW05 fail on unresolved severe issue |
| AT11 | Value leakage challenge | Trace usage-to-value conversion and identify breakpoints | Leakage measured and controlled with accountable owner | D5.6 capped at 25 |
| AT12 | Doc-product mismatch | Compare artifact claims to shipped behavior and support reality | Variance minor and corrected with dated plan | TW15 fail on material mismatch |
| AT13 | Reproducibility challenge | Independent evaluator reconstructs key claim from evidence | <= 5% unexplained variance | TW10 fail if irreproducible |
| AT14 | Harm edge-case simulation | Simulate high-risk edge case for vulnerable stakeholder | Controls activate, containment and rollback succeed | TW09 fail on control failure |
| AT15 | Objective drift detection | Diff early and latest objectives with approval trail | Objective changes are approved and re-baselined | D1 and D2 capped at 50 if silent drift |
| AT16 | Support overload scenario | Stress incident/support volume above forecast | Support model and escalation meet SLA | D5.5 capped at 50 |
| AT17 | Dependency failure scenario | Simulate top dependency outage or vendor delay | Contingency enables degraded but safe operation | D4.5 and D5.1 capped at 50 |
| AT18 | Stakeholder veto scenario | Simulate veto from high-influence stakeholder segment | Governance path resolves within documented protocol | D3.6 capped at 50 |

## Pass/fail tripwires (hard stop conditions)

Tripwires override score and force fail.

| Tripwire ID | Trigger | Result |
|---|---|---|
| TW01 | No measurable baseline for primary value claim | Immediate fail |
| TW02 | Primary KPI missing formula, owner, or lineage | Immediate fail |
| TW03 | Fabricated, falsified, or unverifiable evidence detected | Immediate fail and audit escalation |
| TW04 | Critical stakeholder class omitted without approved rationale | Immediate fail |
| TW05 | Known high-severity accessibility/compliance issue unresolved and unowned | Immediate fail |
| TW06 | Net value negative in base case after lifecycle costs | Immediate fail |
| TW07 | Do-nothing alternative absent in option analysis | Immediate fail |
| TW08 | No pre-defined scale/pivot/stop thresholds | Immediate fail |
| TW09 | High-severity harm risk lacks mitigation owner and stop condition | Immediate fail |
| TW10 | Core impact claim cannot be reproduced independently | Immediate fail |
| TW11 | Required evidence completeness below 80% | Immediate fail |
| TW12 | Critical governance actions overdue > 60 days | Immediate fail |
| TW13 | Adoption claim based only on vanity activity metrics | Immediate fail |
| TW14 | Decision authority for primary outcomes is ambiguous | Immediate fail |
| TW15 | Material mismatch between documented claims and shipped reality | Immediate fail |
| TW16 | Privacy/legal collection method violates policy for core metrics | Immediate fail |
| TW17 | Segment-level harm appears without mitigation and acceptance decision | Immediate fail |
| TW18 | Rollback criteria undefined for high-impact release | Immediate fail |

## Cross-artifact operationalization guidance

This section ensures software/doc/PDF/web artifacts are judged comparably.

### Software products

Required enforcement:
1. Trace value KPIs to event telemetry and operational logs.
2. Validate incident burden, on-call load, and support leakage.
3. Check requirement-to-problem mapping at ticket and release level.
4. Validate pilot and scale gates against production evidence.

### Documents (strategy/PRD/ADR)

Required enforcement:
1. Reject rhetorical claims lacking evidence references.
2. Require explicit alternatives and tradeoff tables.
3. Require segment evidence and burden analysis, not generic personas.
4. Validate decision rights and governance ownership fields.

### PDFs (reports, briefs, assessments)

Required enforcement:
1. Verify static charts against source data extracts.
2. Reject claims without date windows and denominator definitions.
3. Require appendix with methods and reproducibility notes.
4. Audit whether revisions silently changed objectives or thresholds.

### Web artifacts

Required enforcement:
1. Validate user-facing claims against product behavior and support documentation.
2. Enforce accessibility audits and remediation tracking.
3. Confirm policy/legal language aligns with actual data collection and use.
4. Verify conversion and burden metrics are instrumented and reviewed.

## Evaluator execution protocol

Strict sequence must be followed.

1. Intake evidence package and verify evidence IDs E01-E16.
2. Run evidence integrity checks (freshness, reproducibility, ownership).
3. Score each sub-dimension using anchor table only.
4. Apply cap/downgrade rules and anti-gaming controls.
5. Execute adversarial test matrix for relevant risk tier.
6. Compute weighted score and dimension floors.
7. Apply tripwire logic.
8. Produce verdict with mandatory remediation list if not pass.

## Risk-tier scaling for adversarial depth

| Risk tier | Typical context | Minimum adversarial tests required | Additional requirements |
|---|---|---:|---|
| Tier 1 | Low-impact internal docs with no external claims | 6 | AT01, AT02, AT04, AT08, AT13, AT15 |
| Tier 2 | Medium-impact product/policy decisions | 10 | Tier 1 tests plus AT03, AT05, AT07, AT11 |
| Tier 3 | High-impact releases, regulated or public claims | 14 | Tier 2 tests plus AT09, AT10, AT14, AT16 |
| Tier 4 | Critical-risk domains or irreversible impact | 18 | Full matrix AT01-AT18 mandatory |

## Scoring worksheet template (operational)

| Sub-dimension | Score | Evidence IDs used | Anti-gaming checks run | Notes on gaps/remediation |
|---|---:|---|---|---|
| D1.1 |  |  |  |  |
| D1.2 |  |  |  |  |
| D1.3 |  |  |  |  |
| D1.4 |  |  |  |  |
| D1.5 |  |  |  |  |
| D1.6 |  |  |  |  |
| D2.1 |  |  |  |  |
| D2.2 |  |  |  |  |
| D2.3 |  |  |  |  |
| D2.4 |  |  |  |  |
| D2.5 |  |  |  |  |
| D2.6 |  |  |  |  |
| D3.1 |  |  |  |  |
| D3.2 |  |  |  |  |
| D3.3 |  |  |  |  |
| D3.4 |  |  |  |  |
| D3.5 |  |  |  |  |
| D3.6 |  |  |  |  |
| D4.1 |  |  |  |  |
| D4.2 |  |  |  |  |
| D4.3 |  |  |  |  |
| D4.4 |  |  |  |  |
| D4.5 |  |  |  |  |
| D4.6 |  |  |  |  |
| D5.1 |  |  |  |  |
| D5.2 |  |  |  |  |
| D5.3 |  |  |  |  |
| D5.4 |  |  |  |  |
| D5.5 |  |  |  |  |
| D5.6 |  |  |  |  |
| D6.1 |  |  |  |  |
| D6.2 |  |  |  |  |
| D6.3 |  |  |  |  |
| D6.4 |  |  |  |  |
| D6.5 |  |  |  |  |
| D6.6 |  |  |  |  |

## Verdict definitions

| Verdict | Conditions |
|---|---|
| Fail | Any tripwire triggered, or one or more gate conditions fail |
| Conditional Pass | No tripwire, all gates except limited remediable gaps with owner and due date within one cycle |
| Pass | All gates satisfied, no tripwire, and remediation backlog contains only non-critical improvements |

## Calibration rules for multi-evaluator consistency

1. Use evidence IDs in every scoring note.
2. If two evaluators differ by >= 25 points on any sub-dimension, require joint evidence replay.
3. Do not average incompatible interpretations; resolve by replaying anchor tests.
4. If reproducibility disagreement persists, default to lower score.
5. Maintain a calibration log with disagreements and final rationale.

## Common failure patterns and mandatory corrective actions

| Failure pattern | Typical manifestation | Required corrective action before re-evaluation |
|---|---|---|
| Problem-solution inversion | Artifact starts with preferred solution, then back-fits problem | Rebuild D1 with independent baseline and causal alternatives |
| Outcome ambiguity | Multiple KPIs with no primary value metric | Define single primary KPI with formula/owner and guardrails |
| Stakeholder tokenism | Personas without direct validation from affected roles | Collect direct segment evidence with timestamp and method |
| Tradeoff concealment | Claimed win on all dimensions with no admitted sacrifice | Quantify tradeoffs and add signed acceptance of sacrificed metrics |
| Pilot illusion | Success claims exclude dropouts and support burden | Recompute pilot including churn, burden, and incident costs |
| Governance theater | Regular meetings but no closed actions | Establish closure SLA and enforce accountable ownership |

## Strict evaluator checklist

Use this checklist at final decision time:
1. Is the problem frame measurable, bounded, and owner-assigned?
2. Is baseline reproducible and resistant to window manipulation?
3. Is causal logic challenged by alternatives and confounders?
4. Is value model complete with lifecycle cost and opportunity cost?
5. Are stakeholder segments validated directly and comprehensively?
6. Are burdens and harms quantified and mitigated by owner?
7. Are alternatives real and scored consistently?
8. Are rollout, operations, and support viable at planned scale?
9. Are metrics instrumented, review cadence enforced, and decisions timely?
10. Do anti-gaming and adversarial tests hold under challenge?
11. Are all tripwires clear of trigger conditions?

If any answer is no, this section does not pass.

## Minimum remediation packet after fail

A failed artifact must return with:
1. Updated evidence map with changed evidence IDs and dates.
2. Corrected scoring worksheet with explicit score deltas.
3. Closed critical actions tied to prior tripwire(s).
4. Re-executed adversarial tests for affected dimensions.
5. Signed owner attestations for unresolved medium risks.

## Interpretation banding after gates

| Weighted A1 score | Interpretation |
|---|---|
| 0-49 | Non-credible: problem/value fit is materially unsound |
| 50-64 | Weak: structural gaps and decision risk remain high |
| 65-74 | Near-pass but unsafe: targeted remediation required |
| 75-89 | Pass: operationally credible with manageable residual risk |
| 90-100 | High confidence: reproducible value logic and resilient stakeholder fit |

## Final enforcement note

This section deliberately penalizes untested optimism, missing traceability, silent objective drift, and stakeholder tokenism. It rewards measurable value logic, explicit tradeoffs, validated segment fit, and governance that can withstand adversarial scrutiny. If evidence quality degrades, score must degrade.

---

# Section 2: A2
- source_file: `A2_requirements_spec.md`
- scope: Requirements Fidelity, Specification Integrity, Scope Governance
- word_count: 4823
- line_count: 177

# A2 Requirements & Spec Rubric Section

## A2.1 Scope and Enforcement
This section defines mandatory scoring for three quality domains: requirements fidelity, specification integrity, and scope governance. It applies to software products, documentation products, PDFs, and web products. The evaluator must score only evidence that is present, versioned, and auditable. Missing evidence is scored as missing quality.

This rubric is strict by design. It is intended for release gating, vendor acceptance, procurement quality checks, and audit readiness. It is not a coaching checklist. It is a decision instrument.

A2 scoring is based on five top-level dimensions with six sub-dimensions each (30 total scored units). Every sub-dimension is scored at one anchor only: `0`, `25`, `50`, `75`, `90`, or `100`.

If a sub-dimension meets conditions across multiple anchors, assign the highest anchor fully satisfied. If evidence is split or partial between anchors, assign the lower anchor.

## A2.2 Measurement Definitions
1. `Approved requirement`: A requirement in the approved baseline with stable ID, owner, and revision.
2. `Critical requirement`: Any P0/P1 requirement, legal or regulatory requirement, security requirement, privacy requirement, safety requirement, payment requirement, or contractual must-have.
3. `Trace chain`: Source -> requirement -> spec/design -> implementation artifact -> verification artifact -> release artifact.
4. `Coverage %`: `(count of items meeting test condition / total in scope) * 100`.
5. `Broken link`: Any trace link that fails to resolve to an immutable artifact revision.
6. `Orphan artifact`: Design, test, code, content section, UI path, or PDF section with no mapped requirement.
7. `Ghost requirement`: Implemented or published behavior with no approved requirement.
8. `Conflict`: Two active statements that cannot both be true under the same version and scope.
9. `SLA`: Required time to classify and resolve a conflict or change decision.
10. `Evidence`: Immutable artifact with timestamp, author, revision/hash, and reproducibility.

## A2.3 Scoring Mechanics
1. Score each sub-dimension at one anchor only: `0/25/50/75/90/100`.
2. Sub-dimension scores are evidence-based. Statements without evidence are ignored.
3. Dimension score is arithmetic mean of its six sub-dimensions.
4. A2 section score is weighted sum of dimension scores.
5. Tripwire events override numeric score and produce immediate fail.
6. Contradictions unresolved beyond SLA apply caps and may trigger fail.
7. Evidence dated after release cutoff is invalid for release-gate scoring unless waiver exists.

### Dimension Weights
| Dimension Code | Dimension Name | Weight | Minimum to Avoid Dimension Fail |
|---|---|---:|---:|
| D1 | Requirements Fidelity | 20% | 75 |
| D2 | Traceability and Coverage Integrity | 20% | 75 |
| D3 | Specification Integrity | 20% | 75 |
| D4 | Scope Governance and Change Control | 20% | 75 |
| D5 | Acceptance Alignment and Verification Readiness | 20% | 75 |

### Section Pass Rule
- `Pass` requires all conditions:
1. Overall A2 score `>= 85`.
2. Every dimension score `>= 75`.
3. Zero triggered tripwires.
4. Zero Severity-1 unresolved contradictions past SLA.
5. Evidence completeness for critical requirements `= 100%`.

---

## A2.4 Master Operational Scoring Matrix (Dimension -> Sub-dimension -> Indicators)

| Code | Dimension | Sub-dimension | Indicators (Operational and Measurable) | 0% Anchor Test | 25% Anchor Test | 50% Anchor Test | 75% Anchor Test | 90% Anchor Test | 100% Anchor Test | Required Evidence | Anti-gaming Checks | Pass/Fail Tripwire |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1.1 | Requirements Fidelity | Source Baseline Control | Linked requirements with source clause+version; baseline freeze quality; unresolved source conflicts aging | No approved source register or linked requirements <40% | Register exists but mutable; linked 40-59%; unresolved conflicts >10 | Approved register; linked 60-79%; unresolved conflicts <=10 | Signed frozen baseline; linked 80-94%; unresolved conflicts <=3 | Immutable hash baseline; linked 95-99%; conflicts closed <=5 business days | Linked 100%; immutable reproducible source pack; unresolved conflicts 0 | Source register, baseline freeze record, hash manifest, conflict log | Sample max(15, 15% of requirements); verify links and hashes against repository history | Any critical requirement lacks authoritative source linkage |
| D1.2 | Requirements Fidelity | Requirement Atomicity and Testability | Single-behavior requirements; measurable acceptance thresholds; ambiguous modal language rate | Atomic and testable requirements <40% | Atomic and testable 40-59%; ambiguous wording >20% | Atomic and testable 60-79%; ambiguous wording 10-20% | Atomic and testable 80-94%; ambiguous wording <10% | Atomic and testable 95-99%; ambiguous wording <3% | Atomic and testable 100%; ambiguous wording 0% | Requirement catalog, language lint report, acceptance criteria set | Run automatic ambiguity linter plus manual sample of 20 critical requirements | More than 2 critical requirements are non-testable |
| D1.3 | Requirements Fidelity | Stakeholder Intent Capture | Requirements with owner role; stakeholder class completeness; sign-off coverage and conflict closure | Stakeholder map absent or owner mapping <40% | Partial map; owner mapping 40-59%; no active conflict workflow | Primary classes mapped; owner mapping 60-79%; conflict log exists | All mandatory classes mapped; owner mapping 80-94%; conflict triage active | Owner mapping 95-99%; required sign-offs present; conflicts closed <=5 business days | Owner mapping 100%; all required sign-offs; unresolved intent conflicts 0 | Stakeholder map, ownership matrix, sign-off records, intent conflict log | Validate unique signer identity and timestamp order; reject same-minute bulk backfills | Missing sign-off from required authority class (product, security, legal, compliance as applicable) |
| D1.4 | Requirements Fidelity | Functional Requirement Fidelity | Implemented behaviors mapped to approved requirements; unauthorized behavior count; deviation approval quality | Mapped implemented behaviors <40% or unauthorized behaviors >10 | Mapped 40-59%; unauthorized behaviors 6-10 | Mapped 60-79%; unauthorized behaviors 3-5 | Mapped 80-94%; unauthorized behaviors <=2 and tracked | Mapped 95-99%; unauthorized behaviors <=1 and formally approved | Mapped 100%; unauthorized behaviors 0 | Behavior-to-requirement mapping, release notes, deviation approvals | Reverse-audit random shipped feature sample; require requirement ID for each | Any high-impact behavior shipped without approved requirement |
| D1.5 | Requirements Fidelity | Non-Functional Requirement Fidelity | Mandatory NFRs quantified; NFR verification coverage; NFR pass rate and waivers | Quantified and testable mandatory NFRs <40% | Quantified mandatory NFRs 40-59%; executed NFR tests <40% | Quantified 60-79%; executed NFR tests 60-79% | Quantified 80-94%; executed tests 80-94%; waivers recorded | Quantified 95-99%; executed tests 95-99%; pass rate >=95% | Quantified 100%; executed tests 100%; mandatory NFR pass 100% or approved waiver | NFR catalog, test plans, test results, waiver register | Re-run a subset of NFR tests under same environment; compare with submitted results | Any mandatory NFR is unquantified or fails without approved waiver |
| D1.6 | Requirements Fidelity | Regulatory and Policy Fidelity | Mandatory controls mapped to requirements and tests; audit finding status; control evidence completeness | Mandatory controls mapped <40% | Controls mapped 40-59%; evidence linkage weak | Controls mapped 60-79%; evidence coverage >=60% | Controls mapped 80-94%; evidence coverage >=80%; open findings <=5 | Controls mapped 95-99%; open findings <=1 minor | Controls mapped 100%; open findings 0 | Control matrix, policy mapping, compliance test evidence, finding log | Cross-check control IDs with current policy version; detect obsolete references | Any mandatory control unmapped or open failed control at release |
| D2.1 | Traceability and Coverage Integrity | End-to-End Traceability Chain | Requirements with complete chain Source->Req->Spec->Build->Test->Release | Complete chains <40% | Complete chains 40-59% | Complete chains 60-79% | Complete chains 80-94% | Complete chains 95-99%; automated nightly validation | Complete chains 100%; broken chain count 0 | Trace matrix export, link validator report, release manifest | Independent run of link validator on frozen baseline | Any critical requirement missing any chain stage |
| D2.2 | Traceability and Coverage Integrity | Bidirectional Link Validity | Reciprocal forward/back links; broken link rate; stale link rate | Reciprocal links <40% or broken links >20% | Reciprocal links 40-59%; broken links 11-20% | Reciprocal links 60-79%; broken links 6-10% | Reciprocal links 80-94%; broken links <=5% | Reciprocal links 95-99%; broken links <=1% | Reciprocal links 100%; broken links 0% | Link integrity report, artifact index, versioned references | Randomly traverse 25 links both directions from release claims | Any release claim cannot be traversed backward to approved requirement |
| D2.3 | Traceability and Coverage Integrity | Orphan and Ghost Artifact Elimination | Orphan artifact rate; ghost requirement count; closure latency for orphan/ghost defects | Orphan or ghost artifacts >20% | Orphan or ghost artifacts 11-20% | Orphan or ghost artifacts 6-10% | Orphan or ghost artifacts 2-5% | Orphan or ghost artifacts 1% | Orphan or ghost artifacts 0% | Orphan/ghost report, remediation tickets, closure evidence | Scan repo/content/test suite for items lacking requirement IDs; verify false positive rate <5% | Any ghost requirement is implemented or published |
| D2.4 | Traceability and Coverage Integrity | Coverage Completeness by Requirement Class | Coverage across classes: functional, security, privacy, accessibility, performance, legal, content accuracy | Covered classes <40% | Covered classes 40-59% | Covered classes 60-79% | Covered classes 80-94% | Covered classes 95-99%; critical classes each >=95% | Covered classes 100%; each requirement has at least one validating artifact | Coverage matrix by class, critical class checklist, verification records | Enforce class tagging at requirement creation; audit tag drift monthly | Any mandatory class coverage <90% |
| D2.5 | Traceability and Coverage Integrity | Version-Aligned Traceability | Links referencing same approved baseline; mismatch count; mismatch resolution time | Version-aligned links <40% | Version-aligned links 40-59%; mismatches >20 | Version-aligned links 60-79%; mismatches 10-20 | Version-aligned links 80-94%; mismatches <=9 | Version-aligned links 95-99%; mismatches <=1 and closed <=2 days | Version-aligned links 100%; mismatch count 0 | Baseline manifest, link version report, mismatch ticket log | Recompute version alignment from raw IDs, not dashboard rollups | Any critical chain uses obsolete spec version in release baseline |
| D2.6 | Traceability and Coverage Integrity | Dependency and External Interface Mapping | External dependencies/interfaces mapped to requirements, risk class, owner, SLA, fallback | Mapping coverage <40% | Mapping coverage 40-59% | Mapping coverage 60-79% | Mapping coverage 80-94% | Mapping coverage 95-99%; risk class complete | Mapping coverage 100%; critical dependencies include failover or exit criteria | Dependency register, interface catalog, owner matrix, SLA docs, risk register | Verify dependency inventory against runtime/package scan and published docs | Any critical external dependency lacks owner, SLA, or risk class |
| D3.1 | Specification Integrity | Terminology and Glossary Integrity | Critical terms uniquely defined; definition-reference coverage; duplicate definition count | Glossary absent or unique definitions <40% | Unique definitions 40-59%; conflicting definitions >10 | Unique definitions 60-79%; conflicting definitions 5-10 | Unique definitions 80-94%; conflicting definitions <=4 | Unique definitions 95-99%; conflicting definitions <=1 | Unique definitions 100%; conflicting definitions 0 | Glossary, term usage index, conflict resolution log | Use term extractor and detect same term with conflicting constraints | Any legal or safety term has multiple active definitions |
| D3.2 | Specification Integrity | Cross-Section Consistency | Contradiction count across sections and artifacts; closure velocity; severity mix | Unresolved contradictions >20 | Unresolved contradictions 11-20 | Unresolved contradictions 6-10 | Unresolved contradictions 2-5 | Unresolved contradictions 1 minor only | Unresolved contradictions 0 | Consistency check report, contradiction log, resolution approvals | Run pairwise contradiction checks on numeric limits, states, and shall statements | Any unresolved contradiction between active shall/must statements |
| D3.3 | Specification Integrity | Interface and Contract Precision | API/interface contracts include schema version, field constraints, error semantics, examples | Fully specified contracts <40% | Fully specified contracts 40-59% | Fully specified contracts 60-79% | Fully specified contracts 80-94% | Fully specified contracts 95-99%; backward compatibility rules defined | Fully specified contracts 100%; schema lint and contract tests pass | Interface specs, schema files, contract tests, compatibility policy | Validate examples against schema; reject hand-edited examples that fail parsing | Any production interface lacks schema version or mandatory constraints |
| D3.4 | Specification Integrity | Data Model Integrity | Entities include keys, cardinality, lifecycle state, retention, access class, lineage | Complete entities <40% | Complete entities 40-59% | Complete entities 60-79% | Complete entities 80-94% | Complete entities 95-99%; lineage complete for critical entities | Complete entities 100%; model validation scripts pass with 0 critical issues | Data dictionary, ER/UML model, retention matrix, access matrix, lineage map | Compare declared data model against actual storage schema and API payloads | Any PII or regulated field lacks classification, retention, or access rule |
| D3.5 | Specification Integrity | Ambiguity and Contradiction Elimination | Ambiguous terms per 100 requirements; unresolved ambiguity age; quantification ratio | Ambiguous terms >20 per 100 requirements | Ambiguous terms 11-20 per 100 | Ambiguous terms 6-10 per 100 | Ambiguous terms 2-5 per 100 | Ambiguous terms 1 per 100 | Ambiguous terms 0 per 100 | Ambiguity lint report, rewrite log, quantified thresholds list | Spot-check 30 requirements for vague terms fast/easy/soon/etc without numbers | Any critical requirement contains unquantified vague qualifier |
| D3.6 | Specification Integrity | Feasibility and Constraint Realism | Requirements validated against capacity, legal, physical, budget, and schedule constraints | Validated requirements <40% or infeasible items >10 | Validated 40-59%; infeasible items 6-10 | Validated 60-79%; infeasible items 3-5 | Validated 80-94%; infeasible items <=2 with mitigation | Validated 95-99%; infeasible items <=1 with approved exception | Validated 100%; infeasible items 0 | Capacity model, cost model, schedule critical path, legal constraint checks, exception approvals | Recalculate estimates from source assumptions; flag copied estimates without model inputs | Any must-have requirement violates hard legal or physical constraint without waiver |
| D4.1 | Scope Governance and Change Control | Scope Boundary Definition | In-scope and out-of-scope clarity; boundary tags on artifacts; signed boundary statement | Boundary definition absent or tagged items <40% | Boundary tagging 40-59%; out-of-scope list incomplete | Boundary tagging 60-79%; partial signed boundaries | Boundary tagging 80-94%; signed boundary statement exists | Boundary tagging 95-99%; boundary checklist enforced in reviews | Boundary tagging 100%; signed boundaries and checklist compliance 100% | Scope statement, tagged backlog/spec index, signed boundary approval | Sample 20 random items and verify scope tags match approved boundary | No approved out-of-scope list for release baseline |
| D4.2 | Scope Governance and Change Control | Change Request Quality | Implemented changes with complete approved CR: reason, delta, impact, owner, approvals | Valid complete CR coverage <40% | Valid complete CR coverage 40-59% | Valid complete CR coverage 60-79% | Valid complete CR coverage 80-94% | Valid complete CR coverage 95-99%; median approval <=5 business days | Valid complete CR coverage 100%; all approvals pre-implementation | CR register, approval records, implementation references, timestamps | Compare implementation timestamps vs CR approval timestamps for sequence integrity | Any implemented scope change has no approved CR ID |
| D4.3 | Scope Governance and Change Control | Impact Analysis Rigor | CRs with quantified impact on schedule, cost, risk, compliance, and verification | Quantified impact analyses <40% | Quantified analyses 40-59% | Quantified analyses 60-79% | Quantified analyses 80-94% | Quantified analyses 95-99%; post-change variance tracked | Quantified analyses 100%; variance within +-10% for >=90% CRs | Impact assessments, variance reports, risk delta logs, updated plans | Recompute sample impact analysis from raw assumptions and compare to submitted deltas | Any high-impact CR approved without quantified impact analysis |
| D4.4 | Scope Governance and Change Control | Decision Log and Approval Chain | Scope decisions logged with decision owner, authority role, rationale, and timestamp | Logged decisions <40% | Logged decisions 40-59% | Logged decisions 60-79% | Logged decisions 80-94% | Logged decisions 95-99%; authority matrix compliance 100% | Logged decisions 100%; immutable audit trail and no missing owners | Decision log, authority matrix, approval signatures, audit trail export | Verify approver roles against authority matrix and HR/org roster | Any scope decision lacks accountable approver role |
| D4.5 | Scope Governance and Change Control | Scope Creep Detection and Containment | Unauthorized scope growth vs baseline; detection latency; closure rate | Unauthorized growth >20% or no detection controls | Unauthorized growth 11-20% or detection latency >14 days | Unauthorized growth 6-10% or detection latency 8-14 days | Unauthorized growth 3-5% and detection <=7 days | Unauthorized growth 1-2% and detection <=3 days | Unauthorized growth 0% and detection <=1 day | Baseline snapshots, growth trend report, creep alerts, remediation records | Compare baseline scope count vs delivered count with CR filter to detect hidden growth | Any unapproved scope item shipped in release |
| D4.6 | Scope Governance and Change Control | De-scope Governance and Debt Disclosure | Descoped items with rationale, stakeholder impact, debt ticket, owner, due date | Documented descopes <40% | Documented descopes 40-59% | Documented descopes 60-79% | Documented descopes 80-94% | Documented descopes 95-99%; owners and due dates complete | Documented descopes 100%; accepted by affected stakeholders | De-scope register, debt backlog, stakeholder impact approvals, recovery plan | Track descoped items against later release plans to prevent silent drops | Mandatory requirement descoped without risk acceptance sign-off |
| D5.1 | Acceptance Alignment and Verification Readiness | Acceptance Criteria Quality | Requirements with measurable acceptance criteria including tolerance and boundary conditions | Measurable criteria coverage <40% | Coverage 40-59% | Coverage 60-79% | Coverage 80-94% | Coverage 95-99%; critical items include edge conditions | Coverage 100%; all criteria measurable with explicit tolerances | Acceptance criteria catalog, requirement IDs, boundary condition set | Reject criteria using subjective terms only; enforce numeric or binary pass condition | Any critical requirement missing measurable acceptance criteria |
| D5.2 | Acceptance Alignment and Verification Readiness | Requirement-to-Test Mapping | Requirements mapped to test cases; critical requirements with positive and negative tests | Test mapping coverage <40% | Coverage 40-59% | Coverage 60-79% | Coverage 80-94% | Coverage 95-99%; critical req positive/negative coverage >=95% | Coverage 100%; all critical req have positive, negative, and error-path tests | Test trace matrix, test suite index, critical requirement coverage report | Execute random sample tests to verify they assert stated requirement criteria | Any critical requirement has no verifying test |
| D5.3 | Acceptance Alignment and Verification Readiness | Definition of Done Alignment | Completed items satisfying mandatory DoD checklist elements | DoD compliance <40% | DoD compliance 40-59% | DoD compliance 60-79% | DoD compliance 80-94% | DoD compliance 95-99%; mandatory checks automated where possible | DoD compliance 100%; mandatory override count 0 | DoD checklist logs, workflow status records, gate automation report | Audit done-state transitions for manual overrides and missing artifacts | Any released item marked done with unmet mandatory DoD criterion |
| D5.4 | Acceptance Alignment and Verification Readiness | Evidence Readiness and Audit Package | Completion claims supported by immutable, reproducible evidence packages | Evidence-backed claims <40% | Evidence-backed claims 40-59% | Evidence-backed claims 60-79% | Evidence-backed claims 80-94% | Evidence-backed claims 95-99%; provenance hashes present | Evidence-backed claims 100%; independent auditor reproduces claims | Evidence index, hashes, reproducibility scripts, audit package manifest | Replay evidence generation for sample claims; detect post-facto edits | Any critical completion claim lacks verifiable evidence artifact |
| D5.5 | Acceptance Alignment and Verification Readiness | Residual Risk Acceptance | Open risks with owner, severity, decision, expiry; waiver hygiene | Risks with full disposition <40% | Risks with full disposition 40-59% | Risks with full disposition 60-79% | Risks with full disposition 80-94% | Risks with full disposition 95-99%; no overdue critical reviews | Risks with full disposition 100%; expired waivers 0 | Risk register, acceptance decisions, waiver expiries, owner attestations | Validate approver authority and verify no blanket evergreen waivers | Any critical open risk lacks named approver and expiry date |
| D5.6 | Acceptance Alignment and Verification Readiness | Release Gate and Fairness Compliance | Mandatory gates passed: security, privacy, accessibility, performance, legal, documentation, and fairness/disparity governance; explicit disparity thresholds, mitigation SLA, and waiver authority present | Mandatory gates passed <40% or fairness controls absent | Mandatory gates passed 40-59%; fairness metrics listed with no thresholds/authority | Mandatory gates passed 60-79%; thresholds defined but mitigation/waiver governance incomplete | Mandatory gates passed 80-94%; fairness threshold breaches logged and triaged within SLA | Mandatory gates passed 95-99%; fairness waivers documented with authority chain and expiry | Mandatory gates passed 100%; critical gate waivers 0; unresolved critical fairness breaches 0 | Gate results, fairness threshold register, mitigation log, waiver log, sign-off package, release checklist | Independently rerun critical gate checks and fairness slice audits on release candidate | Release promoted with failed mandatory gate, unresolved critical fairness breach, or invalid waiver |

---

## A2.5 Contradiction-Resolution Protocol (Mandatory)

All detected contradictions must be logged, classified, and resolved using this protocol. Failure to follow this protocol is scored as specification and governance failure, even when product output appears functional.

| Protocol ID | Conflict Pattern | Detection Trigger (Measurable) | Precedence Rule | Decision Authority | Resolution SLA | Required Evidence | Scoring/Tripwire Impact |
|---|---|---|---|---|---|---|---|
| CR-01 | Regulatory or legal obligation vs product request | Requirement states behavior that violates current law/regulation/policy citation | Law/regulation/policy always overrides product preference | Compliance lead + legal approver | Classify in 1 business day; resolve in 5 business days | Conflict ticket with legal citation, decision log, updated requirement text | Related sub-dimensions capped at 50 until resolved; unresolved past SLA triggers fail |
| CR-02 | Contract/SOW commitment vs internal requirement | Internal artifact conflicts with active customer contract clause | Signed contract/SOW overrides internal draft unless contract amendment approved | Commercial owner + legal + product owner | Classify in 2 business days; resolve in 7 business days | Contract clause reference, amendment record if any, trace updates | D1.1 and D4.2 capped at 50 until corrected |
| CR-03 | Approved baseline vs draft/newer unofficial text | Two versions exist and draft is used without approval | Approved baseline wins until formal change approval | Configuration manager + approver per authority matrix | Classify in 1 business day; resolve in 3 business days | Baseline hash record, CR approval, replaced references | D2.5 immediate cap at 25 if release uses unofficial draft |
| CR-04 | Functional requirement vs security/privacy NFR | Functional target conflicts with security/privacy minimum control | Security/privacy minimum controls override unless explicit risk acceptance | Security lead + privacy officer + product owner | Classify in 1 business day; resolve in 5 business days | Risk assessment, compensating controls, acceptance decision with expiry | If unresolved at release cutoff, release gate tripwire triggers fail |
| CR-05 | Stakeholder intent conflict across authority classes | Required signers provide incompatible mandatory statements | Authority matrix priority applies; tie requires steering decision | Program steering authority named in governance charter | Classify in 2 business days; resolve in 10 business days | Signed conflict statement, authority matrix excerpt, final ruling | D1.3 capped at 50 while unresolved |
| CR-06 | Requirement text vs test evidence mismatch | Test passes but requirement says fail condition or inverse condition | Requirement semantics and approved acceptance criteria control test interpretation | QA lead + requirement owner | Classify in 1 business day; resolve in 5 business days | Requirement revision, corrected tests, rerun evidence | D5.2 cannot exceed 75 until retest evidence is complete |
| CR-07 | Cross-artifact numeric contradiction | Different numeric limits for same metric across spec/doc/web/help/PDF | Most recently approved authoritative artifact wins; others must synchronize | Artifact owners + configuration manager | Classify in 1 business day; resolve in 3 business days | Contradiction diff, synchronization commit IDs, review approval | D3.2 capped at 50 while active contradiction exists |
| CR-08 | Scope increase request vs locked delivery constraints | New feature added without time/cost/resource offset | Scope-cost-schedule triangle must balance; no silent quality reduction allowed | Program manager + product owner + engineering lead | Classify in 1 business day; resolve in 5 business days | Impact analysis, approved CR, updated baseline plan | D4.5 tripwire if unapproved scope enters release |
| CR-09 | De-scope request vs mandatory control or contractual must-have | De-scope candidate contains mandatory legal/security/contract item | Mandatory obligations cannot be descoped without approved substitute and legal sign-off | Compliance lead + legal + product owner | Classify in 1 business day; resolve in 5 business days | Substitute control evidence, legal approval, trace updates | D4.6 tripwire if de-scope proceeds without approvals |
| CR-10 | Evidence timestamp contradiction | Claimed completion date predates evidence creation or approval dates | Chronological integrity required: approval before implementation before release | Release manager + audit owner | Classify in 1 business day; resolve in 2 business days | Immutable timestamps, CI logs, approval records | D5.4 set to 0 for affected claims; repeated offense triggers fail |
| CR-11 | Version mismatch in external dependencies | Dependency version in runtime differs from approved spec/baseline | Approved dependency baseline controls; runtime must match or approved exception exists | Architecture owner + security owner | Classify in 1 business day; resolve in 3 business days | Dependency scan report, exception approval, updated baseline | D2.6 capped at 50 until corrected |
| CR-12 | Unresolved contradiction aging | Any Severity-1 contradiction remains open beyond SLA | Aging rule override: unresolved Severity-1 is automatic release block | Program accountable executive | Immediate escalation at SLA breach | Aging dashboard, escalation records, final disposition | Immediate overall fail until contradiction closure evidence exists |

### Contradiction Severity Classes
1. `Severity-1`: legal/security/safety/financial integrity or release-gate contradiction.
2. `Severity-2`: functional, performance, accessibility, data integrity contradiction.
3. `Severity-3`: wording, style, non-normative reference inconsistency.

### Mandatory Protocol Timers
1. Detection-to-log time must be `<= 1 business day` for Severity-1.
2. Severity-1 must be resolved or explicitly blocked within protocol SLA.
3. SLA breach for Severity-1 is an immediate release block and section fail.

---

## A2.6 Global Anti-Gaming Controls
1. Randomized secondary audit of at least `20%` of sub-dimensions and `15%` of critical requirements per release.
2. Evidence authenticity checks must include hash verification and immutable timestamp verification.
3. Dashboard screenshots without raw artifacts are inadmissible.
4. Synthetic mapping inflation is prohibited: each trace link must resolve to unique, valid artifact IDs.
5. Bulk same-minute approvals for large batches require manual investigation.
6. Any manual data correction in scoring sheets must carry approver, reason, and before/after value.
7. Sampling bias control: auditor must sample from each requirement class and each critical workflow.
8. Duplicate language reuse detection: near-identical requirements with different IDs are flagged for deduplication.
9. Backfilled sign-offs after release cutoff do not count for release scoring.
10. Any proven evidence fabrication sets affected sub-dimensions to `0` and triggers overall fail.

---

## A2.7 Required Evidence Pack (Minimum)
The evaluator must require this package before scoring starts. Missing package items are scored as absent evidence, not deferred.

| Evidence Category | Software Product Examples | Documentation/PDF/Web Examples | Minimum Acceptance Condition |
|---|---|---|---|
| Authoritative sources | PRD/SOW/regulatory baseline with hashes | Policy docs, source references, approved content baseline | Every source has version ID and immutable locator |
| Requirement catalog | Backlog/requirements DB export with IDs and owners | Requirements table in spec/doc set with IDs and owners | ID uniqueness 100%; owner field populated 100% |
| Traceability matrix | Source->req->design->code->test->release links | Source->req->section/page->validation links | Critical chain completeness 100% |
| Change governance records | CR tickets, approvals, impact analyses | Revision logs, redlines, approval memos | Every scope delta has approved CR or revision decision |
| Verification evidence | CI tests, NFR test runs, gate reports | Review checklists, fact checks, accessibility checks, validation logs | Evidence is reproducible and timestamped |
| Risk and exception records | Risk register, waivers, expiry dates | Content/legal risk log, waivers, expiry dates | No critical risk without named approver and expiry |
| Release or publish package | Release checklist, gate approvals, manifests | Publish checklist, sign-off package, artifact hashes | Mandatory gates passed or documented waivers |

---

## A2.8 Hard Tripwire Summary
Any one of the following causes immediate section fail regardless of numeric score.

1. Any critical requirement lacks authoritative source mapping.
2. Any critical requirement is non-testable.
3. Any mandatory control is unmapped or failed at release.
4. Any critical requirement lacks end-to-end trace chain.
5. Any high-impact behavior ships without approved requirement.
6. Any unapproved scope change is shipped.
7. Any mandatory requirement is descoped without approved risk acceptance.
8. Any critical requirement lacks measurable acceptance criteria.
9. Any critical requirement has no verifying test.
10. Release promoted with failed mandatory gate and no signed waiver.
11. Any Severity-1 contradiction unresolved past SLA.
12. Evidence chronology contradiction not resolved before release cutoff.

---

## A2.9 Score Interpretation Bands
| Final A2 Score | Classification | Enforcement Action |
|---:|---|---|
| 0-49 | Non-compliant | Reject artifact; mandatory remediation and full re-evaluation |
| 50-74 | Conditionally deficient | Block release/publish; corrective action plan required |
| 75-84 | Marginal pass | Limited acceptance only with approved remediation plan and deadline |
| 85-94 | Pass | Acceptable for release/publish if no tripwires |
| 95-100 | High assurance pass | Accept; retain as audit exemplar |

This concludes the A2 section for Requirements Fidelity, Specification Integrity, and Scope Governance.

---

# Section 3: A3
- source_file: `A3_correctness_verification.md`
- scope: Technical/Domain Correctness, Verification Rigor
- word_count: 4786
- line_count: 360

# A3 Correctness & Verification Rubric Section

## 1) Scope and Governing Intent
This section defines an enforcement-grade rubric for evaluating three tightly coupled quality properties across software, documentation, PDF, and web artifacts:
1. Technical correctness.
2. Domain and factual correctness.
3. Verification rigor.

The evaluator must treat this rubric as adversarial by default. The burden of proof is on the artifact owner. Assertions are not accepted without verifiable evidence. Tests are not accepted without falsifiable oracles. Claimed passes are not accepted unless independently replayable.

The rubric is designed to prevent false confidence caused by polished presentation, selective testing, incomplete citations, or non-reproducible pipelines. This section is intentionally strict and should be applied as written.

## 2) Evaluation Model
### 2.1 Top-Level Dimension Weights
| Dimension ID | Dimension | Weight |
|---|---|---:|
| D1 | Technical Specification Conformance | 22% |
| D2 | Domain and Factual Correctness | 20% |
| D3 | Verification Design and Coverage | 18% |
| D4 | Evidence Integrity and Auditability | 14% |
| D5 | Independent Replay and Recomputation Rigor | 16% |
| D6 | Corrective Action and Regression Governance | 10% |
|  | **Total** | **100%** |

Default sub-dimension weighting is equal inside each dimension unless a pre-declared program governance document specifies otherwise.

### 2.2 Non-Negotiable Principles
1. A score above 75 requires successful independent replay.
2. A score above 90 requires cross-environment replay and independent recomputation with no unresolved severe defects.
3. A score of 100 requires dual independent witness replay and perfect evidence completeness.
4. Any evidence fabrication, source invention, or log tampering sets the overall score to 0.

### 2.3 Core Metrics Definitions
| Metric | Definition | Required data source |
|---|---|---|
| `TRC` | Traceability Coverage = traced normative requirements / total normative requirements | Requirement inventory + trace matrix |
| `CRP` | Critical Requirement Pass = passed critical requirement tests / total critical requirement tests | Test report mapped to requirement IDs |
| `FCV` | Factual Claim Verification = verified material claims / total material claims | Claim ledger + citation map |
| `RCM` | Recomputation Match = key recomputed values matching published values / total recomputed key values | Recompute scripts/workbooks + raw inputs |
| `IRS` | Independent Replay Success = successful independent replays / required independent replays | Witness replay logs |
| `MKR` | Mutation Kill Rate = killed mutants / total non-equivalent mutants | Mutation test report |
| `EIC` | Evidence Integrity & Completeness = valid required evidence items / required evidence items | Evidence manifest + hashes |
| `OSD` | Open Severe Defects = count of unresolved critical/high defects | Defect tracker snapshot |

## 3) Global Anchor Scale With Explicit Tests (0/25/50/75/90/100)
Evaluators must assign the highest anchor where **all tests at that anchor pass** and no tripwire overrides apply.

| Anchor | Explicit mandatory thresholds | Replay requirement | Defect gate |
|---:|---|---|---|
| **0** | Any of: `EIC < 0.30`, critical evidence unverifiable, fabricated claim/source detected, replay impossible | None | Not applicable |
| **25** | Any of: `TRC < 0.40`, `CRP < 0.60`, `FCV < 0.50`, `EIC < 0.60` | At most author-only rerun | Critical defects may exist |
| **50** | `TRC >= 0.60`, `CRP >= 0.75`, `FCV >= 0.70`, `RCM >= 0.85`, `IRS >= 0.50`, `MKR >= 0.45`, `EIC >= 0.75` | One independent replay succeeds | Critical=0, High<=5 |
| **75** | `TRC >= 0.85`, `CRP >= 0.90`, `FCV >= 0.85`, `RCM >= 0.95`, `IRS >= 0.80`, `MKR >= 0.65`, `EIC >= 0.90` | At least two independent replay runs succeed | Critical=0, High<=2 |
| **90** | `TRC >= 0.95`, `CRP >= 0.97`, `FCV >= 0.95`, `RCM >= 0.99`, `IRS >= 0.95`, `MKR >= 0.80`, `EIC >= 0.97` | Cross-environment replay successful with equivalent conclusions | Critical=0, High=0 |
| **100** | `TRC=1.00`, `CRP=1.00`, `FCV=1.00`, `RCM=1.00`, `IRS=1.00`, `EIC=1.00`, `MKR>=0.90` | Two independent teams replay from cold start and match outputs within declared tolerances | Critical=0, High=0 for two consecutive evaluation cycles |

## 4) Dimension Hierarchy: Dimension -> Sub-dimension -> Indicators (Primary Operational Table)

### D1) Technical Specification Conformance (22%)
| Sub-dimension ID | Sub-dimension | Indicators (operational tests) | Evidence requirements | Anti-gaming checks | Tripwire failures |
|---|---|---|---|---|---|
| D1.1 | Requirement-to-behavior fidelity | `TRC >= target`; each normative requirement has at least one behavior assertion; each changed requirement has same-change-set test updates | Requirement register, trace matrix, commit links | Sample 10% of user-visible statements for missing requirement IDs | Any critical requirement untraced |
| D1.2 | Algorithmic/output correctness | Golden dataset pass rate >=99%; invariant/property checks pass; edge numerical tolerances met | Golden fixtures, oracle definitions, baseline outputs with hashes | Hidden holdout dataset and alternate algorithm spot-check | Critical output mismatch in required scenario |
| D1.3 | Contract/schema integrity | API/schema conformance pass rate 100% for mandatory interfaces; backward compatibility for stable contracts | OpenAPI/schema files, contract tests, compatibility matrix | Previous-client replay suite; random field omission/injection | Breaking change without versioning policy compliance |
| D1.4 | Boundary and error handling correctness | Boundary classes tested (min/max/null/empty/overflow); documented error modes returned; no uncaught critical exceptions | Negative tests, error map, exception logs | Fuzz malformed payloads and boundary storms | Crash/hang/undefined state in critical flow |
| D1.5 | State transition and data integrity | State invariants hold pre/post operations; transaction atomicity and rollback verified; migration correctness checks | Invariant tests, transaction logs, migration replay results | Fault injection during commit/rollback and concurrency writes | Data corruption, silent truncation, lost updates |
| D1.6 | Determinism/idempotence/concurrency safety | Repeated runs equivalent within tolerance; idempotent endpoints remain idempotent after retries; concurrency stress passes | Seed logs, idempotence tests, stress reports | Seed sweep and scheduler perturbation challenge | Undeclared nondeterminism affecting critical outputs |

### D2) Domain and Factual Correctness (20%)
| Sub-dimension ID | Sub-dimension | Indicators (operational tests) | Evidence requirements | Anti-gaming checks | Tripwire failures |
|---|---|---|---|---|---|
| D2.1 | Material claim inventory completeness | 100% of material claims listed and classified (normative/quantitative/temporal/interpretive) | Claim ledger with claim IDs and artifact locations | Independent blind claim extraction and ledger delta test | Missing high-impact material claim |
| D2.2 | Source authority and hierarchy discipline | Critical claims use primary/authoritative sources; policy compliance >=95% | Source registry with authority rank and retrieval metadata | Remove weak sources and retest support sufficiency | Critical claim based only on weak/unverifiable source |
| D2.3 | Claim-citation binding accuracy | Citation mismatch <=2%; each claim points to precise source locator | Citation map with anchors/page/section URLs, archived source snapshots | Random 20-claim blind audit | Missing or wrong citation for critical claim |
| D2.4 | Quantitative and unit correctness | Key numbers recomputable 100%; unit conversion checks pass; rounding policy consistency | Recompute scripts/workbooks, raw inputs, unit dictionary | Independent recomputation with alternate toolchain | Arithmetic or unit error altering material conclusion |
| D2.5 | Temporal/version/legal validity | Time-sensitive claims carry effective date/version; stale-source control in place | Timestamped sources, version manifest, legal applicability notes | Time-shift revalidation (baseline date vs evaluation date) | Use of superseded rule/standard causing wrong conclusion |
| D2.6 | Cross-source contradiction handling | Contradictions logged, adjudicated, and resolved for critical claims | Contradiction register, adjudication rationale, reviewer signoff | Inject known contradictory source and verify detection | Hidden unresolved contradiction affecting material claim |

### D3) Verification Design and Coverage (18%)
| Sub-dimension ID | Sub-dimension | Indicators (operational tests) | Evidence requirements | Anti-gaming checks | Tripwire failures |
|---|---|---|---|---|---|
| D3.1 | Risk model completeness | Failure mode inventory by severity x likelihood; 100% critical risks mapped to tests | Risk register and risk-to-test matrix | Independent risk elicitation and delta analysis | Critical risk with no verification activity |
| D3.2 | Requirement coverage depth | High-risk requirement coverage >=95%; medium >=85%; positive and negative assertions present | Coverage report linked to requirement IDs | Hidden requirement sampling for fake coverage | Inflated coverage via duplicate trivial tests |
| D3.3 | Oracle precision and falsifiability | Pass/fail criteria objective and machine-checkable; ambiguity rate <=5% | Oracle specs and assertion definitions | Independent reviewer reproduces pass/fail decisions | Critical checks rely on subjective interpretation |
| D3.4 | Negative/adversarial/abuse verification | Abuse tests for trust boundaries, auth misuse, and malformed inputs all executed | Adversarial catalog, threat links, execution logs | Surprise abuse scenario insertion | Security/privacy abuse path untested or failing |
| D3.5 | Statistical rigor and uncertainty | Statistical claims include confidence bounds, sample rationale, uncertainty propagation | Statistical analysis plan and recompute outputs | Independent CI/p-value recomputation | Deterministic claim made from uncertain estimate |
| D3.6 | Defect discovery power | `MKR` meets anchor thresholds; fault injection reveals intended protections | Mutation report, equivalent mutant rationale, survivor analysis | Seeded defect detection challenge | Persistently low mutation kill in critical module |

### D4) Evidence Integrity and Auditability (14%)
| Sub-dimension ID | Sub-dimension | Indicators (operational tests) | Evidence requirements | Anti-gaming checks | Tripwire failures |
|---|---|---|---|---|---|
| D4.1 | Evidence manifest completeness | Required artifact manifest completeness >=95% with command provenance | Machine-readable manifest, runbook, artifact index | Random replay of manifest entries | Missing raw logs for claimed passes |
| D4.2 | Provenance and chain-of-custody | All critical artifacts linked to creator, timestamp, commit/build IDs | Provenance ledger and signed metadata | Lineage cross-check and hash validation | Critical evidence not traceable to origin state |
| D4.3 | Environment/toolchain reproducibility | Pinned versions and reproducible setup success >=95% | Container/lockfiles/runtime manifests | Clean-machine rebuild without cache | Undeclared dependency drift alters output |
| D4.4 | Log/artifact immutability | Append-only or signed logs; historical runs preserved and verifiable | Signed logs, checksum reports, storage policy | Tamper simulation with single-byte change detection | Edited logs represented as original evidence |
| D4.5 | Independent review integrity | Critical checks reviewed by non-author; role separation enforced | Review records, approval matrix, dissent record | Role and identity audit for self-approval | Author self-approves critical correctness claims |
| D4.6 | Public claim verifiability (doc/PDF/web) | Public claims have resolvable locator; broken reference rate <=2% | Built artifacts, locator map, link checker output | Anchor-shift and dead-link stress checks | Public material claim cannot be located or verified |

### D5) Independent Replay and Recomputation Rigor (16%)
| Sub-dimension ID | Sub-dimension | Indicators (operational tests) | Evidence requirements | Anti-gaming checks | Tripwire failures |
|---|---|---|---|---|---|
| D5.1 | Cold-start replay success | Clean environment replay succeeds with documented commands only | Cold-start runbook, complete logs, generated artifacts | Non-author operator replay without live assistance | Replay depends on undocumented local state |
| D5.2 | Cross-environment replay consistency | Supported environment matrix produces equivalent conclusions within tolerance | Environment matrix outputs and comparison report | Extra environment permutations beyond author-preferred setup | Material conclusion changes across supported environments |
| D5.3 | Independent numerical recomputation | All key published numbers independently recomputed; mismatch rate=0 | Independent recompute scripts and discrepancy ledger | Blind recomputation before seeing published values | Key metric mismatch beyond tolerance |
| D5.4 | External dependency snapshot control | External APIs/data/models pinned or snapshotted for replay | Data snapshots/API fixtures/version locks | Network-off replay mode test | Live external drift changes outputs silently |
| D5.5 | Randomness and nondeterminism control | Seeds logged; deterministic validation mode exists; variance envelopes stable | Seed manifest, repeated-run variance report | Multi-seed robustness challenge | Result claimed deterministic without reproducibility support |
| D5.6 | Replay recency and drift monitoring | Replay cadence policy met; drift thresholds monitored and acted upon | Replay schedule logs, drift alerts, response records | Surprise replay on latest commit | Certification relies on stale replay beyond policy limit |

### D6) Corrective Action and Regression Governance (10%)
| Sub-dimension ID | Sub-dimension | Indicators (operational tests) | Evidence requirements | Anti-gaming checks | Tripwire failures |
|---|---|---|---|---|---|
| D6.1 | Defect severity calibration | Severity aligns with impact policy; misclassification <=5% | Defect tracker and severity rationale | Independent blind re-triage sample | Critical defect down-classified to bypass gate |
| D6.2 | Root cause analysis rigor | Critical issues include causal chain and proof of root-cause coverage | RCA docs and causal evidence links | Counterfactual challenge for symptom-only fixes | Repeated critical issue closed without true root fix |
| D6.3 | Fix verification completeness | Every critical fix has pre-fix reproducer and post-fix passing evidence | Reproducer logs, added tests, regression pass logs | Remove-fix challenge to ensure test is effective | Critical fix closed without reproducible verification |
| D6.4 | Regression prevention controls | Recurring classes tracked; preventative controls added and measured | Static checks/guards/monitors changelog | Reintroduce historical defect signatures | Repeat critical defect class with no added controls |
| D6.5 | Release tripwire enforcement | CI/CD gating blocks unresolved critical tripwires; exceptions are formal and independent | Pipeline gate configs, override log, release record | Controlled gate-bypass simulation in staging | Production release despite active critical tripwire |
| D6.6 | Continuous correctness monitoring | Post-release monitoring catches correctness/factual drift within SLA | Dashboards, alert logs, incident postmortems | Synthetic incident/drift injection drill | Severe correctness incident undetected beyond SLA |

## 5) Independent Replay and Recomputation Protocol Matrix (Mandatory)
Scores above 75 require successful execution of this matrix.

| Protocol ID | Objective | Software replay procedure | Documentation replay procedure | PDF replay procedure | Web replay procedure | Pass criteria |
|---|---|---|---|---|---|---|
| RP-1 | Source identity freeze | Checkout exact commit/tag, verify hash and dependency lock state | Freeze doc source commit and citation index hash | Freeze source/template/build versions | Freeze frontend/backend commit + infra config snapshot | Hashes/manifests exactly match declared target |
| RP-2 | Cold-start reproducibility | Clean machine bootstrap and full verification run | Clean build of docs and references | Full PDF rebuild from source | Clean deploy and verification suite run | Success without undocumented steps |
| RP-3 | Determinism rerun | Repeat run with same seed/config, compare outputs | Rebuild docs twice and compare claim extraction outputs | Build PDF twice and compare extracted text/table hashes | Redeploy/retest and compare invariant outputs | Differences only within declared tolerances |
| RP-4 | Cross-environment consistency | Replay on required OS/runtime matrix | Replay on alternate supported runtime | Validate PDF output on alternate renderer/version | Replay on browser/device matrix | Material conclusions equivalent across environments |
| RP-5 | Independent recomputation | Recompute key metrics with independent toolchain | Recompute all quantitative doc claims from raw data | Recompute table/figure numbers from original datasets | Recompute displayed KPIs and computed values | Key mismatch rate = 0 (or approved tolerance met) |
| RP-6 | Dependency drift insulation | Replay with pinned data/API fixtures and locked packages | Validate citations against archived snapshots | Validate embedded references are archived and versioned | Mock external APIs/CDNs and replay | Results do not rely on unstable live dependencies |
| RP-7 | Adversarial and negative replay | Execute malformed inputs, fault injections, abuse tests | Inject citation faults and contradictory source cases | Inject rendering faults, broken assets, stale figures | Execute auth/input/browser abuse scenarios | Critical negative/adversarial tests pass or fail-safe |
| RP-8 | Temporal freshness revalidation | Re-run time-sensitive logic against evaluation date | Revalidate temporal/legal claims and version references | Revalidate standards/legal references in PDF | Revalidate live-content claims and freshness labels | No silent stale claims; stale items flagged |
| RP-9 | Failure reproduction proof | Reproduce severe defects on prior state and verify fixed state inversion | Reproduce prior factual/citation failures then verify correction | Reproduce prior PDF rendering/data defects then verify correction | Reproduce prior web regressions then verify correction | Reproducer fails before fix and passes after fix |
| RP-10 | Independent witness replay | Non-author operator runs full protocol with checklist | Non-author reviewer rebuilds and verifies claims | Non-author reviewer rebuilds and validates page-level claims | Non-author operator deploys and verifies public behavior | Witness report confirms full independent reproducibility |

## 6) Recomputation Protocol Matrix (Metric-Level)
This matrix defines minimum recomputation expectations for numeric and logical claims.

| Metric class | Input evidence required | Independent recomputation method | Tolerance policy | Failure classification |
|---|---|---|---|---|
| Deterministic arithmetic totals | Raw tables, transformation scripts, published totals | Recompute with independent script/spreadsheet and compare line-by-line | Exact match unless rounding policy explicitly defined | High if material; Medium otherwise |
| Statistical summaries | Sample definition, raw sample, method notes | Recompute mean/median/variance/CI with independent package | CI endpoints within declared numerical tolerance | High if affects conclusions |
| Derived rates/ratios | Numerator/denominator definitions and inclusion rules | Independently recalc with denominator audits | Exact match or documented precision tolerance | High if denominator policy mismatch |
| Forecast/projection outputs | Model version, parameters, seed, training/eval splits | Re-run model with fixed seeds and independent evaluator scripts | Distribution overlap and metric tolerance declared in advance | Critical if conclusion reverses |
| Conversion-driven values | Unit dictionary, conversion constants, input units | Recompute conversions from raw units and constants | Exact constant use and rounding consistency | High for any unit mismatch |
| Compliance thresholds | Regulatory/spec threshold source and effective date | Recompute pass/fail with raw values and active threshold version | Binary pass/fail must match | Critical if wrong compliance outcome |
| Web KPI calculations | Event schema, query definitions, aggregation windows | Independent query run on snapshot data | Aggregates must match within tolerance and same window rules | High if KPI direction changes |
| PDF table/figure numbers | Figure/table source data and generation scripts | Rebuild figures/tables from source and validate extracted numbers | Exact or declared rounding tolerance | High if published figure is wrong |

## 7) Evidence Minimums and Rejection Rules
### 7.1 Minimum evidence bundle per artifact type
| Artifact type | Mandatory evidence bundle |
|---|---|
| Software | Source hash, dependency locks, requirement trace matrix, full test logs, mutation/fault report, seed log, replay witness report, defect ledger snapshot |
| Documentation | Source hash, claim ledger, citation map with anchors, archived source snapshots, quantitative recomputation workbook, independent review records |
| PDF | Source files/templates, deterministic build command, extracted text hash, figure/table generation logs, page-level claim map, renderer compatibility evidence |
| Web | Frontend/backend commit hashes, infra config snapshot, API contract reports, browser/device replay logs, KPI recomputation outputs, monitoring and incident logs |

### 7.2 Mandatory reject conditions
Automatic reject from score above 25 if any of the following hold:
1. Claim ledger missing for fact-heavy artifacts.
2. Requirement trace matrix missing for behavior-heavy artifacts.
3. No independent replay evidence.
4. No recomputation evidence for published quantitative claims.
5. No severe-defect disclosure snapshot for the evaluated version.

## 8) Anti-Gaming Controls (Mandatory Execution)
1. Hidden holdout tests for algorithmic correctness and citation binding.
2. Blind extraction of material claims from a random artifact sample.
3. Replay by a non-author witness with no live coaching.
4. Prohibition of screenshot-only proof for critical checks.
5. Seed sweep challenge for stochastic systems.
6. Coverage inflation detection by mapping tests to actual assertions and runtime traces.
7. Citation laundering detection requiring primary-source support for critical claims.
8. Time-shift checks to catch stale but unflagged facts.
9. Tamper-evident checksum verification of raw logs and artifacts.
10. Defect suppression audit comparing runtime errors with ticketing records.

A score above 90 is prohibited if any mandatory anti-gaming control is skipped.

## 9) Tripwire Catalog and Immediate Consequences
Tripwires override weighted averages.

| Tripwire ID | Trigger condition | Severity | Immediate consequence | Required remediation before re-score |
|---|---|---|---|---|
| TW-1 | Fabricated evidence, invented source, forged citation, or altered logs represented as original | Critical | Overall score set to 0 | Forensic audit + full rerun from trusted baseline |
| TW-2 | Any critical requirement untraced or untested | Critical | Overall capped at 25 | Add requirement trace/tests + rerun critical suite |
| TW-3 | Material factual claim unsupported, contradicted, or misquoted | Critical | Overall capped at 25 | Correct claim/citation and revalidate full claim set |
| TW-4 | Independent replay not executable from runbook | High | Overall capped at 50 | Repair automation/runbook + witness replay pass |
| TW-5 | Key recomputation mismatch beyond tolerance | High/Critical | Overall capped at 50 or 25 | Correct computation pipeline + independent recompute pass |
| TW-6 | Undocumented manual intervention required for success | High | Overall capped at 50 | Document/automate steps and pass cold-start replay |
| TW-7 | Active unresolved critical defect at release decision | Critical | Overall capped at 25 | Fix, verify with reproducer inversion, and re-gate |
| TW-8 | Author self-approval for critical correctness/factual checks | High | Overall capped at 50 | Independent reviewer signoff with traceable identity |
| TW-9 | External dependency drift changes material outcomes silently | High | Overall capped at 50 | Pin/snapshot external dependencies and re-evaluate |
| TW-10 | Severe post-release correctness drift not detected within SLA | High | Overall capped at 50 | Monitoring correction + validation drill |
| TW-11 | Statistical claim reported without uncertainty where required | High | Overall capped at 50 | Add uncertainty analysis and refresh claims |
| TW-12 | Security/privacy abuse case fails without mitigating controls | Critical | Overall capped at 25 | Mitigate and pass adversarial replay suite |

## 10) Sub-dimension Scoring Procedure (Operational)
Apply this sequence independently to each sub-dimension:
1. Execute all mandatory indicator tests.
2. Validate required evidence items and provenance.
3. Execute mandatory anti-gaming checks.
4. Compute:
   - `P = passed indicator tests / mandatory indicator tests`
   - `E = valid evidence items / required evidence items`
   - `A = passed anti-gaming checks / required anti-gaming checks`
5. Assign preliminary anchor:
   - 0 if `P < 0.30` or `E < 0.30`.
   - 25 if `P < 0.60` or `E < 0.60`.
   - 50 if `P >= 0.60` and `E >= 0.75`.
   - 75 if `P >= 0.85`, `E >= 0.90`, and `A >= 0.70`.
   - 90 if `P >= 0.95`, `E >= 0.97`, and `A >= 0.90`.
   - 100 if `P=1.00`, `E=1.00`, `A=1.00`, and dual independent replay success.
6. Apply tripwire overrides.
7. Record explicit pass/fail test IDs, evidence IDs, and any exceptions.

Evaluator rule: when uncertainty exists and cannot be resolved with objective evidence, assign the lower anchor.

## 11) Dimension-Specific Anchor Interpretation Guides
### 11.1 D1 Technical Specification Conformance
- 0: critical behavior undefined or failing; major requirement gaps.
- 25: basic behavior partially works but critical boundaries/contracts fail.
- 50: core functionality passes typical paths; significant edge and integrity risk remains.
- 75: broad conformance across normal and edge cases with minor non-critical defects.
- 90: near-complete conformance with strong determinism and contract stability.
- 100: complete conformance with exhaustive critical-path proof and zero severe defects.

### 11.2 D2 Domain and Factual Correctness
- 0: claims unsupported or fabricated.
- 25: many claims weakly sourced, stale, or misbound.
- 50: majority claims valid but some material weaknesses remain.
- 75: strong source discipline and recomputable quantitative claims.
- 90: authoritative sourcing, precise claim-citation binding, and zero critical contradictions.
- 100: complete material claim verification, complete temporal validity, and full contradiction resolution.

### 11.3 D3 Verification Design and Coverage
- 0: verification absent or non-falsifiable.
- 25: ad hoc tests with weak risk and oracle discipline.
- 50: moderate verification with notable coverage and adversarial gaps.
- 75: robust risk-linked coverage with reliable oracles.
- 90: strong negative/adversarial rigor and high defect discovery power.
- 100: comprehensive risk-complete verification with demonstrated fault-detection strength.

### 11.4 D4 Evidence Integrity and Auditability
- 0: evidence cannot be trusted.
- 25: fragmented evidence with weak provenance.
- 50: mostly complete evidence but important integrity/provenance gaps.
- 75: auditable evidence with high completeness and good reproducibility metadata.
- 90: near-perfect integrity, provenance, and immutable logs.
- 100: complete, immutable, independently verified evidence chain for all critical claims.

### 11.5 D5 Independent Replay and Recomputation Rigor
- 0: replay impossible.
- 25: author-only reruns with undocumented dependencies.
- 50: one independent replay success but weak cross-environment coverage.
- 75: stable independent replay and recomputation with controlled dependencies.
- 90: cross-environment replay and independent recomputation with negligible drift.
- 100: dual-team replay success and perfect key-metric recomputation.

### 11.6 D6 Corrective Action and Regression Governance
- 0: defects unmanaged, no trustworthy correction loop.
- 25: inconsistent triage, weak fix verification.
- 50: functional correction loop but recurrence risk high.
- 75: reliable fix verification and regression controls.
- 90: strong governance with enforced release gates and stable recurrence trend.
- 100: exemplary governance with proactive prevention and continuous correctness assurance.

## 12) Mandatory Replay Execution Protocol (Step-by-Step)
1. **Target freeze**: capture commit hashes, build ID, environment metadata, evaluation timestamp.
2. **Manifest validation**: check manifest completeness and random checksum sampling.
3. **Cold-start execution**: run from clean environment without undocumented manual changes.
4. **Determinism rerun**: rerun same inputs/seeds and compare outputs.
5. **Cross-environment run**: execute defined environment matrix.
6. **Independent recomputation**: recompute key metrics from raw inputs using alternate tooling.
7. **Claim revalidation**: verify high-impact claims against source authority and current effective dates.
8. **Adversarial pass**: execute negative/abuse tests and confirm fail-safe behavior.
9. **Defect gate check**: confirm severe-defect status and release gate conformance.
10. **Scoring and adjudication**: apply anchors, tripwires, caps, and publish evidence-backed scorecard.

Any skipped mandatory step must be explicitly recorded. A skipped critical step disqualifies scores above 75.

## 13) Artifact-Class Specific Test Packs
### 13.1 Software
Required packs:
1. Requirement-linked unit/integration/E2E tests.
2. Boundary and malformed input tests.
3. Contract and backward compatibility tests.
4. Concurrency and idempotence tests.
5. Mutation/fault injection runs.
6. Cold-start and cross-environment replay.

### 13.2 Documentation
Required packs:
1. Material claim inventory and classification.
2. Claim-citation binding and authority checks.
3. Quantitative claim recomputation.
4. Temporal/legal validity checks.
5. Contradiction adjudication.
6. Independent rebuild and locator validation.

### 13.3 PDF
Required packs:
1. Reproducible source-to-PDF build.
2. Page-level claim locator mapping.
3. Table/figure number recomputation from source data.
4. Renderer compatibility checks.
5. Link/reference integrity checks.
6. Independent rebuild witness record.

### 13.4 Web
Required packs:
1. API and schema contract conformance.
2. Browser/device matrix behavior replay.
3. Public claim verifiability and freshness checks.
4. KPI recomputation from event logs/snapshots.
5. Abuse/pathological input tests.
6. Post-release monitoring and drift detection drills.

## 14) Scoring Integrity Safeguards and Common Failure Patterns
### 14.1 Frequent failure patterns
1. Trace matrix exists but maps to non-assertive tests.
2. Citations point to broad documents without exact locators.
3. Quantitative claims rely on manual spreadsheet edits not captured in logs.
4. Replay requires unstated credentials, local caches, or personal scripts.
5. Mutation tests excluded from critical modules without justification.
6. Defects marked resolved without failing pre-fix reproducer evidence.

### 14.2 Required evaluator actions when pattern detected
1. Force a focused retest of implicated sub-dimensions.
2. Increase blind sampling percentage for affected dimension.
3. Apply conservative anchor interpretation until objective evidence closes the gap.
4. Trigger tripwire when failure pattern matches catalog thresholds.

## 15) Enforcement Posture
The rubric is intentionally conservative. High scores require not only correct outputs but robust proof that correctness survives independent scrutiny, environment changes, adversarial inputs, and temporal drift. The evaluator must deny score inflation from presentation quality, partial evidence, or unverifiable claims.

Minimum standard for release confidence:
1. No active critical tripwire.
2. Independent replay success.
3. Key metric recomputation success.
4. Material claim verification with authoritative sources.
5. Defect governance evidence demonstrating sustainable correctness.

Without these conditions, the artifact does not meet a high-confidence correctness threshold regardless of superficial quality.

## 16) Final Adjudication Template (Mandatory Output Fields)
Every evaluation must publish the following fields:
1. Artifact ID and frozen commit/version.
2. Evaluation date/time and evaluator identities.
3. Dimension and sub-dimension scores with anchor rationale.
4. Core metric values (`TRC`, `CRP`, `FCV`, `RCM`, `IRS`, `MKR`, `EIC`, `OSD`).
5. Tripwire status list with severity and disposition.
6. Replay matrix completion status and evidence pointers.
7. Recomputation matrix completion status and discrepancy ledger.
8. Open severe defects and release-gate decision.
9. Residual risks and mandatory remediation actions.
10. Re-evaluation criteria and due date.

This template is required for comparability across teams and evaluation cycles.

---

# Section 4: A4
- source_file: `A4_reliability_security.md`
- scope: Reliability, Security, Privacy, Abuse Resistance, Performance
- word_count: 5854
- line_count: 271

# A4 Reliability-Security Rubric Section

## 1) Scope, Authority, and Scoring Contract
This rubric section is a strict evaluation instrument for artifact quality across software systems, documentation pipelines, PDFs, and web products. It governs five top-level dimensions only:

1. Reliability
2. Security
3. Privacy
4. Abuse Resistance
5. Performance

This section is not advisory. It is pass/fail anchored with graded maturity thresholds. The evaluator must score what is evidenced, not what is planned. Any control that is undocumented, untested, or unsupported by reproducible artifacts is scored as absent.

A score in this section is valid only when tested under all three operating modes:

1. Nominal conditions: expected production behavior and expected load.
2. Edge conditions: foreseeable but stressful conditions (partial outage, degraded dependencies, unusual but legal inputs, sudden surges).
3. Adversarial conditions: intentional attack, abuse, evasion, corruption, or gaming attempts by capable operators.

The scoring unit is the sub-dimension. There are 30 sub-dimensions total (6 under each top-level dimension). Each sub-dimension must receive one anchor score only: `0`, `25`, `50`, `75`, `90`, or `100`. Intermediate values are prohibited.

Dimension score is the arithmetic mean of its six sub-dimensions.

Overall A4 score is the weighted sum of dimension scores. Default weighting is equal unless formal governance dictates otherwise:

1. Reliability: 20%
2. Security: 20%
3. Privacy: 20%
4. Abuse Resistance: 20%
5. Performance: 20%

Tripwire penalties override arithmetic. Tripwires are defined in Section 9.

## 2) Global Anchor Ladder (Mandatory for Every Sub-dimension)
The anchor ladder below applies to all 30 sub-dimensions before row-specific checks. A row cannot score higher than an anchor level if the global criteria at that level are not satisfied.

| Anchor | Nominal test requirement | Edge test requirement | Adversarial test requirement | Evidence requirement | Interpretation |
|---|---|---|---|---|---|
| `0` | No repeatable nominal test exists, or critical flow fails in >50% of 20 runs. | No edge testing exists. | No adversarial testing exists. | Missing or non-verifiable evidence. | Control absent or non-operational. |
| `25` | One-off or manual nominal check only; no stable automation. | Edge case attempted without objective thresholds or repeatability. | Tabletop-only adversarial claims. | Screenshots, narratives, or policy text only. | Prototype control, not production-safe. |
| `50` | Automated nominal tests exist and pass >=85% over 3 consecutive runs for critical path. | At least 3 edge scenarios tested per quarter, pass >=60%. | At least one scripted adversarial simulation per quarter. | Raw outputs retained >=30 days. | Baseline control exists but fragile under stress. |
| `75` | Continuous nominal monitoring and release gates with pass >=95%. | Monthly edge campaign, pass >=85%, graceful degradation documented. | Quarterly adversarial simulation, pass >=70%, corrective actions closed <=30 days. | Immutable traceability >=90 days. | Production-credible control. |
| `90` | Nominal outcomes satisfy target in >=99% of measured weeks across >=180 days. | Weekly edge tests, pass >=95%, no uncontrolled cascade. | Monthly adversarial tests, pass >=90%, MTTD/MTTR within target. | Independent corroboration required. | High-assurance operations. |
| `100` | Stable nominal control over >=2 quarters with no critical regression. | Continuous boundary testing (fuzz, property, stress) with pass >=99% and confidence bounds. | Unannounced adversarial drills include compound attacks and fail-safe behavior. | Reproducible replay package plus independent attestation. | Exceptional, sustained, independently verified excellence. |

Global scoring enforcement:

1. Any claim without raw evidence is ignored.
2. Any evidence that cannot be replayed is downgraded by at least one anchor tier.
3. Any discrepancy >5% between dashboard metrics and recomputed raw metrics triggers anti-gaming review and score hold.
4. No sub-dimension may receive `90` or `100` without adversarial test evidence from the same evaluation window.

## 3) Evidence and Reproducibility Standard
Every scored row must include artifacts from this mandatory evidence package:

| Evidence class | Minimum required contents | Freshness | Reproducibility gate |
|---|---|---|---|
| Raw telemetry | Logs, metrics, traces, synthetic probes, alert streams | Last 90 days minimum (180 days for `90+`) | Evaluator can re-run extraction and reproduce KPI values |
| Test artifacts | Test scripts/configs for nominal, edge, adversarial runs | Current release cycle and previous cycle baseline | Re-execution in controlled env yields equivalent result within tolerance |
| Incident records | Sev1/Sev2 timeline, root cause, containment, corrective actions | Full scoring period | Timeline correlates to telemetry and paging logs |
| Control evidence | Policies/configs for auth, privacy, abuse, perf, failover | Current signed version plus change history | Effective state is observable in system |
| Delivery provenance | Build metadata, signatures, SBOM, rollout and rollback history | Full scoring period | Artifact chain validates end-to-end integrity |
| Independent corroboration | External monitor, internal independent team, or third-party audit | Required for any `90+` claim | Findings map to tested controls and sampled events |

Evidence integrity constraints:

1. Logs must be tamper-evident (WORM, signed exports, append-only chain, or equivalent).
2. Test windows must include at least one blind run where operators cannot pre-condition controls.
3. Each major score claim must cite exact test ID, timestamp, environment, and pass/fail threshold.
4. Failure artifacts are mandatory; withholding failures is treated as integrity violation.

## 4) Hierarchical Rubric: Dimension -> Sub-dimension -> Indicators
The table below is the grading core. Each row includes strict indicators, required evidence, anti-gaming checks, tripwire triggers, and explicit anchor tests for `50/75/90/100` (global `0/25` still apply from Section 2).

| Dimension | Sub-dimension | Indicators required for `>=75` | Required evidence | Anti-gaming check | Tripwire failure | Anchor-specific explicit tests (`50/75/90/100`) |
|---|---|---|---|---|---|---|
| Reliability | `R1 Availability and SLO Integrity` | Critical journeys defined with SLOs; SLIs based on user outcomes; error-budget policy gates risky change. | 180-day SLI timelines, release gate logs, outage/postmortem records. | Recompute uptime from raw outcome logs and compare to status page and external monitor. | Hidden outage >30 minutes, fabricated SLI definitions, or missing SLO for critical journey. | `50`: Nominal run at target load, success >=95% over 20 runs. `75`: Edge single-zone failure, success >=90%, detection <=5 min. `90`: Adversarial monthly failover drill, SLO met >=99% weeks. `100`: Internal vs independent uptime variance <0.1% for 2 quarters. |
| Reliability | `R2 Fault Tolerance and Graceful Degradation` | Timeouts/retries bounded; circuit breakers and bulkheads active; fallback modes documented and observable. | Fault injection outputs, resilience config, queue and saturation metrics. | Inject dependency brownout and verify core path continues with declared degraded capability. | Single non-critical dependency failure causes full service collapse. | `50`: Nominal dependency timeout handled without full failure. `75`: Edge hard-down dependency, core success >=90%. `90`: Adversarial multi-dependency brownout recovered <=15 min. `100`: Continuous chaos program shows bounded blast radius for 2 quarters. |
| Reliability | `R3 Correctness and Data Integrity Under Failure` | Idempotency contracts, consistency boundaries, reconciliation jobs, and data checksums are enforced. | Transaction traces, reconciliation reports, duplicate-event replay results. | Replay duplicated/reordered events and verify deterministic outcome and no duplicate side effects. | Silent data corruption or unreconciled divergence in regulated/customer-critical data. | `50`: Nominal retry tests produce zero duplicate side effects. `75`: Edge reordered event sets reconcile >=99.5%. `90`: Adversarial partial-write faults yield no silent corruption. `100`: Independent replay audit confirms integrity across failover and rollback paths. |
| Reliability | `R4 Backup, Recovery, and Continuity` | Tiered RTO/RPO defined; backups encrypted and tested; restore runbooks executable by on-call staff. | Backup catalog, restore logs, DR drill reports, RTO/RPO compliance. | Blind-restore random snapshot and compare checksum/state against source baseline. | Restore unusable when needed, RTO breached >2x, or unreported RPO breach. | `50`: Nominal monthly backup+restore succeeds. `75`: Edge restore after schema drift meets RTO/RPO. `90`: Adversarial ransomware/wiper drill restores cleanly <=4 hours. `100`: Unannounced DR drills pass for 2 consecutive quarters. |
| Reliability | `R5 Observability and Incident Response Reliability` | Metrics/logs/traces/synthetics cover all critical paths; alerts are actionable; runbooks tested. | Coverage map, alert quality metrics, incident timelines, runbook drill logs. | Select random Sev2 and reconstruct full timeline from telemetry to closure without gaps. | Sev1 not detected by monitoring or missing forensic data prevents root-cause analysis. | `50`: Nominal known fault detected <=15 min. `75`: Edge fault injection yields precision >=80% and recall >=90%. `90`: Adversarial stealth fault detected <=10 min, MTTR <=60 min. `100`: Independent drill confirms repeated accurate detection and response across two cycles. |
| Reliability | `R6 Dependency and Change Reliability` | Dependency risk scored; canary + rollback gates active; compatibility tests enforce forward/backward safety. | CI/CD gates, canary metrics, dependency update history, rollback evidence. | Re-run prior release rollback under load and validate schema compatibility and state safety. | Irreversible migration or unbounded dependency drift causing repeat Sev1 without guard changes. | `50`: Nominal canary and rollback succeed in prod-like environment. `75`: Edge compatibility tests pass across supported client versions. `90`: Adversarial bad dependency release blocked/rolled back <=10 min. `100`: Change failure rate <5% for 2 quarters with signed release provenance. |
| Security | `S1 Identity and Authentication Strength` | MFA for privileged access; session controls and risk checks active; recovery abuse-resistant. | Auth policy configs, enrollment metrics, auth logs, penetration findings. | Run credential stuffing and session replay attempts against controls and verify containment. | Privileged access without MFA or repeated account takeover due to weak auth controls. | `50`: Nominal auth controls enforced on all critical routes. `75`: Edge recovery and lockout controls resist abuse with acceptable false rejects. `90`: Adversarial stuffing blocked >=99% with real-time response. `100`: Independent red team fails to obtain privileged session via auth path in two campaigns. |
| Security | `S2 Authorization and Least Privilege` | Deny-by-default policy; object-level checks; role minimization and periodic access review implemented. | Policy-as-code, role matrix, access review records, authz test suite. | Differential role/object matrix tests verify no horizontal/vertical privilege escalation. | Confirmed broken access control exposing sensitive object/action beyond entitlement. | `50`: Nominal allowed/denied role tests pass. `75`: Edge tenant-boundary tests show zero unauthorized object access. `90`: Adversarial escalation probes blocked and alerted <=5 min. `100`: Independent adversarial audit finds no critical authz flaws across object graph. |
| Security | `S3 Secrets, Cryptography, and Key Lifecycle` | Secrets vaulted and rotated; strong cryptography standards enforced; key access strictly scoped and audited. | Secret inventory, rotation logs, KMS/HSM audit trails, TLS/crypto config evidence. | Canary secret insertion and leak search across logs/artifacts/outbound channels. | Hardcoded production secret or plaintext sensitive data where encryption is required. | `50`: Nominal secret retrieval and rotation automation works. `75`: Edge forced key rotation completes without outage. `90`: Adversarial key-compromise drill triggers rotation/containment within SLA. `100`: External crypto review finds no critical implementation defects for two periods. |
| Security | `S4 Vulnerability and Hardening Management` | Asset inventory complete; vulnerability scanning continuous; patch SLAs and hardening baselines enforced. | Scan outputs, asset inventory, patch timelines, baseline drift reports. | Cross-check random discovered assets against scan scope and patch status. | Critical exploitable vuln beyond SLA on exposed asset with no compensating control. | `50`: Nominal scanning covers >=80% in-scope assets and tracks critical findings. `75`: Edge hardening baseline applied >=95% of assets. `90`: Adversarial exploit simulation of current CVEs blocked/contained quickly. `100`: Independent assessment validates sustained critical patch SLA compliance over 2 quarters. |
| Security | `S5 Secure SDLC and Supply Chain Integrity` | Security gates in CI/CD; artifact signatures and provenance enforced; dependency policy and SBOM maintained. | SAST/DAST/SCA logs, build attestations, artifact signatures, SBOM, gate decisions. | Attempt unsigned artifact and poisoned package insertion in pipeline; verify mandatory block. | Unsigned/tampered artifact reaches production path or provenance chain is broken. | `50`: Nominal CI security gates run and block high-severity issues. `75`: Edge branch protections and signing requirements enforced for releases. `90`: Adversarial package poisoning blocked before deploy. `100`: Third-party audit confirms end-to-end supply chain controls in repeated cycles. |
| Security | `S6 Security Monitoring, Detection, and Response` | Security telemetry covers crown jewels; detection rules map to threat model; containment playbooks practiced. | SIEM coverage, detection quality metrics, incident timelines, forensics retention proof. | Replay known attack traces and verify claimed MTTD/MTTR and containment scope. | Active compromise persists undetected beyond target, or missing logs prevent investigation. | `50`: Nominal detections trigger on baseline attack classes. `75`: Edge low-signal attacks triaged and contained <=4 hours. `90`: Adversarial multi-stage intrusion detected+contained <=1 hour. `100`: Independent purple-team confirms repeated high-fidelity detection and containment. |
| Privacy | `P1 Data Inventory, Mapping, and Classification` | Personal data map complete, field-level classes tagged, ownership and processing context defined. | Data maps, schema tags, processing registers, owner assignments. | Sample production fields/log attributes and verify inventory coverage and proper classification. | Unknown personal data store in production or misclassified regulated data category. | `50`: Nominal core systems mapped and classified. `75`: Edge derived datasets and ingestion pipelines fully mapped. `90`: Adversarial discovery finds <=2% unmapped personal fields and fixes closed quickly. `100`: Independent audit confirms sustained map accuracy across two cycles. |
| Privacy | `P2 Lawful Basis, Consent, and Notice Fidelity` | Purpose-to-basis mapping explicit; consent capture/versioning traceable; notice-to-practice alignment demonstrable. | Consent logs, policy versions, legal mapping registry, processing audit traces. | Reconstruct historical user consent state and compare to actual processing at timestamp. | Processing without lawful basis or continued processing after valid withdrawal. | `50`: Nominal lawful basis mapping exists for primary purposes. `75`: Edge consent updates propagate <=24h across systems. `90`: Adversarial replay shows zero unauthorized processing after withdrawal in sampled cohort. `100`: Independent legal/privacy review confirms no critical notice-practice mismatch. |
| Privacy | `P3 Data Minimization and Purpose Limitation` | Collection constrained to approved minimum schema; purpose-scoped access and use controls are enforced. | Collection payload logs, purpose registry, access audit logs, minimization review records. | Compare actual payloads/forms/API schemas against approved minimums and detect over-collection. | Prohibited sensitive category collected without approved purpose and control package. | `50`: Nominal payloads align to minimum schema for core flows. `75`: Edge feature releases blocked until minimization review passes. `90`: Adversarial attempts to coerce extra collection fail. `100`: Two-quarter history with zero unauthorized over-collection findings. |
| Privacy | `P4 Retention, Deletion, and Secure Disposal` | Retention schedules enforced; deletion traverses downstream stores; legal holds explicit and auditable. | Retention schedule map, deletion jobs/logs, disposal records, hold exceptions. | Seed records with expiry and verify deletion across primary, replica, cache, analytic stores. | Expired regulated data remains without legal hold justification. | `50`: Nominal deletion jobs run with auditable outcomes. `75`: Edge cross-store deletion success >=95% in quarterly tests. `90`: Adversarial high-volume deletion surge handled without integrity failures. `100`: Independent verification confirms deterministic disposal behavior over two quarters. |
| Privacy | `P5 De-identification and Re-identification Resistance` | De-identification method documented; risk thresholds defined; release gates enforce re-identification limits. | Method docs, risk assessments, linkage test outputs, release approval records. | Conduct linkage attacks using internal and external auxiliary datasets on released samples. | Re-identification exceeds approved threshold in released dataset without immediate mitigation. | `50`: Nominal de-identification applied consistently for non-prod analytics. `75`: Edge quasi-identifier controls meet k-anonymity/l-diversity thresholds. `90`: Adversarial linkage attempts remain below approved risk target. `100`: Independent privacy lab review confirms robust resistance repeatedly. |
| Privacy | `P6 Data Subject Rights, Transparency, and Transfers` | DSAR intake/identity/fulfillment operational; transfer controls enforce processor and jurisdiction limits. | DSAR SLA logs, transfer assessments, processor contracts, transparency records. | Run synthetic DSAR and transfer attempts and verify SLA/legal compliance plus data boundary enforcement. | Statutory DSAR deadline breach in sample set, or unauthorized cross-border transfer. | `50`: Nominal access/deletion DSAR workflows function end-to-end. `75`: Edge DSAR surge retains >=95% SLA compliance. `90`: Adversarial unauthorized transfer attempt blocked with immediate alert. `100`: Independent audit validates DSAR accuracy and transfer governance over repeated cycles. |
| Abuse Resistance | `A1 Abuse Threat Modeling and Coverage` | Abuse model includes actors, vectors, economic incentives, and mapped controls/detections/owners. | Abuse taxonomy, threat models, traceability matrix, review cadence evidence. | Insert new abuse scenario and verify updates to controls/tests before release approval. | High-risk feature shipped without abuse model or stale model after major behavior change. | `50`: Nominal abuse model exists for core journeys. `75`: Edge misuse scenarios tested pre-release. `90`: Adversarial red-team playbooks executed quarterly with closure tracking. `100`: Independent review confirms comprehensive, current abuse coverage. |
| Abuse Resistance | `A2 Account Integrity and Fraud Resistance` | Controls cover fake accounts, takeover, referral/payment abuse, and recovery hijack patterns. | Fraud model metrics, challenge outcomes, account lifecycle logs, loss reports. | Replay known fraud ring patterns and synthetic mule behavior to verify prevention and detection. | Automated account farm and monetization pipeline operates at material scale undeterred. | `50`: Nominal anti-fraud checks block common abuse classes. `75`: Edge adaptive challenge tuning balances fraud and friction thresholds. `90`: Adversarial coordinated fraud campaign disrupted <=30 min. `100`: Sustained low fraud-loss plus independently validated false-positive governance. |
| Abuse Resistance | `A3 Rate Limiting, Quotas, and Economic Abuse Controls` | Per-actor and global limits present; high-cost endpoints bounded; abuse economics unfavorable to attacker. | Quota configs, throttle logs, cost anomaly alerts, incident records. | Test distributed identity rotation and verify effective enforcement and bounded unit cost impact. | Unbounded expensive endpoint abuse causing material cost or reliability harm. | `50`: Nominal critical endpoint limits active (per-IP/account/token). `75`: Edge distributed abuse triggers adaptive quotas. `90`: Adversarial botnet saturation remains bounded with graceful shedding. `100`: Independent validation confirms no practical bypass for major economic abuse paths. |
| Abuse Resistance | `A4 Automation and Bot Evasion Resistance` | Detection fuses network/device/behavioral signals; challenge mechanisms resist replay and farmed solves. | Detection quality reports, challenge telemetry, bypass analyses, tuning history. | Execute scripted + human-assisted bot campaigns across evasion variants and measure bypass. | Known high-impact bot bypass remains unmitigated beyond response SLA. | `50`: Nominal commodity bots blocked in harness. `75`: Edge low-and-slow automation recall >=85% with controlled false positives. `90`: Adversarial adaptive bot campaign bypass <5%. `100`: Independent red-team bot operation fails to sustain abuse in repeated tests. |
| Abuse Resistance | `A5 Policy Enforcement and Harmful Behavior Moderation` | Policy mapped to deterministic/risk-based enforcement; high-severity classes have fail-safe controls. | Policy map, moderation outputs, challenge set metrics, appeal statistics. | Evaluate blinded evasive abuse set matching current traffic distribution shifts. | High-severity prohibited behavior consistently passes without mitigation. | `50`: Nominal baseline harmful cases detected and handled. `75`: Edge ambiguous cases routed with documented quality/SLA controls. `90`: Adversarial evasions detected with robust recall and containment actions. `100`: Independent evaluation confirms sustained high quality and fairness controls. |
| Abuse Resistance | `A6 Abuse Incident Response, Appeals, and Kill Switches` | Abuse incidents severity-classified; emergency controls tested; user remediation and appeal paths auditable. | Incident timelines, kill-switch drill logs, appeal outcomes, operator communication records. | Simulate controlled abuse spike and verify emergency controls activate safely within target SLA. | Inability to disable actively harmful pathway during incident. | `50`: Nominal abuse response runbook executed successfully in drill. `75`: Edge kill-switch activation <=15 min with controlled blast radius. `90`: Adversarial live-fire simulation contained and restored safely with rollback proof. `100`: Unannounced drills repeatedly confirm fast safe containment and appeal integrity. |
| Performance | `F1 Latency SLO and Tail-Latency Control` | P50/P95/P99 targets declared by journey; tail latency sources measured and controlled. | Latency histograms, trace analysis, SLO reports, release deltas. | Correlate external synthetic latency with internal tracing under same workload profile. | Critical journey P99 exceeds 2x target with no containment plan. | `50`: Nominal load meets baseline latency target. `75`: Edge peak maintains P95 within SLO. `90`: Adversarial mixed burst keeps P99 within error budget. `100`: Two-quarter tail stability with independent verification. |
| Performance | `F2 Throughput, Concurrency, and Saturation Management` | Capacity limits known; backpressure and shedding strategy implemented; saturation detection is proactive. | Load test outputs, queue depth metrics, autoscaling events, error-rate trends. | Push service to near-saturation and verify bounded latency/errors without runaway retries. | Saturation causes queue runaway and cascading timeout collapse. | `50`: Nominal target QPS sustained with acceptable error rate. `75`: Edge 2x burst handled with bounded degradation. `90`: Adversarial sustained 3x burst stabilized via controlled shedding. `100`: Demonstrated >=30% safe headroom at forecast peak over two quarters. |
| Performance | `F3 Scalability, Elasticity, and Capacity Planning` | Forecast model used; elasticity validated; regional and seasonal demand shifts accommodated. | Forecast vs actual reports, scale test logs, reservation plans, autoscaling audits. | Compare forecast error to real peak events and confirm preemptive capacity actions. | Predictable peak causes preventable Sev1 due to capacity planning failure. | `50`: Nominal scale test supports current peak +20% headroom. `75`: Edge seasonal replay remains in SLO. `90`: Adversarial sudden regional demand shift absorbed without critical failure. `100`: Two peak cycles demonstrate forecast accuracy and proactive scaling actions. |
| Performance | `F4 Resource Efficiency and Cost-Performance` | Resource utilization tracked by workload unit; regressions budgeted; efficiency optimization is governed. | Utilization dashboards, cost per unit metrics, optimization backlog, post-change deltas. | Validate claimed efficiency gains against billing exports normalized by workload units. | Material cost-performance regression unresolved beyond governance SLA. | `50`: Nominal unit cost measured and trendable. `75`: Edge stress profile reveals no uncontrolled leaks. `90`: Adversarial noisy-neighbor contention stays within bounded efficiency loss. `100`: Two-quarter efficiency gains without reliability/security/privacy regression. |
| Performance | `F5 Client-Side and Distribution Performance (Web/Doc/PDF)` | Budgeted render/load/download targets; asset and document size controls; cache/CDN behavior validated. | Core Web Vitals/RUM, render timings, file-size history, cache metrics. | Test constrained device/network cohorts and verify usable core journey within budgets. | Baseline target cohort cannot complete critical flow due to performance failure. | `50`: Nominal standard-profile users meet baseline load targets. `75`: Edge low bandwidth/high latency remains usable with graceful degradation. `90`: Adversarial cache-miss/cold-start storms remain within threshold. `100`: Two-quarter cross-cohort high-percentile stability achieved. |
| Performance | `F6 Regression Prevention and Performance Governance` | Performance tests are release gates; budgets and rollback triggers codified; ownership and escalation clear. | CI perf gate logs, benchmark histories, rollback records, regression RCA documentation. | Seed synthetic regression and confirm automatic gate failure or rapid rollback trigger. | Release proceeds despite known critical performance regression in priority journey. | `50`: Nominal benchmark suite runs in CI and tracks baseline. `75`: Edge cold-start/large-payload benchmarks gate release. `90`: Adversarial regression injection detected pre-prod with automated enforcement. `100`: Two-quarter window with no severe regression escapes and independent gate audit pass. |

## 5) Threat/Fault Injection Matrix (Required for `>=75` Claims)
At least one test from each mode category must be executed per dimension each cycle. For any `90+` claim, at least one adversarial test per relevant sub-dimension must be executed in the same scoring window.

| ID | Scenario | Mode | Primary targets | Procedure | Pass criteria | Required artifacts | Tripwire trigger if failed |
|---|---|---|---|---|---|---|---|
| `TF-01` | Steady-state production-like replay | Nominal | `R1`, `F1`, `F2` | Run representative traffic for 60 minutes at expected peak. | SLO targets met, no unplanned degradation. | Workload manifest, raw telemetry, SLO computation sheets. | Claimed baseline unsupported or falsified. |
| `TF-02` | Single-zone failure | Edge | `R1`, `R2`, `R4` | Remove one zone and continue live traffic routing. | Core journey success >=90%, alert <=5 min, no data loss. | Failover logs, alert timelines, outcome metrics. | Hidden outage or integrity fault. |
| `TF-03` | Dependency timeout and retry amplification | Edge | `R2`, `R5`, `F1` | Inject latency spikes and partial timeouts in critical dependency. | Circuit breakers and backoff prevent collapse. | Injection config, queue metrics, retry behavior traces. | Cascading retry storm outage. |
| `TF-04` | Regional loss / failover | Adversarial | `R1`, `R4`, `F3` | Simulate region outage with controlled traffic shift and consistency checks. | RTO/RPO met; critical service continuity maintained. | DR drill output, consistency checksums, incident log. | RTO/RPO breach or silent divergence. |
| `TF-05` | Storage corruption and partial commit | Adversarial | `R3`, `R4` | Induce write interruption/corruption in mirror environment with replay. | Corruption fully detected, reconciled, and recovered. | Integrity reports, replay outcomes, recovery evidence. | Silent corruption persists. |
| `TF-06` | Credential stuffing at scale | Adversarial | `S1`, `A2`, `A4` | Run distributed login attempts with known leaked credentials. | >=99% blocked or challenged; takeover prevented. | Auth logs, defense events, containment actions. | Account takeover at protected tier. |
| `TF-07` | Authorization escalation probing | Adversarial | `S2`, `S6` | Execute object/function-level escalation attempts with crafted tokens. | Zero unauthorized read/write; alerts triggered. | Request traces, policy decisions, SIEM records. | Broken access control confirmed. |
| `TF-08` | Canary secret leakage | Adversarial | `S3`, `S6` | Plant synthetic secret; monitor logs/artifacts/egress for exfil path. | Leak detected and rotation executed within SLA. | Detector logs, key rotation records, RCA. | Real secret exposure unresolved beyond SLA. |
| `TF-09` | Supply chain poisoning attempt | Adversarial | `S5`, `R6` | Attempt unsigned/tampered artifact or malicious dependency in pipeline. | Promotion blocked by signatures/provenance/gates. | CI gate logs, signature checks, SBOM diffs. | Tampered artifact reaches deployable stage. |
| `TF-10` | DSAR deletion surge | Edge | `P4`, `P6`, `R3` | Flood deletion requests and verify downstream deletion completion. | >=95% SLA adherence, no non-target data damage. | DSAR workflow logs, deletion verification, exceptions. | Statutory breach or deletion incompleteness. |
| `TF-11` | Unauthorized transfer route | Adversarial | `P2`, `P6`, `S6` | Attempt export to disallowed processor or geography. | Transfer blocked, alert emitted, no boundary breach. | DLP/egress logs, policy decisions, incident ticket. | Unauthorized cross-border transfer succeeds. |
| `TF-12` | Re-identification linkage attack | Adversarial | `P5` | Use auxiliary datasets to re-identify sample of de-identified records. | Risk remains below approved threshold. | Attack method, computed risk metrics, mitigation record. | Risk threshold exceeded without immediate block. |
| `TF-13` | Distributed economic abuse | Adversarial | `A3`, `A4`, `F2` | Botnet-style access to high-cost endpoints and scraping targets. | Costs and service degradation bounded by controls. | Throttle metrics, bot detections, cost impact report. | Material economic or reliability harm. |
| `TF-14` | Harm policy evasion challenge set | Adversarial | `A5`, `A6` | Execute blinded evasive abuse corpus with variant encodings/tactics. | High-severity abuse contained; appeal process audit-complete. | Challenge outputs, moderation decisions, appeal outcomes. | High-severity class repeatedly bypasses controls. |
| `TF-15` | Cache stampede and cold-start storm | Edge | `R2`, `F1`, `F5` | Invalidate hot cache keys and trigger burst traffic on cold nodes. | Bounded tail latency, no cascading timeouts. | Cache metrics, latency histograms, autoscale logs. | Unbounded tail collapse. |
| `TF-16` | Constrained client network/device | Edge | `F5`, `R1` | Measure critical journeys on low-end devices and poor networks. | Journey completion within declared budget for target cohort. | Filmstrips, RUM slices, device/network profile logs. | Target cohort cannot complete critical flow. |
| `TF-17` | Insider privileged misuse simulation | Adversarial | `S2`, `S6`, `P1` | Controlled privileged account attempts out-of-scope sensitive access. | Denied or detected and contained with complete audit trail. | Access logs, alert records, containment timeline. | Privileged misuse undetected/unlogged. |
| `TF-18` | Live rollback during schema mismatch | Adversarial | `R6`, `R3`, `F6` | Deploy forward migration then rollback under realistic traffic. | Rollback succeeds without corruption or severe perf impact. | Deploy logs, migration checks, integrity and latency reports. | Irreversible change causes outage or data loss. |

Execution frequency minimums:

1. Nominal: weekly.
2. Edge: monthly.
3. Adversarial: quarterly for `75`, monthly for `90+`.
4. Blind scenarios: at least 30% of total adversarial set per cycle.

## 6) Dimension-by-Dimension Interpretation Guidance
This section constrains evaluator discretion and blocks optimistic grading.

### Reliability interpretation
1. Reliability scores primarily represent user-outcome continuity under disturbance, not just service uptime.
2. Retries that inflate apparent availability while increasing user-visible latency or failure count are considered failures.
3. Any unreconciled data divergence suppresses high reliability scores even if uptime is high.
4. DR claims without blind restore proof are capped at `50`.

### Security interpretation
1. Passing scanner output is insufficient without exploit-resistance validation.
2. Vulnerability closure is measured by production risk reduction, not ticket closure.
3. Identity and authorization controls are evaluated on bypass resistance, not documentation quality.
4. Security detection quality requires both high recall and manageable false positives.

### Privacy interpretation
1. Privacy controls must be operationally enforceable, not legal text-only artifacts.
2. Consent/notice scoring is based on actual processing behavior under timestamped historical replay.
3. Deletion and minimization require downstream propagation proof.
4. `90+` privacy scores require adversarial re-identification or transfer-boundary tests.

### Abuse resistance interpretation
1. Abuse resistance is measured against adaptive adversaries, not static spam filters.
2. Economic abuse must be unprofitable or materially constrained for strong scores.
3. Harm policy enforcement must include evasion-resistance and appeal integrity.
4. Kill-switch capability must be tested and fast, with safe rollback.

### Performance interpretation
1. Performance quality is tail-first, not average-only.
2. Throughput claims without saturation behavior evidence are capped at `50`.
3. Client-side performance is mandatory for web/doc/pdf artifacts, not optional.
4. Efficiency gains that degrade reliability, security, or privacy do not receive positive credit.

## 7) Anti-Gaming Regime (Mandatory)
Evaluators must actively test for measurement gaming and procedural evasion.

1. Raw metric recomputation: Recompute at least 20% of claimed KPIs directly from raw logs.
2. Signal triangulation: Compare at least two independent measurement channels for each high-stakes KPI.
3. Blind testing: Run at least one blind scenario per dimension per cycle.
4. Seeded canaries: Use canary secrets, canary DSAR records, and canary abuse payloads to validate detector honesty.
5. Historical replay: Reconstruct one prior incident and one prior release to verify timeline and control claims.
6. Suppression check: Compare unresolved alert anomalies against closed tickets for inconsistency patterns.
7. Threshold manipulation check: Inspect whether improved pass rates come from weaker thresholds or relaxed definitions.
8. Sampling integrity: Randomly sample evidence slices; pre-curated datasets cannot be sole basis.
9. Closure truthfulness: Any repeated "fixed" finding reappearing without control changes triggers severity escalation.
10. Integrity escalation: Any evidence tampering, selective omission, or non-reproducible key result triggers immediate tripwire review.

Mandatory anti-gaming penalties:

1. Fabricated or materially altered evidence: immediate Critical tripwire and A4 score hold.
2. Failure to provide raw evidence for `90+` claim: score downgraded to max `50` for that row.
3. Repeated inability to reproduce core KPI: dimension cap at `25` until corrected.

## 8) Scoring Workflow (Operational Procedure)
The evaluator must execute this sequence in order:

1. Validate submission completeness against Section 3.
2. Apply global anchor prerequisites from Section 2.
3. Evaluate each row in Section 4 with row-specific tests.
4. Execute required threat/fault scenarios from Section 5.
5. Run anti-gaming checks from Section 7.
6. Assign each sub-dimension one anchor score only.
7. Compute dimension means and weighted A4 aggregate.
8. Apply tripwire overrides from Section 9.
9. Publish mandatory remediation actions for any row below `75`.
10. Deny `90+` certification without independent corroboration.

Evaluator output template for each sub-dimension should include:

1. Assigned anchor score.
2. Exact test IDs and timestamps used.
3. Pass/fail thresholds and measured values.
4. Evidence locations.
5. Open risks and required remediation deadline.

## 9) Tripwire Regime (Hard Overrides)
Tripwires are hard constraints that prevent inflated scoring. They are not negotiable.

| Severity | Trigger examples | Mandatory score consequence | Exit criteria |
|---|---|---|---|
| Critical | Unauthorized sensitive data disclosure; unrecoverable data loss; active compromise unmanaged; fabricated evidence; unbounded harmful abuse event; production control bypass with verified exploitability | Overall A4 score capped at `25` regardless of weighted result | Verified remediation in production, independent validation, and one clean reassessment cycle |
| Major | Critical vulnerability beyond SLA on exposed asset; repeated broken authz findings; DSAR statutory breach; DR/RTO test failure; severe perf regression released knowingly | Affected dimension capped at `50`; two Major tripwires in separate dimensions cap overall A4 at `50` | Root-cause closure plus successful rerun of failed scenarios |
| Moderate | Repeated edge/adversarial test failures; unresolved high-risk findings past SLA; incomplete evidence in high-impact controls | Affected sub-dimension capped at `75` | Evidence completion and successful retest |

Tripwire enforcement rules:

1. Tripwire conditions supersede mathematical averages.
2. Tripwire history must be retained and visible in subsequent cycles.
3. Closing a tripwire requires both control fix and proof of non-regression.
4. Any recurrence within two cycles escalates one severity level.

## 10) Minimum Acceptance Baselines and Rating Semantics
Use this interpretation for governance decisions:

1. `0-25`: Not deployable for high-stakes use. Controls are absent, decorative, or non-operational.
2. `50`: Basic controls exist but fail under stress or adversarial pressure. Deployment only with explicit risk acceptance.
3. `75`: Production-credible baseline. Controls generally work across nominal and common edge scenarios.
4. `90`: High assurance. Controls remain effective under sustained adversarial testing and independent corroboration.
5. `100`: Rare. Sustained excellence with independent validation, blind-drill success, and no critical regression over two quarters.

Baseline gating rules:

1. No dimension may be below `50` for enterprise deployment.
2. Any Critical tripwire blocks production expansion.
3. Any sub-dimension below `75` requires dated remediation plan and accountable owner.
4. `90+` overall requires all dimensions >=`75` and no open Major/Critical tripwires.

## 11) Artifact-Specific Testing Adaptation (Software, Doc, PDF, Web)
The same rubric applies across artifact classes, but explicit test mapping is required.

| Artifact class | Reliability emphasis | Security/privacy emphasis | Abuse/performance emphasis | Mandatory additions |
|---|---|---|---|---|
| Software/API | Uptime, integrity under retries, rollback safety | AuthN/AuthZ, secret lifecycle, vuln management | API abuse controls, latency tail and throughput stability | Contract test replays and schema migration rollback tests |
| Web application | Full journey continuity frontend+backend | Session/browser security, client data leakage controls | Bot resistance, scraping resistance, Core Web Vitals and tail latency | Real-device constrained network tests |
| Documentation platform | Publish pipeline consistency and rollback | Access control, change provenance, metadata leak prevention | Edit spam abuse controls and search/render latency | Version consistency and tamper detection tests |
| PDF generation/distribution | Deterministic rendering and retrieval continuity | Redaction correctness, metadata hygiene, encryption/signature | Download abuse throttling, file-size/render budget | Pixel/content diff checks, metadata leakage scans |

Adaptation constraints:

1. Artifact-specific substitutions are allowed only if they preserve equivalent risk coverage.
2. Waivers require documented rationale, expiry, and compensating controls.
3. Waived rows cannot score above `50` without explicit governance sign-off.

## 12) Strict Evaluator Notes (Non-negotiable)
1. Score evidence, not confidence.
2. Do not award `90+` on internal claims alone.
3. Do not convert unresolved findings into "accepted risk" without documented authority.
4. Do not accept policy maturity as a proxy for operational control efficacy.
5. Require explicit test IDs and reproducible outputs for every high-score assertion.
6. Enforce tripwires exactly; no discretionary override within this section.

This completes the A4 Reliability-Security rubric section as an operational, adversarially testable, anti-gaming scoring instrument with strict tripwire enforcement.

---

# Section 5: A5
- source_file: `A5_ux_accessibility_visual.md`
- scope: UX, Accessibility, Information Design, Visual/Document Quality
- word_count: 7413
- line_count: 1237

# A5 UX-Accessibility-Visual Rubric Section

## Scope and Authority
This section is a release-gating rubric for evaluating UX, accessibility, information design, and visual/document quality across software, web products, documentation, and PDFs. It is binding and operational. It is not advisory language, and it is not a style preference checklist. It defines objective checks, constrained subjective review, required evidence, anti-gaming controls, and tripwire failures that can block release.

The section evaluates whether an artifact is:
- Usable for priority tasks without coaching.
- Accessible for users with assistive technologies and diverse sensory, cognitive, and motor profiles.
- Structured so information can be located, understood, and acted on quickly.
- Visually and document-wise production quality for intended delivery channels.
- Auditable with reproducible evidence, not presentation claims.

## Scoring Architecture

### Dimension Weights
| Dimension | Weight |
|---|---:|
| D1 Task UX and Interaction Integrity | 22 |
| D2 Accessibility and Inclusive Access | 26 |
| D3 Information Architecture and Content Systems | 20 |
| D4 Visual Design and Document Craft | 18 |
| D5 QA, Trust Signals, and Sustainability | 14 |
| **Total** | **100** |

### Sub-dimension Rule
Each sub-dimension is scored only at anchors `0 / 25 / 50 / 75 / 90 / 100`.
No free-form percentages are allowed.

Formula:
- `Sub-dimension points = sub-dimension weight x (anchor / 100)`
- `Dimension score = sum(sub-dimension points in that dimension)`
- `Section score = sum(all five dimension scores)`

### Release Thresholds
- Overall section score must be `>= 75`.
- D2 Accessibility score must be `>= 75`.
- No unresolved tripwire failures.
- Any unresolved tripwire caps overall section score at `50` and blocks release.
- Any missing critical evidence item caps the affected sub-dimension at `50`.

---

## Anchor Definitions With Explicit Tests

| Anchor | Objective Pass Tests | Subjective Review Tests | Evidence Tests | Defect Burden | Decision Rule |
|---:|---|---|---|---|---|
| 0 | Objective pass `<20%` or core task untestable | Reviewers fail to complete core tasks unaided | Required evidence mostly missing or unverifiable | Any unresolved critical tripwire | Immediate fail. No conditional pass. |
| 25 | Objective pass `20-39%` | Tasks complete only with major confusion or intervention | Partial evidence, core traces absent | Multiple major defects on core path | Severe quality failure. Rework mandatory. |
| 50 | Objective pass `40-59%` | Core tasks possible but inefficient and error-prone | Evidence present but incomplete for edge states | Major defects remain | Functional floor only, not production-grade UX quality. |
| 75 | Objective pass `60-79%` | Review median `>=3.5/5` with acceptable consistency | Complete evidence for primary paths | Mostly minor defects on core path | Acceptable baseline with tracked debt. |
| 90 | Objective pass `80-94%` | Review median `>=4.3/5`, low reviewer variance | Complete evidence for primary plus edge paths | No major unresolved defects | Strong production quality. |
| 100 | Objective pass `>=95%`, reproducible on rerun | Review median `>=4.8/5` and calibration stable | Complete evidence, independently reproducible | No major or critical defects; negligible minor issues | Reference-standard quality. |

### Dimension Anchor Gate
For each dimension, weighted sub-dimension anchors are computed first, then gated:

| Dimension Anchor | Required Dimension Condition |
|---:|---|
| 0 | Any unresolved tripwire in that dimension, or `>=2` sub-dimensions at anchor 0 |
| 25 | Fewer than half of sub-dimensions reach 50 |
| 50 | At least half of sub-dimensions reach 50 and no unresolved critical tripwire |
| 75 | At least 4 of 6 sub-dimensions at 75+, none below 50 |
| 90 | At least 5 of 6 sub-dimensions at 90+, remaining one at 75+, no major unresolved issues |
| 100 | All 6 sub-dimensions at 100, with independent retest evidence |

---

## Mandatory Subjective Review Constraints
- Minimum 3 independent reviewers.
- At least 1 reviewer with accessibility testing competence.
- Reviewers score independently before discussion.
- Each subjective score must cite evidence IDs and observable behavior.
- If reviewer spread exceeds one anchor band, perform reconciliation plus rerun on disputed tasks.
- No sub-dimension score above 75 from mockups-only or static-image evidence.
- No sub-dimension score above 90 without edge-case and failure-state proof.
- No sub-dimension score above 90 if supported contexts were excluded.
- Reviews must include at least one timed task set and one no-guidance task set.

---

## Strict Evidence Requirements
Missing a required evidence artifact caps the corresponding sub-dimension at 50. Missing two or more critical evidence artifacts in a dimension caps that dimension at 50.

| Evidence ID | Required Artifact | Software/Web | Documentation | PDF | Minimum Standard |
|---|---|---|---|---|---|
| E1 | Task walkthrough logs | Required | Required | Required | 5 representative tasks, timestamped, with pass/fail reason |
| E2 | IA/content architecture map | Required | Required | Required | Navigation tree and cross-reference map |
| E3 | State and component inventory | Required | Required for interactive docs | Required for interactive PDFs | Default/focus/error/loading/empty state coverage |
| E4 | Automated accessibility scan output | Required | Required where tooling supports | Required where tooling supports | Raw output attached, not summarized only |
| E5 | Keyboard traversal transcript | Required | Required if interactive | Required if interactive | Full task path with focus order and controls |
| E6 | Screen reader transcript | Required | Required | Required | Name-role-value, headings, landmarks, form announcements |
| E7 | Contrast and perception report | Required | Required | Required | Numeric threshold checks and failures listed |
| E8 | Media alternatives audit | Required if media exists | Required if media exists | Required if media exists | Alt text, captions, transcripts and equivalence quality |
| E9 | Language/readability audit | Required | Required | Required | Grade target, terminology consistency, ambiguity notes |
| E10 | Link/reference integrity report | Required | Required | Required | Broken-link rate and sample proof |
| E11 | Visual QA board | Required | Required | Required | Multi-viewport/page captures including error and edge states |
| E12 | Performance traces | Required | Required for heavy docs | Required for heavy PDFs | Interaction and load timings |
| E13 | Localization and expansion audit | Required if localized | Required if localized | Required if localized | Long-string, truncation, bidi and format checks |
| E14 | Privacy/consent flow evidence | Required when data is collected | Required when data is collected | Required when data is collected | Consent choices, reversibility and copy clarity |
| E15 | Document/PDF preflight output | N/A for non-document artifact | Required | Required | Tags, reading order, bookmarks, metadata |
| E16 | Defect register with severity and owner | Required | Required | Required | Open/closed status, priority, evidence links |

### Evidence Integrity Rules
- Raw evidence must be retained; edited summaries are supplementary only.
- If sample selection excludes failures, evidence is invalid for scores above 50.
- All evidence must include artifact version/build identifier.
- Time-sensitive evidence older than one release cycle is invalid unless rerun.
- Claims without evidence IDs are scored as unproven.

---

## Anti-Gaming Controls (Global)
- At least 30% of tested screens/sections/tasks are randomly selected by a reviewer not involved in creation.
- At least 2 adverse or edge-case tasks are mandatory in each task pack.
- Demo environments cannot be the sole evidence source.
- Happy-path-only evidence caps affected sub-dimensions at 50.
- Automated accessibility scans without manual keyboard and screen reader evidence cap D2 sub-dimensions at 50.
- Single-browser or single-device evidence caps D1.6 and D4 at 75.
- Synthetic-only content samples cap D3 at 75 unless real samples are audited.
- Claimed fixes without rerun evidence retain previous failing score.
- Curation-only screenshots without timestamps/log correlation cap at 50.

### Adversarial Validation Set (Required)
Use at least five adversarial checks per evaluation cycle:
- Disable pointer and complete all core tasks by keyboard.
- Run screen reader and verify role/name/value on randomized controls.
- Force low vision simulation and verify non-color cues.
- Inject invalid, boundary, stale, and out-of-sequence inputs.
- Enter from deep link or bookmarked section without homepage context.
- Export to PDF and verify tags/bookmarks/reading order from binary output.
- Apply pseudo-localization or long-string expansion.
- Throttle network and re-run core completion tasks.

---

## Tripwire Failures (Global)
Any tripwire forces anchor `0` for the affected sub-dimension and blocks release until fixed and retested.

Tripwires:
- Core task cannot be completed by intended user role.
- Keyboard trap, hidden focus, or inaccessible critical control.
- Unlabeled critical control for assistive technology.
- Critical content contrast below minimum thresholds.
- Compliance/safety/legal instruction missing, inaccessible, or misleading.
- Broken critical link, bookmark, citation, or reference path.
- PDF/doc reading order alters required meaning.
- Coercive consent flow or hidden opt-out.
- Evidence falsification, unverifiable claims, or defect-hiding redactions.

Tripwire Remediation Rule:
- Fix must be verified with fresh evidence and independent reviewer confirmation.
- Previous pass claims are invalidated for affected sub-dimension until rerun.

---

## Large Master Evaluation Table (Dimension -> Sub-dimension -> Indicators)

| Dimension (Weight) | Sub-dimension (Weight) | Indicators | Objective Checks | Evidence Required | Anti-Gaming Check | Tripwire Failure |
|---|---|---|---|---|---|---|
| D1 Task UX (22) | 1.1 Primary Task Completion (4) | Core goals complete unaided with low abandonment | `>=85%` success on 5 core tasks; median time `<=1.5x` expert baseline | E1, E12, E16 | Task set includes independent random tasks | Primary task impossible or blocked |
| D1 Task UX (22) | 1.2 Navigation and Wayfinding (4) | Orientation maintained and recoverable | Top tasks reachable in `<=3` moves; no orphan critical pages | E2, E1, E11 | Test deep-entry flows not in demo route | Cannot recover location/context in core flow |
| D1 Task UX (22) | 1.3 Feedback and System Status (4) | State changes visible and understandable | Visible focus/active/disabled states; progress for long ops | E3, E11, E6 | Verify success and failure states are both evidenced | Critical action without visible/audible status |
| D1 Task UX (22) | 1.4 Error Prevention and Recovery (4) | Errors prevented and recoverable | Validation catches known invalid input `>=95%`; undo/confirm for destructive actions | E1, E3, E16 | Inject malformed and stale inputs | Irreversible destructive action without warning |
| D1 Task UX (22) | 1.5 Learnability and Onboarding (3) | New user reaches first success quickly | First task completed within onboarding target; help in one step | E1, E9, E11 | Use reviewer with no prior product exposure | New user cannot complete first meaningful action |
| D1 Task UX (22) | 1.6 Cross-Context Consistency (3) | Stable behavior across supported contexts | No clipping/behavior mismatch on supported viewports/pages | E11, E1, E16 | Random context combinations are mandatory | Core flow fails on advertised supported context |
| D2 Accessibility (26) | 2.1 WCAG 2.2 AA Baseline (5) | Baseline conformance in critical paths | No unresolved critical A/AA failures; automated + manual checks | E4, E6, E16 | Random rerun on non-demo pages | Unresolved WCAG A failure on core path |
| D2 Accessibility (26) | 2.2 Keyboard and Focus (5) | Full operation without pointer | Keyboard-only completion of core tasks; visible focus and logical order | E5, E11, E16 | Validate with mouse disabled | Keyboard trap or lost focus |
| D2 Accessibility (26) | 2.3 Screen Reader Semantics (4) | Correct names, roles, values and structure | Labeled critical controls; coherent headings/landmarks | E6, E4, E15 | Independent reviewer transcript | Unlabeled critical control/input |
| D2 Accessibility (26) | 2.4 Contrast and Non-Color Cues (4) | Readable and non-color dependent signals | Text/UI contrast thresholds met; state not color-only | E7, E11, E16 | Grayscale simulation sample checks | Critical status encoded by color alone |
| D2 Accessibility (26) | 2.5 Alternative Media Access (4) | Media alternatives provide equivalent meaning | Alt coverage `>=98%`; captions/transcripts where required | E8, E6, E15 | Random sample includes complex media | Essential media lacks alternative |
| D2 Accessibility (26) | 2.6 Cognitive and Language Access (4) | Plain language and actionable sequence | Readability target met; jargon defined; steps coherent | E9, E1, E16 | Test with unfamiliar reviewer | Safety-critical instruction ambiguous |
| D3 Info Design (20) | 3.1 Audience-Task Model (4) | IA matches real user goals | `>=90%` key tasks map to clear IA nodes | E2, E1, E10 | Include low-frequency high-criticality role | Core audience cannot locate mandatory content |
| D3 Info Design (20) | 3.2 Labeling and Taxonomy (4) | Distinct and predictable naming | No conflicting top-level labels; vocabulary consistency | E2, E9, E10 | Blind label interpretation test | Conflicting labels misroute critical task |
| D3 Info Design (20) | 3.3 Structure and Scannability (3) | Chunked content supports skim-to-act behavior | Valid heading hierarchy; long sections segmented effectively | E2, E9, E11 | Audit densest sections, not curated samples | Critical procedure hidden in text wall |
| D3 Info Design (20) | 3.4 Search and Retrieval (3) | High success locating needed content | Top queries return correct result in top 3 `>=80%` | E10, E1, E2 | Include synonym/misspelling tests | Common task terms return no useful result |
| D3 Info Design (20) | 3.5 Data/Chart/Table Explainability (3) | Data visuals are interpretable and honest | Title/unit/timeframe/source/legend included where needed | E11, E9, E15 | Random axis/scale integrity checks | Misleading scale or omitted context |
| D3 Info Design (20) | 3.6 Reference Integrity and Navigation Aids (3) | TOC/bookmarks/links are reliable | Broken-link rate `<0.5%`; bookmark/anchor correctness | E10, E15, E11 | Deep-link random verification | Broken legal/safety reference |
| D4 Visual Craft (18) | 4.1 Typography and Legibility (3) | Readable typography across contexts | Body size/line length/line spacing within target ranges | E11, E7, E15 | Verify at zoom and constrained viewports | Critical text unreadable at standard use |
| D4 Visual Craft (18) | 4.2 Layout and Spatial Rhythm (3) | Spatial hierarchy aids comprehension | Grid/spacing tokens consistent; no overlap/clipping | E11, E3, E16 | Include high-density real content sample | Overlap/clipping obscures critical content |
| D4 Visual Craft (18) | 4.3 Color and Semantic Usage (3) | Consistent semantic color mapping | Status/severity/category tokens applied consistently | E11, E7, E3 | Compare semantics across screens/pages | Contradictory semantic colors |
| D4 Visual Craft (18) | 4.4 Imagery and Iconography Quality (3) | Assets clear, purposeful, coherent | Resolution and clarity thresholds met; icon meaning clear | E11, E8, E16 | Interpretation test without adjacent labels | Critical icon misunderstood |
| D4 Visual Craft (18) | 4.5 Component and State Consistency (3) | Same patterns behave consistently | Component states fully covered and parity verified | E3, E11, E16 | Random instance parity audit | Same component behaves inconsistently |
| D4 Visual Craft (18) | 4.6 Document/PDF Finish Quality (3) | Output production-ready and accessible | Tagged structure, metadata, bookmarks, print-safe output | E15, E10, E11 | Validate exported binary, not source view only | Untagged or misordered required PDF/doc |
| D5 QA/Trust (14) | 5.1 Evidence Traceability (3) | Claims are reproducible | Score rows map to evidence IDs and raw artifacts | E1-E16 mapping | Independent replay on random claims | Claim not reproducible |
| D5 QA/Trust (14) | 5.2 Performance Experience (2) | Interaction responsiveness supports task flow | Critical action latency within threshold under constraints | E12, E1, E16 | Include throttled runs | Latency blocks core completion |
| D5 QA/Trust (14) | 5.3 Localization and Cultural Fit (2) | Locale variations safe and clear | No truncation in critical text; locale formats accurate | E13, E11, E16 | Pseudo-loc and expansion checks | Localized critical text misleading |
| D5 QA/Trust (14) | 5.4 Privacy/Consent/Safety Communication (2) | Clear, reversible, non-coercive choices | Granular consent and explicit withdrawal path | E14, E9, E16 | Dark-pattern checklist by independent reviewer | Coercive consent or hidden opt-out |
| D5 QA/Trust (14) | 5.5 Monitoring and Regression Controls (3) | Quality protected after release | Scheduled/CI checks for a11y/links/visual regressions | E4, E10, E11, E16 | Verify checks run beyond demo branches | No active control despite recurring regressions |
| D5 QA/Trust (14) | 5.6 Design System Governance (2) | Maintainable consistency at scale | Versioned tokens/components, ownership, deprecation policy | E3, E11, E16 | Audit local overrides and exception registry | Uncontrolled overrides break critical consistency |

---

## Detailed Dimension Criteria

## D1 Task UX and Interaction Integrity (22)

### 1.1 Primary Task Completion (Weight 4)
Indicators:
- Intended users can complete priority tasks unaided.
- Completion includes valid end-state, not partial progression.

Objective checks:
- Test 5 core tasks with representative users/reviewers.
- Require `>=85%` successful completion.
- Median completion time `<=1.5x` expert baseline.

Subjective constraints:
- No live coaching.
- No hidden acceptance criteria withheld from reviewers.

Evidence:
- E1 task logs.
- E12 timings.
- E16 defects tied to failed tasks.

Anti-gaming:
- At least 2 non-happy-path tasks included.

Tripwire:
- Any core task impossible for intended role.

Anchor tests:
- 0: Fewer than 1 in 5 complete correctly.
- 25: Completion exists only with repeated guidance.
- 50: Completion possible but with high abandonment or rework.
- 75: Most complete core tasks with manageable friction.
- 90: Completion reliable across primary and edge contexts.
- 100: Near-universal completion with stable rerun outcomes.

### 1.2 Navigation and Wayfinding (Weight 4)
Indicators:
- Users understand where they are and where to go next.
- Orientation survives detours and deep links.

Objective checks:
- Top tasks reachable in `<=3` navigation moves.
- No orphan pages/sections in critical content.
- Return path to known context in one clear action.

Subjective constraints:
- Reviewer starts from non-home entry at least once.

Evidence:
- E2 IA map.
- E1 path traces.
- E11 navigation captures.

Anti-gaming:
- Random deep-link entry tests mandatory.

Tripwire:
- User cannot recover orientation in core flow.

Anchor tests:
- 0: Navigation failure prevents task completion.
- 25: Frequent dead ends or mislabeled routes.
- 50: Main route works; alternative route confusion remains.
- 75: Navigation mostly predictable; minor edge confusion.
- 90: Strong orientation across most contexts and entry points.
- 100: Navigation fully coherent with robust wayfinding resilience.

### 1.3 Interaction Feedback and System Status (Weight 4)
Indicators:
- System communicates state changes promptly.
- Feedback is perceivable in visual and assistive contexts.

Objective checks:
- All controls expose focus/active/disabled states.
- Operations exceeding 400ms show progress indicator.
- Failure and success outcomes are distinguishable.

Subjective constraints:
- Reviewers must validate loading, success, empty, and error states.

Evidence:
- E3 state inventory.
- E11 screenshots.
- E6 SR announcements.

Anti-gaming:
- Missing failure-state evidence caps at 50.

Tripwire:
- Critical action without confirmation or failure notice.

Anchor tests:
- 0: No reliable status feedback on critical actions.
- 25: Inconsistent feedback leads to repeated accidental actions.
- 50: Core feedback exists but edge states are unclear.
- 75: Feedback clear on primary states.
- 90: Feedback clear on primary plus edge states.
- 100: Complete status clarity with consistent multimodal signaling.

### 1.4 Error Prevention and Recovery (Weight 4)
Indicators:
- Preventable errors blocked before commitment.
- Recovery path is explicit and low-friction.

Objective checks:
- Validation blocks known invalid patterns `>=95%`.
- Destructive actions require confirm/undo.
- Error message states cause and corrective action.

Subjective constraints:
- Reviewers intentionally trigger invalid states.

Evidence:
- E1 negative-path logs.
- E3 validation map.
- E16 defect tracking.

Anti-gaming:
- Include malformed, stale, and boundary input set.

Tripwire:
- Irreversible destructive action with no protection.

Anchor tests:
- 0: Destructive mistakes frequent and unrecoverable.
- 25: Validation weak and recovery unclear.
- 50: Basic prevention but recovery still costly.
- 75: Good prevention and practical recovery.
- 90: Strong prevention across edge conditions.
- 100: Prevention and recovery are comprehensive and consistent.

### 1.5 Learnability and Onboarding (Weight 3)
Indicators:
- New users achieve meaningful progress rapidly.
- Help and guidance are contextual and concise.

Objective checks:
- First core task completion within target time for first-time user.
- Help is reachable in one action from relevant context.

Subjective constraints:
- At least one novice reviewer is mandatory.

Evidence:
- E1 first-session logs.
- E9 clarity audit.
- E11 onboarding captures.

Anti-gaming:
- Team insiders cannot substitute as novice evidence.

Tripwire:
- First meaningful action cannot be completed unaided.

Anchor tests:
- 0: New users fail before first success.
- 25: Heavy dependence on external explanation.
- 50: First success possible but confusing.
- 75: New users usually reach first success with acceptable effort.
- 90: New users succeed quickly with clear transfer to next tasks.
- 100: Onboarding is concise, reliable, and resilient across contexts.

### 1.6 Cross-Context Consistency (Weight 3)
Indicators:
- Behavior is consistent across supported channels and device classes.

Objective checks:
- Supported viewports/pages show no core-task breakage.
- Behavior and terminology parity maintained across contexts.

Subjective constraints:
- Same task set run in at least two supported contexts.

Evidence:
- E11 cross-context board.
- E1 comparative logs.
- E16 compatibility defects.

Anti-gaming:
- Random context pairing chosen by reviewer.

Tripwire:
- Any advertised supported context fails core task.

Anchor tests:
- 0: Core task fails in supported context.
- 25: Major functional divergence by context.
- 50: Primary context stable; others degrade.
- 75: Stable behavior with limited minor variation.
- 90: High parity across supported contexts.
- 100: Near-perfect parity and resilience under context transitions.

---

## D2 Accessibility and Inclusive Access (26)

### 2.1 WCAG 2.2 AA Baseline Conformance (Weight 5)
Indicators:
- Critical paths meet baseline success criteria.

Objective checks:
- Automated and manual checks show no unresolved critical A/AA failures in core flows.

Subjective constraints:
- Accessibility-qualified reviewer validates high-risk controls manually.

Evidence:
- E4 scan outputs.
- E6 manual notes.
- E16 remediation records.

Anti-gaming:
- Random non-demo page selection for rerun.

Tripwire:
- Unresolved WCAG A failure on core path.

Anchor tests:
- 0: Critical baseline violations unresolved.
- 25: Frequent A/AA failures in key journeys.
- 50: Core path mostly compliant but notable gaps remain.
- 75: Baseline compliance on primary paths.
- 90: Baseline compliance on primary and edge paths with solid evidence.
- 100: Full baseline conformance with independent reproducibility.

### 2.2 Keyboard Operability and Focus Management (Weight 5)
Indicators:
- Pointer-free operation is complete and predictable.

Objective checks:
- Every action in core journey keyboard accessible.
- Focus visible and logical throughout.
- No keyboard traps.

Subjective constraints:
- Entire core task set executed without pointer.

Evidence:
- E5 traversal transcript.
- E11 focus captures.
- E16 defect log.

Anti-gaming:
- Disable pointer device during verification.

Tripwire:
- Keyboard trap or hidden focus in critical path.

Anchor tests:
- 0: Keyboard-only completion impossible.
- 25: Frequent focus loss and inaccessible controls.
- 50: Main flow possible with notable keyboard friction.
- 75: Keyboard flow workable and mostly coherent.
- 90: Strong keyboard ergonomics including edge states.
- 100: Complete, efficient, and robust keyboard operation.

### 2.3 Screen Reader Semantics (Weight 4)
Indicators:
- Semantic structure supports non-visual navigation and understanding.

Objective checks:
- Critical controls expose accurate names/roles/values.
- Headings/landmarks enable efficient navigation.

Subjective constraints:
- Reviewer completes core tasks via screen reader.

Evidence:
- E6 transcripts.
- E4 semantic findings.
- E15 tag/structure report for document outputs.

Anti-gaming:
- Deep-page randomized transcript required.

Tripwire:
- Unlabeled critical control or incorrect role causing wrong action.

Anchor tests:
- 0: Core function unusable with screen reader.
- 25: Frequent unlabeled/misleading controls.
- 50: Core controls mostly labeled; structural friction remains.
- 75: Good semantic support in primary paths.
- 90: Strong semantic reliability across edge states.
- 100: Excellent screen reader performance and structural clarity.

### 2.4 Contrast and Non-Color Cues (Weight 4)
Indicators:
- Content remains understandable under varied visual conditions.

Objective checks:
- Contrast thresholds met (`4.5:1` normal text, `3:1` large text/UI graphics).
- No critical meaning conveyed by color alone.

Subjective constraints:
- Reviewer uses grayscale/zoom checks.

Evidence:
- E7 contrast report.
- E11 visual proof.
- E16 defect closures.

Anti-gaming:
- Random checks on production screens/pages, not token docs only.

Tripwire:
- Critical status communicated only by color.

Anchor tests:
- 0: Critical text/status fails contrast or color-independence.
- 25: Frequent low-contrast and color-only signaling.
- 50: Baseline mostly met with notable exceptions.
- 75: Strong contrast and non-color cues in primary paths.
- 90: Robust compliance across primary and edge scenarios.
- 100: Complete clarity under low-vision and color-deficit simulations.

### 2.5 Alternative Media Access (Weight 4)
Indicators:
- Non-text content has meaningful alternatives.

Objective checks:
- Alt coverage `>=98%` for informative images.
- Required media includes captions/transcripts.
- Alternatives preserve critical meaning.

Subjective constraints:
- Reviewer verifies equivalence quality, not checkbox presence.

Evidence:
- E8 media audit.
- E6 SR verification.
- E15 doc/PDF structure checks.

Anti-gaming:
- Random sample includes complex visual media.

Tripwire:
- Essential media lacks accessible equivalent.

Anchor tests:
- 0: Essential media inaccessible.
- 25: Sparse or low-quality alternatives.
- 50: Core alternatives present with quality gaps.
- 75: Good alternatives for primary media.
- 90: High-coverage, high-quality alternatives including edge assets.
- 100: Full multimodal equivalence quality.

### 2.6 Cognitive and Language Accessibility (Weight 4)
Indicators:
- Language and sequence reduce avoidable cognitive load.

Objective checks:
- Readability target documented and met.
- Jargon defined on first use.
- Instructions sequenced and actionable.

Subjective constraints:
- Reviewer unfamiliar with domain can execute key instructions.

Evidence:
- E9 readability audit.
- E1 comprehension task logs.
- E16 confusion-related defects.

Anti-gaming:
- Stress-condition task included (interrupt/resume).

Tripwire:
- Safety-critical wording ambiguous or contradictory.

Anchor tests:
- 0: Instructions unusable or dangerously unclear.
- 25: High ambiguity and jargon overload.
- 50: Understandable with frequent rereading.
- 75: Clear language on primary paths.
- 90: Clear, concise, and robust comprehension including edge cases.
- 100: Exemplary plain-language and sequence design.

---

## D3 Information Architecture and Content Systems (20)

### 3.1 Audience-Task Information Model (Weight 4)
Indicators:
- Content structure reflects actual user intents and roles.

Objective checks:
- `>=90%` of top tasks map to clear, discoverable IA nodes.

Subjective constraints:
- Role-specific walkthrough required.

Evidence:
- E2 IA model.
- E1 task logs.
- E10 reference structure.

Anti-gaming:
- Include at least one high-risk low-frequency role task.

Tripwire:
- Intended role cannot locate mandatory content.

Anchor tests:
- 0: IA does not support core audience tasks.
- 25: Frequent task/structure mismatch.
- 50: Partial alignment with notable gaps.
- 75: Good alignment for primary roles.
- 90: Strong role-task alignment including edge roles.
- 100: Comprehensive, resilient IA-task fit.

### 3.2 Labeling and Taxonomy Quality (Weight 4)
Indicators:
- Labels are unique, stable, and domain-appropriate.

Objective checks:
- No conflicting high-level labels.
- Controlled vocabulary consistent across channels.

Subjective constraints:
- Blind interpretation by uninvolved reviewer.

Evidence:
- E2 taxonomy map.
- E9 terminology audit.
- E10 cross-reference usage.

Anti-gaming:
- Synonym and near-duplicate challenge set.

Tripwire:
- Conflicting labels cause critical misrouting.

Anchor tests:
- 0: Labels misleading in critical content.
- 25: Frequent ambiguity and inconsistency.
- 50: Basic consistency with recurring confusion points.
- 75: Generally clear and predictable terminology.
- 90: High semantic precision across contexts.
- 100: Terminology system is exact, coherent, and durable.

### 3.3 Structure and Scannability (Weight 3)
Indicators:
- Users can skim and still perform correctly.

Objective checks:
- Heading hierarchy valid.
- Long sections chunked with purposeful headings and summaries.

Subjective constraints:
- Time-boxed skim-to-action test.

Evidence:
- E2 outline.
- E11 page samples.
- E9 scan/readability results.

Anti-gaming:
- Include densest sections.

Tripwire:
- Critical procedure buried in unstructured content block.

Anchor tests:
- 0: Content structure blocks correct action.
- 25: Poor chunking causes repeated misses.
- 50: Primary sections scannable, dense sections weak.
- 75: Mostly scannable with manageable exceptions.
- 90: Strong chunking and rapid retrieval across sections.
- 100: Excellent information flow and scan reliability.

### 3.4 Search and Retrieval Effectiveness (Weight 3)
Indicators:
- Users retrieve needed information quickly with realistic queries.

Objective checks:
- `>=80%` of top queries return correct item in top 3 results.

Subjective constraints:
- Reviewer uses role terms, lay terms, and abbreviation variants.

Evidence:
- E10 search logs.
- E1 retrieval tasks.
- E2 index metadata mapping.

Anti-gaming:
- Include misspellings and synonym set.

Tripwire:
- Common query for critical task returns no actionable result.

Anchor tests:
- 0: Search fails critical retrieval.
- 25: Frequent irrelevant results for common terms.
- 50: Search works for exact terms only.
- 75: Good retrieval for common terms and variants.
- 90: High retrieval reliability across variant phrasing.
- 100: Near-perfect retrieval precision and relevance.

### 3.5 Data/Chart/Table Explainability (Weight 3)
Indicators:
- Quantitative visuals are understandable and not deceptive.

Objective checks:
- Required context fields present: title, unit, timeframe, source, legend where needed.
- No manipulative axes/scales for critical decisions.

Subjective constraints:
- Reviewer independently interprets chart and explains decisions supported by it.

Evidence:
- E11 visual board.
- E9 explanatory-text audit.
- E15 table semantics for docs/PDFs.

Anti-gaming:
- Random axis and baseline inspection.

Tripwire:
- Distorted scale or missing context changes likely decision outcome.

Anchor tests:
- 0: Visualizations misleading on critical information.
- 25: Major omissions in context/labels.
- 50: Basic clarity with notable interpretive risk.
- 75: Good interpretability for primary use.
- 90: Strong interpretability and transparent context.
- 100: Exemplary data communication discipline.

### 3.6 Reference Integrity and Navigation Aids (Weight 3)
Indicators:
- TOC/bookmarks/anchors/links are accurate and reliable.

Objective checks:
- Broken-link rate `<0.5%`.
- Internal anchors/bookmarks map to correct target.

Subjective constraints:
- One complete task performed via navigation aids only.

Evidence:
- E10 link report.
- E15 preflight output.
- E11 deep-link captures.

Anti-gaming:
- Validate post-export binaries and deep links.

Tripwire:
- Broken safety/compliance/legal reference.

Anchor tests:
- 0: Navigation aids fail critical use.
- 25: Frequent broken references.
- 50: Core references mostly intact with recurring defects.
- 75: Reliable references in primary paths.
- 90: High integrity across primary and edge links.
- 100: Fully reliable reference system with resilient maintenance.

---

## D4 Visual Design and Document Craft (18)

### 4.1 Typography and Legibility (Weight 3)
Indicators:
- Typography supports fast scanning and sustained reading.

Objective checks:
- Body size, line height, and line length remain in defined legibility range for target medium.

Subjective constraints:
- Long-form reading test required, not only headline views.

Evidence:
- E11 typography captures.
- E7 contrast pairings.
- E15 output checks.

Anti-gaming:
- Verify under zoom and narrow viewports/pages.

Tripwire:
- Critical text unreadable in normal usage.

Anchor tests:
- 0: Legibility failure on critical text.
- 25: Frequent strain and hierarchy confusion.
- 50: Readable baseline but inconsistent rhythm.
- 75: Good readability and hierarchy.
- 90: High readability consistency across contexts.
- 100: Reference-grade typographic control.

### 4.2 Layout and Spatial Rhythm (Weight 3)
Indicators:
- Layout creates stable hierarchy and scan paths.

Objective checks:
- Grid and spacing tokens applied consistently.
- No overlap/clipping in supported contexts.

Subjective constraints:
- Dense-state and sparse-state review required.

Evidence:
- E11 layout captures.
- E3 layout/state inventory.
- E16 layout defects.

Anti-gaming:
- Include high-density real content samples.

Tripwire:
- Critical content/control obscured by overlap or clipping.

Anchor tests:
- 0: Spatial structure blocks task flow.
- 25: Frequent collisions and rhythm breaks.
- 50: Basic structure with notable inconsistencies.
- 75: Coherent layout for most tasks.
- 90: Strong spatial hierarchy across contexts.
- 100: Exceptional spatial coherence and resilience.

### 4.3 Color System and Semantic Use (Weight 3)
Indicators:
- Color reinforces meaning consistently and safely.

Objective checks:
- Semantic tokens mapped and applied consistently.
- Status meaning not contradictory across artifacts.

Subjective constraints:
- Reviewer interprets status from color+label with no ambiguity.

Evidence:
- E11 semantic color captures.
- E7 color audit.
- E3 state-token map.

Anti-gaming:
- Cross-screen and cross-document semantic parity sample.

Tripwire:
- Contradictory color semantics create wrong action risk.

Anchor tests:
- 0: Semantic color usage unsafe or contradictory.
- 25: Frequent inconsistency in status colors.
- 50: Primary semantics work, edge ambiguity remains.
- 75: Solid semantic consistency.
- 90: Strong semantic clarity across contexts.
- 100: Complete, scalable semantic color discipline.

### 4.4 Imagery and Iconography Quality (Weight 3)
Indicators:
- Visual assets are interpretable, accurate, and context-fit.

Objective checks:
- Required assets meet clarity and resolution thresholds.
- Icons are distinguishable at deployed sizes.

Subjective constraints:
- Uninvolved reviewer icon interpretation test.

Evidence:
- E11 asset board.
- E8 media alignment.
- E16 asset defects.

Anti-gaming:
- Interpretation test includes unlabeled icon instances.

Tripwire:
- Critical icon/image meaning misleads user action.

Anchor tests:
- 0: Critical visual assets mislead.
- 25: Frequent ambiguity and quality defects.
- 50: Acceptable assets with notable weak points.
- 75: Good clarity and coherence.
- 90: High visual clarity and consistency.
- 100: Exceptional communicative asset quality.

### 4.5 Component and State Consistency (Weight 3)
Indicators:
- Same component pattern behaves consistently everywhere.

Objective checks:
- Required states covered: default, hover, focus, disabled, loading, empty, error.
- Behavioral parity verified across instances.

Subjective constraints:
- Compare at least three real instances per critical component.

Evidence:
- E3 component matrix.
- E11 parity captures.
- E16 inconsistency defects.

Anti-gaming:
- Randomly select component instances outside showcase.

Tripwire:
- Conflicting behavior for same component in critical flow.

Anchor tests:
- 0: Component inconsistency causes major errors.
- 25: Frequent inconsistency in behavior and states.
- 50: Core consistency with edge-state divergence.
- 75: Consistent behavior in primary use.
- 90: High consistency including edge states.
- 100: Complete component-state integrity.

### 4.6 Document/PDF Production Finish (Weight 3)
Indicators:
- Exported artifact is distribution-ready and accessible.

Objective checks:
- Tagged structure valid.
- Bookmarks and metadata present.
- Reading order preserved.
- Print-safe rendering confirmed.

Subjective constraints:
- Reviewer completes full task from exported artifact only.

Evidence:
- E15 preflight.
- E10 post-export link check.
- E11 render board.

Anti-gaming:
- Source-file-only checks are invalid.

Tripwire:
- Untagged or misordered required PDF/doc delivery.

Anchor tests:
- 0: Export artifact unusable or inaccessible.
- 25: Frequent export defects in required paths.
- 50: Basic export quality with recurring issues.
- 75: Reliable production finish with minor defects.
- 90: High export fidelity and accessibility.
- 100: Distribution-grade, accessibility-robust output.

---

## D5 QA, Trust Signals, and Sustainability (14)

### 5.1 Evidence Traceability and Auditability (Weight 3)
Indicators:
- Every score is traceable to raw evidence.

Objective checks:
- Score entries map to evidence IDs and immutable artifacts.
- Independent reviewer reproduces random claims.

Subjective constraints:
- Auditor uninvolved in evidence creation.

Evidence:
- E1-E16 evidence map.

Anti-gaming:
- Random 10% claim replay minimum.

Tripwire:
- Unreproducible claim.

Anchor tests:
- 0: Evidence is missing or non-auditable.
- 25: Traceability weak and partial.
- 50: Traceability present but inconsistent.
- 75: Solid reproducibility for primary claims.
- 90: Strong and reliable audit trail.
- 100: Complete, independent reproducibility.

### 5.2 Performance Experience (Weight 2)
Indicators:
- Interaction performance supports real task flow.

Objective checks:
- Core interactions meet latency targets under realistic constraints.

Subjective constraints:
- Reviewer evaluates perceived responsiveness under throttled conditions.

Evidence:
- E12 traces.
- E1 timed tasks.
- E16 performance defects.

Anti-gaming:
- Warm-cache-only runs invalid.

Tripwire:
- Performance prevents core task completion.

Anchor tests:
- 0: Severe latency blocks use.
- 25: Frequent performance stalls.
- 50: Mixed responsiveness, visible friction.
- 75: Acceptable performance in primary paths.
- 90: Strong performance under realistic load.
- 100: Excellent performance and stability.

### 5.3 Localization and Cultural Fit (Weight 2)
Indicators:
- Locale variants preserve meaning and usability.

Objective checks:
- No critical truncation.
- Date/number/currency formats valid for locale.

Subjective constraints:
- End-to-end review in at least one non-default locale.

Evidence:
- E13 localization audit.
- E11 localized screenshots.
- E16 i18n defects.

Anti-gaming:
- Pseudo-localization mandatory when full locale coverage unavailable.

Tripwire:
- Localized critical copy misleading or cut off.

Anchor tests:
- 0: Localization breaks critical use.
- 25: Widespread truncation/format errors.
- 50: Basic localization with notable defects.
- 75: Reliable localization on primary paths.
- 90: Strong localization quality and cultural fit.
- 100: Excellent localization robustness across supported locales.

### 5.4 Privacy, Consent, and Safety Communication (Weight 2)
Indicators:
- Data choices are clear, explicit, and reversible.

Objective checks:
- Consent options granular.
- Withdrawal path discoverable and functional.

Subjective constraints:
- Reviewer executes refuse and withdraw scenarios.

Evidence:
- E14 flow evidence.
- E9 copy review.
- E16 trust defects.

Anti-gaming:
- Dark-pattern checklist by independent reviewer.

Tripwire:
- Coercive consent or hidden opt-out.

Anchor tests:
- 0: Deceptive or coercive consent UX.
- 25: Significant ambiguity and friction in controls.
- 50: Basic consent controls with clarity gaps.
- 75: Clear and practical consent management.
- 90: Strong transparency and reversibility.
- 100: Exemplary trust communication and control clarity.

### 5.5 Monitoring and Regression Controls (Weight 3)
Indicators:
- Quality safeguards are active post-release.

Objective checks:
- Automated checks cover accessibility, links, visual regressions.
- Alerts and triage process demonstrated.

Subjective constraints:
- Reviewer verifies one seeded regression is detected and triaged.

Evidence:
- E4/E10/E11 historical run logs.
- E16 regression issue logs.

Anti-gaming:
- Validate controls on production-like pipeline branches.

Tripwire:
- No active control despite known recurring defects.

Anchor tests:
- 0: No regression protection.
- 25: Fragile, unreliable checks.
- 50: Partial coverage with blind spots.
- 75: Reliable controls for key risks.
- 90: Broad, stable monitoring coverage.
- 100: Comprehensive, reliable, and continuously enforced controls.

### 5.6 Design System Governance (Weight 2)
Indicators:
- Consistency is maintained through explicit ownership and standards.

Objective checks:
- Versioned tokens/components with ownership and deprecation policy.

Subjective constraints:
- Reviewer traces one change across lifecycle and verifies rollout integrity.

Evidence:
- E3 governance inventory.
- E11 conformance captures.
- E16 governance defects.

Anti-gaming:
- Audit local overrides and exception inventory.

Tripwire:
- Uncontrolled overrides cause critical inconsistency.

Anchor tests:
- 0: No governance; inconsistency unmanaged.
- 25: Governance exists nominally but ineffective.
- 50: Basic governance with gaps in enforcement.
- 75: Functional governance for primary system areas.
- 90: Strong governance and controlled change behavior.
- 100: Mature governance with high consistency resilience.

---

## Visual-Review Calibration Matrix
Use this matrix to normalize reviewer judgments for D4 and the visual portions of D1 and D3.

Rules:
- If two or more rows score 25 or below, D4 cannot exceed 50.
- If any row scores 0 with tripwire evidence, D4 anchor is forced to 0 until remediation and retest.

| Visual Signal | 0 | 25 | 50 | 75 | 90 | 100 |
|---|---|---|---|---|---|---|
| Hierarchy and Focus | No discernible priority; critical actions disappear | Weak priority cues; frequent misfocus | Basic hierarchy exists but unstable | Clear hierarchy in most states | Strong hierarchy across contexts | Unambiguous hierarchy even in edge/failure states |
| Typography Discipline | Illegible critical text | Legible only under favorable conditions | Readable baseline, weak long-form rhythm | Good readability and type hierarchy | High readability consistency | Reference-grade typographic system |
| Spacing and Rhythm | Crowded/fragmented flow | Uneven spacing causes scan failure | Mixed rhythm, occasional collisions | Coherent spacing on primary paths | Strong rhythm in dense and sparse states | Exceptional spatial coherence and cognitive flow |
| Color Semantics | Contradictory or unsafe color meaning | Frequent semantic drift | Basic status color coding with ambiguity | Stable semantic coding plus labels | Strong semantic clarity across contexts | Highly reliable, scalable semantic color language |
| Asset Clarity | Critical icons/images misleading | Frequent ambiguity/pixelation | Mostly acceptable with notable weak assets | Clear assets for key tasks | High clarity and cohesive style | Exceptional communicative asset quality |
| State Completeness | Critical states missing | Partial state coverage | Core states covered; edge states weak | Most states complete and coherent | Full state coverage with strong consistency | Exhaustive state integrity across contexts |
| Document Finish | Export/read order failures | Frequent export/accessibility defects | Basic export quality with recurring issues | Reliable export and navigation | High fidelity and accessibility | Distribution-grade output with robust accessibility |
| Credibility Signal | Visual quality undermines trust | Noticeable debt reduces confidence | Adequate but generic quality | Trustworthy and coherent craft | Strongly credible execution | Premium, durable, highly credible quality |

---

## Objective Check Protocol by Artifact Type

### Software/Web
- Validate primary tasks with E1/E12 under realistic device/network profiles.
- Run E4 automated scan and E5/E6 manual accessibility checks.
- Verify responsive behavior and state consistency via E11 and E3.
- Execute adverse tasks including input errors, timeout/retry, empty data, and permission denial.

### Documentation
- Validate scannability, heading hierarchy, terminology consistency, and retrieval.
- Confirm reference integrity with E10 and IA mapping with E2.
- For interactive docs, include keyboard and screen-reader behavior.
- Validate export and print workflows where required.

### PDF
- Perform full E15 preflight checks: tagging, reading order, bookmark integrity, metadata.
- Verify selectable text, logical heading structure, and link correctness.
- Confirm accessibility behavior in mainstream readers with E6 where possible.
- Test navigation aids and deep-link references in distributed binaries.

---

## Scoring Procedure (Operational)
1. Gather evidence set E1-E16 and verify version integrity.
2. Execute objective checks across all 30 sub-dimensions.
3. Conduct independent subjective scoring under constraints.
4. Apply anti-gaming caps and tripwire overrides.
5. Assign anchor per sub-dimension using allowed anchors only.
6. Compute dimension and total weighted scores.
7. Record all defects by severity and owner with due dates.
8. Trigger remediation for any tripwire and rerun affected checks.
9. Finalize release recommendation with explicit pass/fail gates.

### Rounding and Tie Rules
- No interpolation between anchors.
- When evidence spans two anchors, assign the lower anchor unless objective threshold for higher anchor is fully met.
- In reviewer disputes, the lower anchor is binding until reconciliation rerun is complete.

---

## Scorecard Template (Required Fields)

| Field | Requirement |
|---|---|
| Artifact ID/version | Mandatory and immutable |
| Evaluator IDs and roles | Mandatory |
| Sub-dimension anchor | Mandatory, one of 0/25/50/75/90/100 |
| Objective results summary | Mandatory with metric values |
| Subjective rationale | Mandatory with evidence IDs |
| Evidence references | Mandatory, at least one per claim |
| Anti-gaming checks executed | Mandatory yes/no with notes |
| Tripwire status | Mandatory pass/fail |
| Defects and owners | Mandatory if score <100 |
| Retest status | Mandatory for remediated items |

Failure to populate required scorecard fields caps affected sub-dimension at 50.

---

## Strict Enforcement Notes
- Do not award points for intent, effort, roadmap plans, or verbal assurances.
- Do not award scores above 50 for unresolved accessibility defects lacking retest evidence.
- Do not award scores above 75 if edge states are untested.
- Do not average away tripwires; tripwire rules override weighted arithmetic.
- If observed behavior conflicts with documentation claims, observed behavior governs.
- If evidence is stale or unverifiable, treat claim as failing for current release.
- If compliance-critical content is visually polished but inaccessible, score fails on accessibility and trust dimensions.

## Minimum Pass Profile for Production Approval
All conditions below are mandatory:
- Section score `>=75`.
- D2 score `>=75`.
- No unresolved tripwires.
- Evidence completeness with no critical omissions.
- No major unresolved defects in core user path.

If any condition fails, release is not approved under this rubric section.

---

## Final Evaluator Statement Format
Use this statement verbatim pattern at close of assessment:

`Result: PASS` or `Result: FAIL`

`Section Score: <value>/100`

`Blocking Issues: <count>`

`Tripwires: <none|list>`

`Evidence Completeness: <percent and missing IDs>`

`Required Remediation Before Release: <numbered list>`

This keeps outcomes auditable and non-ambiguous under strict evaluator standards.

---

# Section 6: A6
- source_file: `A6_operability_governance.md`
- scope: Operability, Maintainability, Auditability, Compliance, Lifecycle Governance
- word_count: 5748
- line_count: 352

# A6 Operability-Governance Rubric Section

## 1. Enforcement Scope and Use Model
This section defines strict, enforceable scoring criteria for artifact quality in five governance-heavy dimensions: Operability, Maintainability, Auditability, Compliance, and Lifecycle Governance. It applies to software systems, documentation products, PDF pipelines, and web products. It is intended for use by delivery organizations, internal audit, platform engineering, legal/compliance functions, and release governance councils.

This rubric is not descriptive maturity guidance. It is a control enforcement mechanism with fail conditions and progression gates.

### 1.1 Evaluation Unit
A scored unit is a **controlled artifact scope item**:
1. A deployable software service/application.
2. A documentation corpus or publication system.
3. A PDF generation template and distribution workflow.
4. A web product or web content platform.

Large programs should score each scope item separately before portfolio aggregation.

### 1.2 Non-Waivable Conditions
1. All five top-level dimensions are mandatory.
2. Every dimension has six mandatory sub-dimensions.
3. Scores must use anchor values only: `0`, `25`, `50`, `75`, `90`, `100`.
4. Tripwire failures override computed averages.
5. Evidence must meet admissibility requirements; self-attestation alone is invalid above `25`.

### 1.3 Dimension and Sub-Dimension Hierarchy
**Dimension -> Sub-dimension -> Indicators**

1. **Operability**
1. D1.1 Runbook and On-Call Execution
2. D1.2 Observability and SLO Control
3. D1.3 Deployment, Release, and Rollback Safety
4. D1.4 Incident Response and Learning Closure
5. D1.5 Capacity and Performance Resilience
6. D1.6 Environment and Dependency Operability

2. **Maintainability**
1. D2.1 Architectural Modularity and Coupling
2. D2.2 Standards and Readability Enforcement
3. D2.3 Testability and Regression Safety
4. D2.4 Documentation Maintainability and Source-of-Truth Integrity
5. D2.5 Technical Debt Governance
6. D2.6 Change Efficiency and Recoverability

3. **Auditability**
1. D3.1 End-to-End Traceability
2. D3.2 Evidence Integrity and Retention
3. D3.3 Decision and Exception Logging
4. D3.4 Access Auditability and Tamper Resistance
5. D3.5 Reproducibility and Deterministic Artifact Build
6. D3.6 Audit Readiness and Finding Closure

4. **Compliance**
1. D4.1 Obligations-to-Control Mapping and Accountability
2. D4.2 Data Classification and Handling Control
3. D4.3 Privacy, Consent, and Data Subject Rights
4. D4.4 Security Baseline, Vulnerability, and Secret Management
5. D4.5 Third-Party, OSS, and License Compliance
6. D4.6 Regulatory Reporting and Breach Notification Readiness

5. **Lifecycle Governance**
1. D5.1 Intake, Prioritization, and Risk Triage
2. D5.2 Stage-Gate Authority and Release Approval
3. D5.3 Portfolio Alignment, Ownership, and Sunset Triggers
4. D5.4 Change Governance and CAB Discipline
5. D5.5 KPI/OKR Governance and Review Cadence
6. D5.6 Decommissioning, Archival, and Knowledge Continuity

## 2. Scoring Method: Percent Anchors With Explicit Tests
Each sub-dimension is scored at anchor values only. No interpolation and no partial percentages are allowed.

### 2.1 Mandatory Anchor Tests (`C1`-`C6`)
Every sub-dimension must be evaluated against these six tests:

1. `C1 Definition`: Control objective, owner, scope, and success thresholds are documented and approved.
2. `C2 Coverage`: Control applies to measurable in-scope population percentage.
3. `C3 Execution`: Control runs at required cadence with timestamped records.
4. `C4 Outcome`: Control achieves target risk or reliability outcome.
5. `C5 Independent Assurance`: Reviewer independent from control owner verifies evidence.
6. `C6 Closed Loop`: Findings are corrected and recurrence is measured with demonstrated improvement.

### 2.2 Anchor Table
| Anchor | Required test outcome |
|---|---|
| `0%` | `C1` fails, or no admissible evidence exists for period, or unresolved tripwire active. |
| `25%` | `C1` passes. `C2` below 50% or unknown. `C3` ad hoc. `C4-C6` absent/failing. |
| `50%` | `C1-C3` pass. `C2` = 50-74%. At least one full execution cycle in current quarter. `C4` partially measured, not stable. |
| `75%` | `C1-C4` pass. `C2` = 75-89%. Outcomes met two consecutive cycles. No major control break older than 30 days. |
| `90%` | `C1-C5` pass. `C2` >= 90%. Independent assurance in current cycle; no unresolved major finding. |
| `100%` | `C1-C6` pass. `C2` >= 98% for two consecutive quarters. Demonstrable recurrence reduction and preventive improvement. |

### 2.3 Roll-Up Rules
1. Sub-dimension score equals one anchor value.
2. Dimension score is weighted average of its six sub-dimensions. Default equal weighting unless approved before cycle start.
3. A6 section score is weighted average of five dimensions. Default equal weighting.
4. Round down to nearest whole number.
5. Any tripwire can cap sub-dimension, dimension, or full section score.

## 3. Evidence Admissibility Standard
Evidence is accepted only if all conditions are met:
1. Comes from a system of record with attributable actor identity.
2. Timestamp lies inside freshness window.
3. Tied to control scope and includes denominator definition where percentages are used.
4. Reproducible by an independent reviewer.
5. Retained under legal/policy retention requirements.
6. Not reconstructed after audit notice without operational provenance.

### 3.1 Freshness Windows
| Evidence class | Maximum age at scoring date |
|---|---|
| Operability evidence | 30 days |
| Maintainability evidence | 45 days |
| Auditability evidence | 45 days |
| Compliance evidence | 60 days unless stricter law applies |
| Lifecycle governance evidence | 90 days |

If evidence exceeds freshness window, that sub-dimension cannot score above `50`.

## 4. Anti-Gaming Controls (Mandatory)
These checks apply to all dimensions every cycle:

1. Random sample of at least 10% records per sub-dimension, minimum sample size 5.
2. At least one surprise test per dimension per cycle.
3. Cross-system corroboration: dashboards must reconcile with raw logs, tickets, source history, and release records.
4. Reviewer independence required for anchors `90` and `100`.
5. Denominator integrity verification required for every coverage/outcome metric.
6. Evidence mutations after audit notice must be explicitly logged and approved.
7. Screenshots are supporting artifacts only; not sole evidence above `50`.
8. Waivers must be approved, time-bound, and compensating controls verified.
9. Renaming findings/incidents/debt does not reset recurrence if root cause is same.
10. Metric definition changes mid-cycle require backfilled recalculation or score cap at `50`.

## 5. Tripwire Failure Framework
Tripwires are immediate hard-fail conditions. High performance elsewhere does not offset them.

### 5.1 Severity Effects
| Tripwire class | Mandatory scoring effect |
|---|---|
| `TW-Critical` | Sub-dimension forced to `0`; related dimension capped at `25`; A6 section capped at `50` until independently re-validated. |
| `TW-Major` | Sub-dimension forced to `0`; related dimension capped at `50` until closure verification. |
| `TW-Material` | Sub-dimension capped at `25` until validated remediation evidence exists. |

### 5.2 Escalation Rules
1. Two or more `TW-Critical` in one cycle set A6 score to `0` pending executive remediation review.
2. Any missed mandatory regulatory notification (D4.6) triggers immediate legal escalation and release freeze for affected artifact.
3. Evidence integrity breach (D3.2) invalidates dependent control scores for the period.
4. Unauthorized production release (D5.2) triggers release-process remediation and 100% change sampling next cycle.

## 6. Master Control Table (Large)
The following table is the enforceable control catalog. Each row is evaluated independently.

| ID | Dimension | Sub-dimension | Indicators (explicit tests) | Scoring criteria (anchor-sensitive) | Evidence requirements | Anti-gaming checks | Tripwire failures |
|---|---|---|---|---|---|---|---|
| D1.1 | Operability | Runbook and On-Call Execution | Runbook covers start, stop, rollback, failover, dependency outage, communication paths for each Tier-1 artifact. Quarterly drill pass >= 90%. p95 drill execution <= 15 min. Reachability monthly >= 99%. | `0`: no Tier-1 runbook or no evidence. `25`: runbook exists but outdated/ad hoc drills. `50`: coverage 50-74% and one cycle evidence. `75`: coverage 75-89% with two successful cycles. `90`: >=90% with independent drill witness. `100`: >=98% coverage for two quarters and measurable incident-response improvement. | Versioned runbooks, on-call roster exports, drill tickets, timing logs, remediation actions. | Unannounced drill and live contact test; compare runbook to actual incident timeline. | No runbook for Tier-1; repeated unreachable responder >15 min; Sev1 without incident lead. |
| D1.2 | Operability | Observability and SLO Control | SLIs/SLOs defined for availability, latency, correctness, and publication integrity where applicable. Monitoring covers >=90% Tier-1 flows. Sev1 MTTD p95 <= 5 min. Error budget linked to release governance. | Anchors map to coverage and operational outcomes using `C1-C6`; `90+` requires independent alert-path validation and no major unresolved alerting defects. | Monitoring configs, SLO dashboards (90 days), alert logs, error-budget decisions. | Replay historical fault against rules; reconcile dashboard and raw telemetry. | Outage >15 min with no alert; missing SLO for critical capability; unauthorized alert suppression. |
| D1.3 | Operability | Deployment, Release, and Rollback Safety | Production changes via controlled pipeline with mandatory checks. High-risk changes staged/canary with blast-radius control. Monthly rollback drill p95 <= 10 min. 90-day change failure rate < 15%. | `0`: uncontrolled/manual release path. `25`: controls documented but bypassed. `50`: pipeline used inconsistently. `75`: consistent use, partial independent verification. `90`: >=90% compliant and independent sampled verification. `100`: >=98% compliant across two quarters and sustained failure-rate reduction. | Pipeline logs, release manifests, approval records, rollback drill outputs, CFR report methodology. | Evaluator-selected rollback exercise; detect out-of-band changes. | Manual production deploy without approval; failed rollback drill unresolved; promotion after failed mandatory check. |
| D1.4 | Operability | Incident Response and Learning Closure | Severity matrix and incident command used. Sev1 IC assignment <= 10 min. PIR for Sev1/Sev2 <= 5 business days. Corrective action closure >= 85% by due date. | `75+` requires timely PIR outcomes; `90+` requires independent verification of closed actions; `100` requires recurrence reduction trend over two quarters. | Incident tickets, timeline logs, PIR records, action tracker with timestamps. | Compare PIR claims to chat/log chronology; sample closed actions for actual implementation. | Repeated Sev1 from same root cause with no corrective action; missing PIR; intentional severity downgrading. |
| D1.5 | Operability | Capacity and Performance Resilience | Monthly capacity model update. Load test before expected >20% demand growth. Failover/restore drills twice yearly meeting RTO/RPO. p95 steady-state resource saturation <80%. | `50` requires baseline modeling + one test cycle. `75` requires threshold conformance for two cycles. `90+` requires independent drill witness and demonstrated forecast accuracy. | Capacity plans, load/failover reports, RTO/RPO logs, performance trends. | Independent rerun of load subset; compare synthetic vs real-user patterns. | Sustained >95% saturation without mitigation; failed backup restore unresolved; no capacity model for Tier-1. |
| D1.6 | Operability | Environment and Dependency Operability | IaC or equivalent for environments; weekly drift detection. Stage-prod parity >=95%. Dependency inventory includes owner, criticality, EOL, patch state. High-risk secret rotation <=90 days. | `90+` requires independent parity/drift validation and no unresolved critical drift. `100` requires two-quarter parity stability >=98%. | IaC repos, drift reports, parity outputs, dependency inventory, secret-rotation logs. | Seed known drift in non-prod; spot-check secret age in vault/KMS. | Unknown critical dependency in prod; expired active secret; critical drift unresolved >14 days. |
| D2.1 | Maintainability | Architectural Modularity and Coupling | Architecture boundaries enforced. Cyclic dependencies <=2 per system scope. Ownership explicit. ADR required for material architecture changes. | `0`: no boundaries/owner. `25`: boundaries narrative-only. `50`: partial enforcement. `75`: boundaries enforced on most paths. `90`: independent hotspot/coupling validation. `100`: sustained coupling reduction + recurrence controls. | Dependency graph reports, ADR index, ownership map, enforcement logs. | Compare declared boundaries with actual imports/calls. | Critical module unowned; boundary checks disabled; high-coupling hotspot unmanaged. |
| D2.2 | Maintainability | Standards and Readability Enforcement | Mandatory style/lint/static checks. Complexity thresholds on changed scope. Documentation/PDF/web templates enforced. Non-author qualified review required for normal changes. | Anchor progression driven by gate compliance and review independence. `100` requires stable high compliance and low waiver abuse over two quarters. | CI quality reports, review metadata, template conformance outputs, waiver approvals. | Re-run checks on random merged commits; verify reviewer independence. | Protected-branch bypass without emergency waiver; direct normal-change commit to release branch; expired waivers still active. |
| D2.3 | Maintainability | Testability and Regression Safety | Tier-1 paths include unit, integration, and end-to-end tests. Critical-path coverage >=90%, noncritical >=70%. Flaky test rate <=2% (30-day rolling). Regression suite required pre-release. | `50` requires measurable baseline and execution cadence. `75` requires two-cycle consistency. `90` requires independent seed-defect catch validation. `100` requires recurrence reduction in escaped defects. | Coverage reports mapped to shipped scope, flakiness logs, release test evidence, exception approvals. | Seed defect in non-prod; audit skipped/muted tests. | Release without Tier-1 regression pass; muted failing tests without approved expiry; no test evidence for critical changes. |
| D2.4 | Maintainability | Documentation Maintainability and Source-of-Truth Integrity | Single source of truth for operational and user instructions. Critical doc owner assigned. Review cadence enforced. Behavior-change to doc lag <=5 business days. Broken links <=1%. | `75+` requires measured lag compliance and stale-content controls. `90+` requires independent conflict scan across channels. | Doc repo metadata, ownership register, review logs, link-check results, publication history. | Compare release notes vs doc timestamps; independent link scan. | Contradictory official instructions >14 days; critical docs unowned; stale critical guidance after behavior change. |
| D2.5 | Maintainability | Technical Debt Governance | Debt register with severity, owner, due date, remediation strategy. Quarterly debt capacity >=15% unless approved waiver. Critical overdue debt limited. Monthly debt governance decisions documented. | Anchor outcomes depend on backlog integrity and closure performance. `100` requires sustained reduction in high-risk debt age and incident linkage. | Debt register export, planning capacity records, governance minutes, closure evidence. | Cross-check incident/bug history against debt register; detect relabeling debt as feature. | Critical debt overdue >90 days without sign-off; stale/absent debt register; repeated deferral without authority. |
| D2.6 | Maintainability | Change Efficiency and Recoverability | Track lead time, deployment frequency, change failure rate, MTTR monthly. p75 lead-time target (default <=7 days) and MTTR target (default <=24h Sev1 restore) enforced. Post-change verification >=95%. | `50` requires complete metric instrumentation. `75` requires target adherence across two cycles. `90` requires independent metric recalculation. `100` requires durable improvement with no denominator manipulation. | DORA reports + methodology, incident restore logs, PIR/PIR-lite records, trend charts. | Recompute month from raw events; inspect denominator exclusions. | No metrics for full quarter; repeated Sev1 MTTR >72h with no governance correction; metric manipulation. |
| D3.1 | Auditability | End-to-End Traceability | Bidirectional trace from requirement to design, implementation, test, release, and operation evidence. High-risk requirements trace coverage >=95%. Immutable unique trace IDs. | `75` requires broad coverage and low broken-link rate. `90` requires independent trace walk. `100` requires sustained high coverage with recurrence prevention for breakages. | Trace matrix exports, requirement IDs, release evidence, test mappings, sample results. | Evaluator-selected trace walk on random sample. | High-risk requirement untraceable to shipped and validated artifact; trace mutations without audit trail. |
| D3.2 | Auditability | Evidence Integrity and Retention | Evidence stored with immutability/tamper controls. Records include timestamp, actor, source ID, checksum/signature where possible. Retention rules enforced. Retrieval SLA <=2 business days. | `90+` requires independent integrity test and retrieval test pass. `100` requires two-cycle zero integrity breaches with preventive controls matured. | Repository configs, retention policy + purge logs, access logs, retrieval test records. | Check checksums/signatures on sample; surprise historical retrieval test. | Missing or overwritten records inside retention window; unauthorized evidence writes; retention violation on regulated records. |
| D3.3 | Auditability | Decision and Exception Logging | ADR required for material architecture/security/privacy decisions. Exception register includes rationale, approver, compensating controls, expiry. Monthly review and escalation of expired exceptions. | `75` requires exception cadence control. `90` requires independent validation of compensating controls. `100` requires declining exception age and count for high-risk exceptions. | ADR index, exception register, approval records, monthly review logs. | Sample exception authority validity; verify compensating controls in runtime. | Expired exception active beyond grace period; unauthorized approver; undocumented policy deviation. |
| D3.4 | Auditability | Access Auditability and Tamper Resistance | Privileged actions logged with actor/action/target/before-after/timestamp/session/source. Log integrity alerts active. Quarterly access recertification complete; stale access removed <=5 business days. Correlation IDs support event reconstruction. | `90` requires independent reconstruction success from sampled events. `100` requires sustained recertification and zero critical logging outages. | IAM logs, SIEM data, recertification reports, revocation tickets, correlation event set. | Reconstruct sampled privileged change; compare IAM roster vs active sessions. | Privileged production change with no attributable actor; critical logging disabled without emergency record; stale privileged account active. |
| D3.5 | Auditability | Reproducibility and Deterministic Artifact Build | Pinned dependencies and versioned configs. Same source+input produces same hash or approved deterministic equivalence. Reproducibility tested each release cycle. Provenance signed and archived. | `50` requires baseline deterministic setup. `75` requires routine reproducibility tests. `90` independent rebuild pass. `100` repeated independent reproducibility pass with no critical drift. | Build manifests, lock files, provenance attestations, reproducibility logs. | Evaluator-triggered rebuild; runtime dependency cross-check. | Artifact unreproducible within 24h; invalid/missing provenance signature; unpinned critical dependency in release path. |
| D3.6 | Auditability | Audit Readiness and Finding Closure | Audit packet generated <=2 business days. Mock audit semiannual by independent reviewer. Major findings have owner, due date, and closure evidence. Repeat major finding rate <=10%. | `75` requires packet timeliness and closure workflow. `90` requires independent closure verification. `100` requires sustained low repeat-finding trend. | Audit packet exports, mock audit report, finding tracker, closure validations. | Surprise packet request; sample closed findings for objective proof. | Repeat major finding across consecutive cycles; inability to produce packet in SLA; no independent mock audit in 6 months. |
| D4.1 | Compliance | Obligations-to-Control Mapping and Accountability | Applicable obligations mapped to controls with accountable owner and cadence. Quarterly map review and legal-change updates. Unmapped applicable obligations = 0. | `50` requires baseline map and ownership. `75` requires maintained updates. `90` requires legal independent sample verification. `100` requires stable zero-unmapped status and rapid legal-update incorporation. | Obligation register, control map, ownership list, review logs, legal impact analyses. | Independent legal sample for mapping integrity. | Applicable obligation absent from map; critical control unowned; stale map beyond cadence. |
| D4.2 | Compliance | Data Classification and Handling Control | Full data inventory with classification by sensitivity/jurisdiction. Class-based handling controls enforced: encryption/access/transfer/retention/destruction. Coverage for regulated stores = 100%. Flows updated on material changes. | `75` requires broad enforcement and drift management. `90` requires independent store sampling. `100` requires sustained 100% regulated-store classification and control evidence. | Data inventory exports, control enforcement logs, policy settings, flow diagrams, change logs. | Sample stores for tag integrity; trace regulated element across systems. | Regulated store unclassified; required protections missing; shadow store in production. |
| D4.3 | Compliance | Privacy, Consent, and Data Subject Rights | Lawful basis/consent captured and retrievable. Preference withdrawals propagate within policy SLA. DSAR statutory deadlines met >=99%. Web/PDF tracking honors consent before processing. | `75` requires tested DSAR/consent workflows. `90` requires independent synthetic withdrawal validation. `100` requires sustained statutory compliance with recurrence reduction. | Consent logs, preference propagation records, DSAR tracker, tag/consent configurations. | Synthetic withdrawal test; raw timestamp verification for DSAR SLA. | Missed statutory DSAR deadline; processing after valid withdrawal; undisclosed tracking on regulated surface. |
| D4.4 | Compliance | Security Baseline, Vulnerability, and Secret Management | Hardening baseline applied. Scans at required cadence, internet-facing daily. Patch SLA: critical <=7d, high <=30d unless approved exception. Secret scanning and rotation controls active. | `50` requires operational scan coverage. `75` requires SLA adherence trend. `90` requires independent validation of closure and exceptions. `100` requires sustained SLA compliance and secret hygiene. | Benchmark reports, scan logs, patch tickets, secret-rotation evidence, exception approvals. | Match scanner scope to asset inventory; seed leaked secret in non-prod for detector check. | Exploitable critical vulnerability overdue without approved exception; active hardcoded secret; required scan disabled. |
| D4.5 | Compliance | Third-Party, OSS, and License Compliance | SBOM per release. License scanning blocks prohibited/unknown licenses. Vendor risk assessment pre-onboard and annual refresh. Contract controls tracked. | `75` requires complete release SBOM and active license policy. `90` independent SBOM/license sample pass. `100` sustained zero prohibited-license releases and current critical vendor assessments. | SBOM outputs, license reports, vendor assessments, contract tracker. | Independent SBOM rebuild on sample release; transitive license inspection. | Prohibited license shipped; critical vendor onboarded without assessment; expired vendor review on critical path. |
| D4.6 | Compliance | Regulatory Reporting and Breach Notification Readiness | Reportability decision <=24h after breach confirmation. Jurisdiction timelines mapped. Legal/security approvals recorded. Semiannual breach-notification drill with closure actions. | `75` requires rehearsal evidence and timeline ownership. `90` requires independent drill timing verification. `100` requires sustained drill quality and no missed clocks. | Incident logs, notification playbooks, legal approvals, drill reports, action tracker. | Cross-jurisdiction scenario simulation timed from raw incident stamps. | Missed mandatory notification deadline; inability to establish breach scope due to missing evidence; no legal sign-off on decision. |
| D5.1 | Lifecycle Governance | Intake, Prioritization, and Risk Triage | Work starts only with intake ID containing owner, purpose, risk class, data class, dependencies, expected lifecycle. Triage <=5 business days. Deferred/rejected rationale captured. | `50` requires systematic intake adoption. `75` requires triage SLA adherence. `90` independent sample shows no ghost work. `100` sustained full intake discipline with low reclassification defects. | Intake records, triage board logs, risk outputs, portfolio link records. | Sample active items for missing intake IDs; detect retroactive intake creation. | Work started with no intake/risk class; splitting work to evade triage thresholds. |
| D5.2 | Lifecycle Governance | Stage-Gate Authority and Release Approval | Mandatory gates defined from design to retirement. Named gate authorities and delegation rules. Non-emergency production release requires dual approval (delivery + control owner). Emergency release requires retrospective review. | `75` requires gate process adherence. `90` requires independent authority validation. `100` sustained gate integrity with near-zero approval defects. | Gate templates, approval records, emergency review logs, release decisions. | Validate approver role authority; detect backdated approvals. | Production release without required approvals; unauthorized approver; missing emergency retrospective review. |
| D5.3 | Lifecycle Governance | Portfolio Alignment, Ownership, and Sunset Triggers | Every artifact has business owner + technical steward. Annual viability review of value/risk/cost. Sunset triggers measurable (usage, risk, EOL, contract expiry). Orphaned artifacts corrected <=30 days. | `75` requires complete ownership and annual review adherence. `90` independent sample validates trigger measurability. `100` sustained owner accuracy and timely sunset action. | Ownership registry, annual review packs, sunset criteria, remediation plans. | Cross-check owner assignments with org records; sample stale reviews. | Active artifact ownerless >30 days; obsolete high-risk artifact with no sunset plan; ownership assigned only to generic alias. |
| D5.4 | Lifecycle Governance | Change Governance and CAB Discipline | Objective change classification (standard/normal/emergency). CAB decisions capture risk, rollback, verification plan. Post-implementation review for normal/emergency changes. Emergency-rate trend monitored. | `50` requires reliable class recording and CAB log. `75` requires consistent PIR and class integrity. `90` independent class-reassessment mostly matches recorded class. `100` sustained low abuse of emergency path. | Change records, CAB minutes, PIR files, classification audit reports. | Reclassify sampled changes against policy; verify true emergency evidence. | Emergency change no review <=2 business days; intentional misclassification to bypass controls; normal change lacking rollback plan. |
| D5.5 | Lifecycle Governance | KPI/OKR Governance and Review Cadence | KPI set includes reliability, maintainability, audit readiness, compliance, lifecycle. Monthly review with quorum. Action closure >=85% by due date. Breaches require corrective program by next cycle. | `75` requires reliable cadence and action closure. `90` independent verification of action outcomes. `100` sustained threshold control and proactive corrective governance. | KPI dashboards, meeting logs, attendance, action tracker, escalation records. | Verify minutes vs attendance/calendar; sample closed actions for concrete outcomes. | Two consecutive cycles missed; repeated threshold breaches with no corrective action; quorum absent but decisions marked approved. |
| D5.6 | Lifecycle Governance | Decommissioning, Archival, and Knowledge Continuity | Retirement plan includes migration, retention/legal hold checks, stakeholder comms, redirects for web/PDF, access/secret revocation, knowledge transfer package. Post-retirement validation confirms no critical breakage and archive retrievability. | `50` requires basic retirement checklist use. `75` requires consistent evidence of legal/privacy closure. `90` independent archive retrieval and redirect validation pass. `100` sustained clean retirements with no regulated-data loss incidents. | Decommission checklists, archive attestations, IAM revocation logs, redirect crawl reports, knowledge base records. | Crawl retired URLs/docs; sample archived record retrieval; verify no post-retirement credential activity. | Retirement without legal/retention sign-off; irretrievable regulated records; critical journeys broken due to missing redirects. |

## 7. Lifecycle Control Matrix (Mandatory)
No phase may exit unless all required gate tests pass. Gate failure is a stop condition.

| Lifecycle phase | Mandatory control IDs | Gate tests (all required) | Required evidence at gate | Gate authority | Hard stop conditions |
|---|---|---|---|---|---|
| Intake and Triage | D5.1, D4.1, D4.2, D3.1 | Intake complete with owner and risk class; preliminary data classification complete; obligations mapped at least to control families; trace root created. | Intake ticket, owner acceptance, risk and data-class outputs, obligations snapshot, trace root ID. | Portfolio lead + compliance lead. | No owner; missing risk class; work started pre-intake; regulated-data possibility with no classification. |
| Design and Planning | D2.1, D3.3, D4.3, D1.6 | Architecture boundaries defined; ADR started for material decisions; privacy impact assessed; environment/dependency plan completed. | ADR draft, architecture package, privacy review output, dependency inventory baseline. | Architecture authority + security/privacy reviewer. | Material design with no ADR; unassessed privacy impact; unknown critical dependency. |
| Build and Authoring | D2.2, D2.3, D4.4, D3.5 | Quality checks enforced; required tests implemented and passing; security scans enabled; deterministic build/publish controls active. | CI policy evidence, test inventory and results, scan output, lock files/provenance setup. | Delivery lead + security owner. | Protected checks bypassed; critical tests absent; required scans disabled; unpinned critical dependency. |
| Verification and Pre-Release | D1.2, D1.3, D3.2, D4.5 | SLO and alert coverage thresholds met; rollback test passed; evidence integrity check passed; SBOM/license checks passed. | SLO snapshots, rollback drill logs, evidence-integrity report, SBOM/license report. | Release manager + audit/compliance reviewer. | No detection for Tier-1 outage; rollback failure unresolved; evidence integrity break; prohibited license present. |
| Release Authorization | D5.2, D1.4, D3.4, D4.6 | Dual approvals recorded; incident readiness validated; privileged logging active; reportability ownership clear for regulated incidents. | Signed approvals, on-call readiness confirmation, logging health proof, notification playbook acknowledgment. | Delivery authority + control owner. | Production release missing dual approval; critical logging disabled; no reportability owner. |
| Operate and Monitor | D1.1, D1.2, D1.5, D5.5 | Drill currency valid; SLO within governance thresholds; capacity within guardrails; monthly KPI governance operating. | Drill records, SLO trends, capacity reports, governance minutes/actions. | Operations manager + governance chair. | Repeated unreachable on-call; sustained saturation without mitigation; governance cadence broken. |
| Change and Emergency | D5.4, D1.3, D2.6, D3.3 | Valid change classification; rollback/verification plan complete; metrics updated; exceptions registered with expiry and controls. | CAB records, deployment logs, metric reports, exception register. | CAB chair + change owner. | Emergency change no retrospective review; unapproved exception; no rollback plan for normal change. |
| Periodic Assurance | D3.6, D4.1, D4.4, D4.5 | Mock audit completed; obligations-control map refreshed; vulnerability SLA validated; vendor/license compliance current. | Mock audit report, updated mapping, vuln SLA report, vendor review status and license summary. | Internal audit lead + compliance/security leads. | Repeat major findings unresolved; unmapped applicable obligation; critical vuln overdue without approved exception. |
| Retirement and Decommission | D5.6, D4.2, D4.3, D3.2 | Archive/retention complete; legal holds checked; privacy/DSAR continuity addressed; retrieval and redirect tests pass. | Decommission approvals, archive attestations, legal/privacy sign-off, retrieval and redirect validation output. | Product owner + legal/compliance authority. | Retirement with no legal retention approval; regulated record loss; archive not retrievable. |

## 8. Dimension-Level Evaluation Guidance
This section defines strict interpretation rules so teams cannot score high on formality while failing operational behavior.

### 8.1 Operability (D1)
Operability measures ability to run, detect, recover, and sustain service/document/product integrity under normal and adverse conditions.

Minimum acceptable outcomes:
1. Failures are detected quickly enough to protect users and obligations.
2. Recovery methods are executable by non-authors under pressure.
3. Capacity and dependency drift are preempted, not merely observed.

Dimension-level tripwire trigger examples:
1. Unalerted user-facing outage longer than threshold.
2. Rollback not executable for Tier-1 release.
3. Critical dependency drift unresolved beyond policy.

### 8.2 Maintainability (D2)
Maintainability measures how safely and economically artifacts can be changed without compounding risk.

Minimum acceptable outcomes:
1. Architecture and ownership reduce hidden coupling.
2. Tests and quality controls catch regressions before production/publication.
3. Debt and change metrics are governed and improved, not just recorded.

Dimension-level tripwire trigger examples:
1. Critical releases proceed with muted failing tests.
2. Quality gates repeatedly bypassed on protected branches.
3. Technical debt risks repeatedly deferred without authority.

### 8.3 Auditability (D3)
Auditability measures ability to reconstruct what happened, why, who approved it, and whether controls worked.

Minimum acceptable outcomes:
1. End-to-end trace from requirement through release and operation.
2. Evidence is immutable, retrievable, and attributable.
3. Decisions and exceptions are explicit, time-bound, and reviewable.

Dimension-level tripwire trigger examples:
1. Unattributable privileged production action.
2. Material evidence gap within retention period.
3. Inability to reproduce released artifact.

### 8.4 Compliance (D4)
Compliance measures whether obligations are mapped, controlled, and demonstrated with evidence under real operations.

Minimum acceptable outcomes:
1. No applicable obligation remains unmapped.
2. Data class controls and privacy rights are enforced in real flows.
3. Security and third-party controls prevent known avoidable violations.

Dimension-level tripwire trigger examples:
1. Missed mandatory breach notification timeline.
2. Regulated data store without classification and required controls.
3. Prohibited license released to production/publication.

### 8.5 Lifecycle Governance (D5)
Lifecycle governance measures whether work enters, changes, releases, and exits under controlled authority with clear accountability.

Minimum acceptable outcomes:
1. No unmanaged work enters delivery pipeline.
2. Gate approvals are valid, attributable, and role-authorized.
3. Retirement protects records, users, and continuity obligations.

Dimension-level tripwire trigger examples:
1. Production release with missing required approvals.
2. Repeated emergency-change abuse to evade governance.
3. Retirement without legal/retention sign-off.

## 9. Cross-Artifact Interpretation (Software, Doc, PDF, Web)
| Artifact class | Tier-1 flow definition | Operability focus | Maintainability focus | Auditability and compliance focus |
|---|---|---|---|---|
| Software/API | User-critical runtime transactions and integration paths | SLO detection, rollback drills, failover, incident response | Modular boundaries, regression depth, debt governance, MTTR/lead time | Requirement-to-release traceability, reproducible builds, privileged audit logs, vulnerability/license obligations |
| Documentation system | Critical user procedures, legal/policy statements, operation instructions | Publication reliability, stale-content correction, link integrity, escalation | Source-of-truth rigor, review cadence, template consistency, change lag control | Version and approval traceability, retention of publication evidence, obligation language alignment |
| PDF pipeline | Data-to-template render path and distribution endpoints | Render correctness checks, distribution observability, rollback to previous template/output | Template modularity and version control, regression comparisons for layout/content | Provenance, retention/archive retrieval, legal text correctness, access and disclosure controls |
| Web product | Critical user journeys and compliance-sensitive interactions | Real-user monitoring, staged rollout, capacity/caching resilience | Frontend architecture discipline, flow tests, content maintainability | Consent-before-tracking, DSAR path evidence, third-party script governance, immutable event logs |

## 10. Pass/Fail Policy for This A6 Section
A6 passes only when all criteria below are true:
1. Overall A6 score >= `80`.
2. No dimension score < `75`.
3. D3 Auditability and D4 Compliance each >= `80` for non-regulated scope, >= `90` for regulated scope.
4. Zero unresolved `TW-Critical` tripwires.
5. No lifecycle phase bypass recorded in current window.

Conditional pass:
1. Overall >= `75`.
2. Exactly one dimension in `70-74`.
3. No unresolved `TW-Critical`.
4. Approved corrective program with due dates inside next cycle.

Fail:
1. Any pass condition not met.

## 11. Evaluator Operating Procedure
This procedure is required for consistent enforcement across teams.

1. Freeze scope inventory at assessment start.
2. Confirm control weights and thresholds before collecting evidence.
3. Pull admissible evidence by sub-dimension and freshness windows.
4. Execute anti-gaming checks, including random samples and surprise tests.
5. Score every sub-dimension using anchor tests `C1-C6`.
6. Apply tripwire overrides immediately.
7. Compute dimension and A6 scores using locked weight model.
8. Record every failed indicator as corrective action with owner/due date.
9. Apply lifecycle gate decisions and freeze progression where required.
10. Re-score remediated controls only after independent validation evidence is complete.

## 12. Corrective Action Standard
Every failed indicator requires an action record containing:
1. Root cause statement linked to evidence.
2. Specific control change implemented.
3. Owner and accountable approver.
4. Due date based on risk severity.
5. Verification method and numeric success metric.
6. Recurrence check date.

Closure rules:
1. No measurable verification means action cannot close.
2. Closed actions enter next-cycle sample pool.
3. Recurrence reopens prior finding and can trigger tripwire escalation.

## 13. Audit Packet Requirements (Mandatory Retained Section)
A scope item is audit-ready only if packet contains all elements below. Missing any element is a control deficiency and blocks `90+` for D3.6.

1. Full scorecard for all 30 sub-dimensions with anchor rationale.
2. Evidence index with links, timestamps, owners, retention classes, and admissibility status.
3. Tripwire register with status, severity, disposition, and remediation evidence.
4. Lifecycle gate history for current and previous cycle with approvals and exceptions.
5. Open finding register with risk ratings, owners, due dates, and closure ETA.
6. Independent assurance statement for any sub-dimension scored `90` or `100`.
7. Metric dictionary defining numerators, denominators, and exclusion rules.
8. Change log of control definitions and threshold updates since prior cycle.

Packet timeliness requirement:
1. Complete packet must be producible within `2 business days` of formal request.

Packet integrity requirement:
1. Packet references must resolve to immutable or version-locked evidence artifacts.

## 14. Enforcement Notes for Real Teams
1. This rubric is calibrated to reward demonstrated control execution, not documentation volume.
2. Teams cannot “paper over” weak operations by producing retrospective records.
3. Emergency paths remain available, but emergency use without retrospective control closure reduces scores and can trigger hard stops.
4. The fastest path to high scores is steady control operation with short evidence retrieval latency, independent review hygiene, and measurable recurrence reduction.
5. Portfolio leaders should treat repeated low anchors (`0`, `25`, `50`) as structural risk signals requiring funding and ownership correction, not just tactical remediation.

## 15. Summary of Non-Negotiables
1. Five dimensions, thirty sub-dimensions, all mandatory.
2. Anchor-only scoring at `0/25/50/75/90/100` with explicit `C1-C6` tests.
3. Evidence admissibility, anti-gaming checks, and tripwire overrides are compulsory.
4. Lifecycle control matrix is a gate mechanism with hard stops.
5. Audit packet completeness and retrieval SLAs are enforceable requirements.

This section is intentionally strict. High scores require sustained, independently verifiable control behavior across operations, maintenance, evidence integrity, compliance obligations, and lifecycle authority.

---

# Appendix A: Scoring Workbook Skeleton
Use this table to record operational scores with evidence references.

| Row ID | Section | Dimension | Sub-dimension | Anchor (0/25/50/75/90/100) | Evidence IDs | Reviewer | Notes |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| EX-001 | A1 | ... | ... | 0 | ... | ... | ... |
| EX-002 | A2 | ... | ... | 25 | ... | ... | ... |
| EX-003 | A3 | ... | ... | 50 | ... | ... | ... |
| EX-004 | A4 | ... | ... | 75 | ... | ... | ... |
| EX-005 | A5 | ... | ... | 90 | ... | ... | ... |
| EX-006 | A6 | ... | ... | 100 | ... | ... | ... |

# Appendix B: Minimal Evidence Ledger Schema
```json
{
  "evidence_id": "EV-XXXX",
  "who": "role_or_identity",
  "what": "specific_claim_or_test",
  "where": "path_or_locator",
  "time_utc": "timestamp",
  "rubric_snapshot_id": "iteration_###_snapshot_###",
  "rubric_snapshot_hash": "sha256-of-rubric-snapshot",
  "version": "artifact-or-dataset-version",
  "hash": "sha256-or-equivalent",
  "provenance_chain": {
    "source_system": "system-of-record",
    "provenance_uri": "immutable-record-locator",
    "transform_steps": ["extract", "normalize", "score"]
  },
  "aliases": {
    "version_id": "version",
    "evidence_hash": "hash",
    "provenance_source": "provenance_chain"
  },
  "replayable": true
}
```

# Appendix C: Operating Rule
1. No score above `75` is admissible in any section unless independent review evidence is present in the same iteration.
2. No score above `90` is admissible unless independent review, adversarial challenge, replay, and recomputation evidence are all present in the same iteration.
3. Missing required proof triggers deterministic caps defined in the role and gate sections.
