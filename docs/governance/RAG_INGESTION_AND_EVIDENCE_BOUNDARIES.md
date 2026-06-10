# RAG Ingestion and Evidence Boundaries

Status: active support doctrine — RAG reference distillation and evidence boundary note.

This document clarifies how Pantheon Next interprets recent RAG references, chunking evaluation methods and long-document benchmarks.

It does not implement a RAG pipeline.

It does not add dependencies.

It does not define an OpenWebUI plugin, Function, Pipe, Filter, Action, Tool or Pipeline.

It does not define a Hermes skill, runtime or ingestion worker.

It does not authorize automatic Knowledge Base mutation, automatic evidence approval, automatic memory promotion, scheduler, queue, provider router, GraphRAG runtime, observability backend or hidden workflow runner.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

RAG quality is not a single technical score.

It is a governed chain that starts before embeddings and continues after retrieval.

This document answers:

```text
When a document is prepared, chunked, indexed and retrieved, what has actually been established?
```

## Core boundary

```text
A source can become retrievable.
A retrieved chunk can become an Evidence Candidate.
An Evidence Candidate can become an Evidence Item only through governed selection.
An Evidence Item can support a deliverable only inside an Evidence Pack.
None of these transitions creates a Registre Probatoire entry by itself.
```

## Governed chain

Pantheon preserves the following distinctions:

```text
Raw Source
→ Source Reference
→ Ingestion Candidate
→ Knowledge Item
→ Chunk / Retrieval Unit
→ Retrieved Knowledge
→ Context Sufficiency Check
→ Evidence Candidate
→ Evidence Item
→ Evidence Pack
→ Output Candidate
→ Approval Event
→ Register Candidate
→ Registre Probatoire entry
```

Forbidden shortcuts:

```text
uploaded -> validated
converted -> approved
chunked -> evidence
indexed -> evidence
retrieved -> truth
citation displayed -> proof
score passed -> approval
benchmark passed -> professional validation
memory candidate -> canonical memory
```

## Reference signals distilled in this wave

| Reference | What it contributes | Pantheon interpretation | Forbidden interpretation |
|---|---|---|---|
| `chunk-norris` | empirical comparison of chunking strategies before ingestion | chunking fitness can be measured per document or corpus | best chunker becomes global KB doctrine |
| `MMLongBench-Doc` | long multimodal PDF evaluation with evidence pages, evidence modalities, cross-page and unanswerable questions | document QA systems should preserve page/source grounding and refusal behavior | benchmark score validates professional answers |
| Medium RAG 10M+ article | large-scale RAG reliability signal and caution against weak retrieval | watch-level architecture signal only | near-zero hallucination claim becomes proof |
| Reddit RAG discussions | practitioner weak signals and failure-mode vocabulary | watch only unless backed by reproducible method | anecdote becomes doctrine |
| `contextschema-py` | post-retrieval context sufficiency check | retrieved context can be tested before action | context score becomes C0-C5 approval |

## Minimum evidence expectations for RAG-backed outputs

A RAG-backed output should disclose at least:

```text
source_id
source_type
source_version_or_date_when_known
source_scope
chunk_id_or_page_reference
retrieval_method_when_relevant
retrieval_limitations
context_sufficiency_status
selected_evidence_items
unresolved_source_conflicts
unanswerable_or_insufficient-evidence status
approval_status
```

A retrieved chunk should not be cited alone when the claim depends on:

- several pages;
- a table or chart;
- an image or figure;
- a contradiction between sources;
- a fresh regulatory, legal, contractual or professional fact;
- a document boundary chosen by the user;
- a professional judgment.

## Chunking fitness

Chunking fitness means:

```text
The chosen chunking strategy was tested against representative questions, retrieval traces and source-bound evidence expectations for a defined source scope.
```

It does not mean:

```text
The answer is correct.
The source is reliable.
The document has been validated.
The same chunking strategy should apply to every corpus.
```

Governance rule:

```text
A chunking strategy can be measured.
Its measurement is not proof, approval or memory.
```

## Long-document and multimodal evidence

Long professional documents create evidence problems that ordinary text retrieval can hide.

A governed RAG workflow should preserve:

- page-level evidence;
- page ranges when evidence spans several pages;
- source modality such as text, table, chart, image, caption, layout or annex;
- unanswerable questions as first-class test cases;
- conflict markers when two evidence items disagree;
- quality flags when OCR, layout extraction, table extraction or figure interpretation is uncertain.

Governance rule:

```text
A fluent long-document answer is not valid unless its evidence remains localizable and reviewable.
```

## Context sufficiency

After retrieval and before action, Pantheon should be able to ask:

```text
Is the retrieved context complete enough for this decision?
Is it fresh enough?
Is it sourced enough?
Was it invalidated by a later source, user instruction or scope boundary?
Does the task require escalation rather than generation?
```

This is a status signal.

It is not an approval.

## OpenWebUI exposure boundary

OpenWebUI may expose:

- selected sources;
- source status;
- chunking evaluation summaries;
- retrieval traces when useful;
- context sufficiency status;
- Evidence Pack display;
- unanswerable / insufficient evidence state;
- approval panel;
- User Decision Gate.

OpenWebUI must not become:

- ingestion runtime owner;
- source of truth;
- evidence authority;
- approval authority;
- automatic KB rewriter;
- memory canonizer;
- plugin or skill installer.

## Hermes execution boundary

Hermes may execute, under Task Contract:

- document profiling;
- conversion;
- chunking;
- retrieval evaluation;
- long-document evaluation;
- quality reporting;
- Evidence Candidate linking.

Hermes must return candidates and reports.

Hermes must not:

- approve evidence;
- mutate a Registre Probatoire entry;
- rewrite OpenWebUI Knowledge without authorization;
- send sensitive documents to external APIs without approval;
- convert a benchmark result into professional validation;
- make a chunking strategy globally sovereign.

## Pantheon governance boundary

Pantheon governs:

- source scope;
- Task Contract;
- external tool authorization;
- evidence status;
- approval status;
- memory status;
- Reference Boundaries;
- User Decision Gates;
- module activation rules.

Pantheon does not run retrieval, chunking, parsing, OCR, embedding, vector search or benchmark evaluation.

## User Decision Gate triggers

Escalate when:

- the answer depends on evidence across several pages and retrieval is partial;
- the question is probably unanswerable from the available dossier;
- an external API would receive private or professional documents;
- the retrieved evidence conflicts with another source;
- a benchmark or score is being used as if it were approval;
- the output has legal, contractual, financial, medical, architectural or client-facing effect.

## Relationship to `RAG_INGESTION_PIPELINE.md`

`RAG_INGESTION_PIPELINE.md` describes the governed preparation path for PDF and document ingestion.

This document clarifies the boundary after and around that path:

```text
ingestion quality
+ retrieval fitness
+ context sufficiency
+ evidence selection
+ approval status
```

It deliberately does not redefine converter routing, chunk record formats or ingestion directory layout.

## Final rule

```text
Large-scale RAG must be judged by evidence behavior, not by architectural promises.
A benchmark can reveal failure modes.
A retrieval score can compare methods.
Only governed evidence and approval can support delivery.
```