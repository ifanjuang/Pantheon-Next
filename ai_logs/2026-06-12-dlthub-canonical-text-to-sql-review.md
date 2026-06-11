# AI log — dltHub canonical Text-to-SQL review

Date: 2026-06-12

## Change

Added an external reference review for dltHub's canonical Text-to-SQL article:

```text
docs/governance/reference_reviews/DLTHUB_CANONICAL_TEXT_TO_SQL.md
```

Updated the external reference review index:

```text
docs/governance/reference_reviews/README.md
```

## Why

The article provides useful vocabulary for a Pantheon-compatible pattern:

```text
definition before answer
scope before retrieval
meaning before query
lineage before trust
status before delivery
```

The review distills this as `canonical governance mapping`, not as a new canonical doctrine file.

## Classification

```text
Authority: support review only / external reference distillation
Repo state: documented non-implemented
Decision Zeus: À vérifier
Implementation status: non applicable
```

## Accepted

The reference is useful as support vocabulary for definitions-first, taxonomy-bounded and lineage-aware reasoning.

It can inform future MCP Policy Server fixtures and data-platform review questions.

## Refused

The change does not import or approve:

```text
Text-to-SQL execution
SQL generation
data-platform implementation
warehouse implementation
schema generation
ontology execution
GraphRAG runtime
connector adoption
protected-path changes
```

## Risks and limitations

The phrase `canonical governance mapping` is candidate vocabulary only. It must not silently create a new doctrine layer or duplicate `CORE_CONCEPTS_MAP.md` and `KNOWLEDGE_TAXONOMY.md`.

The review does not modify MCP implementation work, the data-platform candidate documents, schemas, tests, operations, platform files, Docker or `.env`.

## Diff discipline

Expected touched paths:

```text
docs/governance/reference_reviews/DLTHUB_CANONICAL_TEXT_TO_SQL.md
docs/governance/reference_reviews/README.md
ai_logs/2026-06-12-dlthub-canonical-text-to-sql-review.md
```
