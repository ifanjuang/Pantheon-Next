# 2026-06-22 exposure-surface verification — pattern declined (4th)

Status: implemented (classifier + tool + CLI + schema + cockpit + parity guard).
Fourth decline of the verification pattern (install #201–#204, observability #205,
backup #206).

## Why a distinct verification

The others ask installed / observable / recoverable; `verify_exposure` asks
whether the **exposure surface is safe**: how far it is reachable (local / VPN /
public), whether authentication is enforced and whether access scope is limited.
The doctrine is explicit that internal runtimes must not be reachable publicly
without protection and a public surface must stay authenticated and
least-privilege. The unsafe extreme — publicly reachable with no auth — gets its
own verdict (`exposed`), distinct from the family's other "bad baseline" verdicts.

## Changes (contract → classifier → surfaces → guard)

- mcp-server/pantheon_mcp/exposure.py (new) — `verify_exposure(evidence)`. From
  provided reach + auth + scope it derives `reach_contained` / `authenticated` /
  `scoped` and a verdict (`guarded` / `degraded` / `exposed` / `unknown`). Missing
  evidence → capability gaps. Read-only: no probe, no NAS access, opens no port,
  sends nothing, decides nothing.
- server.py — exposes the `verify_exposure(evidence_yaml)` tool.
- exposure_cli.py (new) + pyproject — `pantheon-verify-exposure`; exit 0 only when
  the verdict is `guarded`, 1 otherwise.
- schemas/exposure_evidence.schema.yaml (new) + example, registered in
  tests/test_schema_examples.py. Documented-not-enforced. Verified: the example
  validates and the tool classifies it `guarded`.
- docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md — tool list entry plus
  a verify_exposure evidence-contract section (field table, verdict semantics,
  Python classifier as single source of truth the cockpit mirrors).
- docs/assets/pantheon-control/exposure-verify.js (new) + services.html — a
  "Vérification d'exposition" panel on the services page, mirroring the classifier
  for display. services.html loads ui.js so chip()/kv() are used; the verdict
  function is DOM-free so the parity guard can evaluate it under node.
- mcp-server/README.md — intro, tool table, CLI section, layout.

Tests:
- tests/test_exposure.py — 8 classifier cases (guarded / exposed / degraded×3 /
  unknown×2 / non-mapping error).
- tests/test_exposure_cli.py — 5 CLI cases.
- tests/test_exposure_parity.py — replays a 4×3×3 = 36-case matrix through the
  Python classifier and the shipped cockpit JS (sandboxed node) and asserts the
  same verdict, so the mirror cannot drift. Skips when node is absent; runs in CI.

## Validation

`unittest discover -s mcp-server/tests` — 94 OK (80 prior + 14). `pytest tests/`
9 passed (schema example validates). `node --check` on the cockpit script passes.
governance doctor checks green vs baseline; runtime-phrase guard passes on the
edited authority doc.

Boundary: read-only, candidate-only; the gate and the human decide. The cockpit
displays; it does not act. No probe, no NAS access, no port opened, nothing sent,
no routing, scheduling, queueing, approval or promotion. One-way dependency intact.

The verification family is now four (install, observability, backup, exposure),
each with a tested schema example and a CI parity guard.
