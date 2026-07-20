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
```

A Project Document Card has a required `parent_project_id` and points to the NAS original. A Knowledge Card projects either a Markdown subject or a structured referential record. A plant catalogue may therefore generate one specialized Knowledge Card per plant without one Markdown file per plant.

```text
referential knowledge ⊂ knowledge
```

```text
card != source
card != evidence
card != memory
```

## Automatic knowledge publication decision

Human validation is not mandatory for conversion or publication as Knowledge.

Hermes may publish a converted Markdown note automatically with a visible state such as `generated_unreviewed`, provided that the original and provenance remain preserved and no existing note is silently overwritten or merged.

Human validation remains required for destructive replacement, Evidence admission, Registre Probatoire promotion, consequential professional reliance and external action.

```text
automatic Knowledge publication != automatic truth
automatic Knowledge publication != Evidence
automatic Knowledge publication != governed memory
```

## Minimal open-source stack decision

The user selected the simplified target stack:

```text
Pantheon PWA + open-source Tiptap editor
PostgreSQL + pgvector
Hermes
Docling / Docling Serve
NAS
```

Responsibility is deliberately narrow:

```text
NAS          originals and delivery/contractual exports
PostgreSQL   cards, issues, metadata, structured CCTP, versions and chunks
pgvector     embeddings on PostgreSQL chunk records
Pantheon     editing, cards, consultation and mobile offline surface
Hermes       bounded orchestration and knowledge operations
Docling      local document extraction and structure understanding
```

Docling is selected as the primary parser. Alternative converters, a separate vector database, SilverBullet, Yjs and Hocuspocus are deferred until testing demonstrates a need.

Ordinary project documents do not receive a permanent visible Markdown and JSONL derivative set by default. Their original remains on the NAS; derived structure, provenance, chunks and embeddings belong in PostgreSQL. Markdown is persisted when content is intentionally published as reusable editorial Knowledge.

This is an adopted architecture direction, not proof of deployment. The repository already contains a Docling resource catalog entry and a PyMuPDF-based ingestion prototype, but does not yet prove a live Docling service, a production pgvector writer, a Tiptap editor or offline synchronization.

## Repository effect

This trace supports the candidate organization documented in `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`.

It records a human choice but does not claim that NAS folders, files, PostgreSQL/pgvector, Tiptap, SilverBullet, Docling, OCR, vectorization, Hermes ingestion, PWA synchronization or any connector has been installed or activated.

No runtime, schema, test, CI, approval engine, memory engine, scheduler, queue or external action is created.
