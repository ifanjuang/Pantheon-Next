# Cockpit V2 — structured agency interface foundation

Status: executable candidate — partial / current branch CI validation pending / not production-authorized.

This document records the implementation state of the Cockpit V2 branch in `pantheon-mvp`.

Pantheon Next remains authoritative for governance doctrine. This file does not promote candidate behavior into canonical doctrine.

## Product direction

```text
PostgreSQL Agency Data = default system of record for native agency records
Cockpit                = projection / interaction surface
Hermes                  = external execution runtime
Pantheon                = governance of consequential effects and status
Notion                  = optional collaborative projection
Human                   = decision authority where required
```

The Cockpit is a user-friendly interface over structured professional records shared between agency work and AI-assisted work.

```text
Card != source of truth
PostgreSQL system of record != Pantheon governance authority
Hermes runtime success != Evidence
```

## Current implementation map

```text
Agency Data PostgreSQL                    implemented candidate / CI to verify
Agency Data bounded HTTP API              implemented candidate / CI to verify
Cockpit V2 spatial route                  implemented candidate / CI to verify
Universal Card projections                implemented candidate / CI to verify
Live Context Resolver                     implemented candidate / CI to verify
Project → Intervenants hierarchy          implemented candidate / CI to verify
Hermes handoff preview                    implemented candidate / CI to verify
Human Work Issue submission               implemented candidate / CI to verify
Read-only execution admission             implemented candidate / CI to verify
Hermes envelope lookup by admission_id    implemented candidate / CI to verify
Hermes runtime-start callback record      implemented candidate / CI to verify
Hermes normalized return callback         implemented candidate / CI to verify
Live Hermes transport / dispatcher        not implemented
Admission expiry / revocation / retry     not implemented
Notion live synchronization               not implemented
Production activation                     not authorized
```

## Agency Data PostgreSQL

Server-side implementation:

```text
mvp_vertical/sql/002_agency_data.sql
mvp_vertical/agency_data.py
mvp_vertical/agency_directory.py
mvp_vertical/agency_data_api.py
```

Current record families:

```text
agency_projects
agency_people
agency_organizations
agency_project_participations
agency_project_events
```

`agency_project_events` is append-only.

Project mutations use explicit actor identity, optimistic revision checks, idempotency keys, a bounded field allowlist and append-only material events. There is no generic SQL endpoint.

### Read API

```text
GET /v1/agency/projects
GET /v1/agency/projects/{project_id}
GET /v1/agency/projects/{project_id}/participations
GET /v1/agency/participations
GET /v1/agency/people
GET /v1/agency/people/{person_id}
GET /v1/agency/organizations
GET /v1/agency/organizations/{organization_id}
```

### Project write API

```text
POST  /v1/agency/projects
PATCH /v1/agency/projects/{project_id}
```

People, Organization and ProjectParticipation writes are not implemented yet.

### Hermes write ceiling

A Hermes credential identifies the executor. It is not approval.

Current direct Hermes Project write ceiling:

```text
admitted reversible field:
  description

blocked pending a verifiable consequential gate:
  project creation
  code
  display_name
  status
  phase
  location
  primary_client
  tags
```

Blocked fields raise `GovernanceGateRequired` rather than being silently persisted.

```text
Hermes credential != approval
bounded write capability != unrestricted mutation authority
mutation persisted != professional validation
```

## Live Context Resolver

Implementation:

```text
mvp_vertical/cockpit/context_resolver.js
mvp_vertical/cockpit/agency_data_binding.js
mvp_vertical/cockpit/v2_context.js
```

Namespaces:

```text
_  Affaires / Projects
#  capabilities when a provider is registered
@  People
*  permitted global providers
```

Current Agency Data provider coverage:

```text
_  Projects
@  People
*  Projects + People + Organizations + ProjectParticipations
```

Behavior includes accent/case normalization, project-code identity aliasing, multiple providers per namespace, provider-failure isolation, stable identity deduplication, match explanations, debounce, stale-response protection and explicit selection only.

```text
search result != selected context
selected context != relied-upon evidence
selected context != Evidence
scope_widened_implicitly = false
```

## Spatial V2 route

Route:

```text
mvp_vertical/cockpit/index.html
```

Primary spaces:

```text
Pantheon ↔ Décisions ↔ Affaires ↔ Connaissances ↔ Outils
```

Navigation grammar:

```text
root horizontal        = primary spaces
horizontal at depth    = siblings in current collection
↑                      = descend into declared children
↓                      = return to parent
recto / verso          = same object identity
```

The implementation includes keyboard/pointer controls, breadcrumb, reduced-motion handling and Universal Card family skins.

### Affaires hierarchy

```text
Affaires
  ↓
Project
  ↓
Intervenants ↔ Documents ...
  ↓
ProjectParticipation
```

A ProjectParticipation retains separate Person, Organization, role, type and revision identity.

Documents, Knowledge and Work Issues remain owned by their established persistence/API surfaces rather than being copied into Agency Data.

## Card Context and Hermes dock

Current files:

```text
mvp_vertical/card_scope.py
mvp_vertical/hermes_handoff_preview.py
mvp_vertical/hermes_handoff_store.py
mvp_vertical/hermes_handoff_api.py
mvp_vertical/cockpit/v2_handoff.js
mvp_vertical/cockpit/styles/v2_handoff.css
```

The dock presents three separate human-visible steps:

```text
1 Préparer
2 Créer le Work Issue
3 Admettre pour Hermes
```

None of these steps starts Hermes from the Cockpit.

### Step 1 — prepare

```text
POST /v1/cockpit/hermes-handoffs/preview
```

Produces deterministic `Task Contract Candidate` and `Context Pack Candidate` snapshots.

Current Card Context:

```text
current Card
+ declared descendants only when explicitly selected
+ explicit Context Resolver additions
- explicit exclusions
```

Declared descendants are resolved server-side. DOM nesting is not a scope boundary.

For a Project the current policy may include ProjectParticipations, Documents directly owned by the Project and Document source refs. It does not silently include all Knowledge, other Projects or the whole database.

The preview exposes:

```text
execution_authorized = false
requested_effect = read_only
```

### Step 2 — create Work Issue

```text
POST /v1/cockpit/hermes-handoffs/submit
```

Requires editor credential, `X-Pantheon-Human-Actor`, exact preview/Task Contract/Context Pack identity and idempotency.

The server recalculates the preview before persistence. A stale preview returns HTTP 409.

A valid submission persists:

```text
cockpit_hermes_handoffs immutable snapshot
+
Work Issue assigned_to=hermes
```

It does not create a Hermes run.

```text
Work Issue assigned_to=hermes != Hermes run
submission != execution
candidate contract snapshot != canonical governance admission
```

## Execution Admission bridge

Current implementation:

```text
mvp_vertical/sql/004_hermes_execution_admissions.sql
mvp_vertical/hermes_execution.py
mvp_vertical/hermes_execution_api.py
mvp_vertical/hermes_runtime_return.py
```

Doctrine counterpart:

```text
Pantheon-Next/docs/governance/HERMES_EXECUTION_ADMISSION_BRIDGE.md
```

### Step 3 — human execution admission

```text
POST /v1/cockpit/hermes-handoffs/{handoff_id}/admissions
```

The first slice is deliberately conservative:

```text
requested_effect = read_only
human admission required
one handoff
one Work Issue
one admission
one consuming Hermes run
```

Admission verifies that the Work Issue is still open, assigned to Hermes, bound to the same Task Contract and Context Pack and unused by a Hermes run.

The immutable record is stored in `hermes_execution_admissions`.

```text
ready_for_external_runtime = eligibility
ready_for_external_runtime != dispatch
admission != Hermes run
```

## External Hermes runtime boundary

The Cockpit never calls runtime-start or runtime-return routes.

Only an external Hermes adapter with the Hermes credential may access the runtime-facing surface.

### Exact envelope lookup

```text
GET /v1/hermes/execution-admissions/{admission_id}
```

There is deliberately no pending-work collection, `claim-next-job`, lease, scheduler or retry-worker endpoint.

### Runtime start callback

After Hermes has started itself externally:

```text
POST /v1/hermes/execution-admissions/{admission_id}/runs/start
```

The external adapter supplies the real `run_id`. Pantheon validates and records the observation.

```text
runtime-start callback != command to start
runtime started != task succeeded
runtime started != Evidence
```

### Runtime return callback

After execution:

```text
POST /v1/hermes/execution-admissions/{admission_id}/runs/{run_id}/return
```

Normalized outcomes:

```text
result_candidate
partial
failed
capability_gap
```

A return requires `outcome`, `summary` and `trace_refs`; optional fields can carry source refs, Evidence candidates, limitations and open questions.

Current issue projection:

```text
result_candidate -> review
partial          -> waiting
failed           -> waiting
capability_gap   -> waiting
```

The callback explicitly returns:

```text
result_status = candidate
evidence_admitted = false
```

A runtime return never closes the Work Issue automatically.

```text
Hermes returned != issue resolved
runtime return != Evidence admitted
result candidate != canonical truth
runtime success != governance success
```

## What is not implemented

### Live Hermes transport

No verified live Hermes client/endpoint exists in this repo.

The implementation therefore stops at the runtime-facing contract:

```text
human creates admission
        ↓
admission_id exists
        ↓
external integration delivers admission_id to Hermes
        ↓
Hermes fetches exact envelope
        ↓
Hermes starts itself
```

The delivery/binding step is not implemented here. Pantheon does not invent it and does not become a dispatcher to compensate.

### Admission lifecycle gaps

Before production runtime activation, explicit design is still required for:

```text
expiry
revocation before consumption
stale-admission invalidation
failed-start retry
partial continuation
new execution after failed/returned run
single-use versus bounded multi-use
```

Current posture:

```text
one admission = one execution opportunity
```

### Consequential effects

The execution admission currently covers `read_only` work only. It is not authority for Agency Data consequential mutation, external communication, repository mutation, document transmission, memory/Evidence promotion, installation or capability activation.

Those effects retain their own Pantheon gate requirements.

## Notion collaboration

`mvp_vertical/cockpit/notion_agency_binding.js` remains an optional collaboration contract over PostgreSQL-owned Agency Data.

```text
Notion projection != system of record
Notion editable != unrestricted write authority
sync success != Evidence
Notion permission != Hermes execution admission
```

The live synchronization adapter remains unimplemented.

## Responsibility allocation

### Pantheon governs

- scope and effect ceiling;
- exact candidate contract/context binding;
- human execution admission;
- validation of runtime callbacks;
- observed run state;
- downstream Evidence/approval boundaries.

### Hermes executes

- actual runtime start;
- tools/subagents/workers;
- provider/model choice;
- runtime scheduling/retries within admitted authority;
- real run IDs;
- execution traces.

### Cockpit exposes

- current Card scope;
- selected Context;
- Task Contract / Context Pack preview;
- Work Issue creation;
- execution admission receipt;
- returned candidate status.

### Human approves

Current conservative first slice:

- durable Work Issue creation;
- execution admission.

### Forbidden

- Pantheon as runtime;
- Pantheon/PostgreSQL as execution queue or scheduler;
- Cockpit calling runtime-start/runtime-return callbacks;
- Pantheon provider routing;
- automatic downstream consequential authority;
- runtime success treated as Evidence.

## Next slices

```text
1 validate current head CI and PostgreSQL acceptance tests
2 design admission expiry / revocation / stale invalidation
3 define a real external Hermes delivery binding only after observing its actual API/runtime surface
4 add bounded Person / Organization / Participation mutation policies
5 add verifiable gate receipts for consequential Agency Data mutations
6 add Tag Registry owner API + picker
7 implement optional Notion synchronization for declared FieldSyncPolicy
8 expand Document revision/representation/issues Cards
9 expose live Capability / RuntimeHost / model observations under Outils
```

## Final boundaries

```text
card != source of truth
search result != selected context
selected context != Evidence
Work Issue != authorization
execution admission != dispatch
admission != Hermes run
runtime-start callback != start command
Hermes returned != issue resolved
runtime return != Evidence admitted
PostgreSQL system of record != Pantheon governance authority
Notion projection != system of record
```

The cockpit is now served from the single page `mvp_vertical/cockpit/index.html` (the separate `v2.html` was removed during consolidation). It and the execution-admission bridge remain candidate implementation until reviewed, CI-validated and explicitly adopted for production.