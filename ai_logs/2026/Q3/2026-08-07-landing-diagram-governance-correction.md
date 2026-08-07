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
flow; the PR description states that replacement rather than claiming that no
content was removed.

## Responsive visual validation

The shared diagram surface and the French source were rendered in headless Chromium
at:

```text
desktop: 1440 px viewport
mobile: 390 px viewport
```

Measured results:

```text
document scroll width == viewport width at both sizes
no page-level horizontal overflow
all three figure bounds remain inside the page
all diagram headers and notes remain inside their containers
all legends wrap without horizontal overflow
mobile diagram bodies use overflow-x: auto
mobile diagram body client width: 284 px
mobile diagram body scroll width: 680 px
```

The desktop render shows the complete four-role diagram, nine-station flow and
honesty map without clipped text. The mobile render shows the expected left edge of
each wide SVG inside its bounded horizontal scroller; headers, notes and legends
remain fully visible.

The English source was then compared structurally with the rendered French source:

```text
same three figure wrappers
same viewBox dimensions
same diagram-body and legend classes
same responsive stylesheet
same horizontal containment behavior
```

The English authority, memory and status wording was reviewed in the actual source.
Its corresponding diagram labels fit the same fixed SVG boxes and are no longer
than the French critical labels already rendered. No FR/EN structural divergence or
additional overflow risk was found.

This validation concerns the static landing only. It does not claim a live
capability, installed integration or runtime status.

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
