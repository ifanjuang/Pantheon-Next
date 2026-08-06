# F to J Hermes Trajectory Adjustment

Status: validation-only roadmap adjustment — documented, not implemented.
Boundary profile: candidate_support_note.
Date: 2026-08-06

## 1. Objective

Record the bounded trajectory adjustments required for the current F-to-J development sequence after review of the current Pantheon repositories and the complete Hermes documentation surface.

This note does not reopen the completed Source, Information, EntityRef relation, WorkIssue scope or Decision Request tranches. It does not create a new runtime contract, execution object, scheduler, queue, provider router, plugin manager, skill manager, approval engine or memory engine.

The adjustment is a convergence decision:

```text
reuse existing Pantheon execution contracts
reduce duplicated Hermes management
validate with real project material throughout F-to-J
```

## 2. Observed current state

The current repositories already contain the execution boundary that a new intermediate tranche might otherwise have introduced:

```text
docs/governance/HERMES_EXECUTION_ADMISSION_BRIDGE.md
→ one bounded execution opportunity
→ exact WorkIssue version and Context Pack
→ separate effect authorization
→ normalized Hermes return


docs/governance/HERMES_RUN_LAUNCH_JUNCTION.md
→ binding-specific launch reservation
→ immutable launch context snapshot
→ qualified Hermes tool surface
→ native POST /v1/runs outside Pantheon
→ distributed ambiguity handled fail-closed

catalog/schemas/execution-result-candidate.schema.json
→ canonical candidate result envelope
→ runtime success explicitly not Evidence
→ human review required
```

Therefore:

```text
new generic ExecutionRequest concept is not justified
new F-to-J tranche X is not justified
existing admission + launch + candidate-result spine must be reused
```

The implementation must first inventory the exact current executable counterparts in `pantheon-mvp` before extending any shape.

## 3. Trajectory decision

The F-to-J order remains:

```text
F — ProjectClaims and consequential values
G — variants validated before any universal branch object
H — Anatomy relations and projection
I — Capability registry and bounded Hermes implementation links
J — optional adapters and real-project validation
```

The order is retained. The following boundaries are tightened.

## 4. F — ProjectClaims

F remains focused on consequential professional values and their provenance, effective date, contradiction, supersession and human adoption.

```text
Hermes output != ProjectClaim
runtime extraction != professional truth
runtime success != Evidence
```

A Hermes-produced value may be represented as candidate material linked to admitted sources and traces. It becomes a ProjectClaim only through the existing governed ProjectClaim transition.

Preferred lineage:

```text
Source / Document
→ admitted context
→ HermesResultCandidate or existing candidate result
→ review / Decision when required
→ ProjectClaim
```

No Hermes run, Skill, profile or provider becomes a direct professional source merely because it produced the value.

### F completion addition

F is complete only when one real project demonstrates that:

- an extracted or calculated candidate remains distinct from a ProjectClaim;
- provenance survives review and adoption;
- contradiction and supersession do not rely on runtime state;
- disabling Hermes does not remove authoritative ProjectClaims.

## 5. G — Variants

G retains the current refusal to create a universal `InformationBranch` before demonstrated need.

Variants produced by Hermes or another runtime must reuse the existing candidate-result spine rather than introduce a runtime-specific variant model.

```text
one execution
→ one or more candidate items / alternatives
→ comparison projection
→ human selection or refusal
→ governed application
```

Each candidate variant must retain, when applicable:

- producing execution and binding reference;
- admitted input and source references;
- assumptions and known limits;
- structured differences from the current state or sibling variants;
- compatibility findings;
- open questions;
- selection or rejection trace.

```text
variant selected != mutation applied
variant selected != Decision recorded
variant produced != Information retained
```

### G completion addition

G is complete only when a real CCTP, technical option or design alternative demonstrates selection, rejection and retained provenance without a universal branch object.

## 6. H — Anatomy

H remains after F and G.

Hermes may support plan, IFC, image, photograph, CCTP and detail reconciliation, but it may produce only bounded Anatomy candidates or mapping candidates.

```text
Hermes analysis
→ candidate objects / relations / mappings
→ compatibility and provenance review
→ governed application to APU authority
→ calculated Cockpit projection
```

Hermes must not mutate APU authority directly.

The generic EntityRef carrier does not become an open Anatomy relation graph. It remains generic in shape and closed in meaning. Anatomy relation vocabulary and authority must reuse or deliberately extend the existing APU contracts after inventory.

### H completion addition

H is complete only when one real multi-source project set demonstrates:

- candidate extraction from at least two source modes;
- explicit uncertainty and provenance;
- refusal of an incompatible or out-of-scope candidate;
- reviewed application without direct runtime mutation;
- stable authoritative APU data after the runtime is disabled.

## 7. I — Capabilities and Hermes

I is narrowed to Pantheon-owned governance responsibilities.

Pantheon owns:

```text
Capability identity
Implementation candidate
Implementation release or immutable revision
Runtime Binding
Admission posture
Scope activation
Observed compatibility and version drift
Improvement / replacement / retirement request
```

Hermes owns its native operational responsibilities:

```text
Skill storage and loading
plugin and MCP mechanics
profile configuration
provider routing
sandbox and terminal selection
agent sessions and sub-agents
cron, hooks, Kanban and internal automation
native runtime execution
```

Pantheon may observe these runtime states through reviewed adapters. It does not reproduce them as canonical governance objects merely because Hermes exposes them.

Required distinctions:

```text
Capability != Hermes Skill
Implementation != installed runtime copy
Binding selected != dependency adopted
installed != approved
healthy != safe
profile != Pantheon Scope
Hermes task / Kanban card != WorkIssue
Hermes approval event != Decision
```

### I implementation constraint

Before adding a new schema or registry, the implementation must verify whether the responsibility is already covered by:

- Capability Slot and Capability registry contracts;
- Tool Card governance contracts;
- runtime adapter and binding contracts;
- Hermes Execution Admission Bridge;
- Hermes Run Launch Junction;
- existing candidate-result contracts.

A new concept is permitted only when none of these can express a genuinely distinct responsibility.

### I completion addition

I is complete when one admitted Capability can use one bounded Hermes Binding while:

- Cockpit exposes the professional Capability rather than Hermes internals;
- the exact runtime version and compatible surfaces are observed;
- runtime configuration remains replaceable;
- activation remains scoped and human-governed;
- an unavailable or version-drifted Hermes binding fails closed;
- another future runtime could implement the same Capability without changing its identity.

## 8. J — Adapters and real-project validation

J remains the final consolidation tranche, but real-project validation must not be deferred entirely to J.

Validation cadence:

```text
after F
→ real consequential ProjectClaims

after G
→ real competing CCTP / technical / design variants

after H
→ real plans + IFC/images/photos/CCTP Anatomy set

after I
→ one bounded real Hermes Capability binding
```

J then consolidates:

- optional adapter replacement and disablement;
- version-drift behavior;
- ambiguous distributed launch reconciliation;
- failure and partial-result handling;
- trace and artifact retention;
- end-to-end human review;
- removal of temporary or parallel paths;
- confirmation that authoritative project data survives adapter removal.

```text
adapter available != adapter adopted
live target reachable != production qualified
acceptance run passed != Capability admitted everywhere
```

## 9. No new intermediate execution tranche

The earlier architectural concern was valid: F-to-I must not invent incompatible execution shapes.

The repository state resolves that concern through reuse, not addition.

```text
Execution Admission
+ Hermes Run Launch Junction
+ existing Context Pack / WorkIssue bindings
+ existing candidate-result contracts
= current execution spine to reuse
```

Any missing field discovered during F-to-I must be handled in this order:

1. reuse an existing field or contract;
2. extend the existing contract if the responsibility is the same;
3. generalize an existing structure if several runtimes need it;
4. create a new concept only for a distinct responsibility demonstrated by implementation and real-project validation.

## 10. Implementation guardrails

During F-to-J:

```text
Hermes result != Evidence
Hermes result != ProjectClaim
Hermes result != Information retained
Hermes relation candidate != APU relation
Hermes approval != Decision
Hermes profile != Scope
Hermes Skill != Capability
runtime success != WorkIssue closure
```

No tranche may introduce:

- a Pantheon-owned runtime or dispatcher;
- a second execution admission model;
- a second candidate-result model without inventory;
- a universal plugin, Skill or MCP manager;
- direct Hermes mutation of Project, Information, ProjectClaim, Decision, Knowledge or APU authority;
- automatic promotion from runtime output to Evidence or memory;
- a Cockpit projection that becomes backend authority.

## 11. Verification required before each implementation tranche

Before modifying executable code, verify:

- current `Pantheon-Next/main` contracts and authority indexes;
- current `pantheon-mvp/main` migrations, APIs, projections and Hermes adapters;
- recent commits, open branches, PRs and issues touching the tranche;
- existing tests for the same responsibility;
- schema provenance pins and vendored copies;
- consumers of any field or contract proposed for change;
- upstream Hermes version and exact surfaces used by the binding.

## 12. Completion criteria for this adjustment

This roadmap adjustment is satisfied when:

1. F-to-J proceeds without a new execution synonym or intermediate runtime layer;
2. F and G reuse the existing candidate-result spine;
3. H applies runtime-produced Anatomy candidates only through governed review;
4. I remains a Capability / Binding / Admission surface rather than a Hermes administration clone;
5. real-project validation occurs after each relevant tranche;
6. J verifies replacement, disablement, drift and end-to-end convergence;
7. authoritative Pantheon data remains valid when Hermes is unavailable or removed.

## 13. Decision summary

```text
F-to-J direction              retained
new execution tranche         rejected
existing execution spine      reused
F ProjectClaim boundary        tightened
G candidate-result reuse       required
H direct Hermes APU writes     forbidden
I Hermes management scope      reduced
J real validation              distributed then consolidated
```

This note adjusts trajectory only. It authorizes no implementation, runtime launch, capability admission, adapter activation, Project mutation or Evidence admission.
