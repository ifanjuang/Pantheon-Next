# Cockpit consolidation roadmap launch

Date: 2026-07-13
Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

Added `docs/roadmaps/COCKPIT_CONSOLIDATION_ROADMAP.md` to sequence the remaining documentary reconciliation, cockpit visual-language work, deterministic current-state projections and the return to the external executable vertical.

## Why

Pantheon Next has accumulated enough owner documents and candidate projections that the principal risk is now inconsistency, premature promotion or duplicated implementation paths. The roadmap establishes explicit gates between cleanup, visual language, read-only resolvers and executable integration.

## Immediate sequence

```text
A1 Card Stack single-source reconciliation
A2 Source / ingestion / retrieval reconciliation
A3 transverse terminology audit
B cockpit visual language
C Current Decision Resolver and related projections
D return to pantheon-mvp vertical
```

## Boundary

No runtime, renderer, schema, validator, scheduler, queue, connector, installer, approval engine, memory engine, OpenWebUI plugin, Hermes skill or external action is introduced.

```text
roadmap != authority
roadmap != implementation
merged != promoted
CI green != safe
```
