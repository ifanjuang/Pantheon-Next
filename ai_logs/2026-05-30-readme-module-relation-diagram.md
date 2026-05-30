# AI Log — README: module relation diagram

Date: 2026-05-30

## Scope

Added a Mermaid diagram to both READMEs showing the modules, their usage and
their relations, inside the "Under the hood / Three parts" section.

## Changes made

Updated:

- `README.md`;
- `README.fr.md`.

Added:

- `ai_logs/2026-05-30-readme-module-relation-diagram.md`.

## What the diagram shows

Three layers matching the doctrine (OpenWebUI exposes / Hermes executes /
Pantheon governs), plus the interchangeable AI engines as an external node:

- you hand over the dossier + request through OpenWebUI;
- Pantheon: Task Contract bounds the work → Context Pack (minimum necessary)
  fed by RAG retrieval of useful passages from your sources → strict minimum to
  Hermes → output candidate → Evidence Pack → Approval → scoped Memory
  (reusable, bounded) ; a Decision Gate sends the question back to the human when
  risk exceeds safe arbitration;
- Hermes profiles execute by making a bounded call to an AI engine and return
  candidates;
- statuses and sources flow back to OpenWebUI; the reviewable result returns to
  the practitioner.

Node names and "must not become" boundaries are taken from
`docs/governance/CORE_CONCEPTS_MAP.md` (Core object map) and the one-line
doctrine. The section ends with a pointer to that map.

## Validation

The diagram was validated with the Mermaid render tool: `valid: true`,
diagramType `flowchart`. GitHub renders ```mermaid fences natively.

## Honesty boundary

The diagram is a method/relationship map, not an implemented runtime. The
caption keeps the doctrine boundaries verbatim in spirit: output stays a
candidate until validated; a retrieved excerpt is not proof; nothing enters
memory without approval. No runtime, RAG engine or router is implemented (see
`STATUS.md`).

## Explicit non-implementation

No files touched under `schemas/`, `tests/`, `hermes/`, `operations/`,
`pyproject.toml`, or `CLAUDE.md`. No runtime behavior added.
