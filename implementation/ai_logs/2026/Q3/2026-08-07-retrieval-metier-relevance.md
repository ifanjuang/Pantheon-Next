# Retrieval métier relevance cases

Date: 2026-08-07

## Objective

Add the smallest executable relevance set for the existing PostgreSQL lexical/vector retrieval candidate without selecting a new engine, embedding provider, reranker or evaluation framework.

## Repository state

```text
base: pantheon-mvp main
base commit: 3195adf3131d30494348552c4dacba312eb7fc03
```

No open MVP pull request overlapped the selected paths.

## Existing owners reused

```text
mvp_vertical/store.py       scope-first pgvector retrieval
mvp_vertical/retrieval.py   PostgreSQL lexical retrieval and weighted RRF
tests/test_block1.py        governed loop and perimeter acceptance
tests/test_hybrid_retrieval.py  fusion-unit behaviour
```

The new tests do not duplicate the RRF formula tests. They execute the real PostgreSQL paths against the existing synthetic `devis_reprise` dossier.

## Added cases

Six exact métier queries have explicit expected sources and rank ceilings:

```text
client deadline;
quote payment condition;
membrane system;
pare-vapeur;
contract-change decision;
contradictory degradation observation.
```

Two additional cases are observation-only:

```text
accentless French technical query;
semantic paraphrase against the deterministic feature-hashing placeholder.
```

Observation-only means the hard boundaries are tested while no production semantic-quality claim is invented.

## Hard invariants

Every case verifies:

```text
Task Contract source perimeter;
contract, ingestion and source provenance;
no duplicate fused result;
deterministic repeated ordering.
```

A separate test plants an exact rare marker:

```text
same dossier + undeclared source;
other dossier + declared source_ref.
```

Neither lexical nor hybrid retrieval may return the planted material.

## Boundary

```text
vector path implemented != semantic quality established
fixture rank passed != production relevance accepted
retrieved != Evidence
hybrid score != confidence
benchmark case != production authorization
```

No runtime code, SQL migration, index, embedding implementation, retrieval weight, dependency, Hermes tool, MCP surface, Evidence admission, memory promotion or automatic approval is changed.

## Verification posture

The test module requires the existing pgvector integration lane. A local network checkout was unavailable in the execution environment, so no local PostgreSQL result is claimed. GitHub CI on the exact branch head remains the authoritative execution check.
