# AI intervention trace — Document runtime live observations

Date: 2026-07-24
Reconciled against current repositories: 2026-07-25
Status: validation-only trace
Boundary profile: validation_only_trace.

## Human direction

After the first read-only Document Runtime Status projection, the repository owner asked to continue and later explicitly warned that repository updates had landed before deployment.

The next bounded tranche remains independently sourced runtime observations plus an operator-run synthetic acceptance check. The later issuer-authentication implementation changes how the synthetic receipt is classified, but do not change the runtime/authority boundary.

## External implementation history

Historical implementation was `ifanjuang/pantheon-mvp#62`, merged into an intermediate branch rather than the final external `main`.

The slice has now been reconstructed on the real current main as:

```text
repository: ifanjuang/pantheon-mvp
replacement: #73 merged
observer: mvp_vertical.document_runtime_observer
Cockpit: openwebui/pantheon_document_runtime_live_status.py
synthetic helper: scripts/document_runtime_synthetic_check.py
```

## Observation sources

```text
Paperless / gateway -> bounded gateway /health
Pantheon PDP        -> /readyz + /v1/meta
Docling Serve       -> /health
Hermes skill        -> fixed native `hermes skills list` when explicitly co-located
```

Every observation retains its own `source`, `observation_source` and `observed_at`.

The aggregate explicitly reports:

```text
synthetic_global_health = not_computed
authority_effect = none
write_effect = false
activation_changed = false
```

## Issuer-authentication reconciliation

The historical slice could only declare issuer authentication unproven. Repository updates #473 and external #66 added a PDP verifier and matching signing producer.

Replacement #73 therefore supports an optional operator proof:

```text
human-supplied synthetic decision
-> operator helper signs bounded decision fields
-> installed Hermes skill receives a temporary signed decision
-> gateway/PEP returns its derived decision expectation
-> helper calls PDP decisions:validate read-only with that exact expectation
-> receipt records verdict + issuer_authenticated
```

Proof becomes true only when:

```text
verdict = valid
issuer_authenticated = true
```

Preserved distinctions:

```text
issuer_authenticated != approval
valid decision verdict != effect authorized
runtime success != Evidence
synthetic pass != production adoption
```

Current PDP V0 external/canonical denial is unchanged by issuer proof.

## Secret isolation hardening

The replacement helper explicitly strips operator-only secrets from the skill subprocess environment:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
```

The skill retains only its bounded normal gateway/runtime inputs.

## Status after reconciliation

```text
external observer code                  merged candidate in pantheon-mvp #73
Paperless observation                   implemented candidate
Pantheon PDP readiness/meta observation implemented candidate
Docling health observation              implemented candidate
Hermes native inventory observation     implemented candidate / co-location required
OpenWebUI live projection               implemented candidate
synthetic read-only assessment          implemented candidate
optional synthetic intake helper        implemented candidate / not run on target
optional issuer-auth proof helper        implemented candidate / not run on target
target deployment                       not established
live observations                       not established
target issuer-authenticated decision    not proven
Hermes normal agent invocation          not proven
activation                              not authorized
production                              forbidden
```

This trace creates no authority and records no target-runtime health claim.
