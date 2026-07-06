# PostgreSQL Property Graph Capability

Date: 2026-07-06

Status: documented non-implemented

Type: candidate support doctrine

## Summary

Added a candidate capability note for PostgreSQL Property Graph as an optional read layer over Pantheon governance relationships.

The note classifies PostgreSQL 19 SQL/PGQ Property Graph as a possible future read capability, not as a central dependency, runtime, graph engine, schema migration or install instruction.

## Files changed

- `docs/governance/POSTGRES_PROPERTY_GRAPH_CAPABILITY.md`
- `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`
- `docs/governance/WHAT_RUNS.md`
- `ai_logs/2026-07-06-postgres-property-graph-capability.md`

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Boundary

The capability remains:

- optional;
- documented non-implemented;
- disabled by default;
- outside runtime behavior;
- outside schema migration;
- outside approval automation;
- outside memory promotion;
- outside Hermes execution.

## Key distinctions

```text
relation_detected ≠ evidence
runtime_success ≠ evidence
installed ≠ approved
healthy ≠ safe
update_available ≠ update_authorized
binding_selected ≠ dependency_adopted
```

## Decision

Do not adopt PostgreSQL Property Graph as core dependency.

Do not replace the relational governance model.

Record it as a candidate read-layer capability with SQL views, joins, recursive CTEs, adjacency tables and JSON exports as fallbacks.

Any future activation requires explicit human review, PostgreSQL version verification, schema review, migration compatibility review and performance review.
