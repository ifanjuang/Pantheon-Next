# AI Log — Hermes MoA Review Classification

Date: 2026-06-29

Actor: ChatGPT

## Context

The user asked how to treat Hermes Mixture-of-Agents in the Pantheon Next model after reviewing public MoA material and the ongoing Method Card / Card Stack work.

PR #237 already contains the correct Method Card / Card Stack reconciliation branch:

```text
chatgpt/reconcile-method-cards-html
```

Because `CARD_STACK_MODEL.md` and `METHOD_CARD_MODEL.md` already exist in that PR, this intervention avoids creating a duplicate model on `main`.

## Decision

Accepted:

```text
MoA as Hermes runtime capability / runtime_pattern Method Card candidate.
```

Refused:

```text
MoA as Pantheon authority, Zeus substitute, truth engine, approval engine, proof engine, canonical memory engine or external-action authority.
```

To verify:

```text
quality lift;
cost;
latency;
provider exposure;
repeatability on Pantheon and architecture-domain tasks.
```

To arbitrate:

```text
whether MoA should later move from candidate runtime_pattern to active adapter support after internal benchmark.
```

## Files changed

Updated:

```text
docs/governance/METHOD_CARD_MODEL.md
```

Created:

```text
docs/governance/reference_reviews/HERMES_MOA_REVIEW.md
ai_logs/2026-06-29-hermes-moa-review.md
```

## Boundary preserved

Documentation only.

No schema, test, runtime, platform, operations file, Docker file, environment file, Hermes preset, Hermes skill, connector, provider router, benchmark harness, approval engine, memory engine or external action was added.

## Placement

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

MoA belongs to Hermes-side execution.

Pantheon only governs consequential effects: truth, evidence, memory, approval, scope and external action.

## Short invariant

```text
MoA increases deliberation.
It does not increase authority.
```

The validated remains.
