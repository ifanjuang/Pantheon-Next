# Hermes ecosystem adaptability review — 2026-08-04

Status: completed repository review and governance distillation. No runtime, dependency, installation, activation or task authorization added.

## Objective

Re-evaluate the current adaptability of OpenWebUI, Hermes Agent, Mem0, Mnemosyne, Langflow, Langfuse, LangGraph, LangChain, Docling, Paperless-ngx and adjacent retrieval/RAG frameworks to the existing Pantheon-Hermes architecture.

The objective was convergence, not accumulation:

```text
reuse an existing Capability Slot
extend an existing owner document
keep optional systems outside the standard Hermes distribution
avoid a second runtime, memory authority, provider router or evidence engine
```

## Repository state checked

Pantheon repositories checked before modification:

```text
ifanjuang/Pantheon-Next main
ifanjuang/pantheon-mvp main
open pull requests: none observed at review start
```

Relevant current Pantheon owners:

```text
docs/governance/HERMES_RUNTIME_SURFACE_REVIEW.md
docs/governance/HERMES_RUNTIME_GOVERNANCE.md
docs/governance/HERMES_CAPABILITY_BINDINGS.md
docs/governance/HERMES_KNOWLEDGE_RETRIEVAL_BINDING.md
docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md
docs/governance/OPENWEBUI_INTEGRATION.md
docs/governance/PAPERLESS_NGX_DOCUMENT_RUNTIME.md
docs/governance/DOCUMENT_OCR_DERIVATION_PIPELINE.md
docs/governance/DOCUMENT_RUNTIME_LIVE_OBSERVATIONS.md
docs/governance/RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md
operations/langfuse-hermes-first-test-runbook.md
```

Existing coverage was substantial. A new architecture or product-specific authority document was not justified.

## External sources checked

Primary repositories and release surfaces reviewed:

```text
NousResearch/hermes-agent
  reviewed release: 0.20.0
  release commit: 3c27eb6234bf91b8ceee9e9071591b31e9b148cb

open-webui/open-webui
mem0ai/mem0
mnemosyne-oss/mnemosyne
langfuse/langfuse
langflow-ai/langflow
langchain-ai/langgraph
langchain-ai/langchain
docling-project/docling
docling-project/docling-mcp
paperless-ngx/paperless-ngx
deepset-ai/haystack
run-llama/llama_index
infiniflow/ragflow
```

External sources remain references. Retrieval date and repository activity do not establish installation, safety or adoption.

## Facts observed

### Hermes memory surface

The Hermes 0.20.0 memory-provider documentation states:

```text
eight bundled external provider plugins
one external provider active at a time
built-in MEMORY.md / USER.md remains active alongside the provider
provider activation may inject context
provider activation may prefetch recall
provider activation may synchronize conversation turns
provider activation may extract memory on session end
provider activation may mirror built-in writes
provider activation may expose provider-specific tools
```

Mem0 is one of the documented Hermes providers.

Mnemosyne presents a Hermes plugin and MCP path in its own repository, but it is not listed among the eight providers in the reviewed Hermes 0.20.0 documentation. It is therefore classified as a third-party candidate, not a bundled Hermes capability.

### Existing Pantheon document vertical

The repositories already distinguish:

```text
document_source_management
!= document_ocr
!= document_structural_analysis
!= knowledge_retrieval_pipeline
!= evidence qualification
```

Paperless-ngx is already optional and not required for core local/NAS ingestion.

A bounded Docling implementation path already exists in `pantheon-mvp`, and current Next doctrine already recognizes Docling health and structured derivations. This justified promoting Docling as the preferred candidate for `document_structural_analysis`, not creating a new document platform.

### Existing retrieval placement

Haystack, LlamaIndex and LangChain were already classified in `HERMES_KNOWLEDGE_RETRIEVAL_BINDING.md`.

LangGraph already had a `bounded_workflow_runtime` placement.

RAGFlow was already listed as an integrated document/RAG candidate. The current review found that its combined parsing, retrieval, agents, workflow, memory, MCP, model and UI surfaces overlap too many selected replaceable responsibilities to remain a preferred default binding.

### Existing Langfuse material

Langfuse was already the preferred observability candidate and had a first-test operations runbook.

The runbook still referenced one-shot reference-review files removed during the 2026-07-07 governance cleanup. It also did not require proof that the actual Hermes API-server/Runs/OpenWebUI path loaded and emitted the observability hook.

## Interpretations

### One governed Hermes profile cannot safely use automatic external memory

Automatic prompt injection, background recall and background memory writes would add runtime context and state outside the immutable admitted Context Pack.

Therefore:

```text
pantheon-governed
  external memory provider off
  automatic recall off
  automatic runtime memory write off
  hidden OpenWebUI memory/RAG enrichment off

assistant-personal
  one optional external memory provider
  no Pantheon authority
  no professional task authorization
```

This is runtime profile separation, not a new Pantheon identity or memory model.

### Docling complements Hermes; RAGFlow and LangGraph tend to duplicate it

Docling can remain a bounded stateless or separately operated document-analysis binding.

LangGraph may be useful only behind one specialized capability contract when a demonstrated stateful workflow gap exists.

Langflow is useful as a temporary visual laboratory, not as a hidden production orchestrator.

RAGFlow may remain a reference or bounded existing-system adapter, but should not replace Hermes, Docling, Paperless, OpenWebUI and Pantheon governance simultaneously.

### LangChain and LlamaIndex are component sources, not architecture owners

Selected packages may be reused inside a bounded adapter. Their agent, memory, provider-routing and workflow surfaces must not become global Pantheon-Hermes infrastructure.

## Decisions applied

Updated:

```text
docs/governance/HERMES_RUNTIME_SURFACE_REVIEW.md
  records memory-provider behavior
  defines pantheon-governed and assistant-personal separation
  classifies ecosystem compatibility
  leaves the standard distribution unchanged

docs/governance/HERMES_CAPABILITY_BINDINGS.md
  prefers Docling for document_structural_analysis
  preserves optional Paperless document_source_management
  keeps Langfuse preferred but live-path unqualified
  leaves external_runtime_memory unbound
  classifies Mem0 and Mnemosyne separately
  downgrades RAGFlow to watch/reference by default
  refuses LangGraph as default runtime

docs/governance/HERMES_KNOWLEDGE_RETRIEVAL_BINDING.md
  keeps Haystack candidate
  limits LangChain/LlamaIndex to selected components
  places Langflow, LangGraph and RAGFlow outside the default retrieval path
operations/langfuse-hermes-first-test-runbook.md
  removes deleted review references
  requires exact Hermes artifact and actual trace-path observation
  requires run correlation and synthetic-data-only validation

tests/test_hermes_ecosystem_adaptability.py
  locks the non-adoption and profile-separation boundaries
```

Not changed:

```text
pantheon-mvp
Hermes distribution lock
schemas
runtime code
Docker or Compose
OpenWebUI configuration
Hermes configuration
memory provider selection
Langfuse installation
Docling installation
Paperless selection
```

## Verification criteria

The work is complete when:

```text
new ecosystem test passes
existing Governance CI passes
existing Obsolete Authority Consistency passes
no optional binding enters the distribution by implication
no deleted Langfuse review path remains in the active runbook
no memory provider is selected for pantheon-governed
```

## Boundaries retained

```text
available != selected
selected != installed
installed != approved
healthy != safe
profile created != scope governed
provider selected != memory admitted
retrieved != truth
trace recorded != Evidence
workflow checkpoint != approval
runtime success != Evidence
```
