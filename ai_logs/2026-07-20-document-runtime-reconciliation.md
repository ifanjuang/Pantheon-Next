# Document architecture and runtime reconciliation

Date: 2026-07-20

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Updated the architecture-agency Document and Knowledge organization to use the exact NAS hierarchy enforced by the external adapter.
- Recorded OpenWebUI as the current cockpit candidate and Tiptap as a future editor, not the first implemented surface.
- Recorded `ifanjuang/pantheon-mvp@f1a6689c` and the successful Work Issue, Docling, NAS intake and Document Card CI progression.
- Reconciled `WHAT_RUNS.md`, the external binding review and the runtime-adapter authority index.
- Kept Knowledge publication, Knowledge Cards, offline mobile synchronization, adoption and production deployment explicitly non-implemented.

## Why

The executable document progression landed after the first architecture draft. Without reconciliation, the draft used folder names that the strict NAS parser would reject and repository status stopped at the earlier Work Issue commit.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none; external code is observed, not installed or activated.
Authority impact: candidate architecture and support-status reconciliation only.
Schema/test/CI impact: no schema, test or CI file changed; existing immutable workflow results are cited.
External action: GitHub documentation update only.
Memory behavior: none.

## Local distinctions

```text
external implementation observed != binding adopted
plugin committed != plugin installed
Document Card implemented != Knowledge publication implemented
CI success != professional validation
```
