# AI log — MVP validation report shape

Date: 2026-07-08

Branch: `mvp-report-shape-306`

Status: documentation-only expected report shape.

## Purpose

Define the expected output shape of a future MVP fixture validator before any validator code exists.

## Files

```text
docs/governance/examples/mvp_vertical_fixture/validation_report.example.yaml
docs/governance/examples/mvp_vertical_fixture/VALIDATION_REPORT_SHAPE.md
```

## Decision

The example report uses:

```yaml
status: reviewable
```

It does not use approval-like language.

## Boundary

No validator was added.
No command was added.
No CI was changed.
No runtime was added.
No database mapping was added.
No OpenWebUI feature was added.
No Hermes contract was added.
No approval engine or memory promotion was added.

## Preserved distinctions

```text
schema_valid != approved
schema_valid != evidence
reference_valid != truth
governance_invariant_pass != external_action_authorization
fixture_pass != runtime_success
```

Next step: add a deliberate failing fixture and expected failing report before any CI gate.
