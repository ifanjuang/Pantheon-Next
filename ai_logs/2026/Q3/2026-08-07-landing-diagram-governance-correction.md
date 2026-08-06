# Landing diagrams — governance correction

Date: 2026-08-07
Status: documentation and static-site change only.

## Objective

Add visual explanations to the public landing while preserving the current
Pantheon authority and runtime-status boundaries.

## Corrections after review

The first diagram draft incorrectly assigned authorization to the framework and
described memory as requiring a generic second signature.

The reviewed wording is:

```text
OpenWebUI displays.
Hermes executes bounded work.
Pantheon governs, verifies and records.
The professional decides consequential effects.
```

Memory promotion is a separate governed decision. It is not an automatic step and
is not inferred from a prior decision record.

The honesty map was compared with `docs/governance/WHAT_RUNS.md`. Its third column
now means `not operational here`: external implementation candidate, not deployed,
not connected or documentation-only. It no longer labels all those states as
`written, not built`.

## Diff posture

The PR adds three inline explanatory diagrams and a bounded diagram stylesheet. It
also replaces the previous four-card flow presentation with a nine-station visual
flow; the PR description must state that replacement rather than claim that no
content was removed.

## Boundaries

```text
static diagram != live capability
external implementation != installed
implemented != adopted
framework governance != human authorization
memory candidate != promoted memory
```

No runtime, schema, API, Cockpit behavior, approval engine, memory engine,
scheduler, queue, provider router or external effect is added.
