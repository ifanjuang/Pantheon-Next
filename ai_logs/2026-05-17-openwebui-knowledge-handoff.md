# AI Log — Governed OpenWebUI Knowledge handoff doctrine

Date: 2026-05-17

## Scope

Integrated the governed OpenWebUI Knowledge handoff rule into active governance documentation.

The intervention clarifies how Hermes Agent may consult content organized in OpenWebUI without receiving broad or direct access to OpenWebUI data stores.

## Files changed

- `docs/governance/OPENWEBUI_INTEGRATION.md`
- `docs/governance/HERMES_INTEGRATION.md`
- `docs/governance/STATUS.md`
- `CHANGELOG.md`
- `ai_logs/2026-05-17-openwebui-knowledge-handoff.md`

## Why

OpenWebUI can organize user-side folders, files, Notes and Knowledge Bases.

Hermes Agent can execute technical work and may need to consult dossier knowledge.

The governance risk is granting Hermes broad access to all OpenWebUI Knowledge, folders, Notes, database tables, Postgres, pgvector or internal storage.

That would bypass:

- user-visible scope;
- dossier compartmentalization;
- Task Contract limits;
- evidence discipline;
- approval thresholds;
- memory governance.

## Doctrine added

The canonical rule is now:

```text
OpenWebUI organizes user knowledge.
Pantheon turns that organization into a bounded task scope.
Hermes consults only the authorized scope and returns candidates with evidence.
```

## OpenWebUI side

`OPENWEBUI_INTEGRATION.md` now states that OpenWebUI may expose user selection of:

- dossier;
- project;
- folder;
- Knowledge Base;
- file;
- Note;
- source subset;
- conversation or channel excerpt.

Pantheon must translate the selection into a bounded governance artifact before execution.

Allowed handoff artifacts include:

- Task Contract;
- Context Pack;
- allowed knowledge/file/note IDs;
- source references;
- retrieved excerpts;
- exclusion list;
- approval ceiling;
- memory rule.

## Hermes side

`HERMES_INTEGRATION.md` now states that Hermes may consult OpenWebUI-managed knowledge only through a governed handoff.

Allowed handoff forms include:

- Context Pack;
- selected excerpts;
- source references;
- allowed knowledge/file/note IDs;
- read-only scoped gateway result;
- Evidence Candidate references.

Hermes must not freely browse OpenWebUI folders, Notes, Knowledge Bases, files, Postgres tables, pgvector stores or internal storage.

## Status and changelog

`STATUS.md` now tracks governed OpenWebUI Knowledge handoff as documentation-level doctrine and explicitly lists the following as not implemented:

- OpenWebUI Knowledge gateway implementation;
- direct Hermes bridge to OpenWebUI database or vector store.

`CHANGELOG.md` records the doctrine in version `0.1.3 - 2026-05-17`.

## Boundary check

This intervention is documentation-only.

It does not implement:

- OpenWebUI plugin;
- OpenWebUI Knowledge gateway;
- Hermes tool;
- database connector;
- Postgres or pgvector access;
- runtime bridge;
- scheduler;
- queue;
- provider router;
- automatic Knowledge-to-Memory promotion;
- automatic memory promotion;
- hidden workflow execution.

OpenWebUI exposes.

Hermes Agent executes.

Pantheon Next governs.

## Status

Implemented as active governance documentation.

Runtime implementation not started.
