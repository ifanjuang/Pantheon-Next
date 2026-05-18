# Roadmap Phase 1 Workflow and RAG Reconcile

Date: 2026-05-18

## Scope

Reconcile `docs/governance/ROADMAP.md` Phase 1 active doctrine list with `docs/governance/STATUS.md` and `docs/governance/README.md`.

Files changed:

- `docs/governance/ROADMAP.md`.

## Finding

`ROADMAP.md` Phase 1 "Implemented active doctrine" list omitted two documents already listed as active governance in `STATUS.md` and indexed in `docs/governance/README.md`:

- `docs/governance/MARKDOWN_DOSSIER_WORKFLOW.md`;
- `docs/governance/RAG_INGESTION_PIPELINE.md`.

Both files exist and are present in the active governance list of `STATUS.md` and in the governance index under their boundary sections (Document workflow support, RAG ingestion support).

## Change

The two entries were inserted in the Phase 1 "Implemented active doctrine" list, between `REQUEST_ORCHESTRATION.md` and `HERMES_INTEGRATION.md`, matching the ordering used in `STATUS.md`.

No other section was modified.

## Doctrine boundary

No runtime was introduced.

`MARKDOWN_DOSSIER_WORKFLOW.md` remains documentation-level governance only. It does not implement an editor, runtime, plugin, OpenWebUI extension or Hermes tool.

`RAG_INGESTION_PIPELINE.md` remains documentation-level governance only. It does not implement PDF parsing, OCR, chunking, indexing, an OpenWebUI plugin, a Hermes tool, a scheduler, a queue or an ingestion runtime.

## Note on prior attempt

A previous PR (#14, branch `claude/repo-audit-HWbAd`) carried the same reconciliation against an earlier `main` state. It is now superseded by this branch, which is based on the current `main` HEAD (post `EXECUTION_DISCIPLINE.md` migration).

## Risks and limitations

- This reconciliation does not address the broader audit findings (phase vocabulary mismatch with `MIGRATION_PLAYBOOK.md`, missing schema examples, no per-phase closure criterion, list duplication between STATUS and ROADMAP).
- `CHANGELOG.md` is not updated; that reconciliation is left to a separate pass.

## Next recommended action

1. Consider whether ROADMAP Phase 1 should keep duplicating the STATUS active doctrine list or point to STATUS as the single source of truth.
2. Close PR #14 in favor of this branch.
