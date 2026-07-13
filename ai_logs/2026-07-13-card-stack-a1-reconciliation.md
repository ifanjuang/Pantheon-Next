# Card Stack A1 reconciliation

Date: 2026-07-13
Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

Reconciled the governance README and authority sub-index with the current `CARD_STACK_MODEL.md`.

## Corrections

- removed the retired `CARD_STACK_HARDENING_NOTE.md` row from the registered governance authority sub-index;
- replaced the obsolete exhaustive Workflow Scene wording with the bounded Work Scene rule;
- retained `CARD_STACK_MODEL.md` as candidate support doctrine, without promotion.

## Invariants

```text
Scene = bounded filtered ordered projection
Scene != exhaustive graph
retired file != active authority row
merged != promoted
```

No UI, renderer, schema, runtime, approval engine, memory engine, OpenWebUI plugin, Hermes skill or external action is introduced.
