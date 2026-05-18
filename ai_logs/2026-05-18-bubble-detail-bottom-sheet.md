# AI Log — Bubble detail bottom sheet

Date: 2026-05-18

## Scope

Adjusted the interactive Pantheon map UX so bubble selection no longer opens the main control menu.

## Files changed

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `ai_logs/2026-05-18-bubble-detail-bottom-sheet.md`

## Summary

Changed the interaction model:

- the right-side menu remains a control menu only;
- clicking a bubble opens a lightweight bottom detail sheet;
- the bottom sheet shows only the selected element;
- the bottom sheet includes tags, description and usage examples;
- clicking elsewhere on the canvas closes the bottom sheet;
- closing the sheet clears the selected bubble highlight;
- switching view mode or toggling forbidden paths closes the active sheet.

This reduces cognitive load and prevents the menu from mixing global controls with contextual information.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The map remains a documentation asset only.

No runtime, provider routing, scheduler, queue, hidden workflow engine, automatic approval, automatic memory promotion or skill installation was added.
