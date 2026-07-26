# 2026-07-26 — Hermes skill supply chain / magnus919 / Haystack

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Context

Reviewed the current Pantheon Next repository organization before deciding whether external skill catalogues and Haystack-related capability work belonged in Pantheon Next or `pantheon-mvp`.

Active repository documents consulted included `README.md`, `STATUS.md`, `WHAT_RUNS.md`, `AUTHORITY_INDEX.md`, `CAPABILITY_PLACEMENT.md`, `MODULAR_DOMAIN_REORIENTATION.md`, `ADAPTERS_AND_BINDINGS.md`, `HERMES_CAPABILITY_BINDINGS.md`, runtime-adapter/external-reference authority indexes, `CONTRIBUTING.md` and `STATUS_HEADER_RULES.md`.

## Decision

Keep the governance and classification work in Pantheon Next.

Do not add executable Haystack, LangChain, LlamaIndex, LangGraph or `magnus919/agent-skills` runtime material to `pantheon-mvp` at this stage.

Create a bounded external reference review that formalizes the distinctions:

```text
Skill Source
!= Skill Candidate
!= Capability Binding
!= Installed Skill
!= Approved Skill
!= Activated Skill
!= Task-authorized Skill
```

`magnus919/agent-skills` is retained as an external Hermes skill-source candidate only.

Haystack is retained as a candidate binding to compare. This change does not replace RAGFlow, does not create a new canonical Capability Slot and does not adopt Haystack as a dependency.

LangGraph keeps its existing `bounded_workflow_runtime` placement. LlamaIndex and LangChain remain comparison/watch candidates in this review only.

## Placement

```text
Pantheon Next:
  governs classification, status, scope, evidence expectations,
  installation proposal, activation, update review and consequential gates.

Hermes:
  may discover, install, load and execute skills only through separately
  configured runtime/operator paths.

OpenWebUI:
  may display lifecycle state and collect decisions; it is not the installer.

Human:
  approves consequential installation, activation, sensitive data scope,
  breaking updates and external effects where required.
```

## Deferred registry change

`docs/governance/HERMES_CAPABILITY_BINDINGS.md` was deliberately not modified in this pass.

Reason: the current registry already contains `document_parsing_rag_ingestion`. A tool-specific Haystack entry should not force a new abstract slot. The next review must first determine whether a durable, tool-agnostic `knowledge_retrieval_pipeline` capability exists independently of Haystack.

This follows the current kernel/adapters rule: product-specific features default to adapter or binding review; only missing abstract governance/capability distinctions justify kernel-level changes.

## Runtime status

```text
runtime_added: no
MVP_changed: no
skill_installed: no
framework_dependency_added: no
binding_selected: no
activation_changed: no
protected_paths_touched: no
repo_state: documented review only
```

## Created artifact

`docs/governance/reference_reviews/HERMES_SKILL_SUPPLY_CHAIN_MAGNUS919.md`

The existing grouped external-reference authority row covers `docs/governance/reference_reviews/`; no authority promotion is implied by that coverage.
