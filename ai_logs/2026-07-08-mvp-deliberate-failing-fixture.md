# AI log — MVP deliberate failing fixture

Date: 2026-07-08

Branch: `mvp-failing-fixture-307`

Status: documentation-only failing fixture.

## Purpose

Add a deliberate failing fixture and expected blocked report before any validator or CI gate exists.

## Files

```text
docs/governance/examples/mvp_vertical_fixture/failing_external_action.fixture.yaml
docs/governance/examples/mvp_vertical_fixture/failing_external_action.expected_report.yaml
docs/governance/examples/mvp_vertical_fixture/FAILING_FIXTURE.md
```

## Deliberate failure

The fixture is expected to pass schema and reference checks, but fail governance invariants.

```text
schema_status: pass
reference_status: pass
governance_status: fail
status: blocked
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

## Preserved distinctions

```text
schema_valid != approved
schema_valid != evidence
reference_valid != truth
governance_invariant_pass != external_action_authorization
fixture_pass != runtime_success
```
