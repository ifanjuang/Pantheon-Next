# AI Log — Architecture role reflex coordination

Date: 2026-06-26

Actor: ChatGPT

## Context

The user proposed that when a role / god detects a situation requiring a reflex, it may consult another god for advice, invoke Zeus for arbitration or request a rite. This explains how a main approach can be enriched by many small local governance moves without becoming a hidden runtime.

Active boundaries checked:

- `docs/governance/STATUS.md` confirms Pantheon is not an agent loop, runtime, scheduler, queue, hidden workflow runner, automatic approval system or automatic memory promotion engine.
- `docs/governance/CAPABILITY_PLACEMENT.md` confirms the exposure surface may warn, request more evidence and open gates, but must not become authority, runtime, scheduler, hidden workflow runner or automatic approval/memory engine.

Repo search found no direct equivalent for role-reflex coordination.

## Change made

Created:

- `docs/governance/ARCHITECTURE_ROLE_REFLEX_COORDINATION.md`

Updated:

- `docs/governance/ARCHITECTURE_REFLEX_OPERATING_MODEL.md`
- `templates/architecture/reflex_response_card_candidate.md`

The new coordination model defines:

```text
Main Approach
-> Situation surfaces
-> Detect relevant consequence domain
-> Role-owned reflex fires
-> Optional role consultation
-> Optional rite request
-> Optional Zeus arbitration
-> Tactic / warning / gate / missing information
-> Candidate updated
-> Return to Main Approach
```

It clarifies that this is conceptual governance, not an executable graph.

It also defines bounded consultation rules:

- consult another role only when its domain is materially touched;
- normally limit consultation to 1-3 roles;
- request a rite or Zeus arbitration instead of expanding silently;
- avoid hidden loops and default all-role consultation.

## Boundary preserved

The change is documentation and template only.

No agent loop, workflow engine, micro-workflow runtime, router, scheduler, queue, message bus, UI, memory engine, approval engine, rite runner, role executor, checker, sender or external action was implemented.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- main approaches may be enriched by role-owned reflexes;
- role-owned reflexes may consult other roles;
- roles may request rites when a tension is structured or recurring;
- roles may invoke Zeus when status or approval ceiling must be arbitrated;
- response card exposes consulted roles, rite request and Zeus arbitration;
- all coordination remains visible, bounded and candidate.

Refused:

- hidden micro-workflows;
- automatic all-role consultation;
- role consultation loops;
- Zeus as automatic approval;
- rites as runtime workflows;
- implementation.

To verify:

- add `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md` and `ARCHITECTURE_METHOD_TAXONOMY.md` to `AUTHORITY_INDEX.md` in a controlled index update;
- test this model on a site-report finalization example.

To arbitrate:

- whether role-reflex coordination should remain architecture-specific or become a generic Pantheon support doctrine.
