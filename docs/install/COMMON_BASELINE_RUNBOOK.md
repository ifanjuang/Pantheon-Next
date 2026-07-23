# Common Installation Baseline — Manual Runbook

Status: candidate operator runbook — documented non-implemented; no automatic installer.

This runbook prepares the common baseline through SSH, Docker Compose, Portainer or equivalent operator tooling. It executes nothing, stores no secret and does not authorize production use.

Read first:

```text
docs/governance/COMMON_INSTALLATION_BASELINE.md
docs/install/REFERENCE_PLATFORM_COMPONENTS.md
docs/governance/BOOTSTRAP_INSTALLATION_LADDER.md
docs/governance/COCKPIT_RUNTIME_CONFIGURATION_ASSISTANCE.md
templates/hermes/connection/pantheon_policy_mcp.template.yaml
templates/openwebui/pantheon_common.env.template
```

## 1. Record operator decisions

Keep these values outside the repository:

```text
TARGET_HOST
HOST_OS_AND_ARCHITECTURE
HERMES_CONTAINER
OPENWEBUI_CONTAINER
CONTAINER_DATA_ROOT
PRIVATE_CONTAINER_NETWORK
PANTHEON_COMMIT
PANTHEON_VERSION
PINNED_CONTAINER_IMAGES_OR_DIGESTS
SELECTED_CONDITIONAL_SERVICES
MODEL_PROVIDER_AND_MODEL
EMBEDDING_PROVIDER_MODEL_AND_DIMENSION
HERMES_API_SERVER_KEY
OPENWEBUI_SECRET_KEY
DATABASE_PASSWORDS
BROWSERLESS_TOKEN when selected
BACKUP_TARGET
ROLLBACK_TARGET
```

Do not promote one local path such as `/volume3/docker` into a portable default. Do not commit real `.env` files or secret values.

## 2. Bootstrap manually

Before Hermes exists, the human uses SSH, Docker Compose, Portainer or vendor tooling. Hermes cannot install itself, and OpenWebUI cannot configure an unavailable Hermes API.

Required foundation:

```text
administrative access
container runtime
private user-defined container network
persistent storage
backup or snapshot posture
Hermes
OpenWebUI
PostgreSQL with pgvector available
```

Install conditional services only when a reviewed binding needs them:

```text
Ollama or another local model runtime
embedding service
Docling
OCR adapter
SearXNG
Chromium / Browserless
observability
external runtime memory
```

Record installation sources, versions and image digests.

## 3. Create or verify `ai-net`

Command Candidate — not executed by Pantheon:

```bash
docker network inspect ai-net >/dev/null 2>&1 \
  || docker network create --driver bridge ai-net
```

Expected:

```bash
docker network inspect ai-net
```

Use another network name only when the deployment records it consistently. Check subnet conflicts before creation.

## 4. Network posture

Expected internal service names for the reference deployment:

```text
hermes
openwebui
postgres
```

Conditional service names when installed:

```text
ollama
searxng
browserless
docling
```

Default host exposure:

```text
Hermes dashboard   -> operator-selected LAN/VPN exposure
OpenWebUI cockpit  -> operator-selected LAN/VPN exposure
Hermes API 8642    -> internal only
PostgreSQL 5432    -> internal only
Ollama 11434       -> internal only when installed
SearXNG             -> internal only when installed
Browserless 3000   -> internal only when installed
```

Container-to-container traffic on the private network does not require host-port publication.

## 5. Install PostgreSQL with pgvector

Use the reviewed image and version recorded in `REFERENCE_PLATFORM_COMPONENTS.md`.

Create separate databases and roles:

```text
openwebui_app
  role: openwebui_app
  purpose: OpenWebUI application state

pantheon_knowledge
  role: pantheon_knowledge_writer
  purpose: source references, provenance, chunks, embeddings and quality metadata

pantheon_knowledge_reader
  purpose: future bounded read-only access where approved
```

Enable pgvector administratively in the selected database:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Do not publish PostgreSQL or provide Hermes with an unrestricted database administrator credential.

## 6. Install the selected model provider

A model provider is required for Hermes use, but Ollama itself is conditional.

When Ollama is selected:

```text
service endpoint -> http://ollama:11434
model download -> explicit operator action
GPU runtime -> host-specific and separately verified
host publication -> disabled by default
```

Record the model identity, size, hardware requirements and capability-passport status before activation.

```text
model downloaded != model approved
model reachable != task-authorized
```

## 7. Configure Hermes

Minimum container environment:

```yaml
API_SERVER_ENABLED: "true"
API_SERVER_HOST: "0.0.0.0"
API_SERVER_PORT: "8642"
API_SERVER_KEY: "${HERMES_API_SERVER_KEY}"
HERMES_INFERENCE_PROVIDER: "<PINNED_PROVIDER>"
HERMES_INFERENCE_MODEL: "<PINNED_MODEL>"
```

Provider-specific variables remain outside the repository.

```text
provider API key -> Hermes to the selected provider
API_SERVER_KEY   -> OpenWebUI to Hermes
```

Persist the Hermes data directory. Do not run two Hermes gateway containers against the same data directory. Do not give Hermes a write mount to the Pantheon repository, Docker socket or host SSH credentials.

## 8. Prepare a pinned Pantheon checkout

Run through SSH on the NAS or Docker host:

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

Mount the selected checkout read-only where the reviewed adapter requires it.

## 9. Install the Pantheon policy MCP in Hermes

Keep the previous working MCP for rollback.

Command Candidate:

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

Merge the reviewed fragment:

```text
templates/hermes/connection/pantheon_policy_mcp.template.yaml
```

Required posture:

```text
reviewed tool include allowlist
prompts disabled
resources disabled
sampling disabled
parallel calls disabled
pinned read-only repository path
restricted API-server toolset
```

A static warning before dynamic MCP registration is not acceptance. A real bounded Pantheon call is required.

## 10. Connect OpenWebUI

Apply the reviewed template:

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

The OpenWebUI connection key must equal the Hermes `API_SERVER_KEY`.

OpenWebUI may persist connection values in its database after first launch. For an existing installation, verify separately:

```text
container environment
Admin Settings -> Connections
actual model discovery
```

Changing environment variables alone may not change the effective connection.

## 11. Keep conditional bindings default-off

Initial posture:

```text
Ollama or selected provider -> Hermes       disabled until provider/model review
SearXNG -> Hermes search                    disabled until reviewed
SearXNG -> OpenWebUI web search             disabled until reviewed
Browserless -> Hermes browser capability    disabled until reviewed
Docling -> ingestion worker                 disabled until reviewed
OCR adapter -> extraction worker            disabled until reviewed
embedding -> pantheon_knowledge             disabled until model/dimension review
OpenWebUI native canonical RAG              disabled until reviewed
Hermes direct database access               disabled
```

```text
service present != binding selected
binding selected != dependency adopted
```

## 12. Install the Hermes dashboard plugin when selected

Command Candidate:

```bash
docker exec -it <HERMES_CONTAINER> \
  hermes plugins install \
  "file:///opt/pantheon-next-<COMMIT_SHORT>#templates/hermes/dashboard-plugins/pantheon-modules" \
  --no-enable
```

Review the copied files, then enable separately:

```bash
docker exec -it <HERMES_CONTAINER> \
  hermes plugins enable pantheon-modules
```

The plugin receives no Docker, SSH, database or Pantheon write authority. Installation and enablement are Hermes operational states only.

## 13. Acceptance checks

### Hermes API

```bash
# /health is version-dependent (classified health_probe_to_verify in the
# connection template): probe it best-effort, do not gate on it.
curl -sS http://hermes:8642/health || echo "(/health not implemented by this Hermes version — not a failure)"
# Authoritative acceptance check: the OpenAI-compatible models endpoint.
curl -fsS \
  -H "Authorization: Bearer <HERMES_API_SERVER_KEY>" \
  http://hermes:8642/v1/models
```

Expected: `/v1/models` returns HTTP 200 with the selected Hermes model visible. Treat `/health` as an optional probe: verify it only for a pinned Hermes version that documents the endpoint, never as a required gate.

### OpenWebUI to Hermes

Expected:

```text
connection URL includes /v1
saved key matches Hermes API_SERVER_KEY
Hermes model appears in the model list
one bounded test request succeeds
```

### Exposure

Expected by default:

```text
8642 not host-published
5432 not host-published
conditional service ports not host-published
```

### Pantheon consultation

Expected:

```text
contract=pantheon.consultation.v1
authority_effect=none
external_action_authorized=false
```

Unknown architecture topics and contradictory status candidates must fail closed according to the selected policy contract.

### Conditional services

For each installed conditional service, record:

```text
version or image digest
reachability
health observation
binding state
published-port state
backup or recreation posture
```

```text
readiness != safe use
backup present != restore verified
```

## 14. Cockpit configuration assistance

The cockpit may expose the configuration-assistance pattern defined in:

```text
docs/governance/COCKPIT_RUNTIME_CONFIGURATION_ASSISTANCE.md
```

Initial product posture:

```text
observe
explain
propose a diff
route to the native Hermes/OpenWebUI surface
record the human decision
verify the resulting observation
```

Direct runtime configuration mutation remains documented non-implemented and default-off.

## 15. Rollback

Retain before change:

```text
previous Hermes configuration
previous MCP executable
previous pinned Pantheon checkout
previous image references
PostgreSQL and OpenWebUI backups
conditional-service configuration snapshots
network and port notes
```

Rollback order:

```text
disable the new binding or plugin
restore the previous native configuration
restart only the affected external runtime when required
verify OpenWebUI -> Hermes
verify the previous Pantheon consultation path
verify conditional-service bindings
preserve failure logs as technical trace
```

Do not delete a database, model or application volume during routine rollback.

## 16. Responsibility map

```text
Pantheon governs  -> baseline, status, gates, checks, update and rollback visibility
Hermes executes   -> model calls and reviewed tool bindings
OpenWebUI exposes -> user interaction and candidate results
Human installs    -> infrastructure and services
Human approves    -> secrets, bindings, exposure, updates, restart and rollback
Forbidden         -> hidden bootstrap, arbitrary cockpit shell, Docker control, silent activation
```
