# AI Log — Placement, templates and audit consolidation

Date: 2026-05-31

## Scope

Documentary consolidation after the placement / prompt / bridge / execution minimalism work.

This intervention stayed within allowed documentation and template surfaces:

- `docs/governance/*`
- `templates/*`
- `ai_logs/*`

No protected runtime area was modified.

## Changes made

- Added or reconciled governance doctrine around capability placement, prompt placement, bridge boundaries and execution minimalism.
- Added non-executable template surfaces for OpenWebUI, Hermes, Langflow, Langfuse and provenance.
- Added `templates/TEMPLATE_REGISTRY.md` to make the template list explicit.
- Corrected `templates/README.md` so the provenance template folder matches the actual path.
- Reconciled `docs/governance/STATUS.md` with the new doctrine and template baseline.

## Important boundary

All new template material is declarative only.

It does not implement OpenWebUI Functions, Tools, Pipes, Filters, Actions or Pipelines. It does not install Hermes profiles, skills or toolsets. It does not deploy Langflow, LangGraph, Langfuse, GraphRAG, provenance storage, a bridge, scheduler, queue, provider router, platform code, operations tooling, schemas, tests, Docker changes, automatic approval or automatic memory promotion.

## Issue encountered

A direct full-file update of `CHANGELOG.md` was blocked by the tool safety layer because it required resending the whole changelog history. The changelog should still receive a future entry for this consolidation through a local patch or a safer targeted update path.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes executes.
Pantheon governs.
Templates describe candidates.
They do not execute, approve, prove or remember.
```

## Follow-up

- Verify final diff against `main`.
- Consider a safe `CHANGELOG.md` update for this consolidation.
- Avoid moving from templates to runtime until the bridge and capability placement rules are explicitly accepted.
