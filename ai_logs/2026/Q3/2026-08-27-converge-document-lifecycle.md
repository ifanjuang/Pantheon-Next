# Converge document lifecycle authority

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: governed document lifecycle
Change level: semantic

## Objective

Reduce `DOCUMENT_LIFECYCLE_GOVERNANCE.md` to a current lifecycle-composition owner after its upstream source/document owners were converged in PR #778.

## Verified state before change

`main` was verified at `baf64ad43c27349786f629e06f3b631578a4f0f6` after PR #778.

The complete lifecycle document had previously been read through EOF. Before this change, its upstream owners were re-verified through the merged state:

- `DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md`;
- `SOURCE_INGESTION_RETRIEVAL_MODEL.md`;
- `RAW_DERIVED_GOVERNED_RECORDS.md`;
- `schemas/document_knowledge_slice.schema.yaml`;
- current source/document convergence tests.

## Observed issues

The lifecycle mixed several responsibilities:

- source/document/Knowledge lifecycle composition;
- duplicate conceptual record shapes;
- OpenWebUI product ownership;
- a named Hermes Skill candidate and operation inventory;
- provider/model/vector-store candidate lists;
- delivery phases and implementation backlog;
- implementation questions that were no longer safe to treat as current repository truth.

This made the file overlap existing schemas and owners and encouraged historical bindings to look architectural.

## Change

- retain lifecycle purpose, source/intake/derivative/project/Knowledge/index/retrieval distinctions;
- make current owners and machine-schema authority explicit;
- keep conceptual lifecycle objects non-persistent unless separately reconciled;
- preserve exact-source identity/provenance, non-destructive versioning and idempotency references;
- preserve external execution, runtime observation, progress/freshness and processing-attestation boundaries;
- preserve Gates A-G and human consequential-decision requirements;
- remove OpenWebUI ownership, named Skill/provider/model/vector-store assumptions and delivery roadmap;
- require exact-SHA current implementation verification before implementation/adoption/activation claims;
- acknowledge the deliberate large reduction and add regression tests.

No schema or runtime file was modified.

## Invariants

```text
source != derivative
source != Card
Knowledge != Evidence
retrieval != truth
runtime observation != governance state
runtime success != authorization
projection != persistence
processing attestation != professional Evidence
index publication != source retention
```

## Exit criteria

- lifecycle contains no OpenWebUI dependency or named provider/runtime binding ownership;
- current machine shapes remain with `document_knowledge_slice.schema.yaml`;
- source/derivative/Knowledge/index/retrieval/Evidence boundaries remain explicit;
- gates and human consequential decisions remain explicit;
- no runtime, queue, scheduler, vector store or automatic approval path is introduced;
- CI/review are green on the exact PR head before merge.
