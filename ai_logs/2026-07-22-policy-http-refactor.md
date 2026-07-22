# Policy HTTP adapter refactor

Status: validation-only trace — implementation refactor; not authority.

Date: 2026-07-22

## Scope

Refactor the bounded Pantheon Policy HTTP adapter without removing routes, tools or governance functions.

## Changes

- added bounded ASGI request-body middleware instead of mutating Starlette private request internals;
- added request correlation through `X-Request-ID`, `X-Pantheon-Request-ID` and response `request_id`;
- registered trivial GET/POST projections from explicit allowlisted route tables;
- kept policy preflight, scoped source routes, Context Pack routes and compatibility routes explicit;
- removed the internal checkout path from the HTTP repository-state projection;
- extended HTTP acceptance tests for correlation and path redaction.

## Validation

Head `232dd75466cf53184871590a19fdb619f576dcf5`:

- Governance CI run `29939850505`: success;
- Obsolete Authority Consistency run `29939849747`: success;
- MCP/HTTP module tests: success;
- read-only governance checks: success;
- packaging and clean wheel installation: success.

## Boundary

```text
request_id != evidence
route registration != dynamic authority
HTTP projection != execution
ready != safe
implemented != installed
```

The refactor does not install, activate, approve, execute, send, schedule, route providers, update or promote memory.
