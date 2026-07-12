# Source ingestion and retrieval reconciliation

Date: 2026-07-12
Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

A clean bounded replacement for historical PR #341 was added as `docs/governance/SOURCE_INGESTION_RETRIEVAL_MODEL.md`.

The model is intentionally subordinate to `RAW_DERIVED_GOVERNED_RECORDS.md` and only specializes the governed path from Source through derived representation and retrieval to Evidence Candidate.

## Why

The historical PR mixed connector inventory, storage posture, OCR, Markdown, indexing, vectorization, evidence, decision and memory in one large model. Since then, Pantheon Next gained owner documents for catalogue objects, graph relationships, evidence, decisions, Register and provisioner handoffs.

The clean replacement avoids redefining those owners.

## Classification

```text
implemented:
- documentation;
- validation trace.

partial:
- external pantheon-mvp scoped retrieval loop;
- static catalogue and review projections.

documented non-implemented:
- generic Source Registry;
- live connectors;
- generic ingestion and retrieval runtime;
- Docling live binding;
- production source cockpit.
```

## Boundary

No connector, credential, OAuth flow, OCR pipeline, vector database, scheduler, queue, runtime, approval engine, memory engine, schema, test or external action is introduced.

## Local distinctions

```text
Source != Evidence
retrieved != true
ingested != Register Entry
binding selected != dependency adopted
runtime success != evidence
merged != promoted
```
