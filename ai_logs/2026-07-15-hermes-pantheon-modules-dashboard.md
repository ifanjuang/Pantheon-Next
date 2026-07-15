# Hermes Pantheon Modules dashboard plugin

Date: 2026-07-15

Status: validation-only trace — external Hermes integration implemented but not installed.
Boundary profile: validation_only_trace.

## Change

- Added an installable dashboard-only Hermes plugin template that reads native
  memory, MCP catalog/server and plugin inventories.
- Added explicit, separately confirmed native Hermes actions for provider
  selection, MCP catalog installation, MCP testing/toggling and plugin toggling.
- Added cautious placement metadata for the Pantheon policy MCP, Mem0, n8n,
  LangGraph and Memvid.
- Added a narrow `.gitignore` exception for this plugin's required pre-built
  `dashboard/dist/` browser assets.
- Added an inert Python package marker because Hermes gates user dashboard
  assets on plugin enablement; it registers no runtime hooks, tools or routes.
- Clarified that a one-shot human-confirmed Hermes administration request is
  operational enablement, not Pantheon governance activation or Task Contract
  authorization.
- Added manifest, boundary, security and JavaScript normalizer tests.

## Why

Hermes already provides authenticated dashboard APIs for installed plugins,
memory providers and MCP servers. Reusing those APIs avoids a second runtime or
credential gateway while giving the operator the requested module visibility
and controlled activation surface.

n8n is included as an optional automation MCP because its official Hermes
catalog entry is pinned and read-mostly by default. It remains high risk when
live workflow mutation is enabled and is not an MVP dependency.

## Verification source

Hermes Agent commit `8b209e0dd7b8e308d5b923fa80f7a72f71042636`
was audited on 2026-07-15. The n8n catalog entry pins
`CyberSamuraiX/hermes-n8n-mcp` at
`7a9ae00795593aa1fdb4e61ecd640e8bfd0c3841`.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: governance documentation and tests, with explicit user authorization.
Runtime impact: none inside Pantheon; the browser bundle runs only after external Hermes installation and enablement.
Authority impact: clarifies an existing human-confirmed operational boundary; no role or approval authority changes.
Schema/test/CI impact: additive tests only; no schema or CI workflow change.
External action: no installation, provider selection or module activation was performed.
Memory behavior: no memory write or promotion; Mem0 selection remains an external operator action.

## Local distinctions

```text
plugin template present != installed != enabled
Hermes enabled != Pantheon governance activation != task authorization
reachable != healthy != safe
runtime_success != evidence
```
