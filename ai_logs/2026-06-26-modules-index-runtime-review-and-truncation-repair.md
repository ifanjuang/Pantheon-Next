# AI Log — MODULES.md: index runtime-review validation + repair truncation

Date: 2026-06-26

## Request

ChatGPT reported it had not modified `AUTHORITY_INDEX.md` nor `MODULES.md` for the
runtime-review / model-passport validation promotion, because the connector
truncated reads of the long index files and a partial overwrite was too risky. It
left this as a remaining action (traced in its log and Notion). Picked up as a
governance reconciliation (Claude indexes; ChatGPT creates).

## Findings

- `AUTHORITY_INDEX.md` is healthy and already indexes
  `RUNTIME_REVIEW_MODEL_PASSPORT_VALIDATION_PROMOTION.md` (line 113); its length
  grows monotonically across history — no truncation. No change needed.
- `MODULES.md` was missing the row for that document — and, more seriously, it was
  **truncated**: commit `37c51c4` ("register runtime review and model passport
  modules") reduced it from 481 to 302 lines, dropping the entire narrative tail
  from the Approval module body through the Final rule (Approval, Evidence, Memory
  and Registre Probatoire, Knowledge, Integration, External tools, Schemas,
  Operations and tests, Legacy, Global governance flow, Final rule). This matches
  the recurring truncate-then-restore pattern visible in the file's history.

## Change made

- Added the canonical-module-map row for
  `RUNTIME_REVIEW_MODEL_PASSPORT_VALIDATION_PROMOTION.md` (status `to_verify`:
  validation-only promotion proposal; modifying `schemas/`, `tests/` and
  `mcp-server/` stays blocked pending explicit approval).
- Restored the truncated tail by splicing the current (up-to-date) table head with
  the byte-identical tail from commit `9d6cdb7` (the last complete version, which
  already carries the current Registre Probatoire vocabulary: "Register Candidate",
  "Registre Probatoire entry", "Memory and Registre Probatoire module"). The
  restored tail is byte-identical to `9d6cdb7`; no section is duplicated; the new
  row and all current table rows are preserved.

`MODULES.md`: 302 -> 525 lines. Governance forbidden-phrase lint: clean.

## Boundary

Documentation reconciliation only. No schema, test, mcp-server, runtime or
protected-path change. No doctrine was authored or altered — the lost content was
recovered verbatim from git history; only one index row was added.

## Prevention added

To stop the recurring truncate-then-restore cycle, added a read-only CI tripwire:

- `.github/scripts/check_no_truncation.py` — fails when a curated long file
  (`MODULES.md`, `AUTHORITY_INDEX.md`) drops below a minimum line count or loses a
  stable end-sentinel. Wired into the "Governance doctor read-only checks" step.
- Self-tested: passes on the repaired tree; fails on a simulated 302-line
  truncation (both the line-count and the sentinel signals fire); passes again
  after restore.

The check is a tripwire: if one of these files legitimately shrinks or its ending
changes, the minimum / sentinel must be updated in the same PR.

## Note for future edits

Do not use a truncated connector read as full replacement content for a long file.
When a long index must change, edit in place (anchored replacement) rather than
rewriting the whole file, or restore the tail from history as done here.
