# Bird's-Eye: How This System Actually Works

## 1) Direct Answer

No hidden control path was intentionally concealed.
What made the system hard to read was spread-out logic across orchestrator code, stabilizer code, and epoch artifacts.
This document is the plain-language map.

## 2) One-Minute Mental Model

The system is a pipeline of chain links:

- `Rubric_5 -> Rubric_4`
- `Rubric_4 -> Rubric_3`
- `Rubric_3 -> Rubric_2`
- `Rubric_2 -> Rubric_1`
- `Rubric_1 -> Rubric_0`

Each link means: "use the higher rubric to improve/score the lower rubric."
`Rubric_1 -> Rubric_0` is the project-facing link (artifact/prompt-facing).

## 3) Exact Epoch Mechanics

Every epoch does this:

1. Compute `next_chain` from `STABILITY_STATUS.json`.
2. Snapshot the run into `parallel_epochs*/epoch_XXX/snapshot`.
3. Launch one worker per active link in parallel.
4. Each worker runs exactly one chain iteration (`--run-chain-once`).
5. Evaluate worker outputs.
6. Merge only the worker result for `next_chain` into main run.
7. Recompute stability state.
8. Start next epoch.

Important: parallel workers can all improve, but only `next_chain` advances main state in that epoch.

Code anchors:

- active chain selection and `next_chain` window: `scripts/rbd_parallel_links.py:839`
- parallel worker launch: `scripts/rbd_parallel_links.py:863`
- single-chain merge gate: `scripts/rbd_parallel_links.py:890`
- epoch summary emission: `scripts/rbd_parallel_links.py:912`

## 4) Why Improvements Don’t Always Become "Stable"

There are three levels of "good":

1. `REJECT`
2. `PROVISIONAL_ACCEPT`
3. `ACCEPT`

`PROVISIONAL_ACCEPT` means real improvement happened and merge may proceed, but strict perfect quality is not yet met.

Strict perfect quality requires all of these at once:

- `recheck_mean >= 100.0`
- `recheck_defects <= 0`
- `recheck_blocking_defects <= 0`
- non-negative delta
- integrity gates pass

Code anchors:

- quality thresholds: `scripts/rbd_stabilize.py:280`
- provisional acceptance logic: `scripts/rbd_stabilize.py:391`
- strict perfect logic: `scripts/rbd_stabilize.py:378`

## 5) Dependency Invalidation (The Big Non-Obvious Rule)

When a link finishes, downstream prompt-facing links are invalidated and must reconverge again.

Example:

- If `Rubric_3 -> Rubric_2` improves,
- then `Rubric_2 -> Rubric_1` and `Rubric_1 -> Rubric_0` are reset for recovery accounting.

This is why you see loops that look repetitive: they are required recomputation, not random churn.

Code anchor:

- invalidation/reset behavior: `scripts/rbd_stabilize.py:3758`

## 6) Prompt Satisfaction Gate

Prompt satisfaction is hard-gated on `Rubric_1 -> Rubric_0`.
If that link is not prompt-satisfied, the full chain cannot stabilize.

Code anchors:

- prompt-required chain rule: `scripts/rbd_stabilize.py:3621`
- prompt-satisfaction reconciliation: `scripts/rbd_stabilize.py:3494`

## 7) Run-Level Budgets and Stop Conditions

The orchestrator can stop before stability if limits are hit:

- epoch budget (`--max-epochs`)
- merged-iteration budget (`--max-total-iterations`)
- too many consecutive no-merge epochs

Code anchors:

- budget exhaustion path: `scripts/rbd_parallel_links.py:820`
- no-merge stop path: `scripts/rbd_parallel_links.py:969`
- max-epochs stop path: `scripts/rbd_parallel_links.py:977`

## 8) Current Run, Mechanically

Run:

- `runs/depth5_codex_low_restart_20260226T015701Z`

Merged progression (what actually advanced main state):

| Phase | Epoch | Pre next | Merged chain | Iter | Baseline->Recheck | Delta pp | Post next |
|---|---:|---|---|---:|---:|---:|---|
| base | 1 | Rubric_5 -> Rubric_4 | Rubric_5 -> Rubric_4 | 001 | 74.0->88.0 | +14.0 | Rubric_4 -> Rubric_3 |
| base | 2 | Rubric_4 -> Rubric_3 | Rubric_4 -> Rubric_3 | 002 | 62.0->88.0 | +26.0 | Rubric_3 -> Rubric_2 |
| base | 3 | Rubric_3 -> Rubric_2 | Rubric_3 -> Rubric_2 | 003 | 68.0->92.0 | +24.0 | Rubric_2 -> Rubric_1 |
| base | 4 | Rubric_2 -> Rubric_1 | Rubric_2 -> Rubric_1 | 004 | 72.0->91.0 | +19.0 | Rubric_1 -> Rubric_0 |
| base | 5 | Rubric_1 -> Rubric_0 | Rubric_1 -> Rubric_0 | 005 | 62.0->96.0 | +34.0 | Rubric_5 -> Rubric_4 |
| base | 6 | Rubric_5 -> Rubric_4 | Rubric_5 -> Rubric_4 | 006 | 72.0->91.0 | +19.0 | Rubric_4 -> Rubric_3 |
| base | 7 | Rubric_4 -> Rubric_3 | Rubric_4 -> Rubric_3 | 007 | 72.0->91.0 | +19.0 | Rubric_3 -> Rubric_2 |
| base | 8 | Rubric_3 -> Rubric_2 | Rubric_3 -> Rubric_2 | 008 | 74.0->91.0 | +17.0 | Rubric_2 -> Rubric_1 |
| resume1 | 1 | Rubric_2 -> Rubric_1 | Rubric_2 -> Rubric_1 | 009 | 71.9->93.4 | +21.5 | Rubric_1 -> Rubric_0 |
| resume1 | 2 | Rubric_1 -> Rubric_0 | Rubric_1 -> Rubric_0 | 010 | 72.4->96.0 | +23.6 | Rubric_5 -> Rubric_4 |
| resume1 | 3 | Rubric_5 -> Rubric_4 | Rubric_5 -> Rubric_4 | 011 | 82.4->96.3 | +13.9 | Rubric_4 -> Rubric_3 |
| resume1 | 4 | Rubric_4 -> Rubric_3 | Rubric_4 -> Rubric_3 | 012 | 74.0->93.0 | +19.0 | Rubric_3 -> Rubric_2 |
| resume1 | 5 | Rubric_3 -> Rubric_2 | Rubric_3 -> Rubric_2 | 013 | 74.2->92.1 | +17.9 | Rubric_2 -> Rubric_1 |
| resume1 | 6 | Rubric_2 -> Rubric_1 | Rubric_2 -> Rubric_1 | 014 | 72.0->89.0 | +17.0 | Rubric_1 -> Rubric_0 |
| resume1 | 7 | Rubric_1 -> Rubric_0 | Rubric_1 -> Rubric_0 | 015 | 71.8->96.4 | +24.6 | Rubric_5 -> Rubric_4 |

Aggregate view across completed epochs:

- workers completed: `45`
- merged into main run: `15`
- decisions: `PROVISIONAL_ACCEPT=39`, `ACCEPT=5`, `REJECT=1`
- mean delta per worker:
  - `base: +21.6 pp`
  - `resume1: +20.9 pp`

Baseline reset visibility (this is what was missing before):

| merged_iter | chain | prev_baseline -> new_baseline | baseline_drop_pp |
|---:|---|---:|---:|
| 006 | Rubric_5 -> Rubric_4 | 74.0->72.0 | -2.0 |
| 009 | Rubric_2 -> Rubric_1 | 72.0->71.9 | -0.1 |
| 015 | Rubric_1 -> Rubric_0 | 72.4->71.8 | -0.6 |
| 017 | Rubric_4 -> Rubric_3 | 74.0->72.0 | -2.0 |
| 018 | Rubric_3 -> Rubric_2 | 74.2->72.0 | -2.2 |

## 9) Live Status (Last Capture)

- `stable=false`
- `phase=edge_of_chaos_dynamics`
- `next_chain=Rubric_5 -> Rubric_4`
- `current_streak=0`, `required_streak=1`

Latest known per chain:

- `Rubric_5 -> Rubric_4`: `82.4 -> 96.3` (`+13.9`), `PROVISIONAL_ACCEPT`, blocking `0`, defects `2`
- `Rubric_4 -> Rubric_3`: `74.0 -> 93.0` (`+19.0`), `PROVISIONAL_ACCEPT`, blocking `0`, defects `1`
- `Rubric_3 -> Rubric_2`: `74.2 -> 92.1` (`+17.9`), `PROVISIONAL_ACCEPT`, blocking `1`, defects `2`
- `Rubric_2 -> Rubric_1`: `72.0 -> 89.0` (`+17.0`), `PROVISIONAL_ACCEPT`, blocking `0`, defects `2`
- `Rubric_1 -> Rubric_0`: `71.8 -> 96.4` (`+24.6`), `PROVISIONAL_ACCEPT`, blocking `1`, defects `1`

## 10) One Honest Constraint In This Build

Rubric axes are currently deterministic around a canonical 16-role company model; they are not fully unconstrained emergent axes yet.

Code anchors:

- fixed roles catalog: `scripts/rbd_stabilize.py:287`
- fixed role dimensions: `scripts/rbd_stabilize.py:309`
- explicit fixed-axis rationale: `scripts/rbd_stabilize.py:4657`
