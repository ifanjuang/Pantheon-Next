# 2026-06-21 CI: run mcp-server module tests + align mcp doctor

Status: CI + test-only change — documented.

Lands the long-open #116 (the 29 mcp-server tests and the end-to-end vertical
never ran in CI) rebuilt cleanly on current main, with one necessary consistency
fix discovered while verifying:

- `.github/workflows/governance-ci.yml`: new `mcp-server` job (Python 3.11,
  `pip install -e mcp-server/.[test]`, `unittest discover -s mcp-server/tests`).
- `mcp-server/pyproject.toml`: `test` optional-dependency extra carrying
  jsonschema (runtime install stays minimal; server passport validation is stdlib).
- `mcp-server/pantheon_mcp/doctor.py`: the `runtime_phrases` check now skips
  `docs/governance/reference_reviews/`, mirroring the workflow guard fix in #171.
  Without it the mcp-server doctor test failed on ROW_BOT_4_2_0_REVIEW.md line 24
  ("queue safeguards", an external product), which would have turned the new CI
  job red. The mcp doctor is a second copy of the runtime-phrases guard; both now
  exempt external-tool reference reviews.

Verification: full suite green locally against current main —
`Ran 29 tests ... OK` (unit + e2e vertical over real MCP stdio), with the mcp SDK
installed.

Boundary: CI config + a test-only dependency extra + a guard-scope alignment in
the read-only doctor. No runtime added; the server gains no new runtime
dependency; no schema or governance-doctrine change.
