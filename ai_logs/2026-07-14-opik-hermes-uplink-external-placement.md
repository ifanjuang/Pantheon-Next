# Opik and Hermes Uplink external placement

Date: 2026-07-14

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Updated: `docs/governance/EXTERNAL_TOOL_PLACEMENT_REGISTER.md`.
- Added: a Capability Slot and bounded Langfuse comparison target for `comet-ml/opik`.
- Added: a refusal-as-integration / UX-reference-only placement for `mr-september/hermes-uplink`.
- Removed: nothing.

## Why

The two repositories expose different capabilities and must not be treated as interchangeable additions to Pantheon Next.

Opik may support external runtime observability and evaluation, but its traces, scores and optimizers cannot become proof, approval or automatic mutation authority.

Hermes Uplink provides a mobile thin-client pattern, but adopting it would add a parallel Hermes access surface outside the governed OpenWebUI cockpit and could bypass the consequential chokepoint.

The human decision for this intervention was to document the placement only. It did not authorize installation, activation, cloud transfer, configuration, gateway restart, tunnel exposure or runtime integration.

## Sources reviewed

- `https://github.com/comet-ml/opik` — repository, README, SDK description and self-hosted deployment composition; retrieved 2026-07-14.
- `https://www.comet.com/docs/opik/integrations/opentelemetry` — generic OpenTelemetry ingestion surface; retrieved 2026-07-14.
- `https://www.comet.com/docs/opik/integrations/openwebui` — OpenWebUI Pipeline integration surface; retrieved 2026-07-14.
- `https://github.com/mr-september/hermes-uplink` — repository, proxy, launcher and security boundary; retrieved 2026-07-14.
- Official Hermes dashboard and remote-surface documentation reviewed 2026-07-14.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: no promotion; the placement register remains active support and the tool records remain candidate/reference decisions.
Schema/test/CI impact: none.
External action: GitHub documentation branch and PR only; no external tool was contacted through Pantheon runtime.
Memory behavior: none.

## Local distinctions

```text
installed != approved
trace_recorded != evidence
evaluation_score != approval
prompt_optimized != prompt_authorized
reference_visibility != adoption
remote_access_success != governed_access
```

## Remaining verification

- No native Hermes-to-Opik binding was verified.
- Opik versus Langfuse remains a future bounded comparison, not an adopted implementation.
- Current container, retention, access-control, backup and rollback requirements remain untested.
- Hermes Uplink compatibility with the current containerized environment remains unverified and is not required while the integration is refused.
