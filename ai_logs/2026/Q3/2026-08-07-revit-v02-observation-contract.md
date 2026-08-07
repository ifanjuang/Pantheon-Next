# AI log — Revit 2027 / Project Anatomy V0.2 observation contract

Date: 2026-08-07

## Scope

Critical reread of the stabilized Project Anatomy V0.2 design before continuing the Revit adapter.

This pass does not alter the frozen V0.2 core schemas and does not implement a runtime.

## Repo state observed

Project Anatomy V0.2 is now conceptually stabilized around:

```text
stable_object
source_representation
attribute_claim
relation_claim
```

The earlier duplicate carriers are compatibility/history concerns rather than active V0.2 design primitives.

The current Revit tree remains a non-executable reference skeleton. The repository explicitly requires production add-in and Host Agent code to live in a dedicated implementation repository.

The pantheon-mvp H4c migration PR is materially implemented but was observed failing the architecture convergence guard because active implementation/test filenames still contain generation naming (`v02`). A bounded review comment was added to that PR; no semantic change was made from this branch.

OpenTakeoff distillation remains in separate draft PR #579 and is not folded into this slice.

## Decisions recorded

1. Do not reopen the frozen Project Anatomy V0.2 core for the Revit adapter.
2. Make the Revit seam source-representation-first.
3. The add-in may observe Revit native identity but must not create Pantheon stable identity automatically.
4. Revit observations should be expressible as source representations plus attribute/relation claim candidates.
5. `identity.represents` remains a governed relation from `source_representation` to `stable_object`, not an add-in fact.
6. High-density Revit exchange should be delta-first and must report coverage before absence can be inferred.
7. Preserve `withheld`, `blocked`, `refused`, `failed` and `rolled_back` as distinct operational outcomes.
8. Target Revit 2027; expected .NET 10/Windows target remains implementation metadata to verify live.
9. The Operation Registry remains closed and must feed capability/tool/documentation/conformance surfaces rather than allowing API reflection.
10. Human UI and Hermes must call the same deterministic Revit operation implementation.
11. Revit internal units must not leak into the Pantheon/Hermes contract.
12. No external MCP repository is adopted as runtime by this pass.

## Files added/updated

- `revit-plugin/docs/PROJECT_ANATOMY_V02_OBSERVATION_CONTRACT.md`
- `revit-plugin/README.md`
- this log

## Explicitly not changed

- `schemas/`
- `tests/`
- `pyproject.toml`
- `operations/`
- `platform/`
- Docker files
- `.env*`
- `.github/scripts/`
- `CLAUDE.md`
- Project Anatomy frozen core
- pantheon-mvp executable owner
- OpenTakeoff draft PR #579

## Status

Documented:

- Revit 2027 adapter output seam aligned with Project Anatomy V0.2;
- Observation Bundle conceptual shape;
- delta/coverage/gap semantics;
- operation registry and conformance expectations.

Not implemented:

- production Revit repository;
- compiling Revit 2027 add-in;
- Host Agent;
- executable Observation Bundle schema;
- Operation Registry code;
- live Revit 2027 conformance tests;
- adapter ingestion into pantheon-mvp.

No documented item above should be reported as implemented.
