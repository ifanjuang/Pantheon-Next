# AI Log — Interactive map visual hierarchy update

Date: 2026-05-18

## Scope

Updated the interactive Pantheon connection map visual hierarchy and detail panel behavior.

## Files changed

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `ai_logs/2026-05-18-interactive-map-visual-hierarchy.md`

## Summary

Applied a clearer visual hierarchy to the interactive map:

- `OpenWebUI` and `Hermes` use black backgrounds, white text and white outlines;
- `Pantheon` and `Memory Gateway` use white backgrounds, black text and black outlines;
- LLM nodes use semi-transparent black backgrounds;
- document, Knowledge and Context Pack nodes use transparent-style backgrounds with colored outlines;
- MCP, Google Workspace, Notion and Trello use colored backgrounds;
- secondary nodes were reduced in size compared with the three structural nodes;
- blocked direct paths remain visually distinct.

Changed the side panel behavior:

- the general overview is shown by default;
- clicking a bubble hides the general overview;
- the panel then shows only the selected element;
- selected element details now include tags and practical usage examples.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The map remains a documentation asset only.

No runtime, provider routing, scheduler, hidden workflow engine, automatic approval, automatic memory promotion or skill installation was added.
