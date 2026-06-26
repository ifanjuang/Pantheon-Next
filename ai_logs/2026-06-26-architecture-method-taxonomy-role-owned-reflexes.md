# AI Log — Architecture method taxonomy and role-owned reflexes

Date: 2026-06-26

Actor: ChatGPT

## Context

The user corrected the previous terminology: `reflex` should not be used as a generic name for all architecture workflows or reusable patterns.

A reflex should be limited to situations where, during project progress, during work on a subject, or while producing a deliverable, something surfaces that requires cadrage, rappel, warning, boundary marking or escalation.

The user also clarified that each role / god may own its own reflexes as part of its role.

## Change made

Created:

- `docs/governance/ARCHITECTURE_METHOD_TAXONOMY.md`

Updated:

- `docs/governance/ARCHITECTURE_REFLEX_OPERATING_MODEL.md`
- `templates/architecture/reflex_response_card_candidate.md`

The taxonomy now separates:

- Method / Méthode;
- Approach / Démarche;
- Discipline;
- Strategy;
- Procedure;
- Tactic;
- Reflex / Réflexe.

The operating grammar is now:

```text
Request
-> Depth
-> Context
-> Approach / Procedure
-> Disciplines
-> Strategies
-> Tactics
-> Reflexes when triggered
-> Candidate
-> Gate
```

The short form is:

```text
Request -> Depth -> Context -> Method Objects -> Candidate -> Gate
```

Role-owned reflexes were added:

```text
role = standing guardian of a consequence domain;
reflex = triggered signal emitted by that role when a situation requires cadrage, rappel, warning or escalation.
```

Examples:

- Zeus: approval-ceiling warning, status-promotion caution, external-action arbitration.
- Athena: contradiction warning, weak-proof warning, overconfident-conclusion warning.
- Themis: mission-boundary warning, responsibility warning, forbidden-wording warning.
- Mnemosyne: stale-recall warning, duplicate-memory warning, unvalidated-memory-write warning.
- Hermes: execution-scope warning, connector-risk warning, handoff-boundary warning.
- Hephaestus: missing-template warning, production-readiness warning, deliverable-structure warning.
- Iris: tone-risk warning, ambiguity warning, expression-without-substance-change warning.

## Boundary preserved

The change is documentation and template only.

No runtime, workflow engine, router, scheduler, queue, UI, memory engine, approval engine, document generator, checker, sender, external action, legal review or professional validation was implemented.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- `reflex` narrowed to triggered cadrage / rappel / warning;
- full deliverable paths reclassified as approaches or procedures;
- cross-cutting rules reclassified as disciplines;
- route selection reclassified as strategies;
- local moves and wording as tactics;
- roles may own reflexes as part of their guardian behavior;
- response card updated to show method objects and triggered role reflexes.

Refused:

- using `reflex` as generic name for all methods;
- treating roles as reflexes;
- treating a reflex as a full workflow;
- runtime implementation.

To verify:

- add `ARCHITECTURE_METHOD_TAXONOMY.md` to `AUTHORITY_INDEX.md` in a separate controlled index update;
- progressively reclassify existing files whose names still contain `REFLEX` but actually describe approaches or disciplines.

To arbitrate:

- whether `ARCHITECTURE_REFLEX_OPERATING_MODEL.md` should eventually be renamed to `ARCHITECTURE_METHOD_OPERATING_MODEL.md`.
