# Commit Hygiene

## Scope
This repository uses Git to preserve an auditable history for rubric-driven and meta-rubric-driven development.

## Commit format
Use Conventional Commit style:

- `feat: ...` new capability
- `fix: ...` bug/logic fix
- `refactor: ...` structural change without behavior change
- `docs: ...` documentation change
- `chore: ...` maintenance/config change

## Rules
1. One intent per commit.
2. Include only files needed for that intent.
3. Never include generated run/eval artifacts (`runs/`, `eval/`).
4. Never include transient logs (`swarm_outputs/**/log_*.txt`).
5. For rubric edits, mention impacted rubric(s) in the subject/body (for example `Rubric_0`, `Rubric_1`).
6. For scoring-logic edits, include a short rationale in the commit body.

## Recommended workflow
1. Create or update files for one scoped change.
2. Run a quick sanity check (`rg`, schema checks, or replay checks as applicable).
3. Stage explicitly (`git add <paths>`), avoid broad `git add .` when possible.
4. Commit with a precise message.
5. Repeat for the next scoped change.

## Example messages
- `fix: align Rubric_0 aggregation with 70/30 domain-role weighting`
- `fix: add Rubric_1 aggregate decision bands and explicit output contract`
- `docs: add commit hygiene policy and repository gitignore`
