# Capability governance convergence inventory — 2026-08-09

Status: audit / repository-truth inventory. Non-normative.

Parent issues: #620, #615.

## Objective

Inventory the current Capability / Capability Slot / skill admission / binding / implementation / activation / compatibility surfaces before tranche I changes any schema or executable owner.

This audit distinguishes current `main` from historical closed-unmerged proposals.

## Authority baseline

```text
Pantheon-Next = governance doctrine, schemas, status vocabulary and boundaries
pantheon-mvp  = executable implementation and Cockpit projections
Pantheon-plugins = external adapter/plugin implementation
Hermes / external runtimes = execution
human = consequential decision
```

I must not create a runtime, installer, plugin manager, provider router, scheduler, queue or autonomous approval engine.

## Historical correction

Pantheon-Next PRs #554 and #555 were closed without merge.

Their proposed F-to-J wording is historical context only. It is not current repository authority and is not used here as a merged baseline.

## Current Pantheon-Next surfaces

### `docs/governance/CAPABILITY_PLACEMENT.md`

Observed status: active support doctrine.

Observed responsibility:

- tool-agnostic placement;
- durable runtime/governance boundaries;
- governed handoff posture;
- Capability Gap semantics;
- explicit rule that runtime availability does not authorize use.

Decision: **retain as placement/boundary owner**.

It should not become the registry of concrete implementations.

### `docs/governance/CAPABILITY_REGISTRY.md`

Observed status: candidate / to verify.

Observed responsibility:

- abstract capability declarations;
- purpose, inputs, outputs, forbidden effects, risk, dependencies, scope and evidence expectations;
- governed composition support.

Observed convergence issue:

One shared-vocabulary section states:

```text
skill_manifest.skill_id == capability_step.capability_id
```

The current workflow schema already models:

```text
capability_step.capability_id
capability_step.skill_manifest_ref -> skill_manifest.skill_id
```

Those shapes are not equivalent. The schema already supports an abstract Capability with an optional backing Skill reference, while the prose still contains an identifier-collapse assumption.

Decision: **retain the abstract registry purpose; reconcile identity wording in I1 only after consumer checks**.

### `docs/governance/HERMES_CAPABILITY_BINDINGS.md`

Observed status: candidate support doctrine / documented non-implemented.

Observed responsibility:

```text
Capability Slot
-> preferred / fallback / watch / rejected binding
-> separate install / health / update / activation states
```

Useful existing distinctions:

```text
binding_selected != dependency_adopted
installed != approved
healthy != safe
update_available != update_authorized
runtime_success != Evidence
```

Decision: **retain as the principal candidate source for binding/slot convergence; do not promote wholesale before executable-owner reconciliation**.

### `schemas/skill_manifest.schema.yaml`

Observed executable schema responsibility:

- watched/candidate Skill or capability-pack declaration;
- `skill_id` identity;
- lifecycle, installation state, approvals, risk, allowed/forbidden use, evidence expectation;
- explicitly no runtime, plugin manager or automatic installation.

Decision: **retain as Skill admission-oriented contract; do not silently redefine `skill_id` as abstract Capability identity**.

### `schemas/workflow_manifest.schema.yaml`

Observed executable schema responsibility:

`governed_composition.capability_steps[]` carries:

```text
capability_id
optional skill_manifest_ref
scope
forbidden scope
Task Contract requirement
Evidence expectation
approval ceiling
risk
refusal tests
```

Decision: **retain**. Its explicit `skill_manifest_ref` is the strongest current schema evidence for separating Capability identity from backing Skill identity.

## Current pantheon-mvp surfaces

### `mvp_vertical/capability_manager.py`

Observed current-main implementation:

`CapabilityRecord` contains:

```text
capability_id
capability_type
installation_status
enablement_status
activation_scope
health_status
update_status
source_ref
```

Its accepted `capability_type` values are:

```text
skill
function
workflow
runtime_agent
plugin
mcp_binding
connector
```

The manager plans and gates lifecycle actions and asks an injected external executor to perform one native operation. Technical receipt remains distinct from Evidence.

Observed issue:

The record name says `Capability`, while `capability_type` enumerates runtime/component forms. This may be an implementation convenience or a semantic conflation between abstract Capability and implementation kind.

Decision: **retain current code unchanged during I0; inspect consumers and tests before deciding whether I1/I2 must narrow or split the record**.

### `tests/test_capability_manager.py`

Observed coverage confirms:

- unknown capability types are refused;
- install requires a human decision;
- blocked policy prevents executor invocation;
- install/update/enable/retire remain explicit transitions;
- technical executor effect is externally injected.

Gap observed for tranche I:

The tests do not currently prove an abstract Capability identity can remain stable across multiple implementation kinds/releases.

Decision: **candidate failing scenario for I1/I2, not a reason to change code in I0**.

### Tool Card catalogue

`mvp_vertical/cockpit/tool_catalog.json` already separates:

```text
tool_id
capability_slots[]
binding_role
installation_state
health_state
governance_state
update_state
activation_state
```

The catalogue explicitly declares itself non-authoritative.

Decision: **retain as projection/catalogue data; never make `tool_id` the Capability owner**.

### Agent Plugin package/component observations

`mvp_vertical/agent_plugin_package.py` already preserves:

```text
package name/version/digest
component_id
component_kind
component_ref
component status
unreviewed governance state
not_activated activation state
unauthorized task state
observed_at
```

and explicitly does not install, activate or authorize.

Decision: **reuse this provenance pattern for I2 before inventing a new implementation/release model**.

### Execution Admission

Existing MVP Execution Admission already owns bounded task/run legitimacy.

Decision: **retain as the sole task/run admission seam**.

Tranche I may define implementation eligibility or scoped activation, but must not create a parallel task authorization owner.

## Closed-unmerged MVP material

pantheon-mvp PR #201 proposed `mvp_vertical/runtime_profile.py`, but it was closed without merge.

Decision: **historical reference only; do not cite as current implementation and do not resurrect by default**.

## Pantheon-plugins

The Revit adapter is an external implementation candidate. Its current live qualification remains part of H.

Decision:

```text
Revit implementation identity may later participate in I
Revit project/source qualification remains H
```

I must not duplicate the H PDF/IFC/Revit qualification protocols.

## Current convergence map

### Retain

```text
CAPABILITY_PLACEMENT.md                 placement/boundary owner
workflow_manifest capability_id        abstract workflow-step capability reference
skill_manifest                         Skill admission-oriented declaration
HERMES_CAPABILITY_BINDINGS.md          candidate binding/slot vocabulary
Tool Card catalogue                    UI/catalogue projection
Agent Plugin component provenance      implementation observation pattern
Execution Admission                    task/run legitimacy owner
```

### Reconcile later, only with tests

```text
CAPABILITY_REGISTRY identity wording
CapabilityRecord semantic level
Skill <-> Capability join semantics
Capability Slot <-> implementation binding identity
admission <-> scoped activation <-> task authorization boundaries
compatibility observation vocabulary
```

### Do not resurrect by default

```text
closed-unmerged runtime_profile implementation
closed-unmerged F-to-J trajectory proposals
historical assumed Hermes native capability-operation endpoint
```

## Proven gaps / candidate test obligations

The following gaps are demonstrated by current shapes and should become failing scenarios before implementation changes:

1. One abstract Capability must be able to reference multiple implementations/releases without changing `capability_id`.
2. One Skill/component must not become a Capability merely because it is discovered, valid or installed.
3. Binding selection must not imply dependency adoption or activation.
4. Implementation admission must not imply Task Contract / Execution Admission authorization.
5. Scoped activation must not authorize an arbitrary task.
6. Health/runtime success must not produce compatibility/safety/Evidence automatically.
7. Tool Card state must remain a projection of canonical owners.
8. H source/adapter qualification must remain independent from I admission.

## Recommended I sequence from repository truth

```text
I0  inventory and convergence decisions
I1  abstract Capability identity + vocabulary convergence
I2  implementation/release identity and provenance
I3  Capability Slot / binding convergence
I4  admission and eligibility
I5  scoped activation vs task authorization
I6  observed compatibility posture
I7  Cockpit / Tool Card projection convergence
I8  representative end-to-end vertical + adversarial cases
I9  convergence audit and closure
```

The sequence is a planning result of this audit. It becomes implementation work only slice by slice after its predecessor proves the next change is necessary.

## I0 remaining verification

Before I0 closes:

- enumerate direct consumers of `CapabilityRecord`;
- enumerate tests and runtime consumers of Capability Slot fields;
- map current policy/User Decision Gate fields against Skill/Capability admission;
- map current activation scope against Task Contract / Execution Admission;
- inventory current compatibility observations actually merged on `main`;
- select one representative existing Capability/binding for I8 based on coverage, not convenience.

## Current conclusion

No new schema or owner is justified yet.

The strongest convergence direction already present in the repository is:

```text
abstract capability_id
-> explicit backing implementation/skill reference
-> replaceable binding
-> separate admission
-> optional scoped activation
-> separate task/run authorization
-> bounded runtime observation
-> non-authoritative Cockpit projection
```

This is an audit conclusion, not a schema promotion.