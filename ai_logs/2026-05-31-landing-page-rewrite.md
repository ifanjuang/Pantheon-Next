# AI Log — Landing page rewrite for liberal professions

Date: 2026-05-31

## Scope

Rewrote the GitHub Pages landing page (`docs/index.html`) to be more impactful,
simpler, more professional, addressed to liberal professions, and more
compelling — within the editorial honesty boundary.

## Changes made

Updated:

- `docs/index.html` (full rewrite).

Added:

- `ai_logs/2026-05-31-landing-page-rewrite.md`.

## Grounding in the sources of truth

Per `CLAUDE.md`, the rewrite follows the active doctrine:

- `NARRATIVE.md` — start from the reader's situation, never from technology or
  tooling; boundaries before mechanisms; end on the human decision. The previous
  page opened with "couche de gouvernance pour systèmes IA" (technology-first);
  the new hero opens with "L'IA répond vite. C'est vous qui signez."
- `PRODUCT_DIFFERENTIATION.md` — "the governed configuration layer between AI
  tools and professional responsibility"; not a chatbot / agent builder / RAG
  product / provider router / plugin marketplace / compliance certification.
- `EDITORIAL_LANGUAGE.md` — allowed language used; forbidden claims avoided. The
  honesty section states what Pantheon is NOT, in negated form ("ne sécurise pas
  tout seul", "ne garantit aucune conformité automatique"), and points to
  `STATUS.md`. No "safe AI", "automatic protection", "compliance guarantee" or
  "turnkey" claim.
- `VISUAL_LANGUAGE.md` — exposure (cool/blue), execution (warm/amber),
  governance (gold); risk in red; a direction-bearing flow line that ends on
  "vous décidez".

## What changed structurally

- new situation-first hero with a one-line flow (you -> what enters -> AI ->
  what leaves -> you decide) and clear CTAs;
- "Le vrai problème" reduced to three concrete risks (accidental commitment,
  source-vs-proof, drifting memory);
- "Comment ça marche" as three plain layers (expose / execute / govern) stating
  Pantheon is not a funnel;
- a concrete email example (compelling and true);
- a "Pour votre métier" section with one line per profession;
- a benefits block; an honest "ce que ce n'est pas" trust section with a
  `STATUS.md` pointer.

## Removed

- the technical "Modules optionnels" grid (Langflow / LangGraph / Langfuse /
  provenance) — engineering noise for a liberal-profession audience; this keeps
  the page simpler and on-message. Those layers remain documented in governance.

## Honesty boundary

The page describes method, not implemented product. It markets the method and
the human-decision boundary, never a guarantee. Verified: no forbidden
affirmative phrase; HTML tags balanced.

## Refinement pass (same day)

After review, two message ("propos") deviations were corrected and the tone was
refined toward "impactful but sober and restrained":

- **broken link fixed:** the footer linked `governance/PRODUCT_POSITIONING.md`,
  which does not exist; corrected to `PRODUCT_DIFFERENTIATION.md` (the real
  positioning doc);
- **message corrected:** the hero said "Pantheon gouverne la décision", which
  conflicts with `EDITORIAL_LANGUAGE.md` (public verb is *cadrer*, not
  *gouverner*; the human decides). Reworded: "Vos outils portent le travail ;
  vous gardez la décision et la signature" and a lead built on the real market
  sentence ("la couche de méthode entre les outils ... et la responsabilité");
- **sober visual:** background gradients softened (lower alpha), keeping a
  restrained, editorial dark theme.

All other claims were verified faithful to doctrine: frames what enters / sent /
leaves / remains; human decides; not a chatbot or agent; interchangeable tools;
no forbidden affirmative phrase.

## Note: unrelated CI state

The governance phrase scan is red on `main` itself (not from this page): several
recently added governance docs (`REVIEW_QUEUE.md`, `URGENT_REVIEW_TRIAGE.md`,
`ARCHITECTURE_PROOF_REGISTER.md`, etc.) use the word "queue" in the
review-queue / human-decision sense, which the scanner flags as runtime. The
scanner does not read `index.html`. Resolving that is a separate governance
decision, surfaced to the user.

## Explicit non-implementation

No runtime added. No files touched under `schemas/`, `tests/`, `hermes/`,
`operations/`, `pyproject.toml`, or `CLAUDE.md`.
