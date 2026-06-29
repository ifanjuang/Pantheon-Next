# AI Log — Architecture Method Deck Pruning Review

Date: 2026-06-29

Actor: ChatGPT

## Context

The architecture Method Card deck was reviewed after the Method Card / Card Stack reconciliation.

The original PR #241 conflicted with current `main` because `main` had added role-registry cleanup and `human_review` fields in the same document.

## Change made

Updated:

```text
docs/governance/ARCHITECTURE_METHOD_DECK.md
```

Added a practical cockpit-density layer:

```text
Tier A — gateway methods.
Tier B — dossier-specialist methods.
Tier C — productive method.
```

The change preserves the role-registry discipline already present on `main`.

## Decision

Accepted:

```text
Keep the deck broad as candidate reference material.
Add visibility tiers and selection rules.
Use PR #238 run tests to verify practical cockpit density.
```

Refused:

```text
Flat display of every Method Card.
Treating method order as a workflow engine.
Treating constrained_generation as proof, validation or approval.
```

## Boundary

Documentation only.

No schema, test, runtime, UI, platform, Docker, environment file, Hermes skill, connector, approval engine, memory engine, queue, scheduler or external action was added.

The validated remains.
