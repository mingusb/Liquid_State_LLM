#!/usr/bin/env python3
"""Run parallel chain-link iterations with epoch snapshots and barrier merges.

Model:
- Freeze a full run snapshot per epoch.
- Launch one worker per adjacency chain (`Rubric_k -> Rubric_(k-1)`) in isolated workspaces.
- Each worker executes exactly one chain iteration (`--run-chain-once`).
- Merge accepted worker results into the main run in canonical chain order.
- Recompute stability and repeat until stable or epoch limit reached.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import json
import re
import runpy
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ITER_NAME_RE = re.compile(r"^iteration_(\d+)$")
EPOCH_NAME_RE = re.compile(r"^epoch_(\d+)$")
TEXT_EXTS = {
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".sh",
    ".py",
}


@dataclasses.dataclass
class WorkerResult:
    chain: str
    worker_root: Path
    rc: int
    iteration_dir: Path | None
    record: Any | None
    stdout_log: Path
    stderr_log: Path
    attempts: int = 1
    retry_reasons: tuple[str, ...] = ()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Run epoch/barrier parallel chain workers (one per chain link) "
            "and merge accepted results into a single run root."
        )
    )
    p.add_argument("--project-root", required=True, help="Run root to improve in place.")
    p.add_argument("--depth", type=int, required=True, help="Rubric depth N.")
    p.add_argument(
        "--required-streak",
        type=int,
        default=1,
        help="Consecutive full-chain qualifying units required for stability.",
    )
    p.add_argument(
        "--max-epochs",
        type=int,
        default=20,
        help="Maximum snapshot epochs to execute before exiting as unstable.",
    )
    p.add_argument(
        "--epochs-dir",
        default="parallel_epochs",
        help="Directory under project-root for epoch snapshots/workspaces.",
    )
    p.add_argument(
        "--iterations-dir",
        default="iterations",
        help="Iterations directory relative to project-root (default: iterations).",
    )
    p.add_argument(
        "--codex-timeout-seconds",
        type=int,
        default=0,
        help="Per-worker codex timeout in seconds (0 disables timeout).",
    )
    p.add_argument(
        "--codex-no-progress-seconds",
        type=int,
        default=0,
        help="Per-worker no-progress watchdog in seconds (0 disables).",
    )
    p.add_argument("--codex-bin", default="codex", help="Codex CLI binary.")
    p.add_argument(
        "--codex-reasoning-effort",
        default="xhigh",
        help="Reasoning effort for worker codex sessions.",
    )
    p.add_argument("--codex-model", default="", help="Optional codex model override.")
    p.add_argument(
        "--worker-max-attempts",
        type=int,
        default=2,
        help=(
            "Maximum attempts per worker within the same epoch. "
            "Retries are only used for bootstrap/timeout/missing-record failures."
        ),
    )
    p.add_argument(
        "--worker-retry-backoff-seconds",
        type=int,
        default=3,
        help="Backoff between worker retries (default: 3).",
    )
    p.add_argument(
        "--max-consecutive-no-merge-epochs",
        type=int,
        default=3,
        help="Fail only after this many consecutive epochs with no mergeable results.",
    )
    p.add_argument(
        "--max-total-iterations",
        type=int,
        default=0,
        help=(
            "Global cap on merged main-run iterations during this invocation "
            "(0 disables; useful for honoring autonomous-iteration budgets)."
        ),
    )
    p.add_argument(
        "--require-chain-destabilization",
        action="store_true",
        help="Require non-trivial destabilization before recovery credit.",
    )
    p.add_argument(
        "--min-destabilization-defects",
        type=int,
        default=3,
        help="Minimum baseline defects for destabilization proof.",
    )
    p.add_argument(
        "--min-destabilization-baseline-mean",
        type=float,
        default=40.0,
        help="Lower bound for destabilization baseline mean.",
    )
    p.add_argument(
        "--max-destabilization-baseline-mean",
        type=float,
        default=95.0,
        help="Upper bound for destabilization baseline mean.",
    )
    p.add_argument(
        "--min-recovery-iteration-gap",
        type=int,
        default=1,
        help="Min iteration gap between first destabilization and counted recovery.",
    )
    return p.parse_args()


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def chain_slug(chain: str) -> str:
    return chain.replace(" ", "").replace("->", "_to_")


def latest_iteration_dir(iterations_dir: Path) -> Path | None:
    if not iterations_dir.exists():
        return None
    pairs: list[tuple[int, Path]] = []
    for child in iterations_dir.iterdir():
        if not child.is_dir():
            continue
        m = ITER_NAME_RE.match(child.name)
        if not m:
            continue
        pairs.append((int(m.group(1)), child))
    if not pairs:
        return None
    pairs.sort(key=lambda x: x[0])
    return pairs[-1][1]


def normalize_relative_subdir(value: str, flag_name: str) -> Path:
    raw = Path(str(value).strip())
    if raw.is_absolute():
        raise SystemExit(f"{flag_name} must be relative to --project-root")
    if not raw.parts:
        raise SystemExit(f"{flag_name} must be a non-empty relative path")
    cleaned_parts: list[str] = []
    for part in raw.parts:
        if part in {"", "."}:
            continue
        if part == "..":
            raise SystemExit(f"{flag_name} must not contain '..'")
        cleaned_parts.append(part)
    if not cleaned_parts:
        raise SystemExit(f"{flag_name} must be a non-empty relative path")
    return Path(*cleaned_parts)


def epoch_namespace_stem(name: str) -> str:
    match = re.match(r"^(.*?)(?:_resume_\d+)?$", name)
    if match is None:
        return name
    stem = match.group(1)
    return stem if stem else name


def is_epoch_namespace(name: str, stem: str) -> bool:
    if name == stem:
        return True
    return re.fullmatch(rf"{re.escape(stem)}_resume_\d+", name) is not None


def next_global_epoch_number(project_root: Path, epochs_rel: Path) -> int:
    namespace_parent = (project_root / epochs_rel.parent).resolve()
    stem = epoch_namespace_stem(epochs_rel.name)
    max_epoch = 0
    if not namespace_parent.exists():
        return 1
    for namespace_dir in namespace_parent.iterdir():
        if not namespace_dir.is_dir():
            continue
        if not is_epoch_namespace(namespace_dir.name, stem):
            continue
        for child in namespace_dir.iterdir():
            if not child.is_dir():
                continue
            match = EPOCH_NAME_RE.match(child.name)
            if match is None:
                continue
            max_epoch = max(max_epoch, int(match.group(1)))
    return max_epoch + 1


def collect_iteration_dir_state(iterations_dir: Path) -> dict[str, tuple[int, int]]:
    state: dict[str, tuple[int, int]] = {}
    if not iterations_dir.exists():
        return state
    for child in iterations_dir.iterdir():
        if not child.is_dir():
            continue
        if ITER_NAME_RE.match(child.name) is None:
            continue
        try:
            stat = child.stat()
        except OSError:
            continue
        state[child.name] = (int(stat.st_mtime_ns), int(stat.st_ctime_ns))
    return state


def detect_new_or_updated_iteration_dir(
    iterations_dir: Path,
    before_state: dict[str, tuple[int, int]],
) -> Path | None:
    if not iterations_dir.exists():
        return None
    candidates: list[tuple[int, int, Path]] = []
    for child in iterations_dir.iterdir():
        if not child.is_dir():
            continue
        match = ITER_NAME_RE.match(child.name)
        if match is None:
            continue
        try:
            stat = child.stat()
            mtime_ns = int(stat.st_mtime_ns)
            ctime_ns = int(stat.st_ctime_ns)
        except OSError:
            continue
        before_sig = before_state.get(child.name)
        if before_sig is None or before_sig != (mtime_ns, ctime_ns):
            candidates.append((mtime_ns, int(match.group(1)), child))
    if not candidates:
        return None
    candidates.sort(key=lambda item: (item[0], item[1]))
    return candidates[-1][2]


def ensure_tree_has_no_external_symlinks(root: Path) -> None:
    offenders: list[tuple[Path, str]] = []
    root_resolved = root.resolve()
    if root.is_symlink():
        offenders.append((root, "root_is_symlink"))
    for child in root.rglob("*"):
        try:
            if not child.is_symlink():
                continue
        except OSError:
            continue
        try:
            target = child.resolve(strict=True)
        except OSError:
            offenders.append((child, "broken_symlink"))
            if len(offenders) >= 5:
                break
            continue
        try:
            target.relative_to(root_resolved)
        except ValueError:
            offenders.append((child, f"external_target={target}"))
            if len(offenders) >= 5:
                break
    if offenders:
        rels = ", ".join(
            (
                (str(path.relative_to(root)) if path != root else ".")
                + f" ({reason})"
            )
            for path, reason in offenders
        )
        raise SystemExit(
            f"refusing to copy tree containing external/broken symlinks under {root}: {rels}"
        )


def copy_tree(src: Path, dst: Path, epochs_rel: Path) -> None:
    ensure_tree_has_no_external_symlinks(src)
    if dst.exists():
        shutil.rmtree(dst)
    ignore_tokens = [
        "parallel_epochs*",
        "runs",
        ".git",
        "__pycache__",
        "*.pyc",
        ".mypy_cache",
        ".pytest_cache",
    ]
    if epochs_rel.parts:
        ignore_tokens.append(epochs_rel.name)
    ignore = shutil.ignore_patterns(*ignore_tokens)
    shutil.copytree(src, dst, symlinks=False, ignore=ignore)


def rewrite_label_text(text: str, old_label: str, new_label: str) -> str:
    updated = re.sub(
        rf"\biteration_{re.escape(old_label)}(?!\d)",
        f"iteration_{new_label}",
        text,
    )
    updated = re.sub(
        rf"(?m)(-?\s*iteration:\s*){re.escape(old_label)}(?!\d)\b",
        rf"\1{new_label}",
        updated,
    )
    return updated


def rewrite_label_file(path: Path, old_label: str, new_label: str) -> None:
    if path.suffix.lower() not in TEXT_EXTS:
        return
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return
    updated = rewrite_label_text(text, old_label, new_label)
    if updated == text:
        return
    path.write_text(updated, encoding="utf-8")


def rewrite_label_tree(root: Path, old_label: str, new_label: str) -> None:
    for child in root.rglob("*"):
        if child.is_file():
            rewrite_label_file(child, old_label, new_label)


def evaluate_state(rbd: dict[str, Any], args: argparse.Namespace, project_root: Path) -> Any:
    iterations_dir = project_root / args.iterations_dir
    return rbd["evaluate_current_state"](
        iterations_dir=iterations_dir,
        depth_arg=args.depth,
        required_streak=args.required_streak,
        rubrics_dir=project_root / "rubrics",
        require_chain_destabilization=args.require_chain_destabilization,
        min_destabilization_defects=args.min_destabilization_defects,
        min_destabilization_baseline_mean=args.min_destabilization_baseline_mean,
        max_destabilization_baseline_mean=args.max_destabilization_baseline_mean,
        min_recovery_iteration_gap=args.min_recovery_iteration_gap,
        require_prompt_linkage=True,
        require_prompt_satisfaction=True,
    )


def write_state(rbd: dict[str, Any], result: Any, project_root: Path, iterations_dir: Path) -> None:
    rbd["write_outputs"](
        result,
        iterations_dir,
        project_root / "STABILITY_STATUS.md",
        project_root / "STABILITY_STATUS.json",
    )


def run_worker(
    *,
    worker_root: Path,
    chain: str,
    args: argparse.Namespace,
) -> WorkerResult:
    max_attempts = max(1, int(args.worker_max_attempts))
    retry_reasons: list[str] = []
    final_result: WorkerResult | None = None
    for attempt in range(1, max_attempts + 1):
        attempt_timeout = int(args.codex_timeout_seconds)
        attempt_no_progress = int(args.codex_no_progress_seconds)
        result = run_worker_attempt(
            worker_root=worker_root,
            chain=chain,
            args=args,
            attempt=attempt,
            codex_timeout_seconds=attempt_timeout,
            codex_no_progress_seconds=attempt_no_progress,
        )
        final_result = result
        retry_reason = classify_worker_retry_reason(result)
        if retry_reason is None:
            return dataclasses.replace(
                result,
                attempts=attempt,
                retry_reasons=tuple(retry_reasons),
            )
        retry_reasons.append(f"attempt_{attempt:02d}:{retry_reason}")
        if attempt >= max_attempts:
            return dataclasses.replace(
                result,
                attempts=attempt,
                retry_reasons=tuple(retry_reasons),
            )
        if args.worker_retry_backoff_seconds > 0:
            time.sleep(args.worker_retry_backoff_seconds)
    if final_result is None:
        return WorkerResult(
            chain=chain,
            worker_root=worker_root,
            rc=1,
            iteration_dir=None,
            record=None,
            stdout_log=worker_root / "_parallel_worker.stdout.log",
            stderr_log=worker_root / "_parallel_worker.stderr.log",
            attempts=max_attempts,
            retry_reasons=tuple(retry_reasons),
        )
    return dataclasses.replace(
        final_result,
        attempts=max_attempts,
        retry_reasons=tuple(retry_reasons),
    )


def run_worker_attempt(
    *,
    worker_root: Path,
    chain: str,
    args: argparse.Namespace,
    attempt: int,
    codex_timeout_seconds: int,
    codex_no_progress_seconds: int,
) -> WorkerResult:
    worker_script = worker_root / "scripts" / "rbd_stabilize.py"
    cmd = [
        sys.executable,
        str(worker_script),
        "--project-root",
        str(worker_root),
        "--iterations-dir",
        args.iterations_dir,
        "--depth",
        str(args.depth),
        "--required-streak",
        str(args.required_streak),
        "--run-chain-once",
        chain,
        "--codex-bin",
        args.codex_bin,
        "--codex-reasoning-effort",
        args.codex_reasoning_effort,
        "--codex-timeout-seconds",
        str(codex_timeout_seconds),
        "--codex-no-progress-seconds",
        str(codex_no_progress_seconds),
        "--output",
        "STABILITY_STATUS.md",
        "--json-output",
        "STABILITY_STATUS.json",
    ]
    if args.codex_model:
        cmd.extend(["--codex-model", args.codex_model])
    if args.require_chain_destabilization:
        cmd.extend(
            [
                "--require-chain-destabilization",
                "--min-destabilization-defects",
                str(args.min_destabilization_defects),
                "--min-destabilization-baseline-mean",
                str(args.min_destabilization_baseline_mean),
                "--max-destabilization-baseline-mean",
                str(args.max_destabilization_baseline_mean),
                "--min-recovery-iteration-gap",
                str(args.min_recovery_iteration_gap),
            ]
        )

    iterations_dir = worker_root / args.iterations_dir
    before_state = collect_iteration_dir_state(iterations_dir)

    suffix = f".attempt_{attempt:02d}" if int(args.worker_max_attempts) > 1 else ""
    stdout_log = worker_root / f"_parallel_worker{suffix}.stdout.log"
    stderr_log = worker_root / f"_parallel_worker{suffix}.stderr.log"
    with stdout_log.open("w", encoding="utf-8") as out_f, stderr_log.open(
        "w", encoding="utf-8"
    ) as err_f:
        proc = subprocess.Popen(
            cmd,
            cwd=worker_root,
            stdout=out_f,
            stderr=err_f,
            text=True,
        )
        rc = proc.wait()

    rbd = runpy.run_path(str(worker_script))
    iter_dir = detect_new_or_updated_iteration_dir(iterations_dir, before_state)
    record = rbd["resolve_record"](iter_dir) if iter_dir is not None else None
    if iter_dir is not None:
        match = ITER_NAME_RE.match(iter_dir.name)
        if match is not None:
            try:
                reconciled = rbd["reconcile_iteration_truth"](
                    project_root=worker_root,
                    iterations_dir=iterations_dir,
                    iteration_label=match.group(1),
                    chain=chain,
                )
                if reconciled:
                    record = rbd["resolve_record"](iter_dir)
            except Exception:
                # Best-effort final reconciliation; keep original record on failure.
                pass
    return WorkerResult(
        chain=chain,
        worker_root=worker_root,
        rc=rc,
        iteration_dir=iter_dir,
        record=record,
        stdout_log=stdout_log,
        stderr_log=stderr_log,
    )


def classify_worker_retry_reason(worker: WorkerResult) -> str | None:
    if worker.rc == 124:
        return "watchdog_timeout"
    if worker.record is None:
        return "missing_parseable_record"
    if worker.record.chain != worker.chain:
        return "parsed_chain_mismatch"
    if getattr(worker.record, "synthetic_iteration", False):
        return "synthetic_iteration"
    decision = str(getattr(worker.record, "decision", "UNKNOWN")).upper()
    baseline_mean = float(getattr(worker.record, "baseline_mean", -1.0))
    recheck_mean = float(getattr(worker.record, "recheck_mean", -1.0))
    if decision == "REJECT" and baseline_mean <= 0.0 and recheck_mean <= 0.0:
        return "bootstrap_reject"
    return None


def classify_non_merge_reason(worker: WorkerResult) -> str:
    if worker.iteration_dir is None:
        return "missing_iteration_dir"
    if worker.record is None:
        return "missing_parseable_record"
    if worker.record.chain != worker.chain:
        return "parsed_chain_mismatch"
    if worker.record.is_improvement_accepted:
        return "mergeable"
    if worker.record.synthetic_iteration:
        return "synthetic_iteration"
    prompt_required = bool(
        getattr(
            worker.record,
            "prompt_required",
            str(worker.record.chain).replace(" ", "") == "Rubric_1->Rubric_0",
        )
    )
    if prompt_required and (not worker.record.prompt_satisfaction):
        return "prompt_satisfaction_false"
    if not worker.record.identity_lock:
        return "identity_lock_false"
    if not worker.record.real_delta_evidence:
        return "real_delta_evidence_false"
    if not worker.record.objective_gate:
        return "objective_gate_false"
    if worker.record.truth_reconciled:
        return "truth_reconciled"
    return f"decision_{str(worker.record.decision).lower()}"


def copy_if_exists(src: Path, dst: Path, old_label: str, new_label: str) -> None:
    if not src.exists() or not src.is_file():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    rewrite_label_file(dst, old_label, new_label)


def merge_worker_iteration(
    *,
    rbd: dict[str, Any],
    main_root: Path,
    worker: WorkerResult,
) -> Path | None:
    if worker.iteration_dir is None or worker.record is None:
        return None
    if worker.record.chain != worker.chain:
        return None
    if not worker.record.is_improvement_accepted:
        return None
    prompt_required = bool(
        getattr(
            worker.record,
            "prompt_required",
            str(worker.record.chain).replace(" ", "") == "Rubric_1->Rubric_0",
        )
    )
    if prompt_required and (not bool(getattr(worker.record, "prompt_satisfaction", False))):
        return None
    if not bool(getattr(worker.record, "identity_lock", False)):
        return None
    if bool(getattr(worker.record, "synthetic_iteration", True)):
        return None
    if not bool(getattr(worker.record, "real_delta_evidence", False)):
        return None
    if not bool(getattr(worker.record, "objective_gate", False)):
        return None
    if bool(getattr(worker.record, "truth_reconciled", False)):
        return None

    parsed = rbd["parse_chain"](worker.chain)
    if parsed is None:
        return None
    _, lower = parsed

    match = ITER_NAME_RE.match(worker.iteration_dir.name)
    if match is None:
        return None
    old_label = f"{int(match.group(1)):03d}"
    new_num = rbd["next_iteration_number"](main_root / "iterations")
    new_label = f"{new_num:03d}"

    dest_iter_dir = main_root / "iterations" / f"iteration_{new_label}"
    if dest_iter_dir.exists():
        shutil.rmtree(dest_iter_dir)
    # Flatten links so merged iterations remain self-contained after worker
    # workspaces are discarded.
    shutil.copytree(worker.iteration_dir, dest_iter_dir, symlinks=False)
    rewrite_label_tree(dest_iter_dir, old_label, new_label)

    worker_root = worker.worker_root
    file_mappings = [
        (
            worker_root / f"rubrics/Rubric_{lower}/iteration_{old_label}.json",
            main_root / f"rubrics/Rubric_{lower}/iteration_{new_label}.json",
        ),
        (
            worker_root / f"scorecards/Rubric_{lower}_grid_iteration_{old_label}.md",
            main_root / f"scorecards/Rubric_{lower}_grid_iteration_{new_label}.md",
        ),
        (
            worker_root / f"collateral/Rubric_{lower}/manifest_iteration_{old_label}.md",
            main_root / f"collateral/Rubric_{lower}/manifest_iteration_{new_label}.md",
        ),
        (
            worker_root / f"collateral/Rubric_{lower}/access_log_iteration_{old_label}.md",
            main_root / f"collateral/Rubric_{lower}/access_log_iteration_{new_label}.md",
        ),
        (
            worker_root / f"evidence/iteration_{old_label}.md",
            main_root / f"evidence/iteration_{new_label}.md",
        ),
        (
            worker_root / f"deltas/iteration_{old_label}.md",
            main_root / f"deltas/iteration_{new_label}.md",
        ),
        (
            worker_root / f"contradictions/iteration_{old_label}.md",
            main_root / f"contradictions/iteration_{new_label}.md",
        ),
    ]
    for src, dst in file_mappings:
        copy_if_exists(src, dst, old_label, new_label)

    run_level_files = (
        "ARTIFACT_MANIFEST.md",
        "PROMPT_SATISFACTION.md",
        "LIQUID_STATE_IDENTITY.md",
        "RUBRIC_SCORECARD_SUMMARY.md",
        "FINAL_STATUS.md",
        "OBJECTIVE_SPEC.md",
        "BEST_KNOWN_FRONTIER.md",
    )
    for name in run_level_files:
        copy_if_exists(worker_root / name, main_root / name, old_label, new_label)

    # Prompt primary artifacts may be referenced by any chain's prompt-satisfaction
    # evidence; merge them whenever they exist in the worker run.
    prompt_refs = rbd["infer_prompt_primary_artifact_refs"](main_root / "prompt.txt")
    for ref in prompt_refs:
        src = rbd["resolve_run_path"](worker_root, ref)
        dst = rbd["resolve_run_path"](main_root, ref)
        if src is None or dst is None or not src.exists() or not src.is_file():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    chain_requires_prompt = rbd.get("chain_requires_prompt_satisfaction")
    should_copy_run_level = (
        chain_requires_prompt(worker.chain)
        if callable(chain_requires_prompt)
        else worker.chain.replace(" ", "") == "Rubric_1->Rubric_0"
    )
    if should_copy_run_level:
        run_level_files = [
            "PROMPT_SATISFACTION.md",
            "OBJECTIVE_SPEC.md",
            "BEST_KNOWN_FRONTIER.md",
            "ARTIFACT_MANIFEST.md",
            "RUBRIC_SCORECARD_SUMMARY.md",
            "FINAL_STATUS.md",
            "LIQUID_STATE_IDENTITY.md",
        ]
        for name in run_level_files:
            src = worker_root / name
            dst = main_root / name
            if not src.exists() or not src.is_file():
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    merge_meta = dest_iter_dir / "PARALLEL_MERGE_METADATA.md"
    merge_meta.write_text(
        "\n".join(
            [
                "# Parallel Merge Metadata",
                f"- merged_utc: {now_utc()}",
                f"- source_worker_root: {worker_root}",
                f"- source_iteration: iteration_{old_label}",
                f"- merged_iteration: iteration_{new_label}",
                f"- chain: {worker.chain}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return dest_iter_dir


def write_epoch_summary(
    *,
    epoch_dir: Path,
    pre_state: Any,
    post_state: Any,
    all_chains: list[str],
    active_chains: list[str],
    workers: list[WorkerResult],
    merged: list[dict[str, str]],
) -> None:
    lines: list[str] = []
    lines.append("# Parallel Epoch Summary")
    lines.append(f"- generated_utc: {now_utc()}")
    lines.append(f"- pre_stable: {'yes' if pre_state.stable else 'no'}")
    lines.append(f"- post_stable: {'yes' if post_state.stable else 'no'}")
    lines.append(
        "- next_chain_before_batch: "
        + (pre_state.next_chain if pre_state.next_chain else "none")
    )
    lines.append(
        "- next_chain_after_batch: "
        + (post_state.next_chain if post_state.next_chain else "none")
    )
    lines.append("- all_chains: " + (" ; ".join(all_chains) if all_chains else "none"))
    lines.append(
        "- active_chains: " + (" ; ".join(active_chains) if active_chains else "none")
    )
    skipped = [chain for chain in all_chains if chain not in set(active_chains)]
    lines.append("- skipped_chains: " + (" ; ".join(skipped) if skipped else "none"))
    lines.append("")
    lines.append("## Workers")
    for worker in workers:
        rec = worker.record
        decision = rec.decision if rec is not None else "MISSING"
        chain = rec.chain if rec is not None else "MISSING"
        non_merge_reason = classify_non_merge_reason(worker)
        lines.append(
            f"- {worker.chain}: rc={worker.rc}, parsed_chain={chain}, "
            f"decision={decision}, attempts={worker.attempts}, "
            f"non_merge_reason={non_merge_reason}, "
            f"stdout={worker.stdout_log.name}, stderr={worker.stderr_log.name}"
        )
        if worker.retry_reasons:
            lines.append(f"  retries: {', '.join(worker.retry_reasons)}")
    lines.append("")
    lines.append("## Merged Result Applied")
    if not merged:
        lines.append("- merged_link_applied: none")
    else:
        for item in merged:
            lines.append(
                f"- merged_link_applied: {item['chain']}"
            )
            lines.append(
                f"  merged_source_iteration: iteration_{item['source_iteration']}"
            )
            lines.append(
                f"  merged_destination_iteration: iteration_{item['merged_iteration']}"
            )
    (epoch_dir / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    if args.depth < 1:
        raise SystemExit("--depth must be >= 1 for parallel chain links")
    if args.required_streak < 1:
        raise SystemExit("--required-streak must be >= 1")
    if args.max_epochs < 1:
        raise SystemExit("--max-epochs must be >= 1")
    if args.worker_max_attempts < 1:
        raise SystemExit("--worker-max-attempts must be >= 1")
    if args.worker_retry_backoff_seconds < 0:
        raise SystemExit("--worker-retry-backoff-seconds must be >= 0")
    if args.max_consecutive_no_merge_epochs < 1:
        raise SystemExit("--max-consecutive-no-merge-epochs must be >= 1")
    if args.max_total_iterations < 0:
        raise SystemExit("--max-total-iterations must be >= 0")

    project_root = Path(args.project_root).resolve()
    iterations_rel = normalize_relative_subdir(args.iterations_dir, "--iterations-dir")
    epochs_rel = normalize_relative_subdir(args.epochs_dir, "--epochs-dir")
    args.iterations_dir = iterations_rel.as_posix()
    args.epochs_dir = epochs_rel.as_posix()
    iterations_dir = project_root / iterations_rel
    script_dir = Path(__file__).resolve().parent
    rbd = runpy.run_path(str(script_dir / "rbd_stabilize.py"))

    epochs_root = project_root / epochs_rel
    epochs_root.mkdir(parents=True, exist_ok=True)

    consecutive_no_merge_epochs = 0
    for epoch_attempt in range(1, args.max_epochs + 1):
        if args.max_total_iterations > 0:
            current_records = len(rbd["collect_records"](iterations_dir))
            if current_records >= args.max_total_iterations:
                final_state = evaluate_state(rbd, args, project_root)
                write_state(rbd, final_state, project_root, iterations_dir)
                print(
                    "parallel_stability=budget_exhausted "
                    + json.dumps(
                        {
                            "max_total_iterations": args.max_total_iterations,
                            "current_records": current_records,
                        }
                    )
                )
                return 2

        pre_state = evaluate_state(rbd, args, project_root)
        write_state(rbd, pre_state, project_root, iterations_dir)
        if pre_state.stable:
            print("parallel_stability=already_stable")
            return 0

        expected_chains = list(pre_state.expected_chains)
        if pre_state.next_chain and pre_state.next_chain in expected_chains:
            active_start = expected_chains.index(pre_state.next_chain)
            active_chains = expected_chains[active_start:]
        else:
            active_chains = list(expected_chains)
        epoch_global = next_global_epoch_number(project_root, epochs_rel)
        epoch_dir = epochs_root / f"epoch_{epoch_global:03d}"
        workers_root = epoch_dir / "workers"
        snapshot_root = epoch_dir / "snapshot"
        workers_root.mkdir(parents=True, exist_ok=True)

        print(
            "parallel_epoch_start="
            + json.dumps(
                {
                    "epoch": epoch_global,
                    "epoch_attempt": epoch_attempt,
                    "chains": expected_chains,
                    "active_chains": active_chains,
                    "next_chain_before_batch": pre_state.next_chain,
                }
            )
        )

        copy_tree(project_root, snapshot_root, epochs_rel=epochs_rel)

        worker_results: list[WorkerResult] = []
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=max(1, len(active_chains))
        ) as executor:
            futures: list[concurrent.futures.Future[WorkerResult]] = []
            for chain in active_chains:
                worker_root = workers_root / chain_slug(chain)
                copy_tree(snapshot_root, worker_root, epochs_rel=epochs_rel)
                futures.append(
                    executor.submit(
                        run_worker,
                        worker_root=worker_root,
                        chain=chain,
                        args=args,
                    )
                )
            for future in concurrent.futures.as_completed(futures):
                worker_results.append(future.result())

        worker_results.sort(
            key=lambda w: active_chains.index(w.chain)
            if w.chain in active_chains
            else 10**6
        )

        merged: list[dict[str, str]] = []
        merge_state = pre_state
        merge_chain = merge_state.next_chain
        if merge_chain:
            worker = next((w for w in worker_results if w.chain == merge_chain), None)
            if worker is not None and worker.iteration_dir is not None:
                merged_dir = merge_worker_iteration(
                    rbd=rbd, main_root=project_root, worker=worker
                )
                if merged_dir is not None:
                    src_match = ITER_NAME_RE.match(worker.iteration_dir.name)
                    dst_match = ITER_NAME_RE.match(merged_dir.name)
                    src_lbl = src_match.group(1) if src_match else "unknown"
                    dst_lbl = dst_match.group(1) if dst_match else "unknown"
                    merged.append(
                        {
                            "chain": merge_chain,
                            "source_iteration": src_lbl,
                            "merged_iteration": dst_lbl,
                        }
                    )

        post_state = evaluate_state(rbd, args, project_root)
        write_state(rbd, post_state, project_root, iterations_dir)
        write_epoch_summary(
            epoch_dir=epoch_dir,
            pre_state=pre_state,
            post_state=post_state,
            all_chains=expected_chains,
            active_chains=active_chains,
            workers=worker_results,
            merged=merged,
        )

        print(
            "parallel_epoch_end="
            + json.dumps(
                {
                    "epoch": epoch_global,
                    "epoch_attempt": epoch_attempt,
                    "merged": len(merged),
                    "post_stable": post_state.stable,
                    "next_chain_after_batch": post_state.next_chain,
                }
            )
        )

        if post_state.stable:
            print("parallel_stability=achieved")
            return 0
        if args.max_total_iterations > 0:
            current_records = len(rbd["collect_records"](iterations_dir))
            if current_records >= args.max_total_iterations:
                print(
                    "parallel_stability=budget_exhausted "
                    + json.dumps(
                        {
                            "max_total_iterations": args.max_total_iterations,
                            "current_records": current_records,
                        }
                    )
                )
                return 2
        made_progress = (
            post_state.stable
            or (len(merged) > 0)
            or (post_state.next_chain != pre_state.next_chain)
            or (post_state.streak > pre_state.streak)
        )
        if not made_progress:
            consecutive_no_merge_epochs += 1
            print(
                "parallel_epoch_stall="
                + json.dumps(
                    {
                        "epoch": epoch_global,
                        "epoch_attempt": epoch_attempt,
                        "merged": len(merged),
                        "consecutive_no_merge_epochs": consecutive_no_merge_epochs,
                        "max_consecutive_no_merge_epochs": args.max_consecutive_no_merge_epochs,
                    }
                )
            )
            if consecutive_no_merge_epochs >= args.max_consecutive_no_merge_epochs:
                print("parallel_stability=not_achieved no_mergeable_worker_results")
                return 2
            continue
        consecutive_no_merge_epochs = 0

    final_state = evaluate_state(rbd, args, project_root)
    write_state(rbd, final_state, project_root, iterations_dir)
    print("parallel_stability=not_achieved max_epochs_reached")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
