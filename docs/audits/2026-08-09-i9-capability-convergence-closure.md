# I9 Capability convergence closure audit — 2026-08-09

Status: audit / repository-truth closure record. Non-normative.

Parent: #620  
Audit issue: #645

## Objective

Re-evaluate tranche I after I0–I8 against current Pantheon-Next, pantheon-mvp and Pantheon-plugins state, remove proven competing semantic paths, and close I only if the final owners remain distinct without adding runtime-management responsibilities to Pantheon.

## Baseline

Tranche I entered I9 with these merged concerns:

```text
Capability Passport / governed Capability unit
exact implementation/release provenance
CapabilityBinding
CapabilityActivation
CapabilityCompatibilityObservation
MVP Execution Admission
MVP Tool Card projection
```

H remains independently responsible for Project Anatomy source/adapter qualification, including the real-environment/Revit work still tracked by H5.9.

## I9 corrections

### Competing I7 path removed

pantheon-mvp #310 and its duplicate issue #309 were closed as superseded by the already merged canonical I7 path #311.

No second Tool Card projection path remains active through an open PR/issue.

### Passport ownership converged

Pantheon-Next #648 merged as `0f9e14522a17167d9a9dd7a05fc3af0ae7cfb2ec`.

Final responsibility:

```text
Capability Passport
= governed Capability classification + exact-release eligibility

CapabilityActivation
= scoped governance activation for one exact CapabilityBinding

Task Contract / Execution Admission
= task/run legitimacy
```

Historical Passport `activation_state` and `task_authorization` fields are compatibility-only. They are optional/deprecated, and a positive Passport `task_authorized` claim is invalid.

### Binding repository status reconciled

Pantheon-Next #650 merged as `4efbc09140eeb45b413f0ceb970ff5a57f429ca7`.

`HERMES_CAPABILITY_BINDINGS.md` and its authority-index row now distinguish implemented declarative Binding/Activation/Compatibility records from external runtime installation/adoption/activation.

```text
declarative contract implemented != runtime binding installed
```

### Operational status vs exact-release eligibility

The legacy read-only `qualify_capability_status()` surface is retained as a caller-provided operational-status qualifier only.

It is not a second admission owner:

```text
reported governance_status
!= Capability Passport exact-release eligibility

reported task_use_status
!= Task Contract / Execution Admission
```

The canonical exact-release eligibility owner is the Passport validator. The operational qualifier remains non-authorizing and performs no runtime probe.

### Task Contract / Binding boundary — corrected I9 interpretation

The initial I9 audit considered adding exact `binding_id` / implementation anchor continuity into Task Contract / Execution Admission.

Deeper authority and consumer review rejects that as the default convergence target.

Reason:

- Capability Binding is a replaceable governance relation;
- CapabilityActivation governs where an exact Binding is enabled;
- Task Contract governs task intent/scope/constraints and must not become provider/runtime routing;
- Execution Admission freezes task/run legitimacy through the immutable Task Contract / Context Pack / preview basis;
- Hermes remains responsible for execution mechanics.

Therefore the final invariant is separation, not forced identity collapse:

```text
Capability activation != task authorization
Task Contract != runtime binding selection
Execution Admission != Capability admission
```

An adapter may preserve exact implementation/binding provenance where an existing interface explicitly supports it, but I does not create a universal binding field in Task Contract merely to connect two distinct authorities.

### Cockpit projection boundary — corrected I9 interpretation

The canonical I7 Tool Card projection already consumes the I2–I6 dimensions when supplied and displays missing values as `not_observed`.

The fact that current deployment does not yet feed canonical I2–I6 records through a server-side join is an operational integration posture, not proof of a missing semantic owner.

A future live feed must reuse the same canonical owners. It must not make the static Tool catalogue, Hermes inventory or browser authoritative.

pantheon-mvp #313 records this closure boundary; it must be merged only after exact-head CI is green.

## Representative vertical interpretation

I8 mechanically validates the exact Capability governance chain:

```text
Capability Slot
-> Capability Passport + exact release
-> CapabilityBinding
-> CapabilityActivation
-> CapabilityCompatibilityObservation
```

The adjacent MVP tests independently prove:

```text
Capability activation has no task-authorization effect
Execution Admission is required for task/run legitimacy
Tool Card projection has no authorization effect
```

I9 therefore treats the representative vertical as a composed proof across deliberately distinct owners rather than requiring a single object or identifier to traverse every boundary.

This is stronger convergence than adding an artificial universal identifier because it preserves replaceability and authority separation.

## Final evaluation of #620 exit criteria

```text
1  Slot / Passport / Binding responsibilities        PASS
2  Skill/Tool availability does not imply admission PASS
3  exact release provenance sufficient              PASS
4  replaceable bindings != dependency adoption      PASS
5  eligibility distinct install/task authorization  PASS
6  scoped activation distinct task authorization    PASS
7  compatibility distinct health/safety/Evidence    PASS
8  Execution Admission sole task/run legitimacy     PASS
9  Cockpit projects without owning                   PASS
10 representative vertical proves composed chain    PASS
11 no runtime-management moved into Pantheon        PASS
12 Next/docs/MVP/plugins agree final semantics       PASS after #313 exact-head merge
13 H source/adapter qualification unchanged         PASS
```

## Residual non-blocking items

- `mvp_vertical/capability_manager.py::CapabilityRecord` retains older broad lifecycle naming. No conflicting semantic owner or failing consumer was demonstrated, so I9 does not refactor it for aesthetics.
- historical closed-unmerged F→J branches remain visible remotely where branch deletion is not available through the current connector. They are not current authority and have no open PR.
- live canonical Tool Card feed remains deployment/integration work, not an I semantic owner.
- H5.9 real NAS/Hermes/Revit qualification remains H work and is not blocked by I closure.

## Closure condition

I9 may close after:

1. pantheon-mvp #313 exact-head CI is green and the documentation boundary is merged;
2. this final audit/consultation clarification passes exact-head Pantheon-Next CI;
3. #620 is updated from its stale I2-NEXT body to the final I0–I9 result.

No additional schema, runtime, join service, installer, scheduler, queue, provider router, plugin manager, admission engine or UI authority is justified by the current repository state.