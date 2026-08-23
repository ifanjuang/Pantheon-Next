# Phase B Portainer deployment candidate

Status: external operator artifact — implementation candidate / not deployed.

This guide is for an additive Portainer/Docker deployment around an existing OpenWebUI installation. Paperless is an optional `document_source_management` capability, not a prerequisite for governed document ingestion.

```text
Pantheon Next governs.
Hermes executes.
OpenWebUI exposes.
Local/NAS sources remain a valid governed ingestion path.
Paperless optionally manages document sources.
Docling derives structured representations when selected.
The human/operator deploys and decides activation.
```

## Deployment shapes

### Core Phase B

```text
pgvector
Docling
Cockpit API
Hermes Agent
document-runtime observer
```

Document ingestion may use the mounted read-only `MVP_DOCUMENT_ROOT` path with declared Task Contract sources, path-boundary checks, digests and the existing document pipeline.

The core Compose file is:

```text
compose.phase-b.yaml
```

It contains no Paperless service, image, storage path or required Paperless secret.

### Optional Paperless overlay

```text
compose.paperless.yaml
```

adds:

```text
paperless-broker
paperless-db
paperless
paperless-gateway
```

and augments Hermes/the observer with the Paperless-specific gateway binding.

Paperless is the preferred binding for the optional `document_source_management` slot. It adds DMS/search/version/classification convenience but does not create the document-ingestion capability itself.

```text
Paperless absent != Pantheon degraded
Paperless absent != document ingestion unavailable
Paperless installed != binding selected
binding selected != activated
```

Using a separate Compose overlay also ensures that core Compose parsing does not require Paperless-only `${VAR:?…}` values when the capability is unselected.

## Existing services remain in place

Do not create a second OpenWebUI or SearXNG. Attach the existing OpenWebUI service to external `ai-net` when connecting it to Hermes.

```text
Hermes API    http://hermes:8642/v1
Cockpit API   http://cockpit-api:8081
Observer      http://document-runtime-observer:8083
```

Existing OpenWebUI application storage remains separate from the MVP/Agency Data/Knowledge store.

## Private network

Create or verify one external bridge network:

```bash
docker network inspect ai-net >/dev/null 2>&1 \
  || docker network create --driver bridge ai-net
```

Do not hard-code a subnet that may collide with LAN/VPN addressing.

## Deploy Pantheon policy first

Deploy `compose.policy-api.yaml` from the reviewed Pantheon Next checkout.

Required secret:

```text
PANTHEON_POLICY_API_KEY
```

Acceptance from `ai-net`:

```bash
curl -fsS http://pantheon-policy-api:8000/livez
curl -fsS http://pantheon-policy-api:8000/readyz
curl -fsS \
  -H "Authorization: Bearer $PANTHEON_POLICY_API_KEY" \
  http://pantheon-policy-api:8000/v1/meta
```

```text
ready != safe
PDP reachable != effect authorized
```

## Core persistent inputs

Required core paths/secrets include:

```text
MVP_PG_DATA_PATH
HERMES_DATA_PATH
MVP_DOCUMENT_ROOT
MVP_PG_PASSWORD
MVP_PG_DSN
PANTHEON_POLICY_API_KEY
MVP_COCKPIT_API_KEY
HERMES_API_SERVER_KEY
```

Required reviewed core images:

```text
MVP_PGVECTOR_IMAGE
DOCLING_IMAGE
HERMES_IMAGE
```

These are operator/deployment inputs and must not be committed.

## Start core Phase B

```bash
docker compose -f compose.phase-b.yaml up -d
```

No Paperless variable is required by this command.

Core acceptance:

```text
MVP PostgreSQL ready
Docling reachable when selected
Hermes /v1/models reachable
Cockpit API reachable internally
observer reachable
local/NAS declared-source ingestion path available
```

The core observer defaults to:

```text
MVP_DOCUMENT_SOURCE_BINDING=governed_local_source
```

## Enable optional Paperless capability

Only when the operator selects:

```text
document_source_management -> paperless_ngx
```

provide the Paperless-specific image/path/secret inputs required by `compose.paperless.yaml`, including:

```text
PAPERLESS_BROKER_IMAGE
PAPERLESS_DB_IMAGE
PAPERLESS_IMAGE
PAPERLESS_BROKER_DATA_PATH
PAPERLESS_DB_DATA_PATH
PAPERLESS_DATA_PATH
PAPERLESS_MEDIA_PATH
PAPERLESS_CONSUME_PATH
PAPERLESS_EXPORT_PATH
PAPERLESS_DB_PASSWORD
PAPERLESS_SECRET_KEY
MVP_HERMES_API_KEY
```

Then start the core plus overlay:

```bash
docker compose \
  -f compose.phase-b.yaml \
  -f compose.paperless.yaml \
  up -d
```

The overlay sets:

```text
MVP_DOCUMENT_SOURCE_BINDING=paperless_ngx
PANTHEON_PAPERLESS_GATEWAY_URL=http://paperless-gateway:8082
```

for the observer, and adds the bounded gateway inputs to Hermes.

Bootstrap Paperless natively, create a dedicated API identity/token, then set:

```text
PAPERLESS_API_TOKEN=<dedicated-runtime-token>
```

and recreate the `paperless-gateway` service through the same two-file Compose invocation.

The raw token remains absent from OpenWebUI, Hermes and the Cockpit.

The `pantheon-document-intake` skill is installed/configured only when this Paperless binding is selected.

## Hermes

Core Hermes API:

```text
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0
API_SERVER_PORT=8642
API_SERVER_KEY=<HERMES_API_SERVER_KEY>
```

Provider/model configuration remains operator-owned.

The network observer uses the authenticated read-only inventory endpoint:

```text
GET http://hermes:8642/v1/skills
```

```text
skill listed != capability approved
skill listed != task authorized
```

## Runtime observation semantics

The observer always checks Pantheon PDP, Docling and Hermes.

Document-source behavior depends on the selected binding:

```text
MVP_DOCUMENT_SOURCE_BINDING=governed_local_source
  -> no Paperless gateway probe
  -> Paperless selection_status = not_selected
  -> installation_status = not_applicable
  -> reachability_status = not_applicable
  -> health_status = not_applicable

MVP_DOCUMENT_SOURCE_BINDING=paperless_ngx
  -> bounded Paperless gateway probe
  -> failure may be classified as unreachable/degraded for that selected binding
```

An unsupported binding yields `unsupported_binding` / `not_observed`; the observer does not guess a runtime state.

The aggregate never computes a synthetic global health value.

```text
reachable != healthy
healthy != safe
installed != approved
runtime observation != activation decision
```

## OpenWebUI connection

Attach the existing OpenWebUI container to `ai-net`, then configure:

```text
base URL: http://hermes:8642/v1
API key:  HERMES_API_SERVER_KEY
```

Do not give OpenWebUI Paperless, PDP, issuer or administrative PostgreSQL secrets.

## Acceptance order — core

```text
1. ai-net exists
2. Pantheon PDP livez/readyz/meta observed
3. MVP PostgreSQL ready
4. Docling health observed when selected
5. Hermes /v1/models reachable
6. document-runtime observer reachable
7. observer reports governed_local_source and Paperless not_selected/not_applicable
8. existing OpenWebUI lists selected Hermes model
9. synthetic/local governed document ingestion test
```

## Additional acceptance — Paperless overlay only

```text
1. Paperless DB/broker/Paperless reachable
2. dedicated Paperless API token created
3. Paperless gateway reachable
4. observer reports document_source_binding=paperless_ngx
5. Hermes /v1/skills lists pantheon-document-intake
6. exact-version Paperless synthetic intake
7. optional signed-issuer synthetic proof
```

The Paperless-specific synthetic helper remains a binding acceptance test. Its non-use when Paperless is unselected does not invalidate core local/NAS document ingestion.

## Rollback

Core rollback and Paperless rollback remain separable.

```text
Paperless overlay rollback
  return MVP_DOCUMENT_SOURCE_BINDING to governed_local_source
  redeploy core without compose.paperless.yaml
  retain Paperless persistent data for governed rollback/recovery
  keep local/NAS ingestion available

Core rollback
  disconnect OpenWebUI/Hermes connection if required
  stop external runtime services without deleting governed records
  restore reviewed database/runtime backups as applicable
```

## Maximum justified states

Core installation without Paperless may validly report:

```text
selected document source   governed_local_source
Paperless binding          not_selected
Paperless installation     not_applicable
core document ingestion    available candidate
Pantheon degraded          no implication
```

When Paperless is selected, its installation/reachability/health are observed separately.

In all cases:

```text
installed != approved
healthy != safe
runtime success != Evidence
synthetic pass != production adoption
```
