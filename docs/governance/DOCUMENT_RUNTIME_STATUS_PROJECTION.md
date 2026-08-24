# Document Runtime Status Projection

Status: candidate support doctrine — co-located read-only implementation candidate exists / not installed.

This document defines how the Pantheon Cockpit may expose document-runtime observations without turning them into installation, health, safety, approval or activation claims.

Current candidate source:

```text
Pantheon implementation: implementation/
surface: implementation/openwebui/pantheon_document_runtime_live_status.py
historical source slices: former pantheon-mvp #61 and clean reapplication #72
```

Those former PR identifiers remain repository-history provenance only. Neither repository presence nor a merged implementation establishes installation or target runtime health.

This document does not implement a runtime monitor, install a probe, create a health authority, activate a capability or aggregate unrelated observations into one global status.

## Core rule

```text
observation source -> observed field
Pantheon governance -> classification/status semantics
Cockpit -> display
human -> consequential decision
```

No component may infer a stronger state than its observation supports.

```text
reachable != healthy
healthy != safe
installed != approved
skill name known != skill installed
skill installed != task authorized
gateway healthy != PDP reachable
PDP reachable != effect authorized
issuer authentication implementation != issuer authenticated on target
issuer_authenticated != approval
runtime success != Evidence
runtime observation != activation decision
```

## First status-card slice

The first candidate reads only the bounded Paperless gateway health projection.

It may display:

```text
Paperless reachability
Paperless gateway service status
Project Document intake surface status
native Paperless write surface status
```

It must display the following as explicitly unobserved when no independent source has been connected:

```text
Hermes skill installation
Pantheon PDP reachability/health
Docling reachability/health
capability activation/adoption
```

`not_observed` is an intentional status, not a defect to fill with inference.

## Observation source map

| Field | Required observation source | First-slice status |
|---|---|---|
| Paperless reachability | bounded Paperless gateway probe | implemented candidate under `implementation/` |
| Paperless health | dedicated reviewed Paperless health observation | not established by simple reachability |
| Paperless safety | governance/security review | never inferred from health |
| Paperless gateway status | gateway response | implemented candidate under `implementation/` |
| Hermes `pantheon-document-intake` installed | Hermes native skill inventory | not connected in first slice |
| Hermes skill enabled/usable | Hermes native runtime observation + binding config | not connected |
| Pantheon PDP reachable | Pantheon policy service observation | not connected in first slice |
| Pantheon effect posture | exact PDP preflight response for the proposed effect | evaluated at effect time, not inferred by card |
| issuer authenticated for a decision | exact decision-validation result under configured issuer registry | effect/decision-time fact, not inferred by card |
| Docling reachable/healthy | reviewed Docling runtime observation | not connected |
| binding activation | Pantheon governed status + human decision | never inferred from runtime probes |

## Why the gateway cannot report everything

The Paperless gateway is authoritative only for its own bounded observations.

It is not the source of truth for:

```text
Hermes native skill inventory
Pantheon policy health
Pantheon issuer registry state
Docling health
human approval
capability activation
```

A future cockpit aggregation may combine these fields, but every field must retain:

```text
observation source
observed_at
evidence/reference when available
status vocabulary
```

The aggregate view must not collapse them into one Boolean `healthy` or `ready` flag.

## Paperless status semantics

A successful gateway probe may establish only:

```text
Paperless reachability = reachable
```

It does not establish:

```text
Paperless health = healthy
Paperless safety = safe
backup = valid
restore = proven
binding = activated
real-dossier scope = authorized
```

If the gateway cannot reach Paperless:

```text
reachability = unreachable
```

The cockpit may show degradation, but it must not silently switch to NAS or another source runtime.

## Hermes skill status semantics

Knowing the selected binding name:

```text
pantheon-document-intake
```

does not prove that Hermes has installed it.

The installation state must come from Hermes native inventory or another reviewed Hermes observation adapter.

```text
binding selected != skill installed
skill installed != skill healthy
skill healthy != capability approved
```

The Paperless gateway must not fabricate this field from successful HTTP calls.

## Pantheon PDP status semantics

The status card must not derive policy authorization from gateway health.

Current effect authorization remains evaluated by the PEP using the exact preflight response for the proposed effect.

For the current PDP V0:

```text
external_effect_allowed = false
canonical_effect_allowed = false
```

This is an effect-time policy observation, not a static runtime health field.

The PDP may additionally authenticate a bounded human decision issuer when an operator-managed read-only issuer registry is configured. That fact also belongs to the exact decision-validation result, not to generic runtime health.

```text
issuer_authenticated != approval
valid decision verdict != effect authorized
```

## Docling status semantics

Paperless reachability says nothing about Docling.

```text
Paperless reachable != Docling reachable
Docling reachable != extraction quality validated
```

Until a reviewed Docling runtime observation is connected, the card must show its status as `not_observed` or `not_established`.

## Security boundary

The first OpenWebUI status card may receive only the bounded Cockpit read credential needed for the gateway observation.

It must not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
MVP_HERMES_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
issuer signing secret
Paperless database credentials
```

Status projection must not become a secret-discovery surface.

## No authority effect

Rendering the card has no consequential effect.

```text
write_effect = false
authority_effect = none
activation_changed = false
```

The card cannot approve, install, enable, update, roll back, publish Knowledge or admit Evidence.

## Capability state

```text
capability: document_runtime_status_projection
Pantheon implementation: candidate under implementation/
historical origin: former pantheon-mvp #72 (source slice #61)
Paperless reachability observation: implemented candidate
Hermes native inventory binding: documented non-implemented in this first slice
Pantheon PDP observation binding: documented non-implemented in this first slice
Docling health observation binding: documented non-implemented in this first slice
installation: not established
activation: not authorized
production adoption: not decided
```

## Responsibility map

```text
Pantheon governance
  status vocabulary
  non-equivalence rules
  activation/adoption semantics

Pantheon implementation
  bounded observer and status projection code

OpenWebUI exposes
  read-only status cards

Hermes executes
  nothing because of this status card
  native inventory remains an external observation source

Paperless gateway observes
  bounded Paperless reachability and its own surface status

Human decides
  activation/adoption and consequential remediation

Forbidden
  synthetic global healthy flag
  reachability -> safety promotion
  guessed Hermes installation state
  guessed PDP authorization
  guessed issuer authentication
  hidden fallback source runtime
  secret exposure
  automatic activation
```

```text
projection != persistence
co-location != authority transfer
runtime success != Evidence
```
