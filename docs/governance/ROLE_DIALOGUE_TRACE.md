# Role Dialogue Trace

Status: candidate orientation — observable workflow trace, role dialogue and cockpit log.

This document is a candidate orientation, not an implementation.

It does not create a workflow runtime, agent loop, queue, scheduler, hidden chain-of-thought recorder, approval engine, memory engine, skill runtime, file watcher, registry writer, connector gateway, LangGraph runtime, Langflow runtime or Hermes command surface.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon may expose a readable workflow log as a role dialogue.

The purpose is to make professional AI work inspectable without pretending that hidden reasoning is accessible or authoritative.

The log should show:

- what visible role acted;
- what it observed;
- what source or document it used;
- what skill or adapter it requested;
- what result candidate was produced;
- which files, registers or cockpit views were changed;
- what remains candidate, blocked, refused, accepted or to verify;
- where Hermes, LangGraph, Langflow or another runtime stands.

It should not show or require hidden chain-of-thought.

It should show observable role moves.

## Core distinction

```text
Hidden reasoning is not the log.
Observable role action is the log.
```

Allowed:

```text
Athena checked source coverage.
Hermes retrieved document X.
Hephaistos prepared file patch Y.
Zeus marked decision as to arbitrate.
Cerberus blocked memory promotion.
```

Forbidden:

```text
full private chain-of-thought
unbounded model scratchpad
unverifiable internal mental narrative
runtime state treated as approval
retrieval treated as proof
memory recall treated as truth
```

## Role dialogue as display metaphor

The dialogue between roles may be visualized as a readable operational transcript.

Example:

```text
Athena — Review
Observed: source gap in DCE package.
Asked Hermes: retrieve latest DCE files.
Result: 4 files found, 1 missing.
Status: Evidence Candidate.

Hermes — Execution Runtime
Action: retrieved files from project directory.
Used skill: document inventory.
Output: Result Candidate + Evidence Pack Candidate.

Hephaistos — Fabrication / Patch
Action: prepared cockpit mockup file update.
Files touched: project-graphs.html, project-graphs-ui.js.
Status: documented non-implemented.

Zeus — Status Arbitration
Decision: to verify before promotion.
Reason: graph page is candidate UI, not canonical registry.
```

The names are a surface metaphor for role responsibilities.

They must not imply autonomous authority.

## Event model

A trace event should be structured enough to filter, replay and audit.

Minimum event shape:

```yaml
trace_event:
  id:
  workflow_id:
  project_id:
  timestamp:
  visible_role:
  role_family:
  event_type:
  summary:
  observed_inputs:
  requested_action:
  target_runtime:
  skill_or_adapter:
  source_refs:
  produced_candidates:
  files_touched:
  registers_touched:
  status_before:
  status_after:
  approval_state:
  memory_state:
  risk:
  next_action:
  boundary_note:
```

Event types may include:

```text
observe
retrieve
ask_skill
ask_hephaistos
prepare_patch
modify_file
read_source
produce_candidate
qualify_status
request_approval
block_memory
record_trace
handoff_to_runtime
receive_result
mark_to_verify
mark_accepted
mark_refused
mark_blocked
```

## What each role may show

### Athena / analysis role

May show:

```text
review angle
source coverage
contradiction found
missing evidence
reason summary
risk summary
recommended next action
```

Must not show hidden chain-of-thought.

### Hermes / execution runtime

May show:

```text
runtime status
skill invoked
tool used
connector used
retrieval request
source returned
Result Candidate
Evidence Pack Candidate
failure / waiting state
```

Hermes completion is not Pantheon approval.

### Hephaistos / fabrication role

May show:

```text
file prepared
patch drafted
artifact produced
template shaped
mockup updated
schema candidate shaped
```

Hephaistos fabrication is not validation.

### Zeus / arbitration role

May show:

```text
accepted
refused
to verify
to arbitrate
blocked
promoted
not promoted
```

Zeus status is procedural unless backed by the required human decision.

### Cerberus / boundary role

May show:

```text
memory promotion blocked
scope violation blocked
external action blocked
approval missing
source insufficient
```

### Charon / transfer role

May show:

```text
handoff prepared
handoff blocked
external transmission pending
scope checked
```

## Workflow state view

The role dialogue trace should be visible from a workflow page.

Target page:

```text
Workflows & executions
```

The page should expose:

- current workflows;
- past workflows;
- runtime state;
- Pantheon status;
- role dialogue log;
- artifacts;
- files touched;
- sources retrieved;
- evidence candidates produced;
- approvals requested;
- blockers;
- next actions.

Filters:

```text
project
workflow status
runtime
role
event type
risk
approval state
memory state
date
source
file touched
```

Views:

```text
list
timeline
dialogue
graph
artifact table
```

## LangGraph and Langflow placement

Langflow may design or prototype a workflow.

LangGraph may execute durable, interruptible or checkpointed workflows behind Hermes or another governed bridge.

Hermes remains the execution runtime binding when used.

Pantheon records status and boundary conditions.

```text
Langflow designs.
LangGraph orchestrates when needed.
Hermes executes.
Pantheon governs.
```

This page must not become the workflow engine.

It may display or request:

```text
prepare retry
prepare cancellation
prepare approval request
prepare human input
prepare source retrieval
```

It must not silently:

```text
retry
cancel
approve
send
promote memory
write a validated evidence entry
```

## Relationship with project graphs

The role dialogue trace is related to the project graph but is not the same layer.

Project graph answers:

```text
What is connected in the project?
```

Role dialogue answers:

```text
Who did what, with what source, through what runtime, and with what status?
```

A project graph node may link to workflow trace events.

Example:

```text
Evidence E-042
-> produced_by -> trace_event T-119
-> touched_file -> project-graphs-ui.js
-> requested_skill -> document_inventory
-> status_after -> to_verify
```

## Visual grammar

Dialogue log entries should be compact and readable.

Each log row may show:

```text
role badge
time
workflow
project
event type
summary
runtime
skill
status
risk
source count
files touched
next action
```

Role display can use the Pantheon metaphor:

```text
Athena     -> analysis / review
Hermes     -> runtime execution
Hephaistos -> fabrication / patch / artifact shaping
Zeus       -> status arbitration
Cerberus   -> boundary guard
Charon     -> transfer / handoff
```

The metaphor is a display layer only.

## Boundary with private reasoning

The trace must be safe to display to a user or reviewer.

It must not contain:

- hidden chain-of-thought;
- raw model scratchpad;
- secret prompts;
- credentials;
- private tokens;
- unnecessary personal data;
- unrestricted connector payloads;
- unredacted sensitive source content.

It may contain:

- concise rationale summaries;
- source identifiers;
- document titles;
- file paths;
- status changes;
- skill names;
- runtime state;
- approval state;
- next action.

## Governance boundary

This orientation does not implement tracing.

It defines what a future cockpit trace may safely display.

Pantheon governs the status vocabulary and boundary conditions.

Runtime logs, connector logs, skill logs and workflow checkpoints remain outside Pantheon unless imported as candidate trace records.

## Doctrine summary

```text
The role dialogue shows observable work.
It does not expose hidden thought.
Hermes execution is not approval.
Hephaistos fabrication is not validation.
Retrieval is not proof.
Memory recall is not truth.
A trace supports review but does not decide.
Pantheon governs status.
The human decides.
```
