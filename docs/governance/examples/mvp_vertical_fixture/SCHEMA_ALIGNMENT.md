# MVP Fixture / Schema Alignment

Status: alignment note — documented non-implemented.

Date: 2026-07-08

This note compares the original vertical fixture with the candidate schema bundle introduced in `schemas/mvp_governed_loop_objects.schema.yaml`.

It adds no validator, test, CI, runtime, database mapping, OpenWebUI feature, Hermes contract, approval engine or memory promotion.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Files

```text
docs/governance/examples/mvp_vertical_fixture/fixture.yaml
docs/governance/examples/mvp_vertical_fixture/fixture.schema_targets.yaml
schemas/mvp_governed_loop_objects.schema.yaml
```

## Result

`fixture.schema_targets.yaml` is a normalized schema-target subset of the original fixture.

It uses the hybrid object shape from `OBJECT_SHAPE_RECONCILIATION.md`:

```yaml
object_type: task_contract
object_id: mvp.devis-reprise.tc-001
contract_id: mvp.devis-reprise.tc-001
```

## Central objects aligned

The following original fixture objects now have schema-target forms:

```text
task_contract
result_candidate
evidence_pack_candidate
decision_record
register_candidate
```

The sequence remains intact:

```text
task_contract
→ result_candidate risky draft
→ evidence_pack_candidate
→ decision_record request_revision
→ result_candidate revised draft
→ decision_record approve_for_internal_draft
→ register_candidate pending admission
```

## Intentional exclusions

The original fixture also contains:

```text
source_manifest
retrieval_trace
```

These remain support objects and are not schema targets yet.

Reason: the implementation-facing pass still needs to decide whether they are standalone records or embedded sections of the Evidence Pack.

Current recommendation:

```text
Source Manifest -> likely embedded or linked from Task Contract / Evidence Pack.
Retrieval Trace -> likely embedded in Evidence Pack items, not a first-class governed record yet.
```

## Alignment gaps still open

### 1. No actual validator

The schema exists, but no validation command, CI check or fixture test has been added.

This PR only creates a human-readable alignment target.

### 2. Status strings remain loose

The schema still accepts any string status. This avoids premature enum freezing, but it does not yet protect the workflow.

### 3. ID equality is not enforced

The schema allows both:

```yaml
object_id: mvp.devis-reprise.tc-001
contract_id: mvp.devis-reprise.tc-001
```

It does not enforce equality between the two. That check should remain a later validation rule, not a schema trick.

### 4. Cross-object references are not checked

The schema can require `applies_to`, `revision_of`, `related_evidence_pack` or `created_because_of`, but it does not prove that the referenced object exists.

This requires a lightweight graph/reference validator later.

### 5. `additionalProperties: true` remains deliberate

The schema is permissive by design while shapes are still settling.

Do not harden it until the first validation pass has produced concrete failures.

## Preserved boundaries

```text
schema_target != validated run
fixture != runtime
retrieved != truth
runtime_success != approval
internal_draft_approval != external_send_authorization
register_candidate != admitted memory
```

## Next recommended step

The next step should be a local/manual validation plan, not CI yet:

```text
#305 — MVP fixture validation plan
```

That PR should define how to parse the multi-document YAML, validate each schema-target document against the candidate schema, and separately check reference integrity. It should still add no runtime behavior.
