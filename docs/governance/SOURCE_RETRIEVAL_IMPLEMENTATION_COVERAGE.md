# Source and Retrieval Implementation Coverage

Status: candidate support note — descriptive inventory, no doctrine change.
Observed repositories:

```text
Pantheon-Next: main at 6c32aa7e5589dd925d1d6770a480d3bdef5d6ee4
pantheon-mvp: main observed 2026-08-03
```

## Purpose

Record the current coverage between the governed source/retrieval model and the external candidate implementation without creating a new `Knowledge Pipeline`, runtime, connector framework, memory engine or authority layer.

The existing owners remain:

```text
SOURCE_INGESTION_RETRIEVAL_MODEL.md
HERMES_KNOWLEDGE_RETRIEVAL_BINDING.md
RAW_DERIVED_GOVERNED_RECORDS.md
EVIDENCE_PACK.md
ANSWER_VERIFICATION_GATE.md
NON_EQUIVALENCE_RULES.md
```

This inventory is observational. Repository code remains authoritative for implementation state and the governance corpus remains authoritative for doctrine.

## Executive conclusion

The ecosystem already covers the architecture commonly presented as:

```text
source
→ extraction
→ chunks
→ embeddings
→ vector retrieval
→ candidate generation
```

It covers it through separated responsibilities rather than one adopted RAG product:

```text
Pantheon Next governs scope, provenance, status, Evidence boundaries and gates.
pantheon-mvp implements bounded candidate persistence, extraction, retrieval and projections.
Hermes remains the intended external executor and binding host.
Cockpit / OpenWebUI expose projections and review surfaces.
The human decides consequential reliance and promotion.
```

No new top-level abstraction is required merely to describe this path.

## Coverage matrix

### 1. Source declaration and scope

Governance posture:

```text
source access is bounded by Case, Situation, scope and confidentiality;
linked, cached and ingested are operational postures, not authority levels;
Source != Evidence.
```

Observed candidate implementation:

```text
implemented:
- Task Contract loading and validation;
- ingestion limited to explicitly declared sources;
- source-path perimeter checks before database mutation;
- dossier and contract identity retained on chunks;
- optional NAS-mounted document intake;
- source digest and version records.
```

Coverage: `implemented candidate`.

### 2. Original and derived representations

Governance posture:

```text
original source remains superior to OCR, extracted text, Markdown, chunks and embeddings;
derivatives retain method, version, source location and inherited scope;
extraction success != source truth.
```

Observed candidate implementation:

```text
implemented:
- source_documents;
- document_versions;
- extraction_runs;
- extraction_observations;
- document_extraction_bindings;
- source and configuration digests;
- converter identity and version;
- Markdown and structured JSON outputs;
- quality flags and review status;
- optional Docling Serve binding.
```

Coverage: `implemented candidate`, with live binding still deployment-dependent.

### 3. Chunking and structural provenance

Governance posture:

```text
chunk set is a derived representation;
chunk != source;
chunk != Evidence.
```

Observed candidate implementation:

```text
implemented:
- bounded text chunking;
- structured extraction compilation;
- source reference and chunk ordinal;
- source digest;
- page range where available;
- structural locator;
- parent heading and section path;
- quality flags.
```

Coverage: `implemented candidate`.

### 4. Embeddings and vector persistence

Governance posture:

```text
vectorization is selective;
embedding != memory;
vector store availability != adoption.
```

Observed candidate implementation:

```text
implemented:
- deterministic embedding seam;
- PostgreSQL vector extension;
- vector column on bounded chunks;
- pgvector-backed candidate retrieval.
```

Coverage: `implemented candidate` for the bounded vertical, not a generic adopted embedding service.

### 5. Scope-first semantic retrieval

Governance posture:

```text
scope and confidentiality filters precede retrieval;
retrieval returns source-linked candidates;
retrieved != true.
```

Observed candidate implementation:

```text
implemented:
- SQL perimeter filtering before vector ranking;
- retrieval limited to the Task Contract dossier and declared sources;
- distance returned with each candidate chunk;
- Retrieval Trace URI;
- contract, ingestion and source audit identity;
- structural provenance returned separately from ranking.
```

Coverage: `implemented candidate`.

### 6. Keyword and hybrid retrieval

Governance posture:

```text
structured identifiers and native search should be preferred where available;
full-text search precedes or complements semantic retrieval;
ranking and reranking remain replaceable execution capabilities.
```

Observed candidate implementation:

```text
not established by this review:
- explicit PostgreSQL full-text index and query path;
- lexical/vector result fusion;
- configurable hybrid weighting;
- independent reranking stage;
- retrieval comparison benchmark across bindings.
```

Coverage: `gap / not established`.

This is the main functional difference from the Reddit diagram. It is a bounded implementation gap, not a missing Pantheon concept.

### 7. Candidate generation and refusal

Governance posture:

```text
retrieval output may inform a Result Candidate or Evidence Pack Candidate;
runtime success != Evidence;
result candidate != approved result.
```

Observed candidate implementation:

```text
implemented:
- bounded question runner;
- deterministic candidate and refusal paths;
- candidate YAML stream;
- refusal when scope or contract conditions are not met;
- source-linked retrieval traces in candidate material.
```

Coverage: `implemented candidate`.

### 8. Verification and Evidence boundary

Governance posture:

```text
retrieval result
→ deliberate selection for a scoped assertion
→ Evidence Candidate
→ gate or human decision where consequential.
```

Observed candidate implementation:

```text
implemented candidate:
- terminal human decision stand-in;
- explicit approve, refuse, request revision and request more evidence outcomes;
- human identity required;
- separate Register Candidate proposal;
- explicit retention authorization required;
- no automatic durable promotion.

not established as adopted integration:
- live Pantheon Evidence admission service;
- adopted answer-verification gate endpoint;
- end-to-end Hermes handoff under an activated Capability Slot.
```

Coverage: `implemented stand-in / partial integration`.

### 9. Knowledge and document projections

Governance posture:

```text
Cockpit cards are projections;
UI state != authorization;
server contracts remain authoritative.
```

Observed candidate implementation:

```text
implemented:
- Project Document projection;
- Knowledge item persistence;
- source-chunk links;
- review statuses;
- append-only Knowledge events;
- optimistic version checks and idempotency fields;
- Hermes edit-request seam;
- Cockpit APIs and schema-driven card surfaces.
```

Coverage: `implemented candidate`.

### 10. External adapters

Governance posture:

```text
adapter available != source of truth;
installed != approved;
healthy != safe;
activated != task authorized.
```

Observed candidate implementation:

```text
implemented or declared as optional candidate seams:
- Docling;
- Paperless;
- OpenWebUI;
- read-only mounted document root.

not established:
- generic connector framework;
- live Google Drive ingestion;
- generic multi-source retrieval resolver;
- production source cockpit;
- adopted Hermes retrieval binding.
```

Coverage: `specific optional adapters`, not a generic integration platform.

## What already exists

The following must not be proposed as new concepts:

```text
source identity and access posture;
derived representation candidate;
retrieval trace;
Evidence Candidate boundary;
Capability Slot for knowledge retrieval;
Result Candidate and refusal path;
Knowledge projection;
human decision gate;
Register Candidate promotion boundary.
```

## Confirmed gaps

The current review identifies five concrete gaps worth treating separately:

```text
1. lexical / PostgreSQL full-text retrieval;
2. explicit hybrid lexical-vector fusion;
3. optional reranking binding and benchmark;
4. adopted Hermes handoff contract for knowledge_retrieval_pipeline;
5. conformance evidence linking the MVP outputs to active Pantheon schemas and gates.
```

The first three are execution capabilities. The fourth is an integration boundary. The fifth is verification evidence. None requires a new authority object.

## Recommended sequence

```text
A. Preserve current concepts and owners.
B. Add tests that prove the currently implemented scope-first vector path.
C. Add lexical retrieval as a separate bounded candidate path.
D. Add deterministic hybrid fusion with provenance retained per result.
E. Benchmark before selecting any reranker or framework binding.
F. Define and test the Hermes handoff against existing Capability Slot and Evidence contracts.
G. Update this inventory from verified code and CI evidence.
```

## Non-goals

This inventory does not authorize:

```text
Pantheon becoming a RAG runtime;
Pantheon hosting embeddings or vector search as a doctrine requirement;
adoption of LangChain, Haystack, LlamaIndex, RAGFlow or Chroma;
a generic connector manager;
a memory engine;
a provider router;
a scheduler or queue;
automatic Evidence admission;
automatic approval or durable promotion.
```

## Invariants

```text
coverage documented != adoption
implemented candidate != activated capability
retrieval score != evidence quality
hybrid retrieval != truth
source projection != source authority
successful extraction != verified content
Cockpit display != authorization
Hermes execution != Pantheon decision
```

---

## Reconciliation update — 2026-08-07

This addendum records a later observation and supersedes only the implementation-status statements in:

```text
Coverage matrix / 6. Keyword and hybrid retrieval;
Confirmed gaps;
Recommended sequence.
```

The historical review above is retained unchanged. Existing governance owners, authority boundaries, non-goals and invariants remain authoritative.

Observed repositories:

```text
Pantheon-Next: fde7e856cd04c56e718d2bb133e65262c80d5d52
pantheon-mvp: 3195adf3131d30494348552c4dacba312eb7fc03
observation date: 2026-08-07
```

### Corrected implementation status

Current `pantheon-mvp` provides an implemented candidate for:

```text
PostgreSQL lexical retrieval using websearch_to_tsquery('simple', query),
to_tsvector('simple', body) and ts_rank_cd;
Task Contract dossier and declared-source filtering before lexical ranking;
scope-first pgvector retrieval;
deterministic weighted Reciprocal Rank Fusion;
configurable vector and lexical weights, candidate_k, top_k and rrf_k;
separate lexical rank, vector rank and fused score;
runner integration before candidate generation;
contract, ingestion, source and structural provenance on returned chunks.
```

The active vector embedder is a deterministic offline feature-hashing placeholder. It proves the replaceable vector path and scope boundary; it does not establish production semantic quality or select an embedding provider.

```text
vector path implemented != semantic quality established
placeholder available != production binding selected
hybrid score != confidence
hybrid score != Evidence quality
```

Corrected matrix:

```text
source perimeter and provenance         implemented candidate
structured extraction and chunks        implemented candidate
scope-first pgvector path                implemented candidate
production semantic embedding binding   not established
PostgreSQL lexical retrieval             implemented candidate
weighted hybrid RRF                      implemented candidate
runner integration                       implemented candidate
labelled métier relevance evaluation     not established
independent reranking binding             not established
Hermes search-tool handoff                not implemented
agency/NAS Hermes acceptance              not completed (#227)
production activation                     not authorized
```

### Hermes placement

The existing `knowledge_retrieval_pipeline` Capability Slot remains the owner. No additional Capability Slot is introduced.

The Hermes `0.20.0` laboratory baseline currently qualifies only:

```text
pantheon_context_manifest
pantheon_context_entity
```

The real agency/NAS acceptance remains open in `pantheon-mvp` issue #227. This reconciliation therefore does not add or activate another Hermes tool.

After that two-tool baseline is accepted on the real target, the bounded candidate extension is:

```text
Hermes admitted run
  -> pantheon_context_search
    -> pantheon-mvp retrieval API
      -> Task Contract perimeter
      -> vector + lexical retrieval
      -> weighted RRF
      -> provenance-linked candidate hits
```

The tool must resolve its corpus from the admission and Task Contract. It must not accept an arbitrary path, undeclared corpus or caller-selected project perimeter. The local MCP/HTTP policy service remains a read-only policy and validation projection; it does not become the private project-document search engine.

### Updated gaps and sequence

```text
1. Add a small labelled métier relevance set in pantheon-mvp.
2. Record exact lexical successes and placeholder limitations.
3. Correct only defects demonstrated by those cases.
4. Complete Hermes 0.20.0 agency/NAS acceptance #227 with the two-tool baseline.
5. Specify and implement pantheon_context_search as a bounded third tool.
6. Requalify the exact tool surface and rollback.
7. Evaluate production embeddings, reranking or another PostgreSQL extension only if measurements require them.
8. Link candidate outputs to active Pantheon gates with conformance evidence.
```

External repositories remain references rather than adopted dependencies:

```text
pgvector / pgvector-python  implementation reference;
Vespa rag-blueprint         evaluation-method reference;
ranx / ir_measures          optional development-only metrics;
ParadeDB                     watch candidate on measured PostgreSQL limits;
Qdrant, Weaviate, OpenSearch and Elasticsearch  references only.
```

```text
implemented candidate != activated capability
benchmark passed != production adoption
search tool exposed != task authorized
retrieved != Evidence
Hermes execution != Pantheon decision
```