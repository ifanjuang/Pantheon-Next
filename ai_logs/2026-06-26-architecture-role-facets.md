# AI Log — Architecture role facets

Date: 2026-06-26

Actor: ChatGPT

## Context

The user approved documenting the second proposed document, then asked for critique and improvement before freezing it.

The improvement made was to avoid a decorative or agentic use of gods / roles. Roles are formalized as multi-faceted guardians with jurisdiction, detection logic, disciplines, strategies, procedures, tactics, role-owned reflexes, consultations, rites, gates and limits.

Repo search found no direct equivalent for role facets.

## Change made

Created:

- `docs/governance/ARCHITECTURE_ROLE_FACETS.md`
- `templates/architecture/role_facets_candidate.md`

The document defines:

- role facet model;
- role-is-not-agent boundary;
- architecture candidate role table;
- facet examples for Themis, Mnemosyne and Iris;
- output visibility;
- anti-patterns;
- relationship with `ARCHITECTURE_METHOD_TAXONOMY.md` and `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md`.

## Boundary preserved

The change is documentation and template only.

No agents, role executors, multi-agent loops, workflow engine, router, scheduler, queue, message bus, UI, approval engine, memory engine, rite runner, sender, checker, legal review or professional validation were implemented.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- role as multi-faceted guardian, not worker;
- facets: jurisdiction, detection, disciplines, strategies, procedures, tactics, reflexes, consultations, rites, gates, output trace and limits;
- role-owned reflexes as part of role behavior;
- anti-agent boundary;
- template for future role cards.

Refused:

- role as decorative label;
- role as autonomous agent;
- all roles commenting on every request;
- role consultation as hidden chain-of-thought;
- automatic approval, sending, memory promotion or execution.

To verify:

- add `ARCHITECTURE_ROLE_FACETS.md`, `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md` and `ARCHITECTURE_METHOD_TAXONOMY.md` to `AUTHORITY_INDEX.md` in a controlled update;
- decide whether this stays architecture-specific or becomes generic Pantheon support doctrine.

To arbitrate:

- whether the next run should test role facets on CR chantier finalization.
