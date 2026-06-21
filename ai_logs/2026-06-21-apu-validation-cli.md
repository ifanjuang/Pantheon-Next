# 2026-06-21 Read-only APU validation CLI

Status: implemented (bounded read-only mcp-server entry point; tests added).

Adds a command-line entry point around the existing `validate_apu_dossier` tool
so a candidate Architecture Project Understanding dossier can be validated
outside the MCP transport (developer / CI use). It reuses the same read-only
logic; it validates and reports only — it executes, canonizes and approves
nothing. The exit code reflects the validation result, never a side effect.

Changes:

- mcp-server/pantheon_mcp/cli.py (new) — `run(argv) -> int` / `main()`:
  reads a YAML dossier from a file path or stdin (`-`), calls
  `apu.validate_apu_dossier`, prints the gate-posture report as JSON, and returns
  0 when `result == "ok"` else 1. Unreadable file and invalid YAML are reported
  as JSON errors with exit 1.
- mcp-server/pyproject.toml — registers the `pantheon-apu-validate` console
  script.
- mcp-server/README.md — documents the CLI (usage, exit codes, read-only
  posture); adds `cli.py` to the layout.
- mcp-server/tests/test_cli.py (new) — four read-only tests: clean dossier exits
  0, unknown type exits 1, missing file exits 1, invalid YAML exits 1.

Validation: `python3 -m unittest discover -s mcp-server/tests` — 39 tests OK
(35 prior + 4 CLI). Stdin smoke test returns the candidate-only report and
exit 0.

Boundary: read-only, candidate-only; the gate and the human decide. No
execution, routing, scheduling, queueing or approval. One-way dependency intact
(the CLI depends on the governance core, never the reverse).
