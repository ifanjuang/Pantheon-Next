# Flexible GraphRAG Review

Status: external reference / adapter candidate — document intelligence, hybrid retrieval, GraphRAG and knowledge-ingestion review.

Reviewed source:

```text
https://github.com/stevereiner/flexible-graphrag
Review date: 2026-06-22
```

This document records a Pantheon Next placement review of Flexible GraphRAG.

It is not canonical doctrine.

It is not an implementation request.

It does not install Flexible GraphRAG, configure Docker, create a GraphRAG runtime, create a vector database, create a graph database, create an RDF store, create a search index, start FastAPI, start an MCP server, enable auto-sync, ingest documents, call LlamaParse, add provider keys, change `.env`, mutate `operations/`, mutate `platform/`, add schemas or create tests.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Source signal

Flexible GraphRAG presents itself as an open source platform for document processing, knowledge graph auto-building, GraphRAG, RAG-only, hybrid search, AI query and AI chat.

The reviewed source describes a stack around:

```text
Docling or LlamaParse document processing;
automatic knowledge graph construction;
schemas and ontology support;
property graph databases;
RDF triple stores;
SPARQL / RDF retrieval;
vector databases;
full-text search through OpenSearch / Elasticsearch / BM25;
FastAPI backend;
React / Vue / Angular frontends;
MCP server;
multiple data sources;
optional incremental auto-sync;
OpenTelemetry / Prometheus / Jaeger / Grafana observability;
Docker or standalone deployment.
```

The useful signal for Pantheon is not that a single platform should own the agency knowledge layer.

The useful signal is this pipeline pattern:

```text
Document Source
-> Ingestion Candidate
-> Fragment Candidate
-> Relationship / Graph Candidate
-> Retrieval Candidate
-> Evidence Pack Candidate
-> governed status
-> human decision
```

## Pantheon placement

Flexible GraphRAG belongs, if ever used, outside the Pantheon kernel.

Candidate placement:

```text
exposure surface -> OpenWebUI / Pantheon Control
execution runtime -> Hermes Agent
knowledge ingestion / retrieval adapter -> Flexible GraphRAG candidate
provenance graph -> Flexible GraphRAG / dedicated graph candidate
observability -> Langfuse / Plano / OTEL candidate
Pantheon -> source status, evidence, proof, memory, scope, approval and external-action governance
```

Flexible GraphRAG may ingest, parse, index, retrieve and propose.

It must not validate, remember canonically, approve, decide or act externally.

## Capability classification

| Flexible GraphRAG surface | Pantheon classification | Accepted use | Refused interpretation |
|---|---|---|---|
| Document processing | ingestion adapter candidate | Produce parsed document and Fragment Candidates | source validation or proof |
| Docling parsing | local parser candidate | Local extraction with provenance review | trusted extraction by default |
| LlamaParse parsing | cloud parser candidate | Optional parser when data policy allows | default parser for sensitive dossiers |
| Knowledge graph auto-building | relationship discovery candidate | Produce entity / relationship / Graph Candidates | factual graph authority |
| Ontology / schema guidance | domain-model candidate | Test controlled architecture vocabulary and relations | automatic professional ontology authority |
| RDF triple stores / SPARQL | provenance graph candidate | Structured retrieval and relation testing | Registre Probatoire or canonical source |
| Property graph databases | graph runtime candidate | Relationship exploration and multi-hop retrieval | memory engine |
| Vector databases | retrieval candidate | Semantic search support | evidence, truth or memory |
| Full-text search | retrieval candidate | Keyword/BM25 support and recall baseline | proof |
| Hybrid search | retrieval strategy candidate | Compare vector, full-text and graph retrieval | final answer authority |
| AI query / AI chat | runtime interaction candidate | Candidate responses under Task Contract | professional advice or delivery |
| MCP server | high-risk tool adapter candidate | Possible bounded search/query tool after passport review | unrestricted tool access or write authority |
| Auto-sync | high-risk ingestion automation candidate | Later controlled update detection if scoped | autonomous ingestion pipeline |
| Observability stack | runtime observation candidate | Trace / metric support | Evidence Pack by itself |
| Multiple source connectors | connector candidates | Later source-specific admission review | broad connector authorization |
| Docker stack | implementation candidate | Sandbox deployment option | Pantheon infrastructure requirement |

## Accepted

```text
Flexible GraphRAG as external document-intelligence reference.
Flexible GraphRAG as hybrid retrieval / GraphRAG / RAG comparison candidate.
Flexible GraphRAG as possible architecture-domain sandbox for fictive or desensitized corpora.
Flexible GraphRAG as possible source of Fragment Candidates, Retrieval Candidates, Graph Candidates and Evidence Pack Candidates.
Flexible GraphRAG as inspiration for provenance graph and architecture-domain knowledge registry adapters.
Flexible GraphRAG as benchmark platform for RAG vs GraphRAG vs hybrid search.
```

## Refused

```text
Flexible GraphRAG as Pantheon runtime.
Flexible GraphRAG as Registre Probatoire.
Flexible GraphRAG as canonical memory.
Flexible GraphRAG as source of truth.
Flexible GraphRAG as proof authority.
Flexible GraphRAG as approval engine.
Flexible GraphRAG as autonomous ingestion pipeline.
Flexible GraphRAG as direct MCP tool with write / ingest / sync authority.
Flexible GraphRAG as default production data platform before admission review.
Flexible GraphRAG as automatic professional ontology builder.
Flexible GraphRAG as automatic external-action authorizer.
```

## To verify

Before any local installation, verify:

```text
self-hosting complexity;
Docker footprint;
standalone feasibility;
minimum database set for a small local test;
source connector permissions;
auto-sync disablement;
MCP tool permissions and write controls;
Docling provenance quality;
LlamaParse data-perimeter impact;
knowledge graph extraction hallucination rate;
relationship confidence and explainability;
RDF / ontology usefulness for architecture documents;
incremental update auditability;
ability to export source-fragment-provenance links;
ability to disable AI chat / external query surfaces;
ability to restrict to filesystem-only corpus;
OpenTelemetry trace export and retention;
compatibility with Pantheon Evidence Pack discipline;
compatibility with Hermes profile / Kanban handoff discipline.
```

## To arbitrate

```text
Should the first test be document-only, with graph write disabled?
Should graph extraction be allowed only on fictive corpus first?
Should auto-sync be categorically disabled for the first sandbox?
Should the MCP server remain disabled until a capability passport review exists?
Should cloud parsing such as LlamaParse be forbidden for client material by default?
Should Flexible GraphRAG be treated as a benchmark tool rather than future production layer?
Does it overlap with the architecture knowledge registry blueprint or only inform it?
```

## Recommended first sandbox

First trial should be deliberately narrow:

```text
local / NUC or development machine;
fictive or desensitized architecture corpus;
10 to 20 Markdown or PDF-like documents;
filesystem source only;
manual ingest only;
auto-sync off;
MCP off;
cloud connectors off;
cloud parsing off unless explicitly approved;
RDF off at first;
graph extraction optional and separately reported;
output limited to Fragment Candidates, Retrieval Candidates, Graph Candidates and Evidence Pack Candidates.
```

This sandbox tests evidence discipline before testing platform power.

## Architecture-domain relation

Flexible GraphRAG is most relevant to the first deep domain pack: architecture.

Possible fictive architecture corpus:

```text
client email;
program note;
site description;
PLU excerpt;
DCE / CCTP excerpt;
site meeting report;
contractor estimate;
structural note;
thermal note;
photo annotation;
plan description in Markdown.
```

Expected output posture:

```text
received documents;
referenced-but-absent documents;
source authority class;
date / version signals;
retrieval candidates;
fragment candidates;
relationship candidates;
contradictions;
missing evidence;
assumptions;
risk triggers;
User Decision Gate candidate.
```

## Required return discipline

If Flexible GraphRAG is used in a governed execution handoff, the return path must separate:

```text
ingestion_status;
parser_used;
source_refs;
fragment_refs;
retrieval_candidate_refs;
graph_candidate_refs;
search_candidate_refs;
evidence_pack_candidate;
result_candidate;
contradictions;
confidence / uncertainty signal;
approval_gap;
memory_impact;
external_effect_status;
unchanged_objects.
```

A retrieved excerpt is not evidence by itself.

A graph relation is not a fact by itself.

A vector hit is not proof.

A high similarity score is not validation.

An MCP tool response is not authorization.

An auto-sync event is not an admitted source.

## Capability Gap examples

Flexible GraphRAG should surface, not hide, gaps such as:

```text
source version missing;
source authority unknown;
parser output incomplete;
page / section reference missing;
fragment provenance absent;
graph relation unsupported by source text;
conflicting fragments;
auto-sync attempted outside admitted scope;
MCP write / ingest requested without passport;
cloud parser requested for sensitive material;
retrieval result not sufficient for conclusion;
Evidence Pack expectation unmet;
Task Contract missing;
approval ceiling missing;
memory impact unclear.
```

## Admission test

Flexible GraphRAG is admissible only if it can be constrained to this rule:

```text
It may ingest admitted sources.
It may parse and index bounded material.
It may retrieve and relate fragments.
It may return candidates and gaps.
It does not decide truth, proof, memory, approval, scope or external legitimacy.
```

If it cannot preserve source-fragment-provenance links, it is not acceptable for Pantheon evidence workflows.

If it cannot disable auto-sync, broad connectors and MCP write/ingest authority, it is refused for first sandbox use.

## Status decisions

```text
Accepted:
Flexible GraphRAG as external document-intelligence and hybrid retrieval reference.
Flexible GraphRAG as possible sandbox candidate for architecture-domain corpus review.
Flexible GraphRAG as possible source of Fragment, Retrieval, Graph and Evidence Pack Candidates.
Flexible GraphRAG as comparison surface for RAG, GraphRAG and hybrid search.

Refused:
Flexible GraphRAG as Pantheon runtime.
Flexible GraphRAG as Registre Probatoire or canonical memory.
Flexible GraphRAG as source of truth, proof authority or approval engine.
Flexible GraphRAG as autonomous ingestion / auto-sync pipeline.
Flexible GraphRAG MCP server as unrestricted tool surface.
Flexible GraphRAG as production data platform before admission review.

To verify:
Parser provenance.
Auto-sync disablement.
MCP permissions.
Graph extraction reliability.
RDF / ontology value for architecture.
Source-fragment-provenance export.
Hermes / Kanban compatibility.

To arbitrate:
Whether first sandbox is document-only or includes graph extraction.
Whether cloud parsing is allowed for non-sensitive test material.
Whether MCP server remains disabled until capability passport review.
Whether Flexible GraphRAG is a benchmark tool, future adapter or rejected overkill.
```

## Final rule

```text
Flexible GraphRAG may ingest, index, retrieve and propose.
It may build graph candidates.
It may support Evidence Pack Candidates.
It does not remember canonically.
It does not prove.
It does not approve.
It does not decide.
```
