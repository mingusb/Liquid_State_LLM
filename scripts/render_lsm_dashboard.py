#!/usr/bin/env python3
"""Render a compact LSM dashboard for a run (single-screen infoviz)."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


EPOCH_DIR_RE = re.compile(r"^epoch_(\d+)$")
RESUME_DIR_RE = re.compile(r"^parallel_epochs_resume_(\d+)$")
ITER_DIR_RE = re.compile(r"^iteration_(\d+)$")
CHAIN_LINE_RE = re.compile(r"^- (?P<chain>Rubric_\d+ -> Rubric_\d+): (?P<kv>.+)$")
KV_PAIR_RE = re.compile(r"([a-zA-Z_]+)=([^,]+)(?:,|$)")
OLD_MERGED_LINE_RE = re.compile(
    r"^- chain=(?P<chain>.+?) source_iteration=(?P<src>\d+) merged_iteration=(?P<dst>\d+)$"
)
CHAIN_RE = re.compile(r"Rubric_(\d+)\s*->\s*Rubric_(\d+)")


@dataclass(frozen=True)
class EpochRef:
    phase_name: str
    phase_sort: tuple[int, int]
    phase_epoch: int
    summary_path: Path


@dataclass
class Cell:
    chain: str
    decision: str
    baseline: float | None
    after: float | None
    delta: float | None
    blocking: int | None
    defects: int | None
    prompt_ok: bool | None
    id_lock: bool | None
    phase: str
    perfect: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render compact LSM dashboard.")
    parser.add_argument("--run-dir", required=True, help="Run directory")
    parser.add_argument(
        "--output",
        default="scorecards/LSM_DASHBOARD.md",
        help="Output markdown path",
    )
    return parser.parse_args()


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
            if summary_path.exists():
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


def normalize_scalar(text: str) -> str:
    value = text.strip()
    if value.startswith("`") and value.endswith("`") and len(value) >= 2:
        value = value[1:-1]
    return value.strip()


def parse_float(text: str | None) -> float | None:
    if not text:
        return None
    value = normalize_scalar(text)
    if value.endswith("%"):
        value = value[:-1]
    try:
        return float(value)
    except ValueError:
        return None


def parse_int(text: str | None) -> int | None:
    if not text:
        return None
    value = normalize_scalar(text)
    try:
        return int(value)
    except ValueError:
        return None


def parse_bool(text: str | None) -> bool | None:
    if not text:
        return None
    value = normalize_scalar(text).lower()
    if value in {"yes", "true"}:
        return True
    if value in {"no", "false"}:
        return False
    return None


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


def parse_workers(lines: list[str]) -> list[dict[str, str]]:
    workers: list[dict[str, str]] = []
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
        entry: dict[str, str] = {"chain": chain}
        for pair in KV_PAIR_RE.finditer(kv_raw + ","):
            entry[pair.group(1).strip()] = pair.group(2).strip()
        workers.append(entry)
    return workers


def chain_slug(chain: str) -> str:
    return chain.replace(" ", "").replace("->", "_to_")


def latest_worker_decision(epoch_dir: Path, chain: str) -> dict[str, str]:
    worker_root = epoch_dir / "workers" / chain_slug(chain) / "iterations"
    if not worker_root.exists():
        return {}
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
        return {}
    candidates.sort(key=lambda t: t[0])
    return parse_md_kv(candidates[-1][1].read_text(encoding="utf-8").splitlines())


def parse_merged(lines: list[str], head_kv: dict[str, str]) -> str:
    merged_chain = head_kv.get("merged_link_applied", "none")
    if merged_chain != "none":
        return merged_chain
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
            if match:
                return match.group("chain").strip()
    return "none"


def chain_order(chains: list[str]) -> list[str]:
    scored: list[tuple[int, int, str]] = []
    for chain in chains:
        match = CHAIN_RE.search(chain)
        if not match:
            continue
        src = int(match.group(1))
        dst = int(match.group(2))
        scored.append((-src, -dst, chain))
    scored.sort()
    return [item[2] for item in scored]


def short_chain(chain: str) -> str:
    match = CHAIN_RE.search(chain)
    if not match:
        return chain
    return f"{match.group(1)}>{match.group(2)}"


def phase_digit(phase: str) -> str:
    match = re.search(r"S(\d+)", phase)
    return match.group(1) if match else "?"


def decision_letter(decision: str) -> str:
    d = decision.upper()
    if d == "ACCEPT":
        return "A"
    if d == "PROVISIONAL_ACCEPT":
        return "P"
    if d == "REJECT":
        return "R"
    return "?"


def mark(cell: Cell) -> str:
    if cell.perfect:
        return "*"
    if cell.prompt_ok is False:
        return "x"
    if cell.blocking is not None and cell.blocking > 0:
        return "!"
    return "."


def cell_code(cell: Cell) -> str:
    after = "NA" if cell.after is None else f"{int(round(cell.after)):02d}"
    return f"{phase_digit(cell.phase)}{decision_letter(cell.decision)}{mark(cell)}{after}"


def state_code(cell: Cell) -> str:
    return f"{phase_digit(cell.phase)}{decision_letter(cell.decision)}{mark(cell)}"


def fmt(v: float | None) -> str:
    if v is None:
        return "N/A"
    return f"{v:.1f}"


def fmt_delta(v: float | None) -> str:
    if v is None:
        return "N/A"
    return f"{v:+.1f}"


def fmt_int(v: float | None) -> str:
    if v is None:
        return "NA"
    return str(int(round(v)))


def fmt_delta_short(v: float | None) -> str:
    if v is None:
        return "NA"
    return f"{int(round(v)):+d}"


def build_ascii_table(headers: list[str], rows: list[list[str]]) -> str:
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    def border() -> str:
        return "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def line(vals: list[str]) -> str:
        cells = [f" {vals[i].ljust(widths[i])} " for i in range(len(vals))]
        return "|" + "|".join(cells) + "|"

    out = [border(), line(headers), border()]
    for row in rows:
        out.append(line(row))
    out.append(border())
    return "\n".join(out)


def main() -> int:
    args = parse_args()
    run_dir = Path(args.run_dir).resolve()
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    status_path = run_dir / "STABILITY_STATUS.json"
    status = json.loads(status_path.read_text(encoding="utf-8")) if status_path.exists() else {}

    epochs = discover_epochs(run_dir)
    chain_set: set[str] = set()
    per_epoch_cells: list[dict[str, Cell]] = []
    merged_chains: list[str] = []

    for ref in epochs:
        lines = ref.summary_path.read_text(encoding="utf-8").splitlines()
        head_kv = parse_md_kv(lines)
        workers = parse_workers(lines)
        merged_chain = parse_merged(lines, head_kv)
        merged_chains.append(merged_chain)

        cells: dict[str, Cell] = {}
        for worker in workers:
            chain = worker.get("chain", "")
            chain_set.add(chain)
            decision_kv = latest_worker_decision(ref.summary_path.parent, chain)
            baseline = parse_float(decision_kv.get("baseline_mean"))
            after = parse_float(decision_kv.get("recheck_mean"))
            delta = (after - baseline) if (after is not None and baseline is not None) else None
            blk = parse_int(decision_kv.get("recheck_blocking_defects"))
            defects = parse_int(decision_kv.get("recheck_total_defects"))
            phase = normalize_scalar(decision_kv.get("liquid_state_phase", "UNK"))
            prompt_ok = parse_bool(decision_kv.get("prompt_satisfaction"))
            id_lock = parse_bool(decision_kv.get("identity_lock"))
            perfect = (
                after is not None
                and after >= 100.0
                and (defects or 0) == 0
                and (blk or 0) == 0
            )
            cells[chain] = Cell(
                chain=chain,
                decision=worker.get("decision", "UNKNOWN"),
                baseline=baseline,
                after=after,
                delta=delta,
                blocking=blk,
                defects=defects,
                prompt_ok=prompt_ok,
                id_lock=id_lock,
                phase=phase,
                perfect=perfect,
            )
        per_epoch_cells.append(cells)

    ordered_chains = chain_order(list(chain_set))

    legend_headers = ["TOKEN", "KIND", "D1", "D2", "D3", "D4"]
    legend_rows = [
        ["[S][D][M]", "cell", "chain code triplet", "", "", ""],
        ["S", "phase", "3 = edge", "4 = train", "5 = reconv", "6 = stable"],
        ["D", "decision", "A = accept", "P = prov", "R = reject", ""],
        ["M", "marker", "* = perfect", "! = block", "x = prompt-miss", ". = other"],
        ["MG", "merged", "link selected", "this epoch", "", ""],
        ["AFT", "merged", "merged-link", "after score", "", ""],
        ["Δ", "merged", "merged-link", "delta", "(after-baseline)", ""],
        ["B", "merged", "merged-link", "blocking defects", "", ""],
        ["D", "merged", "merged-link", "total defects", "", ""],
        ["EX", "example", "5A* = ideal", "4P! = blocked", "4Px = prompt-miss", ""],
    ]
    legend_table = build_ascii_table(legend_headers, legend_rows)

    header_lines: list[str] = [
        "# LSM Dashboard (Narrow)",
        "",
        f"- run: `{run_dir.name}`",
        f"- epochs: `{len(epochs)}`",
        f"- final_phase: `{status.get('liquid_state_phase', 'unknown')}`",
        f"- stable: `{'yes' if bool(status.get('stable', False)) else 'no'}`",
        "",
        "Legend (fixed-width):",
        "```text",
        legend_table,
        "```",
        "",
    ]

    # Chain bottleneck summary stats for footer rows.
    chain_seen: dict[str, int] = {}
    chain_avg_after: dict[str, str] = {}
    chain_perfect: dict[str, int] = {}
    chain_blk_epochs: dict[str, int] = {}
    chain_prompt_no: dict[str, int] = {}
    for chain in ordered_chains:
        chain_cells = [epoch[chain] for epoch in per_epoch_cells if chain in epoch]
        seen = len(chain_cells)
        afters = [c.after for c in chain_cells if c.after is not None]
        avg_after = sum(afters) / len(afters) if afters else None
        perfect_cnt = sum(1 for c in chain_cells if c.perfect)
        blk_epochs = sum(1 for c in chain_cells if (c.blocking or 0) > 0)
        prompt_no = sum(1 for c in chain_cells if c.prompt_ok is False)
        chain_seen[chain] = seen
        chain_avg_after[chain] = fmt(avg_after)
        chain_perfect[chain] = perfect_cnt
        chain_blk_epochs[chain] = blk_epochs
        chain_prompt_no[chain] = prompt_no

    # Unified dashboard table: per-epoch + merged trajectory + bottleneck footer.
    unified_headers = ["ROW"] + [short_chain(c) for c in ordered_chains] + [
        "MG",
        "AFT",
        "Δ",
        "B",
        "D",
    ]
    unified_rows: list[list[str]] = []
    for i, (cells, merged) in enumerate(zip(per_epoch_cells, merged_chains, strict=True), start=1):
        row = [f"E{i:02d}"]
        for chain in ordered_chains:
            cell = cells.get(chain)
            row.append(state_code(cell) if cell is not None else "...")

        merged_cell = cells.get(merged)
        if merged_cell is None:
            row.extend(
                [
                    short_chain(merged) if merged != "none" else "none",
                    "N/A",
                    "NA",
                    "NA",
                    "N/A",
                    "N/A",
                ]
            )
        else:
            row.extend(
                [
                    short_chain(merged),
                    fmt_int(merged_cell.after),
                    fmt_delta_short(merged_cell.delta),
                    str(merged_cell.blocking if merged_cell.blocking is not None else "N/A"),
                    str(merged_cell.defects if merged_cell.defects is not None else "N/A"),
                ]
            )
        unified_rows.append(row)

    unified_rows.append(
        ["Σ_AVG_AFTER"]
        + [chain_avg_after[c] for c in ordered_chains]
        + ["-", "-", "-", "-", "-"]
    )
    unified_rows.append(
        ["Σ_PERFECT"]
        + [str(chain_perfect[c]) for c in ordered_chains]
        + ["-", "-", "-", "-", "-"]
    )
    unified_rows.append(
        ["Σ_BLK_EPOCHS"]
        + [str(chain_blk_epochs[c]) for c in ordered_chains]
        + ["-", "-", "-", "-", "-"]
    )
    unified_rows.append(
        ["Σ_PROMPT_NO"]
        + [str(chain_prompt_no[c]) for c in ordered_chains]
        + ["-", "-", "-", "-", "-"]
    )
    unified_rows.append(
        ["Σ_SEEN"]
        + [str(chain_seen[c]) for c in ordered_chains]
        + ["-", "-", "-", "-", "-"]
    )

    table_text = build_ascii_table(unified_headers, unified_rows)
    max_line = max(len(line) for line in table_text.splitlines()) if table_text else 0

    out: list[str] = []
    out.extend(header_lines)
    out.append(f"- max_table_line_chars: `{max_line}`")
    out.append("")
    out.extend(
        [
            "## Unified LSM Table",
            "",
            "```text",
            table_text,
            "```",
            "",
        ]
    )

    output.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
