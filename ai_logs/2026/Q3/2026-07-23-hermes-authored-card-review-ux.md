# 2026-07-23 — Hermes-authored card review UX

Status: validation-only intervention trace.

## Request

The maintainer requested a transverse Cockpit rule for every content-bearing card whose primary content was materially drafted, rewritten, synthesized or enriched by Hermes.

The requested behavior is:

```text
Hermes-authored content
-> card promoted as BROUILLON before validation
-> recto with concise draft identity and index
-> verso/details with the complete document
-> direct editing or comments requesting correction, improvement, detail or enrichment
-> comments sent to Hermes as bounded revision requests
-> new traceable draft version returned
-> exact human validation
-> visible message that finalization was sent to Hermes
-> archive, chunking, embeddings and index publication as authorized
-> ordinary card appearance only after finalization completes
-> active index remains visible
-> later modification creates a new index without deleting the prior one
```

The maintainer explicitly distinguished this from faithful OCR, format conversion, Markdown normalization and sectorization.

## Documents consulted

- `docs/governance/DOCUMENT_PRODUCTION_LIFECYCLE.md`;
- `docs/governance/DOCUMENT_LIFECYCLE_GOVERNANCE.md`;
- `docs/governance/CARD_STACK_MODEL.md`;
- `docs/governance/PANTHEON_COCKPIT_UX_SPEC.md`;
- `docs/governance/KNOWLEDGE_NAVIGATION_UX.md`;
- `docs/domain-packs/architecture/PROJECT_NAVIGATION_UX.md`;
- `docs/governance/ITERATIVE_DELIBERATION_LIFECYCLE.md`;
- `docs/governance/WORK_ISSUE_AND_DELEGATED_MERGE_MODEL.md`;
- `docs/governance/HERMES_INTEGRATION.md`.

## Decision recorded

A new transverse candidate specification was added:

- `docs/governance/HERMES_AUTHORED_CARD_REVIEW_UX.md`.

It distinguishes:

```text
faithful transformation
= OCR, extraction, conversion, normalization, chunking or sectorization without
  material editorial authorship

material Hermes authorship
= drafting, rewriting, synthesis, expansion, enrichment, semantic merge,
  insertion or material reorganization of retained primary content
```

Only material authorship automatically triggers the full Draft Card editorial review state. Faithful transformation may still require extraction-quality review.

## UX decisions

The Draft Card is a temporary transverse state, not a permanent card family.

It is promoted in an `À relire` surface and exposes:

- persistent `BROUILLON` marker;
- target index;
- internal draft revision;
- full content on the reverse/details surface;
- direct editing;
- anchored comments;
- structured Hermes revision requests;
- version diff;
- exact validation;
- finalization progress.

The index model separates:

```text
public index: A, B, C or project-defined
working revision: v1, v2, v3 inside one target index
```

Example:

```text
Indice A · Brouillon v3
Indice A · Validé
Indice A · Finalisé
Indice B · Brouillon v1 while A remains active
```

## Finalization boundary

Validation applies to one exact card, target index, Draft Version and content hash.

A visible, declared finalization bundle may include:

- freezing validated Markdown;
- rendering outputs;
- sectorization;
- archive;
- chunking;
- embeddings;
- index publication;
- retrieval verification.

Distribution remains separate unless explicitly governed.

The card does not take its ordinary retained appearance until the required finalization steps are observed as complete.

## Structured-directory exception

Project identity, Contacts and Entreprises cards may contain Hermes-proposed structured fields without turning the entire directory card into a document-style Draft Card.

Field-level candidate review remains appropriate unless the card's primary payload is an authored textual artifact.

## Classification

```text
authority class: candidate support specification
repository state: documented non-implemented
runtime state: unchanged
protected paths touched: none
schema or test change: none
installation or activation: none
```

## Non-effects

This intervention creates no:

- card component;
- editor;
- comment engine;
- revision worker;
- Hermes Skill;
- archive service;
- chunker;
- embedding runtime;
- vector store;
- approval engine;
- external action.
