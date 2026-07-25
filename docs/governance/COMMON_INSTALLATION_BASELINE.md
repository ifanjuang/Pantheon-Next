# Common Installation Baseline

Status: candidate support doctrine — selected common installation direction — documented non-implemented.

This document records the common installation baseline for supported deployments.

It defines required foundation presence, conditional service posture and responsibility boundaries. It creates no installer, Docker stack, database schema, secret store, scheduler, queue, provider router, plugin manager or approval engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human installs and approves consequential changes.
```

## Core decision

Every supported installation starts from the same foundation. Conditional services are added only when a reviewed capability binding requires them.

For the reference professional deployment, document source management is part of the initial foundation: Paperless-ngx is present as the external document backing runtime, while its Pantheon/Hermes binding remains default-off until reviewed and configured.

```text
required foundation != every optional service installed
installed != configured
configured != reachable
reachable != healthy
healthy != safe
enabled != task-authorized
runtime success != evidence
```

There is one baseline status model. Variants are expressed through observed service presence, selected bindings, activation posture and human decisions rather than through several competing Pantheon architectures.

## Required foundation

| Component | Baseline posture |
|---|---|
| Container runtime or equivalent substrate | required and operator-managed |
| Operator maintenance access | required for bootstrap, maintenance and break-glass use; never a dashboard shell |
| Private container network such as `ai-net` | required for internal service communication |
| Persistent storage | required; paths selected by the human, never hard-coded to one NAS |
| Backup and rollback posture | required and recorded before consequential changes |
| Hermes Agent | required external execution runtime with authenticated API |
| OpenWebUI | required exposure surface connected to Hermes |
| PostgreSQL | required internal relational service for OpenWebUI and governed data projections |
| pgvector availability | required platform capability; actual vector use remains separately bound |
| Paperless-ngx | required document source-management runtime for the reference professional installation; installed presence does not activate project intake, Knowledge publication or metadata writes |
| Paperless internal broker | required only as an implementation dependency of the installed Paperless runtime; never a Pantheon/Hermes queue or scheduler |
| Pantheon policy interface | required reviewed consultation/preflight path; current repository implementation remains partial / to verify |

Paperless may use a dedicated PostgreSQL instance or a separate database/role on the common PostgreSQL server. Database separation, backup ownership and rollback evidence are required either way.

## Conditional services

The following services are documented platform options. They are not universal dependencies of the Pantheon kernel or of every installation.

| Component | Conditional posture |
|---|---|
| Ollama | install when a reviewed local-model binding requires it |
| Embedding service | install when governed indexing or retrieval requires a selected model and recorded dimension |
| SearXNG | install when a reviewed web-search binding is selected |
| Chromium / Browserless | install when a reviewed browser or page-rendering binding requires it |
| Docling | install when a reviewed document-analysis binding requires it |
| PaddleOCR, olmOCR or vision extraction service | install only for a selected extraction capability slot |
| Observability backend | install when a reviewed runtime-observation binding requires it |
| External runtime memory | install when separately reviewed; it remains outside the Registre Probatoire |

```text
service documented != service required
service installed != binding selected
binding selected != dependency adopted
dependency adopted != task use authorized
```

## Canonical active path

```text
user
-> OpenWebUI / Cockpit
-> authenticated Hermes API on the private container network
-> Hermes Agent
-> allowlisted Pantheon policy consultation/preflight when needed
-> candidate result returned to OpenWebUI
```

Document browsing may additionally use the bounded Paperless read adapter. Consequential Paperless effects such as upload, metadata/classification mutation, deletion, permission changes or version replacement remain behind the Pantheon/Hermes chokepoint.

Default network posture:

```text
Hermes API 8642      -> internal only
PostgreSQL 5432      -> internal only
Paperless API 8000   -> internal only or loopback during bootstrap
conditional services -> internal only unless separately approved
```

Publishing any internal service port is a separate human decision.

## Minimal cockpit relationship

The cockpit is not a second runtime administrator and not a duplicate policy engine.

Its future minimum runtime-connection view may observe:

```text
Hermes and OpenWebUI version and reachability
effective OpenWebUI -> Hermes connection
Pantheon MCP binding presence and reachability
Paperless version, reachability and bounded API binding status
configuration compatibility after update
```

Policy, classification, validation, status distinctions and refusal reasons remain in the Pantheon MCP. Installation and maintenance remain in native/operator tooling.

```text
cockpit display != policy source
runtime observation != governance decision
configuration guidance != configuration execution
```

Configuration formats may change between runtime versions. No hard-coded YAML, JSON, environment-variable or file path is a universal contract. Unsupported versions route to native/upstream guidance.

## Required but default-off bindings

Presence does not activate a service or binding. Initial posture remains default-off until reviewed:

```text
Paperless -> Cockpit/Hermes document source adapter
Paperless metadata -> Pantheon business-classification mirror
Paperless source -> Project Document / Knowledge publication
SearXNG -> Hermes search
SearXNG -> OpenWebUI native web search
Browserless/Chromium -> browser capability
Docling -> governed document analysis
OCR/vision extraction -> document extraction workflow
embedding service -> pantheon_knowledge indexing
OpenWebUI native RAG -> pgvector
Hermes -> direct database access
external runtime memory -> Hermes recall/checkpoint path
```

An inactive binding changes only the qualified state of the installation.

## Data separation

One PostgreSQL server may host several databases, but responsibilities remain separate.

```text
openwebui_app
  OpenWebUI accounts, conversations, settings and application state

paperless_app
  Paperless document metadata, task/runtime state and application configuration
  source bytes remain in Paperless-managed media storage

pantheon_knowledge
  source references, digests, extraction provenance, structured content,
  chunks, embeddings, quality flags and governed status metadata
```

Use separate database roles. OpenWebUI receives no administrative Pantheon role. Hermes receives no unrestricted access to OpenWebUI or Paperless tables. Pantheon/Hermes integrations use the reviewed Paperless API rather than direct Paperless database access.

Paperless media, data and export/backup storage must be included in the operator backup plan. A Paperless database backup without source media is not a complete document backup.

## Minimum connection contract

Hermes:

```text
authenticated API server
pinned inference provider and model
reviewed Pantheon policy interface
bounded API-facing tool exposure
Paperless API token only when the document-source binding is explicitly configured
```

OpenWebUI:

```text
OpenWebUI -> http://hermes:8642/v1
OpenWebUI connection key == Hermes API server key
OpenAI API passthrough disabled unless separately reviewed
application database == openwebui_app
native search/RAG paths disabled until reviewed
```

Paperless:

```text
pinned image tag or digest
private API endpoint
separate database role/database
internal broker private to Paperless
persistent data + media storage
backup and restore plan
API token held by the external runtime, never by Pantheon doctrine
remote OCR and Paperless AI/LLM/vector paths unconfigured by default
```

The effective OpenWebUI configuration may be persisted in its database and may differ from container environment declarations. Operator verification must inspect the effective connection.

## Search and ingestion boundary

```text
search result != verified source
page fetched != evidence
Paperless OCR != source truth
Paperless task success != professional validation
Paperless metadata != canonical business classification
retrieval success != truth
parsed != validated
chunked != evidence
embedded != approved
indexed != Registre Probatoire entry
```

The original source retains a stable locator and digest outside the derived store. A governed Paperless Source Capture should bind an exact document/version identifier and content hash; a mutable "latest" view is insufficient provenance for immutable intake.

## Responsibility map

```text
bootstrap and infrastructure -> human operator / SSH / Portainer / vendor tooling
Paperless native processing   -> Paperless external runtime
runtime execution            -> Hermes Agent
cockpit exposure             -> OpenWebUI and Pantheon MVP projection
policy and validation        -> Pantheon MCP
status and gates             -> Pantheon
consequential approval       -> human
```

Before Hermes exists, the operator installs Hermes, OpenWebUI and the required Paperless source runtime manually. After Hermes exists, native administration surfaces may expose bounded operations. The Pantheon cockpit remains a minimal observation and guidance surface, not a general shell or configuration editor.

Paperless's own broker, workers and scheduler are implementation details of the external Paperless runtime. Their presence does not authorize Pantheon or Hermes to create a parallel queue, scheduler or hidden workflow.

## Common acceptance criteria

Required foundation:

```text
private network exists
persistent storage and backup posture recorded
Hermes API authenticated
OpenWebUI lists the Hermes model
Hermes API and PostgreSQL are not host-published by default
OpenWebUI effective connection targets Hermes through the private network
Paperless exact image/tag/digest recorded
Paperless database and media/data storage are persistent
Paperless API is reachable only through the intended private/loopback path
Paperless API token ownership is identified and not committed
Paperless backup includes database plus media/data/export requirements
Paperless AI/remote OCR paths are absent unless separately reviewed
Pantheon policy consultation path is observable
unknown architecture topics fail closed in the policy interface
contradictory capability status fails closed
rollback target identified
```

Conditional service acceptance applies only when selected:

```text
exact service version and image/package reference recorded
service is reachable only through the intended network path
selected binding identified
health signal observed
secret owner identified
backup/update/rollback notes recorded
activation remains separately approved
```

```text
acceptance passed != professional validation
acceptance passed != capability adoption
acceptance passed != task authorization
```

## Forbidden defaults

```text
public PostgreSQL, Paperless, SearXNG, Browserless or Hermes API exposure
OpenWebUI API passthrough without review
shared administrative database credentials
unrestricted Hermes database access
direct Hermes/Pantheon writes to Paperless database tables
Paperless AI/LLM or remote OCR activation by implication
silent ingestion or cross-project indexing
automatic source-to-evidence promotion
automatic capability activation
background installation or retry loops
arbitrary shell execution from a dashboard
arbitrary cockpit configuration-file editing
hard-coded config field paths treated as version-independent
secret retention in Pantheon
```

## Repository status

```text
common baseline doctrine             -> candidate support doctrine
manual runbook                       -> candidate operator artifact
component guide                      -> implemented as documentation
Paperless source runtime direction   -> selected for initial reference installation; target install still to verify
Paperless executable adapter         -> implemented externally in pantheon-mvp candidate branch / not adopted
minimal cockpit connection model     -> implemented as documentation
live runtime observation adapters    -> documented non-implemented
configuration write adapter          -> not selected / documented non-implemented
universal installer                  -> intentionally absent
PostgreSQL/pgvector deployment       -> external / to verify per installation
conditional service bindings         -> documented non-implemented here
```
