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

The Obsidian workspace has a narrower human-facing need: preserve the exact source file, optionally produce readable Markdown when that is useful to a person or to the already-qualified Markdown ingestion path, and avoid turning every structured record into a note.

Current operator choice recorded on 2026-09-06:

```text
exact PDF / office source = preserved source representation
OCR-AI / L3-N0X/obsidian-marker = selected optional/manual workspace PDF-to-Markdown convenience surface
Docling = preferred document_structural_analysis candidate under #662
Hindsight native file retain = not selected in the current qualified workspace producer path
SourceDown = historical prior workspace choice, not the current selected daily conversion surface
```

This selection is intentionally narrow. It does **not** classify Marker as the winning structural-analysis provider, does not close #662, does not adopt Marker as a Pantheon dependency and does not require a Markdown derivative for every binary source.

```text
Marker workspace selection != structural-analysis qualification
Marker conversion success != professionally validated
Marker Markdown != original source
Markdown present != source replacement
no Markdown derivative != source unavailable
```

The ordinary manual path is therefore:

```text
exact PDF source
-> optional OCR-AI / Marker conversion in Obsidian
-> readable Markdown derivative
-> existing designated hindsight-obsidian-sync producer when that Markdown is inside admitted sync scope
-> Hindsight derived recall
```

Do not simultaneously activate a second native-PDF Hindsight producer for the same source merely because `/files/retain` exists. Native Hindsight file ingestion may be re-qualified later if it demonstrates a real simplification over the existing Markdown producer lifecycle.

The earlier SourceDown qualification logs remain historical provenance and are not rewritten to pretend that the earlier operator choice never existed.

## 12. Workspace metadata and human notes

The Workspace/Cockpit may observe or derive document metadata without serializing every field into Markdown.

Keep three classes distinct:

```text
reconstructible observation
= filename, MIME, digest, filesystem timestamps, parser-derived structure, detected index/date/type candidates

human-authored workspace material
= notes, comments, corrections, intentionally authored summaries or Markdown knowledge

derived cache/projection
= generated summary, essentials, extracted index/date candidates, optional Markdown representation
```

For index/date/reference extraction, preserve what was actually observed and where it was observed before any professional admission:

```yaml
extracted:
  issuer_reference_candidates:
    - value: A-203
      source_locator: title_block
  index_candidates:
    - value: D
      source_locator: title_block
  date_candidates:
    - value: 2026-08-28
      label_observed: Date
      role_candidate: issue_date
      source_locator: title_block
```

```text
detected index != admitted Document version
highest-looking index != purpose-specific currentness
date printed in document != receipt date
date printed in document != effective date
human note != extracted fact
derived summary != Evidence
```

No new production `document.yaml` or workspace-metadata schema is adopted by this posture. Reuse the existing Workspace Manifest Inspector candidate, Professional Document owners and `document_knowledge_slice` structure contract. Persist only non-reconstructible human material or explicitly useful derived cache when justified; routing remains calculated where existing owners can calculate it.

A derived summary may retain its exact source basis, for example:

```yaml
derived_summary:
  text: Plan architectural du RDC...
  based_on_digest: <exact source digest>
  generation_status: generated_unreviewed
```

When the exact source digest changes, the old summary is stale rather than silently current.

## 13. Markdown, Hindsight and Project Anatomy

Do not make Markdown or Hindsight the universal interchange format for structured project state.

Use Markdown when it has direct human/workspace value:

```text
human-authored notes
reviewable summaries
meeting notes
reusable editorial Knowledge
optional Marker/OCR derivative
optional reconstructible project narrative such as Projet.md
```

The designated Hindsight reference path remains one-way:

```text
Obsidian Markdown
-> designated hindsight-obsidian-sync producer
-> Hindsight derived bank
-> bounded read/recall consumers
```

```text
Hindsight recall != truth
memory != Evidence
Hindsight ingestion != governed persistence
```

Do not manufacture Markdown copies solely to push these structures through Hindsight:

```text
document_structure
Observation Bundle
Project Anatomy stable_objects
Project Anatomy attribute_claims
Project Anatomy relation_claims
governed Professional Document/currentness records
```

When document analysis produces project semantics, use the existing path:

```text
exact source
-> document structural/semantic analysis when needed
-> canonical Observation Bundle
-> existing review/application path
-> Project Anatomy
-> bounded Hermes/Cockpit projection
```

Hermes may read admitted Project Anatomy through its bounded Project Anatomy context seam. An optional `Projet.md` may summarize that state for human consultation and Hindsight recall, but it remains a reconstructible projection and must not become the only persistence path or a second project-knowledge authority.

```text
Projet.md != Project Anatomy
projection != persistence
source observation != project truth
```

## 14. Structural-analysis qualification sequence

The workspace convenience choice does not pre-judge #662. Structural-analysis providers remain compared on one frozen IFJA corpus through the existing `document_structural_analysis` responsibility.

Current posture:

```text
Docling = preferred candidate / bounded implementation path
Marker = candidate to qualify for structural analysis
other candidates = remain under #662 as recorded there
```

Before replacing the structural-analysis binding or adding parser-specific downstream code, record exact identities, source/config/output digests, structured JSON availability, hierarchy/reading-order/table/assets behavior, reconversion behavior, provenance quality and operational cost.

No new adapter is justified until the comparison demonstrates a gap the existing structural-analysis and deterministic compilation responsibilities cannot cover.
