# Document runtime live observations

Status: external executable candidate — source-attributed read-only observation implemented / not deployed or adopted.

This slice extends the first Document Runtime Status card without turning the Cockpit, observer, Paperless gateway or Pantheon into a runtime manager.

```text
OpenWebUI exposes observations.
External observer reads bounded technical surfaces.
Hermes native CLI supplies its own skill inventory when co-located.
Pantheon PDP supplies policy readiness/meta observations.
Docling supplies its own health-endpoint observation.
Pantheon governs status and activation semantics.
Human decides consequential activation.
```

## Observation sources

`mvp_vertical.document_runtime_observer` exposes:

```text
GET /health
GET /v1/document-runtime/observations
```

`/health` means only that the observer process answers.

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

### Hermes native skill inventory

When the observer is explicitly configured on the Hermes host:

```text
hermes skills list
```

The command is fixed and executed without a shell. The output is checked for the exact skill token:

```text
pantheon-document-intake
```

Possible observations:

```text
installed_observed
not_listed_observed
not_observed
```

Default mode is `disabled`, which returns `not_observed` rather than guessing absence.

```text
skill listed != approved
skill listed != activated for project scope
skill listed != normal model/agent invocation proven
```

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

The OpenWebUI Tool does not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
MVP_HERMES_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
DOCLING_SERVE_API_KEY
Paperless database credentials
```

It renders source-attributed observations and non-equivalence reminders.

## Synthetic deployment check

`scripts/document_runtime_synthetic_check.py` is an operator-run acceptance helper. It is not a scheduler, monitor, approval engine or production health authority.

Default mode is read-only. It requires independent observations for:

```text
Paperless source path reachable
Pantheon PDP ready endpoint observed
Docling health endpoint reachable
pantheon-document-intake listed by native Hermes inventory
```

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

from the child environment. The skill retains only the ordinary Hermes/gateway runtime inputs already configured for it.

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

## Configuration

Observer server-side configuration:

```text
MVP_COCKPIT_API_KEY
PANTHEON_PAPERLESS_GATEWAY_URL
PANTHEON_POLICY_API_URL
PANTHEON_POLICY_API_KEY
DOCLING_SERVE_URL
DOCLING_SERVE_API_KEY              optional
MVP_HERMES_INVENTORY_MODE          disabled | local_cli
HERMES_CLI_PATH
MVP_RUNTIME_OBSERVER_TIMEOUT
```

The optional issuer signing secret is **not** observer configuration. It is an operator-only synthetic-test input.

## Current status

```text
Paperless observation source          implemented candidate
Pantheon PDP observation              implemented candidate
Docling health observation            implemented candidate
Hermes native inventory observer      implemented candidate / co-location required
OpenWebUI live status projection      implemented candidate
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
