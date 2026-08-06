# Hermes Execution Preparation Convergence

Status: validation-only convergence map.

## Objective

Make the existing Pantheon-to-Hermes execution-preparation path inspectable end to end without introducing a new runtime object, generic agent graph or execution authority.

This document is subordinate to the existing governance owners. It does not replace their contracts.

## Decision

```text
No Hermes Execution Plan object.
No generic ExecutionRequest object.
No Extra runtime dependency.
No LangGraph adoption.
No Agent / Orchestrator / Resolver model in Pantheon.
```

The existing spine is sufficient:

```text
Cockpit handoff preview
→ Task Contract Candidate
→ Context Pack Candidate
→ human Work Issue
→ immutable Execution Admission
→ Hermes runtime posture qualification
→ immutable launch reservation
→ Launch Context Snapshot
→ external Hermes run
→ bounded scoped-context reads
→ Runtime Return / Execution Result Candidate
→ human review and consequential paths
```

## Existing authority owners

```text
MVP_GOVERNED_TASK_LOOP.md
→ smallest governed end-to-end loop

TRIPARTITE_INTERFACE_SPEC.md
→ cross-layer object grammar

HERMES_EXECUTION_ADMISSION_BRIDGE.md
→ one bounded human-admitted runtime opportunity

HERMES_RUN_LAUNCH_JUNCTION.md
→ external Runs binding, reservation and launch correlation

Task Contract
→ governed intent and output expectations

Context Pack
→ admitted context identity and scope

Work Issue
→ durable work owner, not a queue

Execution Admission
→ human permission for one bounded runtime opportunity

Launch Context Snapshot
→ immutable technical launch material

Runtime Return / Execution Result Candidate
→ candidate output, never Evidence or Decision by execution success
```

## Executable path observed in `pantheon-mvp`

### 1. Handoff preparation

The Cockpit prepares a bounded preview from server-reconstructed scope. The resulting handoff retains exact Task Contract and Context Pack references plus a deterministic preview digest.

```text
preview != submission
submission != admission
UI request != authorized context
```

### 2. Human admission

`hermes_execution` creates one immutable, TTL-bounded Execution Admission tied to the exact Work Issue version and handoff basis.

```text
admission != dispatch
admission != effect authorization
```

### 3. Runtime posture qualification

Before a launch reservation is requested, the external binding requires one qualified observation combining:

```text
exact named profile route
reviewed API-server tool surface
fresh profile-local memory-status receipt
```

The memory receipt is accepted only when:

- the observed profile equals the expected profile;
- the source is the official read-only Hermes memory-status command;
- the capture time is timezone-aware and no older than five minutes;
- the command targets the observed profile;
- external memory provider, built-in memory injection, built-in user-profile injection and memory tool are all off;
- no raw output, mutation effect, authority effect or Evidence classification is claimed;
- the output digest is well formed.

The observer also verifies the reviewed toolset envelope and explicit allowed/required tools. A non-qualified observation fails before reservation or submission.

```text
runtime posture qualified != task authorized
memory off != built-in memory injection off
qualified tool surface != production activation
```

### 4. Launch reservation and immutable snapshot

`hermes_launch_context.reserve_launch` runs in a `REPEATABLE READ` transaction. It:

- locks the admission;
- requires exact `admitted` state;
- refuses a second reservation;
- compares the admission and immutable handoff through the same execution basis;
- requires the first slice to remain `read_only`;
- materializes only admitted entities;
- freezes Task Contract, Context Pack manifest, Work Issue version and bounded owner reads;
- computes a canonical SHA-256 digest;
- applies a short launch TTL and maximum snapshot size.

A replay returns the same reservation but may not be interpreted as permission to submit Hermes again.

```text
launch reservation != runtime dispatch
reservation consumed != Hermes run started
launch snapshot != Evidence
```

### 5. External run and start correlation

The external run binding:

1. qualifies the runtime posture;
2. requests exactly one launch reservation;
3. refuses automatic resubmission of a replayed reservation;
4. submits exactly one external Hermes run;
5. passes the admission identity as the session correlation;
6. does not select model or provider;
7. records the real Hermes `run_id` against the exact reservation and expected Work Issue version.

Ambiguous submission or registration remains explicit and requires operator reconciliation. There is no automatic retry.

### 6. Scoped runtime context

A running Hermes invocation may read only identities already admitted in the Context Pack through fixed field projections. There is no global Agency Data listing, search, arbitrary SQL, source-binary dereference or write path.

```text
Context Pack inclusion != Evidence
current owner read != admission-time snapshot
read access != write authority
```

### 7. Candidate return

The runtime return remains linked to admission, run and Work Issue. Rich output is persisted as candidate material and may enter existing ProjectClaim, Knowledge variant, relation, Work Issue or Decision Request review paths only through their separate governed transitions.

```text
runtime success != Evidence
runtime return != Work Issue resolution
result candidate != Knowledge
result candidate != Decision
```

## Validation matrix

The current executable path was checked for the following conditions.

```text
Task Contract / Context Pack basis mismatch
→ refused at launch reservation

stale Work Issue version
→ refused during start/return registration

unqualified Hermes profile or tool surface
→ refused before reservation

missing, stale, future-dated or misattributed memory receipt
→ not qualified

active external or built-in memory axis
→ not qualified

tool-surface drift outside the reviewed allowlist
→ not qualified

scope widening
→ refused by admitted-identity checks

second launch reservation or replay submission
→ refused; operator reconciliation required

provider/model override
→ absent from the binding contract

automatic retry after ambiguous launch
→ forbidden and tested

missing run/admission correlation
→ start or scoped-context access refused
```

## Distillation from `extra-org/extra`

The reviewed repository is useful only as a pattern source for:

- semantic validation before execution;
- immutable normalized runtime input;
- separation of long-lived runtime infrastructure from request-scoped context;
- stable trace correlation;
- later adapter stub generation from stable contracts.

Pantheon already provides the first four through its existing admission spine. Adapter generation may be reconsidered only after multiple concrete adapter contracts stabilize.

Extra is not selected as a dependency, binding or runtime.

## Remaining work

No generic execution-preparation gap was demonstrated.

Future work must remain capability-specific. The Revit preflight and single-use action authorization documented separately are one such specialization; they must compose with this spine rather than replace it.

Any later code change must be justified by a reproduced failing invariant and must extend an existing validator or adapter boundary.

## Completion criteria

This convergence subject is complete when:

- the map agrees with current `pantheon-mvp` code and tests;
- open PRs do not introduce a competing execution owner;
- `extra-org/extra` remains classified as reference material only;
- no new schema, runtime, queue, scheduler, provider router, plugin manager, memory engine or automatic approval path is added.

## Final rule

```text
Pantheon governs intent, scope and admission.
pantheon-mvp owns authoritative persistence and bounded junctions.
Hermes qualifies its runtime posture and executes.
Cockpit projects state and review needs.
The human decides consequential outcomes.
```
