# 2026-08-09 — I5 scoped Capability Binding activation

Parent: #620
Issue: #636

## Objective

Attach governance activation to an exact Capability Binding and scope without creating runtime activation or task authorization.

## Repository basis

- `MODULE_ACTIVATION.md` already defines detection -> governance activation -> task authorization.
- `module_manifest.schema.yaml` already owns the activation-state vocabulary.
- `task_contract.schema.yaml` already owns the scope-type vocabulary.
- I3 already owns exact `CapabilityBinding` identity.

## Demonstrated gap

No current machine-checkable record joined an exact binding to the existing scoped activation vocabulary. Module-level activation alone cannot prove that replacement binding B inherited no activation from A.

## Convergence

Add one bounded `CapabilityActivation` record under the candidate catalog. It references `binding_id` only and reuses existing activation and scope vocabularies.

Enabled states require:

```text
reviewed record
+ exact binding_id
+ scope_type + scope_id
+ decision_ref
```

The record always states:

```text
record_only: true
runtime_activation_effect: none
task_authorization_effect: none
automatic_activation: false
binding_replacement_inherits_activation: false
```

## Boundaries

```text
binding selected != activated
activated for scope != task-authorized
activation record != runtime activation effect
activation of binding A != activation of replacement binding B
human decision reference != execution authorization
```

No runtime activator, installer, provisioner, autonomous approval, Task Contract authorization, Evidence admission or H qualification path is introduced.
