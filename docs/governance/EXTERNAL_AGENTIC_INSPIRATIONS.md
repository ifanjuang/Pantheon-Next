# External Agentic Inspirations

Status: active support appendix — inspiration and distillation only.

This document extends `EXTERNAL_REPO_INSPIRATIONS.md` for agentic runtimes, observability systems, graph-based RAG and skill ecosystems.

It does not add dependencies.

It does not approve implementation.

It does not define runtime integration.

It does not authorize a LangGraph runtime, agent runtime, MCP layer, observability backend, skill installer, scheduler, queue, provider router, automatic memory system or hidden workflow runner inside Pantheon Next.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Agentic and observability systems show what modern AI stacks can execute, trace, evaluate, remember or automate.

Pantheon Next must not copy those systems.

Pantheon Next should distill their useful patterns into governance vocabulary:

```text
scope
source status
evidence status
approval threshold
memory status
auditability
runtime drift risk
```

The governing rule is:

```text
External systems show capabilities.
Pantheon defines the governance conditions under which those capabilities may be used.
```

## Distillation grid

Every external agentic pattern should be reviewed through the same grid.

| Field | Purpose |
|---|---|
| External system | The project, product or repository being studied. |
| Capability shown | What the system can do operationally. |
| Pantheon concern | Which governance concern the capability touches. |
| Allowed distillation | What Pantheon may learn from it. |
| External execution surface | Where implementation may belong, usually Hermes or another external runtime. |
| OpenWebUI exposure surface | What the cockpit may display or capture. |
| Evidence expectation | What must be reviewable. |
| Approval implication | Which approval threshold may be involved. |
| Memory implication | Whether the output may only become a Register Candidate. |
| Forbidden import | What must not enter Pantheon Next. |
| Status | Inspiration only, candidate proposal, deferred or rejected. |

## LangGraph

Source: official LangGraph documentation.

LangGraph is a low-level orchestration framework and runtime for long-running, stateful agents. Its documented capabilities include durable execution, streaming, human-in-the-loop, persistence, memory and subgraphs.

Useful patterns:

- explicit state transitions;
- human-in-the-loop interruption points;
- resumable long-running work;
- graph-shaped execution traces;
- subgraph decomposition;
- runtime state visibility.

Pantheon distillation:

```text
Use LangGraph as an external runtime reference for Hermes-side execution patterns.
Do not introduce LangGraph as a Pantheon runtime.
```

Potential Pantheon relevance:

- Run Trace View vocabulary;
- approval interruption semantics;
- capability-gap reporting;
- external runtime evidence summaries;
- anti-runtime drift tests.

Risks:

- turning Workflow Manifest into an executable graph;
- treating runtime state as Evidence Pack;
- treating LangGraph memory as a Registre Probatoire entry;
- making Pantheon depend on graph execution;
- introducing a central LangGraph runtime.

Forbidden import:

```text
LangGraph runtime
StateGraph execution
checkpoint memory
scheduler or retry semantics
worker state
subgraph runtime
provider orchestration
```

## LangSmith

Source: official LangSmith documentation.

LangSmith is a framework-agnostic platform for building, debugging and deploying AI agents and LLM applications. It supports tracing, evaluation, prompt testing, deployment, audit logs and platform setup.

Useful patterns:

- trace inspection;
- prompt versioning;
- evaluation datasets;
- experiment comparison;
- audit logs;
- deployment visibility;
- debugging workflow.

Pantheon distillation:

```text
Use LangSmith as inspiration for observability summaries, eval reports and AI usage registers.
Do not treat LangSmith traces or evals as Pantheon approval.
```

Potential Pantheon relevance:

- Evidence Pack support material;
- AI usage register;
- prompt review record;
- quality review report;
- regression report for Hermes-side skills;
- audit-ready export vocabulary.

Risks:

- trace equals evidence fallacy;
- eval pass equals approval fallacy;
- deployment surface becomes Pantheon runtime;
- prompt version treated as doctrine;
- cloud observability treated as canonical record.

Forbidden import:

```text
LangSmith deployment
LangSmith as source of truth
trace store as Evidence Pack
experiment pass as approval
prompt registry as doctrine
```

## Langfuse

Source: official Langfuse documentation.

Langfuse is an open-source, self-hostable and extensible LLM engineering platform for debugging, analyzing and iterating on LLM applications. It includes observability, prompt management, evaluation, metrics and API/data platform features.

Useful patterns:

- self-hostable LLM observability;
- trace logging;
- cost and latency visibility;
- prompt version control;
- evaluation workflows;
- production health monitoring;
- data export posture;
- session and user tracking;
- agent graph representation.

Pantheon distillation:

```text
Use Langfuse as the preferred observability inspiration when local-first or self-hostable posture matters.
Do not make Langfuse a memory authority, approval authority or Evidence Pack replacement.
```

Potential Pantheon relevance:

- Hermes-side observability candidate;
- OpenWebUI display of trace summaries;
- audit-ready export support;
- quality and cost review;
- prompt change review;
- AI usage register;
- Setup Doctor observability checklist.

Risks:

- observability dashboard mistaken for governance dashboard;
- traces mistaken for proof;
- prompt management mistaken for doctrine management;
- eval scores mistaken for professional validation;
- user/session tracking leaking into memory without approval.

Forbidden import:

```text
Langfuse as a Registre Probatoire entry
Langfuse as approval authority
Langfuse as Pantheon dashboard runtime
Langfuse trace store as Evidence Pack
automatic trace-to-memory promotion
```

## GraphRAG and graph-based RAG

Source: Microsoft GraphRAG documentation and research.

GraphRAG is a structured and hierarchical approach to retrieval-augmented generation. It extracts a knowledge graph from raw text, builds community hierarchies, generates community summaries and uses global, local or DRIFT-style query modes.

Useful patterns:

- text units with fine-grained references;
- entity extraction;
- relationship extraction;
- claim extraction;
- graph community detection;
- community summaries;
- global search for corpus-level questions;
- local search for entity-level questions;
- DRIFT search combining local and community context;
- graph visualization of corpus structure.

Pantheon distillation:

```text
Use GraphRAG as inspiration for structured corpus preparation and graph-based retrieved context.
Do not treat a generated graph as proof, memory or doctrine.
```

Potential Pantheon relevance:

- RAG Ingestion Pipeline extension;
- source graph manifest;
- contradiction graph;
- evidence candidate selection;
- project dossier map;
- corpus-level synthesis with visible limits;
- retrieval quality review.

Risks:

- knowledge graph equals truth fallacy;
- community summary equals evidence fallacy;
- graph centrality equals authority fallacy;
- generated relationship becomes a Registre Probatoire entry;
- graph pipeline becomes Pantheon runtime.

Forbidden import:

```text
GraphRAG indexing runtime
GraphRAG query runtime
automatic graph-to-evidence conversion
automatic graph-to-memory promotion
graph database as governance source of truth
```

Governed chain:

```text
Raw Source
→ structured source graph
→ retrieved graph context
→ Evidence Candidate
→ Evidence Pack
→ Approval Event
→ Register Candidate
→ Registre Probatoire entry
```

## GenAI_Agents

Source: `NirDiamant/GenAI_Agents`.

GenAI_Agents is a large educational and implementation repository for generative AI agents. It includes examples across LangGraph, LangChain, MCP, RAG, memory, multi-agent collaboration, contract analysis, browser automation, email, self-improvement, testing and content generation.

Useful patterns:

- broad agent-pattern catalog;
- tutorial structure;
- professional use-case examples;
- contract analysis pattern;
- system-inspector pattern;
- RAG evaluation pattern;
- visual explanation discipline;
- comparison between implementations.

Pantheon distillation:

```text
Use GenAI_Agents as a catalog of external patterns that Pantheon should know how to govern.
Do not use it as Pantheon architecture.
```

Potential Pantheon relevance:

- professional dossier pattern library;
- Hermes skill candidate review;
- Governance Doctor inspiration;
- Evidence Pack completeness checks;
- retrieval evaluation signals;
- pattern cards for external capabilities.

Risks:

- tutorial code mistaken for production architecture;
- agent roles confused with Pantheon Roles;
- LangGraph centrality;
- autonomous research drift;
- self-improvement mistaken for governance;
- memory loops mistaken for a Registre Probatoire entry.

Forbidden import:

```text
agent runtime
notebook execution dependency
LangGraph workflow core
self-improving agent
memory-enhanced agent
browser automation agent
email agent
provider wiring
```

## Shokunin

Source: `EliasOulkadi/shokunin`.

Shokunin is a developer-oriented AI ecosystem built around persistent memory, `SKILL.md` files, multi-strategy recall, ChromaDB, MCP servers, OpenCode configuration, scripts, subagents, dashboards and declarative self-updates.

Useful patterns:

- `SKILL.md` anatomy;
- YAML frontmatter with name and description;
- trigger-focused skill descriptions;
- progressive disclosure;
- bundled scripts and references;
- production checklists;
- anti-patterns;
- cited sources;
- skill creation lifecycle;
- skill evals;
- benchmark with and without skill;
- human feedback loop;
- package and compatibility thinking.

Pantheon distillation:

```text
Use Shokunin as strong inspiration for Skill Candidate lifecycle and Hermes skill pack design.
Reject its memory, MCP, auto-save, scheduler and self-update mechanisms as Pantheon core patterns.
```

Potential Pantheon relevance:

- future `SKILL_LIFECYCLE.md` reconciliation;
- Skill Candidate review checklist;
- Hermes Profile Pack conventions;
- skill eval report;
- skill source requirements;
- skill anti-pattern library;
- Setup Doctor checklist for skill sprawl.

Risks:

- persistent ChromaDB memory mistaken for a Registre Probatoire entry;
- auto-save wrapper causing accidental memory capture;
- MCP servers becoming hidden runtime;
- one-command installer drift;
- scheduler and dashboard drift;
- declarative self-updates becoming self-evolution;
- skills auto-activating without Task Contract.

Forbidden import:

```text
ChromaDB memory as Pantheon memory
context search on every start as governance rule
auto-save to memory
MCP server installation
one-command install scripts
scheduler
dashboard runtime
declarative self-updates
skill auto-installer
subagent runtime
```

Governed chain:

```text
External skill idea
→ Skill Candidate
→ Task Contract fit
→ evidence and source review
→ eval report
→ human review
→ approved governance wrapper
→ optional Hermes execution skill
```

## Priority ranking

Recommended inspiration priority for Pantheon Next:

```text
1. Shokunin
   Best inspiration for Skill Candidate lifecycle, but highest memory/runtime drift risk.

2. Langfuse
   Best observability inspiration for local-first and self-hostable posture.

3. GraphRAG
   Best inspiration for complex corpus structure and graph-based retrieval status.

4. GenAI_Agents
   Best broad catalog for pattern cards and professional use-case discovery.

5. LangGraph
   Important external runtime reference, mainly for Hermes boundary doctrine.

6. LangSmith
   Useful observability and eval reference, strongest when LangChain/LangGraph is already used.
```

## Candidate future pattern cards

A future follow-up may define pattern cards for:

```text
Contract Analysis Pattern
Governance Doctor Pattern
Retrieval Evaluation Pattern
Skill Candidate Lifecycle Pattern
Observability-to-Evidence Summary Pattern
GraphRAG Source Graph Pattern
```

Each card must remain support doctrine until a separate governed adoption decision exists.

## Status

Research and support doctrine only.

No dependency added.

No implementation started.

No OpenWebUI plugin added.

No Hermes tool added.

No observability backend added.

No GraphRAG runtime added.

No LangGraph runtime added.

No MCP server added.

No skill installer added.

No memory system added.

No schema added.

No tests added.

No operations tooling added.
