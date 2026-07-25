# Document Runtime Live Observations

Status: candidate support doctrine — external implementation merged / target deployment not established.
Boundary profile: candidate_support_note.

This document governs the live-observation layer of the document vertical after the first read-only status card.

Current external implementation:

```text
repository: ifanjuang/pantheon-mvp
historical live-observation slice: #62
current-main reconstruction: #73 merged
network-native container extension: #76 merged
legacy/co-located observer: mvp_vertical.document_runtime_observer
preferred container observer: mvp_vertical.document_runtime_network_observer
Cockpit projection: openwebui/pantheon_document_runtime_live_status.py
synthetic helper: scripts/document_runtime_synthetic_check.py
Phase B composition: compose.phase-b.yaml
```

Repository implementation does not establish that any target host runs these components.

## Boundary

```text
OpenWebUI exposes source-attributed observations.
External observers read bounded technical surfaces.
Hermes reports its skill inventory through a read-only runtime surface.
Paperless reports source-runtime reachability through the bounded gateway.
Docling reports its own health endpoint.
Pantheon PDP reports policy readiness/meta and validates bounded decisions.
Pantheon governs status semantics, gates and activation.
The human decides consequential activation and use.
```

Pantheon does not run the probes, schedule them, restart services or turn observations into automatic approvals.

## Required non-equivalences

```text
reachable != healthy
healthy != safe
installed != approved
skill listed != skill activated for scope
PDP ready != effect authorized
issuer verification implemented != issuer authenticated on target
issuer_authenticated != approval
Docling health endpoint responds != extraction quality established
runtime success != Evidence
runtime observation != activation decision
synthetic check pass != production adoption
compose present != target deployed
```

A runtime observation set must not collapse these dimensions into one global green/red health score.

## Observation record minimum

Each source observation retains at least:

```yaml
source:
observation_source:
observed_at:
reachability_status:
```

The aggregate projection declares:

```yaml
synthetic_global_health: not_computed
authority_effect: none
write_effect: false
activation_changed: false
```

## Paperless / bounded gateway

Observation source:

```text
GET <PANTHEON_PAPERLESS_GATEWAY_URL>/health
```

This may establish gateway reachability and the gateway's observed Paperless reachability. It does not establish Paperless safety, backup validity, restore readiness, professional suitability or activation.

## Pantheon PDP

Candidate observation surfaces:

```text
GET /readyz
GET /v1/meta
```

The policy credential stays server-side. `/readyz` is readiness of the policy projection, not authorization of a concrete effect.

Current effect authorization remains evaluated by the PEP from the exact preflight response. The V0 posture remains conservative:

```text
external_effect_allowed = false
canonical_effect_allowed = false
```

Issuer authentication is decision-time data. It must not be inferred from PDP readiness, from the presence of `PANTHEON_DECISION_ISSUER_KEYS_PATH`, or from the existence of signing code.

```text
configured registry != issuer authenticated
issuer_authenticated != approval
valid decision verdict != effect authorized
```

## Docling

Observation source:

```text
GET <DOCLING_SERVE_URL>/health
```

A responding health endpoint does not establish extraction/OCR quality, professional validation, source truth or Evidence status.

## Hermes skill inventory

For multi-container and Portainer deployments, the preferred candidate observation source is the authenticated read-only Hermes API:

```text
GET <HERMES_API_URL>/v1/skills
Authorization: Bearer <HERMES_API_SERVER_KEY>
```

The external network observer projects only whether the exact skill name is present and a bounded inventory count. It does not expose the full inventory or the API credential.

Target skill:

```text
pantheon-document-intake
```

Possible observations:

```text
installed_observed
not_listed_observed
not_observed
```

An invalid/unexpected API payload yields `not_observed`, not a guessed absence.

```text
skill listed != approved
skill listed != activated
skill listed != normal Hermes model/agent invocation proven
```

### Legacy/co-located observation

The earlier observer may still use the fixed native command:

```text
hermes skills list
```

when explicitly co-located with the Hermes CLI. It remains a valid local/offline adapter, but co-location is no longer required for the reference container deployment.

The command must remain fixed and shell-free; caller-provided command fragments are forbidden.

## Cockpit secret boundary

The OpenWebUI status Tool receives only:

```text
bounded observer URL
Cockpit read credential
```

The Tool must not receive:

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

The external observer may hold `HERMES_API_SERVER_KEY` and other read credentials server-side for its own bounded probes. Those credentials are not projected into the observation payload.

The OpenWebUI application may separately hold the Hermes API-server key for its normal server-to-server model connection. That does not grant the status Tool access to the key.

## Synthetic acceptance relationship

The external helper may consume the independent observations to determine only:

```text
candidate_ready_for_synthetic_intake = true | false
```

This is a technical prerequisite classification, not a safety or production verdict.

A synthetic intake remains explicitly operator-triggered and must use the installed Hermes skill transport plus the existing PEP/PDP path.

With the network-native observer, the Hermes inventory prerequisite may be observed over the private container network; CLI co-location is not required for that observation.

When authenticated issuer proof is explicitly required, the helper may additionally:

```text
operator signs the supplied synthetic human decision
-> installed skill receives a temporary signed decision
-> gateway/PEP derives the actual decision expectation
-> helper performs separate read-only PDP decision validation
   using that exact returned expectation
-> receipt records verdict + issuer_authenticated
```

Proof is valid only when:

```text
verdict = valid
issuer_authenticated = true
```

This proof does not authorize a Paperless external mutation and does not alter the current PDP V0 effect-denial posture.

## Operator-secret isolation

Issuer-signing and PDP secrets belong to the operator helper, not the Hermes skill.

The external implementation strips from the skill subprocess environment:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
```

```text
operator can prove issuer != skill owns issuer secret
```

## Phase B Portainer relationship

The external `pantheon-mvp#76` candidate adds `compose.phase-b.yaml` for an additive multi-stack deployment on external `ai-net`.

It does not recreate an existing OpenWebUI or SearXNG installation. The intended composition is:

```text
Pantheon policy stack
  pantheon-policy-api

external execution/document stack
  pgvector
  Docling
  Paperless + private broker/database
  Paperless gateway
  Cockpit API
  Hermes
  document-runtime network observer

existing OpenWebUI
  attached separately to ai-net
  server-to-server connection to Hermes
```

The specialized operator handoff is `docs/install/PORTAINER_PHASE_B_HANDOFF.md`.

```text
Compose file != deployed stack
container running != binding activated
OpenWebUI connected != real-dossier authorized
```

## Responsibility split

### Pantheon governs

- status vocabulary and non-equivalence rules;
- Task Contract scope;
- preflight/decision-validation semantics;
- configured issuer-signature verification;
- adoption/activation state;
- Knowledge/Evidence boundaries.

### Hermes executes

- the installed document skill externally;
- exposes read-only skill inventory to the bounded observer;
- no Pantheon authority function.

### OpenWebUI displays

- source-attributed observations;
- timestamps and `not_observed` states;
- no global health/safety verdict.

### Human approval remains required for

- target installation/adoption;
- activation;
- real-dossier use;
- target issuer-key provisioning;
- any future Paperless external mutation once policy permits it.

### Forbidden

- Pantheon running/scheduling the probes;
- observer installing/restarting/updating runtimes;
- `reachable -> healthy -> safe -> approved` promotion;
- fabricated Hermes installation from unrelated gateway status;
- fabricated policy authorization from `/readyz`;
- fabricated issuer authentication from registry configuration;
- treating synthetic receipts as Evidence;
- using the synthetic helper on a real client dossier.

## Current status

```text
external live-observation core          merged candidate in pantheon-mvp #73
network-native Hermes observer          merged candidate in pantheon-mvp #76
Phase B Portainer composition           merged candidate in pantheon-mvp #76
Paperless observation                   implemented candidate
Pantheon PDP readiness/meta observation implemented candidate
Docling health observation              implemented candidate
Hermes /v1/skills observation           implemented candidate / target not observed
legacy Hermes CLI observation           implemented candidate / co-location optional
OpenWebUI live projection               implemented candidate
synthetic read-only assessment          implemented candidate
optional synthetic intake helper        implemented candidate / not run on target
optional issuer-auth proof helper        implemented candidate / not run on target
target deployment                       not established
live target observations                not established
Hermes normal agent skill invocation    not proven
target issuer-authenticated decision    not proven
adoption                                not decided
activation                              not authorized
production                              forbidden pending separate review
```
