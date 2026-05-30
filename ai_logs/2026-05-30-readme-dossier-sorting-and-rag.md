# AI Log — README: dossier sorting and plain-language RAG

Date: 2026-05-30

## Scope

Added two reader-facing ideas to both READMEs, after the "How a dossier flows"
section:

1. the system sorts the handed-over dossier (keep / flag / send / ask) according
   to the user's request;
2. a plain-language explanation of RAG for readers who have never heard the term.

## Changes made

Updated:

- `README.md`;
- `README.fr.md`.

Added:

- `ai_logs/2026-05-30-readme-dossier-sorting-and-rag.md`.

## Editorial intent

Following `docs/governance/EDITORIAL_LANGUAGE.md`:

- **"You hand over the dossier, the system sorts it"** — the practitioner does not
  pre-cut their file. They hand over material; the system reads, classifies and
  acts per request, with four verbs: keep, flag, send, ask. The "ask" verb maps
  to the User Decision Gate (consult the human rather than decide alone). Example
  kept architecture-only (surface note vs commitment letter).
- **"RAG, in plain terms"** — defined without jargon: retrieve the relevant
  passages from the user's own documents first, send only those. Binder/two-pages
  analogy. Two benefits framed as less exposure + source-traceable answers.

## Honesty boundary

RAG runtime, retrieval, chunking and document filtering are **not implemented**
(see `docs/governance/RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` and `STATUS.md`).
The sections are written as method and end with an explicit `STATUS.md` pointer.

The doctrine boundary "retrieval is not proof" is preserved verbatim in spirit:
"Finding the right passage is not proving it. A retrieved excerpt stays a
candidate." No "automatic proof", "safe AI" or "compliant by design" promise was
introduced.

## Explicit non-implementation

No runtime added. No files touched under `schemas/`, `tests/`, `hermes/`,
`operations/`, `pyproject.toml`, or `CLAUDE.md`.

## Boundary phrase

```text
The system retrieves and sorts; it does not prove or decide.
Retrieved excerpt = candidate. The human validates.
```
