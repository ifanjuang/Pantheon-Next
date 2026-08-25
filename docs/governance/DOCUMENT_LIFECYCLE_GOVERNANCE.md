# Pantheon Next — Governed Document Lifecycle

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

This document proposes a governed lifecycle for document intake, processing, classification, Knowledge publication, indexing, retrieval and runtime observation.

It specializes and connects:

- `DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md`;
- `SOURCE_INGESTION_RETRIEVAL_MODEL.md`;
- `RAW_DERIVED_GOVERNED_RECORDS.md`;
- `HERMES_INTEGRATION.md`;
- `OPENWEBUI_INTEGRATION.md`;
- `PANTHEON_CONTROL_PLANE_BOUNDARY.md`;
- `PANTHEON_COCKPIT_UX_SPEC.md`;
- `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`;
- `NEXT_MVP_REPOSITORY_PLACEMENT.md`.

It does not implement an upload endpoint, OCR pipeline, converter, worker, queue, scheduler, vector store, model host, Hermes Skill, Cockpit UI, OpenWebUI Tool, database migration, approval engine or memory engine.

```text
The exposure surface captures intent and displays.
Hermes executes through bounded external capabilities.
Pantheon governs consequential status and scope.
The human decides where consequence requires a decision.
```

## 1. Purpose

The target is not a monolithic RAG pipeline.

The target is a governed document lifecycle that can answer:

```text
What original source was received?
Where did it come from?
What did the user ask to do with it?
What did Hermes understand before processing?
Which processing profile and bindings were used?
What derived representations were produced?
What quality signals and warnings were observed?
Which project or Knowledge scope received it?
Which projection is active?
Which chunks and embedding version were indexed?
What may be downloaded, retrieved, revoked, reprocessed or rolled back?
```

The lifecycle must preserve the following distinctions:

```text
source received != source accepted
source captured != document classified
user intent != Hermes interpretation
Hermes interpretation != authorized action
native extraction completed != content validated
OCR completed != transcription validated
Markdown generated != projection approved
summary generated != source evidence
project link created != Knowledge publication
Knowledge published != Evidence admitted
projection admitted != indexing authorized
indexed != retrievable in every scope
retrieved != authoritative
runtime success != professional correctness
```

## 2. Scope

The lifecycle applies to sources received through:

- the Pantheon Cockpit;
- OpenWebUI;
- a bounded Hermes handoff;
- a connector or approved source system;
- an existing NAS reference;
- a URL;
- an email or attachment;
- a repository or Drive reference;
- a controlled CLI or API intake.

Supported source categories may include:

- PDF;
- DOCX;
- PPTX;
- XLSX;
- Markdown or text;
- PNG, JPEG, TIFF or scan;
- email and attachments;
- URL or web page capture;
- ZIP or export package;
- repository file;
- structured source reference.

A supported category declaration is not proof that a binding is installed, approved, healthy or appropriate for a particular source.

## 3. Core model

The lifecycle separates the following objects:

```text
Intake Item
Source Origin
Source Capture
Intake Intent
Intake Brief
Pipeline Run
Pipeline Step Observation
Projection
Document Record
Project Document Link
Knowledge Item
Knowledge Source Link
Chunk Set
Embedding Manifest
Index Publication
Processing Attestation
```

The names are conceptual. Exact schema names remain to be reconciled against the current Pantheon implementation under `implementation/` before implementation work extends them.

### 3.1 Intake Item

An `Intake Item` is the temporary lifecycle object created when a source enters the system.

It supports both unclassified intake and direct targeted intake.

```yaml
intake_item:
  intake_id:
  source_origin_id:
  source_capture_id:
  origin_channel: cockpit | openwebui | connector | cli | existing_source
  requested_destination: unclassified | project | knowledge | project_and_knowledge
  requested_project_ids: []
  requested_phase_by_project: {}
  requested_knowledge_family:
  classification_status:
  requested_by:
  received_at:
```

An Intake Item may remain unclassified until later review.

```text
received
-> awaiting_context
-> interpretation_ready
-> classification_pending
-> classified
-> archived
-> rejected
```

These labels are lifecycle candidates, not one compressed implementation state.

### 3.2 Source Origin

`Source Origin` records where the material came from.

Examples:

```yaml
source_origin:
  origin_kind: upload | url | nas | email | drive | repository | connector
  origin_reference:
  observed_at:
  actor_or_connector:
  access_posture:
```

The origin may remain mutable or disappear. It is not the immutable source capture.

### 3.3 Source Capture

`Source Capture` is the preserved, content-addressed object used for reproducibility.

```yaml
source_capture:
  source_id:
  source_type:
  original_filename:
  mime_type:
  size_bytes:
  content_hash:
  captured_at:
  storage_reference:
  integrity_status:
  security_status:
  retention_policy:
```

Invariants:

- the captured bytes are not rewritten by later processing;
- the content hash is computed before derived processing;
- every projection refers to one exact capture;
- an updated URL or changed external file creates a new capture;
- the original remains downloadable when the requesting identity and source policy allow it;
- deleting an index or deactivating a projection does not silently delete the original.

```text
external location != immutable capture
same URL != same content
same filename != same source
Markdown derivative != original file
```

### 3.4 Intake Intent

`Intake Intent` records what the user asked and the context visible at the moment of the request.

```yaml
intake_intent:
  intent_id:
  intake_id:
  user_message:
  current_project_ids: []
  current_knowledge_family:
  current_query:
  selected_context_refs: []
  requested_outcomes: []
  created_by:
  created_at:
```

The Cockpit may keep this interaction simple. Typical actions are:

- search for information;
- inspect a source;
- inspect project context;
- send a source and context to Hermes;
- ask for a proposed classification;
- ask for a summary or extraction;
- display processing progress;
- display outputs and source links.

The Cockpit does not need to expose the full technical pipeline in the primary user flow.

### 3.5 Intake Brief

`Intake Brief` is Hermes' reformulation of the source subject, user intent, proposed destination and proposed processing plan before consequential execution.

```yaml
intake_brief:
  brief_id:
  intake_id:
  intent_id:
  understood_subject:
  short_description:
  technical_profile_candidate:
  business_profile_candidate:
  proposed_project_links: []
  proposed_knowledge_publication:
  proposed_operations: []
  uncertainties: []
  verification_points: []
  confirmation_posture: direct | policy_allowed | human_confirmation_required
  created_by_binding:
  binding_version:
  review_status:
```

This object supports a bounded two-stage exchange:

```text
Stage 1 — understand and reformulate
Stage 2 — execute the authorized processing plan
```

The source capture must exist before Stage 1 so the interpretation and later execution refer to the same content.

```text
Hermes understood subject != source assertion
Hermes proposed destination != approved classification
Hermes proposed profile != authorized pipeline
```

## 4. Entry modes

The same intake boundary supports three product modes.

### 4.1 Unclassified drop

```text
Cockpit or OpenWebUI
-> Source Capture
-> Intake Item: unclassified
-> Hermes interpretation when requested
-> later classification
```

This is the default when the user does not know the destination yet.

### 4.2 Direct project intake

The user may explicitly select one or more projects and a phase for each project.

```text
Source Capture
-> Document Record
-> Project Document Link A / phase
-> Project Document Link B / phase
```

The user's explicit selection is already a human classification decision. A second mandatory confirmation is not required unless policy, uncertainty, sensitivity or conflict requires it.

### 4.3 Direct Knowledge intake

The user may explicitly target the general Knowledge corpus and optionally select a first-level family.

```text
Source Capture
-> Hermes interpretation and derived projection
-> Knowledge Item or Knowledge publication candidate
```

The publication may be automatic with visible review status when existing Knowledge policy allows it. Consequential reliance, destructive merge, Evidence promotion or external action remains separately governed.

### 4.4 Project and Knowledge

A source may support both a project document and reusable Knowledge.

The model must preserve two independent relationships:

```text
Source Capture
├── Document Record -> one or more project links
└── Knowledge Item -> one or more source links
```

The source is not duplicated merely because it participates in both spaces.

## 5. Project document model

A project document is not defined only by a filesystem path.

### 5.1 Document Record

```yaml
document_record:
  document_id:
  source_id:
  title:
  document_type:
  document_date:
  revision:
  distributor:
  subject:
  classification_status:
```

### 5.2 Project Document Link

A separate many-to-many link allows one document to belong to one or more projects.

```yaml
project_document_link:
  link_id:
  document_id:
  project_id:
  phase_code:
  relation_type:
  is_primary:
  linked_by:
  linked_at:
```

The phase belongs to the project-document relationship because one source may have a different role in another project.

### 5.3 Flat phase structure

The architecture-agency phase structure remains shallow:

```text
00_Gestion/
10_Conception/
20_Autorisations/
30_DCE/
40_Marche/
50_Chantier/
60_Reception/
90_Sinistres/
```

No mandatory subfolder exists inside a phase.

Granular classification belongs in metadata, relations, types and tags rather than deeper filesystem trees.

The existing strict filename rule applies when a source is classified as a project document. It is not required at the moment of an unclassified drop or for a Knowledge-only source.

### 5.4 Card projection

A Project Document Card may remain project-scoped even when the underlying document has several project links.

```text
one Document Record
+ one Project Document Link
-> one project-scoped Document Card
```

This reconciles multi-project storage with the existing rule that a displayed project card has one current project context.

## 6. General Knowledge model

Knowledge is a general, reusable corpus. It is not a child folder of one project.

### 6.1 Knowledge Item

```yaml
knowledge_item:
  knowledge_id:
  title:
  family:
  description:
  short_summary:
  detailed_summary:
  review_status:
  visibility_scope:
  created_at:
  updated_at:
```

The five first-level families defined by the architecture domain document remain the candidate navigation structure:

```text
Référentiels
Responsabilité
Méthodologie
Techniques
Réglementations
```

No mandatory subfolder is required below these families.

### 6.2 Knowledge Source Link

One Knowledge Item may derive from one or more sources.

```yaml
knowledge_source_link:
  link_id:
  knowledge_id:
  source_id:
  projection_id:
  source_role: principal | supporting | contradictory | superseded
  page_refs: []
  section_refs: []
  access_policy_ref:
```

This supports reusable synthesis across several projects without losing provenance.

```text
Knowledge visibility != source download permission
Knowledge Item != source copy
Knowledge summary != source evidence
```

A general Knowledge Item may expose a summary and citations while withholding a confidential project source from identities that cannot access it.

### 6.3 Original source download

The Knowledge card or detail surface should expose the original source when permitted.

For each source link, the UI may show:

```yaml
source_download:
  source_id:
  original_filename:
  mime_type:
  content_hash:
  download_allowed:
  access_reason:
```

The original file remains superior to Markdown, summary, chunks or embeddings.

### 6.4 Description and summaries

A Knowledge Item may expose:

- a concise description of the source or subject;
- a short summary for cards and search results;
- a detailed structured summary;
- key points;
- decisions or requirements detected;
- risks, uncertainties and verification points;
- dates, actors, organizations and references.

These are derived candidates and must identify the projection from which they were generated.

```text
description generated != metadata verified
summary generated != professional conclusion
summary useful != summary authoritative
```

## 7. Pipeline profiles

The target should separate technical processing from business enrichment.

### 7.1 Technical profile

Examples:

```text
pdf_native
pdf_scanned
pdf_hybrid
office_document
image_document
email_package
web_capture
archive_package
```

A technical profile determines candidate operations such as:

- native extraction;
- OCR if required;
- layout analysis;
- table reconstruction;
- image extraction;
- Markdown conversion.

### 7.2 Business enrichment profile

Examples:

```text
contract
cctp
plu_or_plui
invoice
meeting_minutes
technical_report
regulatory_document
architectural_notice
```

A business profile determines:

- metadata fields to propose;
- sections to preserve;
- summary structure;
- chunking constraints;
- terminology;
- validation warnings;
- candidate project or Knowledge classification.

A source may therefore use:

```text
technical profile: pdf_scanned
business profile: contract
```

The business model must not name a specific OCR, VLM, converter or embedding model.

## 8. External execution through Hermes

Hermes is the preferred candidate execution binding for the first operational implementation.

Pantheon remains independent of Hermes in its domain model.

```text
preferred current executor binding = Hermes Skill
business dependency on Hermes = forbidden
```

### 8.1 Candidate skill boundary

Candidate Skill name:

```text
pantheon-document-intake
```

Candidate operations:

```text
inspect_source
prepare_intake_brief
run_native_extraction
run_ocr
run_layout_understanding
generate_raw_markdown
normalize_markdown
extract_metadata
generate_description
generate_short_summary
generate_detailed_summary
build_chunk_set
generate_embeddings
publish_index
revoke_index
get_run_status
request_cancel
```

The Skill may orchestrate external services. It does not need to host every model itself.

### 8.2 Two-stage Hermes exchange

The default assisted path is:

```text
1. Pantheon sends Source Capture reference + Intake Intent + governed context.
2. Hermes returns an Intake Brief.
3. Pantheon applies policy and records any required human correction or confirmation.
4. Pantheon sends an authorized bounded execution request.
5. Hermes executes externally and returns output references and observations.
6. Pantheon records lifecycle status, provenance, gates and decisions.
7. The Cockpit displays progress and results.
```

A direct path may skip explicit confirmation when the destination is already selected by the user and policy authorizes the processing profile.

### 8.3 Structured request

A consequential pipeline request should be structured rather than a free-form command.

```yaml
action_request:
  action_request_id:
  action_type: document_pipeline.run
  source_id:
  approved_intake_brief_id:
  requested_operations: []
  destination_refs: []
  data_policy_ref:
  task_contract_ref:
  requested_by:
```

Free-form user text may be attached as intent context, but must not be the only execution contract.

## 9. Processing pipeline

A candidate end-to-end sequence is:

```text
capture source
-> verify integrity and access posture
-> identify technical media type
-> prepare Intake Brief
-> select authorized profile and bindings
-> native extraction when sufficient
-> OCR when required
-> layout understanding when required
-> generate raw Markdown
-> generate normalized Markdown
-> generate metadata candidates
-> generate description and summaries
-> build provenance-bearing chunks
-> generate embedding manifest when authorized
-> classify or publish
-> index when authorized
```

### 9.1 Native extraction before OCR

OCR should not be used merely because an OCR binding is available.

```text
sufficient native text -> prefer native extraction
insufficient native text -> use OCR or visual processing when authorized
```

### 9.2 Raw and normalized Markdown

Two representations may be useful:

```text
raw Markdown
= faithful converter output retained for diagnostics and reproducibility

normalized Markdown
= stable readable representation for review, summarization and chunking
```

Normalization must not silently rewrite the source meaning.

The normalized projection should preserve, where available:

- title hierarchy;
- paragraphs;
- lists;
- tables;
- figure references;
- page references;
- notes;
- hyperlinks;
- code blocks;
- section provenance.

### 9.3 Source-specific preservation

A CCTP profile should preserve:

- lot and article numbering;
- prescriptions;
- included and excluded services;
- standards;
- units;
- tables;
- procedural lists.

A regulatory profile should preserve:

- territory and authority;
- document version and date;
- zone;
- article and subsection;
- rule, exception and condition;
- annex references;
- applicability warnings.

A contract profile should preserve:

- parties;
- object;
- duration;
- amounts;
- obligations;
- insurance;
- termination;
- dates;
- signature blocks.

Architectural drawings and plans remain a distinct experimental or partial capability. Text extraction alone must not imply full drawing understanding.

## 10. Pipeline Run and projections

### 10.1 Pipeline Run

```yaml
pipeline_run:
  run_id:
  source_id:
  technical_profile:
  business_profile:
  approved_intake_brief_id:
  requested_at:
  requested_by:
  external_run_reference:
  run_status:
  policy_snapshot_ref:
  input_hash:
  output_refs: []
  warnings: []
  errors: []
```

### 10.2 Pipeline Step Observation

```yaml
pipeline_step_observation:
  step_observation_id:
  run_id:
  capability_slot:
  binding_id:
  binding_version:
  installation_status:
  approval_status:
  health_snapshot:
  activation_status:
  runtime_status:
  progress:
  input_refs: []
  output_refs: []
  processing_attestation_refs: []
  warnings: []
  errors: []
```

The record observes external execution. Pantheon does not own the runtime's internal queue, scheduler or worker state.

### 10.3 Projection

```yaml
projection:
  projection_id:
  source_id:
  run_id:
  projection_type:
  projection_version:
  content_reference:
  content_hash:
  created_by_binding:
  generation_status:
  review_status:
  usage_status:
  supersedes_projection_id:
```

Status dimensions should remain orthogonal:

```yaml
generation_status: pending | running | succeeded | failed
review_status: not_required | pending | accepted | rejected
usage_status: inactive | active | superseded | deprecated
```

A new run creates new projections. It does not overwrite previous projections.

## 11. Cockpit progress display

The Cockpit should display the progress that Hermes or another executor actually exposes.

It must not invent a percentage.

### 11.1 Minimum status

When only a global status exists:

```text
requested
authorized
submitted_external
running_external
completed
completed_with_warnings
failed
cancellation_requested
cancelled
```

### 11.2 Step progress

Preferred display:

```text
Source capture              completed
Context understanding       completed
Native extraction           completed with warnings
OCR                         running — 18 / 42 pages
Markdown normalization      pending
Description and summaries   pending
Chunking                    pending
Embeddings                  pending
Index publication           pending
```

### 11.3 Quantified progress

A percentage is permitted only when backed by a measurable unit reported by the executor.

Examples:

```text
18 / 42 pages
67 / 120 chunks
38 MB / 90 MB
```

A language-model summary should not be shown as `73%` unless the executor exposes a meaningful measurable unit.

### 11.4 Freshness

Pantheon should record when an external status was observed.

```yaml
external_state:
  reported_by: hermes
  status: running
  reported_at:

pantheon_observation:
  observed_at:
  freshness: fresh | stale | unreachable | unknown
```

```text
Hermes unreachable != run failed
last known running != currently running with certainty
Hermes completed != projection accepted
```

### 11.5 Transport options

The implementation may use:

- polling for the MVP;
- callback events;
- server-sent events;
- another bounded observation transport.

The governance contract should describe observable states rather than mandate one transport technology.

The browser-facing Cockpit must not receive a privileged Hermes secret or call the execution runtime directly.

```text
Cockpit frontend
-> Cockpit/Pantheon backend
-> governed executor adapter
-> Hermes
```

## 12. Chunking and embeddings

### 12.1 Chunk Set

```yaml
chunk:
  chunk_id:
  projection_id:
  section_path: []
  page_refs: []
  content:
  content_hash:
  chunk_strategy:
  parent_chunk_id:
```

Candidate principles:

- preserve parent headings;
- keep a table together where practical;
- preserve procedural lists;
- preserve page or section references;
- distinguish annexes, notes, tables and body text;
- use stable or reproducible identifiers where possible;
- avoid arbitrary fixed-character splitting as the only strategy.

### 12.2 Embedding Manifest

```yaml
embedding_manifest:
  manifest_id:
  chunk_set_id:
  binding_id:
  model_name:
  model_version:
  vector_dimension:
  created_at:
  content_hashes: []
```

An embedding is produced only when the target indexing policy authorizes it.

### 12.3 Candidate bindings

Candidate bindings may include, after separate review and benchmark:

- PaddleOCR;
- olmOCR;
- Marker;
- Docling or Docling Serve;
- Qwen2.5-VL or a compatible successor;
- bge-m3;
- Qwen Embedding;
- Jina Embeddings;
- PostgreSQL + pgvector.

This list creates no installation, approval, adoption or activation.

Selection criteria should include:

- French and multilingual quality;
- exact citation retrieval;
- table and layout fidelity;
- local execution capability;
- latency and resource use;
- model and API stability;
- version reproducibility;
- license;
- confidentiality posture;
- compatibility with reranking;
- rollback and reindexing cost.

## 13. Index publication

Indexing is distinct from Knowledge publication and project classification.

```yaml
index_publication:
  index_publication_id:
  projection_id:
  chunk_set_id:
  embedding_manifest_id:
  target_index:
  target_scope:
  authorization_ref:
  runtime_status:
  verification_status:
  revoked_at:
```

A projection may be:

- classified but not indexed;
- published as Knowledge but not indexed;
- indexed only in one project scope;
- indexed in a general Knowledge scope;
- revoked from retrieval without deleting the source or projection.

```text
index exists != index verified
index verified != result authoritative
index revoked != source deleted
```

## 14. Retrieval and citations

Every retrieval result should be traceable to:

```yaml
retrieval_result:
  source_id:
  projection_id:
  projection_version:
  chunk_id:
  section_path: []
  page_refs: []
  score:
  retrieval_method:
  embedding_model_version:
  reranker_ref:
  scope:
```

The exposure surface should distinguish:

- source original;
- extracted or normalized projection;
- generated summary;
- metadata candidate;
- retrieved passage;
- accepted citation;
- Evidence Candidate;
- governed Evidence.

## 15. Processing attestations

Runtime logs and manifests should not use an undifferentiated `Evidence` label when they only attest processing.

Preferred local terms:

```text
Processing Attestation
Run Evidence
Execution Observation
```

A processing attestation may include:

- source and output hashes;
- binding and model versions;
- page counts;
- processed page counts;
- warnings;
- table or layout diagnostics;
- duration;
- resource metrics;
- output manifest references;
- error traces.

```text
processing attestation
= evidence that processing occurred under stated conditions

processing attestation
!= proof that every extracted statement is correct
```

## 16. Quality model

A single confidence score is insufficient.

Candidate dimensions:

```yaml
quality:
  page_coverage:
    value:
    method:
    method_version:
  text_coverage:
    value:
    method:
    method_version:
  table_preservation:
  heading_preservation:
  page_alignment:
  unreadable_character_rate:
  language_consistency:
  citation_alignment:
  human_review_status:
  warnings: []
```

Each numeric value should identify its measurement method. An estimated OCR confidence is not ground truth.

## 17. Gates

### Gate A — Source acceptable

Checks:

- source type;
- size;
- integrity;
- origin;
- access posture;
- security posture;
- capture and retention policy;
- allowed scope.

### Gate B — Interpretation sufficient

Checks:

- user intent retained;
- Intake Brief present when needed;
- proposed destination explicit;
- uncertainty visible;
- required verification points recorded;
- confirmation posture determined.

### Gate C — Pipeline authorized

Checks:

- technical and business profiles allowed;
- required Capability Slots available;
- selected bindings approved and active;
- health sufficient for the task;
- local or external execution policy satisfied;
- scope and confidentiality compatible.

### Gate D — Projection reviewable

Checks:

- non-empty output;
- expected pages processed;
- hashes and processing attestations available;
- warnings visible;
- structure usable;
- partial or provisional state declared.

### Gate E — Classification or publication authorized

Checks:

- project links and phases explicit;
- Knowledge family explicit;
- user selection or allowed publication policy present;
- conflicts and duplicates exposed;
- destructive merge prohibited without review.

### Gate F — Index publication authorized

Checks:

- target scope;
- projection and chunk set;
- embedding binding approval;
- confidentiality and isolation;
- reindex and revocation posture;
- retrieval verification expectation.

### Gate G — Binding activation or update authorized

Checks:

- installation status;
- health;
- approval;
- benchmark;
- data posture;
- version compatibility;
- rollback;
- explicit activation or update decision.

## 18. Human review posture

Human review should be proportional.

Human review is not required merely because a source was processed.

A user's explicit direct selection may count as the classification decision.

Automatic processing or Knowledge publication may be allowed under a governed policy when:

- the original source is preserved;
- provenance is retained;
- review status remains visible;
- no silent overwrite or semantic merge occurs;
- no Evidence or memory promotion occurs;
- no external action is triggered;
- low-quality or sensitive cases escalate.

Human review is required before, at minimum:

- destructive source replacement;
- semantic merge with an existing Knowledge Item where meaning may change;
- promotion to Evidence or the Registre Probatoire;
- consequential reliance on legal, contractual, regulatory or safety content when policy requires it;
- external action based on the derived content;
- activation of a new binding;
- update authorization where compatibility or rollback is uncertain.

## 19. Responsibility split

### 19.1 Pantheon governs

Pantheon governs:

- lifecycle vocabulary;
- source scope and provenance requirements;
- classification and publication consequences;
- Capability Slots and binding status;
- policy checks;
- gates;
- projection review and active-selection status;
- indexing scope and revocation;
- access and download policy references;
- processing attestation requirements;
- activation, update and rollback visibility;
- human-decision requirements.

Pantheon does not execute:

- source download;
- OCR;
- document conversion;
- summarization;
- chunking;
- embeddings;
- vector storage operations;
- polling workers;
- callbacks;
- queues;
- schedulers;
- model hosting.

### 19.2 Hermes executes

Hermes may:

- inspect the captured source;
- reformulate the subject and intake intention;
- propose technical and business profiles;
- call native extraction, OCR, layout, conversion and embedding bindings;
- generate descriptions and summaries;
- create output manifests;
- report progress;
- request policy checks;
- return candidate outputs and processing attestations.

Hermes must not:

- silently expand project or Knowledge scope;
- classify a proposal as an approved decision;
- activate or install a binding merely because it is available;
- overwrite an earlier projection silently;
- promote content to Evidence or durable memory;
- hide warnings or source provenance.

### 19.3 Cockpit and OpenWebUI expose

They may:

- accept a file, URL or source reference;
- capture a direct destination or leave the item unclassified;
- show project and Knowledge context;
- send bounded context to Hermes through the backend;
- display Hermes' reformulation;
- display progress and warnings;
- display source and projection views;
- expose source downloads subject to permission;
- display candidate classification and publication decisions;
- capture a human correction, confirmation or rejection.

They must not:

- hold privileged Hermes secrets in the browser;
- bypass Pantheon gates;
- present a generated summary as the source;
- fabricate progress;
- perform OCR, embeddings or indexing in the Cockpit layer;
- become the system of authority for project or Knowledge truth.

### 19.4 The human decides

The human decides where consequence requires:

- destination correction;
- conflict resolution;
- destructive merge;
- Evidence promotion;
- consequential reliance;
- external action;
- binding adoption, activation or update;
- rollback choice.

## 20. Capability Slot view

```yaml
capability_slot: governed_document_intake_and_processing
abstract_function: >-
  capture a source, understand the intake context, produce traceable derived
  representations, classify or publish them in bounded scopes, and optionally
  index them without collapsing source, projection, Knowledge, Evidence or memory.
candidate_binding:
  executor: Hermes
  skill: pantheon-document-intake
  specialized_bindings:
    - native extraction
    - OCR
    - layout understanding
    - Markdown conversion
    - summarization
    - chunking
    - embeddings
    - vector storage
implementation_status: documented non-implemented governance model; co-located executable slices may exist under `implementation/`
installation_status: to verify per binding
health_status: to verify per binding
update_status: to verify per binding
activation_status: not authorized by this document
pantheon_gates:
  - source acceptable
  - interpretation sufficient
  - pipeline authorized
  - projection reviewable
  - classification or publication authorized
  - index publication authorized
  - binding activation or update authorized
```

## 21. Repository placement

### Pantheon Next governance

Owns:

- this governance model;
- status distinctions;
- contracts and candidate data shapes;
- Capability Slot classification;
- gate definitions;
- conformance expectations;
- reconciliation against active doctrine.

### Pantheon implementation under `implementation/`

Owns co-located candidate executable product implementation such as:

- Cockpit intake UI;
- Cockpit backend routes;
- database migrations;
- source storage adapter;
- progress display;
- OpenWebUI Tool implementation;
- integration scenarios;
- end-to-end tests.

Historical `pantheon-mvp` commits or PRs remain provenance only; they are not a second active implementation owner.

### Hermes-side executable repository or runtime

Owns:

- the `pantheon-document-intake` Skill;
- runtime adapters;
- model and service calls;
- external job/status mechanisms;
- processing implementation;
- return manifests.

Executable Hermes-side code does not move into Pantheon governance merely because Pantheon governs it.

## 22. Delivery sequence

### Phase 0 — repository alignment

- compare this proposal to active documents, schemas and current co-located implementation under `implementation/`;
- classify each element as implemented, external, partial, documented non-implemented, to verify, obsolete or not applicable;
- identify contradictions and owners;
- produce the smallest compatible delta.

### Phase 1 — Intake and Source Capture

- Intake Item;
- unclassified or direct destination;
- immutable capture reference;
- source download policy;
- origin and hash;
- no OCR requirement yet.

### Phase 2 — Document and Knowledge relationships

- Document Record;
- multi-project links and per-link phase;
- general Knowledge Item;
- multi-source Knowledge links;
- descriptions and summaries;
- compatibility with current project-scoped cards.

### Phase 3 — Intake Brief and Hermes handoff

- Intake Intent;
- Intake Brief;
- structured bounded action request;
- candidate Hermes Skill contract;
- policy check and explicit correction path.

### Phase 4 — Pipeline Run and projections

- run and step observations;
- raw and normalized Markdown;
- versioned projections;
- progress display;
- processing attestations;
- non-destructive reprocessing and active-selection rollback.

### Phase 5 — Chunking and index publication

- Chunk Set;
- Embedding Manifest;
- explicit Index Publication;
- target-scope isolation;
- revocation and reindexing;
- retrieval trace.

### Phase 6 — Binding benchmark and control-plane display

- corpus benchmark;
- installation, health, approval, activation and update axes;
- binding comparison;
- rollback evidence;
- no installation route in Pantheon.

## 23. Acceptance criteria

The candidate model is coherent when:

1. an unclassified source can be captured before destination selection;
2. a user can directly target general Knowledge or one or more projects;
3. project phases remain flat and have no mandatory subfolders;
4. one source can support several project links without binary duplication;
5. one Knowledge Item can cite several sources;
6. the original is preserved and downloadable when authorized;
7. Hermes may first reformulate the subject and proposed treatment;
8. the approved execution request remains structured and bounded;
9. Cockpit actions remain simple and context-oriented;
10. the Cockpit shows only progress actually exposed by Hermes;
11. percentages are backed by measurable units;
12. raw and normalized Markdown remain distinct projections;
13. descriptions and summaries remain derived and versioned;
14. a new run creates a new projection rather than overwriting the prior one;
15. project classification, Knowledge publication and index publication remain distinct;
16. index publication can be revoked without deleting the source;
17. retrieval can trace back to source, projection, pages and model version;
18. runtime logs are not confused with professional Evidence;
19. the model remains independent of named OCR, VLM, converter and embedding bindings;
20. no Pantheon runtime, queue, scheduler, model host, installer or automatic approval engine is introduced.

## 24. Open questions for implementation reconciliation

Before executable work, the current co-located Pantheon implementation and Hermes bindings must answer:

1. Does the current `Document` model represent source, classification record, projection or several at once?
2. Where are original bytes stored and how is immutability enforced?
3. Can one current document link to several projects?
4. Is phase stored on the document or on the project-document relationship?
5. Does current Knowledge copy content or reference a source and projection?
6. Can one Knowledge Item reference several sources?
7. Which current routes expose original download?
8. Which current routes are project-scoped by design?
9. Which current pgvector tables or indexes are active?
10. How does OpenWebUI currently send a file or URL?
11. What Hermes API or Skill contract can return an Intake Brief?
12. What progress states can Hermes expose: global, per step, per page or per chunk?
13. Does Hermes support polling, callback or event streaming for this use?
14. What cancellation semantics are real?
15. What is the current rollback mechanism for Knowledge updates and index versions?
16. Which existing schemas can be extended without creating a parallel object model?
17. Which status terms must be reused rather than duplicated?
18. Which identities and permissions control source download across project and general Knowledge scopes?

## 25. Non-objectives

This proposal does not:

- install PaddleOCR, Qwen, olmOCR, Marker, Docling, an embedding model or pgvector;
- declare one candidate binding adopted;
- create an installation route;
- create a scheduler or queue;
- create a job worker;
- create a vector database;
- make Pantheon a provider router;
- make the Cockpit a runtime;
- make OpenWebUI a control plane;
- make Hermes an approval authority;
- make indexing automatic for every source;
- make a generated summary Evidence;
- promote any document into the Registre Probatoire;
- authorize real professional-dossier use;
- authorize production activation.

## 26. Final decision candidate

```text
The Cockpit captures source, user intent and context, then displays progress,
projections, provenance and decisions.

Hermes may first understand and reformulate the intake, then execute an approved
bounded processing request through interchangeable document capabilities.

Pantheon governs source scope, lifecycle status, projection use, project and
Knowledge consequences, indexing scope, runtime posture and rollback visibility.

The original remains recoverable. Derived representations remain versioned.
Project documents and general Knowledge remain distinct but may share sources.
The human decides where the consequence requires a human decision.
```
