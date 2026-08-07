# Retrieval coverage verified state

Date: 2026-08-07

## Objective

Correct the existing source/retrieval implementation inventory from verified repository state without replacing it with a smaller parallel summary.

## Repositories observed

```text
Pantheon-Next main: fde7e856cd04c56e718d2bb133e65262c80d5d52
pantheon-mvp main: 666bd32301f5ffd247756f4a859bf1667d884fb6
```

The MVP commit is the squash merge of PR #256 after successful Pantheon Architecture Audit and Pantheon MVP CI.

## Prior attempt

PR #566 correctly identified stale lexical and hybrid coverage, but its first document rewrite reduced a curated long governance file by 36 percent. The no-net-truncation guard rejected it. The branch was later reset during parallel repository work and the PR closed without fusion.

That result is not reused as validation.

## Corrective approach

Preserve the complete ten-section inventory and update only the stale implementation claims:

```text
PostgreSQL lexical retrieval           implemented candidate
weighted deterministic RRF             implemented candidate
hybrid runner integration              implemented candidate
bounded métier acceptance set          implemented candidate
production semantic embedding binding  not established
independent reranking binding           not established
Hermes search handoff                   not implemented
```

The active embedder remains deterministic local feature hashing. It proves a replaceable vector path and zero-exposure seam, not production semantic quality.

## Merged métier evidence

`pantheon-mvp` PR #256 adds:

```text
six exact métier queries with explicit source-rank expectations;
two observation-only cases for accentless French and semantic paraphrase;
Task Contract source and dossier marker attacks;
contract, ingestion and source provenance checks;
duplicate refusal and repeated-order determinism checks.
```

## Hermes posture

The owner remains the existing `knowledge_retrieval_pipeline` Capability Slot.

```text
current qualified laboratory tools:
- pantheon_context_manifest
- pantheon_context_entity

real agency/NAS acceptance:
- still open in pantheon-mvp issue #227

future candidate after acceptance:
- pantheon_context_search
```

Hermes may orchestrate the admitted retrieval call. `pantheon-mvp` and PostgreSQL remain responsible for storage, retrieval and ranking. Pantheon remains responsible for scope, lifecycle and gates.

## External references

```text
pgvector / pgvector-python  implementation reference
Vespa rag-blueprint         evaluation-method reference
ranx / ir_measures          optional development-only metrics
ParadeDB                     watch candidate on measured PostgreSQL limits
```

No external engine, embedding provider, reranker or evaluation package is adopted.

## Boundaries

```text
implemented vector path != semantic quality
retrieved != Evidence
hybrid score != confidence
benchmark passed != production adoption
Hermes execution != Pantheon decision
search tool exposed != task authorized
```

No schema, runtime, MCP implementation, Hermes profile, database migration, dependency, activation, Evidence admission, memory promotion or automatic approval is changed.
