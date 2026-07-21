# Common Installation Baseline

Status: candidate support doctrine — common installation baseline; documented non-implemented.

Pantheon uses one common installation baseline for supported deployments. The user does not choose a Pantheon preset.

This document defines required presence, default activation and responsibility boundaries. It creates no installer, Docker stack, database schema, secret store, scheduler, queue, provider router, plugin manager or approval engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human installs and approves consequential changes.
```

## Core decision

Every installation receives the same base capabilities. A required component is not automatically enabled for every task.

```text
required presence != enabled binding
installed != configured
configured != reachable
reachable != healthy
healthy != safe
enabled != task-authorized
runtime success != evidence
```

`INSTALL_MODULE_CATALOG.md` remains a generic grammar for module records and dependency descriptions. Its preset examples are not the active installation contract.

## Common required components

| Component | Baseline posture |
|---|---|
| Container runtime | required and operator-managed |
| SSH operator access | required for bootstrap, maintenance and break-glass use; never a Pantheon dashboard shell |
| Private container network | required for internal service communication |
| Persistent storage | required; paths selected by the human, never hard-coded to one NAS |
| Hermes Agent | required execution runtime with authenticated API |
| OpenWebUI | required user cockpit connected to Hermes |
| PostgreSQL | required internal-only relational service |
| pgvector | required PostgreSQL extension; use remains separately bound |
| Embedding service | required presence; model and vector dimension selected before indexing |
| Docling | required presence for governed ingestion; no automatic ingestion by presence alone |
| SearXNG | required presence for search; no automatic binding by presence alone |
| Pinned Pantheon checkout | required and mounted read-only |
| Pantheon policy MCP | required with the reviewed read-only allowlist |
| Pantheon Modules plugin | required dashboard observation surface; native actions remain separately confirmed |
| Health, backup and rollback | required and visible |

## Canonical active path

```text
user
-> OpenWebUI
-> authenticated Hermes API on the private container network
-> Hermes Agent
-> allowlisted Pantheon policy MCP consultation when needed
-> candidate result returned to OpenWebUI
```

Default network posture:

```text
Hermes API 8642      -> internal only
PostgreSQL 5432      -> internal only
SearXNG service port -> internal only
```

Publishing any of these ports is a separate human decision.

## Required but default-off bindings

These services belong to the common baseline, but their execution bindings remain inactive until reviewed:

```text
SearXNG -> Hermes search
SearXNG -> OpenWebUI native web search
Docling -> governed ingestion worker
embedding service -> pantheon_knowledge indexing
OpenWebUI native RAG -> pgvector
Hermes -> direct database access
```

```text
service installed
!= binding selected
!= dependency adopted
!= task use authorized
```

No alternate preset is created by leaving a binding inactive. The installation remains the same; only its qualified status differs.

## Data separation

One PostgreSQL server may host several databases, but responsibilities remain separate.

```text
openwebui_app
  OpenWebUI accounts, conversations, settings and application state

pantheon_knowledge
  source references, digests, extraction provenance, structured content,
  chunks, embeddings, quality flags and governed status metadata
```

Use separate database roles. OpenWebUI does not receive an administrative Pantheon role. Hermes does not receive unrestricted access to OpenWebUI internal tables.

Direct database access is not the normal governed workflow. A future read-only gateway or bounded database view requires separate review.

## Minimum configuration contract

Hermes:

```text
authenticated API server
pinned inference provider and model
versioned Pantheon MCP executable
pinned read-only Pantheon checkout
six-tool MCP allowlist
prompts/resources/sampling disabled
parallel MCP calls disabled by conservative default
```

OpenWebUI:

```text
OpenWebUI -> http://hermes:8642/v1
OpenWebUI API key == Hermes API_SERVER_KEY
OpenAI API passthrough disabled
application database == openwebui_app
native web search/RAG/Docling paths disabled until reviewed
```

## Search and ingestion boundary

SearXNG results are source candidates.

```text
search result != verified source
page fetched != evidence
retrieval success != truth
```

Docling and embeddings produce derived knowledge candidates with provenance.

```text
parsed != validated
chunked != evidence
embedded != approved
indexed != Registre Probatoire entry
```

The original source retains a stable locator and digest outside the derived store.

## Installation and operational ownership

```text
bootstrap and infrastructure -> human operator / SSH / Portainer / vendor tooling
runtime execution            -> Hermes Agent
cockpit                       -> OpenWebUI and Hermes dashboard
status and gates              -> Pantheon
consequential approval        -> human
```

Before Hermes exists, the operator installs Hermes and OpenWebUI manually. After Hermes exists, its dashboard may expose only bounded, separately confirmed native operations. It must not become a general shell.

## Common acceptance criteria

The baseline is technically accepted only when the applicable observations are present:

```text
Hermes API authenticated
OpenWebUI lists the Hermes model
8642, 5432 and SearXNG are not host-published by default
PostgreSQL internal readiness observed
pgvector extension version visible
SearXNG and Docling versions visible
embedding model and dimension recorded
Pantheon checkout commit visible and read-only
Pantheon MCP exposes only the reviewed allowlist
unknown architecture topics fail closed
contradictory capability status fails closed
authority_effect == none
write_effect == false
runtime_probe_performed == false
backup present
restore procedure documented
rollback target identified
```

```text
acceptance passed != professional validation
acceptance passed != capability adoption
acceptance passed != task authorization
```

## Forbidden defaults

```text
public PostgreSQL, SearXNG or Hermes API exposure
OpenWebUI API passthrough
shared administrative database credentials
unrestricted Hermes database access
silent ingestion or cross-project indexing
automatic source-to-evidence promotion
automatic capability activation
background installation or retry loops
arbitrary shell execution from a dashboard
secret retention in Pantheon
```

## Repository status

```text
common baseline doctrine       -> candidate support doctrine
manual runbook                 -> candidate operator artifact
Hermes/OpenWebUI templates     -> candidate external configuration
universal installer            -> intentionally absent
PostgreSQL/pgvector deployment -> external / to verify per installation
Docling and SearXNG bindings   -> documented non-implemented here
```

## Boundary phrase

```text
The baseline makes the same capabilities available to everyone.
It does not silently activate every capability for every task.
Hermes executes. OpenWebUI exposes. Pantheon governs. The human decides.
```
