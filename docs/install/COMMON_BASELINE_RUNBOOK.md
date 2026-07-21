# Common Installation Baseline — Manual Runbook

Status: candidate operator runbook — documented non-implemented; no automatic installer.

This runbook prepares the common Pantheon baseline through SSH, Docker Compose, Portainer or equivalent operator tooling.

It assumes that Hermes Agent and OpenWebUI may be installed manually before Pantheon integration begins.

It does not execute commands, create secrets, select a provider, open ports, change a firewall, modify a reverse proxy, create a database, install a package, restart a stack or authorize production use by its presence in this repository.

Read first:

```text
docs/governance/COMMON_INSTALLATION_BASELINE.md
docs/governance/BOOTSTRAP_INSTALLATION_LADDER.md
docs/governance/HERMES_INTEGRATION.md
docs/governance/OPENWEBUI_INTEGRATION.md
templates/hermes/connection/pantheon_policy_mcp.template.yaml
```

## 1. Human decisions before installation

Record these values outside the repository:

```text
TARGET_HOST
CONTAINER_DATA_ROOT
PANTHEON_COMMIT
PANTHEON_VERSION
HERMES_IMAGE_OR_INSTALL_SOURCE
OPENWEBUI_IMAGE
POSTGRES_IMAGE_WITH_PGVECTOR_SUPPORT
EMBEDDING_PROVIDER_AND_MODEL
DOCLING_INSTALL_SOURCE
SEARXNG_IMAGE
PRIVATE_CONTAINER_NETWORK
HERMES_API_SERVER_KEY
OPENWEBUI_SECRET_KEY
DATABASE_PASSWORDS
BACKUP_TARGET
ROLLBACK_TARGET
```

Do not use a local deployment path such as `/volume3/docker` as a portable default. The operator selects the real storage root.

## 2. Bootstrap boundary

Before Hermes exists:

```text
human / SSH / Portainer / Docker Compose installs
Hermes cannot install Hermes
OpenWebUI cannot configure an unavailable Hermes API
Pantheon provides plans and checks only
```

The operator must first establish:

```text
administrative access
container runtime
private container network
persistent storage
backup or snapshot posture
Hermes installation
OpenWebUI installation
```

Hermes and OpenWebUI may be installed using their reviewed upstream procedures. The exact provider, model and image versions remain operator decisions and must be pinned or recorded.

## 3. Network posture

Use one private container network for service-to-service communication.

Expected internal names:

```text
hermes
openwebui
postgres
searxng
```

Default host-port posture:

```text
Hermes dashboard port     -> operator-selected LAN/VPN exposure
OpenWebUI port            -> operator-selected cockpit exposure
Hermes API 8642           -> internal only
PostgreSQL 5432           -> internal only
SearXNG service port      -> internal only
```

Publishing a port is a separate exposure decision. A service listening inside its container does not require a host mapping for another container on the same network.

## 4. Hermes container configuration

Minimum environment contract:

```yaml
API_SERVER_ENABLED: "true"
API_SERVER_HOST: "0.0.0.0"
API_SERVER_PORT: "8642"
API_SERVER_KEY: "${HERMES_API_SERVER_KEY}"

HERMES_INFERENCE_PROVIDER: "<PINNED_PROVIDER>"
HERMES_INFERENCE_MODEL: "<PINNED_MODEL>"
OPENAI_BASE_URL: "<MODEL_ENDPOINT>/v1"
OPENAI_API_KEY: "<MODEL_ENDPOINT_KEY_OR_LOCAL_PLACEHOLDER>"
```

The two keys have different responsibilities:

```text
OPENAI_API_KEY  -> Hermes to the model provider
API_SERVER_KEY  -> OpenWebUI to Hermes
```

Do not replace a working local-provider key merely to align names.

Persist the Hermes data/configuration directory. Do not mount the Pantheon repository read-write.

## 5. Pinned Pantheon checkout

Prepare a separate checkout for the selected revision.

Illustrative operator sequence:

```bash
export PANTHEON_COMMIT="<FULL_COMMIT_SHA>"
export PANTHEON_SHORT="$(printf '%s' "$PANTHEON_COMMIT" | cut -c1-7)"
export PANTHEON_ROOT="<CONTAINER_DATA_ROOT>/pantheon"
export PANTHEON_CHECKOUT="$PANTHEON_ROOT/pantheon-next-$PANTHEON_SHORT"

git clone https://github.com/ifanjuang/Pantheon-Next.git "$PANTHEON_CHECKOUT"
git -C "$PANTHEON_CHECKOUT" checkout --detach "$PANTHEON_COMMIT"
git -C "$PANTHEON_CHECKOUT" status --short
git -C "$PANTHEON_CHECKOUT" rev-parse HEAD
```

Expected:

```text
working tree clean
resolved commit == selected commit
```

Mount this checkout read-only in Hermes, for example:

```yaml
volumes:
  - <HOST_PINNED_CHECKOUT>:/opt/pantheon-next-<COMMIT_SHORT>:ro
```

```text
checkout present != revision verified
revision verified != revision approved
read-only mount != source truth by itself
```

## 6. Versioned Pantheon MCP installation

Install the MCP package into a side-by-side versioned virtual environment. Do not overwrite the previous working environment before acceptance passes.

Illustrative operator sequence inside or against the Hermes persistent data area:

```bash
python3 -m venv /opt/data/pantheon-mcp/<PANTHEON_VERSION>/venv
/opt/data/pantheon-mcp/<PANTHEON_VERSION>/venv/bin/python \
  -m pip install --upgrade pip
/opt/data/pantheon-mcp/<PANTHEON_VERSION>/venv/bin/python \
  -m pip install "/opt/pantheon-next-<COMMIT_SHORT>/mcp-server"
/opt/data/pantheon-mcp/<PANTHEON_VERSION>/venv/bin/pantheon-mcp-server --help
```

Keep the previous executable path available for rollback.

## 7. Hermes MCP configuration

Merge the reviewed fragment from:

```text
templates/hermes/connection/pantheon_policy_mcp.template.yaml
```

The common baseline exposes only:

```text
list_sources
read_doctrine
explain_governance_structure
get_consultation_catalog
explain_architecture
get_capability_status
```

Required posture:

```text
prompts disabled
resources disabled
sampling disabled
parallel tool calls disabled
repository path pinned and read-only
```

Do not add undocumented tools because the server package contains them. Server implementation presence is not API exposure approval.

Do not copy a `platform_toolsets.api_server` name from another Hermes version without testing that exact version. Dynamic MCP registration and the static `/v1/toolsets` catalog may not use the same naming surface.

## 8. OpenWebUI connection to Hermes

Minimum environment contract:

```yaml
ENABLE_OPENAI_API: "true"
OPENAI_API_BASE_URL: "http://hermes:8642/v1"
OPENAI_API_KEY: "${HERMES_API_SERVER_KEY}"
ENABLE_OPENAI_API_PASSTHROUGH: "false"
WEBUI_SECRET_KEY: "${OPENWEBUI_SECRET_KEY}"
DATABASE_URL: "postgresql://openwebui_app:${OPENWEBUI_DB_PASSWORD}@postgres:5432/openwebui_app"
```

OpenWebUI and Hermes must use the same `HERMES_API_SERVER_KEY` value for this connection.

OpenWebUI persistent configuration may override later environment changes. For an existing installation, verify both the container environment and the OpenWebUI administration settings.

Default-off until separately reviewed:

```text
OpenWebUI native web search
OpenWebUI native canonical RAG
OpenWebUI Docling extraction
OpenWebUI API passthrough
```

## 9. PostgreSQL and pgvector

Use an internal-only PostgreSQL service with persistent storage and backup.

Minimum logical separation:

```text
database: openwebui_app
role:     openwebui_app
purpose:  OpenWebUI application state

database: pantheon_knowledge
role:     pantheon_knowledge_writer
purpose:  governed derived document and retrieval data

role:     pantheon_knowledge_reader
purpose:  future bounded read-only consultation where approved
```

Enable the `vector` extension in the database that will hold Pantheon retrieval embeddings.

Illustrative administrative SQL:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Run database creation and extension changes with an administrative role, then use limited application roles for normal operation.

Do not give Hermes an unrestricted administrative database credential. Do not expose port 5432 on `0.0.0.0`.

## 10. Embeddings, Docling and SearXNG

These services belong to the common baseline, but installation presence does not select their active binding.

Record for embeddings:

```text
provider
exact model
vector dimension
data-processing posture
reindex requirement
```

Record for Docling:

```text
exact version
installation source
light/deep configuration
input roots
output database
quality report path
```

Record for SearXNG:

```text
exact image/version
internal endpoint
enabled engines
JSON response support
outbound network policy
```

Initial posture:

```text
Docling installed/reachable      -> binding not yet adopted
SearXNG installed/reachable      -> binding not yet adopted
embedding service reachable      -> no indexing before model/dimension approval
OpenWebUI native search disabled -> prevents a second ungoverned search path
```

A later implementation may bind Hermes to these services under a Task Contract and evidence expectations.

## 11. Pantheon Modules dashboard plugin

Install without enabling first:

```bash
hermes plugins install \
  ifanjuang/Pantheon-Next/templates/hermes/dashboard-plugins/pantheon-modules \
  --no-enable
```

Review the installed files, then enable explicitly:

```bash
hermes plugins enable pantheon-modules
```

The plugin may observe native Hermes state and submit separately confirmed Hermes-native actions. It does not gain Docker, SSH, database or Pantheon write authority.

## 12. Acceptance checks

### 12.1 OpenWebUI to Hermes

From the OpenWebUI container or network namespace:

```text
GET http://hermes:8642/v1/models
Authorization: Bearer <HERMES_API_SERVER_KEY>
```

Expected:

```text
HTTP 200
hermes-agent model visible
```

### 12.2 Host exposure

Verify:

```text
8642 not published on the host
5432 not published on the host
SearXNG not published on the host
```

### 12.3 Pantheon consultation

Expected consultation indicators:

```text
contract=pantheon.consultation.v1
authority_effect=none
external_action_authorized=false
```

### 12.4 Fail-closed architecture topic

Call `explain_architecture` with an unallowlisted value such as `../../etc/passwd`.

Expected:

```text
result=unknown_topic
first_limit=No free-path repository read or invented architecture explanation.
authority_effect=none
write_effect=false
```

### 12.5 Contradictory capability status

Provide a caller-supplied status containing:

```text
detected=false + installed=true
configured=false + enabled=true
detected=false + reachable=true
```

Expected:

```text
result=invalid
use_posture=blocked_invalid_candidate
authorization_effect=none
runtime_probe_performed=false
problem_count=3
```

### 12.6 Native API toolsets

Verify that no sensitive native Hermes API toolset is enabled.

Do not interpret the absence of a dynamic MCP server from the static `/v1/toolsets` list as proof that the MCP is unavailable. The real OpenWebUI MCP call is the functional test.

### 12.7 Data and service checks

Observe:

```text
PostgreSQL internal readiness
pgvector extension version
SearXNG internal readiness
Docling executable/service version
embedding model identity and dimension
backup presence
rollback target
```

```text
readiness observed != safe use
version visible != update authorized
backup present != restore verified
```

## 13. Rollback

Before changing a working installation, retain:

```text
previous Hermes configuration
previous MCP executable path
previous pinned Pantheon checkout
previous container image references
PostgreSQL backup
OpenWebUI database backup
operator notes for network and port changes
```

Rollback order:

```text
disable the new MCP or plugin
restore the previous Hermes configuration
restart or recreate only the affected container
verify OpenWebUI -> Hermes model listing
verify the previous MCP consultation
preserve failed-install logs as technical trace
```

Do not delete a database volume as part of routine rollback.

## 14. Responsibility map

```text
Pantheon governs:
  baseline definition, status distinctions, gates, evidence expectations,
  exposure posture, acceptance criteria and rollback visibility

Hermes executes:
  model calls and later reviewed search, ingestion or retrieval bindings

OpenWebUI exposes:
  user interaction and candidate results

Human approves:
  installation, paths, secrets, bindings, public exposure, updates and rollback

Forbidden:
  hidden bootstrap, arbitrary dashboard shell, silent activation, secret retention,
  direct source-to-evidence promotion and automatic task authorization
```
