# AI Log — RAG ingestion pipeline doctrine

Date: 2026-05-17

## Scope

Created a governance document for PDF and document ingestion into RAG-ready sources.

The intervention formalizes how Pantheon Next should treat PDF-to-Markdown conversion, chunking, quality reporting, OpenWebUI Knowledge packaging and candidate Hermes skills without implementing an ingestion runtime.

## Files changed

- `docs/governance/RAG_INGESTION_PIPELINE.md`
- `docs/governance/README.md`
- `docs/governance/STATUS.md`
- `CHANGELOG.md`
- `ai_logs/2026-05-17-rag-ingestion-pipeline.md`

## Why

The user asked how to automate PDF decomposition into Markdown optimized for RAG, whether open-source tools exist, whether skills exist, and how to improve the pipeline.

Issue #12 collected the architecture discussion.

This intervention distills the PDF/RAG ingestion part into a dedicated governance document.

## Doctrine added

Core rule:

```text
The PDF becomes an exploitable source.
It does not become validated truth.
```

Pipeline distinction:

```text
Raw Source
→ Source Reference
→ Knowledge Item
→ Retrieved Knowledge
→ Evidence Candidate
→ Evidence Item
→ Evidence Pack
→ Output Candidate
→ Approval Event
→ Memory Candidate
→ Canonical Memory
```

Forbidden shortcuts:

```text
uploaded → validated
converted → approved
indexed → evidence
retrieved → truth
retrieved → memory
quality_passed → human approval
```

## Content added

`RAG_INGESTION_PIPELINE.md` defines:

- PDF profile detection;
- converter routing;
- candidate open-source tools;
- required outputs;
- Markdown frontmatter and anchors;
- chunking policy;
- chunk record format;
- table handling;
- image and figure handling;
- header/footer cleanup rules;
- manifest structure;
- quality doctor expectations;
- performance tiers;
- batch processing expectations;
- retrieval metadata;
- candidate skill decomposition;
- OpenWebUI, Hermes and Pantheon boundaries;
- MVP and optional advanced paths;
- anti-drift guardrails.

## Candidate tools

Recorded as external candidate capabilities, not dependencies:

- Docling;
- PyMuPDF4LLM;
- Marker;
- Unstructured;
- OpenWebUI Knowledge.

## Candidate skills

Recorded as candidates only:

- `pdf-profile-detector`;
- `pdf-to-md-docling`;
- `rag-quality-doctor`;
- `converter-router`;
- `rag-markdown-normalizer`;
- `rag-semantic-chunker`;
- `rag-manifest-builder`;
- `table-integrity-checker`;
- `figure-extraction-describer`;
- `header-footer-cleaner`;
- `source-freshness-classifier`;
- `openwebui-knowledge-packager`;
- `postgres-registry-writer`;
- `evidence-source-linker`.

## Boundary check

This intervention is documentation-only.

It does not implement:

- PDF parsing;
- OCR;
- Markdown conversion;
- chunking;
- indexing;
- OpenWebUI import;
- OpenWebUI plugin;
- Hermes tool;
- Postgres registry writer;
- Evidence Candidate writer;
- memory promotion;
- ingestion scheduler;
- queue;
- provider router;
- hidden runtime;
- dependency installation.

## Status

Implemented as active governance documentation.

Runtime implementation not started.
