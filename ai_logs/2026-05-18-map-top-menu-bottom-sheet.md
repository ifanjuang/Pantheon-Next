# AI Log — Map top menu and bottom sheet UX

Date: 2026-05-18

## Scope

Updated the interactive Pantheon map UX to separate view controls, global controls and bubble details.

## Files changed

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `ai_logs/2026-05-18-map-top-menu-bottom-sheet.md`

## Summary

Changed the map interaction model:

- view type controls are fixed at the top of the canvas:
  - `Vue simple`;
  - `Vue technique`;
  - `Interdits`.
- the global menu is now a top sheet:
  - full width;
  - limited height;
  - comes from the top;
  - includes secondary controls and the legend;
  - swipe up closes it on touch devices.
- bubble details remain a bottom sheet:
  - limited height;
  - comes from the bottom;
  - contains only the selected bubble information;
  - swipe down closes it on touch devices.

The right-side desktop panel was removed from the interactive map in favor of a unified responsive interaction model.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The map remains a documentation asset only.

No runtime, provider routing, scheduler, queue, hidden workflow engine, automatic approval, automatic memory promotion or skill installation was added.
