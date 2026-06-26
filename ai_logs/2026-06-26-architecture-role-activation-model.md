# AI Log — Architecture role activation model

Date: 2026-06-26

Actor: ChatGPT

## Context

The user asked whether the role/god model should be improved further and invited innovation if needed.

The critique: the role-facet model is useful, but if all roles become visible on every request, Pantheon becomes noisy and slow. The improvement is an activation model with role circles, activation levels and speech thresholds.

Active boundaries checked:

- `docs/governance/STATUS.md` confirms Pantheon is governance-first and not an agent loop, runtime, scheduler, queue, hidden workflow runner, automatic approval system or automatic memory promotion engine.
- `docs/governance/CAPABILITY_PLACEMENT.md` confirms surfaces may warn, request more evidence and open gates, but must not become authority, runtime, scheduler, approval engine or memory engine.

Repo search found no direct existing activation model.

## Change made

Created:

- `docs/governance/ARCHITECTURE_ROLE_ACTIVATION_MODEL.md`

Updated:

- `templates/architecture/reflex_response_card_candidate.md`

The activation model defines:

- role circles: core, conditional and production;
- activation levels: dormant, watch, active, blocking, arbitration;
- speech threshold: a role is visible only if it changes the answer, status, risk, wording, evidence requirement, gate or next action;
- blocking precedence;
- Zeus escalation limits;
- anti-noise rules;
- output modes: minimal, compact role trace, detailed role trace.

## Boundary preserved

The change is documentation and template only.

No agents, role executors, role routing, multi-agent loops, workflow runtime, scheduler, queue, message bus, UI, approval engine, memory engine, rite runner, sender, checker, legal review or professional validation were implemented.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- core roles: Hestia, Athena, Themis, Mnemosyne, Zeus;
- conditional roles: Hermes, Chronos, Ploutos;
- production roles: Hephaestus, Iris, Apollo;
- activation levels dormant/watch/active/blocking/arbitration;
- role visibility only when a role changes output or status;
- first-layer response should stay sober;
- detailed role trace only on demand or Deep review.

Refused:

- all roles visible by default;
- all-role panels;
- role comments that do not change anything;
- Zeus for every small uncertainty;
- hidden role loops;
- implementation.

To verify:

- add `ARCHITECTURE_ROLE_ACTIVATION_MODEL.md`, `ARCHITECTURE_ROLE_FACETS.md`, `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md` and `ARCHITECTURE_METHOD_TAXONOMY.md` to `AUTHORITY_INDEX.md` in a controlled index update;
- test role activation on site-report finalization.

To arbitrate:

- whether role activation should remain architecture-specific or become generic Pantheon support doctrine.
