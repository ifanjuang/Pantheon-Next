# directory-mcp Reference Review

Status: support review only — local MCP entity/identity directory, Hermès identity-resolution candidate boundary, and forbidden-import record.

Observed date: 2026-06-07

Reviewed sources:

- `https://github.com/ePaint/directory-mcp`.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Review scope

This review evaluates directory-mcp, a local MCP server that maintains a graph-based knowledge base resolving fuzzy references (for example "my boss", "the client", "the MOA") to concrete identities and their external coordinates.

This document does not approve installation.

This document does not add a dependency.

This document does not create a Pantheon runtime, MCP server, MCP host, memory engine, entity registry runtime, connector, scheduler, queue, approval engine or automatic memory promotion engine.

## External project summary

directory-mcp uses a flexible graph schema instead of rigid tables. Five object types:

```text
Entities       people / projects / teams / orgs (open "kind" field)
Anchors        external coordinates (system + reference type + value)
Edges          relationships (reports_to, member_of, ...)
Observations   sourced facts, with optional structured keys
Interactions   append-only usage log, used to rank ambiguous matches
```

Read tools resolve and find (`whois`, `who_to_query`, `find`, `vocab`); write tools record and relate (`remember_person`, `relate`, `link`, `note`, `merge`, ...). Local SQLite, stdio to a single local agent, single-user, MIT, young (v0.2.0, 2026).

Pantheon interpretation:

```text
directory-mcp is useful because its graph models who said what, sourced, which the evidence layer needs.
directory-mcp is risky because it is a write-capable memory runtime that "remembers" by itself.
```

## Technical characterization

directory-mcp should be classified as:

```text
local_entity_identity_directory
graph_knowledge_base
mcp_tool_server
write_capable_runtime_memory
external_runtime_candidate
```

It is not:

```text
Pantheon governance
the Registre Probatoire
Pantheon approval
Pantheon runtime
Registre Probatoire entry
proof by itself
```

A directory-mcp Observation is a sourced Evidence Candidate.

A `whois` resolution is an attribution aid.

A `remember_*` write is an operational note, not a governed record.

None of these objects is a Registre Probatoire entry, approval, proof by itself or doctrine.

## Layer mapping

| Layer | Classification |
|---|---|
| Pantheon Next | governance of evidence, attribution, scope, certainty and approval over entities |
| Hermes Agent | optional entity-resolution and identity-memory candidate under MCP capability passport |
| directory-mcp | external local MCP directory of entities, anchors, relations and sourced observations |
| OpenWebUI | cockpit exposure of resolved identities and sourced observations only |

## Recommended classification

```text
name: directory_mcp
classification: External Local MCP Entity/Identity Directory
pantheon_status: reference_review_only
hermes_status: optional_entity_resolution_candidate
openwebui_status: identity_and_observation_display_surface_candidate
memory_status: non_canonical
approval_status: not_approved_for_installation
runtime_status: external_only
```

## Valuable patterns to distill

The strongest takeaway is the schema, which models the actor side of the evidence record (the Registre Probatoire direction):

```text
graph schema (Entities / Anchors / Edges / Observations / Interactions) over rigid tables
Observations as SOURCED facts — the evidence-with-citation posture
Anchors that separate an identity from its channels (email, Slack, Jira)
an append-only interaction log used to RANK ambiguous matches, never to decide
whois-style entity resolution to attribute a piece of evidence to a real actor
```

These feed the Registre Probatoire's actor fields (`author_detected`, `interlocutors_detected`, `organization_detected`, `origin_channel`) with a concrete, flexible shape.

## Relationship to the memory decision

A people/projects directory is operational recall. It belongs to Hermès' own runtime memory (free, self-evolving), not to Pantheon. It illustrates the decision cleanly:

```text
The directory may remember freely and propose.
Only the Registre Probatoire may be cited for a consequential decision.
An Observation enters the register as an Evidence Candidate, never as canon by itself.
```

## Forbidden imports

Pantheon must not import:

```text
directory-mcp as an internal Pantheon entity registry or memory engine
its remember_* / merge writes as canonical facts
its Observations as proof or approval by themselves
its append-only log as a Pantheon runtime store
any in-Pantheon MCP server, host or directory runtime
OpenWebUI or Hermès direct writes treated as governed records without review
```

## Boundary phrase

```text
directory-mcp resolves who.
Hermès remembers operationally.
Pantheon governs whether an observation becomes probative.
The human decides what is established.
```

## Decision

```text
Distill the graph schema for the actor layer of the Registre Probatoire.
Do not adopt the tool into Pantheon; it is too young to depend on and write-capable by nature.
Keep it external as an optional Hermès-side identity directory under an MCP capability passport.
Treat every Observation as a sourced Evidence Candidate, never as canon or approval.
Expose resolved identities and sourced observations through OpenWebUI only.
```

## Final rule

```text
Review first.
Distill only the schema that survives the boundary.
Install nothing by implication.
```
