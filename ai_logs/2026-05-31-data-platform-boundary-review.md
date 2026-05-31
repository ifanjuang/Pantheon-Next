# AI Log — Data platform boundary review

Date: 2026-05-31

## Scope

Applied the boundary review of Issue #30 for the `DATA_PLATFORM_*` candidate cluster.
Documentation only. After PR #26 merged, this work was rebased onto the current `main`
as PR #31. It also indexes `DATA_PLATFORM_RECONCILIATION.md`, which ChatGPT added
directly to `main` in parallel; ChatGPT did not touch the governance index files, so
indexing remains the reconciler's task. Source-level boundary fixes to
`DATA_PLATFORM_ARCHITECTURE.md` remain in this PR because the reconciliation doc
counters the wording in a separate file but does not fix the source.

## Files changed

- `docs/governance/DATA_PLATFORM_ARCHITECTURE.md`:
  - `Directus exposes and controls` → `Directus exposes controlled records`;
  - `## Deployment profiles` → `## Candidate deployment profiles outside Pantheon`
    with a disclaimer that they authorize no `operations/`, `platform/`, Docker or
    `.env` change;
  - table families marked conceptual registry families, not approved database tables,
    with schema candidates requiring a separate approved change under `schemas/`;
  - status / adapter-binding note added (candidate, non-executable blueprint; names
    products only as a candidate adapter/platform binding).
- `docs/governance/STATUS.md`, `docs/governance/README.md`, `docs/governance/MODULES.md`:
  `ARCHITECTURE_AGENCY_DOMAIN_PACK.md`, `KNOWLEDGE_INGESTION_AND_MEMORY.md` and
  `WORKFLOW_LIFECYCLE.md` realigned to `candidate / to verify` to match their own
  headers; `DATA_PLATFORM_*` remain `to verify`.
- `CHANGELOG.md`: 0.1.23 extended with the data-platform boundary review.
- `ai_logs/2026-05-31-data-platform-boundary-review.md` (this trace).

## Why

`STATUS.md` had listed three cluster documents as active support doctrine while their
own headers declare `candidate`. #30 asked to reconcile this, strengthen the data
platform boundary (Directus not sovereign, deployment profiles external, table
families not approved schema) and keep the cluster `candidate / to verify` until a
boundary patch lands.

## Governance boundary

Documentation only.

It does not implement a Postgres schema, Directus project, worker, OCR pipeline,
vector database, connector, workflow runtime, memory engine or approval automation.

It does not promote the data platform to canonical active doctrine. Any future
schema, platform, Docker or operations work still requires explicit confirmation.

## Explicit non-implementation

No files were touched under:

```text
schemas/
tests/
operations/
platform/
Docker
.env
pyproject.toml
CLAUDE.md
```

## Boundary phrase

```text
Keep the data-platform direction.
Strengthen its boundary.
Do not promote it yet.
```
