# Hermes Execution Admission Bridge

Status: candidate support doctrine — external MVP partial / live Hermes transport not implemented.

Date: 2026-07-25

This document defines the narrow boundary between a governed Work Issue and the external Hermes runtime that actually executes it.

It specializes `HERMES_INTEGRATION.md`, `HERMES_INTEGRATION_MODELS_RECONCILIATION.md`, `TASK_CONTRACTS.md`, `CONTEXT_PACKS.md`, `REQUEST_LIFECYCLE.md` and `WORK_ISSUE_AND_DELEGATED_MERGE_MODEL.md`.

It does not create a Pantheon runtime, queue, scheduler, worker, dispatcher, provider router, retry engine, Hermes client, automatic approval engine or memory engine.

```text
Cockpit exposes and captures intent.
Pantheon governs admission and consequential effects through distinct gates.
Hermes executes externally.
The human decides execution admission in the conservative first slice.
```

The active reconciliation rule is:

```text
Execution Admission = permission to START one bounded Hermes run
Effect chokepoint    = authorization gate for EACH consequential effect during a run

admission granted != consequential effect authorized
read_only admission  != later write/external/canonical authority
```

## Core distinction

```text
Work Issue assigned_to=hermes
!= execution admitted
!= Hermes run started
!= consequential effect authorized
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
Hermes executes within admitted run ceiling
        ↓
[each consequential effect, if any, requires the separate effect chokepoint]
        ↓
Hermes reports normalized return + optional separate rich Result Candidate
        ↓
review / waiting
        ↓
human/governance review continues
```

Critical non-equivalences:

```text
admission != dispatch
admission != Hermes run
admission != effect authorization
expiry check != scheduler
revocation != runtime cancellation after start
runtime-start callback != command to start
Hermes returned != issue resolved
HermesResultCandidate != Evidence
runtime return != Evidence admitted
runtime success != governance success
```

## Execution Admission

An Execution Admission is an immutable authorization record for one exact runtime opportunity. It answers whether one exact run may start; it does not pre-authorize consequential effects that the runtime may later attempt.

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

The `decision: allow` field above is the admission disposition of this candidate record. It must not be read as a reusable Pantheon Decision authorizing downstream effects.

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
- a consequential effect during the run is authorized;
- the Task Contract became canonical memory or doctrine;
- a result will be accepted;
- evidence exists;
- consequential downstream effects are pre-approved.

The current `read_only` admission therefore authorizes a run opportunity only within a read-only ceiling. If Hermes later requests a write, external effect, canonical effect, installation, activation, transmission or other consequential operation, that operation remains subject to the effect-centered Pantheon chokepoint and its own decision expectation. The admission record cannot be reused as that effect authorization.

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

## Effect authorization during the run

Execution Admission and effect authorization are composed layers, not competing models.

```text
Execution Admission
→ may this exact bounded run start?

Effect chokepoint / PEP → PDP
→ may this exact consequential effect occur now?
```

The effect gate binds its own scope, object identity, digest, required ceiling, current policy flags and human decision. Human issuer authentication proves who signed the decision when configured; it still does not itself grant approval.

```text
issuer_authenticated != approval
valid decision != policy effect flag allow
admission granted != effect authorization
```

The current admission slice is `read_only`. Therefore an external or canonical effect attempted during that run must not be inferred from the admission and remains blocked unless a separately reviewed future contract explicitly permits the applicable effect path.

Pantheon remains the policy/governance plane; Hermes remains the executor. The PEP/chokepoint may be implemented in the external runtime integration layer, but Pantheon does not execute the native operation itself.

## External Hermes return

Hermes returns candidate material through a callback tied to the exact `admission_id` and external `run_id`.

Current candidate outcome vocabulary:

```text
result_candidate
partial
failed
capability_gap
```

The persisted Work Issue return shape remains deliberately bounded to:

```text
outcome
summary
trace_refs
result_refs                  optional
evidence_candidate_refs      optional
```

`schemas/work_issue_slice.schema.yaml` remains the persistence authority for this Work Issue slice and has `additionalProperties: false`. Therefore `source_refs`, limitations/known limits, open questions and arbitrary candidate payload are not silently embedded in the Work Issue return.

The richer representation documented at `templates/hermes/returns/loop_result_candidate.json` remains a descriptive candidate template, explicitly `not_executable_schema`; it is still not persistence authority for the Work Issue slice.

A separate external implementation candidate now exists in stacked `ifanjuang/pantheon-mvp` PR #67. It persists an immutable `HermesResultCandidate` linked to the exact `run_id`, `admission_id` and `issue_id`, while the Work Issue keeps only the bounded normalized return plus a server-generated `result_ref`.

Candidate rich fields include:

```text
result_type
candidate_payload
confidence_note
known_limits
open_questions
source_refs
trace_refs
missing_evidence
evidence_candidate_refs
```

The external candidate enforces these distinctions as data:

```text
governance_result_status = candidate
evidence_status = candidate
trace_is_not_proof = true
approval_still_required = true
human_decision_required = true
```

Its `source_refs` must be a subset of the source references admitted in the exact Context Pack. A source outside that Context Pack is refused atomically rather than being accepted as post-hoc authority.

```text
HermesResultCandidate implemented candidate externally
!= Work Issue schema widened
!= Evidence admitted
!= Knowledge promoted
!= Decision recorded
!= canonical truth
```

The richer candidate and bounded Work Issue return are persisted atomically in the external #67 slice: failure of either side rolls back the combined return transaction.

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

Those effects retain their own applicable Pantheon gates. The per-effect chokepoint remains authoritative even after a run has been admitted and started.

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

- run admissibility;
- exact Task Contract / Context Pack binding;
- exact Work Issue version binding;
- run effect ceiling and bounded lifetime;
- human admission decision and revocation trace;
- admission identity/digest/state;
- admission consumption;
- validation of runtime start/return callbacks;
- observed run status;
- policy/preflight/decision validation for each consequential effect;
- downstream Evidence, Knowledge, approval and canonicalization boundaries.

### Hermes executes

- actual runtime start;
- worker/subagent selection;
- tools;
- provider/model routing;
- runtime scheduling/retries within admitted authority;
- read-only work within the current admission ceiling;
- native consequential operations only after their applicable effect gate authorizes them;
- runtime run identifiers;
- execution traces;
- rich candidate material returned for review.

### Cockpit / OpenWebUI exposes

- prepared handoff scope;
- Work Issue;
- explicit admission lifetime choice;
- admission/revocation action and receipt;
- admission projected state;
- observed run status;
- returned normalized result;
- linked rich Result Candidate and review need when available;
- separate effect Decision Requests/Gates when a consequential effect is proposed.

### Human approves

In the conservative first slice:

- creation of the durable Work Issue;
- execution admission with explicit lifetime;
- optional revocation before consumption;
- separately, any consequential effect decision required by its own gate.

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
- admission being reused as an effect Decision;
- runtime success being treated as Evidence or approval;
- rich result candidate being promoted automatically to Evidence, Knowledge or canonical truth.

## External MVP mapping

`ifanjuang/pantheon-mvp` contains external implementation candidates.

Current base candidate components in PR #65:

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

The stacked PR #67 adds the separate rich return persistence:

```text
hermes_result_candidates
HermesResultCandidate
bounded normalized_return + server-generated result_ref
```

There is deliberately no collection route for pending admissions.

Current implementation status:

```text
handoff preview                         implemented candidate externally (#65)
human Work Issue submission             implemented candidate externally (#65)
server-validated Context Pack scope      implemented candidate externally (#65)
read-only execution admission           implemented candidate externally (#65)
explicit bounded TTL                    implemented candidate externally (#65)
lazy expiry projection                  implemented candidate externally (#65)
Work Issue version stale invalidation   implemented candidate externally (#65)
human pre-consumption revocation        implemented candidate externally (#65)
exact execution-envelope lookup by ID   implemented candidate externally (#65)
external runtime-start callback record  implemented candidate externally (#65)
normalized runtime-return callback      implemented candidate externally (#65)
rich HermesResultCandidate persistence  implemented candidate externally (#67)
rich result source-scope validation     implemented candidate externally (#67)
Hermes global Agency Data bypass        disabled in external #65 candidate
scoped Hermes Agency Data capability    not implemented
live Hermes transport/client binding    not implemented
runtime dispatch                        forbidden in Pantheon
retry/continuation/runtime cancel       not implemented
production activation                   not authorized
```

The external status remains subject to its own CI and review. This document does not promote or activate it.

## Final rule

```text
Pantheon may say: this exact bounded work is admitted until this expiry.
Pantheon may say: this unconsumed admission was revoked or became stale.
Pantheon may say: this exact consequential effect is allowed or refused by its own gate.
Pantheon may record: Hermes reports this exact run started/returned.
Pantheon may retain: Hermes returned this Result Candidate for review.

Pantheon must not say: I dispatched or ran Hermes.
Pantheon must not say: run admission pre-authorized every later effect.
Pantheon must not say: a returned candidate is Evidence or truth.

Hermes starts Hermes.
Hermes executes native operations.
Pantheon governs what admission, effect authorization, start and return mean.
```
