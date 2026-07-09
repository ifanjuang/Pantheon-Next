# 2026-07-09 — Governed Resource Dashboard model

Status: validation-only trace.

Boundary profile: validation_only_trace.

## What changed

Added `docs/governance/GOVERNED_RESOURCE_DASHBOARD_MODEL.md` as candidate support doctrine.

Updated `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md` to index the new document under runtime-adapter support material.

## Why

The repository discussion converged on a simpler dashboard model:

```text
User-facing surface:
  Resource Card

Internal model:
  strictly typed governed resource
```

This keeps the beginner-facing dashboard simple while preserving distinctions between infrastructure modules, runtimes, runtime surfaces, AI runtime nodes, models, bindings, policies, exposures, prompt surfaces, data stores and credential references.

## Scope

The new document is documentation only.

It defines:

```text
Resource Card simplification
internal resource types
lifecycle states
chronological phases
dependency rule
adapter families
gate classes
non-equivalence rules
OpenWebUI placement
Hermes placement
AI runtime node placement
forbidden interpretations
```

## Boundary

This intervention does not implement a dashboard, installer, registry, plugin marketplace, provider router, scheduler, queue, model marketplace, runtime orchestrator, approval engine, memory engine, connector gateway or secret store.

It does not create Docker, Portainer, OpenWebUI, Hermes, PostgreSQL, Ollama, reverse-proxy or protected-path artifacts.

## Known limitation

An attempted update to `docs/governance/WHAT_RUNS.md` was blocked by the tool safety layer while rewriting the full file content. The new document was still indexed in `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`, which is the authority coverage location for runtime-adapter candidate documents.

A follow-up can add a WHAT_RUNS status row if the write path is available.

## Risk notes

The main risk is over-simplification: Resource Card must remain a user-facing simplification only. It must not erase internal resource typing.

The second risk is product drift: a governed resource dashboard must not become a plugin manager, installer, provider router or automatic approval engine.

## Status classification

```text
implemented:
  none.

documented non-implemented:
  governed resource dashboard model.

partial:
  runtime-adapter index coverage added.

to verify:
  future UI, schemas, adapters, state storage, health checks and external runtime behavior.
```
