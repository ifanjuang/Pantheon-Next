# AI Log — Governance index optimization and de-duplication

Date: 2026-06-01

## Scope

Rewrote `docs/governance/STATUS.md` and `docs/governance/README.md` to remove
redundancy and make them editable again. STATUS had grown to 368 lines (ChatGPT
reported it too long to edit) and README to 637 lines. STATUS reduced to ~75 lines,
README to ~150 lines.

Established explicit ownership across the four index files so the duplication does
not recur:

```text
README.md          -> entry point and read path
STATUS.md          -> posture and live exceptions
AUTHORITY_INDEX.md -> authority class and status of each item
MODULES.md         -> module map per governance area
```

## README change

README had two exhaustive document listings (duplicating STATUS / AUTHORITY_INDEX)
and ~13 per-doctrine "boundary" sections (each duplicating the source doc and
MODULES). Both removed. README now keeps the read path, a thematic navigation, one
consolidated boundary statement, and precedence rules delegating enumeration and
classification to the authoritative indexes.

## Problem

STATUS.md had drifted into a mirror of three other indexes:

- it re-listed every active governance document (already in `README.md` and
  `AUTHORITY_INDEX.md`);
- it repeated a per-doctrine summary for most documents (already in `MODULES.md` and
  each doctrine's own file);
- it restated the "does not implement runtime/scheduler/queue/..." boundary roughly
  ten times.

This is the doctrine sprawl the repository itself warns against, and it made the file
costly to maintain.

## What changed

STATUS.md now records only what is specific to a status dashboard:

- doctrine and posture;
- the migration rule;
- a single consolidated non-runtime boundary statement;
- precedence rules pointing to the authoritative indexes (`AUTHORITY_INDEX.md`,
  `README.md`, `MODULES.md`);
- the migrated-from-OS list;
- a `Live exceptions` table for candidate / to-verify items with their pending issues.

The exhaustive document enumeration and per-doctrine summaries are intentionally
delegated to the authoritative indexes rather than duplicated here.

## CI safety

The only CI check that reads STATUS.md verifies that a `## Stub present` section does
not list migrated files as stub. The rewrite has no `## Stub present` section, so the
check passes. The queue/scheduler runtime lint also passes (verified locally: 0
failures over STATUS.md).

## Not touched

- The truncated-file repair (MODULES.md / CHANGELOG history) is left to ChatGPT.
- `ai_logs/migration-mapping.md` is unchanged.
- No file under `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`,
  `pyproject.toml` or `CLAUDE.md` was touched.

## Boundary

Documentation only. No doctrine removed in substance; redundant restatements
consolidated. No runtime, schema, test or executable change.

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```
