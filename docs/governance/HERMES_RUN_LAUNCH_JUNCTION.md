# Hermes Run Launch Junction

Status: candidate support doctrine — clean external implementation candidate / live Hermes binding not verified / activation not authorized.

Date: 2026-07-25

This document specializes `HERMES_EXECUTION_ADMISSION_BRIDGE.md` for one candidate binding to the public Hermes Agent Runs API.

It does not replace the generic Execution Admission model and does not make `launch_reserved` mandatory for every future runtime binding.

It creates no Pantheon runtime, dispatcher, scheduler, queue, retry worker, provider router, MCP host, plugin manager, memory engine or automatic approval system.

```text
Pantheon governs the launch opportunity and its meaning.
An external Hermes Run Binding performs the native Hermes API call.
Hermes starts and executes its own run.
The human decides admission and separately gated consequential effects.
```

## Current external candidate

The historical implementation PRs were rebuilt after the Cockpit / Agency Data aggregate landed on `pantheon-mvp/main`.

Current review path:

```text
pantheon-mvp #78
  verified Hermes Runs API observer
        ↓
pantheon-mvp #79
  launch reservation
  + Launch Context Snapshot
  + external Runs binding
  + active-context bridge
  + native Pantheon context plugin
```

Historical PRs #71, #75 and technical sync #77 are superseded and closed without merge.

```text
clean replay #78/#79
!= historical branch stack
```

Both current PRs remain draft.

## Why the junction exists

The generic bridge deliberately leaves actual runtime start outside Pantheon.

Hermes exposes `POST /v1/runs`, but that endpoint existing does not make Pantheon a dispatcher.

The candidate therefore separates four acts:

```text
1. Pantheon records one Execution Admission.
2. An external binding reserves that exact launch opportunity.
3. The external binding asks Hermes to create exactly one run.
4. Pantheon records the real run identity returned by Hermes.
```

Core distinctions:

```text
admission != dispatch
launch reservation != dispatch
launch reservation != Hermes run
POST /v1/runs != Pantheon execution
runtime start receipt != Evidence
runtime success != Evidence
```

## Binding-specific lifecycle

The generic bridge remains:

```text
admitted
→ external runtime start
→ consumed
```

The Hermes Runs candidate adds a narrower pre-launch boundary:

```text
admitted
→ launch_reserved
→ consumed

launch_reserved
→ launch_expired
```

`launch_reserved` is binding-specific operational governance state.

```text
launch_reserved
!= universal Execution Admission state
```

For this binding, runtime start must match the exact valid `launch_reservation_id`.

## Launch reservation

Clean external PR #79 implements one immutable reservation per Execution Admission.

Candidate identity includes:

```text
launch_reservation_id
admission_ref
snapshot_ref
snapshot_digest
field_projection_version
work_issue_version
launch_expires_at
idempotency_key
reserved_by
reserved_at
```

Reservation is allowed only while the admission is still `admitted` and consumable.

It closes the first-slice pre-launch revocation window before the native network call begins.

This avoids pretending that a human revocation and an already-started cross-system network submission can be atomically ordered.

### Lifetime

The candidate reservation expires no later than 120 seconds after reservation and never later than the parent admission expiry.

Expiry is projected lazily.

```text
no launch-expiry scheduler
no cleanup worker required to change governance meaning
launch_expired != renewed launch permission
```

An expired or ambiguous reservation is not automatically recycled.

## Launch Context Snapshot

Before the native Hermes call, the candidate freezes a bounded bootstrap snapshot from the exact admitted Context Pack.

External implementation contract:

```text
PostgreSQL isolation = REPEATABLE READ
field projection = scoped-context-v1
serialized ceiling = 120000 characters
source binary included = false
```

The snapshot contains only already-admitted bounded entity projections.

```text
Launch Context Snapshot
!= Evidence
!= global Agency Data
!= source-native binary
!= canonical memory
!= future owner state
```

After start, current owner values may be re-read only through Scoped Hermes Data Access for the same admitted identities.

```text
launch snapshot revision
!= later current owner revision
```

## Tool-surface qualification before launch

Clean observer PR #78 reads only:

```text
GET /v1/capabilities
GET /v1/toolsets
```

It verifies Runs API support and compares the concrete active Hermes tool surface with an explicit reviewed allowlist and required-tool set.

The launch binding requires:

```text
runs_api_status = compatible
safety_status = qualified
```

Otherwise no launch reservation and no native run submission occur.

```text
reachable != healthy
healthy != safe
Runs API available != run authorized
toolset configured != toolset approved
read-only prompt != dangerous tool removed
```

The general Hermes API-server profile is not automatically qualified.

## External native run submission

The executable binding is outside Pantheon in `pantheon-mvp` PR #79.

After successful qualification and reservation it performs exactly one:

```text
POST /v1/runs
```

The candidate request provides:

```text
input        = bounded immutable launch material
session_id   = exact Pantheon admission_id
instructions = fixed read-only governance constraints
```

It does not provide a model or provider override.

```text
Pantheon selects no provider/model
external binding selects no provider/model
Hermes retains provider/model routing
```

`session_id` is correlation only.

```text
session_id correlation != memory promotion
```

## Distributed ambiguity and retry refusal

Pantheon and Hermes do not share one atomic transaction.

If `POST /v1/runs` has an uncertain network outcome after reservation:

```text
no automatic second POST
no reservation recycling
explicit reconciliation required
```

If Hermes returns a `run_id` but the Pantheon start registration fails:

```text
preserve run_id
preserve launch_reservation_id
explicit reconciliation required
no second run submitted automatically
```

These are operational error states, not queue entries.

```text
submission_unknown != retry instruction
registration_unknown != queue item
```

## Active context after runtime start

Once the exact Hermes run is recorded as `running`, the candidate exposes admission-session reads over the existing scoped reader.

Conceptual surfaces:

```text
active context manifest
active context exact entity read
```

Pantheon resolves the single running Hermes run associated with the admission server-side.

The caller/model does not supply a `run_id`.

The read still inherits the full Scoped Hermes Data Access boundary:

```text
exact admitted identity only
scoped-context-v1 allowlisted fields
current_owner_read semantics
no global Agency Data list/search
no source binary dereference
no write
access ends when the run is no longer running
```

## Candidate native Hermes context plugin

Clean PR #79 includes the external candidate plugin named `pantheon-context-bridge` in the sibling executable repository.

It registers only:

```text
pantheon_context_manifest
pantheon_context_entity
```

The model-facing tool schemas do not expose:

```text
admission_id
run_id
Pantheon URL
credential
arbitrary query
```

The model may request an exact entity already present in its admitted manifest. It cannot choose another admission or run through tool arguments.

The plugin derives the admission identity from host-provided Hermes task/session context and fails closed if the host identity is absent or is not shaped as a Pantheon admission identity.

### Live identity proof still open

The binding submits:

```text
Hermes session_id = Pantheon admission_id
```

The plugin receives host `task_id` context.

The exact live equality:

```text
handler task_id == submitted Runs API session_id
```

remains to verify against a real Hermes v0.19 target.

Therefore:

```text
plugin code                 implemented candidate
session identity binding    to verify live
plugin installation         not performed
plugin enablement           not performed
plugin activation           not authorized
```

This uncertainty does not widen scope because the candidate fails closed when the identity is not as expected.

## One-shot reconciliation

The external adapter may explicitly inspect one known run once.

Current mapping:

```text
completed -> Result Candidate path
failed    -> failed return
running   -> observation only
pending   -> observation only
stopping  -> observation only
cancelled -> observation only; no invented mapping
```

It is not a poll loop, scheduler or monitor.

```text
Hermes completed != Evidence
Hermes completed != Knowledge
Hermes completed != Decision
Hermes completed != Work Issue resolved automatically
```

## Transaction-boundary hardening

The first implementation CI exposed an older handoff transaction defect: owner/case resolution occurred before the explicit handoff transaction, which could leave an implicit outer transaction and prevent a genuine `REPEATABLE READ` launch snapshot.

The clean candidate keeps the correction:

```text
owner/case resolution
inside explicit handoff transaction
→ top-level handoff returns connection to IDLE
→ launch snapshot may establish real REPEATABLE READ
```

The fix is covered by a regression test.

```text
CI found transaction defect
→ cause corrected
→ clean acceptance suite green

CI green != adoption
```

## Responsibility allocation

### Pantheon governs

- Work Issue / Task Contract / Context Pack admission;
- whether one exact launch opportunity exists;
- reservation identity and bounded lifetime;
- launch snapshot provenance and digest;
- allowed identity perimeter and field projection contract;
- meaning of runtime start/return observations;
- consequential effect gates;
- Evidence, Knowledge, Decision and canonicalization boundaries.

Pantheon does not call Hermes `/v1/runs`.

### Hermes executes

- actual agent run;
- provider/model routing;
- runtime tool calls inside its configured tool surface;
- runtime session/run identity;
- runtime status and candidate output.

### External Hermes Run Binding executes

- read-only Hermes API/tool-surface observation;
- one launch reservation request;
- exactly one native Runs API submission;
- start registration;
- optional explicit one-shot reconciliation.

It owns no queue, scheduler, retry worker, provider router or approval engine.

### Cockpit / OpenWebUI exposes

- Work Issue and admitted scope;
- admission / reservation / run observation states;
- unqualified profile, launch expiry and ambiguous-submission warnings;
- returned candidate and review need.

Cockpit does not fabricate the runtime `run_id` and does not receive runtime service credentials through this contract.

### Human approves

- Work Issue where required;
- Execution Admission;
- separately gated consequential effects;
- later installation, enablement and activation of the Hermes plugin/profile if adopted.

### Forbidden

- Pantheon dispatching or running Hermes;
- PostgreSQL becoming a runtime queue;
- automatic launch retry after an ambiguous network outcome;
- model-selected admission or run identity;
- generic Hermes profile being treated as safe because it is healthy;
- source binary authority inferred from Context Pack inclusion;
- plugin installation implying approval or activation;
- runtime success being treated as Evidence or professional truth.

## Capability Slot

```text
abstract capability:
  execute one admitted read-only Hermes work item

candidate Hermes binding:
  Hermes Agent Runs API
  + external Run Binding
  + pantheon-context-bridge plugin

installation:
  plugin not installed
  live target not established

health:
  public API contract verified
  clean candidate acceptance tests green
  live target health not established

update:
  no update action authorized by this doctrine

activation:
  not authorized

Pantheon gates:
  Execution Admission before launch opportunity
  tool-surface qualification before native submission
  separate effect chokepoint for consequential effects
```

## Current implementation status

```text
clean observer PR #78                    implemented candidate / draft / CI green
clean launch junction PR #79             implemented candidate / draft / CI green
launch reservation persistence           implemented candidate externally
Launch Context Snapshot                  implemented candidate externally
launch_reserved / launch_expired state   implemented candidate externally
Hermes Runs HTTP client                  implemented candidate externally
external one-shot launch binding         implemented candidate externally
active-context server resolver           implemented candidate externally
native Hermes context plugin             implemented candidate externally
one-shot runtime reconciliation          implemented candidate externally
transaction-boundary regression fix      implemented candidate externally
live Hermes target                       not connected
plugin task_id/session_id equality       to verify live
plugin installation                      not performed
plugin enablement                        not performed
production activation                    not authorized
```

Historical PRs #71, #75 and #77 are retained only as superseded review history.

## Final rule

```text
Pantheon may govern and record one exact launch opportunity.
Pantheon may freeze and qualify the context boundary that opportunity carries.
Pantheon may record the real Hermes run identity returned by the external binding.

Pantheon must not perform the native Hermes run submission itself.
Pantheon must not convert launch uncertainty into a hidden retry queue.
Pantheon must not treat runtime success or output as Evidence or truth.

The external binding asks Hermes to run.
Hermes runs Hermes.
Pantheon governs what the opportunity, context, observations and later effects mean.
```
