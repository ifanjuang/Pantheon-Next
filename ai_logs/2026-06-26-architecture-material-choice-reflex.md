# AI Log — Architecture material choice reflex

Date: 2026-06-26

Actor: ChatGPT

## Context

The user asked for a simple-question workflow for material choices, for example facade materials. The system should retrieve the latest decision/resolution, list preselected options, check PLU / recommendations, look for communications with MOE / instruction / ABF, and surface economic or technical issues such as masonry facing on timber frame being complicated or costly.

The workflow must remain lightweight by default and escalate only when risk requires it.

Active doctrine checked:

- `docs/governance/STATUS.md`
- `docs/governance/WORKFLOW_DEPTH_POLICY.md`

Repo search found no existing dedicated material-choice reflex.

## Change made

Created:

- `docs/governance/ARCHITECTURE_MATERIAL_CHOICE_REFLEX.md`
- `templates/architecture/material_choice_candidate.md`

The reflex defines:

- trigger conditions;
- default workflow depth;
- Fast / Normal / Deep source expectations;
- review axes: last known decision, preselected options, regulatory / instruction context, technical context, economic context and prior communications;
- option matrix;
- safe recommendation language;
- candidate actions;
- forbidden actions without approval;
- missing information handling.

## Boundary preserved

The change is documentation and template only.

No runtime, search tool, PLU checker, ABF checker, estimator, CCTP generator, Notion write, approval engine, memory engine or external communication workflow was implemented.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Notion project record was written.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- material choice as architecture-domain reflex;
- Normal as default depth;
- escalation to Deep for PLU, ABF, CCTP, cost, technical system, insurance, client decision or external action;
- last-known-decision-first approach;
- material option matrix;
- recommendation as candidate only.

Refused:

- choosing materials by authority;
- claiming PLU / ABF authorization without official source;
- claiming economy without estimate / source;
- modifying CCTP or Notion final state without approval;
- sending external communications without approval.

To verify:

- whether this reflex should be linked from the future architecture domain pack index;
- whether a fictive run should test timber cladding vs brick facing on timber frame.

To arbitrate:

- whether this reflex becomes a shared pattern for other choice questions: material, equipment, layout, technical system, heating, facade color, landscape palette.
