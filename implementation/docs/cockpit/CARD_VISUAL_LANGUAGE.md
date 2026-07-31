# Cockpit card visual language

## Status

This document is the presentation contract for the main Cockpit card families.
It does not redefine the backend model, authorization, Evidence, claims, status
semantics or the CockpitSnapshot contract.

```text
visual projection != semantic model
project colour != status
UI status != authorization
animation != runtime activity unless explicitly projected
```

## Visual grammar

| Level / family | Front | Signature | Colour | Motion | Back |
|---|---|---|---|---|---|
| Pantheon Pack | dark solid or restrained gradient | three overlapping organic outline blobs | cyan, yellow, magenta | none by default; slow deformation only for explicitly projected activity | 4 px general border |
| Affaires Pack | strong solid gradient | several full organic blobs | Affaires palette | none by default | 1 px business border |
| Project Booster | white or very light solid surface | one full organic blob | stable project colour | none | 1 px business border |
| Work | white solid surface | project-coloured corner, 12 × 12 px | inherited project colour | none | 1 px business border |
| Folder | white solid surface | project-coloured top band, 12 px high | inherited project colour | none | 1 px business border |
| Information | solid or restrained family gradient | no blob | family palette | none | domain border |
| Knowledge | broad multicolour gradient | no extra motif | rich, calm palette | none | 4 px general border |
| Skills | richer mesh gradient | no permanent blob | more energetic than Knowledge | only for an explicit proposal or generation event | 4 px general border |
| Tools | flat bands or large colour fields | clean bands | stable technical palette | none | 4 px general border |
| Decision | highly legible solid surface | discreet project marker when applicable | project colour and status remain separate | none | 1 px business border |

## Invariants

- No paper texture, ruled paper, notebook grid or fake material texture.
- No drop shadow, glow, coloured shadow or relief effect.
- No decorative transparency as the main surface treatment.
- No hover animation and no animation tied to swipe navigation.
- Gradients belong to cards, not to the Cockpit backdrop.
- Project colour expresses project membership only.
- Status remains a separate icon, label or badge.
- Family styling is selected through projected attributes such as `data-family`.
- Family styles must not change Swiper geometry or card DOM contracts.

## Shared primitives

The following values are shared tokens rather than family-local magic numbers:

```text
business back border = 1 px
general back border = 4 px
project accent marker = 12 px
```

The same 12 px primitive is used as:

- a corner for Work;
- a full-width top band for Folder.

## Pantheon outline blobs

Pantheon uses organic outline blobs, not circles or rings.

The reference composition must:

- use three different asymmetric paths;
- keep cyan, yellow and magenta as separate contours;
- use a constant, crisp stroke;
- overlap without becoming a circular emblem;
- allow parts of the composition to extend beyond the card frame;
- remain decorative and `aria-hidden`;
- prefer reusable SVG paths over browser-dependent random `border-radius` shapes.

The final paths should be derived from the existing Pantheon site language rather
than invented independently inside each card stylesheet.

## Implementation boundary

Recommended cascade:

```text
shared card styles
→ v3_card_tokens.css
→ family-specific styles
→ v3_geometry.css
```

Family files may define colour and decoration, but must not own viewport, slide,
card size, safe-area or Swiper rules.

The renderer may project a stable family and a validated project accent value.
It must not contain rules such as “Work draws a corner” or “Folder draws a band”.
Those decisions remain CSS presentation rules.
