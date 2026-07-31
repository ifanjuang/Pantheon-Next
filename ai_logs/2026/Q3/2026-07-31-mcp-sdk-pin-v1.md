# 2026-07-31 — Pin the mcp SDK to the 1.x line (`mcp>=1.2,<2`)

Status: implementation artifact — dependency pin fix.
Boundary profile: implementation_artifact.

## Trigger

`mcp-server module tests` went red on CI for a docs-only PR (#493). The failure
was pre-existing and environment-driven, not caused by that change.

## Root cause

The `mcp` Python SDK cut two releases on 2026-07-28 (the spec date):

```text
1.29.0  last 1.x — still ships mcp.server.fastmcp and the legacy handshake;
        continues to receive critical bug / security fixes
2.0.0   first 2.x — "major rework" for the 2026-07-28 spec; relocated FastMCP
        out of mcp.server.fastmcp and removed the legacy initialize handshake;
        pip now installs this by default
```

`mcp-server/pyproject.toml` pinned `mcp>=1.2` (unbounded), so CI resolved to
`2.0.0` and failed at import:

```text
ModuleNotFoundError: No module named 'mcp.server.fastmcp'
```

with a downstream `test_vertical_e2e` failure on the removed `session.initialize()`
handshake.

## Change

```text
mcp-server/pyproject.toml   mcp>=1.2  ->  mcp>=1.2,<2
```

A single dependency bound. It restores `mcp.server.fastmcp` and the legacy
handshake the current `server.py` and `examples/hermes_vertical_runner.py` rely
on, and keeps the ongoing 1.x bug / security fixes. No source code changes.

## Verification

```text
venv with mcp>=1.2,<2 resolved to mcp 1.29.0
python -m unittest discover -s mcp-server/tests  ->  196 tests OK
```

## Boundary

```text
pin != migration
staying on 1.x != rejecting 2.x
```

This pin is the deliberate choice to keep the module on the stable 1.x SDK line
until the move to `mcp` 2.x (new FastMCP surface + stateless handshake) is done
as its own reviewed migration — tracked separately, per the upstream review in
`docs/governance/reference_reviews/MCP_SPEC_2026_07_28_REVIEW.md`. This change
adds no runtime behaviour or authority; `mcp-server/` stays read-only.
