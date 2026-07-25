# Hermes Execution Admission Bridge

Status: candidate support doctrine — external MVP partial / live Hermes transport not implemented.

Date: 2026-07-25

This document defines the narrow boundary between a governed Work Issue that is ready for Hermes and the external Hermes runtime that actually executes it.

It specializes `HERMES_INTEGRATION.md`, `TASK_CONTRACTS.md`, `CONTEXT_PACKS.md`, `REQUEST_LIFECYCLE.md` and `WORK_ISSUE_AND_DELEGATED_MERGE_MODEL.md`.

It does not create a Pantheon runtime, queue, scheduler, worker, dispatcher, provider router, retry engine, Hermes client, automatic approval engine or memory engine.

```text
Cockpit exposes and captures intent.
Pantheon governs admissibility.
Hermes executes externally.
The human decides the execution admission in the conservative first slice.
```

## Problem

A Work Issue assigned to Hermes is not sufficient authority to start execution.

```text
Work Issue assigned_to=hermes
!=
execution admitted
!=
Hermes run started
```

The system needs a traceable bridge that can answer:

- which exact Work Issue is eligible;
- which exact Task Contract and Context Pack are bound;
- who admitted execution;
- whether that admission has already been consumed;
- which external Hermes run, if any, reported that it started under the admission.

The bridge must answer those questions without becoming a dispatch system.

## Core model

```text
submitted Cockpit handoff
        ↓
Work Issue assigned_to=hermes
        ↓
Human Execution Admission
        ↓
immutable admission_id
        ↓
external delivery / binding outside Pantheon
        ↓
Hermes adapter fetches exact envelope by admission_id
        ↓
Hermes runtime starts itself
        ↓
Hermes adapter reports external run_id
        ↓
Pantheon records the HermesRun observation
```

Critical non-equivalences:

```text
admission != dispatch
admission != Hermes run
callback recorded != command to start
runtime started != task succeeded
runtime success != Evidence
runtime success != governance success
```

## Execution Admission

An Execution Admission is a governed authorization record for one exact execution opportunity.

Candidate shape:

```yaml
execution_admission:
  admission_id:
  handoff_ref:
  work_issue_ref:
  decision: allow
  requested_effect: read_only
  task_contract_ref:
  context_pack_ref:
  preview_digest:
  handoff_request_digest:
  admission_digest:
  admitted_by:
  admitted_at:
```

The first executable MVP slice is intentionally narrow:

```text
requested_effect = read_only
human admission required
single handoff
single Work Issue
single execution admission
single consuming Hermes run
```

This is a conservative implementation boundary, not a universal future policy.

## What admission means

Admission means:

> This exact Work Issue, under this exact Task Contract, Context Pack, scope and effect ceiling, may be consumed once by an external Hermes runtime binding.

Admission does not mean:

- Pantheon has called Hermes;
- Hermes is running;
- a provider has been selected;
- a worker has been assigned inside Hermes;
- the Task Contract became canonical memory or doctrine;
- the result will be accepted;
- evidence exists;
- a consequential downstream effect is pre-approved.

## Admission preconditions

For the first slice, the admission guard verifies at minimum:

```text
handoff exists
Work Issue exists
Work Issue assigned_to = hermes
Work Issue status = open
requested_effect = read_only
Task Contract ref unchanged
Context Pack ref unchanged
immutable handoff digest still matches
no existing Hermes run
no prior admission for the same single-use handoff
human actor present
idempotency key present
```

If one condition fails, admission is refused rather than repaired automatically.

## Runtime-facing envelope

Pantheon may expose one admitted envelope to Hermes by exact `admission_id`.

```yaml
hermes_execution_envelope:
  admission:
  task_contract:
  context_pack:
  question:
  selected_context:
  runtime_instruction: null
  dispatch_requested: false
```

The lookup is explicit by ID.

The governance surface must not expose a generic endpoint equivalent to:

```text
GET /pending-hermes-work
GET /queue
claim-next-job
lease-work
retry-job
```

Those patterns would make Pantheon or its PostgreSQL store part of the execution queue.

## Delivery of admission_id

How an `admission_id` reaches the Hermes adapter is a runtime/deployment binding concern.

Candidate mechanisms may later include:

- an OpenWebUI/Hermes integration action;
- a runtime-owned callback;
- a Hermes-side polling source that is not a Pantheon queue;
- an operator-mediated invocation;
- another explicitly reviewed adapter.

No delivery mechanism is adopted merely because the admission record exists.

```text
admission created != runtime notified
binding available != binding selected
binding selected != dependency adopted
```

## External Hermes start

Hermes owns the actual execution start.

After the runtime has started work, its adapter may report:

```yaml
external_runtime_start_observation:
  admission_id:
  external_run_id:
  expected_work_issue_version:
  hermes_actor:
  idempotency_key:
```

Pantheon then verifies that:

- the admission exists and is unused;
- the Work Issue is still current and open;
- the Work Issue is still assigned to Hermes;
- Task Contract and Context Pack still match;
- the callback comes through the Hermes adapter credential;
- the admission has not been consumed by another run.

Only then may the governed record show the Hermes run as `running`.

This records observed runtime state. It does not start the runtime.

## Run return

The existing Work Issue model remains responsible for normalized Hermes return records.

Hermes may return:

```text
Result Candidate
Evidence Pack Candidate
Capability Gap
Risk Escalation
Runtime Trace Reference
```

The return remains candidate material.

```text
Hermes returned != issue resolved
Hermes result != Evidence admitted
Hermes done != Pantheon approved
```

Human review and consequential-effect gates remain downstream where required.

## Effect ceiling

The first execution-admission slice accepts only:

```text
read_only
```

This avoids incorrectly treating a general execution admission as permission for:

- Agency Data mutation;
- external communication;
- repository mutation;
- document transmission;
- canonical promotion;
- memory promotion;
- installation or activation;
- external professional commitment.

Any such effect still resolves through its applicable Pantheon gate.

## Revocation, expiry and retry

These are not implemented in the first slice.

Before a production runtime binding is activated, the design must explicitly settle:

```text
admission expiry
human revocation before consumption
stale admission invalidation
failed-start retry policy
partial-run continuation
new run after returned/failed state
single-use versus bounded multi-use
```

Until then:

```text
one admission = one execution opportunity
```

A failed or obsolete admission is not silently recycled.

## Responsibility allocation

### Pantheon governs

- admissibility;
- exact Task Contract / Context Pack binding;
- scope and effect ceiling;
- human decision trace;
- admission identity and digest;
- consumption status;
- validation of runtime callbacks;
- observed run status;
- downstream evidence/approval boundaries.

### Hermes executes

- worker/subagent selection;
- runtime scheduling;
- tools;
- provider/model routing;
- retries within its runtime authority;
- actual network/process execution;
- runtime run identifiers;
- execution traces.

### Cockpit / OpenWebUI exposes

- prepared handoff scope;
- Work Issue;
- admission action and receipt;
- whether an admission has been consumed;
- run status returned by the governed record;
- candidate outputs and review needs.

### Human approves

In the conservative first slice:

- creation of the durable Work Issue;
- execution admission.

Future low-risk automatic admission requires a separately reviewed policy; runtime convenience does not create it implicitly.

### Forbidden

- Pantheon dispatching Hermes;
- PostgreSQL acting as a runtime work queue;
- a `claim next job` endpoint;
- automatic provider/model selection by Pantheon;
- Pantheon retries or runtime scheduling;
- Cockpit fabricating a Hermes `run_id`;
- admission implying downstream consequential authority;
- runtime success being treated as Evidence or approval.

## External MVP mapping

`ifanjuang/pantheon-mvp` contains an external implementation candidate for this bridge.

Current candidate components:

```text
cockpit_hermes_handoffs
hermes_execution_admissions
hermes_runs.admission_ref

POST /v1/cockpit/hermes-handoffs/{handoff_id}/admissions
GET  /v1/hermes/execution-admissions/{admission_id}
POST /v1/hermes/execution-admissions/{admission_id}/runs/start
```

The third route is a runtime callback record. It is not a command issued by Cockpit to start Hermes.

There is deliberately no collection route for pending admissions.

Current implementation status:

```text
handoff preview                         implemented candidate externally
human Work Issue submission             implemented candidate externally
read-only execution admission           implemented candidate externally
exact execution-envelope lookup by ID   implemented candidate externally
external runtime-start callback record  implemented candidate externally
live Hermes transport/client binding    not implemented
runtime dispatch                        forbidden in Pantheon
admission expiry/revocation/retry        not implemented
production activation                   not authorized
```

## Final rule

```text
Pantheon may say: this exact work is admitted.
Pantheon must not say: I have now run Hermes.

Hermes starts Hermes.
Pantheon records and governs what that start means.
```
