# Pantheon Next — Document OCR Derivation Pipeline

Status: candidate support doctrine — provider-agnostic derivation boundary / documented non-implemented.
Boundary profile: candidate_support_note.

This document owns the governed placement of OCR and document derivations. It does not make Pantheon an OCR runtime, scheduler, queue, provider router, document store, plugin manager or automatic approval system.

It complements `DOCUMENT_LIFECYCLE_GOVERNANCE.md` and the existing Source/document contracts. It does not replace Source, Projection, Trace, Knowledge, Evidence, Claim, ChangeCandidate or Capability Slot models.

## 1. Decision

OCR is an independent capability.

```text
document_source_management
!= document_ocr
!= document_structural_analysis
!= document_classification
!= document_validation
```

A source-management product may expose native OCR, but product bundling does not transfer capability ownership or governance authority.

An admitted OCR or classification task may be orchestrated by Hermes and executed by the selected external runtime or bounded native binding. Native execution does not bypass the Task Contract, provenance requirements or applicable gates.

```text
provider selected != dependency adopted
native execution != task authorized
runtime success != Evidence
```

## 2. Capability slots

### `document_ocr`

```yaml
capability_id: document_ocr
function: produce searchable text and/or an archival searchable representation from an exact captured source version
owner_layer: external runtime
orchestrated_by: Hermes when governed orchestration is required
executed_by: selected external runtime or bounded native binding
exposed_by: Pantheon Cockpit as status, warnings and reviewable derivations
governed_by: Pantheon Next
approved_by: human where remote transmission, activation, consequential replacement or real-dossier use requires approval
```

Candidate bindings may include Tesseract, PaddleOCR, remote document-intelligence services or specialized local VLMs. This is comparative candidate data only.

Adjacent responsibilities remain distinct:

```text
document_source_management = capture/preserve/version/retrieve exact sources
document_structural_analysis = layout-aware blocks/tables/headings/Markdown
document_classification = propose metadata and project/phase links
document_validation = check completeness, consistency and mismatch signals
```

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
- every derivative records producing binding, version, parameters, execution identity, digest and time;
- reprocessing creates a new derivative revision rather than rewriting history;
- deleting an index/projection does not delete the source;
- extraction success does not establish correctness, Evidence or professional validation;
- a provider/runtime identifier is a backing reference, not Pantheon authority.

A candidate derivation therefore needs at least:

```yaml
document_derivation:
  derivation_id:
  source_id:
  source_version_id:
  derivation_kind:
  mime_type:
  produced_by:
    capability_slot: document_ocr
    binding_id:
    binding_version:
    execution_id:
    parameters_profile:
  produced_at:
  digest:
  quality_observations:
    warnings: []
    mismatch_count: 0
    confidence_summary: unknown
  status: candidate
  supersedes_derivation_id:
```

## 4. Validation and silent-failure posture

Extraction success is insufficient. Validation must be able to surface missing pages/regions, changed numbers or units, corrupted tables, altered equations, incorrect reading order, low-confidence/empty sections and double-OCR degradation.

```text
no_warning != verified_correct
confidence_score != truth
visual_match_signal != Evidence
```

Consequential sources may require blocking or human review when mismatch observations exceed the applicable policy threshold.

## 5. Routing profiles

Candidate profiles:

```text
LOCAL_STANDARD
  ordinary readable documents; local binding; no external transmission

LOCAL_ADVANCED
  difficult scans/plans/layouts; specialized local OCR/VLM; explicit resource/confidentiality scope

REMOTE_EXCEPTION
  external provider; explicit provider/document/retention scope; gate before transmission when required
```

Pantheon must not become the provider router. Hermes or another external execution layer may resolve an authorized binding within the admitted Task Contract.

## 6. Source-management provider boundary

A source-management provider is optional. When one is selected, it may preserve versions, expose search or run native OCR, but those facilities remain subordinate to the same source/provenance and policy rules.

```text
provider OCR text != source truth
provider metadata != governed classification
provider search hit != Evidence
provider task success != professional validation
provider absent != document ingestion unavailable
```

The current selected architecture therefore requires no DMS product. Bounded local/NAS sources remain a valid source path, and Obsidian remains a human Markdown workspace rather than a professional source authority.

## 7. Classification and mutation path

Classification produces a candidate, not an immediate authoritative write.

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

## 8. Runtime boundary

Batching, model residency, GPU utilization, retries, queues and concurrency belong to Hermes or the selected external inference runtime.

Pantheon may observe only task states needed for decision and traceability, for example `requested`, `admitted`, `running`, `candidate_output_available`, `review_required`, `failed` and `cancelled`.

Pantheon does not schedule OCR jobs, maintain a GPU queue, select providers automatically or infer authorization from runtime throughput.

## 9. Cockpit projection

The Cockpit may project source availability, preferred derivative, OCR state, binding family when useful, warnings, mismatch status, classification-candidate state, review reason and links to original/derivative.

```text
projection != persistence
UI status != authorization
```

The UI must not dictate the backend model or expose provider queues and OCR internals by default.

## 10. Current executable seam

The co-located candidate implementation under `implementation/` already demonstrates a bounded Docling/structured-extraction path with exact source linkage, revisioned compilation, ordered extraction units, diagnostics and retrieval chunks.

That existing slice is not a universal OCR/derivative authority. Extension requires demonstrated need and must reuse its deterministic compilation responsibility rather than creating a second cleaner/pipeline.

## 11. Obsidian-facing conversion posture

The Obsidian workspace has a narrower human-facing need: place a PDF/office document in the vault, convert it to readable Markdown and reorganize the note later.

Current qualified working direction from 2026-08-19:

```text
SourceDown = selected workspace conversion surface
Docling = preferred structural-analysis candidate where available
OCR-AI / L3-N0X/obsidian-marker = later comparison candidate
```

SourceDown publicly documents MarkItDown as its default engine, optional Docling/Marker engines, imported/existing-file conversion, generated Markdown plus source/conversion metadata, adjacent extracted assets, numbered duplicate filenames and desktop-only operation in the reviewed listing.

Public material did not establish whether SourceDown preserves the complete `DoclingDocument`, exposes all Docling pipeline options, or can independently route structured JSON/assets. Those remain qualification questions.

```text
SourceDown selected for workspace use != Pantheon document runtime adopted
SourceDown conversion success != professionally validated
SourceDown Markdown != original source
duplicate filename handling != professional revision semantics
```

OCR-AI remains a later candidate, not a second active pipeline.

## 12. Markdown quality convergence order

Do not introduce a generic AI Markdown cleaner before exhausting the structured path.

```text
exact source
-> SourceDown workspace conversion
-> selected structural parser profile
-> parser-native repair
-> existing deterministic compilation/rendering seam
-> targeted agentic repair only when ambiguity remains
-> final Markdown projection
-> optional one-way Hindsight synchronization
```

Docling heading-level inference should be qualified before adding downstream hierarchy repair. Deterministic cleanup may normalize whitespace, Markdown heading syntax, stable lists, known table structure and asset/link presentation, but must not paraphrase clauses, change numbers/units or invent missing content.

Docling Agent remains a targeted fallback candidate for ambiguous structural repair only when the exact structured document is available and deterministic/native repair proved insufficient. Agentic repair output remains a traced derivative.

Hindsight remains downstream derived memory/index:

```text
Obsidian Markdown source -> designated sync -> Hindsight derived bank -> bounded read consumers
Hindsight recall != truth
memory != Evidence
```

## 13. Qualification sequence

Before implementing another parser, cleaner or agentic repair path, compare on one frozen control source:

```text
A. SourceDown current/default profile
B. SourceDown + current Docling profile where selectable
C. Docling native heading hierarchy where exposed
D. deterministic presentation normalization only if defects remain
E. targeted Docling Agent repair only if structured ambiguity remains
F. OCR-AI later as a separate workspace UX/parser candidate
```

Record exact identities, source digest, configuration, output digest, structured-artifact availability, heading/reading-order/table/asset behavior, edit survival and duplicate-document behavior.

No new adapter is justified until this comparison demonstrates a gap the existing SourceDown + Docling + compilation responsibilities cannot cover.
