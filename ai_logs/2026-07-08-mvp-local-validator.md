# AI log — MVP local validator

Date: 2026-07-08

Branch: `mvp-local-validator-310`

Status: local/manual validator implementation; no CI.

## Purpose

Implement the first report-only local validator and commit generated reports for the positive and deliberate failing fixtures.

## Added files

```text
scripts/validate_mvp_fixture.py
docs/governance/examples/mvp_vertical_fixture/generated_reports/README.md
docs/governance/examples/mvp_vertical_fixture/generated_reports/fixture.schema_targets.generated_report.yaml
docs/governance/examples/mvp_vertical_fixture/generated_reports/failing_external_action.generated_report.yaml
```

## Updated files

```text
docs/governance/examples/mvp_vertical_fixture/PREVALIDATOR_READINESS.md
```

## Validator behavior

The local validator reports three layers separately:

```text
schema validation
reference validation
governance invariant validation
```

Positive fixture outcome:

```text
status: reviewable
schema_status: pass
reference_status: pass_with_warnings
governance_status: pass_with_warnings
```

Deliberate failing fixture outcome:

```text
status: blocked
schema_status: pass
reference_status: pass
governance_status: fail
```

## Boundary

No CI was added.
No runtime was added.
No database mapping was added.
No OpenWebUI feature was added.
No Hermes contract was added.
No approval engine was added.
No memory promotion was added.
No external action authorization was added.

## Dependencies

The script expects local Python packages:

```text
PyYAML
jsonschema
```

No global dependency file was modified and no automatic installation was added.

## Preserved distinctions

```text
schema_valid != approved
source_ref != evidence
retrieval_trace != proof
reference_valid != truth
governance_invariant_pass != external_action_authorization
validator_success != runtime_success
```
