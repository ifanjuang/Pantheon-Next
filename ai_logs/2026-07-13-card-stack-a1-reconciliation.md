# Card Stack A1 reconciliation

Date: 2026-07-13
Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Changes

- removed the retired `CARD_STACK_HARDENING_NOTE.md` row from the registered governance authority sub-index;
- replaced the obsolete exhaustive Workflow Scene wording in `docs/governance/README.md`;
- clarified Card as a cockpit projection of an identifiable governed entity or record;
- clarified Work Scene as bounded and complete enough for governed review, not an exhaustive graph;
- kept Gate and Decision distinct in the navigation text;
- removed the implication that external AI systems share promotion authority.

## Boundary

Documentation reconciliation only. No UI, renderer, state machine, schema, runtime, scheduler, queue, approval engine, memory engine, OpenWebUI plugin, Hermes skill or external action.

```text
Scene != exhaustive graph
Gate != Decision
card projection != object ownership
UI intent != Hermes execution
merged != promoted
```
