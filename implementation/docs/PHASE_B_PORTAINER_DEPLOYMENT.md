# Phase B Portainer deployment candidate

Status: external operator artifact — implementation candidate / not deployed.

This guide is for an additive Portainer/Docker deployment of the external Pantheon MVP runtime around an existing OpenWebUI installation. It does not replace the operator's existing OpenWebUI, SearXNG or unrelated PostgreSQL services.

It is not an installer, activation action, production authorization or proof of health.

```text
Pantheon Next governs.
Hermes executes.
OpenWebUI exposes.
Paperless stores document sources.
Docling derives structured representations.
The human/operator deploys and decides activation.
```

## 1. Two-stack boundary

Deploy two separately owned stacks on the same external Docker network:

```text
Stack A — Pantheon policy
  source: ifanjuang/Pantheon-Next
  compose: compose.policy-api.yaml
  service: pantheon-policy-api

Stack B — external execution/document runtime
  source: ifanjuang/pantheon-mvp
  compose: compose.phase-b.yaml
  services:
    pgvector
    docling
    paperless-broker
    paperless-db
    paperless
    paperless-gateway
    cockpit-api
    hermes
    document-runtime-observer
```

The split is intentional:

```text
Pantheon policy service != execution runtime
MVP runtime != governance authority
```

## 2. Existing services remain in place

Do not create a second OpenWebUI or SearXNG merely because the Phase B stack is added.

The existing OpenWebUI service should be attached to the same external `ai-net` network so it can reach:

```text
Hermes API    http://hermes:8642/v1
Cockpit API   http://cockpit-api:8081
Observer      http://document-runtime-observer:8083
```

Connecting OpenWebUI to `ai-net` does not give it Paperless, PDP, database or issuer credentials.

The existing OpenWebUI PostgreSQL database remains its own application database. The Phase B `pgvector` service is the external MVP/Agency Data/Knowledge candidate store and must not reuse unrestricted OpenWebUI credentials.

## 3. Create the external network once

Operator command candidate:

```bash
docker network inspect ai-net >/dev/null 2>&1 \
  || docker network create --driver bridge ai-net
```

In Portainer, the equivalent is an externally managed bridge network named exactly:

```text
ai-net
```

Do not hard-code a subnet that may collide with the LAN, VPN or another Docker network.

## 4. Deploy Pantheon policy first

Deploy `compose.policy-api.yaml` from a reviewed Pantheon Next commit/tag.

Required secret:

```text
PANTHEON_POLICY_API_KEY
```

Expected internal endpoint:

```text
http://pantheon-policy-api:8000
```

The policy stack publishes no host port by default.

Acceptance from a container on `ai-net`:

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

## 5. Prepare Phase B paths outside the repositories

Choose operator-owned persistent paths for:

```text
MVP_PG_DATA_PATH
PAPERLESS_BROKER_DATA_PATH
PAPERLESS_DB_DATA_PATH
PAPERLESS_DATA_PATH
PAPERLESS_MEDIA_PATH
PAPERLESS_CONSUME_PATH
PAPERLESS_EXPORT_PATH
HERMES_DATA_PATH
MVP_DOCUMENT_ROOT
```

These are deployment inputs and must not be committed to the repository.

Backup scope must include at minimum:

```text
MVP PostgreSQL data
Paperless PostgreSQL data
Paperless media/data
Hermes data/profile/skills
operator secret references
```

## 6. Required reviewed image references

Portainer environment must provide pinned/reviewed image references:

```text
MVP_PGVECTOR_IMAGE
DOCLING_IMAGE
PAPERLESS_BROKER_IMAGE
PAPERLESS_DB_IMAGE
PAPERLESS_IMAGE
HERMES_IMAGE
```

The MVP services are built from the reviewed Git checkout through the repository Dockerfile and share one local image name/tag:

```text
PANTHEON_MVP_IMAGE_NAME
PANTHEON_MVP_IMAGE_TAG
```

A floating upstream image is not equivalent to an authorized update.

```text
image available != update authorized
```

## 7. Required runtime secrets

Store values in Portainer's protected environment/secret mechanism or another operator secret store, not in Git:

```text
MVP_PG_PASSWORD
MVP_PG_DSN
PAPERLESS_DB_PASSWORD
PAPERLESS_SECRET_KEY
PANTHEON_POLICY_API_KEY
MVP_COCKPIT_API_KEY
MVP_HERMES_API_KEY
HERMES_API_SERVER_KEY
```

Initially optional/default-off:

```text
PAPERLESS_API_TOKEN
MVP_EDITOR_API_KEY
MVP_UPDATE_SIGNING_SECRET
DOCLING_SERVE_API_KEY
```

`MVP_PG_DSN` must point to the Phase B `pgvector` service and correspond to the configured database/user/password. Encode special password characters correctly in the DSN.

## 8. Deploy the Phase B stack

Use `compose.phase-b.yaml` from the reviewed `pantheon-mvp` checkout.

The deployment candidate intentionally:

- attaches every service to external `ai-net`;
- publishes no PostgreSQL, Docling, gateway, Cockpit, Hermes or observer port to the host;
- leaves only Paperless's bootstrap/admin port host-bindable, loopback by default;
- keeps the Paperless and PDP credentials server-side;
- gives Hermes only its own API-server key plus the bounded gateway key needed by the document skill;
- gives the Cockpit no raw Paperless or PDP credential.

## 9. Bootstrap Paperless, then configure the gateway token

Paperless may be temporarily reachable through:

```text
PAPERLESS_HOST_BIND
PAPERLESS_HOST_PORT
```

Default binding is loopback. A LAN binding or reverse proxy is an explicit operator decision.

Create the Paperless administrator and a dedicated API identity/token using the reviewed native Paperless procedure. Then set:

```text
PAPERLESS_API_TOKEN=<dedicated runtime token>
```

and redeploy/recreate the `paperless-gateway` service.

The raw token remains absent from OpenWebUI, Hermes skill configuration and the Cockpit.

## 10. Configure Hermes

The Compose candidate enables Hermes' authenticated API server internally:

```text
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0
API_SERVER_PORT=8642
API_SERVER_KEY=<HERMES_API_SERVER_KEY>
```

No CORS allowlist is set because the intended OpenWebUI connection is server-to-server over `ai-net`.

Hermes provider/model configuration remains operator-owned in its persisted `/opt/data` profile. A running API server without a usable provider/model is not a successful runtime acceptance.

Install the complete `pantheon-document-intake` skill from a reviewed commit-pinned `SKILL.md` URL using native Hermes tooling.

Verify through Hermes itself or the authenticated API:

```text
GET http://hermes:8642/v1/skills
```

The current network observer uses this read-only endpoint; it does not need CLI co-location.

```text
skill listed != capability approved
skill listed != task authorized
```

## 11. Network-native runtime observation

`document-runtime-observer` runs:

```text
python -m mvp_vertical.document_runtime_network_observer
```

It independently observes:

```text
Paperless gateway /health
Pantheon PDP /readyz + /v1/meta
Docling /health
Hermes /v1/skills
```

Its read endpoint is:

```text
GET http://document-runtime-observer:8083/v1/document-runtime/observations
Authorization: Bearer <MVP_COCKPIT_API_KEY>
```

The observer returns source-attributed statuses and explicitly does not compute a synthetic global health value.

```text
reachable != healthy
healthy != safe
installed != approved
PDP ready != effect authorized
runtime observation != activation decision
```

## 12. Connect existing OpenWebUI to Hermes

Once the existing OpenWebUI service is attached to `ai-net`, configure its OpenAI-compatible backend as:

```text
base URL: http://hermes:8642/v1
API key:  HERMES_API_SERVER_KEY
```

The model list check should resolve through Hermes' `/v1/models` endpoint.

Do not give OpenWebUI:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
MVP_HERMES_API_KEY
issuer signing material
PostgreSQL administrative credentials
```

## 13. Acceptance order

Perform checks in this order:

```text
1. ai-net exists
2. Pantheon PDP livez/readyz/meta
3. pgvector ready
4. Paperless DB/broker/Paperless reachable
5. dedicated Paperless API token created
6. Paperless gateway reachable
7. Docling health endpoint reachable
8. Hermes /v1/models reachable with API key
9. Hermes /v1/skills lists pantheon-document-intake
10. document-runtime-observer returns four source observations
11. existing OpenWebUI lists the Hermes model
12. synthetic exact-version document acceptance
```

A failure at one source is diagnosed at that source. Do not replace a failed Paperless path with an implicit NAS fallback and do not bypass a failed PDP.

## 14. Synthetic check

After all four independent runtime observations are present, use the existing operator helper described in `docs/SYNTHETIC_DOCUMENT_RUNTIME_CHECK.md`.

Expected boundaries remain:

```text
technical_receipt_is_evidence = false
production_authorization = false
activation_changed = false
```

Authenticated issuer proof remains optional and separately configured. The signing/PDP secrets belong to the operator helper and must not be passed to the Hermes skill process.

## 15. Resulting status

After deployment and read-only acceptance only, the maximum justified state is:

```text
installed                  observed per component
reachable                  observed per source
health                     only where a dedicated health check supports it
skill listed               observed through Hermes API
PDP policy surface         observed
approved                   not implied
binding activated          not implied
real-dossier authorization not implied
production adoption        not implied
```

This Portainer composition remains an external deployment candidate. Pantheon governs its states; it does not become the installer, Portainer controller, runtime, scheduler, queue or automatic approval engine.
