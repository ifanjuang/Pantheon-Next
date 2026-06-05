# Pantheon Control — Document and Media Stack Selection

Status: candidate — to verify.

This document captures candidate dashboard functions for Markdown viewing, document processing, OCR, audio transcription, media extraction and skill/module vectorization.

This is documentation only. It does not install anything on a NAS, ship Docker files, create an executable stack, add a runtime, add a queue or authorize automated processing of user data.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Control should support document and media processing as first-class stack families.

The goal is not to install every available repository. The goal is to select one preferred tool per functional slot, expose conflicts, and mark alternatives as fallback, sandbox or rejected.

```text
One slot.
One preferred tool.
Explicit fallbacks.
No tool pile-up.
```

## NAS installation rule

The NAS should host stable, durable, low-volatility services.

Good NAS candidates:

```text
PostgreSQL / pgvector
Qdrant when selected
SearXNG
Pantheon Control
OpenWebUI if chosen for the NAS
Git mirror
backup / restore artifacts
Markdown documentation viewer
Document processing workers if CPU load is acceptable
```

Poor NAS candidates by default:

```text
GPU-heavy vision workers
large ComfyUI model folders unless storage-only
unbounded media conversion workers
experimental OCR/VLM models
unstable repo experiments
automatic provider routers
```

A GPU workstation or dedicated worker should handle GPU-heavy image, video and transcription workloads when needed.

## Markdown viewer

Pantheon Control should include a Markdown viewer for governance docs, AI logs, generated manifests, diffs and preflight reports.

Required features:

```text
safe Markdown rendering
GitHub Flavored Markdown support
frontmatter display
code block rendering
link validation
anchor navigation
mermaid or diagram support only if sandboxed
side-by-side source / preview
rendered diff for Markdown changes
```

Preferred stack:

```text
Primary dashboard renderer: internal Markdown renderer using markdown-it or equivalent
Static documentation view: MkDocs / Material for MkDocs as optional generated site
Conversion/export: Pandoc as optional expert tool
```

The Markdown viewer must not treat rendered text as canonical truth. It only displays repository content and generated reports.

## Document processing slots

### PDF and document parsing

Preferred primary:

```text
Docling
```

Role:

```text
PDF / DOCX / document conversion into structured Markdown, JSON or intermediate representations.
```

Reason:

```text
Good fit for AI-ready document conversion, layout-aware extraction, tables and structured document pipelines.
```

Fallbacks:

```text
Unstructured: fallback / compatibility
PyMuPDF: low-level PDF extraction fallback
pdfplumber: table/text fallback for simple PDFs
Apache Tika: broad file-type fallback, not primary
```

### OCR for scanned PDFs

Preferred primary:

```text
OCRmyPDF + Tesseract language packs
```

Role:

```text
Add searchable OCR text layers to scanned PDFs.
```

Fallbacks:

```text
PaddleOCR: candidate for image OCR and multilingual cases
EasyOCR: lightweight fallback
```

### Office and format conversion

Preferred primary:

```text
LibreOffice headless
```

Role:

```text
Convert DOCX, ODT, XLSX, PPTX and other office formats to PDF or intermediate files.
```

Optional expert:

```text
Pandoc for Markdown / DOCX / HTML / PDF publishing workflows.
```

### Audio transcription

Preferred primary:

```text
faster-whisper
```

Role:

```text
Local transcription of meeting audio, voice notes and chantier recordings.
```

Fallbacks:

```text
whisper.cpp: CPU / edge fallback
OpenAI Whisper API or other external APIs: external provider, gated by privacy policy
```

### Speaker diarization

Preferred candidate:

```text
pyannote.audio
```

Role:

```text
Speaker separation for meetings or multi-speaker recordings.
```

Status:

```text
candidate / to verify, because model access, tokens and privacy constraints must be reviewed.
```

### Video and audio extraction

Preferred primary:

```text
FFmpeg
```

Role:

```text
Extract audio, frames, metadata, thumbnails and normalized media formats before analysis.
```

## Skill and module vectorization

Pantheon Control may index module declarations, skills, templates, docs and examples for retrieval.

This should produce retrieval candidates only.

```text
Vectorization != capability authorization.
Similarity != suitability.
Retrieved skill != approved skill.
```

Preferred base:

```text
PostgreSQL + pgvector for small / controlled indexes
Qdrant for larger module, document or skill retrieval
```

The dashboard should show:

```text
indexed collections
embedding model used
embedding dimension
index freshness
source commit
scope
candidate-only status
reindex requirement
```

Changing the embedding model must mark affected indexes as stale.

## Repository selection policy

The dashboard should maintain a curated repository allowlist, not a broad installer marketplace.

Each repo entry should declare:

```text
slot
repo URL
status: preferred | fallback | candidate | rejected
license
maintenance state
last reviewed
install target: NAS | worker | desktop | external
resource profile
risk
preflight commands
update policy
backup policy
```

Selection modes:

```text
required_single
optional_single
primary_plus_fallback
multiple_with_roles
rejected
```

Example preferred slots:

```text
Markdown viewer: internal renderer, optional MkDocs generated site
Document parsing: Docling
Scanned PDF OCR: OCRmyPDF
Office conversion: LibreOffice headless
Publication conversion: Pandoc optional
Audio transcription: faster-whisper
Diarization: pyannote candidate
Media extraction: FFmpeg
Vector store base: pgvector
Vector store advanced: Qdrant
```

## Dashboard functions

The dashboard should add these views:

```text
Document & Media modules
Markdown viewer
Parsed document preview
OCR quality report
Audio transcription report
Diarization report
Media extraction report
Skill / module vector index
Repository allowlist
Repository review status
```

## Preflight checks

Minimum preflights:

```text
Markdown renderer can safely render GFM test document
Markdown renderer blocks unsafe HTML/script
Docling can parse a synthetic PDF
OCRmyPDF can OCR a scanned test PDF
Tesseract has required language packs
LibreOffice can convert DOCX to PDF
faster-whisper can transcribe a short audio sample
FFmpeg can extract audio and frames
Vector index can insert/search/delete a sandbox skill record
Embedding model matches index metadata
Rejected repos cannot be installed from dashboard
```

## Governance boundary

Document and media modules produce candidates.

They do not produce:

```text
validated truth
canonical memory
approved evidence
authorized external action
final professional judgment
```

## Open questions

```text
Should the repository allowlist live in Pantheon Next or in a separate operational config repo?
Should Markdown rendering be built into Pantheon Control or served by a generated MkDocs site?
Should Docling be the only primary document parser at first?
Should OCR workers run on NAS or separate machines?
Should audio transcription be local-only by default?
Should pyannote be included now or deferred until privacy and token handling are reviewed?
```

## Final rule

```text
Install the best stable tool per slot.
Expose alternatives, conflicts and fallbacks.
Do not turn the NAS into an uncontrolled experiment shelf.
```