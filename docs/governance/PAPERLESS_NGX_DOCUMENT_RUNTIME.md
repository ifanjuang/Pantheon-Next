# Paperless-ngx Document Runtime Candidate

Status: candidate support doctrine — external DMS runtime with co-located Pantheon adapter candidate / target installation not established.
Boundary profile: candidate_support_note.

This document classifies `paperless-ngx/paperless-ngx` as a candidate external document-management runtime for Pantheon Next. It is product-specific adapter material. It does not replace the tool-agnostic document lifecycle, source, Knowledge, Evidence, approval or memory models.

Historical upstream observation retained from the original review on 2026-07-23:

```text
repository: paperless-ngx/paperless-ngx
default branch: dev
observed commit: c9443e890f63d98ce64ee275c2dc2e62770c9187
license: GPL-3.0
```

That observation is provenance for the review, not a claim that the same upstream commit remains current.

Current Pantheon-side adapter placement is under `implementation/`. Former `ifanjuang/pantheon-mvp` PRs remain historical implementation provenance only; they are not a current owner or source checkout.

Non-equivalence rules apply: see `NON_EQUIVALENCE_RULES.md`.

## 1. Capability placement

```text
capability_id: document_source_management
function: capture, preserve, version, retrieve and expose professional source documents
preferred_binding: paperless-ngx/paperless-ngx
runtime owner: Paperless-ngx for native DMS operations
orchestration: Hermes for bounded governed work
Pantheon adapter: implementation/ gateway / PEP / projections
governed_by: Pantheon governance
approved_by: human where installation, activation, consequential mutation or real-dossier use requires approval
```

Paperless is optional. Governed local/NAS source ingestion remains a valid core path without it.

```text
capability_slot != installed_capability
binding_selected != dependency_adopted
installed != approved
healthy != safe
```

## 2. What Paperless may own

Paperless may own operational document functions such as:

- intake and preservation of source files;
- file versions, checksums and file metadata;
- native OCR/search text and thumbnails;
- full-text search;
- tags, correspondents, document types and custom fields;
- object-level permissions;
- email ingestion where separately selected;
- native task execution/status;
- Paperless-internal workflows;
- API access to documents and versions.

These runtime capabilities do not become Pantheon authority by being available.

## 3. What Paperless must not own

Paperless must not become the authority for:

```text
Pantheon Source identity
project identity
project-phase membership
multi-project document relationships
Knowledge publication
Knowledge authority
Evidence admission
professional correctness
approval
external-action authorization
Registre Probatoire memory
Pantheon capability activation
```

Paperless metadata may mirror governed metadata for operational search, but the mirror is not canonical merely because it is stored in Paperless.

```text
Paperless metadata != Pantheon business classification
Paperless OCR text != source truth
Paperless search hit != Evidence
Paperless task success != professional validation
```

## 4. Exact source capture

A governed Source Capture may refer to one exact Paperless document version:

```yaml
source_capture:
  source_id: src_example
  backing_resource: paperless_ngx
  external_document_id: "4182"
  external_version_id: "7"
  original_filename: CCTP_LOT03.pdf
  mime_type: application/pdf
  digest: sha256:example
  captured_at: 2026-07-23T12:00:00Z
  storage_reference: paperless://documents/4182/versions/7
  integrity_status: candidate_verified
```

Required invariants:

- one governed source reference identifies one exact captured version;
- a new Paperless version does not silently rewrite the earlier source identity;
- original bytes remain superior to OCR, Markdown, summaries, chunks and embeddings;
- removing an index/projection does not silently delete the source;
- source download remains subject to identity and source policy;
- Paperless IDs are backing-runtime identifiers, not Pantheon authority.

```text
latest pointer != immutable provenance
Paperless Source Capture != Evidence
```

## 5. Pantheon implementation adapter

Current candidate source is co-located under `implementation/`, including the bounded Paperless gateway/PEP path and related document projections.

Relevant responsibilities include:

```text
implementation/mvp_vertical/paperless_gateway.py
implementation/mvp_vertical/paperless_ingestion.py
implementation/mvp_vertical/policy_gate.py
implementation/mvp_vertical/policy_request.py
implementation/mvp_vertical/document_runtime_network_observer.py
implementation/openwebui/...
implementation/compose.paperless.yaml
```

Historical former `pantheon-mvp` PRs such as #56, #59, #84 and #85 remain useful provenance for when these slices were introduced. They are not current placement instructions.

```text
same repository != same authority
co-location != activation
implementation present != target deployed
```

## 6. Cockpit projection

The Cockpit may expose Paperless-backed documents without reproducing the Paperless administration interface.

A candidate Document Card may show:

```text
title
source type
page/file metadata when available
project links
phase links
document type
source availability
processing status
projection status
Knowledge publication status
warnings and blocking reasons
```

Candidate user actions may include preview, permitted original access, search, metadata inspection, Hermes analysis, classification proposals, project-link proposals, Knowledge-publication requests and reprocessing requests.

The primary Cockpit should not expose implementation-specific queues, Celery internals or Paperless administration concepts unless troubleshooting explicitly requires them.

```text
projection != persistence
visible action != authorized effect
```

## 7. Consequential mutation path

Read-only Paperless access may use the bounded adapter. Consequential mutations must follow the governed path:

```text
Cockpit intent
-> Task Contract / scope
-> Pantheon implementation PEP derives effect facts
-> Pantheon policy / decision validation
-> bounded Hermes/runtime request
-> Paperless REST mutation only when authorized
-> runtime observation
-> candidate result / governed status update
-> Cockpit projection
```

A free-form natural-language request must not be the only consequential execution contract.

Known runtime effect facts remain PEP-owned. Caller flags cannot downgrade a known external Paperless effect.

```text
caller request flag != executor fact
external Paperless executor -> external_effect = true
```

## 8. Hermes binding

Candidate higher-level binding:

```text
pantheon-document-intake
```

Current reviewed source is co-located at:

```text
implementation/hermes/skills/pantheon-document-intake/
```

Hermes remains the external installer/executor. It may inspect sources, retrieve an exact version, call the bounded gateway and return candidate outputs/runtime observations.

Hermes must not:

- treat Paperless metadata as approved classification;
- promote OCR or LLM output directly to Evidence;
- broaden project/confidentiality scope;
- delete/replace sources without the applicable gate;
- promote Knowledge or durable memory automatically;
- receive raw Paperless or PDP backing credentials through the skill.

```text
skill source present != installed
skill installed != activated
skill loaded != task authorized
```

## 9. Separation from Docling/OCR

Paperless and Docling occupy different responsibilities:

```text
Paperless-ngx
= source capture, document persistence, versions, basic OCR/search, DMS runtime

Docling
= structured document analysis, Markdown derivation, table extraction and layout-aware representations
```

Selection rule:

```text
native searchable content sufficient
-> Paperless/native extraction may be sufficient

structured representation required
-> use selected document-analysis binding such as Docling

poor scan / specialist OCR required
-> use a separately authorized OCR/VLM binding
```

Availability does not imply authorization or suitability for every source.

## 10. Classification and Knowledge boundaries

Hermes may produce Classification Candidates from exact sources and current governed context. After authorization, selected metadata may be mirrored into Paperless for search/operations.

Canonical many-to-many relationships remain outside Paperless:

```text
Document Record
-> Project Document Link A / phase
-> Project Document Link B / phase
```

A Paperless document is a Source, not a Knowledge Item.

```text
Paperless document/version
-> governed Source Capture
-> approved extraction / Projection
-> Knowledge Source Link
-> Knowledge candidate/update candidate
-> review/gate where required
-> index publication when authorized
```

```text
Source Capture != Knowledge
Knowledge != Evidence
Paperless tag != Project Document Link
```

## 11. Built-in AI, remote processing and second-path prevention

Initial posture:

```text
Paperless AI / LLM features: disabled unless separately reviewed
Paperless internal vector/RAG path: not a Pantheon Knowledge authority
remote OCR provider: disabled unless separately reviewed and authorized
external document transmission: gated
```

This prevents a second ungoverned Knowledge/vectorization path or hidden external-provider route.

## 12. Security and runtime posture

Initial candidate assumptions:

```text
trusted internal host / NAS-side deployment
no unauthenticated public exposure
runtime credentials outside Pantheon governance records
backup + restore proof before real-dossier activation
network scope reviewed
source confidentiality preserved
remote AI/OCR disabled by default
```

Paperless health must be observed from the target runtime, not inferred from repository state.

Candidate observations may include API reachability, observed version, DB/broker state, source storage, read path, upload/task round-trip, original download and backup status.

```text
reachable != healthy
healthy != safe
runtime success != Evidence
repository merged != deployed
```

## 13. Responsibility map

```text
Pantheon governance
  capability classification
  source identity expectations
  Task Contract / policy / decision boundaries
  Knowledge/Evidence rules
  activation/update/rollback status semantics

Pantheon implementation
  bounded Paperless gateway / PEP adapter
  source capture / project-document candidate path
  cockpit projections / observer
  optional Compose overlay

Hermes external runtime
  skill installation and execution
  bounded orchestration
  runtime credentials appropriate to the skill boundary

Paperless external runtime
  native DMS storage/search/version/task operations
  native mutation only when separately authorized

Docling external runtime
  structured extraction when selected

Human/operator
  adoption
  installation
  credential/network configuration
  real-dossier authorization
  activation and consequential decisions
```

Forbidden collapses:

```text
Paperless == Pantheon data model
Paperless == Knowledge
Paperless == Evidence
Paperless == approval authority
Paperless tags == canonical project relations
Pantheon governance == Paperless worker/scheduler
Hermes == automatic document authority
```

## 14. Current classification and exit criterion

```text
upstream software: external product
Pantheon Capability manifest: candidate
Pantheon Resource manifest: candidate
Pantheon adapter/gateway: co-located implementation candidate
Hermes skill source: co-located candidate / runtime installation not established
Paperless target installation: not established
health: not established
adoption: not decided
activation: not authorized
real-dossier use: not authorized
production use: forbidden pending separate gates
```

Next outcomes remain:

```text
promote as reviewed preferred binding
-> after bounded implementation + target qualification + human adoption decision

retain as candidate
-> while implementation, installation or target review remains incomplete

refuse / supersede
-> if security, maintainability, licensing, integration or professional-use constraints are unacceptable
```

No state transition in this document performs installation or activation.
