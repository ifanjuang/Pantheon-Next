# Hermes-native MCP policy/wiki configuration

Date: 2026-07-15

## Intent

Turn the previously generic MCP-client example into an accurate, bounded
Hermes Agent configuration candidate for the Pantheon read-only governance
wiki.

## Verification source

The upstream Hermes Agent documentation was checked on 2026-07-15. Hermes
loads MCP servers from `~/.hermes/config.yaml` under `mcp_servers`, discovers
tools at startup and supports per-server tool inclusion, prompt/resource
wrapper controls, parallel-call opt-in and sampling controls.

Source:
https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

## Changes

- added a native YAML fragment for the external Hermes configuration;
- replaced the generic JSON client example in the MCP README;
- restricted Hermes exposure to `list_sources`, `read_doctrine` and
  `explain_governance_structure`;
- disabled prompt/resource wrappers and MCP sampling;
- enabled parallel calls only for the three read-only tools;
- documented absolute executable path and read-only repository mount
  requirements.

## Boundary

The template does not install or activate Hermes, publish a release, mutate
Pantheon, approve an answer or execute an external action.

```text
template present != installed
installed != reachable != registered != approved != used
Hermes executes.
Pantheon governs.
```
