# OpenTakeoff / drawing takeoff specialization on APU V0.2

Date: 2026-08-08

## Objective

Re-port the still-useful drawing-takeoff and Revit engineering-conformance work from superseded draft PR #579 onto the current Project Anatomy V0.2 adapter chokepoint without restoring stale V0.1 output semantics.

## Repo state checked

- generic APU adapter chokepoint converged on Project Anatomy V0.2 via #591;
- Revit V0.2 observation seam merged via #589;
- pantheon-mvp executable V0.2 owner migration merged via #267;
- draft #579 was 19 commits behind current `main`, not mergeable, and still edited the parent adapter contract from a V0.1 output model;
- #579 was therefore closed as superseded rather than merged.

## Re-ported material

- `docs/domain-packs/architecture/DRAWING_TAKEOFF_LOCAL_ADAPTER.md`;
- `revit-plugin/docs/ENGINEERING_CONFORMANCE.md`;
- minimal parent/README pointers required for discoverability.

The two specialization documents remain documented non-implemented and subordinate to the existing governance owners.

## V0.2 convergence

For APU source adapters:

```text
Task Contract + bounded source/context
-> external adapter
-> Observation Bundle Candidate
 + Evidence Pack Candidate
```

Drawing takeoff is a sibling source binding to Revit/IFC, not another Project Anatomy owner.

```text
PDF geometry != Revit geometry
OpenTakeoff shape id != stable_object_id
quantity computed != quantity accepted
marked plan exported != document published
engine review flag != Pantheon approval
```

The drawing-takeoff specialization does not emit deprecated V0.1 canonical carriers and does not create durable stable identity.

## OpenTakeoff posture

OpenTakeoff remains an optional external implementation candidate for later bounded local evaluation.

This change does not:

- adopt or install OpenTakeoff;
- select an exact production version;
- enable an MCP server;
- admit upstream tools as Pantheon capabilities;
- create an adapter runtime;
- accept any measured quantity;
- create Evidence, Proof, ProjectClaims or Decisions;
- add any Revit executable code.

Any later adoption slice must prove exact package identity, license review, offline reproducibility, closed capability mapping, metric normalization, source-path controls, parity/conformance, withheld/refusal propagation and removal without loss of Project Anatomy authority.

## Revit engineering patterns retained

`ENGINEERING_CONFORMANCE.md` keeps the reusable engineering checks distilled from external references:

- one closed operation registry;
- one deterministic implementation behind human/agent entry points;
- typed requests/results and explicit refusal/withheld outcomes;
- provenance for every meaningful operation;
- original machine proposal preserved before human correction;
- deterministic correction rules after review;
- human/agent parity tests;
- conformance suite and fixture corpus;
- safe file effects;
- no arbitrary-code/reflection execution surface.

These are engineering constraints only. They do not adopt OpenTakeoff or RevitMCPSDK as runtime dependencies.
