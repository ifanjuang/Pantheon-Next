# AgentCanvas Trace Visualization Reference Review

Status: external reference — candidate / to verify.

Source: `https://github.com/vstorm-co/agentcanvas`

Tracking issue: `#128`

Review date: 2026-06-14

## Purpose

This note records the Pantheon Next qualification of AgentCanvas as an external trace-visualization reference.

It is a reference review, not an integration plan and not an implementation.

AgentCanvas is useful because it makes agent execution understandable: model calls, tool calls, nested agents, transcript, tokens, timing and cost can be inspected as an interactive HTML trace.

Pantheon Next may learn from this display pattern. It must not inherit AgentCanvas as a governance layer.

## Doctrine boundary

```text
The trace observes.
The dashboard exposes.
Pantheon governs status, scope, evidence, approval and memory.
```

The standing doctrine remains:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

AgentCanvas belongs, if used at all, to the observability / exposure-surface side. It must not become Pantheon core doctrine, a runtime, an approval system, a memory authority, an Evidence Pack authority or a source of truth.

## Accepted

Accepted as an external reference candidate for:

- visualizing execution traces;
- inspecting agent, model and tool-call structure;
- making Hermes or execution-runtime runs legible to a professional user;
- supporting audit review by exposing what happened during a run;
- inspiring a future dashboard view such as `Agent Trace Canvas`.

This acceptance is limited to observability and display patterns.

## Refused

Refused as:

- Pantheon governance layer;
- execution runtime;
- approval engine;
- Registre Probatoire entry;
- canonical memory;
- Evidence Pack authority;
- source of truth;
- required dependency of Pantheon doctrine;
- direct proof that a professional claim is valid.

A successful trace visualization is not proof, approval, professional validation, canonization, transmission authority or memory promotion.

## To verify

Before any adapter or dashboard work, verify:

1. whether Hermes can emit or expose a tool-agnostic execution trace;
2. whether the trace can be normalized into a `Trace Candidate` without hard-coding Logfire or Pydantic AI into Pantheon;
3. whether secrets, client data, prompts, raw tool payloads and private excerpts can be redacted before display;
4. whether role-based visibility is sufficient for professional use;
5. whether a trace can support an Evidence Pack Candidate without being treated as the Evidence Pack itself;
6. whether trace retention rules are needed per dossier, project or organization.

## To arbitrate

Future arbitration point:

```text
Should Pantheon Next define an `Agent Trace Canvas` dashboard candidate after a generic Trace Candidate contract exists?
```

This must be treated as a dashboard / observability question, not as a governance-core expansion.

## Candidate adapter shape

Non-executable conceptual shape:

```text
Execution Trace
-> redaction / minimization
-> Trace Candidate
-> optional Evidence Pack Candidate support
-> Pantheon status gate
```

The trace may support review. It does not decide review outcome.

## Placement rule

If the trace display is only used to show what happened, it belongs outside Pantheon core as observability or exposure-surface UX.

If the trace is used to decide truth, memory, approval, scope or external action legitimacy, Pantheon governs that decision.

Governing the decision is not implementing the trace viewer.

## Repository state

Documented non-implemented.

This note does not add:

- code;
- schema;
- test;
- runtime dependency;
- Logfire binding;
- Pydantic AI binding;
- dashboard implementation;
- OpenWebUI function;
- Hermes skill;
- approval workflow;
- memory promotion.

## Decision register

```text
Accepted: external observability / trace-visualization reference candidate.
Refused: governance authority, runtime, approval engine, canonical memory, Evidence Pack authority or source of truth.
To verify: generic Trace Candidate contract, redaction, visibility, Hermes trace compatibility and retention rules.
To arbitrate: future Agent Trace Canvas dashboard candidate after a generic trace contract exists.
```
