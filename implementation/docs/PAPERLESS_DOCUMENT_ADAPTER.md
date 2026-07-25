# Paperless-ngx document adapter

Status: external executable candidate — implemented in this repository / not deployed or adopted.

This adapter implements the bounded Paperless-ngx source-management surface required by the Pantheon document-source candidate defined in Pantheon Next PR #467.

```text
Paperless-ngx     stores source bytes, versions and operational metadata.
Docling           derives structured Markdown/JSON when selected.
Hermes            orchestrates analysis and candidate classification.
Pantheon          governs scope, gates, status, Evidence and Knowledge boundaries.
Cockpit/OpenWebUI exposes reviewed projections.
Human             approves consequential writes and activation.
```

## Implemented API adapter

`mvp_vertical.paperless.PaperlessClient` provides:

- authenticated document list and full-text search;
- document and metadata reads;
- exact-version original/preview download;
- immutable `PaperlessSourceCapture` material with SHA-256 and a stable `paperless://` storage reference;
- temporary local materialization for Docling/OCR without treating the temporary path as canonical;
- document upload and task observation;
- an allowlisted metadata update surface for classification mirrors;
- `governed_post_document` and `governed_update_document_metadata`, which route external writes through the existing Pantheon policy chokepoint.

The adapter requires an exact Paperless `version_id` before creating a governed Source Capture. Browsing "latest" may be useful to a human, but it is not sufficient provenance for immutable intake.

## Implemented internal gateway

`mvp_vertical.paperless_gateway` provides a server-side gateway so the Cockpit and Hermes never need the raw Paperless token in the browser.

Read surface, protected by the Cockpit read key:

```text
GET /health
GET /v1/paperless/documents
GET /v1/paperless/documents/{id}
GET /v1/paperless/documents/{id}/capture?version_id=<exact>
GET /v1/paperless/tasks/{task_id}
```

The document projection deliberately excludes Paperless extracted `content` and marks operational metadata as non-authoritative for business classification, Knowledge, Evidence and approval.

The consequential mutation surface is protected by the Hermes key and the live Pantheon policy client:

```text
POST /v1/paperless/documents/{id}/metadata
```

A missing policy key, unreachable PDP, blocked preflight or invalid human decision fails closed before Paperless is mutated.

## Implemented OpenWebUI source inbox

`openwebui/pantheon_paperless_documents.py` provides a read-only Source Inbox candidate over the internal gateway:

```text
search_document_sources
inspect_document_source
inspect_exact_source_capture
```

The tool escapes source metadata before rendering and exposes no classification/write method.

## Implemented Paperless -> Document vertical intake

`mvp_vertical.paperless_ingestion` reuses the existing `store.ingest` Document -> Knowledge pipeline instead of creating a second ingestion/RAG engine.

Flow:

```text
exact Paperless document/version
-> PaperlessSourceCapture + SHA-256
-> Task Contract scope check
-> temporary contained materialization
-> existing store.ingest
-> Docling/direct converter
-> source_documents + document_versions + extraction + chunks
-> paperless_source_bindings
```

`paperless_source_bindings` preserves the external identity beside the Project Document:

```text
document_id
backing_resource = paperless_ngx
paperless_document_id
paperless_version_id
storage_reference
original_filename
source_digest
```

The temporary file is deleted after processing. Paperless remains the backing source runtime; the temporary filesystem path is not the canonical locator.

Critically, the Task Contract must explicitly declare the generated Paperless `source_ref`. Paperless visibility therefore does not broaden project scope.

This intake produces a Project Document and its derived representation. It does not automatically publish Knowledge or admit Evidence. Existing Knowledge publication rules remain unchanged.

## Runtime configuration

The runtime reads:

```text
PAPERLESS_API_URL
PAPERLESS_API_TOKEN
PAPERLESS_API_TIMEOUT
PANTHEON_POLICY_API_URL
PANTHEON_POLICY_API_KEY
MVP_COCKPIT_API_KEY
MVP_HERMES_API_KEY
```

The API token and policy keys are external runtime secrets. They must not be committed, returned to the browser, stored in Pantheon governance records or copied into an Evidence Pack.

The optional `paperless` Docker Compose profile provides a local executable candidate using:

```text
paperless
paperless-db
paperless-broker
paperless-gateway
```

The Paperless image has no default. The operator must supply a reviewed pinned tag or digest through `PAPERLESS_IMAGE`. Database and application secrets are also required externally.

Example candidate invocation:

```bash
export PAPERLESS_IMAGE='ghcr.io/paperless-ngx/paperless-ngx:<reviewed-pin>'
export PAPERLESS_DB_PASSWORD='<external-secret>'
export PAPERLESS_SECRET_KEY='<external-secret>'
docker compose --profile paperless up -d paperless paperless-gateway
```

This is an operator action. The repository does not run it automatically.

## Source identity

One exact external version is represented as:

```text
paperless document id
+ exact version id
+ original filename
+ byte size
+ media type
+ sha256
+ paperless://document/<id>/version/<version>
+ Task-Contract-safe relative source_ref
```

Example:

```text
paperless://document/42/version/7
paperless/42/versions/7/Lieurey-DCE-CCTP.pdf
```

The relative `source_ref` is suitable for declaration in the existing Task Contract without weakening its absolute-path or traversal guards. The mapping to the external Paperless identity remains adapter data, not a filesystem claim.

## Classification

Hermes may produce a Classification Candidate such as:

```text
project = Lieurey
phase = DCE
document_type = CCTP
subject = charpente
knowledge_publication = no
```

After the required Pantheon policy check and human decision, selected operational mirrors may be written to allowlisted Paperless fields:

```text
title
correspondent
document_type
storage_path
tags
archive_serial_number
custom_fields
```

The adapter refuses arbitrary document fields such as `content`, permission rewrites or file replacement through this metadata method.

```text
Paperless metadata != canonical business classification
Paperless OCR != source truth
Paperless task success != professional validation
```

## Paperless internals

Paperless may use its own PostgreSQL database, Valkey broker, workers and scheduler. Those are Paperless implementation details.

They are not:

```text
Pantheon queue
Pantheon scheduler
Hermes queue
Hermes workflow engine
Evidence
approval
```

The adapter observes Paperless task state through the documented `/api/tasks/` API; it does not reimplement Paperless workers or scheduling.

## AI and remote processing posture

The initial candidate does not configure Paperless AI/LLM/vector features or remote OCR. Their absence from this adapter is deliberate. Enabling any external model/provider or remote OCR path requires a separate capability review covering data exposure, provider identity, scope and approval.

Local Paperless OCR remains derived processing. Docling remains the preferred Pantheon candidate for structured document analysis.

## Current status

```text
Paperless API adapter            implemented
exact-version Source Capture     implemented
Document vertical intake         implemented using existing store.ingest
external identity binding table  implemented
internal Paperless gateway       implemented
OpenWebUI Source Inbox           implemented / not installed
unit + integration tests         implemented
optional compose profile         implemented as external candidate
live Paperless connection        not established
target installation              not established
target health                    not established
live Hermes runtime wiring       not established
automatic Knowledge publication  not added; existing governed path remains separate
adoption                         not decided
activation                       not authorized
production / real dossier        forbidden pending separate review
```
