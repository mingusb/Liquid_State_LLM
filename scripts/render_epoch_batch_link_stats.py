#!/usr/bin/env python3
"""Render per-epoch parallel-link stats with explicit LSM edge-of-chaos evidence."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


EPOCH_DIR_RE = re.compile(r"^epoch_(\d+)$")
RESUME_DIR_RE = re.compile(r"^parallel_epochs_resume_(\d+)$")
ITER_DIR_RE = re.compile(r"^iteration_(\d+)$")
CHAIN_LINE_RE = re.compile(r"^- (?P<chain>Rubric_\d+ -> Rubric_\d+): (?P<kv>.+)$")
KV_PAIR_RE = re.compile(r"([a-zA-Z_]+)=([^,]+)(?:,|$)")
OLD_MERGED_LINE_RE = re.compile(
    r"^- chain=(?P<chain>.+?) source_iteration=(?P<src>\d+) merged_iteration=(?P<dst>\d+)$"
)


@dataclass(frozen=True)
class EpochRef:
    phase_name: str
    phase_sort: tuple[int, int]
    phase_epoch: int
    summary_path: Path


@dataclass
class WorkerRow:
    chain: str
    decision: str
    attempts: int
    non_merge_reason: str
    worker_iteration: str
    baseline_mean: float | None
    recheck_mean: float | None
    delta_pp: float | None
    baseline_blocking: int | None
    recheck_blocking: int | None
    baseline_defects: int | None
    recheck_defects: int | None
    liquid_state_phase: str
    prompt_satisfaction: str
    identity_lock: str
    edge_band_ok: str
    destabilization_ok: str
    quality_perfect: str
    merged: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render epoch batch link stats with LSM evidence columns."
    )
    parser.add_argument("--run-dir", required=True, help="Run directory path.")
    parser.add_argument(
        "--output",
        default="scorecards/EPOCH_BATCH_LINK_STATS.md",
        help="Output markdown path.",
    )
    return parser.parse_args()


def normalize_scalar(text: str) -> str:
    value = text.strip()
    if value.startswith("`") and value.endswith("`") and len(value) >= 2:
        value = value[1:-1]
    return value.strip()


def parse_float(text: str) -> float | None:
    value = normalize_scalar(text)
    if value.endswith("%"):
        value = value[:-1]
    try:
        return float(value)
    except ValueError:
        return None


def parse_int(text: str) -> int | None:
    value = normalize_scalar(text)
    try:
        return int(value)
    except ValueError:
        return None


def parse_bool_yn(text: str) -> str:
    value = normalize_scalar(text).lower()
    if value in {"yes", "true"}:
        return "YES"
    if value in {"no", "false"}:
        return "NO"
    return "UNK"


def chain_slug(chain: str) -> str:
    return chain.replace(" ", "").replace("->", "_to_")


def parse_phase(root_name: str) -> tuple[str, tuple[int, int]]:
    if root_name == "parallel_epochs":
        return "base", (0, 0)
    match = RESUME_DIR_RE.match(root_name)
    if match:
        idx = int(match.group(1))
        return f"resume{idx}", (1, idx)
    return root_name, (99, 99)


def discover_epochs(run_dir: Path) -> list[EpochRef]:
    refs: list[EpochRef] = []
    for phase_root in sorted(run_dir.glob("parallel_epochs*")):
        if not phase_root.is_dir():
            continue
        phase_name, phase_sort = parse_phase(phase_root.name)
        for epoch_dir in sorted(phase_root.glob("epoch_*")):
            if not epoch_dir.is_dir():
                continue
            match = EPOCH_DIR_RE.match(epoch_dir.name)
            if not match:
                continue
            summary_path = epoch_dir / "SUMMARY.md"
            if not summary_path.exists():
                continue
            refs.append(
                EpochRef(
                    phase_name=phase_name,
                    phase_sort=phase_sort,
                    phase_epoch=int(match.group(1)),
                    summary_path=summary_path,
                )
            )
    refs.sort(key=lambda r: (r.phase_sort, r.phase_epoch))
    return refs


def parse_md_kv(lines: list[str]) -> dict[str, str]:
    kv: dict[str, str] = {}
    for line in lines:
        if not line.startswith("- "):
            continue
        if ":" not in line:
            continue
        key, value = line[2:].split(":", 1)
        kv[key.strip()] = normalize_scalar(value)
    return kv


def parse_workers(lines: list[str]) -> list[dict[str, Any]]:
    workers: list[dict[str, Any]] = []
    in_workers = False
    for raw in lines:
        line = raw.rstrip()
        if line.strip() == "## Workers":
            in_workers = True
            continue
        if in_workers and line.startswith("## "):
            break
        if not in_workers:
            continue
        match = CHAIN_LINE_RE.match(line.strip())
        if not match:
            continue
        chain = match.group("chain").strip()
        kv_raw = match.group("kv").strip()
        entry: dict[str, Any] = {"chain": chain}
        for pair in KV_PAIR_RE.finditer(kv_raw + ","):
            k = pair.group(1).strip()
            v = pair.group(2).strip()
            entry[k] = v
        entry["decision"] = str(entry.get("decision", "UNKNOWN"))
        entry["attempts"] = int(str(entry.get("attempts", "1")))
        entry["non_merge_reason"] = str(entry.get("non_merge_reason", "unknown"))
        workers.append(entry)
    return workers


def parse_merged(lines: list[str], head_kv: dict[str, str]) -> tuple[str, str, str]:
    # New-format first.
    merged_chain = head_kv.get("merged_link_applied", "none")
    merged_src = head_kv.get("merged_source_iteration", "none")
    merged_dst = head_kv.get("merged_destination_iteration", "none")
    if merged_chain != "none":
        return merged_chain, merged_src, merged_dst

    in_merged = False
    for raw in lines:
        line = raw.strip()
        if line == "## Merged" or line == "## Merged Result Applied":
            in_merged = True
            continue
        if in_merged and line.startswith("## "):
            break
        if not in_merged:
            continue
        if line.startswith("- chain="):
            match = OLD_MERGED_LINE_RE.match(line)
            if not match:
                return "none", "none", "none"
            merged_chain = match.group("chain").strip()
            src = f"iteration_{match.group('src')}"
            dst = f"iteration_{match.group('dst')}"
            return merged_chain, src, dst
    return "none", "none", "none"


def parse_decision_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    lines = path.read_text(encoding="utf-8").splitlines()
    return parse_md_kv(lines)


def latest_worker_decision(epoch_dir: Path, chain: str) -> tuple[str, dict[str, str]]:
    worker_root = epoch_dir / "workers" / chain_slug(chain) / "iterations"
    if not worker_root.exists():
        return "missing", {}
    candidates: list[tuple[int, Path]] = []
    for it_dir in worker_root.glob("iteration_*"):
        if not it_dir.is_dir():
            continue
        match = ITER_DIR_RE.match(it_dir.name)
        if not match:
            continue
        decision = it_dir / "judge_recheck" / "FINAL_DECISION.md"
        if decision.exists():
            candidates.append((int(match.group(1)), decision))
    if not candidates:
        return "missing", {}
    candidates.sort(key=lambda t: t[0])
    iter_num, decision_path = candidates[-1]
    return f"iteration_{iter_num:03d}", parse_decision_file(decision_path)


def fmt_float(value: float | None) -> str:
    if value is None:
        return "N/A"
    return f"{value:.1f}"


def fmt_delta(value: float | None) -> str:
    if value is None:
        return "N/A"
    return f"{value:+.1f}"


def yn(value: bool) -> str:
    return "YES" if value else "NO"


def parse_prompt_linked(decision_kv: dict[str, str]) -> bool:
    rationale = decision_kv.get("rationale", "")
    return "prompt-linked" in rationale.lower()


def build_ascii_table(headers: list[str], rows: list[list[str]]) -> str:
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if len(cell) > widths[i]:
                widths[i] = len(cell)

    def border() -> str:
        return "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def render_row(values: list[str]) -> str:
        cells = [f" {v.ljust(widths[i])} " for i, v in enumerate(values)]
        return "|" + "|".join(cells) + "|"

    out = [border(), render_row(headers), border()]
    for row in rows:
        out.append(render_row(row))
    out.append(border())
    return "\n".join(out)


def main() -> int:
    args = parse_args()
    run_dir = Path(args.run_dir).resolve()
    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    status_path = run_dir / "STABILITY_STATUS.json"
    status: dict[str, Any] = {}
    if status_path.exists():
        status = json.loads(status_path.read_text(encoding="utf-8"))

    min_defects = int(status.get("min_destabilization_defects", 3))
    min_base = float(status.get("min_destabilization_baseline_mean", 40.0))
    max_base = float(status.get("max_destabilization_baseline_mean", 95.0))

    epochs = discover_epochs(run_dir)
    header_lines: list[str] = [
        "# Epoch Batch Link Stats (Monospace + LSM Evidence)",
        "",
        f"- run: `{run_dir.name}`",
        f"- epoch_count: `{len(epochs)}`",
        "- epoch_definition: `one parallel optimization batch; at most one update per chain link in that batch`",
        "- lsm_edge_band: "
        f"`baseline_mean in [{min_base:.1f}, {max_base:.1f}] with baseline_total_defects >= {min_defects}`",
        "",
    ]

    body_lines: list[str] = []
    lsm_rows: list[list[str]] = []
    timeline_rows: list[list[str]] = []
    global_epoch = 0
    merged_total = 0
    prior_merged_phase = "START"
    for ref in epochs:
        global_epoch += 1
        summary_lines = ref.summary_path.read_text(encoding="utf-8").splitlines()
        head_kv = parse_md_kv(summary_lines)
        workers = parse_workers(summary_lines)
        merged_chain, merged_src, merged_dst = parse_merged(summary_lines, head_kv)
        if merged_chain != "none":
            merged_total += 1

        next_before = head_kv.get("next_chain_before_batch") or head_kv.get("pre_next_chain") or "none"
        next_after = head_kv.get("next_chain_after_batch") or head_kv.get("post_next_chain") or "none"
        active_chains = head_kv.get("active_chains", "none").replace(" ; ", ", ")

        body_lines.extend(
            [
                f"## E{global_epoch:02d} ({ref.phase_name}:{ref.phase_epoch:02d})",
                "",
                f"- global_epoch: `{global_epoch:02d}`",
                f"- active_chain_set: `{active_chains}`",
                f"- next_chain_before_batch: `{next_before}`",
                f"- next_chain_after_batch: `{next_after}`",
                f"- merged_link_applied: `{merged_chain}`",
                f"- merged_source_iteration: `{merged_src}`",
                f"- merged_destination_iteration: `{merged_dst}`",
                "",
            ]
        )

        table_rows: list[list[str]] = []
        worker_row_objs: dict[str, WorkerRow] = {}
        for worker in workers:
            chain = str(worker["chain"])
            iter_label, decision_kv = latest_worker_decision(ref.summary_path.parent, chain)

            baseline_mean = parse_float(decision_kv.get("baseline_mean", ""))
            recheck_mean = parse_float(decision_kv.get("recheck_mean", ""))
            delta_pp = None
            if baseline_mean is not None and recheck_mean is not None:
                delta_pp = recheck_mean - baseline_mean

            baseline_blocking = parse_int(decision_kv.get("baseline_blocking_defects", ""))
            recheck_blocking = parse_int(decision_kv.get("recheck_blocking_defects", ""))
            baseline_defects = parse_int(decision_kv.get("baseline_total_defects", ""))
            recheck_defects = parse_int(decision_kv.get("recheck_total_defects", ""))

            prompt_satisfaction = parse_bool_yn(decision_kv.get("prompt_satisfaction", ""))
            identity_lock = parse_bool_yn(decision_kv.get("identity_lock", ""))
            liquid_state_phase = normalize_scalar(decision_kv.get("liquid_state_phase", "UNK"))

            in_band = (
                baseline_mean is not None and min_base <= baseline_mean <= max_base
            )
            defects_ok = baseline_defects is not None and baseline_defects >= min_defects
            prompt_linked = parse_prompt_linked(decision_kv)
            destabilization_ok = in_band and defects_ok and prompt_linked

            perfect = (
                recheck_mean is not None
                and recheck_mean >= 100.0
                and (recheck_defects or 0) <= 0
                and (recheck_blocking or 0) <= 0
            )

            merged_flag = "YES" if chain == merged_chain else "NO"

            row = WorkerRow(
                chain=chain,
                decision=str(worker.get("decision", "UNKNOWN")),
                attempts=int(worker.get("attempts", 1)),
                non_merge_reason=str(worker.get("non_merge_reason", "unknown")),
                worker_iteration=iter_label,
                baseline_mean=baseline_mean,
                recheck_mean=recheck_mean,
                delta_pp=delta_pp,
                baseline_blocking=baseline_blocking,
                recheck_blocking=recheck_blocking,
                baseline_defects=baseline_defects,
                recheck_defects=recheck_defects,
                liquid_state_phase=liquid_state_phase,
                prompt_satisfaction=prompt_satisfaction,
                identity_lock=identity_lock,
                edge_band_ok=yn(in_band),
                destabilization_ok=yn(destabilization_ok),
                quality_perfect=yn(perfect),
                merged=merged_flag,
            )
            worker_row_objs[row.chain] = row

            table_rows.append(
                [
                    row.chain,
                    row.worker_iteration,
                    fmt_float(row.baseline_mean),
                    fmt_float(row.recheck_mean),
                    fmt_delta(row.delta_pp),
                    row.decision,
                    str(row.recheck_blocking if row.recheck_blocking is not None else "N/A"),
                    str(row.recheck_defects if row.recheck_defects is not None else "N/A"),
                    row.liquid_state_phase,
                    row.edge_band_ok,
                    row.destabilization_ok,
                    row.quality_perfect,
                    row.merged,
                ]
            )

            lsm_rows.append(
                [
                    f"E{global_epoch:02d}",
                    row.chain,
                    row.liquid_state_phase,
                    row.edge_band_ok,
                    row.destabilization_ok,
                    row.prompt_satisfaction,
                    row.identity_lock,
                    row.quality_perfect,
                ]
            )

        merged_row = worker_row_objs.get(merged_chain)
        merged_phase = merged_row.liquid_state_phase if merged_row is not None else "UNK"
        merged_decision = merged_row.decision if merged_row is not None else "UNKNOWN"
        merged_delta = fmt_delta(merged_row.delta_pp) if merged_row is not None else "N/A"
        merged_destab = merged_row.destabilization_ok if merged_row is not None else "UNK"
        merged_perfect = merged_row.quality_perfect if merged_row is not None else "UNK"
        timeline_rows.append(
            [
                f"E{global_epoch:02d}",
                merged_chain,
                merged_phase,
                merged_decision,
                merged_delta,
                merged_destab,
                merged_perfect,
                f"{prior_merged_phase} -> {merged_phase}",
            ]
        )
        prior_merged_phase = merged_phase

        headers = [
            "LINK",
            "WORKER_ITER",
            "BEFORE",
            "AFTER",
            "DELTA",
            "DECISION",
            "BLK",
            "DEF",
            "LSM_PHASE",
            "EDGE_BAND",
            "DESTAB_OK",
            "PERFECT",
            "MERGED",
        ]
        body_lines.append("```text")
        body_lines.append(build_ascii_table(headers, table_rows))
        body_lines.append("```")
        body_lines.append("")

    summary_headers = [
        "EPOCH",
        "CHAIN",
        "LSM_PHASE",
        "EDGE_BAND",
        "DESTAB_OK",
        "PROMPT_OK",
        "ID_LOCK",
        "PERFECT",
    ]
    lines: list[str] = list(header_lines)
    timeline_headers = [
        "EPOCH",
        "MERGED_LINK",
        "MERGED_PHASE",
        "MERGED_DECISION",
        "MERGED_DELTA",
        "DESTAB_OK",
        "PERFECT",
        "TRANSITION",
    ]
    lines.extend(
        [
            "## LSM State-Transition Timeline (Merged Link Per Epoch)",
            "",
            "```text",
            build_ascii_table(timeline_headers, timeline_rows),
            "```",
            "",
        ]
    )
    lines.extend(body_lines)
    lines.extend(
        [
            "## LSM Evidence Summary",
            "",
            f"- merged_batches: `{merged_total}`",
            f"- final_phase: `{status.get('liquid_state_phase', 'unknown')}`",
            f"- stable: `{'yes' if bool(status.get('stable', False)) else 'no'}`",
            "",
            "```text",
            build_ascii_table(summary_headers, lsm_rows),
            "```",
            "",
        ]
    )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
