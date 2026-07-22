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

## Reconciliation

The branch was replayed onto the common-installation baseline and the subsequent Pantheon MVP cockpit status reconciliation. Shared status and runtime-adapter documents preserve the module-only installation catalog, `configuration_ref` handoff scope and the external cockpit pin while adding the HTTP/MCP implementation posture.

The generated `ai_logs/INDEX.md` now contains 663 entries and includes both the common-installation baseline trace and this policy transport trace. The bounded regeneration workflow removed itself and is absent from the resulting tree.

## Validation

Earlier focused checkpoints:

- HTTP refactor head `232dd75466cf53184871590a19fdb619f576dcf5`: Governance CI and Obsolete Authority Consistency succeeded;
- MCP refactor head `234b7f1c28b98ef74f2d69a7745a7999f102c987`: MCP unit/stdio tests, governance checks, packaging and clean wheel installation succeeded;
- reconciled head before index regeneration `270618d2f2a33d0a0084aaba5a26ef89048ca082`: Governance CI run `29951984470` and Obsolete Authority Consistency run `29951984461` succeeded.

The final reviewed head must pass the same checks after deterministic index regeneration.

## Boundary

```text
request_id != evidence
route registration != dynamic authority
cached read-only service != runtime state authority
MCP tool discovery != capability authorization
HTTP projection != execution
ready != safe
implemented != installed
merged != activated
```

The refactor does not install, activate, approve, execute, send, schedule, route providers, update or promote memory.
