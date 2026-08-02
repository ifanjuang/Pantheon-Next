# Pantheon Next — Document OCR Derivation Pipeline

Status: candidate support doctrine — documented non-implemented.

Boundary profile: candidate_support_note.

This document defines the governed placement of OCR and document derivations without making Pantheon an OCR runtime, scheduler, queue, provider router, document store, plugin manager or automatic approval system.

It complements `DOCUMENT_LIFECYCLE_GOVERNANCE.md` and the product-specific `PAPERLESS_NGX_DOCUMENT_RUNTIME.md`. It does not replace Source, Projection, Trace, Knowledge, Evidence, Claim, ChangeCandidate or Capability Slot models.

## 1. Decision

OCR is an independent abstract capability.

```text
document_source_management
!= document_ocr
!= document_structural_analysis
!= document_classification
!= document_validation
```

Paperless-ngx may preserve or expose a document and may consume an OCR-derived representation. It does not own the governed OCR capability merely because it includes native OCR.

Hermes may execute an admitted OCR or classification task through an authorized binding. Pantheon governs identity, scope, provenance, state and consequential gates. The human remains the authority for consequential adoption and review.

## 2. Capability Slots

### 2.1 `document_ocr`

```yaml
capability_id: document_ocr
function: produce searchable text and/or a searchable archival document representation from an exact captured source version
owner_layer: external runtime
executed_by: Hermes through a selected binding
exposed_by: Cockpit as status, warnings and reviewable derivations
governed_by: Pantheon Next
approved_by: human where remote transmission, activation, consequential replacement or real-dossier use requires approval
```

Candidate bindings may include:

```text
tesseract
paddleocr
google_document_ai
azure_document_intelligence
adobe_document_services
specialized_local_vlm
```

This list is comparative candidate data only.

```text
binding_catalogued != binding_selected
binding_selected != dependency_adopted
installed != approved
healthy != safe
runtime_success != Evidence
```

### 2.2 Adjacent slots

```text
document_source_management
= capture, preserve, version, retrieve and expose source documents

document_structural_analysis
= produce layout-aware blocks, tables, headings, reading order or Markdown

document_classification
= propose title, correspondent, type, tags, project links and phase links

document_validation
= check completeness, consistency, uncertainty and derivation mismatch signals
```

A single product may implement several functions, but availability does not collapse the slots or transfer authority.

## 3. Canonical derivation chain

```text
exact Source Capture version
├── searchable PDF or PDF/A derivative
├── plain-text derivative
├── layout-aware structural derivative
├── table/equation/image derivative
├── thumbnail or preview derivative
└── index or embedding projection
```

Required invariants:

- the original exact source version remains immutable and superior to every derivative;
- no OCR result silently replaces the original source;
- every derivative points to one exact source version;
- every derivative records the producing binding and execution trace;
- a later reprocessing run creates a new derivative revision rather than rewriting history;
- deleting an index or projection does not delete the original source;
- successful extraction does not establish correctness, Evidence or professional validation;
- a source-management runtime identifier is a backing reference, not Pantheon authority.

## 4. Candidate derivation record

The current `pantheon-mvp` structured-extraction compiler already persists
source-linked extractions, compilation revisions, ordered extraction units and
retrieval chunks. That implementation is a candidate operational slice, not the
complete derivation contract below. Any extension must preserve the following
semantics without renaming the existing objects merely to mirror this document:

```yaml
document_derivation:
  derivation_id: drv_example
  source_id: src_example
  source_version_id: srcv_7
  derivation_kind: searchable_pdf
  mime_type: application/pdf
  archival_profile: PDF/A-2b

  produced_by:
    capability_slot: document_ocr
    binding_id: google_document_ai
    binding_version: observed-version
    execution_id: run_example
    parameters_profile: ocr-profile-v1

  produced_at: 2026-07-31T15:00:00Z
  digest: sha256:example
  page_count: 84
  pages_processed: 84
  languages: [fr]

  quality_observations:
    warnings: []
    mismatch_count: 0
    confidence_summary: unknown

  status: candidate
  supersedes_derivation_id: null
```

Minimum required provenance:

```text
exact source version
binding identity
observed binding version
execution identity
parameter profile
output digest
production time
warnings and incomplete-page signals
```

## 5. Validation and silent-failure posture

Extraction success is not sufficient. The pipeline must be able to surface silent mismatch risks such as:

- missing pages or regions;
- changed numbers, symbols or units;
- corrupted table cells;
- altered equations;
- incorrect reading order;
- low-confidence or empty sections;
- a second OCR pass degrading an already searchable document.

A validation binding may compare the derivative against the original page representation and return observations. Those observations remain candidate signals.

```text
no_warning != verified_correct
confidence_score != truth
visual_match_signal != Evidence
```

The architecture must support a blocking or review-required state when the source is consequential and mismatch signals exceed the applicable policy threshold.

## 6. OCR routing profiles

Candidate policy profiles:

```text
LOCAL_STANDARD
- ordinary readable documents
- local OCR binding
- no external document transmission

LOCAL_ADVANCED
- difficult scans, plans or complex layouts
- specialized local OCR or VLM binding
- explicit resource and confidentiality scope

REMOTE_EXCEPTION
- external OCR provider
- explicit provider, document scope and retention posture
- human or policy gate before transmission where required
```

Remote use remains disabled unless separately reviewed and authorized.

Pantheon must not become the provider router. Hermes or an external execution layer may resolve an authorized binding within the admitted Task Contract.

## 7. Paperless-ngx placement

Paperless-ngx remains an optional `document_source_management` binding.

Valid placement:

```text
scanner or source intake
-> exact source preservation
-> admitted OCR task through Hermes
-> governed derivative
-> optional Paperless searchable representation or version
-> candidate classification
-> reviewed metadata mutation
```

Paperless native OCR may be used only as one selected binding or operational fallback under the same provenance and policy requirements. It must not silently re-run Tesseract over a superior preprocessed derivative when OCR skip or equivalent controls are required.

```text
Paperless OCR text != source truth
Paperless metadata != governed classification
Paperless search hit != Evidence
Paperless task success != professional validation
```

## 8. Classification and mutation path

Classification must produce a candidate, not an immediate authoritative write.

```yaml
classification_candidate:
  candidate_id: cc_example
  source_id: src_example
  source_version_id: srcv_7
  derivation_ids: [drv_example]
  proposed_title: Example title
  proposed_correspondent: Example correspondent
  proposed_document_type: invoice
  proposed_tags: [insurance]
  proposed_project_links: []
  confidence_by_field: {}
  supporting_spans: []
  uncertainties: []
  base_revision: 3
```

Consequential metadata changes should follow:

```text
Classification Candidate
-> validation observations
-> ChangeCandidate with base revision and provenance
-> human review where required
-> authorized mutation
-> runtime observation
-> updated Cockpit projection
```

A successful API write is not approval and does not promote the result to Knowledge or Evidence.

## 9. Runtime and GPU boundary

Batching, model residency, GPU utilization, retries, queues and concurrency belong to Hermes or the selected external inference runtime.

Pantheon may observe only the governed task states needed for decision and traceability, for example:

```text
requested
admitted
running
candidate_output_available
review_required
failed
cancelled
```

Pantheon does not schedule OCR jobs, maintain a GPU queue, select providers automatically or infer authorization from runtime throughput.

## 10. Cockpit projection

The Cockpit may show a simple Document projection containing:

```text
source availability
current preferred derivative
OCR status
binding family when useful
processing warnings
validation or mismatch status
classification candidate status
review-required reason
open original
open derivative
request reprocessing
review proposed classification
```

The card remains a UX projection. It must not dictate the backend model or expose provider queues and OCR internals by default.

## 11. MVP reconciliation and extension gate

`pantheon-mvp` already implements a bounded Docling path:

```text
exact document bytes
-> structured extraction identity
-> revisioned compilation
-> ordered units with section context and diagnostics
-> retrieval chunks tied to the compilation identity
```

This existing slice does not yet establish a universal derivative record,
remote-transmission policy, OCR-provider router, visual source verification or
automatic Evidence admission. Before extending it toward the broader pipeline,
stabilize:

1. the exact derivative record schema;
2. source-version and digest semantics;
3. allowed status vocabulary;
4. remote-transmission policy fields;
5. idempotence and reprocessing rules;
6. ChangeCandidate mapping for classification;
7. read-only Cockpit projection requirements;
8. synthetic fixtures for silent extraction mismatch and double-OCR degradation.

Until those remaining contracts are reviewed:

```text
documented != implemented
candidate binding != adopted dependency
runtime receipt != Evidence
UI status != authorization
```
