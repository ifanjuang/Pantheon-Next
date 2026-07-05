# 2026-07-05 — Loop governance model distillation

Status: documented non-implemented.

Authority class: candidate support doctrine.

Branch: `docs/loop-governance-model`.

## Context

The external Loop Engineering reference was distilled into a Pantheon-compatible governance model for bounded runtime loops.

The distillation keeps the useful mechanism:

```text
act -> observe -> check -> retry or stop
```

but refuses to import runtime authority into Pantheon.

## Sources reviewed

Repository documents read before writing:

```text
docs/governance/STATUS.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/CARD_STACK_MODEL.md
docs/governance/WORKFLOW_FORGING_PROTOCOL.md
docs/governance/README.md
docs/governance/MODULES.md
```

Related repository coordination reviewed:

```text
Issue #273 — first external OpenWebUI -> Hermes live run.
Issue #192 — Intent Candidate log in Pantheon Control.
Issue #220 — read-only RAG backend benchmark protocol.
Issue #118 — Hermes-first external modules shortlist.
PR #278 — Revit plugin skeleton and adapter-side blocker / retry-loop discussion.
```

## Files changed

```text
docs/governance/LOOP_GOVERNANCE_MODEL.md
docs/governance/README.md
ai_logs/2026-07-05-loop-governance-model.md
```

## Decision classification

Accepted:

```text
- Distill bounded loops as a governable runtime-execution pattern.
- Keep Loop Contract, event stream, blocker taxonomy, stop rules and checker gate as documentary candidate shapes.
- Map loop state to existing Run, Task, Evidence, Trace, Decision / Gate and Record card families.
- Keep tool-specific mechanics in adapters.
```

Refused:

```text
- Pantheon loop engine.
- Hidden retry queue.
- Scheduler or runtime state inside Pantheon.
- Runtime self-approval.
- Loop-based memory promotion.
- External action inside retry loop without explicit gate.
- Canonical effect as runtime work.
```

To verify:

```text
- Alignment with the external OpenWebUI -> Hermes live-run checklist in issue #273.
- Alignment with the Revit adapter prototype once PR #278 is resolved.
- Whether LOOP_GOVERNANCE_MODEL.md should receive an AUTHORITY_INDEX row before merge or be covered by a later authority-index pass.
```

To arbitrate:

```text
- Whether the candidate remains standalone support doctrine or later folds into WORKFLOW_FORGING_PROTOCOL.md / CAPABILITY_PLACEMENT.md.
```

## Repo state

```text
Documented non-implemented.
No runtime.
No schema.
No test.
No protected path.
No approval engine.
No memory engine.
No external action.
```

## Boundary phrase

```text
Pantheon ne boucle pas.
Pantheon borne les boucles.
Le runtime boucle.
Zeus qualifie.
L'humain décide.
```

The validated remains.
