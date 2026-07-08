# AI log — MVP validation plan

Date: 2026-07-08

Branch: `mvp-validation-plan-305`

Status: documentation-only validation plan.

## Purpose

Define how to validate the MVP fixture target later without adding a validator, CI check or runtime.

## File

```text
docs/governance/examples/mvp_vertical_fixture/VALIDATION_PLAN.md
```

## Layers

```text
Layer 1: YAML and schema validation
Layer 2: cross-object reference validation
Layer 3: governance invariant validation
```

## Boundary

No validator was added.
No command was added.
No CI was changed.
No runtime was added.
No database mapping was added.
No OpenWebUI feature was added.
No Hermes contract was added.
No approval engine or memory promotion was added.

## Key rule

The first validation should be local/manual, not CI.

```text
schema_valid != approved
schema_valid != evidence
reference_valid != truth
governance_invariant_pass != external_action_authorization
fixture_pass != runtime_success
```
