# Scoped hybrid retrieval tranche

Date: 2026-08-03

## Change

Add a bounded PostgreSQL lexical retrieval path and deterministic weighted reciprocal-rank fusion over the existing scope-first semantic retrieval.

## Boundary

```text
lexical match != truth
hybrid score != Evidence quality
retrieved != approved
implemented candidate != adopted binding
```

Every database query applies the Task Contract dossier and declared-source perimeter before ranking. No provider, reranker, runtime router, memory engine, Evidence admission or approval behavior is introduced.

## Status

Implemented candidate in `pantheon-mvp`; not adopted or activated.
