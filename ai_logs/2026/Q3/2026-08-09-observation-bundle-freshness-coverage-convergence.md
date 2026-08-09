# Observation Bundle freshness and coverage convergence

Date: 2026-08-09

Status: validation-only trace — executable candidate contract.
Boundary profile: validation_only_trace.

## Change

- Added one responsibility-named `observation_bundle` candidate schema and a
  fictional executable example.
- Reused the active `source_representation`, `attribute_claim` and
  `relation_claim` schemas rather than copying their primitives.
- Defined `scope` as the requested boundary and `coverage.observed_scope` as the
  actual observation boundary, with closed completeness and absence-safety
  postures.
- Converged Revit documentation on independent document, view and selection
  execution freshness while retaining document freshness as the sole Project
  Anatomy source-observation token.
- Added positive and negative fixtures for partial coverage, unresolved identity,
  contradictions, candidate identity, operational gaps and zero authority.

## Why

The first Revit adapter consumer exposed two contract gaps: the conceptual
Observation Bundle had no executable validation shape, and older documents still
described one composite context token. Leaving those gaps would force the adapter
to invent field names, coverage semantics and authority posture locally.

The schema is the smallest existing-responsibility extension that closes the
exchange seam without introducing a fifth Project Anatomy primitive or another
owner.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: yes — schemas, governance documentation and tests.
Runtime impact: none in Pantheon Next; the schema validates candidate payloads only.
Authority impact: all bundle authority flags are fixed to false.
Persistence impact: none; execution-result persistence remains owned by
`pantheon-mvp`.
External adapter impact: DTOs must serialize the executable snake-case contract;
their compilation and live Revit behavior remain separately validated.
Evidence and memory behavior: none.

## Local distinctions

```text
scope requested != coverage observed
complete for declared scope != complete project
partial or unknown coverage != absence
document freshness != view freshness != selection freshness
valid bundle != APU write
runtime success != Evidence
```
