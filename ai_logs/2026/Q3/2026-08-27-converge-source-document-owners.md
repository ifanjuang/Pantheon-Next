# Converge source and document upstream owners

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: source access, document-to-Knowledge contract, layered records
Change level: semantic

## Objective

Converge the upstream source/document governance owners before modifying `DOCUMENT_LIFECYCLE_GOVERNANCE.md`, so the lifecycle does not point to owners that still embed the retired OpenWebUI boundary or stale external implementation observations.

## Verified state before change

`main` was verified at `547ab692ea069c89abeac6432524f62db4934b32` after PR #777.

The following current owners were read before modification:

- `docs/governance/DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md`;
- `docs/governance/SOURCE_INGESTION_RETRIEVAL_MODEL.md`;
- `docs/governance/RAW_DERIVED_GOVERNED_RECORDS.md`;
- `schemas/document_knowledge_slice.schema.yaml`;
- tests covering the document/Knowledge schema;
- current `implementation/mvp_vertical/` directory and a bounded code search for the older `scoped_retrieval` wording.

No open PR was found covering this exact owner slice.

## Observed issues

- `DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md` still assigned exposure to OpenWebUI even though its machine-readable contract is transport-neutral.
- `SOURCE_INGESTION_RETRIEVAL_MODEL.md` still named OpenWebUI as exposure and upload source and mixed a dated external `pantheon-mvp` observation into current implementation posture.
- `RAW_DERIVED_GOVERNED_RECORDS.md` still named an OpenWebUI upload area and repeated technology/product examples that are not authority.
- `schemas/document_knowledge_slice.schema.yaml` already owns the seven machine-readable record families and their non-authority boundaries; it did not need modification.

## Change

- preserve the complete document-to-Knowledge schema contract, provenance, idempotency and non-authority rules;
- replace product-specific exposure language with replaceable runtime interaction plus governed Cockpit/Card projection;
- preserve linked/cached/ingested source-access modes and the Retrieval Trace -> Evidence Candidate boundary;
- remove the dated external `pantheon-mvp` implementation snapshot from current doctrine and require current repository/module/test verification before implementation claims;
- retain the seven-layer raw/derived/governed/retrieval/provenance/Evidence/approval model while removing product-specific storage/cockpit assumptions;
- acknowledge the deliberate reduction of `RAW_DERIVED_GOVERNED_RECORDS.md` in the truncation registry;
- add targeted convergence tests.

## Invariants

```text
Source != Evidence
Derived Representation != Source
retrieved != truth
projection != persistence
card != source
knowledge publication != Evidence admission
memory != Evidence
runtime success != authorization
external observation != current implementation
schema contract != adopted persistence
```

## Deferred

`DOCUMENT_LIFECYCLE_GOVERNANCE.md` remains unchanged until these upstream owners merge. `OPENWEBUI_INTEGRATION.md` remains present while active consumers and mandatory governance-file checks still require it.

## Exit criteria

- no OpenWebUI dependency remains in the three upstream owners;
- `schemas/document_knowledge_slice.schema.yaml` remains unchanged;
- source, provenance, retrieval, Evidence and approval distinctions remain intact;
- stale external implementation observation is not presented as current repository truth;
- CI and review are green on the exact PR head before merge.
