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

```text
Work Issue assigned_to=hermes
!= execution admitted
!= Hermes run started
!= Hermes result accepted
```

The bridge records legitimacy and runtime observations without becoming the runtime path.

## Governed lifecycle

```text
Cockpit handoff preview
        ↓
human creates durable Work Issue
        ↓
Work Issue assigned_to=hermes
        ↓
human creates bounded Execution Admission
        ↓
admission_id + exact Work Issue version + explicit expiry
        ↓
[optional human revocation before consumption]
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
review / waiting
        ↓
human/governance review continues
```

Critical non-equivalences:

```text
admission != dispatch
admission != Hermes run
expiry check != scheduler
revocation != runtime cancellation after start
runtime-start callback != command to start
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
  work_issue_version:
  decision: allow
  requested_effect: read_only
  task_contract_ref:
  context_pack_ref:
  preview_digest:
  handoff_request_digest:
  ttl_seconds:
  expires_at:
  admission_digest:
  admitted_by:
  admitted_at:
```

The first executable slice is deliberately narrow:

```text
requested_effect = read_only
human admission required
explicit bounded lifetime required
single handoff
single Work Issue version
single admission
single consuming Hermes run
```

This is a conservative implementation boundary, not a permanent policy for every low-risk task.

## Admission states

The candidate external implementation projects these states:

```text
admitted  = valid and consumable
revoked   = human revocation recorded before consumption
expired   = expires_at passed
stale     = bound Work Issue or contract state changed
consumed  = one Hermes run already claimed the admission
```

State projection is governance status. It is not a runtime worker state machine.

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
explicit ttl present and bounded
idempotency key present
```

The admitted Work Issue version is captured atomically with the admission.

A failed condition is refused rather than repaired automatically.

## Bounded lifetime

An admission must have an explicit finite lifetime.

The first external MVP candidate constrains the TTL to a bounded interval. The exact product choices may change, but the governance rule is stable:

```text
no implicit infinite admission
```

Expiry is checked when the admission is read or consumed.

Pantheon does not create an expiry scheduler, timer worker or cleanup queue merely to change the projected state.

```text
now >= expires_at
→ projected state = expired
→ runtime envelope refused
```

## Stale invalidation

Admission is bound to the exact Work Issue version that existed when the human admitted execution.

If the Work Issue changes before Hermes starts — including a meaningful comment/version change — the admission becomes stale.

```text
admitted work_issue_version != current work_issue_version
→ stale
→ runtime envelope refused
→ runtime start refused
```

This prevents a previously approved execution boundary from silently following later dossier changes.

## Human revocation before consumption

A human may revoke an unconsumed admission.

Revocation is recorded as a separate append-only event rather than mutating the immutable admission.

Candidate shape:

```yaml
execution_admission_event:
  event_type: revoked
  admission_ref:
  actor:
  reason:
  idempotency_key:
  occurred_at:
```

Revocation is allowed only while the projected state is `admitted`.

```text
revoked/expired/stale/consumed
→ cannot be revoked again as a new effect
```

A revocation does not pretend to cancel a Hermes process that has already started. Runtime cancellation, if adopted later, belongs to a separate Hermes/runtime capability and gate.

## What admission authorizes

Admission means:

> This exact Work Issue version, under this exact Task Contract, Context Pack, scope, effect ceiling and bounded lifetime, may be consumed once by an external Hermes runtime binding.

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

Hermes may retrieve one exact consumable envelope by `admission_id`.

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

A revoked, expired, stale or consumed admission is not returned as a consumable execution envelope.

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

After Hermes has started work, its adapter reports the external runtime identity with the `admission_id`, external `run_id`, admitted Work Issue version, Hermes actor and idempotency key.

Pantheon verifies that:

- the admission is still `admitted`;
- it has not expired or been revoked;
- the Work Issue version still equals the admitted version;
- the Work Issue remains open and assigned to Hermes;
- Task Contract and Context Pack remain unchanged;
- another run has not consumed the admission;
- the callback uses the Hermes adapter credential.

Only then is the governed HermesRun observation recorded as `running` and the admission projected as `consumed`.

This callback records external runtime state. It does not start the runtime.

## External Hermes return

Hermes returns candidate material through a normalized callback tied to the exact `admission_id` and external `run_id`.

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

The first admission slice accepts only `read_only`.

It does not authorize Agency Data consequential mutation, external communication, repository mutation, document transmission, canonical/memory promotion, installation, activation or external professional commitment.

Those effects retain their own applicable Pantheon gates.

## Retry and continuation remain open

Expiry, stale invalidation and pre-consumption human revocation are now defined and have an external MVP candidate implementation.

Still unresolved before production runtime binding:

```text
failed-start retry policy
partial-run continuation
new run after returned/failed state
bounded multi-use admission, if ever needed
runtime cancellation after consumption
```

Current posture remains:

```text
one admission = one execution opportunity
```

A failed, revoked, expired, stale or consumed admission is not silently recycled.

## Responsibility allocation

### Pantheon governs

- admissibility;
- exact Task Contract / Context Pack binding;
- exact Work Issue version binding;
- effect ceiling and bounded lifetime;
- human decision and revocation trace;
- admission identity/digest/state;
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
- explicit admission lifetime choice;
- admission/revocation action and receipt;
- admission projected state;
- observed run status;
- returned candidate and review need.

### Human approves

In the conservative first slice:

- creation of the durable Work Issue;
- execution admission with explicit lifetime;
- optional revocation before consumption.

Future low-risk automatic admission requires a separately reviewed policy.

### Forbidden

- Pantheon dispatching Hermes;
- PostgreSQL acting as runtime queue;
- `claim next job` semantics;
- automatic provider/model selection by Pantheon;
- Pantheon retries or runtime scheduling;
- expiry scheduler introduced merely for admission status;
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
hermes_execution_admission_events
hermes_runs.admission_ref

POST /v1/cockpit/hermes-handoffs/{handoff_id}/admissions
GET  /v1/cockpit/hermes-execution-admissions/{admission_id}
POST /v1/cockpit/hermes-execution-admissions/{admission_id}/revocations
GET  /v1/hermes/execution-admissions/{admission_id}
POST /v1/hermes/execution-admissions/{admission_id}/runs/start
POST /v1/hermes/execution-admissions/{admission_id}/runs/{run_id}/return
```

There is deliberately no collection route for pending admissions.

Current implementation status:

```text
handoff preview                         implemented candidate externally
human Work Issue submission             implemented candidate externally
read-only execution admission           implemented candidate externally
explicit bounded TTL                    implemented candidate externally
lazy expiry projection                  implemented candidate externally
Work Issue version stale invalidation   implemented candidate externally
human pre-consumption revocation        implemented candidate externally
exact execution-envelope lookup by ID   implemented candidate externally
external runtime-start callback record  implemented candidate externally
normalized runtime-return callback      implemented candidate externally
live Hermes transport/client binding    not implemented
runtime dispatch                        forbidden in Pantheon
retry/continuation/runtime cancel        not implemented
production activation                   not authorized
```

The external status remains subject to its own CI and review. This document does not promote or activate it.

## Final rule

```text
Pantheon may say: this exact bounded work is admitted until this expiry.
Pantheon may say: this unconsumed admission was revoked or became stale.
Pantheon may record: Hermes reports this exact run started/returned.

Pantheon must not say: I dispatched or ran Hermes.

Hermes starts Hermes.
Pantheon governs what the admission, start and return mean.
```
