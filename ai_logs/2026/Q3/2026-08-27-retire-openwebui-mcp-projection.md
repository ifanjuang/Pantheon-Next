# Retire OpenWebUI MCP projection

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: MCP read-only architecture/exposure projection
Change level: semantic

## Objective

Remove OpenWebUI as an active MCP architecture owner while preserving the useful generic exposure-verification capability.

## Observed state

After #769 removed the client-specific OpenWebUI template namespace, the read-only MCP surface still exposed `openwebui-integration` as a governed source, returned `OpenWebUI exposes` in its structure boundary and resolved `cockpit` to an `openwebui` architecture topic. The exposure verifier itself was already generic but its examples and test fixtures still used OpenWebUI.

PR review then identified a second-order contradiction: `source_map.py` still exposed `MCP_PANTHEON_MINIMAL_PROFILE.md` as an active boundary source while that document itself continued to assign integration/display responsibility to OpenWebUI. That active owner also had to converge in the same slice.

## Change

- remove `openwebui-integration` from the MCP source map and policy-interface structure;
- replace the historical exposure boundary with distinct Hermes client, Hermes Agent, Pantheon governance and Pantheon Cockpit responsibilities;
- remove the active `openwebui` architecture topic;
- add `hermes-client` for replaceable Hermes-compatible runtime interaction clients;
- add `pantheon-cockpit` for governed Cards/navigation/status/review/decision projections;
- preserve the generic read-only exposure verifier unchanged in behavior;
- replace OpenWebUI exposure examples/fixtures with `runtime_client` and `hermes_web`;
- align `MCP_PANTHEON_MINIMAL_PROFILE.md` with the implemented read-only `mcp-server/`, Hermes clients, Hermes Agent and Pantheon Cockpit owners;
- add regression tests preventing `cockpit` from resolving to a retired client owner.

Historical earlier `ai_logs/` and dated audits are not modified.

## Invariants

```text
runtime success != authorization
projection != persistence
client selected != governance authority
exposure verification != client ownership
green CI != adoption
```

## Verification

Targeted MCP and root regression tests must pass. The PR must pass Governance CI, Architecture Audit and Obsolete Authority Consistency on its exact head before merge.

## Next

Converge remaining active documentation pointers to the current Hermes/Cockpit owners. Remove `OPENWEBUI_INTEGRATION.md` only after its active incoming links are eliminated. Historical provenance remains in Git, `ai_logs/` and dated audits.
