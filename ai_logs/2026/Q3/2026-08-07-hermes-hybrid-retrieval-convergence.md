# Hermes hybrid retrieval convergence

Date: 2026-08-07

## Objective

Reconcile the existing source/retrieval inventory with current `pantheon-mvp` code without adding a capability, runtime, schema or activated Hermes tool.

## Observed state

```text
Pantheon-Next base: fde7e856cd04c56e718d2bb133e65262c80d5d52
pantheon-mvp retrieval evaluation: 666bd32301f5ffd247756f4a859bf1667d884fb6
```

The MVP contains scope-first pgvector retrieval, PostgreSQL full-text retrieval, deterministic weighted RRF, separate branch ranks, runner integration and source-linked provenance.

The active vector embedder remains a deterministic offline placeholder. The vector path is implemented; production semantic quality is not established.

## Evaluation result

The bounded métier relevance set was merged through `pantheon-mvp` PR #256. GitHub CI used PostgreSQL 16 with pgvector and reported:

```text
Pantheon MVP CI: success
Pantheon Architecture Audit: success
full suite: 1250 passed, 5 skipped, 1 warning
new retrieval métier cases: all passed
```

The merged cases verify exact technical retrieval, deterministic hybrid ordering, provenance retention, duplicate-free fusion and rejection of planted undeclared-source and other-dossier markers. Accentless French and semantic paraphrase remain observations, not production guarantees.

## Decision

Preserve the historical inventory and append a dated reconciliation. Keep `knowledge_retrieval_pipeline` as the existing owner.

No engine correction is justified by this first bounded set. The measured result closes the immediate lexical/RRF verification step; it does not select a production embedding model or prove general semantic quality.

The Hermes laboratory baseline currently exposes only:

```text
pantheon_context_manifest
pantheon_context_entity
```

The real agency/NAS acceptance remains open in MVP issue #227. `pantheon_context_search` is staged only after that two-tool baseline is accepted and requalified.

## Remaining sequence

```text
preserve the current retrieval baseline;
record a concrete defect before changing ranking or lexical configuration;
complete Hermes agency/NAS acceptance #227;
then specify and qualify pantheon_context_search as a bounded third tool;
evaluate production embeddings, reranking or another PostgreSQL extension only on measured need.
```

## Boundaries

```text
implemented vector path != semantic quality
retrieved != Evidence
hybrid score != truth
search tool exposed != task authorized
benchmark passed != production adoption
```

No runtime, MCP implementation, Hermes profile, database migration, dependency, installation, activation, Evidence admission, memory promotion or automatic approval is changed.
