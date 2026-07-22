# Policy transport adapter refactor

Status: validation-only trace — implementation refactor; not authority.

Date: 2026-07-22

## Scope

Refactor the bounded Pantheon Policy HTTP and MCP adapters without removing routes, tools, resources or governance functions.

## HTTP changes

- added bounded ASGI request-body middleware instead of mutating Starlette private request internals;
- added request correlation through `X-Request-ID`, `X-Pantheon-Request-ID` and response `request_id`;
- registered trivial GET/POST projections from explicit allowlisted route tables;
- kept policy preflight, scoped source routes, Context Pack routes and compatibility routes explicit;
- removed the internal checkout path from the HTTP repository-state projection;
- extended HTTP acceptance tests for correlation and path redaction.

## MCP changes

- retained explicit named tool functions and signatures for MCP discovery;
- centralized the repeated YAML mapping parse/error/projection path;
- reused one lazy read-only `PantheonPolicyService` instance per stdio process;
- centralized service invocation while preserving the historical `list_sources` array response;
- kept resource registration allowlisted from `source_map.SOURCES`.

## Validation

HTTP refactor head `232dd75466cf53184871590a19fdb619f576dcf5`:

- Governance CI run `29939850505`: success;
- Obsolete Authority Consistency run `29939849747`: success.

MCP refactor head `234b7f1c28b98ef74f2d69a7745a7999f102c987`:

- Governance CI run `29944399780`: success;
- Obsolete Authority Consistency run `29944400598`: success;
- MCP unit tests and end-to-end stdio vertical: success;
- read-only governance checks: success;
- packaging and clean wheel installation: success.

## Boundary

```text
request_id != evidence
route registration != dynamic authority
cached read-only service != runtime state authority
MCP tool discovery != capability authorization
HTTP projection != execution
ready != safe
implemented != installed
```

The refactor does not install, activate, approve, execute, send, schedule, route providers, update or promote memory.
