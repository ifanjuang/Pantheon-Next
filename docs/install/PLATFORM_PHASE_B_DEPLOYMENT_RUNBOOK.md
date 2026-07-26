# Platform Phase B — Deployment Runbook

Status: candidate operator artifact — documented non-implemented.
Boundary profile: candidate_support_note.

This runbook is the operator handoff for Phase B of `docs/roadmaps/PLATFORM_IMPLEMENTATION_ROADMAP.md`: deploy the policy PDP and the common core, then wire reviewed external adapters so consequential effects route through the chokepoint.

It documents commands; it runs none of them. It stores no secret, changes no host and authorizes no production use. Deployment is a reviewed operator action; adoption Gate 8 remains a separate human decision.

```text
OpenWebUI exposes.
Hermes Agent executes and enforces.
Local/NAS governed sources support core document ingestion.
Paperless-ngx optionally manages document sources.
Docling derives structured representations when selected.
Pantheon Next governs.
The human decides consequential effects.
```

## What already exists

```text
PDP capability              Pantheon mcp-server policy/preflight/decision validation
PDP container candidate     Dockerfile.policy-api, compose.policy-api.yaml
PEP seam                    external pantheon-mvp policy_gate + policy_request
policy HTTP client          external pantheon-mvp
local/NAS document intake   external pantheon-mvp declared-source/store.ingest path
Paperless adapter/gateway   external pantheon-mvp, optional binding
Paperless Hermes skill      external pantheon-mvp, optional binding
network observer            external pantheon-mvp
Portainer specialization    docs/install/PORTAINER_PHASE_B_HANDOFF.md
```

Phase B connects external candidates. It does not move runtime workers, queues, schedulers, source bytes, issuer keys or secrets into Pantheon.

## Prerequisites — core

```text
a Docker host the operator controls
the external network ai-net
a pinned Pantheon Next checkout mounted read-only
a secret manager holding PANTHEON_POLICY_API_KEY and runtime credentials
a reviewed pantheon-mvp commit
a reviewed read-only issuer-key registry only when authenticated issuer proof is required
persistent governed database/runtime storage
a bounded read-only local/NAS source root when local-source ingestion is used
```

Paperless image, database, media paths and broker are not core prerequisites. They become prerequisites only after explicit selection of `document_source_management -> paperless_ngx`.

```text
Paperless absent != Pantheon degraded
Paperless absent != document ingestion unavailable
```

## Step 1 — Deploy the policy PDP

Bring up `pantheon-policy-api` on `ai-net` from the hardened candidate. It publishes no host port, mounts the repository read-only, drops capabilities and receives no Docker socket.

```bash
export PANTHEON_POLICY_API_KEY='<external-secret>'
docker compose -f compose.policy-api.yaml up -d
```

Acceptance from `ai-net`:

```bash
curl -fsS http://pantheon-policy-api:8000/livez
curl -fsS http://pantheon-policy-api:8000/readyz
curl -fsS -H "Authorization: Bearer $PANTHEON_POLICY_API_KEY" \
  http://pantheon-policy-api:8000/v1/meta
```

```text
ready != safe
PDP reachable != effect authorized
```

Current bounded V0 posture remains:

```text
external_effect_allowed = false
canonical_effect_allowed = false
```

### Optional issuer-authentication input

When acceptance requires proof of who issued a human decision, provision the reviewed read-only issuer registry outside the repository and mount/reference it through operator tooling.

```text
issuer registry configured != issuer authenticated
issuer_authenticated != approval
```

## Step 2 — Deploy the common core

Deploy the required core described by `COMMON_INSTALLATION_BASELINE.md` and the environment-specific handoff.

Reference core includes:

```text
private ai-net
persistent governed PostgreSQL/pgvector
Hermes Agent
OpenWebUI exposure connection
Pantheon policy interface
Cockpit/runtime projection as selected
read-only local/NAS source root when local ingestion is used
```

Conditional components such as Docling, SearXNG, Browserless, Ollama and Paperless are present only when their reviewed capability binding is selected.

```text
conditional service absent != core degraded
```

## Step 3 — Prove core local/NAS document ingestion

Before adding an optional DMS, prove one synthetic source through the core source path.

Expected sequence:

```text
synthetic file under reviewed read-only document root
-> Task Contract declares exact source
-> resolved path remains inside allowed root
-> source digest computed
-> reviewed extraction binding when needed
-> Project Document candidate
-> Knowledge publication remains separate
```

Verify:

```text
undeclared source -> refused
path escape -> refused
source digest retained
runtime success != Evidence
Project Document != Knowledge Item
Knowledge != Evidence
```

This is the baseline document-ingestion proof.

## Step 4 — Configure Hermes / PEP posture

The Pantheon HTTP policy contract remains generic. External PEPs translate runtime-specific actions into the reviewed request/gate-signals contract and honor explicit policy effect flags independently of decision validation.

Required behavior:

```text
PDP unavailable -> fail closed
external_effect_allowed != true + external effect -> block
canonical_effect_allowed != true + canonical/memory effect -> block
caller expectation cannot override PEP-observed effect facts
```

Disable or neutralize any runtime smart-approval mechanism for consequential effects. Runtime/model review never substitutes for the human decision and Pantheon preflight.

## Step 5 — Optional: select Paperless source management

Only when the operator/human selects:

```text
Capability Slot: document_source_management
binding: paperless_ngx
```

follow `docs/install/PAPERLESS_INITIAL_INSTALLATION.md` and the Portainer specialization.

Required Paperless-specific state then includes:

```text
reviewed image tag/digest
private Paperless network endpoint
private broker
separate database role/database or instance
persistent data/media/export/consume paths
backup + restore target
dedicated API identity/token owner
PANTHEON_PAPERLESS_BINDING_SELECTED=true
```

Start the optional profile in the external runtime candidate:

```bash
docker compose -f compose.phase-b.yaml --profile paperless up -d
```

```text
binding selected != installed
installed != activated
```

## Step 6 — Optional: deploy the bounded Paperless gateway

After native Paperless bootstrap, create a dedicated API token and inject it only into the server-side gateway/runtime environment.

```text
PAPERLESS_API_URL=http://paperless:8000
PAPERLESS_API_TOKEN=<external-secret>
PANTHEON_POLICY_API_URL=http://pantheon-policy-api:8000
PANTHEON_POLICY_API_KEY=<external-secret>
MVP_COCKPIT_API_KEY=<external-secret>
MVP_HERMES_API_KEY=<external-secret>
```

The Cockpit and Hermes skill must not receive the raw Paperless token or PDP/issuer secrets.

For a future policy version authorizing Paperless mutation, the gateway still revalidates exact source identity before applying the effect.

## Step 7 — Optional: install the Paperless Hermes skill

Follow `docs/install/HERMES_PANTHEON_DOCUMENT_INTAKE_SKILL.md` only when the Paperless binding is selected.

The Paperless-specific skill receives only its bounded gateway inputs. It does not receive Paperless/PDP/database/issuer backing credentials.

```text
skill installed != skill approved
skill loaded != task authorized
```

## Step 8 — Prove policy chokepoints

Core policy cases:

```text
PDP stopped -> governed consequential executor does not run
wrong decision object/digest/scope -> effect refused
issuer signature invalid/unknown -> decision invalid when issuer registry configured
```

Paperless-specific cases apply only when selected:

```text
exact-version capture repeatable
source outside Task Contract refused
caller external_effect=false cannot downgrade Paperless external effect
current PDP V0 Paperless metadata PATCH/upload blocked
changed live source invalidates previous mutation decision
```

```text
valid decision verdict != effect authorization
issuer_authenticated != effect authorization
```

## Step 9 — Optional: verify Paperless exact-version intake

When Paperless is selected, run its synthetic binding acceptance:

```text
Paperless exact document/version
-> Source Capture + digest
-> Task Contract membership
-> PEP-owned expectation
-> Pantheon preflight / decision validation
-> existing store.ingest
-> reviewed extraction
-> Project Document candidate
```

The result retains Paperless provenance and does not automatically publish Knowledge or admit Evidence.

```text
Paperless Source Capture != Evidence
Project Document != Knowledge Item
```

This is an additional binding proof, not the core ingestion proof.

## Step 10 — Record issuer proof separately when required

Record only bounded evidence such as:

```text
PDP version/commit
issuer registry reference, never raw key
issuer id
decision id
object/digest reference
issuer_authenticated result
timestamp
```

```text
issuer authentication implementation available != target proof established
```

## Runtime observations

The network observer must represent service selection honestly.

Without Paperless selected:

```text
binding_status = not_selected
installation_status = not_applicable
reachability_status = not_applicable
health_status = not_applicable
```

It must not probe the absent Paperless gateway.

With Paperless selected, gateway reachability/health observations become applicable to that binding only.

## Rollback

Core and Paperless rollback remain separable.

Paperless rollback:

```text
disable binding
set PANTHEON_PAPERLESS_BINDING_SELECTED=false
stop optional profile
retain persistent Paperless data for reviewed restore
local/NAS ingestion remains available
```

Core rollback remains operator-owned and must preserve governed records and recorded source provenance.

## Boundary

```text
deployed != adopted
installed != approved
Paperless absent != Pantheon degraded
Paperless absent != document ingestion unavailable
Paperless reachable != document binding authorized
Hermes skill installed != task authorized
healthy != safe
PDP reachable != effect authorized
issuer_authenticated != approval
runtime success != Evidence
green synthetic acceptance != production authorization
```

Phase B connects reviewed candidates in one operator environment. It does not close adoption Gate 8, authorize real-dossier use or make Pantheon a runtime, DMS, queue, scheduler, installer, secret store or identity provider. The human decides consequential effects and activation.
