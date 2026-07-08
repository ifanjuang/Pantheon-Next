# AI log — MVP minimal schema candidates

Date: 2026-07-08

Branch: `mvp-minimal-schema-candidates`

Status: candidate schema bundle.

## Purpose

Add a minimal JSON Schema/YAML bundle for the five central MVP governed loop objects.

## File

```text
schemas/mvp_governed_loop_objects.schema.yaml
```

## Covered object types

```text
task_contract
result_candidate
evidence_pack_candidate
decision_record
register_candidate
```

## Deliberate exclusions

Source Manifest and Retrieval Trace are not schemas yet. They remain fixture/support objects until the implementation-facing pass decides whether they are standalone records or embedded sections of an Evidence Pack.

## Shape decision

The candidate schema follows the reconciliation direction:

```yaml
object_type: task_contract
object_id: mvp.devis-reprise.tc-001
contract_id: mvp.devis-reprise.tc-001
```

`object_type/object_id` provides a uniform spine. Object-specific aliases remain allowed for readability during transition.

## Boundary

No runtime was added.
No validator was added.
No CI was changed.
No database mapping was added.
No OpenWebUI feature was added.
No Hermes contract was added.
No automatic approval or memory promotion was added.

The schema is permissive by design and uses `additionalProperties: true` while object shapes are still settling.
