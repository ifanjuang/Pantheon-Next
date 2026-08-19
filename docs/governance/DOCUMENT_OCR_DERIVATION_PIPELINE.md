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

An admitted OCR or classification task may be orchestrated by Hermes and executed by the selected external runtime or by a bounded native binding. Native execution does not bypass the admitted Task Contract, provenance requirements or applicable gates. Pantheon governs identity, scope, provenance, state and consequential gates. The human remains the authority for consequential adoption and review.

## 2. Capability Slots

### 2.1 `document_ocr`

```yaml
capability_id: document_ocr
function: produce searchable text and/or a searchable archival document representation from an exact captured source version
owner_layer: external runtime
orchestrated_by: Hermes when governed orchestration is required
executed_by: selected external runtime or bounded native binding
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
native_execution != task_authorized
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
-> admitted OCR task
-> Hermes orchestration or bounded native execution
-> governed derivative
-> optional Paperless searchable representation or version
-> candidate classification
-> reviewed metadata mutation
```

Paperless native OCR may be used as a selected native binding or operational fallback under the same Task Contract, provenance and policy requirements. Its native execution does not make Paperless the governance layer and does not require Hermes to host the OCR engine. It must not silently re-run Tesseract over a superior preprocessed derivative when OCR skip or equivalent controls are required.

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

## 12. Obsidian-facing conversion posture

The Obsidian workspace has a narrower human-facing need than the governed project-document pipeline: a user may receive a PDF or office document, place it in the vault, convert it to readable Markdown and reorganize that Markdown later.

The current IFJA working choice, recorded on 2026-08-19, is:

```text
Obsidian conversion surface
= SourceDown selected for the real daily-workspace path

later comparison candidate
= OCR-AI / L3-N0X/obsidian-marker
```

This is a workspace integration choice, not a new Capability Slot or a change to the canonical `document_structural_analysis` binding. `HERMES_CAPABILITY_BINDINGS.md` continues to record Docling as the preferred structural-analysis candidate.

The public SourceDown plugin listing observed on 2026-08-19 documents:

- MarkItDown as the default conversion engine;
- optional Docling and Marker engines;
- conversion from imported files and files already present in the vault;
- generated Markdown plus source/conversion metadata;
- extracted assets stored beside the generated note;
- duplicate imports preserved with numbered filenames;
- desktop-only operation in the current public listing.

The currently available public material does **not** establish whether SourceDown preserves the complete Docling JSON / `DoclingDocument`, exposes every current Docling pipeline option, or can direct the structured JSON and assets independently from the Markdown. Those points remain local qualification items and must not be inferred from the plugin UI.

Therefore:

```text
SourceDown selected for workspace use
!= SourceDown adopted as Pantheon document runtime

SourceDown conversion success
!= document professionally validated

SourceDown Markdown
!= original source

SourceDown duplicate filename handling
!= professional revision semantics
```

OCR-AI remains a later candidate, not a second active pipeline. Its public repository documents batch PDF conversion, mobile-compatible plugin operation when an API endpoint is reachable, optional PDF movement, asset subfolders and smart integration into an existing same-named folder. These are useful UX characteristics to compare later, but they do not justify parallel production ingestion or a second structural-analysis owner.

References observed for this posture:

- SourceDown public Obsidian listing: `https://community.obsidian.md/plugins/sourcedown`;
- OCR-AI / Obsidian Marker: `https://github.com/L3-N0X/obsidian-marker`;
- parser qualification remains tracked in Pantheon-Next #662.

## 13. Markdown quality convergence order

Do not introduce a generic AI Markdown cleaner before exhausting the native structured path.

The preferred order is:

```text
exact source
-> SourceDown workspace conversion surface
-> selected structural parser profile
-> parser-native structural repair
-> existing deterministic compilation / rendering seam
-> targeted agentic repair only when ambiguity remains
-> final Markdown projection
-> Obsidian one-way Hindsight sync when that vault is in scope
```

### 13.1 Docling native heading hierarchy first

Docling PR `docling-project/docling#3633`, merged on 2026-06-23, added opt-in PDF heading-level inference. The implementation changes heading levels only; it does not add, remove or reorder document items. Numbering is the primary signal and style is a fallback. The feature is off by default; style fallback requires parsed-page data.

Before adding a downstream hierarchy fixer, the same-corpus qualification must therefore test the current Docling profile with native heading hierarchy enabled where the active SourceDown/Docling integration can expose the option.

```text
Docling default profile
!= Docling heading-hierarchy-enabled profile
```

If SourceDown does not expose the option, record that as an integration limitation. Do not silently bypass SourceDown with an unrelated permanent parser path merely to enable one option.

Reference: `https://github.com/docling-project/docling/pull/3633`.

### 13.2 Deterministic cleanup before agentic rewriting

The current `pantheon-mvp` structured-extraction compiler already owns deterministic structural normalization for the candidate runtime path, including Docling-native structured units, Markdown fallback and explicit table repair/quality flags.

If a human-facing canonical Markdown renderer is demonstrated as necessary, prefer extending that existing compilation responsibility rather than adding a separate cleaner service.

Safe deterministic presentation work may include:

```text
blank-line and whitespace normalization
Markdown heading syntax normalization without semantic relabelling
stable list rendering
explicit table rendering from known structure
asset/link normalization
removal of deterministic parser/export noise when provenance is preserved
```

It must not silently paraphrase clauses, change numbers or units, invent missing text, reinterpret professional requirements or turn a parser guess into a validated statement.

```text
cleaner output != source truth
format normalization != semantic correction
well-formed Markdown != professionally verified content
```

### 13.3 Docling Agent is a targeted repair candidate, not the default step

`docling-project/docling-agent` is an official Docling project. The repository observed on 2026-08-19 declares version `0.6.0`, `Development Status :: 3 - Alpha`, and explicitly describes the package as immature/work-in-progress.

Its editing agent accepts a `DoclingDocument` and applies targeted natural-language edits. The upstream `task-configs/editor.yaml` includes the exact structural-repair example:

```text
Review the indentation levels of the sections and correct if necessary
```

This makes Docling Agent a relevant **fallback candidate for ambiguous structural repair**, especially heading hierarchy that remains wrong after parser-native inference. It is not a reason to run an LLM over every document.

Use is gated by three conditions:

1. the exact Docling structured document is available to the repair step;
2. deterministic/native repair has been insufficient on the same source;
3. the output remains a traced derivative and any consequential semantic change is reviewable.

If SourceDown only exposes the final Markdown and does not preserve/reveal the Docling structured document, do not create a hidden second permanent conversion pipeline solely to insert Docling Agent. First qualify whether the structured artifact can be retained or exposed through the selected path.

References:

- `https://github.com/docling-project/docling-agent`;
- `https://github.com/docling-project/docling-agent/blob/main/task-configs/editor.yaml`.

### 13.4 Hindsight remains downstream and unchanged

The official Obsidian/Hindsight posture is already owned by `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`:

```text
Obsidian Markdown source
-> designated one-way synchronization path
-> Hindsight derived bank
-> bounded read consumers
```

Hindsight does not need to know whether SourceDown, Docling or a later OCR-AI candidate produced the note. It receives the final Markdown selected for synchronization and remains derived memory/index, not source authority.

Document revision/currentness semantics also remain outside the converter:

```text
new parser output != new professional revision
same filename != same source
higher index != professional authority
Hindsight recall != professional currentness
```

A revised professional document may update one stable human-facing Markdown projection while exact historical source revisions remain governed by the existing Document lifecycle. A chronological series such as site reports remains a series of distinct documents rather than versions merely because later reports exist.

### 13.5 Qualification sequence before implementation

The next bounded qualification should compare, on one already-frozen IFJA control source from #662:

```text
A. SourceDown current/default profile
B. SourceDown with current Docling profile where selectable
C. Docling with native heading hierarchy enabled where SourceDown exposes it
D. deterministic presentation normalization only if defects remain
E. Docling Agent targeted hierarchy repair only if structured ambiguity remains
F. OCR-AI later as a separate workspace UX/parser candidate
```

Record for each executed profile:

- exact plugin/parser/model identities;
- source digest;
- configuration;
- Markdown output digest;
- structured JSON availability or absence;
- heading hierarchy, reading order, table and asset behavior;
- whether user edits survive a re-conversion/update workflow;
- whether the resulting note remains one intended Hindsight document rather than accidental numbered duplicates.

No renderer, Docling Agent integration, OCR-AI activation or additional parser adapter should be implemented until this comparison demonstrates a concrete gap that the existing SourceDown + Docling + compiler responsibilities cannot cover.
