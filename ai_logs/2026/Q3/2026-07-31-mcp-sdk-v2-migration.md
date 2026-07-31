# 2026-07-31 — Migrate the mcp-server module to the mcp SDK 2.x

Status: implementation artifact — SDK migration.
Boundary profile: implementation_artifact.

## Trigger

The `mcp` Python SDK released `2.0.0` on 2026-07-28 (the spec date), a major
rework for the 2026-07-28 specification. It relocated the high-level server class
out of `mcp.server.fastmcp` and removed the legacy `initialize` handshake, so the
module's `from mcp.server.fastmcp import FastMCP` no longer imported.

This is the deliberate migration the upstream review flagged as a separate
reviewed action (`docs/governance/reference_reviews/MCP_SPEC_2026_07_28_REVIEW.md`),
and the follow-on to the interim 1.x pin (`mcp>=1.2,<2`).

## Discovery (against an installed mcp 2.0.0)

```text
FastMCP           removed from mcp.server.fastmcp
MCPServer         the v2 successor high-level server (mcp.server.MCPServer);
                  .tool() / .resource(uri, ...) / .run(transport="stdio")
                  decorators are call-compatible with the FastMCP usage
ClientSession     retained; .initialize() and positional .call_tool(name, args)
                  still work over stdio (used by the conformance harness)
```

## Change

```text
mcp-server/pyproject.toml                    mcp>=1.2  ->  mcp>=2,<3
mcp-server/pantheon_mcp/server.py            FastMCP import + instantiation -> MCPServer
mcp-server/README.md                         "FastMCP wiring" -> "MCPServer wiring"
mcp-server/docs/HTTP_API_CONTRACT.md         "FastMCP stdio" -> "MCPServer stdio"
CHANGELOG.md                                 0.1.64 Changed: SDK 2.x migration note
```

Two functional lines in `server.py`; the rest is the pin bound and documentation.
The read-only tools, resources, the `PantheonPolicyService` core, the HTTP adapter
and the end-to-end stdio conformance harness (`examples/hermes_vertical_runner.py`)
are unchanged — the `ClientSession` client path is v2-compatible as written.

## Verification

```text
venv with mcp>=2,<3 resolved to mcp 2.0.0
python -m unittest discover -s mcp-server/tests  ->  196 tests OK
  (includes test_vertical_e2e over the real MCP stdio protocol)
check_packaging_contract.py  ->  OK (metadata/changelog/VERSION agree on 0.1.64)
```

## Boundary

```text
new SDK surface != new capability
MCPServer != agent runtime
initialize handshake removed upstream != behaviour change here
```

The surface stays read-only and side-effect-free: it serves governed sources,
validates caller-provided structures and returns verdicts as data. No execution,
scheduling, queue, provider routing, sampling or memory promotion is introduced.
The MCP Tasks extension and MRTR remain out of scope per the upstream review. This
change adds no runtime authority; Hermes executes and the human decides.
