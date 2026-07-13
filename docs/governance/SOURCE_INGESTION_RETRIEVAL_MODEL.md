# Source Ingestion and Retrieval Model

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

This document defines a bounded governance view of source access, derived representations, indexing and retrieval. It does not create a connector runtime, ingestion engine, OCR pipeline, vector database, scheduler, queue, memory engine or approval engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```

## Jurisdiction

`RAW_DERIVED_GOVERNED_RECORDS.md` remains owner of the layered data model.

This document only specializes the path:

```text
Source
→ Derived Representation Candidate
→ bounded retrieval object
→ Retrieval Trace
→ Evidence Candidate when selected for a scoped assertion
```

It does not redefine Capability, Resource, Preset, Binding, Provisioner, Evidence, Decision, Register Candidate or Register Entry.

## Source access modes

A source may be exposed through one of three modes:

```text
linked
= original remains in its external system and is accessed by reference.

cached
= a temporary bounded copy is materialized for processing.

ingested
= a governed local representation is retained under an explicit scope and policy.
```

These modes are operational postures, not authority levels.

```text
linked != approved
cached != retained
retained != Register Entry
ingested != evidence
```

## Source identity

Every source projection should preserve, where available:

```text
source_id;
source_system;
original_uri or stable reference;
digest;
mime type;
scope;
confidentiality;
version or modification time;
access mode;
observed_at;
status.
```

The original source remains superior to its extracted text, OCR, summary, chunk or embedding.

## Derived representations

A derived representation may include:

```text
OCR text;
extracted text;
Markdown;
structured table candidate;
layout map;
summary candidate;
chunk set;
embedding reference.
```

Each derivative must retain:

```text
derived_from;
method and version;
source page or region where applicable;
created_at;
confidence where meaningful;
scope and confidentiality inherited from the source.
```

```text
OCR != truth
Markdown != original
summary != evidence
embedding != memory
```

## Retrieval progression

Retrieval should remain progressive and bounded:

```text
1. apply Case, Situation, scope and confidentiality filters;
2. use structured identifiers and native search where available;
3. use full-text search;
4. use semantic or vector retrieval only when useful;
5. return source-linked candidates;
6. verify consequential claims against the original source.
```

Vectorization is selective. A source does not need embeddings merely because it exists.

## Retrieval output

A retrieval result should expose:

```text
source reference;
derived representation reference;
matched passage or structured item;
retrieval method;
score where applicable;
scope;
confidentiality;
retrieved_at;
query or task reference.
```

A `Retrieval Trace` records how material was found. It does not prove the returned claim.

```text
retrieved != true
high score != authority
runtime success != evidence
```

## Evidence boundary

A retrieved passage becomes an `Evidence Candidate` only when it is deliberately selected to support or contradict a scoped Assertion and retains sufficient provenance.

```text
retrieval result
→ selection for one Assertion
→ Evidence Candidate
→ Gate or Human Decision where consequential
```

No retrieval pipeline may self-promote a result to accepted Evidence or durable Register memory.

## Multi-source posture

Candidate source systems may include:

```text
Google Drive;
Gmail;
Notion;
GitHub;
Slack;
NAS or filesystem;
OpenWebUI upload;
web source;
professional database or API.
```

Their presence in this list does not mean a connector is installed, approved, healthy, safe or activated.

Each concrete connector remains an external Hermes-side or provider-side binding governed through Pantheon scope, credentials posture, evidence expectations and human gates.

## Docling and document analysis

Docling or another document-analysis resource may produce a `Derived Representation Candidate`.

```text
Docling available != selected
binding selected != dependency adopted
extraction success != source truth
```

The catalogue remains owner of Docling Capability, Resource and Preset declarations.

## External observation record

The external `ifanjuang/pantheon-mvp` repository was observed on 2026-07-13 at commit:

```text
0c2d216c0eea7a0c78e754a44270b0e836656364
```

Review scope for this document:

```text
- scoped retrieval and candidate-production behavior;
- local fixture and pgvector-backed demonstration posture;
- register-seam hardening visible in the observed commit history;
- no claim of generic connector support;
- no claim of Pantheon adoption, activation or production readiness.
```

No pull-request-triggered workflow run was returned for that exact merge commit through the available GitHub workflow query at observation time. This absence is recorded as `CI evidence not established for this observation`, not as failure and not as success.

```text
observed externally != implemented in Pantheon Next
implemented externally != integrated
verified behavior != evidence accepted
integrated != adopted
adopted != activated
```

## Implementation and integration posture

```text
implemented in Pantheon Next:
- this documentation model;
- declarative Google Drive and Docling catalogue entries;
- static catalogue and review projections;
- validation traces and authority-index coverage.

externally observed / verified candidate:
- scoped retrieval and candidate production in ifanjuang/pantheon-mvp at the pinned commit above;
- local fixture and pgvector-backed behavior observed within the bounded review scope.

partial integration:
- conformance evidence between the external loop and Pantheon governance contracts;
- bounded handoff assumptions;
- fixture-backed demonstration without adopted live binding.

documented non-implemented in Pantheon Next:
- generic Source Registry;
- live Google Drive ingestion;
- generic connector framework;
- Docling live binding;
- OCR orchestration;
- generic multi-source retrieval resolver;
- production OpenWebUI source cockpit.
```

No item appears simultaneously as implemented in Pantheon Next and partial integration.

## Core invariants

```text
Source != Evidence
Derived Representation Candidate != Source
Retrieval Trace != proof
embedding != Register
connector present != connector approved
healthy != safe
Hermes execution != Pantheon validation
external implementation != Pantheon implementation
verified != adopted
observed != integrated
integrated != activated
```

## Boundary

Pantheon governs source scope, access posture, candidate status, provenance expectations, gates and durable retention decisions.

Hermes Agent or another approved external runtime performs connector access, extraction, conversion and retrieval under an explicit bounded handoff.

OpenWebUI exposes source, retrieval, evidence and decision projections.

The human decides consequential reliance, external action and durable promotion.
