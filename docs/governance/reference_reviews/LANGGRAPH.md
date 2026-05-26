# LangGraph Reference Review

Status: external runtime reference review — support doctrine only.

This document reviews LangGraph as an external inspiration for Pantheon Next.

It does not add a dependency.

It does not approve installation.

It does not implement LangGraph.

It does not authorize a Pantheon workflow runtime, central graph engine, scheduler, queue, provider router, memory store, MCP layer, A2A endpoint, observability backend, automatic approval system or automatic memory promotion.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Source reviewed

Primary source:

```text
https://docs.langchain.com/oss/python/langgraph/overview
```

Related deployment source:

```text
https://docs.langchain.com/langsmith/deployment
```

The reviewed documentation describes LangGraph as a low-level orchestration framework and runtime for long-running, stateful agents, with durable execution, streaming, human-in-the-loop and persistence.

The LangSmith Deployment documentation describes an agent-server runtime with assistants, threads, runs, cron jobs, streaming API, human-in-the-loop API, time travel, MCP endpoint, A2A endpoint, distributed tracing, webhooks, authentication, custom stores, checkpointers, custom routes and deployment options.

## Pantheon classification

| Axis | Classification |
|---|---|
| Reference type | external runtime / orchestration framework |
| Pantheon use | governance vocabulary and boundary stress-test |
| Hermes use | optional runtime candidate, only under Task Contract |
| OpenWebUI use | cockpit exposure of run state and user decisions only |
| Installation status | not installed |
| Adoption status | not approved |
| Doctrine status | support review only |

## What LangGraph solves

LangGraph is designed for workflows where a model-driven system needs durable, stateful and interruptible execution.

Relevant capability families:

- graph-structured workflow or agent execution;
- long-running stateful tasks;
- persistence and checkpointing;
- durable execution after failures;
- streaming execution updates;
- human-in-the-loop interruptions;
- inspection or modification of runtime state;
- short-term and long-term agent memory patterns;
- subgraphs and composable execution structures;
- deployment as an agent server with assistants, threads and runs.

These capabilities are valuable.

They are also exactly why LangGraph must remain outside Pantheon core.

## Boundary decision

```text
LangGraph may structure Hermes execution.
OpenWebUI may expose LangGraph state.
Pantheon must never absorb LangGraph runtime state as governance truth.
```

## Allowed Pantheon distillation

Pantheon may distill the following patterns:

| LangGraph pattern | Pantheon distillation |
|---|---|
| interrupt | approval interruption, User Decision Gate trigger or evidence pause |
| resume | Task Contract revision or bounded execution continuation |
| checkpoint | external runtime continuity marker, not validation |
| run trace | Evidence Pack candidate material, not proof by itself |
| state | runtime state, not Canonical Memory |
| human-in-the-loop | governed approval or clarification moment |
| durable execution | Hermes-side reliability pattern, not Pantheon scheduler |
| streaming | OpenWebUI run-status exposure pattern |
| subgraph | Hermes-side execution decomposition, not Pantheon role graph |
| memory | memory-risk pattern, never automatic Pantheon memory |

## Forbidden imports

Pantheon must not import:

- LangGraph as central runtime;
- executable graph definitions as governance doctrine;
- graph state as Pantheon memory;
- checkpoint state as approval;
- run completion as validation;
- assistant/thread/run objects as Pantheon artifacts;
- LangGraph scheduler or cron jobs;
- LangGraph memory stores;
- LangGraph MCP or A2A endpoints;
- LangGraph provider routing;
- LangGraph deployment platform as Pantheon infrastructure;
- LangGraph debugging or tracing as Evidence Pack by itself;
- LangGraph human-in-the-loop interrupt as automatic approval;
- graph transitions as hidden Governance College debate.

## Risk analysis

### Runtime drift

Highest risk.

LangGraph is a runtime. Installing it into Pantheon would make Pantheon execute workflows, manage state, resume work and potentially dispatch tools.

That violates the core doctrine.

Safe posture:

```text
LangGraph belongs only behind Hermes, if used at all.
```

### Memory drift

LangGraph supports stateful agents and memory patterns.

Pantheon memory requires candidate status, scope, evidence, confidence, risk, review horizon and approval.

Safe posture:

```text
LangGraph state may produce Memory Candidates.
It cannot produce Canonical Memory.
```

### Evidence drift

LangGraph traces and states are useful, but they are activity records.

They are not evidence until selected, summarized and tied to claims, sources, assumptions, risks and outputs.

Safe posture:

```text
Run trace -> Evidence Candidate -> Evidence Pack review.
```

### Approval drift

A human-in-the-loop interrupt is not the same as a Pantheon approval.

A user may inspect or modify runtime state, but Pantheon approval still requires clear object, scope, evidence, level and memory implication.

Safe posture:

```text
Interrupts may request decisions.
They do not grant approval by themselves.
```

### Scope drift

A long-running graph may accumulate context, tool results and transient state.

Without strict scoping, it may cross dossier, project or memory boundaries.

Safe posture:

```text
Every LangGraph run must be bound by Task Contract, Context Pack, allowed tools, memory rule and approval ceiling.
```

### OpenWebUI drift

OpenWebUI could be tempted to host LangGraph through a Function, Pipe, Tool or Pipeline.

That would turn the cockpit into runtime.

Safe posture:

```text
OpenWebUI displays run status and captures user decisions.
It does not run LangGraph as Pantheon core.
```

## Pantheon / Hermes / OpenWebUI split

| Layer | Allowed | Forbidden |
|---|---|---|
| Pantheon | boundary doctrine, pattern distillation, approval rules, Evidence Pack requirements | runtime graph, state store, scheduler, provider router, memory store |
| Hermes | optional LangGraph runtime candidate under Task Contract | global agent runtime, unscoped memory, approval authority, doctrine mutation |
| OpenWebUI | run status panel, interrupt panel, resume/cancel buttons, Evidence Pack display | central LangGraph Function/Pipe/Pipeline, global native-mode agent, plugin manager |

## Hermes installation posture

LangGraph may be tested only as a Hermes runtime candidate.

Minimum conditions:

```text
Task Contract required
Context Pack required
allowed tools declared
forbidden tools declared
approval ceiling declared
memory rule declared
no direct Pantheon doctrine mutation
no direct OpenWebUI database access
Evidence Pack return required
User Decision Gate respected
```

Initial test environment should be:

```text
Hermes sandbox
fictional task
read-only or low-risk tools
no production credentials
no protected files
no canonical memory writes
no automatic external effects
```

## OpenWebUI exposure posture

OpenWebUI may expose:

- task/run status;
- current step summary;
- pause reason;
- human interrupt prompt;
- evidence produced so far;
- unresolved tensions;
- resume / cancel / request more evidence / revise scope actions;
- Evidence Pack return;
- User Decision Gate when required.

OpenWebUI must not:

- run the graph directly as Pantheon;
- convert run status into approval;
- convert trace into evidence automatically;
- convert graph memory into Canonical Memory;
- grant Hermes broad Knowledge access because a run exists;
- hide interrupt reasons or unresolved tensions.

## Distillation candidates

Candidate entries for `DISTILLATION_REGISTRY.md` after review:

```text
LangGraph interrupt -> User Decision Gate / approval interruption vocabulary
LangGraph checkpoint -> runtime continuity marker
LangGraph run trace -> Evidence Pack candidate material
LangGraph state -> runtime state, not memory
LangGraph human-in-the-loop -> user decision exposure pattern
LangGraph durable execution -> Hermes reliability candidate pattern
```

Candidate entries for `REJECTED_PATTERNS.md` after review:

```text
central LangGraph runtime inside Pantheon
LangGraph state as Canonical Memory
LangGraph run completion as approval
LangGraph trace as Evidence Pack by itself
LangGraph Agent Server as Pantheon platform
OpenWebUI Function/Pipeline as LangGraph core runtime
```

Candidate entries for `TENSIONS_AND_RISKS.md` after review:

```text
execution continuity vs governance authority
runtime state vs Canonical Memory
trace visibility vs evidence sufficiency
human interrupt vs approval semantics
cockpit exposure vs runtime execution
```

## Recommendation

Do not install LangGraph directly in Pantheon.

Do not install LangGraph directly as an OpenWebUI Function, Pipe, Tool or Pipeline for Pantheon workflows.

Allow a future Hermes sandbox candidate only if the task requires long-running, stateful, interruptible execution and the run is bounded by Task Contract, Context Pack, approval ceiling, allowed tools, memory rule and Evidence Pack return.

## Final rule

```text
LangGraph can help Hermes execute complex work.
LangGraph must not become the hidden operating system of Pantheon.
```