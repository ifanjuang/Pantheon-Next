# 2026-06-22 update-availability verification — pattern declined (5th)

Status: implemented (classifier + tool + CLI + schema + cockpit + parity guard).
Fifth decline of the verification pattern (install, observability, backup,
exposure). Requested by the owner ("vérif s'il y a une mise à jour possible").

## Why a distinct verification

The family asks installed / observable / recoverable / exposed; `verify_update`
asks whether a component is **current**: given a provided current version and the
latest available version, is an update available. It reports availability as data;
it goes nowhere to fetch the latest version and installs nothing — Pantheon is not
an updater. The comparison is provided-evidence-in, verdict-out.

## Changes (contract → classifier → surfaces → guard)

- mcp-server/pantheon_mcp/update.py (new) — `verify_update(evidence)` with a
  tolerant version parse/compare (strips a leading v, drops pre-release/build
  suffix, reads the leading integer of each dotted component, pads, compares).
  Verdict: `current` / `update_available` / `ahead` / `unknown`; missing or
  unparseable versions → capability gaps / unknown. Read-only: no probe, no
  network fetch, no NAS access, no update, decides nothing.
- server.py — exposes the `verify_update(evidence_yaml)` tool.
- update_cli.py (new) + pyproject — `pantheon-verify-update`; exit 0 only when the
  verdict is `current`, 1 otherwise.
- schemas/update_evidence.schema.yaml (new) + example, registered in
  tests/test_schema_examples.py. Documented-not-enforced. Verified: the example
  validates and the tool classifies it `update_available`.
- docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md — tool list entry plus
  a verify_update evidence-contract section (field table, verdict semantics, the
  Python classifier — including its version compare — as single source of truth).
- docs/assets/pantheon-control/update-verify.js (new) + skills.html — a
  "Vérification de mise à jour" panel on the skills page, mirroring the classifier
  including the identical version parse/compare. skills.html loads ui.js so
  chip()/kv() are used; the verdict function is DOM-free so the parity guard can
  evaluate it under node.
- mcp-server/README.md — intro, tool table, CLI section, layout.

Tests:
- tests/test_update.py — 8 classifier cases (current / update_available / ahead /
  v-prefix+prerelease / padded / unknown×2 / non-mapping error).
- tests/test_update_cli.py — 5 CLI cases.
- tests/test_update_parity.py — replays an 8×8 = 64 version-pair matrix (equal,
  behind, ahead, v-prefix, pre-release, padded, empty, unparseable) through the
  Python classifier and the shipped cockpit JS (sandboxed node) and asserts the
  same verdict, so the version compare cannot drift between the two. Skips when
  node is absent; runs in CI.

## Validation

`unittest discover -s mcp-server/tests` — 108 OK (94 prior + 14). `pytest tests/`
9 passed (schema example validates). `node --check` on the cockpit script passes.
governance doctor checks green vs baseline; runtime-phrase guard passes on the
edited authority doc.

Boundary: read-only, candidate-only; the gate and the human decide. The cockpit
displays; it does not act. No probe, no network fetch, no NAS access, no update
run, no routing, scheduling, queueing, approval or promotion. One-way dependency
intact.

The verification family is now five (install, observability, backup, exposure,
update), each with a tested schema example and a CI parity guard.
