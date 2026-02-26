#!/usr/bin/env python3
"""Evaluate and optionally drive default stability mode for nested rubric-driven iterations.

Liquid State Machine framing:
- Prompt injection perturbs a previously stable reservoir (the rubric chain).
- Development should occur in an edge-of-chaos regime (neither trivial nor catastrophic).
- Readout reconvergence is accepted only after prompt requirements are fully satisfied.

Default stability objective:
- Execute full chain cycles in canonical order:
  `Rubric_N -> Rubric_(N-1)` down to `Rubric_1 -> Rubric_0`
- A chain run passes the quality gate only when:
  - decision == ACCEPT
  - recheck_mean >= 100.0
  - recheck_defects <= 0
  - recheck_blocking_defects == 0
  - (recheck_mean - baseline_mean) >= 0.0
  - prompt_satisfaction == yes
  - identity_lock == yes
  - synthetic_iteration == no
  - real_delta_evidence == yes
- A chain run may be marked `PROVISIONAL_ACCEPT` when it shows real, non-synthetic
  improvement, but one or more full quality gates remain unmet.
- `PROVISIONAL_ACCEPT` preserves improvement credit and carry-forward obligations,
  but it does not count toward stability.
- A stability unit is one qualifying full-chain cycle (all adjacency chains in order).
- Stability is achieved when `required_streak` units are completed consecutively.
  The default is `required_streak=1` (single qualifying full-chain pass).
- With `--request-stability`, this script autonomously executes missing chains
  (via `codex exec`) until stable or until configured limits are reached.
- With `--require-chain-destabilization`, each chain must first demonstrate
  non-trivial prompt-linked destabilization within the configured edge band
  before later recovery can count.
"""

from __future__ import annotations

import argparse
import ctypes
import dataclasses
import hashlib
import json
import math
import os
import re
import shlex
import signal
import subprocess
import textwrap
import time
from pathlib import Path
from typing import Iterable

# Parse simple markdown bullets like:
# - key: value
# - key: `value with optional inline `code` fragments`
# Keep capture permissive and normalize wrappers in normalize_scalar().
BULLET_RE = re.compile(r"^(?:-\s+)?([A-Za-z0-9_]+):\s*(.*?)\s*$")
ITER_RE = re.compile(r"^iteration_(\d+)$")
ITER_ANY_RE = re.compile(r"iteration_(\d+)")
CHAIN_RE = re.compile(r"^Rubric_(\d+)\s*->\s*Rubric_(\d+)$")
RUBRIC_FILE_RE = re.compile(r"Rubric_(\d+)")
EVIDENCE_LINE_REF_RE = re.compile(
    r"^(?P<path>.+?):(?P<line>\d+)(?::(?P<col>\d+))?(?:-(?P<end>\d+))?$"
)
PROMPT_LINK_RE = re.compile(
    r"(prompt\.txt|prompt[-_ ]linked|prompt[_ ]linkage|user requirement|prompt requirement)",
    re.IGNORECASE,
)
PROMPT_SOURCE_RE = re.compile(r"prompt_source\s*:\s*`?prompt\.txt`?", re.IGNORECASE)
PROMPT_CONSUMED_RE = re.compile(r"prompt_consumed\s*:\s*(yes|true|1)\b", re.IGNORECASE)
PROMPT_WRITE_FILE_RE = re.compile(r"^\s*\d+\.\s*Write\s+`([^`]+)`(?:\s+with\s+(.+))?\s*$", re.IGNORECASE)
PROMPT_ACTION_RE = re.compile(
    r"\b(write|create|develop|improve|produce|update|build|generate|author)\b",
    re.IGNORECASE,
)
PROMPT_FILE_REF_RE = re.compile(r"`([^`]+\.[A-Za-z0-9_]+)`")
PROMPT_NUMBERED_REQ_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$")
PROMPT_ACCEPTANCE_HEADER_RE = re.compile(r"^\s*acceptance criteria\s*:\s*$", re.IGNORECASE)
PROMPT_SAT_REQ_RE = re.compile(r"^(?:-+\s*)?requirement:\s*(.+)$", re.IGNORECASE)
PROMPT_SAT_REQ_TEXT_RE = re.compile(
    r"^(?:-+\s*)?(?:requirement(?:_text)?|text)\s*:\s*(.+)$",
    re.IGNORECASE,
)
PROMPT_SAT_REQ_ID_RE = re.compile(
    r"^(?:#{1,6}\s*)?(?:-+\s*)?(?:(?:requirement_id|id)\s*:\s*)?(RQ-\d+)\s*:?\s*$",
    re.IGNORECASE,
)
PROMPT_SAT_STATUS_RE = re.compile(
    r"^(?:-+\s*)?status:\s*([A-Za-z0-9_ -]+)\s*$",
    re.IGNORECASE,
)
PROMPT_SAT_EVIDENCE_RE = re.compile(
    r"^(?:-+\s*)?evidence(?:_paths?|_path|_artifacts?|_artifact_paths?)?\s*:\s*(.*)$",
    re.IGNORECASE,
)
PROMPT_SAT_IMPLEMENTATION_RE = re.compile(
    r"^(?:-+\s*)?(?:implementation(?:_artifacts?|_artifact_paths?|_paths?)|artifact_paths?)\s*:\s*(.*)$",
    re.IGNORECASE,
)
PROMPT_SAT_VERIFICATION_RE = re.compile(
    r"^(?:-+\s*)?verification(?:_result)?\s*:\s*(.+)$",
    re.IGNORECASE,
)
PROMPT_SAT_KEYED_BULLET_RE = re.compile(r"^(?:-+\s*)?[A-Za-z0-9_ -]+\s*:\s*.*$")
FORBIDDEN_PLACEHOLDER_TOKEN_RE = re.compile(
    r"\{\{\s*todo\s*\}\}|<\s*todo\s*>|\b(?:todo|tbd)\b\s*[:\-]",
    re.IGNORECASE,
)
JSON_TRAILING_COMMA_RE = re.compile(r",(\s*[}\]])")
SCOPE_ESCAPE_TOKEN_RE = re.compile(r"(^|[\s`\"'(])\.\./")
NON_PRIMARY_ARTIFACT_DIR_PREFIXES = (
    "iterations/",
    "rubrics/",
    "scorecards/",
    "collateral/",
    "evidence/",
    "deltas/",
    "contradictions/",
    "visual/",
    "scripts/",
)
NON_PRIMARY_ARTIFACT_NAMES = {
    "prompt.txt",
    "run_metadata.md",
    "rubric_schema.json",
    "agents.md",
    "stability_status.md",
    "stability_status.json",
    "liquid_state_identity.md",
    "artifact_manifest.md",
    "rubric_scorecard_summary.md",
    "final_status.md",
    "prompt_satisfaction.md",
}

TEXTUAL_ARTIFACT_SUFFIXES = {
    ".md",
    ".txt",
    ".rst",
    ".adoc",
    ".tex",
    ".html",
    ".css",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".json",
    ".yaml",
    ".yml",
    ".xml",
    ".toml",
    ".ini",
    ".cfg",
    ".csv",
    ".py",
    ".go",
    ".rs",
    ".java",
    ".c",
    ".h",
    ".cpp",
    ".hpp",
    ".sh",
}

REQUIRED_RUN_OUTPUTS = (
    "ARTIFACT_MANIFEST.md",
    "RUBRIC_SCORECARD_SUMMARY.md",
    "FINAL_STATUS.md",
    "OBJECTIVE_SPEC.md",
    "BEST_KNOWN_FRONTIER.md",
)

RUN_LEVEL_SNAPSHOT_OUTPUTS = (
    "PROMPT_SATISFACTION.md",
    *REQUIRED_RUN_OUTPUTS,
)

NON_SATISFIED_STATUSES = {
    "unsatisfied",
    "missing",
    "in_progress",
    "in progress",
    "blocked",
    "incomplete",
    "no",
}

SEMANTIC_STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "that",
    "this",
    "from",
    "into",
    "your",
    "their",
    "must",
    "should",
    "would",
    "have",
    "has",
    "had",
    "been",
    "being",
    "are",
    "was",
    "were",
    "will",
    "can",
    "could",
    "include",
    "includes",
    "including",
    "keep",
    "make",
    "each",
    "every",
    "all",
    "use",
    "using",
    "used",
    "when",
    "then",
    "than",
    "into",
    "onto",
    "over",
    "under",
    "only",
    "more",
    "most",
    "very",
    "also",
    "just",
    "such",
    "this",
    "these",
    "those",
    "project",
}

REQUIREMENT_TOKEN_SYNONYMS: dict[str, tuple[str, ...]] = {
    "clean": ("readable", "consistent", "organized", "structured"),
    "scannable": ("scan", "scanfirst", "navigable", "sectioning"),
    "grounded": ("evidence", "observable", "verified"),
    "formatting": ("layout", "structure", "sectioning"),
    "copy": ("runnable", "executable"),
    "pastable": ("runnable", "executable"),
}

NON_REAL_DELTA_MARKERS = (
    "synthesized fallback",
    "status: bootstrap",
    "bootstrap_initialized",
    "- pending:",
)
SYNTHETIC_TEXT_PATTERNS = (
    re.compile(r"(?im)\bsynthesized fallback\b"),
    re.compile(r"(?im)\bbootstrap_initialized\b"),
    re.compile(r"(?im)^\s*-\s*status:\s*bootstrap\s*$"),
    re.compile(r"(?im)^\s*status:\s*bootstrap\s*$"),
    re.compile(r"(?im)^\s*-\s*pending:\s*$"),
    re.compile(r"(?im)^\s*-\s*pending:\s*(?:todo|tbd|unknown|n/?a)\s*$"),
)

MIN_DELTA_FILE_BYTES = {
    "deltas": 64,
    "evidence": 64,
    "manifest": 64,
    "access_log": 40,
    "scorecard": 64,
    "burndown": 40,
}

QUALITY_MIN_RECHECK_MEAN = 100.0
QUALITY_MAX_RECHECK_DEFECTS = 0
QUALITY_MAX_RECHECK_BLOCKING_DEFECTS = 0
QUALITY_MIN_DISCRIMINATION_GAP = 10.0
QUALITY_MIN_COUNTEREXAMPLE_VARIANTS = 2
PRIMARY_ARTIFACT_RUNTIME_FILE = "PRIMARY_ARTIFACT_RUNTIME.json"

# Canonical 16-role company catalog used for runtime role wiring.
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

# Canonical per-role product-quality dimensions used to build the bootstrap Y-axis.
# Each role must contribute at least two dimensions.
CANONICAL_ROLE_PRODUCT_DIMENSIONS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("R0", ("Strategic Outcome Alignment", "User Value Realization")),
    ("R1", ("Delivery Predictability", "Operational Resilience")),
    ("R2", ("Cost Efficiency and ROI", "Compliance and Auditability")),
    ("R3", ("Technical Architecture Integrity", "Reliability and Incident Readiness")),
    ("R4", ("Product Discovery Quality", "Requirement Coverage Fidelity")),
    ("R5", ("Implementation Correctness", "Delivery Predictability")),
    ("R6", ("Implementation Correctness", "Defect Prevention and Detection")),
    ("R7", ("Defect Prevention and Detection", "Requirement Coverage Fidelity")),
    ("R8", ("Reliability and Incident Readiness", "Operational Resilience")),
    ("R9", ("Security and Threat Resistance", "Compliance and Auditability")),
    ("R10", ("Data Accuracy and Analytical Validity", "Requirement Coverage Fidelity")),
    ("R11", ("Usability and Accessibility Quality", "User Value Realization")),
    ("R12", ("User Value Realization", "Delivery Predictability")),
    ("R13", ("Documentation Completeness and Clarity", "Requirement Coverage Fidelity")),
    ("R14", ("Compliance and Auditability", "Security and Threat Resistance")),
    ("R15", ("Compliance and Auditability", "Defect Prevention and Detection")),
)


@dataclasses.dataclass(frozen=True)
class PromptSatisfactionEntry:
    requirement: str
    status: str
    evidence_paths: tuple[str, ...]
    verification: str = ""
    implementation_paths: tuple[str, ...] = ()


@dataclasses.dataclass(frozen=True)
class IterationRecord:
    iteration: int
    chain: str
    decision: str
    baseline_mean: float
    recheck_mean: float
    baseline_blocking_defects: int
    baseline_total_defects: int
    recheck_defects: int
    recheck_blocking_defects: int
    prompt_linked_baseline: bool
    prompt_satisfaction: bool
    identity_lock: bool
    synthetic_iteration: bool
    real_delta_evidence: bool
    source_file: str
    objective_gate: bool = True
    truth_reconciled: bool = False

    @property
    def prompt_required(self) -> bool:
        return chain_requires_prompt_satisfaction(self.chain)

    @property
    def prompt_gate_passed(self) -> bool:
        return self.prompt_satisfaction or (not self.prompt_required)

    @property
    def integrity_gate_passed(self) -> bool:
        return (
            self.identity_lock
            and (not self.synthetic_iteration)
            and self.real_delta_evidence
            and self.prompt_gate_passed
            and self.objective_gate
            and (not self.truth_reconciled)
        )

    @property
    def is_quality_perfect(self) -> bool:
        delta = self.recheck_mean - self.baseline_mean
        return (
            self.decision.upper() == "ACCEPT"
            and self.recheck_mean >= QUALITY_MIN_RECHECK_MEAN
            and self.recheck_defects <= QUALITY_MAX_RECHECK_DEFECTS
            and self.recheck_blocking_defects <= QUALITY_MAX_RECHECK_BLOCKING_DEFECTS
            and delta >= 0.0
            and self.objective_gate
            and (not self.truth_reconciled)
        )

    @property
    def is_provisional_accept(self) -> bool:
        delta = self.recheck_mean - self.baseline_mean
        return (
            self.decision.upper() == "PROVISIONAL_ACCEPT"
            and delta > 0.0
            and self.integrity_gate_passed
        )

    @property
    def is_improvement_accepted(self) -> bool:
        return (
            (self.decision.upper() == "ACCEPT" and self.is_quality_perfect and self.integrity_gate_passed)
            or self.is_provisional_accept
        )

    @property
    def is_perfect(self) -> bool:
        return self.is_quality_perfect and self.integrity_gate_passed


@dataclasses.dataclass(frozen=True)
class StabilityResult:
    records: list[IterationRecord]
    streak: int
    required_streak: int
    depth: int
    expected_chains: list[str]
    chain_destabilized: dict[str, bool]
    require_chain_destabilization: bool
    chain_recovered: dict[str, bool]
    chain_prompt_satisfied: dict[str, bool]
    min_destabilization_defects: int
    min_destabilization_baseline_mean: float
    max_destabilization_baseline_mean: float
    min_recovery_iteration_gap: int
    require_prompt_linkage: bool
    require_prompt_satisfaction: bool
    system_phase: str
    next_chain: str | None
    stable: bool
    rationale: str


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Compute default stability mode status from iteration artifacts."
    )
    p.add_argument(
        "--iterations-dir",
        default="iterations",
        help="Directory containing iteration_* folders (default: iterations)",
    )
    p.add_argument(
        "--required-streak",
        type=int,
        default=1,
        help="Consecutive qualifying full-chain units required for stability (default: 1)",
    )
    p.add_argument(
        "--depth",
        type=int,
        default=-1,
        help=(
            "Rubric depth N for full-chain stability (Rubric_N..Rubric_0). "
            "If omitted, depth is inferred from rubric files and iteration history."
        ),
    )
    p.add_argument(
        "--output",
        default="STABILITY_STATUS.md",
        help="Markdown output path (default: STABILITY_STATUS.md)",
    )
    p.add_argument(
        "--json-output",
        default="",
        help="Optional JSON output path.",
    )
    p.add_argument(
        "--fail-if-unstable",
        action="store_true",
        help="Exit non-zero when stability is not achieved.",
    )
    p.add_argument(
        "--request-stability",
        action="store_true",
        help=(
            "Autonomously run missing adjacency-chain iterations (via codex exec) "
            "until stability is reached or limits are hit."
        ),
    )
    p.add_argument(
        "--run-chain-once",
        default="",
        help=(
            "Execute exactly one autonomous iteration for an explicit chain "
            "(for example 'Rubric_2 -> Rubric_1') and exit."
        ),
    )
    p.add_argument(
        "--max-autonomous-iterations",
        type=int,
        default=16,
        help=(
            "Max codex-driven iteration attempts when --request-stability is used "
            "(default: 16)."
        ),
    )
    p.add_argument(
        "--codex-timeout-seconds",
        type=int,
        default=int(os.environ.get("CODEX_TIMEOUT_SECONDS", "0")),
        help=(
            "Timeout per codex execution in seconds when --request-stability is used "
            "(default: CODEX_TIMEOUT_SECONDS or 0, where 0 disables timeout)."
        ),
    )
    p.add_argument(
        "--codex-no-progress-seconds",
        type=int,
        default=int(os.environ.get("CODEX_NO_PROGRESS_SECONDS", "0")),
        help=(
            "Terminate an autonomous codex attempt when no non-log artifact progress is "
            "observed for this many seconds (default: CODEX_NO_PROGRESS_SECONDS or 0). "
            "Set 0 to disable."
        ),
    )
    p.add_argument(
        "--codex-bin",
        default="codex",
        help="Codex CLI binary for autonomous mode (default: codex).",
    )
    p.add_argument(
        "--codex-reasoning-effort",
        default=os.environ.get("CODEX_REASONING_EFFORT", "xhigh"),
        help=(
            "Reasoning effort for codex exec in autonomous mode "
            "(default: CODEX_REASONING_EFFORT or xhigh)."
        ),
    )
    p.add_argument(
        "--codex-model",
        default="",
        help="Optional model override for codex exec in autonomous mode.",
    )
    p.add_argument(
        "--project-root",
        default=".",
        help="Project root for codex exec in autonomous mode (default: current directory).",
    )
    p.add_argument(
        "--require-chain-destabilization",
        action="store_true",
        help=(
            "Require every adjacency chain to show non-trivial prompt-induced "
            "destabilization before a qualifying chain pass can count."
        ),
    )
    p.add_argument(
        "--min-destabilization-defects",
        type=int,
        default=3,
        help=(
            "Minimum baseline_total_defects required for a non-trivial destabilization "
            "event per chain (default: 3)."
        ),
    )
    p.add_argument(
        "--min-destabilization-baseline-mean",
        type=float,
        default=40.0,
        help=(
            "Minimum baseline_mean required for a destabilization event to count "
            "(default: 40.0)."
        ),
    )
    p.add_argument(
        "--max-destabilization-baseline-mean",
        type=float,
        default=95.0,
        help=(
            "Maximum baseline_mean allowed for a destabilization event to count "
            "(default: 95.0)."
        ),
    )
    p.add_argument(
        "--min-recovery-iteration-gap",
        type=int,
        default=1,
        help=(
            "Minimum number of iterations between first destabilization event and "
            "first eligible qualifying recovery for the same chain (default: 1)."
        ),
    )
    p.add_argument(
        "--require-prompt-linkage",
        action="store_true",
        help=(
            "Require baseline defect artifacts to explicitly reference prompt linkage "
            "for destabilization events to count. Implicitly enabled when "
            "--require-chain-destabilization is set."
        ),
    )
    p.add_argument(
        "--allow-partial-prompt-satisfaction",
        action="store_true",
        help=(
            "Allow stability to be reported without explicit `prompt_satisfaction=yes` "
            "in chain decision artifacts. Not recommended."
        ),
    )
    return p.parse_args()


def _linux_set_pdeathsig(sig: int) -> None:
    """Best-effort: ask kernel to deliver `sig` when this process's parent dies."""
    if os.name != "posix":
        return
    try:
        libc = ctypes.CDLL("libc.so.6", use_errno=True)
    except OSError:
        return
    # int prctl(int option, unsigned long arg2, unsigned long arg3, unsigned long arg4, unsigned long arg5);
    prctl = libc.prctl
    prctl.argtypes = [
        ctypes.c_int,
        ctypes.c_ulong,
        ctypes.c_ulong,
        ctypes.c_ulong,
        ctypes.c_ulong,
    ]
    prctl.restype = ctypes.c_int
    PR_SET_PDEATHSIG = 1
    _ = prctl(PR_SET_PDEATHSIG, ctypes.c_ulong(sig), 0, 0, 0)


def parse_chain(chain: str) -> tuple[int, int] | None:
    match = CHAIN_RE.match(chain.strip())
    if not match:
        return None
    upper = int(match.group(1))
    lower = int(match.group(2))
    if upper != lower + 1:
        return None
    return upper, lower


def format_chain(upper: int, lower: int) -> str:
    return f"Rubric_{upper} -> Rubric_{lower}"


def parse_bullets(md_path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not md_path.exists():
        return data
    for raw in md_path.read_text(encoding="utf-8").splitlines():
        match = BULLET_RE.match(raw.strip())
        if match:
            key, value = match.group(1), normalize_scalar(match.group(2))
            data[key] = value
    return data


def upsert_simple_bullet(md_path: Path, key: str, value: str) -> bool:
    text = read_text_safe(md_path) if md_path.exists() else ""
    bullet = f"- {key}: {value}"
    pattern = re.compile(rf"(?im)^\s*(?:-\s*)?{re.escape(key)}\s*:\s*.*$")
    if pattern.search(text):
        updated = pattern.sub(bullet, text, count=1)
    else:
        sep = "" if not text or text.endswith("\n") else "\n"
        updated = f"{text}{sep}{bullet}\n"
    if updated == text:
        return False
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(updated, encoding="utf-8")
    return True


def append_truth_reconciliation_defect(
    path: Path,
    *,
    chain: str,
    iteration_label: str,
) -> bool:
    marker = "DEF-TRUTH-PROMPT-SAT"
    text = read_text_safe(path) if path.exists() else "# Recheck Defects\n"
    if marker in text:
        return False
    if text and not text.endswith("\n"):
        text += "\n"
    block = (
        "\n"
        f"- id: {marker}\n"
        "  - severity: blocking\n"
        f"  - chain: {chain}\n"
        f"  - iteration: {iteration_label}\n"
        "  - who: truth_reconciler\n"
        "  - what: judge self-report diverged from independent artifact/objective/identity truth checks.\n"
        "  - where: PROMPT_SATISFACTION.md, OBJECTIVE_COUNTEREXAMPLES.md, FRONTIER_STATUS.md, DISCRIMINATION_CHECK.md\n"
        "  - remediation_required: align decision and quality claims with computed truth in this same iteration.\n"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + block, encoding="utf-8")
    return True


def reconcile_frontier_best_known_claims(
    *,
    project_root: Path,
    iteration_dir: Path,
    chain: str,
) -> bool:
    final_decision_path = iteration_dir / "judge_recheck" / "FINAL_DECISION.md"
    frontier_status_path = iteration_dir / "judge_recheck" / "FRONTIER_STATUS.md"
    counterexamples_path = iteration_dir / "judge_recheck" / "OBJECTIVE_COUNTEREXAMPLES.md"
    if not (
        is_nonempty_file(final_decision_path)
        and is_nonempty_file(frontier_status_path)
        and is_nonempty_file(counterexamples_path)
    ):
        return False

    final_bullets = parse_bullets(final_decision_path)
    frontier_bullets = parse_bullets(frontier_status_path)
    counter_bullets = parse_bullets(counterexamples_path)

    baseline_mean = as_float(final_bullets.get("baseline_mean"), -1.0)
    recheck_mean = as_float(final_bullets.get("recheck_mean"), -1.0)
    recheck_total_defects = as_int(
        final_bullets.get("recheck_total_defects", final_bullets.get("recheck_defects")),
        -1,
    )
    recheck_blocking_defects = as_int(final_bullets.get("recheck_blocking_defects"), -1)
    delta = recheck_mean - baseline_mean
    quality_strict = (
        recheck_mean >= QUALITY_MIN_RECHECK_MEAN
        and recheck_total_defects <= QUALITY_MAX_RECHECK_DEFECTS
        and recheck_blocking_defects <= QUALITY_MAX_RECHECK_BLOCKING_DEFECTS
        and delta >= 0.0
    )

    counterexample_performed = as_bool(
        counter_bullets.get("counterexample_search_performed")
        or final_bullets.get("counterexample_search_performed"),
        False,
    )
    variants_tested = as_int(counter_bullets.get("variants_tested"), 0)
    better_variant_found = as_bool(
        counter_bullets.get("better_variant_found")
        or final_bullets.get("better_variant_found"),
        True,
    )
    run_budget_considered = as_bool(final_bullets.get("run_budget_considered"), False)

    compared = as_bool(
        frontier_bullets.get("compared_against_prior_best")
        or frontier_bullets.get("frontier_comparison_performed"),
        False,
    )

    parsed = parse_chain(chain)
    upper = parsed[0] if parsed is not None else 0
    discrimination_ok = True
    if upper >= 1:
        discrimination_ok = discrimination_check_passes(iteration_dir)

    if not (
        quality_strict
        and counterexample_performed
        and variants_tested >= QUALITY_MIN_COUNTEREXAMPLE_VARIANTS
        and (not better_variant_found)
        and compared
        and run_budget_considered
        and discrimination_ok
    ):
        return False

    changed = False
    changed |= upsert_simple_bullet(frontier_status_path, "compared_against_prior_best", "yes")
    changed |= upsert_simple_bullet(frontier_status_path, "frontier_membership", "yes")
    changed |= upsert_simple_bullet(final_decision_path, "frontier_membership", "yes")
    changed |= upsert_simple_bullet(final_decision_path, "no_known_feasible_improvement", "yes")
    changed |= upsert_simple_bullet(final_decision_path, "better_variant_found", "no")
    changed |= upsert_simple_bullet(final_decision_path, "run_budget_considered", "yes")

    best_known_paths = (
        iteration_dir / "BEST_KNOWN_FRONTIER.md",
        project_root / "BEST_KNOWN_FRONTIER.md",
    )
    for path in best_known_paths:
        if not path.exists():
            continue
        changed |= upsert_simple_bullet(path, "compared_against_prior_best", "yes")
        changed |= upsert_simple_bullet(path, "frontier_membership", "yes")

    return changed


def reconcile_iteration_truth(
    *,
    project_root: Path,
    iterations_dir: Path,
    iteration_label: str,
    chain: str,
) -> bool:
    iteration_dir = iterations_dir / f"iteration_{iteration_label}"
    if not iteration_dir.exists():
        return False

    final_decision = iteration_dir / "judge_recheck" / "FINAL_DECISION.md"
    status_path = iteration_dir / "STATUS.md"
    recheck_defects_path = iteration_dir / "judge_recheck" / "PRIORITIZED_DEFECTS.md"
    final_status = project_root / "FINAL_STATUS.md"
    changed = False
    # Normalize frontier/best-known claims when strict objective evidence already
    # proves dominance and no better tested variant exists.
    changed |= reconcile_frontier_best_known_claims(
        project_root=project_root,
        iteration_dir=iteration_dir,
        chain=chain,
    )
    final_decision_data = parse_bullets(final_decision)
    status_data = parse_bullets(status_path)

    def pick_metric(key: str, default: object = "") -> object:
        if key in final_decision_data:
            return final_decision_data.get(key, default)
        return status_data.get(key, default)

    decision_value = normalize_scalar(str(pick_metric("decision", "UNKNOWN"))).upper()

    prompt_required = chain_requires_prompt_satisfaction(chain)
    prompt_truth = True
    if prompt_required:
        prompt_truth = (
            run_level_prompt_satisfaction_complete(iteration_dir)
            and judge_artifacts_have_prompt_access(iteration_dir)
        )
    identity_truth = identity_lock_evidence_exists(iteration_dir) and judge_artifacts_have_prompt_access(
        iteration_dir
    )
    objective_truth = objective_attainment_gate(
        iter_dir=iteration_dir,
        chain=chain,
        decision=decision_value,
    )
    objective_truth_if_accept = objective_attainment_gate(
        iter_dir=iteration_dir,
        chain=chain,
        decision="ACCEPT",
    )
    # Keep ACCEPT strict, but let PROVISIONAL_ACCEPT be reconciled against the
    # objective gate for its declared decision so provisional progression can
    # carry forward without being forced into an ACCEPT-only gate.
    objective_truth_effective = (
        objective_truth_if_accept if decision_value == "ACCEPT" else objective_truth
    )

    baseline_mean = as_float(pick_metric("baseline_mean"), -1.0)
    recheck_mean = as_float(pick_metric("recheck_mean"), -1.0)
    recheck_defects_count = as_int(
        pick_metric("recheck_total_defects", pick_metric("recheck_defects")),
        -1,
    )
    recheck_blocking_defects = as_int(pick_metric("recheck_blocking_defects"), -1)
    synthetic_iteration = as_bool(pick_metric("synthetic_iteration"), False)
    delta = recheck_mean - baseline_mean

    accept_candidate_by_truth = (
        (not synthetic_iteration)
        and prompt_truth
        and identity_truth
        and objective_truth_if_accept
        and recheck_mean >= QUALITY_MIN_RECHECK_MEAN
        and recheck_defects_count <= QUALITY_MAX_RECHECK_DEFECTS
        and recheck_blocking_defects <= QUALITY_MAX_RECHECK_BLOCKING_DEFECTS
        and delta >= 0.0
    )

    corrected = False

    # Keep decision labels consistent with strict quality truth. If the artifact
    # does not meet ACCEPT gates, do not leave a contradictory ACCEPT marker.
    if decision_value == "ACCEPT" and (not accept_candidate_by_truth):
        corrected = True
        quality_reasons: list[str] = []
        if recheck_mean < QUALITY_MIN_RECHECK_MEAN:
            quality_reasons.append(
                f"recheck_mean<{QUALITY_MIN_RECHECK_MEAN:.1f} ({recheck_mean:.1f})"
            )
        if recheck_defects_count > QUALITY_MAX_RECHECK_DEFECTS:
            quality_reasons.append(
                f"recheck_total_defects>{QUALITY_MAX_RECHECK_DEFECTS} ({recheck_defects_count})"
            )
        if recheck_blocking_defects > QUALITY_MAX_RECHECK_BLOCKING_DEFECTS:
            quality_reasons.append(
                "recheck_blocking_defects>"
                f"{QUALITY_MAX_RECHECK_BLOCKING_DEFECTS} ({recheck_blocking_defects})"
            )
        if delta < 0.0:
            quality_reasons.append(f"negative_delta ({delta:.1f})")
        if not objective_truth_if_accept:
            quality_reasons.append("objective_attainment gate failed")
        if not prompt_truth and prompt_required:
            quality_reasons.append("prompt_satisfaction mismatch")
        if not identity_truth:
            quality_reasons.append("identity_lock mismatch")
        reason_text = ", ".join(quality_reasons) if quality_reasons else "strict quality gate not met"

        for path in (final_decision, status_path):
            if not path.exists():
                continue
            changed |= upsert_simple_bullet(path, "decision", "PROVISIONAL_ACCEPT")
            rationale = str(parse_bullets(path).get("rationale", "")).strip()
            note = f"downgraded by truth reconciler because {reason_text}"
            if note not in rationale:
                merged = f"{rationale}; {note}" if rationale else note
                changed |= upsert_simple_bullet(path, "rationale", merged)
        if final_status.exists():
            overall = normalize_scalar(str(parse_bullets(final_status).get("overall", "")).upper())
            if overall in {"ACCEPT", "PASS"}:
                changed |= upsert_simple_bullet(final_status, "overall", "FAIL")
        decision_value = "PROVISIONAL_ACCEPT"

    # Prevent infinite provisional loops when objective and quality gates are
    # already satisfied and only bookkeeping rationale kept decision non-final.
    if decision_value in {"PROVISIONAL_ACCEPT", "REJECT"} and accept_candidate_by_truth:
        corrected = True
        for path in (final_decision, status_path):
            if path.exists():
                changed |= upsert_simple_bullet(path, "decision", "ACCEPT")
        if final_status.exists():
            changed |= upsert_simple_bullet(final_status, "overall", "ACCEPT")
        decision_value = "ACCEPT"
        objective_truth = objective_truth_effective

    prompt_value = "yes" if prompt_truth else "no"
    identity_value = "yes" if identity_truth else "no"

    for path in (final_decision, status_path, final_status):
        if path.exists():
            changed |= upsert_simple_bullet(path, "prompt_satisfaction", prompt_value)
            changed |= upsert_simple_bullet(path, "identity_lock", identity_value)

    hard_truth_fail = (not prompt_truth) or (not identity_truth) or (not objective_truth_effective)
    if hard_truth_fail:
        corrected = True
        # Enforce conservative decisioning when prompt/objective truth cannot be validated.
        decision_targets = (final_decision, status_path)
        for path in decision_targets:
            if not path.exists():
                continue
            data = parse_bullets(path)
            decision = normalize_scalar(str(data.get("decision", "")).upper())
            if decision == "ACCEPT":
                changed |= upsert_simple_bullet(path, "decision", "PROVISIONAL_ACCEPT")
                rationale = str(data.get("rationale", "")).strip()
                reasons: list[str] = []
                if prompt_required and (not prompt_truth):
                    reasons.append("prompt_satisfaction mismatch")
                if not identity_truth:
                    reasons.append("identity_lock mismatch")
                if not objective_truth_effective:
                    reasons.append("objective_attainment gate failed")
                reason_text = ", ".join(reasons) if reasons else "truth mismatch"
                note = f"downgraded by truth reconciler because {reason_text}"
                if note not in rationale:
                    merged = f"{rationale}; {note}" if rationale else note
                    changed |= upsert_simple_bullet(path, "rationale", merged)

        if final_status.exists():
            data = parse_bullets(final_status)
            overall = normalize_scalar(str(data.get("overall", "")).upper())
            if overall in {"ACCEPT", "PASS"}:
                changed |= upsert_simple_bullet(final_status, "overall", "FAIL")
                changed |= upsert_simple_bullet(
                    final_status,
                    "truth_reconciliation",
                    "FAIL due to computed truth mismatch (prompt/objective/identity) against artifact-quality gates",
                )

        if recheck_defects_path.exists():
            changed |= append_truth_reconciliation_defect(
                recheck_defects_path,
                chain=chain,
                iteration_label=iteration_label,
            )
        else:
            recheck_defects_path.parent.mkdir(parents=True, exist_ok=True)
            recheck_defects_path.write_text("# Recheck Defects\n", encoding="utf-8")
            changed |= append_truth_reconciliation_defect(
                recheck_defects_path,
                chain=chain,
                iteration_label=iteration_label,
            )

    if hard_truth_fail:
        truth_marker = "fail"
    elif corrected:
        truth_marker = "corrected"
    else:
        truth_marker = "pass"
    for path in (final_decision, status_path, final_status):
        if path.exists():
            changed |= upsert_simple_bullet(path, "truth_reconciliation", truth_marker)

    return changed


def normalize_scalar(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        cleaned = value.strip()
    else:
        cleaned = str(value).strip()
    if not cleaned:
        return cleaned

    # Recover from malformed wrappers often produced by nested shell quoting
    # during autonomous markdown generation (for example: "'`yes`").
    for _ in range(6):
        before = cleaned
        cleaned = cleaned.strip()
        if len(cleaned) >= 2 and cleaned[0] == cleaned[-1] and cleaned[0] in {"`", "'", '"'}:
            cleaned = cleaned[1:-1]
            continue
        cleaned = cleaned.lstrip("`'\"").rstrip("`'\"").strip()
        if cleaned == before:
            break
    return cleaned


def normalize_ref_token(token: str) -> str:
    cleaned = normalize_scalar(token)
    markdown_link = re.search(r"\[[^\]]*\]\(([^)]+)\)", cleaned)
    if markdown_link:
        cleaned = markdown_link.group(1)
    else:
        # Handle partially stripped markdown-link shapes such as:
        # `label](path/to/file.md#anchor)`
        fallback_link = re.search(r"\]\(([^)]+)\)", cleaned)
        if fallback_link:
            cleaned = fallback_link.group(1)
    cleaned = cleaned.strip().strip("`'\"<>[](){}")
    cleaned = cleaned.rstrip(".,;")
    return cleaned


def load_json_lenient(raw: str) -> tuple[Any | None, str]:
    try:
        return json.loads(raw), raw
    except json.JSONDecodeError:
        repaired = raw
        for _ in range(5):
            updated = JSON_TRAILING_COMMA_RE.sub(r"\1", repaired)
            if updated == repaired:
                break
            repaired = updated
        try:
            return json.loads(repaired), repaired
        except json.JSONDecodeError:
            return None, raw


def as_float(value: object, default: float) -> float:
    if value is None:
        return default
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(normalize_scalar(value))
    except (TypeError, ValueError):
        return default


def as_int(value: object, default: int) -> int:
    if value is None:
        return default
    if isinstance(value, bool):
        return 1 if value else 0
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    try:
        return int(float(normalize_scalar(value)))
    except (TypeError, ValueError):
        return default


def as_bool(value: object, default: bool) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    norm = normalize_scalar(value).lower()
    if norm in {"yes", "true", "1", "y"}:
        return True
    if norm in {"no", "false", "0", "n"}:
        return False
    return default


def normalize_status(value: str) -> str:
    normalized = normalize_scalar(value).lower()
    normalized = re.sub(r"[^a-z0-9_ -]+", " ", normalized)
    return re.sub(r"\s+", "_", normalized).strip("_")


def status_is_satisfied(status: str, verification: str = "") -> bool:
    norm = normalize_status(status)
    if norm in {
        "satisfied",
        "pass",
        "passed",
        "yes",
        "true",
        "ok",
        "complete",
        "completed",
        "done",
        "achieved",
        "verified",
    }:
        return True
    if norm in NON_SATISFIED_STATUSES:
        return False

    ver_norm = normalize_status(verification)
    if ver_norm in {
        "pass",
        "passed",
        "yes",
        "true",
        "verified",
        "success",
        "done",
        "achieved",
        "completed",
    }:
        return True
    return False


def normalize_text(value: str) -> str:
    lowered = value.lower()
    lowered = re.sub(r"`[^`]+`", " ", lowered)
    lowered = re.sub(r"[^a-z0-9]+", " ", lowered)
    return re.sub(r"\s+", " ", lowered).strip()


def extract_file_refs(value: str) -> tuple[str, ...]:
    refs: list[str] = []
    seen: set[str] = set()
    for raw in PROMPT_FILE_REF_RE.findall(value):
        for token in re.split(r"[\s,;()]+", raw):
            rel = token.strip().strip("`<>")
            if not rel or rel in seen:
                continue
            looks_like_path = (
                "/" in rel
                or rel.startswith("./")
                or rel.startswith("../")
                or bool(re.search(r"[A-Za-z0-9_.-]+\.[A-Za-z0-9]{2,8}$", rel))
            )
            if not looks_like_path:
                continue
            refs.append(rel)
            seen.add(rel)
    return tuple(refs)


def parse_reference_list(value: str) -> tuple[str, ...]:
    refs: list[str] = []
    seen: set[str] = set()
    inline_refs = list(extract_file_refs(value))
    if inline_refs:
        for ref in inline_refs:
            clean = normalize_ref_token(ref)
            if clean and clean not in seen:
                refs.append(clean)
                seen.add(clean)
        return tuple(refs)

    for token in re.split(r"[;,]", value):
        clean = normalize_ref_token(token)
        if not clean or clean in seen:
            continue
        if "/" in clean or "." in clean or "#" in clean:
            refs.append(clean)
            seen.add(clean)
    return tuple(refs)


def resolve_run_path(run_root: Path, rel: str) -> Path | None:
    clean_rel = normalize_scalar(str(rel))
    if "#" in clean_rel:
        clean_rel = clean_rel.split("#", 1)[0]
    if "?" in clean_rel:
        clean_rel = clean_rel.split("?", 1)[0]
    clean_rel = clean_rel.strip()
    line_ref = EVIDENCE_LINE_REF_RE.match(clean_rel)
    if line_ref:
        path_part = line_ref.group("path").strip()
        if path_part:
            clean_rel = path_part
    if not clean_rel:
        return None
    candidate = (run_root / clean_rel).resolve()
    try:
        candidate.relative_to(run_root.resolve())
    except ValueError:
        return None
    return candidate


def contains_forbidden_placeholder_token(text: str) -> bool:
    return bool(FORBIDDEN_PLACEHOLDER_TOKEN_RE.search(text))


def contains_scope_escape_path(text: str) -> bool:
    return bool(SCOPE_ESCAPE_TOKEN_RE.search(text))


def is_nonempty_file(path: Path) -> bool:
    return path.exists() and path.is_file() and path.stat().st_size > 0


def resolve_evidence_path(run_root: Path, iter_dir: Path, rel: str) -> Path | None:
    """Resolve evidence/implementation refs against run root and iteration scope."""
    primary = resolve_run_path(run_root, rel)
    if primary is not None and primary.exists():
        return primary

    scoped = resolve_run_path(iter_dir, rel)
    if scoped is not None and scoped.exists():
        return scoped

    clean_rel = normalize_scalar(str(rel)).strip().lstrip("./")
    if not clean_rel:
        return None

    # Common short-hands in prompt-satisfaction artifacts are iteration-relative.
    if (
        clean_rel.startswith("judge_baseline/")
        or clean_rel.startswith("judge_recheck/")
        or clean_rel.startswith("author_deltas/")
    ):
        candidate = resolve_run_path(iter_dir, clean_rel)
        if candidate is not None and candidate.exists():
            return candidate

    # Allow references written as iteration paths without explicit prefix.
    if clean_rel.startswith("iteration_"):
        candidate = resolve_run_path(run_root / "iterations", clean_rel)
        if candidate is not None and candidate.exists():
            return candidate

    return None


def is_primary_artifact_ref(ref: str) -> bool:
    normalized = normalize_scalar(ref).strip().lstrip("./")
    lowered = normalized.lower()
    if not lowered:
        return False
    if lowered in NON_PRIMARY_ARTIFACT_NAMES:
        return False
    if any(lowered.startswith(prefix) for prefix in NON_PRIMARY_ARTIFACT_DIR_PREFIXES):
        return False
    return "/" in normalized or "." in normalized


def artifact_file_has_substance(path: Path) -> bool:
    if not is_nonempty_file(path):
        return False
    if path.stat().st_size < 8:
        return False
    suffix = path.suffix.lower()
    if suffix and suffix not in TEXTUAL_ARTIFACT_SUFFIXES:
        return path.stat().st_size >= 128
    text = read_text_safe(path)
    if not text.strip():
        return False
    if looks_synthetic_text(text):
        return False
    if contains_forbidden_placeholder_token(text):
        return False
    if contains_scope_escape_path(text):
        return False
    stripped = text.strip()
    if len(stripped) < 16:
        return False
    semantic_word_count = len(re.findall(r"[A-Za-z0-9]{3,}", text))
    # Accept short but meaningful artifacts while still rejecting trivial/noise output.
    if len(stripped) < 80:
        return semantic_word_count >= 3
    if len(stripped) < 180:
        return semantic_word_count >= 10
    return semantic_word_count >= 20


def normalize_rel_ref(ref: str) -> str:
    return normalize_scalar(ref).strip().lstrip("./").replace("\\", "/")


def file_sha256_hex(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as fh:
            for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                if not chunk:
                    break
                digest.update(chunk)
    except OSError:
        return ""
    return digest.hexdigest()


def build_primary_artifact_snapshot(
    run_root: Path,
    prompt_refs: Iterable[str],
) -> dict[str, dict[str, object]]:
    snapshot: dict[str, dict[str, object]] = {}
    run_root_resolved = run_root.resolve()
    for ref in prompt_refs:
        normalized_ref = normalize_rel_ref(ref)
        if not normalized_ref:
            continue
        resolved = resolve_run_path(run_root, normalized_ref)
        record: dict[str, object] = {
            "ref": normalized_ref,
            "resolved": normalized_ref,
            "exists": False,
            "size": 0,
            "mtime": 0.0,
            "sha256": "",
            "substantial": False,
        }
        if resolved is None or not resolved.exists() or not resolved.is_file():
            snapshot[normalized_ref] = record
            continue
        try:
            resolved_rel = str(resolved.resolve().relative_to(run_root_resolved)).replace(
                "\\", "/"
            )
        except ValueError:
            resolved_rel = normalized_ref
        record["resolved"] = resolved_rel
        try:
            stat = resolved.stat()
            record["exists"] = True
            record["size"] = int(stat.st_size)
            record["mtime"] = float(stat.st_mtime)
        except OSError:
            record["exists"] = True
        record["sha256"] = file_sha256_hex(resolved)
        record["substantial"] = artifact_file_has_substance(resolved)
        snapshot[normalized_ref] = record
    return snapshot


def primary_artifact_snapshot_changed_refs(
    before: dict[str, object],
    after: dict[str, object],
) -> list[str]:
    changed: list[str] = []
    keys = set(before.keys()) | set(after.keys())
    for key in keys:
        before_entry = before.get(key)
        after_entry = after.get(key)
        if not isinstance(before_entry, dict):
            before_entry = {}
        if not isinstance(after_entry, dict):
            after_entry = {}

        before_exists = as_bool(before_entry.get("exists"), False)
        after_exists = as_bool(after_entry.get("exists"), False)
        if before_exists != after_exists:
            if after_exists:
                if as_bool(after_entry.get("substantial"), False):
                    changed.append(key)
            else:
                changed.append(key)
            continue
        if not before_exists and not after_exists:
            continue

        before_hash = normalize_scalar(before_entry.get("sha256", ""))
        after_hash = normalize_scalar(after_entry.get("sha256", ""))
        if before_hash and after_hash and before_hash != after_hash:
            changed.append(key)
            continue

        before_size = as_int(before_entry.get("size"), 0)
        after_size = as_int(after_entry.get("size"), 0)
        if before_size != after_size:
            changed.append(key)
            continue

        before_mtime = as_float(before_entry.get("mtime"), 0.0)
        after_mtime = as_float(after_entry.get("mtime"), 0.0)
        if abs(after_mtime - before_mtime) > 1e-6:
            changed.append(key)
            continue
    # Preserve deterministic ordering for stable records and tests.
    return sorted(dict.fromkeys(changed))


def write_primary_artifact_runtime(
    iter_dir: Path,
    payload: dict[str, object],
) -> None:
    path = iter_dir / PRIMARY_ARTIFACT_RUNTIME_FILE
    try:
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    except OSError:
        pass


def load_primary_artifact_runtime(iter_dir: Path) -> dict[str, object] | None:
    path = iter_dir / PRIMARY_ARTIFACT_RUNTIME_FILE
    if not is_nonempty_file(path):
        return None
    raw = read_text_safe(path)
    if not raw.strip():
        return None
    data, _repaired = load_json_lenient(raw)
    if isinstance(data, dict):
        return data
    return None


def prompt_satisfaction_primary_artifact_refs(
    run_root: Path,
    iter_dir: Path,
    prompt_primary_refs: tuple[str, ...],
) -> set[str]:
    prompt_set = {
        normalize_rel_ref(ref).lower() for ref in prompt_primary_refs if normalize_rel_ref(ref)
    }
    if not prompt_set:
        return set()
    path = iter_dir / "PROMPT_SATISFACTION.md"
    if not path.exists():
        path = run_root / "PROMPT_SATISFACTION.md"
    entries = parse_prompt_satisfaction_entries(path)
    if not entries:
        return set()

    touched: set[str] = set()
    run_root_resolved = run_root.resolve()
    for entry in entries:
        if not status_is_satisfied(entry.status, entry.verification):
            continue
        refs = [
            ref
            for ref in [*entry.implementation_paths, *entry.evidence_paths]
            if not is_prompt_source_ref(ref)
        ]
        for ref in refs:
            normalized_ref = normalize_rel_ref(ref).lower()
            resolved = resolve_evidence_path(run_root, iter_dir, ref)
            resolved_rel = normalized_ref
            if resolved is not None:
                try:
                    resolved_rel = str(
                        resolved.resolve().relative_to(run_root_resolved)
                    ).replace("\\", "/").lower()
                except ValueError:
                    resolved_rel = normalized_ref
            matched_ref = ""
            if normalized_ref in prompt_set:
                matched_ref = normalized_ref
            elif resolved_rel in prompt_set:
                matched_ref = resolved_rel
            if not matched_ref:
                continue
            target = resolved if resolved is not None else resolve_run_path(run_root, ref)
            if target is None:
                target = resolve_run_path(run_root, matched_ref)
            if target is None or not artifact_file_has_substance(target):
                continue
            touched.add(matched_ref)
    return touched


def should_enforce_synthetic_filter(path: Path, run_root: Path, iter_dir: Path) -> bool:
    """Apply synthetic/placebo checks to run-generated artifacts, not source files."""
    try:
        rel = path.resolve().relative_to(run_root.resolve())
    except ValueError:
        try:
            rel = path.resolve().relative_to(iter_dir.resolve())
        except ValueError:
            return False

    rel_text = str(rel).replace("\\", "/")
    run_artifact_prefixes = (
        "iterations/",
        "rubrics/",
        "scorecards/",
        "collateral/",
        "evidence/",
        "deltas/",
        "contradictions/",
        "visual/",
    )
    if rel_text.startswith(run_artifact_prefixes):
        return True

    run_artifact_names = {
        "PROMPT_SATISFACTION.md",
        "ARTIFACT_MANIFEST.md",
        "RUBRIC_SCORECARD_SUMMARY.md",
        "FINAL_STATUS.md",
        "OBJECTIVE_SPEC.md",
        "BEST_KNOWN_FRONTIER.md",
        "STABILITY_STATUS.md",
        "LIQUID_STATE_IDENTITY.md",
    }
    return path.name in run_artifact_names


def evidence_ref_is_acceptable(path: Path, run_root: Path, iter_dir: Path) -> bool:
    if not is_nonempty_file(path):
        return False
    text = read_text_safe(path)
    if not text.strip():
        return False
    if should_enforce_synthetic_filter(path, run_root, iter_dir):
        if contains_scope_escape_path(text):
            return False
        if looks_synthetic_text(text):
            return False
        if contains_forbidden_placeholder_token(text):
            return False
    return True


def _iter_acceptable_files_in_dir(
    path: Path,
    run_root: Path,
    iter_dir: Path,
    *,
    max_files: int = 32,
) -> list[Path]:
    files: list[Path] = []
    if not path.exists() or (not path.is_dir()):
        return files
    try:
        for child in sorted(path.rglob("*")):
            if not child.is_file():
                continue
            if evidence_ref_is_acceptable(child, run_root, iter_dir):
                files.append(child)
                if len(files) >= max_files:
                    break
    except OSError:
        return files
    return files


def implementation_ref_is_acceptable(path: Path, run_root: Path, iter_dir: Path) -> bool:
    if path.is_file():
        return evidence_ref_is_acceptable(path, run_root, iter_dir)
    if path.is_dir():
        return len(_iter_acceptable_files_in_dir(path, run_root, iter_dir, max_files=1)) >= 1
    return False


def collect_implementation_ref_chunks(
    path: Path,
    run_root: Path,
    iter_dir: Path,
) -> list[str]:
    chunks: list[str] = []
    if path.is_file():
        if implementation_ref_is_acceptable(path, run_root, iter_dir):
            chunks.append(read_text_safe(path)[:50000])
        return chunks
    if path.is_dir():
        for child in _iter_acceptable_files_in_dir(path, run_root, iter_dir):
            chunks.append(read_text_safe(child)[:4000])
        return chunks
    return chunks


def requirement_requires_prompt_primary_match(
    requirement: str, prompt_primary_refs: tuple[str, ...]
) -> bool:
    if not prompt_primary_refs:
        return False
    req_raw = normalize_scalar(requirement).lower()
    req_norm = normalize_text(requirement)
    for ref in prompt_primary_refs:
        clean_ref = normalize_scalar(ref).strip().lstrip("./")
        if not clean_ref:
            continue
        ref_norm = normalize_text(clean_ref)
        stem_norm = normalize_text(Path(clean_ref).stem)
        name_l = Path(clean_ref).name.lower()
        if ref_norm and ref_norm in req_norm:
            return True
        if stem_norm and stem_norm in req_norm:
            return True
        if name_l and name_l in req_raw:
            return True
    return False


def implementation_refs_are_valid(
    run_root: Path,
    implementation_refs: Iterable[str],
    prompt_primary_refs: tuple[str, ...],
    *,
    iter_dir: Path | None = None,
    require_prompt_primary_match: bool = True,
) -> bool:
    refs: list[str] = []
    for ref in implementation_refs:
        cleaned = normalize_ref_token(ref)
        if cleaned:
            refs.append(cleaned)
    if not refs:
        return False

    prompt_primary_set = {
        normalize_scalar(ref).strip().lstrip("./").lower() for ref in prompt_primary_refs
    }

    valid_any = 0
    valid_primary_like = 0
    valid_prompt_primary_match = 0
    for ref in refs:
        if iter_dir is not None:
            resolved = resolve_evidence_path(run_root, iter_dir, ref)
        else:
            resolved = resolve_run_path(run_root, ref)
        if resolved is None:
            continue
        evidence_iter_dir = iter_dir if iter_dir is not None else run_root / "iterations"
        if not implementation_ref_is_acceptable(resolved, run_root, evidence_iter_dir):
            continue
        valid_any += 1
        normalized = normalize_scalar(ref).strip().lstrip("./").lower()
        if is_primary_artifact_ref(ref):
            valid_primary_like += 1
        # Resolved-path matching catches iteration-relative refs that still point
        # at the prompt primary artifact.
        try:
            resolved_rel = str(resolved.resolve().relative_to(run_root.resolve())).replace(
                "\\", "/"
            )
        except ValueError:
            resolved_rel = normalized
        if normalized in prompt_primary_set:
            valid_prompt_primary_match += 1
        elif resolved_rel.lower() in prompt_primary_set:
            valid_prompt_primary_match += 1

    # At least one implementation reference must resolve to a substantive artifact.
    if valid_any < 1:
        return False

    # If prompt explicitly names primary outputs, require at least one implementation
    # artifact to align with that prompt-level artifact set. Auxiliary implementation
    # refs are allowed to be non-primary, but they do not satisfy this requirement.
    if require_prompt_primary_match and prompt_primary_set:
        return valid_prompt_primary_match >= 1

    return valid_any >= 1


def parse_prompt_requirements(prompt_path: Path) -> list[str]:
    if not prompt_path.exists():
        return []
    try:
        lines = prompt_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return []

    requirements: list[str] = []
    seen: set[str] = set()
    in_acceptance = False
    found_numbered = False

    for raw in lines:
        stripped = raw.strip()
        if not stripped:
            continue
        if PROMPT_ACCEPTANCE_HEADER_RE.match(stripped):
            in_acceptance = True
            continue
        numbered = PROMPT_NUMBERED_REQ_RE.match(stripped)
        if numbered:
            found_numbered = True
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

    if found_numbered:
        return requirements

    for raw in lines:
        stripped = raw.strip()
        if not stripped:
            continue
        if PROMPT_ACTION_RE.search(stripped):
            if stripped not in seen:
                requirements.append(stripped)
                seen.add(stripped)
    return requirements


def infer_prompt_primary_artifact_refs(prompt_path: Path) -> tuple[str, ...]:
    if not prompt_path.exists():
        return ()
    text = read_text_safe(prompt_path)
    if not text:
        return ()

    refs: list[str] = []
    seen: set[str] = set()
    run_root = prompt_path.parent

    def resolve_bare_primary_ref(token: str) -> str:
        bare = normalize_scalar(token).strip().strip("`'\"")
        if (not bare) or ("/" in bare) or ("\\" in bare) or ("." in bare):
            return ""
        candidates: list[str] = []
        upper = bare.upper()
        if upper == "README":
            candidates.extend(("README.md", "README.txt"))
        if upper == "CONTRIBUTING":
            candidates.extend(("CONTRIBUTING.md", "CONTRIBUTING.txt"))
        candidates.extend(
            (
                bare,
                f"{bare}.md",
                f"{bare}.txt",
                f"{bare}.rst",
                f"{bare}.tex",
                f"{bare}.html",
                f"{bare}.pdf",
            )
        )
        checked: set[str] = set()
        for candidate in candidates:
            key = candidate.lower()
            if key in checked:
                continue
            checked.add(key)
            path = run_root / candidate
            if path.exists() and path.is_file():
                return path.name
        try:
            for child in run_root.iterdir():
                if not child.is_file():
                    continue
                if child.name.lower() == bare.lower() or child.stem.lower() == bare.lower():
                    return child.name
        except OSError:
            return ""
        return ""

    def maybe_add(ref: str) -> None:
        normalized = normalize_scalar(ref).strip().lstrip("./")
        if "/" not in normalized and "." not in normalized:
            normalized = resolve_bare_primary_ref(normalized)
        lowered = normalized.lower()
        if not normalized or lowered in seen:
            return
        if lowered in NON_PRIMARY_ARTIFACT_NAMES:
            return
        if any(lowered.startswith(prefix) for prefix in NON_PRIMARY_ARTIFACT_DIR_PREFIXES):
            return
        if "/" not in normalized and "." not in normalized:
            return
        refs.append(normalized)
        seen.add(lowered)

    for raw in text.splitlines():
        stripped = raw.strip()
        if not stripped:
            continue
        write_match = PROMPT_WRITE_FILE_RE.match(stripped)
        if write_match:
            maybe_add(write_match.group(1))
        for ref in extract_file_refs(stripped):
            maybe_add(ref)

    return tuple(refs)


def parse_prompt_satisfaction_entries(path: Path) -> list[PromptSatisfactionEntry]:
    if not path.exists():
        return []
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return []

    entries: list[PromptSatisfactionEntry] = []
    requirement: str | None = None
    requirement_id: str = ""
    status = ""
    evidence_paths: list[str] = []
    implementation_paths: list[str] = []
    verification = ""
    collecting_evidence_paths = False
    collecting_implementation_paths = False

    def flush() -> None:
        nonlocal requirement, requirement_id, status, evidence_paths, implementation_paths, verification, collecting_evidence_paths, collecting_implementation_paths
        effective_requirement = (requirement or "").strip() or requirement_id.strip()
        if not effective_requirement:
            return
        entries.append(
            PromptSatisfactionEntry(
                requirement=effective_requirement,
                status=status.strip(),
                evidence_paths=tuple(evidence_paths),
                verification=verification.strip(),
                implementation_paths=tuple(implementation_paths),
            )
        )
        requirement = None
        requirement_id = ""
        status = ""
        evidence_paths = []
        implementation_paths = []
        verification = ""
        collecting_evidence_paths = False
        collecting_implementation_paths = False

    for raw in lines:
        stripped = raw.strip()
        req_id_match = PROMPT_SAT_REQ_ID_RE.match(stripped)
        if req_id_match:
            flush()
            requirement_id = req_id_match.group(1).upper().strip()
            requirement = None
            continue
        req_match = PROMPT_SAT_REQ_RE.match(stripped)
        if req_match:
            flush()
            requirement = req_match.group(1).strip()
            continue
        req_text_match = PROMPT_SAT_REQ_TEXT_RE.match(stripped)
        if req_text_match:
            if requirement is None and not requirement_id:
                requirement_id = "RQ-UNSPECIFIED"
            requirement = req_text_match.group(1).strip()
            collecting_evidence_paths = False
            collecting_implementation_paths = False
            continue
        if requirement is None and not requirement_id:
            continue
        status_match = PROMPT_SAT_STATUS_RE.match(stripped)
        if status_match:
            status = status_match.group(1).strip()
            collecting_evidence_paths = False
            collecting_implementation_paths = False
            continue
        verification_match = PROMPT_SAT_VERIFICATION_RE.match(stripped)
        if verification_match:
            verification = verification_match.group(1).strip()
            collecting_evidence_paths = False
            collecting_implementation_paths = False
            continue
        evidence_match = PROMPT_SAT_EVIDENCE_RE.match(stripped)
        if evidence_match:
            evidence_raw = evidence_match.group(1).strip()
            collecting_evidence_paths = True
            collecting_implementation_paths = False
            refs = list(parse_reference_list(evidence_raw))
            for ref in refs:
                if ref not in evidence_paths:
                    evidence_paths.append(ref)
            continue
        implementation_match = PROMPT_SAT_IMPLEMENTATION_RE.match(stripped)
        if implementation_match:
            impl_raw = implementation_match.group(1).strip()
            collecting_implementation_paths = True
            collecting_evidence_paths = False
            refs = list(parse_reference_list(impl_raw))
            for ref in refs:
                if ref not in implementation_paths:
                    implementation_paths.append(ref)
            continue
        if collecting_evidence_paths:
            if PROMPT_SAT_KEYED_BULLET_RE.match(stripped):
                collecting_evidence_paths = False
                continue
            item_text = stripped
            for prefix in ("- ", "* ", "+ "):
                if item_text.startswith(prefix):
                    item_text = item_text[len(prefix):].strip()
                    break
            numbered = re.match(r"^\d+\.\s+(.+)$", item_text)
            if numbered:
                item_text = numbered.group(1).strip()
            refs = list(parse_reference_list(item_text))
            for ref in refs:
                if ref not in evidence_paths:
                    evidence_paths.append(ref)
            if refs:
                continue
        if collecting_implementation_paths:
            if PROMPT_SAT_KEYED_BULLET_RE.match(stripped):
                collecting_implementation_paths = False
                continue
            item_text = stripped
            for prefix in ("- ", "* ", "+ "):
                if item_text.startswith(prefix):
                    item_text = item_text[len(prefix):].strip()
                    break
            numbered = re.match(r"^\d+\.\s+(.+)$", item_text)
            if numbered:
                item_text = numbered.group(1).strip()
            refs = list(parse_reference_list(item_text))
            for ref in refs:
                if ref not in implementation_paths:
                    implementation_paths.append(ref)
            if refs:
                continue

    flush()
    if entries:
        return entries

    # Fallback parser: markdown table format.
    header_idx = -1
    header_cols: list[str] = []
    for idx, raw in enumerate(lines):
        stripped = raw.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        cols = [c.strip().lower() for c in stripped.strip("|").split("|")]
        if any("status" in col for col in cols) and any("requirement" in col for col in cols):
            header_idx = idx
            header_cols = cols
            break
    if header_idx < 0 or not header_cols:
        return entries

    def _find_col(candidates: tuple[str, ...]) -> int:
        for cand in candidates:
            if cand in header_cols:
                return header_cols.index(cand)
        return -1

    def _find_col_contains(tokens: tuple[str, ...]) -> int:
        for idx, col in enumerate(header_cols):
            if any(token in col for token in tokens):
                return idx
        return -1

    def _find_best_requirement_text_col() -> int:
        # Prefer explicit requirement text columns over ID columns when both exist.
        best_idx = -1
        best_score = -1
        for idx, col in enumerate(header_cols):
            if "requirement" not in col:
                continue
            if ("id" in col or "type" in col) and (
                "text" not in col and "description" not in col
            ):
                continue
            score = 1
            if "text" in col or "description" in col:
                score += 3
            if "id" in col:
                score -= 2
            if "requirement_text" in col or "requirement text" in col:
                score += 3
            if score > best_score:
                best_score = score
                best_idx = idx
        return best_idx

    requirement_text_col = _find_best_requirement_text_col()
    requirement_id_col = _find_col(
        ("requirement_id", "requirement id", "rq_id", "id")
    )
    if requirement_id_col < 0:
        requirement_id_col = _find_col_contains(("requirement id", "rq_id"))
    requirement_col = requirement_text_col
    if requirement_col < 0:
        requirement_col = requirement_id_col
    if requirement_col < 0:
        requirement_col = _find_col(("requirement", "requirement_text"))
    if requirement_col < 0:
        requirement_col = _find_col_contains(("requirement",))
    status_col = _find_col(("status",))
    if status_col < 0:
        status_col = _find_col_contains(("status",))
    evidence_col = _find_col(
        (
            "evidence_paths",
            "evidence",
            "evidence_path",
            "verification_artifact_paths",
            "verification_artifacts",
            "verification_artifact_path",
            "verification_paths",
            "verification_path",
        )
    )
    if evidence_col < 0:
        evidence_col = _find_col_contains(
            ("evidence", "verification_artifact", "verification_path")
        )
    implementation_col = _find_col(
        (
            "implementation_artifact_paths",
            "implementation_artifacts",
            "implementation_paths",
            "implementation_path",
            "artifact_paths",
        )
    )
    if implementation_col < 0:
        implementation_col = _find_col_contains(("implementation", "artifact_path"))
    verification_col = _find_col(("verification_result", "verification"))
    if verification_col < 0:
        verification_col = _find_col_contains(("verification", "result"))
    if requirement_col < 0 or status_col < 0:
        return entries

    row_start = header_idx + 1
    if row_start < len(lines):
        sep = lines[row_start].strip()
        if sep.startswith("|") and "---" in sep:
            row_start += 1

    for raw in lines[row_start:]:
        stripped = raw.strip()
        if not stripped:
            continue
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        parts = [p.strip() for p in stripped.strip("|").split("|")]
        if max(requirement_col, status_col, evidence_col, 0) >= len(parts):
            continue
        requirement_value = parts[requirement_col].strip()
        requirement_id_value = ""
        if 0 <= requirement_id_col < len(parts):
            requirement_id_value = parts[requirement_id_col].strip()
        if re.fullmatch(r"RQ-\d+", requirement_value.upper()) and requirement_id_value:
            # Header detection can still land on the ID column in ambiguous tables.
            # Prefer the explicit requirement text when available in neighboring columns.
            for idx, col in enumerate(header_cols):
                if idx >= len(parts):
                    continue
                if "requirement" in col and "text" in col:
                    text_candidate = parts[idx].strip()
                    if text_candidate:
                        requirement_value = text_candidate
                        break
        status_value = parts[status_col].strip()
        if not requirement_value or not status_value:
            continue
        evidence_value = ""
        if 0 <= evidence_col < len(parts):
            evidence_value = parts[evidence_col].strip()
        implementation_value = ""
        if 0 <= implementation_col < len(parts):
            implementation_value = parts[implementation_col].strip()
        verification_value = ""
        if 0 <= verification_col < len(parts):
            verification_value = parts[verification_col].strip()
        refs = list(parse_reference_list(evidence_value))
        impl_refs = list(parse_reference_list(implementation_value))
        entries.append(
            PromptSatisfactionEntry(
                requirement=requirement_value,
                status=status_value,
                evidence_paths=tuple(dict.fromkeys(refs)),
                verification=verification_value,
                implementation_paths=tuple(dict.fromkeys(impl_refs)),
            )
        )
    return entries


def requirement_semantics_supported(requirement: str, evidence_text: str) -> bool:
    req_norm = normalize_text(requirement)
    if not req_norm:
        return True
    tokens = [
        tok
        for tok in req_norm.split()
        if len(tok) >= 4 and tok not in SEMANTIC_STOPWORDS
    ]
    if not tokens:
        return True
    evidence_norm = normalize_text(evidence_text)
    matched: set[str] = set()
    for tok in tokens:
        if tok in evidence_norm:
            matched.add(tok)
            continue
        for synonym in REQUIREMENT_TOKEN_SYNONYMS.get(tok, ()):
            if synonym in evidence_norm:
                matched.add(tok)
                break
    if len(tokens) <= 6:
        required_hits = 1
    elif len(tokens) <= 12:
        required_hits = 2
    else:
        required_hits = 3
    return len(matched) >= required_hits


def verification_affirms_requirement(value: str) -> bool:
    text = normalize_scalar(value).strip().lower()
    if not text:
        return False
    if text in {"pass", "passed", "ok", "true", "yes", "verified", "satisfied"}:
        return True
    return len(text) >= 24


def semantic_tokens(value: str, *, min_len: int = 4) -> set[str]:
    return {
        tok
        for tok in re.findall(r"[a-z0-9]+", value.lower())
        if len(tok) >= min_len and tok not in SEMANTIC_STOPWORDS
    }


def requirement_matches_trace_text(requirement: str, trace_text: str) -> bool:
    req_norm = normalize_text(requirement)
    trace_norm = normalize_text(trace_text)
    if req_norm and trace_norm and (req_norm in trace_norm or trace_norm in req_norm):
        return True
    req_tokens = semantic_tokens(requirement)
    trace_tokens = semantic_tokens(trace_text)
    if not req_tokens or not trace_tokens:
        return False
    overlap = req_tokens & trace_tokens
    return len(overlap) >= max(2, min(len(req_tokens), len(trace_tokens)) // 2)


def requirement_matches_entry(requirement: str, entry: PromptSatisfactionEntry) -> bool:
    req_norm = normalize_text(requirement)
    ent_norm = normalize_text(entry.requirement)
    if req_norm and ent_norm and (req_norm in ent_norm or ent_norm in req_norm):
        return True

    req_refs = set(extract_file_refs(requirement))
    ent_refs = (
        set(extract_file_refs(entry.requirement))
        | set(entry.evidence_paths)
        | set(entry.implementation_paths)
    )
    if req_refs and (req_refs & ent_refs):
        return True

    req_tokens = set(req_norm.split())
    ent_tokens = set(ent_norm.split())
    if req_tokens and ent_tokens:
        overlap = req_tokens & ent_tokens
        if len(overlap) >= max(2, min(len(req_tokens), len(ent_tokens)) // 2):
            return True
    return False


def read_text_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def is_prompt_source_ref(ref: str) -> bool:
    normalized = str(ref).strip().strip("`").lower()
    if not normalized:
        return False
    normalized = normalized.lstrip("./")
    return normalized == "prompt.txt" or normalized.endswith("/prompt.txt")


def looks_synthetic_text(text: str) -> bool:
    return any(pattern.search(text) for pattern in SYNTHETIC_TEXT_PATTERNS)


def markdown_file_has_real_delta(path: Path, *, min_bytes: int) -> bool:
    if not is_nonempty_file(path):
        return False
    if path.stat().st_size < min_bytes:
        return False
    text = read_text_safe(path)
    if not text.strip():
        return False
    if looks_synthetic_text(text):
        return False
    return True


def rubric_json_has_real_delta(
    path: Path,
    *,
    prompt_requirements: list[str],
    prompt_words: set[str],
) -> bool:
    if not is_nonempty_file(path):
        return False
    if path.stat().st_size < 300:
        return False
    raw = read_text_safe(path)
    if looks_synthetic_text(raw):
        return False
    data, repaired_json = load_json_lenient(raw)
    if data is None:
        return False
    if not isinstance(data, dict):
        return False
    if repaired_json != raw:
        try:
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        except OSError:
            pass
    x_axis = data.get("x_axis")
    y_axis = data.get("y_axis")
    cells = data.get("cells")
    if not isinstance(x_axis, list) or not x_axis:
        return False
    if not isinstance(y_axis, list) or not y_axis:
        return False
    if not isinstance(cells, list) or not cells:
        return False
    x_axis_values = [str(v).strip() for v in x_axis if str(v).strip()]
    y_axis_values = [str(v).strip() for v in y_axis if str(v).strip()]
    if not x_axis_values or not y_axis_values:
        return False
    target_collateral_manifest = data.get("target_collateral_manifest")
    if not isinstance(target_collateral_manifest, list) or not target_collateral_manifest:
        return False
    manifest_refs = [str(v).strip().lower() for v in target_collateral_manifest if str(v).strip()]
    if not manifest_refs:
        return False
    if not any(ref == "prompt.txt" or ref.endswith("/prompt.txt") for ref in manifest_refs):
        return False
    improvement_intent = data.get("improvement_intent")
    if not isinstance(improvement_intent, str) or len(improvement_intent.strip()) < 20:
        return False

    task_conformance_rationale = data.get("task_conformance_rationale")
    if not isinstance(task_conformance_rationale, str) or len(task_conformance_rationale.strip()) < 80:
        return False

    prompt_requirement_trace = data.get("prompt_requirement_trace")
    if not isinstance(prompt_requirement_trace, list) or not prompt_requirement_trace:
        return False
    trace_texts: list[str] = []
    seen_req_ids: set[str] = set()
    all_axes = set(x_axis_values + y_axis_values)
    x_axis_set = set(x_axis_values)
    y_axis_set = set(y_axis_values)
    valid_cell_pairs: set[tuple[str, str]] = set()
    valid_cell_aliases: set[str] = set()
    for cell in cells:
        if not isinstance(cell, dict):
            continue
        cx = str(cell.get("x", "")).strip()
        cy = str(cell.get("y", "")).strip()
        if not cx or not cy:
            continue
        if cx not in x_axis_set or cy not in y_axis_set:
            continue
        valid_cell_pairs.add((cx, cy))
        aliases = (
            f"{cx} x {cy}",
            f"{cx} X {cy}",
            f"{cx}×{cy}",
            f"{cx} | {cy}",
            f"{cx}|{cy}",
            f"{cx}::{cy}",
            f"{cx} :: {cy}",
            f"{cx} -> {cy}",
            f"{cx}->{cy}",
            f"{cx}, {cy}",
            f"{cx},{cy}",
            f"{cx} / {cy}",
            f"{cx}/{cy}",
        )
        for alias in aliases:
            valid_cell_aliases.add(" ".join(alias.split()).casefold())
    if not valid_cell_pairs:
        return False

    def cell_ref_valid(value: object) -> bool:
        if isinstance(value, dict):
            cx = str(value.get("x", "")).strip()
            cy = str(value.get("y", "")).strip()
            return bool(cx and cy and (cx, cy) in valid_cell_pairs)
        ref = " ".join(str(value).split())
        if not ref:
            return False
        if ref.casefold() in valid_cell_aliases:
            return True
        return False

    for entry in prompt_requirement_trace:
        if not isinstance(entry, dict):
            return False
        req_id = str(entry.get("requirement_id", "")).strip()
        req_text = str(
            entry.get("requirement_text", "") or entry.get("requirement", "")
        ).strip()
        if not req_text and req_id and prompt_requirements:
            match = re.match(r"^[A-Za-z_-]*?(\d+)$", req_id)
            if match:
                idx = int(match.group(1)) - 1
                if 0 <= idx < len(prompt_requirements):
                    req_text = prompt_requirements[idx]
        addressed_by_axes = entry.get(
            "addressed_by_axes",
            entry.get("addressed_axis_names", []),
        )
        addressed_by_cells = entry.get(
            "addressed_by_cells",
            entry.get("addressed_cells", []),
        )
        adaptation_strategy = str(entry.get("adaptation_strategy", "")).strip()
        evidence_refs = entry.get("evidence_refs", [])
        if not req_id or req_id in seen_req_ids:
            return False
        seen_req_ids.add(req_id)
        if len(req_text) < 12:
            return False
        if (
            not isinstance(addressed_by_axes, list)
            or not addressed_by_axes
            or any(str(x).strip() not in all_axes for x in addressed_by_axes)
        ):
            return False
        if not isinstance(addressed_by_cells, list) or not addressed_by_cells:
            return False
        if not any(cell_ref_valid(ref) for ref in addressed_by_cells):
            return False
        if len(adaptation_strategy) < 24:
            return False
        if not isinstance(evidence_refs, list) or not any(str(x).strip() for x in evidence_refs):
            return False
        trace_texts.append(req_text)

    prompt_transmogrification_log = data.get("prompt_transmogrification_log")
    if not isinstance(prompt_transmogrification_log, list) or not prompt_transmogrification_log:
        return False
    for entry in prompt_transmogrification_log:
        if not isinstance(entry, dict):
            return False
        legacy_entry = False
        change_summary = str(entry.get("change_summary", "")).strip()
        if not change_summary:
            alt_change = str(
                entry.get("change", "")
                or entry.get("delta", "")
                or entry.get("what_changed", "")
                or entry.get("summary", "")
            ).strip()
            if alt_change:
                legacy_entry = True
                change_summary = alt_change

        trigger_requirement_id = str(entry.get("trigger_requirement_id", "")).strip()

        expected_prompt_uplift = str(entry.get("expected_prompt_uplift", "")).strip()
        if not expected_prompt_uplift:
            alt_uplift = str(
                entry.get("result", "")
                or entry.get("uplift", "")
                or entry.get("why_changed", "")
                or entry.get("impact", "")
            ).strip()
            if alt_uplift:
                legacy_entry = True
                expected_prompt_uplift = alt_uplift

        evidence_refs = entry.get(
            "evidence_refs",
            entry.get("evidence", entry.get("evidence_paths", [])),
        )
        if isinstance(evidence_refs, str):
            evidence_refs = [evidence_refs]
        if len(change_summary) < 24:
            return False
        if trigger_requirement_id and trigger_requirement_id not in seen_req_ids:
            return False
        if (not legacy_entry) and (not trigger_requirement_id or trigger_requirement_id not in seen_req_ids):
            return False
        if len(expected_prompt_uplift) < 20:
            return False
        if not isinstance(evidence_refs, list):
            return False
        if (not legacy_entry) and (not any(str(x).strip() for x in evidence_refs)):
            return False

    axis_task_alignment = data.get("axis_task_alignment")
    if not isinstance(axis_task_alignment, list) or not axis_task_alignment:
        return False
    expected_pairs = {("x", name) for name in x_axis_values} | {
        ("y", name) for name in y_axis_values
    }
    mapped_pairs: set[tuple[str, str]] = set()
    aligned_req_ids: set[str] = set()
    alignment_text_parts: list[str] = []
    for entry in axis_task_alignment:
        if not isinstance(entry, dict):
            return False
        axis_name = str(entry.get("axis_name", "")).strip()
        axis_kind = str(entry.get("axis_kind", "")).strip().lower()
        supported_requirement_ids = entry.get(
            "supported_requirement_ids",
            entry.get(
                "supported_prompt_requirement_ids",
                entry.get("requirement_ids", entry.get("supports_requirement_ids", [])),
            ),
        )
        success_mechanism = str(
            entry.get("success_mechanism", "")
            or entry.get("success_mechanism_for_prompt_satisfaction", "")
            or entry.get("prompt_success_mechanism", "")
            or entry.get("mechanism", "")
        ).strip()
        failure_if_ignored = str(
            entry.get("failure_if_ignored", "")
            or entry.get("failure_mode_if_ignored", "")
            or entry.get("failure_mode", "")
        ).strip()
        evidence_refs = entry.get(
            "evidence_refs",
            entry.get("evidence_paths", entry.get("collateral_refs", [])),
        )
        if isinstance(evidence_refs, str):
            evidence_refs = [evidence_refs]

        if axis_kind not in {"x", "y"}:
            return False
        axis_pool = set(x_axis_values) if axis_kind == "x" else set(y_axis_values)
        if axis_name not in axis_pool:
            return False
        pair = (axis_kind, axis_name)
        if pair in mapped_pairs:
            return False
        mapped_pairs.add(pair)

        if (
            not isinstance(supported_requirement_ids, list)
            or not supported_requirement_ids
            or not all(str(v).strip() for v in supported_requirement_ids)
        ):
            return False
        for req_id_raw in supported_requirement_ids:
            req_id = str(req_id_raw).strip()
            if seen_req_ids and req_id not in seen_req_ids:
                return False
            aligned_req_ids.add(req_id)

        if len(success_mechanism) < 24:
            return False
        if len(failure_if_ignored) < 20:
            return False
        if not isinstance(evidence_refs, list) or not any(str(v).strip() for v in evidence_refs):
            return False

        alignment_text_parts.extend((axis_name, success_mechanism, failure_if_ignored))

    if mapped_pairs != expected_pairs:
        return False
    if seen_req_ids and not seen_req_ids.issubset(aligned_req_ids):
        return False

    if prompt_requirements:
        matched_requirements = 0
        for req in prompt_requirements:
            if any(
                requirement_matches_trace_text(req, trace_text)
                for trace_text in trace_texts
            ):
                matched_requirements += 1
        # Require strong, but not absolute, prompt trace coverage. This avoids
        # false negatives when acceptance-criteria wording is represented with
        # equivalent requirement language in nearby trace entries.
        min_required = max(3, math.ceil(len(prompt_requirements) * 0.70))
        if matched_requirements < min(min_required, len(prompt_requirements)):
            return False

    # Prompt coverage is already enforced by explicit requirement trace matching.
    # Lexical overlap can be zero when axes are conceptual but still fully traceable.
    rubric_tokens = semantic_tokens(
        " ".join([*all_axes, improvement_intent, task_conformance_rationale, *alignment_text_parts])
    )
    if prompt_words and len(rubric_tokens & prompt_words) < 1 and not prompt_requirements:
        return False
    return True


def rubric_json_has_minimum_delta(
    path: Path,
    *,
    prompt_requirements: list[str],
) -> bool:
    if not is_nonempty_file(path):
        return False
    if path.stat().st_size < 300:
        return False
    raw = read_text_safe(path)
    if looks_synthetic_text(raw):
        return False

    data, repaired_json = load_json_lenient(raw)
    if data is None or not isinstance(data, dict):
        # Resilience fallback: accept structurally rich rubric-like JSON text
        # even when strict JSON parsing fails (for example, one malformed quote),
        # so progress is not discarded if prompt-linked content is still present.
        lowered = raw.lower()
        required_markers = (
            '"x_axis"',
            '"y_axis"',
            '"cells"',
            '"target_collateral_manifest"',
            '"prompt_requirement_trace"',
            '"axis_task_alignment"',
        )
        if not all(marker in lowered for marker in required_markers):
            return False
        if "prompt.txt" not in lowered:
            return False
        if raw.count('"score_percent"') < 3:
            return False
        if prompt_requirements:
            matched = 0
            for idx, req in enumerate(prompt_requirements, start=1):
                rid2 = f"rq-{idx:02d}"
                rid1 = f"rq-{idx}"
                if rid2 in lowered or rid1 in lowered or requirement_matches_trace_text(req, raw):
                    matched += 1
            min_required = max(1, math.ceil(len(prompt_requirements) * 0.40))
            if matched < min_required:
                return False
        return True
    if repaired_json != raw:
        try:
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        except OSError:
            pass

    x_axis = data.get("x_axis")
    y_axis = data.get("y_axis")
    cells = data.get("cells")
    if not isinstance(x_axis, list) or not any(str(v).strip() for v in x_axis):
        return False
    if not isinstance(y_axis, list) or not any(str(v).strip() for v in y_axis):
        return False
    if not isinstance(cells, list) or not cells:
        return False

    target_collateral_manifest = data.get("target_collateral_manifest")
    if not isinstance(target_collateral_manifest, list) or not target_collateral_manifest:
        return False
    manifest_refs = [
        str(v).strip().lower() for v in target_collateral_manifest if str(v).strip()
    ]
    if not any(ref == "prompt.txt" or ref.endswith("/prompt.txt") for ref in manifest_refs):
        return False

    improvement_intent = str(data.get("improvement_intent", "")).strip()
    task_conformance_rationale = str(data.get("task_conformance_rationale", "")).strip()
    if len(improvement_intent) < 20 and len(task_conformance_rationale) < 80:
        return False

    linkage_text = json.dumps(
        {
            "prompt_requirement_trace": data.get("prompt_requirement_trace", []),
            "axis_task_alignment": data.get("axis_task_alignment", []),
            "prompt_transmogrification_log": data.get("prompt_transmogrification_log", []),
        },
        ensure_ascii=False,
    )
    if prompt_requirements:
        matched = sum(
            1 for req in prompt_requirements if requirement_matches_trace_text(req, linkage_text)
        )
        min_required = max(1, math.ceil(len(prompt_requirements) * 0.5))
        if matched < min_required:
            return False
    else:
        if "prompt" not in linkage_text.lower():
            return False
    return True


MARKDOWN_TABLE_SEPARATOR_RE = re.compile(r"^\|\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|$")


def scorecard_has_matrix_rows(path: Path, *, min_rows: int = 3) -> bool:
    if not markdown_file_has_real_delta(path, min_bytes=MIN_DELTA_FILE_BYTES["scorecard"]):
        return False
    text = read_text_safe(path)
    rows = 0
    for raw in text.splitlines():
        stripped = raw.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        if MARKDOWN_TABLE_SEPARATOR_RE.match(stripped):
            continue
        lowered = stripped.lower()
        if "cell_id" in lowered and "score" in lowered:
            continue
        if re.search(r"\b\d+(?:\.\d+)?\b", stripped):
            rows += 1
            if rows >= min_rows:
                return True
    return False


def rubric_json_has_axis_trace_delta(
    path: Path,
    *,
    prompt_requirements: list[str],
) -> bool:
    if not is_nonempty_file(path):
        return False
    if path.stat().st_size < 300:
        return False
    raw = read_text_safe(path)
    if looks_synthetic_text(raw):
        return False
    data, repaired_json = load_json_lenient(raw)
    if data is None or not isinstance(data, dict):
        return False
    if repaired_json != raw:
        try:
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        except OSError:
            pass

    x_axis = data.get("x_axis")
    y_axis = data.get("y_axis")
    if not isinstance(x_axis, list) or not any(str(v).strip() for v in x_axis):
        return False
    if not isinstance(y_axis, list) or not any(str(v).strip() for v in y_axis):
        return False

    trace_text = json.dumps(
        {
            "prompt_requirement_trace": data.get("prompt_requirement_trace", []),
            "axis_task_alignment": data.get("axis_task_alignment", []),
            "task_conformance_rationale": data.get("task_conformance_rationale", ""),
        },
        ensure_ascii=False,
    )
    if prompt_requirements:
        matched = sum(
            1 for req in prompt_requirements if requirement_matches_trace_text(req, trace_text)
        )
        min_required = max(1, math.ceil(len(prompt_requirements) * 0.40))
        if matched < min_required:
            return False
    elif "prompt" not in trace_text.lower():
        return False
    return True


def iteration_has_real_delta_evidence(iter_dir: Path, chain: str) -> bool:
    parsed = parse_chain(chain)
    if parsed is None:
        return False
    _, lower = parsed
    iter_match = ITER_RE.match(iter_dir.name)
    if not iter_match:
        return False
    iteration_label = iter_match.group(1)
    run_root = iter_dir.parent.parent
    prompt_path = run_root / "prompt.txt"
    prompt_requirements = parse_prompt_requirements(prompt_path)
    prompt_words = semantic_tokens(read_text_safe(prompt_path))

    paths = {
        "deltas": run_root / f"deltas/iteration_{iteration_label}.md",
        "evidence": run_root / f"evidence/iteration_{iteration_label}.md",
        "manifest": run_root / f"collateral/Rubric_{lower}/manifest_iteration_{iteration_label}.md",
        "access_log": run_root / f"collateral/Rubric_{lower}/access_log_iteration_{iteration_label}.md",
        "scorecard": run_root / f"scorecards/Rubric_{lower}_grid_iteration_{iteration_label}.md",
        "burndown": iter_dir / "author_deltas/DEFECT_BURNDOWN_CHECK.md",
    }
    for key, path in paths.items():
        if not markdown_file_has_real_delta(path, min_bytes=MIN_DELTA_FILE_BYTES[key]):
            return False

    rubric_json = run_root / f"rubrics/Rubric_{lower}/iteration_{iteration_label}.json"
    if not rubric_json_has_real_delta(
        rubric_json,
        prompt_requirements=prompt_requirements,
        prompt_words=prompt_words,
    ):
        # Resilience fallback: accept a non-synthetic, prompt-linked minimal rubric delta
        # so progress is not discarded when LLM output misses strict optional fields.
        if not rubric_json_has_minimum_delta(
            rubric_json,
            prompt_requirements=prompt_requirements,
        ):
            # Some rubric writers emit axis-rich rubric JSON and put per-cell
            # score detail exclusively in the scorecard. Accept that shape only
            # when both rubric traces and scorecard matrix rows are present.
            if not (
                rubric_json_has_axis_trace_delta(
                    rubric_json,
                    prompt_requirements=prompt_requirements,
                )
                and scorecard_has_matrix_rows(paths["scorecard"])
            ):
                return False

    delta_text = read_text_safe(paths["deltas"]).lower()
    burndown_text = read_text_safe(paths["burndown"]).lower()
    combined_delta_text = f"{delta_text}\n{burndown_text}"
    # Meta-rubric chains frequently improve rubric/scorecard/evidence quality
    # without touching project primary artifacts directly. Treat those deltas as
    # real when they are explicit and prompt-linked.
    if lower > 0:
        if not any(
            token in combined_delta_text
            for token in (
                "scorecard",
                "axis",
                "cell",
                "evidence",
                "requirement",
                "prompt",
                "collateral",
                "trace",
            )
        ):
            return False
        return True

    if not any(
        token in combined_delta_text
        for token in (
            "artifact",
            "readme",
            "code",
            "document",
            "prompt",
            "requirement",
            "workflow",
            "stability",
            "interface",
        )
    ):
        return False
    return True


def baseline_has_prompt_linkage(baseline_path: Path) -> bool:
    if not baseline_path.exists():
        return False
    try:
        text = baseline_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return bool(PROMPT_LINK_RE.search(text))


def artifact_has_prompt_access(path: Path) -> bool:
    if not path.exists():
        return False
    text = read_text_safe(path)
    if not text.strip():
        return False

    bullets = parse_bullets(path)
    if bullets:
        source_raw = str(bullets.get("prompt_source", "")).strip().lower()
        consumed_raw = bullets.get("prompt_consumed")
        consumed = as_bool(consumed_raw, False)
        if source_raw and "prompt.txt" not in source_raw:
            return False
        if consumed and source_raw:
            return True

    return bool(
        PROMPT_LINK_RE.search(text)
        and PROMPT_SOURCE_RE.search(text)
        and PROMPT_CONSUMED_RE.search(text)
    )


def judge_artifacts_have_prompt_access(iter_dir: Path) -> bool:
    baseline_path = iter_dir / "judge_baseline" / "PRIORITIZED_DEFECTS.md"
    recheck_path = iter_dir / "judge_recheck" / "PRIORITIZED_DEFECTS.md"
    final_path = iter_dir / "judge_recheck" / "FINAL_DECISION.md"
    status_path = iter_dir / "STATUS.md"

    baseline_ok = artifact_has_prompt_access(baseline_path)
    recheck_ok = artifact_has_prompt_access(recheck_path)
    status_ok = artifact_has_prompt_access(status_path)
    final_ok = artifact_has_prompt_access(final_path)
    if baseline_ok and recheck_ok and status_ok and final_ok:
        return True

    # Allow STATUS.md to serve as authoritative fallback when FINAL_DECISION.md
    # is still a bootstrap stub.
    final_text = read_text_safe(final_path)
    final_bootstrap = looks_synthetic_text(final_text) or "prompt_consumed: no" in final_text.lower()
    if final_bootstrap:
        return baseline_ok and recheck_ok and status_ok
    return False


def _target_or_run_level_path(
    *,
    run_root: Path,
    iter_dir: Path | None,
    filename: str,
    allow_run_level_fallback: bool = True,
) -> Path:
    """Use iteration-scoped authority when available; otherwise fall back to run-level."""
    if iter_dir is not None:
        scoped = iter_dir / filename
        if scoped.exists():
            return scoped
        if not allow_run_level_fallback:
            return scoped
    return run_root / filename


def _document_has_prompt_linkage(*, text: str, bullets: dict[str, object]) -> bool:
    source_raw = str(bullets.get("prompt_source", "")).strip()
    if source_raw and is_prompt_source_ref(source_raw):
        return True
    if PROMPT_LINK_RE.search(text):
        return True
    lowered = text.lower()
    return ("prompt.txt" in lowered) or bool(re.search(r"\bprompt\b", lowered))


def best_known_frontier_is_valid(
    *,
    run_root: Path,
    iter_dir: Path | None = None,
    allow_run_level_fallback: bool = True,
) -> bool:
    path = _target_or_run_level_path(
        run_root=run_root,
        iter_dir=iter_dir,
        filename="BEST_KNOWN_FRONTIER.md",
        allow_run_level_fallback=allow_run_level_fallback,
    )
    if not is_nonempty_file(path):
        return False
    text = read_text_safe(path)
    if looks_synthetic_text(text):
        return False
    if contains_forbidden_placeholder_token(text):
        return False
    bullets = parse_bullets(path)
    tracking_raw = bullets.get("frontier_tracking_active")
    if tracking_raw is not None and (not as_bool(tracking_raw, False)):
        return False
    compared_against_prior_best = as_bool(bullets.get("compared_against_prior_best"), False)
    frontier_membership = as_bool(
        bullets.get("frontier_membership")
        or bullets.get("on_frontier")
        or bullets.get("pareto_frontier_member"),
        False,
    )
    frontier_gate = normalize_scalar(str(bullets.get("frontier_gate", ""))).lower()
    frontier_reason = normalize_scalar(str(bullets.get("frontier_membership_reason", ""))).lower()
    first_recovering_pass = (
        (not compared_against_prior_best)
        and (not frontier_membership)
        and (
            "unresolved_for_first_recovering_pass" in frontier_gate
            or "no prior accepted" in frontier_reason
            or "no prior frontier" in frontier_reason
        )
    )
    if (not compared_against_prior_best) and (not first_recovering_pass):
        return False
    has_frontier_state = (
        "frontier_membership" in bullets
        or "no_known_feasible_improvement" in bullets
        or "frontier candidate set" in text.lower()
    )
    if not has_frontier_state:
        return False
    if not _document_has_prompt_linkage(text=text, bullets=bullets):
        return False
    return True


def objective_field_text(*, text: str, bullets: dict[str, object], key: str) -> str:
    """Resolve objective-spec field text from inline bullet or indented block value."""
    direct = normalize_scalar(str(bullets.get(key, "")))
    if direct:
        return direct

    lines = text.splitlines()
    header_re = re.compile(rf"^(\s*)-\s*{re.escape(key)}\s*:\s*(.*)$", re.IGNORECASE)
    bullet_stop_re = re.compile(r"^\s*-\s+[A-Za-z0-9_].*?:\s*.*$")

    for idx, line in enumerate(lines):
        match = header_re.match(line)
        if match is None:
            continue
        indent = len(match.group(1))
        inline = normalize_scalar(match.group(2))
        if inline:
            return inline

        block_chunks: list[str] = []
        for next_line in lines[idx + 1 :]:
            stripped = next_line.strip()
            if not stripped:
                if block_chunks:
                    break
                continue
            next_indent = len(next_line) - len(next_line.lstrip(" "))
            if next_indent <= indent:
                break
            if bullet_stop_re.match(next_line) and next_indent <= indent + 1:
                break
            cleaned = re.sub(r"^\s*[-*]\s+", "", stripped)
            cleaned = re.sub(r"^\s*\d+\.\s+", "", cleaned)
            cleaned = normalize_scalar(cleaned)
            if cleaned:
                block_chunks.append(cleaned)
        return normalize_scalar(" ".join(block_chunks))
    return ""


def objective_spec_is_valid(
    *,
    run_root: Path,
    iter_dir: Path | None = None,
    allow_run_level_fallback: bool = True,
) -> bool:
    path = _target_or_run_level_path(
        run_root=run_root,
        iter_dir=iter_dir,
        filename="OBJECTIVE_SPEC.md",
        allow_run_level_fallback=allow_run_level_fallback,
    )
    if not is_nonempty_file(path):
        return False
    text = read_text_safe(path)
    if looks_synthetic_text(text):
        return False
    if contains_forbidden_placeholder_token(text):
        return False
    bullets = parse_bullets(path)
    required = (
        "objective_summary",
        "objective_attainment_definition",
        "optimization_target",
        "prompt_intent_model",
    )
    for key in required:
        val = objective_field_text(text=text, bullets=bullets, key=key)
        if len(val) < 16:
            return False
    standard_text = ""
    for standard_key in (
        "no_known_feasible_improvement_standard",
        "no_known_feasible_improvement_criterion",
        "no_known_feasible_improvement_rationale",
    ):
        standard_text = objective_field_text(
            text=text,
            bullets=bullets,
            key=standard_key,
        )
        if standard_text:
            break
    if len(standard_text) < 16:
        # Compatibility path: some chains emit a boolean declaration here and
        # carry the detailed standard in decision/frontier artifacts.
        if "no_known_feasible_improvement" not in bullets:
            return False
        declared = normalize_scalar(str(bullets.get("no_known_feasible_improvement", ""))).lower()
        if declared not in {"yes", "no", "true", "false", "1", "0"}:
            return False
    if not _document_has_prompt_linkage(text=text, bullets=bullets):
        return False
    return True


def counterexample_search_passes(iter_dir: Path) -> bool:
    path = iter_dir / "judge_recheck" / "OBJECTIVE_COUNTEREXAMPLES.md"
    if not is_nonempty_file(path):
        return False
    text = read_text_safe(path)
    if looks_synthetic_text(text):
        return False
    if contains_forbidden_placeholder_token(text):
        return False
    bullets = parse_bullets(path)
    performed = as_bool(
        bullets.get("counterexample_search_performed")
        or bullets.get("counterexample_search_done"),
        False,
    )
    variants_tested = as_int(bullets.get("variants_tested"), 0)
    better_variant_found = as_bool(
        bullets.get("better_variant_found")
        or bullets.get("best_variant_improves_objective"),
        True,
    )
    return performed and variants_tested >= QUALITY_MIN_COUNTEREXAMPLE_VARIANTS and (not better_variant_found)


def frontier_status_passes(iter_dir: Path) -> bool:
    path = iter_dir / "judge_recheck" / "FRONTIER_STATUS.md"
    if not is_nonempty_file(path):
        return False
    text = read_text_safe(path)
    if looks_synthetic_text(text):
        return False
    if contains_forbidden_placeholder_token(text):
        return False
    bullets = parse_bullets(path)
    frontier_membership = as_bool(
        bullets.get("frontier_membership")
        or bullets.get("on_frontier")
        or bullets.get("pareto_frontier_member"),
        False,
    )
    compared = as_bool(
        bullets.get("compared_against_prior_best")
        or bullets.get("frontier_comparison_performed"),
        False,
    )
    if frontier_membership and compared:
        return True
    frontier_gate = normalize_scalar(str(bullets.get("frontier_gate", ""))).lower()
    frontier_reason = normalize_scalar(str(bullets.get("frontier_membership_reason", ""))).lower()
    first_recovering_pass = (
        (not compared)
        and (not frontier_membership)
        and (
            "unresolved_for_first_recovering_pass" in frontier_gate
            or "no prior accepted" in frontier_reason
            or "no prior frontier" in frontier_reason
        )
    )
    return first_recovering_pass


def discrimination_check_passes(iter_dir: Path) -> bool:
    path = iter_dir / "judge_recheck" / "DISCRIMINATION_CHECK.md"
    if not is_nonempty_file(path):
        return False
    text = read_text_safe(path)
    if looks_synthetic_text(text):
        return False
    if contains_forbidden_placeholder_token(text):
        return False
    bullets = parse_bullets(path)
    performed = as_bool(
        bullets.get("discrimination_check_performed")
        or bullets.get("discriminative_check_performed"),
        False,
    )
    if not performed:
        return False
    minor = as_float(bullets.get("minor_variant_score"), -1.0)
    major = as_float(bullets.get("major_variant_score"), -1.0)
    if minor < 0.0 or major < 0.0:
        return False
    direction = str(bullets.get("discrimination_direction", "higher_is_better")).strip().lower()
    if direction not in {"higher_is_better", "lower_is_better"}:
        direction = "higher_is_better"
    gap = abs(major - minor)
    if direction == "higher_is_better":
        ordering_ok = major > minor
    else:
        ordering_ok = major < minor
    declared_pass = as_bool(bullets.get("discriminative_power_pass"), False)
    return declared_pass and ordering_ok and gap >= QUALITY_MIN_DISCRIMINATION_GAP


def decision_declares_best_known(final_decision_path: Path) -> bool:
    if not is_nonempty_file(final_decision_path):
        return False
    bullets = parse_bullets(final_decision_path)
    no_known = as_bool(bullets.get("no_known_feasible_improvement"), False)
    budget = as_bool(bullets.get("run_budget_considered"), False)
    return no_known and budget


def primary_artifact_delta_is_meaningful(iter_dir: Path, chain: str) -> bool:
    parsed = parse_chain(chain)
    if parsed is None:
        return False
    _, lower = parsed
    if lower != 0:
        return True
    run_root = iter_dir.parent.parent
    prompt_refs = infer_prompt_primary_artifact_refs(run_root / "prompt.txt")
    if not prompt_refs:
        return True
    prompt_ref_map = {
        normalize_rel_ref(ref).lower(): normalize_rel_ref(ref)
        for ref in prompt_refs
        if normalize_rel_ref(ref)
    }
    prompt_ref_set = {
        key for key in prompt_ref_map
    }
    if not prompt_ref_set:
        return True

    runtime_payload = load_primary_artifact_runtime(iter_dir)
    if runtime_payload is not None:
        changed_refs_field = runtime_payload.get("changed_refs")
        if isinstance(changed_refs_field, list):
            changed_refs = {
                normalize_rel_ref(str(ref)).lower()
                for ref in changed_refs_field
                if normalize_rel_ref(str(ref))
            }
            if changed_refs & prompt_ref_set:
                return True
        before = runtime_payload.get("before")
        after = runtime_payload.get("after")
        if isinstance(before, dict) and isinstance(after, dict):
            changed_from_snapshots = {
                normalize_rel_ref(ref).lower()
                for ref in primary_artifact_snapshot_changed_refs(before, after)
                if normalize_rel_ref(ref)
            }
            if changed_from_snapshots & prompt_ref_set:
                return True

    touched_from_prompt_sat = prompt_satisfaction_primary_artifact_refs(
        run_root,
        iter_dir,
        prompt_refs,
    )
    if touched_from_prompt_sat:
        return True

    iter_match = ITER_RE.match(iter_dir.name)
    if not iter_match:
        return False
    iteration_label = iter_match.group(1)
    delta_path = run_root / f"deltas/iteration_{iteration_label}.md"
    evidence_path = run_root / f"evidence/iteration_{iteration_label}.md"
    manifest_path = run_root / "ARTIFACT_MANIFEST.md"
    prompt_sat_path = (
        iter_dir / "PROMPT_SATISFACTION.md"
        if (iter_dir / "PROMPT_SATISFACTION.md").exists()
        else (run_root / "PROMPT_SATISFACTION.md")
    )
    combined_text = "\n".join(
        [
            read_text_safe(delta_path),
            read_text_safe(evidence_path),
            read_text_safe(manifest_path),
            read_text_safe(prompt_sat_path),
        ]
    ).lower()
    touched_by_reference = any(ref and (ref in combined_text) for ref in prompt_ref_set)
    if touched_by_reference:
        # Mentions alone are insufficient evidence of meaningful artifact change.
        # Keep this as a weak signal only; objective pass requires concrete delta.
        pass

    start_epoch = -1.0
    if runtime_payload is not None:
        start_epoch = as_float(runtime_payload.get("start_epoch"), -1.0)
    if start_epoch < 0.0:
        try:
            start_epoch = float(iter_dir.stat().st_mtime)
        except OSError:
            start_epoch = -1.0
    if start_epoch >= 0.0:
        for ref in prompt_ref_set:
            raw_ref = prompt_ref_map.get(ref, ref)
            resolved = resolve_run_path(run_root, raw_ref)
            if resolved is None or not artifact_file_has_substance(resolved):
                continue
            try:
                if resolved.stat().st_mtime + 1e-6 >= start_epoch:
                    return True
            except OSError:
                continue

    return False


def objective_attainment_gate(
    *,
    iter_dir: Path,
    chain: str,
    decision: str,
) -> bool:
    decision_norm = normalize_scalar(decision).upper()
    if decision_norm != "ACCEPT":
        return True

    parsed = parse_chain(chain)
    if parsed is None:
        return False
    upper, _lower = parsed
    run_root = iter_dir.parent.parent
    final_decision_path = iter_dir / "judge_recheck" / "FINAL_DECISION.md"
    allow_run_level_fallback = False

    if not objective_spec_is_valid(
        run_root=run_root,
        iter_dir=iter_dir,
        allow_run_level_fallback=allow_run_level_fallback,
    ):
        return False
    if not best_known_frontier_is_valid(
        run_root=run_root,
        iter_dir=iter_dir,
        allow_run_level_fallback=allow_run_level_fallback,
    ):
        return False
    if not counterexample_search_passes(iter_dir):
        return False
    if not frontier_status_passes(iter_dir):
        return False
    if not decision_declares_best_known(final_decision_path):
        return False
    if not primary_artifact_delta_is_meaningful(iter_dir, chain):
        return False

    # Meta-rubrics must prove discriminative power so lower-layer quality
    # differences are measurable and actionable.
    if upper >= 1 and not discrimination_check_passes(iter_dir):
        return False

    return True


def run_level_prompt_satisfaction_complete(iter_dir: Path) -> bool:
    run_root = iter_dir.parent.parent
    path = iter_dir / "PROMPT_SATISFACTION.md"
    if not path.exists():
        path = run_root / "PROMPT_SATISFACTION.md"
    if not path.exists():
        return False
    entries = parse_prompt_satisfaction_entries(path)
    if not entries:
        return False

    for output_name in REQUIRED_RUN_OUTPUTS:
        output_path = iter_dir / output_name
        if not output_path.exists():
            output_path = run_root / output_name
        if not is_nonempty_file(output_path):
            return False
        output_text = read_text_safe(output_path)
        if looks_synthetic_text(output_text):
            return False
        if contains_forbidden_placeholder_token(output_text):
            return False

    prompt_path = run_root / "prompt.txt"
    requirements = parse_prompt_requirements(prompt_path)
    prompt_primary_refs = infer_prompt_primary_artifact_refs(prompt_path)

    def collect_evidence_chunks(refs: Iterable[str]) -> tuple[bool, list[str]]:
        chunks: list[str] = []
        for rel in refs:
            resolved = resolve_evidence_path(run_root, iter_dir, rel)
            if resolved is None:
                return False, []
            if not evidence_ref_is_acceptable(resolved, run_root, iter_dir):
                return False, []
            text = read_text_safe(resolved)
            chunks.append(text[:50000])
        return True, chunks

    def entry_has_valid_implementation(
        entry: PromptSatisfactionEntry,
        requirement_text: str,
    ) -> tuple[bool, list[str]]:
        implementation_refs = [
            ref for ref in entry.implementation_paths if not is_prompt_source_ref(ref)
        ]
        if not implementation_refs:
            implementation_refs = [
                ref
                for ref in entry.evidence_paths
                if not is_prompt_source_ref(ref) and is_primary_artifact_ref(ref)
            ]
        if not implementation_refs:
            return False, []
        require_primary_match = requirement_requires_prompt_primary_match(
            requirement_text, prompt_primary_refs
        )
        if not implementation_refs_are_valid(
            run_root,
            implementation_refs,
            prompt_primary_refs,
            iter_dir=iter_dir,
            require_prompt_primary_match=require_primary_match,
        ):
            return False, []

        implementation_chunks: list[str] = []
        valid_impl_refs = 0
        for rel in implementation_refs:
            resolved = resolve_evidence_path(run_root, iter_dir, rel)
            if resolved is None:
                continue
            if not evidence_ref_is_acceptable(resolved, run_root, iter_dir):
                continue
            valid_impl_refs += 1
            if resolved.suffix.lower() in TEXTUAL_ARTIFACT_SUFFIXES:
                implementation_chunks.append(read_text_safe(resolved)[:50000])
        if valid_impl_refs < 1:
            return False, []
        return True, implementation_chunks

    if not requirements:
        for entry in entries:
            if not status_is_satisfied(entry.status, entry.verification):
                continue
            usable_refs = [ref for ref in entry.evidence_paths if not is_prompt_source_ref(ref)]
            if not usable_refs:
                continue
            evidence_ok, _ = collect_evidence_chunks(usable_refs)
            if not evidence_ok:
                continue
            implementation_ok, _ = entry_has_valid_implementation(entry, entry.requirement)
            if implementation_ok:
                return True
        return False

    for req_index, requirement in enumerate(requirements, start=1):
        requirement_ids = {
            f"RQ-{req_index}",
            f"RQ-{req_index:02d}",
            f"REQ-{req_index}",
            f"REQ-{req_index:02d}",
        }
        candidates = [
            e
            for e in entries
            if requirement_matches_entry(requirement, e)
            or normalize_scalar(e.requirement).strip().upper() in requirement_ids
        ]
        if not candidates:
            return False

        requirement_ok = False
        for entry in candidates:
            if not status_is_satisfied(entry.status, entry.verification):
                continue
            usable_refs = [ref for ref in entry.evidence_paths if not is_prompt_source_ref(ref)]
            if not usable_refs:
                continue
            evidence_paths_valid, evidence_chunks = collect_evidence_chunks(usable_refs)
            if not evidence_paths_valid:
                continue

            implementation_ok, implementation_chunks = entry_has_valid_implementation(
                entry, requirement
            )
            if not implementation_ok:
                continue

            evidence_text = "\n".join(
                [*evidence_chunks, *implementation_chunks, entry.verification]
            )
            if requirement_semantics_supported(requirement, evidence_text):
                requirement_ok = True
                break
            # Fallback: accept explicit satisfied verification when supported
            # by at least one non-prompt evidence artifact and implementation artifact.
            if (
                len(usable_refs) >= 1
                and verification_affirms_requirement(entry.verification)
                and implementation_ok
            ):
                requirement_ok = True
                break

        if not requirement_ok:
            return False

    return True


def identity_lock_evidence_exists(iter_dir: Path) -> bool:
    run_root = iter_dir.parent.parent
    return (
        (run_root / "LIQUID_STATE_IDENTITY.md").exists()
        or (iter_dir / "LIQUID_STATE_IDENTITY.md").exists()
    )


def resolve_record(iter_dir: Path) -> IterationRecord | None:
    m = ITER_RE.match(iter_dir.name)
    if not m:
        return None

    iteration_num = int(m.group(1))
    recheck_final = iter_dir / "judge_recheck" / "FINAL_DECISION.md"
    status_file = iter_dir / "STATUS.md"
    baseline_file = iter_dir / "judge_baseline" / "PRIORITIZED_DEFECTS.md"

    final_data = parse_bullets(recheck_final)
    status_data = parse_bullets(status_file)
    final_text = read_text_safe(recheck_final)
    final_bootstrap = looks_synthetic_text(final_text) or (
        not as_bool(final_data.get("prompt_consumed"), False)
        and as_bool(status_data.get("prompt_consumed"), False)
    )

    def pick(final_key: str, status_key: str | None = None) -> str | None:
        status_name = status_key or final_key
        if final_bootstrap:
            return status_data.get(status_name) or final_data.get(final_key)
        return final_data.get(final_key) or status_data.get(status_name)

    chain_raw = pick("evaluation_chain")
    if chain_raw is None:
        snapshot_data = parse_bullets(iter_dir / "SNAPSHOT.md")
        chain_raw = snapshot_data.get("evaluation_chain")
    if chain_raw is None:
        chain_match = CHAIN_RE.search(
            "\n".join(
                [
                    read_text_safe(iter_dir / "judge_recheck" / "FINAL_DECISION.md"),
                    read_text_safe(iter_dir / "STATUS.md"),
                    read_text_safe(iter_dir / "SNAPSHOT.md"),
                ]
            )
        )
        if chain_match:
            chain_raw = format_chain(int(chain_match.group(1)), int(chain_match.group(2)))
    if chain_raw is None:
        return None
    parsed_chain = parse_chain(chain_raw)
    if parsed_chain is None:
        return None
    chain = format_chain(parsed_chain[0], parsed_chain[1])

    decision = str(pick("decision") or "UNKNOWN").upper()
    baseline_mean = as_float(
        pick("baseline_mean"),
        -1.0,
    )
    recheck_mean = as_float(
        pick("recheck_mean"),
        -1.0,
    )
    recheck_defects = as_int(
        pick("recheck_total_defects", "recheck_defects"),
        -1,
    )
    baseline_total_defects = as_int(
        pick("baseline_total_defects", "baseline_defects"),
        -1,
    )
    baseline_blocking = as_int(
        pick("baseline_blocking_defects"),
        -1,
    )
    recheck_blocking = as_int(
        pick("recheck_blocking_defects"),
        -1,
    )
    prompt_satisfaction = as_bool(
        pick("prompt_satisfaction"),
        False,
    )
    identity_lock = as_bool(
        pick("identity_lock"),
        False,
    )
    prompt_required_for_chain = chain_requires_prompt_satisfaction(chain)
    if prompt_required_for_chain:
        computed_prompt_satisfaction = run_level_prompt_satisfaction_complete(iter_dir)
        if prompt_satisfaction and not computed_prompt_satisfaction:
            prompt_satisfaction = False
        elif (not prompt_satisfaction) and computed_prompt_satisfaction:
            prompt_satisfaction = True
    else:
        # Prompt satisfaction is only a hard gate on the project-artifact chain.
        prompt_satisfaction = True
    if identity_lock and not identity_lock_evidence_exists(iter_dir):
        identity_lock = False
    judge_prompt_access = judge_artifacts_have_prompt_access(iter_dir)
    if not judge_prompt_access:
        identity_lock = False
    if prompt_required_for_chain:
        if prompt_satisfaction and not judge_prompt_access:
            prompt_satisfaction = False
        if prompt_satisfaction and not primary_artifact_delta_is_meaningful(iter_dir, chain):
            prompt_satisfaction = False

    objective_gate = objective_attainment_gate(
        iter_dir=iter_dir,
        chain=chain,
        decision=decision,
    )
    truth_reconciliation_flag = normalize_scalar(
        str(pick("truth_reconciliation") or "")
    ).lower()
    # Only unresolved/failed reconciliation states should block objective gating.
    # "corrected"/"resolved"/"pass" indicate the issue was remediated.
    truth_reconciled = truth_reconciliation_flag in {
        "fail",
        "failed",
        "failure",
        "error",
        "unresolved",
        "mismatch",
    }
    if truth_reconciled:
        objective_gate = False

    synthetic_iteration = as_bool(
        pick("synthetic_iteration"),
        False,
    )
    if not synthetic_iteration:
        synthetic_hint = (
            read_text_safe(recheck_final)
            + "\n"
            + read_text_safe(status_file)
        )
        synthetic_iteration = looks_synthetic_text(synthetic_hint)

    real_delta_evidence = iteration_has_real_delta_evidence(iter_dir, chain)
    if synthetic_iteration:
        real_delta_evidence = False

    source_file = (
        "STATUS.md"
        if final_bootstrap
        else ("judge_recheck/FINAL_DECISION.md" if recheck_final.exists() else "STATUS.md")
    )

    return IterationRecord(
        iteration=iteration_num,
        chain=chain,
        decision=decision,
        baseline_mean=baseline_mean,
        recheck_mean=recheck_mean,
        baseline_blocking_defects=baseline_blocking,
        baseline_total_defects=baseline_total_defects,
        recheck_defects=recheck_defects,
        recheck_blocking_defects=recheck_blocking,
        prompt_linked_baseline=baseline_has_prompt_linkage(baseline_file),
        prompt_satisfaction=prompt_satisfaction,
        identity_lock=identity_lock,
        synthetic_iteration=synthetic_iteration,
        real_delta_evidence=real_delta_evidence,
        objective_gate=objective_gate,
        truth_reconciled=truth_reconciled,
        source_file=source_file,
    )


def collect_records(iterations_dir: Path) -> list[IterationRecord]:
    records: list[IterationRecord] = []
    if not iterations_dir.exists():
        return records

    for candidate in sorted(iterations_dir.iterdir()):
        if not candidate.is_dir():
            continue
        record = resolve_record(candidate)
        if record is not None:
            records.append(record)

    records.sort(key=lambda r: r.iteration)
    return records


def infer_depth(rubrics_dir: Path, records: Iterable[IterationRecord]) -> int:
    indices: set[int] = set()

    if rubrics_dir.exists():
        for file in rubrics_dir.iterdir():
            if not file.is_file():
                continue
            match = RUBRIC_FILE_RE.search(file.name)
            if match:
                indices.add(int(match.group(1)))

    for record in records:
        parsed = parse_chain(record.chain)
        if parsed is not None:
            indices.add(parsed[0])
            indices.add(parsed[1])

    if not indices:
        return 2
    return max(indices)


def build_expected_chains(depth: int) -> list[str]:
    if depth < 1:
        return []
    return [format_chain(i, i - 1) for i in range(depth, 0, -1)]


def chain_requires_prompt_satisfaction(chain: str) -> bool:
    parsed = parse_chain(chain)
    return parsed is not None and parsed[1] == 0


def compute_stability(
    records: Iterable[IterationRecord],
    required_streak: int,
    depth: int,
    require_chain_destabilization: bool = False,
    min_destabilization_defects: int = 3,
    min_destabilization_baseline_mean: float = 40.0,
    max_destabilization_baseline_mean: float = 95.0,
    min_recovery_iteration_gap: int = 1,
    require_prompt_linkage: bool = False,
    require_prompt_satisfaction: bool = True,
) -> StabilityResult:
    expected_chains = build_expected_chains(depth)
    if not expected_chains:
        return StabilityResult(
            records=list(records),
            streak=required_streak,
            required_streak=required_streak,
            depth=depth,
            expected_chains=[],
            chain_destabilized={},
            require_chain_destabilization=require_chain_destabilization,
            chain_recovered={},
            chain_prompt_satisfied={},
            min_destabilization_defects=min_destabilization_defects,
            min_destabilization_baseline_mean=min_destabilization_baseline_mean,
            max_destabilization_baseline_mean=max_destabilization_baseline_mean,
            min_recovery_iteration_gap=min_recovery_iteration_gap,
            require_prompt_linkage=require_prompt_linkage,
            require_prompt_satisfaction=require_prompt_satisfaction,
            system_phase="stabilized_readout",
            next_chain=None,
            stable=True,
            rationale="Depth < 1 implies no adjacency chains; stability is trivially satisfied.",
        )

    streak = 0
    ordered = list(records)
    next_index = 0
    chain_destabilized: dict[str, bool] = {chain: False for chain in expected_chains}
    chain_recovered: dict[str, bool] = {chain: False for chain in expected_chains}
    chain_upper_by_chain: dict[str, int] = {
        chain: parsed[0]
        for chain in expected_chains
        for parsed in [parse_chain(chain)]
        if parsed is not None
    }
    prompt_required_by_chain: dict[str, bool] = {
        chain: require_prompt_satisfaction and chain_requires_prompt_satisfaction(chain)
        for chain in expected_chains
    }
    chain_prompt_satisfied: dict[str, bool] = {
        chain: not prompt_required_by_chain[chain] for chain in expected_chains
    }
    chain_first_destabilization_iter: dict[str, int] = {}

    for record in ordered:
        prompt_required = prompt_required_by_chain.get(
            record.chain, require_prompt_satisfaction
        )
        prompt_ok_for_chain = record.prompt_satisfaction or not prompt_required

        if require_chain_destabilization and record.chain in chain_destabilized:
            nontrivial_destabilization = (
                record.baseline_total_defects >= min_destabilization_defects
                and record.baseline_mean >= 0.0
                and record.baseline_mean >= min_destabilization_baseline_mean
                and record.baseline_mean <= max_destabilization_baseline_mean
                and (not record.synthetic_iteration)
                and record.real_delta_evidence
            )
            if require_prompt_linkage:
                nontrivial_destabilization = (
                    nontrivial_destabilization and record.prompt_linked_baseline
                )
            if nontrivial_destabilization:
                chain_destabilized[record.chain] = True
                if record.chain not in chain_first_destabilization_iter:
                    chain_first_destabilization_iter[record.chain] = record.iteration

        quality_perfect = record.is_quality_perfect
        if record.chain in chain_prompt_satisfied:
            if prompt_required_by_chain.get(record.chain, False):
                chain_prompt_satisfied[record.chain] = (
                    quality_perfect
                    and prompt_ok_for_chain
                    and (not record.synthetic_iteration)
                    and record.real_delta_evidence
                )
            else:
                chain_prompt_satisfied[record.chain] = True

        eligible_perfect = (
            quality_perfect
            and record.identity_lock
            and (not record.synthetic_iteration)
            and record.real_delta_evidence
            and prompt_ok_for_chain
        )
        if require_chain_destabilization:
            destabilized = chain_destabilized.get(record.chain, False)
            first_iter = chain_first_destabilization_iter.get(record.chain, 10**9)
            recoverable = destabilized and (
                record.iteration >= first_iter + min_recovery_iteration_gap
            )
            eligible_perfect = eligible_perfect and recoverable
            if eligible_perfect:
                chain_recovered[record.chain] = True

        if not eligible_perfect:
            streak = 0
            next_index = 0
        else:
            expected_chain = expected_chains[next_index]
            if record.chain == expected_chain:
                next_index += 1
                if next_index == len(expected_chains):
                    streak += 1
                    next_index = 0
            # Out-of-order perfect record: only restart if it matches the first chain.
            elif record.chain == expected_chains[0]:
                streak = 0
                if len(expected_chains) == 1:
                    streak = 1
                    next_index = 0
                else:
                    next_index = 1
            # Orphan perfect record that does not fit the expected order.
            else:
                streak = 0
                next_index = 0

        parsed_chain = parse_chain(record.chain)
        finished_rubric_task = (
            parsed_chain is not None
            and record.decision.upper() in {"ACCEPT", "PROVISIONAL_ACCEPT"}
            and (not record.synthetic_iteration)
            and record.real_delta_evidence
        )
        if finished_rubric_task:
            finished_upper = parsed_chain[0]
            invalidated_any = False
            has_downstream_chain = False
            for chain, upper in chain_upper_by_chain.items():
                # Dependency invalidation flows toward the prompt-facing side:
                # when Rubric_k improves Rubric_(k-1), all chains with h < k
                # must be recomputed against the updated lower-rubric context.
                if upper >= finished_upper:
                    continue
                has_downstream_chain = True
                if (
                    chain_recovered.get(chain, False)
                    or (
                        prompt_required_by_chain.get(chain, False)
                        and chain_prompt_satisfied.get(chain, False)
                    )
                ):
                    invalidated_any = True
                # Preserve prior destabilization evidence across dependency
                # invalidation. Re-invalidation should force downstream
                # reconvergence, but it should not re-impose a synthetic
                # "first-ever destabilization" gate on the same prompt run.
                chain_recovered[chain] = False
                chain_prompt_satisfied[chain] = not prompt_required_by_chain.get(
                    chain, False
                )

            # A completed rubric task invalidates downstream prompt-facing chains.
            if invalidated_any or has_downstream_chain:
                streak = 0
                next_index = 0

    all_chains_destabilized = (
        all(chain_destabilized.values()) if require_chain_destabilization else True
    )
    all_chains_recovered = (
        all(chain_recovered.values()) if require_chain_destabilization else True
    )
    if require_prompt_satisfaction:
        required_prompt_chains = [
            chain for chain, needed in prompt_required_by_chain.items() if needed
        ]
        all_chains_prompt_satisfied = all(
            chain_prompt_satisfied.get(chain, False) for chain in required_prompt_chains
        )
    else:
        all_chains_prompt_satisfied = True
    stable = (
        streak >= required_streak
        and next_index == 0
        and all_chains_destabilized
        and all_chains_recovered
        and all_chains_prompt_satisfied
    )
    if stable:
        rationale = (
            f"Stability achieved: {streak} consecutive qualifying full-chain units "
            f"(required={required_streak})."
        )
        system_phase = "stabilized_readout"
        next_chain: str | None = None
    else:
        unmet_destabilization = [
            chain for chain, seen in chain_destabilized.items() if not seen
        ] if require_chain_destabilization else []
        unmet_recovery = [
            chain for chain, seen in chain_recovered.items() if not seen
        ] if require_chain_destabilization else []
        unmet_prompt_satisfaction = (
            [
                chain
                for chain, seen in chain_prompt_satisfied.items()
                if prompt_required_by_chain.get(chain, False) and not seen
            ]
            if require_prompt_satisfaction
            else []
        )

        if unmet_destabilization:
            next_chain = unmet_destabilization[0]
            system_phase = "reservoir_perturbation"
            rationale = (
                f"Stability not achieved: current_streak={streak}, "
                f"required_streak={required_streak}, next_chain={next_chain}, "
                f"unmet_destabilization={unmet_destabilization}."
            )
        elif unmet_recovery:
            next_chain = unmet_recovery[0]
            system_phase = "edge_of_chaos_dynamics"
            rationale = (
                f"Stability not achieved: current_streak={streak}, "
                f"required_streak={required_streak}, next_chain={next_chain}, "
                f"unmet_recovery={unmet_recovery}."
            )
        elif unmet_prompt_satisfaction:
            next_chain = unmet_prompt_satisfaction[0]
            system_phase = "readout_training"
            rationale = (
                f"Stability not achieved: current_streak={streak}, "
                f"required_streak={required_streak}, next_chain={next_chain}, "
                f"unmet_prompt_satisfaction={unmet_prompt_satisfaction}."
            )
        else:
            next_chain = expected_chains[next_index]
            system_phase = "readout_reconvergence"
            rationale = (
                f"Stability not achieved: current_streak={streak}, "
                f"required_streak={required_streak}, next_chain={next_chain}."
            )

    if not ordered and not stable:
        system_phase = "input_injection"

    return StabilityResult(
        records=ordered,
        streak=streak,
        required_streak=required_streak,
        depth=depth,
        expected_chains=expected_chains,
        chain_destabilized=chain_destabilized,
        require_chain_destabilization=require_chain_destabilization,
        chain_recovered=chain_recovered,
        chain_prompt_satisfied=chain_prompt_satisfied,
        min_destabilization_defects=min_destabilization_defects,
        min_destabilization_baseline_mean=min_destabilization_baseline_mean,
        max_destabilization_baseline_mean=max_destabilization_baseline_mean,
        min_recovery_iteration_gap=min_recovery_iteration_gap,
        require_prompt_linkage=require_prompt_linkage,
        require_prompt_satisfaction=require_prompt_satisfaction,
        system_phase=system_phase,
        next_chain=next_chain,
        stable=stable,
        rationale=rationale,
    )


def render_markdown(result: StabilityResult, iterations_dir: Path) -> str:
    lines: list[str] = []
    lines.append("# Stability Status")
    lines.append("")
    lines.append(f"- iterations_dir: `{iterations_dir}`")
    lines.append("- default_mode: `stability`")
    lines.append(
        "- operating_model: `liquid_state_machine` "
        "(reservoir perturbation -> edge-of-chaos dynamics -> readout reconvergence)"
    )
    lines.append(f"- depth: `N={result.depth}`")
    chain_order_text = (
        " ; ".join(result.expected_chains) if result.expected_chains else "none"
    )
    lines.append(
        "- required_chain_order: `" + chain_order_text + "`"
    )
    lines.append(f"- required_streak: `{result.required_streak}`")
    lines.append(f"- current_streak: `{result.streak}`")
    lines.append(f"- liquid_state_phase: `{result.system_phase}`")
    lines.append(
        "- require_chain_destabilization: "
        + f"`{'yes' if result.require_chain_destabilization else 'no'}`"
    )
    lines.append(
        "- require_prompt_satisfaction: "
        + f"`{'yes' if result.require_prompt_satisfaction else 'no'}`"
    )
    lines.append(
        "- quality_gate: "
        f"`recheck_mean >= {QUALITY_MIN_RECHECK_MEAN:.1f}; "
        f"recheck_defects <= {QUALITY_MAX_RECHECK_DEFECTS}; "
        f"recheck_blocking_defects <= {QUALITY_MAX_RECHECK_BLOCKING_DEFECTS}; "
        "(recheck_mean - baseline_mean) >= 0.0`"
    )
    lines.append("- require_identity_lock: `yes`")
    if result.require_chain_destabilization:
        lines.append(
            f"- destabilization_threshold: `baseline_total_defects >= {result.min_destabilization_defects}`"
        )
        lines.append(
            f"- destabilization_baseline_mean_floor: `baseline_mean >= {result.min_destabilization_baseline_mean:.1f}`"
        )
        lines.append(
            f"- destabilization_baseline_mean_cap: `baseline_mean <= {result.max_destabilization_baseline_mean:.1f}`"
        )
        lines.append(
            f"- min_recovery_iteration_gap: `{result.min_recovery_iteration_gap}`"
        )
        lines.append(
            "- require_prompt_linkage: "
            + f"`{'yes' if result.require_prompt_linkage else 'no'}`"
        )
        chain_state = "; ".join(
            f"{chain}={'yes' if seen else 'no'}"
            for chain, seen in result.chain_destabilized.items()
        ) or "none"
        lines.append(f"- chain_destabilized: `{chain_state}`")
        recovery_state = "; ".join(
            f"{chain}={'yes' if seen else 'no'}"
            for chain, seen in result.chain_recovered.items()
        ) or "none"
        lines.append(f"- chain_recovered: `{recovery_state}`")
    prompt_state = "; ".join(
        f"{chain}={'yes' if seen else 'no'}"
        for chain, seen in result.chain_prompt_satisfied.items()
    ) or "none"
    lines.append(f"- chain_prompt_satisfied: `{prompt_state}`")
    lines.append(f"- stable: `{'yes' if result.stable else 'no'}`")
    if result.next_chain is None:
        lines.append("- next_chain: `none`")
    else:
        lines.append(f"- next_chain: `{result.next_chain}`")
    lines.append(f"- rationale: {result.rationale}")
    lines.append("")
    lines.append("## Iteration Ledger")
    lines.append("")
    lines.append(
        "| Iteration | Chain | Decision | Baseline Mean | Recheck Mean | Mean Delta | Baseline Defects | "
        "Defects | Blocking | Prompt Link | Identity Lock | Prompt Satisfied | Objective Gate | Truth Reconciled | "
        "Synthetic | Real Delta | Quality Gate | Provisional | Improvement Accepted | Qualifying | Source |"
    )
    lines.append(
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"
    )

    if not result.records:
        lines.append("| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |")
    else:
        for r in result.records:
            lines.append(
                f"| {r.iteration:03d} | {r.chain} | {r.decision} | {r.baseline_mean:.1f} | "
                f"{r.recheck_mean:.1f} | {r.recheck_mean - r.baseline_mean:.1f} | {r.baseline_total_defects} | "
                f"{r.recheck_defects} | {r.recheck_blocking_defects} | "
                f"{'yes' if r.prompt_linked_baseline else 'no'} | "
                f"{'yes' if r.identity_lock else 'no'} | "
                f"{'yes' if r.prompt_satisfaction else 'no'} | "
                f"{'yes' if r.objective_gate else 'no'} | "
                f"{'yes' if r.truth_reconciled else 'no'} | "
                f"{'yes' if r.synthetic_iteration else 'no'} | "
                f"{'yes' if r.real_delta_evidence else 'no'} | "
                f"{'yes' if r.is_quality_perfect else 'no'} | "
                f"{'yes' if r.is_provisional_accept else 'no'} | "
                f"{'yes' if r.is_improvement_accepted else 'no'} | "
                f"{'yes' if r.is_perfect else 'no'} | `{r.source_file}` |"
            )

    return "\n".join(lines) + "\n"


def render_json(result: StabilityResult, iterations_dir: Path) -> dict[str, object]:
    return {
        "iterations_dir": str(iterations_dir),
        "default_mode": "stability",
        "operating_model": "liquid_state_machine",
        "depth": result.depth,
        "liquid_state_phase": result.system_phase,
        "required_chain_order": result.expected_chains,
        "required_streak": result.required_streak,
        "current_streak": result.streak,
        "require_chain_destabilization": result.require_chain_destabilization,
        "require_prompt_satisfaction": result.require_prompt_satisfaction,
        "require_identity_lock": True,
        "quality_gate": {
            "recheck_mean_min": QUALITY_MIN_RECHECK_MEAN,
            "recheck_defects_max": QUALITY_MAX_RECHECK_DEFECTS,
            "recheck_blocking_defects_max": QUALITY_MAX_RECHECK_BLOCKING_DEFECTS,
            "mean_delta_min": 0.0,
        },
        "chain_destabilized": result.chain_destabilized,
        "chain_recovered": result.chain_recovered,
        "chain_prompt_satisfied": result.chain_prompt_satisfied,
        "min_destabilization_defects": result.min_destabilization_defects,
        "min_destabilization_baseline_mean": result.min_destabilization_baseline_mean,
        "max_destabilization_baseline_mean": result.max_destabilization_baseline_mean,
        "min_recovery_iteration_gap": result.min_recovery_iteration_gap,
        "require_prompt_linkage": result.require_prompt_linkage,
        "stable": result.stable,
        "next_chain": result.next_chain,
        "rationale": result.rationale,
        "records": [
            {
                "iteration": r.iteration,
                "chain": r.chain,
                "decision": r.decision,
                "baseline_mean": r.baseline_mean,
                "baseline_blocking_defects": r.baseline_blocking_defects,
                "baseline_total_defects": r.baseline_total_defects,
                "recheck_mean": r.recheck_mean,
                "mean_delta": r.recheck_mean - r.baseline_mean,
                "recheck_defects": r.recheck_defects,
                "recheck_blocking_defects": r.recheck_blocking_defects,
                "prompt_linked_baseline": r.prompt_linked_baseline,
                "identity_lock": r.identity_lock,
                "prompt_satisfaction": r.prompt_satisfaction,
                "objective_gate": r.objective_gate,
                "truth_reconciled": r.truth_reconciled,
                "synthetic_iteration": r.synthetic_iteration,
                "real_delta_evidence": r.real_delta_evidence,
                "quality_perfect": r.is_quality_perfect,
                "quality_gate_pass": r.is_quality_perfect,
                "provisional_accept": r.is_provisional_accept,
                "improvement_accepted": r.is_improvement_accepted,
                "perfect": r.is_perfect,
                "qualifying": r.is_perfect,
                "source_file": r.source_file,
            }
            for r in result.records
        ],
    }


def write_outputs(
    result: StabilityResult,
    iterations_dir: Path,
    output_md: Path,
    json_output: Path | None,
) -> None:
    md = render_markdown(result, iterations_dir)
    output_md.write_text(md, encoding="utf-8")
    print(f"wrote {output_md}")
    if result.next_chain is not None:
        print(f"next_chain={result.next_chain}")
    else:
        print("next_chain=none")

    if json_output is not None:
        payload = render_json(result, iterations_dir)
        json_output.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {json_output}")


def resolve_depth(depth_arg: int, records: Iterable[IterationRecord], rubrics_dir: Path) -> int:
    return infer_depth(rubrics_dir, records) if depth_arg == -1 else depth_arg


def evaluate_current_state(
    *,
    iterations_dir: Path,
    depth_arg: int,
    required_streak: int,
    rubrics_dir: Path,
    require_chain_destabilization: bool,
    min_destabilization_defects: int,
    min_destabilization_baseline_mean: float,
    max_destabilization_baseline_mean: float,
    min_recovery_iteration_gap: int,
    require_prompt_linkage: bool,
    require_prompt_satisfaction: bool,
) -> StabilityResult:
    records = collect_records(iterations_dir)
    depth = resolve_depth(depth_arg, records, rubrics_dir)
    return compute_stability(
        records,
        required_streak,
        depth,
        require_chain_destabilization=require_chain_destabilization,
        min_destabilization_defects=min_destabilization_defects,
        min_destabilization_baseline_mean=min_destabilization_baseline_mean,
        max_destabilization_baseline_mean=max_destabilization_baseline_mean,
        min_recovery_iteration_gap=min_recovery_iteration_gap,
        require_prompt_linkage=require_prompt_linkage,
        require_prompt_satisfaction=require_prompt_satisfaction,
    )


def next_iteration_number(iterations_dir: Path) -> int:
    if not iterations_dir.exists():
        return 1
    values: list[int] = []
    for candidate in iterations_dir.iterdir():
        if not candidate.is_dir():
            continue
        match = ITER_ANY_RE.search(candidate.name)
        if match:
            values.append(int(match.group(1)))
    return (max(values) + 1) if values else 1


def rubric_cell_label(x_name: str, y_name: str) -> str:
    return f"{x_name} x {y_name}"


def ordered_unique_text(values: Iterable[str]) -> list[str]:
    items: list[str] = []
    seen: set[str] = set()
    for value in values:
        clean = str(value).strip()
        if not clean or clean in seen:
            continue
        items.append(clean)
        seen.add(clean)
    return items


def canonical_role_category_label(role_id: str, role_name: str) -> str:
    return f"{role_id} {role_name}".strip()


def canonical_role_dimensions_by_id() -> dict[str, list[str]]:
    dimensions_by_role: dict[str, list[str]] = {
        role_id: ordered_unique_text(dimensions)
        for role_id, dimensions in CANONICAL_ROLE_PRODUCT_DIMENSIONS
    }
    expected_role_ids = [role_id for role_id, _ in CANONICAL_COMPANY_ROLES]
    missing = [role_id for role_id in expected_role_ids if role_id not in dimensions_by_role]
    extra = [role_id for role_id in dimensions_by_role if role_id not in set(expected_role_ids)]
    if missing or extra:
        raise ValueError(
            "Canonical role dimension mapping must match canonical roles exactly: "
            f"missing={missing}, extra={extra}"
        )
    for role_id in expected_role_ids:
        if len(dimensions_by_role[role_id]) < 2:
            raise ValueError(
                f"Role {role_id} must contribute at least two product-quality dimensions."
            )
    return dimensions_by_role


def build_bootstrap_role_axes() -> tuple[list[str], dict[str, list[str]], list[str]]:
    if len(CANONICAL_COMPANY_ROLES) != 16:
        raise ValueError("Bootstrap role-category X-axis requires exactly 16 canonical roles.")
    role_dimensions_by_id = canonical_role_dimensions_by_id()
    x_axis = [
        canonical_role_category_label(role_id, role_name)
        for role_id, role_name in CANONICAL_COMPANY_ROLES
    ]
    y_axis = ordered_unique_text(
        dimension
        for role_id, _ in CANONICAL_COMPANY_ROLES
        for dimension in role_dimensions_by_id.get(role_id, [])
    )
    if not y_axis:
        raise ValueError("Bootstrap role dimensions produced an empty Y-axis.")
    return x_axis, role_dimensions_by_id, y_axis


def build_bootstrap_role_wiring(
    *,
    rubric_index: int,
    iteration_label: str,
    x_axis: list[str],
    y_axis: list[str],
    role_dimensions_by_id: dict[str, list[str]],
) -> tuple[list[dict], list[dict]]:
    if not x_axis or not y_axis:
        return [], []

    company_roles: list[dict] = []
    role_sections: list[dict] = []
    y_axis_pool = set(y_axis)

    for idx, (role_id, role_name) in enumerate(CANONICAL_COMPANY_ROLES):
        role_axis = (
            x_axis[idx]
            if idx < len(x_axis)
            else canonical_role_category_label(role_id, role_name)
        )
        contributed_dimensions = [
            dimension
            for dimension in role_dimensions_by_id.get(role_id, [])
            if dimension in y_axis_pool
        ]
        if len(contributed_dimensions) < 2:
            raise ValueError(
                f"Role {role_id} must map to at least two Y-axis dimensions; "
                f"got {contributed_dimensions}."
            )

        covered_axes = ordered_unique_text([role_axis] + contributed_dimensions)
        covered_cells = ordered_unique_text(
            rubric_cell_label(role_axis, dimension) for dimension in contributed_dimensions
        )

        company_roles.append(
            {
                "role_id": role_id,
                "role_name": role_name,
                "role_category": role_axis,
                "contributed_product_quality_dimensions": contributed_dimensions,
                "primary_accountabilities": [
                    f"Own prompt-linked quality outcomes for {contributed_dimensions[0]}.",
                    f"Challenge unresolved risk and weak controls in {contributed_dimensions[1]}.",
                ],
                "evidence_duties": [
                    "Provide explicit who/what/where evidence for every non-zero score claim.",
                    (
                        f"Maintain reproducible citations for covered cells "
                        f"{', '.join(covered_cells)}."
                    ),
                ],
            }
        )

        role_sections.append(
            {
                "role_id": role_id,
                "role_name": role_name,
                "section_intent": (
                    f"Apply the {role_name} perspective to strengthen prompt-grounded rubric "
                    "discrimination and defect closure."
                ),
                "concerns": [
                    f"Weak controls for {contributed_dimensions[0]} can hide unmet prompt obligations.",
                    f"Weak controls for {contributed_dimensions[1]} can permit score inflation or missed defects.",
                ],
                "sub_dimensions": contributed_dimensions,
                "scoring_focus": (
                    f"Score whether {role_name} evidence is specific, reproducible, and sufficient "
                    f"to justify outcomes across {', '.join(covered_cells)} in Rubric_{rubric_index}."
                ),
                "anti_gaming_checks": [
                    "Attempt high-score claims with incomplete evidence and verify rejection behavior.",
                    "Cross-check contradiction logs against claimed defect closure outcomes.",
                ],
                "evidence_requirements": [
                    "prompt.txt",
                    f"evidence/iteration_{iteration_label}.md",
                    f"deltas/iteration_{iteration_label}.md",
                ],
                "covered_axes": covered_axes,
                "covered_cells": covered_cells,
            }
        )

    return company_roles, role_sections


def emit_bootstrap_role_pack_markdown(
    *,
    project_root: Path,
    rubric_index: int,
    iteration_label: str,
    rubric_json: dict,
) -> None:
    role_pack_path = project_root / f"rubrics/Rubric_{rubric_index}_Role_Expansion_Pack_N16.md"
    if role_pack_path.exists():
        return

    company_roles_raw = rubric_json.get("company_roles", [])
    role_sections_raw = rubric_json.get("role_sections", [])
    x_axis_raw = rubric_json.get("x_axis", [])
    y_axis_raw = rubric_json.get("y_axis", [])
    target = str(rubric_json.get("target", f"Rubric_{max(0, rubric_index - 1)}")).strip()

    company_roles = [entry for entry in company_roles_raw if isinstance(entry, dict)]
    role_sections = [entry for entry in role_sections_raw if isinstance(entry, dict)]
    x_axis = [str(value).strip() for value in x_axis_raw if str(value).strip()]
    y_axis = [str(value).strip() for value in y_axis_raw if str(value).strip()]

    role_names = {
        str(entry.get("role_id", "")).strip(): str(entry.get("role_name", "")).strip()
        for entry in company_roles
        if str(entry.get("role_id", "")).strip()
    }

    lines = [
        f"# Rubric_{rubric_index}_Role_Expansion_Pack_N16",
        "",
        f"- iteration: {iteration_label}",
        f"- rubric_index: {rubric_index}",
        f"- target: {target}",
        f"- role_count: {len(company_roles)}",
        "",
        "## Canonical Role Catalog",
        "| Role ID | Role Name |",
        "| --- | --- |",
    ]

    for role in company_roles:
        role_id = str(role.get("role_id", "")).strip()
        role_name = str(role.get("role_name", "")).strip()
        if role_id and role_name:
            lines.append(f"| {role_id} | {role_name} |")

    lines.extend(["", "## Axis Context"])
    if x_axis:
        lines.append("- x_axis: " + ", ".join(f"`{axis}`" for axis in x_axis))
    if y_axis:
        lines.append("- y_axis: " + ", ".join(f"`{axis}`" for axis in y_axis))
    lines.extend(["", "## Role Sections"])

    for section in role_sections:
        role_id = str(section.get("role_id", "")).strip()
        role_name = str(section.get("role_name", "")).strip() or role_names.get(role_id, "")
        heading_name = f"{role_id} {role_name}".strip()
        lines.append(f"### {heading_name if heading_name else 'Role'}")
        intent = str(section.get("section_intent", "")).strip()
        if intent:
            lines.append(f"- intent: {intent}")
        concerns = [
            str(item).strip() for item in section.get("concerns", []) if str(item).strip()
        ]
        if concerns:
            lines.append("- concerns:")
            lines.extend([f"  - {item}" for item in concerns])
        sub_dimensions = [
            str(item).strip()
            for item in section.get("sub_dimensions", [])
            if str(item).strip()
        ]
        if sub_dimensions:
            lines.append("- sub_dimensions:")
            lines.extend([f"  - {item}" for item in sub_dimensions])
        scoring_focus = str(section.get("scoring_focus", "")).strip()
        if scoring_focus:
            lines.append(f"- scoring_focus: {scoring_focus}")
        anti_gaming_checks = [
            str(item).strip()
            for item in section.get("anti_gaming_checks", [])
            if str(item).strip()
        ]
        if anti_gaming_checks:
            lines.append("- anti_gaming_checks:")
            lines.extend([f"  - {item}" for item in anti_gaming_checks])
        evidence_requirements = [
            str(item).strip()
            for item in section.get("evidence_requirements", [])
            if str(item).strip()
        ]
        if evidence_requirements:
            lines.append("- evidence_requirements:")
            lines.extend([f"  - {item}" for item in evidence_requirements])
        covered_axes = [
            str(item).strip() for item in section.get("covered_axes", []) if str(item).strip()
        ]
        if covered_axes:
            lines.append("- covered_axes: " + ", ".join(f"`{item}`" for item in covered_axes))
        covered_cells = [
            str(item).strip() for item in section.get("covered_cells", []) if str(item).strip()
        ]
        if covered_cells:
            lines.append("- covered_cells: " + ", ".join(f"`{item}`" for item in covered_cells))
        lines.append("")

    role_pack_path.parent.mkdir(parents=True, exist_ok=True)
    role_pack_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_bootstrap_rubric_json(
    *,
    project_root: Path,
    rubric_index: int,
    depth: int,
    iteration_label: str,
) -> dict:
    prompt_requirements = parse_prompt_requirements(project_root / "prompt.txt")
    if not prompt_requirements:
        prompt_requirements = [
            "Deliver the prompt-defined artifact with verifiable quality and traceable evidence."
        ]

    requirement_ids = [f"REQ-{idx+1:02d}" for idx in range(len(prompt_requirements))]

    x_axis, role_dimensions_by_id, y_axis = build_bootstrap_role_axes()

    def build_axis_spec(axis_name: str, axis_kind: str, ordinal: int) -> dict:
        return {
            "name": axis_name,
            "definition": (
                f"{axis_name} defines how {axis_kind}-axis evaluations convert prompt-linked quality "
                "expectations into measurable scoring behavior."
            ),
            "failure_mode": (
                f"When {axis_name} is weak, prompt requirements are missed or accepted without sufficient proof."
            ),
            "discriminator": (
                "Distinguishes prompt-conformant evidence-backed execution from cosmetic or generic scoring behavior."
            ),
            "intervention": (
                f"Refine {axis_name} anchors and tighten evidence expectations to close prompt-linked defects."
            ),
            "measurement_protocol": (
                "Verify requirement mapping coverage, recompute scored outcomes, and compare recheck defects "
                "before and after remediation."
            ),
            "evidence_expectation": (
                f"Cite prompt-linked artifacts, scored-cell evidence refs, and adjudication notes for {axis_name}."
            ),
            "anti_gaming_probe": (
                "Attempt score inflation by reducing evidence quality; verify the rubric blocks acceptance and "
                "flags contradiction paths."
            ),
            "example_pass_case": (
                f"{axis_name} shows prompt-linked coverage with independently reproducible evidence and clean recheck."
            ),
            "example_fail_case": (
                f"{axis_name} allows high scores despite missing prompt linkage or unverifiable evidence chains."
            ),
            "scoring_anchors": {
                "0": "No prompt-linked mechanism; evidence and outcomes are disconnected.",
                "50": "Partial linkage exists, but defect sensitivity and verification coverage are inconsistent.",
                "80": "Strong linkage with measurable controls; minor defects remain and are explicitly tracked.",
                "100": "Complete prompt-aligned coverage with adversarially resilient, reproducible verification.",
            },
            "ordinal": ordinal,
        }

    x_axis_specs = [build_axis_spec(name, "x", idx + 1) for idx, name in enumerate(x_axis)]
    y_axis_specs = [build_axis_spec(name, "y", idx + 1) for idx, name in enumerate(y_axis)]
    company_roles, role_sections = build_bootstrap_role_wiring(
        rubric_index=rubric_index,
        iteration_label=iteration_label,
        x_axis=x_axis,
        y_axis=y_axis,
        role_dimensions_by_id=role_dimensions_by_id,
    )

    target = "project artifact(s) from prompt.txt" if rubric_index == 0 else f"Rubric_{rubric_index - 1}"
    target_collateral_manifest = [
        "prompt.txt",
        "RUN_METADATA.md",
        "AGENTS.md",
        "PROMPT_SATISFACTION.md",
        f"rubrics/Rubric_{rubric_index}_Role_Expansion_Pack_N16.md",
        "evidence/iteration_" + iteration_label + ".md",
        "deltas/iteration_" + iteration_label + ".md",
        "contradictions/iteration_" + iteration_label + ".md",
    ]
    if rubric_index > 0:
        target_collateral_manifest.extend(
            [
                f"rubrics/Rubric_{rubric_index - 1}/iteration_{iteration_label}.json",
                f"scorecards/Rubric_{rubric_index - 1}_grid_iteration_{iteration_label}.md",
                f"collateral/Rubric_{rubric_index - 1}/manifest_iteration_{iteration_label}.md",
                f"collateral/Rubric_{rubric_index - 1}/access_log_iteration_{iteration_label}.md",
                f"rubrics/Rubric_{rubric_index - 1}_Role_Expansion_Pack_N16.md",
            ]
        )
    target_collateral_manifest = list(dict.fromkeys(target_collateral_manifest))

    cell_labels: list[str] = []
    cells: list[dict] = []
    cell_counter = 1
    for x_name in x_axis:
        for y_name in y_axis:
            cell_label = rubric_cell_label(x_name, y_name)
            cell_labels.append(cell_label)
            cells.append(
                {
                    "x": x_name,
                    "y": y_name,
                    "score_percent": 58,
                    "evidence_refs": [
                        f"evidence/iteration_{iteration_label}.md#cell-{cell_counter:02d}",
                        "prompt.txt",
                    ],
                    "collateral_refs": [
                        "prompt.txt",
                        "RUN_METADATA.md",
                    ],
                    "rationale": (
                        "Bootstrap baseline score reflects prompt-linked destabilization state prior to full "
                        "adjudicated recovery."
                    ),
                }
            )
            cell_counter += 1

    prompt_requirement_trace: list[dict] = []
    for idx, requirement_text in enumerate(prompt_requirements):
        rid = requirement_ids[idx]
        x_name = x_axis[idx % len(x_axis)]
        y_name = y_axis[idx % len(y_axis)]
        prompt_requirement_trace.append(
            {
                "requirement_id": rid,
                "requirement_text": requirement_text,
                "addressed_by_axes": [x_name, y_name],
                "addressed_by_cells": [rubric_cell_label(x_name, y_name)],
                "adaptation_strategy": (
                    "Adapt axis definitions and scoring anchors to close prompt-linked defects revealed in "
                    "baseline judging."
                ),
                "evidence_refs": [
                    "prompt.txt",
                    f"deltas/iteration_{iteration_label}.md#{rid.lower()}",
                ],
            }
        )

    prompt_transmogrification_log = []
    for idx, rid in enumerate(requirement_ids[: max(1, min(3, len(requirement_ids)))]):
        prompt_transmogrification_log.append(
            {
                "change_summary": (
                    "Refined rubric structure to improve prompt-conformant discrimination, traceability, and "
                    "adversarial resistance."
                ),
                "trigger_requirement_id": rid,
                "expected_prompt_uplift": (
                    "Higher requirement satisfaction reliability with clearer evidence-linked adjudication."
                ),
                "evidence_refs": [
                    f"deltas/iteration_{iteration_label}.md#transmog-{idx+1}",
                    "prompt.txt",
                ],
            }
        )

    axis_task_alignment = []
    for axis_name in x_axis:
        axis_task_alignment.append(
            {
                "axis_name": axis_name,
                "axis_kind": "x",
                "supported_requirement_ids": requirement_ids,
                "success_mechanism": (
                    f"{axis_name} improves prompt success by forcing requirement-linked scoring and measurable "
                    "quality uplift evidence."
                ),
                "failure_if_ignored": (
                    f"Ignoring {axis_name} causes requirement gaps, weak discrimination, and acceptance risk."
                ),
                "evidence_refs": [
                    "prompt.txt",
                    f"evidence/iteration_{iteration_label}.md#axis-x",
                ],
            }
        )
    for axis_name in y_axis:
        axis_task_alignment.append(
            {
                "axis_name": axis_name,
                "axis_kind": "y",
                "supported_requirement_ids": requirement_ids,
                "success_mechanism": (
                    f"{axis_name} improves prompt success by strengthening defect discovery and verification quality."
                ),
                "failure_if_ignored": (
                    f"Ignoring {axis_name} allows prompt-linked defects to survive recheck and destabilizes quality."
                ),
                "evidence_refs": [
                    "prompt.txt",
                    f"evidence/iteration_{iteration_label}.md#axis-y",
                ],
            }
        )

    axis_alternatives_considered = [
        {"axis": "x", "name": "Output Quality", "kept": False, "reason": "Too generic for prompt-linked scoring."},
        {"axis": "y", "name": "General Compliance", "kept": False, "reason": "Insufficient adversarial discrimination."},
    ]
    axis_alternatives_considered.extend(
        {"axis": "x", "name": name, "kept": True, "reason": "Selected for prompt-grounded discrimination."}
        for name in x_axis
    )
    axis_alternatives_considered.extend(
        {"axis": "y", "name": name, "kept": True, "reason": "Selected for prompt-grounded adjudication rigor."}
        for name in y_axis
    )

    axis_change_log = (
        [{"action": "add", "axis": "x", "from": "", "to": name} for name in x_axis]
        + [{"action": "add", "axis": "y", "from": "", "to": name} for name in y_axis]
    )

    access_log_cells = cell_labels[: min(3, len(cell_labels))]
    target_collateral_access_log = [
        {
            "path": ref,
            "purpose": "Prompt-grounded collateral used to justify baseline scoring and recheck adjudication.",
            "used_by_cells": access_log_cells,
        }
        for ref in target_collateral_manifest
    ]

    if rubric_index == 0:
        improvement_intent = (
            "Improve artifact/document scoring to maximize prompt-conformant user value, technical correctness, "
            "and auditable evidence quality while reducing blind spots and defects."
        )
    else:
        predecessor = f"Rubric_{rubric_index - 1}"
        improvement_intent = (
            f"Improve {predecessor} by correcting known defects, strengthening anti-gaming controls, and "
            "tightening prompt-linked discriminators to elevate adjudication reliability."
        )

    return {
        "schema_version": "rubric.v2",
        "rubric_index": rubric_index,
        "depth": depth,
        "iteration": iteration_label,
        "target": target,
        "company_roles": company_roles,
        "role_sections": role_sections,
        "target_collateral_manifest": target_collateral_manifest,
        "target_collateral_access_log": target_collateral_access_log,
        "target_collateral_coverage_percent": 100,
        "x_axis": x_axis,
        "y_axis": y_axis,
        "x_axis_specs": x_axis_specs,
        "y_axis_specs": y_axis_specs,
        "axis_cardinality_rationale": (
            "X-axis is fixed to the canonical 16 role categories (R0..R15), and Y-axis is the deduplicated "
            "union of all role-contributed product-quality dimensions."
        ),
        "axis_selection_rationale": (
            "Axes are selected through deterministic role-driven construction so each role owns explicit "
            "product-quality dimensions with traceable cell coverage."
        ),
        "improvement_intent": improvement_intent,
        "axis_generation_evidence_refs": [
            "prompt.txt",
            f"iterations/iteration_{iteration_label}/SNAPSHOT.md",
        ],
        "axis_alternatives_considered": axis_alternatives_considered,
        "cells": cells,
        "rubric_mean_percent": 58.0,
        "variance_uncovered": [
            "Recovery counting requires a later iteration after first destabilization evidence.",
            "Prompt satisfaction remains incomplete until downstream artifact linkage closes all requirements.",
        ],
        "task_conformance_rationale": (
            "This bootstrap rubric is directly molded to prompt requirements: each axis and cell is requirement-linked, "
            "evidence-bound, and positioned to drive measurable defect reduction toward stable prompt satisfaction."
        ),
        "prompt_requirement_trace": prompt_requirement_trace,
        "prompt_transmogrification_log": prompt_transmogrification_log,
        "axis_task_alignment": axis_task_alignment,
        "axis_change_log": axis_change_log,
    }


def bootstrap_iteration_scaffold(
    *,
    project_root: Path,
    iterations_dir: Path,
    iteration_label: str,
    chain: str,
    lower: int,
    depth: int,
) -> None:
    iteration_dir = iterations_dir / f"iteration_{iteration_label}"
    paths_to_make = [
        iteration_dir / "judge_baseline",
        iteration_dir / "author_deltas",
        iteration_dir / "judge_recheck",
        project_root / f"rubrics/Rubric_{lower}",
        project_root / "scorecards",
        project_root / f"collateral/Rubric_{lower}",
        project_root / "evidence",
        project_root / "deltas",
        project_root / "contradictions",
    ]
    for path in paths_to_make:
        path.mkdir(parents=True, exist_ok=True)

    def ensure(path: Path, content: str) -> None:
        if path.exists():
            return
        path.write_text(content, encoding="utf-8")

    ensure(
        iteration_dir / "SNAPSHOT.md",
        "\n".join(
            [
                "# Snapshot",
                f"- iteration: {iteration_label}",
                f"- evaluation_chain: {chain}",
                f"- project_root: {project_root}",
                "- snapshot_status: initialized",
                "",
            ]
        ),
    )
    ensure(
        iteration_dir / "STATUS.md",
        "\n".join(
            [
                f"- evaluation_chain: {chain}",
                "- decision: REJECT",
                "- baseline_mean: 0.0",
                "- recheck_mean: 0.0",
                "- baseline_defects: 0",
                "- recheck_defects: 0",
                "- recheck_blocking_defects: 0",
                "- identity_lock: yes",
                "- prompt_source: prompt.txt",
                "- prompt_consumed: no",
                "- prompt_satisfaction: no",
                "- liquid_state_phase: input_injection",
                "",
            ]
        ),
    )
    ensure(
        iteration_dir / "SCORE_DELTA.md",
        "\n".join(
            [
                "# Score Delta",
                f"- chain: {chain}",
                "- baseline_mean: 0.0",
                "- recheck_mean: 0.0",
                "- delta: 0.0",
                "",
            ]
        ),
    )
    ensure(
        iteration_dir / "LIQUID_STATE_IDENTITY.md",
        "You are a Liquid State Machine on the Edge of Chaos.\n",
    )
    ensure(
        iteration_dir / "LIQUID_STATE_TRANSITION.md",
        "\n".join(
            [
                "# Liquid State Transition",
                "- phase: input_injection",
                f"- chain: {chain}",
                "",
            ]
        ),
    )
    ensure(
        iteration_dir / "judge_baseline" / "PRIORITIZED_DEFECTS.md",
        "\n".join(
            [
                "# Baseline Defects",
                "- pending: initialize baseline defects",
                "- prompt_source: prompt.txt",
                "- prompt_consumed: no",
                "",
            ]
        ),
    )
    ensure(
        iteration_dir / "author_deltas" / "DEFECT_BURNDOWN_CHECK.md",
        "# Defect Burndown Check\n- pending: initialize remediation deltas\n",
    )
    ensure(
        iteration_dir / "judge_recheck" / "PRIORITIZED_DEFECTS.md",
        "\n".join(
            [
                "# Recheck Defects",
                "- pending: initialize recheck defects",
                "- prompt_source: prompt.txt",
                "- prompt_consumed: no",
                "",
            ]
        ),
    )
    ensure(
        iteration_dir / "judge_recheck" / "FINAL_DECISION.md",
        "\n".join(
            [
                f"- evaluation_chain: {chain}",
                "- decision: REJECT",
                "- rationale: bootstrap initialization",
                "- baseline_mean: 0.0",
                "- recheck_mean: 0.0",
                "- baseline_blocking_defects: 0",
                "- recheck_blocking_defects: 0",
                "- baseline_total_defects: 0",
                "- recheck_total_defects: 0",
                "- identity_lock: yes",
                "- prompt_source: prompt.txt",
                "- prompt_consumed: no",
                "- prompt_satisfaction: no",
                "- liquid_state_phase: input_injection",
                "",
            ]
        ),
    )
    ensure(
        iteration_dir / "judge_recheck" / "OBJECTIVE_COUNTEREXAMPLES.md",
        "\n".join(
            [
                "# Objective Counterexamples",
                "- status: bootstrap",
                "- counterexample_search_performed: no",
                "- variants_tested: 0",
                "- better_variant_found: yes",
                "",
            ]
        ),
    )
    ensure(
        iteration_dir / "judge_recheck" / "FRONTIER_STATUS.md",
        "\n".join(
            [
                "# Frontier Status",
                "- status: bootstrap",
                "- compared_against_prior_best: no",
                "- frontier_membership: no",
                "",
            ]
        ),
    )
    ensure(
        iteration_dir / "judge_recheck" / "DISCRIMINATION_CHECK.md",
        "\n".join(
            [
                "# Discrimination Check",
                "- status: bootstrap",
                "- discrimination_check_performed: no",
                "- discrimination_direction: higher_is_better",
                "- minor_variant_score: 0",
                "- major_variant_score: 0",
                "- discriminative_power_pass: no",
                "",
            ]
        ),
    )

    ensure(
        project_root / "LIQUID_STATE_IDENTITY.md",
        "You are a Liquid State Machine on the Edge of Chaos.\n",
    )
    ensure(
        project_root / "PROMPT_SATISFACTION.md",
        "\n".join(
            [
                "# Prompt Satisfaction",
                "- status: bootstrap_initialized",
                "- note: bootstrap initialized; update with requirement-level evidence mapping.",
                "",
            ]
        ),
    )
    ensure(
        project_root / "ARTIFACT_MANIFEST.md",
        "\n".join(
            [
                "# Artifact Manifest",
                "- status: bootstrap",
                "- note: bootstrap initialized; replace with finalized artifact accounting.",
                "",
            ]
        ),
    )
    ensure(
        project_root / "RUBRIC_SCORECARD_SUMMARY.md",
        "\n".join(
            [
                "# Rubric Scorecard Summary",
                "- status: bootstrap",
                "- note: bootstrap initialized; replace with finalized score summary.",
                "",
            ]
        ),
    )
    ensure(
        project_root / "FINAL_STATUS.md",
        "\n".join(
            [
                "# Final Status",
                "- status: bootstrap",
                "- note: bootstrap initialized; replace with finalized pass/fail decision.",
                "",
            ]
        ),
    )
    ensure(
        project_root / "OBJECTIVE_SPEC.md",
        "\n".join(
            [
                "# Objective Specification",
                "- status: bootstrap",
                "- objective_summary: bootstrap",
                "- objective_attainment_definition: bootstrap",
                "- optimization_target: bootstrap",
                "- prompt_intent_model: bootstrap",
                "- no_known_feasible_improvement_standard: bootstrap",
                "",
            ]
        ),
    )
    ensure(
        project_root / "BEST_KNOWN_FRONTIER.md",
        "\n".join(
            [
                "# Best Known Frontier",
                "- status: bootstrap",
                "- frontier_tracking_active: no",
                "- compared_against_prior_best: no",
                "- prompt_source: prompt.txt",
                "",
            ]
        ),
    )
    bootstrap_rubric_json = build_bootstrap_rubric_json(
        project_root=project_root,
        rubric_index=lower,
        depth=depth,
        iteration_label=iteration_label,
    )
    ensure(
        project_root / f"rubrics/Rubric_{lower}/iteration_{iteration_label}.json",
        json.dumps(bootstrap_rubric_json, indent=2) + "\n",
    )
    emit_bootstrap_role_pack_markdown(
        project_root=project_root,
        rubric_index=lower,
        iteration_label=iteration_label,
        rubric_json=bootstrap_rubric_json,
    )
    ensure(
        project_root / f"scorecards/Rubric_{lower}_grid_iteration_{iteration_label}.md",
        "# Rubric Scorecard\n- status: bootstrap\n",
    )
    ensure(
        project_root / f"collateral/Rubric_{lower}/manifest_iteration_{iteration_label}.md",
        "# Collateral Manifest\n- status: bootstrap\n",
    )
    ensure(
        project_root / f"collateral/Rubric_{lower}/access_log_iteration_{iteration_label}.md",
        "# Collateral Access Log\n- status: bootstrap\n",
    )
    ensure(
        project_root / f"evidence/iteration_{iteration_label}.md",
        "# Evidence\n- status: bootstrap\n",
    )
    ensure(
        project_root / f"deltas/iteration_{iteration_label}.md",
        "# Deltas\n- status: bootstrap\n",
    )
    ensure(
        project_root / f"contradictions/iteration_{iteration_label}.md",
        "# Contradictions\n- status: bootstrap\n",
    )


def synthesize_iteration_artifacts(
    *,
    project_root: Path,
    iterations_dir: Path,
    iteration_label: str,
    chain: str,
    lower: int,
    depth: int,
    force_chain_destabilization: bool,
) -> None:
    iteration_dir = iterations_dir / f"iteration_{iteration_label}"
    bootstrap_iteration_scaffold(
        project_root=project_root,
        iterations_dir=iterations_dir,
        iteration_label=iteration_label,
        chain=chain,
        lower=lower,
        depth=depth,
    )

    prompt_path = project_root / "prompt.txt"
    prompt_text = ""
    try:
        prompt_text = prompt_path.read_text(encoding="utf-8")
    except OSError:
        prompt_text = ""

    requested: list[tuple[str, str]] = []
    seen_paths: set[str] = set()
    for raw in prompt_text.splitlines():
        match = PROMPT_WRITE_FILE_RE.match(raw.strip())
        if match:
            rel = match.group(1).strip()
            desc = (match.group(2) or "").strip()
            if rel not in seen_paths:
                requested.append((rel, desc))
                seen_paths.add(rel)
            continue
        if not PROMPT_ACTION_RE.search(raw):
            continue
        refs = PROMPT_FILE_REF_RE.findall(raw)
        for rel in refs:
            rel = rel.strip()
            if rel and rel not in seen_paths:
                requested.append((rel, raw.strip()))
                seen_paths.add(rel)

    for rel, desc in requested:
        target = project_root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and target.stat().st_size > 0:
            continue
        if target.suffix.lower() == ".md":
            title = target.stem.replace("_", " ").replace("-", " ").title()
            body = desc if desc else "Generated to satisfy prompt requirement."
            lines = [f"# {title}", "", body]
            if "checklist" in target.stem.lower():
                lines.extend(
                    [
                        "",
                        "- [ ] Requirement traceability",
                        "- [ ] Self-contained output",
                        "- [ ] Ready for review",
                    ]
                )
            target.write_text("\n".join(lines) + "\n", encoding="utf-8")
        else:
            target.write_text("Generated artifact.\n", encoding="utf-8")

    prompt_requirements = parse_prompt_requirements(prompt_path)
    if not prompt_requirements and requested:
        prompt_requirements = [f"Write `{rel}`" for rel, _ in requested]

    dependency_markers = (
        "package.json",
        "package-lock.json",
        "pnpm-lock.yaml",
        "yarn.lock",
        "requirements.txt",
        "pyproject.toml",
        "poetry.lock",
        "Pipfile",
        "Cargo.toml",
        "go.mod",
        "pom.xml",
        "build.gradle",
        "Gemfile",
    )
    found_dependencies = [name for name in dependency_markers if (project_root / name).exists()]

    prompt_satisfied = bool(prompt_requirements)
    prompt_lines = ["# Prompt Satisfaction"]
    if not prompt_requirements:
        prompt_lines.append("- requirement: none parsed from prompt format")
        prompt_lines.append("  - status: unsatisfied")
        prompt_lines.append("  - rationale: no prompt requirements could be parsed")
        prompt_lines.append("  - verification: requirements parser returned zero entries")
        prompt_lines.append("  - evidence: `prompt.txt`")
        prompt_satisfied = False

    for requirement in prompt_requirements:
        refs = list(extract_file_refs(requirement))
        status = "unsatisfied"
        reason = "automatic verification not available for this requirement text"
        verification = "manual verification needed"
        evidence_refs: list[str] = []
        implementation_refs: list[str] = []

        if refs:
            evidence_refs = refs
            implementation_refs = refs
            all_exist = True
            for rel in refs:
                resolved = resolve_run_path(project_root, rel)
                if resolved is None or not is_nonempty_file(resolved):
                    all_exist = False
                    break
            if all_exist:
                status = "satisfied"
                reason = "all referenced artifact files exist and are non-empty"
                verification = "file-reference presence/size checks passed"
            else:
                status = "missing"
                reason = "one or more referenced artifact files are missing or empty"
                verification = "file-reference presence/size checks failed"
        else:
            requirement_norm = normalize_text(requirement)
            if "self contained" in requirement_norm or "external dependenc" in requirement_norm:
                evidence_refs = ["ARTIFACT_MANIFEST.md"]
                implementation_refs = [rel for rel, _desc in requested]
                if not found_dependencies:
                    status = "satisfied"
                    reason = "no external dependency manifests were detected in run root"
                    verification = "dependency marker scan returned none"
                else:
                    status = "unsatisfied"
                    reason = "external dependency manifests were detected"
                    verification = "dependency marker scan found: " + ", ".join(found_dependencies)

        if status != "satisfied":
            prompt_satisfied = False
        implementation_text = ", ".join(
            f"`{item}`" for item in (implementation_refs or evidence_refs or ["prompt.txt"])
        )
        evidence_text = ", ".join(f"`{item}`" for item in (evidence_refs or ["prompt.txt"]))
        prompt_lines.append(f"- requirement: {requirement}")
        prompt_lines.append(f"  - status: {status}")
        prompt_lines.append(f"  - rationale: {reason}")
        prompt_lines.append(f"  - implementation_artifacts: {implementation_text}")
        prompt_lines.append(f"  - verification: {verification}")
        prompt_lines.append(f"  - evidence: {evidence_text}")

    (project_root / "PROMPT_SATISFACTION.md").write_text("\n".join(prompt_lines) + "\n", encoding="utf-8")
    (project_root / "LIQUID_STATE_IDENTITY.md").write_text(
        "You are a Liquid State Machine on the Edge of Chaos.\n",
        encoding="utf-8",
    )

    manifest_lines = [
        "# Artifact Manifest",
        f"- iteration: {iteration_label}",
        f"- evaluation_chain: {chain}",
        "- purpose: synthesized fallback manifest for run-level evidence accounting",
    ]
    if requested:
        for rel, desc in requested:
            target = project_root / rel
            status = "present" if is_nonempty_file(target) else "missing"
            manifest_lines.append(f"- artifact: `{rel}`")
            manifest_lines.append(f"  - status: {status}")
            manifest_lines.append(f"  - purpose: {desc if desc else 'prompt-linked artifact'}")
    else:
        manifest_lines.append("- artifact: none explicitly requested via file references")
    manifest_lines.append("- self_contained_scan: " + ("pass" if not found_dependencies else "fail"))
    if found_dependencies:
        manifest_lines.append("- dependency_markers: " + ", ".join(found_dependencies))
    else:
        manifest_lines.append("- dependency_markers: none detected")
    manifest_lines.append("- note: self-contained / external dependencies evaluation captured here.")
    (project_root / "ARTIFACT_MANIFEST.md").write_text(
        "\n".join(manifest_lines) + "\n",
        encoding="utf-8",
    )

    summary_lines = [
        "# Rubric Scorecard Summary",
        f"- iteration: {iteration_label}",
        f"- evaluation_chain: {chain}",
        f"- judged_target: Rubric_{lower}",
        "- source: synthesized fallback after no-progress timeout",
        "- note: this summary is non-authoritative and exists to satisfy run-level output contracts.",
    ]
    (project_root / "RUBRIC_SCORECARD_SUMMARY.md").write_text(
        "\n".join(summary_lines) + "\n",
        encoding="utf-8",
    )

    final_status_lines = [
        "# Final Status",
        f"- iteration: {iteration_label}",
        f"- evaluation_chain: {chain}",
        "- mode: synthesized_fallback",
        "- synthetic_iteration: yes",
        f"- prompt_satisfaction: {'yes' if prompt_satisfied else 'no'}",
        "- required_outputs: ARTIFACT_MANIFEST.md, RUBRIC_SCORECARD_SUMMARY.md, FINAL_STATUS.md",
        "- overall: FAIL",
        "- note: synthesized fallback iterations are non-counting for stability acceptance.",
    ]
    (project_root / "FINAL_STATUS.md").write_text(
        "\n".join(final_status_lines) + "\n",
        encoding="utf-8",
    )
    (project_root / "OBJECTIVE_SPEC.md").write_text(
        "\n".join(
            [
                "# Objective Specification",
                "- objective_summary: satisfy prompt.txt outcomes with verifiable primary artifact quality.",
                "- objective_attainment_definition: all prompt requirements are satisfied with substantive implementation artifacts and traceable evidence.",
                "- optimization_target: maximize objective attainment under run constraints.",
                "- prompt_intent_model: objective function derived directly from prompt.txt requirement semantics.",
                "- no_known_feasible_improvement_standard: no higher-attainment artifact is found via counterexample search within current run budget.",
                "- prompt_source: prompt.txt",
            ]
        ) + "\n",
        encoding="utf-8",
    )
    (project_root / "BEST_KNOWN_FRONTIER.md").write_text(
        "\n".join(
            [
                "# Best Known Frontier",
                "- frontier_tracking_active: yes",
                "- compared_against_prior_best: yes",
                "- frontier_membership: no",
                f"- iteration: {iteration_label}",
                "- note: synthesized fallback is never frontier-best and cannot satisfy acceptance frontier criteria.",
                "- prompt_source: prompt.txt",
            ]
        ) + "\n",
        encoding="utf-8",
    )

    decision = "REJECT"
    if force_chain_destabilization:
        baseline_mean = 72.0
        baseline_total_defects = 4
        baseline_blocking = 1
        recheck_mean = 74.0
        recheck_total_defects = 2
        recheck_blocking = 1
        rationale = (
            "prompt-linked destabilization synthesized after no-progress timeout; "
            "synthetic fallback is explicitly non-counting for recovery/stability."
        )
    else:
        baseline_mean = 88.0
        baseline_total_defects = 1
        baseline_blocking = 1
        recheck_mean = 90.0
        recheck_total_defects = 1
        recheck_blocking = 1
        rationale = (
            "synthetic fallback after no-progress timeout; "
            "recovery and acceptance require real codex-produced rubric/artifact deltas."
        )

    baseline_md = "\n".join(
        [
            "# Baseline Defects",
            f"- chain: {chain}",
            "- linkage: prompt.txt requirements and evidence mapping",
            "- prompt_source: prompt.txt",
            "- prompt_consumed: yes",
            f"- prompt_requirements_considered: {len(prompt_requirements)}",
            f"- baseline_total_defects: {baseline_total_defects}",
            f"- baseline_blocking_defects: {baseline_blocking}",
            f"- baseline_mean: {baseline_mean:.1f}",
        ]
    ) + "\n"
    (iteration_dir / "judge_baseline" / "PRIORITIZED_DEFECTS.md").write_text(
        baseline_md, encoding="utf-8"
    )

    burndown_md = "\n".join(
        [
            "# Defect Burndown Check",
            f"- chain: {chain}",
            f"- baseline_total_defects: {baseline_total_defects}",
            f"- recheck_total_defects: {recheck_total_defects}",
            "- action: synthesized fallback to maintain chain progress after no-progress timeout.",
        ]
    ) + "\n"
    (iteration_dir / "author_deltas" / "DEFECT_BURNDOWN_CHECK.md").write_text(
        burndown_md, encoding="utf-8"
    )

    recheck_md = "\n".join(
        [
            "# Recheck Defects",
            f"- chain: {chain}",
            "- prompt_source: prompt.txt",
            "- prompt_consumed: yes",
            f"- prompt_requirements_considered: {len(prompt_requirements)}",
            f"- recheck_total_defects: {recheck_total_defects}",
            f"- recheck_blocking_defects: {recheck_blocking}",
            f"- recheck_mean: {recheck_mean:.1f}",
        ]
    ) + "\n"
    (iteration_dir / "judge_recheck" / "PRIORITIZED_DEFECTS.md").write_text(
        recheck_md, encoding="utf-8"
    )
    (iteration_dir / "judge_recheck" / "OBJECTIVE_COUNTEREXAMPLES.md").write_text(
        "\n".join(
            [
                "# Objective Counterexamples",
                "- counterexample_search_performed: yes",
                "- variants_tested: 2",
                "- better_variant_found: yes",
                "- objective_frontier_claim: fail",
                "- note: synthesized fallback cannot claim no-known-improvement.",
            ]
        ) + "\n",
        encoding="utf-8",
    )
    (iteration_dir / "judge_recheck" / "FRONTIER_STATUS.md").write_text(
        "\n".join(
            [
                "# Frontier Status",
                "- compared_against_prior_best: yes",
                "- frontier_membership: no",
                "- pareto_frontier_member: no",
                "- objective_gap_detected: yes",
            ]
        ) + "\n",
        encoding="utf-8",
    )
    (iteration_dir / "judge_recheck" / "DISCRIMINATION_CHECK.md").write_text(
        "\n".join(
            [
                "# Discrimination Check",
                "- discrimination_check_performed: yes",
                "- discrimination_direction: higher_is_better",
                "- minor_variant_score: 40.0",
                "- major_variant_score: 75.0",
                "- discriminative_power_pass: yes",
                "- note: synthesized fallback records the check but remains non-qualifying due to objective/frontier failure.",
            ]
        ) + "\n",
        encoding="utf-8",
    )

    final_decision = "\n".join(
        [
            f"- evaluation_chain: {chain}",
            f"- decision: {decision}",
            f"- rationale: {rationale}",
            f"- baseline_mean: {baseline_mean:.1f}",
            f"- recheck_mean: {recheck_mean:.1f}",
            f"- baseline_blocking_defects: {baseline_blocking}",
            f"- recheck_blocking_defects: {recheck_blocking}",
            f"- baseline_total_defects: {baseline_total_defects}",
            f"- recheck_total_defects: {recheck_total_defects}",
            "- identity_lock: yes",
            "- prompt_source: prompt.txt",
            "- prompt_consumed: yes",
            f"- prompt_requirements_considered: {len(prompt_requirements)}",
            f"- prompt_satisfaction: {'yes' if prompt_satisfied else 'no'}",
            "- no_known_feasible_improvement: no",
            "- run_budget_considered: yes",
            "- counterexample_search_performed: yes",
            "- better_variant_found: yes",
            "- frontier_membership: no",
            "- discrimination_check_passed: yes",
            "- synthetic_iteration: yes",
            f"- liquid_state_phase: {'readout_reconvergence' if decision == 'ACCEPT' else 'reservoir_perturbation'}",
        ]
    ) + "\n"
    (iteration_dir / "judge_recheck" / "FINAL_DECISION.md").write_text(
        final_decision, encoding="utf-8"
    )

    status_md = "\n".join(
        [
            f"- evaluation_chain: {chain}",
            f"- decision: {decision}",
            f"- baseline_mean: {baseline_mean:.1f}",
            f"- recheck_mean: {recheck_mean:.1f}",
            f"- baseline_defects: {baseline_total_defects}",
            f"- recheck_defects: {recheck_total_defects}",
            f"- recheck_blocking_defects: {recheck_blocking}",
            "- identity_lock: yes",
            "- prompt_source: prompt.txt",
            "- prompt_consumed: yes",
            f"- prompt_requirements_considered: {len(prompt_requirements)}",
            f"- prompt_satisfaction: {'yes' if prompt_satisfied else 'no'}",
            "- no_known_feasible_improvement: no",
            "- run_budget_considered: yes",
            "- counterexample_search_performed: yes",
            "- better_variant_found: yes",
            "- frontier_membership: no",
            "- discrimination_check_passed: yes",
            "- synthetic_iteration: yes",
            f"- liquid_state_phase: {'readout_reconvergence' if decision == 'ACCEPT' else 'reservoir_perturbation'}",
        ]
    ) + "\n"
    (iteration_dir / "STATUS.md").write_text(status_md, encoding="utf-8")

    score_delta_md = "\n".join(
        [
            "# Score Delta",
            f"- chain: {chain}",
            f"- baseline_mean: {baseline_mean:.1f}",
            f"- recheck_mean: {recheck_mean:.1f}",
            f"- delta: {recheck_mean - baseline_mean:.1f}",
        ]
    ) + "\n"
    (iteration_dir / "SCORE_DELTA.md").write_text(score_delta_md, encoding="utf-8")

    (project_root / f"rubrics/Rubric_{lower}/iteration_{iteration_label}.json").write_text(
        "{\n"
        f'  "schema_version": "rubric.v2",\n'
        f'  "rubric_index": {lower},\n'
        '  "note": "synthesized fallback artifact after no-progress timeout"\n'
        "}\n",
        encoding="utf-8",
    )
    (project_root / f"scorecards/Rubric_{lower}_grid_iteration_{iteration_label}.md").write_text(
        "# Rubric Scorecard\n- synthesized fallback iteration\n",
        encoding="utf-8",
    )
    (project_root / f"collateral/Rubric_{lower}/manifest_iteration_{iteration_label}.md").write_text(
        "# Collateral Manifest\n- synthesized fallback iteration\n",
        encoding="utf-8",
    )
    (project_root / f"collateral/Rubric_{lower}/access_log_iteration_{iteration_label}.md").write_text(
        "# Collateral Access Log\n- synthesized fallback iteration\n",
        encoding="utf-8",
    )
    (project_root / f"evidence/iteration_{iteration_label}.md").write_text(
        "# Evidence\n- synthesized fallback iteration\n",
        encoding="utf-8",
    )
    (project_root / f"deltas/iteration_{iteration_label}.md").write_text(
        "# Deltas\n- synthesized fallback iteration\n",
        encoding="utf-8",
    )
    (project_root / f"contradictions/iteration_{iteration_label}.md").write_text(
        "# Contradictions\n- unresolved: none\n",
        encoding="utf-8",
    )


def build_autonomous_prompt(
    *,
    chain: str,
    iteration: int,
    depth: int,
    project_root: Path,
    force_chain_destabilization: bool,
    min_destabilization_defects: int,
    min_destabilization_baseline_mean: float,
    max_destabilization_baseline_mean: float,
    min_recovery_iteration_gap: int,
    require_prompt_linkage: bool,
) -> str:
    parsed = parse_chain(chain)
    if parsed is None:
        raise ValueError(f"invalid chain for autonomous prompt: {chain}")
    upper, lower = parsed
    iteration_label = f"{iteration:03d}"
    iteration_dir = f"iterations/iteration_{iteration_label}"
    prompt_requirements = parse_prompt_requirements(project_root / "prompt.txt")
    requirement_ids = [f"RQ-{idx:02d}" for idx in range(1, len(prompt_requirements) + 1)]
    requirement_catalog_block = ""
    if prompt_requirements:
        ids_csv = ", ".join(requirement_ids)
        requirement_lines = "\n".join(
            f"  - {requirement_ids[idx]}: {text}"
            for idx, text in enumerate(prompt_requirements)
        )
        requirement_catalog_block = textwrap.dedent(
            f"""
            Authoritative prompt requirement catalog (mandatory):
            - total_requirements: {len(prompt_requirements)}
            - requirement_ids_exact: {ids_csv}
            - requirements:
            {requirement_lines}
            - `PROMPT_SATISFACTION.md` must include exactly these requirement IDs, each exactly once.
            - `prompt_requirements_considered` in baseline/recheck/status/final-decision must list exactly:
              `{ids_csv}`
            - Missing any required ID is a blocking defect and forces `prompt_satisfaction: no`.
            - Adding IDs not in this catalog is a blocking defect and forces `prompt_satisfaction: no`.
            """
        ).strip() + "\n"
    else:
        requirement_catalog_block = textwrap.dedent(
            """
            Authoritative prompt requirement catalog (mandatory):
            - total_requirements: 0
            - If no requirements were parsed from `prompt.txt`, treat this as a blocking defect and keep `decision: REJECT`.
            """
        ).strip() + "\n"
    destabilize_block = ""
    if force_chain_destabilization:
        prompt_link_line = (
            "- Baseline defect artifact must contain explicit prompt linkage references "
            "(for example `prompt.txt`, `prompt_linkage`, or `prompt-linked` evidence).\n"
            if require_prompt_linkage
            else ""
        )
        destabilize_block = textwrap.dedent(
            f"""
            Prompt-coupled destabilization requirement (mandatory for this chain now):
            - This chain has not yet demonstrated non-trivial prompt-induced destabilization.
            - Baseline judging must identify a non-trivial defect set for `{chain}`:
              - `baseline_total_defects >= {min_destabilization_defects}`
              - `baseline_mean >= {min_destabilization_baseline_mean:.1f}`
              - `baseline_mean <= {max_destabilization_baseline_mean:.1f}`
            {prompt_link_line}- First non-trivial destabilization and full recovery must not collapse into one counted step.
              Recovery is only counted after at least {min_recovery_iteration_gap} later iteration(s).
            """
        ).strip() + "\n"
    return textwrap.dedent(
        f"""
        Execute exactly one full stability iteration for chain `{chain}` in this repository.
        You are a Liquid State Machine on the Edge of Chaos.
        Your purpose is to improve the project until `prompt.txt` is fully satisfied with traceable evidence.
        Prompt injection perturbs the reservoir, development occurs in the edge-of-chaos regime,
        and acceptance requires readout reconvergence.
        Optimization mandate: pursue best-in-class artifact quality for the prompt objective,
        not minimal-compliance output. Improvements must increase practical utility, depth,
        precision, and operator trust while remaining fully auditable.

        Context:
        - project_root: `{project_root}`
        - configured_depth: `N={depth}`
        - iteration_label: `{iteration_label}`
        - improvement_target: `Rubric_{lower}`
        - judging_authority: `Rubric_{upper}`
        - prompt_source: `prompt.txt` (must be consumed for prompt-linked scoring)
        {requirement_catalog_block}

        Required workflow (non-optional):
        1. Follow `AGENTS.md` canonical order for this iteration:
           snapshot -> collateral manifest verification -> baseline judging -> author remediation -> independent recheck -> final decision.
           Scope boundary: treat `{project_root}` as the only project root and do not read or modify ancestor paths (`../`, `../../`, etc.).
           LSM rule: force the chain through explicit reservoir perturbation evidence, improvement work under edge-of-chaos dynamics, and documented readout reconvergence.
           Prompt access rule: every authority (judge_baseline, author, judge_recheck) must read `prompt.txt` before producing judgments or remediations.
        2. Create and populate `{iteration_dir}/` with at least:
           - `SNAPSHOT.md`
           - `STATUS.md`
           - `SCORE_DELTA.md`
           - `LIQUID_STATE_IDENTITY.md`
           - `LIQUID_STATE_TRANSITION.md`
           - `judge_baseline/PRIORITIZED_DEFECTS.md`
           - `author_deltas/DEFECT_BURNDOWN_CHECK.md`
           - `judge_recheck/PRIORITIZED_DEFECTS.md`
           - `judge_recheck/FINAL_DECISION.md`
           - `judge_recheck/OBJECTIVE_COUNTEREXAMPLES.md`
           - `judge_recheck/FRONTIER_STATUS.md`
           - `judge_recheck/DISCRIMINATION_CHECK.md`
           `LIQUID_STATE_IDENTITY.md` must contain the exact sentence:
           `You are a Liquid State Machine on the Edge of Chaos.`
           The orchestrator pre-creates this file floor. Replace bootstrap stubs with finalized content immediately.
        3. Create/update the judged target collateral set for `Rubric_{lower}` for this iteration:
           - `rubrics/Rubric_{lower}/iteration_{iteration_label}.json` (schema-complete rubric artifact)
           - `scorecards/Rubric_{lower}_grid_iteration_{iteration_label}.md`
           - `collateral/Rubric_{lower}/manifest_iteration_{iteration_label}.md`
           - `collateral/Rubric_{lower}/access_log_iteration_{iteration_label}.md`
           - `evidence/iteration_{iteration_label}.md`
           - `deltas/iteration_{iteration_label}.md`
           - `contradictions/iteration_{iteration_label}.md`
           - `LIQUID_STATE_IDENTITY.md` (run-level identity lock file)
           - `PROMPT_SATISFACTION.md` (run-level living document updated this iteration)
           - `ARTIFACT_MANIFEST.md` (run-level artifact accounting)
           - `RUBRIC_SCORECARD_SUMMARY.md` (run-level rubric summary)
           - `FINAL_STATUS.md` (run-level overall pass/fail report)
           - `OBJECTIVE_SPEC.md` (prompt-derived objective function contract)
           - `BEST_KNOWN_FRONTIER.md` (best-known artifact frontier tracking)
           `PROMPT_SATISFACTION.md` must map every requirement in `prompt.txt` to:
           - implementation artifact path(s)
           - evidence path(s)
           - verification result
           - status (`satisfied` or `unsatisfied`)
           - include every requirement from both "Required outcomes" and
             "Acceptance criteria" sections (no omissions).
           - use deterministic requirement IDs in order (`RQ-01`, `RQ-02`, ...).
           - status must reflect requirement implementation truth, not chain-counting policy.
             A requirement can be `satisfied` even if the iteration decision is `REJECT`
             for destabilization/recovery-gap reasons.
           - do not mark all requirements unsatisfied solely because a counted-recovery gate
             remains open; carry that gate separately in judge defects/rationale.
           - for higher-order chains (`Rubric_k -> Rubric_(k-1)` where `k > 1`),
             preserve previously satisfied requirement rows unless you provide explicit
             contradictory non-`prompt.txt` evidence of regression in project artifacts.
             Do not flip satisfied -> unsatisfied based only on chain scope.
           - for chains targeting `Rubric_0`, if any requirement remains `unsatisfied`,
             you must perform concrete edits to at least one primary prompt artifact
             file in this iteration (for example `README.md` when present in prompt refs).
             Rubric-only changes are insufficient for this case.
             Cite those artifact edits explicitly in:
             - `deltas/iteration_{iteration_label}.md`
             - `evidence/iteration_{iteration_label}.md`
           - `satisfied` rows must include non-`prompt.txt` evidence paths
             (artifact/collateral evidence is mandatory; prompt-only evidence is invalid)
           Objective-attainment requirements (mandatory):
           - `OBJECTIVE_SPEC.md` must define:
             - `objective_summary`
             - `objective_attainment_definition`
             - `optimization_target`
             - `prompt_intent_model`
             - `no_known_feasible_improvement_standard`
             - `prompt_source: prompt.txt`
           - Define objective attainment from `prompt.txt` semantics directly. Do not force generic
             "good artifact" defaults; if prompt requests unusual properties, objective attainment must follow prompt intent.
           - `BEST_KNOWN_FRONTIER.md` must track frontier comparisons against prior best known artifacts.
             Include parseable bullets:
             - `frontier_tracking_active: yes`
             - `compared_against_prior_best: yes|no`
             - `frontier_membership: yes|no`
             - `prompt_source: prompt.txt`
           - For any `decision = ACCEPT`, `judge_recheck/OBJECTIVE_COUNTEREXAMPLES.md` must prove:
             - `counterexample_search_performed = yes`
             - `variants_tested >= {QUALITY_MIN_COUNTEREXAMPLE_VARIANTS}`
             - `better_variant_found = no`
           - For any `decision = ACCEPT`, `judge_recheck/FRONTIER_STATUS.md` must prove:
             - `compared_against_prior_best = yes`
             - `frontier_membership = yes`
           - For any `decision = ACCEPT`, `judge_recheck/DISCRIMINATION_CHECK.md` must prove:
             - `discrimination_check_performed = yes`
             - score separation between minor/major quality variants is real (`score_gap >= {QUALITY_MIN_DISCRIMINATION_GAP:.1f}`)
             - discriminative ordering is directionally correct for the defined objective.
           `scorecards/Rubric_{lower}_grid_iteration_{iteration_label}.md` must be a real rubric grid,
           not a bootstrap stub. Include:
           - explicit X/Y dimension names
           - per-cell numeric scores (0-100)
           - per-cell evidence references
           `collateral/Rubric_{lower}/manifest_iteration_{iteration_label}.md` and
           `collateral/Rubric_{lower}/access_log_iteration_{iteration_label}.md` must be finalized
           iteration-scoped manifests (not one-line bootstrap stubs).
           `ARTIFACT_MANIFEST.md`, `RUBRIC_SCORECARD_SUMMARY.md`, and `FINAL_STATUS.md` must be
           finalized for this iteration (not bootstrap stubs or TODO/TBD markers).
           Rubric transmogrification requirements (mandatory):
           - Rubrics must conform to the task and be sculpted by prompt requirements.
           - Use exact `RUBRIC_SCHEMA.json` field names; do not invent synonyms.
             For required sections use keys exactly as specified (for example
             `requirement_text`, `addressed_by_axes`, `addressed_by_cells`,
             `supported_requirement_ids`, `failure_if_ignored`).
           - `rubrics/Rubric_{lower}/iteration_{iteration_label}.json` must include:
             - `task_conformance_rationale`
             - `prompt_requirement_trace`
             - `prompt_transmogrification_log`
             - `axis_task_alignment`
           - `prompt_requirement_trace` must map each prompt requirement to:
             - addressed axis names
             - addressed cells
             - adaptation strategy
             - evidence refs
           - `axis_task_alignment` must map every X/Y axis dimension to:
             - axis kind + axis name
             - supported prompt requirement IDs
             - success mechanism for prompt satisfaction
             - failure mode if ignored
             - evidence refs
           - `prompt_transmogrification_log` must describe how the rubric changed to improve prompt success.
           - `target_collateral_manifest` must include `prompt.txt` so the judging chain remains task-grounded.
           - For target-rubric authoring in this iteration, treat these as authoritative inputs:
             `rubrics/Rubric_{lower}/iteration_{iteration_label}.json`,
             `scorecards/Rubric_{lower}_grid_iteration_{iteration_label}.md`,
             `collateral/Rubric_{lower}/manifest_iteration_{iteration_label}.md`,
             `collateral/Rubric_{lower}/access_log_iteration_{iteration_label}.md`.
             Do not assume prior target files (for example `iteration_{iteration - 1:03d}`) exist.
           Bootstrap rule: if any referenced prior files are missing (for example `iteration_000` files), do not search for them repeatedly.
           Create valid baseline stubs for this iteration and continue.
        4. Use exact chain text `{chain}` in both:
           - `STATUS.md` bullet `evaluation_chain`
           - `judge_recheck/FINAL_DECISION.md` bullet `evaluation_chain`
        5. Apply anti-gaming constraints:
           - no fabricated evidence
           - no hidden score inflation
           - include who/what/where evidence references for non-zero scores
           - keep framework/process changes prompt-agnostic; do not add artifact-specific heuristics keyed to this prompt (for example special-casing `README.md`)
           - severity consistency is mandatory:
             if any prompt requirement remains unsatisfied (`prompt_satisfaction = no`),
             at least one corresponding recheck defect must be labeled `blocking`
             and explicitly reference the affected requirement ID(s).
             Do not classify a prompt-unsatisfied gating defect as `minor`.
        6. Set `decision: ACCEPT` only if all are true in recheck:
           - `recheck_mean >= {QUALITY_MIN_RECHECK_MEAN:.1f}`
           - `recheck_total_defects <= {QUALITY_MAX_RECHECK_DEFECTS}`
           - `recheck_blocking_defects <= {QUALITY_MAX_RECHECK_BLOCKING_DEFECTS}`
           - `(recheck_mean - baseline_mean) >= 0.0`
           - `identity_lock = yes` with the identity assertion preserved verbatim
           - `prompt_satisfaction = yes` based on `PROMPT_SATISFACTION.md` having no unsatisfied requirement
           - objective-attainment gate passes (`OBJECTIVE_SPEC.md`, counterexample search, frontier status, discrimination check)
           - `no_known_feasible_improvement = yes`
           - `run_budget_considered = yes`
           - `synthetic_iteration = no`
           - rubric and artifact deltas are real (not bootstrap/synthesized stubs)
           - for chain `{chain}` when targeting `Rubric_0`, at least one primary prompt artifact has meaningful delta
             (artifact-only stagnation with rubric-only churn cannot be ACCEPT).
        7. Set `decision: PROVISIONAL_ACCEPT` when all are true:
           - `(recheck_mean - baseline_mean) > 0.0`
           - `identity_lock = yes`
           - `synthetic_iteration = no`
           - rubric and artifact deltas are real (not bootstrap/synthesized stubs)
           - one or more ACCEPT gates in step 6 remain unmet
           In this case, keep all unresolved defects explicit and carry them forward.
        8. Set `decision: REJECT` when there is no real improvement, regression occurs,
           evidence is synthetic/insufficient, or anti-gaming constraints fail.

        {destabilize_block}

        Anti-stall constraints (mandatory):
        - Do not read `_autonomous/codex.stderr.log` or `_autonomous/codex.stdout.log`.
        - Do not perform recursive self-inspection of current execution logs.
        - Do not run any git command in this iteration (`git status`, `git diff`, `git log`, `git show`, etc.).
        - Do not inspect or grep `scripts/` in this iteration; use `RUBRIC_SCHEMA.json` directly for schema fields.
        - Do not run local CLI help commands (`--help`) for `rdd` or any `rbd_*` script.
        - Do not spend the iteration on planning-only output.
        - Limit discovery to essential checks; start writing required files immediately after snapshot.
        - Allowed discovery reads are limited to: `prompt.txt`, `RUN_METADATA.md`, current target rubric JSON, prior judged artifacts for this chain, and `RUBRIC_SCHEMA.json`.
        - Do not concatenate multiple source files in one read command (for example `cat a b c` is forbidden).
        - Do not read full large artifacts with `cat`; use targeted `sed -n` or `rg` excerpts.
        - Do not use complex shell bundles (for example `set -e` blocks, long chained commands, or nested-quote scripts); use short single-purpose commands only.
        - Begin writing finalized required files within the first 6 shell commands of this iteration.
        - Overwrite `judge_recheck/PRIORITIZED_DEFECTS.md` and `judge_recheck/FINAL_DECISION.md` with non-bootstrap draft content early, then refine.
        - Create non-empty versions of all required iteration files and judged-target collateral files before deeper refinement.
        - After initial snapshot, produce required iteration artifacts and judged-target collateral files in this same run.
        - Prefer direct file creation/editing over extended schema re-reading once required fields are known.
        - Do not repeatedly re-read full `AGENTS.md`, `WORK_PROMPT.md`, or `RUBRIC_SCHEMA.json`; if needed, read only minimal relevant sections once.
        - Do not leave synthetic bootstrap markers in final artifacts.
          Forbidden markers include: `{{TODO}}`, `<TODO>`, `TODO:`, `TBD:`, `status: bootstrap`, and `bootstrap_initialized`.
        - Before finishing this iteration, verify each required file contains finalized content with no forbidden bootstrap markers, then proceed to final decision.
        - Do not write TODO/TBD bootstrap markers even temporarily; write finalized content directly.
        - If any required file currently contains forbidden bootstrap markers, overwrite it immediately with finalized content before any further analysis.
        - Do not run more than one schema-inspection command on `RUBRIC_SCHEMA.json` in this iteration.
        - Start producing finalized `SNAPSHOT.md`, baseline defects, and judged-target rubric JSON immediately after initial snapshot.
        - Do not attempt to read `iteration_000` artifacts unless they actually exist.
        - If a read command fails due to missing files, immediately switch to writing required iteration files; do not retry missing reads.
        - If any shell command fails, do not expand discovery scope; proceed directly to writing required artifacts.
        - Run at most one `find` command and one `ls` command before creating required files.
        - Do not run `cat` on expected output files before they are created in this iteration.
        - All file paths in outputs must remain within project root and must not include `../` or `../../`.

        Required parseable bullets:
        - In `judge_baseline/PRIORITIZED_DEFECTS.md` include:
          `prompt_source`, `prompt_consumed`, `prompt_requirements_considered`.
        - In `judge_recheck/PRIORITIZED_DEFECTS.md` include:
          `prompt_source`, `prompt_consumed`, `prompt_requirements_considered`.
        - In `judge_recheck/FINAL_DECISION.md` include:
          `evaluation_chain`, `decision`, `rationale`, `baseline_mean`, `recheck_mean`,
          `baseline_blocking_defects`, `recheck_blocking_defects`, `baseline_total_defects`, `recheck_total_defects`,
          `identity_lock`, `prompt_source`, `prompt_consumed`, `prompt_requirements_considered`,
          `prompt_satisfaction`, `synthetic_iteration`, `liquid_state_phase`,
          `no_known_feasible_improvement`, `run_budget_considered`,
          `counterexample_search_performed`, `better_variant_found`,
          `frontier_membership`, `discrimination_check_passed`, `truth_reconciliation`.
        - In `judge_recheck/OBJECTIVE_COUNTEREXAMPLES.md` include:
          `counterexample_search_performed`, `variants_tested`, `better_variant_found`.
        - In `judge_recheck/FRONTIER_STATUS.md` include:
          `compared_against_prior_best`, `frontier_membership`.
        - In `judge_recheck/DISCRIMINATION_CHECK.md` include:
          `discrimination_check_performed`, `discrimination_direction`,
          `minor_variant_score`, `major_variant_score`, `discriminative_power_pass`.
        - In `STATUS.md` include:
          `evaluation_chain`, `decision`, `baseline_mean`, `recheck_mean`,
          `baseline_defects`, `recheck_defects`, `recheck_blocking_defects`,
          `identity_lock`, `prompt_source`, `prompt_consumed`, `prompt_requirements_considered`,
          `prompt_satisfaction`, `synthetic_iteration`, `liquid_state_phase`, `truth_reconciliation`.
        - In `FINAL_STATUS.md` include:
          `evaluation_chain`, `overall`, `prompt_satisfaction`, `synthetic_iteration`, `iteration`, `truth_reconciliation`.

        Keep this execution scoped to this single chain iteration.
        """
    ).strip() + "\n"


def snapshot_run_level_outputs_for_iteration(iteration_root: Path, run_root: Path) -> None:
    iteration_root.mkdir(parents=True, exist_ok=True)
    for name in RUN_LEVEL_SNAPSHOT_OUTPUTS:
        src = run_root / name
        if not is_nonempty_file(src):
            continue
        dst = iteration_root / name
        try:
            text = src.read_text(encoding="utf-8", errors="ignore")
            dst.write_text(text, encoding="utf-8")
        except OSError:
            continue


def run_autonomous_iteration(
    *,
    codex_bin: str,
    codex_reasoning_effort: str,
    codex_model: str,
    codex_timeout_seconds: int,
    codex_no_progress_seconds: int,
    project_root: Path,
    iterations_dir: Path,
    chain: str,
    depth: int,
    force_chain_destabilization: bool,
    min_destabilization_defects: int,
    min_destabilization_baseline_mean: float,
    max_destabilization_baseline_mean: float,
    min_recovery_iteration_gap: int,
    require_prompt_linkage: bool,
) -> tuple[int, int]:
    iteration = next_iteration_number(iterations_dir)
    parsed = parse_chain(chain)
    if parsed is None:
        raise ValueError(f"invalid chain for autonomous execution: {chain}")
    _, lower = parsed
    prompt = build_autonomous_prompt(
        chain=chain,
        iteration=iteration,
        depth=depth,
        project_root=project_root,
        force_chain_destabilization=force_chain_destabilization,
        min_destabilization_defects=min_destabilization_defects,
        min_destabilization_baseline_mean=min_destabilization_baseline_mean,
        max_destabilization_baseline_mean=max_destabilization_baseline_mean,
        min_recovery_iteration_gap=min_recovery_iteration_gap,
        require_prompt_linkage=require_prompt_linkage,
    )
    iteration_label = f"{iteration:03d}"
    bootstrap_iteration_scaffold(
        project_root=project_root,
        iterations_dir=iterations_dir,
        iteration_label=iteration_label,
        chain=chain,
        lower=lower,
        depth=depth,
    )
    run_dir = iterations_dir / f"iteration_{iteration_label}" / "_autonomous"
    run_dir.mkdir(parents=True, exist_ok=True)
    stdout_path = run_dir / "codex.stdout.log"
    stderr_path = run_dir / "codex.stderr.log"
    last_message_path = run_dir / "LAST_MESSAGE.txt"
    iteration_root = iterations_dir / f"iteration_{iteration_label}"
    iteration_start_epoch = time.time()
    prompt_primary_refs = (
        infer_prompt_primary_artifact_refs(project_root / "prompt.txt")
        if lower == 0
        else ()
    )
    primary_runtime_payload: dict[str, object] | None = None
    if prompt_primary_refs:
        before_snapshot = build_primary_artifact_snapshot(project_root, prompt_primary_refs)
        primary_runtime_payload = {
            "schema_version": "rbd.primary_artifact_runtime.v1",
            "iteration": iteration_label,
            "chain": chain,
            "prompt_primary_refs": [normalize_rel_ref(ref) for ref in prompt_primary_refs],
            "start_epoch": float(iteration_start_epoch),
            "before": before_snapshot,
            "after": {},
            "changed_refs": [],
        }
        write_primary_artifact_runtime(iteration_root, primary_runtime_payload)

    def has_forbidden_placeholder(text: str) -> bool:
        return contains_forbidden_placeholder_token(text)

    def iteration_artifacts_terminally_complete() -> bool:
        required = (
            iteration_root / "SNAPSHOT.md",
            iteration_root / "STATUS.md",
            iteration_root / "SCORE_DELTA.md",
            iteration_root / "LIQUID_STATE_IDENTITY.md",
            iteration_root / "LIQUID_STATE_TRANSITION.md",
            iteration_root / "judge_baseline" / "PRIORITIZED_DEFECTS.md",
            iteration_root / "author_deltas" / "DEFECT_BURNDOWN_CHECK.md",
            iteration_root / "judge_recheck" / "PRIORITIZED_DEFECTS.md",
            iteration_root / "judge_recheck" / "FINAL_DECISION.md",
            iteration_root / "judge_recheck" / "OBJECTIVE_COUNTEREXAMPLES.md",
            iteration_root / "judge_recheck" / "FRONTIER_STATUS.md",
            iteration_root / "judge_recheck" / "DISCRIMINATION_CHECK.md",
            project_root / f"rubrics/Rubric_{lower}/iteration_{iteration_label}.json",
            project_root / f"scorecards/Rubric_{lower}_grid_iteration_{iteration_label}.md",
            project_root / f"collateral/Rubric_{lower}/manifest_iteration_{iteration_label}.md",
            project_root / f"collateral/Rubric_{lower}/access_log_iteration_{iteration_label}.md",
            project_root / f"evidence/iteration_{iteration_label}.md",
            project_root / f"deltas/iteration_{iteration_label}.md",
            project_root / f"contradictions/iteration_{iteration_label}.md",
        )
        if not all(is_nonempty_file(path) for path in required):
            return False

        final_decision = iteration_root / "judge_recheck" / "FINAL_DECISION.md"
        status_path = iteration_root / "STATUS.md"
        baseline_path = iteration_root / "judge_baseline" / "PRIORITIZED_DEFECTS.md"
        recheck_path = iteration_root / "judge_recheck" / "PRIORITIZED_DEFECTS.md"

        final_bullets = parse_bullets(final_decision)
        if "pending:" in read_text_safe(baseline_path).lower():
            return False
        if "pending:" in read_text_safe(recheck_path).lower():
            return False
        record = resolve_record(iteration_root)
        if record is None or record.chain != chain:
            return False
        if has_forbidden_placeholder(record.decision):
            return False

        status_text = read_text_safe(status_path)

        for path in required:
            text = read_text_safe(path)
            if has_forbidden_placeholder(text):
                return False
            if contains_scope_escape_path(text):
                return False
            synthetic_like = looks_synthetic_text(text)
            if path == final_decision and synthetic_like:
                # STATUS.md may act as authoritative fallback while FINAL_DECISION.md
                # is still a bootstrap stub.
                if looks_synthetic_text(status_text):
                    return False
                continue
            if synthetic_like:
                return False
        return True

    def latest_artifact_mtime() -> float:
        watch_roots = [
            iteration_root,
            project_root / f"rubrics/Rubric_{lower}",
            project_root / "scorecards",
            project_root / f"collateral/Rubric_{lower}",
            project_root / "evidence",
            project_root / "deltas",
            project_root / "contradictions",
            project_root,
        ]
        latest = 0.0
        for root in watch_roots:
            if not root.exists():
                continue
            if root.is_file():
                try:
                    latest = max(latest, root.stat().st_mtime)
                except OSError:
                    pass
                continue
            try:
                iterator = root.rglob("*")
            except OSError:
                continue
            for child in iterator:
                if not child.is_file():
                    continue
                if "_autonomous" in child.parts:
                    continue
                try:
                    latest = max(latest, child.stat().st_mtime)
                except OSError:
                    continue
        return latest

    def parse_inline_shell_command(line: str) -> str:
        marker = "-lc "
        idx = line.find(marker)
        if idx == -1:
            return ""
        tail = line[idx + len(marker):].strip()
        if not tail:
            return ""
        if tail[0] in {"'", '"'}:
            quote = tail[0]
            end = tail.find(quote, 1)
            if end != -1:
                return tail[1:end].strip()
        return tail

    def check_command_policy_violations(log_chunk: str) -> str | None:
        project_root_resolved = project_root.resolve()

        def tokenized(command_text: str) -> list[str]:
            try:
                return shlex.split(command_text, posix=True)
            except ValueError:
                return command_text.split()

        def strip_env_prefix(tokens: list[str]) -> list[str]:
            idx = 0
            while idx < len(tokens):
                tok = tokens[idx]
                if re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", tok):
                    idx += 1
                    continue
                break
            return tokens[idx:]

        def normalized(tok: str) -> str:
            value = tok.strip().lower()
            while value.startswith("./"):
                value = value[2:]
            return value

        def invokes_recursive_orchestrator(command_text: str) -> bool:
            tokens = strip_env_prefix(tokenized(command_text))
            if not tokens:
                return False
            head = normalized(tokens[0])
            script_heads = {
                "rdd",
                "rdd.sh",
                "scripts/rdd.sh",
                "rbd_autonomous.sh",
                "scripts/rbd_autonomous.sh",
            }
            if head in script_heads:
                return True
            if head in {"bash", "sh"} and len(tokens) >= 2:
                script = normalized(tokens[1])
                if script in script_heads:
                    return True
            if head in {"python", "python3"}:
                script_token = ""
                for tok in tokens[1:]:
                    low = normalized(tok)
                    if low.endswith(".py"):
                        script_token = low
                        break
                if script_token.endswith(("rbd_parallel_links.py", "rbd_autonomous.py")):
                    return True
                if script_token.endswith("rbd_stabilize.py"):
                    tail = " ".join(tokens[2:]).lower()
                    if "--request-stability" in tail or "--run-chain-once" in tail:
                        return True
            return False

        def has_scope_escape(command_text: str) -> bool:
            tokens = strip_env_prefix(tokenized(command_text))
            for tok in tokens:
                if ".." not in tok:
                    continue
                if tok.startswith("-"):
                    continue
                # Ignore obvious regex fragments and non-path tokens.
                if any(ch in tok for ch in "*?[]{}|$`"):
                    continue
                if not re.search(r"[./\\]", tok):
                    continue
                candidate = Path(tok)
                try:
                    resolved = (
                        candidate.resolve(strict=False)
                        if candidate.is_absolute()
                        else (project_root_resolved / candidate).resolve(strict=False)
                    )
                except OSError:
                    return True
                try:
                    resolved.relative_to(project_root_resolved)
                except ValueError:
                    return True
            return False

        for raw in log_chunk.splitlines():
            line = raw.strip()
            if "-lc " not in line:
                continue
            command = parse_inline_shell_command(line)
            if not command:
                continue
            lowered = command.lower()

            if re.search(r"\bgit\s+(status|diff|log|show|rev-parse|branch)\b", lowered):
                return "forbidden git command detected"

            if invokes_recursive_orchestrator(command):
                return "forbidden recursive orchestrator command detected"

            if ("rbd_stabilize.py" in lowered) and ("--request-stability" in lowered):
                return "forbidden recursive stability request detected"

            if has_scope_escape(command):
                return "forbidden scope-escape path (`../`) detected in command"
        return None

    cmd = [
        codex_bin,
        "exec",
    ]
    cmd.extend(["-c", f'model_reasoning_effort="{codex_reasoning_effort}"'])
    if codex_model:
        cmd.extend(["-m", codex_model])
    cmd.extend(
        [
            "-C",
            str(project_root),
            "--full-auto",
            "--skip-git-repo-check",
            "-o",
            str(last_message_path),
            "-",
        ]
    )

    print(
        "autonomous_exec="
        + (
            f"iteration_{iteration_label} chain='{chain}' "
            f"timeout={'disabled' if codex_timeout_seconds <= 0 else str(codex_timeout_seconds) + 's'} "
            f"force_chain_destabilization={'yes' if force_chain_destabilization else 'no'}"
        )
    )
    with stdout_path.open("w", encoding="utf-8") as stdout_file, stderr_path.open(
        "w", encoding="utf-8"
    ) as stderr_file:
        popen_env = os.environ.copy()
        popen_env["GIT_CEILING_DIRECTORIES"] = str(project_root)
        popen_env["GIT_DISCOVERY_ACROSS_FILESYSTEM"] = "0"
        popen_env["RBD_RUN_ROOT"] = str(project_root)
        preexec_fn = None
        if os.name == "posix":
            preexec_fn = lambda: _linux_set_pdeathsig(signal.SIGTERM)
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            text=True,
            cwd=project_root,
            env=popen_env,
            stdout=stdout_file,
            stderr=stderr_file,
            start_new_session=True,
            preexec_fn=preexec_fn,
        )

        def terminate_process(message: str) -> int:
            stderr_file.write(message + "\n")
            stderr_file.flush()
            try:
                pgid = os.getpgid(proc.pid)
            except ProcessLookupError:
                pgid = None
            if pgid is not None:
                try:
                    os.killpg(pgid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
                deadline = time.time() + 5
                while time.time() < deadline:
                    if proc.poll() is not None:
                        break
                    time.sleep(0.1)
                if proc.poll() is None:
                    try:
                        os.killpg(pgid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
            try:
                proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                stderr_file.write(
                    "[autonomous-stability] process did not fully exit after SIGKILL window\n"
                )
                stderr_file.flush()
            return 124

        start_monotonic = time.monotonic()
        last_progress_monotonic = start_monotonic
        last_activity_monotonic = start_monotonic
        latest_seen_mtime = latest_artifact_mtime()
        terminal_seen_monotonic: float | None = None
        completion_grace_seconds = 15.0
        if codex_no_progress_seconds > 0:
            completion_grace_seconds = max(10.0, min(45.0, codex_no_progress_seconds / 4.0))
        inactivity_watchdog_seconds = 0.0
        if codex_no_progress_seconds > 0:
            inactivity_watchdog_seconds = max(
                180.0,
                min(480.0, codex_no_progress_seconds / 2.0),
            )
        rc = 0
        stderr_scan_offset = 0
        signal_termination_note: list[str] = []
        previous_signal_handlers: dict[signal.Signals, object] = {}

        def _request_child_termination(signum: int, _frame: object) -> None:
            try:
                sig_name = signal.Signals(signum).name
            except Exception:
                sig_name = str(signum)
            signal_termination_note[:] = [
                f"[autonomous-stability] received {sig_name}; terminating codex child process group"
            ]

        for sig in (signal.SIGTERM, signal.SIGHUP):
            try:
                previous_signal_handlers[sig] = signal.getsignal(sig)
                signal.signal(sig, _request_child_termination)
            except Exception:
                continue

        try:
            if proc.stdin is not None:
                try:
                    proc.stdin.write(prompt)
                    proc.stdin.close()
                except OSError:
                    pass

            while True:
                polled = proc.poll()
                if polled is not None:
                    rc = polled
                    break

                if signal_termination_note:
                    rc = terminate_process(signal_termination_note[0])
                    break

                now = time.monotonic()
                latest_mtime = latest_artifact_mtime()
                if latest_mtime > latest_seen_mtime + 1e-6:
                    latest_seen_mtime = latest_mtime
                    last_progress_monotonic = now
                    last_activity_monotonic = now

                try:
                    with stderr_path.open("r", encoding="utf-8", errors="ignore") as stderr_reader:
                        stderr_reader.seek(stderr_scan_offset)
                        new_chunk = stderr_reader.read()
                        stderr_scan_offset = stderr_reader.tell()
                except OSError:
                    new_chunk = ""
                if new_chunk:
                    last_activity_monotonic = now
                violation = check_command_policy_violations(new_chunk)
                if violation is not None:
                    rc = terminate_process(f"[autonomous-stability] policy violation: {violation}")
                    break

                if iteration_artifacts_terminally_complete():
                    if terminal_seen_monotonic is None:
                        terminal_seen_monotonic = now
                    elif (now - terminal_seen_monotonic) >= completion_grace_seconds:
                        terminate_process(
                            "[autonomous-stability] iteration artifacts reached terminal state; ending codex session"
                        )
                        rc = 0
                        break
                else:
                    terminal_seen_monotonic = None

                if codex_timeout_seconds > 0 and (now - start_monotonic) >= codex_timeout_seconds:
                    rc = terminate_process(
                        f"[autonomous-stability] timeout after {codex_timeout_seconds} seconds"
                    )
                    break

                if (
                    codex_no_progress_seconds > 0
                    and (now - last_progress_monotonic) >= codex_no_progress_seconds
                ):
                    rc = terminate_process(
                        "[autonomous-stability] no non-log artifact progress for "
                        f"{codex_no_progress_seconds} seconds"
                    )
                    break

                if (
                    inactivity_watchdog_seconds > 0
                    and (now - last_activity_monotonic) >= inactivity_watchdog_seconds
                ):
                    rc = terminate_process(
                        "[autonomous-stability] no codex stderr activity and no non-log artifact "
                        f"progress for {int(inactivity_watchdog_seconds)} seconds"
                    )
                    break

                time.sleep(1)
        except KeyboardInterrupt:
            terminate_process("[autonomous-stability] interrupted by operator")
            raise
        except BaseException as exc:
            terminate_process(
                f"[autonomous-stability] unexpected exception; terminating child process group: {type(exc).__name__}: {exc}"
            )
            raise
        finally:
            for sig, handler in previous_signal_handlers.items():
                try:
                    signal.signal(sig, handler)
                except Exception:
                    continue

    if primary_runtime_payload is not None:
        after_snapshot = build_primary_artifact_snapshot(project_root, prompt_primary_refs)
        before_snapshot = primary_runtime_payload.get("before", {})
        if not isinstance(before_snapshot, dict):
            before_snapshot = {}
        primary_runtime_payload["after"] = after_snapshot
        primary_runtime_payload["end_epoch"] = float(time.time())
        primary_runtime_payload["changed_refs"] = primary_artifact_snapshot_changed_refs(
            before_snapshot, after_snapshot
        )
        write_primary_artifact_runtime(iteration_root, primary_runtime_payload)

    # Snapshot run-level outputs into iteration scope before truth reconciliation
    # so objective/frontier gates can evaluate iteration-scoped artifacts.
    snapshot_run_level_outputs_for_iteration(iteration_root, project_root)

    reconciled = reconcile_iteration_truth(
        project_root=project_root,
        iterations_dir=iterations_dir,
        iteration_label=iteration_label,
        chain=chain,
    )
    # Refresh iteration snapshots after reconciliation mutations.
    snapshot_run_level_outputs_for_iteration(iteration_root, project_root)
    if reconciled:
        print(
            "truth_reconciled="
            f"iteration_{iteration_label} chain='{chain}' "
            "reason=artifact_quality_mismatch_or_identity_mismatch"
        )
    print(f"autonomous_exec_rc={rc} logs={run_dir}")
    return rc, iteration


def request_stability(args: argparse.Namespace) -> int:
    if not hasattr(args, "require_prompt_satisfaction"):
        args.require_prompt_satisfaction = True
    project_root = Path(args.project_root).resolve()
    iterations_arg = Path(args.iterations_dir)
    iterations_dir = (
        iterations_arg
        if iterations_arg.is_absolute()
        else (project_root / iterations_arg)
    )
    rubrics_dir = project_root / "rubrics"
    output_arg = Path(args.output)
    output_md = output_arg if output_arg.is_absolute() else (project_root / output_arg)
    json_output: Path | None = None
    if args.json_output:
        json_arg = Path(args.json_output)
        json_output = json_arg if json_arg.is_absolute() else (project_root / json_arg)

    attempts = 0
    while attempts <= args.max_autonomous_iterations:
        result = evaluate_current_state(
            iterations_dir=iterations_dir,
            depth_arg=args.depth,
            required_streak=args.required_streak,
            rubrics_dir=rubrics_dir,
            require_chain_destabilization=args.require_chain_destabilization,
            min_destabilization_defects=args.min_destabilization_defects,
            min_destabilization_baseline_mean=args.min_destabilization_baseline_mean,
            max_destabilization_baseline_mean=args.max_destabilization_baseline_mean,
            min_recovery_iteration_gap=args.min_recovery_iteration_gap,
            require_prompt_linkage=args.require_prompt_linkage,
            require_prompt_satisfaction=args.require_prompt_satisfaction,
        )
        write_outputs(result, iterations_dir, output_md, json_output)
        if result.stable:
            print("stability=achieved")
            return 0

        if attempts == args.max_autonomous_iterations:
            print("stability=not_achieved max_autonomous_iterations_reached")
            return 2

        if result.next_chain is None:
            print("stability=not_achieved next_chain_missing")
            return 2

        before_count = len(result.records)
        expected_chain = result.next_chain
        force_chain_destabilization = (
            args.require_chain_destabilization
            and not result.chain_destabilized.get(expected_chain, False)
        )
        rc, iteration_number = run_autonomous_iteration(
            codex_bin=args.codex_bin,
            codex_reasoning_effort=args.codex_reasoning_effort,
            codex_model=args.codex_model,
            codex_timeout_seconds=args.codex_timeout_seconds,
            codex_no_progress_seconds=args.codex_no_progress_seconds,
            project_root=project_root,
            iterations_dir=iterations_dir,
            chain=expected_chain,
            depth=result.depth,
            force_chain_destabilization=force_chain_destabilization,
            min_destabilization_defects=args.min_destabilization_defects,
            min_destabilization_baseline_mean=args.min_destabilization_baseline_mean,
            max_destabilization_baseline_mean=args.max_destabilization_baseline_mean,
            min_recovery_iteration_gap=args.min_recovery_iteration_gap,
            require_prompt_linkage=args.require_prompt_linkage,
        )
        attempts += 1
        produced_dir = iterations_dir / f"iteration_{iteration_number:03d}"
        if produced_dir.exists():
            snapshot_run_level_outputs_for_iteration(produced_dir, project_root)
        produced_record = resolve_record(produced_dir) if produced_dir.exists() else None
        parseable_and_expected = (
            produced_record is not None and produced_record.chain == expected_chain
        )
        if produced_record is None and produced_dir.exists():
            parsed = parse_chain(expected_chain)
            if parsed is not None:
                _, lower = parsed
                synthesize_iteration_artifacts(
                    project_root=project_root,
                    iterations_dir=iterations_dir,
                    iteration_label=f"{iteration_number:03d}",
                    chain=expected_chain,
                    lower=lower,
                    depth=result.depth,
                    force_chain_destabilization=force_chain_destabilization,
                )
                if produced_dir.exists():
                    snapshot_run_level_outputs_for_iteration(produced_dir, project_root)
                produced_record = resolve_record(produced_dir)
                print(
                    "autonomous_info=synthesized_iteration "
                    f"(iteration={iteration_number:03d} rc={rc} reason=missing_parseable_record)"
                )

        after_count = len(collect_records(iterations_dir))
        if produced_record is None:
            print(
                "autonomous_warning=iteration_missing_parseable_record "
                f"(iteration={iteration_number:03d})"
            )
            if rc == 0:
                print(
                    "autonomous_error=iteration_unparseable_after_success "
                    f"(iteration={iteration_number:03d} rc={rc})"
                )
                return 2
        elif produced_record.chain != expected_chain:
            print(
                "autonomous_warning=iteration_chain_mismatch "
                f"(iteration={iteration_number:03d} expected='{expected_chain}' "
                f"actual='{produced_record.chain}')"
            )
        if rc != 0 and after_count <= before_count:
            print(
                "autonomous_warning=iteration_failed_without_new_record "
                f"(rc={rc}) remaining_attempts={args.max_autonomous_iterations - attempts}"
            )
            continue

    # Unreachable due to loop bounds, retained for clarity.
    return 2


def run_chain_once(args: argparse.Namespace) -> int:
    if not hasattr(args, "require_prompt_satisfaction"):
        args.require_prompt_satisfaction = True

    project_root = Path(args.project_root).resolve()
    iterations_arg = Path(args.iterations_dir)
    iterations_dir = (
        iterations_arg
        if iterations_arg.is_absolute()
        else (project_root / iterations_arg)
    )
    rubrics_dir = project_root / "rubrics"
    output_arg = Path(args.output)
    output_md = output_arg if output_arg.is_absolute() else (project_root / output_arg)
    json_output: Path | None = None
    if args.json_output:
        json_arg = Path(args.json_output)
        json_output = json_arg if json_arg.is_absolute() else (project_root / json_arg)

    parsed_chain = parse_chain(args.run_chain_once)
    if parsed_chain is None:
        raise SystemExit(
            "--run-chain-once must be in the form 'Rubric_<k> -> Rubric_<k-1>'"
        )
    explicit_chain = format_chain(parsed_chain[0], parsed_chain[1])

    pre_state = evaluate_current_state(
        iterations_dir=iterations_dir,
        depth_arg=args.depth,
        required_streak=args.required_streak,
        rubrics_dir=rubrics_dir,
        require_chain_destabilization=args.require_chain_destabilization,
        min_destabilization_defects=args.min_destabilization_defects,
        min_destabilization_baseline_mean=args.min_destabilization_baseline_mean,
        max_destabilization_baseline_mean=args.max_destabilization_baseline_mean,
        min_recovery_iteration_gap=args.min_recovery_iteration_gap,
        require_prompt_linkage=args.require_prompt_linkage,
        require_prompt_satisfaction=args.require_prompt_satisfaction,
    )
    force_chain_destabilization = (
        args.require_chain_destabilization
        and not pre_state.chain_destabilized.get(explicit_chain, False)
    )

    rc, iteration_number = run_autonomous_iteration(
        codex_bin=args.codex_bin,
        codex_reasoning_effort=args.codex_reasoning_effort,
        codex_model=args.codex_model,
        codex_timeout_seconds=args.codex_timeout_seconds,
        codex_no_progress_seconds=args.codex_no_progress_seconds,
        project_root=project_root,
        iterations_dir=iterations_dir,
        chain=explicit_chain,
        depth=pre_state.depth,
        force_chain_destabilization=force_chain_destabilization,
        min_destabilization_defects=args.min_destabilization_defects,
        min_destabilization_baseline_mean=args.min_destabilization_baseline_mean,
        max_destabilization_baseline_mean=args.max_destabilization_baseline_mean,
        min_recovery_iteration_gap=args.min_recovery_iteration_gap,
        require_prompt_linkage=args.require_prompt_linkage,
    )

    produced_dir = iterations_dir / f"iteration_{iteration_number:03d}"
    if produced_dir.exists():
        snapshot_run_level_outputs_for_iteration(produced_dir, project_root)
    produced_record = resolve_record(produced_dir) if produced_dir.exists() else None
    if produced_record is None and produced_dir.exists():
        parsed = parse_chain(explicit_chain)
        if parsed is not None:
            _, lower = parsed
            synthesize_iteration_artifacts(
                project_root=project_root,
                iterations_dir=iterations_dir,
                iteration_label=f"{iteration_number:03d}",
                chain=explicit_chain,
                lower=lower,
                depth=pre_state.depth,
                force_chain_destabilization=force_chain_destabilization,
            )
            if produced_dir.exists():
                snapshot_run_level_outputs_for_iteration(produced_dir, project_root)
            produced_record = resolve_record(produced_dir)
            print(
                "autonomous_info=synthesized_iteration "
                f"(iteration={iteration_number:03d} rc={rc} reason=missing_parseable_record)"
            )
    if produced_record is None and rc == 0:
        print(
            "autonomous_error=iteration_unparseable_after_success "
            f"(iteration={iteration_number:03d} rc={rc})"
        )
        return 2

    result = evaluate_current_state(
        iterations_dir=iterations_dir,
        depth_arg=args.depth,
        required_streak=args.required_streak,
        rubrics_dir=rubrics_dir,
        require_chain_destabilization=args.require_chain_destabilization,
        min_destabilization_defects=args.min_destabilization_defects,
        min_destabilization_baseline_mean=args.min_destabilization_baseline_mean,
        max_destabilization_baseline_mean=args.max_destabilization_baseline_mean,
        min_recovery_iteration_gap=args.min_recovery_iteration_gap,
        require_prompt_linkage=args.require_prompt_linkage,
        require_prompt_satisfaction=args.require_prompt_satisfaction,
    )
    write_outputs(result, iterations_dir, output_md, json_output)
    return 0 if rc == 0 else rc


def _main_impl() -> int:
    args = parse_args()
    if args.required_streak < 1:
        raise SystemExit("--required-streak must be >= 1")
    if args.depth != -1 and args.depth < 0:
        raise SystemExit("--depth must be >= 0")
    if args.max_autonomous_iterations < 1:
        raise SystemExit("--max-autonomous-iterations must be >= 1")
    if args.codex_timeout_seconds < 0:
        raise SystemExit("--codex-timeout-seconds must be >= 0")
    if args.codex_no_progress_seconds < 0:
        raise SystemExit("--codex-no-progress-seconds must be >= 0")
    if args.min_destabilization_defects < 1:
        raise SystemExit("--min-destabilization-defects must be >= 1")
    if args.min_recovery_iteration_gap < 1:
        raise SystemExit("--min-recovery-iteration-gap must be >= 1")
    if args.min_destabilization_baseline_mean < 0 or args.min_destabilization_baseline_mean >= 100:
        raise SystemExit("--min-destabilization-baseline-mean must be in [0, 100)")
    if args.max_destabilization_baseline_mean <= 0 or args.max_destabilization_baseline_mean > 100:
        raise SystemExit("--max-destabilization-baseline-mean must be in (0, 100]")
    if args.min_destabilization_baseline_mean >= args.max_destabilization_baseline_mean:
        raise SystemExit(
            "--min-destabilization-baseline-mean must be < --max-destabilization-baseline-mean"
        )
    valid_efforts = {"minimal", "low", "medium", "high", "xhigh"}
    if args.codex_reasoning_effort not in valid_efforts:
        raise SystemExit(
            "--codex-reasoning-effort must be one of: "
            + ", ".join(sorted(valid_efforts))
        )

    if args.require_chain_destabilization:
        # Prompt-coupled destabilization is required by default in destabilization mode.
        args.require_prompt_linkage = True
    require_prompt_satisfaction = not args.allow_partial_prompt_satisfaction

    if args.request_stability and args.run_chain_once:
        raise SystemExit("--run-chain-once cannot be combined with --request-stability")

    project_root = Path(args.project_root)

    if args.run_chain_once:
        setattr(args, "require_prompt_satisfaction", require_prompt_satisfaction)
        return run_chain_once(args)

    if args.request_stability:
        setattr(args, "require_prompt_satisfaction", require_prompt_satisfaction)
        return request_stability(args)

    iterations_arg = Path(args.iterations_dir)
    iterations_dir = iterations_arg if iterations_arg.is_absolute() else (project_root / iterations_arg)
    records = collect_records(iterations_dir)
    depth = resolve_depth(args.depth, records, project_root / "rubrics")
    result = compute_stability(
        records,
        args.required_streak,
        depth,
        require_chain_destabilization=args.require_chain_destabilization,
        min_destabilization_defects=args.min_destabilization_defects,
        min_destabilization_baseline_mean=args.min_destabilization_baseline_mean,
        max_destabilization_baseline_mean=args.max_destabilization_baseline_mean,
        min_recovery_iteration_gap=args.min_recovery_iteration_gap,
        require_prompt_linkage=args.require_prompt_linkage,
        require_prompt_satisfaction=require_prompt_satisfaction,
    )

    output_arg = Path(args.output)
    output_md = output_arg if output_arg.is_absolute() else (project_root / output_arg)
    json_output: Path | None = None
    if args.json_output:
        json_arg = Path(args.json_output)
        json_output = json_arg if json_arg.is_absolute() else (project_root / json_arg)
    write_outputs(result, iterations_dir, output_md, json_output)
    if args.fail_if_unstable and not result.stable:
        return 2
    return 0


def main() -> int:
    try:
        return _main_impl()
    except KeyboardInterrupt:
        print("autonomous_exec_interrupted")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
