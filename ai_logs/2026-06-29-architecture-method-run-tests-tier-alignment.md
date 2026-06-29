# AI Log — Architecture Method Run Tests Tier Alignment

Date: 2026-06-29

Actor: ChatGPT

## Context

PR #244 merged the Architecture Method Deck visibility tiers.

The previous run-test PR #238 was useful but too dense: its examples displayed long visible task chains that conflicted with the cockpit budget.

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
specialist method only if triggered;
gate.
```

## Decision

Accepted:

```text
Use run tests as candidate support examples.
Test cockpit density, not exhaustive method display.
Keep Hermes bounded by Task Contract.
Keep gates visible before consequential effects.
```

Refused:

```text
Flat display of every plausible method.
Method chains acting as a hidden workflow engine.
Raw reasoning modes as cockpit cards.
```

## Boundary

Documentation only.

No schema, executable test, runtime, UI implementation, Hermes skill, connector, approval engine, memory engine, scheduler, queue or external action was added.

The validated remains.
