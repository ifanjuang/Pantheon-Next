# Platform Phase B — Deployment Runbook

Status: candidate operator artifact — documented non-implemented.
Boundary profile: candidate_support_note.

This runbook is the operator handoff for Phase B of
`docs/roadmaps/PLATFORM_IMPLEMENTATION_ROADMAP.md`: deploy the policy PDP and the
reference stack, then wire the already-implemented clients so consequential
effects really route through the chokepoint.

It documents commands; it runs none of them. It stores no secret, changes no
host and authorizes no production use. Deployment is a reviewed operator action;
adoption Gate 8 remains a separate human decision.

```text
OpenWebUI exposes.
Hermes Agent executes and enforces.
Paperless-ngx stores document sources externally.
Pantheon Next governs.
The human decides consequential effects.
```

## What already exists (do not rebuild)

```text
PDP capability             Pantheon mcp-server: preflight + validate_decision (implemented)
PDP container candidate    Dockerfile.policy-api, compose.policy-api.yaml (not activated)
PEP seam                    pantheon-mvp policy_gate: enforce_consequential (implemented)
real policy client          pantheon-mvp policy_gate.HttpPolicyClient (implemented)
capability lifecycle        pantheon-mvp capability_manager (implemented)
Paperless API adapter       pantheon-mvp paperless.PaperlessClient (implementation candidate)
Paperless internal gateway  pantheon-mvp paperless_gateway (implementation candidate)
Paperless document intake   pantheon-mvp paperless_ingestion -> existing store.ingest
Paperless Source Inbox      pantheon-mvp OpenWebUI read-only tool candidate
Paperless install runbook   docs/install/PAPERLESS_INITIAL_INSTALLATION.md
reference components        docs/install/REFERENCE_PLATFORM_COMPONENTS.md
baseline handoff            docs/install/COMMON_BASELINE_RUNBOOK.md
```

Phase B installs and connects these. It does not move Paperless workers, queues,
schedulers, document bytes or secrets into Pantheon.

## Prerequisites

```text
a Docker host the operator controls (SSH / Portainer)
the external network `ai-net` created:  docker network create ai-net
a pinned Pantheon Next checkout mounted read-only
a secret manager holding PANTHEON_POLICY_API_KEY and stack credentials
a reviewed pinned Paperless image/tag/digest
persistent Paperless database + data/media backup targets
the reference components reviewed (REFERENCE_PLATFORM_COMPONENTS.md)
```

Secrets are referenced from the operator's secret manager, never committed.

## Step 1 — Deploy the policy PDP

Bring up `pantheon-policy-api` on `ai-net` from the hardened candidate. It
publishes no host port, mounts the repository read-only, drops capabilities and
receives no Docker socket.

```bash
export PANTHEON_POLICY_API_KEY="$(op read op://pantheon/policy-api/key)"   # example
docker compose -f compose.policy-api.yaml up -d
```

Acceptance (from another container on `ai-net`; the API has no host port):

```bash
curl -fsS http://pantheon-policy-api:8000/livez
curl -fsS http://pantheon-policy-api:8000/readyz
curl -fsS -H "Authorization: Bearer $PANTHEON_POLICY_API_KEY" \
  http://pantheon-policy-api:8000/v1/meta
```

`readyz` confirms the checkout is readable; it does not establish safety
(`ready != safe`).

## Step 2 — Deploy the reference stack

Deploy the components of `REFERENCE_PLATFORM_COMPONENTS.md` on `ai-net`, each
pinned: PostgreSQL/pgvector, Paperless-ngx with its private broker, Ollama,
Hermes Agent 0.19, OpenWebUI, SearXNG, Browserless/Chromium and any conditional
document-analysis/extraction service a reviewed binding selects.

Follow `COMMON_BASELINE_RUNBOOK.md` for the SSH/Docker/Portainer handoff, and
its acceptance checks. Treat `/health` as an optional, version-guarded probe and
`GET /v1/models` as the authoritative Hermes check.

Paperless is installed as source-management infrastructure; Docling remains a
separate document-analysis binding.

```text
Paperless installed != Paperless binding activated
Paperless OCR != validated extraction
Paperless task success != Evidence
```

## Step 3 — Configure and verify Paperless

Follow `docs/install/PAPERLESS_INITIAL_INSTALLATION.md`.

Required retained observations:

```text
reviewed image tag/digest
private network endpoint
separate database role/database or dedicated DB instance
persistent data/media paths
backup + restore target
broker private to Paperless
API identity/token secret owner
Paperless AI/remote OCR unconfigured unless separately reviewed
```

Create a dedicated Paperless API token outside the repository and inject only a
secret reference/value into the external runtime environment:

```text
PAPERLESS_API_URL=http://paperless:8000
PAPERLESS_API_TOKEN=<external-secret>
```

Read-only acceptance:

```bash
curl -fsS \
  -H "Authorization: Token $PAPERLESS_API_TOKEN" \
  "http://paperless:8000/api/documents/?page_size=1"
```

Then perform the synthetic exact-version Source Capture check from the Paperless
runbook. A mutable `latest` pointer is insufficient for immutable intake.

## Step 4 — Configure the Hermes Policy Enforcement Point

On the Hermes host, adapt the connection blueprint
`templates/hermes/connection/pantheon_policy_http.template.yaml`:

```text
base_url: http://pantheon-policy-api:8000
api_key_env: PANTHEON_POLICY_API_KEY
consequential_unavailable: fail_closed
always_block_effects_when_false: [external_effect_allowed, canonical_effect_allowed]
```

Required for Hermes 0.19 (see `HERMES_INTEGRATION.md`, Hermes 0.19 review):
**disable smart-approvals for consequential effects** so an in-runtime model
review never substitutes for the human gate. Re-verify the MCP tool names
(`mcp__server__tool`) and the `platform_toolsets.api_server` restriction against
the observed 0.19 install before enabling.

## Step 5 — Deploy the bounded Paperless gateway

The Cockpit and OpenWebUI should not receive the raw Paperless API token.
Deploy the external `pantheon-mvp` Paperless gateway on the private network with:

```text
PAPERLESS_API_URL=http://paperless:8000
PAPERLESS_API_TOKEN=<external-secret>
PANTHEON_POLICY_API_URL=http://pantheon-policy-api:8000
PANTHEON_POLICY_API_KEY=<external-secret>
MVP_COCKPIT_API_KEY=<external-secret>
MVP_HERMES_API_KEY=<external-secret>
```

Reference gateway surface:

```text
Cockpit read key:
  GET /v1/paperless/documents
  GET /v1/paperless/documents/{id}
  GET /v1/paperless/documents/{id}/capture?version_id=<exact>
  GET /v1/paperless/tasks/{task_id}

Hermes key + Pantheon PDP:
  POST /v1/paperless/documents/{id}/metadata
```

The read projection must not expose the Paperless token or promote extracted
Paperless `content` into governed Knowledge by implication.

```text
gateway_read != source_truth
gateway_health != Paperless_safe
```

## Step 6 — Point Hermes at the governed adapters

The live runtime uses the same `HttpPolicyClient` already implemented in
`pantheon-mvp`. Direct Paperless writes are never a fallback path.

```python
import os

from mvp_vertical.paperless import PaperlessClient
from mvp_vertical.policy_gate import HttpPolicyClient

policy = HttpPolicyClient(
    base_url="http://pantheon-policy-api:8000",
    api_key=os.environ["PANTHEON_POLICY_API_KEY"],
)

paperless = PaperlessClient(
    base_url=os.environ["PAPERLESS_API_URL"],
    token=os.environ["PAPERLESS_API_TOKEN"],
)
```

The same policy client backs `capability_manager.governed_execute` and the
Paperless mutation helpers:

```text
governed_post_document
governed_update_document_metadata
```

A Paperless classification write must never be triggered solely because Hermes
produced a Classification Candidate.

## Step 7 — Verify the chokepoint end to end

Use the read-only verifications the repository already ships:

```text
mcp-server verify_install / verify_exposure / run_doctor_checks on the deployment evidence
a preflight round-trip: POST /v1/policy/preflights:evaluate returns a disposition
a decision round-trip:  POST /v1/policy/decisions:validate returns a verdict
a blocked case: with the PDP stopped, a consequential effect fails closed (does not run)
```

Add Paperless-specific synthetic cases:

```text
gateway read/search succeeds with Cockpit key
direct browser access never receives the Paperless token
exact-version download yields repeatable SHA-256
metadata update with valid Hermes key + gate executes
metadata update with missing/invalid decision does not call Paperless
metadata update with the PDP unavailable does not call Paperless
upload with invalid decision does not create a Paperless task
```

The blocked checks are essential: stopping the PDP must block the Paperless
write, not let it through.

## Step 8 — Verify Paperless -> existing Document vertical

Use the external `pantheon-mvp` `paperless_ingestion.intake_paperless_document`
path for one synthetic source. It must reuse the existing `store.ingest`; a
second RAG/chunk/index pipeline is not admitted.

```text
Paperless exact document/version
-> PaperlessSourceCapture + SHA-256
-> Task Contract source membership check
-> temporary contained materialization
-> existing store.ingest
-> Docling structured extraction
-> source_documents / document_versions / extraction / chunks
-> paperless_source_bindings
```

The binding must retain:

```text
Project Document id
Paperless document id
Paperless version id
paperless:// storage reference
original filename
source digest
```

Verify:

```text
Paperless original remains retrievable
Project Document digest == exact Paperless capture digest
Docling derivative carries its own identity/provenance
temporary source file is not the canonical locator
same Paperless version may back more than one project/document link
Paperless visibility does not expand the Task Contract source perimeter
```

## Step 9 — Verify Knowledge separation

For the synthetic source, the result after intake is still a Project Document
and derived extraction. Knowledge publication remains a separate governed step.

```text
Paperless Source Capture
-> Project Document
-> derived Projection
-> optional Knowledge candidate/publication under existing rules
```

Verify:

```text
Paperless metadata is only an operational mirror
Project Document != Knowledge Item
Knowledge publication does not mutate the Paperless original
Knowledge != Evidence
Paperless Source Capture != Evidence
```

## Rollback

Policy rollback:

```text
docker compose -f compose.policy-api.yaml down
revert the Hermes connection fragment to no policy binding
the cockpit/runtime refuses consequential effects fail-closed
```

Paperless rollback:

```text
disable the Paperless adapter/gateway binding first
retain existing Source Capture and paperless_source_bindings references as historical observations
restore the reviewed previous Paperless image + compatible database/media backup
re-run read-only gateway probe and exact-version capture check
never silently substitute NAS or another DMS for missing Paperless sources
```

## Boundary

```text
deployed != adopted
installed != approved
Paperless reachable != document binding authorized
healthy != safe
PDP reachable != effect authorized
Paperless task success != professional validation
green acceptance != production authorization
```

Phase B connects reviewed candidates in one operator environment. It does not
close adoption Gate 8, authorize real-dossier use or make Pantheon a runtime,
DMS, queue, scheduler or installer. The human decides consequential effects and
any activation.
