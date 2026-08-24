# Document Runtime Live Observations

Status: candidate support doctrine — co-located implementation merged / target deployment not established.
Boundary profile: candidate_support_note.

This document governs live observations for the document vertical.

Current candidate source:

```text
Pantheon implementation: implementation/
preferred observer: implementation/mvp_vertical/document_runtime_network_observer.py
Cockpit projection: implementation/openwebui/pantheon_document_runtime_live_status.py
core Compose: implementation/compose.phase-b.yaml
optional Paperless overlay: implementation/compose.paperless.yaml
```

Historical lineage remains traceable through former `pantheon-mvp` PRs #73, #76, #84 and #85. Those references are provenance only after the monorepo import.

Repository implementation does not establish that any target host runs these components.

## Boundary

```text
OpenWebUI exposes source-attributed observations.
Pantheon implementation observers read bounded technical surfaces.
Hermes reports runtime/skill inventory through reviewed read-only surfaces.
Local/NAS governed source ingestion remains available in the core.
Paperless is observed only when its optional binding is selected.
Docling reports its own health endpoint when selected.
Pantheon PDP reports policy readiness/meta and validates bounded decisions.
Pantheon governance defines status semantics, gates and activation.
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
overlay selected != binding activated
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

## Document-source binding selection

The implementation observer uses one explicit binding value:

```text
MVP_DOCUMENT_SOURCE_BINDING=governed_local_source   # core default
MVP_DOCUMENT_SOURCE_BINDING=paperless_ngx           # optional DMS binding
```

An unknown value is not interpreted optimistically. It is classified as an unsupported binding with runtime state left `not_observed`.

```text
binding string != dependency adoption
binding selected != activation
```

## Core local/NAS document path

With the default:

```text
MVP_DOCUMENT_SOURCE_BINDING=governed_local_source
```

the observer does not call the Paperless gateway.

Paperless is projected as an optional binding that is not selected:

```text
source = document_source_management
observation_source = binding_configuration
selected_binding = governed_local_source
Paperless selection_status = not_selected
installation_status = not_applicable
reachability_status = not_applicable
health_status = not_applicable
```

This is a valid core installation state, not a degradation.

Core ingestion continues through the declared local/NAS source path:

```text
read-only governed source root
-> Task Contract declared-source check
-> path-boundary check
-> source digest
-> reviewed extraction such as Docling when selected
-> Project Document candidate
```

```text
Paperless observation status != document ingestion capability status
```

## Optional Paperless observation

When:

```text
MVP_DOCUMENT_SOURCE_BINDING=paperless_ngx
```

the bounded observation source becomes:

```text
GET <PANTHEON_PAPERLESS_GATEWAY_URL>/health
```

The returned observation is explicitly qualified as:

```text
capability = document_source_management
binding = paperless_ngx
selection_status = selected
```

Only in this selected state may an unavailable gateway be classified as unreachable/degraded for that binding.

```text
selected binding failure != whole Pantheon unsafe
```

## Pantheon PDP

Observation surfaces:

```text
GET /readyz
GET /meta
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

The Paperless-specific `pantheon-document-intake` skill is relevant only when `paperless_ngx` is selected and configured.

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

Current deployment composition is one reviewed Pantheon Next revision with two implementation Compose files:

```text
implementation/compose.phase-b.yaml
  core only
  pgvector
  Docling when selected
  Cockpit API
  Hermes
  network observer
  default binding = governed_local_source

implementation/compose.paperless.yaml
  optional overlay
  Paperless broker
  Paperless DB
  Paperless-ngx
  Paperless gateway
  Hermes Paperless binding overrides
  observer binding = paperless_ngx
```

Former `pantheon-mvp#85` remains provenance for the overlay split. It is not a second deployment source.

The core file contains no Paperless-only required image/path/secret substitutions. Therefore an installation that does not select Paperless does not need to provide Paperless deployment variables merely to parse/start the core Compose model.

Existing OpenWebUI/SearXNG are reused separately.

```text
overlay absent != degraded
overlay included != binding activated
Paperless variables absent from core != configuration error
```

## Responsibility split

### Pantheon governance

- status vocabulary and Capability Slot selection semantics;
- Task Contract scope;
- preflight/decision-validation semantics;
- adoption/activation state;
- Knowledge/Evidence boundaries.

### Pantheon implementation

- bounded document-runtime observer;
- Paperless gateway/adapter candidate;
- read-only cockpit projection;
- source-attributed runtime observations.

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
network observer                     co-located implementation candidate
optional Paperless semantics         co-located implementation candidate; historical origin #84
separate Paperless Compose overlay   co-located implementation candidate; historical origin #85
core local/NAS ingestion             implementation candidate / target not observed
Paperless binding                    optional / preferred / default-off
Paperless target installation        not established
live target observations             not established
activation                           not authorized
production                           forbidden pending separate review
```

```text
co-location != target deployment
runtime success != Evidence
projection != persistence
```
