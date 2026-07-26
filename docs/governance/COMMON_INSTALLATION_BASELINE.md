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

Document ingestion is a core capability, but document source management is not a universal dependency.

```text
document_ingestion
  core capability

local/NAS governed source
  default supported source path

document_source_management
  optional Capability Slot

preferred binding
  paperless_ngx
```

Paperless-ngx is recommended for the reference professional deployment when a managed DMS is useful, but a valid Pantheon installation does not require it.

```text
Paperless absent != Pantheon degraded
Paperless absent != document ingestion unavailable
Paperless installed != binding selected
binding selected != activated
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
| PostgreSQL | required internal relational service for governed data projections; OpenWebUI may keep its own application DB |
| pgvector availability | required platform capability; actual vector use remains separately bound |
| Governed local/NAS document source root | required when local-source ingestion is used; read-only mount and scope/path checks apply |
| Pantheon policy interface | required reviewed consultation/preflight path; current repository implementation remains partial / to verify |

## Conditional services

The following services are documented platform options. They are not universal dependencies of the Pantheon kernel or of every installation.

| Component | Conditional posture |
|---|---|
| Paperless-ngx | preferred binding for optional `document_source_management`; install when a managed DMS/source runtime is selected |
| Paperless internal broker | required only when Paperless is selected; Paperless implementation dependency only |
| Paperless database | required only when Paperless is selected; separate role/database or dedicated instance |
| Paperless bounded gateway | required only for the selected Paperless Pantheon/Hermes binding |
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

Core local document ingestion may use:

```text
read-only local/NAS source
-> Task Contract declared-source check
-> path-boundary check
-> source digest
-> Docling/other reviewed extraction when selected
-> Project Document candidate
-> optional later Knowledge publication
```

When Paperless is selected, document browsing/intake may instead use the bounded Paperless source adapter and exact-version Source Capture.

```text
local source path != unmanaged ingestion
Paperless source path != canonical Knowledge authority
```

Consequential Paperless effects such as upload, metadata/classification mutation, deletion, permission changes or version replacement remain behind the Pantheon/Hermes chokepoint.

## Default network posture

```text
Hermes API 8642      -> internal only
PostgreSQL 5432      -> internal only
conditional services -> internal only unless separately approved
Paperless API 8000   -> only when Paperless selected; internal/loopback during bootstrap
```

Publishing any internal service port is a separate human decision.

## Minimal cockpit relationship

The cockpit is not a second runtime administrator and not a duplicate policy engine.

Its future minimum runtime-connection view may observe:

```text
Hermes and OpenWebUI version and reachability
effective OpenWebUI -> Hermes connection
Pantheon MCP binding presence and reachability
selected document-source binding
Paperless version/reachability only when selected
configuration compatibility after update
```

Policy, classification, validation, status distinctions and refusal reasons remain in the Pantheon MCP. Installation and maintenance remain in native/operator tooling.

```text
cockpit display != policy source
runtime observation != governance decision
configuration guidance != configuration execution
```

## Default-off bindings

Presence does not activate a service or binding. Initial posture remains default-off until reviewed:

```text
Paperless -> Cockpit/Hermes document source adapter        optional
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

An inactive or unselected binding changes only the qualified state of the installation.

## Data separation

One PostgreSQL server may host several databases, but responsibilities remain separate.

```text
openwebui_app
  OpenWebUI accounts, conversations, settings and application state

pantheon_knowledge / Agency Data
  source references, digests, extraction provenance, structured content,
  chunks, embeddings, quality flags and governed status metadata

paperless_app                     only when Paperless selected
  Paperless document metadata, task/runtime state and application configuration
  source bytes remain in Paperless-managed media storage
```

Use separate database roles. OpenWebUI receives no administrative Pantheon role. Hermes receives no unrestricted access to OpenWebUI or Paperless tables.

When Paperless is selected, integrations use its reviewed API rather than direct database access. Paperless media/data/export storage then becomes part of the operator backup plan.

## Minimum connection contract

Hermes core:

```text
authenticated API server
pinned inference provider and model
reviewed Pantheon policy interface
bounded API-facing tool exposure
```

Paperless-specific Hermes/gateway inputs are required only when the Paperless binding is selected.

OpenWebUI:

```text
OpenWebUI -> http://hermes:8642/v1
OpenWebUI connection key == Hermes API server key
OpenAI API passthrough disabled unless separately reviewed
application database isolated from governed data store
native search/RAG paths disabled until reviewed
```

Paperless, when selected:

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

For any source path, the original source retains a stable locator and digest outside the derived store.

For Paperless, an immutable intake binds exact document/version identity and content hash; a mutable `latest` pointer is insufficient provenance.

For local/NAS ingestion, the Task Contract declared source, resolved-path boundary and content digest provide the corresponding bounded source identity.

## Responsibility map

```text
bootstrap and infrastructure -> human operator / SSH / Portainer / vendor tooling
local source storage          -> operator/NAS filesystem
Paperless native processing   -> Paperless external runtime, only when selected
runtime execution             -> Hermes Agent
cockpit exposure              -> OpenWebUI and Pantheon MVP projection
policy and validation         -> Pantheon MCP
status and gates              -> Pantheon
consequential approval        -> human
```

Before Hermes exists, the operator installs the required core manually. Paperless is added separately only when the document-source-management capability is selected.

Paperless's own broker, workers and scheduler remain implementation details of that external runtime. Their presence does not authorize Pantheon or Hermes to create a parallel queue, scheduler or hidden workflow.

## Common acceptance criteria

Required core foundation:

```text
private network exists
persistent storage and backup posture recorded
Hermes API authenticated
OpenWebUI lists the Hermes model
Hermes API and PostgreSQL are not host-published by default
OpenWebUI effective connection targets Hermes through the private network
local/NAS source root is read-only and bounded when used
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

Paperless-specific acceptance, only when selected:

```text
Paperless image/tag/digest recorded
Paperless database and media/data storage persistent
Paperless API only on intended private/loopback path
Paperless API token ownership identified and not committed
Paperless backup covers database plus media/data/export requirements
Paperless AI/remote OCR absent unless separately reviewed
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
document ingestion core             -> local/NAS governed path implemented externally / target deployment to verify
document_source_management          -> optional Capability Slot
Paperless preferred binding          -> external implementation merged / optional profile / target install to verify
Paperless executable adapter         -> implemented externally / not adopted
minimal cockpit connection model     -> implemented as documentation
runtime observation adapters         -> external implementation candidate / target not observed
configuration write adapter          -> not selected / documented non-implemented
universal installer                  -> intentionally absent
PostgreSQL/pgvector deployment       -> external / to verify per installation
conditional service bindings         -> documented non-implemented here
```
