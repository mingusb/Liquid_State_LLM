Develop and improve this project's `README.md` as the primary artifact.

Project context:
- Repository: rubric-driven autonomous development toolkit.
- Primary audience: technical users who need to run prompt-driven autonomous development to stability.
- Tone: concise, factual, operator-focused.

Required outcomes:
1. Produce a `README.md` that is complete, practical, and internally consistent.
2. Make `./rdd --prompt <prompt.txt> --depth <N>` the default/most prominent workflow.
3. Clearly explain the chaos-to-recovery stability model:
   - chain destabilization is required,
   - non-trivial destabilization thresholds,
   - prompt linkage requirements,
   - recovery requirements.
4. Include a clear quickstart with copy-pastable commands.
5. Include script index with purpose and when to use each script.
6. Include troubleshooting section for common operational failures (timeouts, stalled runs, missing collateral, unstable status).
7. Keep claims grounded in repository behavior; do not invent unsupported features.
8. Keep formatting clean and scannable.

Acceptance criteria:
- `README.md` must be usable as a standalone operator guide for this repo.
- Commands in README must align with actual script interfaces.
- Terminology is consistent (`rubric-driven development`, `Rubric_0..Rubric_N`, `stability`).
