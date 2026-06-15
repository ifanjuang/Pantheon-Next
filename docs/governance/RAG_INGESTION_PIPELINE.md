# RAG Ingestion Pipeline

Status: to verify — active governance proposal, documentation only.

This document defines how Pantheon Next should govern PDF and document ingestion for RAG-ready knowledge.

It does not implement ingestion.

It does not add dependencies.

It does not define an OpenWebUI plugin.

It does not define a Hermes tool.

It does not introduce a scheduler, queue, provider router, hidden runtime, automatic import pipeline, automatic evidence approval or automatic memory promotion.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Professional RAG quality starts before embeddings.

A PDF should not be treated as reliable context merely because it was uploaded, parsed or indexed.

The ingestion pipeline must transform documents into structured, traceable and reviewable sources.

Core principle:

```text
The PDF becomes an exploitable source.
It does not become validated truth.
```

## Scope

This document covers:

- PDF profile detection;
- converter routing;
- Markdown normalization;
- table and image preservation;
- semantic chunking;
- manifest generation;
- quality reporting;
- OpenWebUI Knowledge packaging;
- optional Postgres registry alignment;
- candidate Hermes skill decomposition;
- governance statuses for source, evidence and memory.

It does not cover:

- actual parser implementation;
- dependency installation;
- Docker deployment;
- OpenWebUI configuration;
- Hermes runtime installation;
- Postgres schema implementation;
- pgvector indexing implementation;
- OCR service deployment.

## Doctrine

The ingestion chain must preserve the Pantheon distinction:

```text
Raw Source
→ Source Reference
→ Ingestion Candidate
→ Knowledge Item
→ Chunk / Retrieval Unit
→ Retrieved Knowledge
→ Context Sufficiency Check
→ Evidence Candidate
→ Evidence Item
→ Evidence Pack
→ Output Candidate
→ Approval Event
→ Register Candidate
→ Registre Probatoire entry
```

`RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` defines the extended evidence-boundary chain around chunking fitness, context sufficiency, Evidence Candidate selection and approval status.

Forbidden shortcuts:

```text
uploaded → validated
converted → approved
indexed → evidence
retrieved → truth
retrieved → memory
quality_passed → human approval
```

## Recommended pipeline

```text
PDF original
→ file hash and metadata
→ PDF profile detection
→ converter selection
→ structured Markdown export
→ table and image extraction
→ Markdown normalization
→ semantic chunking
→ quality doctor
→ manifest generation
→ optional OpenWebUI Knowledge packaging
→ governed Task Contract use
→ scoped Hermes retrieval or analysis
→ Evidence Candidate only if selected
```

The original PDF remains the Raw Source.

The Markdown is a Knowledge Item.

The chunks are retrievable knowledge units.

Evidence and memory require later governed transitions.

## Converter routing

Do not use one universal converter for every PDF.

Use a router.

```text
PDF text-native, simple layout
→ PyMuPDF4LLM

PDF professional, structured, mixed layout
→ Docling

PDF scanned, table-heavy, form-heavy, OCR-heavy
→ Marker

multi-format ingestion at scale
→ Unstructured or Docling, after benchmarks
```

The router should output:

```text
recommended_converter
fallback_converter
ocr_required
layout_complexity
table_complexity
image_density
risk_level
manual_review_recommended
```

## Candidate open-source tools

Candidate tools remain external capabilities.

They are not Pantheon dependencies by default.

| Tool | Candidate use | Governance note |
|---|---|---|
| Docling | default serious document conversion | good candidate for structured PDF and Markdown export |
| PyMuPDF4LLM | fast lightweight PDF-to-Markdown | useful for simple text-native PDFs |
| Marker | complex PDFs, OCR, tables, forms, images, chunks | license and commercial use must be reviewed before adoption |
| Unstructured | broad multi-format preprocessing | useful for larger ingestion platform patterns |
| OpenWebUI Knowledge | user-facing Knowledge/RAG exposure | cockpit surface, not source of truth |

A future adoption must be reviewed through `EXTERNAL_TOOLS_POLICY.md` and `EXTERNAL_REPO_INSPIRATIONS.md`.

## Required outputs

A governed ingestion run should produce at least:

```text
document.md
chunks.jsonl
manifest.json
quality_report.md
assets/ when images are extracted
tables/ when tables are extracted
```

Recommended directory shape:

```text
rag_ready/
  manifest.json
  sources/
    src_<hash>/
      original.pdf
      document.md
      chunks.jsonl
      manifest.json
      quality_report.md
      tables/
      assets/
```

## Markdown format

Markdown should be stable and boring.

It should optimize retrieval, provenance and citation.

It should not optimize decorative rendering.

Recommended frontmatter:

```markdown
---
source_id: src_...
original_file: document.pdf
file_hash: sha256:...
conversion_tool: docling
conversion_version: ...
conversion_date: ...
language: fr
source_type: uploaded_pdf
freshness_status: metadata_insufficient
evidence_status: retrieved_knowledge
memory_status: not_memory
---
```

Recommended anchors:

```markdown
# Document title

<!-- page: 1 -->
<!-- source_ref: src_...:p001 -->

## Section title

<!-- chunk_id: src_...:p001:s001 -->
<!-- evidence_status: retrieved_knowledge -->
<!-- memory_status: not_memory -->
```

## Chunking policy

Do not chunk only by fixed character length.

Chunk by professional structure when possible:

```text
article
clause
section
subsection
table
figure_caption
annex
page range
heading hierarchy
```

Chunking expectations:

- keep a legal article whole when possible;
- keep a contract clause whole when possible;
- keep a technical table intact when possible;
- keep section path and parent headings;
- avoid mixing annexes with the main body;
- avoid losing page references;
- avoid splitting a citation from the statement it supports.

Each chunk should carry:

```text
chunk_id
source_id
source_hash
page_start
page_end
section_path
content_type
parent_heading
previous_chunk_id
next_chunk_id
conversion_tool
quality_flags
freshness_status
evidence_status = retrieved_knowledge
memory_status = not_memory
```

## Chunk record format

Recommended JSONL record:

```json
{
  "chunk_id": "src_abc123:p014:s003",
  "source_id": "src_abc123",
  "source_hash": "sha256:...",
  "document_title": "Contrat de mission",
  "page_start": 14,
  "page_end": 15,
  "section_path": ["Mission", "Honoraires", "Révision"],
  "content_type": "clause",
  "text": "Les honoraires pourront être révisés...",
  "markdown": "### Révision des honoraires\n\nLes honoraires pourront être révisés...",
  "quality_flags": [],
  "freshness_status": "metadata_insufficient",
  "evidence_status": "retrieved_knowledge",
  "memory_status": "not_memory"
}
```

## Table handling

Tables must not be flattened blindly into prose.

Recommended outputs:

```text
tables/table_<n>.md
tables/table_<n>.csv
tables/table_<n>.json
linked excerpt in document.md
source page reference
```

A table record should preserve:

```text
caption
columns
row labels
page number
continued_table flag
confidence score
```

If a table spans pages, mark:

```text
table_continues_from_previous_page
table_continues_to_next_page
manual_review_recommended
```

## Image and figure handling

Images and figures should not disappear.

Minimum behavior:

```text
extract image asset
insert Markdown placeholder
record page reference
record source reference
mark description_status = not_described
```

Optional advanced behavior:

```text
image_description_candidate
chart_to_table_candidate
figure_relevance_candidate
```

Generated descriptions remain candidates.

They are not evidence unless selected and reviewed.

## Header and footer cleanup

Repeated headers, footers, page numbers and watermarks may be removed from chunk text where safe.

Cleanup must be logged.

Possible flags:

```text
removed_repeated_header
removed_footer
removed_watermark
removed_page_number
ambiguous_cleanup_skipped
```

Ambiguous text must not be removed silently.

## Manifest

Each source should have a manifest.

```json
{
  "source_id": "src_...",
  "original_file": "document.pdf",
  "file_hash": "sha256:...",
  "conversion_tool": "docling",
  "conversion_version": "...",
  "conversion_date": "...",
  "page_count": 42,
  "language": "fr",
  "source_type": "uploaded_pdf",
  "quality_status": "review_recommended",
  "freshness_status": "metadata_insufficient",
  "markdown_file": "document.md",
  "chunks_file": "chunks.jsonl",
  "assets_dir": "assets/",
  "tables_dir": "tables/"
}
```

The manifest is the bridge to:

- OpenWebUI Knowledge packaging;
- Context Pack generation;
- optional Postgres registry;
- audit and review;
- future Evidence Candidate linking.

## Quality doctor

Every conversion should produce a quality report.

Suggested scores:

```text
text_coverage_score
ocr_confidence_score
layout_confidence_score
table_integrity_score
heading_detection_score
page_anchor_score
chunkability_score
provenance_score
```

Suggested statuses:

```text
ready_for_rag
review_recommended
manual_review_required
conversion_failed
ocr_required
source_quality_low
```

Recommended report sections:

```text
conversion summary
PDF profile
tool used
OCR status
page coverage
tables detected
images detected
pages with low confidence
removed headers/footers
chunk count
quality flags
limits
recommended next action
```

## Performance strategy

Do not process all PDFs with the heaviest pipeline.

Use tiers:

```text
fast path      → PyMuPDF4LLM, no OCR, simple layout
standard path  → Docling, layout/table support
heavy path     → Marker, OCR/table correction if needed
manual path    → conversion blocked until human review
```

Recommended cache key:

```text
file_hash
converter_name
converter_version
conversion_config_hash
```

If the file and configuration are unchanged, reuse outputs.

## Batch processing

For folders:

```text
process changed files only
parallelize by file
limit OCR concurrency
separate failed conversions
write per-file quality reports
write global batch report
```

Global batch report should include:

```text
converted_count
failed_count
review_required_count
ocr_used_count
tables_extracted_count
images_extracted_count
average_quality_score
```

## RAG retrieval optimization

The ingestion output should support later hybrid retrieval:

```text
semantic vector search
+ full-text search
+ metadata filtering
+ section/path boosting
+ freshness filtering
+ source type filtering
+ quality filtering
```

Useful retrieval metadata:

```text
content_type
section_path
page_start
page_end
source_type
freshness_status
quality_status
sensitivity
project_id
dossier_id
```

Do not rely only on embeddings.

## Candidate skills

These are candidate external execution capabilities.

They are not implemented here.

### MVP candidates

```text
pdf-profile-detector
pdf-to-md-docling
rag-quality-doctor
```

### Near-term candidates

```text
converter-router
rag-markdown-normalizer
rag-semantic-chunker
rag-manifest-builder
```

### Advanced optional candidates

```text
table-integrity-checker
figure-extraction-describer
header-footer-cleaner
source-freshness-classifier
openwebui-knowledge-packager
postgres-registry-writer
evidence-source-linker
```

## Skill boundary

A skill may execute conversion, extraction, chunking or reporting.

A skill must not approve evidence.

A skill must not promote memory.

A skill must not import into OpenWebUI silently.

A skill must not expand task scope.

A skill must not become a hidden ingestion runtime.

Recommended rule:

```text
The skill does not make the PDF true.
The skill turns the PDF into a structured, traceable, verifiable source for RAG.
```

## OpenWebUI role

OpenWebUI may expose:

- upload;
- user selection;
- Knowledge Base organization;
- ingestion action request;
- result display;
- quality report display;
- Knowledge packaging status;
- approval or review action.

OpenWebUI must not become:

- a Registre Probatoire entry;
- evidence authority;
- approval authority;
- ingestion runtime owner;
- hidden source of truth.

## Hermes role

Hermes may execute:

- profile detection;
- conversion;
- normalization;
- chunking;
- quality review;
- packaging candidate;
- Evidence Candidate linking when authorized.

Hermes must return candidates and reports.

Hermes must not canonize the source, approve evidence or promote memory.

## Pantheon role

Pantheon governs:

- Task Contract;
- allowed source scope;
- ingestion status;
- evidence status;
- memory status;
- approval requirements;
- quality thresholds;
- external tool policy;
- audit expectations.

Pantheon does not parse PDFs itself.

Pantheon does not run the ingestion pipeline.

## Status vocabulary

Recommended ingestion statuses:

```text
received
profiled
converted
normalized
chunked
quality_checked
ready_for_rag
review_required
packaged_for_openwebui
indexed
retrieved
selected_as_evidence_candidate
```

Recommended evidence and memory defaults:

```text
evidence_status = retrieved_knowledge
memory_status = not_memory
```

## MVP path

Keep the first implementation simple.

```text
User selects PDF or folder
→ Task Contract records allowed scope
→ Hermes runs pdf-profile-detector
→ Hermes runs pdf-to-md-docling
→ Hermes runs rag-quality-doctor
→ outputs are reviewed
→ OpenWebUI receives processed Knowledge only after review
```

No automatic Evidence Pack approval.

No automatic memory promotion.

No silent OpenWebUI import.

## Optional advanced path

Later, if volume and audit needs justify it:

```text
shared Postgres registry
→ source_id / chunk_id / manifest storage
→ scoped read-only retrieval functions
→ OpenWebUI Knowledge references
→ evidence candidate links
→ audit lineage
```

This remains optional.

It must not block the MVP.

## Anti-drift guardrails

Do not introduce:

- Pantheon PDF parsing runtime;
- hidden ingestion scheduler;
- queue;
- provider router;
- automatic OpenWebUI import pipeline without review;
- automatic evidence approval;
- automatic memory promotion;
- free skill installer;
- plugin marketplace;
- direct Hermes write access to a Registre Probatoire entry;
- direct Hermes global access to all OpenWebUI Knowledge.

## Product-facing explanation

For professional users:

```text
Le PDF est transformé en source lisible par l’IA.
Chaque extrait garde sa page, son origine et son statut.
Les tableaux et images ne sont pas perdus.
La qualité de conversion est signalée.
La source devient consultable, pas automatiquement validée.
```

## Final rule

```text
A good RAG pipeline starts before embeddings.
The PDF must become structured, traceable Markdown.
The chunks must preserve professional meaning.
The quality report must expose uncertainty.
Pantheon governs status.
Hermes executes conversion.
OpenWebUI exposes searchable Knowledge.
```
