# Role Dialogue Trace

Status: candidate support specification — presentation foundation, transient
derived-event projector, bounded Cockpit SSE relay, admitted-run attachment hook,
composed-Cockpit dialogue UI and optional Ubuntu Workspace-Cockpit sidecar
implemented; native runtime events and persistence non-implemented.

The first presentation slice is implemented as an external Hermes template and
an Ubuntu profile configurator. It produces bounded role-labelled milestones in
supported Hermes response streams.

It does not make Hermes emit native `role.stage` events or persist Role Signals.
The implemented dialogue view is available in the composed Cockpit candidate
and through an optional transient sidecar in the filesystem Workspace Cockpit.
Neither path creates a workflow runtime, agent loop, queue, scheduler, hidden
chain-of-thought recorder, approval engine, memory engine, file watcher,
registry writer, connector gateway, LangGraph runtime or Langflow runtime.

```text
Hermes Web/dashboard exposes runtime interaction.
Hermes Agent executes.
Pantheon Cockpit may project governed trace state.
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
Themis blocked memory promotion because approval was missing.
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

### Themis / risk and boundary role

May show:

```text
memory promotion blocked
scope violation blocked
external action blocked
approval missing
source insufficient
```

### Iris / transmission role

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
Themis     -> risk / compliance / boundary
Iris       -> transmission / adaptation
Argos      -> sources / traceability
Apollo     -> quality / readiness
Mnemosyne  -> continuity / memory framing
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

## Implemented presentation slice

The following repository artifacts implement a bounded first slice:

```text
templates/hermes/skills/pantheon-activity-projection/SKILL.md
templates/hermes/profiles/pantheon-governed/SOUL.append.md
deployment/ubuntu/configure-hermes-activity-projection
```

The skill defines role selection and visible milestone grammar. The SOUL
supplement makes that projection expected for non-trivial governed requests.
The Ubuntu configurator installs both into an existing `pantheon-governed`
profile with a recoverable backup.

This slice can expose ordered labels in a streamed answer and can request
interim assistant messages when the Hermes transport supports them. It does not
claim a separate durable event for every label.

```text
ordered streamed label != structured trace event
structured trace event != persisted Role Signal
persisted Role Signal != Evidence or approval
```

## Implemented transient event projection

`implementation/mvp_vertical/hermes_role_stage_projection.py` implements a
bounded incremental projector over the public Hermes Runs stream. It consumes:

```text
message.delta
tool.started
tool.completed
run.completed | run.failed | run.cancelled | run.interrupted
```

It emits transient display events shaped as:

```yaml
event: role.stage
phase: started | updated | completed
stage_id:
run_id:
sequence:
timestamp:
visible_role:
role_family:
semantic_function:
summary:
details: {}
tool:
source_event:
projection: derived_transient
authority_effect: none
private_reasoning_included: false
```

The projector recognizes only canonical visible Role headers. Tool lifecycle
events become observable `Hermes · Exécution` stages because they report real
runtime activity. `reasoning.available` is ignored by construction. Arbitrary
labels do not create Roles, and unterminated public lines or excessive stage
counts fail closed.

The existing live-acceptance SSE collector now returns these projections beside
the unmodified upstream events. This is an adapter seam and test surface, not a
public service, durable trace store or Cockpit view.

## Implemented bounded relay

`implementation/mvp_vertical/hermes_role_trace_relay.py` provides one
in-memory transport seam per already-admitted Hermes run:

```text
one upstream event consumer
-> one incremental Role projector
-> bounded replay window
-> multiple identical read-only subscribers
```

It refuses a second upstream consumer, retains at most 500 projected events per
run and at most 32 traces per process, evicts only a terminal trace when full,
and fails closed on invalid run identifiers or replay gaps. It cannot create,
stop, approve or retry a Hermes run.

The same component includes a fixed-URL, server-side-key Runs reader. It accepts
only an existing `run_id`, consumes no more than 1,000 public SSE events, checks
that every event remains within that run and requires a terminal event. It has
no submission or control method.

The composed Cockpit exposes authenticated read routes:

```text
GET /cockpit/role-traces/{run_id}
GET /cockpit/role-traces/{run_id}/events
```

The second route is a finite/replayable SSE view with `Last-Event-ID` support.
The relay is transient process memory, not a message bus, database, Evidence
store or Role Signal registry.

## Implemented admitted-run attachment and browser dialogue

After the external Hermes callback has successfully recorded the exact
`run_id`, `hermes_execution_api.py` notifies an optional display observer. The
composed Cockpit configures that observer only when both of these deployment
values are present:

```text
MVP_HERMES_ROLE_TRACE_BASE_URL
MVP_HERMES_ROLE_TRACE_API_KEY
```

The pair is fail-closed: one missing value refuses startup, and no values mean
no outbound Role source. A replayed runtime-start callback does not attach a
second upstream reader. A projection failure cannot reinterpret or roll back
the already-recorded runtime start.

The composed Cockpit Hermes dock now contains a compact progressive timeline.
It follows the authenticated SSE stream through `fetch`, resumes from
`Last-Event-ID`, replaces repeated updates for the same `stage_id`, keeps detail
fields collapsed and labels every item `dérivé` or `natif`. It also states that
the surface contains public observable milestones and no private reasoning.

```text
visible Role label != autonomous agent
derived event != proof that an independent review ran
timeline completion != approval
```

## Implemented filesystem Cockpit adapter

The Ubuntu Workspace Cockpit now includes an optional credentialed sidecar and
a same-origin read-only browser proxy. The sidecar attaches only an exact
already-admitted `run_id`, keeps the bounded relay in transient memory and
reads the configured governed Hermes Runs stream. Its attach listener is
published on host loopback only. Separate attach and read keys remain outside
Git, and the browser receives neither those keys nor the Hermes API key.

This adapter does not introduce PostgreSQL, pgvector, durable trace admission,
run control or approval authority. Attachment failure is reported as display
diagnostic state and cannot reinterpret the canonical run start.

## Remaining implementation boundary

Native Hermes `role.stage` emission, durable trace admission and Role Signal
persistence remain non-implemented. The live Ubuntu deployment still requires
operator-provided secrets and activation. A model that emits all public Role
text only at final-answer time cannot be represented as having exposed those
Roles during private reasoning.

Pantheon governs their future status vocabulary and boundary conditions.

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
