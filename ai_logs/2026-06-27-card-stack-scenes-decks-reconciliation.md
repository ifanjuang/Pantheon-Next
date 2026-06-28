# AI Log — Card Stack Model reconciled to scenes / decks / constellation

Date: 2026-06-27

Actor: Claude (claude-opus-4-8)

## Context

Verification showed `CARD_STACK_MODEL.md` had been rewritten on main (commit
`32ec89e`, +391/-616) into a Run/Task model that explicitly replaced the earlier
scenes-as-peers idea. The architect chose (option B) to return to the
scenes / decks / cards / constellation grammar, reconciled — not a blind revert.

On the navigation backbone the architect specified three levels:
**Project → Scene → Deck** (subject is a scope label, not a navigation level).

## Change made

Rewrote `docs/governance/CARD_STACK_MODEL.md` as a reconciliation:

- Spine = scenes / decks / cards / constellation (hard rule: card = entity,
  scene = filtered presentation, deck = vertical order, constellation = project
  switch + global read).
- Navigation backbone = Project → Scene → Deck (→ Card). Constellation switches
  project; rail switches scene; vertical reads the deck; horizontal = sibling
  cards at the current level; tap = recto/verso; long press = quick actions
  (never auto-validate). Subject is a scope filter on scenes, not a level and
  not the horizontal axis.
- Kept the good content of the prior version: Pantheon-reference vs real-project
  separation, run card / task card / responsibility model, spawned-cards expose
  origin, process-vs-governance status model, and the three worked examples
  (condensed), now living inside the Workflow Scene.
- Applied review refinements: card families are entities not lifecycle states
  (Draft/Memory Candidate/Register/Promotion/Obsolete consolidated into one
  Record with a status; Competence + on-the-flow into one with a maturity field);
  answer-first default for the Workflow deck (draft + main gate + top evidence,
  full deck on demand); risk/certainty reuse the existing C/K and E0-E4 axes
  rather than a parallel faible/moyen/fort scale; role-quality cards appear only
  when a quality changes the treatment; universal recto/verso field contract;
  typed, capped, local links.

## Verification

Full read-only doctor suite green under the CI base ref (status headers,
internal links, index coverage, axis vocabulary, no_truncation,
no_net_truncation). 672 -> 515 lines: a deliberate, denser rewrite, not a
truncation (content reorganized and broadened, not dropped).

## Boundary preserved

Documentation only, candidate. No UI, renderer, Swiper, runtime, schema,
workflow engine, approval engine or memory engine. No `schemas/`, `tests/`,
`operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md`
change. No external action. Nothing promoted to canonical doctrine.

## Repo state

Documented non-implemented.

## Decision status

Accepted (architect):

- return to scenes / decks / cards / constellation (option B);
- navigation backbone Project -> Scene -> Deck; subject = scope filter.

To verify / to arbitrate:

- the gesture-axis mapping (rail = scene, vertical = deck, horizontal = siblings)
  vs the alternative left/right = hierarchy depth; remains candidate until mobile
  testing;
- forward reference to `ITERATIVE_DELIBERATION_LIFECYCLE.md` (PR #231) resolves
  once that note merges.
