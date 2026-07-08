# AI log — MVP prevalidator consolidation

Date: 2026-07-08

Branch: `mvp-prevalidator-consolidation-309`

Status: documentation-only prevalidator consolidation.

## Purpose

Close the Source Manifest / Retrieval Trace placement question and define local validator behavior before any implementation.

## Added files

```text
docs/governance/examples/mvp_vertical_fixture/SOURCE_RETRIEVAL_PLACEMENT.md
docs/governance/examples/mvp_vertical_fixture/LOCAL_VALIDATOR_DESIGN.md
docs/governance/examples/mvp_vertical_fixture/PREVALIDATOR_READINESS.md
```

## Decision

`source_manifest` and `retrieval_trace` are not central governed object schemas in the MVP loop.

```text
Source Manifest -> support scope register embedded or linked from Task Contract, optionally echoed in Evidence Pack metadata.
Retrieval Trace -> support audit trail embedded or referenced from Evidence Pack items.
```

## Validator design

Future local validator should run three separate layers:

```text
schema validation
reference validation
governance invariant validation
```

It should be local/manual and report-only.

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
source_ref != evidence
retrieval_trace != proof
reference_valid != truth
governance_invariant_pass != external_action_authorization
validator_success != runtime_success
```
