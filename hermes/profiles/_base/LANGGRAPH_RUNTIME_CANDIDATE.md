# LangGraph Runtime Candidate for Hermes

Status: Hermes runtime candidate template — not installed, not implemented.

This document defines when LangGraph may be considered as an optional execution backend behind Hermes Agent.

It does not install LangGraph.

It does not configure LangGraph.

It does not create a runtime.

It does not authorize Pantheon to execute workflows.

It does not authorize OpenWebUI to run LangGraph directly.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

LangGraph is a candidate runtime pattern for Hermes when execution needs are too stateful, long-running, interruptible or checkpoint-heavy for a simple linear execution profile.

It remains external to Pantheon.

Pantheon defines the frame.

Hermes may execute inside that frame.

OpenWebUI may expose the run and ask the human for decisions.

## Candidate identity

```yaml
runtime_candidate: langgraph
owner_layer: hermes
status: not_installed_candidate
pantheon_role: none
canonical_authority: none
governed_by:
  - docs/governance/TASK_CONTRACTS.md
  - docs/governance/EVIDENCE_PACK.md
  - docs/governance/APPROVALS.md
  - docs/governance/MEMORY.md
  - docs/governance/SCOPE_ISOLATION.md
  - docs/governance/HERMES_INTEGRATION.md
  - docs/governance/OPENWEBUI_INTEGRATION.md
  - docs/governance/EXTERNAL_TOOLS_POLICY.md
```

## Use when

Consider LangGraph only when a Hermes task requires one or more of:

- long-running workflow;
- checkpoint and resume;
- human interrupt during execution;
- multi-step evidence construction;
- bounded tool sequence with recoverable state;
- repository analysis with restart or recovery;
- RAG ingestion with quality gates;
- patch candidate workflow with tests and controlled retry;
- multi-phase review where intermediate state matters.

## Do not use when

Do not use LangGraph for:

- simple chat;
- short rewrite;
- translation;
- basic summary;
- one-step file edit;
- low-risk email draft;
- small source check;
- task without Task Contract;
- task without bounded scope;
- task where a linear Hermes profile is enough;
- task where state would create more governance risk than value.

## Required inputs

A LangGraph-backed Hermes run must receive an explicit bounded frame:

```yaml
required_inputs:
  task_contract: required
  context_pack: required
  approval_ceiling: required
  allowed_tools: required
  forbidden_tools: required
  memory_rule: required
  evidence_requirements: required
  output_contract: required
  user_decision_gate_policy: required
```

## Forbidden inputs

A LangGraph-backed Hermes run must not receive:

- unscoped OpenWebUI Knowledge;
- raw OpenWebUI database access;
- global vector store access;
- raw global memory;
- unrelated project context;
- protected files without approval;
- production credentials by default;
- write-capable external tools without explicit approval;
- Pantheon doctrine as mutable workspace;
- authority to promote memory;
- authority to approve its own output.

## Required outputs

A LangGraph-backed Hermes run must return:

```yaml
required_outputs:
  output_candidate: required
  run_trace_summary: required
  evidence_notes: required
  assumptions: required
  risks: required
  unresolved_interrupts: required
  approval_implications: required
  memory_candidates_if_any: required
  capability_gaps_if_any: required
  next_action_recommendation: required
```

It must not return a raw trace dump as a substitute for an Evidence Pack.

## Runtime state rule

LangGraph state is runtime state.

It is not:

- Registre Probatoire entry;
- Evidence Pack;
- approval;
- doctrine;
- source of truth;
- user decision;
- Pantheon Role Signal;
- Governance College debate.

If runtime state contains a durable claim, it may be summarized as a Register Candidate only.

## Interrupt rule

A LangGraph interrupt may request a user decision.

It does not grant approval.

Every interrupt exposed to OpenWebUI should identify:

- what is blocked;
- why human input is required;
- evidence visible so far;
- options available;
- risk of each option;
- effect on output;
- effect on memory;
- effect on approval;
- effect on delivery.

If the issue is a governed conflict, escalate to User Decision Gate rather than resolving inside the graph.

## Checkpoint rule

A checkpoint preserves external execution continuity.

It does not validate the work.

A resumed run must preserve:

- original Task Contract ID;
- context scope;
- approval ceiling;
- allowed tools;
- memory rule;
- evidence requirements;
- unresolved tensions.

If any of those change, request Task Contract revision or a new Task Contract.

## Tool rule

Tools used by a LangGraph-backed Hermes run must remain governed by `EXTERNAL_TOOLS_POLICY.md`.

Allowed tool access must be explicit.

Write-capable tools require approval matching the external effect.

A graph edge cannot grant tool authority by itself.

## Memory rule

LangGraph memory or state must not be treated as Pantheon memory.

Allowed:

```text
runtime state summary
Register Candidate proposal
source freshness note
scope-limited recall inside current run
```

Forbidden:

```text
automatic Registre Probatoire entry
cross-project memory reuse
silent user preference storage
auto-promotion from repeated state
graph memory as source of truth
```

## Evidence rule

Run trace may support evidence preparation.

It is not evidence by itself.

A valid return should map:

```text
claim -> source or action -> output effect -> limitation -> risk
```

Raw graph logs should be summarized into governance-relevant evidence notes.

## OpenWebUI exposure rule

OpenWebUI may expose:

- run status;
- current step summary;
- interrupt reason;
- pause/resume/cancel request;
- evidence produced so far;
- unresolved risks;
- User Decision Gate;
- Evidence Pack return.

OpenWebUI must not:

- host the LangGraph runtime as Pantheon core;
- approve run output by displaying it;
- convert run state into memory;
- grant unbounded Knowledge access;
- hide unresolved risk behind progress UI.

## Anti-patterns

Reject:

- central LangGraph runtime for Pantheon;
- LangGraph as Governance College;
- graph nodes as Pantheon Roles;
- graph completion as approval;
- checkpoint as memory;
- run trace as Evidence Pack;
- OpenWebUI Function as graph runner for Pantheon;
- background graph jobs without Task Contract;
- cron jobs inside Pantheon;
- graph-managed provider routing;
- graph-managed skill installation;
- graph-managed memory promotion.

## Minimal sandbox test

A first Hermes sandbox test, if ever approved, should use:

```text
fictional task
read-only or low-risk tools
no production credentials
no protected files
no canonical memory writes
no automatic external effects
small bounded graph
explicit interrupt
Evidence Pack candidate return
```

The sandbox output should be reviewed by Pantheon before any broader adoption.

## Final rule

```text
Hermes may use LangGraph to execute better.
LangGraph must not decide better than Pantheon.
```