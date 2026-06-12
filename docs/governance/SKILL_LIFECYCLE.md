# Skill Lifecycle

Status: candidate support doctrine — to verify. Written fresh by distillation (per the migration policy: distill, never bulk-copy); replaces the former Pantheon-OS stub.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A skill moves through governed states from the moment it becomes visible to the moment it is retired. This document names those states and the gate between each pair. It composes what already exists — the manifest (`SKILL_MANIFEST.md`), the capability passport (`UNIFORM_CAPABILITY_GOVERNANCE.md`), the registry and admission guard (`CAPABILITY_REGISTRY.md`), the invocation preflight (`MODULE_INVOCATION_PREFLIGHT.md`) — into one lifecycle. It adds no new mechanism.

## The lifecycle

```text
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
| declared → validated | schema validation (`skill_manifest`, `capability_passport`) |
| validated → admitted | admission guard review — `visible != admitted` |
| admitted → preflighted | invocation preflight — `connected != authorized` |
| preflighted → task-authorized | Task Contract under the approval ceiling — `admitted != task-authorized` |
| any → suspended / superseded / retired | maintainer decision through the chokepoint |

No state is ever skipped, and no state grants the next one automatically. Authorization is **per task**: it expires with the Task Contract and is never a standing permission. Probation and quarantine, from the former stub's intended scope, are covered by `admitted`-with-constraints and `suspended` respectively.

## Non-collapses

```text
visible != declared != validated != admitted != preflighted != task-authorized
runtime success != lifecycle promotion
repeated use != admission
an installed skill != a usable skill
```

## Boundary

The standard non-implementation boundary applies — see `BOUNDARY_STANDARD.md`. In addition, this document specifically does not implement a skill installer, a marketplace, automatic admission, or any lifecycle automation: every transition above is a human-reviewed decision recorded as data.

## Relationship to existing doctrine

| Concern | Owner |
|---|---|
| Manifest shape | `SKILL_MANIFEST.md`, `schemas/skill_manifest.schema.yaml` |
| Passport shape | `schemas/capability_passport.schema.yaml` |
| Admission and registry | `CAPABILITY_REGISTRY.md` (SkillsGate) |
| Invocation preflight | `MODULE_INVOCATION_PREFLIGHT.md` |
| Per-task authorization | `TASK_CONTRACTS.md`, `APPROVALS.md` |
| Watch on external skills | `SKILL_WATCHLIST.md` |
