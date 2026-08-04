# Revit Local Adapter Boundary

Status: candidate support doctrine — canonical local-adapter boundary — documented non-implemented.
Boundary profile: external_runtime_adapter.

This document is the single authority for the placement of a future local Revit adapter in the Pantheon ecosystem. It consolidates the useful boundary material already present in the repository; it does not create a new semantic layer or claim that an add-in is installed, healthy, activated or authorized.

```text
Pantheon Next governs contracts, scope, status, Evidence posture and human gates.
pantheon-mvp may implement candidate APIs, projections and adapter seams.
Hermes may orchestrate an admitted task as an external runtime.
The Revit add-in alone executes Revit API calls inside Revit context.
Cockpit or OpenWebUI exposes preflight, warnings, proposals and results.
The human decides consequential mutations.
```

```text
installed != approved
healthy != safe
activated != task_authorized
preflight_passed != effect_authorized
transaction_success != accepted_result
runtime_success != Evidence
UI status != authorization
```

## Purpose

The adapter connects a live Revit document to governed Pantheon work without moving Revit execution into Pantheon. It may observe exact model context, prepare bounded candidates and, after explicit authorization, execute a named local transaction through an external add-in.

This repository currently contains documentation, examples and a non-compiling reference skeleton only. It contains no active Revit add-in, installer, updater, relay, scheduler, queue, provider router, plugin manager, approval engine or autonomous transaction runner.

## Responsibility split

### Pantheon Next

Pantheon Next owns:

```text
Capability Slot and binding boundaries
Task Contract and requested-effect vocabulary
scope and Context Pack requirements
approval ceiling and human-decision requirements
Claim, ChangeCandidate and Evidence posture
status semantics and non-equivalences
adapter adoption and revocation doctrine
```

Pantheon Next does not call the Revit API, open a transaction, save, synchronize or mutate an RVT file.

### pantheon-mvp

A future implementation candidate may own:

```text
bounded adapter API surfaces
Cockpit projections
preflight and result-candidate persistence
external-runtime handoff seams
technical observations and receipts
```

Implementation and successful CI do not constitute adoption or activation.

### Hermes or another admitted runtime

An external runtime may:

```text
consume one admitted Task Contract and Context Pack
prepare a method or action candidate
request a bounded adapter operation
continue independent admitted work while one action is blocked
return a Result Candidate and technical trace
```

It may not infer a broader scope, manufacture human approval, bypass the add-in, select a hidden provider on Pantheon's behalf or promote its result to Evidence.

### Revit add-in

The add-in owns:

```text
Revit API compatibility
active-document and active-view observation
selection and element resolution
freshness checks
Revit-thread execution
named Transaction and TransactionGroup discipline
failure handling and rollback observation
changed-element journaling
local stop and disable controls
```

The add-in is the only component allowed to execute Revit API mutations. Production code should live in a dedicated implementation repository. The `revit-plugin/` directory in this repository is a non-executable reference skeleton and is not a code-hosting precedent.

### Cockpit or OpenWebUI

The user surface may display:

```text
binding and installation observations
Task Contract and exact scope
Context Pack summary
preflight observations and unresolved blockers
method and ChangeCandidate previews
affected elements
human decision controls
technical result and rollback posture
Evidence candidates and provenance references
```

A projection does not own business truth or authorization.

### Human

A human decision remains required for adapter adoption, binding activation and every consequential mutation. Acceptance of a technical result, application of a ChangeCandidate, Evidence admission, saving, synchronization, publication and transmission remain separate decisions.

## Reuse of existing Pantheon concepts

The Revit boundary reuses the current model rather than defining a parallel workflow.

| Need | Existing owner |
|---|---|
| declare the abstract function | Capability Slot and binding records |
| bound one request | Task Contract |
| carry exact project, model, view and selection context | Context Pack and source references |
| represent observed project understanding | Project Understanding adapter contract and Result Candidate |
| propose a consequential model or Project change | ChangeCandidate |
| record technical execution | Trace, action-report candidate or technical receipt |
| qualify supporting material | Evidence Pack Candidate followed by separate admission |
| report an unavailable prerequisite | Capability Gap or typed blocker observation |
| expose work and decisions | Work Issue and Cockpit projections |

Labels such as `Model Observation Candidate`, `Preflight Report Candidate` or `Action Log Candidate` are presentation labels inside these existing envelopes. They are not new canonical entities.

## Capability and binding posture

```yaml
capability_id: revit_local_adapter
abstract_function: inspect and modify a bounded Revit document through a local add-in
binding_state: candidate
installation_state: not_observed
health_state: not_observed
activation_state: not_activated
task_authorization_state: not_authorized
executed_by: external Revit add-in
orchestrated_by: admitted external runtime when selected
governed_by: Pantheon Next
approved_by: human for consequential effects
```

The product version, .NET target, packaging method and Revit API compatibility belong to the binding observation. They must not be encoded in the architecture identity.

## Effect classification

Adapter-local effect classes must map to the Task Contract requested effect and approval ceiling.

| Adapter-local class | Meaning | Default posture |
|---|---|---|
| `read_only` | observe document, view, selection, elements, warnings or parameters | allowed only inside admitted scope |
| `candidate_only` | highlight, preview, analyze, prepare a method or ChangeCandidate | no Revit mutation |
| `write_light` | create a bounded review artifact or explicitly allowed review parameter | human authorization and named transaction required |
| `write_model` | create or modify architectural model elements | blocked until a dedicated binding slice proves scope, preflight, rollback and review |
| `external_effect` | save, sync, publish, transmit, install, execute arbitrary code or alter shared state | refused unless a later explicit contract and human decision authorize the exact effect |

The former numbered warning levels are historical planning vocabulary, not a second approval model. Their useful meaning converges as follows:

```text
historical observation level       -> read_only
historical proposal level          -> candidate_only
historical light-write level       -> write_light
historical model-write level       -> write_model
historical destructive/code levels -> external_effect or refusal
```

## Admission and execution sequence

```text
1. A binding is selected and separately observed.
2. A human or governed surface prepares a Task Contract and exact Context Pack.
3. Pantheon records admission for the requested effect; no dispatch is inferred.
4. The external runtime prepares a method or ChangeCandidate when required.
5. The add-in performs a fresh preflight against the open Revit document.
6. A human authorizes the exact consequential effect when required.
7. The add-in executes one named local transaction or refuses.
8. The add-in returns changed-element observations, failures and rollback posture.
9. Hermes returns a Result Candidate and Trace.
10. Result acceptance, ChangeCandidate application and Evidence admission remain separate.
```

A stale document, view, selection, element set, phase, design option, workset or host invalidates the preflight. The correct result is a visible conflict or Capability Gap, not an improvised mutation.

## Preflight minimum

Before a write, the add-in should return at least:

```text
document identity and Revit binding version
active view and view type
exact target element references
selection or work-area source
phase and design-option context
worksharing, workset and ownership observations
linked-model involvement
pinned, grouped, constrained and hosted-element observations
family and type availability
requested effect and approval reference
transaction-name candidate
expected created, modified and deleted categories
rollback or manual-reversal posture
freshness token or equivalent document-state observation
forbidden-effect findings
```

A passed preflight is a technical observation. It does not authorize the effect.

## Transaction discipline

Every committed mutation must execute inside Revit context with a deterministic name:

```text
PantheonRevit:<task_id>:<action_id>:<short_effect>
```

The add-in should journal:

```text
binding and Revit versions
document reference
transaction name
Task Contract and approval references
started_at and finished_at
created, modified and deleted ElementIds where available
warnings and failures
commit, rollback or partial-result observation
manual reversal note when rollback is unavailable
```

The add-in must not silently save or synchronize after a successful transaction.

## Blockers and partial continuation

Missing families, invalid hosts, pinned or grouped elements, linked targets, worksharing locks, stale selections, phase conflicts and design-option conflicts are typed technical observations.

They do not create a second task-state machine. Existing Work Issue, run event, Result Candidate and Capability Gap surfaces carry the state. Hermes may continue only independent admitted actions; it may not create a hidden queue, silently change the method or resume a stale write without a new preflight.

## Source, Claim and Evidence posture

A Revit observation preserves:

```text
source document identity
binding and Revit version
view, selection and element references
observation time
method and parameters
technical warnings
```

```text
observed != validated
absence_of_warning != safe
transaction_success != professional_validation
action_log != Evidence
screenshot != proof
Result Candidate != accepted result
Evidence Pack Candidate != Evidence admitted
```

A consequential model proposal remains a ChangeCandidate until reviewed and applied through its owning authority. The adapter must not mutate unrelated Project records directly.

## Sandbox and production

A disposable local copy may use a reviewed sandbox policy for learning. Sandbox freedom does not alter canonical authority, authorize production use or make destructive effects acceptable.

Real, workshared, linked, contractual or client models require stricter binding policy. Save, sync, purge, linked-model writes, arbitrary generated code and silent background mutation remain refused by the current boundary.

## Adoption gates

Before any binding is adopted or activated, verify together:

```text
implementation repository and owner
exact Revit and .NET compatibility
signed or otherwise reviewed package identity
installer and rollback procedure
no silent startup mutation
no implicit save, sync, purge or publication
visible stop and disable control
Task Contract and Context Pack correlation
fresh preflight and named transactions
changed-element trace
refusal of out-of-scope and stale operations
human gate before consequential effects
sandbox and production profiles separated
secrets and sensitive local paths redacted
one read-only acceptance and one rollback proof
```

## Supporting documents

The existing Revit documents remain subordinate specializations, not parallel authorities:

```text
PANTHEON_REVIT_GATE.md
  capability catalogue and exploratory scenarios

PANTHEON_REVIT_LOCAL_SANDBOX_EXCEPTION.md
  optional disposable-copy sandbox posture

PANTHEON_REVIT_FIRST_SANDBOX_ACTION_CONTRACT.md
  first bounded action example

PANTHEON_REVIT_GATE_2027_PROTOTYPE_PLAN.md
  product-version and implementation planning

PANTHEON_REVIT_GATE_DEVELOPER_DOSSIER.md
  detailed developer-oriented planning

revit-plugin/
  non-executable reference skeleton
```

Where a supporting document conflicts with this boundary or later canonical schemas and registries, this boundary and the canonical owner prevail.

## Final rule

```text
Pantheon governs.
Hermes may orchestrate an admitted task.
The Revit add-in executes locally.
Cockpit exposes the decision surface.
The human decides consequential effects.
Technical success remains technical evidence only.
```
