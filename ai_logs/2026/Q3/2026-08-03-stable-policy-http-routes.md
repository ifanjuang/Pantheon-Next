# Stable Pantheon Policy HTTP routes

Date: 2026-08-03

Status: applied implementation refactor — internal route identity only.

## Context

The architecture convergence plan orders the bounded read-only MCP HTTP projection as the first pilot for removing internal generation-prefixed routes.

The previous audit reported nine direct decorator routes under `/v1`, but `mcp-server/pantheon_mcp/http_api.py` also declared sixteen routes through static operation tables. The mounted application therefore exposed twenty-five internal policy routes under the generation prefix.

## Change

All Pantheon Policy HTTP routes now use stable responsibility paths, for example:

```text
/v1/meta                         -> /meta
/v1/repository/state             -> /repository/state
/v1/policy/requests:classify     -> /policy/requests:classify
/v1/context-packs:validate       -> /context-packs:validate
```

The old `/v1` routes are removed in the same change. No compatibility alias is added.

Tests, transport contracts, the Hermes binding blueprint and active operator/observation documents are updated atomically.

A mounted-route test now inspects the composed FastAPI application so routes declared through tables cannot escape the generation-prefix guard.

## Preserved revisions

The migration does not rename legitimate contract or protocol revisions:

```text
pantheon.policy.v1
pantheon.consultation.v1
FastAPI application version 1.0.0-candidate
external Hermes /v1/models and /v1/skills
```

## Boundaries

```text
route identity != contract revision
stable route != frozen payload semantics
route migration != authority change
HTTP response != authorization
runtime_success != Evidence
```

No policy meaning, Evidence state, approval rule, scope rule, execution behavior or human-decision boundary is changed.
