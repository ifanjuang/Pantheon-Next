# AI Log — Missing Information Discipline

Date: 2026-06-25

Actor: ChatGPT

## Context

The user emphasized that the system must not imagine missing information. It should identify, target and list missing information; cross-check several sources; infer only when obvious and low-risk; otherwise ask the user or block.

Active doctrine was checked first:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

No existing direct equivalent was found for a missing-information register / assumption ledger discipline.

## Change made

Created:

- `docs/governance/MISSING_INFORMATION_DISCIPLINE.md`
- `templates/missing_information_register_candidate.md`
- `templates/assumption_ledger_candidate.md`

The discipline defines:

- Required Information Maps;
- Missing Information Register;
- Assumption Ledger;
- deduction policy;
- ask policy;
- search-before-asking rule;
- production with gaps;
- compact output format;
- interaction with Workflow Depth Policy;
- interaction with learning.

## Boundary preserved

The change is documentation and templates only.

No runtime, extractor, router, scheduler, queue, UI, schema, memory engine, approval engine, document generator or automatic question-asking system was implemented.
No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` file was modified.
No external action was performed.
No Notion project record was written.
No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- missing information as a visible governed status;
- required information maps per output type;
- explicit assumption / deduction ledger;
- search before asking where proportional;
- ask or block for consequential gaps;
- compact information-status output by default.

Refused:

- filling consequential gaps by imagination;
- silent assumptions;
- automatic promotion of assumptions to facts;
- deduction for structure, insurance, DTU/compliance, urbanism, finance, responsibility, external action or memory;
- automatic implementation.

To verify:

- whether future CCTP-from-plan and CR-chantier runs should include this register by default;
- whether the compact output format is sufficient for Fast / Normal depths.

To arbitrate:

- whether this discipline should later become support doctrine or remain candidate.
