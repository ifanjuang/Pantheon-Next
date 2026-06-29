# AI Log — Method Hermes Handoff Template

Date: 2026-06-29

Actor: ChatGPT

## Context

Created a candidate support template for projecting Method Cards into bounded Hermes execution.

The document is positioned as a Method Card specialization. It does not replace Task Contracts, Capability Placement or broader governed handoff doctrine.

## Change made

Created:

- `docs/governance/METHOD_HERMES_HANDOFF_TEMPLATE.md`

The document defines handoff candidates, executable Hermes handoffs, minimum handoff fields, approval ceilings, stop conditions, output discipline, Evidence Pack Candidate requirements, gate mapping, cost and density review, examples, bad handoffs and a review checklist.

## Boundary preserved

Documentation only.

The YAML shapes are templates only and non-schema.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- Hermes remains runtime only.
- Method handoffs must declare source perimeter, allowed outputs, forbidden outputs, approval ceiling, stop condition and return contract.
- Stop conditions must return a stop reason instead of runtime guessing.

To verify:

- merge order with PR 238;
- authority index placement;
- whether a future machine-checkable shape is needed later.

The validated remains.
