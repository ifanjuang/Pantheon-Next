# PaddleOCR Dashboard Install Candidate

Status: candidate support note — dashboard install affordance and Hermes-managed OCR boundary.

Observed date: 2026-06-14

Reviewed sources:

- `https://github.com/PaddlePaddle/PaddleOCR`, README blob observed at `6458242fc136e2fc514fee9c8e4896d09bb8fab5`;
- `https://github.com/PaddlePaddle/PaddleOCR`, MCP server documentation blob observed at `b5d906ff9fbbfcf50781c06417fedf085d8c6b84`.

This document records a narrow placement decision.

It does not install PaddleOCR.

It does not create a dashboard, Hermes skill, MCP host, connector, OCR pipeline, queue, scheduler, approval engine, evidence validator or memory promoter.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Decision

PaddleOCR is accepted as a dashboard-installable external module candidate for document parsing and OCR.

Decision Zeus:

```text
Accepté as Hermes-managed install candidate.
À vérifier before production or dossier activation.
```

Repo state:

```text
Documented non implemented.
```

The dashboard may show PaddleOCR as an installable module, but the installed runtime remains outside Pantheon. Hermes, or a Hermes-adjacent module manager, handles installation, configuration, health checks, logs, version inspection, execution and uninstall.

Pantheon only governs whether the capability may be activated for a scope and which outputs may be trusted, reviewed, rejected or promoted through a separate governed path.

## Placement

| Concern | Placement | Rule |
|---|---|---|
| Install button, configuration form, status display, logs display | dashboard / administration cockpit | exposure only |
| Package installation, runtime configuration, MCP process, local inference, service call, smoke test | Hermes / execution runtime | execution only |
| Allowed inputs, forbidden outputs, evidence expectation, scope, approval, memory boundary | Pantheon | governance only |
| Professional reliance on extracted text | human decision after review | never automatic |

## Dashboard card

Recommended actions:

```text
Install
Configure
Check health
Show logs
Run smoke test
Open module UI if provided by the runtime
Disable
Uninstall
```

Forbidden dashboard actions:

```text
Validate extracted source
Approve OCR result as truth
Promote extraction into a Registre Probatoire entry
Transmit an OCR-derived conclusion externally
Write canonical project data from OCR without review
```

## Hermes responsibility

Hermes may install, configure, test and run PaddleOCR under Task Contract.

Hermes returns candidates only:

```text
Extraction Candidate
Fragment Candidate
Evidence Pack Candidate
Capability Gap
Health Observation Candidate
```

Hermes must not approve the tool for production, promote OCR text to validated source content, write project identity data as canonical, create or modify a Registre Probatoire entry, or send OCR-derived material externally without a User Decision Gate.

## Candidate envelope

Correct shape:

```text
Task Contract in
-> PaddleOCR module executed by Hermes
-> Extraction Candidate + Evidence Pack Candidate out
```

Minimum returned fields:

```text
source_ref
source_hash
page_or_region
extraction_method
model_or_mode
runtime_version
extracted_text_or_structure
confidence_or_limits
status: candidate | partial | failed | blocked
```

## Benchmark admission

The first benchmark is an admission test for the dashboard card and Hermes-managed execution path, not a production benchmark.

Recommended corpus:

```text
clean text PDF
low-quality scanned PDF
CERFA or form-like PDF
arrêté mairie or administrative decision
quote / estimate with tables
site report with reserves
image containing handwriting or annotations
layout-heavy architectural notice
```

Expected result for each item:

```text
Extraction Candidate produced or Capability Gap signaled.
Source reference preserved.
Page or region reference preserved.
Method and version recorded.
Low-confidence or unsupported areas surfaced.
No professional conclusion marked as final.
No memory promotion.
No external action.
```

Promotion from sandbox to dossier scope requires a separate User Decision Gate.

## Architecture-domain use cases

PaddleOCR is useful for architecture dossiers when it remains candidate-only:

```text
CERFA field extraction candidate
arrêté mairie text extraction candidate
quote / estimate table extraction candidate
site report and reserve follow-up extraction candidate
scanned PLU excerpt extraction candidate
attestation and diagnostic OCR candidate
handwritten note transcription candidate
```

These outputs may support review. They do not become proof, source validity, compliance verdict or professional advice by themselves.

## Relation to Docling and other parsers

PaddleOCR does not replace other document parsers by doctrine.

Dashboard placement should allow several document parsing modules to coexist behind the same capability family:

```text
document_parse_ocr:
  - PaddleOCR
  - Docling
  - MarkItDown
  - other parser candidates
```

The dashboard should expose capability status, not force the professional to choose a library name at the first level.

User-facing action:

```text
Analyze project documents
```

System-facing candidate modules:

```text
PaddleOCR, Docling, MarkItDown, source-audit, evidence-pack-builder
```

Policy first, model second. The capability router may rank eligible modules, but it must not bypass Pantheon gates.

## Boundary phrase

```text
PaddleOCR may be installable from the dashboard.
Hermes manages the tool.
Pantheon governs what its output is allowed to mean.
```
