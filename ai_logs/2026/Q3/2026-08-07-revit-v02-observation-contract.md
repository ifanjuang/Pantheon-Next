# AI log — Revit 2027 / Project Anatomy V0.2 observation contract

Date: 2026-08-07

## Scope

Critical reread of the stabilized Project Anatomy V0.2 design before continuing the Revit adapter, followed by a focused implementation-foundation review of Nice3point/RevitTemplates, Nice3point/RevitApi and DTDucas/RevitMCPSDK.

This pass does not alter the frozen V0.2 core schemas and does not implement a runtime.

## Repo state observed

Project Anatomy V0.2 is conceptually stabilized around:

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

No dedicated Pantheon/Revit production implementation repository was found among the connected GitHub repositories during this pass.

## Project Anatomy decisions recorded

1. Do not reopen the frozen Project Anatomy V0.2 core for the Revit adapter.
2. Make the Revit seam source-representation-first.
3. The add-in may observe Revit native identity but must not create Pantheon stable identity automatically.
4. Revit observations should be expressible as source representations plus attribute/relation claim candidates.
5. `identity.represents` remains a governed relation from `source_representation` to `stable_object`, not an add-in fact.
6. High-density Revit exchange should be delta-first and must report coverage before absence can be inferred.
7. Preserve `withheld`, `blocked`, `refused`, `failed`, `cancelled` and `rolled_back` as distinct operational outcomes.
8. Revit internal units must not leak into the Pantheon/Hermes contract.

## Revit 2027 implementation-foundation decisions

1. Target Revit 2027 first; expected runtime target is .NET 10/Windows and remains subject to live Revit 2027 verification.
2. Use `Nice3point.Revit.Sdk` as the preferred scaffold/build mechanism because it already handles Revit-version-aware target frameworks, R27/.NET 10 mapping, manifest patching, deployment/publishing and modern dependency isolation patterns.
3. Treat `Nice3point.Revit.Api.RevitAPI` / `RevitAPIUI` as build-reference candidates only after exact version pinning, offline mirroring/SBOM and a separate Autodesk redistribution/licensing review.
4. Do not make `RevitMCPSDK` the V0 execution kernel. Its command registry and `IRevitCommand` are useful references but do not carry Pantheon operation metadata, scope, freshness, preflight, authorization, transaction, result or conformance policies.
5. Do not inherit `ExternalEventCommandBase` synchronously as the Pantheon request lifecycle. Pantheon needs request-bound reset/correlation, stale-result protection, explicit busy behavior and cleanup guarantees.
6. Implement a small Pantheon-owned `OperationRegistry` and request-bound `ExternalEvent` dispatcher.
7. Keep one Revit API operation in flight in V0; no persistent queue, scheduler or automatic retry in the add-in.
8. Use a local out-of-process Host Agent as Named Pipe server and the Revit add-in as Named Pipe client.
9. Keep MCP/protocol translation outside Revit; the in-process domain layer uses strongly typed .NET requests/results rather than `JObject`.
10. Human UI and Hermes use the same deterministic operation implementation.
11. Prefer modern Revit 2027 dependency isolation over assembly repacking unless a tested compatibility case requires otherwise.
12. Require live Revit 2027 conformance before a capability can be called `supported`.

## Proposed first executable registry slice

```text
revit.system.observe_runtime.v1
revit.document.observe_context.v1
revit.view.observe_active.v1
revit.selection.observe.v1
revit.architecture.observe_rooms.v1
revit.architecture.observe_doors.v1
```

No write operation is required for the first proof.

## Files added/updated

- `revit-plugin/docs/PROJECT_ANATOMY_V02_OBSERVATION_CONTRACT.md`
- `revit-plugin/docs/IMPLEMENTATION_FOUNDATION_2027.md`
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

## External repository status used in this decision

Verified as external reference, not Pantheon implementation:

```text
Nice3point/RevitTemplates
- R27 project/build patterns
- Revit 2027 maps to .NET 10 in its current MSBuild SDK documentation
- test templates include live Revit-oriented patterns

Nice3point/RevitApi
- packages original Revit installation API libraries by version for build convenience

DTDucas/RevitMCPSDK
- MIT-licensed basic command/registry/ExternalEvent abstractions
- explicit R27/net10 target in the current project
- direct dependency not approved for Pantheon V0
```

## Status

Documented:

- Revit 2027 adapter output seam aligned with Project Anatomy V0.2;
- Observation Bundle conceptual shape;
- delta/coverage/gap semantics;
- closed operation registry and conformance expectations;
- production-repository responsibility layout;
- dependency posture;
- Named Pipe direction;
- request-bound ExternalEvent lifecycle requirements;
- first read-only registry slice.

Documented non-implemented:

- production Revit repository;
- compiling Revit 2027 add-in;
- Host Agent;
- executable Observation Bundle schema;
- Operation Registry code;
- request-bound ExternalEvent dispatcher;
- live Revit 2027 conformance tests;
- adapter ingestion into pantheon-mvp;
- model mutations.

No documented item above should be reported as implemented.
