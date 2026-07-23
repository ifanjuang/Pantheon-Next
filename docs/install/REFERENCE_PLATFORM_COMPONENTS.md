# Reference Platform Components — Operator Guide

Status: candidate support note — operator installation guide — documented non-implemented.
Boundary profile: candidate_support_note.

This guide records how an operator may prepare the external technical platform used around Pantheon Next.

It is not a universal installer, Docker stack, Portainer template, secret store, update service or production authorization. Commands are reviewable operator candidates. The human selects versions, paths, credentials, exposure and rollback posture before running them.

```text
Pantheon governs the baseline, status distinctions and activation gates.
The human or infrastructure tooling installs and maintains the services.
Hermes executes.
OpenWebUI exposes.
The external services remain independently operated.
```

## 1. Scope and posture

The reference platform is divided into two groups.

### Required foundation

```text
container runtime
private user-defined container network, normally ai-net
persistent storage
backup and rollback posture
Hermes Agent
OpenWebUI
PostgreSQL with pgvector available
Pantheon MVP Cockpit when the external candidate is selected
Pantheon policy service or MCP binding when the governed consultation path is selected
```

### Conditional services

Install only when a reviewed capability binding needs them:

```text
Ollama or another local model runtime
embedding service
SearXNG
Chromium / Browserless
Docling
OCR adapters such as PaddleOCR, olmOCR or vision-model extraction
observability
external runtime memory
```

```text
required foundation != every service installed
service installed != binding selected
binding selected != dependency adopted
healthy != safe
configured != task-authorized
```

## 2. Operator record

Record these values outside the repository before installation:

```text
TARGET_HOST
HOST_OS_AND_ARCHITECTURE
CONTAINER_RUNTIME_VERSION
PRIVATE_CONTAINER_NETWORK
CONTAINER_DATA_ROOT
BACKUP_TARGET
ROLLBACK_TARGET
SELECTED_COMPONENTS
PINNED_IMAGE_TAGS_OR_DIGESTS
PUBLISHED_PORTS
INTERNAL_SERVICE_NAMES
SECRET_OWNER
SECRET_STORAGE_LOCATION
GPU_RUNTIME_AND_DRIVER
MODEL_PROVIDER_AND_MODEL
EMBEDDING_MODEL_AND_DIMENSION
```

Do not commit real API keys, passwords, tokens, private paths or unredacted environment files.

## 3. Common component record

Each installed service should have one operator record:

```yaml
component_installation_record:
  component:
  purpose:
  required_for_selected_binding: true | false
  source:
  version_or_image_digest:
  installation_status: not_checked | absent | installed | configured | enabled
  reachability: not_checked | reachable | unreachable | partial
  health_observation: not_checked | observed_ready | degraded | failed | unknown
  internal_service_name:
  internal_port:
  published_port:
  persistent_paths:
  secret_owner:
  backup_reference:
  rollback_reference:
  update_available: false | true | unknown
  update_authorized: false
  activation_status: inactive | sandbox | project | blocked | to_verify
  evidence_refs:
```

This is a status record, not a deployment manifest.

## 4. Private Docker network — `ai-net`

Official references:

- <https://docs.docker.com/reference/cli/docker/network/create/>
- <https://docs.docker.com/engine/network/drivers/bridge/>

Use a user-defined bridge network so containers can resolve one another by service name. Do not rely on the default bridge network for the reference platform.

Command Candidate — not executed by Pantheon. Review before running:

```bash
docker network inspect ai-net >/dev/null 2>&1 \
  || docker network create --driver bridge ai-net
```

Expected observation:

```bash
docker network inspect ai-net
```

The exact subnet and gateway remain operator decisions. Do not hard-code a subnet already used by another Docker network, VPN or LAN.

Default rule:

```text
container-to-container service port -> internal ai-net only
host-published port -> explicit operator decision
public exposure -> separate security and approval review
```

## 5. PostgreSQL with pgvector

Official references:

- <https://github.com/pgvector/pgvector>
- <https://github.com/pgvector/pgvector#docker>

Use an official pgvector image with a reviewed PostgreSQL major version and a pinned tag or digest. Avoid an unreviewed floating tag for a maintained installation.

Illustrative Compose fragment — adapt and review:

```yaml
services:
  postgres:
    image: pgvector/pgvector:<PINNED_PG_TAG>
    restart: unless-stopped
    environment:
      POSTGRES_USER: postgres_admin
      POSTGRES_PASSWORD: ${POSTGRES_ADMIN_PASSWORD}
    volumes:
      - <POSTGRES_DATA_PATH>:/var/lib/postgresql/data
    networks:
      - ai-net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres_admin"]
      interval: 10s
      timeout: 5s
      retries: 10

networks:
  ai-net:
    external: true
```

Do not publish port `5432` by default.

Create separate databases and limited roles for distinct responsibilities. At minimum:

```text
openwebui_app
  OpenWebUI application data

pantheon_knowledge
  source references, extraction provenance, chunks, embeddings and quality metadata
```

Enable pgvector administratively in the database that needs it:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Checks:

```sql
SELECT version();
SELECT extversion FROM pg_extension WHERE extname = 'vector';
```

```text
extension available != indexing binding activated
vector table exists != retrieval quality established
indexed != evidence
```

## 6. Ollama — conditional local model runtime

Official references:

- <https://docs.ollama.com/docker>
- <https://docs.ollama.com/api/introduction>

Ollama is optional. It is not required when Hermes uses another approved local or remote model provider.

Illustrative Compose fragment:

```yaml
services:
  ollama:
    image: ollama/ollama:<PINNED_TAG_OR_DIGEST>
    restart: unless-stopped
    volumes:
      - <OLLAMA_DATA_PATH>:/root/.ollama
    networks:
      - ai-net
    # Add the GPU configuration appropriate to the host only after review.

networks:
  ai-net:
    external: true
```

Default internal endpoint:

```text
http://ollama:11434
```

Do not publish `11434` unless a host client genuinely requires it.

Model download remains an explicit operator action because it affects storage, network use, licensing, hardware load and the model capability passport.

Command Candidate:

```bash
docker exec -it ollama ollama pull <REVIEWED_MODEL>
```

Checks:

```bash
docker exec ollama ollama list
curl -fsS http://ollama:11434/api/tags
```

```text
model downloaded != model approved
model reachable != suitable for the task
larger model != better professional result
```

## 7. Hermes Agent

Official references:

- <https://github.com/NousResearch/hermes-agent>
- <https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/docker.md>
- <https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/api-server.md>

For the reference container layout, Hermes persists its data under `/opt/data`. Do not run two Hermes gateway containers against the same data directory.

Illustrative Compose fragment:

```yaml
services:
  hermes:
    image: nousresearch/hermes-agent:<PINNED_TAG_OR_DIGEST>
    command: gateway run
    restart: unless-stopped
    environment:
      API_SERVER_ENABLED: "true"
      API_SERVER_HOST: "0.0.0.0"
      API_SERVER_PORT: "8642"
      API_SERVER_KEY: ${HERMES_API_SERVER_KEY}
      HERMES_DASHBOARD: "1"
    volumes:
      - <HERMES_DATA_PATH>:/opt/data
    networks:
      - ai-net

networks:
  ai-net:
    external: true
```

The API key must be strong and held outside the repository. The dashboard and any LAN/VPN exposure are separate operator decisions.

Default posture:

```text
Hermes API 8642 -> ai-net only
Hermes dashboard -> LAN/VPN only when explicitly selected
browser CORS -> not required for server-to-server OpenWebUI connection
Pantheon checkout -> read-only when mounted
Docker socket -> not mounted
host SSH credentials -> not mounted
```

Checks:

```bash
curl -fsS http://hermes:8642/health
curl -fsS \
  -H "Authorization: Bearer ${HERMES_API_SERVER_KEY}" \
  http://hermes:8642/v1/models
```

The API server is the Hermes runtime location. Tools invoked through OpenWebUI execute on the Hermes API-server host, not on the user device.

## 8. OpenWebUI

Official references:

- <https://docs.openwebui.com/getting-started/quick-start/>
- <https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/hermes-agent/>
- <https://docs.openwebui.com/reference/env-configuration/>

Illustrative Compose fragment:

```yaml
services:
  openwebui:
    image: ghcr.io/open-webui/open-webui:<PINNED_TAG_OR_DIGEST>
    restart: unless-stopped
    environment:
      OPENAI_API_BASE_URL: http://hermes:8642/v1
      OPENAI_API_KEY: ${HERMES_API_SERVER_KEY}
      ENABLE_OLLAMA_API: "false"
      WEBUI_SECRET_KEY: ${OPENWEBUI_SECRET_KEY}
      DATABASE_URL: postgresql://openwebui_app:${OPENWEBUI_DB_PASSWORD}@postgres:5432/openwebui_app
    volumes:
      - <OPENWEBUI_DATA_PATH>:/app/backend/data
    networks:
      - ai-net

networks:
  ai-net:
    external: true
```

Set `ENABLE_OLLAMA_API` according to whether OpenWebUI should also expose Ollama directly. The canonical governed execution path remains OpenWebUI to Hermes.

Important persistence rule:

```text
OpenWebUI connection environment variables may initialize the first launch.
After the connection is persisted in OpenWebUI's database, later changes may need
Admin Settings -> Connections rather than only changing the container environment.
```

Checks:

```text
OpenWebUI loads
Hermes connection URL includes /v1
connection key equals Hermes API_SERVER_KEY
Hermes model appears in the model list
one bounded test conversation succeeds
```

A successful OpenWebUI connection test establishes connectivity only. It does not prove model discovery, tool posture, governance enforcement or professional correctness.

## 9. SearXNG — conditional search service

Official references:

- <https://docs.searxng.org/admin/installation.html>
- <https://docs.searxng.org/admin/installation-docker>

The official documentation recommends the container installation or installation script for most deployments. For this reference platform, prefer the official container/Compose method, reviewed and pinned by the operator.

Expected service posture:

```text
service name: searxng
internal port: 8080 unless changed in the selected configuration
host publication: none by default
configuration: persisted settings.yml and related files
optional Valkey: only when the selected SearXNG features require it
```

Do not assume the retired `searxng-docker` repository layout is the current canonical template. Review the current official container template before each planned update.

Checks:

```bash
curl -fsS http://searxng:8080/
docker compose logs --tail=100 searxng
```

Bindings remain separate decisions:

```text
SearXNG -> Hermes search
SearXNG -> OpenWebUI web search
```

Neither binding is activated merely because the service is installed.

## 10. Chromium / Browserless — conditional browser runtime

Official references:

- <https://docs.browserless.io/enterprise/open-source>
- <https://docs.browserless.io/enterprise/docker/config>

For a self-hosted open-source Chromium service, Browserless publishes the official image:

```text
ghcr.io/browserless/chromium
```

Illustrative Compose fragment:

```yaml
services:
  browserless:
    image: ghcr.io/browserless/chromium:<PINNED_VERSION>
    restart: unless-stopped
    environment:
      TOKEN: ${BROWSERLESS_TOKEN}
      CONCURRENT: "2"
      HEALTH: "true"
      MAX_CPU_PERCENT: "80"
      MAX_MEMORY_PERCENT: "80"
    networks:
      - ai-net

networks:
  ai-net:
    external: true
```

Browserless requires a token. Keep it outside the repository. Do not publish port `3000` by default; use the internal address from an approved adapter:

```text
http://browserless:3000
```

Only persist browser user data when a reviewed workflow requires session continuity. Shared cookies, cache and authenticated profiles materially increase exposure and require a dedicated secret and scope review.

Checks:

```text
container running
health/pressure endpoint reachable according to the selected version
invalid or missing token refused
concurrency limit observed
no public port unless explicitly approved
```

```text
browser reachable != browser use authorized
page fetched != evidence
browser session authenticated != source admitted
```

## 11. Docling and OCR — conditional document extraction

Docling, OCR engines and vision models are external extraction adapters. Their detailed binding selection remains separate from this installation guide.

Initial posture:

```text
service may be installed
binding remains disabled
exact versions and model weights are recorded
original source remains outside the derived store
failed or partial extraction remains visible
extracted text remains derived content
```

```text
parsed != validated
OCR confidence != professional truth
chunked != evidence
```

Use the specific extraction-adapter documents and capability passports before activating a binding.

## 12. Recommended installation order

```text
1. Record host, storage, backup, network and secret decisions.
2. Install or verify the container runtime.
3. Create and inspect ai-net.
4. Install PostgreSQL/pgvector and create separated databases/roles.
5. Install the selected model provider, such as Ollama, only if required.
6. Install Hermes and verify its authenticated API.
7. Install OpenWebUI and connect it to Hermes.
8. Install Pantheon policy and cockpit candidates according to their own reviewed runbooks.
9. Install SearXNG, Browserless, Docling, OCR or other conditional services only when a selected binding requires them.
10. Run acceptance checks and record observed status.
11. Keep activation and production-use decisions separate.
```

## 13. Update discipline

Before an update:

```text
read upstream release and migration notes
record current image digest and configuration digest
verify backup and rollback target
classify changed surfaces
review data, tool, browser, memory and external-effect consequences
obtain human update authorization
```

After an update:

```text
observe version
observe reachability and health
verify expected connections
verify that no additional port or tool surface appeared
preserve logs and changed digests
keep activation status unchanged until reviewed
```

```text
update_available != update_authorized
container_recreated != migration_verified
health_check_passed != safe
```

## 14. Rollback minimum

Retain before any material change:

```text
previous image tag or digest
previous configuration snapshot with secrets protected
previous database backup or storage snapshot
previous connection settings
previous service and network inventory
operator rollback command or procedure
```

Do not delete persistent volumes during an ordinary rollback. Database migrations and model-store changes require component-specific rollback review.

## 15. Responsibility boundary

```text
exposed_by:
  OpenWebUI, Hermes dashboard, Pantheon cockpit cards and operator documentation.

executed_by:
  Human operator, Docker/Portainer/vendor tooling and the installed external services.

governed_by:
  Pantheon baseline, capability placement, status distinctions, activation gates,
  update authorization, exposure review, evidence expectations and rollback visibility.

approved_by:
  Human for installation, secrets, port exposure, provider/model selection,
  binding activation, updates, production use and rollback.

forbidden:
  Pantheon as universal installer, Docker controller, shell runner, secret store,
  provider router, plugin manager, automatic updater or health-to-safety oracle.
```

## 16. Current repository status

```text
this guide                         -> implemented as documentation
universal installation stack       -> intentionally absent
component installation             -> external / to verify per host
component reachability and health   -> external observations
binding activation                  -> documented non-implemented unless separately shown
cockpit configuration assistance    -> owned by COCKPIT_RUNTIME_CONFIGURATION_ASSISTANCE.md
```
