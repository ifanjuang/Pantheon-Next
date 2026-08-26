# RAG / Retrieval Ingestion Pipeline

Status: active support proposal — provider-agnostic ingestion and retrieval preparation boundary.

Pantheon does not require a canonical RAG stack.

This document defines only the invariants that must survive whichever ingestion/retrieval implementation is selected.

## Core rule

```text
source can become retrievable
retrievable != true
indexed != Evidence
retrieved != authorized
```

A deployment may use direct Hermes file/context access, the co-located PostgreSQL/pgvector candidate, the qualified Obsidian/Hindsight reference, or another compatible retrieval implementation.

Pantheon governs the boundary, not the product choice.

## Required ingestion invariants

Any document-retrieval path used for consequential work should preserve:

```text
exact source identity
source digest/version when available
bounded task/source scope
conversion/extraction provenance
retrieval-unit identity
source locator/page/section when available
quality/uncertainty flags
reviewable retrieval trace when consequential
```

Forbidden shortcuts:

```text
uploaded -> validated
converted -> approved
chunked -> Evidence
indexed -> Evidence
retrieved -> truth
retrieval score -> approval
```

## Valid deployment profiles

### 1. Hermes-native / direct-source profile

Use no additional RAG subsystem when direct bounded context is sufficient.

```text
identified files / project context
-> Hermes bounded read/context use
-> candidate reasoning/output
```

This is a valid architecture, not a degraded fallback.

### 2. Current co-located document-retrieval candidate

The executable candidate under `implementation/` currently demonstrates:

```text
local/NAS source
-> Task Contract scope enforcement
-> Docling or direct-text conversion
-> PostgreSQL source/extraction provenance
-> scoped chunks
-> pgvector embeddings/retrieval
-> candidate Knowledge/document projections
```

The implementation enforces source scope before retrieval ranking and persists contract, ingestion and source provenance on retrieval units.

This is a tested Pantheon implementation candidate. It is not a requirement that every Pantheon deployment use PostgreSQL, pgvector or Docling.

### 3. Qualified external workspace/retrieval recommendation

When a user wants a richer note/workspace and semantic recall layer, the strongest currently demonstrated external composition is:

```text
Obsidian / Markdown
-> Self-hosted LiveSync / CouchDB when synchronization is needed
-> filesystem vault mirror
-> hindsight-obsidian-sync
-> Hindsight
-> bounded Hermes consumer
```

That path is documented in `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` and is recommended because it has real qualification/regression evidence.

It remains optional and replaceable.

## Parser / extraction posture

Docling is currently the preferred document-structure extraction candidate because the co-located implementation already uses and tests that seam.

Other parsers may be selected for a demonstrated corpus need.

```text
parser success != source truth
OCR output != Evidence
structured extraction != professional validation
```

Do not create a universal converter router unless representative corpus testing demonstrates the need.

## Retrieval implementation posture

Pantheon does not require a particular:

- vector store;
- embedding model;
- reranker;
- knowledge graph;
- chunker;
- retrieval framework;
- memory provider.

A replacement must preserve scope and provenance behavior rather than file formats or product APIs.

```text
implementation replaceable
invariants stable
```

## Chunking and retrieval units

Chunking is an implementation technique, not an authority transition.

A retrieval unit should remain traceable to its source representation. If a claim spans several pages/sections or depends on a table/image, retrieval should preserve enough localization to review the underlying source rather than treating a chunk as self-sufficient proof.

## Knowledge publication

Derived Markdown, summaries or structured representations do not automatically become governed Knowledge.

```text
retrieval derivative
-> candidate material
-> existing Knowledge review/publication owner when durable Knowledge is wanted
```

A workspace note may remain a working note indefinitely without being promoted.

## Evidence boundary

`RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` owns the evidence-specific interpretation around retrieval, context sufficiency and Evidence Candidates.

This pipeline must not duplicate Evidence admission or approval logic.

## External-provider rule

Select an additional RAG/retrieval provider only when a concrete capability gap exists, for example:

- corpus size or search quality exceeds native/direct-source behavior;
- semantic cross-document recall is actually needed;
- shared workspace retrieval is desired;
- provider-specific access/filtering is required;
- a specialist multimodal retrieval capability is justified.

Prefer an already-qualified implementation before introducing a new parallel stack when it meets the requirement.

## Current recommendations

```text
No extra retrieval needed
-> Hermes native/direct bounded source access

Pantheon document retrieval candidate needed
-> current implementation/ Docling + PostgreSQL/pgvector path

External workspace + semantic recall desired
-> qualified Obsidian + Hindsight reference composition

Different demonstrated need
-> select another replaceable binding through HERMES_CAPABILITY_BINDINGS.md
```

## Final rule

```text
Pantheon requires provenance and bounded scope, not RAG branding.
Keep the paths that are already demonstrated.
Add a provider only for a real gap.
Retrieval remains candidate support until Evidence and approval owners say otherwise.
```