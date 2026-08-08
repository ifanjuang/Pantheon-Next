# Landing and README system diagrams

Date: 2026-08-08

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added portable French and English SVGs for the system boundary and information authority chain.
- Replaced the landing's linear four-role diagram with direct and assisted paths around one authoritative server.
- Replaced the nine-station request flow with a six-phase conceptual authority chain.
- Embedded the compact system map in `README.md` and `README.fr.md`.

## Why

The earlier landing diagrams were readable but implied that Hermes was a mandatory route, assigned recording to Pantheon Next, and did not show the separate `pantheon-mvp` implementation/server responsibility. The new views separate semantic governance, optional external assistance, consequential human decision, authoritative persistence and computed projections.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: none; the diagrams project existing ownership boundaries.
Schema/test/CI impact: none.
External action: none.
Memory behavior: none.

## Local distinctions

```text
direct path != Hermes path
runtime_success != Evidence
projected != persisted
static diagram != live capability
```
