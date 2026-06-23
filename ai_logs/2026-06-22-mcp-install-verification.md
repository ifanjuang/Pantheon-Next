# 2026-06-22 mcp-server install / liveness verification surface

Status: implemented (bounded read-only mcp-server tool; tests added).

First real slice toward the dashboard's mandate ("verifies installs from their
logs and liveness: is it installed, does it answer, are the checks green").
Following the owner's decision, the read-only verification brain lives in the
existing `mcp-server/` surface (not a new module yet); the dashboard surface
would display its verdict. It classifies *provided* evidence only — it performs
no probe, makes no NAS access, installs nothing and decides nothing.

Changes:

- mcp-server/pantheon_mcp/install.py (new) — `verify_install(evidence: dict) ->
  dict`. From provided evidence (component, installed / installed_markers /
  install_success_markers + logs, health probe result, check results,
  expected_checks) it derives `installed`, `answers`, `checks_green` and a
  `verdict` (`green` / `degraded` / `absent` / `unknown`). Insufficient evidence
  is reported in `capability_gaps`, never improvised. Returns `posture:
  read-only`, `decides: false` and a note that it probes nothing and accesses no
  NAS.
- mcp-server/pantheon_mcp/server.py — imports `install` and exposes the
  `verify_install(evidence_yaml)` tool (YAML in -> JSON out).
- mcp-server/README.md — intro, tool table row, and layout (`install.py`).
- docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md — adds
  `verify_install(input) -> install_verification_report` to the Phase 4 read-only
  validation tools, with its read-only / no-probe / no-NAS posture.
- mcp-server/tests/test_install.py (new) — seven read-only tests: green,
  degraded (unreachable; red check), absent, unknown + capability gaps,
  install-from-log-markers, non-mapping error.

Design note: the tool is a pure classifier over evidence the caller already
gathered. The actual probing / log reading / NAS access is runtime work that
stays outside Pantheon (Hermes / dashboard side); Pantheon only turns the
evidence into a verdict as data. This keeps the boundary: it verifies, it does
not act.

Validation: `python3 -m unittest discover -s mcp-server/tests` — 46 tests OK
(39 prior + 7). docs/governance doctor checks green vs baseline; the
runtime-phrase guard passes (the doc states the boundary in negated form).

Boundary: read-only, candidate-only; the gate and the human decide. No probe, no
NAS access, no install, no routing, scheduling, queueing or approval. One-way
dependency intact.
