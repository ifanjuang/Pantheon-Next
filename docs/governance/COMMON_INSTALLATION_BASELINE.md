# Common Installation Baseline

Status: candidate support doctrine — common installation baseline; documented non-implemented.

This document defines one common Pantheon installation baseline for all supported deployments.

It replaces preset selection as the current installation orientation. It does not create an installer, Docker stack, package, shell runner, database schema, secret store, scheduler, queue, provider router, plugin manager or approval engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human installs and approves consequential changes.
```

## Purpose

Every supported installation should expose the same minimum technical capabilities and the same status distinctions.

The common baseline is not a promise that every installed component is activated for every task.

```text
required presence != enabled binding
installed != configured
configured != reachable
reachable != healthy
healthy != safe
runtime success != evidence
enabled != task-authorized
```

## No preset selection

The current installation path does not ask the user to choose a Pantheon preset.

`INSTALL_MODULE_CATALOG.md` remains a generic candidate grammar for describing modules, dependencies and gates. Its preset examples are not the active installation contract for the common baseline.

The common baseline may still record conditional activation, capability gaps and environment-specific bindings. Those distinctions do not create alternate product editions.

## Common required components

| Component | Required baseline presence | Default operational posture |
|---|---|---|
| Container runtime | yes | active and operator-managed |
| SSH operator access | yes | administrative and break-glass use only; never exposed as a Pantheon dashboard shell |
| Private container network | yes | internal service communication; no implicit public exposure |
| Persistent storage | yes | paths selected by the human operator; no hard-coded NAS volume |
| Hermes Agent | yes | execution runtime; API authenticated |
| OpenWebUI | yes | user cockpit connected to Hermes |
| PostgreSQL | yes | internal-only relational service with persistent backup |
| pgvector | yes | installed as a PostgreSQL extension; use remains separately bound and verified |
| Embedding service | yes | installed or reachable; model and vector dimension must be explicitly selected before indexing |
| Docling | yes | available for governed ingestion; no automatic ingestion binding by presence alone |
| SearXNG | yes | internal-only search service; no automatic OpenWebUI or Hermes binding by presence alone |
| Pinned Pantheon checkout | yes | mounted read-only for consultation and verification |
| Pantheon policy MCP | yes | bounded read-only allowlist; no authority or write effect |
| Pantheon Modules dashboard plugin | yes | observation and separately confirmed Hermes-native controls only |
| Health, backup and rollback | yes | visible and testable; configured backup is not a verified restore |

## Required active path

The minimum active interaction path is:

```text
user
-> OpenWebUI
-> authenticated Hermes API on the private container network
-> Hermes Agent
-> allowlisted Pantheon policy MCP consultation when governance context is needed
-> candidate result returned to OpenWebUI
```

The Hermes API, PostgreSQL and SearXNG must not be published to the host or LAN merely because the containers are running. Any broader exposure is a separate human decision.

## Installed but not automatically activated

The following components belong to the common baseline but their bindings remain default-off until their exact path, scope and verification are established:

```text
SearXNG -> Hermes search binding
SearXNG -> OpenWebUI native web-search binding
Docling -> governed ingestion worker
embedding service -> pantheon_knowledge indexing
OpenWebUI native RAG -> pgvector
Hermes -> direct database access
```

Default rule:

```text
service installed
!= binding selected
!= dependency adopted
!= task use authorized
```

## Data separation

One PostgreSQL server may host multiple databases, but responsibilities must remain explicit.

Minimum separation:

```text
openwebui_app
  OpenWebUI accounts, conversations, settings and application state

pantheon_knowledge
  source references, file digests, extraction provenance, structured content,
  retrieval chunks, embeddings, quality flags and governed status metadata
```

Separate database roles must be used. OpenWebUI must not receive an administrative Pantheon database role. Hermes must not receive unrestricted access to OpenWebUI internal tables.

Direct Hermes access to raw OpenWebUI or Pantheon database tables is not the normal workflow. A future governed read-only gateway or bounded database view may be adopted separately.

## OpenWebUI posture

OpenWebUI is configured as the common cockpit and as an OpenAI-compatible client of Hermes.

Required:

```text
OpenWebUI -> http://hermes:8642/v1
OpenWebUI API key == Hermes API_SERVER_KEY
OpenAI API passthrough disabled
```

Default-off in the common baseline until a reviewed binding exists:

```text
OpenWebUI native web search
OpenWebUI-native canonical RAG
OpenWebUI Docling extraction path
OpenWebUI direct ownership of pantheon_knowledge
```

OpenWebUI may display selected Knowledge, retrieved material, evidence candidates and governed status. Display does not grant authority.

## Hermes posture

Hermes owns execution and runtime administration.

The common baseline requires:

```text
authenticated API server
private network access from OpenWebUI
pinned inference provider and model configuration
versioned Pantheon MCP executable
read-only pinned Pantheon checkout
explicit MCP tool allowlist
prompts disabled
resources disabled
sampling disabled
parallel MCP calls disabled by conservative default
```

Hermes may execute search, ingestion and retrieval only after the corresponding binding and task scope are established. Hermes must not infer authorization from component presence or health.

## Search and ingestion posture

SearXNG search results are source candidates.

```text
search result != verified source
page fetched != evidence
retrieval success != truth
```

Docling extraction produces derived knowledge candidates with provenance.

```text
parsed != validated
chunked != evidence
embedded != approved
indexed != Registre Probatoire entry
```

A source original remains outside the derived store and must retain a stable locator and digest.

## Installation and administration path

Before Hermes exists, installation is manual through the human operator, SSH, Docker Compose, Portainer or vendor tooling.

After Hermes exists, its dashboard may expose native, bounded and separately confirmed operations. It must not become a general shell or silently change Docker, network, volume, secret or database state.

```text
bootstrap owner        -> human operator / vendor tooling
runtime execution      -> Hermes
cockpit                -> OpenWebUI and Hermes dashboard
status governance      -> Pantheon
consequential approval -> human
```

## Common acceptance criteria

A common installation is not operationally accepted until all applicable checks are observed:

```text
Hermes API authenticated
OpenWebUI can list the Hermes model
Hermes API host port is not published unless explicitly approved
PostgreSQL is reachable internally and not publicly exposed
pgvector extension version is visible
SearXNG is reachable internally and not publicly exposed
Pantheon checkout commit is visible and mounted read-only
Pantheon MCP exposes only the reviewed tool allowlist
unknown architecture topics fail closed
contradictory capability status fails closed
MCP authority_effect is none
MCP write_effect is false
MCP runtime_probe_performed is false
backup exists
restore procedure is documented
rollback target is identified
```

Acceptance confirms the observed technical baseline only.

```text
acceptance passed != professional validation
acceptance passed != capability adoption
acceptance passed != task authorization
```

## Forbidden defaults

The common baseline must not introduce:

```text
public PostgreSQL exposure
public SearXNG exposure
public Hermes API exposure without an explicit guard
OpenWebUI API passthrough
shared administrative database credentials
unrestricted Hermes database access
silent document ingestion
automatic cross-project indexing
automatic source-to-evidence promotion
automatic capability activation
background installation or retry loops
a dashboard terminal with arbitrary shell execution
secret retention in Pantheon
```

## Repository status

This file is the reviewed orientation target for a future common installation runbook and templates.

Current classification:

```text
common baseline doctrine       -> candidate support doctrine
manual runbook                 -> candidate artifact
Hermes/OpenWebUI templates     -> candidate external configuration
live universal installer       -> intentionally absent
PostgreSQL/pgvector deployment -> external / to verify per installation
Docling binding                -> documented non-implemented here
SearXNG binding                -> documented non-implemented here
```

## Boundary phrase

```text
The baseline makes the same capabilities available to everyone.
It does not silently activate every capability for every task.
Hermes executes.
OpenWebUI exposes.
Pantheon governs status.
The human approves installation, binding, exposure and consequential use.
```
