#!/usr/bin/env python3
"""Render all rubric layers for a run as readable ASCII tables."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path


RUBRIC_INDEX_RE = re.compile(r"(?:Rubric_|R)(\d+)")
ITERATION_RE = re.compile(r"(?:iteration|cycle)_(\d+)")
PERCENT_RE = re.compile(r"(-?\d+(?:\.\d+)?)\s*%")


@dataclass
class LayerRubric:
    layer: int
    iteration: str
    target: str
    x_axis: list[str]
    y_axis: list[str]
    x_axis_specs: list[dict]
    y_axis_specs: list[dict]
    matrix: list[list[float | None]]
    layer_mean: float | None
    gate: str
    source_path: Path
    source_mode: str


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Pretty print all rubric layers from a run directory."
    )
    p.add_argument("--run-dir", required=True, help="Run directory path")
    p.add_argument(
        "--output",
        default="",
        help="Output markdown file path (default: <run-dir>/RUBRICS_PRETTY_PRINT.md)",
    )
    p.add_argument(
        "--iteration",
        "--cycle",
        dest="iteration",
        default="latest",
        help='Iteration id to render (e.g. "001"), or "latest" (default). `--cycle` is accepted as a legacy alias.',
    )
    p.add_argument(
        "--chunk-size",
        type=int,
        default=6,
        help="Max number of X-axis dimensions per rendered grid chunk (default: 6)",
    )
    return p.parse_args()


def now_utc() -> str:
    return (
        dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def mean(values: list[float | None]) -> float | None:
    nums = [v for v in values if v is not None]
    if not nums:
        return None
    return sum(nums) / len(nums)


def fmt_percent(value: float | None) -> str:
    if value is None:
        return "N/A"
    rounded = round(value, 4)
    if abs(rounded - round(rounded)) < 1e-9:
        return f"{int(round(rounded))}%"
    return f"{rounded:.1f}%"


def parse_percent(text: str) -> float | None:
    m = PERCENT_RE.search(text)
    if not m:
        return None
    return float(m.group(1))


def extract_layer(path: Path) -> int | None:
    # Prefer the closest rubric token to the file itself. This avoids
    # mislabeling nested worker paths such as
    # .../workers/Rubric_1_to_Rubric_0/rubrics/Rubric_0/iteration_007.json
    # where the worker directory appears earlier than the actual rubric folder.
    for part in reversed(path.parts):
        m = RUBRIC_INDEX_RE.search(part)
        if m:
            return int(m.group(1))
    return None


def extract_iteration(path: Path) -> str | None:
    m = ITERATION_RE.search(path.as_posix())
    if not m:
        return None
    return m.group(1)


def parse_meta_value(lines: list[str], key: str) -> str | None:
    needle = f"- {key}:"
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith(needle):
            continue
        value = stripped[len(needle) :].strip()
        if value.startswith("`") and value.endswith("`") and len(value) >= 2:
            value = value[1:-1]
        return value
    return None


def scorecard_block(lines: list[str]) -> list[str]:
    start = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "Y \\ X" in line:
            start = i
            break
    if start < 0:
        raise ValueError("missing scorecard table with 'Y \\ X' header")

    block: list[str] = []
    for i in range(start, len(lines)):
        stripped = lines[i].strip()
        if not stripped.startswith("|"):
            break
        block.append(stripped)
    if len(block) < 3:
        raise ValueError("scorecard table is incomplete")
    return block


def parse_markdown_row(row_line: str) -> list[str]:
    inner = row_line.strip().strip("|")
    return [cell.strip() for cell in inner.split("|")]


def load_scorecard(path: Path) -> LayerRubric:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    layer = extract_layer(path)
    if layer is None:
        raise ValueError(f"could not infer layer from {path}")
    iteration = extract_iteration(path) or "unknown"
    target = parse_meta_value(lines, "target") or "(unknown target)"
    gate = (
        parse_meta_value(lines, "gate_result")
        or parse_meta_value(lines, "hard_gate_status")
        or "(unknown)"
    )

    layer_mean_line = parse_meta_value(lines, "layer_mean")
    layer_mean = parse_percent(layer_mean_line or "")

    block = scorecard_block(lines)
    header = parse_markdown_row(block[0])
    if len(header) < 4:
        raise ValueError(f"malformed header in {path}")
    x_axis = header[1:-1]

    y_axis: list[str] = []
    matrix: list[list[float | None]] = []

    for row_line in block[2:]:
        row = parse_markdown_row(row_line)
        if len(row) < len(header):
            continue
        row_name = row[0]
        if row_name.lower() == "column mean":
            continue
        y_axis.append(row_name)
        scores = [parse_percent(cell) for cell in row[1 : 1 + len(x_axis)]]
        matrix.append(scores)

    if layer_mean is None:
        layer_mean = mean([v for r in matrix for v in r])

    return LayerRubric(
        layer=layer,
        iteration=iteration,
        target=target,
        x_axis=x_axis,
        y_axis=y_axis,
        x_axis_specs=[],
        y_axis_specs=[],
        matrix=matrix,
        layer_mean=layer_mean,
        gate=gate,
        source_path=path,
        source_mode="scorecards",
    )


def load_rubric_json(path: Path) -> LayerRubric:
    data = json.loads(path.read_text(encoding="utf-8"))
    layer = extract_layer(path)
    if layer is None:
        raw_layer = str(data.get("layer", f"Rubric_{data.get('rubric_index', 0)}"))
        m = RUBRIC_INDEX_RE.search(raw_layer)
        if m:
            layer = int(m.group(1))
        elif isinstance(data.get("rubric_index"), int):
            layer = int(data["rubric_index"])
        else:
            raise ValueError(f"could not infer layer from {path}")

    iteration = str(data.get("iteration") or data.get("cycle") or extract_iteration(path) or "unknown")
    target = str(data.get("target", "(unknown target)"))
    x_axis = [str(x) for x in data.get("x_axis", [])]
    y_axis = [str(y) for y in data.get("y_axis", [])]
    x_axis_specs = list(data.get("x_axis_specs", []) or [])
    y_axis_specs = list(data.get("y_axis_specs", []) or [])

    cells = data.get("cells", [])

    def norm(text: str) -> str:
        return re.sub(r"[^a-z0-9]+", "", text.lower())

    x_exact = {x: x for x in x_axis}
    x_norm = {norm(x): x for x in x_axis}
    role_id_to_x: dict[str, str] = {}
    for x in x_axis:
        m = re.match(r"^(R\d+)\b", x)
        if m:
            role_id_to_x[m.group(1)] = x

    y_exact = {y: y for y in y_axis}
    y_norm = {norm(y): y for y in y_axis}

    def resolve_x_list(cell: dict) -> list[str]:
        raw_x = str(cell.get("x", "")).strip()
        if raw_x:
            if raw_x in x_exact:
                return [x_exact[raw_x]]
            if norm(raw_x) in x_norm:
                return [x_norm[norm(raw_x)]]
            if re.fullmatch(r"R\d+(?:-R\d+)+", raw_x):
                hits = []
                for token in raw_x.split("-"):
                    resolved = role_id_to_x.get(token) or x_exact.get(token) or x_norm.get(norm(token))
                    if resolved:
                        hits.append(resolved)
                if hits:
                    # Preserve source order while removing duplicates.
                    return list(dict.fromkeys(hits))
            resolved = role_id_to_x.get(raw_x) or x_exact.get(raw_x) or x_norm.get(norm(raw_x))
            if resolved:
                return [resolved]

        cell_label = str(cell.get("cell", "")).strip()
        if "|" in cell_label:
            left = cell_label.split("|", 1)[0].strip()
            resolved = role_id_to_x.get(left) or x_exact.get(left) or x_norm.get(norm(left))
            if resolved:
                return [resolved]
        return []

    def resolve_y(cell: dict) -> str | None:
        raw_y = str(cell.get("y", "")).strip()
        if raw_y:
            if raw_y in y_exact:
                return y_exact[raw_y]
            hit = y_norm.get(norm(raw_y))
            if hit:
                return hit

        cell_label = str(cell.get("cell", "")).strip()
        if "|" in cell_label:
            right = cell_label.split("|", 1)[1].strip()
            if right in y_exact:
                return y_exact[right]
            return y_norm.get(norm(right))
        return None

    score_map: dict[tuple[str, str], float | None] = {}
    for cell in cells:
        if not isinstance(cell, dict):
            continue
        x_values = resolve_x_list(cell)
        y_value = resolve_y(cell)
        score_raw = cell.get("score_percent")
        if score_raw is None:
            score_raw = cell.get("score")
        score: float | None
        if isinstance(score_raw, (int, float)):
            score = float(score_raw)
        else:
            score = None
        if y_value is None or not x_values:
            continue
        for x_value in x_values:
            score_map[(y_value, x_value)] = score

    matrix: list[list[float | None]] = []
    for y in y_axis:
        row_scores: list[float | None] = []
        for x in x_axis:
            row_scores.append(score_map.get((y, x)))
        matrix.append(row_scores)

    layer_mean_raw = data.get("layer_mean_percent")
    if layer_mean_raw is None:
        layer_mean_raw = data.get("rubric_mean_percent")
    layer_mean = float(layer_mean_raw) if isinstance(layer_mean_raw, (int, float)) else None
    if layer_mean is None:
        layer_mean = mean([v for r in matrix for v in r])

    scores = [v for r in matrix for v in r if v is not None]
    gate = "PASS" if scores and all(v >= 100 for v in scores) else "FAIL"

    return LayerRubric(
        layer=layer,
        iteration=iteration,
        target=target,
        x_axis=x_axis,
        y_axis=y_axis,
        x_axis_specs=x_axis_specs,
        y_axis_specs=y_axis_specs,
        matrix=matrix,
        layer_mean=layer_mean,
        gate=gate,
        source_path=path,
        source_mode="rubrics_json",
    )


def pick_iteration_files(files: list[Path], iteration: str) -> list[Path]:
    iteration_map: dict[str, list[Path]] = {}
    for file in files:
        it = extract_iteration(file)
        if it is None:
            continue
        iteration_map.setdefault(it, []).append(file)
    if not iteration_map:
        raise ValueError("no iteration-tagged files found")

    if iteration == "latest":
        selected_iteration = max(iteration_map, key=lambda c: int(c))
        return sorted(iteration_map[selected_iteration], key=lambda p: p.as_posix())

    if iteration in iteration_map:
        return sorted(iteration_map[iteration], key=lambda p: p.as_posix())

    normalized = iteration.zfill(3)
    if normalized in iteration_map:
        return sorted(iteration_map[normalized], key=lambda p: p.as_posix())
    raise ValueError(f"iteration {iteration} not present; available={sorted(iteration_map)}")


def discover_layers(run_dir: Path, iteration: str) -> list[LayerRubric]:
    root_json_files = {
        *run_dir.glob("rubrics/Rubric_*/iteration_*.json"),
        *run_dir.glob("rubrics/R*/iteration_*.json"),  # legacy compatibility
        *run_dir.glob("rubrics/Rubric_*/cycle_*.json"),
        *run_dir.glob("rubrics/R*/cycle_*.json"),  # legacy compatibility
    }
    if root_json_files:
        json_files = sorted(root_json_files, key=lambda p: p.as_posix())
    else:
        json_files = sorted(
            {
                *run_dir.glob("**/rubrics/Rubric_*/iteration_*.json"),
                *run_dir.glob("**/rubrics/R*/iteration_*.json"),
                *run_dir.glob("**/rubrics/Rubric_*/cycle_*.json"),
                *run_dir.glob("**/rubrics/R*/cycle_*.json"),
            },
            key=lambda p: p.as_posix(),
        )
        json_files = [p for p in json_files if "snapshot" not in p.parts]
    layers_by_index: dict[int, LayerRubric] = {}
    if json_files:
        per_layer_json: dict[int, list[Path]] = {}
        for file in json_files:
            layer = extract_layer(file)
            if layer is None:
                continue
            per_layer_json.setdefault(layer, []).append(file)

        for layer in sorted(per_layer_json):
            candidates = pick_iteration_files(per_layer_json[layer], iteration)
            loaded: LayerRubric | None = None
            for candidate in candidates:
                try:
                    loaded = load_rubric_json(candidate)
                    break
                except Exception:
                    continue
            if loaded is not None:
                layers_by_index[layer] = loaded

    root_scorecards = {
        *run_dir.glob("scorecards/Rubric_*_grid_iteration_*.md"),
        *run_dir.glob("scorecards/R*_grid_iteration_*.md"),  # legacy compatibility
        *run_dir.glob("scorecards/Rubric_*_grid_cycle_*.md"),
        *run_dir.glob("scorecards/R*_grid_cycle_*.md"),  # legacy compatibility
    }
    if root_scorecards:
        scorecards = sorted(root_scorecards, key=lambda p: p.as_posix())
    else:
        scorecards = sorted(
            {
                *run_dir.glob("**/scorecards/Rubric_*_grid_iteration_*.md"),
                *run_dir.glob("**/scorecards/R*_grid_iteration_*.md"),
                *run_dir.glob("**/scorecards/Rubric_*_grid_cycle_*.md"),
                *run_dir.glob("**/scorecards/R*_grid_cycle_*.md"),
            },
            key=lambda p: p.as_posix(),
        )
        scorecards = [p for p in scorecards if "snapshot" not in p.parts]
    per_layer: dict[int, list[Path]] = {}
    for file in scorecards:
        layer = extract_layer(file)
        if layer is None:
            continue
        per_layer.setdefault(layer, []).append(file)

    for layer in sorted(per_layer):
        if layer in layers_by_index:
            continue
        candidates = pick_iteration_files(per_layer[layer], iteration)
        loaded: LayerRubric | None = None
        for candidate in candidates:
            try:
                loaded = load_scorecard(candidate)
                break
            except Exception:
                continue
        if loaded is not None:
            layers_by_index[layer] = loaded

    if not layers_by_index:
        raise FileNotFoundError(
            f"no parseable rubric files found under {run_dir} (checked rubrics/ and scorecards/ recursively)"
        )

    return [layers_by_index[idx] for idx in sorted(layers_by_index)]


def wrap_lines(text: str, width: int) -> list[str]:
    if not text:
        return [""]
    lines: list[str] = []
    for part in text.splitlines() or [""]:
        wrapped = textwrap.wrap(
            part,
            width=width,
            break_long_words=True,
            break_on_hyphens=False,
        )
        lines.extend(wrapped if wrapped else [""])
    return lines or [""]


def render_ascii_table(
    headers: list[str],
    rows: list[list[str]],
    *,
    numeric_cols: set[int] | None = None,
    max_col_width: int = 24,
) -> str:
    if numeric_cols is None:
        numeric_cols = set()

    col_count = len(headers)
    widths: list[int] = [0] * col_count

    all_rows = [headers] + rows
    for col in range(col_count):
        natural = max(len(str(r[col])) for r in all_rows)
        if col in numeric_cols:
            widths[col] = max(4, natural)
        else:
            widths[col] = min(max(4, natural), max_col_width)

    def sep() -> str:
        return "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    out: list[str] = [sep()]

    def emit_row(row_values: list[str]) -> None:
        wrapped_cells: list[list[str]] = []
        for i, value in enumerate(row_values):
            text = str(value)
            if i in numeric_cols:
                wrapped_cells.append([text])
            else:
                wrapped_cells.append(wrap_lines(text, widths[i]))

        height = max(len(lines) for lines in wrapped_cells)
        for line_idx in range(height):
            rendered_cells = []
            for col, lines in enumerate(wrapped_cells):
                cell_line = lines[line_idx] if line_idx < len(lines) else ""
                if col in numeric_cols:
                    cell_line = cell_line.rjust(widths[col])
                else:
                    cell_line = cell_line.ljust(widths[col])
                rendered_cells.append(f" {cell_line} ")
            out.append("|" + "|".join(rendered_cells) + "|")

    emit_row(headers)
    out.append(sep())
    for row in rows:
        emit_row(row)
    out.append(sep())
    return "\n".join(out)


def chunk_indexes(total: int, chunk_size: int) -> list[tuple[int, int]]:
    chunks: list[tuple[int, int]] = []
    i = 0
    while i < total:
        j = min(total, i + chunk_size)
        chunks.append((i, j))
        i = j
    return chunks


def render_layer_grid(layer: LayerRubric, chunk_size: int) -> list[str]:
    x_count = len(layer.x_axis)
    y_count = len(layer.y_axis)
    row_means = [mean(row) for row in layer.matrix]
    col_means = [mean([layer.matrix[r][c] for r in range(y_count)]) for c in range(x_count)]
    layer_mean = layer.layer_mean if layer.layer_mean is not None else mean(row_means)

    blocks: list[str] = []
    for block_idx, (start, end) in enumerate(chunk_indexes(x_count, max(1, chunk_size)), start=1):
        x_subset = layer.x_axis[start:end]
        headers = ["Y \\ X"] + x_subset + ["Row Mean"]
        rows: list[list[str]] = []

        for y_idx, y_label in enumerate(layer.y_axis):
            data = [fmt_percent(v) for v in layer.matrix[y_idx][start:end]]
            rows.append([y_label] + data + [fmt_percent(row_means[y_idx])])

        col_mean_cells = [fmt_percent(v) for v in col_means[start:end]]
        rows.append(["Column Mean"] + col_mean_cells + [fmt_percent(layer_mean)])

        numeric_cols = set(range(1, len(headers)))
        table = render_ascii_table(
            headers,
            rows,
            numeric_cols=numeric_cols,
            max_col_width=36,
        )

        if len(x_subset) < x_count:
            title = f"Grid segment {block_idx} ({start + 1}-{end} of {x_count} X dimensions)"
            blocks.append(title + "\n" + table)
        else:
            blocks.append(table)
    return blocks


def render_report(run_dir: Path, layers: list[LayerRubric], chunk_size: int, iteration: str) -> str:
    source_mode = "rubrics_json" if any(l.source_mode == "rubrics_json" for l in layers) else "scorecards"
    iterations = sorted({l.iteration for l in layers}, key=lambda c: int(c) if c.isdigit() else c)

    summary_headers = [
        "Rubric",
        "Iteration",
        "Target",
        "X",
        "Y",
        "Cells",
        "Mean",
        "Gate",
        "Source",
    ]
    summary_rows: list[list[str]] = []
    for layer in layers:
        x_count = len(layer.x_axis)
        y_count = len(layer.y_axis)
        summary_rows.append(
            [
                f"Rubric_{layer.layer}",
                layer.iteration,
                layer.target,
                str(x_count),
                str(y_count),
                str(x_count * y_count),
                fmt_percent(layer.layer_mean),
                layer.gate,
                str(layer.source_path.relative_to(run_dir)),
            ]
        )

    summary_table = render_ascii_table(
        summary_headers,
        summary_rows,
        numeric_cols={3, 4, 5},
        max_col_width=34,
    )

    parts: list[str] = []
    parts.append("# Rubrics Pretty Print")
    parts.append("")
    parts.append(f"- run_dir: `{run_dir}`")
    parts.append(f"- generated_utc: `{now_utc()}`")
    parts.append(f"- source_mode: `{source_mode}`")
    parts.append(f"- requested_iteration: `{iteration}`")
    parts.append(f"- rendered_iterations: `{', '.join(iterations)}`")
    parts.append(f"- rubric_count: `{len(layers)}`")
    parts.append("")
    parts.append("## Rubric Overview")
    parts.append("")
    parts.append("```text")
    parts.append(summary_table)
    parts.append("```")

    for layer in layers:
        parts.append("")
        parts.append(f"## Rubric {layer.layer}")
        parts.append("")
        parts.append(f"- target: `{layer.target}`")
        parts.append(f"- iteration: `{layer.iteration}`")
        parts.append(f"- gate: `{layer.gate}`")
        parts.append(f"- rubric_mean: `{fmt_percent(layer.layer_mean)}`")
        parts.append(f"- source: `{layer.source_path.relative_to(run_dir)}`")
        parts.append("")

        axis_table = render_ascii_table(
            ["Axis", "Dimension Names"],
            [
                ["X", "; ".join(layer.x_axis) if layer.x_axis else "(none)"],
                ["Y", "; ".join(layer.y_axis) if layer.y_axis else "(none)"],
            ],
            max_col_width=96,
        )
        parts.append("```text")
        parts.append(axis_table)
        parts.append("```")

        def to_cell_text(value: object) -> str:
            if value is None:
                return ""
            if isinstance(value, (str, int, float, bool)):
                return str(value)
            if isinstance(value, list):
                return "; ".join(to_cell_text(v) for v in value if v is not None)
            if isinstance(value, dict):
                preferred_keys = (
                    "name",
                    "definition",
                    "measurement_protocol",
                    "anti_gaming_probe",
                    "who",
                    "what",
                    "where",
                )
                kv_pairs: list[str] = []
                for key in preferred_keys:
                    if key in value:
                        kv_pairs.append(f"{key}:{to_cell_text(value[key])}")
                if kv_pairs:
                    return " | ".join(kv_pairs)
                return " | ".join(f"{k}:{to_cell_text(v)}" for k, v in value.items())
            return str(value)

        def summarize_anchors(anchors: object) -> str:
            if anchors is None:
                return ""
            if isinstance(anchors, str):
                return anchors
            if isinstance(anchors, list):
                return "; ".join(to_cell_text(a) for a in anchors)
            if isinstance(anchors, dict):
                def sort_key(item: tuple[object, object]) -> tuple[int, str]:
                    key = str(item[0])
                    if key.isdigit():
                        return (0, f"{int(key):03d}")
                    return (1, key)

                return " | ".join(
                    f"{str(k)}:{to_cell_text(v)}"
                    for k, v in sorted(anchors.items(), key=sort_key)
                )
            return to_cell_text(anchors)

        def render_axis_specs(title: str, specs: list[dict]) -> None:
            if not specs:
                return
            spec_rows: list[list[str]] = []
            for spec in specs:
                if isinstance(spec, dict):
                    anchor_summary = summarize_anchors(spec.get("scoring_anchors"))
                    spec_rows.append(
                        [
                            to_cell_text(spec.get("name")),
                            to_cell_text(spec.get("definition")),
                            to_cell_text(spec.get("measurement_protocol")),
                            to_cell_text(spec.get("anti_gaming_probe")),
                            anchor_summary,
                        ]
                    )
                else:
                    spec_rows.append([to_cell_text(spec), "", "", "", ""])
            spec_table = render_ascii_table(
                ["Dimension", "Definition", "Measurement", "Anti-Gaming Probe", "Anchors"],
                spec_rows,
                max_col_width=44,
            )
            parts.append("")
            parts.append(f"### {title}")
            parts.append("")
            parts.append("```text")
            parts.append(spec_table)
            parts.append("```")

        render_axis_specs("X Axis Specs", layer.x_axis_specs)
        render_axis_specs("Y Axis Specs", layer.y_axis_specs)

        for block in render_layer_grid(layer, chunk_size):
            parts.append("")
            parts.append("```text")
            parts.append(block)
            parts.append("```")

    parts.append("")
    return "\n".join(parts)


def main() -> int:
    args = parse_args()
    run_dir = Path(args.run_dir).resolve()
    if not run_dir.is_dir():
        raise SystemExit(f"error: run dir not found: {run_dir}")
    if args.chunk_size < 1:
        raise SystemExit("error: --chunk-size must be >= 1")

    layers = discover_layers(run_dir, args.iteration)
    if not layers:
        raise SystemExit(f"error: no layers discovered under {run_dir}")

    report = render_report(run_dir, layers, args.chunk_size, args.iteration)

    out_path = Path(args.output) if args.output else run_dir / "RUBRICS_PRETTY_PRINT.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")
    print(f"generated {out_path} (layers={len(layers)}, iteration={args.iteration})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
