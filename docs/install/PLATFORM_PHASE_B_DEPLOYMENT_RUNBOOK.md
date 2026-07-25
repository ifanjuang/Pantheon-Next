# Platform Phase B — Deployment Runbook

Status: candidate operator artifact — documented non-implemented.
Boundary profile: candidate_support_note.

This runbook is the operator handoff for Phase B of
`docs/roadmaps/PLATFORM_IMPLEMENTATION_ROADMAP.md`: deploy the policy PDP and the
reference stack, then wire reviewed external adapters so consequential effects
route through the chokepoint.

It documents commands; it runs none of them. It stores no secret, changes no
host and authorizes no production use. Deployment is a reviewed operator action;
adoption Gate 8 remains a separate human decision.

```text
OpenWebUI exposes.
Hermes Agent executes and enforces.
Paperless-ngx stores document sources externally.
Docling derives structured representations.
Pantheon Next governs.
The human decides consequential effects.
```

## What already exists (do not rebuild)

```text
PDP capability              Pantheon mcp-server: preflight + validate_decision + optional issuer signature verification
PDP container candidate     Dockerfile.policy-api, compose.policy-api.yaml (not activated)
PEP seam                    pantheon-mvp policy_gate + policy_request (merged)
real policy HTTP client     pantheon-mvp policy_gate.HttpPolicyClient (merged)
decision signing producer   pantheon-mvp decision_signing.py (merged)
capability lifecycle        pantheon-mvp capability_manager (merged)
Paperless API adapter       pantheon-mvp paperless.PaperlessClient (merged)
Paperless internal gateway  pantheon-mvp paperless_gateway (merged)
Paperless document intake   pantheon-mvp paperless_ingestion -> existing store.ingest
Paperless Source Inbox      pantheon-mvp OpenWebUI read-only candidate
Hermes document skill       pantheon-mvp pantheon-document-intake (merged candidate)
Paperless install runbook   docs/install/PAPERLESS_INITIAL_INSTALLATION.md
Hermes skill runbook        docs/install/HERMES_PANTHEON_DOCUMENT_INTAKE_SKILL.md
reference components        docs/install/REFERENCE_PLATFORM_COMPONENTS.md
baseline handoff            docs/install/COMMON_BASELINE_RUNBOOK.md
```

Phase B installs and connects candidates. It does not move Paperless workers,
queues, schedulers, document bytes, issuer keys or runtime secrets into Pantheon.

## Prerequisites

```text
a Docker host the operator controls (SSH / Portainer)
the external network `ai-net` created: docker network create ai-net
a pinned Pantheon Next checkout mounted read-only
a secret manager holding PANTHEON_POLICY_API_KEY and stack credentials
a reviewed read-only issuer-key registry when authenticated human-decision proof is required
a reviewed pinned Paperless image/tag/digest
persistent Paperless database + data/media backup targets
a reviewed pantheon-mvp commit containing the merged gateway/skill/decision-signing code
the reference components reviewed (REFERENCE_PLATFORM_COMPONENTS.md)
```

Secrets are referenced from the operator's secret manager, never committed.

```text
repository contains signing/verification code != repository contains issuer secrets
```

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

`readyz` confirms the checkout is readable; it does not establish safety.

```text
ready != safe
PDP reachable != effect authorized
```

Record the observed policy version/contract. The current bounded V0 posture remains:

```text
external_effect_allowed = false
canonical_effect_allowed = false
```

An eligible candidate-work disposition does not override these flags.

### Optional issuer-authentication deployment input

When the acceptance scope requires proof of who issued the human decision, create
a reviewed read-only registry outside the repository and expose its path to the
PDP as:

```text
PANTHEON_DECISION_ISSUER_KEYS_PATH=<operator-managed-read-only-path>
```

The registry/key material remains an operator secret-management concern. Mount
it read-only and do not copy raw keys into Pantheon documentation, Task Contracts,
Knowledge, logs or the Hermes skill package.

Verify the PDP reports/behaves as configured using a synthetic signed decision.
Do not infer authentication merely from the environment variable being present.

```text
issuer registry configured != issuer authenticated
issuer_authenticated != approval
```

## Step 2 — Deploy the reference stack

Deploy the components of `REFERENCE_PLATFORM_COMPONENTS.md` on `ai-net`, each
pinned: PostgreSQL/pgvector, Paperless-ngx with its private broker, Ollama,
Hermes Agent, OpenWebUI, SearXNG, Browserless/Chromium and any conditional
document-analysis/extraction service a reviewed binding selects.

Follow `COMMON_BASELINE_RUNBOOK.md` for the SSH/Docker/Portainer handoff and its
acceptance checks. Treat generic `/health` as a version-guarded observation, not
a universal safety verdict. Verify the effective Hermes API/model surface against
the installed Hermes version rather than assuming old configuration names.

Paperless is source-management infrastructure; Docling remains a separate
analysis binding.

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

Create a dedicated Paperless API token outside the repository and inject it only
into the server-side gateway/runtime environment:

```text
PAPERLESS_API_URL=http://paperless:8000
PAPERLESS_API_TOKEN=<external-secret>
```

Read-only operator acceptance:

```bash
curl -fsS \
  -H "Authorization: Token $PAPERLESS_API_TOKEN" \
  "http://paperless:8000/api/documents/?page_size=1"
```

Then perform the synthetic exact-version Source Capture check from the Paperless
runbook. A mutable `latest` pointer is insufficient for immutable intake.

## Step 4 — Configure the Hermes Policy Enforcement Point posture

The Pantheon HTTP policy contract is generic. The external PEP translates
runtime-specific actions to:

```text
request
+ gate_signals
```

and honors explicit policy effect flags independently of decision validation.

Required PEP behavior:

```text
PDP unavailable -> fail closed
external_effect_allowed != true + external effect -> block
canonical_effect_allowed != true + canonical/memory effect -> block
caller decision expectation -> cannot override PEP-observed effect facts
known Paperless external executor -> caller cannot downgrade external_effect to false
```

For `pantheon-document-intake`, the PEP derives ceiling, scope, object identity
and digest from the Task Contract, exact source and requested operation before
validating the human decision.

Disable or otherwise neutralize any Hermes runtime/model smart-approval mechanism
for consequential effects. An in-runtime model review never substitutes for the
human decision and Pantheon preflight.

Re-verify native Hermes tool/config names against the observed runtime version
before enabling the binding.

## Step 5 — Deploy the bounded Paperless gateway

The Cockpit and Hermes must not receive the raw Paperless API token, Pantheon
policy key or issuer-signing material.

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
Cockpit or Hermes read key:
  GET /v1/paperless/documents
  GET /v1/paperless/documents/{id}
  GET /v1/paperless/documents/{id}/capture?version_id=<exact>
  GET /v1/paperless/tasks/{task_id}

Hermes key + Pantheon PDP:
  POST /v1/paperless/intakes
  POST /v1/paperless/documents/{id}/metadata
```

The read projection must not expose the Paperless token or promote extracted
Paperless `content` into governed Knowledge by implication.

```text
gateway_read != source_truth
gateway_health != Paperless_safe
```

For a future policy version that authorizes metadata PATCH, the gateway revalidates
the selected exact version immediately before the effect and, on the real
Paperless client, compares the current/latest source bytes to the approved capture
hash. If the source changed, the PATCH is refused and a new capture/decision is
required.

```text
approved historical capture != authority to classify changed live bytes
```

## Step 6 — Install the bounded Hermes document skill

Follow `docs/install/HERMES_PANTHEON_DOCUMENT_INTAKE_SKILL.md`.

Install the complete commit-pinned skill package with native Hermes tooling. The
package contains both `SKILL.md` and its supporting transport script.

The Hermes runtime receives only:

```text
PANTHEON_PAPERLESS_GATEWAY_URL=http://paperless-gateway:8082
MVP_HERMES_API_KEY=<runtime-secret>
```

It must not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
issuer signing secret
Paperless database credentials
```

Native Hermes inventory must show the installed skill before the synthetic
workflow is attempted.

```text
skill installed != skill approved
skill loaded != task authorized
```

## Step 7 — Prove the chokepoint end to end

Use repository verification surfaces and the external synthetic skill path:

```text
mcp-server verify_install / verify_exposure / run_doctor_checks on deployment evidence
POST /v1/policy/preflights:evaluate returns a disposition and effect flags
POST /v1/policy/decisions:validate returns a decision verdict
PDP stopped -> governed executor does not run
```

When an issuer registry is configured, include signed-decision cases:

```text
known issuer + correct signature -> issuer_authenticated observed true in validation result
unknown issuer -> invalid/refused
incorrect signature -> invalid/refused
missing signature when registry requires authentication -> invalid/refused
```

Record the issuer identifier and validation result, never the raw key.

Add Paperless/Hermes cases:

```text
Hermes search/inspect reaches gateway with Hermes key
browser/Hermes never receives Paperless token
exact-version capture yields repeatable SHA-256
source outside Task Contract is refused before policy/persistence
malformed Task Contract YAML returns bounded 422/refusal
wrong decision object/digest/scope prevents persistence
caller-provided external_effect=false cannot downgrade a known Paperless upload/PATCH
Project Document candidate intake can run only through the governed intake path
current PDP V0 metadata PATCH is blocked_external_effect_not_authorized
current PDP V0 upload/external effects remain blocked
changed live Paperless bytes invalidate a previously approved metadata-mutation source
```

For current V0, **do not** expect a valid signed decision to make a Paperless
PATCH execute. Correct behavior is that the PEP honors
`external_effect_allowed=false` and never calls Paperless.

```text
valid decision verdict != effect authorization
issuer_authenticated != effect authorization
```

## Step 8 — Verify Paperless → existing Document vertical through Hermes

Use the installed `pantheon-document-intake` skill with one synthetic source. The
gateway reuses the existing external `store.ingest`; a second RAG/chunk/index
pipeline is not admitted.

```text
Hermes skill
-> Paperless gateway
-> exact Paperless document/version
-> PaperlessSourceCapture + SHA-256
-> Task Contract source membership check
-> PEP-owned effect expectation
-> Pantheon preflight + decision validation
-> configured issuer-signature verification when required
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
Hermes skill does not receive backing Paperless/PDP/issuer secrets
```

## Step 9 — Verify Knowledge separation

For the synthetic source, the result after intake remains a Project Document
candidate and derived extraction. Knowledge publication is a separate governed
step.

```text
Paperless Source Capture
-> Project Document candidate
-> derived Projection
-> optional later Knowledge candidate/publication under existing rules
```

Verify:

```text
Paperless metadata is only an operational mirror
Project Document != Knowledge Item
Knowledge publication does not mutate the Paperless original
Knowledge != Evidence
Paperless Source Capture != Evidence
```

The intake response should explicitly preserve:

```text
knowledge_published: false
evidence_admitted: false
```

## Step 10 — Record authenticated-issuer proof separately

The code path now supports issuer signature production and PDP verification. The
remaining requirement is environment evidence, not a missing architecture.

For the synthetic acceptance, record:

```text
PDP version/commit
issuer registry secret/reference/path identifier, not raw key
issuer id used by the synthetic human decision
decision id
object identity + digest reference
signature verification result / issuer_authenticated observation
timestamp
```

If the target cannot produce a verified issuer-authenticated round-trip when the
acceptance policy requires it, classify:

```text
issuer authentication implementation -> available
issuer authentication target proof    -> not established
```

Do not silently fall back to a caller-provided `decided_by` string.

## Rollback

Hermes skill rollback:

```bash
hermes skills uninstall pantheon-document-intake
```

Policy rollback:

```text
disable the gateway/PEP binding
remove/disable the target issuer registry mount through operator tooling if needed
the cockpit/runtime refuses governed mutations fail-closed
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
Hermes skill installed != task authorized
healthy != safe
PDP reachable != effect authorized
asserted decided_by != authenticated human issuer
issuer_authenticated != approval
Paperless task success != professional validation
runtime success != Evidence
green synthetic acceptance != production authorization
```

Phase B connects reviewed candidates in one operator environment. It does not
close adoption Gate 8, authorize real-dossier use or make Pantheon a runtime,
DMS, queue, scheduler, installer, secret store or identity provider. The human
decides consequential effects and activation.
