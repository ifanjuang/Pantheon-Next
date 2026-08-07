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

The exact changed SVG structures and shared diagram stylesheet were rendered in an
isolated Chromium harness in French and English at:

```text
desktop: 1440 px viewport
mobile: 390 px viewport
```

The automated measurements covered:

```text
document scroll width against viewport width
all three figure bounds
per-diagram body client and scroll widths
horizontal-scroller containment on mobile
all SVG text bounds against each viewBox
French / English geometry parity
```

The first pass found one bounded French-only defect: `décision séparée` extended
slightly beyond the request-path SVG viewBox. The shared station-9 technical label
was reduced from 9 px to 8 px through the diagram stylesheet. The second pass found:

```text
no page-level horizontal overflow in either language or viewport
all three figures contained on desktop
headers, notes and legends contained at both sizes
mobile diagram body client width: 284 px
mobile diagram body scroll width: 680 px
horizontal scrolling confined to each diagram body on mobile
no SVG text outside any viewBox
```

The visual renders show the complete four-role diagram, nine-station flow and
honesty map in both languages. This correction changes presentation only; it does
not alter the meaning or position of the separate memory-promotion gate.

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
