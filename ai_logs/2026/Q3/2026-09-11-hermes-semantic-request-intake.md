# Hermes semantic request intake — 2026-09-11

## Objective

Continue from merged `main` `9c2d9fcfb7e040b7fe49ee64c0ac362c5d38656e`
after progressive request handling landed. Add the smallest Hermes-side semantic
adapter needed to feed that policy surface without creating another policy,
planner, router, Role or workflow engine.

## Repository checks

Observed before the change:

- `main` HEAD was `9c2d9fcfb7e040b7fe49ee64c0ac362c5d38656e`;
- no open PR matching Hermes semantic intake / request preflight was found;
- `REQUEST_LIFECYCLE.md` already owns request/cap lifecycle and proportional activation;
- `ROLE_ACTIVATION.md` already owns governed trigger vocabulary;
- `mcp-server/pantheon_mcp/request_handling.py` already accepts candidate `conditions`, coordination relations and completion requirements;
- `mcp-server/docs/HERMES_INTEGRATION_CONTRACT.md` already states that Pantheon is not the natural-language runtime;
- executable Hermes integration belongs under `implementation/`, while declarative Hermes skill guidance belongs under `templates/hermes/skills/`;
- the current context bridge is deliberately narrow and only owns admitted context reads plus gateway attachment framing, so semantic intake was not added to that plugin.

## Change

Added `templates/hermes/skills/pantheon-request-intake/SKILL.md` as a declarative
runtime adapter candidate.

The adapter:

- preserves the user's cap in `intent`;
- emits only materially supported existing governed conditions;
- may describe generic coordination relations and observable completion requirements;
- never derives K/V/C, approval, Role authority or authorization;
- does not choose topology;
- reconsults only when a material governed condition changes.

`ifja-project-context` now reuses this generic adapter before Pantheon
classification instead of growing an IFJA-specific classifier.

A broad synthetic fixture corpus covers harmless rewrite, factual explanation,
current product comparison, software diagnosis, contradictory documents,
creative options, professional document review, disputed invoice drafting,
prior-decision recall, external send, conditional branching, formatting of
consequential text without semantic review, contract verification, memory
promotion and public output.

## Invariants

```text
semantic candidate != truth
condition candidate != consequence classification
Role trigger != runtime dispatch
coordination relation != topology dispatch
completion requirement != approval
retrieved != Evidence
runtime success != authorization
projection != persistence
```

## Validation boundary

Repository tests can verify vocabulary ownership, fixture structure and policy
projection. They do not prove live-model semantic precision or recall. A later
runtime qualification must run the same corpus through the exact selected Hermes
runtime/model and record false-positive / false-negative behavior before this
candidate is treated as operationally qualified.
