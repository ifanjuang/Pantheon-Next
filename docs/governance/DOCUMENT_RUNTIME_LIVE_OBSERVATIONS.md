# Document Runtime Live Observations

Status: candidate support doctrine — external implementation merged / target deployment not established.
Boundary profile: candidate_support_note.

This document governs live observations for the document vertical.

Current external implementation:

```text
repository: ifanjuang/pantheon-mvp
live observation core: #73 merged
network-native observer: #76 merged
optional Paperless profile/semantics: #84 merged
preferred observer: mvp_vertical.document_runtime_network_observer
Cockpit projection: openwebui/pantheon_document_runtime_live_status.py
```

Repository implementation does not establish that any target host runs these components.

## Boundary

```text
OpenWebUI exposes source-attributed observations.
External observers read bounded technical surfaces.
Hermes reports runtime/skill inventory through reviewed read-only surfaces.
Paperless is observed only when its optional binding is selected.
Docling reports its own health endpoint when selected.
Pantheon PDP reports policy readiness/meta and validates bounded decisions.
Pantheon governs status semantics, gates and activation.
The human decides consequential activation and use.
```

## Required non-equivalences

```text
Paperless absent != Pantheon degraded
Paperless absent != document ingestion unavailable
Paperless not selected != Paperless unreachable
reachable != healthy
healthy != safe
installed != approved
skill listed != skill activated for scope
PDP ready != effect authorized
issuer_authenticated != approval
Docling health endpoint responds != extraction quality established
runtime success != Evidence
runtime observation != activation decision
synthetic check pass != production adoption
compose present != target deployed
```

No aggregate global green/red health score is computed.

## Observation record minimum

```yaml
source:
observation_source:
observed_at:
reachability_status:
```

Aggregate:

```yaml
synthetic_global_health: not_computed
authority_effect: none
write_effect: false
activation_changed: false
```

## Optional Paperless observation

Selection signal:

```text
PANTHEON_PAPERLESS_BINDING_SELECTED=false | true
```

When not selected, the observer must not call the Paperless gateway and reports:

```text
source = paperless_gateway
observation_source = binding_selection
binding_status = not_selected
installation_status = not_applicable
reachability_status = not_applicable
health_status = not_applicable
```

This is a valid installation state.

When selected, the bounded observation source becomes:

```text
GET <PANTHEON_PAPERLESS_GATEWAY_URL>/health
```

Only then may an unavailable gateway be classified as unreachable/degraded for that selected binding.

```text
selected binding failure != whole Pantheon unsafe
```

## Core local/NAS document path

The observer's Paperless status does not determine whether governed document ingestion exists.

Core ingestion can use a declared local/NAS source through the Task Contract, path-boundary and digest pipeline.

```text
Paperless observation status != document ingestion capability status
```

## Pantheon PDP

Observation surfaces:

```text
GET /readyz
GET /v1/meta
```

`/readyz` is readiness of the policy projection, not authorization of a concrete effect.

Current V0 posture remains:

```text
external_effect_allowed = false
canonical_effect_allowed = false
```

Issuer authentication is decision-time data and must not be inferred from generic readiness.

```text
configured issuer registry != issuer authenticated
issuer_authenticated != approval
valid decision verdict != effect authorized
```

## Docling

When the reviewed Docling binding is selected:

```text
GET <DOCLING_SERVE_URL>/health
```

A responding endpoint does not establish extraction quality, professional validation, source truth or Evidence status.

## Hermes skill/runtime inventory

Preferred container observation:

```text
GET <HERMES_API_URL>/v1/skills
Authorization: Bearer <HERMES_API_SERVER_KEY>
```

Possible skill inventory observations:

```text
installed_observed
not_listed_observed
not_observed
```

The Paperless-specific `pantheon-document-intake` skill is relevant only when that binding is selected.

```text
skill listed != approved
skill listed != activated
skill listed != normal Hermes model/agent invocation proven
```

Legacy/co-located fixed CLI observation may remain available for local/offline use.

## Cockpit secret boundary

The status Tool receives only the bounded observer URL and Cockpit read credential.

It does not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
MVP_HERMES_API_KEY
HERMES_API_SERVER_KEY
issuer signing/key-registry secrets
DOCLING_SERVE_API_KEY
Paperless database credentials
```

The observer may hold required read credentials server-side; it does not project them.

## Synthetic acceptance relationship

Core/local-source acceptance and Paperless binding acceptance are separate proofs.

```text
core local/NAS ingestion proof
  validates declared source / path / digest / Project Document path

Paperless exact-version synthetic proof
  applies only when document_source_management -> paperless_ngx is selected
```

The existing Paperless synthetic helper must not make an unselected Paperless capability look like a failed core acceptance.

Authenticated issuer proof remains separate from both:

```text
issuer_authenticated != approval
valid decision verdict != effect authorized
```

## Phase B Portainer relationship

External `pantheon-mvp#84` keeps `compose.phase-b.yaml` as one architecture with optional service presence:

```text
core
  pgvector
  Docling when selected
  Cockpit API
  Hermes
  network observer

profile paperless
  Paperless broker
  Paperless DB
  Paperless-ngx
  Paperless gateway
```

Existing OpenWebUI/SearXNG are reused separately.

```text
profile absent != degraded
profile enabled != binding activated
```

## Responsibility split

### Pantheon governs

- status vocabulary and Capability Slot selection semantics;
- Task Contract scope;
- preflight/decision-validation semantics;
- adoption/activation state;
- Knowledge/Evidence boundaries.

### Hermes executes

- core governed work;
- Paperless-specific skill only when selected/configured;
- no Pantheon authority function.

### OpenWebUI displays

- source-attributed observations;
- explicit `not_selected/not_applicable` states;
- no global safety verdict.

### Human approves

- optional Paperless installation/selection;
- binding activation;
- real-dossier use;
- future consequential Paperless effects.

## Current status

```text
network observer                     external implementation merged
optional Paperless semantics         external implementation merged in #84
core local/NAS ingestion             external implementation candidate / target not observed
Paperless binding                    optional / preferred / default-off
Paperless target installation        not established
live target observations             not established
activation                           not authorized
production                           forbidden pending separate review
```
