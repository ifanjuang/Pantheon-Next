# Pantheon consultation contract

Status: implemented read-only / partial / protected path — transport-neutral
response contract for the bounded `mcp-server/` consultation slice.

This contract lets MCP clients consume the current implementation and lets a
future bounded HTTP adapter project the same semantics without duplicating
Pantheon policy logic.

It does not implement an HTTP API, remote MCP transport, authentication
service, Hermes runtime inventory, evidence store, document retrieval engine, Mem0 or
Memvid connector, approval engine or write path.

## Boundary

```text
repository sources or caller-provided status candidate
  -> transport-neutral consultation function
  -> MCP response today
  -> possible bounded HTTP projection later
```

The consultation functions may:

- list honest surface availability;
- explain allowlisted architecture placement and rationale;
- cite governed repository sources with authority and status;
- qualify a caller-provided operational-status candidate;
- report missing evidence, freshness, scope or status fields.

They must not:

- probe Hermes or another runtime;
- claim to discover installed modules;
- retrieve project documents, private knowledge or memory;
- authorize activation, installation, update or execution;
- approve evidence or write the Registre Probatoire;
- infer a missing status from another status.

## Common response envelope

Every consultation response carries:

```text
contract          pantheon.consultation.v1
repository_version declared VERSION of the consulted checkout
object            response-object type
source_mode       where the response material came from
authority_effect  none
write_effect      false
result            operation-specific result
```

Source-backed responses also carry source references containing, where
available:

```text
uri
title
source_file
exists
authority
status
declared_status
content_sha256
```

The response is a projection. The cited source retains its declared authority
and status.

## Implemented read-only functions

### Consultation catalog

`get_consultation_catalog()` distinguishes:

```text
implemented_read_only
implemented_read_only_partial
implemented_external_read_only_partial
documented_non_implemented
```

The installable external Hermes dashboard plugin is the partial producer of
live runtime observations. Runtime inventory remains non-implemented in the
MCP itself. Evidence-instance queries, knowledge retrieval, Mem0/Memvid
retrieval, scoped permission enforcement, HTTP API and remote MCP transport
also remain non-implemented in the MCP.

### Architecture explanation

`explain_architecture(topic)` supports an allowlist of architecture concepts:

```text
pantheon
hermes
openwebui
pantheon-control
mcp
api
capabilities
knowledge
memory
evidence
```

Each result contains placement, purpose, rationale, forbidden responsibilities
and governed source references. Aliases such as `dashboard`, `mem0` and
`memvid` resolve to the relevant topic. Unknown input returns
`unknown_topic`; it never becomes a repository path.

### Capability-status qualification

`get_capability_status(status_yaml)` retains the requested client-facing name,
but its source mode is always `provided_status_candidate`. It performs no
runtime lookup.

The provided YAML mirrors the nine dashboard axes and may carry lifecycle
extensions:

```yaml
capability_id: document-retrieval
producer: hermes_dashboard
listed: true
detected: true
installed: true
configured: true
enabled: true
reachable: true
health: healthy
governance_status: approved_for_project
task_use_status: eligible_under_reviewed_contract
update_status: up_to_date
rollback_status: tested
observed_at: "2026-07-15T21:00:00+02:00"
scope:
  scope_type: project
  scope_id: example-project
evidence_refs:
  - evidence-pack.example
```

`listed`, `detected`, `installed`, `configured`, `enabled` and `reachable` are
independent boolean-or-null observations. `health`, `governance_status`,
`task_use_status`, `update_status` and `rollback_status` use bounded
vocabularies. Missing fields remain capability gaps. Unsupported values and
impossible combinations such as `detected: false` with `installed: true` fail
closed as `result: invalid`.

The dashboard's descriptive `policy.governance` label is not proof of a
Pantheon approval and must not be copied into `governance_status` without a
separately governed decision source.

Even a complete candidate returns:

```text
authorization_effect: none
runtime_probe_performed: false
use_posture: requires_task_preflight_and_any_applicable_human_decision
```

## Non-equivalence rules

```text
listed != installed
detected != configured
configured != enabled
enabled != reachable
reachable != healthy
installed != approved
hermes_enabled != pantheon_governance_activation
healthy != safe
governance_eligible != task_authorized
update_available != update_authorized
runtime_success != evidence
binding_selected != dependency_adopted
retrieved != evidence
```

## Future transport projection

A future API adapter may map the contract approximately as follows:

| Transport-neutral function | Possible HTTP projection | Current status |
|---|---|---|
| `consultation_catalog()` | `GET /v1/consultation` | documented non-implemented |
| `explain_architecture(topic)` | `GET /v1/architecture/{topic}` | documented non-implemented |
| `qualify_capability_status(candidate)` | `POST /v1/capability-status:qualify` | documented non-implemented |

The table reserves no endpoint and creates no service. Authentication,
authorization, rate limits, tenant/project isolation and deployment require a
separate reviewed adapter before any HTTP surface exists.

## Final rule

```text
The core defines one consultation meaning.
MCP projects it today.
An API may project it later.
Neither transport becomes authority or runtime.
```
