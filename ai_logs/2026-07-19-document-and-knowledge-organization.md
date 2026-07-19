# Architecture document and knowledge organization decision

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

Date: 2026-07-19.

## Human decision recorded

The user selected a shallow project-document hierarchy on the NAS:

```text
00_GESTION
10_CONCEPTION
20_AUTORISATIONS
30_DCE
40_MARCHES
50_CHANTIER
60_RECEPTION
90_SINISTRES
```

Project filenames follow:

```text
PROJET_INDICE_PHASE_DISTRIBUTEUR_TYPE_OBJET_DATE.ext
```

The user also selected a separate Markdown-only reusable Knowledge corpus:

```text
Référentiels
Responsabilité
Méthodologie
Techniques
Réglementations
```

Knowledge filenames use a free subject title, without mandatory project name, index, phase, distributor, type prefix or date.

Project originals remain on the NAS. Project documents are not converted into the reusable Markdown corpus by default. Large catalogues such as a plant dictionary may remain structured data with Markdown views.

## Card decision

Cards are retained as generated projections rather than files:

```text
Project Document Card
Knowledge Card
Referential Card
```

A Project Document Card points to the NAS original. A Knowledge Card points to a Markdown subject. A Referential Card may be generated from structured data, including one plant card per record without one Markdown file per plant.

```text
card != source
card != evidence
card != memory
```

## Repository effect

This trace supports the candidate organization documented in `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`.

It records a human choice but does not claim that NAS folders, files, PostgreSQL, SilverBullet, OCR, vectorization, Hermes ingestion or any connector has been installed or activated.

No runtime, schema, test, CI, approval engine, memory engine, scheduler, queue or external action is created.
