# Hermes hybrid retrieval convergence

Date: 2026-08-07

## Objective

Reconcile the existing source/retrieval inventory with current `pantheon-mvp` code without adding a capability, runtime, schema or activated Hermes tool.

## Observed state

```text
Pantheon-Next: fde7e856cd04c56e718d2bb133e65262c80d5d52
pantheon-mvp: 3195adf3131d30494348552c4dacba312eb7fc03
```

The MVP already contains scope-first pgvector retrieval, PostgreSQL full-text retrieval, deterministic weighted RRF, separate branch ranks, runner integration and source-linked provenance.

The active vector embedder remains a deterministic offline placeholder. The vector path is implemented; production semantic quality is not established.

## Decision

Preserve the historical inventory and append a dated reconciliation. Keep `knowledge_retrieval_pipeline` as the existing owner.

The Hermes laboratory baseline currently exposes only:

```text
pantheon_context_manifest
pantheon_context_entity
```

The real agency/NAS acceptance remains open in MVP issue #227. `pantheon_context_search` is staged only after that two-tool baseline is accepted and requalified.

## Next step

Add a small labelled métier relevance set in `pantheon-mvp`. Correct only defects demonstrated by those cases. Do not select a reranker, external engine or production embedding binding from this documentation change.

## Boundaries

```text
implemented vector path != semantic quality
retrieved != Evidence
hybrid score != truth
search tool exposed != task authorized
benchmark passed != production adoption
```

No runtime, MCP implementation, Hermes profile, database migration, dependency, installation, activation, Evidence admission, memory promotion or automatic approval is changed.
