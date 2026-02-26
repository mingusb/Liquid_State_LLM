#!/usr/bin/env python3
"""Emit AGENTS.md for nested rubric-driven development."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

CANONICAL_COMPANY_ROLES: tuple[tuple[str, str], ...] = (
    ("R0", "Chief Executive Officer"),
    ("R1", "Chief Operating Officer"),
    ("R2", "Chief Financial Officer"),
    ("R3", "Chief Technology Officer"),
    ("R4", "Chief Product Officer"),
    ("R5", "Head of Engineering"),
    ("R6", "Staff Software Engineer"),
    ("R7", "Quality Assurance Lead"),
    ("R8", "Site Reliability Engineer"),
    ("R9", "Security Engineer"),
    ("R10", "Data and Analytics Lead"),
    ("R11", "UX Research and Design Lead"),
    ("R12", "Customer Success Lead"),
    ("R13", "Technical Documentation Lead"),
    ("R14", "Compliance and Risk Officer"),
    ("R15", "Independent External Auditor"),
)
CANONICAL_COMPANY_ROLE_COUNT = len(CANONICAL_COMPANY_ROLES)


def canonical_company_role_catalog_md() -> str:
    return "\n".join(
        f"  - `{role_id}`: {role_name}" for role_id, role_name in CANONICAL_COMPANY_ROLES
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Emit AGENTS.md for a prompt + nested rubric depth"
    )
    p.add_argument("--prompt-file", required=True, help="Path to prompt text file")
    p.add_argument("--depth", required=True, type=int, help="Rubric depth N (>=0)")
    p.add_argument("--output", required=True, help="Output AGENTS.md path")
    p.add_argument(
        "--schema-output",
        default="",
        help="Optional output path for RUBRIC_SCHEMA.json",
    )
    p.add_argument(
        "--project-name",
        default="Nested Rubric-Driven Project",
        help="Project display name",
    )
    p.add_argument(
        "--emitter-version",
        default="v1",
        help="Emitter version tag included in dimensions metadata",
    )
    p.add_argument(
        "--dimensions-output",
        default="",
        help="Optional output path for rubric dimensions at-a-glance markdown",
    )
    p.add_argument(
        "--vision-mode",
        choices=["required", "disabled"],
        default="required",
        help="Default/fallback vision policy for the run",
    )
    return p.parse_args()


def now_utc() -> str:
    return (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def rubric_label(index: int) -> str:
    return f"Rubric {index}"


def rubric_target(index: int) -> str:
    if index == 0:
        return "project artifact(s) from prompt.txt"
    return rubric_label(index - 1)


def rubric_target_collateral(index: int) -> str:
    if index == 0:
        return "ARTIFACT_MANIFEST.md"
    return f"collateral/Rubric_{index - 1}/manifest_iteration_XXX.md"


def rubric_chain(depth: int) -> str:
    return " -> ".join(rubric_label(i) for i in range(depth, -1, -1))


def build_agents_md(*, vision_mode: str) -> str:
    role_catalog_md = canonical_company_role_catalog_md()
    return f"""# AGENTS.md

## 1) Scope And Authority

- The purpose of this document is to ensure transparent, accountable, and safe autonomous execution for each run.
- This document outlines the operating rules for autonomous execution during the current run.
- Instruction precedence (highest to lowest):
  1. Platform, system, or developer safety instructions.
  2. This `AGENTS.md`.
  3. `prompt.txt`.
- If instructions conflict, apply the precedence order above and document the conflict resolution in evidence.
- Runtime inputs are external to this policy:
  - Prompt: `prompt.txt`
  - Depth `N`: `RUN_METADATA.md` field `depth`
  - Vision policy: `RUN_METADATA.md` field `vision_policy` (fallback: `{vision_mode}`)
- Core execution identity: You are a Liquid State Machine on the Edge of Chaos.
- Purpose invariant: improve the project until `prompt.txt` is fully satisfied with traceable evidence.
- The agent must optimize both project artifacts and rubric quality simultaneously.
- Framework and process improvements must be prompt-agnostic; do not introduce artifact-specific execution heuristics keyed to the current prompt unless explicitly required as a deliverable in `prompt.txt`.
- If a trade-off is required, record a decision log entry with:
  - impacted rubric cell(s)
  - attempted mitigations
  - final rationale
  - evidence links
- The agent must not fabricate scores, evidence, or validation results under any circumstances.

## 2) Fast Execution Contract (Authoritative)

- Identity lock sentence (required, exact):
  - `You are a Liquid State Machine on the Edge of Chaos.`
- Mission (required):
  - improve the project until all mandatory `prompt.txt` requirements are satisfied with traceable evidence.
- Canonical iteration order (required):
  1. Snapshot `Rubric_0 .. Rubric_N`.
  2. Build/update collateral manifests for the judged target.
  3. Judge top-down (`Rubric_k` scores `Rubric_(k-1)`).
  4. Author remediation for discovered defects.
  5. Independent judge recheck with adversarial spot checks.
  6. Accept/reject and iterate.
- Per-iteration file floor (required for a valid iteration):
  - `iterations/iteration_XXX/SNAPSHOT.md`
  - `iterations/iteration_XXX/STATUS.md`
  - `iterations/iteration_XXX/SCORE_DELTA.md`
  - `iterations/iteration_XXX/judge_baseline/PRIORITIZED_DEFECTS.md`
  - `iterations/iteration_XXX/author_deltas/DEFECT_BURNDOWN_CHECK.md`
  - `iterations/iteration_XXX/judge_recheck/PRIORITIZED_DEFECTS.md`
  - `iterations/iteration_XXX/judge_recheck/FINAL_DECISION.md`
- Per-run output floor (required before PASS):
  - `ARTIFACT_MANIFEST.md`
  - `PROMPT_SATISFACTION.md`
  - `LIQUID_STATE_IDENTITY.md`
  - `RUBRIC_SCORECARD_SUMMARY.md`
  - `FINAL_STATUS.md`
- Perfect-chain gate (required):
  - decision is `ACCEPT`
  - recheck mean is `100.0`
  - recheck defects are `0`
  - recheck blocking defects are `0`
  - `identity_lock=yes`
  - `prompt_satisfaction=yes`
- Anti-gaming floor (required):
  - no non-zero score without explicit `who/what/where` evidence
  - no hidden post-snapshot edits
  - no unresolved contradictions at accept time
  - no prompt-specific overfit heuristics unless explicitly required by prompt scope
- Non-ambiguity rule:
  - if any explanatory text conflicts with this section, this section wins.
  - if blocked, emit explicit blockers and keep decision `REJECT`.

## 3) Liquid State Machine Identity Doctrine (Explanatory)

- This section explains model vocabulary and failure patterns.
- It does not authorize skipping, delaying, or reordering Section 2 requirements.
- If constrained, execute Section 2 first and use this section as interpretation support.

- Identity axiom: You are a Liquid State Machine on the Edge of Chaos.
- Mission axiom: your purpose is to improve the project until `prompt.txt` is fully satisfied with traceable evidence.
- Reservoir framing:
  - the rubric chain is the reservoir state carrier
  - prompt injection is the driving signal
  - artifacts/collateral are observable traces
  - judge decisions are readout outputs
- Input injection rule:
  - a new prompt must induce measurable mismatch before convergence claims are allowed.
- Edge-of-chaos rule:
  - development must remain in a productive middle regime: non-trivial prompt-linked defects exist, but the system remains evaluable and correctable.
  - trivial near-perfect baselines with cosmetic deltas do not count as meaningful adaptation.
  - catastrophic collapse does not count as productive adaptation.
- Separation rule:
  - adjacent rubric layers must produce non-redundant defect structure; generic duplicated findings indicate weak reservoir separation.
- Fading-memory rule:
  - retain useful historical deltas/evidence while privileging fresh prompt-linked findings when conflict exists.
- Readout reconvergence rule:
  - stability is reached only after perfect chain rechecks plus explicit prompt satisfaction evidence.
- Identity lock rule:
  - each scored iteration must carry explicit identity assertion and `identity_lock=yes`.
  - missing identity lock invalidates convergence claims.
- Anti-rhetoric rule:
  - LSM claims without concrete state-transition artifacts are invalid.
  - required evidence classes: perturbation, corrective deltas, independent recheck, prompt-satisfaction mapping.
- Generalization rule:
  - process improvements must be prompt-agnostic by default; prompt-specific heuristic branching is prohibited unless explicitly required deliverable scope.

### 3.1) State Transition Semantics

- `S0_QUESCENT`: prior stability exists, but is not evidence of suitability for a new prompt.
- `S1_INPUT_INJECTION`: prompt is injected and must be allowed to perturb the chain.
- `S2_RESERVOIR_PERTURBATION`: baseline judging reveals meaningful prompt-linked defects.
- `S3_EDGE_OF_CHAOS_DEVELOPMENT`: remediation proceeds under bounded instability.
- `S4_READOUT_TRAINING`: quality improves but prompt closure may still be incomplete.
- `S5_READOUT_RECONVERGENCE`: independent rechecks verify recovered quality.
- `S6_STABILIZED_READOUT`: stability is accepted only after prompt-complete evidence.
- Illegal shortcut examples:
  - claiming `S1 -> S6` without measured defects and recovery
  - claiming `S3 -> S6` with unresolved contradictions
  - claiming `S5 -> S6` with any unsatisfied prompt requirement

### 3.2) Edge-Of-Chaos Envelope

- Productive instability is required:
  - not trivially stable
  - not catastrophically degraded
  - still auditable and correctable
- Use bounded destabilization thresholds to keep runs in this envelope.
- Baseline findings must be explicitly prompt-linked; synthetic or cosmetic defects do not count.
- Recovery must occur in later iterations, not the same instant as first perturbation evidence.

### 3.3) Identity Lock Protocol

- Identity assertion must be explicit and exact:
  - `You are a Liquid State Machine on the Edge of Chaos.`
- Every scored iteration must carry `identity_lock=yes`.
- Missing identity lock invalidates convergence claims regardless of score values.
- Identity lock is enforcement logic, not style:
  - it binds the run to perturbation -> adaptation -> reconvergence behavior.

### 3.4) Prompt Satisfaction Calculus

- Prompt satisfaction is a hard gate, not a soft quality signal.
- Every mandatory prompt requirement must map to:
  - implementation artifact(s)
  - evidence artifact(s)
  - verification result
  - status marker
- `prompt_satisfaction=yes` is valid only when all mandatory requirements are satisfied and evidenced.
- Any unresolved contradiction affecting a prompt requirement forces `prompt_satisfaction=no`.
- A converged score without prompt-complete mapping is treated as a false readout.
- Prompt text restatement alone is never counted as requirement fulfillment.
- Every satisfaction claim must be independently auditable from produced artifacts.

## 4) Inputs And Outputs

Inputs:
- `prompt.txt`
- `RUN_METADATA.md`
- `RUBRIC_SCHEMA.json`

Required outputs:
- Primary artifact(s) required by `prompt.txt`
  - Primary artifacts are the explicit mandatory deliverables in `prompt.txt` required to satisfy project goals and scoring criteria.
- `rubrics/Rubric_<rubric_index>/iteration_XXX.json` for all rubrics from `Rubric 0` through `Rubric N`
- `scorecards/Rubric_<rubric_index>_grid_iteration_XXX.md` for all rubrics from `Rubric 0` through `Rubric N`
- `collateral/Rubric_<rubric_index>/manifest_iteration_XXX.md` for all rubrics from `Rubric 0` through `Rubric N`
- `collateral/Rubric_<rubric_index>/access_log_iteration_XXX.md` for all rubrics from `Rubric 0` through `Rubric N`
- `RUBRIC_SCORECARD_SUMMARY.md`
- `RUBRIC_DIMENSIONS_AT_A_GLANCE.md`
- `ARTIFACT_MANIFEST.md`
- `PROMPT_SATISFACTION.md`
- `LIQUID_STATE_IDENTITY.md`
- `FINAL_STATUS.md`
- `evidence/iteration_XXX.md`
- `deltas/iteration_XXX.md`
- `contradictions/iteration_XXX.md`
- If vision policy is required: `VISUAL_EVIDENCE_INDEX.md` and `visual/iteration_XXX/*`

## 5) Rubric Chain Contract (Canonical)

- `Rubric 0` scores project artifact quality against `prompt.txt`.
- For every `k >= 1`, `Rubric k` scores `Rubric (k-1)`.
- For configured depth `N`, the required authority chain is:
  `Rubric N -> ... -> Rubric 2 -> Rubric 1 -> Rubric 0`.
- Role-company model contract (mandatory in every rubric):
  - Every rubric JSON must include `company_roles` and `role_sections`.
  - `company_roles` and `role_sections` must cover the canonical 16-role company catalog below.
  - `x_axis` must be exactly the canonical 16 role IDs `R0..R15` in canonical order (no extras, no omissions, no duplicates).
  - `y_axis` must be composed of role-contributed dimensions sourced from `role_sections[*].sub_dimensions`.
  - Every role `R0..R15` must contribute at least 2 dimensions.
  - Every role-contributed dimension must map to one or more concrete X×Y cells via `role_sections[*].covered_cells`.
  - Judges must score collateral-vs-rubric evidence through these role definitions and cite role IDs in findings.
- Canonical 16-role company catalog:
{role_catalog_md}
- Collateral access contract:
  - Every rubric must expose its scored collateral through `collateral/Rubric_<k>/manifest_iteration_XXX.md`.
  - For every `k >= 1`, `Rubric k` must consume scored collateral from `Rubric (k-1)` and record usage in `target_collateral_access_log`.
  - `Rubric k` is invalid if it scores `Rubric (k-1)` without citing the collateral it inspected.
- Quality objective by order:
  - `Rubric 0` must be a high-insight, high-discrimination rubric that drives exceptional end-product quality (not a generic checklist).
  - For every `k >= 1`, `Rubric k` must explicitly improve on `Rubric (k-1)` by increasing clarity, discriminative power, anti-gaming strength, and practical uplift.
  - Dimension names must be human-readable evaluation concepts (not variable identifiers or code-style labels).
  - `Rubric 0` must explicitly cover user/stakeholder outcome quality, technical rigor, robustness under stress/adversarial conditions, and evidence trustworthiness.
- Scoring path:
  - Rubrics may improve iteratively across iterations.
  - Final pass requires every cell in every rubric = `100%` with linked evidence.
  - A lower rubric is accepted only if the rubric directly above it also scores it at `100%`.
  - Default mode is `stability`: execute all adjacency chains in canonical order (`Rubric N -> Rubric (N-1)` down to `Rubric 1 -> Rubric 0`), and treat one full perfect pass as one stability unit.
  - A chain run is perfect only when decision is `ACCEPT`, recheck mean is `100.0`, recheck defects are `0`, recheck blocking defects are `0`, `identity_lock=yes`, and `prompt_satisfaction=yes`.
  - Any non-perfect chain run resets the stability streak.
  - Stability is achieved after one perfect full-chain unit by default (single 100% pass), unless run metadata explicitly overrides the required streak.
- Axis contract:
  - `x_axis` is fixed at 16 categories and must enumerate `R0..R15`.
  - `y_axis` cardinality is adaptive, but dimensions must remain role-contributed and evidence-justified.
  - Fixed or copied `y_axis` templates without explicit evidence-backed rationale are prohibited.
- A rubric must be a decision instrument, not a label list.
  - Every dimension must be operationalized with definition, measurement protocol, evidence expectation, anti-gaming probe, and scoring anchors.
  - Generic one-word dimensions (for example: `Quality`, `Completeness`, `Correctness`) are invalid unless domain-qualified and operationalized.
- Any violation of this contract results in an overall FAIL.
- Task-sculpting mandate:
  - Rubrics must conform to the task, be sculpted by prompt requirements, and transmogrify across iterations to improve prompt success.
  - Every rubric JSON must include:
    - `task_conformance_rationale`
    - `prompt_requirement_trace`
    - `prompt_transmogrification_log`
    - `axis_task_alignment`
  - Every axis dimension in `x_axis` and `y_axis` must be explicitly mapped to prompt-success contribution exactly once (no omissions, no duplicates).
  - Every rubric collateral manifest must include `prompt.txt` so judges score against explicit task requirements.
  - Generic rubrics that do not adapt to prompt-linked defects are invalid.

## 6) Execution Loop

1. Read `prompt.txt`, `RUN_METADATA.md`, and `RUBRIC_SCHEMA.json`.
2. Determine deliverables, constraints, depth `N`, and vision policy.
3. Snapshot all rubric versions and collateral manifests before scoring.
4. Build scored-collateral manifests:
   - `Rubric 0` collateral manifest references project artifacts and project evidence.
   - For every `k >= 1`, `Rubric k` collateral manifest references outputs produced by `Rubric (k-1)`.
5. Judge swarms run top-down:
   - For each `k` from `N` down to `1`, score `Rubric (k-1)` using `Rubric k` with explicit collateral citations.
   - Judges must route scoring through `role_sections`, the fixed role X-axis (`R0..R15`), and role-contributed Y dimensions.
   - Every judge must consume `prompt.txt` before scoring and record `prompt_source: prompt.txt` and `prompt_consumed: yes` in judge artifacts.
   - Emit ordered defect lists with `who/what/where` evidence for each scored target.
6. Author swarms improve rubrics bottom-up:
   - Improve `Rubric 0` to satisfy `Rubric 1`.
   - Improve each higher rubric `Rubric k` (`k>=1`) to satisfy `Rubric (k+1)` when present.
   - Record deltas and evidence immediately after each change.
7. Independent judge swarms re-score each adjacency pair with adversarial spot checks.
8. Accept or reject iteration:
   - Accept only if Section 5 and Section 7 are satisfied.
   - If rejected, start a new iteration and repeat from step 3.
9. For accepted iterations, write all required artifacts, scorecards, and collateral outputs.

## 7) Anti-Gaming Gates

- Do not assign a non-zero score without traceable evidence references.
- Each evidence reference must include mini-metadata:
  - who: contributor/verifier identity
  - what: specific evidence claim
  - where: path or locator to source material
- No hidden rubric edits after scoring snapshot.
- No unresolved contradictions between adjacent rubrics.
- Prioritization defines execution order, not scope exclusion.
- Any newly discovered pass-blocking defect is in-scope for the current iteration when feasible; otherwise it must be explicitly carried with rationale.
- Axis changes must be reflected in both rubric JSON (`axis_change_log`) and `deltas/`.
- Every rubric JSON must include scored-collateral fields:
  - `schema_version` must be exactly `rubric.v2`
  - `company_roles` (minimum 16 entries)
  - `role_sections` (minimum 16 entries)
  - `target_collateral_manifest`
  - `target_collateral_access_log`
  - `target_collateral_coverage_percent`
  - For `Rubric k` (`k>=1`), scored-collateral entries must reference `Rubric (k-1)` outputs.
  - For `Rubric k` (`k>=1`), the collateral manifest must include predecessor artifacts from `rubrics/`, `scorecards/`, `evidence/`, `deltas/`, and `contradictions/`.
- Every rubric JSON must satisfy role-dimension coverage rules:
  - `x_axis` must list exactly `R0..R15` in canonical order.
  - Each `role_sections` entry must provide at least 2 `sub_dimensions`.
  - Each listed `sub_dimension` must be traceably mapped to one or more explicit X×Y cell references in `covered_cells`.
- Every rubric JSON must include explicit axis design fields:
  - `axis_cardinality_rationale`
  - `axis_selection_rationale`
  - `axis_generation_evidence_refs`
  - `axis_alternatives_considered` (must include considered-and-rejected alternatives for both `x` and `y`)
  - In `axis_alternatives_considered`, entries with `kept=true` must fully enumerate the final `x_axis` and `y_axis` names.
- Every rubric JSON must include explicit improvement intent:
  - `Rubric 0` intent must describe how it drives outstanding artifact quality.
  - `Rubric k>0` intent must describe how it improves `Rubric (k-1)` and what weakness it addresses.
  - Improvement intents must be substantive and specific, not single-sentence boilerplate.
- Every rubric JSON must include operational axis specifications:
  - `x_axis_specs`
  - `y_axis_specs`
  - Each spec must include:
    - `name`
    - `definition`
    - `failure_mode`
    - `discriminator`
    - `intervention`
    - `measurement_protocol`
    - `evidence_expectation`
    - `anti_gaming_probe`
    - `example_pass_case`
    - `example_fail_case`
    - `scoring_anchors` (`0`,`50`,`80`,`100`)
  - Specs must be dimension-specific; copy/paste measurement or anti-gaming text across all dimensions is invalid.
- Cell-level scoring must be dimension-specific:
  - Cell rationales and evidence mappings must vary by cell and reflect the actual X×Y interaction, not generic repeated text.
  - A rubric where every cell cites the same evidence bundle or same rationale text is invalid.
- No non-zero cell score without non-empty `collateral_refs` that resolve to the rubric's `target_collateral_manifest`.
- At least one adversarial fail-before/pass-after check per iteration.
- No cosmetic-only score inflation at any rubric.
- No convergence claim without:
  - `LIQUID_STATE_IDENTITY.md` containing exact identity assertion
  - `PROMPT_SATISFACTION.md` showing every prompt requirement as satisfied with evidence mapping
- If vision is required: no visual-quality claim without image evidence and review notes.

## 8) Definition Of Done

- Completion must provide clear, auditable value for users, reviewers, and stakeholders.
- Section 5 (Rubric Chain Contract) is fully satisfied.
- All outputs listed in Section 4 exist and are internally consistent.
- All rubric JSON files validate against `RUBRIC_SCHEMA.json`.
- All anti-gaming gates in Section 7 pass.
- No unresolved contradictions or unresolved blockers remain.

## 9) Failure And Escalation

- If completion is blocked, first attempt at least one creative mitigation strategy and document it.
- If still blocked, create `BLOCKERS.md` with:
  - blocking condition
  - evidence of failure mode
  - attempted remediations
  - explicit unblock request
- Escalation owner (project lead/escalation manager in `RUN_METADATA.md`) should respond within two business days.
- Do not claim PASS when blocked.
- In blocked cases, `FINAL_STATUS.md` must report overall FAIL and list all unmet conditions.
"""


def build_rubric_schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "rubric.v2",
        "type": "object",
        "required": [
            "schema_version",
            "rubric_index",
            "depth",
            "iteration",
            "target",
            "company_roles",
            "role_sections",
            "target_collateral_manifest",
            "target_collateral_access_log",
            "target_collateral_coverage_percent",
            "x_axis",
            "y_axis",
            "x_axis_specs",
            "y_axis_specs",
            "axis_cardinality_rationale",
            "axis_selection_rationale",
            "improvement_intent",
            "axis_generation_evidence_refs",
            "axis_alternatives_considered",
            "cells",
            "rubric_mean_percent",
            "variance_uncovered",
            "axis_change_log",
            "task_conformance_rationale",
            "prompt_requirement_trace",
            "prompt_transmogrification_log",
            "axis_task_alignment",
        ],
        "properties": {
            "schema_version": {"const": "rubric.v2"},
            "rubric_index": {"type": "integer", "minimum": 0},
            "depth": {"type": "integer", "minimum": 0},
            "iteration": {"type": "string", "pattern": "^[0-9]{3}$"},
            "target": {"type": "string", "minLength": 1},
            "company_roles": {
                "type": "array",
                "minItems": CANONICAL_COMPANY_ROLE_COUNT,
                "items": {
                    "type": "object",
                    "required": [
                        "role_id",
                        "role_name",
                        "primary_accountabilities",
                        "evidence_duties",
                    ],
                    "properties": {
                        "role_id": {"type": "string", "pattern": "^R([0-9]|1[0-5])$"},
                        "role_name": {"type": "string", "minLength": 1},
                        "primary_accountabilities": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "evidence_duties": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                    },
                    "additionalProperties": True,
                },
            },
            "role_sections": {
                "type": "array",
                "minItems": CANONICAL_COMPANY_ROLE_COUNT,
                "items": {
                    "type": "object",
                    "required": [
                        "role_id",
                        "section_intent",
                        "concerns",
                        "sub_dimensions",
                        "scoring_focus",
                        "anti_gaming_checks",
                        "evidence_requirements",
                        "covered_axes",
                        "covered_cells",
                    ],
                    "properties": {
                        "role_id": {"type": "string", "pattern": "^R([0-9]|1[0-5])$"},
                        "section_intent": {"type": "string", "minLength": 1},
                        "concerns": {
                            "type": "array",
                            "minItems": 2,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "sub_dimensions": {
                            "type": "array",
                            "minItems": 2,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "scoring_focus": {"type": "string", "minLength": 1},
                        "anti_gaming_checks": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "evidence_requirements": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "covered_axes": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "covered_cells": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                    },
                    "additionalProperties": True,
                },
            },
            "target_collateral_manifest": {
                "type": "array",
                "minItems": 1,
                "items": {"type": "string", "minLength": 1},
                "contains": {"type": "string", "pattern": "(^|/)prompt\\.txt$"},
                "uniqueItems": True,
            },
            "target_collateral_access_log": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": ["path", "purpose", "used_by_cells"],
                    "properties": {
                        "path": {"type": "string", "minLength": 1},
                        "purpose": {"type": "string", "minLength": 1},
                        "used_by_cells": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                    },
                    "additionalProperties": True,
                },
            },
            "target_collateral_coverage_percent": {
                "type": "number",
                "minimum": 0,
                "maximum": 100,
            },
            "x_axis": {
                "type": "array",
                "items": {"type": "string", "minLength": 1},
                "minItems": 1,
                "uniqueItems": True,
            },
            "y_axis": {
                "type": "array",
                "items": {"type": "string", "minLength": 1},
                "minItems": 1,
                "uniqueItems": True,
            },
            "x_axis_specs": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": [
                        "name",
                        "definition",
                        "failure_mode",
                        "discriminator",
                        "intervention",
                        "measurement_protocol",
                        "evidence_expectation",
                        "anti_gaming_probe",
                        "example_pass_case",
                        "example_fail_case",
                        "scoring_anchors",
                    ],
                    "properties": {
                        "name": {"type": "string", "minLength": 1},
                        "definition": {"type": "string", "minLength": 1},
                        "failure_mode": {"type": "string", "minLength": 1},
                        "discriminator": {"type": "string", "minLength": 1},
                        "intervention": {"type": "string", "minLength": 1},
                        "measurement_protocol": {"type": "string", "minLength": 1},
                        "evidence_expectation": {"type": "string", "minLength": 1},
                        "anti_gaming_probe": {"type": "string", "minLength": 1},
                        "example_pass_case": {"type": "string", "minLength": 1},
                        "example_fail_case": {"type": "string", "minLength": 1},
                        "scoring_anchors": {
                            "type": "object",
                            "required": ["0", "50", "80", "100"],
                            "properties": {
                                "0": {"type": "string", "minLength": 1},
                                "50": {"type": "string", "minLength": 1},
                                "80": {"type": "string", "minLength": 1},
                                "100": {"type": "string", "minLength": 1},
                            },
                            "additionalProperties": True,
                        },
                    },
                    "additionalProperties": True,
                },
            },
            "y_axis_specs": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": [
                        "name",
                        "definition",
                        "failure_mode",
                        "discriminator",
                        "intervention",
                        "measurement_protocol",
                        "evidence_expectation",
                        "anti_gaming_probe",
                        "example_pass_case",
                        "example_fail_case",
                        "scoring_anchors",
                    ],
                    "properties": {
                        "name": {"type": "string", "minLength": 1},
                        "definition": {"type": "string", "minLength": 1},
                        "failure_mode": {"type": "string", "minLength": 1},
                        "discriminator": {"type": "string", "minLength": 1},
                        "intervention": {"type": "string", "minLength": 1},
                        "measurement_protocol": {"type": "string", "minLength": 1},
                        "evidence_expectation": {"type": "string", "minLength": 1},
                        "anti_gaming_probe": {"type": "string", "minLength": 1},
                        "example_pass_case": {"type": "string", "minLength": 1},
                        "example_fail_case": {"type": "string", "minLength": 1},
                        "scoring_anchors": {
                            "type": "object",
                            "required": ["0", "50", "80", "100"],
                            "properties": {
                                "0": {"type": "string", "minLength": 1},
                                "50": {"type": "string", "minLength": 1},
                                "80": {"type": "string", "minLength": 1},
                                "100": {"type": "string", "minLength": 1},
                            },
                            "additionalProperties": True,
                        },
                    },
                    "additionalProperties": True,
                },
            },
            "axis_cardinality_rationale": {"type": "string", "minLength": 1},
            "axis_selection_rationale": {"type": "string", "minLength": 1},
            "improvement_intent": {"type": "string", "minLength": 1},
            "axis_generation_evidence_refs": {
                "type": "array",
                "minItems": 1,
                "items": {"type": "string", "minLength": 1},
            },
            "axis_alternatives_considered": {
                "type": "array",
                "minItems": 2,
                "items": {
                    "type": "object",
                    "required": ["axis", "name", "kept", "reason"],
                    "properties": {
                        "axis": {"type": "string", "enum": ["x", "y"]},
                        "name": {"type": "string", "minLength": 1},
                        "kept": {"type": "boolean"},
                        "reason": {"type": "string", "minLength": 1},
                    },
                    "additionalProperties": True,
                },
            },
            "cells": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": [
                        "x",
                        "y",
                        "score_percent",
                        "evidence_refs",
                        "collateral_refs",
                        "rationale",
                    ],
                    "properties": {
                        "x": {"type": "string", "minLength": 1},
                        "y": {"type": "string", "minLength": 1},
                        "score_percent": {"type": "number", "minimum": 0, "maximum": 100},
                        "evidence_refs": {
                            "type": "array",
                            "items": {"type": "string", "minLength": 1},
                        },
                        "collateral_refs": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "rationale": {"type": "string", "minLength": 1},
                    },
                    "additionalProperties": True,
                },
            },
            "rubric_mean_percent": {"type": "number", "minimum": 0, "maximum": 100},
            "variance_uncovered": {
                "type": "array",
                "items": {"type": "string"},
            },
            "task_conformance_rationale": {"type": "string", "minLength": 1},
            "prompt_requirement_trace": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": [
                        "requirement_id",
                        "requirement_text",
                        "addressed_by_axes",
                        "addressed_by_cells",
                        "adaptation_strategy",
                        "evidence_refs",
                    ],
                    "properties": {
                        "requirement_id": {"type": "string", "minLength": 1},
                        "requirement_text": {"type": "string", "minLength": 1},
                        "addressed_by_axes": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "addressed_by_cells": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "adaptation_strategy": {"type": "string", "minLength": 1},
                        "evidence_refs": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                    },
                    "additionalProperties": True,
                },
            },
            "prompt_transmogrification_log": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": [
                        "change_summary",
                        "trigger_requirement_id",
                        "expected_prompt_uplift",
                        "evidence_refs",
                    ],
                    "properties": {
                        "change_summary": {"type": "string", "minLength": 1},
                        "trigger_requirement_id": {"type": "string", "minLength": 1},
                        "expected_prompt_uplift": {"type": "string", "minLength": 1},
                        "evidence_refs": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                    },
                    "additionalProperties": True,
                },
            },
            "axis_task_alignment": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": [
                        "axis_name",
                        "axis_kind",
                        "supported_requirement_ids",
                        "success_mechanism",
                        "failure_if_ignored",
                        "evidence_refs",
                    ],
                    "properties": {
                        "axis_name": {"type": "string", "minLength": 1},
                        "axis_kind": {"type": "string", "enum": ["x", "y"]},
                        "supported_requirement_ids": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "success_mechanism": {"type": "string", "minLength": 1},
                        "failure_if_ignored": {"type": "string", "minLength": 1},
                        "evidence_refs": {
                            "type": "array",
                            "minItems": 1,
                            "items": {"type": "string", "minLength": 1},
                        },
                    },
                    "additionalProperties": True,
                },
            },
            "axis_change_log": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["action", "axis", "from", "to"],
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove", "split", "merge", "rename"],
                        },
                        "axis": {"type": "string", "enum": ["x", "y"]},
                        "from": {"type": "string"},
                        "to": {"type": "string"},
                    },
                    "additionalProperties": True,
                },
            },
            # Backward-compatible optional aliases.
            "cycle": {"type": "string", "pattern": "^[0-9]{3}$"},
            "layer": {"type": "string"},
            "layer_mean_percent": {"type": "number"},
        },
        "additionalProperties": True,
    }


def build_schema_json() -> str:
    return json.dumps(build_rubric_schema(), indent=2) + "\n"


def build_dimensions_md(
    *,
    project_name: str,
    prompt_path: Path,
    depth: int,
    emitter_version: str,
    vision_mode: str,
) -> str:
    generated = now_utc()
    rows = "\n".join(
        f"| {rubric_label(index)} | {rubric_target(index)} | `R0..R15 (fixed)` | "
        f"`(runtime_role_contributed)` | `rubrics/Rubric_{index}/iteration_XXX.json` | "
        f"`{rubric_target_collateral(index)}` |"
        for index in range(depth + 1)
    )
    return f"""# Rubric Dimensions At A Glance

- project_name: `{project_name}`
- generated_utc: `{generated}`
- emitter_version: `{emitter_version}`
- prompt_source: `{prompt_path}`
- depth: `N={depth}`
- vision_mode: `{vision_mode}`
- rubric_chain: `{rubric_chain(depth)}`

This file is a runtime target. `x_axis` is fixed to canonical role IDs `R0..R15`;
`y_axis` is runtime role-contributed and must be filled from `role_sections` in
`rubrics/Rubric_<rubric_index>/iteration_XXX.json` outputs.

| Rubric | Target | X Dimensions | Y Dimensions | Rubric JSON Pattern | Scored Collateral |
| --- | --- | --- | --- | --- | --- |
{rows}
"""


def main() -> int:
    args = parse_args()
    if args.depth < 0:
        raise SystemExit("error: --depth must be >= 0")

    prompt_path = Path(args.prompt_file)
    if not prompt_path.is_file():
        raise SystemExit(f"error: prompt file not found: {prompt_path}")
    prompt_text = prompt_path.read_text(encoding="utf-8")
    if not prompt_text.strip():
        raise SystemExit("error: prompt file is empty")

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    schema_path = (
        Path(args.schema_output) if args.schema_output else out_path.with_name("RUBRIC_SCHEMA.json")
    )
    schema_path.parent.mkdir(parents=True, exist_ok=True)

    out_path.write_text(build_agents_md(vision_mode=args.vision_mode), encoding="utf-8")
    schema_path.write_text(build_schema_json(), encoding="utf-8")

    generated_paths = [str(out_path), str(schema_path)]

    if args.dimensions_output:
        dimensions_path = Path(args.dimensions_output)
        dimensions_path.parent.mkdir(parents=True, exist_ok=True)
        dimensions_md = build_dimensions_md(
            project_name=args.project_name,
            prompt_path=prompt_path,
            depth=args.depth,
            emitter_version=args.emitter_version,
            vision_mode=args.vision_mode,
        )
        dimensions_path.write_text(dimensions_md, encoding="utf-8")
        generated_paths.append(str(dimensions_path))

    print(
        f"generated {', '.join(generated_paths)} "
        f"(depth={args.depth}, emitter={args.emitter_version}, vision_mode={args.vision_mode})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
