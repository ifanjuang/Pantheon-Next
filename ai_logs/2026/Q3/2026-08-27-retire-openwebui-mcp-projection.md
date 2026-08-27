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

## Change

- remove `openwebui-integration` from the MCP source map and policy-interface structure;
- replace the historical exposure boundary with distinct Hermes client, Hermes Agent, Pantheon governance and Pantheon Cockpit responsibilities;
- remove the active `openwebui` architecture topic;
- add `hermes-client` for replaceable Hermes-compatible runtime interaction clients;
- add `pantheon-cockpit` for governed Cards/navigation/status/review/decision projections;
- preserve the generic read-only exposure verifier unchanged in behavior;
- replace OpenWebUI exposure examples/fixtures with `runtime_client` and `hermes_web`;
- add regression tests preventing `cockpit` from resolving to a retired client owner.

Historical `ai_logs/` and dated audits are not modified.

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