# 2026-07-23 — Paperless-ngx document runtime candidate

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Request

The maintainer asked whether Hermes and Paperless-ngx are compatible and whether the Pantheon Cockpit may use Paperless for Documents and Knowledge while keeping documents classifiable and subsequently usable by Hermes.

The resulting direction is to treat Paperless-ngx as an external document-management runtime rather than as Knowledge, Evidence, a Pantheon runtime or a replacement for Docling.

## Active Pantheon documents read

The intervention was reconciled against the current repository state, including:

- `docs/governance/STATUS.md`;
- `docs/governance/WHAT_RUNS.md`;
- `docs/governance/AUTHORITY_INDEX.md`;
- `docs/governance/MODULES.md`;
- `docs/governance/README.md`;
- `CONTRIBUTING.md`;
- `docs/governance/STATUS_HEADER_RULES.md`;
- `docs/governance/BOUNDARY_PROFILES.md`;
- `docs/governance/NON_EQUIVALENCE_RULES.md`;
- `docs/governance/HERMES_INTEGRATION.md`;
- `docs/governance/HERMES_CAPABILITY_BINDINGS.md`;
- `docs/governance/DOCUMENT_LIFECYCLE_GOVERNANCE.md`;
- `docs/governance/SOURCE_INGESTION_RETRIEVAL_MODEL.md`;
- the current declarative capability/resource catalog schemas and examples.

## Upstream Paperless observation

Observed on 2026-07-23:

```text
repository: paperless-ngx/paperless-ngx
default branch: dev
commit: c9443e890f63d98ce64ee275c2dc2e62770c9187
```

Relevant upstream surfaces observed in the repository documentation and code include:

- REST API authentication, document search and upload;
- asynchronous consumption task identifiers and task-status lookup;
- document file versions;
- original-file preservation and archive representations;
- OCR and extracted searchable text;
- tags, document types, custom fields and object permissions;
- email ingestion;
- native background task processing;
- webhook actions;
- optional AI/LLM/vector features;
- optional remote OCR.

Upstream functionality is evidence of external implementation only. It does not establish a Pantheon binding, target installation, health, safety, adoption or activation.

## Decision recorded

A new abstract Capability Slot is proposed:

```text
document_source_management
```

with Paperless-ngx as preferred candidate resource.

Placement:

```text
Paperless-ngx
= external source/document runtime and backing store candidate

Hermes
= governed orchestration, analysis, classification candidate production and authorized mutation

Docling / specialist OCR
= separately selected document-analysis resources

Pantheon
= source identity expectations, scope, gates, lifecycle status, Knowledge/Evidence boundaries

Cockpit / OpenWebUI
= document and Knowledge exposure plus intent capture

Human
= consequential adoption, activation and review decisions
```

## Key distinctions

```text
Paperless document != Knowledge Item
Paperless metadata != canonical project classification
Paperless OCR != source truth
Paperless search hit != Evidence
Paperless task success != professional validation
Paperless health != safety
Paperless installed != approved
binding selected != dependency adopted
```

Paperless tags, document types or custom fields may mirror governed metadata for operational search, but the canonical many-to-many project/phase and Knowledge relations remain outside Paperless.

## Initial AI/remote posture

The initial candidate keeps Paperless optional AI/LLM/vector features and remote OCR outside the admitted path unless separately reviewed.

```text
upstream feature present != Pantheon activation
remote provider available != external transmission authorized
```

## Files changed

- added `docs/governance/PAPERLESS_NGX_DOCUMENT_RUNTIME.md`;
- indexed it in `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`;
- added `catalog/capabilities/document-source-management.yaml`;
- added `catalog/resources/paperless-ngx.yaml`;
- added this validation-only intervention trace.

## Classification

```text
authority: candidate support doctrine + validation-only trace
catalog state: candidate declarations
runtime state: unchanged
protected paths touched: none
installation: none
activation: none
real-dossier authorization: none
external mutation performed: none
```

## Non-effects

This intervention does not:

- install Paperless-ngx;
- create Docker or deployment material;
- create or store credentials;
- implement a Hermes Skill or REST client;
- modify `pantheon-mvp`;
- create a Cockpit Paperless adapter;
- enable Paperless AI, RAG or remote OCR;
- authorize source deletion;
- authorize Knowledge publication;
- promote Evidence or memory;
- change the current runtime-status claims in `WHAT_RUNS.md`.

## Next implementation seam

Executable work remains external to Pantheon Next:

```text
ifanjuang/pantheon-mvp
-> bounded Paperless read adapter + Document/Knowledge projections

Hermes-side runtime or sibling executable repository
-> paperless_documents binding + pantheon-document-intake orchestration

operator deployment
-> Paperless installation, credentials, networking, backup and health checks
```

A later adoption decision should be based on bounded conformance scenarios, target-runtime security posture, backup/restore evidence and explicit human approval.