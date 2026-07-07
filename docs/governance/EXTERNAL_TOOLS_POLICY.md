# External Tools Policy

Status: active doctrine — external capability governance.

External tools are capabilities.

They are not authority.

They are not governance.

They are not memory.

They are not proof by themselves.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

This document defines how Pantheon Next governs external tools and capability surfaces.

It does not define a tool runtime.

It does not define a provider router.

It does not define a plugin manager.

It does not define installation behavior.

It does not authorize hidden execution.

## Definition

An external tool is any capability outside the canonical Pantheon governance documents that can read, transform, generate, write, send, publish, delete, install, configure, execute, retrieve, call another service, alter a repository, alter a project artifact, affect a user-visible output or influence memory.

This includes but is not limited to:

- web search;
- browser retrieval;
- file read and write tools;
- repository tools;
- email tools;
- calendar tools;
- document tools;
- spreadsheet tools;
- diagram tools;
- image tools;
- code execution;
- controlled terminal use;
- MCP servers;
- OpenWebUI functions, tools, pipes, filters, actions or pipelines;
- Hermes tools and skills;
- provider gateways;
- cloud APIs;
- local services;
- import, export or conversion tools;
- installers and configuration tools.

A capability being available does not mean it is authorized.

## Core rule

Tool use must be justified by the task.

Tool use must stay inside the Task Contract when a Task Contract is required.

Tool output must be treated as candidate evidence until reviewed.

Tool availability must never bypass approval.

## Default posture

Default posture:

```text
not authorized unless scope, evidence and approval allow it
```

This default protects Pantheon Next from becoming a free tool runtime.

It also protects the user from silent external effects.

## Tool risk classes

Tool risk is evaluated by capability effect.

These classes guide approval expectations.

Final approval remains governed by `APPROVALS.md`.

### T0 — no external effect

Examples:

```text
local display
formatting without persistence
local non-sensitive transformation
read-only review of already supplied content
```

Expected governance:

```text
low evidence burden
no durable effect
no memory promotion
```

### T1 — read-only retrieval

Examples:

```text
web retrieval
repository read
document read
email read
calendar read
Knowledge Base retrieval
```

Expected governance:

```text
source recorded
freshness considered
sensitive access checked
no write effect
```

### T2 — transformation or candidate artifact generation

Examples:

```text
summarization
classification
diagram draft
document draft
patch draft
local file generation
```

Expected governance:

```text
output marked candidate
sources and assumptions recorded when relevant
no external publication
no automatic memory promotion
```

### T3 — governed project mutation candidate

Examples:

```text
repository file update candidate
governance document update
project artifact revision
structured data transformation that may affect later decisions
```

Expected governance:

```text
Task Contract expected
Evidence Pack expected
diff or output review expected
approval checked
protected areas checked
```

### T4 — external write or communication effect

Examples:

```text
send email
create calendar event
publish document
write to external system
delete or archive external content
share file
change live configuration
```

Expected governance:

```text
explicit user intent
approval required
evidence recorded
rollback or correction path considered
```

### T5 — privileged, irreversible or doctrine-sensitive effect

Examples:

```text
credential handling
secret access
production configuration
runtime installation
plugin installation
provider routing change
memory promotion
doctrine mutation
protected repository area
irreversible deletion
financial or legal external effect
```

Expected governance:

```text
high approval burden
scope must be explicit
evidence must be strong
rollback or mitigation must be addressed
no silent execution
```

## Authorization gates

Before using an external tool, check:

```text
purpose
scope
risk class
input sensitivity
external effect
write effect
memory implication
approval need
evidence need
rollback need
```

For governed work, these checks should appear in the Task Contract or Evidence Pack.

## Least capability principle

Use the smallest capability that can satisfy the task.

Prefer:

```text
read before write
candidate before mutation
local transformation before external write
explicit approval before external effect
source reference before memory proposal
```

Do not use a broad tool when a narrow tool is sufficient.

Do not use a write-capable tool for a read-only task.

## Evidence requirements

Tool output that affects a decision must be recorded as evidence.

Evidence should identify:

- tool category;
- purpose;
- source or target when relevant;
- assumptions;
- output reference;
- risk note;
- approval state;
- limitation or uncertainty.

Tool output must not be presented as self-validating truth.

## Read tools

Read tools may retrieve sources, project data or operational context.

Read access must still be governed when content is sensitive, private, stale, privileged or decision-critical.

Read output should be marked when it is:

```text
partial
stale
contradicted
unverified
sensitive
private
retrieved only
```

Read access does not authorize write access.

## Write tools

Write tools can create external effects.

They require stronger governance than read tools.

Write tools include actions such as:

```text
send
publish
create
update
delete
archive
share
commit
configure
install
```

A write action should not occur from hidden workflow logic.

A write action should be traceable in evidence.

## Repository tools

Repository tools are high-risk when they mutate canonical documents, code or protected areas.

Repository mutation requires:

- scope clarity;
- protected-area check;
- actual diff awareness;
- evidence record;
- rollback or correction awareness;
- approval level appropriate to the touched area.

Patch Candidates are not merge decisions.

Commits are not doctrine validation by themselves.

## Communication tools

Communication tools include email, chat, calendar, messaging and publication channels.

They create external effects.

They should preserve:

- recipient or destination;
- exact content or summary;
- intent;
- approval state;
- send or publication status.

Drafting is lower risk than sending.

Sending is a governed external effect.

## Code and terminal tools

Code execution and controlled terminal use may be useful but risky.

They must not create an internal Pantheon runtime.

They must not bypass repository policy.

They must not install dependencies, services, plugins, skills or providers without explicit authorization and the relevant approval level.

Generated outputs should remain candidates unless reviewed.

## MCP, gateways and provider-facing tools

MCP servers, provider gateways and model routing surfaces are external capability surfaces.

Pantheon Next must not become their router.

Pantheon Next may govern their authorization, evidence expectations and approval requirements.

It must not implement hidden routing, hidden dispatch, hidden scheduling or hidden provider selection.

## Installation and configuration tools

Installation and configuration tools are privileged by default.

They may alter runtime behavior, security posture, provider behavior, tool availability or execution boundaries.

They require explicit scope and approval.

Pantheon Next must not automatically install skills, plugins, tools, providers or runtimes.

## Memory-affecting tools

A tool that stores, indexes, retrieves, ranks, promotes or modifies long-lived information has memory implications.

Such tools must not promote a Registre Probatoire entry automatically.

They may produce Register Candidates only when allowed by Task Contract and approval policy.

Memory promotion remains governed by `MEMORY.md`.

## Secrets and private data

Secrets, credentials, tokens, private data and sensitive project information require strict handling.

External tools must not expose secrets in outputs, logs, prompts, context packs, Evidence Packs or public artifacts.

If secret exposure is suspected, the tool result must be treated as a security risk, not a normal evidence item.

## Revocation and rollback

Tool authorization can be revoked.

A tool may be blocked when it becomes unsafe, stale, misconfigured, overbroad, unreviewable or incompatible with Pantheon doctrine.

For high-risk tool use, rollback or mitigation should be considered before execution.

## Forbidden drift

External tool governance must never become:

- tool runtime;
- provider router;
- automatic installer;
- free plugin manager;
- hidden workflow runner;
- hidden scheduler;
- autonomous execution engine;
- automatic skill installer;
- automatic memory promoter;
- self-evolution loop;
- approval bypass.

If tool availability becomes authorization, the boundary has failed.

If a tool can canonize memory or doctrine without approval, the boundary has failed.

## Implementation note

This policy intentionally avoids tool-specific endpoint, environment variable, Docker, provider, plugin, function, pipe, filter, action, MCP or skill installation details.

Those details must be verified against current official documentation before operational configuration is proposed.

## Final rule

A tool may help produce an output.

A tool may help produce evidence.

A tool does not decide whether the output is legitimate.

Pantheon Next governs that decision.

---

## Absorbed: External Agentic Inspirations (2026-07-07)

Formerly `docs/governance/EXTERNAL_TOOLS_POLICY.md`; absorbed verbatim during the governance cleanup (pass B). Headings demoted one level; content unchanged.

Original status: active support appendix — inspiration and distillation only.

This document extends `EXTERNAL_TOOLS_POLICY.md` for agentic runtimes, observability systems, graph-based RAG and skill ecosystems.

It does not add dependencies.

It does not approve implementation.

It does not define runtime integration.

It does not authorize a LangGraph runtime, agent runtime, MCP layer, observability backend, skill installer, scheduler, queue, provider router, automatic memory system or hidden workflow runner inside Pantheon Next.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Purpose

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

### Distillation grid

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

### LangGraph

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

### LangSmith

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

### Langfuse

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

### GraphRAG and graph-based RAG

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

### GenAI_Agents

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

### Shokunin

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

### Priority ranking

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

### Candidate future pattern cards

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

### Status

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

---

## Absorbed: External Ai Option Reviews (2026-07-07)

Formerly `docs/governance/EXTERNAL_TOOLS_POLICY.md`; absorbed verbatim during the governance cleanup (pass B). Headings demoted one level; content unchanged.

Original status: stub — partially implemented.

This document tracks external AI projects, frameworks and architectures evaluated during Pantheon Next development.

The purpose is:

- architectural comparison;
- doctrine validation;
- runtime drift detection;
- inspiration tracking;
- integration risk analysis.

External projects are references only.

They are not canonical Pantheon Next architecture.

### Evaluation rules

Every external project should be evaluated against the doctrine:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Any project introducing:

- hidden runtime orchestration;
- autonomous scheduling;
- auto-promoted memory;
- hidden workflow engines;
- implicit provider routing;
- self-modifying governance;
- agent self-approval;
- uncontrolled plugin execution;

must be classified as runtime-drift risk.

---

## Duskript/Pantheon

Repository:

- `https://github.com/Duskript/Pantheon`

### Classification

```text
Useful inspiration.
High runtime-drift risk.
Do not import directly.
```

### Positive aspects

- strong user-facing architecture presentation;
- specialized AI profile concept;
- Hermes Agent clearly identified as runtime;
- good explanation of multi-profile interaction;
- good UX narrative around persistent context;
- useful inspiration for Hermes profile ergonomics.

### Incompatible aspects for Pantheon Next

The project includes or proposes:

- shared evolving memory;
- background scheduler agents;
- cron execution;
- webhook execution;
- plugin runtime system;
- sub-agent runtime orchestration;
- automatic installers;
- direct provider routing;
- self-learning behavior;
- runtime-centric architecture.

These concepts are incompatible with Pantheon Next phase 1 governance boundaries.

### Pantheon Next position

Pantheon Next may study:

- profile ergonomics;
- UX concepts;
- Hermes profile decomposition;
- documentation structure;
- role specialization patterns.

Pantheon Next must not import:

- runtime orchestration;
- scheduler systems;
- autonomous memory evolution;
- plugin runtimes;
- hidden execution workflows;
- automatic profile deployment.

---

## Absorbed: External Method Reviews (2026-07-07)

Formerly `docs/governance/EXTERNAL_TOOLS_POLICY.md`; absorbed verbatim during the governance cleanup (pass B). Headings demoted one level; content unchanged.

Original status: active support doctrine — method review only.

This document reviews external reasoning, prompting, evaluation and workflow methods as governance inputs.

It does not define hidden orchestration.

It does not implement methods.

It does not approve autonomous agents.

It does not authorize a planner, executor, debate runtime, reflection loop, LLM judge, scheduler, queue, message bus, runtime graph or automatic approval mechanism inside Pantheon Next.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Purpose

Methods can improve output quality.

They can also hide authority drift.

This document answers:

```text
Does this method improve governance review, or does it merely improve autonomous performance?
```

Pantheon may borrow method vocabulary only when it strengthens visibility, evidence, review, scope or approval.

### Method review record format

Recommended fields:

```text
method_name
method_family
capability_summary
governance_value
risk_surface
allowed_distillation
forbidden_import
related_roles
related_artifacts
status
review_notes
```

### Status values

```text
observe
allowed_as_review_pattern
allowed_as_hermes_candidate_method
boundary_required
rejected_as_hidden_runtime
rejected_as_approval_drift
rejected_as_memory_drift
archived
```

### Current method reviews

| Method | Governance value | Main risk | Pantheon posture |
|---|---|---|---|
| ReAct | separates reasoning-style steps from action-style steps conceptually | hidden tool loop or tool autonomy | use only as inspiration for action/evidence separation |
| Chain-of-thought prompting | may improve model reasoning internally | storing or exposing hidden reasoning as evidence | do not store hidden chain-of-thought; use concise rationale and assumptions |
| Self-critique | useful for draft revision and limitation detection | model self-approval | allow as candidate review signal only |
| Reflection loops | can catch errors over iterations | endless self-improvement loop | allow only bounded Hermes-side candidate method under Task Contract |
| Debate | can surface disagreement | hidden multi-agent theater or collusion | replace with visible Governance College role statuses |
| Tree of Thoughts | explores alternatives | uncontrolled branching and session bloat | allow as bounded option exploration, not runtime graph |
| Planner/executor | separates plan and action | Pantheon becomes orchestrator | plan may inform Task Contract; execution remains Hermes-side |
| LLM-as-judge | useful pre-score or consistency signal | score becomes approval | judge output is signal, never final validation |
| Constitutional prompting | explicit rule layer | prompt rules mistaken for Pantheon doctrine | useful as reminder; Pantheon doctrine remains canonical |
| Retrieval-augmented generation | connects answer to sources | retrieval becomes evidence or truth | retrieval is candidate support only |
| GraphRAG-style synthesis | improves corpus-level view | graph/community summary treated as authority | graph output is retrieved context or Evidence Candidate |
| Multi-agent team | role specialization | autonomous hidden agent team | Governance College is role separation, not team runtime |
| Autonomous research agent | breadth of search | source sprawl and unapproved external browsing | Argos-style source review under scope, not autonomy |
| Memory-enhanced agent | continuity | memory without approval and scope | Register Candidate discipline only |
| Browser automation | action capability | external effect without approval | Hermes-only under tool policy and Task Contract |

### Allowed distillation patterns

#### Method as review lens

A method may become a review lens when it helps classify:

- source gaps;
- assumptions;
- contradictions;
- risk;
- missing scope;
- delivery readiness;
- approval need;
- memory implication.

#### Method as Hermes candidate constraint

A method may belong to Hermes or another external runtime when it controls execution technique, provided Pantheon receives only:

- Task Contract fit;
- evidence summary;
- assumptions;
- risks;
- output candidate;
- capability gaps;
- approval implications.

#### Method as User Decision Gate trigger

A method may reveal conflict that should be exposed to the user.

Example:

```text
self-critique finds unsupported claim
→ ARGOS source_insufficient
→ THEMIS risk_detected
→ ZEUS request_source or human_decision_required
```

### Forbidden method imports

Pantheon must not import:

- hidden reasoning traces;
- autonomous debate loops;
- hidden planner/executor loops;
- agent self-reflection as approval;
- LLM judge as final authority;
- self-improvement loops;
- automatic retry loops;
- background research loops;
- unbounded option exploration;
- automatic external action;
- automatic memory update.

### Role mapping

| Method pressure | Pantheon role that can expose it |
|---|---|
| structure, decomposition, plan | ATHENA |
| source adequacy and provenance | ARGOS |
| risk, policy, approval boundary | THEMIS |
| clarity and delivery readiness | APOLLO |
| artifact or patch preparation | HEPHAISTOS |
| recipient and transmission framing | IRIS |
| status and next procedure | ZEUS |

A method may help one role produce a candidate view.

It must not create autonomous role execution inside Pantheon.

### Evidence rule

Method output may appear in an Evidence Pack only as governance-relevant summary.

Allowed:

```text
assumption noted
source gap found
contradiction detected
variant compared
risk escalated
approval required
```

Forbidden:

```text
raw chain-of-thought
private scratchpad
hidden debate transcript
unbounded reasoning trace
agent deliberation archive
```

### Approval rule

No method approves its own result.

A method can produce:

```text
signal
reserve
candidate review
risk note
contradiction note
next action recommendation
```

It cannot produce:

```text
final approval
memory promotion
external transmission authorization
protected file mutation authorization
professional reliance authorization
```

### Memory rule

Method outputs are not memory.

A repeated critique, score, judgment, plan or conclusion may become a Register Candidate only if it satisfies `MEMORY.md` and `SCOPE_ISOLATION.md`.

### Review questions

Before using a method as inspiration, ask:

```text
What does this method make visible?
What does it hide?
Does it improve evidence or only confidence?
Does it preserve human decision?
Does it create hidden execution state?
Does it expand scope?
Does it imply memory?
Does it require tool access?
Does it create external effect?
```

### Relationship to Watchlist

Unreviewed methods belong on `WATCHLIST.md`.

Reviewed methods belong here.

Distilled method patterns may move to `DISTILLATION_REGISTRY.md`.

Rejected method patterns should be recorded in `REJECTED_PATTERNS.md`.

### Forbidden drift

This document must never become:

- prompt library;
- hidden workflow specification;
- autonomous reasoning engine;
- debate runtime;
- LLM judge policy;
- self-improvement loop;
- planner/executor implementation;
- approval automation;
- memory promotion system.

### Final rule

```text
A method is useful when it improves reviewability.
It is dangerous when it replaces review.
```

---

## Absorbed: External Repo Inspirations (2026-07-07)

Formerly `docs/governance/EXTERNAL_TOOLS_POLICY.md`; absorbed verbatim during the governance cleanup (pass B). Headings demoted one level; content unchanged.

Original status: active support doctrine — inspiration map only.

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

### Purpose

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

### Core rule

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

### Evaluation lens

External repositories should be evaluated by asking:

| Question | Why it matters |
|---|---|
| What problem does this project solve well? | Avoid copying the whole system when only one pattern is useful. |
| Does it reinforce or weaken Pantheon doctrine? | Keep governance separate from execution. |
| Does it blur source, evidence, approval or memory? | Reject patterns that collapse the trust chain. |
| Does it require runtime ownership? | Reject runtime drift into Pantheon. |
| Can it inspire a modular optional component? | Prefer replaceable edges over core dependency. |
| Is it useful for MVP or only advanced scale? | Avoid overbuilding before proof. |

### Inspiration map

#### RAGFlow

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

#### Onyx

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

#### AnythingLLM

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

#### Khoj

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

#### Dify

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

#### Flowise

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

#### Permify, Ory Keto and Casbin

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

#### TerminusDB and Dolt

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

#### Guardrails AI

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

#### Open Policy Agent

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

### Mapping to Pantheon modules

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

### MVP versus optional advanced path

#### MVP inspiration path

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

#### Optional advanced path

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

### What Pantheon must not copy

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

### Stable differentiator

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

### Decision rule for future adoption

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

### Status

Research and support doctrine only.

No dependency added.

No implementation started.

No OpenWebUI plugin added.

No Hermes tool added.

No gateway added.

No schema added.

No authorization service added.

No external repository adopted.

---

## Absorbed: External Runtime Threat Model Review (2026-07-07)

Formerly `docs/governance/EXTERNAL_TOOLS_POLICY.md`; absorbed verbatim during the governance cleanup (pass B). Headings demoted one level; content unchanged.

Original status: active support doctrine — review method for external runtimes and privileged AI workspaces.

This document defines how Pantheon Next reviews an external runtime, AI workspace, tool host, connector host or model-serving surface before it is used around consequential professional work.

It is a review method, not an implementation.

It does not create a runtime, scanner, sandbox, firewall, installer, scheduler, queue, provider router, connector gateway, MCP host, approval engine, memory engine, OpenWebUI configuration, Hermes skill, Docker configuration or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Purpose

External AI systems increasingly combine capabilities that were previously separate:

```text
chat surface
agent execution
tool calling
file access
repository access
email / calendar access
local model serving
memory / retrieval
scheduled tasks
MCP or connector surfaces
administration settings
```

Pantheon must review that combined surface before treating it as safe to use in a professional dossier.

The review answers one question:

```text
What consequential power does this runtime expose, and which Pantheon gate must constrain it?
```

### Core rule

```text
Runtime power is not governance authority.
```

An external runtime may expose powerful capabilities. It may execute. It may observe. It may prepare candidates. It may carry a task.

It must not approve, validate, canonize, promote memory, authorize external effects, alter doctrine or silently expand scope.

### When this review is required

Run this review when a system, adapter, plugin, tool host or workspace can touch one of the following:

```text
private or client material
professional source interpretation
project files or repository content
email, calendar or messaging channels
long-lived memory, index or recall
model serving or provider selection
scheduled or background tasks
runtime installation or configuration
privileged local or host-control surfaces
MCP, gateway or connector access
```

If the system is read-only, low-risk and non-consequential, a light review is sufficient.

If the system can create a false truth, wrong memory, unapproved external effect, invalid approval, unauthorized action or scope expansion, the full review is required.

### Review record

Minimum fields:

```text
external_runtime_review:
  runtime_name:
  reviewed_ref:
  reviewed_date:
  reviewed_by:
  system_role: exposure_surface | execution_runtime | observability_layer | connector_gateway | model_runtime | mixed_workspace | other
  binding_status: unbound | candidate | sandbox | project_scoped | organization_scoped | refused
  trusted_user_assumption:
  exposure_posture:
  privileged_capabilities:
  data_access:
  external_effects:
  memory_effects:
  model_effects:
  scheduling_effects:
  host_control_surface:
  untrusted_content_paths:
  prompt_injection_posture:
  token_or_permission_granularity:
  auditability:
  reversibility_or_mitigation:
  pantheon_gate_required:
  approval_ceiling:
  evidence_expectation:
  safe_default:
  decision: accepted | refused | to_verify | to_arbitrate
  repo_state: documented_non_implemented | adapter_outside_pantheon | implemented_elsewhere | refused
```

This is a governance record. It does not authorize runtime installation by itself.

### Capability surface checklist

The review must identify whether the runtime can:

```text
read private material
write or modify durable material
send, publish or notify externally
store, index, rank or recall long-lived information
execute code or commands
alter runtime configuration
select or serve models
schedule or resume work
call connectors, MCP tools or provider gateways
alter a repository or project artifact
produce user-visible professional output
```

Each positive answer must be mapped to:

```text
risk class
scope
approval need
evidence need
safe fallback
```

### Host-control surface classification

Host-control power is a stronger concern than ordinary tool availability.

Use this vocabulary:

```text
host_control_surface:
  none
  scoped_filesystem
  broad_filesystem
  shell_user
  shell_admin
  container_host_control
  remote_host_control
  cloud_admin
```

Default classification:

```text
none -> not a host-control concern
scoped_filesystem -> review scope and minimization
broad_filesystem -> high risk
shell_user -> high risk
shell_admin -> critical risk
container_host_control -> critical risk
remote_host_control -> critical risk
cloud_admin -> critical risk
```

Critical host-control power must not be treated as a normal skill, plugin or workspace option.

It requires at minimum:

```text
explicit scope
explicit approval path
strong evidence expectation
sandbox or isolation posture where relevant
reversibility or mitigation note
human-visible gate before consequential use
```

### Untrusted content paths

External runtime review must identify untrusted content paths.

Common paths:

```text
web results
fetched pages
uploaded files
read emails
notes
runtime memory
retrieved knowledge
connector output
MCP output
model output reused as context
third-party tool output
```

Pantheon rule:

```text
Untrusted content enters as data.
It must not become instruction, proof, approval or memory by proximity.
```

Any adapter may wrap, label or isolate untrusted content. That adapter behavior lives outside Pantheon. Pantheon governs the requirement and the output status.

### Prompt-injection posture

The review must record whether the runtime distinguishes:

```text
instructions from trusted operator
instructions from system / policy
content from external source
content from retrieved memory
content from tool output
```

If the runtime cannot preserve that distinction, its outputs remain higher-risk candidates and must not be used for consequential delivery without stricter human review.

### Permission and token granularity

The review must classify permission posture:

```text
permission_granularity:
  coarse
  role_based
  capability_scoped
  task_scoped
  dossier_scoped
  unknown
```

Coarse permissions are not forbidden, but they raise the approval burden when a broad token or session can reach more capability than the Task Contract requires.

Least capability remains the default.

### Exposure posture

The review must distinguish:

```text
local_only
private_network
vpn_or_tunnel
reverse_proxy
public_internet
unknown
```

Exposure posture does not authorize use. It only informs risk.

A public or unclear exposure posture blocks professional dossier use until reviewed.

### Relationship to existing doctrine

This review applies:

```text
EXTERNAL_TOOLS_POLICY.md     -> external tools are capabilities, not authority
CAPABILITY_PLACEMENT.md      -> consequential effects pass through Pantheon
ADAPTERS_AND_BINDINGS.md     -> runnable configuration lives outside Pantheon
UNIFORM_CAPABILITY_GOVERNANCE.md -> one law, one passport, one gate
TASK_CONTRACTS.md            -> task scope and allowed outputs
EVIDENCE_PACK.md             -> reviewable evidence and limitations
APPROVALS.md                 -> approval level
MEMORY.md                    -> no automatic memory promotion
SCOPE_ISOLATION.md           -> no silent scope expansion
```

### Outcomes

Allowed review outcomes:

```text
accepted_for_reference
accepted_for_sandbox
accepted_for_adapter_design
accepted_for_project_scoped_use
needs_more_evidence
needs_sandbox
needs_adapter
needs_human_approval
blocked
refused
```

An outcome may approve documentation or adapter design. It does not approve execution unless the separate Task Contract and approval path allow it.

### Safe defaults

If the review is incomplete:

```text
no external effect
no canonical effect
no memory promotion
no privileged execution
no client-data use
candidate-only output
surface the capability gap
```

### Boundary phrase

```text
The runtime may be powerful.
The review makes the power legible.
Pantheon governs the consequence.
The human decides.
Only the validated remains.
```
