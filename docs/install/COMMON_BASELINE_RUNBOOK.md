# Common Installation Baseline — Manual Runbook

Status: candidate operator runbook — documented non-implemented; no automatic installer.

This runbook prepares the common baseline through SSH, Docker Compose, Portainer or equivalent operator tooling. Hermes Agent and OpenWebUI may be installed manually before Pantheon integration.

It executes nothing, stores no secret and does not authorize production use.

Read first:

```text
docs/governance/COMMON_INSTALLATION_BASELINE.md
docs/governance/BOOTSTRAP_INSTALLATION_LADDER.md
templates/hermes/connection/pantheon_policy_mcp.template.yaml
templates/openwebui/pantheon_common.env.template
```

## 1. Record operator decisions

Keep these values outside the repository:

```text
TARGET_HOST
HERMES_CONTAINER
OPENWEBUI_CONTAINER
CONTAINER_DATA_ROOT
PRIVATE_CONTAINER_NETWORK
PANTHEON_COMMIT
PANTHEON_VERSION
PINNED_CONTAINER_IMAGES
MODEL_PROVIDER_AND_MODEL
EMBEDDING_PROVIDER_MODEL_AND_DIMENSION
HERMES_API_SERVER_KEY
OPENWEBUI_SECRET_KEY
DATABASE_PASSWORDS
BACKUP_TARGET
ROLLBACK_TARGET
```

Do not treat a local path such as `/volume3/docker` as a portable default.

## 2. Bootstrap manually

Before Hermes exists:

```text
human / SSH / Portainer / Docker Compose installs
Hermes cannot install Hermes
OpenWebUI cannot configure an unavailable Hermes API
Pantheon provides plans and checks only
```

The operator establishes:

```text
administrative access
container runtime
private container network
persistent storage
backup or snapshot posture
Hermes
OpenWebUI
PostgreSQL with pgvector support
embedding service
Docling
SearXNG
```

Installation sources, image digests and versions must be reviewed and recorded.

## 3. Network and exposure

Expected internal service names:

```text
hermes
openwebui
postgres
searxng
```

Default host-port posture:

```text
Hermes dashboard   -> operator-selected LAN/VPN exposure
OpenWebUI cockpit  -> operator-selected LAN/VPN exposure
Hermes API 8642    -> internal only
PostgreSQL 5432    -> internal only
SearXNG             -> internal only
```

A container-to-container connection on the private network does not require a host port.

## 4. Configure Hermes

Minimum container environment:

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

```text
OPENAI_API_KEY -> Hermes to model provider
API_SERVER_KEY -> OpenWebUI to Hermes
```

Persist the Hermes configuration directory. Do not give Hermes a write mount to the Pantheon repository.

## 5. Prepare a pinned Pantheon checkout on the host

Run on the NAS or Docker host through SSH:

```bash
export PANTHEON_COMMIT="<FULL_COMMIT_SHA>"
export PANTHEON_SHORT="$(printf '%s' "$PANTHEON_COMMIT" | cut -c1-7)"
export PANTHEON_ROOT="<CONTAINER_DATA_ROOT>/pantheon"
export PANTHEON_CHECKOUT="$PANTHEON_ROOT/pantheon-next-$PANTHEON_SHORT"

mkdir -p "$PANTHEON_ROOT"
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

Mount it in the Hermes container as read-only:

```yaml
volumes:
  - <HOST_PINNED_CHECKOUT>:/opt/pantheon-next-<COMMIT_SHORT>:ro
```

Recreate only the affected Hermes container after reviewing the stack diff.

## 6. Install the Pantheon MCP inside the Hermes container

Keep the previous working version for rollback. Run from the host, targeting the Hermes container:

```bash
docker exec -it <HERMES_CONTAINER> sh -lc '
  set -eu
  VENV=/opt/data/pantheon-mcp/<PANTHEON_VERSION>/venv
  python3 -m venv "$VENV"
  "$VENV/bin/python" -m pip install --upgrade pip
  "$VENV/bin/python" -m pip install /opt/pantheon-next-<COMMIT_SHORT>/mcp-server
  "$VENV/bin/pantheon-mcp-server" --help
'
```

Merge the reviewed fragment into the persisted Hermes configuration:

```text
templates/hermes/connection/pantheon_policy_mcp.template.yaml
```

The common MCP allowlist is:

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
parallel calls disabled
pinned read-only repository path
platform_toolsets.api_server == [pantheon-policy]
```

Do not omit the `platform_toolsets.api_server` block: without an explicit override, Hermes restores its broad native API-server toolset.

Hermes 0.18.2 may emit an `unknown name` warning because static toolset validation runs before the dynamic MCP server is registered. Treat that warning as a compatibility defect to observe, not as permission to remove the restriction. Runtime acceptance must prove both:

```text
no native Hermes API toolsets exposed
pantheon-policy callable through OpenWebUI
```

## 7. Connect OpenWebUI to Hermes

Apply the reviewed values from:

```text
templates/openwebui/pantheon_common.env.template
```

Minimum contract:

```yaml
ENABLE_OPENAI_API: "true"
OPENAI_API_BASE_URL: "http://hermes:8642/v1"
OPENAI_API_KEY: "${HERMES_API_SERVER_KEY}"
ENABLE_OPENAI_API_PASSTHROUGH: "false"
WEBUI_SECRET_KEY: "${OPENWEBUI_SECRET_KEY}"
DATABASE_URL: "postgresql://openwebui_app:${OPENWEBUI_DB_PASSWORD}@postgres:5432/openwebui_app"
```

The OpenWebUI key must equal the Hermes `API_SERVER_KEY`.

For an existing OpenWebUI installation, verify both container variables and persisted administration settings.

## 8. Separate PostgreSQL responsibilities

Minimum logical separation:

```text
openwebui_app
  role: openwebui_app
  purpose: OpenWebUI application state

pantheon_knowledge
  role: pantheon_knowledge_writer
  purpose: sources, provenance, chunks, embeddings and quality/status metadata

pantheon_knowledge_reader
  purpose: future bounded read-only consultation where approved
```

Enable `vector` in `pantheon_knowledge` with an administrative role, then use limited application roles:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Do not expose PostgreSQL publicly. Do not give Hermes an unrestricted database administrator credential.

## 9. Keep derived-service bindings default-off

Record exact versions and endpoints for:

```text
embedding service
Docling
SearXNG
```

Initial posture:

```text
service present != binding selected
SearXNG -> Hermes search          disabled until reviewed
SearXNG -> OpenWebUI web search   disabled until reviewed
Docling -> ingestion worker       disabled until reviewed
embedding -> pantheon_knowledge   disabled until model/dimension approval
OpenWebUI native canonical RAG    disabled until reviewed
Hermes direct database access     disabled
```

## 10. Install the Pantheon Modules plugin inside Hermes

Run from the host, targeting the Hermes container:

```bash
docker exec -it <HERMES_CONTAINER> \
  hermes plugins install \
  ifanjuang/Pantheon-Next/templates/hermes/dashboard-plugins/pantheon-modules \
  --no-enable
```

Review the installed files inside the persisted Hermes home, then enable explicitly:

```bash
docker exec -it <HERMES_CONTAINER> \
  hermes plugins enable pantheon-modules
```

The plugin observes Hermes and submits separately confirmed native operations. It receives no Docker, SSH, database or Pantheon write authority.

## 11. Acceptance checks

### OpenWebUI to Hermes

From the OpenWebUI container or another container on the same private network:

```text
GET http://hermes:8642/v1/models
Authorization: Bearer <HERMES_API_SERVER_KEY>
```

Expected:

```text
HTTP 200
hermes-agent visible
```

### Exposure

Expected by default:

```text
8642 not host-published
5432 not host-published
SearXNG not host-published
```

### API tool posture

Expected:

```text
native Hermes API toolsets absent
pantheon-policy dynamically available
six Pantheon tools exposed, no broader MCP tools
```

The static `/v1/toolsets` catalog may not enumerate dynamically registered MCP servers. A real Pantheon MCP call is therefore required in addition to the static inspection.

### Pantheon consultation

Expected:

```text
contract=pantheon.consultation.v1
authority_effect=none
external_action_authorized=false
```

Unknown architecture topic such as `../../etc/passwd`:

```text
result=unknown_topic
first_limit=No free-path repository read or invented architecture explanation.
authority_effect=none
write_effect=false
```

Contradictory capability status:

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

Also observe:

```text
PostgreSQL readiness
pgvector version
SearXNG version and internal readiness
Docling version
embedding model and dimension
backup presence
restore procedure
rollback target
```

```text
readiness != safe use
version visible != update authorized
backup present != restore verified
```

## 12. Rollback

Retain before change:

```text
previous Hermes configuration
previous MCP executable
previous pinned Pantheon checkout
previous image references
PostgreSQL and OpenWebUI backups
network and port notes
```

Rollback order:

```text
disable the new MCP or plugin
restore the previous Hermes configuration
restart only the affected container
verify OpenWebUI -> Hermes
verify the previous MCP consultation
preserve failure logs as technical trace
```

Do not delete a database volume during routine rollback.

## Responsibility map

```text
Pantheon governs  -> baseline, status, gates, checks and rollback visibility
Hermes executes   -> model calls and later reviewed bindings
OpenWebUI exposes -> user interaction and candidate results
Human approves    -> installation, secrets, bindings, exposure, updates, rollback
Forbidden         -> hidden bootstrap, arbitrary dashboard shell, silent activation
```
