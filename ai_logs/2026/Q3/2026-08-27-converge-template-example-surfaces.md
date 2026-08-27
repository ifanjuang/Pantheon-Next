# Converge template and professional-example surfaces

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: non-executable templates and fictional professional examples
Change level: semantic

## Objective

Remove active OpenWebUI ownership from reusable template doctrine and fictional professional UI examples while preserving the useful template contracts and governed projection examples.

## Observed state

`templates/README.md` was already converged and explicitly protected the retired `templates/openwebui/` namespace. `templates/TEMPLATE_MODEL.md` still stated that OpenWebUI exposed templates. `docs/examples/README.md` and `architecture_legal_module_panel/README.md` still presented a future OpenWebUI cockpit/module panel as the UI owner.

## Change

- leave the already-correct `templates/README.md` unchanged;
- align `TEMPLATE_MODEL.md` to Hermes clients for runtime-facing forms, Hermes Agent for external execution and Pantheon Cockpit/Card owners for governed projections;
- keep templates non-executable and non-authoritative;
- converge the architecture/legal module-panel example to a Pantheon Cockpit governed projection;
- preserve domain state, Role readiness, skill eligibility, dependency blockers, Evidence gates, User Decision Gate and separate retention authorization in the example;
- update the professional examples index to the same current boundary;
- add targeted regression tests.

Historical earlier `ai_logs/` and dated audits are unchanged.

## Invariants

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
provider selected != authority transfer
client selected != governance authority
```

## Exit criteria

The three changed active surfaces contain no OpenWebUI owner or integration pointer, useful template/example capabilities remain, and CI is green on the exact PR head.
