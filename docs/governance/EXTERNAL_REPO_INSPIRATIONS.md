# External Repository Inspirations

Status: active support doctrine — inspiration map only.

This document records external open-source repositories that may inspire Pantheon Next governance design.

It does not add dependencies.

It does not authorize implementation.

It does not define runtime integration.

It does not approve plugins, connectors, tools, schedulers, queues, provider routers, workflow engines, agent runtimes or memory systems.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Next should learn from existing open-source systems without becoming a clone of them.

The market already contains:

- RAG platforms;
- enterprise search systems;
- chat-with-docs tools;
- agent builders;
- workflow canvases;
- authorization services;
- versioned data stores;
- output validation libraries.

Pantheon Next should not compete by becoming another one of these.

Pantheon Next should distill useful patterns into governance doctrine while keeping its own differentiator:

```text
source ≠ retrieved knowledge ≠ evidence ≠ approval ≠ memory
```

## Core rule

External repositories are inspirations.

They are not Pantheon doctrine by themselves.

They are not dependencies by default.

They are not implementation decisions.

They are not authority.

Any future adoption, wrapper or integration must pass through:

- Task Contract scope;
- External Tools Policy;
- Evidence Pack expectations;
- approval requirements;
- memory rules;
- anti-runtime drift review.

## Evaluation lens

External repositories should be evaluated by asking:

| Question | Why it matters |
|---|---|
| What problem does this project solve well? | Avoid copying the whole system when only one pattern is useful. |
| Does it reinforce or weaken Pantheon doctrine? | Keep governance separate from execution. |
| Does it blur source, evidence, approval or memory? | Reject patterns that collapse the trust chain. |
| Does it require runtime ownership? | Reject runtime drift into Pantheon. |
| Can it inspire a modular optional component? | Prefer replaceable edges over core dependency. |
| Is it useful for MVP or only advanced scale? | Avoid overbuilding before proof. |

## Inspiration map

### RAGFlow

Repository: `infiniflow/ragflow`

Useful patterns:

- deep document understanding;
- document parsing;
- template-based chunking;
- visible and explainable chunking;
- traceable citations;
- heterogeneous source ingestion;
- enterprise-scale RAG workflow.

Pantheon distillation:

```text
Use as inspiration for ingestion transparency, chunk provenance and citation display.
Do not import RAGFlow as Pantheon runtime.
```

Potential Pantheon relevance:

- future retrieval backend comparison;
- source lineage model;
- citation UX;
- chunk visualization;
- document parsing quality criteria.

Risks:

- turning Pantheon into a RAG engine;
- treating retrieval as proof;
- merging agentic RAG with governance authority.

### Onyx

Repository: `onyx-dot-app/onyx`

Useful patterns:

- enterprise search;
- many indexing connectors;
- RAG and web search;
- deep research workflow;
- custom agents;
- artifacts;
- actions and MCP;
- role-based access control;
- analytics and query history;
- enterprise deployment posture.

Pantheon distillation:

```text
Use as inspiration for enterprise search, access control, connector posture and audit surfaces.
Do not turn Pantheon into the enterprise search platform.
```

Potential Pantheon relevance:

- connector inventory thinking;
- RBAC and team access concepts;
- query audit ideas;
- artifact display patterns;
- enterprise vocabulary.

Risks:

- broad automatic knowledge exposure;
- tool and connector sprawl;
- query history treated as memory;
- custom agents treated as governance roles.

### AnythingLLM

Repository: `Mintplex-Labs/anything-llm`

Useful patterns:

- local-first positioning;
- simple chat-with-docs adoption;
- workspaces;
- multi-user access;
- source citations;
- no-friction setup;
- broad vector database and provider support.

Pantheon distillation:

```text
Use as inspiration for MVP simplicity and user-facing trust language.
Do not confuse workspace convenience with governed dossier state.
```

Potential Pantheon relevance:

- first-use simplicity;
- workspace mental model;
- local-first communication;
- source citation affordances;
- professional onboarding flow.

Risks:

- workspace equals dossier fallacy;
- local-first overpromise if external providers are used;
- document upload treated as validation.

### Khoj

Repository: `khoj-ai/khoj`

Useful patterns:

- personal-to-enterprise knowledge assistant;
- multi-surface access;
- browser, desktop, mobile and messaging surfaces;
- Obsidian and editor-like workflows;
- custom agents with knowledge, persona and tools;
- semantic search across documents and web.

Pantheon distillation:

```text
Use as inspiration for multi-surface cockpit thinking.
Do not treat second-brain recall as a Registre Probatoire entry.
```

Potential Pantheon relevance:

- future Google Docs, Obsidian, desktop or messaging cockpit mapping;
- personal-to-organization scaling narrative;
- assistant surfaces beyond OpenWebUI.

Risks:

- uncontrolled personal memory drift;
- recall treated as truth;
- agent persona confused with Pantheon Role.

### Dify

Repository: `langgenius/dify`

Useful patterns:

- visual workflow canvas;
- RAG pipeline;
- agent capabilities;
- model management;
- observability integrations;
- application logs and annotations;
- API-first integration posture.

Pantheon distillation:

```text
Use as inspiration for workflow visualization and observability.
Do not import workflow execution into Pantheon.
```

Potential Pantheon relevance:

- Run Trace View presentation;
- workflow diagram ideas;
- production observation concepts;
- annotation of results and model behavior.

Risks:

- hidden workflow runtime;
- provider router drift;
- visual workflow treated as governance truth.

### Flowise

Repository: `FlowiseAI/Flowise`

Useful patterns:

- visual AI agent construction;
- node/component decomposition;
- low-code experimentation;
- visible agent flow diagrams.

Pantheon distillation:

```text
Use for visual and modular thinking only.
Do not adopt a hidden graph runtime or plugin marketplace model.
```

Potential Pantheon relevance:

- diagrams for explaining modular pipelines;
- component boundary inspiration;
- optional visual workflow illustrations.

Risks:

- LangGraph-like runtime drift;
- node sprawl;
- plugin-manager temptation;
- execution semantics leaking into governance docs.

### Permify, Ory Keto and Casbin

Repositories:

- `Permify/permify`;
- `ory/keto`;
- `apache/casbin`.

Useful patterns:

- fine-grained authorization;
- RBAC, ABAC and ReBAC models;
- resource-level access checks;
- tenant isolation;
- centralized authorization reasoning;
- policy-based access control.

Pantheon distillation:

```text
Use as inspiration for future scoped Knowledge access and dossier authorization.
Do not add a full authorization service before the MVP needs it.
```

Potential Pantheon relevance:

- KnowledgeSelection permissions;
- project/dossier scope checks;
- read-only gateway authorization;
- tenant or organization isolation.

Risks:

- overbuilding the MVP;
- adding an authorization runtime inside Pantheon;
- confusing runtime permissions with approval legitimacy.

### TerminusDB and Dolt

Repositories:

- `terminusdb/terminusdb`;
- `dolthub/dolt`.

Useful patterns:

- versioned data;
- commits;
- diffs;
- time-travel queries;
- data provenance;
- reviewable data evolution.

Pantheon distillation:

```text
Use as inspiration for evidence, deliverable and memory versioning semantics.
Do not replace Postgres early or make specialized versioned databases a prerequisite.
```

Potential Pantheon relevance:

- Register Candidate supersession;
- a Registre Probatoire entry revocation;
- deliverable version history;
- Evidence Pack lineage;
- diff-based review.

Risks:

- premature database replacement;
- versioned storage confused with governance approval;
- data commits treated as professional validation.

### Guardrails AI

Repository: `guardrails-ai/guardrails`

Useful patterns:

- structured output validation;
- validators;
- schema-like response checks;
- guardrail patterns;
- claim or field-level validation thinking.

Pantheon distillation:

```text
Use as inspiration for structured checks.
Do not treat validator success as human approval.
```

Potential Pantheon relevance:

- citation-required checks;
- unsupported-claim flags;
- output candidate format checks;
- coherence review scaffolding;
- Evidence Pack completeness checks.

Risks:

- validator pass mistaken for validation;
- hidden validation logic;
- loss of professional review threshold.

### Open Policy Agent

Repository: `open-policy-agent/opa`

Useful patterns:

- policy-as-code;
- decision separation;
- auditable policy checks;
- centralized policy evaluation;
- deny-by-default posture.

Pantheon distillation:

```text
Use as conceptual inspiration for policy checks.
Do not embed a policy engine into Pantheon before there is a clear governance need.
```

Potential Pantheon relevance:

- future policy evaluation;
- allowed tool checks;
- external action gates;
- scope and approval policy checks.

Risks:

- turning Pantheon into policy runtime;
- adding operational complexity too early;
- policy pass treated as approval.

## Mapping to Pantheon modules

| Pantheon concern | Useful inspirations | Preferred posture |
|---|---|---|
| Ingestion and parsing | RAGFlow, Dify, AnythingLLM | external capability or inspiration only |
| Retrieval quality | RAGFlow, Onyx, Khoj, AnythingLLM | external execution capability under scope |
| Workspace UX | OpenWebUI, AnythingLLM, Khoj | cockpit surface, not source of truth |
| Connectors | Onyx, Dify, Khoj | optional external capabilities under policy |
| Scoped authorization | Permify, Ory Keto, Casbin, OPA | future optional guardrail, not MVP dependency |
| Workflow visualization | Dify, Flowise | explanatory surface, not runtime |
| Versioning and provenance | TerminusDB, Dolt | semantic inspiration, not early database replacement |
| Validation checks | Guardrails AI, OPA | candidate checks, not approval |
| Audit and observability | Onyx, Dify | evidence and review support, not runtime state ownership |

## MVP versus optional advanced path

### MVP inspiration path

The first practical path should remain simple:

```text
OpenWebUI selection
→ Pantheon Task Contract
→ Context Pack with authorized excerpts
→ Hermes execution
→ sourced candidate output
→ user validation
```

Relevant inspiration:

- AnythingLLM for simple document workspace UX;
- OpenWebUI for cockpit behavior;
- RAGFlow for source/chunk transparency;
- Onyx for audit vocabulary;
- Guardrails-style checks for optional structured review.

### Optional advanced path

Advanced capabilities remain optional:

```text
shared Postgres
→ separated governance domains
→ scoped read-only functions
→ hybrid retrieval
→ audit lineage
→ evidence candidate links
→ memory review workflow
```

Relevant inspiration:

- Onyx for enterprise connectors and audit;
- Permify/Ory/Casbin for scoped authorization;
- TerminusDB/Dolt for provenance and versioning;
- Dify for observability concepts;
- RAGFlow for high-quality parsing and retrieval.

## What Pantheon must not copy

Pantheon Next must not copy these patterns into its governance core:

- full RAG platform;
- agent builder;
- visual workflow runtime;
- provider router;
- plugin marketplace;
- free connector layer;
- hidden scheduler;
- queue manager;
- automatic memory system;
- autonomous research agent;
- runtime authorization service;
- database runtime;
- validation system that bypasses human approval.

## Stable differentiator

Pantheon Next should remain the governance grammar around AI work.

```text
Raw Source
→ Source Reference
→ Retrieved Knowledge
→ Working Context
→ Evidence Candidate
→ Evidence Item
→ Evidence Pack
→ Output Candidate
→ Approval Event
→ Register Candidate
→ Registre Probatoire entry
```

This chain is the differentiator.

Existing tools can help at different steps.

None of them should collapse the chain.

## Decision rule for future adoption

Before adopting an external repository, component or pattern, ask:

```text
Does it improve scope control?
Does it improve source traceability?
Does it improve evidence quality?
Does it improve approval clarity?
Does it improve memory discipline?
Does it improve auditability?
Can it remain optional?
Can it be replaced later?
Does it avoid runtime drift?
```

If the answer is no, do not adopt.

If the answer is yes, create a Task Contract or governance proposal before implementation.

## Status

Research and support doctrine only.

No dependency added.

No implementation started.

No OpenWebUI plugin added.

No Hermes tool added.

No gateway added.

No schema added.

No authorization service added.

No external repository adopted.
