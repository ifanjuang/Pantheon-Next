# AI Log — Document OCR Derivation Pipeline

Date: 2026-07-31

Status: documentation-only candidate support doctrine.

## Context

A two-year operational review of approximately 3,000 documents and 8,000 pages highlighted that OCR quality, derivation integrity and pipeline separation can dominate downstream classification quality. The review also exposed the risk of a source-management runtime reprocessing an already superior OCR layer and silently degrading results.

## Decision

Add `docs/governance/DOCUMENT_OCR_DERIVATION_PIPELINE.md` to:

- separate `document_ocr` from document source management, structural analysis, classification and validation;
- preserve exact source-version superiority over every derivative;
- define minimum provenance for OCR-derived representations;
- make silent extraction mismatch a reviewable validation concern;
- keep remote OCR bindings gated and optional;
- keep batching, GPU utilization, queues and provider execution in Hermes or external runtimes;
- require classification outputs to remain candidates and consequential writes to use ChangeCandidate semantics;
- prevent Paperless-ngx from becoming OCR authority or silently degrading preprocessed documents.

## Boundary

This change adds no runtime, dependency, provider integration, OCR engine, scheduler, queue, model router, Paperless configuration, Hermes skill, Cockpit schema, API, migration, test or automatic approval behavior.

```text
documented != implemented
binding_catalogued != binding_selected
binding_selected != dependency_adopted
runtime_success != Evidence
no_warning != verified_correct
UI status != authorization
```

## Repository placement

- doctrine: `docs/governance/DOCUMENT_OCR_DERIVATION_PIPELINE.md`
- authority placement: `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`

`pantheon-mvp` already contains a bounded Docling structured-extraction
compiler with revisioned compilations, ordered units, diagnostics and
compilation-scoped retrieval chunks. This doctrine does not replace or promote
that candidate implementation. It records the remaining gate for a broader OCR
derivation contract: source-version semantics, derivative statuses, remote
transmission, visual mismatch verification and ChangeCandidate mapping.
