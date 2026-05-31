# AI Log — PaddleOCR Hermes Skill Placement

Date: 2026-05-31

## Change

Added `docs/governance/PADDLEOCR_HERMES_SKILL_NOTE.md`.

The note records PaddleOCR as a candidate document-extraction adapter to be implemented, if adopted, as a Hermes skill rather than as a Pantheon component.

## Why

The discussion identified PaddleOCR as useful for OCR, document parsing, layout extraction, table extraction and RAG preparation.

The governance placement needed to stay modular:

```text
Pantheon defines the extraction contract.
Hermes executes the document-extraction skill.
PaddleOCR may be one adapter implementation.
OpenWebUI exposes upload, status and review.
```

## Doctrine preserved

The change preserves the existing doctrine:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

It also preserves the adapter boundary from `ADAPTERS_AND_BINDINGS.md`:

```text
The blueprint lives in Pantheon.
The adapter lives in the tool.
The dependency always points to Pantheon.
```

## What was not implemented

This is documentation only.

No PaddleOCR dependency was added.

No Hermes skill was installed.

No OpenWebUI plugin, Action, Tool, Function, Pipe or Pipeline was created.

No ingestion runtime, scheduler, queue, provider router, automatic Knowledge import, automatic evidence approval or automatic memory promotion was introduced.

## Risks and limitations

The new document is a candidate adapter note. It must not be treated as a canonical executable specification.

The canonical module manifest shape still lives in `MODULAR_DOMAIN_REORIENTATION.md` until an approved schema exists.

The actual runnable Hermes adapter, if built later, must live outside Pantheon or in the appropriate Hermes-side repository/configuration, and must conform to the Pantheon envelope:

```text
Task Contract in -> module -> { Result Candidate, Evidence Pack Candidate } out
```

PaddleOCR must remain replaceable by other adapters such as Docling, Marker, Mistral OCR, Azure Document Intelligence or Tesseract.

## Status

Documented, not implemented.
