# AI Log — Card stack run-task model revision

Date: 2026-06-28

Actor: ChatGPT

## Context

The user asked to document the revised card/deck model after a long design discussion.

Key decisions to document:

- `Pantheon` becomes the reference project.
- Real projects only expose `Runs`, `Documents` and `Evidences` by default.
- Roles, competences and rites remain reference scenes inside `Pantheon`.
- In real project runs, roles, competences and rites are attached to task cards as references or sub-cards when they carry state.
- A run contains tasks.
- A task is the operational unit that aggregates responsible role, competences, rites, documents, evidences and decisions.
- Result Candidate is lifted into the Run Card as expected result and outputs, rather than treated as an ordinary peer card.
- Flow Adaptation is not a visible card by default; spawned cards appear directly in their actual nature and carry origin metadata.

## Source review

Reviewed active doctrine and related documents before editing:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/WORKFLOW_LIFECYCLE.md`
- `docs/governance/CARD_STACK_MODEL.md`

Checked open issues and PRs for matching terms around workflow/run/task/card/competence/role/rite/evidence/document. No directly matching open issue or PR was found by search.

## Change made

Updated:

- `docs/governance/CARD_STACK_MODEL.md`

## Content added / revised

The document now describes:

- top-level separation between reference project `Pantheon` and real projects;
- real project scenes: `Runs`, `Documents`, `Evidences`;
- reference scenes in `Pantheon`: `Documents`, `Roles`, `Competences`, `Rites`, `Run types`;
- core hierarchy: `Project -> Scene -> Run -> Task -> Detail`;
- role/competence/rite as reference vs instance;
- compact visible card families;
- Run Card as expected-result head card;
- Task Card as operational unit;
- task responsibility model;
- competence, role and rite visibility rules;
- spawned cards without a visible Flow Adaptation Card;
- status model separating process status and governance status;
- current navigation candidate;
- examples for complementary quotation reception, chantier report production and post-client-meeting task preparation;
- relationship with `WORKFLOW_LIFECYCLE.md`.

## Boundary preserved

Documentation only.

No UI, Swiper component, schema, test, runtime, workflow engine, state machine, graph database, scheduler, queue, skill generator, competence engine, evidence engine, approval engine, memory engine, OpenWebUI component, Hermes skill, connector or external action was implemented.

## Repo state

Documented non-implemented.

## Follow-up

A future pass should reconcile the `AUTHORITY_INDEX.md` note for `CARD_STACK_MODEL.md` if the maintainer wants the index wording to explicitly mention the new `Pantheon / Project / Run / Task` model.
