# AI Log — Context Stack candidate

Date: 2026-06-25

## Change

Created `docs/governance/CONTEXT_STACK.md` as candidate support doctrine.

The document formalizes:

- dynamic Context Stack composition;
- specialized Context Card families;
- context item statuses;
- context sufficiency states;
- Context Stack Change Candidate;
- HESTIA as a candidate context-watch role;
- UX projection rules for cockpit/card display;
- architecture examples for client-facing response, visa EXE and PLU questions.

## Why

The user identified that context cards should not be fixed. Their list must change depending on the question, subject, workflow stage, risk level and expected output.

The new document separates:

```text
Context Stack  -> visible, dynamic, card-based context composition.
Context Pack   -> bounded context bundle prepared for a target tool or surface.
Evidence Pack  -> reviewable proof package after execution.
```

## Boundary

Documentation only.

No runtime, UI, scheduler, queue, context engine, retrieval engine, approval engine, memory engine, Hermes skill, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Action or external connector was implemented.

HESTIA is marked candidate and is not promoted to the canonical role registry.

## Risks / limitations

- `CONTEXT_STACK.md` remains candidate support doctrine until reviewed.
- Authority index and module navigation may need follow-up indexing if repository checks require explicit listing.
- HESTIA may need reconciliation with ATHENA, ARGOS, THEMIS and ZEUS before any promotion.
- Context Stack Change Candidate may later require a schema, but no schema path was modified.

## Repo state

Documented non-implemented.
