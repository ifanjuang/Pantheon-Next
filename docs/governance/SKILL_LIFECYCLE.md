# Skill Lifecycle

Status: candidate support doctrine — to verify. Written fresh by distillation; replaces an earlier placeholder.
Boundary profile: candidate_support_note.

Runtime/client/authority placement is inherited from `HERMES_INTEGRATION.md`: optional compatible runtime clients expose interaction, Hermes Agent executes admitted external work, Pantheon Cockpit projects governed state, and Pantheon Next retains governance authority.

## Purpose

A skill moves through governed states from the moment it becomes visible to the moment it is retired. This document names those states and the gate between each pair. It composes what already exists — the manifest (`SKILL_MANIFEST.md`), the capability passport (`UNIFORM_CAPABILITY_GOVERNANCE.md`), the registry and admission guard (`CAPABILITY_REGISTRY.md`), the invocation preflight (`MODULE_INVOCATION_PREFLIGHT.md`) — into one lifecycle. It adds no new mechanism.

A workflow may compose several skills. Some may be admitted Hermes skills, some may be custom skills, and some may be improvised on the flow for one task. This lifecycle distinguishes those cases so useful improvisations can be distilled without becoming automatically approved.

## The lifecycle

```text
on-the-flow       an improvised task-local skill pattern exists during one workflow; no reusable status is implied
candidate         the pattern is worth recording after use; still not declared as a reusable skill
declared          a manifest exists; nothing more is implied
validated         the manifest and passport validate against the schemas
admitted          the admission guard accepted the skill into the registry
preflighted       invocation context checked for a given place and connection
task-authorized   a reviewed Task Contract authorizes it for ONE task
suspended         preflight failure, revoked trust or maintainer decision
superseded        a newer skill replaces it; history kept
retired           removed from the registry; references resolve to history
```

Each transition is a governed decision, not a runtime event:

| Transition | Gate |
|---|---|
| on-the-flow → candidate | post-task review — useful pattern observed, no reuse authorized |
| candidate → declared | distillation into manifest draft and bounded purpose |
| declared → validated | schema validation (`skill_manifest`, `capability_passport`) |
| validated → admitted | admission guard review — `visible != admitted` |
| admitted → preflighted | invocation preflight — `connected != authorized` |
| preflighted → task-authorized | Task Contract under the approval ceiling — `admitted != task-authorized` |
| any → suspended / superseded / retired | maintainer decision through the chokepoint |

No state is ever skipped, and no state grants the next one automatically. Authorization is **per task**: it expires with the Task Contract and is never a standing permission. Probation and quarantine, from the former stub's intended scope, are covered by `admitted`-with-constraints and `suspended` respectively.

## On-the-flow skills

An on-the-flow skill is a task-local technique, prompt pattern, extraction move, transformation step, checklist or micro-workflow assembled during a live workflow.

It may help one task.

It is not automatically reusable.

It is not admitted.

It is not a custom skill.

It is not a standing permission.

It may be logged in the workflow trace as:

```yaml
on_the_flow_skill:
  name:
  workflow_id:
  project_id:
  purpose:
  inputs:
  outputs:
  risks:
  observed_value:
  failure_modes:
  evidence_refs:
  files_touched:
  proposed_next_state: discard | candidate
```

Promotion path:

```text
on-the-flow use
-> workflow trace
-> post-task review
-> candidate pattern
-> manifest draft
-> validation
-> admission
-> per-task authorization
```

A useful on-the-flow skill becomes a custom skill only after distillation, manifesting, validation and admission.

Repeated successful use may justify review.

Repeated successful use does not itself approve the skill.

## Workflow composition

A workflow may combine:

```text
admitted Hermes skills
custom admitted skills
on-the-flow task-local skills
manual human steps
external connector calls
GraphRAG / retrieval / extraction candidates
LangGraph durable steps when externally bound
Langflow-designed patterns when externally bound
```

Pantheon records the composition and status.

Hermes or another runtime executes.

A workflow is therefore not a monolith. It is a sequence or graph of bounded steps with different authorization states.

The workflow trace should record:

```text
which skill ran
which runtime ran it
whether it was admitted, custom or on-the-flow
what source it used
what candidate it produced
what status it received
whether it should be discarded, repeated or distilled
```

## Non-collapses

```text
visible != declared != validated != admitted != preflighted != task-authorized
on-the-flow != candidate != declared != admitted
custom != approved unless admitted and task-authorized
runtime success != lifecycle promotion
repeated use != admission
an installed skill != a usable skill
```

## Boundary

The `candidate_support_note` profile from `BOUNDARY_PROFILES.md` applies. In addition, this document specifically does not implement a skill installer, marketplace, automatic admission, on-the-flow skill recorder, skill distiller, custom skill builder, provider router, scheduler, queue or lifecycle automation. Every transition above is a human-reviewed decision recorded as data.

## Relationship to existing doctrine

| Concern | Owner |
|---|---|
| Manifest shape | `SKILL_MANIFEST.md`, `schemas/skill_manifest.schema.yaml` |
| Passport shape | `schemas/capability_passport.schema.yaml` |
| Admission and registry | `CAPABILITY_REGISTRY.md` (SkillsGate) |
| Invocation preflight | `MODULE_INVOCATION_PREFLIGHT.md` |
| Per-task authorization | `TASK_CONTRACTS.md`, `APPROVALS.md` |
| Workflow trace | `ROLE_DIALOGUE_TRACE.md` |
| Watch on external skills | `WATCHLIST.md`; `SKILL_WATCHLIST.md` is a specialized reference view only |
