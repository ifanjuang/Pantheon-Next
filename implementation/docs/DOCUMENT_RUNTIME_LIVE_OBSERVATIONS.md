# Document runtime live observations

Status: external executable candidate — source-attributed read-only observation implemented / not deployed or adopted.

This slice extends the first Document Runtime Status card without turning the Cockpit, observer, Paperless gateway or Pantheon into a runtime manager.

```text
OpenWebUI exposes observations.
External observers read bounded technical surfaces.
Hermes exposes its skill inventory through its authenticated read-only API.
Pantheon PDP supplies policy readiness/meta observations.
Docling supplies its own health-endpoint observation.
Pantheon governs status and activation semantics.
Human decides consequential activation.
```

## Observation adapters

Two external observer implementations now exist.

### Legacy/co-located observer

```text
mvp_vertical.document_runtime_observer
```

It can use a fixed native `hermes skills list` command when explicitly co-located with the Hermes CLI. This remains useful for local/offline deployments but is not required for the multi-container Phase B layout.

### Network-native observer

```text
mvp_vertical.document_runtime_network_observer
```

This is the preferred container/Portainer candidate. It observes Hermes through the authenticated read-only API:

```text
GET <HERMES_API_URL>/v1/skills
Authorization: Bearer <HERMES_API_SERVER_KEY>
```

Only the target skill's presence and a bounded skill count are projected. The API key and full skill inventory are not returned by the observer.

Both observers expose:

```text
GET /health
GET /v1/document-runtime/observations
```

`/health` means only that the observer process answers.

## Independent observation sources

The bounded observation endpoint returns four independent source observations.

### Paperless / bounded gateway

```text
GET <PANTHEON_PAPERLESS_GATEWAY_URL>/health
```

Observed fields may include gateway reachability, Paperless reachability and declared intake/write surfaces.

```text
Paperless reachable != Paperless healthy
Paperless healthy != safe
```

### Pantheon PDP

```text
GET <PANTHEON_POLICY_API_URL>/readyz
GET <PANTHEON_POLICY_API_URL>/v1/meta
```

The policy credential remains server-side. The projection allowlists bounded meta fields only.

```text
PDP ready != effect authorized
PDP reachable != policy decision for a concrete effect
```

The current V0 external/canonical effect flags remain evaluated at effect time. Generic status observation must not synthesize them.

Human issuer authentication is also decision-time data. The observer does not infer it from PDP readiness or registry configuration.

```text
issuer verification implemented != issuer authenticated on target
issuer_authenticated != approval
```

### Docling Serve

```text
GET <DOCLING_SERVE_URL>/health
```

An optional Docling API key is sent server-side when configured.

```text
Docling health endpoint responds != extraction quality established
Docling reachable != professional validation
```

### Hermes skill inventory

Preferred network-native source:

```text
GET <HERMES_API_URL>/v1/skills
```

Expected bounded target:

```text
pantheon-document-intake
```

Possible observations:

```text
installed_observed
not_listed_observed
not_observed
```

A successful `/v1/skills` observation establishes only that Hermes' current inventory lists the skill.

```text
skill listed != approved
skill listed != activated for project scope
skill listed != normal model/agent invocation proven
```

The co-located CLI observer remains available as a fallback observation adapter. It must execute the fixed native command without a shell and must never accept caller-provided command fragments.

## Aggregate semantics

The observation set intentionally declares:

```text
synthetic_global_health = not_computed
write_effect = false
authority_effect = none
activation_changed = false
```

Each field keeps its own:

```text
source
observation_source
observed_at
source-specific status
```

The observer does not compute a global green/red safety or readiness score.

## Cockpit projection

`openwebui/pantheon_document_runtime_live_status.py` reads only the bounded observer endpoint with the Cockpit read key.

The Tool itself does not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
MVP_HERMES_API_KEY
HERMES_API_SERVER_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
DOCLING_SERVE_API_KEY
Paperless database credentials
```

The OpenWebUI application may separately hold the Hermes API-server key for its normal server-to-server model connection. That connection credential is not passed through the status Tool response.

## Network observer server-side configuration

```text
MVP_COCKPIT_API_KEY
PANTHEON_PAPERLESS_GATEWAY_URL
PANTHEON_POLICY_API_URL
PANTHEON_POLICY_API_KEY
DOCLING_SERVE_URL
DOCLING_SERVE_API_KEY              optional
HERMES_API_URL
HERMES_API_SERVER_KEY
MVP_RUNTIME_OBSERVER_TIMEOUT
```

The observer holds these only to perform read-only server-to-server observations. They are not rendered to the Cockpit.

Legacy/co-located observer configuration remains:

```text
MVP_HERMES_INVENTORY_MODE          disabled | local_cli
HERMES_CLI_PATH
```

## Synthetic deployment check

`scripts/document_runtime_synthetic_check.py` is an operator-run acceptance helper. It is not a scheduler, monitor, approval engine or production health authority.

Default mode is read-only. It requires independent observations for:

```text
Paperless source path reachable
Pantheon PDP ready endpoint observed
Docling health endpoint reachable
pantheon-document-intake listed by Hermes inventory
```

With the network-native observer, the Hermes prerequisite can be established over `ai-net` through `/v1/skills`; CLI co-location is no longer required for this check.

A pass means only:

```text
candidate_ready_for_synthetic_intake = true
```

### Optional synthetic intake

State-writing candidate intake requires explicit operator intent:

```text
--run-intake
--ack SYNTHETIC_ONLY
exact Paperless document id/version
synthetic Task Contract containing exact source_ref
human decision payload
installed Hermes skill transport
MVP_HERMES_API_KEY in operator environment
```

The helper uses the installed skill transport; it does not recreate the PEP/PDP write path locally.

The helper never performs:

```text
Paperless upload
Paperless metadata mutation
delete/version replacement
Knowledge publication
Evidence admission
activation/update/install
provider routing
```

### Optional authenticated-issuer proof

When the operator explicitly requests:

```text
--require-issuer-auth
```

the operator environment must additionally provide:

```text
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
PANTHEON_POLICY_API_KEY
PANTHEON_POLICY_API_URL
```

The helper:

```text
loads the human decision payload
-> signs only the bounded decision fields with decision_signing.py
-> writes a temporary signed decision file
-> invokes the installed Hermes skill
-> receives the PEP-derived decision_expectation from the gateway result
-> calls PDP /v1/policy/decisions:validate read-only
   with the signed decision + that exact returned expectation
-> records verdict + issuer_authenticated
```

This proof does not authorize any additional effect.

```text
issuer_authenticated != approval
valid decision verdict != effect authorization
```

The signing secret and policy key remain in the operator helper process. Before invoking the skill subprocess, the helper explicitly removes:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
```

from the child environment.

The receipt keeps:

```text
technical_receipt_is_evidence = false
activation_changed = false
production_authorization = false
agent_skill_selection_proven = false
```

and classifies issuer proof separately:

```text
human_issuer_authentication_status = not_attempted | not_observed | not_proven | proven
human_issuer_authentication_proven = true | false
```

A proof may be `proven` only when the separate PDP validation returns both:

```text
verdict = valid
issuer_authenticated = true
```

## Phase B Portainer relationship

`compose.phase-b.yaml` uses the network-native observer and the shared external `ai-net` network. It keeps PostgreSQL, Docling, Paperless gateway, Cockpit, Hermes and observer ports internal to Docker; only Paperless's bootstrap/admin port is host-bindable and defaults to loopback.

The composition reuses an existing OpenWebUI service by attaching it to `ai-net`; it does not create a second OpenWebUI or SearXNG instance.

```text
compose present != target deployed
container running != binding activated
```

## Current status

```text
Paperless observation source          implemented candidate
Pantheon PDP observation              implemented candidate
Docling health observation            implemented candidate
Hermes CLI inventory observer         implemented candidate / co-location optional
Hermes HTTP /v1/skills observer       implemented candidate / preferred for containers
OpenWebUI live status projection      implemented candidate
Phase B Portainer composition         implemented candidate / not deployed
synthetic read-only assessment        implemented candidate
optional synthetic intake helper      implemented candidate / not run
optional issuer-auth proof helper      implemented candidate / not run
live target deployment                not established
live observations                     not established by repository tests
Hermes agent skill selection          not proven
target issuer-authenticated decision  not proven
adoption                              not decided
activation                            not authorized
production                            forbidden pending separate review
```
