# Converge small active OpenWebUI consumers

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: distillation registry + Hermes evaluation/simulation candidate
Change level: semantic

## Objective

Remove two remaining active OpenWebUI ownership/integration dependencies before tackling the long Evidence Topology and Document Lifecycle owners.

## Observed state

On `main` after PR #775, `DISTILLATION_REGISTRY.md` still contained an `openwebui_exposure_candidate` status, an OpenWebUI-specific future card, an `OPENWEBUI_INTEGRATION.md` destination and a product-specific boundary rule. `EVALUATION_AND_SIMULATION_CANDIDATE.md` still assigned exposure to OpenWebUI, referenced the retired integration owner, used OpenWebUI-specific forbidden inputs and owned a dedicated exposure section.

No open parallel PR covered either owner.

## Change

- make distillation statuses and future cards projection/client agnostic;
- route governed projection patterns to existing Cockpit/Card owners rather than a product-specific integration document;
- preserve every existing distillation pattern and its substantive destination;
- retain Hermes evaluation/simulation capabilities, Task Contract, Evidence, approval, memory and User Decision Gate constraints;
- separate unconditional authority prohibitions from context/tool inputs that can only be admitted by the applicable Task Contract and policy owner;
- keep runtime interaction replaceable and governed projection non-authoritative;
- add targeted regression tests.

Historical earlier `ai_logs/` and dated audits are unchanged.

## Invariants

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
client selected != governance authority
simulation completed != approval
score produced != policy decision
```

## Exit criteria

- neither active owner references OpenWebUI or `OPENWEBUI_INTEGRATION.md`;
- distillation entries and simulation/evaluation capabilities remain represented;
- no new runtime, client, projection or authority owner is introduced;
- CI/review are green on the exact PR head before merge.
