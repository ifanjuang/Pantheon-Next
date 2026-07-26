# 2026-07-26 — Hermes skill supply chain / magnus919 / Haystack

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Context

Reviewed the current Pantheon Next organization before deciding where external skill sources and Haystack-related capability work belong.

Active repository documents consulted included `README.md`, `STATUS.md`, `WHAT_RUNS.md`, `AUTHORITY_INDEX.md`, `CAPABILITY_PLACEMENT.md`, `MODULAR_DOMAIN_REORIENTATION.md`, `ADAPTERS_AND_BINDINGS.md`, `HERMES_CAPABILITY_BINDINGS.md`, the runtime-adapter and external-reference authority indexes, `CONTRIBUTING.md` and `STATUS_HEADER_RULES.md`.

Current upstream Haystack positioning was also rechecked on 2026-07-26: the framework presents modular RAG, retrieval, context engineering, composable pipelines and agent-oriented workflows. That breadth is an external capability observation, not an adoption decision.

## Initial placement decision

Keep governance and classification in Pantheon Next.

Do not add executable Haystack, LangChain, LlamaIndex, LangGraph or `magnus919/agent-skills` material to `pantheon-mvp` merely because the tools exist.

```text
Skill Source
!= Skill Candidate
!= Capability Binding
!= Installed Skill
!= Approved Skill
!= Activated Skill
!= Task-authorized Skill
```

`magnus919/agent-skills` remains an external Hermes skill-source candidate only.

## Capability-slot arbitration

The question was whether Haystack belongs only under the existing `document_parsing_rag_ingestion` slot or whether a separate abstract capability exists.

Decision: retain a distinct candidate capability:

```text
knowledge_retrieval_pipeline
```

Reason: the function survives replacement of every current product and is useful after document extraction has already completed.

```text
retrieve within declared corpus/scope
filter by project / dossier / metadata
rank and rerank
assemble provenance-linked context
return bounded retrieval candidates / capability gaps
```

This is distinct from:

```text
document_source_management
!= extraction / parsing
!= knowledge_retrieval_pipeline
!= Evidence qualification
!= canonical memory promotion
```

## Binding posture

```text
knowledge_retrieval_pipeline:
  preferred_binding: unbound
  candidate_binding: Haystack
  watchlist_bindings: LlamaIndex, LangChain

RAGFlow:
  existing document_parsing_rag_ingestion placement unchanged

LangGraph:
  existing bounded_workflow_runtime placement unchanged
```

Haystack is not selected as preferred, installed, approved or activated by this decision.

## Repository artifacts

Created / updated:

```text
docs/governance/reference_reviews/HERMES_SKILL_SUPPLY_CHAIN_MAGNUS919.md
docs/governance/HERMES_KNOWLEDGE_RETRIEVAL_BINDING.md
docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
```

`HERMES_CAPABILITY_BINDINGS.md` remains the general registry. This pass adds the specialized candidate binding document and indexes it without rewriting the existing preferred-binding table by implication.

## Runtime status

```text
runtime_added: no
MVP_changed: no
skill_installed: no
framework_dependency_added: no
preferred_binding_selected: no
activation_changed: no
protected_paths_touched: no
repo_state: documented non-implemented / external review
```

## Non-equivalences

```text
candidate_slot != implemented_runtime
binding_candidate != preferred_binding
binding_selected != dependency_adopted
installed != approved
healthy != safe
update_available != update_authorized
retrieved != evidence
runtime_success != evidence
```
