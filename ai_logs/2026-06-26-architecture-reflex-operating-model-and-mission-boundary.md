# AI Log — Architecture reflex operating model and mission boundary

Date: 2026-06-26

Actor: ChatGPT

## Context

The user asked to further improve the system before documenting it.

The discussion identified two missing consolidation layers:

1. a common operating model to prevent the growing set of architecture reflexes from becoming an usine a gaz;
2. a transversal mission / responsibility boundary reflex to ensure that useful answers do not accidentally extend the architect's mission or responsibility.

Active doctrine was checked first:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

Repo search found no direct equivalent for either:

- architecture reflex operating model;
- architecture mission / responsibility boundary reflex.

## Change made

Created:

- `docs/governance/ARCHITECTURE_REFLEX_OPERATING_MODEL.md`
- `docs/governance/ARCHITECTURE_MISSION_RESPONSIBILITY_BOUNDARY_REFLEX.md`
- `templates/architecture/reflex_response_card_candidate.md`
- `templates/architecture/mission_responsibility_boundary_candidate.md`

The operating model reduces architecture-domain behavior to:

```text
Request -> Depth -> Context -> Reflexes -> Candidate -> Gate
```

It also defines:

- four user-facing intents: Answer, Verify, Produce, Act;
- business reflexes versus safety reflexes;
- compact first-layer answer card;
- escalation and stop rules;
- mission boundary as cross-cutting rule;
- compactness and learning rules.

The mission boundary reflex defines:

- mission boundary classification;
- responsibility risk;
- reply posture;
- first internal warning behavior;
- external reply rule;
- safe and dangerous wording;
- common cases such as no OPC, no structural mission, invoice / quote, enterprise methods and insurance;
- required source checks;
- interaction with other architecture reflexes.

## Boundary preserved

The change is documentation and templates only.

No runtime, agent router, workflow engine, scheduler, queue, UI, connector, memory engine, approval engine, document generator or automatic action system was implemented.
No legal review, insurance review, contract management, email sending, Notion write, external communication workflow or professional validation was implemented.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Notion project state was written.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- shared Request / Depth / Context / Reflexes / Candidate / Gate operating model;
- compact first-layer answer card;
- safety reflexes as cross-cutting controls;
- mission and responsibility boundary as mandatory before external-facing outputs;
- internal warning first when a subject may be outside mission;
- external mail candidate only if requested or clearly expected;
- boundary reply / orientation / competent-party referral rather than validation or prescription.

Refused:

- visible proliferation of workflows for every micro-case;
- automatic external reply;
- automatic mission extension;
- validation, prescription, financial acceptance, insurance confirmation or OPC posture outside mission;
- runtime implementation.

To verify:

- whether `ARCHITECTURE_REFLEX_OPERATING_MODEL.md` should become the future index for architecture reflexes;
- whether mission boundary should be referenced from all architecture-domain reflex docs;
- whether `AUTHORITY_INDEX.md` should receive explicit rows for the new candidate docs or remain covered by future grouped architecture-domain indexing.

To arbitrate:

- whether the next full run should be site-report finalization using the new compact response card and mission boundary template.
