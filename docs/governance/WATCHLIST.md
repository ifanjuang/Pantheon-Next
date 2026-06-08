# Watchlist

Status: active support doctrine — observation and triage only.

This document defines how Pantheon Next watches external systems, technical patterns and ecosystem movements without adopting them by default.

It does not add dependencies.

It does not approve implementation.

It does not define runtime integration.

It does not authorize a scheduler, queue, provider router, tool runtime, MCP layer, plugin manager, observability backend, GraphRAG runtime, LangGraph runtime, autonomous agent team, automatic memory system, automatic skill installer or hidden workflow runner inside Pantheon Next.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The Watchlist is the observation layer for external references that may later be distilled into Pantheon governance vocabulary.

It answers:

```text
Should this reference keep being watched, distilled, rejected or archived?
```

It is broader than `SKILL_WATCHLIST.md`.

`SKILL_WATCHLIST.md` watches skill ecosystems and `SKILL.md`-style capability packages.

This document watches frameworks, methods, runtimes, observability systems, memory systems, cockpit surfaces, professional verticalization patterns, connector patterns and governance-adjacent ideas.

## Core rule

```text
Observation is not adoption.
Interest is not approval.
Popularity is not governance value.
Capability is not legitimacy.
```

A watched reference remains external until a separate governed decision changes its status.

## Watchlist record format

A watch record should remain small and reviewable.

Recommended fields:

```text
reference_name
reference_type
source_url_or_identifier
observed_date
capability_summary
pantheon_interest
risk_surface
allowed_distillation
forbidden_import
related_governance_docs
status
review_notes
```

## Status values

Recommended statuses:

```text
observe
pattern_candidate
method_review_required
boundary_required
distill_to_registry
distill_to_skill_watchlist
distill_to_hermes_candidate
reject_runtime_drift
reject_memory_drift
reject_external_effect_risk
reject_authority_drift
archive
```

## Watched domains

| Domain | Examples | Watch reason | Primary risk |
|---|---|---|---|
| Agent and workflow runtimes | LangGraph, CrewAI, AutoGen-style systems | interruption, state, handoff, external execution patterns | Pantheon becomes runtime |
| Observability and evaluation | LangSmith, Langfuse, eval platforms | traces, scores, annotations, regression review | traces become proof or approval |
| Graph RAG and knowledge graphs | GraphRAG, graph memory systems | provenance, corpus structure, contradiction maps | graph becomes truth or memory |
| Skill ecosystems | Agensi, Shokunin, `SKILL.md` repositories | skill anatomy, checks, anti-patterns | marketplace or auto-install drift |
| Contract-driven development | contracts-skill, specification preflight patterns | acceptance, verification, drift checks | technical contract becomes governance authority |
| Cockpit and UI surfaces | OpenWebUI functions, pipes, filters, actions, Knowledge Bases | user action capture and evidence exposure | cockpit becomes authority |
| Connectors and gateways | MCP servers, provider gateways, app connectors | scoped access, tool policy, least capability | plugin manager or provider router drift |
| Local-first memory and RAG | Glia-like shared memory, SQLite/vector memory | privacy, continuity, retrieval scope | shared memory becomes a Registre Probatoire entry |
| Coding agents | SmallCode, terminal agents, patch agents | patch discipline, controlled execution | coding runtime inside Pantheon |
| Professional verticalization | legal, medical, architectural or regulated-domain assistants | domain playbooks, review gates, source discipline | professional agent becomes authority |
| Prompting and reasoning methods | ReAct, debate, reflection, LLM-as-judge | method discipline and review signals | method becomes hidden orchestration |

## Current RAG and document-evaluation watch items

These records are observation and triage only. They do not approve installation, integration, OpenWebUI mutation, Hermes activation or Pantheon runtime behavior.

| Reference | Type | Pantheon interest | Primary risk | Status |
|---|---|---|---|---|
| `contextschema-py` | post-retrieval context validation | context sufficiency, freshness, provenance and invalidation checks before action | context score becomes approval authority | pattern_candidate |
| `chunk-norris` | RAG chunking evaluation | empirical comparison of chunking strategies before ingestion | retrieval score treated as proof or global KB doctrine | pattern_candidate |
| `MMLongBench-Doc` | long-document multimodal benchmark | evidence pages, source modalities, cross-page questions and unanswerable questions | benchmark score treated as professional validation | reference_review |
| Medium RAG 10M+ article | large-scale RAG architecture signal | retrieval/evidence/citation reliability vocabulary | near-zero hallucination claim treated as proof | observe |
| Reddit r/RAG discussions | practitioner weak signal | recurring RAG pain points and failure vocabulary | anecdote becomes doctrine | observe |
| `agent_memory_curator_agent` | memory admission-control reference | structured Register Candidate emission and curation reports | curator becomes a Registre Probatoire entry authority | pattern_candidate |
| `skillsgate` | skill manager / marketplace surface | skill inventory UX and compatibility surface | plugin manager, installer and marketplace drift | boundary_required |

## Triage path

A watched reference may move through the following path:

```text
external reference
→ watch record
→ boundary review
→ method review or skill watch review
→ distillation registry entry
→ candidate doctrine update or Hermes candidate constraint
→ approval decision when required
```

A reference may also be rejected immediately if it crosses a forbidden boundary.

## Routing to other documents

| If the reference is about | Route to |
|---|---|
| External system boundaries | `REFERENCE_BOUNDARIES.md` |
| Ecosystem positioning | `ECOSYSTEM_MAP.md` |
| Extracted governance pattern | `DISTILLATION_REGISTRY.md` |
| Rejected architectural pattern | `REJECTED_PATTERNS.md` |
| Skill package or `SKILL.md` ecosystem | `SKILL_WATCHLIST.md` |
| Prompting, reasoning or evaluation method | `EXTERNAL_METHOD_REVIEWS.md` |
| Persistent architectural tension | `TENSIONS_AND_RISKS.md` |
| Runtime capability or tool use | `EXTERNAL_TOOLS_POLICY.md` |
| Hermes-side execution candidate | `HERMES_INTEGRATION.md` and Task Contract review |
| OpenWebUI exposure candidate | `OPENWEBUI_INTEGRATION.md` |

## Evaluation lens

Watchlist review should ask:

```text
What capability does this show?
What governance problem does it reveal?
What can Pantheon learn without absorbing runtime responsibility?
What evidence would be needed before reuse?
What approval level would be required?
What memory risk does it create?
What external effect risk does it create?
Which existing Pantheon document should own the distilled pattern?
```

## Periodic review

Watched references should not accumulate indefinitely.

A stale watch item should be:

```text
reconfirmed
promoted to pattern candidate
moved to method review
moved to skill watchlist
recorded in rejected patterns
archived
```

Unreviewed accumulation creates architectural noise.

## Forbidden drift

The Watchlist must never become:

- dependency registry;
- vendor endorsement list;
- implementation backlog;
- runtime roadmap;
- plugin marketplace;
- MCP server catalog;
- provider router plan;
- skill installer queue;
- automatic adoption workflow;
- hidden approval mechanism;
- memory promotion queue;
- proof that a reference is safe.

If a watched item is treated as authorization, the boundary has failed.

## Relationship to approvals

Watching a reference is C0 support work.

Distilling a governance pattern may require stronger review when it changes doctrine, evidence expectations, approval posture, memory rules, integration boundaries or protected files.

Implementation remains outside this document.

## Final rule

```text
Watch broadly.
Distill narrowly.
Reject explicitly.
Never import runtime responsibility into Pantheon.
```