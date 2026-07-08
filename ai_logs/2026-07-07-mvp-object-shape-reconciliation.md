# AI log — MVP object shape reconciliation

Date: 2026-07-07

Branch: `mvp-object-shape-reconciliation`

Status: documentation-only reconciliation note.

## Purpose

Compare the MVP vertical fixture with the earlier illustrative object examples before creating schemas.

## Decision

Do not create schemas yet.

Record the preferred future direction:

```yaml
object_type: task_contract
object_id: mvp.devis-reprise.tc-001
```

Object-specific aliases may remain in examples during transition:

```yaml
contract_id: mvp.devis-reprise.tc-001
object_id: mvp.devis-reprise.tc-001
```

## Boundary

No schema was created.
No enum was frozen.
No database table mapping was introduced.
No runtime was added.
No OpenWebUI feature was added.
No Hermes contract was added.
No validation test was added.

## Preserved distinctions

```text
retrieved != truth
runtime_success != approval
approved_draft != external_send_authorization
register_candidate != admitted memory
```
