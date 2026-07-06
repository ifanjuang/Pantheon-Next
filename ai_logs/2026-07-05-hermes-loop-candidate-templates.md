# 2026-07-05 — Hermes loop candidate templates

Status: validation-only intervention log.

Repo state: documented non-implemented.

## Context

Follow-up to PR #282, which added `docs/governance/LOOP_GOVERNANCE_MODEL.md` as candidate support doctrine.

The user asked to start the Hermes templates if they did not already exist.

## Read context

Read or verified:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/LOOP_GOVERNANCE_MODEL.md`
- existing `templates/hermes/README.md`

Searched for existing loop templates and related open issues / PRs. No existing `loop_contract_candidate`, `loop_result_candidate` or open loop-template work was found.

## Changes

Added documentary Hermes-side candidate templates:

```text
templates/hermes/handoffs/loop_contract_candidate.json
templates/hermes/returns/loop_result_candidate.json
```

Updated:

```text
templates/hermes/README.md
```

## Classification

```text
Authority: candidate runtime-adapter templates
Repo state: documented non-implemented
Implementation: none
```

## Boundary

These templates are not executable schemas, validators, runtime configs, queues, schedulers, MCP tools, OpenWebUI templates, Hermes skills, approval engines, memory engines or external actions.

They are governance-readable examples for a future Hermes-side adapter shape.

## Decision classification

Accepted:

```text
- Add Hermes-readable loop handoff and loop return candidate templates.
- Keep templates under `templates/hermes/handoffs/` and `templates/hermes/returns/`.
- Preserve candidate-only status.
```

Refused:

```text
- `schemas/` addition.
- Validator or checker implementation.
- Runtime queue / scheduler / checkpoint store.
- Approval or memory promotion.
- External action.
```

To verify:

```text
- Whether future Hermes adapter work consumes these shapes directly or derives a narrower runtime config outside Pantheon.
- Whether later protected schema review is justified.
```
