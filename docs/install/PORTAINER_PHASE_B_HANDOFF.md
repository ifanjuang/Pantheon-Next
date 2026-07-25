# Portainer Phase B — Operator Handoff

Status: candidate operator artifact — external composition implemented / target deployment not established.
Boundary profile: candidate_support_note.

This handoff specializes `PLATFORM_PHASE_B_DEPLOYMENT_RUNBOOK.md` for an operator-managed Docker/Portainer environment with an existing OpenWebUI installation.

It documents composition and acceptance. It executes nothing, stores no secret, changes no host, authorizes no real dossier and does not make Pantheon an installer or Portainer controller.

```text
OpenWebUI exposes.
Hermes executes.
Paperless stores document sources.
Docling derives structure.
Pantheon governs status, policy and gates.
The human/operator deploys and decides activation.
```

## 1. Current implementation references

Governance repository:

```text
ifanjuang/Pantheon-Next
policy container candidate: compose.policy-api.yaml
```

External runtime repository:

```text
ifanjuang/pantheon-mvp
Phase B composition: compose.phase-b.yaml
network-native observer: mvp_vertical.document_runtime_network_observer
external implementation: merged in pantheon-mvp #76
```

```text
implementation merged != target deployed
```

## 2. Additive deployment rule

The reference deployment uses two separately owned stacks on one private external Docker network.

```text
Stack A — Pantheon policy
  pantheon-policy-api

Stack B — external execution/document runtime
  pgvector
  Docling
  Paperless broker
  Paperless database
  Paperless-ngx
  Paperless gateway
  Cockpit API
  Hermes Agent
  document-runtime observer
```

Existing services such as OpenWebUI and SearXNG are not recreated merely because the Phase B stack is added.

Attach the existing OpenWebUI service to the same private network when the operator is ready to connect it to Hermes.

## 3. Private network

Reference network name:

```text
ai-net
```

Operator command candidate:

```bash
docker network inspect ai-net >/dev/null 2>&1 \
  || docker network create --driver bridge ai-net
```

Portainer may create the equivalent externally managed bridge network.

The subnet/gateway remain operator decisions. Do not hard-code a range that may conflict with the LAN, VPN or another Docker network.

Default exposure rule:

```text
container-to-container port -> ai-net only
host-published port          -> explicit operator decision
public exposure              -> separate review
```

## 4. Stack A — Pantheon policy

Deploy the reviewed Pantheon Next checkout using:

```text
compose.policy-api.yaml
```

Required operator secret:

```text
PANTHEON_POLICY_API_KEY
```

Expected internal endpoint:

```text
http://pantheon-policy-api:8000
```

The reference compose publishes no host port.

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

When authenticated human-issuer proof is selected, provision the reviewed read-only issuer registry through operator tooling as documented in the main Phase B runbook. Do not copy raw issuer keys into this repository.

## 5. Stack B — external runtime

Deploy `compose.phase-b.yaml` from a reviewed/pinned `pantheon-mvp` commit.

The external composition requires reviewed image references for:

```text
pgvector/PostgreSQL
Docling Serve
Paperless broker
Paperless PostgreSQL
Paperless-ngx
Hermes Agent
```

It builds the bounded MVP gateway/Cockpit/observer image from the reviewed checkout.

The reference composition intentionally publishes no host port for:

```text
MVP PostgreSQL
Docling
Paperless broker/database
Paperless gateway
Cockpit API
Hermes API
document-runtime observer
```

Paperless alone retains a bootstrap/admin host binding candidate, loopback by default. Any LAN or reverse-proxy exposure is a separate operator decision.

## 6. Persistent paths and backup

Choose host/NAS paths outside the repositories for:

```text
MVP PostgreSQL data
Paperless broker data
Paperless PostgreSQL data
Paperless data
Paperless media
Paperless consume
Paperless export
Hermes /opt/data
read-only project/document root when used
```

Do not commit private host paths.

Backup scope must include the corresponding database and source-media state. A Paperless database backup without the Paperless media files is not a complete document recovery set.

## 7. Secret ownership

Operator-owned runtime secrets include at minimum:

```text
MVP database password / DSN
Paperless database password
Paperless secret key
Pantheon policy API key
Cockpit read key
Hermes gateway key
Hermes API-server key
```

A dedicated Paperless API token is added after native Paperless bootstrap.

Secret placement remains external to Pantheon doctrine.

### Secret boundary

Cockpit does not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
issuer signing material
```

Hermes does not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
Paperless database password
issuer signing material
```

The server-side Paperless gateway owns the Paperless/PDP credentials needed by that binding.

The network observer may hold the read credentials needed for its bounded server-to-server probes, but its response never projects those credentials.

## 8. Paperless bootstrap

Start Paperless with its private database and broker.

Create the initial administrator and a dedicated API identity/token using the reviewed native Paperless procedure.

Then inject:

```text
PAPERLESS_API_TOKEN=<dedicated-runtime-token>
```

into the server-side Paperless gateway and recreate/redeploy that gateway.

The token must not be placed in OpenWebUI, the Hermes skill or the Cockpit configuration.

## 9. Hermes API and skill inventory

The reference Hermes container enables its authenticated internal API server:

```text
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0
API_SERVER_PORT=8642
API_SERVER_KEY=<external-secret>
```

Hermes provider/model configuration remains operator-owned in its persisted runtime profile.

Install the complete `pantheon-document-intake` skill package through native Hermes tooling from a reviewed commit-pinned source.

For the reference multi-container deployment, the preferred inventory observation is now:

```text
GET http://hermes:8642/v1/skills
Authorization: Bearer <HERMES_API_SERVER_KEY>
```

The bounded network observer uses this read-only surface. CLI co-location is no longer required for the reference Portainer layout.

```text
skill listed != capability approved
skill listed != task authorized
```

## 10. Connect the existing OpenWebUI

After the existing OpenWebUI container is attached to `ai-net`, configure the selected OpenAI-compatible connection to Hermes:

```text
base URL: http://hermes:8642/v1
API key:  HERMES_API_SERVER_KEY
```

This is a server-to-server connection. Do not expose the Hermes API host port merely to make OpenWebUI reach it.

Do not give OpenWebUI:

```text
Paperless API token
Pantheon policy API key
MVP Hermes gateway key
issuer signing material
administrative PostgreSQL credentials
```

Existing OpenWebUI application storage remains separate from the MVP/Agency Data/Knowledge store.

## 11. Network-native observer

The external observer reads four independent sources:

```text
Paperless gateway /health
Pantheon PDP /readyz + /v1/meta
Docling /health
Hermes /v1/skills
```

Observer endpoint:

```text
GET http://document-runtime-observer:8083/v1/document-runtime/observations
Authorization: Bearer <MVP_COCKPIT_API_KEY>
```

Expected aggregate semantics:

```text
synthetic_global_health = not_computed
authority_effect = none
write_effect = false
activation_changed = false
```

No observation may infer safety, approval or activation.

## 12. Acceptance order

Use this order so failures stay attributable to their owner:

```text
1. ai-net exists
2. Pantheon PDP livez/readyz/meta observed
3. MVP PostgreSQL ready
4. Paperless DB/broker/Paperless reachable
5. dedicated Paperless API token created
6. Paperless gateway reachable
7. Docling health endpoint reachable
8. Hermes /v1/models reachable with API key
9. Hermes /v1/skills lists pantheon-document-intake
10. document-runtime observer returns four source observations
11. existing OpenWebUI lists the selected Hermes model
12. synthetic exact-version document acceptance
13. optional signed-issuer synthetic proof
```

A failure at one source is diagnosed at that source. Do not silently bypass a failed PDP or substitute an undeclared source runtime.

## 13. Synthetic acceptance

Use only a synthetic/non-client source and the operator helper documented by the external runtime.

The synthetic receipt remains technical trace:

```text
technical_receipt_is_evidence = false
production_authorization = false
activation_changed = false
```

Authenticated issuer proof, when requested, is separate from effect authorization:

```text
issuer_authenticated != approval
valid decision verdict != effect authorized
```

Current PDP V0 external/canonical effect denial remains authoritative.

## 14. Rollback

Rollback remains operator-owned:

```text
disconnect existing OpenWebUI from Hermes connection if needed
disable/remove the Hermes skill binding
disable/remove Paperless gateway binding
stop Stack B without deleting persistent volumes/paths
stop Stack A if policy service rollback is required
restore reviewed database/media/runtime backups as applicable
```

Do not delete governed records merely because a runtime is rolled back.

## 15. Maximum justified state after deployment checks

After successful deployment and technical acceptance only:

```text
installed                  -> may be observed per component
reachable                  -> may be observed per source
health                     -> only where a dedicated health signal supports it
Hermes skill listed        -> may be observed through /v1/skills
PDP readiness              -> may be observed
approved                   -> not implied
binding activated          -> not implied
real-dossier authorization -> not implied
production adoption        -> not implied
```

```text
installed != approved
healthy != safe
runtime success != Evidence
synthetic pass != production adoption
```
