# Hermes Knowledge Retrieval Binding

Status: candidate support doctrine — documented non-implemented.

## Purpose

Define a bounded candidate Capability Slot for retrieval over already-admitted or already-extracted governed material without coupling Pantheon to a specific retrieval framework.

This document does not install Haystack, LlamaIndex, LangChain or any vector database. It does not create a RAG runtime, memory engine, evidence engine, provider router, queue, scheduler, plugin manager or approval system.

## Boundary

```text
exposed_by: OpenWebUI or another cockpit may show binding and lifecycle state.
executed_by: Hermes or a reviewed external retrieval adapter.
governed_by: Pantheon governs corpus/scope legitimacy, binding status, lifecycle state, evidence expectations and consequential gates.
approved_by: human where installation, sensitive corpus access, activation or consequential downstream effects require it.
forbidden: retrieval output treated as truth, Evidence admission, canonical memory, automatic approval or unrestricted corpus access.
```

## Capability Slot

```text
capability_id: knowledge_retrieval_pipeline
function: scoped retrieval, filtering, ranking/reranking and provenance-linked context assembly over governed material
owner_layer: execution_runtime
executed_by: Hermes / reviewed retrieval adapter
governed_by: Pantheon
binding_status: candidate
preferred_binding: unbound
candidate_bindings: Haystack
watchlist_bindings: LlamaIndex, LangChain
install_status: absent / not established
health_status: unknown
update_status: unknown
activation_status: unavailable
rollback_status: not_applicable until installation
```

## Why this slot is distinct

The capability is defined without naming a product and remains useful if every current framework is replaced.

```text
document source management
!= document extraction / parsing
!= knowledge retrieval
!= evidence qualification
!= memory promotion
```

A document may already be extracted and governed while still requiring retrieval, metadata filtering, ranking, reranking or context assembly for a specific task. Conversely, a parsing/ingestion product may provide retrieval as part of an integrated stack without becoming the only possible implementation of retrieval.

Therefore `knowledge_retrieval_pipeline` is a smaller replaceable capability than `document_parsing_rag_ingestion`.

## Allowed effects

```text
read governed corpus references within declared scope
query already-authorized indexes / stores
apply project, dossier, source and metadata filters
retrieve candidate passages or records
rank / rerank retrieved candidates
assemble provenance-linked context
report retrieval limitations and capability gaps
return Result Candidate / Evidence Pack Candidate inputs
```

## Forbidden effects

```text
expand corpus scope by inference
crawl undeclared sources
promote retrieved material to Evidence automatically
promote retrieval output to canonical memory
claim professional truth from retrieval score
approve a Result Candidate
send or mutate external systems merely because retrieval succeeded
silently switch to another corpus or binding
```

## Candidate bindings

### Haystack

Posture:

```text
binding_status: candidate / to verify
preferred: no
installation: not established
health: unknown
activation: unavailable
```

Reason for candidacy: its current upstream positioning includes modular RAG, retrieval, context engineering, composable pipelines, ranking/reranking patterns and agent-oriented workflows. Those capabilities make it relevant to the slot, but product breadth is not a reason to adopt it automatically.

Primary review risks:

```text
index or document-store scope broader than Task Contract
external embedding/generation provider leakage
pipeline state confused with Pantheon state
retrieval score treated as evidence quality
agent/tool features expanding beyond the retrieval slot
framework dependency adopted by implication
```

### LlamaIndex

```text
binding_status: watch / compare
```

Evaluate when a concrete retrieval vertical requires comparison of indexing, metadata filtering, retrieval composition, local deployment or document-store integration.

### LangChain

```text
binding_status: watch / compare
```

LangChain is broader than this slot. It may provide retrieval components, but it must not become a default abstraction layer merely because it can express many unrelated runtime functions.

## Relationship to RAGFlow

`document_parsing_rag_ingestion -> RAGFlow` remains unchanged in `HERMES_CAPABILITY_BINDINGS.md`.

The two capability shapes serve different replacement boundaries:

```text
document_parsing_rag_ingestion
  integrated document understanding / parsing / chunk transparency / citation-oriented RAG product candidate

knowledge_retrieval_pipeline
  retrieval and context-assembly capability over already-governed material
```

A future benchmark may show that one product satisfies both functions. That still does not collapse the Capability Slots; it means one binding can implement more than one abstract capability.

## Relationship to LangGraph

LangGraph retains its existing `bounded_workflow_runtime` placement. Retrieval does not require Pantheon to introduce a new durable workflow runtime.

A retrieval pipeline may be invoked inside a Hermes task or a separately governed workflow, but:

```text
retrieval state != workflow authority
workflow checkpoint != Evidence
runtime success != approval
```

## Evidence posture

Retrieval produces candidates and provenance links, not Evidence admission.

Minimum useful return shape:

```text
query_ref
scope_ref
corpus_ref
binding_ref
binding_version
retrieved_items[]
source_refs[]
ranking_method
reranking_method
filters_applied[]
known_limits[]
produced_at
```

The downstream Evidence gate decides whether cited source material is admissible for the professional claim at hand.

## Lifecycle posture

```text
candidate binding
-> installation proposal
-> approved_for_sandbox where required
-> installed by Hermes/operator
-> health observed
-> benchmarked on synthetic or authorized corpus
-> scoped activation
-> task authorization remains separate
```

```text
installed != approved
healthy != safe
benchmark_pass != production adoption
binding_selected != dependency_adopted
activation != task_authorization
retrieved != evidence
```

## MVP boundary

No `pantheon-mvp` change is justified by this document alone.

A future MVP vertical becomes admissible only when there is a concrete comparison or acceptance target, for example:

```text
already-extracted synthetic project corpus
-> scoped retrieval
-> reranking
-> Hermes candidate answer
-> provenance-linked Evidence Pack Candidate
-> human review
```

Until then the slot remains documented non-implemented in Pantheon Next.
