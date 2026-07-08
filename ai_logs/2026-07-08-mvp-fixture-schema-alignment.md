# AI log — MVP fixture schema alignment

Date: 2026-07-08

Branch: `mvp-alignment-304`

Status: documentation-only alignment step.

## Purpose

Align the MVP vertical fixture with the candidate schema bundle without adding a validator, CI check or runtime.

## Files

```text
docs/governance/examples/mvp_vertical_fixture/fixture.schema_targets.yaml
docs/governance/examples/mvp_vertical_fixture/SCHEMA_ALIGNMENT.md
```

## Decision

The normalized schema-target fixture includes only the five central object types:

```text
task_contract
result_candidate
evidence_pack_candidate
decision_record
register_candidate
```

`source_manifest` and `retrieval_trace` remain support objects until an implementation-facing pass decides whether they are standalone records or embedded Evidence Pack sections.

## Boundary

No validator was added.
No CI was changed.
No runtime was added.
No database mapping was added.
No OpenWebUI feature was added.
No Hermes contract was added.
No approval engine or memory promotion was added.

## Known gaps preserved deliberately

```text
status strings remain loose
alias equality is not enforced
cross-object references are not checked
additionalProperties: true remains deliberate
```

Next recommended step: a manual/local validation plan, not CI.
