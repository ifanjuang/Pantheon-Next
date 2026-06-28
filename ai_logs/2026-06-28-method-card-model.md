# AI Log — Method Card Model

Date: 2026-06-28

Actor: ChatGPT

## Context

The discussion started from `schemas/reasoning_mods.json`, initially interpreted as a possible MÈTIS reasoning selector. The review concluded that this was too narrow and too runtime-like.

The human direction was to treat reasoning methods as cards in the Pantheon card game, at the same UX level as Roles and Competences, but with a distinct authority class.

A second refinement clarified that methods should not be hardcoded inside Run types. Roles should be able to detect tensions during a task and propose a method when useful.

## Change made

Created:

- `docs/governance/METHOD_CARD_MODEL.md` — candidate support doctrine for Method / Reasoning cards.

No lasting change to `docs/governance/CARD_STACK_MODEL.md` remains in the final diff. A first edit accidentally replaced the long file with a shortened version; the file was restored from `main` before closing the intervention.

Refined in `METHOD_CARD_MODEL.md`:

- Method Cards are not MÈTIS itself.
- MÈTIS may propose a method, but does not own the method deck.
- Other Roles may propose methods according to their jurisdiction: ARGOS for source/proof, THEMIS for mission and responsibility, ATHENA for synthesis/reframing, HEPHAESTOS for decomposition, ZEUS for status-related method changes.
- Runs expose method affordances, not fixed method sequences.
- A Role may issue a `Method Proposal Candidate` when a task exposes a tension, contradiction, uncertainty, failure or opportunity.
- Method changes are split into three levels: internal adjustment, Zeus review, human gate.
- Hermes receives only bounded method handoffs and returns candidates, not proof, approval, memory or external action.

## Boundary preserved

Documentation only.

No schema was changed.

No test, runtime, UI, renderer, workflow engine, scheduler, queue, agent loop, approval engine, memory engine, Hermes skill, connector, platform file, Docker file, environment file or external action was added.

`schemas/reasoning_mods.json` remains untouched and should be treated as a candidate raw method catalog or possible seed for a future Method Deck, not as a canonical schema or runtime selector.

## Repo state

Documented non-implemented.

Partial note:

- `AUTHORITY_INDEX.md` still needs an explicit row for `docs/governance/METHOD_CARD_MODEL.md` before this branch should be considered fully index-clean.

## Decision status

Accepted:

- Create an autonomous Method / Reasoning card family.
- Do not make MÈTIS the owner of the method deck.
- Treat methods as role-proposed candidates when a task tension appears.
- Keep Hermes as execution runtime only.

To verify:

- Exact deck taxonomy: raw methods vs professional methods vs runtime patterns.
- Whether `reasoning_mods.json` should be moved out of `schemas/` or converted later into a true schema under protected-path review.
- How Method Proposal Candidates should appear in the cockpit UI.

To arbitrate:

- Whether `METHOD_CARD_MODEL.md` should remain generic Pantheon support doctrine or later receive an architecture-domain specialization.

## Working formula

```text
Role observes.
Method structures.
Competence produces.
Hermes executes.
Evidence supports.
Gate authorizes or blocks.
Human decides.
```
