# Pantheon Next — Source and Retrieval Authority Index

Status: candidate support map — populated; awaiting review.

This sub-index classifies the bounded source-ingestion and retrieval support model. It does not override `docs/governance/AUTHORITY_INDEX.md`, promote the document, implement a connector, or create a retrieval runtime.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `docs/governance/SOURCE_INGESTION_RETRIEVAL_MODEL.md` | candidate support doctrine | documented non-implemented | Bounded specialization of `RAW_DERIVED_GOVERNED_RECORDS.md` for source posture, derived representations, progressive retrieval, Retrieval Trace and evidence selection. No connector, OAuth flow, OCR pipeline, vector database, retrieval runtime, scheduler, queue, approval engine, memory engine, schema, test or external action. |

## Boundary

```text
indexed != promoted
retrieved != true
ingested != Register Entry
binding selected != dependency adopted
```
