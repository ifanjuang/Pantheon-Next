# Hermes Kanban Execution Patterns

Status: candidate / to verify — tool-specific execution-pattern note for Hermes Kanban.

This document classifies external Hermes Kanban patterns for Pantheon Next.

It is not canonical doctrine.

It is not a Hermes installation guide, runtime specification, dispatcher configuration, queue design, scheduler, approval mechanism, memory mechanism or implementation artifact.

It does not install Hermes Agent, configure profiles, create Kanban boards, start workers, define cron jobs or execute swarm graphs.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A recent external pattern describes Hermes Agent as a multi-profile Kanban execution surface: durable board, task rows, parent links, idempotent task creation, dispatcher-driven workers and swarm-style fan-out.

The useful part for Pantheon is not the marketing claim that Hermes becomes a autonomous team.

The useful part is narrower:

```text
Hermes Kanban can coordinate external execution.
Pantheon can govern what that execution is allowed to mean.
```

This document records which ideas are admissible as execution patterns, which are refused as governance claims, and what must be verified before local use.

## Classification

| Item | Decision | Reason |
|---|---|---|
| Durable task board | Accepted as execution coordination | A durable board can carry task state and handoff material outside Pantheon. |
| Named Hermes profiles | Accepted as execution profiles | Profiles may align with Pantheon Roles but do not inherit Role authority. |
| Parent / child task gates | Accepted as execution sequencing | Useful for research, extraction, review and synthesis dependencies. |
| Idempotency key for automation | Accepted as safety pattern | Prevents duplicate scheduled or webhook-triggered work. |
| Max runtime / retry limits | Accepted as execution guardrail | Limits worker storms and stuck tasks at runtime level. |
| Nightly review task | Accepted only as candidate-only review | It may produce a review note, not a decision. |
| Swarm topology | Accepted as candidate fan-out pattern | Useful only when the task genuinely decomposes into parallel tracks. |
| Hermes verifier | Accepted as pre-review | It can detect gaps, contradictions or insufficient evidence; it does not validate. |
| Hermes synthesizer | Accepted as candidate assembler | It may assemble a Result Candidate and Evidence Pack Candidate. |
| Hermes Kanban as governance | Refused | Coordination is not authority. |
| Hermes done status as approval | Refused | Runtime completion does not create legitimacy. |
| Hermes comments as Canonical Memory | Refused | Runtime state and comments are not governed memory. |
| Automatic external action after worker success | Refused without explicit approval | Execution success is not a delivery, sending, merge or filing authorization. |

## Boundary

Hermes Kanban may be treated as an external execution coordination surface.

Pantheon governs the status of the output, not the internal worker mechanics.

```text
Task Contract in
-> Hermes Kanban execution graph
-> Result Candidate + Evidence Pack Candidate out
-> Pantheon status / proof / approval / memory gate
-> human decision
```

A Hermes Kanban task may finish.

That means only:

```text
runtime work completed or stopped
```

It does not mean:

```text
source validated
claim proven
approval granted
memory promoted
action authorized
document delivered
patch merged
```

## Admissible patterns

### 1. Research-to-draft relay

Use when two or more research or extraction tracks can run independently before a synthesis step.

Allowed output:

```text
Research Candidate
Evidence Pack Candidate
Draft Candidate
Capability Gap
Risk Escalation
```

Required Pantheon gate:

```text
source sufficiency
contradiction review
scope fit
approval expectation
memory impact
```

Forbidden interpretation:

```text
The final writer card does not produce a deliverable by itself.
```

### 2. Scheduled nightly review

Use for routine monitoring tasks such as repository status review, open PR review, issue triage, dashboard status preparation or integration drift detection.

Required execution guardrails:

```text
idempotency key
runtime cap
explicit assignee profile
candidate-only output
no external mutation by default
```

Allowed output:

```text
Review Note
Risk Escalation
Capability Gap
Status Candidate
Next Action Candidate
```

Forbidden interpretation:

```text
A scheduled review must not update doctrine, move approval status, promote memory, merge code or send anything externally without a separate governed approval.
```

### 3. Swarm with verifier and synthesizer

Use only when the work naturally decomposes into parallel viewpoints.

Examples:

```text
source audit + contradiction review + synthesis
repository scan + doctrine compatibility review + patch candidate
multi-domain review + risk classification + decision brief
```

Required structure:

```text
bounded Task Contract
explicit worker purposes
shared scope limit
verifier output as pre-review only
synthesizer output as candidate only
Evidence Pack Candidate
User Decision Gate when consequential
```

Forbidden interpretation:

```text
A swarm is not a Governance College.
A verifier profile is not Zeus.
A synthesizer profile is not final authority.
```

## Command posture

Pantheon must not canonize Hermes CLI syntax.

Hermes command shape can change across versions. Before using a workflow locally, verify the installed surface:

```bash
hermes --version
hermes kanban assignees --json
hermes kanban create --help
hermes kanban swarm --help
```

Minimum checks before treating a Hermes Kanban workflow as locally usable:

```text
profiles exist
board exists
gateway or dispatcher is running if required by the installed version
create command accepts the intended flags
swarm command syntax matches the installed version
idempotency behavior is verified with --json
runtime cap behavior is understood
workspace behavior is understood
```

If the installed CLI differs from an external post, local `--help` wins.

If local behavior conflicts with Pantheon doctrine, Pantheon doctrine wins and the Hermes workflow must be reduced, blocked or reframed.

## Required Evidence Pack summary

For a governed Hermes Kanban run, the returned Evidence Pack Candidate should summarize:

```text
Task Contract id or summary
Hermes board or task references
profiles involved
worker purposes
source references used
assumptions
contradictions
runtime-level actions relevant to governance
outputs produced
capability gaps
risks left open
approval gap
memory candidates, if any
```

Raw runtime logs are not Evidence Pack by themselves.

Kanban comments are not Evidence Pack by themselves.

They may support an Evidence Pack Candidate when summarized, scoped and linked.

## Relation to open work

This pattern must stay compatible with:

```text
Pantheon Control dashboard candidate doctrine
module invocation and connectivity preflight doctrine
governed composition / capability registry candidate doctrine
```

The dashboard may display Hermes Kanban status.

Preflight may check that a module, profile, board, command surface or connector is available.

Governed composition may propose the task graph shape.

None of those makes Hermes Kanban a Pantheon runtime or a governance authority.

## Status decisions

```text
Accepted:
Hermes Kanban as external execution coordination.
Parent gates, idempotency and runtime caps as useful execution guardrails.
Verifier and synthesizer as candidate-producing execution profiles.

Refused:
Hermes Kanban as governance authority.
Hermes done as approval.
Hermes comments or runtime state as Canonical Memory.
Automatic external action after worker success.

To verify:
Installed Hermes CLI syntax.
Dispatcher / gateway behavior in the local stack.
Swarm flag shape for the installed version.
Idempotency behavior against the local board.
Profile availability and scope.

To arbitrate:
Whether nightly reviews may update dashboard status automatically, or only propose status changes.
Whether Pantheon Control may trigger Hermes Kanban tasks directly, and under which Task Contract / approval level.
```

## Final rule

```text
Hermes Kanban coordinates execution.
Pantheon governs status, proof, approval, memory, scope and external action.
```
