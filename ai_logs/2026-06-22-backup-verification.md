# 2026-06-22 backup / recoverability verification — pattern declined (3rd)

Status: implemented (classifier + tool + CLI + schema + cockpit + parity guard).
Third decline of the verification pattern (after install #201–#204 and
observability #205).

## Why a distinct verification

`verify_install` asks "is it installed and answering"; `verify_observability`
asks "can we even see it"; `verify_backup` asks the recovery question: **if it
dies, can we get it back**. A backup that exists but is stale, or has never been
restored, is not recoverability; "we have backups" with no restore test is the
classic false comfort. It is the baseline the bootstrap chain already blocks on
("clarifier backup/snapshot avant tout substrat").

## Changes (contract → classifier → surfaces → guard)

- mcp-server/pantheon_mcp/backup.py (new) — `verify_backup(evidence)`. From
  provided backup presence, freshness and a demonstrated restore it derives
  `present` / `recent` / `restore_verified` and a verdict (`protected` /
  `degraded` / `unprotected` / `unknown`). Missing evidence → capability gaps.
  Read-only: no probe, no NAS access, runs no backup or restore, decides nothing.
- server.py — exposes the `verify_backup(evidence_yaml)` tool.
- backup_cli.py (new) + pyproject — `pantheon-verify-backup`; exit 0 only when the
  verdict is `protected`, 1 otherwise.
- schemas/backup_evidence.schema.yaml (new) + example, registered in
  tests/test_schema_examples.py. Documented-not-enforced, like the other evidence
  schemas. Verified: the example validates and the tool classifies it `protected`.
- docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md — tool list entry plus
  a verify_backup evidence-contract section (field table, verdict semantics,
  Python classifier as single source of truth the cockpit mirrors).
- docs/assets/pantheon-control/backup-verify.js (new) + machines.html — a
  "Vérification de sauvegarde" panel on the machines page, mirroring the
  classifier for display. machines.html loads ui.js so chip()/kv() are used; the
  verdict function is DOM-free so the parity guard can evaluate it under node.
- mcp-server/README.md — intro, tool table, CLI section, layout.

Tests:
- tests/test_backup.py — 8 classifier cases (protected / unprotected / degraded×2
  / present-from-markers / unknown×2 / non-mapping error).
- tests/test_backup_cli.py — 5 CLI cases.
- tests/test_backup_parity.py — replays a 3×3×3 = 27-case matrix through the Python
  classifier and the shipped cockpit JS (sandboxed node) and asserts the same
  verdict, so the mirror cannot drift. Skips when node is absent; runs in CI.

## Validation

`unittest discover -s mcp-server/tests` — 80 OK (66 prior + 14). `pytest tests/`
9 passed (schema example validates). `node --check` on the cockpit script passes.
governance doctor checks green vs baseline; runtime-phrase guard passes on the
edited authority doc.

Boundary: read-only, candidate-only; the gate and the human decide. The cockpit
displays; it does not act. No probe, no NAS access, no backup or restore run, no
routing, scheduling, queueing, approval or promotion. One-way dependency intact.

The verification pattern is now proven three times (install, observability,
backup), each with a tested schema example and a CI parity guard.
