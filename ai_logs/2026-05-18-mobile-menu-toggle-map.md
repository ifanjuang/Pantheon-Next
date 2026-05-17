# AI Log — Mobile menu toggle for interactive map

Date: 2026-05-18

## Scope

Improved the interactive Pantheon connection map for mobile use.

## Files changed

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `ai_logs/2026-05-18-mobile-menu-toggle-map.md`

## Summary

Added a fixed `Menu` toggle button.

On desktop:

- the button shows or hides the right-side information panel;
- the map recenters after the panel state changes.

On mobile:

- the information panel becomes an off-canvas drawer;
- the drawer is hidden by default so it does not cover the graph;
- the toolbar lives inside the drawer;
- selecting a node opens the drawer with its details;
- the map keeps the full viewport available.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

This remains a documentation asset only.

No runtime, scheduler, provider router, automatic approval, automatic memory promotion or execution engine was added.
