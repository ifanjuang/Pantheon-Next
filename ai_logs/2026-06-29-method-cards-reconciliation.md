# AI Log — Method Cards Reconciliation

Date: 2026-06-29

Actor: ChatGPT

## Context

PR #233 diverged from `main` after parallel work moved the former `schemas/reasoning_mods.json` content out of `schemas/` and into `templates/competence/reasoning_modes_guide_candidate.json`, governed by `docs/governance/REASONING_MODES_LIBRARY.md`.

The reconciliation decision was:

```text
REASONING_MODES_LIBRARY.md
= raw reasoning modes as candidate Guide de compétence.

METHOD_CARD_MODEL.md
= visible Method Card grammar and Method Proposal Candidate model.

ARCHITECTURE_METHOD_DECK.md
= architecture-domain professional method cards.

CARD_STACK_MODEL.md
= cockpit placement: where method cards appear.

Pantheon Control HTML prototype
= visual demonstration only, no runtime authority.
```

## Change made

Created a clean branch from `main`:

```text
chatgpt/reconcile-method-cards-html
```

Added:

- `docs/governance/METHOD_CARD_MODEL.md`
- `docs/governance/ARCHITECTURE_METHOD_DECK.md`

Updated:

- `docs/governance/CARD_STACK_MODEL.md`
- `docs/assets/pantheon-control/app.js`
- `docs/assets/pantheon-control/deck.html`

## Card Stack alignment

`CARD_STACK_MODEL.md` now treats methods as first-class references inside the card grammar:

- `Methods / Reasoning` appears in the Pantheon reference project.
- Tasks may carry `methodRefs` and `methodProposalCandidates`.
- A method becomes a visible sub-card only when it carries process state.
- The horizontal axis is reserved for sibling cards or branches.
- The vertical axis is used for deck depth / hierarchy.

## HTML prototype alignment

The deck prototype is updated so:

```text
vertical swiper = hierarchy / depth;
horizontal swiper = sibling cards;
method cards appear in the demo data;
method sub-cards appear under task/run examples.
```

The HTML remains illustrative. It does not implement validation, approval, memory, external action, a real workflow engine or a runtime selector.

## Boundary preserved

Documentation and static HTML/JS prototype only.

No schema was changed.

No tests, runtime, platform, operations file, Docker file, environment file, Hermes skill, connector, memory engine, approval engine or external action were added.

## Operational note

During this intervention, two accidental direct commits briefly created then removed temporary content on `main`:

- `tmp-test-file-please-ignore`
- `docs/governance/METHOD_CARD_MODEL.md` containing only `test`

Both were immediately removed. The final content work is on `chatgpt/reconcile-method-cards-html`.

## Decision status

Accepted:

- Close or supersede PR #233 rather than trying to merge it as-is.
- Reconcile from current `main`.
- Keep `REASONING_MODES_LIBRARY.md` as the raw reasoning-mode library frame.
- Add Method Cards as a separate cockpit/governance grammar.
- Add architecture-domain professional method cards.
- Reflect vertical hierarchy and horizontal siblings in the static deck prototype.

To verify:

- Authority Index rows still need to be added for the two new documents before merge.
- Static prototype should be reviewed visually on mobile.
- Decide whether the architecture deck should stay broad or be reduced for cockpit density.

The validated remains.
