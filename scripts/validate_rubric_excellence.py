#!/usr/bin/env python3
"""Validate rubric quality beyond schema compliance.

This validator enforces anti-template and rubric-excellence constraints so runs
cannot pass with generic or copy-pasted rubric content.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path


GENERIC_UNQUALIFIED = {
    "quality",
    "correctness",
    "completeness",
    "consistency",
    "coverage",
    "compliance",
    "reliability",
    "performance",
    "clarity",
    "readability",
    "security",
    "usability",
    "documentation",
    "accuracy",
    "robustness",
    "traceability",
    "integrity",
    "validity",
    "governance",
}

STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "that",
    "this",
    "into",
    "onto",
    "over",
    "under",
    "between",
    "across",
    "through",
    "against",
    "within",
    "about",
    "axis",
    "rubric",
    "layer",
    "check",
    "score",
    "scoring",
    "quality",
}

MEASURE_VERB_RE = re.compile(
    r"\b(measure|verify|check|compute|compare|test|inspect|count|calculate|evaluate|"
    r"attempt|tamper|inject|falsify|mutate|spoof|alter|remove|delete|replay|recompute|"
    r"simulate|perturb|diff|trace|audit)\b",
    flags=re.IGNORECASE,
)

DISCRIMINATOR_RE = re.compile(
    r"\b(distinguish|separate|boundary|differen|discriminat|pass|fail|threshold)\b",
    flags=re.IGNORECASE,
)

MECHANICAL_NAME_RE = re.compile(r"^(?:r|rubric)[ _-]?\d+\b", re.IGNORECASE)
SNAKE_CASE_RE = re.compile(r"^[a-z0-9_]+$")
PROMPT_NUMBERED_REQ_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$")
PROMPT_ACCEPTANCE_HEADER_RE = re.compile(r"^\s*acceptance criteria\s*:\s*$", re.IGNORECASE)
ADAPTATION_VERB_RE = re.compile(
    r"\b(adapt|reshape|refine|tighten|split|merge|reframe|reweight|prioritize|"
    r"transmogrif|evolve|recompose|retune|correct|strengthen)\b",
    flags=re.IGNORECASE,
)
ALIGNMENT_SUCCESS_RE = re.compile(
    r"\b(enable|support|drive|deliver|satisfy|fulfill|achieve|realize|improve|ensure)\b",
    flags=re.IGNORECASE,
)
ALIGNMENT_FAILURE_RE = re.compile(
    r"\b(fail|miss|degrade|regress|risk|break|violate|block|undermine|delay|reject)\b",
    flags=re.IGNORECASE,
)
BROAD_SCORING_FOCUS_RE = re.compile(
    r"\b(complete|completely|full|fully|100|comprehensive|entire)\b",
    flags=re.IGNORECASE,
)
ROLE_AXIS_LABEL_RE = re.compile(r"^(R(?:[0-9]|1[0-5]))(?:\s*[:|-]\s*|\s+)(.+)$")

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
CANONICAL_COMPANY_ROLE_MAP = {role_id: role_name for role_id, role_name in CANONICAL_COMPANY_ROLES}
MIN_COMPANY_ROLE_COUNT = len(CANONICAL_COMPANY_ROLES)
ROLE_AXIS_CONTRACT = "`company_roles/role_sections/x_axis/y_axis` contract"
MIN_ROLE_NAME_LEN = 8
MIN_ROLE_ARRAY_ITEM_LEN = 16
MIN_ROLE_SECTION_INTENT_LEN = 24
MIN_ROLE_SECTION_SCORING_FOCUS_LEN = 24
MIN_ROLE_SECTION_ITEM_LEN = 16


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate nested rubric excellence quality.")
    p.add_argument("--run-dir", required=True, help="Run directory")
    p.add_argument(
        "--json-out",
        default="",
        help="Optional JSON output path for report details",
    )
    return p.parse_args()


def words(text: str) -> list[str]:
    return [w for w in re.findall(r"[A-Za-z0-9]+", text.lower()) if w]


def norm(text: str) -> str:
    return " ".join(words(text))


def token_set(text: str, *, min_len: int = 4) -> set[str]:
    return {w for w in words(text) if len(w) >= min_len and w not in STOPWORDS}


def parse_prompt_requirements(prompt_text: str) -> list[str]:
    lines = prompt_text.splitlines()
    requirements: list[str] = []
    seen: set[str] = set()
    in_acceptance = False

    for raw in lines:
        stripped = raw.strip()
        if not stripped:
            continue
        if PROMPT_ACCEPTANCE_HEADER_RE.match(stripped):
            in_acceptance = True
            continue
        numbered = PROMPT_NUMBERED_REQ_RE.match(stripped)
        if numbered:
            req = numbered.group(2).strip()
            if req and req not in seen:
                requirements.append(req)
                seen.add(req)
            continue
        if in_acceptance:
            if stripped.startswith("- "):
                req = stripped[2:].strip()
                if req and req not in seen:
                    requirements.append(req)
                    seen.add(req)
                continue
            if stripped.endswith(":"):
                in_acceptance = False
    return requirements


def requirement_matches_trace(requirement: str, trace_text: str) -> bool:
    req_norm = norm(requirement)
    trace_norm = norm(trace_text)
    if req_norm and trace_norm and (req_norm in trace_norm or trace_norm in req_norm):
        return True
    req_tokens = token_set(requirement, min_len=4)
    trace_tokens = token_set(trace_text, min_len=4)
    if not req_tokens or not trace_tokens:
        return False
    overlap = req_tokens & trace_tokens
    return len(overlap) >= max(2, min(len(req_tokens), len(trace_tokens)) // 2)


def unique_ratio(values: list[str]) -> float:
    cleaned = [v for v in values if v]
    if not cleaned:
        return 0.0
    return len(set(cleaned)) / len(cleaned)


def as_specs(value: object) -> list[dict]:
    if isinstance(value, list):
        return [v for v in value if isinstance(v, dict)]
    if isinstance(value, dict):
        out = []
        for k, v in value.items():
            if isinstance(v, dict):
                item = dict(v)
                item.setdefault("name", str(k))
                out.append(item)
        return out
    return []


def normalize_spaces(text: str) -> str:
    return " ".join(str(text).strip().split())


def as_nonempty_string_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    out: list[str] = []
    for item in value:
        if not isinstance(item, str):
            continue
        cleaned = normalize_spaces(item)
        if cleaned:
            out.append(cleaned)
    return out


def parse_role_axis_label(label: str) -> tuple[str, str] | None:
    cleaned = normalize_spaces(label)
    if not cleaned:
        return None
    match = ROLE_AXIS_LABEL_RE.match(cleaned)
    if not match:
        return None
    role_id = match.group(1).strip()
    role_name = normalize_spaces(match.group(2))
    if not role_name:
        return None
    return role_id, role_name


def is_canonical_role_axis_label(label: str) -> bool:
    parsed = parse_role_axis_label(label)
    if not parsed:
        return False
    role_id, role_name = parsed
    return CANONICAL_COMPANY_ROLE_MAP.get(role_id) == role_name


def resolve_manifest_ref(ref: str, manifest_set: set[str]) -> str | None:
    cleaned = normalize_spaces(ref)
    if not cleaned or not manifest_set:
        return None

    candidates = [cleaned]
    if "#" in cleaned:
        candidates.append(cleaned.split("#", 1)[0].strip())
    if cleaned.startswith("./"):
        candidates.append(cleaned[2:].strip())
    for candidate in list(candidates):
        if candidate.startswith("./"):
            candidates.append(candidate[2:].strip())

    for candidate in candidates:
        if candidate and candidate in manifest_set:
            return candidate

    # Allow narrative refs that include a concrete manifest path token inline.
    for token in re.findall(r"[A-Za-z0-9_./-]+(?:#[A-Za-z0-9_./:-]+)?", cleaned):
        token_clean = token.strip()
        if not token_clean:
            continue
        token_base = token_clean.split("#", 1)[0].strip()
        if token_clean in manifest_set:
            return token_clean
        if token_base in manifest_set:
            return token_base
        if token_clean.startswith("./") and token_clean[2:] in manifest_set:
            return token_clean[2:]
        if token_base.startswith("./") and token_base[2:] in manifest_set:
            return token_base[2:]

    return None


def manifest_ref_resolves(ref: str, manifest_set: set[str]) -> bool:
    return resolve_manifest_ref(ref, manifest_set) is not None


def manifest_member_path(run_dir: Path, manifest_member: str) -> Path | None:
    cleaned = normalize_spaces(manifest_member)
    if not cleaned:
        return None
    if "#" in cleaned:
        cleaned = cleaned.split("#", 1)[0].strip()
    if cleaned.startswith("./"):
        cleaned = cleaned[2:].strip()
    if not cleaned:
        return None
    path = (run_dir / cleaned).resolve()
    try:
        path.relative_to(run_dir.resolve())
    except ValueError:
        return None
    return path


def manifest_ref_points_to_existing_file(
    ref: str,
    manifest_set: set[str],
    run_dir: Path,
) -> bool:
    manifest_member = resolve_manifest_ref(ref, manifest_set)
    if manifest_member is None:
        return False
    path = manifest_member_path(run_dir, manifest_member)
    return bool(path is not None and path.exists() and path.is_file())


def build_cell_ref_lookup(
    cell_pairs: set[tuple[str, str]],
) -> tuple[dict[str, tuple[str, str]], dict[tuple[str, str], tuple[str, str]]]:
    ref_lookup: dict[str, tuple[str, str]] = {}
    pair_lookup: dict[tuple[str, str], tuple[str, str]] = {}

    for x_name, y_name in cell_pairs:
        x_clean = normalize_spaces(x_name)
        y_clean = normalize_spaces(y_name)
        pair = (x_name, y_name)
        pair_lookup[(x_clean.casefold(), y_clean.casefold())] = pair
        aliases = (
            f"{x_clean} x {y_clean}",
            f"{x_clean} X {y_clean}",
            f"{x_clean}×{y_clean}",
            f"{x_clean} | {y_clean}",
            f"{x_clean}|{y_clean}",
            f"{x_clean}::{y_clean}",
            f"{x_clean} :: {y_clean}",
            f"{x_clean} -> {y_clean}",
            f"{x_clean}->{y_clean}",
            f"{x_clean}, {y_clean}",
            f"{x_clean},{y_clean}",
            f"{x_clean} / {y_clean}",
            f"{x_clean}/{y_clean}",
        )
        for alias in aliases:
            ref_lookup[normalize_spaces(alias).casefold()] = pair

    return ref_lookup, pair_lookup


def resolve_cell_pair_ref(
    ref: str,
    ref_lookup: dict[str, tuple[str, str]],
    pair_lookup: dict[tuple[str, str], tuple[str, str]],
) -> tuple[str, str] | None:
    cleaned = normalize_spaces(ref)
    if not cleaned:
        return None

    direct = ref_lookup.get(cleaned.casefold())
    if direct:
        return direct

    for splitter in (
        r"\s+[xX]\s+",
        r"\s*×\s*",
        r"\s*\|\s*",
        r"\s*::\s*",
        r"\s*->\s*",
        r"\s*,\s*",
        r"\s*/\s*",
    ):
        parts = re.split(splitter, cleaned, maxsplit=1)
        if len(parts) != 2:
            continue
        x_part = normalize_spaces(parts[0]).casefold()
        y_part = normalize_spaces(parts[1]).casefold()
        resolved = pair_lookup.get((x_part, y_part))
        if resolved:
            return resolved

    return None


def pretty_path(path: Path, run_dir: Path) -> str:
    try:
        return str(path.relative_to(run_dir))
    except ValueError:
        return str(path)


def validate_axis_name(name: str, report: ValidationReport, context: str) -> None:
    axis_words = words(name)
    if len(axis_words) < 2:
        report.error(f"{context}: axis name `{name}` must be multi-word")
    if axis_words and len(axis_words) == 1 and axis_words[0] in GENERIC_UNQUALIFIED:
        report.error(f"{context}: axis name `{name}` is generic/unqualified")
    if MECHANICAL_NAME_RE.match(name) and not is_canonical_role_axis_label(name):
        report.error(f"{context}: axis name `{name}` is mechanical; use conceptual phrasing")
    if SNAKE_CASE_RE.match(name) and "_" in name and " " not in name and "-" not in name:
        report.error(f"{context}: axis name `{name}` is code-style snake_case; use readable phrasing")


def ensure_alternatives_cover_final_axes(
    *,
    kept_items: list[dict],
    axis_values: set[str],
    axis_label: str,
) -> bool:
    if not kept_items:
        return False

    by_name = {str(item.get("name", "")).strip() for item in kept_items}
    if by_name == axis_values:
        return True

    for item in kept_items:
        dims = item.get("dimensions")
        if isinstance(dims, list):
            dim_set = {str(d).strip() for d in dims if str(d).strip()}
            if dim_set == axis_values:
                return True

        name = str(item.get("name", "")).strip().lower()
        if f"final_{axis_label}" in name or f"final {axis_label}" in name:
            if all(v.lower() in name for v in axis_values):
                return True

    return False


def validate_rubric_file(
    path: Path,
    run_dir: Path,
    prompt_words: set[str],
    prompt_requirements: list[str],
    report: ValidationReport,
) -> None:
    rel = pretty_path(path, run_dir)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        report.error(f"{rel}: invalid JSON ({exc})")
        return

    rubric_index = data.get("rubric_index")
    if not isinstance(rubric_index, int):
        report.error(f"{rel}: missing/invalid `rubric_index`")
        return
    schema_version = str(data.get("schema_version", "")).strip()
    if schema_version != "rubric.v2":
        report.error(f"{rel}: expected `schema_version`=`rubric.v2`, found `{schema_version or '(missing)'}`")

    target_collateral_manifest_raw = data.get("target_collateral_manifest", [])
    if not isinstance(target_collateral_manifest_raw, list):
        report.error(f"{rel}: `target_collateral_manifest` must be a non-empty array")
        target_collateral_manifest_raw = []
    target_collateral_manifest = [
        str(p).strip() for p in target_collateral_manifest_raw if str(p).strip()
    ]
    if not target_collateral_manifest:
        report.error(f"{rel}: `target_collateral_manifest` must be non-empty")
    manifest_set = set(target_collateral_manifest)
    manifest_lower = [ref.lower() for ref in target_collateral_manifest]
    if manifest_lower and not any(
        ref == "prompt.txt" or ref.endswith("/prompt.txt") for ref in manifest_lower
    ):
        report.error(
            f"{rel}: `target_collateral_manifest` must include `prompt.txt` so judges score against the prompt"
        )
    for idx, manifest_member in enumerate(target_collateral_manifest):
        resolved_member = manifest_member_path(run_dir, manifest_member)
        if resolved_member is None:
            report.error(
                f"{rel}: target_collateral_manifest[{idx}] `{manifest_member}` is invalid or escapes run scope"
            )
            continue
        if not resolved_member.exists() or not resolved_member.is_file():
            report.error(
                f"{rel}: target_collateral_manifest[{idx}] `{manifest_member}` does not exist as a file"
            )

    target_collateral_access_log = data.get("target_collateral_access_log", [])
    if not isinstance(target_collateral_access_log, list) or not target_collateral_access_log:
        report.error(f"{rel}: `target_collateral_access_log` must be a non-empty array")
        target_collateral_access_log = []

    for idx, entry in enumerate(target_collateral_access_log):
        if not isinstance(entry, dict):
            report.error(f"{rel}: target_collateral_access_log[{idx}] must be an object")
            continue
        path_ref = str(entry.get("path", "")).strip()
        purpose = str(entry.get("purpose", "")).strip()
        used_by_cells = entry.get("used_by_cells", [])
        if not path_ref:
            report.error(f"{rel}: target_collateral_access_log[{idx}] missing `path`")
        elif manifest_set and path_ref not in manifest_set:
            report.error(
                f"{rel}: target_collateral_access_log[{idx}] path `{path_ref}` is not in `target_collateral_manifest`"
            )
        elif manifest_set and not manifest_ref_points_to_existing_file(path_ref, manifest_set, run_dir):
            report.error(
                f"{rel}: target_collateral_access_log[{idx}] path `{path_ref}` does not resolve to an existing collateral file"
            )
        if len(purpose) < 16:
            report.error(f"{rel}: target_collateral_access_log[{idx}] purpose is too weak")
        if not isinstance(used_by_cells, list) or not any(str(x).strip() for x in used_by_cells):
            report.error(f"{rel}: target_collateral_access_log[{idx}] requires non-empty `used_by_cells`")

    coverage_percent = data.get("target_collateral_coverage_percent")
    if not isinstance(coverage_percent, (int, float)):
        report.error(f"{rel}: `target_collateral_coverage_percent` must be numeric")
    elif float(coverage_percent) < 100:
        report.error(f"{rel}: `target_collateral_coverage_percent` must be 100 for pass")

    if rubric_index > 0:
        predecessor = f"rubric_{rubric_index - 1}"
        predecessor_refs = [
            ref for ref in target_collateral_manifest if predecessor in ref.lower()
        ]
        if not predecessor_refs:
            report.error(
                f"{rel}: Rubric_{rubric_index} collateral manifest must reference Rubric_{rubric_index - 1} assets"
            )
        required_collateral_tokens = ("rubrics", "scorecards", "evidence", "deltas", "contradictions")
        lower_manifest = manifest_lower
        for token in required_collateral_tokens:
            if not any(token in ref for ref in lower_manifest):
                report.error(
                    f"{rel}: Rubric_{rubric_index} collateral manifest should include `{token}` artifacts from Rubric_{rubric_index - 1}"
                )

    x_axis = data.get("x_axis", [])
    y_axis = data.get("y_axis", [])
    if not isinstance(x_axis, list) or not isinstance(y_axis, list):
        report.error(f"{rel}: `x_axis` and `y_axis` must both be arrays")
        return
    x_axis = [str(x).strip() for x in x_axis if str(x).strip()]
    y_axis = [str(y).strip() for y in y_axis if str(y).strip()]

    if not x_axis or not y_axis:
        report.error(f"{rel}: axes cannot be empty")
        return
    if set(x_axis) & set(y_axis):
        report.error(f"{rel}: x/y dimensions must be disjoint")

    for axis_name in x_axis:
        validate_axis_name(axis_name, report, f"{rel} x_axis")
    for axis_name in y_axis:
        validate_axis_name(axis_name, report, f"{rel} y_axis")

    if len(x_axis) != MIN_COMPANY_ROLE_COUNT:
        report.error(
            f"{rel}: {ROLE_AXIS_CONTRACT} violation: `x_axis` must contain exactly {MIN_COMPANY_ROLE_COUNT} canonical role labels (`R0`..`R15` with canonical role names)"
        )

    x_axis_role_ids: list[str] = []
    for idx, axis_label in enumerate(x_axis):
        parsed = parse_role_axis_label(axis_label)
        if not parsed:
            report.error(
                f"{rel}: {ROLE_AXIS_CONTRACT} violation: x_axis[{idx}] `{axis_label}` must use canonical role label format `R# <canonical role name>`"
            )
            continue
        role_id, role_name = parsed
        expected_role_name = CANONICAL_COMPANY_ROLE_MAP.get(role_id)
        if expected_role_name is None:
            report.error(
                f"{rel}: {ROLE_AXIS_CONTRACT} violation: x_axis[{idx}] `{axis_label}` uses unknown role id `{role_id}`; expected `R0`..`R15`"
            )
            continue
        if role_name != expected_role_name:
            report.error(
                f"{rel}: {ROLE_AXIS_CONTRACT} violation: x_axis[{idx}] `{axis_label}` must match canonical label `{role_id} {expected_role_name}`"
            )
            continue
        x_axis_role_ids.append(role_id)

    if len(x_axis_role_ids) != len(set(x_axis_role_ids)):
        duplicates = sorted(
            role_id for role_id in set(x_axis_role_ids) if x_axis_role_ids.count(role_id) > 1
        )
        report.error(
            f"{rel}: {ROLE_AXIS_CONTRACT} violation: `x_axis` contains duplicate canonical role ids {duplicates}"
        )

    canonical_role_ids = [role_id for role_id, _ in CANONICAL_COMPANY_ROLES]
    missing_role_ids = sorted(set(canonical_role_ids) - set(x_axis_role_ids))
    extra_role_ids = sorted(set(x_axis_role_ids) - set(canonical_role_ids))
    if missing_role_ids or extra_role_ids:
        report.error(
            f"{rel}: {ROLE_AXIS_CONTRACT} violation: `x_axis` must map exactly to canonical role ids R0..R15; missing={missing_role_ids} extra={extra_role_ids}"
        )
    if len(x_axis_role_ids) == MIN_COMPANY_ROLE_COUNT and x_axis_role_ids != canonical_role_ids:
        report.error(
            f"{rel}: {ROLE_AXIS_CONTRACT} violation: `x_axis` canonical role ids must be ordered exactly as R0..R15"
        )

    improvement_intent = str(data.get("improvement_intent", "")).strip()
    if not improvement_intent:
        report.error(f"{rel}: missing `improvement_intent`")
    elif len(improvement_intent) < 120:
        report.error(f"{rel}: `improvement_intent` is too short")

    if rubric_index == 0:
        lower_intent = improvement_intent.lower()
        if not re.search(r"\b(artifact|document|output|product|deliverable)\b", lower_intent):
            report.error(f"{rel}: Rubric_0 improvement intent must target artifact/document excellence")
        if not re.search(
            r"\b(users?|audiences?|readers?|operators?|stakeholders?)\b", lower_intent
        ):
            report.error(f"{rel}: Rubric_0 improvement intent should explicitly address user/stakeholder value")
    else:
        lower_intent = improvement_intent.lower()
        prev_ref_a = f"rubric_{rubric_index - 1}"
        prev_ref_b = f"rubric {rubric_index - 1}"
        if prev_ref_a not in lower_intent and prev_ref_b not in lower_intent:
            report.error(
                f"{rel}: Rubric_{rubric_index} improvement intent must reference Rubric_{rubric_index - 1}"
            )
        if not re.search(r"\b(weakness|gap|failure|blind spot|shortcoming|defect)\b", lower_intent):
            report.error(
                f"{rel}: Rubric_{rubric_index} improvement intent must name predecessor weaknesses"
            )
        if not re.search(r"\b(improve|strengthen|upgrade|correct|tighten|elevate)\b", lower_intent):
            report.error(
                f"{rel}: Rubric_{rubric_index} improvement intent must describe concrete improvement action"
            )

    required_text_fields = (
        "axis_cardinality_rationale",
        "axis_selection_rationale",
    )
    for field_name in required_text_fields:
        field_value = str(data.get(field_name, "")).strip()
        if len(field_value) < 24:
            report.error(f"{rel}: `{field_name}` is missing or weak")

    refs = data.get("axis_generation_evidence_refs", [])
    if not isinstance(refs, list) or not refs or not any(str(x).strip() for x in refs):
        report.error(f"{rel}: `axis_generation_evidence_refs` must be a non-empty list")

    task_conformance_rationale = str(data.get("task_conformance_rationale", "")).strip()
    if len(task_conformance_rationale) < 80:
        report.error(f"{rel}: `task_conformance_rationale` is too weak")

    all_axis_values = set(x_axis) | set(y_axis)

    company_roles_raw = data.get("company_roles", [])
    if not isinstance(company_roles_raw, list):
        report.error(f"{rel}: `company_roles` must be an array with >= {MIN_COMPANY_ROLE_COUNT} entries")
        company_roles_raw = []
    if len(company_roles_raw) < MIN_COMPANY_ROLE_COUNT:
        report.error(
            f"{rel}: `company_roles` must contain at least {MIN_COMPANY_ROLE_COUNT} entries"
        )

    company_role_id_set: set[str] = set()
    for idx, entry in enumerate(company_roles_raw):
        if not isinstance(entry, dict):
            report.error(f"{rel}: company_roles[{idx}] must be an object")
            continue

        role_id = str(entry.get("role_id", "")).strip()
        role_name = normalize_spaces(str(entry.get("role_name", "")))
        primary_accountabilities_raw = entry.get("primary_accountabilities", [])
        evidence_duties_raw = entry.get("evidence_duties", [])
        primary_accountabilities = as_nonempty_string_list(primary_accountabilities_raw)
        evidence_duties = as_nonempty_string_list(evidence_duties_raw)

        if not role_id:
            report.error(f"{rel}: company_roles[{idx}] missing `role_id`")
        elif role_id in company_role_id_set:
            report.error(f"{rel}: company_roles has duplicate role_id `{role_id}`")
        else:
            company_role_id_set.add(role_id)

        if len(role_name) < MIN_ROLE_NAME_LEN:
            report.error(f"{rel}: company_roles[{idx}] `role_name` is too short")

        if not isinstance(primary_accountabilities_raw, list) or not primary_accountabilities:
            report.error(
                f"{rel}: company_roles[{idx}] `primary_accountabilities` must be a non-empty array"
            )
        else:
            for item_idx, text in enumerate(primary_accountabilities):
                if len(text) < MIN_ROLE_ARRAY_ITEM_LEN:
                    report.error(
                        f"{rel}: company_roles[{idx}] primary_accountabilities[{item_idx}] is too short"
                    )

        if not isinstance(evidence_duties_raw, list) or not evidence_duties:
            report.error(f"{rel}: company_roles[{idx}] `evidence_duties` must be a non-empty array")
        else:
            for item_idx, text in enumerate(evidence_duties):
                if len(text) < MIN_ROLE_ARRAY_ITEM_LEN:
                    report.error(
                        f"{rel}: company_roles[{idx}] evidence_duties[{item_idx}] is too short"
                    )

    role_sections_raw = data.get("role_sections", [])
    if not isinstance(role_sections_raw, list):
        report.error(f"{rel}: `role_sections` must be an array with >= {MIN_COMPANY_ROLE_COUNT} entries")
        role_sections_raw = []
    if len(role_sections_raw) < MIN_COMPANY_ROLE_COUNT:
        report.error(
            f"{rel}: `role_sections` must contain at least {MIN_COMPANY_ROLE_COUNT} entries"
        )

    y_axis_set = set(y_axis)
    role_section_id_set: set[str] = set()
    role_section_sub_dimensions_union: list[str] = []
    role_section_sub_dimensions_seen: set[str] = set()
    role_sections_for_cell_validation: list[tuple[int, str, str, list[str]]] = []
    for idx, entry in enumerate(role_sections_raw):
        if not isinstance(entry, dict):
            report.error(f"{rel}: role_sections[{idx}] must be an object")
            continue

        role_id = str(entry.get("role_id", "")).strip()
        section_intent = normalize_spaces(str(entry.get("section_intent", "")))
        concerns_raw = entry.get("concerns", [])
        sub_dimensions_raw = entry.get("sub_dimensions", [])
        scoring_focus = normalize_spaces(str(entry.get("scoring_focus", "")))
        anti_gaming_checks_raw = entry.get("anti_gaming_checks", [])
        evidence_requirements_raw = entry.get("evidence_requirements", [])
        covered_axes_raw = entry.get("covered_axes", [])
        covered_cells_raw = entry.get("covered_cells", [])

        concerns = as_nonempty_string_list(concerns_raw)
        sub_dimensions = as_nonempty_string_list(sub_dimensions_raw)
        anti_gaming_checks = as_nonempty_string_list(anti_gaming_checks_raw)
        evidence_requirements = as_nonempty_string_list(evidence_requirements_raw)
        covered_axes = as_nonempty_string_list(covered_axes_raw)
        covered_cells = as_nonempty_string_list(covered_cells_raw)

        if not role_id:
            report.error(f"{rel}: role_sections[{idx}] missing `role_id`")
        elif role_id in role_section_id_set:
            report.error(f"{rel}: role_sections has duplicate role_id `{role_id}`")
        else:
            role_section_id_set.add(role_id)

        if len(section_intent) < MIN_ROLE_SECTION_INTENT_LEN:
            report.error(f"{rel}: role_sections[{idx}] `section_intent` is too short")

        if not isinstance(concerns_raw, list) or len(concerns) < 2:
            report.error(f"{rel}: role_sections[{idx}] `concerns` must contain at least 2 entries")
        else:
            for item_idx, text in enumerate(concerns):
                if len(text) < MIN_ROLE_SECTION_ITEM_LEN:
                    report.error(f"{rel}: role_sections[{idx}] concerns[{item_idx}] is too short")

        if not isinstance(sub_dimensions_raw, list) or len(sub_dimensions) < 2:
            report.error(
                f"{rel}: role_sections[{idx}] `sub_dimensions` must contain at least 2 entries"
            )
        else:
            for item_idx, text in enumerate(sub_dimensions):
                if len(text) < MIN_ROLE_SECTION_ITEM_LEN:
                    report.error(
                        f"{rel}: role_sections[{idx}] sub_dimensions[{item_idx}] is too short"
                    )
        for item_idx, text in enumerate(sub_dimensions):
            if text not in y_axis_set:
                report.error(
                    f"{rel}: {ROLE_AXIS_CONTRACT} violation: role_sections[{idx}] sub_dimensions[{item_idx}] `{text}` must appear in `y_axis`"
                )
            if text not in role_section_sub_dimensions_seen:
                role_section_sub_dimensions_seen.add(text)
                role_section_sub_dimensions_union.append(text)

        if len(scoring_focus) < MIN_ROLE_SECTION_SCORING_FOCUS_LEN:
            report.error(f"{rel}: role_sections[{idx}] `scoring_focus` is too short")

        if not isinstance(anti_gaming_checks_raw, list) or not anti_gaming_checks:
            report.error(
                f"{rel}: role_sections[{idx}] `anti_gaming_checks` must be a non-empty array"
            )
        else:
            for item_idx, text in enumerate(anti_gaming_checks):
                if len(text) < MIN_ROLE_SECTION_ITEM_LEN:
                    report.error(
                        f"{rel}: role_sections[{idx}] anti_gaming_checks[{item_idx}] is too short"
                    )

        if not isinstance(evidence_requirements_raw, list) or not evidence_requirements:
            report.error(
                f"{rel}: role_sections[{idx}] `evidence_requirements` must be a non-empty array"
            )
        else:
            for item_idx, ref in enumerate(evidence_requirements):
                if not manifest_ref_resolves(ref, manifest_set):
                    report.error(
                        f"{rel}: role_sections[{idx}] evidence_requirements[{item_idx}] `{ref}` does not resolve to `target_collateral_manifest`"
                    )
                elif not manifest_ref_points_to_existing_file(ref, manifest_set, run_dir):
                    report.error(
                        f"{rel}: role_sections[{idx}] evidence_requirements[{item_idx}] `{ref}` does not resolve to an existing collateral file"
                    )

        if not isinstance(covered_axes_raw, list) or not covered_axes:
            report.error(f"{rel}: role_sections[{idx}] `covered_axes` must be a non-empty array")
        else:
            for axis_ref in covered_axes:
                if axis_ref not in all_axis_values:
                    report.error(
                        f"{rel}: role_sections[{idx}] covered_axes includes unknown axis `{axis_ref}`"
                    )

        if not isinstance(covered_cells_raw, list) or not covered_cells:
            report.error(f"{rel}: role_sections[{idx}] `covered_cells` must be a non-empty array")

        role_sections_for_cell_validation.append((idx, role_id, scoring_focus, covered_cells))

    if len(y_axis) != len(y_axis_set):
        report.error(
            f"{rel}: {ROLE_AXIS_CONTRACT} violation: `y_axis` must contain unique entries because it is the unique union of `role_sections[].sub_dimensions`"
        )
    role_section_sub_dimensions_set = set(role_section_sub_dimensions_union)
    if y_axis_set != role_section_sub_dimensions_set:
        missing_in_y_axis = sorted(role_section_sub_dimensions_set - y_axis_set)
        extra_in_y_axis = sorted(y_axis_set - role_section_sub_dimensions_set)
        report.error(
            f"{rel}: {ROLE_AXIS_CONTRACT} violation: `y_axis` must equal the unique union of `role_sections[].sub_dimensions`; missing_in_y_axis={missing_in_y_axis} extra_in_y_axis={extra_in_y_axis}"
        )

    if company_role_id_set:
        missing_sections = sorted(company_role_id_set - role_section_id_set)
        if missing_sections:
            report.error(
                f"{rel}: role_sections is missing entries for company_roles role_id values {missing_sections}"
            )
    if company_role_id_set and role_section_id_set:
        unknown_sections = sorted(role_section_id_set - company_role_id_set)
        if unknown_sections:
            report.error(
                f"{rel}: role_sections contains role_id values not present in company_roles: {unknown_sections}"
            )

    trace_entries = data.get("prompt_requirement_trace", [])
    if not isinstance(trace_entries, list) or not trace_entries:
        report.error(f"{rel}: `prompt_requirement_trace` must be a non-empty array")
        trace_entries = []
    seen_requirement_ids: set[str] = set()
    trace_requirement_texts: list[str] = []
    for idx, entry in enumerate(trace_entries):
        if not isinstance(entry, dict):
            report.error(f"{rel}: prompt_requirement_trace[{idx}] must be an object")
            continue
        requirement_id = str(entry.get("requirement_id", "")).strip()
        requirement_text = str(entry.get("requirement_text", "")).strip()
        addressed_by_axes = entry.get("addressed_by_axes", [])
        addressed_by_cells = entry.get("addressed_by_cells", [])
        adaptation_strategy = str(entry.get("adaptation_strategy", "")).strip()
        evidence_refs = entry.get("evidence_refs", [])

        if not requirement_id:
            report.error(f"{rel}: prompt_requirement_trace[{idx}] missing requirement_id")
        elif requirement_id in seen_requirement_ids:
            report.error(f"{rel}: duplicate requirement_id `{requirement_id}` in prompt_requirement_trace")
        else:
            seen_requirement_ids.add(requirement_id)

        if len(requirement_text) < 12:
            report.error(f"{rel}: prompt_requirement_trace[{idx}] requirement_text is too weak")
        else:
            trace_requirement_texts.append(requirement_text)

        if not isinstance(addressed_by_axes, list) or not addressed_by_axes:
            report.error(f"{rel}: prompt_requirement_trace[{idx}] addressed_by_axes must be non-empty")
        else:
            for axis_name in addressed_by_axes:
                axis_val = str(axis_name).strip()
                if axis_val not in all_axis_values:
                    report.error(
                        f"{rel}: prompt_requirement_trace[{idx}] addressed_by_axes includes unknown axis `{axis_val}`"
                    )

        if not isinstance(addressed_by_cells, list) or not addressed_by_cells:
            report.error(f"{rel}: prompt_requirement_trace[{idx}] addressed_by_cells must be non-empty")

        if len(adaptation_strategy) < 24:
            report.error(f"{rel}: prompt_requirement_trace[{idx}] adaptation_strategy is too weak")
        elif not ADAPTATION_VERB_RE.search(adaptation_strategy):
            report.error(
                f"{rel}: prompt_requirement_trace[{idx}] adaptation_strategy must describe rubric adaptation action"
            )

        if not isinstance(evidence_refs, list) or not any(str(x).strip() for x in evidence_refs):
            report.error(f"{rel}: prompt_requirement_trace[{idx}] evidence_refs must be non-empty")

    transmogrification_log = data.get("prompt_transmogrification_log", [])
    if not isinstance(transmogrification_log, list) or not transmogrification_log:
        report.error(f"{rel}: `prompt_transmogrification_log` must be a non-empty array")
        transmogrification_log = []
    for idx, entry in enumerate(transmogrification_log):
        if not isinstance(entry, dict):
            report.error(f"{rel}: prompt_transmogrification_log[{idx}] must be an object")
            continue
        change_summary = str(entry.get("change_summary", "")).strip()
        trigger_requirement_id = str(entry.get("trigger_requirement_id", "")).strip()
        expected_prompt_uplift = str(entry.get("expected_prompt_uplift", "")).strip()
        evidence_refs = entry.get("evidence_refs", [])

        if len(change_summary) < 24:
            report.error(f"{rel}: prompt_transmogrification_log[{idx}] change_summary is too weak")
        elif not ADAPTATION_VERB_RE.search(change_summary):
            report.error(
                f"{rel}: prompt_transmogrification_log[{idx}] change_summary must describe structural rubric adaptation"
            )
        if not trigger_requirement_id:
            report.error(f"{rel}: prompt_transmogrification_log[{idx}] missing trigger_requirement_id")
        elif seen_requirement_ids and trigger_requirement_id not in seen_requirement_ids:
            report.error(
                f"{rel}: prompt_transmogrification_log[{idx}] trigger_requirement_id `{trigger_requirement_id}` not found in prompt_requirement_trace"
            )
        if len(expected_prompt_uplift) < 20:
            report.error(f"{rel}: prompt_transmogrification_log[{idx}] expected_prompt_uplift is too weak")
        if not isinstance(evidence_refs, list) or not any(str(x).strip() for x in evidence_refs):
            report.error(f"{rel}: prompt_transmogrification_log[{idx}] evidence_refs must be non-empty")

    if prompt_requirements:
        for requirement in prompt_requirements:
            if not any(
                requirement_matches_trace(requirement, trace_text)
                for trace_text in trace_requirement_texts
            ):
                report.error(
                    f"{rel}: prompt requirement not mapped in prompt_requirement_trace: `{requirement}`"
                )

    axis_task_alignment = data.get("axis_task_alignment", [])
    if not isinstance(axis_task_alignment, list) or not axis_task_alignment:
        report.error(f"{rel}: `axis_task_alignment` must be a non-empty array")
        axis_task_alignment = []

    expected_axis_pairs = {("x", axis_name) for axis_name in x_axis} | {
        ("y", axis_name) for axis_name in y_axis
    }
    covered_axis_pairs: set[tuple[str, str]] = set()
    aligned_requirement_ids: set[str] = set()

    for idx, entry in enumerate(axis_task_alignment):
        if not isinstance(entry, dict):
            report.error(f"{rel}: axis_task_alignment[{idx}] must be an object")
            continue

        axis_name = str(entry.get("axis_name", "")).strip()
        axis_kind = str(entry.get("axis_kind", "")).strip().lower()
        supported_requirement_ids = entry.get("supported_requirement_ids", [])
        success_mechanism = str(entry.get("success_mechanism", "")).strip()
        failure_if_ignored = str(entry.get("failure_if_ignored", "")).strip()
        evidence_refs = entry.get("evidence_refs", [])

        if axis_kind not in {"x", "y"}:
            report.error(f"{rel}: axis_task_alignment[{idx}] axis_kind must be `x` or `y`")
            continue

        axis_pool = set(x_axis) if axis_kind == "x" else set(y_axis)
        if axis_name not in axis_pool:
            report.error(
                f"{rel}: axis_task_alignment[{idx}] axis `{axis_name}` not found in {axis_kind}_axis"
            )
            continue

        pair = (axis_kind, axis_name)
        if pair in covered_axis_pairs:
            report.error(
                f"{rel}: duplicate axis_task_alignment entry for {axis_kind}-axis `{axis_name}`"
            )
        covered_axis_pairs.add(pair)

        if (
            not isinstance(supported_requirement_ids, list)
            or not supported_requirement_ids
            or not all(str(x).strip() for x in supported_requirement_ids)
        ):
            report.error(
                f"{rel}: axis_task_alignment[{idx}] supported_requirement_ids must be non-empty"
            )
        else:
            for requirement_id_raw in supported_requirement_ids:
                requirement_id = str(requirement_id_raw).strip()
                aligned_requirement_ids.add(requirement_id)
                if seen_requirement_ids and requirement_id not in seen_requirement_ids:
                    report.error(
                        f"{rel}: axis_task_alignment[{idx}] unknown requirement_id `{requirement_id}`"
                    )

        if len(success_mechanism) < 24:
            report.error(f"{rel}: axis_task_alignment[{idx}] success_mechanism is too weak")
        elif not ALIGNMENT_SUCCESS_RE.search(success_mechanism):
            report.error(
                f"{rel}: axis_task_alignment[{idx}] success_mechanism must explain how it improves prompt success"
            )

        if len(failure_if_ignored) < 20:
            report.error(f"{rel}: axis_task_alignment[{idx}] failure_if_ignored is too weak")
        elif not ALIGNMENT_FAILURE_RE.search(failure_if_ignored):
            report.error(
                f"{rel}: axis_task_alignment[{idx}] failure_if_ignored must describe prompt-linked risk/failure"
            )

        if not isinstance(evidence_refs, list) or not any(str(x).strip() for x in evidence_refs):
            report.error(f"{rel}: axis_task_alignment[{idx}] evidence_refs must be non-empty")

    if covered_axis_pairs != expected_axis_pairs:
        missing_pairs = sorted(expected_axis_pairs - covered_axis_pairs)
        extra_pairs = sorted(covered_axis_pairs - expected_axis_pairs)
        if missing_pairs:
            report.error(
                f"{rel}: axis_task_alignment missing axis coverage for {missing_pairs}"
            )
        if extra_pairs:
            report.error(
                f"{rel}: axis_task_alignment contains unexpected axis entries {extra_pairs}"
            )

    if seen_requirement_ids and not seen_requirement_ids.issubset(aligned_requirement_ids):
        missing_req_ids = sorted(seen_requirement_ids - aligned_requirement_ids)
        report.error(
            f"{rel}: axis_task_alignment does not link all prompt requirements; missing {missing_req_ids}"
        )

    def validate_specs(specs_key: str, axis_values: list[str]) -> None:
        specs = as_specs(data.get(specs_key, []))
        if not specs:
            report.error(f"{rel}: `{specs_key}` is missing/empty")
            return

        axis_set = set(axis_values)
        names = [str(s.get("name", "")).strip() for s in specs]
        name_set = set(names)
        if name_set != axis_set:
            report.error(
                f"{rel}: `{specs_key}` names must exactly match corresponding axis names"
            )

        definitions = []
        failures = []
        discriminators = []
        interventions = []
        measurements = []
        probes = []

        for spec in specs:
            name = str(spec.get("name", "")).strip()
            definition = str(spec.get("definition", "")).strip()
            failure_mode = str(spec.get("failure_mode", "")).strip()
            discriminator = str(spec.get("discriminator", "")).strip()
            intervention = str(spec.get("intervention", "")).strip()
            measurement = str(spec.get("measurement_protocol", "")).strip()
            expectation = str(spec.get("evidence_expectation", "")).strip()
            anti_gaming = str(spec.get("anti_gaming_probe", "")).strip()
            pass_case = str(spec.get("example_pass_case", "")).strip()
            fail_case = str(spec.get("example_fail_case", "")).strip()
            anchors = spec.get("scoring_anchors", {})

            definitions.append(norm(definition))
            failures.append(norm(failure_mode))
            discriminators.append(norm(discriminator))
            interventions.append(norm(intervention))
            measurements.append(norm(measurement))
            probes.append(norm(anti_gaming))

            if len(definition) < 28:
                report.error(f"{rel}: `{specs_key}` `{name}` definition is too weak")
            if len(failure_mode) < 24:
                report.error(f"{rel}: `{specs_key}` `{name}` failure_mode is too weak")
            if len(discriminator) < 24:
                report.error(f"{rel}: `{specs_key}` `{name}` discriminator is too weak")
            if len(intervention) < 24:
                report.error(f"{rel}: `{specs_key}` `{name}` intervention is too weak")
            if len(measurement) < 32:
                report.error(f"{rel}: `{specs_key}` `{name}` measurement_protocol is too weak")
            if len(expectation) < 24:
                report.error(f"{rel}: `{specs_key}` `{name}` evidence_expectation is too weak")
            if len(anti_gaming) < 32:
                report.error(f"{rel}: `{specs_key}` `{name}` anti_gaming_probe is too weak")
            if len(pass_case) < 24 or len(fail_case) < 24:
                report.error(f"{rel}: `{specs_key}` `{name}` pass/fail examples are too weak")
            if norm(pass_case) == norm(fail_case):
                report.error(f"{rel}: `{specs_key}` `{name}` pass/fail examples are indistinguishable")
            if not MEASURE_VERB_RE.search(measurement):
                report.error(
                    f"{rel}: `{specs_key}` `{name}` measurement_protocol lacks executable action verbs"
                )
            if not MEASURE_VERB_RE.search(anti_gaming):
                report.error(
                    f"{rel}: `{specs_key}` `{name}` anti_gaming_probe lacks executable action verbs"
                )
            if not DISCRIMINATOR_RE.search(discriminator):
                report.error(
                    f"{rel}: `{specs_key}` `{name}` discriminator must describe pass/fail separation"
                )

            if not isinstance(anchors, dict):
                report.error(f"{rel}: `{specs_key}` `{name}` missing scoring_anchors object")
            else:
                for anchor_key in ("0", "50", "80", "100"):
                    anchor_value = str(anchors.get(anchor_key, "")).strip()
                    if len(anchor_value) < 12:
                        report.error(
                            f"{rel}: `{specs_key}` `{name}` scoring anchor `{anchor_key}` is too weak"
                        )

            name_tokens = token_set(name)
            body_tokens = token_set(
                " ".join(
                    [
                        definition,
                        failure_mode,
                        discriminator,
                        intervention,
                        measurement,
                        anti_gaming,
                    ]
                )
            )
            if name_tokens and not (name_tokens & body_tokens):
                report.error(
                    f"{rel}: `{specs_key}` `{name}` is not dimension-specific (name tokens absent in spec text)"
                )

        if unique_ratio(definitions) < 0.65:
            report.error(f"{rel}: `{specs_key}` definitions are overly templated")
        if unique_ratio(failures) < 0.65:
            report.error(f"{rel}: `{specs_key}` failure_mode entries are overly templated")
        if unique_ratio(discriminators) < 0.65:
            report.error(f"{rel}: `{specs_key}` discriminator entries are overly templated")
        if unique_ratio(interventions) < 0.65:
            report.error(f"{rel}: `{specs_key}` intervention entries are overly templated")
        if unique_ratio(measurements) < 0.80:
            report.error(f"{rel}: `{specs_key}` measurement_protocol entries are overly templated")
        if unique_ratio(probes) < 0.80:
            report.error(f"{rel}: `{specs_key}` anti_gaming_probe entries are overly templated")

    validate_specs("x_axis_specs", x_axis)
    validate_specs("y_axis_specs", y_axis)

    alternatives = data.get("axis_alternatives_considered", [])
    if not isinstance(alternatives, list) or len(alternatives) < 4:
        report.error(f"{rel}: `axis_alternatives_considered` must contain rich alternatives for x and y")
    else:
        seen_axis = set()
        rejected_axis = set()
        kept_by_axis = {"x": [], "y": []}
        for alt in alternatives:
            if not isinstance(alt, dict):
                report.error(f"{rel}: alternatives entries must be objects")
                continue
            axis = str(alt.get("axis", "")).strip().lower()
            name = str(alt.get("name", "")).strip()
            reason = str(alt.get("reason", "")).strip()
            kept = alt.get("kept")
            if axis not in {"x", "y"}:
                report.error(f"{rel}: alternative axis must be `x` or `y`")
                continue
            seen_axis.add(axis)
            if kept is False:
                rejected_axis.add(axis)
            if kept is True:
                kept_by_axis[axis].append(alt)
            if not name or len(reason) < 24 or not isinstance(kept, bool):
                report.error(
                    f"{rel}: each alternative needs non-empty name, boolean kept, and strong rationale"
                )
        if seen_axis != {"x", "y"}:
            report.error(f"{rel}: alternatives must cover both axes")
        if rejected_axis != {"x", "y"}:
            report.error(f"{rel}: alternatives must include rejected options for both axes")
        if not ensure_alternatives_cover_final_axes(
            kept_items=kept_by_axis["x"], axis_values=set(x_axis), axis_label="x"
        ):
            report.error(f"{rel}: kept x alternatives do not fully enumerate final x dimensions")
        if not ensure_alternatives_cover_final_axes(
            kept_items=kept_by_axis["y"], axis_values=set(y_axis), axis_label="y"
        ):
            report.error(f"{rel}: kept y alternatives do not fully enumerate final y dimensions")

    cells = data.get("cells", [])
    if not isinstance(cells, list):
        report.error(f"{rel}: `cells` must be an array")
        return

    expected = len(x_axis) * len(y_axis)
    if len(cells) != expected:
        report.error(f"{rel}: expected {expected} cells for {len(x_axis)}x{len(y_axis)}, found {len(cells)}")

    seen_pairs = set()
    rationales = []
    evidence_maps = []
    collateral_maps = []
    seen_collateral_refs: set[str] = set()
    for cell in cells:
        if not isinstance(cell, dict):
            report.error(f"{rel}: each cell must be an object")
            continue
        x = str(cell.get("x", "")).strip()
        y = str(cell.get("y", "")).strip()
        pair = (x, y)
        if pair in seen_pairs:
            report.error(f"{rel}: duplicate cell for x=`{x}` y=`{y}`")
        seen_pairs.add(pair)
        if x not in x_axis or y not in y_axis:
            report.error(f"{rel}: cell references unknown dimension x=`{x}` y=`{y}`")

        score = cell.get("score_percent")
        if not isinstance(score, (int, float)) or not (0 <= float(score) <= 100):
            report.error(f"{rel}: cell ({x},{y}) has invalid score_percent")

        refs = cell.get("evidence_refs", [])
        if not isinstance(refs, list) or not refs:
            report.error(f"{rel}: cell ({x},{y}) has empty evidence_refs")
        collateral_refs = cell.get("collateral_refs", [])
        if not isinstance(collateral_refs, list) or not collateral_refs:
            report.error(f"{rel}: cell ({x},{y}) has empty collateral_refs")
            collateral_refs = []
        for collateral_ref in collateral_refs:
            cref = str(collateral_ref).strip()
            if not cref:
                continue
            seen_collateral_refs.add(cref)
            if manifest_set and not manifest_ref_resolves(cref, manifest_set):
                report.error(
                    f"{rel}: cell ({x},{y}) collateral ref `{cref}` is not in `target_collateral_manifest`"
                )
            elif manifest_set and not manifest_ref_points_to_existing_file(cref, manifest_set, run_dir):
                report.error(
                    f"{rel}: cell ({x},{y}) collateral ref `{cref}` does not resolve to an existing collateral file"
                )

        rationale = str(cell.get("rationale", "")).strip()
        if len(rationale) < 24:
            report.error(f"{rel}: cell ({x},{y}) rationale is too weak")

        combined = f"{x} {y} {rationale}".lower()
        x_tokens = token_set(x, min_len=3)
        y_tokens = token_set(y, min_len=3)
        if (x_tokens or y_tokens) and not ((x_tokens | y_tokens) & token_set(combined, min_len=3)):
            report.error(f"{rel}: cell ({x},{y}) rationale not specific to its dimensions")

        rationales.append(norm(rationale))
        evidence_maps.append(
            "|".join(sorted(str(ref).strip() for ref in refs if str(ref).strip()))
        )
        collateral_maps.append(
            "|".join(sorted(str(ref).strip() for ref in collateral_refs if str(ref).strip()))
        )

    if len(seen_pairs) != expected:
        report.error(f"{rel}: incomplete or duplicate cell coverage for XxY grid")

    cell_ref_lookup, cell_pair_lookup = build_cell_ref_lookup(seen_pairs)
    total_cells_for_guard = max(1, expected)
    for section_idx, role_id, scoring_focus, covered_cells in role_sections_for_cell_validation:
        resolved_pairs: set[tuple[str, str]] = set()
        for cell_idx, cell_ref in enumerate(covered_cells):
            resolved = resolve_cell_pair_ref(cell_ref, cell_ref_lookup, cell_pair_lookup)
            if not resolved:
                report.error(
                    f"{rel}: role_sections[{section_idx}] covered_cells[{cell_idx}] `{cell_ref}` does not reference an existing cell pair"
                )
                continue
            resolved_pairs.add(resolved)

        if BROAD_SCORING_FOCUS_RE.search(scoring_focus):
            min_covered = max(1, int(math.ceil(total_cells_for_guard * 0.10)))
            if len(resolved_pairs) < min_covered:
                role_hint = f" role_id `{role_id}`" if role_id else ""
                report.error(
                    f"{rel}: role_sections[{section_idx}]{role_hint} claims broad scoring_focus but covered_cells is too narrow ({len(resolved_pairs)}/{total_cells_for_guard}; need >= {min_covered})"
                )

    rationale_uniqueness = unique_ratio(rationales)
    evidence_uniqueness = unique_ratio(evidence_maps)
    collateral_uniqueness = unique_ratio(collateral_maps)
    if rationale_uniqueness < 0.75:
        report.error(f"{rel}: cell rationales are overly templated ({rationale_uniqueness:.0%} unique)")
    if evidence_uniqueness < 0.50:
        report.error(f"{rel}: cell evidence mappings are overly templated ({evidence_uniqueness:.0%} unique)")
    if collateral_uniqueness < 0.50:
        report.error(
            f"{rel}: cell collateral mappings are overly templated ({collateral_uniqueness:.0%} unique)"
        )

    if manifest_set:
        min_collateral_coverage = max(1, len(manifest_set) // 2)
        if len(seen_collateral_refs) < min_collateral_coverage:
            report.error(
                f"{rel}: collateral coverage too narrow ({len(seen_collateral_refs)}/{len(manifest_set)} used)"
            )

    if prompt_words:
        rubric_vocab = token_set(
            " ".join(x_axis + y_axis + [improvement_intent, task_conformance_rationale]),
            min_len=4,
        )
        min_overlap = min(3, max(1, len(prompt_words) // 8))
        overlap = len(rubric_vocab & prompt_words)
        if overlap < min_overlap:
            report.error(
                f"{rel}: rubric vocabulary weakly grounded in prompt intent ({overlap} < {min_overlap} token overlap)"
            )

    if rubric_index == 0:
        axis_vocab = token_set(" ".join(x_axis + y_axis + rationales), min_len=4)
        if prompt_words:
            min_overlap = min(4, max(2, len(prompt_words) // 3))
            if len(axis_vocab & prompt_words) < min_overlap:
                report.error(f"{rel}: Rubric_0 vocabulary is weakly grounded in prompt intent")

        category_keywords = {
            "outcome": {
                "impact",
                "outcome",
                "value",
                "benefit",
                "effectiveness",
                "fit",
                "usefulness",
            },
            "rigor": {
                "precision",
                "accuracy",
                "fidelity",
                "correctness",
                "coherence",
                "validity",
            },
            "robustness": {
                "adversarial",
                "risk",
                "failure",
                "resilien",
                "threat",
                "abuse",
                "tamper",
            },
            "evidence": {
                "evidence",
                "trace",
                "audit",
                "verify",
                "reproduc",
                "test",
                "proof",
            },
        }
        coverage = 0
        axis_blob = " ".join((x_axis + y_axis + [improvement_intent])).lower()
        for keywords in category_keywords.values():
            if any(k in axis_blob for k in keywords):
                coverage += 1
        if coverage < 3:
            report.error(
                f"{rel}: Rubric_0 dimensions lack conceptual breadth (need outcome/rigor/robustness/evidence coverage)"
            )


def main() -> int:
    args = parse_args()
    run_dir = Path(args.run_dir).resolve()
    if not run_dir.is_dir():
        raise SystemExit(f"error: run dir not found: {run_dir}")

    report = ValidationReport()
    rubric_files = sorted(
        {
            *run_dir.glob("rubrics/Rubric_*/iteration_*.json"),
            *run_dir.glob("rubrics/R*/iteration_*.json"),  # legacy compatibility
            *run_dir.glob("rubrics/Rubric_*/cycle_*.json"),
            *run_dir.glob("rubrics/R*/cycle_*.json"),  # legacy compatibility
        },
        key=lambda p: p.as_posix(),
    )
    if not rubric_files:
        report.error(
            "no rubric JSON files found under rubrics/Rubric_*/iteration_*.json (or legacy cycle_*.json)"
        )
    prompt_path = run_dir / "prompt.txt"
    prompt_words = set()
    prompt_requirements: list[str] = []
    if prompt_path.exists():
        prompt_text = prompt_path.read_text(encoding="utf-8")
        prompt_words = token_set(prompt_text, min_len=4)
        prompt_requirements = parse_prompt_requirements(prompt_text)

    for rubric_path in rubric_files:
        validate_rubric_file(
            rubric_path,
            run_dir,
            prompt_words,
            prompt_requirements,
            report,
        )

    output = {
        "status": "PASS" if not report.errors else "FAIL",
        "error_count": len(report.errors),
        "warning_count": len(report.warnings),
        "errors": report.errors,
        "warnings": report.warnings,
    }

    if args.json_out:
        out_path = Path(args.json_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")

    if report.errors:
        print("rubric_excellence_check: FAIL")
        for err in report.errors:
            print(f"- {err}")
        if report.warnings:
            print("warnings:")
            for warning in report.warnings:
                print(f"- {warning}")
        return 1

    print("rubric_excellence_check: PASS")
    if report.warnings:
        print("warnings:")
        for warning in report.warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
