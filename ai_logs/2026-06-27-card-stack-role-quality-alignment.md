# AI Log — Card stack role quality alignment

Date: 2026-06-27

Actor: ChatGPT

## Context

The user approved moving to the next UX governance piece after the competence, context stack, governance college and rites work. The supplied working note identified the next piece as:

```text
CARD_STACK_MODEL.md
= grammaire UX des cartes, swipe, gates, lieux, rôles, compétences, templates.
```

The note also proposed cards for:

- roles / gods;
- rites;
- places / lieux;
- competences;
- knowledge;
- guides / resources;
- templates;
- evidence;
- actions;
- Zeus gates.

It proposed navigation by vertical swipe, horizontal swipe, tap, long press and constellation view.

Active doctrine checked:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

Relevant existing file found:

- `docs/governance/CARD_STACK_MODEL.md`

The existing file was already a broad candidate review draft for cockpit UX, card scenes, navigation, role cards, rites, competences, evidence handling and project navigation.

## Change made

Created:

- `docs/governance/CARD_STACK_ROLE_QUALITY_ALIGNMENT.md`

This new note reconciles `CARD_STACK_MODEL.md` with the corrected role-quality vocabulary:

```text
God = governance figure.
Role = function carried by the god.
Jurisdiction = domain the role protects.
Facet = quality that allows the role to protect its jurisdiction.
Expression = contextual manifestation of that quality.
```

It defines how to read older phrases in `CARD_STACK_MODEL.md`:

- `Role / God Cards activated` -> `Role / God Cards whose qualities materially expressed themselves in the treatment`;
- `active facet` -> `visible role quality expression`;
- `Gods are review facets` -> `Gods are governance roles; facets are the qualities through which they review, warn, orient, consult or request gates`.

It also defines:

- corrected Role / God Card fields;
- corrected Role Quality / Facet Card fields;
- Workflow Scene correction;
- visibility rule for quality expressions;
- gesture boundary;
- minimal stack for first site-report test.

## Boundary preserved

Documentation only.

No UI, dashboard, card renderer, swipe engine, graph view, runtime, workflow engine, scheduler, queue, router, approval engine, memory engine, OpenWebUI Function, Hermes skill, connector or external action was implemented.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- keep `CARD_STACK_MODEL.md` as the main candidate UX grammar;
- add a reconciliation note rather than overwriting a long existing draft;
- align card UX with role-quality vocabulary;
- include quality/facet expressions only when they change status, risk, wording, evidence, next action or gate;
- preserve gates as decision surfaces;
- preserve gestures as reveal/request/prepare only, never approval.

Refused:

- replacing the existing `CARD_STACK_MODEL.md` wholesale;
- treating swipes or long press as approval;
- displaying every role or every inherent quality;
- making constellation view authoritative;
- implementing UI or runtime.

To verify:

- whether `CARD_STACK_MODEL.md` itself should be updated later to remove older wording;
- whether `CARD_STACK_MODEL.md` and `CARD_STACK_ROLE_QUALITY_ALIGNMENT.md` should be indexed together in `AUTHORITY_INDEX.md`;
- whether `README.md` should point to the card-stack cluster.

To arbitrate:

- whether the next work package should be the first site-report finalization test using the minimal card stack.
