# Hermes Execution Admission Bridge

Status: candidate support doctrine — external MVP partial / live Hermes transport not implemented.

Date: 2026-07-25

This document defines the narrow boundary between a governed Work Issue and the external Hermes runtime that actually executes it.

It specializes `HERMES_INTEGRATION.md`, `TASK_CONTRACTS.md`, `CONTEXT_PACKS.md`, `REQUEST_LIFECYCLE.md` and `WORK_ISSUE_AND_DELEGATED_MERGE_MODEL.md`.

It does not create a Pantheon runtime, queue, scheduler, worker, dispatcher, provider router, retry engine, Hermes client, automatic approval engine or memory engine.

```text
Cockpit exposes and captures intent.
Pantheon governs admissibility.
Hermes executes externally.
The human decides execution admission in the conservative first slice.
```

## Core distinction

A Work Issue assigned to Hermes is not sufficient authority to start execution.

```text
Work Issue assigned_to=hermes
!=
execution admitted
!=
Hermes run started
!=
Hermes result accepted
```

The bridge must record legitimacy and runtime observations without becoming the runtime path itself.

## Governed lifecycle

```text
Cockpit handoff preview
        ↓
human creates durable Work Issue
        ↓
Work Issue assigned_to=hermes
        ↓
human creates Execution Admission
        ↓
immutable admission_id
        ↓
external delivery/binding outside Pantheon
        ↓
Hermes fetches exact envelope by admission_id
        ↓
Hermes starts itself
        ↓
Hermes reports external run_id
        ↓
Pantheon records HermesRun observation
        ↓
Hermes executes
        ↓
Hermes reports normalized return candidate
        ↓
Pantheon records review/waiting state
        ↓
human/governance review continues
```

Critical non-equivalences:

```text
admission != dispatch
admission != Hermes run
runtime-start callback != command to start
runtime started != task succeeded
Hermes returned != issue resolved
runtime return != Evidence admitted
runtime success != governance success
```

## Execution Admission

An Execution Admission is an immutable authorization record for one exact runtime opportunity.

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

The first executable slice is deliberately narrow:

```text
requested_effect = read_only
human admission required
single handoff
single Work Issue
single admission
single consuming Hermes run
```

This is a conservative implementation boundary, not a permanent policy for every low-risk task.

## Admission preconditions

The guard verifies at minimum:

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

A failed condition is refused rather than repaired automatically.

## What admission authorizes

Admission means:

> This exact Work Issue, under this exact Task Contract, Context Pack, scope and effect ceiling, may be consumed once by an external Hermes runtime binding.

Admission does not mean:

- Pantheon called Hermes;
- Hermes is running;
- a provider/model was selected;
- an internal Hermes worker was assigned;
- the Task Contract became canonical memory or doctrine;
- a result will be accepted;
- evidence exists;
- consequential downstream effects are pre-approved.

## Runtime-facing envelope

Hermes may retrieve one exact admitted envelope by `admission_id`.

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

The governance surface must not expose generic work-claim semantics such as:

```text
GET /pending-hermes-work
GET /queue
claim-next-job
lease-work
retry-job
```

Those patterns would make Pantheon or PostgreSQL part of the runtime queue.

## Delivery of admission_id

How an `admission_id` reaches the Hermes adapter is a runtime/deployment binding concern.

Potential future bindings may include an OpenWebUI/Hermes action, a runtime-owned callback, an operator-mediated invocation or another explicitly reviewed adapter.

No delivery binding is adopted merely because the admission record exists.

```text
admission created != runtime notified
binding available != binding selected
binding selected != dependency adopted
```

## External Hermes start

Hermes owns the actual execution start.

After Hermes has started work, its adapter reports the external runtime identity:

```yaml
external_runtime_start_observation:
  admission_id:
  external_run_id:
  expected_work_issue_version:
  hermes_actor:
  idempotency_key:
```

Pantheon verifies that:

- the admission exists and is unused;
- the Work Issue remains current and open;
- the Work Issue remains assigned to Hermes;
- Task Contract and Context Pack remain unchanged;
- the callback uses the Hermes adapter credential;
- another run has not consumed the admission.

Only then is the governed HermesRun observation recorded as `running`.

This callback records external runtime state. It does not start the runtime.

## External Hermes return

Hermes returns candidate material through a normalized callback tied to the exact `admission_id` and `external_run_id`.

Current candidate outcome vocabulary:

```text
result_candidate
partial
failed
capability_gap
```

A normalized return carries at least:

```text
outcome
summary
trace_refs
```

It may additionally carry source references, Evidence Pack Candidate references, limitations and open questions.

Current issue projection:

```text
result_candidate -> review
partial          -> waiting
failed           -> waiting
capability_gap   -> waiting
```

The return never closes the Work Issue automatically.

```text
result_status = candidate
evidence_admitted = false
```

Candidate returns may later support human review, Evidence admission, Change Proposals or other governed actions. Those are separate decisions.

## Effect ceiling

The first admission slice accepts only:

```text
read_only
```

It does not authorize:

- Agency Data consequential mutation;
- external communication;
- repository mutation;
- document transmission;
- canonical promotion;
- memory promotion;
- installation or activation;
- external professional commitment.

Those effects retain their own applicable Pantheon gates.

## Revocation, expiry and retry

These are not implemented in the first slice.

Before production runtime binding, the design must settle:

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
- admission identity/digest;
- admission consumption;
- validation of runtime start/return callbacks;
- observed run status;
- downstream Evidence and approval boundaries.

### Hermes executes

- actual runtime start;
- worker/subagent selection;
- tools;
- provider/model routing;
- runtime scheduling/retries within admitted authority;
- network/process effects within its authority;
- runtime run identifiers;
- execution traces.

### Cockpit / OpenWebUI exposes

- prepared handoff scope;
- Work Issue;
- admission action and receipt;
- admission consumption state;
- observed run status;
- returned candidate and review need.

### Human approves

In the conservative first slice:

- creation of the durable Work Issue;
- execution admission.

Future low-risk automatic admission requires a separately reviewed policy.

### Forbidden

- Pantheon dispatching Hermes;
- PostgreSQL acting as runtime queue;
- `claim next job` semantics;
- automatic provider/model selection by Pantheon;
- Pantheon retries or runtime scheduling;
- Cockpit fabricating a Hermes run ID;
- Cockpit calling runtime-start/runtime-return callbacks;
- admission implying downstream consequential authority;
- runtime success being treated as Evidence or approval.

## External MVP mapping

`ifanjuang/pantheon-mvp` contains an external implementation candidate.

Current candidate components:

```text
cockpit_hermes_handoffs
hermes_execution_admissions
hermes_runs.admission_ref

POST /v1/cockpit/hermes-handoffs/{handoff_id}/admissions
GET  /v1/hermes/execution-admissions/{admission_id}
POST /v1/hermes/execution-admissions/{admission_id}/runs/start
POST /v1/hermes/execution-admissions/{admission_id}/runs/{run_id}/return
```

The two `/v1/hermes/...` POST routes are runtime observations/callback records. They are not commands issued by Cockpit to start or complete Hermes work.

There is deliberately no collection route for pending admissions.

Current implementation status:

```text
handoff preview                         implemented candidate externally
human Work Issue submission             implemented candidate externally
read-only execution admission           implemented candidate externally
exact execution-envelope lookup by ID   implemented candidate externally
external runtime-start callback record  implemented candidate externally
normalized runtime-return callback      implemented candidate externally
live Hermes transport/client binding    not implemented
runtime dispatch                        forbidden in Pantheon
admission expiry/revocation/retry        not implemented
production activation                   not authorized
```

The external status remains subject to its own CI and review. This document does not promote or activate it.

## Final rule

```text
Pantheon may say: this exact work is admitted.
Pantheon may record: Hermes reports this exact run started/returned.

Pantheon must not say: I dispatched or ran Hermes.

Hermes starts Hermes.
Pantheon governs what the start and return mean.
```
