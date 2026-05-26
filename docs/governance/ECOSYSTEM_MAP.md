# Ecosystem Map

Status: active support doctrine — ecosystem positioning only.

This document maps external AI systems, capability families and integration surfaces around Pantheon Next.

It does not add dependencies.

It does not approve implementation.

It does not define runtime architecture.

It does not authorize Pantheon Next to become an execution runtime, provider router, MCP router, observability backend, GraphRAG runtime, skill marketplace, scheduler, queue or plugin manager.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The ecosystem map prevents conceptual collapse.

Many AI systems use similar words:

```text
agent
memory
workflow
tool
skill
trace
knowledge
approval
```

Pantheon must map those words to its own governance categories before adopting any pattern.

## Three-party anchor

| Layer | Pantheon relation | What belongs here |
|---|---|---|
| OpenWebUI | cockpit and exposure surface | chat, files, Knowledge Bases, approval prompts, Evidence Pack display, user decision capture |
| Hermes Agent | external execution runtime | profiles, skills, tools, workers, terminal, patch candidates, memory candidates, Evidence Pack production |
| Pantheon Next | governance layer | doctrine, roles, Task Contracts, approvals, Evidence Pack rules, memory policy, scope isolation, external tool policy |

No external reference may blur this anchor without a boundary review.

## Ecosystem families

| Family | Examples | Pantheon relation | Main governance question |
|---|---|---|---|
| User cockpit | OpenWebUI, chat UIs, document portals | exposure surface | What can the user see, select, approve or reject? |
| Execution runtime | Hermes, LangGraph, coding agents, agent teams | external runtime or inspiration | What executes, under which Task Contract? |
| Observability | LangSmith, Langfuse, eval dashboards | evidence-support inspiration | What trace summary is reviewable without becoming proof? |
| Retrieval and RAG | OpenWebUI Knowledge, vector stores, GraphRAG, local RAG | knowledge and evidence-support layer | What was retrieved, and what actually supports a claim? |
| Memory systems | shared memory layers, agent memories, ChromaDB-like memory | tension source | What may become Memory Candidate, and what is forbidden? |
| Tool and connector layers | MCP, APIs, browser tools, email/calendar/document connectors | external capability surfaces | What is authorized, least-capability and evidence-bound? |
| Skill ecosystems | Agensi, Shokunin, `SKILL.md` repositories | watch and distillation source | What pattern is useful without auto-installing capability? |
| Method catalogs | ReAct, reflection, debate, LLM-as-judge, planner/executor | method review source | Does the method improve review or hide orchestration? |
| Professional verticals | legal, medical, architectural assistants | domain inspiration | What review gates protect professional responsibility? |
| Governance repository | Pantheon Next | source of doctrine | What remains validated, scoped and reviewable? |

## Authority map

Pantheon does not rank systems by power.

It ranks artifacts by governance authority.

```text
Doctrine governs.
Approvals validate.
Canonical Memory persists.
Evidence supports.
Task Contracts bound work.
Context Packs scope work.
Knowledge Items inform work.
Raw Sources provide material.
Runtime outputs propose candidates.
```

External systems usually produce lower-authority artifacts unless Pantheon governance promotes them through evidence and approval.

## Capability map

| Capability | May belong to | Must not become |
|---|---|---|
| Chat and file selection | OpenWebUI | source of truth |
| User approval display | OpenWebUI | automatic approval engine |
| Tool execution | Hermes or external runtime | Pantheon tool runtime |
| Terminal use | Hermes or controlled external execution | Pantheon terminal runtime |
| Workflow execution | Hermes or external runtime | Pantheon workflow engine |
| Runtime state | Hermes or external runtime | Canonical Memory |
| Trace logging | observability platform or Hermes | Evidence Pack by itself |
| Evidence selection | Pantheon governance expectation, possibly produced by Hermes | raw trace dump |
| Memory proposal | Hermes or governance review | automatic memory promotion |
| Canonical memory | Pantheon governance | vector store, retrieval cache or agent memory |
| Skill operation | Hermes candidate skill | Pantheon marketplace or installer |
| Provider routing | external runtime or gateway | Pantheon router |
| MCP serving | external capability surface | internal Pantheon MCP layer |
| Graph indexing | external RAG pipeline | Pantheon truth engine |

## Import zones

### Green zone — governance vocabulary

Allowed:

- status names;
- checklist structure;
- evidence fields;
- review gates;
- scope labels;
- contradiction categories;
- trace-summary vocabulary;
- skill-card anatomy;
- acceptance and verification trace concepts.

### Yellow zone — candidate constraints

Requires review:

- Hermes candidate skill constraints;
- OpenWebUI exposure candidates;
- Context Pack adapters;
- evidence-summary formats;
- method review cards;
- professional-domain playbooks;
- read-only Doctor checks.

### Red zone — forbidden imports

Forbidden inside Pantheon:

- runtime execution;
- scheduling;
- queueing;
- hidden workflow orchestration;
- provider routing;
- tool dispatch;
- automatic memory promotion;
- autonomous agent teams;
- MCP server layer;
- plugin marketplace;
- automatic skill installation;
- observability backend;
- GraphRAG runtime;
- self-evolution;
- auto-approval.

## External system interpretation table

| External system type | Treat as | Do not treat as |
|---|---|---|
| Runtime framework | capability reference | Pantheon architecture target |
| Observability platform | trace and eval inspiration | approval or proof authority |
| Knowledge graph system | retrieval structure inspiration | truth or memory authority |
| Skill marketplace | pattern discovery surface | approved capability source |
| Coding agent | external execution pattern | Pantheon implementation model |
| Shared memory system | continuity-risk case study | Canonical Memory model |
| Professional AI suite | domain review inspiration | professional decision maker |
| Connector or MCP server | external tool surface | internal Pantheon plugin |

## Relationship to related documents

| Document | Role in ecosystem control |
|---|---|
| `WATCHLIST.md` | observes external references |
| `REFERENCE_BOUNDARIES.md` | defines what references may and may not authorize |
| `EXTERNAL_AGENTIC_INSPIRATIONS.md` | contains detailed agentic reference reviews |
| `SKILL_WATCHLIST.md` | watches skill ecosystems |
| `DISTILLATION_REGISTRY.md` | records patterns actually extracted |
| `REJECTED_PATTERNS.md` | records architectural refusals |
| `EXTERNAL_METHOD_REVIEWS.md` | reviews reasoning and workflow methods |
| `TENSIONS_AND_RISKS.md` | preserves permanent governance tensions |
| `EXTERNAL_TOOLS_POLICY.md` | governs external capability surfaces |
| `HERMES_INTEGRATION.md` | defines runtime boundary |
| `OPENWEBUI_INTEGRATION.md` | defines cockpit boundary |

## Failure modes

Ecosystem mapping has failed when:

- a system name replaces a Pantheon category;
- a runtime feature becomes a governance requirement;
- a trace is treated as evidence without selection;
- a score is treated as approval;
- a retrieved item is treated as truth;
- a graph is treated as memory;
- a watched skill becomes installed by default;
- OpenWebUI display becomes authority;
- Hermes completion becomes validation;
- Pantheon must run for external execution to occur.

## Final rule

```text
Map capabilities before importing vocabulary.
Map authority before trusting outputs.
Map boundaries before designing integration.
```