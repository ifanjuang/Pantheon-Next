# Common Installation Baseline

Status: candidate support doctrine — selected common installation direction — documented non-implemented.

This document records the common installation baseline for supported deployments.

It defines the required foundation, conditional service posture, default activation posture and responsibility boundaries. It creates no installer, Docker stack, database schema, secret store, scheduler, queue, provider router, plugin manager, configuration writer or approval engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human installs and approves consequential changes.
```

## Core decision

There is one governance baseline and one component-status model, but not every deployment must install every optional service.

```text
common baseline
= required foundation
+ conditional services selected by reviewed capability bindings
+ explicit installation and activation status
```

```text
listed != installed
required foundation != every optional service present
installed != configured
configured != reachable
reachable != healthy
healthy != safe
enabled != task-authorized
runtime success != evidence
```

Installation differences are expressed through observed status, selected bindings and human decisions, not through competing Pantheon kernels or hidden installation variants.

## Required foundation

| Component | Baseline posture |
|---|---|
| Container runtime | required and operator-managed |
| SSH or equivalent operator access | required for bootstrap, maintenance and break-glass use; never a cockpit shell |
| Private user-defined container network | required for internal service communication; normally `ai-net` in the reference deployment |
| Persistent storage | required; paths selected by the human, never hard-coded to one NAS |
| Backup and rollback posture | required before consequential activation |
| Hermes Agent | required external execution runtime with authenticated API |
| OpenWebUI | required user exposure surface connected to Hermes |
| PostgreSQL | required internal relational service for the selected platform records |
| pgvector availability | required in the selected PostgreSQL image or package; use remains separately bound |
| Pantheon MVP Cockpit | external executable candidate when the MVP cockpit binding is selected; installation and adoption remain separate |
| Pantheon policy service / MCP | required only for a selected governed consultation or preflight binding; the binding remains separately activated |
| Health, backup and rollback visibility | required as observations and operator records |

The required foundation does not include a universal model provider, search engine, browser runtime, OCR engine or extraction pipeline.

## Conditional services

Install only when a reviewed capability binding needs them.

| Component | Conditional role | Default posture |
|---|---|---|
| Ollama or another local model runtime | local inference provider candidate | absent or installed but unbound until provider/model review |
| Embedding service | vectorization candidate | absent or installed but indexing binding disabled until model/dimension review |
| Docling | structured document extraction candidate | absent or installed but ingestion binding disabled |
| OCR adapter | image/PDF text extraction candidate | absent or installed but extraction binding disabled |
| SearXNG | search service candidate | absent or installed but Hermes/OpenWebUI bindings disabled |
| Chromium / Browserless | browser execution candidate | absent or installed but browser binding disabled |
| Observability service | runtime trace and health observation candidate | external and separately reviewed |
| External runtime memory | recall/checkpoint candidate | external and separately reviewed; never Registre Probatoire authority |

```text
service present != binding selected
binding selected != dependency adopted
dependency adopted != task use authorized
```

The component installation reference is `docs/install/REFERENCE_PLATFORM_COMPONENTS.md`.

## Canonical active path

```text
user
-> OpenWebUI
-> authenticated Hermes API on the private container network
-> Hermes Agent
-> allowlisted Pantheon policy consultation or preflight when the selected task requires it
-> candidate result returned to OpenWebUI or the Pantheon cockpit
-> human review and decision
```

Conditional services remain sidecars or provider bindings behind Hermes or another separately reviewed adapter. They do not become Pantheon modules.

## Default network posture

```text
Hermes API 8642          -> private container network only
PostgreSQL 5432          -> private container network only
Ollama 11434             -> private container network only when installed
SearXNG service port     -> private container network only when installed
Browserless service port -> private container network only when installed
```

Hermes dashboard and OpenWebUI browser access use operator-selected LAN/VPN exposure. Publishing any internal service port is a separate human decision.

A user-defined bridge network allows service-name resolution and avoids dependence on the default Docker bridge. The reference name `ai-net` is a deployment convention, not a Pantheon runtime object.

## Required but default-off bindings

The following bindings remain inactive until reviewed, whether or not the service is present:

```text
Ollama or another provider -> Hermes inference
SearXNG -> Hermes search
SearXNG -> OpenWebUI native web search
Chromium / Browserless -> Hermes browser capability
Docling -> governed ingestion worker
OCR adapter -> governed extraction worker
embedding service -> pantheon_knowledge indexing
OpenWebUI native RAG -> vector store
Hermes -> direct database access
external runtime memory -> canonical memory
```

Direct Hermes database access and automatic runtime-memory promotion remain blocked by default.

## Data separation

One PostgreSQL server may host several databases, but responsibilities remain separate.

```text
openwebui_app
  OpenWebUI accounts, conversations, settings and application state

pantheon_knowledge
  source references, digests, extraction provenance, structured content,
  chunks, embeddings, quality flags and governed status metadata
```

Use separate database roles. OpenWebUI receives no administrative Pantheon role. Hermes receives no unrestricted access to OpenWebUI or Pantheon tables.

```text
same server != same authority
same extension != shared credentials
```

## Minimum Hermes contract

```text
authenticated API server
pinned provider and model identity
persistent Hermes data directory
reviewed profile and tool surface
Pantheon MCP or policy binding only when selected
explicit allowlist for any selected MCP
no write mount to Pantheon Next
no Docker socket
no host SSH credentials
```

The exact Hermes configuration mechanism is owned by Hermes. Pantheon records expected posture, status and gates.

## Minimum OpenWebUI contract

```text
OpenWebUI -> http://hermes:8642/v1 on the private network
OpenWebUI API key == Hermes API_SERVER_KEY
application database == openwebui_app when PostgreSQL is selected
unused direct Ollama connection disabled when Hermes is the canonical execution path
native web search, RAG and extraction paths disabled until reviewed
```

OpenWebUI may persist connection settings in its database after first launch. Container environment, persisted setting and effective connection must be distinguished.

## Search, browser and ingestion boundary

```text
search result != verified source
page fetched != evidence
browser session authenticated != source admitted
retrieval success != truth
parsed != validated
OCR confidence != professional truth
chunked != evidence
embedded != approved
indexed != Registre Probatoire entry
```

The original source retains a stable locator and digest outside the derived store.

## Cockpit configuration-assistance posture

The cockpit may help with external runtime configuration according to `COCKPIT_RUNTIME_CONFIGURATION_ASSISTANCE.md`.

Initial posture:

```text
observe -> explain -> propose -> human/native application -> verify
```

The preferred first capability is a reviewable Configuration Change Candidate. Direct mutation remains documented non-implemented and default-off.

A future bounded write adapter requires:

```text
native documented interface
allowlisted field
current-value observation
explicit human confirmation
secret isolation
post-write readback
health check
rollback
```

The cockpit does not receive general Docker, SSH, database-administrator or secret-store authority.

## Responsibility map

```text
bootstrap and infrastructure -> human operator / SSH / Portainer / vendor tooling
runtime execution            -> Hermes Agent and selected external services
cockpit exposure             -> OpenWebUI and Pantheon MVP Cockpit
native configuration         -> Hermes/OpenWebUI/vendor administration surfaces
status and gates              -> Pantheon
action approval               -> human
```

Before Hermes exists, the operator installs Hermes and OpenWebUI manually. After Hermes exists, native administration surfaces may expose bounded operations. They must not become a general shell or an approval shortcut.

## Common acceptance criteria

Required foundation:

```text
private network observed
persistent storage identified
backup target identified
Hermes API authenticated
OpenWebUI lists the Hermes model
PostgreSQL internal readiness observed
pgvector availability observed
internal services not host-published by default
rollback target identified
```

Selected binding checks:

```text
selected provider and model recorded
selected MCP or policy path callable
selected tool surface matches the reviewed allowlist
selected conditional service version visible
selected service binding observed disabled or enabled as decided
unknown or contradictory governance candidates fail closed where applicable
```

```text
acceptance passed != professional validation
acceptance passed != capability adoption
acceptance passed != task authorization
```

## Forbidden defaults

```text
public PostgreSQL, Ollama, SearXNG, Browserless or Hermes API exposure
shared administrative database credentials
unrestricted Hermes database access
silent ingestion or cross-project indexing
automatic source-to-evidence promotion
automatic capability activation
automatic model download
background installation or retry loops
arbitrary shell execution from a cockpit
Docker socket or host SSH access from the cockpit
secret retention in Pantheon
automatic update or rollback
```

## Repository status

```text
common baseline doctrine                -> candidate support doctrine
manual runbook                          -> candidate operator artifact
component installation guide            -> implemented as documentation
Hermes/OpenWebUI templates              -> candidate external configuration
cockpit configuration assistance        -> documented non-implemented
universal installer                     -> voluntarily absent
configuration write adapter             -> documented non-implemented / default disabled
PostgreSQL/pgvector deployment          -> external / to verify per installation
Ollama/SearXNG/Browserless/Docling/OCR  -> conditional external services
```
