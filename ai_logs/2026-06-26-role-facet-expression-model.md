# AI Log — Role facet expression model

Date: 2026-06-26

Actor: ChatGPT

## Context

The user corrected the prior activation model. The important correction is that role facets are not switched on or off like modules. They are inherent traits of each role. Depending on the context, each facet may express itself more or less strongly and may remain silent, color the answer, become visible, consult another facet, request a rite or ask Zeus for arbitration.

The discussion was long and clarified several points:

- `reflex` is not a complete workflow;
- roles are not autonomous agents;
- gods / roles may own reflexes;
- roles have multiple facets;
- each facet has sensitivities, possible reactions, strategies, tactics, consultations and limits;
- consultation should be facet-to-facet, not broad role-to-role;
- roles should not be mechanically activated;
- a role may judge whether one of its facets should express itself;
- self-expression is not self-authorization;
- no role may validate, send, approve, memorize canonically or replace the architect;
- Zeus governs status thresholds and gates;
- the human decides.

Active doctrine checked:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

Relevant architecture role documents reviewed:

- `docs/governance/ARCHITECTURE_ROLE_FACETS.md`
- `docs/governance/ARCHITECTURE_ROLE_ACTIVATION_MODEL.md`

## Change made

Updated:

- `docs/governance/ARCHITECTURE_ROLE_ACTIVATION_MODEL.md`
- `templates/architecture/reflex_response_card_candidate.md`

Created:

- `templates/architecture/role_facet_expression_candidate.md`

The former activation model now presents itself as:

```text
Architecture Role Expression Model
```

while keeping the historical filename for compatibility:

```text
ARCHITECTURE_ROLE_ACTIVATION_MODEL.md
```

It now states:

```text
A role is not activated as a module.
A role exists as a standing guardian.
Its facets are always present.
The context makes some facets remain silent, color the answer, become visible, consult another facet, request a rite or ask Zeus for arbitration.
```

The response card now uses:

```text
Relevant facet expressions
Consulted facet links
Facet expression detail
Facet consultation trace
```

instead of role activation traces.

## Boundary preserved

The change is documentation and templates only.

No agents, role executors, role routing, multi-agent loops, workflow runtime, scheduler, queue, message bus, UI, approval engine, memory engine, rite runner, sender, checker, legal review or professional validation were implemented.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- roles are permanent guardians, not modules;
- facets are inherent traits, not actions;
- facet expression is contextual and qualitative;
- roles may judge expression of their own facets;
- self-expression is not self-authorization;
- consultations happen facet-to-facet;
- expression may color, warn, request evidence, propose tactics, consult, request rites or ask Zeus;
- expression may not validate, approve, send, canonize memory, accept payment, extend mission or replace professional judgement;
- response card should expose only facet expressions that affect the answer.

Refused:

- mechanical activation as the main concept;
- numerical scoring as required mechanism;
- all-role panel;
- hidden chain-of-thought consultation;
- automatic action;
- automatic approval by Zeus;
- implementation.

To verify:

- whether the file should eventually be renamed from `ARCHITECTURE_ROLE_ACTIVATION_MODEL.md` to `ARCHITECTURE_ROLE_EXPRESSION_MODEL.md` or `ARCHITECTURE_ROLE_FACET_EXPRESSION.md`;
- whether `ARCHITECTURE_ROLE_ACTIVATION_MODEL.md`, `ARCHITECTURE_ROLE_FACETS.md`, `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md` and `ARCHITECTURE_METHOD_TAXONOMY.md` should be indexed together in `AUTHORITY_INDEX.md`;
- whether future CR chantier test runs should use the new facet expression card.

To arbitrate:

- whether this expression model remains architecture-specific or should become generic Pantheon support doctrine.
