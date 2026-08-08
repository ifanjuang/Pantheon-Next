# Hermes Capability Bindings

Status: candidate support doctrine — Hermes capability binding registry. Repository state: documented non-implemented.

This document defines how Pantheon Next may classify candidate repositories, tools and adapters as possible Hermes-side bindings for abstract capabilities.

It does not install tools.

It does not add dependencies.

It does not create a Hermes runtime, installer, scheduler, queue, MCP server, provider router, plugin manager, memory engine, observability backend, connector runtime, OpenWebUI plugin, schema, Docker file, `.env`, operations file or platform service.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon needs a single place where product and repository names may be mentioned without polluting generic doctrine.

The registry answers:

```text
Which external binding is currently the preferred candidate for a given Hermes capability slot?
```

It does not answer:

```text
Which tool is automatically installed?
Which tool is approved for production?
Which output is proof?
Which runtime owns governance?
```

## Core rule

```text
Capability Slot -> Preferred Binding -> Status Probe -> Governance Gate
```

A binding is a candidate execution choice, not a Pantheon dependency.

```text
binding_selected != dependency_adopted
installed != approved
healthy != safe
update_available != update_authorized
runtime_success != evidence
```

## Capability slot record

A capability slot record may contain:

```text
capability_id
function
preferred_binding
fallback_bindings
watchlist_bindings
rejected_bindings
owner_layer
executed_by
governed_by
install_status
health_status
update_status
activation_status
rollback_status
allowed_outputs
forbidden_outputs
risk_surfaces
approval_floor
approval_ceiling
status_probe
review_notes
```

This is a governance-readable shape. It is not an executable schema.

## Status values

### Binding status

```text
external_reference
watch
candidate
to_verify
preferred_candidate
fallback_candidate
rejected
superseded
```

### Install status

```text
unknown
absent
proposed
pending_approval
approved_for_sandbox
installing
installed
failed
blocked
suspended
```

### Health status

```text
unknown
ready
degraded
unavailable
error
stale
```

### Update status

```text
unknown
up_to_date
update_available
security_update_available
breaking_update_available
deprecated
abandoned
```

### Activation status

```text
unavailable
detected
sandbox_enabled
project_enabled
production_enabled
suspended
rejected
```

## Selection principles

Use one preferred binding per abstract function when a preferred candidate is
actually justified. Leave a slot `unbound` when the correct choice is profile-
or project-specific.

```text
more integrations != more modularity
multiple active memory providers != safer memory
second orchestrator != stronger governance
integrated product breadth != required dependency
```

The standard Hermes distribution lock remains limited to the selected execution
bridge core. A candidate listed here does not join that lock by being reviewed.

## Tiering

### Tier 1 — candidate bindings worth framing first

These are the first candidates for Hermes capability planning. They remain documented non-implemented unless a separate implementation package exists.

| Capability slot | Preferred binding | Function | Current posture | Main risk |
|---|---|---|---|---|
| `web_evidence_intake` | `xberg-io/crawlberg` | public web intake, crawl, HTML-to-Markdown, provenance and crawl traces | preferred candidate | crawler/runtime/MCP drift; SSRF; browser rendering; antibot misuse |
| `external_connector_gateway` | Nango | scoped API connector gateway for GitHub, Drive, Calendar, Notion, Slack, Linear, CRM and business systems | candidate support doctrine | credential storage, connector marketplace, hidden external writes |
| `observability` | Langfuse | self-hostable trace, cost, latency and evaluation visibility for Hermes-side runs | preferred candidate; Hermes plugin surface reviewed, live API-server/Runs delivery not observed | traces treated as proof, approval or canonical memory; prompt/data leakage; hook-path mismatch |
| `document_structural_analysis` | Docling through a separately operated service, MCP or API binding | layout-aware blocks, headings, reading order, tables, equations, images and source-linked structured derivatives | preferred candidate; bounded MVP path already exists, target runtime acceptance not established | extraction success treated as truth; unrestricted file access; embedded RAG or vector-store sprawl |
| `document_source_management` | Paperless-ngx when selected | optional source capture, preservation, versioning, retrieval and operational document metadata | preferred optional candidate; not required for core local/NAS ingestion | DMS metadata or OCR treated as Pantheon classification, Evidence or project truth |
| `structural_repo_analysis` | `Lum1104/Understand-Anything` | repository, documentation and knowledge-base structure review | Hermes Skill Candidate | generated graph treated as truth or memory |
| `revit_local_adapter` | Pantheon Revit Gate local plugin | local Revit context, capability registry, light write actions and logs | local sandbox exception candidate | model mutation, professional validation confusion, save/sync/delete risk |
| `agent_artifact_transfer` | `shehryarsaroya/agenttransfer` | governed transfer of files, artifacts and handoff packages between agents, humans and runtimes | candidate to verify | transport receipts treated as proof; external-send drift; MCP bridge mistaken for Pantheon runtime |

### Tier 2 — useful alternatives and bounded component sources

| Capability slot | Candidate bindings | Use | Main risk |
|---|---|---|---|
| `knowledge_retrieval_pipeline` | Haystack; compare LlamaIndex and selected LangChain components | scoped retrieval, metadata filtering, ranking/reranking and provenance-linked context over governed material | the retrieval framework must not broaden into an agent runtime, provider router or evidence authority |
| `enterprise_search` | Onyx | enterprise search, connectors, access and query audit patterns | broad knowledge exposure and connector sprawl |
| `local_knowledge_workspace` | AnythingLLM | simple local-first chat-with-docs and workspace UX | workspace confused with governed dossier |
| `multi_surface_assistant` | Khoj | multi-surface knowledge assistant patterns | second-brain recall treated as truth |
| `workflow_visualization` | Langflow, Dify, Flowise | visual prototyping and one bounded exported flow behind Hermes | visual builder becoming a second production orchestrator or approval path |
| `graph_provenance` | Microsoft GraphRAG | entity, relationship, claim and corpus graph patterns | graph becomes proof, memory or doctrine |
| `structured_output_validation` | Guardrails AI | candidate output and field-level validation checks | validator pass treated as human approval |
| `contract_preflight` | `kombifyio/contracts-skill` | contract discipline, preflight, trace IDs and drift checks | technical contract treated as governance authority |

### Tier 3 — watch, profile-specific or refuse as default runtime

| Capability slot | Candidate bindings | Decision / reason to defer |
|---|---|---|
| `external_runtime_memory` | Hindsight as the first sandbox candidate and bundled Hermes 0.20.0 provider; Mnemosyne as the second, third-party local-first fallback candidate; Mem0 as the third Hermes provider comparison candidate; Honcho, OpenViking, Holographic, RetainDB, ByteRover and Supermemory remain upstream alternatives | leave unbound for Pantheon. For `assistant-personal` sandbox evaluation, preference order is Hindsight → Mnemosyne → Mem0. Hermes allows one external provider at a time and keeps built-in memory additive. External memory is refused in `pantheon-governed`. The official `vectorize-io/hindsight-obsidian` v0.2.0 one-way source connection is sandbox-qualified for Hindsight on `assistant-personal`: bounded tests proved create/edit/delete/rename reconciliation, unchanged-note deduplication, strict vault/folder filtering, exact source path metadata and Hermes recall from the same bank without duplicate ingestion. It remains an optional source connection, not a Pantheon binding or authority. |
| `bounded_workflow_runtime` | LangGraph | refuse as Pantheon or default Hermes runtime. Revisit only for one demonstrated stateful workflow gap exposed behind a bounded capability contract. |
| `document_parsing_rag_ingestion` | RAGFlow | watch/reference only by default. Its integrated parser, retrieval, agents, workflows, memory, MCP, models and UI duplicate selected replaceable slots. Do not adopt as the platform stack. |
| `agent_pattern_catalog` | `NirDiamant/GenAI_Agents` | useful pattern source, not architecture |
| `skill_lifecycle` | Shokunin / Agensi | strong skill lifecycle patterns but high memory/runtime/auto-install risk |
| `scoped_authorization` | Permify, Ory Keto, Casbin | future optional guardrail, not MVP dependency |
| `policy_checking` | Open Policy Agent | future policy evaluation, not approval engine |
| `versioned_provenance` | Dolt, TerminusDB | semantic inspiration, not early database replacement |

The `external_runtime_memory` ordering is a sandbox evaluation preference only.
It does not bind the Pantheon capability slot, add a dependency to the standard
Hermes distribution, authorize installation or permit external memory in the
`pantheon-governed` runtime mode.

The qualified Obsidian source path is similarly bounded:

```text
Obsidian vault
-> official one-way hindsight-obsidian sync
-> Hindsight bank
-> scoped Hermes assistant-personal recall
```

Observed sandbox constraints remain part of that qualification:

```text
sync accepted != materialized
Hindsight recall != truth
Obsidian note != Pantheon Evidence
assistant-personal memory != pantheon-governed Context Pack
```

The upstream sync client submits retains asynchronously, so a completed reconcile
means the operation was accepted, not necessarily materialized by the Hindsight
worker. Consumers that depend immediately on a newly synchronized note must account
for that latency. This does not create a new Pantheon state or authorization.

## Capability slot examples

### `web_evidence_intake`

```text
capability_id: web_evidence_intake
function: public web intake with provenance
preferred_binding: xberg-io/crawlberg
fallback_bindings: onyx-dot-app/onyx, khoj-ai/khoj
owner_layer: execution_runtime
executed_by: Hermes
governed_by: Pantheon
binding_status: preferred_candidate
install_status: unknown
health_status: unknown
update_status: unknown
activation_status: unavailable
allowed_outputs: Result Candidate, Evidence Pack Candidate, Capability Gap
forbidden_outputs: approval, proof, canonical memory, unapproved external action
risk_surfaces: SSRF, robots policy, browser rendering, authentication, antibot bypass, private network access
```

### `external_connector_gateway`

```text
capability_id: external_connector_gateway
function: scoped third-party API access through Hermes
preferred_binding: Nango
owner_layer: execution_runtime / connector gateway
executed_by: Hermes
governed_by: Pantheon
binding_status: candidate
allowed_outputs: External API Result Candidate, Connector Trace Summary, Evidence Pack Candidate, Capability Gap
forbidden_outputs: raw credentials, automatic external write, hidden webhook, automatic memory promotion, connector marketplace semantics
risk_surfaces: OAuth scopes, provider-wide access, sensitive logs, third-party mutation
```

### `observability`

```text
capability_id: observability
function: Hermes run traces, cost, latency and status summaries
preferred_binding: Langfuse
fallback_bindings: LangSmith, Opik
owner_layer: observability layer
executed_by: Hermes / observability adapter
governed_by: Pantheon
binding_status: preferred_candidate
install_status: not established
activation_status: unavailable
live_path_validation: required for API server, OpenWebUI and Runs paths
allowed_outputs: Trace Summary Candidate, Runtime Status Candidate, Regression Review Candidate
forbidden_outputs: proof, approval, canonical memory, Evidence Pack replacement
risk_surfaces: trace leakage, prompt leakage, score-as-validation drift, retention policy, plugin-hook path drift
```

### `document_structural_analysis`

```text
capability_id: document_structural_analysis
function: produce source-linked layout-aware structural derivatives
preferred_binding: Docling
owner_layer: external document-analysis runtime
executed_by: Docling service / MCP / API under Hermes orchestration
governed_by: Pantheon
binding_status: preferred_candidate
install_status: not established on target
activation_status: unavailable
allowed_outputs: Document Derivation Candidate, Extraction Candidate, Evidence Pack Candidate material, Capability Gap
forbidden_outputs: source truth, Evidence admission, professional validation, automatic Knowledge publication
risk_surfaces: path escape, malformed documents, OCR/layout mismatch, missing pages, table corruption, remote model transmission
```

### `external_runtime_memory`

```text
capability_id: external_runtime_memory
function: optional cross-session recall for a non-governed personal-assistant profile
preferred_binding: unbound
sandbox_preference_order: Hindsight, Mnemosyne, Mem0
candidate_bindings: Hindsight, Mnemosyne, Mem0
owner_layer: execution runtime / external memory store
executed_by: selected Hermes memory provider or bounded third-party adapter
governed_by: Pantheon only at the boundary of consequential work
binding_status: watch / sandbox_only
allowed_profiles: assistant-personal
forbidden_profiles: pantheon-governed
allowed_outputs: Recall Candidate, Register Candidate, Runtime Memory Trace Reference
forbidden_outputs: canonical memory, Evidence admission, approval, scope expansion, automatic project mutation
risk_surfaces: hidden prompt injection, background writes, cross-scope leakage, stale recall, deletion ambiguity, non-exportable memory
optional_source_connections: Obsidian -> Hindsight via official vectorize-io/hindsight-obsidian v0.2.0 (sandbox-qualified)
source_connection_status: qualified_for_assistant_personal_sandbox
source_connection_scope: explicit vault/folder tags with all_strict recall filtering
source_connection_retention: conversation retention off; Obsidian vault remains source of truth for synchronized notes
source_connection_runtime_note: retain is asynchronous; reconcile accepted != Hindsight materialized
observed_sandbox: pantheon-mvp#291, pantheon-mvp#295, pantheon-mvp#296
review_notes: Hindsight remains first for sandbox evaluation; Mnemosyne is the second local-first fallback; Mem0 is the third comparison candidate. The qualified Obsidian path is an optional Hindsight source connection only. The order and source qualification do not bind the Pantheon slot, authorize production activation or permit external memory in pantheon-governed.
```

### `revit_local_adapter`

```text
capability_id: revit_local_adapter
function: local Revit model inspection, context packs, candidate actions, light sandbox writes and action logs
preferred_binding: Pantheon Revit Gate local plugin
owner_layer: Revit local plugin / Hermes local side
executed_by: Revit plugin under Hermes orchestration
governed_by: Pantheon
binding_status: candidate
install_status: not_implemented
health_status: unknown
activation_status: unavailable
allowed_outputs: Visual Context Pack Candidate, Action Log Candidate, Method Candidate, Review Action Candidate, Capability Gap
forbidden_outputs: professional validation, automatic save, sync, purge, delete, linked-model write, arbitrary generated code execution
risk_surfaces: live model mutation, phases, families, worksharing, pinned/grouped elements, production files
```

## Installation posture

This registry may mark a binding as installable or proposed, but it never installs.

A binding may move through:

```text
watch
-> reference_review
-> hermes_binding_candidate
-> installation_proposal
-> approved_for_sandbox
-> installed_by_Hermes
-> health_reported
-> project_enabled
-> deprecated / replaced / rejected
```

Each transition requires a record and may require a human gate depending on risk.

## Update posture

Update detection is allowed as a governance signal.

```text
update_available != update_authorized
security_update_available != auto_update
breaking_update_available = review_required
```

Pantheon may display update status, risk and decision state. Hermes or an operator performs the update only after the required approval path.

## Replacement rule

A preferred binding may be replaced when:

```text
health is persistently degraded
repo is abandoned
security risk is unacceptable
capability gap remains unresolved
better binding is reviewed
scope changes
professional risk changes
```

Replacement is not retroactive approval of the new binding. It restarts review at the appropriate status.

## Rejected collapses

The registry must never become:

```text
dependency registry
vendor endorsement list
plugin marketplace
install queue
runtime roadmap
auto-update plan
MCP catalog
provider router plan
approval shortcut
memory promotion queue
proof of safety
```

## Relationship to Pantheon Control

The control-plane status vocabulary is defined in:

```text
docs/governance/PANTHEON_CONTROL_PLANE_BOUNDARY.md
```

This registry supplies candidate bindings for that control plane.

## Status

```text
implemented: no
runtime_added: no
schemas_added: no
protected_paths_touched: no
repo_state: documented non-implemented
```

## Final rule

```text
Choose one binding per function for clarity.
Leave profile-specific slots unbound until selected.
Keep fallbacks visible.
Do not adopt dependencies by implication.
Hermes executes.
Pantheon governs.
The human decides.
```
