# Source ingestion and retrieval reconciliation

Date: 2026-07-13
Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

`docs/governance/SOURCE_INGESTION_RETRIEVAL_MODEL.md` was hardened under issue #366.

The model remains subordinate to `RAW_DERIVED_GOVERNED_RECORDS.md` and only specializes the governed path from Source through derived representation and retrieval to Evidence Candidate.

## Why

The earlier draft mixed connector inventory, storage posture, OCR, Markdown, indexing, vectorization, evidence, decision and memory in one large model. It also classified the external `pantheon-mvp` retrieval loop as both implemented and partial without naming the implementation layer.

The revised model separates Pantheon documentation from externally observed implementation, partial integration and non-implemented capabilities.

## External observation

Repository: `ifanjuang/pantheon-mvp`
Observed commit: `0c2d216c0eea7a0c78e754a44270b0e836656364`
Observation date: 2026-07-13
Review scope: scoped retrieval, candidate production, local fixture / pgvector posture and visible register-seam hardening.

No pull-request-triggered workflow run was returned for that exact merge commit by the available workflow query. CI evidence is therefore recorded as not established for this observation.

## Classification

```text
implemented in Pantheon Next:
- documentation model;
- declarative catalogue entries;
- static review projections;
- validation trace and authority coverage.

externally observed / verified candidate:
- scoped retrieval and candidate production in pantheon-mvp at the pinned commit.

partial integration:
- conformance evidence and bounded handoff posture;
- fixture-backed demonstration without adopted live binding.

documented non-implemented in Pantheon Next:
- generic Source Registry;
- live connectors;
- generic ingestion and retrieval runtime;
- Docling live binding;
- production source cockpit.
```

## Boundary

No connector, credential, OAuth flow, OCR pipeline, vector database, scheduler, queue, runtime, approval engine, memory engine, schema, test or external action is introduced.

## Distinctions

```text
Source != Evidence
retrieved != true
ingested != Register Entry
binding selected != dependency adopted
runtime success != evidence
external implementation != Pantheon implementation
verified != adopted
integrated != activated
merged != promoted
```
