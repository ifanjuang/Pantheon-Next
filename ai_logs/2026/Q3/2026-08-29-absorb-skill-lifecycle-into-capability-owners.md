# 2026-08-29 — absorb Skill Lifecycle into Capability owners

## Objective

Continue #787 and #824 by applying the distinct-owner test to `docs/governance/SKILL_LIFECYCLE.md` from exact base `870518c034d83f216ba224650a2d562649ad3209`.

## Scope

Documentation convergence only:

- `SKILL_LIFECYCLE.md`;
- its direct current governance consumers;
- the Governance Authority Index placement row;
- this dated intervention log.

No schema, test, runtime, implementation, Task Contract, activation record or persistence change is part of this slice.

## Owner test

Question from #787:

> If all rules already owned elsewhere are removed, does enough distinct normative responsibility remain to justify an independent owner?

Observed mapping:

```text
Skill as governed primitive
-> UNIFORM_CAPABILITY_GOVERNANCE.md
-> CAPABILITY_REGISTRY.md
-> capability/skill manifest + passport schemas

Capability detected / activated / suspended / task-authorized
-> MODULE_ACTIVATION.md
-> TASK_CONTRACTS.md / APPROVALS.md

Invocation eligibility / connectivity preflight
-> MODULE_INVOCATION_PREFLIGHT.md

External Skill/package observation
-> WATCHLIST.md
-> REFERENCE_BOUNDARIES.md

Extracted external patterns
-> DISTILLATION_REGISTRY.md
-> REJECTED_PATTERNS.md where applicable

On-the-flow improvisation / execution shape
-> WORKFLOW_FORGING_PROTOCOL.md as task-local technique/composition
-> not a new governed Skill identity merely because it was useful once

Runtime package loading / installation / execution
-> Hermes / external runtime placement
-> not Pantheon Skill lifecycle authority
```

## Decision

No distinct Skill-specific governance seam remained after the existing owners were applied.

`SKILL_LIFECYCLE.md` was therefore absorbed and removed rather than narrowed into another parallel lifecycle owner.

The removed linear chain mixed independent axes:

```text
observation / distillation posture
manifest/schema validation
Capability admission
activation
preflight
task authorization
suspension / supersession
runtime observation
```

Those axes remain deliberately separate.

## Consumer changes

- `UNIFORM_CAPABILITY_GOVERNANCE.md` now routes Skill-backed capabilities through the universal Capability law, `CAPABILITY_REGISTRY.md`, Watchlist/reference owners and runtime placement rather than a Skill lifecycle owner.
- `DISTILLATION_REGISTRY.md` routes Skill anatomy, anti-pattern, evaluation and manager-demotion patterns to existing Capability, Watchlist, Evidence, simulation and rejection owners.
- `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md` no longer lists `SKILL_LIFECYCLE.md` as a candidate owner.

## Preserved invariants

```text
Skill discovered != Capability admitted
Skill installed != activated
binding selected != dependency adopted
activated != task-authorized
task-authorized != approved
runtime success != Evidence
evaluation signal != admission
useful task-local technique != reusable governed Capability
```

## Follow-up

#824 may proceed to external-corpus distillation only after this exact slice passes Governance CI, Pantheon Architecture Audit, Obsolete Authority Consistency and review.

Any future machine-contract change around Skill manifests remains a separate protected-path decision after consumer mapping; this slice changes no schema.
