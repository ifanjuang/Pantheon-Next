# Chunky Capability Review

Status: external reference / capability candidate review — documented non-implemented.

Review date: 2026-07-07.

Repository: `GiovanniPasq/chunky`.

Reviewed source: `https://github.com/GiovanniPasq/chunky`.

This review records a candidate capability for Pantheon Next. It does not adopt, clone, install, execute, configure, approve, index, benchmark or add Chunky as a dependency.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Short assessment

Chunky is a strong sandbox candidate for document preparation before RAG.

It should not become Pantheon runtime, memory, proof system or ingestion authority.

Recommended outcome:

```text
accepted_for_sandbox
```

with strict constraints:

```text
non-sensitive PDF only;
local execution only;
no Cloud API converter by default;
no indexation without human approval;
no memory promotion;
outputs remain candidates.
```

## Abstract function

```text
Prepare and inspect documents before RAG.
```

Capability Slot:

```yaml
capability_slot:
  id: rag_document_preparation
  title: RAG Document Preparation
  abstract_function: convert, clean, inspect, compare and chunk documents before retrieval or indexing
  expected_inputs:
    - PDF files
    - Markdown files
    - converter choice
    - chunking strategy
  expected_outputs:
    - Markdown Candidate
    - Chunk Set Candidate
    - Enrichment Candidate
    - Runtime Status Candidate
  forbidden_outputs:
    - validated evidence
    - approved knowledge
    - canonical memory
    - automatic indexation
    - automatic proof
```

## Candidate binding

```yaml
candidate_binding:
  id: chunky-local-docker
  runtime_owner: hermes
  execution_surface: local Docker or local service outside Pantheon
  exposure_surface: OpenWebUI or Pantheon cockpit card projection
  pantheon_role: govern status, gates, approval and memory boundary
```

Binding selected does not mean dependency adopted.

## What Pantheon governs

Pantheon governs:

```text
capability status;
source admission;
converter admissibility;
chunking-status vocabulary;
external-provider gate;
indexation approval;
evidence expectations;
memory prohibition by default;
version / hash / trace references;
sandbox scope;
what may be shown as candidate.
```

Pantheon must not convert, chunk, enrich, index or run Chunky.

## What Hermes executes

Hermes may execute, if separately authorized:

```text
start or call Chunky;
upload non-sensitive test documents;
run conversion;
run chunking;
collect status reports;
return Markdown Candidates and Chunk Set Candidates;
return errors, metrics and trace references.
```

Hermes must not promote the result to evidence, memory or approved knowledge.

## What OpenWebUI exposes

OpenWebUI may expose:

```text
Capability Candidate Card;
Document Preparation Card;
Markdown Candidate preview;
Chunk Set Candidate preview;
converter comparison;
chunking strategy comparison;
Indexation Gate;
external-provider warning;
trace and version indicators.
```

OpenWebUI must not make a click equivalent to indexation approval.

## What the human approves

Human approval is required for:

```text
sandbox test start;
using any non-public or client document;
using a VLM or LLM enrichment provider;
using the Cloud API converter;
accepting Markdown as project knowledge;
indexing chunks into a RAG store;
promoting any extracted statement to Evidence;
using results in a professional output.
```

## Forbidden by default

```text
client-data use;
cloud conversion;
external API calls;
automatic indexation;
automatic evidence creation;
automatic memory promotion;
production activation;
auto-update adoption.
```

## Status classification

```yaml
repository_status: active_public_repository
governance_status: capability_candidate
runtime_status: not_installed
install_status: absent
health_status: unknown
update_status: unknown
activation_status: unavailable
implementation_status: documented_non_implemented
safe_default: reference_only_until_sandbox_approved
```

## Risk review

| Risk | Classification | Gate |
|---|---|---|
| Broken conversion creates false knowledge | medium | evidence_quality_gate |
| PDF content leaves perimeter via Cloud API | high | data_exit_gate / external_provider_gate |
| LLM enrichment smooths errors | medium | llm_enrichment_gate |
| Chunks treated as proof | high | evidence_quality_gate |
| Chunks indexed automatically | high | indexation_approval_gate |
| Runtime health treated as safety | medium | runtime_health_gate |
| External dependency drift | medium | update_authorization_gate |

## Required gates

```text
sandbox_approval_gate
source_review_gate
external_provider_gate
data_exit_gate
llm_enrichment_gate
indexation_approval_gate
evidence_quality_gate
update_authorization_gate
runtime_health_gate
```

## Sandbox test proposal

Allowed test:

```text
Use one public or anonymized PDF.
Run local conversion.
Compare Markdown candidates.
Run at least two chunking strategies.
Review chunk quality manually.
Record gaps and failure modes.
Do not index into memory.
Do not use Cloud API.
Do not use client data.
```

Expected result:

```text
Markdown Candidate
Chunk Set Candidate
Quality Notes
Capability Gap list
Gate Recommendation
```

## Decision

```yaml
decision_recommendation: accepted_for_sandbox
reason: useful document-preparation layer for RAG, aligned with source/chunk transparency if kept outside Pantheon runtime
blocked_until:
  - sandbox approval
  - local execution path confirmed
  - cloud converter disabled by default
  - indexation gate defined
```

## Boundary phrase

```text
Chunky may prepare the corpus.
Hermes may execute the preparation.
OpenWebUI may expose the result.
Pantheon governs whether the result may matter.
The human decides.
```
