# Paperless-ngx document adapter

Status: external executable candidate — implemented in this repository / not deployed or adopted.

This repository hosts the executable candidate for the Pantheon `document_source_management` binding and the Hermes `pantheon-document-intake` skill. Pantheon Next remains the governance source; this repository executes only when explicitly deployed by the operator.

```text
Paperless-ngx     stores source bytes, versions and operational metadata.
Docling           derives structured Markdown/JSON when selected.
Hermes            executes the bounded skill and orchestration.
Pantheon PDP      classifies/preflights and validates supplied decision references.
MVP PEP/gateway   binds effect facts, enforces fail-closed and executes allowed effects.
Cockpit/OpenWebUI exposes reviewed projections.
Human             supplies consequential decisions.
```

## Implemented Paperless adapter

`mvp_vertical.paperless.PaperlessClient` provides:

- authenticated document list and full-text search;
- document and metadata reads;
- exact-version original/preview download;
- immutable `PaperlessSourceCapture` material with SHA-256 and a stable `paperless://` storage reference;
- temporary local materialization for Docling/OCR without treating the temporary path as canonical;
- document upload and task observation;
- an allowlisted metadata update surface.

One exact source version is represented by:

```text
Paperless document id
+ exact version id
+ original filename
+ byte size
+ media type
+ SHA-256
+ paperless://document/<id>/version/<version>
+ Task-Contract-safe relative source_ref
```

A mutable "latest" pointer is not sufficient provenance for governed intake.

## Implemented PEP/PDP contract normalization

`mvp_vertical.policy_request` adapts runtime-specific effects to the current Pantheon HTTP policy contract.

The PDP receives only:

```text
request
  intent
  external_effect
  writes_state
  transmission_requested
  memory_promotion_requested
  professional_position
  financial_or_contractual_effect
  scope

gate_signals
  task_contract_ref
  evidence_pack_candidate_ref
  human_decision_ref
  human_decision_level
```

Runtime fields such as Paperless document ids, changed fields or local effect names remain outside the policy transport body.

For new consequential bindings, the PEP also supplies `decision_expectation` from facts it observes itself:

```text
required_ceiling
required_scope
object_identity
expected_digest
```

`policy_gate.enforce_consequential` replaces a caller-supplied expectation with those PEP-owned facts before calling `POST /v1/policy/decisions:validate`.

This closes a candidate-level integrity gap where a caller could otherwise supply a false decision and a matching false expectation.

```text
caller expectation != effect requirement
validated matching fields != authenticated human issuer
```

The latter distinction remains important: this candidate still does not prove cryptographic/authenticated human-decision issuance.

## Implemented internal gateway

`mvp_vertical.paperless_gateway` keeps the raw Paperless token server-side.

Read surface accepts the Cockpit read key or Hermes runtime key:

```text
GET /health
GET /v1/paperless/documents
GET /v1/paperless/documents/{id}
GET /v1/paperless/documents/{id}/capture?version_id=<exact>
GET /v1/paperless/tasks/{task_id}
```

The read projection excludes Paperless extracted `content` and marks operational metadata as non-authoritative for business classification, Knowledge, Evidence and approval.

Hermes-only governed surfaces:

```text
POST /v1/paperless/intakes
POST /v1/paperless/documents/{id}/metadata
```

Both require:

```text
exact Paperless version
Task Contract
human decision reference
Hermes gateway key
Pantheon policy service
```

The gateway derives scope, approval ceiling, effect identity and digest rather than trusting those fields from Hermes/model output.

## Governed Project Document intake

`POST /v1/paperless/intakes` performs the following bounded sequence:

```text
read exact Paperless version
-> build Source Capture candidate
-> assert exact source_ref is declared in Task Contract
-> derive effect scope/object/digest/ceiling
-> Pantheon preflight
-> validate human decision reference against PEP-derived expectation
-> execute existing store.ingest only if allowed
-> Docling/direct converter
-> source_documents + versions + extraction + chunks
-> paperless_source_bindings
```

The read/capture happens before the gate because it is needed to identify the exact proposed effect. Database/derived-state persistence happens only inside the governed effect.

`mvp_vertical.paperless_ingestion.intake_paperless_capture` reuses the existing `store.ingest`; it does not create a second RAG/indexing engine.

`paperless_source_bindings` preserves:

```text
document_id
backing_resource = paperless_ngx
paperless_document_id
paperless_version_id
storage_reference
original_filename
source_digest
```

A single Paperless version may back Project Documents in more than one project. The source bytes remain in Paperless; the business relationship stays outside Paperless.

The intake returns explicitly:

```text
knowledge_published: false
evidence_admitted: false
```

## Governed operational metadata mirror

Paperless metadata writes are bound to the same exact-source and Task Contract discipline.

Before PATCH, the gateway:

```text
captures exact Paperless version
checks source_ref is declared
hashes the requested change object with source + Task Contract identity
derives a metadata-effect object identity
binds the human decision expectation
runs Pantheon preflight + decision validation
```

Changing the requested tag/custom-field payload therefore changes the expected digest; a decision for one change cannot be silently reused for another change.

The optional Classification Candidate is trace context only. It cannot define the authoritative scope, ceiling, object identity or expected digest.

```text
Paperless metadata != canonical business classification
```

## Implemented Hermes skill

`hermes/skills/pantheon-document-intake/` is an AgentSkills-compatible candidate skill.

It contains:

```text
SKILL.md
scripts/pantheon_document_intake.py
```

The bundled script is transport-only and reads only:

```text
PANTHEON_PAPERLESS_GATEWAY_URL
MVP_HERMES_API_KEY
```

It never requires or reads:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
```

Supported first-slice commands:

```text
search
inspect
capture
task
intake
update-metadata
```

The skill does not expose upload, delete, version replacement, permission mutation, Knowledge publication, Evidence admission, remote OCR activation, Paperless AI activation or memory promotion.

## OpenWebUI source inbox

`openwebui/pantheon_paperless_documents.py` remains the read-only Cockpit exposure candidate:

```text
search_document_sources
inspect_document_source
inspect_exact_source_capture
```

No write method is exposed from that surface.

## Runtime configuration

External runtime secrets/configuration:

```text
PAPERLESS_API_URL
PAPERLESS_API_TOKEN
PAPERLESS_API_TIMEOUT
PANTHEON_POLICY_API_URL
PANTHEON_POLICY_API_KEY
MVP_COCKPIT_API_KEY
MVP_HERMES_API_KEY
PANTHEON_PAPERLESS_GATEWAY_URL
```

The optional `paperless` Docker Compose profile contains:

```text
paperless
paperless-db
paperless-broker
paperless-gateway
```

The Paperless image has no floating default. Operator-supplied DB/application secrets and a reviewed pinned image are required.

## Paperless / Docling separation

```text
Paperless
  source bytes
  versions
  local/basic OCR
  operational metadata
  native search/tasks

Docling
  structured extraction
  Markdown
  tables
  layout
  derivation provenance
```

The source remains superior to every derivative.

## Paperless internals

Paperless PostgreSQL, Valkey, workers and scheduler are implementation details of the external DMS.

They are not:

```text
Pantheon queue
Pantheon scheduler
Hermes queue
Hermes workflow engine
Evidence
approval
```

## AI and remote processing posture

The candidate does not configure Paperless AI/LLM/vector features or remote OCR. Enabling any external model/provider or remote OCR path requires a separate capability review.

## Current status

```text
Paperless API adapter                 implemented
exact-version Source Capture          implemented
PEP -> PDP request normalization      implemented
PEP-owned decision expectation        implemented candidate
Project Document intake endpoint      implemented candidate
Document vertical intake              implemented using existing store.ingest
external identity binding table       implemented
metadata effect digest binding        implemented candidate
internal Paperless gateway            implemented
Hermes pantheon-document-intake skill implemented candidate / not installed
OpenWebUI Source Inbox                implemented candidate / not installed
unit + integration tests              implemented
optional compose profile              implemented external candidate
live Paperless connection             not established
target installation                   not established
target health                         not established
live Hermes skill installation        not established
live PDP/PEP round-trip               not established
authenticated human decision issuer   not implemented/proven
automatic Knowledge publication       not added
adoption                              not decided
activation                            not authorized
production / real dossier             forbidden pending separate review
```
