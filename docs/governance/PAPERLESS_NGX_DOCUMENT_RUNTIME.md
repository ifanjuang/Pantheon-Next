# Paperless-ngx Document Runtime Candidate

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

This document classifies `paperless-ngx/paperless-ngx` as a candidate external document-management runtime for Pantheon Next.

It is product-specific adapter material. It does not replace the tool-agnostic document lifecycle, source, Knowledge, Evidence, approval or memory models.

Observed upstream on 2026-07-23:

```text
repository: paperless-ngx/paperless-ngx
default branch: dev
observed commit: c9443e890f63d98ce64ee275c2dc2e62770c9187
license: GPL-3.0
```

Primary upstream references:

- https://github.com/paperless-ngx/paperless-ngx
- https://docs.paperless-ngx.com/
- https://docs.paperless-ngx.com/api/

Non-equivalence rules apply: see `NON_EQUIVALENCE_RULES.md`.

## 1. Why this document exists

`DOCUMENT_LIFECYCLE_GOVERNANCE.md` intentionally stays tool-agnostic. It defines `Source Capture`, `Document Record`, project links, Knowledge links, projections, indexing and governed execution without selecting a document-management product.

Paperless-ngx introduces a concrete placement question that generic doctrine should not absorb:

```text
Can an external DMS preserve source files, versions, searchable text and document metadata
while Pantheon keeps governed identity and business classification,
Hermes performs bounded analysis and mutation,
and the Cockpit exposes the result?
```

The candidate answer is yes, subject to the gates and boundaries below.

This is therefore an adapter/binding note, not a parallel document model.

## 2. Capability Slot

Proposed abstract Capability Slot:

```text
capability_id: document_source_management
function: capture, preserve, version, retrieve and expose professional source documents
preferred_binding: paperless-ngx/paperless-ngx
owner_layer: external runtime / professional storage
executed_by: Paperless-ngx for its native document operations; Hermes for governed orchestration
exposed_by: Pantheon Cockpit / OpenWebUI through a separately implemented adapter
governed_by: Pantheon Next
approved_by: human where installation, activation, consequential mutation or real-dossier use requires approval
```

Candidate lifecycle posture at this review:

```text
binding_status: preferred_candidate
install_status: unknown
health_status: unknown
update_status: upstream active / target-runtime status unknown
activation_status: unavailable
rollback_status: unknown
adoption_status: not decided
production_status: forbidden until separately authorized
```

The declarative catalog entries added with this note are candidate data only.

```text
capability_slot != installed_capability
binding_selected != dependency_adopted
installed != approved
healthy != safe
```

## 3. What Paperless-ngx may own

Paperless-ngx is a plausible backing runtime for operational document functions such as:

- intake of uploaded source files;
- preservation of original files;
- generated archival representation where configured;
- file-level document versions;
- checksums and file metadata;
- native OCR and extracted searchable text;
- document preview and thumbnails;
- full-text search;
- tags, correspondents, document types and custom fields;
- object-level permissions;
- email document ingestion;
- native task execution and task status;
- document-management workflows internal to Paperless;
- API access to documents and versions.

These are runtime capabilities of Paperless-ngx. They do not become Pantheon governance capabilities by being available.

## 4. What Paperless-ngx must not own

Paperless-ngx must not become the authority for:

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

Paperless tags, document types and custom fields may mirror selected governed metadata for operational search. The mirror is not canonical merely because it is stored in Paperless.

```text
Paperless metadata != Pantheon business classification
Paperless OCR text != source truth
Paperless search hit != Evidence
Paperless task success != professional validation
```

## 5. Source Capture mapping

The target mapping is reference-based rather than byte duplication.

A governed `Source Capture` may point to an exact Paperless document version:

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

Exact field names remain implementation details to reconcile with the external Cockpit data model.

Required invariants:

- one governed source reference identifies one exact captured version;
- a new file version does not silently rewrite the identity of the earlier source;
- the original source remains superior to OCR, Markdown, summaries, chunks and embeddings;
- removing an index or Knowledge projection does not silently delete the original source;
- source download remains subject to the requesting identity and source policy;
- Paperless internal IDs are backing-runtime identifiers, not Pantheon authority.

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

Candidate user actions:

```text
open preview
open permitted original
search
inspect metadata
send to Hermes for analysis
propose classification
request project linking
request Knowledge publication
request reprocessing
```

The primary Cockpit should not expose implementation-specific queues, Celery internals or Paperless administration concepts unless troubleshooting requires them.

### 6.1 Read-only exposure path

A separately implemented Cockpit adapter may use the Paperless REST API for bounded read-only operations such as:

```text
list/search visible documents
read metadata
preview
thumbnail
permitted original download
read version information
read task/result status
```

This is an exposure adapter, not a Pantheon runtime.

### 6.2 Consequential mutation path

Mutations should use the governed execution path:

```text
Cockpit intent
-> Pantheon policy / gate
-> bounded Hermes request
-> Paperless REST mutation
-> runtime observation
-> candidate result
-> Pantheon status update
-> Cockpit projection
```

Typical mutations include:

- upload/ingest;
- metadata changes;
- tag or document-type changes when used as governed mirrors;
- version upload;
- project/Knowledge side effects in the external Cockpit data model;
- destructive document operations.

A free-form natural-language request must not be the only consequential execution contract.

## 7. Hermes binding

Candidate Hermes binding name:

```text
paperless_documents
```

Candidate low-level operations:

```text
search_documents
get_document
get_document_metadata
get_document_text
get_document_versions
download_original
get_preview
upload_document
get_task_status
update_document_metadata
apply_document_tags
remove_document_tags
add_document_version
```

A higher-level Hermes Skill such as `pantheon-document-intake` may orchestrate those calls with Docling or other authorized extraction resources.

The Paperless binding is not expected to host Pantheon logic.

Hermes may:

- call the REST API with runtime-held credentials;
- inspect a source;
- observe Paperless task state;
- retrieve the exact source version required by a Task Contract;
- invoke separately approved document-analysis resources;
- propose business metadata and classification;
- apply an authorized mutation;
- return candidate outputs and runtime observations.

Hermes must not:

- treat Paperless automatic metadata as approved classification;
- promote OCR or LLM output directly to Evidence;
- silently enable remote providers;
- broaden project or confidentiality scope;
- delete or replace sources without the applicable gate;
- promote Knowledge or durable memory automatically.

## 8. Separation from Docling and OCR resources

Paperless-ngx and Docling occupy different Capability Slots.

```text
Paperless-ngx
= source capture, document persistence, versions, basic OCR/search, document runtime

Docling
= structured document analysis, Markdown derivation, table extraction and layout-aware representations
```

Target selection rule:

```text
native searchable content sufficient
-> Paperless/native extraction may be sufficient for retrieval or basic inspection

structured representation required
-> use Docling or another selected document-analysis binding

poor scan / specialist OCR required
-> use an authorized OCR/VLM binding
```

Availability of Paperless OCR does not authorize using it as the only extraction path for every source.

## 9. Classification model

Hermes may produce a `Classification Candidate` from source content and current Case/Situation context.

Example:

```yaml
classification_candidate:
  source_id: src_example
  proposed_project_ids:
    - lieurey
  proposed_phase_by_project:
    lieurey: 30_DCE
  proposed_document_type: cctp
  proposed_subject: charpente
  proposed_knowledge_publication: false
  uncertainties: []
```

The human's explicit destination selection may already constitute the classification decision when policy allows it. Otherwise the applicable gate remains visible.

After authorization, selected metadata may be mirrored into Paperless tags, document type or custom fields for search and operations.

The governed relationship remains outside Paperless:

```text
Document Record
-> Project Document Link A / phase
-> Project Document Link B / phase
```

One Paperless document therefore does not need to encode the complete many-to-many business relationship inside its own tag taxonomy.

## 10. Knowledge model

A Paperless document is a `Source`, not a `Knowledge Item`.

Candidate path:

```text
Paperless document/version
-> governed Source Capture
-> approved extraction / Projection
-> Knowledge Source Link
-> Knowledge Item candidate or update candidate
-> review/gate where required
-> index publication when authorized
```

This preserves multi-source Knowledge:

```text
Knowledge Item
├── Paperless source A
├── Paperless source B
└── other governed source C
```

Knowledge visibility and source download permission remain distinct.

## 11. Paperless built-in AI and remote processing

Paperless-ngx currently includes optional AI/LLM-oriented features and optional remote OCR capabilities upstream.

Pantheon posture for the initial candidate is:

```text
Paperless AI / LLM features: disabled unless separately reviewed
Paperless internal vector/RAG path: not a Pantheon Knowledge authority
remote OCR provider: disabled unless separately reviewed and authorized
external document transmission: gated
```

This avoids creating a second ungoverned Knowledge/vectorization path or a hidden external-provider route.

An operator may later review such features as separate Capability Slots or bindings. Their presence upstream does not authorize activation.

## 12. Security and data posture

Paperless upstream warns that sensitive documents are stored unencrypted at the application-storage layer and recommends operation on a trusted host with backups.

The initial Pantheon candidate therefore assumes:

```text
trusted internal host or NAS-side deployment
no unauthenticated public exposure
runtime credentials stored outside Pantheon governance records
backup and restore evidence before real-dossier activation
network scope reviewed
source confidentiality preserved end-to-end
remote AI/OCR disabled by default
```

Required review before real-dossier activation:

- host and storage trust boundary;
- backup/restore verification;
- user and group permissions;
- API credential custody;
- network exposure;
- TLS/reverse-proxy posture where applicable;
- document retention and deletion behavior;
- email-account scope if email ingestion is enabled;
- remote OCR and AI settings;
- rollback procedure.

## 13. Runtime status and health

Paperless health must be observed from the target runtime, not inferred from the GitHub repository.

Candidate health observations may include:

```text
API reachable
version observed
database reachable
broker/task processor operational
source storage writable by Paperless
read path functional
upload/task round-trip functional
original download functional
backup status observed
```

These observations remain operational signals.

```text
healthy != safe
runtime_success != evidence
```

## 14. Human approvals

At minimum, separate review is expected for:

```text
adopting Paperless as preferred binding
installing it on a target host
credential and network configuration
real-dossier authorization
activation of write operations
activation of email ingestion
activation of remote OCR or AI features
source deletion or destructive retention actions
production activation
major or breaking updates
rollback decision
```

Routine read-only consultation inside an already approved scope may use lower-friction policy where the active deployment defines it.

## 15. Forbidden collapses

This candidate must not evolve into:

```text
Paperless == Pantheon data model
Paperless == Knowledge
Paperless == Evidence
Paperless == approval authority
Paperless == project management system
Paperless tags == canonical multi-project relations
Pantheon == Paperless worker/scheduler
Cockpit == hidden Paperless administrator
Hermes == automatic document authority
```

Paperless may run its own queue, workers and scheduler because it is an external runtime. Pantheon must not reproduce or absorb them.

## 16. Implementation ownership

### Pantheon Next

Owns:

- Capability Slot classification;
- binding status and lifecycle distinctions;
- source identity expectations;
- governance gates;
- Evidence/Knowledge boundaries;
- cockpit-facing contract expectations;
- installation/health/update/activation/rollback status vocabulary.

Does not install or run Paperless.

### Hermes-side runtime or executable sibling

Owns:

- `paperless_documents` executable binding;
- `pantheon-document-intake` orchestration where implemented;
- runtime credentials;
- API calls;
- Docling/OCR invocation;
- runtime task observation;
- candidate classification and processing results.

### `ifanjuang/pantheon-mvp`

Candidate external owner for:

- Cockpit Paperless read adapter;
- Document Cards backed by Paperless source references;
- governed upload intent;
- project/phase relations;
- Knowledge source links;
- user review surfaces;
- processing/error/status display.

### Human/operator

Owns consequential adoption, installation, activation and professional review decisions.

## 17. Candidate conformance scenarios

An external implementation should eventually prove at least:

1. a PDF dropped in the Cockpit is captured as one exact Paperless source version;
2. task status is observed without fabricated progress;
3. the original remains downloadable when permitted;
4. a later Paperless file version preserves the earlier governed source reference;
5. Hermès can retrieve the exact version and produce an analysis candidate;
6. Docling can derive a structured projection without replacing the original;
7. Hermes can propose project/phase/document-type classification;
8. a classification mutation is not applied when its gate is blocked;
9. an authorized classification may be mirrored to Paperless while canonical project links remain external;
10. one source may be linked to several projects without duplicating source bytes;
11. one Knowledge Item may cite several Paperless-backed sources;
12. Paperless built-in AI or remote OCR cannot become active by implication;
13. source deletion, Knowledge publication and Evidence admission remain separate decisions;
14. target-runtime health is reported independently from adoption and safety status.

These scenarios are conformance targets, not tests implemented by this PR.

## 18. Current classification

```text
upstream software: implemented externally
upstream activity: observed active on 2026-07-23
Pantheon Capability manifest: candidate
Pantheon Resource manifest: candidate
Hermes executable binding: documented non-implemented
Cockpit adapter: documented non-implemented
installation: not established
health: not established
adoption: not decided
activation: not authorized
real-dossier use: not authorized
production use: forbidden pending separate gates
```

## 19. Exit criterion

This candidate should next move to one of three outcomes:

```text
promote as reviewed preferred binding
-> after a bounded implementation proves the conformance scenarios and a human decision records adoption

retain as candidate
-> while implementation, installation or target-runtime review remains absent

refuse / supersede
-> if security, maintainability, licensing, integration or professional-use constraints are unacceptable
```

No state transition in this document performs installation or activation.