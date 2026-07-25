# Cockpit V2 — optional Notion collaborative projection

Status: PostgreSQL Agency Data owner seam implemented / Notion selective sync policy contract implemented / live synchronization not implemented / production adoption not authorized.

## Decision

PostgreSQL is the default system of record for native Agency Data.

Notion is optional and may act as a collaborative human interface for fields explicitly declared visible and, when justified, editable.

```text
PostgreSQL = system of record
Notion = optional collaborative projection
Hermes = bounded Agency Data operations
Pantheon = consequential-effect governance
Cockpit = unified projection
```

Notion is not in the critical path for normal Cockpit/Hermes use.

## Pilot IFJA mapping

The existing workspace remains useful as an optional collaboration surface:

| Notion data source | Agency Data concept | Intended posture |
|---|---|---|
| `_Affaires` | Project / Affaire | selective projection; some fields may be editable |
| `_Personnes` | Person | selective projection; contact fields may be editable |
| `_Sociétés` | Organization | selective projection; bounded identity/contact edits |
| `_Intervenants` | ProjectParticipation / CompanyEngagement | selective projection; relation edits need stronger validation |
| `_Décisions` | agency decision/reference projection | separate from Pantheon governance Decision |

Workspace-specific IDs and credentials are not embedded in the browser contract.

## Two distinct flows

### PostgreSQL to Notion

```text
PostgreSQL revision N
      ↓
external sync adapter
      ↓
Notion collaborative projection
      ↓
projection records revision N
```

### Notion to PostgreSQL

Only declared editable fields may produce an inbound mutation candidate.

```text
human edits Notion field
      ↓
field policy lookup
      ↓
revision/base check
      ↓
validation
      ↓
Agency Data mutation candidate
      ↓
applicable gate / authorization
      ↓
server-side mutation against PostgreSQL
      ↓
PostgreSQL revision N+1
      ↓
projection refresh
```

The browser contract does not execute this flow.

## FieldSyncPolicy

`notion_agency_binding.js` models an explicit policy per field:

```text
entity_type
field
notion_visible
notion_editable
sync_direction
conflict_policy
validation_rule
sensitivity
```

Supported direction vocabulary:

```text
postgres_to_notion
bidirectional
```

A field marked `notion_editable=true` must be bidirectional.

Example candidate policies:

| Field | Visible in Notion | Editable in Notion | Direction | Conflict posture |
|---|---:|---:|---|---|
| `Project.phase` | yes | yes | bidirectional | human_review |
| `Project.status` | yes | yes | bidirectional | human_review |
| `Project.address` | yes | yes | bidirectional | human_review |
| `Project.description` | yes | yes | bidirectional | merge/review candidate |
| `Evidence.status` | optional | no | postgres_to_notion | postgres_authoritative |
| `PantheonDecision.status` | optional | no | postgres_to_notion | postgres_authoritative |
| `Capability.activation` | optional | no | postgres_to_notion | postgres_authoritative |

Actual IFJA policies still require explicit review before live synchronization is enabled.

## Revision discipline

Every synchronized Agency Data record needs a stable internal identity and revision.

Recommended synchronization metadata:

```text
entity_id
postgres_revision
notion_revision or projected revision marker
notion_last_edited_time
last_synced_at
sync_status
mutation_origin
```

A Notion edit must declare or resolve the PostgreSQL revision on which that projection was based.

Example:

```text
Notion base revision = 42
current PostgreSQL revision = 42
→ mutation candidate may be prepared

Notion base revision = 42
current PostgreSQL revision = 43
→ conflict
```

There is no generic last-write-wins policy for business-significant fields.

## Conflict states

The policy contract currently recognizes these conflict postures:

```text
human_review
merge_append
postgres_authoritative
```

And synchronization observations such as:

```text
synced
postgres_ahead
notion_ahead
conflict
notion_unavailable
sync_error
unknown
```

The frontend may display these observations but does not resolve or execute synchronization.

## Notion outage behavior

Notion unavailability must not stop the Agency Data system.

```text
PostgreSQL    available
Cockpit       available
Hermes        available through Agency Data capabilities
Notion UI     unavailable/degraded
sync          unavailable/degraded
```

PostgreSQL writes continue normally.

When Notion becomes available again, the external synchronization implementation must compare revisions before applying an inbound Notion change.

```text
Notion unavailable != PostgreSQL unavailable
Notion stale != PostgreSQL stale
Notion recovery != blind overwrite
```

## Hermes write posture

Hermes should target the Agency Data capability, not direct SQL generated ad hoc.

Candidate shape from `agency_data_binding.js`:

```text
operation: agency_record_mutation_candidate
owner_system: postgres
entity_type
entity_id
field
value
expected_revision
requested_by: hermes
effect
execution_authorized: false
```

A server-side Agency Data adapter may later execute an authorized mutation with optimistic revision checks.

```text
Hermes mutation candidate != authorized mutation
PostgreSQL write success != Evidence
```

## Protected fields

Notion must not become a general-purpose editing route for governance-sensitive records.

Examples that should remain read-only or absent from the Notion collaboration surface unless a separate reviewed design says otherwise:

```text
Evidence qualification/status
formal Pantheon governance Decisions
capability approval/activation
runtime safety qualification
Context scope authorization
Registre Probatoire state
policy/governance state
```

## Tags

The Tag Registry remains an Agency/Pantheon-owned structured vocabulary unless separately decided.

A Notion multi-select may project an existing tag or propose a candidate mapping, but arbitrary Notion text must not silently create canonical vocabulary.

## `_Décisions`

The existing Notion `_Décisions` database may remain useful as an agency collaboration surface, but:

```text
AgencyDecisionRecord
!=
PantheonGovernanceDecision
```

An agency/client choice may be synchronized as an Agency Data record and then related to a Pantheon Decision where useful. It does not authorize a Pantheon effect by itself.

## Runtime placement

The synchronization implementation belongs outside the Cockpit browser and outside Pantheon's governance core.

Pantheon may govern and display:

```text
binding adoption
field policies
scope
health observations
sync observations
conflicts
activation/suspension posture
consequential gates
```

The external integration/runtime performs provider I/O and synchronization.

## Current implementation status

```text
Context Resolver federation                         implemented
PostgreSQL Agency Data projection seam              implemented candidate
Agency Data mutation-intent contract                implemented candidate
Notion field-policy registry                        implemented candidate
Notion revision conflict classification             implemented candidate
Notion outage/sync-state projection                  implemented candidate
browser Notion credentials                          forbidden / absent
browser synchronization execution                    absent by design
live PostgreSQL Agency Data API transport            not connected by this slice
Hermes server-side PostgreSQL mutation adapter       not connected
live Notion sync adapter                             not implemented
IFJA field-policy adoption                           not decided
Notion _Décisions synchronization                    not implemented
production activation                               not authorized
```
