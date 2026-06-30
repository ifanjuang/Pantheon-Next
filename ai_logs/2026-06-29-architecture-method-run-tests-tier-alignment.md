# AI Log — Architecture Method Run Tests Tier Alignment

Date: 2026-06-29

Actor: ChatGPT

## Context

PR #244 merged the Architecture Method Deck visibility tiers.

The previous run-test PR #238 was useful but too dense: its examples displayed long visible task chains that conflicted with the cockpit budget.

Codex review on PR #245 found one valid inconsistency: the chantier run test made `assertion_mapping` the primary method, while `ARCHITECTURE_METHOD_DECK.md` defines the chantier report pattern with `site_observation_review` as the primary method and `assertion_mapping` as verification.

## Change made

Created a compact replacement document:

```text
docs/governance/ARCHITECTURE_METHOD_RUN_TESTS.md
```

The document keeps the three useful architecture cases:

```text
chantier report;
complementary quotation;
CERFA / administrative filing.
```

It rewrites them around:

```text
primary method;
guardrail method;
verification method;
specialist or additional verification only if triggered;
gate.
```

Chantier correction after review:

```text
primary: site_observation_review
verification: assertion_mapping
additional verification if triggered: probative_review
```

Indexed the new document in:

```text
docs/governance/AUTHORITY_INDEX.md
```

Authority class:

```text
candidate support examples
```

Repo state:

```text
documented non-implemented
```

## Decision

Accepted:

```text
Use run tests as candidate support examples.
Test cockpit density, not exhaustive method display.
Keep Hermes bounded by Task Contract.
Keep gates visible before consequential effects.
Align run-test primary methods with the deck selection table.
```

Refused:

```text
Flat display of every plausible method.
Method chains acting as a hidden workflow engine.
Raw reasoning modes as cockpit cards.
Run-test examples contradicting the deck they exercise.
```

## Boundary

Documentation only.

No schema, executable test, runtime, UI implementation, Hermes skill, connector, approval engine, memory engine, scheduler, queue or external action was added.

The validated remains.
