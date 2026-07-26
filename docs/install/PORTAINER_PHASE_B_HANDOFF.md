# Portainer Phase B — Operator Handoff

Status: candidate operator artifact — external composition implemented / target deployment not established.
Boundary profile: candidate_support_note.

This handoff specializes `PLATFORM_PHASE_B_DEPLOYMENT_RUNBOOK.md` for Docker/Portainer with an existing OpenWebUI installation.

It documents composition and acceptance. It executes nothing, stores no secret, changes no host, authorizes no real dossier and does not make Pantheon an installer or Portainer controller.

```text
OpenWebUI exposes.
Hermes executes.
Local/NAS source ingestion is supported in the core.
Paperless optionally manages document sources.
Docling derives structure when selected.
Pantheon governs status, policy and gates.
The human/operator deploys and decides activation.
```

## 1. Current implementation references

```text
Pantheon Next policy candidate
  compose.policy-api.yaml

external runtime
  ifanjuang/pantheon-mvp
  compose.phase-b.yaml
  optional Paperless profile merged in #84
```

```text
implementation merged != target deployed
```

## 2. Additive deployment rule

Reference core stack on private `ai-net`:

```text
Stack A — Pantheon policy
  pantheon-policy-api

Stack B — external core runtime
  pgvector
  Docling when selected
  Cockpit API
  Hermes Agent
  document-runtime observer
```

Optional Paperless capability:

```text
profile: paperless
  Paperless broker
  Paperless database
  Paperless-ngx
  Paperless gateway
```

Existing OpenWebUI/SearXNG are reused rather than recreated.

```text
Paperless absent != Pantheon degraded
Paperless absent != document ingestion unavailable
```

## 3. Private network

Reference network:

```text
ai-net
```

Operator candidate:

```bash
docker network inspect ai-net >/dev/null 2>&1 \
  || docker network create --driver bridge ai-net
```

Do not hard-code a subnet that may collide with LAN/VPN ranges.

## 4. Stack A — Pantheon policy

Deploy the reviewed Pantheon Next checkout with `compose.policy-api.yaml`.

Required operator secret:

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

## 5. Stack B — core runtime

Deploy the reviewed/pinned `pantheon-mvp` `compose.phase-b.yaml` without profiles:

```bash
docker compose -f compose.phase-b.yaml up -d
```

Core reviewed images/inputs include:

```text
MVP_PGVECTOR_IMAGE
HERMES_IMAGE
DOCLING_IMAGE when Docling is selected
MVP_PG_DATA_PATH
HERMES_DATA_PATH
MVP_DOCUMENT_ROOT
MVP_PG_PASSWORD / MVP_PG_DSN
MVP_COCKPIT_API_KEY
HERMES_API_SERVER_KEY
PANTHEON_POLICY_API_KEY
```

Core services must not publish PostgreSQL, Docling, Cockpit, Hermes or observer ports to the host by default.

`MVP_DOCUMENT_ROOT` is a read-only source root for governed local/NAS ingestion. The external runtime still applies Task Contract declared-source, resolved-path and digest checks.

## 6. Optional Paperless profile

Select Paperless only when the `document_source_management` capability is wanted.

Required profile-specific inputs include:

```text
PAPERLESS_BROKER_IMAGE
PAPERLESS_DB_IMAGE
PAPERLESS_IMAGE
Paperless persistent data/media/export/consume paths
PAPERLESS_DB_PASSWORD
PAPERLESS_SECRET_KEY
MVP_HERMES_API_KEY
PANTHEON_PAPERLESS_BINDING_SELECTED=true
```

Start:

```bash
docker compose -f compose.phase-b.yaml --profile paperless up -d
```

Then bootstrap Paperless natively, create a dedicated API identity/token and inject:

```text
PAPERLESS_API_TOKEN=<dedicated-runtime-token>
```

into the server-side gateway.

Paperless is the preferred DMS/source-management binding, not the prerequisite for document ingestion.

## 7. Secret ownership

Core OpenWebUI does not receive:

```text
Paperless API token
Pantheon policy API key
MVP Hermes gateway key
issuer signing material
administrative PostgreSQL credentials
```

Core Hermes does not require Paperless gateway configuration.

When the Paperless binding is selected, its gateway/skill secrets remain runtime/operator configuration and do not become Pantheon secrets.

## 8. Hermes API

Reference core Hermes API:

```text
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0
API_SERVER_PORT=8642
API_SERVER_KEY=<external-secret>
```

Network inventory observation:

```text
GET http://hermes:8642/v1/skills
Authorization: Bearer <HERMES_API_SERVER_KEY>
```

The Paperless-specific `pantheon-document-intake` skill is installed/configured only when that binding is selected.

```text
skill listed != capability approved
skill listed != task authorized
```

## 9. Existing OpenWebUI

Attach existing OpenWebUI to `ai-net`, then configure the reviewed Hermes connection:

```text
base URL: http://hermes:8642/v1
API key: HERMES_API_SERVER_KEY
```

No Paperless service is required for this connection.

## 10. Runtime observer

The network observer always reads the selected core observation surfaces.

Paperless is conditional:

```text
PANTHEON_PAPERLESS_BINDING_SELECTED=false
  -> Paperless gateway is not probed
  -> binding_status = not_selected
  -> installation/reachability/health = not_applicable

PANTHEON_PAPERLESS_BINDING_SELECTED=true
  -> bounded Paperless gateway observation enabled
```

Aggregate semantics remain:

```text
synthetic_global_health = not_computed
authority_effect = none
write_effect = false
activation_changed = false
```

## 11. Core acceptance order

```text
1. ai-net exists
2. Pantheon PDP livez/readyz/meta
3. MVP PostgreSQL ready
4. Docling health when selected
5. Hermes /v1/models reachable
6. document-runtime observer reachable
7. existing OpenWebUI lists selected Hermes model
8. governed local/NAS synthetic document ingestion proof
```

## 12. Additional Paperless acceptance — only when selected

```text
1. Paperless DB/broker/Paperless reachable
2. dedicated Paperless API token created
3. Paperless gateway reachable
4. observer reports binding_status=selected
5. Hermes inventory lists pantheon-document-intake
6. exact-version Paperless synthetic intake
7. optional signed-issuer synthetic proof
```

The existing Paperless synthetic helper is a binding acceptance helper. It is not the acceptance authority for the core local/NAS ingestion path.

## 13. Backup and rollback

Core backup covers governed DB/runtime state and operator-owned source storage.

Paperless-specific database/media/data/export backup is required only when Paperless is selected.

Rollback can remove/disable the Paperless profile while retaining core document ingestion:

```text
Paperless binding -> not_selected
Paperless services -> stopped
local/NAS ingestion -> remains available
```

Do not delete governed records merely because a runtime binding is rolled back.

## 14. Maximum justified state

Without Paperless:

```text
Paperless binding          not_selected
Paperless installation     not_applicable
core ingestion             available candidate
Pantheon degraded          no implication
```

With Paperless selected, its installation/reachability/health are observed separately.

In all cases:

```text
installed != approved
healthy != safe
runtime success != Evidence
synthetic pass != production adoption
```
