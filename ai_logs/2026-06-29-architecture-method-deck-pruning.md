# AI Log — Architecture Method Deck Pruning Review

Date: 2026-06-29

Actor: ChatGPT

## Context

The user asked for a qualitative review of the architecture Method Card deck after PR #237 reconciled Method Cards, the Card Stack model and the static Pantheon Control deck prototype.

Relevant active doctrine reviewed before editing:

```text
docs/governance/STATUS.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
docs/governance/METHOD_CARD_MODEL.md
docs/governance/ARCHITECTURE_METHOD_DECK.md
```

Open follow-up checked:

```text
PR #238 — architecture method run tests, draft, mergeable.
PR #240 — method Hermes handoff template, closed unmerged.
```

No open issue directly covered the qualitative deck-pruning question.

## Review finding

The architecture deck was doctrinally sound on boundaries: non-executable, candidate-only, no approval, no memory promotion, no external action.

The weak point was practical cockpit density.

The file listed all architecture Method Cards at the same apparent level. For agency use, that risks turning a Method Deck into a flat checklist. The cockpit needs a smaller visible set and a rule for when specialist cards appear.

## Change made

Updated:

```text
docs/governance/ARCHITECTURE_METHOD_DECK.md
```

Added:

```text
Practical deck posture
Visibility tiers
Selection rule
Review conclusion — 2026-06-29
```

The change classifies cards into:

```text
Tier A — gateway methods:
source_admission, assertion_mapping, mission_scope_guard,
external_commitment_guard, probative_review.

Tier B — dossier-specialist methods:
authority_qualification, contractual_decomposition, phase_gate_review,
site_observation_review, quote_variation_review, visa_commitment_review,
reception_risk_review, cerfa_field_claim_review.

Tier C — productive method:
constrained_generation.
```

The deck remains broad as a reference deck, but the cockpit should start with the smallest useful method set.

## Decision classification

Accepted:

```text
Keep the broad deck as candidate reference material.
Add visibility tiers and selection rules.
Use PR #238 run tests to check practical density.
```

Refused:

```text
Flat display of every Method Card in ordinary tasks.
Treating method order as a workflow engine.
Treating constrained_generation as proof, validation or approval.
```

To verify:

```text
Whether Tier A/B/C reduces cockpit noise on the three PR #238 run tests.
Whether long French labels and nested method cards remain readable on mobile.
Whether rare Tier B cards should later move to examples rather than main deck.
```

To arbitrate:

```text
Whether the architecture deck should eventually split into:
1. compact active cockpit deck;
2. extended reference deck;
3. run-test examples.
```

## Boundary preserved

Documentation only.

No schema, test, runtime, UI, platform, operations file, Docker file, environment file, Hermes skill, connector, approval engine, memory engine, queue, scheduler, provider router, external action or Registre Probatoire entry was added.

The validated remains.
