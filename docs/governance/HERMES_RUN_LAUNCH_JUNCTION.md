# Hermes Run Launch Junction

Status: candidate support doctrine — external MVP implementation candidate / live Hermes v0.19 binding not verified / activation not authorized.

Date: 2026-07-25

This document specializes `HERMES_EXECUTION_ADMISSION_BRIDGE.md` for one candidate binding to the public Hermes Agent Runs API.

It does not replace the generic Execution Admission model and does not make `launch_reserved` mandatory for every future runtime binding.

It does not create a Pantheon runtime, dispatcher, scheduler, queue, retry worker, provider router, MCP host, plugin manager, memory engine or automatic approval system.

```text
Pantheon governs the exact launch opportunity and meaning of observations.
An external Hermes Run Binding performs the native Hermes API call.
Hermes starts and executes its own run.
The human decides admission and separately required consequential effects.
```

## Why a launch junction is needed

The generic bridge deliberately left delivery of `admission_id` and actual runtime start outside Pantheon.

Hermes Agent v0.19 exposes a public Runs API, but the existence of `POST /v1/runs` does not authorize Pantheon to become a dispatcher.

The candidate junction therefore separates four acts:

```text
1. Pantheon records one Execution Admission.
2. An external binding reserves that exact admitted launch opportunity.
3. The external binding asks Hermes to create one run.
4. Pantheon records the run identity Hermes returned.
```

Critical distinctions:

```text
admission != dispatch
launch reservation != dispatch
launch reservation != Hermes run
POST /v1/runs != Pantheon execution
runtime start receipt != Evidence
runtime success != Evidence
```

## Relationship to the generic admission bridge

The generic bridge remains valid for runtime bindings that may be reviewed later:

```text
admitted
→ external runtime start
→ consumed
```

For the Hermes Runs API candidate described here, a narrower sub-lifecycle is inserted before the network call:

```text
admitted
→ launch_reserved
→ consumed

launch_reserved
→ launch_expired
```

This specialization changes the runtime-start precondition for this binding only:

```text
generic bridge:
  start may consume an exact admitted opportunity

Hermes Runs junction:
  start must match the exact launch_reservation_id
  while that reservation is valid
```

Therefore:

```text
launch_reserved = binding-specific operational governance state
!= universal Execution Admission state required for every runtime
```

## Launch reservation

The external implementation candidate in `ifanjuang/pantheon-mvp` PR #75 introduces one immutable reservation per Execution Admission.

Candidate shape:

```yaml
hermes_run_launch_reservation:
  launch_reservation_id:
  admission_ref:
  snapshot_ref:
  snapshot_digest:
  field_projection_version:
  work_issue_version:
  launch_expires_at:
  idempotency_key:
  reserved_by:
  reserved_at:
```

The reservation is created only while the admission is still `admitted` and consumable.

It consumes the pre-launch revocation window before the external network call begins.

```text
admitted + valid reservation request
→ launch_reserved
→ human pre-consumption revocation no longer available in this first slice
```

This prevents an ambiguous race:

```text
human revokes admission
at the same time
external binding is already submitting the admitted run to Hermes
```

The first slice chooses explicit reconciliation over pretending that a network call can be atomically revoked across systems.

### Bounded lifetime

The candidate launch reservation expires no later than 120 seconds after reservation and never later than the parent admission expiry.

Expiry is projected lazily.

```text
no launch-expiry scheduler
no cleanup worker required to change governance meaning
```

An expired reservation does not silently revert to `admitted` and is not automatically recycled.

```text
launch_expired != new launch permission
```

## Launch Context Snapshot

Before the external network call, the candidate freezes a bounded bootstrap snapshot from the exact admitted Context Pack.

The external MVP uses:

```text
PostgreSQL transaction isolation = REPEATABLE READ
field_projection_version = scoped-context-v1
serialized snapshot ceiling = 120000 characters
```

The snapshot may include only entity projections already admitted by the Context Pack and already exposed by the bounded field projection.

It does not contain source binaries.

```text
Launch Context Snapshot
!= Evidence
!= global Agency Data
!= source-native binary
!= canonical memory
!= future owner state
```

The snapshot answers:

> What bounded owner material was observed for bootstrapping this exact admitted launch?

It does not claim that owner records cannot change after launch.

After the run starts, the separate Scoped Hermes Data Access capability may re-read current owner values for the same admitted identities.

```text
launch snapshot revision
!= later current owner revision
```

## External Hermes Run Binding

The executable candidate lives outside Pantheon in the sibling `pantheon-mvp` repository.

Candidate sequence:

```text
read-only Hermes capability/toolset observation
        ↓
runs_api_status = compatible
AND safety_status = qualified
        ↓
reserve exact launch in Pantheon
        ↓
POST Hermes /v1/runs exactly once
        ↓
Hermes returns run_id
        ↓
report exact run_id + launch_reservation_id to Pantheon
```

The binding is an execution adapter, not a Pantheon component.

It owns no:

```text
queue
scheduler
retry worker
provider router
model selector
background monitor
approval engine
```

### Provider and model routing

The candidate request deliberately does not specify a model or provider override.

```text
Pantheon selects no provider/model
external binding selects no provider/model
Hermes retains provider/model routing inside its runtime
```

### Session correlation

The candidate submits:

```text
Hermes session_id = Pantheon admission_id
```

This is a correlation key for the exact run boundary.

```text
session_id correlation != memory promotion
session_id correlation != Pantheon memory ownership
```

Hermes may retain runtime/session behavior according to its own configured runtime. Pantheon does not become that memory engine.

## Ambiguous launch outcome

A distributed network call cannot provide an atomic transaction spanning Pantheon and Hermes.

The candidate therefore fails conservatively.

### Submission outcome unknown

If the launch reservation exists but `POST /v1/runs` has an uncertain network outcome:

```text
no automatic second POST
no reservation recycling
operator reconciliation required
```

### Hermes run_id returned but Pantheon callback failed

If Hermes returns a `run_id` and the Pantheon start callback fails, the adapter retains:

```text
run_id
launch_reservation_id
```

for explicit reconciliation.

These are operational error conditions, not a hidden Pantheon retry state machine.

```text
submission_unknown != retry instruction
registration_unknown != queue item
```

## Runtime-facing active context

Once the exact external run is recorded as `running`, the candidate provides a session-oriented read seam over the already implemented run-scoped reader.

Candidate routes:

```text
GET /v1/hermes/execution-admissions/{admission_id}/active-context
GET /v1/hermes/execution-admissions/{admission_id}/active-context/entities/{entity_type}/{entity_id}
```

Pantheon resolves the single `running` HermesRun associated with that admission server-side.

The caller does not supply a `run_id`.

```text
caller-selected admission + caller-selected run
!= active-context contract
```

The resulting read still inherits all Scoped Hermes Data Access constraints:

```text
exact admitted identity only
scoped-context-v1 field allowlist
current_owner_read semantics
no global Agency Data list/search
no source binary dereference
no write
access ends when run is no longer running
```

## Candidate native Hermes context plugin

`pantheon-mvp` PR #75 includes the external candidate plugin named `pantheon-context-bridge` in the sibling executable repository.

It registers only:

```text
pantheon_context_manifest
pantheon_context_entity
```

The model-facing tool schemas do not contain:

```text
admission_id
run_id
Pantheon URL
credential
arbitrary query
```

The model may select an `entity_type` and exact stable `entity_id` already presented in its admitted manifest. It cannot choose another admission or run through tool arguments.

The plugin derives the admission identity from host-provided Hermes task/session context and refuses a host identity that is not shaped as `admission-*`.

It then uses the active-context routes above.

### Live identity binding still to verify

Current Hermes plugin documentation exposes host `task_id` to tool handlers. The candidate Runs API launch sends `session_id = admission_id`.

The exact runtime equality:

```text
handler task_id == submitted Runs API session_id
```

has not yet been exercised against a live Hermes v0.19 target by this repository.

Therefore:

```text
plugin code implemented candidate
host session identity binding to verify live
plugin installation not performed
plugin enablement not performed
plugin activation not authorized
```

The candidate fails closed if the expected host identity is absent or different.

## Tool-surface qualification

A working Runs API is not enough.

The external observer must inspect the actual Hermes API-server tool surface before the launch reservation is created.

```text
Runs API reachable
!= compatible
!= safe for this admission
```

The candidate requires:

```text
runs_api_status = compatible
safety_status = qualified
```

where `qualified` means the concrete enabled/configured tool surface fits an explicit reviewed allowlist and required-tool set.

A prompt or run instruction saying `read only` is not a tool-authority boundary.

```text
read-only instruction != dangerous tool removed
plugin installed != profile safe
healthy != safe
```

The general Hermes API-server profile is therefore not automatically adopted for Pantheon work merely because the Pantheon context plugin is installed.

## One-shot runtime reconciliation

The candidate adapter can explicitly observe one run once:

```text
GET /v1/runs/{run_id}
```

This is not a poll loop or scheduler.

Current candidate mapping:

```text
completed -> normalized result_candidate + optional HermesResultCandidate
failed    -> normalized failed return
running   -> observation only
pending   -> observation only
stopping  -> observation only
cancelled -> observation only / no invented return mapping
```

A completed result remains candidate material.

```text
Hermes completed != Evidence
Hermes completed != Knowledge
Hermes completed != Decision
Hermes completed != Work Issue resolved automatically
```

## Transaction boundary discovered by the junction

The external acceptance suite exposed an older transaction-boundary defect in the handoff implementation: Project/case resolution occurred before the explicit handoff transaction, opening an implicit PostgreSQL transaction and turning subsequent transaction contexts into savepoints.

The external PR #75 candidate moves that owner read inside the explicit handoff transaction and adds a non-regression check that a top-level handoff returns the connection to an idle transaction state.

This matters because the launch snapshot must be able to establish a real `REPEATABLE READ` boundary rather than silently inheriting an unrelated outer transaction.

```text
CI failure found a transaction defect
→ defect corrected
→ acceptance suite green

CI green != adoption
```

## Responsibility allocation

### Pantheon governs

- exact Work Issue / Task Contract / Context Pack admission;
- whether one launch opportunity exists;
- reservation identity and bounded lifetime;
- launch snapshot provenance and digest;
- allowed identity perimeter and field projection contract;
- meaning of runtime start/return observations;
- consequential effect policy gates;
- Evidence, Knowledge, Decision and canonicalization boundaries.

Pantheon does not call Hermes `/v1/runs`.

### Hermes executes

- actual agent runtime start and execution;
- provider/model routing;
- runtime tool invocation inside its configured surface;
- runtime session/run identity;
- runtime status and output;
- runtime scheduling/retries only if independently configured and within admitted authority.

### External Hermes Run Binding executes

- read-only capability/toolset observation;
- one launch reservation request;
- exactly one native Runs API submission;
- start callback registration;
- optional explicit one-shot status reconciliation.

It is not Pantheon and is not a queue/scheduler.

### Cockpit / OpenWebUI exposes

- Work Issue and admitted scope;
- admission / reservation / run observation states;
- warnings such as `launch_expired`, ambiguous submission or unqualified Hermes profile;
- returned candidate and review need.

Cockpit does not receive service credentials through this candidate and does not fabricate the runtime `run_id`.

### Human approves

In this candidate posture:

- durable Work Issue where required;
- Execution Admission;
- consequential effect decisions required by the effect chokepoint;
- separately, installation/enablement/activation of the Hermes plugin/profile if later adopted.

### Forbidden

- Pantheon dispatching or running Hermes;
- PostgreSQL becoming a runtime queue;
- automatic launch retry after an ambiguous network outcome;
- model-selected admission or run identity;
- generic Hermes profile being treated as safe because it is healthy;
- source binary access inferred from the Context Pack;
- plugin installation implying approval or activation;
- runtime success being treated as Evidence, Knowledge, Decision or professional truth.

## Capability Slot classification

```text
abstract capability:
  execute one admitted read-only Hermes work item

candidate Hermes binding:
  Hermes Agent v0.19 Runs API
  + external Run Binding
  + pantheon-context-bridge plugin

installation status:
  plugin not installed by this repository
  live target not established

health:
  public API contract verified
  mock/acceptance tests green
  live target health not established

update:
  no update action authorized by this document

activation:
  not authorized

Pantheon gates:
  Execution Admission before launch opportunity
  tool-surface qualification before candidate submission
  separate effect chokepoint for every consequential effect
```

## External implementation status

As of this candidate documentation slice:

```text
launch reservation persistence          implemented candidate externally (#75)
Launch Context Snapshot                 implemented candidate externally (#75)
launch_reserved / launch_expired state  implemented candidate externally (#75)
Hermes v0.19 Runs HTTP client           implemented candidate externally (#75)
external one-shot launch binding        implemented candidate externally (#75)
active-context server resolver          implemented candidate externally (#75)
native Hermes context plugin            implemented candidate externally (#75)
one-shot runtime reconciliation         implemented candidate externally (#75)
transaction-boundary regression fix     implemented candidate externally (#75)
external candidate CI                   green after correction
live Hermes target                      not connected / to verify
plugin task_id/session_id equality       to verify live
plugin installation                     not performed
plugin enablement                       not performed
production activation                   not authorized
```

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
