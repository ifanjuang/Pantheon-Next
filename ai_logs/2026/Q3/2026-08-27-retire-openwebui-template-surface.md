# Retire OpenWebUI template surface

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: non-executable templates / fictional external-run examples
Change level: semantic

## Observed state

After #768, canonical status no longer assigns a target responsibility to OpenWebUI. The remaining `templates/openwebui/` namespace held client-specific non-executable templates. Incoming-link audit found one still referenced request template, but its purpose was only to describe an external Hermes execution request already covered by the existing Hermes run-manifest/handoff owners. Other namespace templates had no demonstrated active consumer beyond the template registry or historical logs.

## Change

- retire the complete `templates/openwebui/` namespace;
- do not create a replacement client-specific template owner;
- update the existing Hermes `devis_reprise` run manifest to own its external runtime/client seam directly;
- update fictional run documentation from OpenWebUI-specific bridge language to Hermes Web/dashboard or compatible replaceable Hermes clients;
- reconcile the template scaffold and registry;
- add regression tests for namespace absence and current runtime owners.

Historical `ai_logs/` remain unchanged.

## Invariants

```text
runtime success != authorization
projection != persistence
provider selected != authority transfer
green CI != adoption
```
