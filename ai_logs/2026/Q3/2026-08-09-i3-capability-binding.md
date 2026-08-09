# 2026-08-09 — I3 Capability Binding convergence

Parent: #620
Issue: #632

## Objective

Converge Capability Slot binding into one bounded candidate relation without restoring obsolete Preset/install-composition manifests or creating a runtime registry.

## Repository facts

- `HERMES_CAPABILITY_BINDINGS.md` already owns the candidate Slot/binding vocabulary.
- current catalog Capability manifests can list candidate Resources but do not express an exact binding selection.
- current Resource manifests describe candidate external/runtime resources.
- I2 Capability Passports can carry exact immutable implementation provenance.
- HandoffDecision and CurrentDecisionProjection own bounded human handoff decision lineage, not binding selection.
- former catalog Presets and installation-composition schema are explicitly obsolete.

## Demonstrated gap

No machine-checkable current contract could represent:

```text
Capability Slot
-> governed Capability Passport
-> exact immutable implementation release anchor
-> binding role/status
```

without either overloading a Capability/Resource record or resurrecting obsolete composition manifests.

## Decision

Add one candidate `CapabilityBinding` relation under `catalog/`.

It references:

```text
slot_id
capability_passport_id
implementation_anchor {kind, value}
optional resource_id
binding_role / status
optional supersedes
```

It does not copy the Capability Passport or I2 implementation provenance body.

`implementation_anchor.kind` reuses I2 immutable anchors:

```text
commit_ref
content_digest
package_digest
```

Binding status reuses `HERMES_CAPABILITY_BINDINGS.md` vocabulary.

`unbound` is explicit and valid, with no target Capability, release or Resource.

## Governance constants

Every binding record is selection-only:

```text
selection_only: true
dependency_adopted: false
installation_authorized: false
activation_authorized: false
task_authorized: false
```

## Non-equivalences

```text
Capability Slot != Capability
candidate_resource != selected_binding
binding_selected != dependency_adopted
binding_selected != installed
binding_selected != activated
binding_selected != task_authorized
fallback visible != active
unbound != missing governance
replacement release != automatic approval
```

## Boundary

No automatic selection, installer, provisioner, plugin manager, provider router, scheduler, queue, runtime inventory mirror, admission engine, activation path, Task Contract authorization, Evidence admission or H qualification behavior is added.
