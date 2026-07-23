# 2026-07-23 — Gate-validation slice implemented (mcp-server)

Status: validation-only intervention trace.
Boundary profile: implementation_artifact.

## Change

Implemented the gate-validation slice in the read-only policy service — Phase E
of `docs/roadmaps/PLATFORM_IMPLEMENTATION_ROADMAP.md`. This is code, not only
documentation: it turns the preflight's `gate_signal_validation_performed: false`
presence check into a real content check a Policy Enforcement Point can call.

```text
mcp-server/pantheon_mcp/gate_validation.py   new pure validator (read-only)
mcp-server/pantheon_mcp/service.py           validate_decision operation
mcp-server/pantheon_mcp/server.py            validate_decision MCP tool
mcp-server/pantheon_mcp/http_api.py          POST /v1/policy/decisions:validate
mcp-server/tests/test_gate_validation.py     12 tests
mcp-server/README.md                         tool + layout
mcp-server/docs/HTTP_API_CONTRACT.md         Human decision validation section
```

## What it does

Given a caller-provided decision reference and the requirement the effect must
satisfy, it validates: structural completeness, a human signer (system / service
/ runtime signers refused), expiry, scope match, approval-ceiling sufficiency,
object identity and content digest. It returns `verdict: valid | invalid` with a
per-check map.

## Boundary held

```text
verdict valid != approval
validated reference != authenticated issuer
gate signal validated != effect authorized
```

Read-only and side-effect free: it fetches nothing, persists nothing,
authenticates no issuer cryptographically and approves nothing. `write_effect`
and `execution_effect` stay false and `authorization_effect` stays `none`. The
human decision remains external to this service.

## Verification

```text
mcp-server suite: 191 tests pass (was 179; +12)
packaging contract: OK (0.1.64)
```

## Not done here (bounded on purpose)

Preflight still reports its own signals unverified; wiring a validated decision
back into `evaluate_preflight` is a separate reviewed step. No CLI entry or new
schema file was added. No live Hermes binding, deployment, adoption or activation
is introduced; `mcp-server/` remains a protected read-only surface.
