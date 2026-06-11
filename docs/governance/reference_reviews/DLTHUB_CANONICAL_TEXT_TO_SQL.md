# dltHub canonical Text-to-SQL review

Status: support review only — external reference distillation.

Reviewed on: 2026-06-12.

Source reviewed:

```text
https://dlthub.com/blog/canonical-text-to-sql
```

This review does not approve dltHub adoption, Text-to-SQL execution, SQL generation, data-model generation, a warehouse, an ontology engine, GraphRAG, a connector, a schema, tests or implementation work.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Reference claim

The source argues that Text-to-SQL fails less because the model cannot write SQL than because the model does not know what the data means. Its proposed fix is to write the definitions first as a canonical knowledge layer, then use that same spec to build the canonical model and to answer questions over it.

The useful structure is:

```text
canonical model
+ taxonomy
+ ontology
```

The taxonomy states what is in scope, what is out of scope and which concepts or metrics exist. The ontology states what the relationships mean, what a join computes, which population a count covers and which grain or window applies.

## Pantheon distillation

Pantheon should not import this as a Text-to-SQL feature.

The useful Pantheon pattern is narrower:

```text
definition before answer
scope before retrieval
meaning before query
lineage before trust
status before delivery
```

Pantheon already has the core separation in `CORE_CONCEPTS_MAP.md` and `KNOWLEDGE_TAXONOMY.md`. This review therefore does not propose a new canonical doctrine file named `CANONICAL_GOVERNANCE_LAYER.md`.

The relevant candidate phrase is:

```text
canonical governance mapping
```

It means mapping a user request or output candidate to a governed concept before treating it as answerable, provable, memorable or actionable.

## Accepted as reference distillation

```text
A consequential answer should be grounded in explicit definitions, not inferred from raw sources or table names.
A taxonomy can support refusal when a requested concept is undefined or out of scope.
An ontology can support review when a relationship, join, scope, grain or population changes the meaning of a result.
A checkable answer should carry its definitions, source path and lineage.
```

Pantheon translation:

```text
Raw Source / Knowledge Item
-> candidate concept mapping
-> Evidence Item or Evidence Pack Candidate
-> Output Candidate or Register Candidate
-> governed status
-> human decision where consequential
```

This is compatible with the existing authority ladder. It does not replace it.

## Refused imports

```text
Pantheon as Text-to-SQL engine.
Pantheon as warehouse or data platform.
Pantheon as schema generator.
Pantheon as ontology engine.
Pantheon as GraphRAG engine.
SQL that runs = truth.
Generated model = doctrine.
Taxonomy document = approval.
Ontology relation = proof by itself.
```

SQL, graph traversal, ontology checks, extraction and data modeling belong outside Pantheon unless a separately approved implementation artifact exists. Pantheon may govern their status, evidence, scope, memory and approval implications.

## MCP implication candidate

For the MCP Policy Server track, this suggests a future development fixture:

```text
ambiguous professional term
-> candidate concept mapping
-> scope / taxonomy check
-> relationship-meaning check
-> result candidate or refusal
```

Example ambiguity:

```text
validation
```

Potential governed concepts:

```text
technical validation
budget validation
regulatory validation
documentary validation
final human approval
action authorization
```

The fixture should test that the policy layer does not treat a shared word as a shared status.

## Data platform implication candidate

For the data-platform candidate layer, this review supports one review question:

```text
Which professional concepts must be defined as governed vocabulary, taxonomy and relationship meaning before any schema or table candidate can safely use them?
```

This does not authorize a schema, table, SQL model, Directus configuration, graph database or workflow. It only names a review pressure for future data-platform work.

## Decision record

Accepted:

```text
Use the reference as support vocabulary for definitions-first, refusal-first and lineage-first reasoning.
```

Refused:

```text
Do not import Text-to-SQL, data modeling, ontology execution or self-service analytics into Pantheon.
```

To verify:

```text
Whether MCP development fixtures should add canonical concept mapping for ambiguous professional vocabulary.
Whether data-platform review should require concept definitions before schema candidates.
```

To arbitrate:

```text
Whether future work needs a dedicated concept-map artifact, or whether `CORE_CONCEPTS_MAP.md` and `KNOWLEDGE_TAXONOMY.md` remain sufficient.
```

## Boundary phrase

```text
The source provides material.
The taxonomy bounds.
The ontology clarifies.
The evidence supports.
The status governs.
The human decides.
```
