# AI Log — Architectural pattern reference boundary

Date: 2026-05-31

## Scope

Added a narrow boundary note to `docs/governance/CAPABILITY_PLACEMENT.md` after reviewing the relevance of external architectural pattern catalogues such as `denyspoltorak/metapatterns`.

Documentation only.

## Files changed

- `docs/governance/CAPABILITY_PLACEMENT.md`:
  - added `Architectural pattern references` section;
  - clarified that external pattern catalogues are vocabulary aids, not Pantheon doctrine;
  - stated that naming a pattern does not authorize Pantheon to implement it;
  - placed execution-heavy forces such as orchestration, microkernel, plugin systems, middleware, pipelines, gateways, shared repositories, event flows, observability layers and provenance graphs outside Pantheon when they imply runtime behavior or external effect;
  - kept Pantheon responsible only for the governing boundary through Task Contracts, manifests, roles, evidence, statuses, approvals, memory rules and action boundaries.

## Why

The repository already contains strong capability-placement doctrine. The risk was not a missing architecture framework, but vocabulary drift: an assistant could treat a software architecture pattern catalogue as authority to turn Pantheon into an orchestrator, microkernel, plugin manager or middleware layer.

The added note keeps such references useful for naming placement risks without promoting them to doctrine.

## Governance boundary

This change does not add a runtime, bridge, queue, scheduler, provider router, plugin manager, module loader, middleware, microkernel, execution graph, observability backend, provenance graph, automatic approval or automatic memory promotion.

It does not make `metapatterns` a dependency, canonical source or governing document.

## Boundary phrase

```text
Use pattern catalogues to name forces.
Do not let them authorize execution inside Pantheon.
Pantheon governs the boundary, not the runtime pattern.
```
