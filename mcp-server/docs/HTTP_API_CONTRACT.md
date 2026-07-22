# Pantheon Policy HTTP API Contract

Status: implementation candidate — implemented read-only / partial / internal-network adapter; protected review required.

This document defines the HTTP projection of the transport-neutral Pantheon policy service.

```text
OpenWebUI exposes.
Hermes Agent executes and enforces.
Pantheon Next governs.
The human decides consequential effects.
```

The API is a Policy Decision Point projection. It returns policy, validation and candidate data. It is not an execution runtime, Policy Enforcement Point, approval engine, evidence store, memory engine, scheduler, queue, provider router, installer, updater, MCP host or connector gateway.

## Transport placement

```text
Pantheon policy modules
        ↓
PantheonPolicyService        one transport-neutral meaning
        ├── FastMCP stdio    agent-native consultation
        └── FastAPI HTTP     deterministic runtime preflight and service integration
```

MCP and HTTP must not implement separate policy logic. For a given operation and input, the operation-specific fields must remain semantically equivalent across the core service, MCP and HTTP projections.

## Common response fields

Every service projection includes, unless an older bounded contract already supplies the equivalent field:

```yaml
contract: pantheon.policy.v1
operation:
source_mode:
authority_effect: none
authorization_effect: none
write_effect: false
execution_effect: false
evaluated_at:
repository:
  version:
  commit:
input_sha256:
```

`input_sha256` is a reproducibility aid. It is not Evidence and does not establish truth, approval or runtime success.

## Authentication and network boundary

All `/v1/*` routes and compatibility policy routes require:

```http
Authorization: Bearer <PANTHEON_POLICY_API_KEY>
```

If no server key is configured, the API fails closed with HTTP `503`. An invalid or missing client credential returns HTTP `401`.

The candidate Compose deployment:

- joins only the external Docker network `ai-net`;
- publishes no host port;
- mounts the Pantheon checkout read-only;
- uses a read-only container filesystem and a bounded `/tmp` tmpfs;
- drops all Linux capabilities;
- applies `no-new-privileges`;
- receives no Docker socket and no external credentials other than its consultation key.

## Health surfaces

### `GET /livez`

Process liveness only.

### `GET /readyz`

Checks that the governed checkout can be read and identified. It does not establish safety, approval or professional readiness.

```text
ready != safe
healthy != authorized
```

### `GET /health`

Compatibility health response. New operators should use `/livez` and `/readyz` separately.

## Metadata and repository state

### `GET /v1/meta`

Returns the API mode, implemented surfaces, policy version and non-equivalence reminders.

### `GET /v1/repository/state`

Returns a read-only observation of the mounted checkout and its declared version/commit.

```text
repository readable != runtime healthy
repository current != binding adopted
```

## Consultation routes

```text
GET /v1/consultation
GET /v1/sources
GET /v1/sources/{key}
GET /v1/architecture/{topic}
```

Source lookup remains allowlisted. A source key never becomes an arbitrary repository path.

## Policy classification

### `POST /v1/policy/requests:classify`

Classifies a caller-provided request using the governed consequence, verification and approval axes.

Typical output fields:

```yaml
result: classified
consequence_level: K0 | K1 | K2 | K3 | K4
required_verification: V0 | V1 | V2 | V3 | V4
required_approval_ceiling: C0 | C1 | C2 | C3 | C4 | C5
task_contract_required:
evidence_required:
blocked_until_gate:
required_gates: []
```

Classification is not authorization.

## Deterministic preflight

### `POST /v1/policy/preflights:evaluate`

Input:

```yaml
request:
  intent:
  external_effect:
  writes_state:
  transmission_requested:
  memory_promotion_requested:
  professional_position:
  financial_or_contractual_effect:
  scope:
    scope_type:
    scope_id:
gate_signals:
  task_contract_ref:
  evidence_pack_candidate_ref:
  human_decision_ref:
  human_decision_level:
```

The gate signals are caller-provided references. V0 does not authenticate their issuer, digest, scope or currentness.

Possible dispositions:

```text
blocked_invalid_request
blocked_pending_scope
blocked_pending_task_contract
blocked_pending_evidence
blocked_pending_human_decision
eligible_for_candidate_work
eligible_with_gate_signals_unverified
```

The V0 response always contains:

```yaml
external_effect_allowed: false
canonical_effect_allowed: false
gate_signal_validation_performed: false
authorization_effect: none
```

Thus the preflight can permit continued preparation of candidate work while still requiring the external runtime to block transmission, canonical mutation, memory promotion or other consequential effects.

## External action check

### `POST /v1/policy/external-actions:check`

Input:

```yaml
description: "..."
```

Returns the blocked-by-default legitimacy path. It never performs the action.

## Capability observation qualification

### `POST /v1/observations/capabilities:qualify`

Qualifies a caller-provided status observation. It performs no runtime inventory or live probe and preserves:

```text
installed != approved
healthy != safe
update_available != update_authorized
runtime_success != evidence
```

## Candidate preparation

```text
POST /v1/candidates/task-contracts:prepare
POST /v1/candidates/evidence-packs:prepare
```

These routes prepare review objects only. They do not create executable authority, approve Evidence or write the Registre Probatoire.

## Validation and provided-evidence verification

```text
POST /v1/validations/passports
POST /v1/validations/apu-dossiers
POST /v1/verifications/install
POST /v1/verifications/observability
POST /v1/verifications/backup
POST /v1/verifications/exposure
POST /v1/verifications/update
POST /v1/verifications/profiles:load
GET  /v1/doctor
```

The verification routes classify only the evidence supplied by the caller. They do not probe the NAS, fetch versions, open ports, run backups or query monitoring systems.

`POST /v1/verifications/profiles:load` validates a caller-provided verification profile and projects a read-only evidence-gathering plan. The retained technical schema identifier `verification_preset` is historical and distinct from the installation preset model removed by the common installation baseline.

```text
verification profile != installation preset
profile validated != verification executed
plan produced != evidence gathered
```

## Context Pack split

Pantheon does not expose a generic current context through `GET /runtime/context-pack`.

### `POST /v1/context-packs:plan`

Returns the boundaries and missing fields for a producer that will assemble a scoped Context Pack candidate.

Pantheon states the constraints. Hermes or another governed producer gathers the actual context.

### `POST /v1/context-packs:validate`

Validates one caller-provided candidate against `schemas/context_pack.schema.yaml`.

```text
schema valid != authorized context
context included != evidence accepted
retrieved != true
```

## Compatibility routes

### `POST /domain/approval/classify`

Temporary alias of `POST /v1/policy/requests:classify`. It classifies the approval ceiling; it does not approve.

### `POST /v1/verifications/presets:load`

Deprecated compatibility alias of `POST /v1/verifications/profiles:load`. The word `preset` here refers only to the retained legacy schema identifier `verification_preset`; it must not be interpreted as the retired installation-composition preset model.

### `GET /runtime/context-pack`

Returns HTTP `501 contract_not_defined` and points to the explicit Context Pack planning and validation routes.

### `GET /domain/snapshot`

Returns HTTP `501 contract_not_defined`. `snapshot` is intentionally not treated as a single object. Callers must request an explicit repository state, capability observation qualification or future typed domain object.

## Failure posture in Hermes

The API itself returns policy data. Hermes remains the Policy Enforcement Point.

Recommended adapter behavior:

```text
non-consequential consultation unavailable
  -> continue only in visible degraded mode

consequential preflight unavailable
  -> fail closed
  -> block external and canonical effects
  -> report Pantheon policy service unavailable
```

No silent fallback from HTTP preflight to model judgment is permitted for a consequential effect.

## Body and documentation limits

The default maximum request body is 256 KiB and can be reduced with `PANTHEON_POLICY_MAX_BODY_BYTES`.

OpenAPI and Swagger are disabled by default. They may be enabled only in a bounded development environment with `PANTHEON_POLICY_ENABLE_DOCS=1`.

Request bodies and bearer credentials must not be written to logs. Uvicorn access logging is disabled by default.

## Human decision boundary

The API does not create or persist a human approval. A future reviewed gate-validation slice may validate a caller-provided decision reference against its scope, digest, approval level, expiry and object identity. The decision itself remains external to this service.

## Final rule

```text
MCP helps the agent understand and prepare.
HTTP lets the runtime enforce a deterministic preflight.
Hermes performs the work outside Pantheon.
OpenWebUI exposes the state and decision surface.
The human decides consequential effects.
Neither transport becomes authority, evidence or runtime.
```
