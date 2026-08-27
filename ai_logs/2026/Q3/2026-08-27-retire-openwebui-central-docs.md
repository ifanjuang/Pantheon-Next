# Retire OpenWebUI central doctrine pointers

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: central governance owners
Change level: semantic

## Objective

Remove active OpenWebUI transition ownership from central governance documents without editing historical logs or creating replacement abstractions.

## Observed state

After #770 retired the active MCP projection, `MODULES.md`, `WATCHLIST.md` and `DOMAIN_PACK_SPEC.md` still routed responsibilities or template guidance through OpenWebUI / `OPENWEBUI_INTEGRATION.md`.

## Change

- `MODULES.md` records OpenWebUI/Paperless only as refused historical product paths and routes surviving responsibilities to existing owners;
- `WATCHLIST.md` watches generic runtime-client/UI patterns and routes exposure to existing external-tool/MCP verification owners and governed projection to Cockpit/Card owners;
- `DOMAIN_PACK_SPEC.md` routes runtime-facing templates and governed visual composition to existing Hermes/client and Cockpit/Card owners, with no client-specific template subsystem;
- add targeted regression tests for these central owners.

Historical earlier `ai_logs/` and dated audits are unchanged.

## Invariants

```text
client selected != governance authority
projection != persistence
runtime success != authorization
memory != Evidence
```

## Next

Continue incoming-link convergence in the remaining active documents before deleting `OPENWEBUI_INTEGRATION.md`. Historical provenance remains in Git and historical logs/audits.
