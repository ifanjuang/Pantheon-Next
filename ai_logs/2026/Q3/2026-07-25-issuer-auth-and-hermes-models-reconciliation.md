# 2026-07-25 — Human issuer authentication and Hermes integration reconciliation

Status: validation-only intervention trace.
Boundary profile: implementation_artifact.

## Change

Two related changes closing the gaps surfaced while reviewing the parallel Codex
programmes (Paperless intake stack and Cockpit V2 / execution admission bridge).

### (d) Human issuer authentication — code

Closes the `validated decision fields != authenticated human issuer` gap that
`mcp-server` gate-validation and the external Paperless PEP both left OPEN.

```text
mcp-server/pantheon_mcp/gate_validation.py  issuer signature verification (HMAC over signed fields)
mcp-server/pantheon_mcp/service.py          read-only issuer key registry from PANTHEON_DECISION_ISSUER_KEYS_PATH
mcp-server/tests/test_gate_validation.py     5 new tests (17 total)
README.md, HTTP_API_CONTRACT.md              document the check
```

When an issuer key registry is configured, the decision must carry a signature
over `decision_id, decided_by, approval_level, scope, object_identity,
content_digest, expires_at` that verifies against the registered key for
`decided_by` → `issuer_authenticated: true`. Missing / unknown-issuer /
non-verifying signature fails the verdict. No registry → `issuer` is
`not_checked` and the issuer stays asserted-but-unauthenticated (pre-existing
behaviour preserved). Read-only; the secret is never returned in a projection.

### (a) Hermes integration models reconciliation — doctrine

`docs/governance/HERMES_INTEGRATION_MODELS_RECONCILIATION.md` fixes how the two
Hermes-integration models compose as layers, not competitors:

```text
Execution Admission = bounded permission to START a run (which Work Issue, version, ttl, effect class)
Chokepoint          = per-effect policy gate DURING the run (is this effect allowed?)
admission granted  != effect authorized
```

Indexed in `RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`.

## Verification

```text
mcp-server suite: 196 tests pass (was 191; +5)
```

## Boundary

```text
issuer_authenticated != approval        (who decided, not permission)
no registry configured != issuer proven
admission != effect authorization
```

No runtime, live Hermes binding, deployment, adoption or activation is
introduced. `mcp-server/` remains a protected read-only surface; the human
decides consequential effects.
