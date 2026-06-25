# AI Log — Workflow Depth Policy

Date: 2026-06-25

Actor: ChatGPT

## Context

The user identified a key risk: Pantheon must not become an usine a gaz where every request triggers a heavy workflow and takes too long.

A proportional governance policy was documented to keep workflows light by default and deep only when risk requires it.

Active doctrine was checked first:

- `docs/governance/STATUS.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`

Relevant boundary confirmed:

- Pantheon is governance-first and not a runtime, scheduler, queue, approval system or memory promotion engine.
- OpenWebUI may show, warn, collect decisions, request more evidence and open gates, but must not become authority or approval engine.
- Runtime outputs remain candidates and must not collapse into proof, approval, validation or memory promotion.

No existing workflow-depth policy was found in repo search before creation.

## Change made

Created:

- `docs/governance/WORKFLOW_DEPTH_POLICY.md`
- `templates/workflow_depth_triage_candidate.md`

The policy defines three workflow depths:

- Fast — short candidate answer, minimal checks.
- Normal — bounded project-context review.
- Deep — consequential review with evidence discipline and gates.

It also defines:

- escalation triggers;
- user depth commands;
- compact output formats;
- progressive disclosure;
- stop conditions;
- learning-loop limits;
- anti-usine-a-gaz rules.

## Boundary preserved

The change is documentation and template only.

No router was implemented.
No scheduler, queue, agent loop, background worker, automatic triage system, approval engine, memory engine, user interface or runtime behavior was created.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Notion project record was written.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- proportional governance as a candidate policy;
- Fast / Normal / Deep workflow depth levels;
- progressive disclosure principle;
- explicit anti-usine-a-gaz rules;
- depth triage candidate template.

Refused:

- heavy workflow by default;
- automatic deep review for every request;
- automatic learning promotion;
- automatic approval or memory promotion;
- runtime implementation.

To verify:

- whether this policy should be referenced by site report, photo observation and financial review workflows;
- whether depth hints should become UI labels in the static cockpit examples.

To arbitrate:

- whether `WORKFLOW_DEPTH_POLICY.md` should later become support doctrine or remain candidate.
