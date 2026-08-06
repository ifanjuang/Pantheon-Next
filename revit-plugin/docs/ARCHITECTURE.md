# Revit Local Adapter Implementation Shape

Status: supporting implementation note — documented non-implemented — subordinate to `docs/governance/REVIT_LOCAL_ADAPTER.md`.

The canonical responsibility boundary is defined by `../../docs/governance/REVIT_LOCAL_ADAPTER.md`. This note records only the intended external implementation shape.

```text
Pantheon Next -> governance, schemas, status and human gates
pantheon-mvp  -> candidate APIs and Cockpit projections when implemented
Hermes        -> admitted external orchestration
Revit add-in  -> Revit API execution inside Revit context
Human         -> consequential decision
```

## First proof target

```text
read active document, view and explicit selection
materialize one bounded Context Pack candidate
perform no hidden global search
return a technical trace
refuse an entity outside the admitted scope
```

A later write slice must add fresh preflight, named transactions, changed-element journaling and rollback proof before it can be reviewed.

This file implements nothing.
