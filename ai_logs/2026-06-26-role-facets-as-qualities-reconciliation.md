# AI Log — Role facets as qualities reconciliation

Date: 2026-06-26

Actor: ChatGPT

## Context

The user clarified an important conceptual correction after a long discussion:

A role / god has several facets, but those facets should not be understood merely as sub-domains such as mission, responsibility, proof, memory or cost. Those are better understood as jurisdiction fields, protected fields, consequence domains or review angles.

Facets are the different qualities that allow the role to fulfill its role:

- sensitivities;
- reflexes;
- orientations;
- tactics;
- consultation habits;
- prudence modes;
- alert thresholds;
- limits.

The user's formulation was that each god possesses several qualities that allow it to ensure its role.

## Doctrine checked

The following active documents had already been checked during the same work cluster:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

The correction remains compatible with the repository boundary: Pantheon governs, it does not execute.

## Change made

Updated:

- `docs/governance/ARCHITECTURE_ROLE_FACETS.md`
- `docs/governance/ARCHITECTURE_ROLE_ACTIVATION_MODEL.md`
- `templates/architecture/role_facets_candidate.md`
- `templates/architecture/role_facet_expression_candidate.md`
- `templates/architecture/reflex_response_card_candidate.md`

The documents now distinguish:

```text
God = governance figure.
Role = function carried by the god.
Jurisdiction = domain the role protects.
Facet = quality that allows the role to protect its jurisdiction.
Expression = contextual manifestation of that quality.
```

The role-facet document now describes each role by:

- jurisdiction;
- protected fields;
- qualities / facets;
- sensitivities;
- reflexes;
- orientations;
- tactics;
- consultation habits;
- prudence modes;
- alert thresholds;
- gates;
- limits.

It also adds Chronos and Ploutos to the candidate architecture role set.

The response card now refers to:

```text
Relevant quality / facet expressions
Consulted quality / facet links
```

instead of treating facets as sub-modules.

## Boundary preserved

Documentation and templates only.

No agents, role executors, multi-agent loops, workflow engine, router, scheduler, queue, message bus, UI, approval engine, memory engine, rite runner, sender, checker, legal review or professional validation were implemented.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- `facet` means role quality;
- jurisdiction/protected fields are distinct from qualities;
- role qualities include sensitivities, reflexes, orientations, tactics, consultation habits, prudence modes, alert thresholds and limits;
- contextual expression applies to qualities;
- consultations happen quality-to-quality / facet-to-facet;
- Chronos and Ploutos remain candidate conditional architecture roles;
- response cards expose only useful quality expressions.

Refused:

- facet as a mere sub-domain;
- role as module;
- hidden all-role panel;
- quality expression as authorization;
- automatic approval, sending, memory promotion, payment acceptance or mission extension.

To verify:

- whether `ARCHITECTURE_ROLE_ACTIVATION_MODEL.md` should be renamed to `ARCHITECTURE_ROLE_EXPRESSION_MODEL.md` or `ARCHITECTURE_ROLE_QUALITY_EXPRESSION.md`;
- whether the set of 11 architecture roles should be stabilized in `AUTHORITY_INDEX.md` as candidate support doctrine;
- whether `ARCHITECTURE_ROLE_FACETS.md`, `ARCHITECTURE_ROLE_ACTIVATION_MODEL.md`, `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md` and `ARCHITECTURE_METHOD_TAXONOMY.md` should be indexed together.

To arbitrate:

- whether the model should remain architecture-specific or become generic Pantheon support doctrine after testing.

Next recommended test:

- run a CR chantier candidate with quality expressions visible only when they change status, risk, wording, evidence, action or gate.
