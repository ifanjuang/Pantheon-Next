# Surface implemented-but-undocumented areas — governance record

Date: 2026-08-02

Status: applied status-map reconciliation — non-authoritative over the governance corpus, non-runtime.

## Purpose

A code-vs-doc review found active, CI-enforced areas of Pantheon Next that
were implemented but absent from the runtime-status spine (`WHAT_RUNS.md`,
`MODULES.md`), and one obsolete-index note that read as contradicting the live
`catalog/` directory. This log records surfacing them honestly, without
overstating their boundary.

## Findings surfaced

- **`catalog/` candidate records** — capability/resource records plus
  current-decision projection, handoff-decision and provisioner-handoff
  candidate schemas, validated by four CI workflows. Present and active; only
  the former installation-composition manifests were removed.
- **Governance CI checks** — ~two dozen read-only `.github/scripts/check_*.py`
  enforced by workflows on every push and pull request. Documented in
  `GITHUB_REPOSITORY_GOVERNANCE.md` but not reflected in the status spine.
- **Architecture Project Understanding (APU)** — `mcp-server/pantheon_mcp/apu.py`
  plus the `schemas/architecture-project-understanding/` schema family and a
  referential-integrity CI check. Implemented as read-only validation; APU
  promotion remains pending (ROADMAP R2 / issue #169).

## Changes

- `WHAT_RUNS.md` — three rows added to "Runs or exists now" for the areas above.
- `MODULES.md` — three canonical-map rows added (Candidate catalog, Architecture
  Project Understanding, Governance CI checks).
- `authority/OBSOLETE_AND_ABSENT_INDEX.md` — two `catalog/` notes clarified so
  the removed installation-composition material is not read as removing the
  active directory.

## What this is not

- No schema, validator, CI check, route or runtime behavior is changed.
- No area is promoted: APU and the catalog records remain read-only /
  candidate, and promotion stays a governed human decision.
- The status labels match each area's real boundary (read-only / candidate),
  not an implementation claim beyond the code.

## Boundary

```text
surfaced in status map != promoted
implemented read-only != approved
candidate record != installed capability
CI enforcement != runtime execution
```
