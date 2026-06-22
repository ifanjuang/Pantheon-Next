# 2026-06-22 observability verification — pattern declined

Status: implemented (classifier + tool + CLI + schema + cockpit + parity guard).
Declines the install-verification pattern (PRs #201–#204) onto a second read-only
verification, per the owner's choice.

## Why a distinct verification

`verify_install` asks "is it installed and answering". `verify_observability`
asks the prior question: **can we even see it** — are observability signals
present, is the data fresh, are errors within threshold. A component can be
installed and answering yet effectively blind (no logs, stale metrics); a verdict
built on absent signals is false comfort. Same four-part pattern, genuinely
different concern.

## Changes (contract → classifier → surfaces → guard)

- mcp-server/pantheon_mcp/observability.py (new) — `verify_observability(evidence)`.
  From a provided signal inventory, freshness and error level it derives
  `has_signal` / `signals_present` / `fresh` / `errors_ok` and a verdict
  (`observable` / `degraded` / `blind` / `unknown`). Missing evidence → capability
  gaps. Read-only: no probe, no NAS access, no metrics query, decides nothing.
- server.py — exposes the `verify_observability(evidence_yaml)` tool.
- observability_cli.py (new) + pyproject — `pantheon-verify-observability`; exit 0
  only when the verdict is `observable`, 1 otherwise.
- schemas/observability_evidence.schema.yaml (new) + example, registered in
  tests/test_schema_examples.py. Documented-not-enforced, like the install schema.
  Verified: the example validates and the tool classifies it `observable`.
- docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md — tool list entry plus
  a verify_observability evidence-contract section (field table, verdict
  semantics, Python classifier as single source of truth the cockpit mirrors).
- docs/assets/pantheon-control/observability-verify.js (new) + observability.html
  — a "Vérification d'observabilité" panel mirroring the classifier for display.
  Uses chip()/toast() (this page does not load ui.js); the verdict function is
  DOM-free so the parity guard can evaluate it under node.
- mcp-server/README.md — intro, tool table, CLI section, layout.

Tests:
- tests/test_observability.py — 8 classifier cases (observable / blind /
  degraded×3 / unknown×2 / non-mapping error).
- tests/test_observability_cli.py — 5 CLI cases.
- tests/test_observability_parity.py — replays a 4×3×3 = 36-case matrix through the
  Python classifier and the shipped cockpit JS (sandboxed node) and asserts the
  same verdict, so the mirror cannot drift. Skips when node is absent; runs in CI.

## Validation

`python3 -m unittest discover -s mcp-server/tests` — 66 OK (52 prior + 14).
`pytest tests/` 9 passed (schema example validates). `node --check` on the cockpit
script passes. governance doctor checks (status headers, internal links, index
coverage, axis vocabulary) green vs baseline; runtime-phrase guard passes on the
edited authority doc.

Boundary: read-only, candidate-only; the gate and the human decide. The cockpit
displays; it does not act. No probe, no NAS access, no metrics query, no routing,
scheduling, queueing, approval or promotion. One-way dependency intact.
