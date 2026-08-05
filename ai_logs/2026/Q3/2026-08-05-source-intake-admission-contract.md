# Source intake admission contract — 2026-08-05

Status: completed documentation trace — no implementation or activation.

## Objective

Record the canonical seam for preserving an incoming Source before project linking,
documentary ingestion or semantic understanding.

## Repository state checked

```text
Pantheon-Next
Dossier Situation Intake, adaptive project roadmap, ProjectClaim, Document and
Information boundaries are present.

pantheon-mvp
native Project identity, NAS/upload ingestion, Paperless bindings, source_documents,
document_versions and Source Inbox projections are present.
```

The existing ingestion paths are reused. No competing inbox, file store, extraction
pipeline or graph is introduced.

## Decisions

```text
Source
= canonical intake identity.

Pièce
= optional business/UX qualification for documentary Sources.

Document
= later documentary authority when applicable.

Information
= later professional content with independent meaning.
```

Minimum Project-link vocabulary:

```text
unassigned
suggested
linked
excluded
```

Candidate Project references carry `project_ref`, `score`, `basis`, `producer` and
`created_at`. A candidate never mutates Project membership by itself.

Attachments remain independent Sources. The relation owner is deliberately deferred
until the current graph and document relations are inventoried.

## Artifacts

```text
schemas/source_intake_admission.schema.yaml
docs/governance/SOURCE_INTAKE_ADMISSION.md
```

## Non-effects

```text
no runtime
no source ingestion
no file copy
no parsing
no Information creation
no Project creation
no Project mutation
no Evidence admission
no memory promotion
no APU mapping
```

```text
source preserved != source understood
project suggested != project linked
source linked != Document created
Document created != Information created
```
