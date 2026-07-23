# 2026-07-23 — Governed document production extension

Status: validation-only intervention trace.

## Request

The maintainer extended the document-lifecycle proposal with a production path.

The target must allow a document to be produced from:

- a list of notes;
- a scanned draft;
- a voice recording or dictated account;
- a meeting transcript;
- supplied text;
- text to insert into an existing document;
- existing project or Knowledge sources.

The maintainer then required a firm gate:

```text
A produced document must be reviewed before sectorization and archiving.
```

## Decision recorded

A separate companion candidate was added rather than compressing ingestion and production into one undifferentiated pipeline.

```text
ingestion
= derive representations from an existing source

document production
= compose a new versioned draft from heterogeneous source material and instructions
```

The production lifecycle introduces candidate concepts for:

- Production Request;
- Production Source Set;
- Production Brief;
- Draft Document and Draft Version;
- segment-level provenance;
- Review Record;
- Correction Request;
- Sectorization Record;
- Archive Record;
- Distribution Record.

## Mandatory review gate

The documented sequence is:

```text
draft generated
-> review required
-> reviewed or corrections requested
-> exact reviewed version selected
-> sectorization authorized
-> archive authorized
```

Sectorization includes assignment to:

- one or more projects;
- a project phase;
- general Knowledge;
- a Knowledge family;
- a governed document type or other organizational sector.

Archiving and distribution remain separate decisions.

```text
reviewed != archived
sectorized != archived
archived != distributed
```

## Files changed

- added `docs/governance/DOCUMENT_PRODUCTION_LIFECYCLE.md`;
- indexed it in `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`;
- added this intervention trace.

## Classification

```text
authority class: candidate support doctrine
repository state: documented non-implemented
runtime status: unchanged
protected paths touched: none
installation or activation: none
```

## Boundary

Pantheon governs draft status, review, sectorization, archive and distribution conditions.

Hermes may transcribe, OCR, structure, draft, revise and render through separately reviewed external bindings.

The Cockpit may expose sources, progress, drafts, diffs, review actions and blocking reasons.

The human reviews the exact draft version before sectorization and archiving.

This change implements no transcription engine, OCR engine, editor, renderer, archive service, sender, Hermes Skill, queue, scheduler, schema, API or Cockpit UI.
