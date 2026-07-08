# 2026-07-08 — Resolved MVP fixture guard repair

## Intervention

Re-applied the useful repairs from PR #311 on a fresh branch from current `main`, after #311 became unmergeable due to conflicts with the local validator work merged in #310.

## Repairs

- Normalized MVP fixture note `Status:` headers to accepted support-note families.
- Normalized the generated reports README status header.
- Added coverage rows to `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md` for `POSTGRES_PROPERTY_GRAPH_CAPABILITY.md` and the grouped MVP vertical fixture directory.
- Aligned the narrative `fixture.yaml` object keys from `object` / `id` to `object_type` / `object_id` while preserving the narrative fixture design.
- Added `x-boundary` metadata and `governance_refs.default` to `schemas/mvp_governed_loop_objects.schema.yaml` without changing validation fields, enums or `additionalProperties`.
- Added `schemas/examples/mvp_governed_loop_objects.example.yaml`.
- Wired the MVP schema example into existing schema tests.

## Boundary

No runtime was added.
No OpenWebUI feature was added.
No Hermes contract was added.
No approval engine was added.
No memory promotion was added.
No provider routing, scheduler, queue or external action authorization was added.
No schema field was added, removed or renamed.
No `additionalProperties` hardening was introduced.

## Cause of earlier failures

The MVP vertical content was doctrinally coherent, but previous merges did not check the repository's mechanical governance guards before merging: accepted `Status:` vocabulary, authority index coverage, schema examples and schema test registration.

## Corrective discipline

Future MVP/documentation PRs should check, before merge:

```text
Status header vocabulary
Authority index coverage
Schema example coverage when schemas/ is touched
Test registration when schema candidates are added
No runtime phrase or boundary violation
```
