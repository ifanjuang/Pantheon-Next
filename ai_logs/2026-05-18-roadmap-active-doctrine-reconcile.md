# Roadmap Active Doctrine Reconcile

Date: 2026-05-18

## Scope

This intervention reconciled `docs/governance/ROADMAP.md` Phase 1 against `docs/governance/STATUS.md` and `docs/governance/README.md`.

Files changed:

- `docs/governance/ROADMAP.md`.

This log records the intervention.

## Finding

Audit of `ROADMAP.md` revealed that the Phase 1 "Implemented active doctrine" list omitted two documents already listed as active governance in `STATUS.md` and indexed in `docs/governance/README.md`:

- `docs/governance/MARKDOWN_DOSSIER_WORKFLOW.md`;
- `docs/governance/RAG_INGESTION_PIPELINE.md`.

`STATUS.md` lines 85-86 list both as active governance documents.

`docs/governance/README.md` indexes both in the active governance list and in dedicated boundary sections (Document workflow support, RAG ingestion support).

The two files are present (14 KB and 15 KB respectively).

## Change

The two entries were inserted in `ROADMAP.md` Phase 1 "Implemented active doctrine" list, between `REQUEST_ORCHESTRATION.md` and `HERMES_INTEGRATION.md`, matching the ordering used in `STATUS.md`.

No other section was modified.

## Doctrine boundary

No runtime was introduced.

No endpoint, Docker stack, scheduler, queue, message bus, provider router, workflow engine, plugin manager, skill installer, automatic approval system or automatic memory promotion was introduced.

`MARKDOWN_DOSSIER_WORKFLOW.md` remains documentation-level governance only. It does not implement an editor, runtime, plugin, OpenWebUI extension or Hermes tool.

`RAG_INGESTION_PIPELINE.md` remains documentation-level governance only. It does not implement PDF parsing, OCR, chunking, indexing, an OpenWebUI plugin, a Hermes tool, a scheduler, a queue or an ingestion runtime.

## Risks and limitations

- The intervention is a reconciliation, not a doctrine change.
- Other audit findings (phase vocabulary mismatch with `MIGRATION_PLAYBOOK.md`, missing schema examples, no per-phase closure criterion, list duplication between STATUS and ROADMAP) were not addressed in this pass.
- `CHANGELOG.md` was not updated; that reconciliation is left to a separate pass.
- `STATUS.md` "Status date" remains 2026-05-17 while this log is dated 2026-05-18.

## Next recommended action

1. Decide whether ROADMAP Phase 1 should keep duplicating the STATUS active doctrine list or point to STATUS as the single source of truth.
2. Add a correspondence table between ROADMAP Phase 0-6 and MIGRATION_PLAYBOOK Phase C/D/E and 8 lots.
3. Add per-phase closure criteria in ROADMAP, modeled on MIGRATION_PLAYBOOK "Critère d'arrêt for Phase C".
4. Refresh `STATUS.md` Status date to 2026-05-18 when next reconciliation pass occurs.
