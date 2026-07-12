# Card Stack Hardening Note

Status: obsolete — superseded by `CARD_STACK_MODEL.md`.
Boundary profile: candidate_support_note.

Related issue: #293.

This former companion note has been superseded by the reconciled `docs/governance/CARD_STACK_MODEL.md` merged through PR #350.

It no longer defines active cockpit requirements and must not be used to override the current Card Stack model.

The following rules were absorbed into the current model:

- Card-versus-field visibility discipline;
- exceptional visibility of Role / God quality expressions;
- separation of Source, reusable knowledge, Evidence and Register;
- recto / detail / Constellation separation;
- answer-first presentation;
- bounded gestures and Gate preservation.

The former claim that the Workflow Scene must remain exhaustive is retired.

Current rule:

```text
A Work Scene must be complete enough for governed review.
It is not required to expose the complete graph or every mobilized reference.
```

Terminology and object ownership remain governed by:

- `TERMINOLOGY_BOUNDARIES.md`;
- `CORE_CONCEPTS_MAP.md`;
- `CARD_STACK_MODEL.md`;
- `PANTHEON_GRAPH_MODEL.md`;
- `DECISION_SURFACE_SPEC.md`.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```

This retirement adds no UI, schema, runtime, workflow engine, approval engine, memory engine, connector or external action.
