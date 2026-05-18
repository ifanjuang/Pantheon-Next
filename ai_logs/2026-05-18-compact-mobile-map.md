# AI Log — Compact mobile map adjustment

Date: 2026-05-18

## Scope

Adjusted the vertical interactive Pantheon map for mobile readability after visual review on iPhone.

## Files changed

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `ai_logs/2026-05-18-compact-mobile-map.md`

## Summary

The previous vertical layout was doctrinally clearer but still too wide on mobile. The rendered view showed:

- too much empty vertical space above the graph;
- bubbles too small after auto-fit;
- left and right satellites placed too far from the central spine;
- side labels consuming useful mobile width.

Updated the diagram to a compact vertical coordinate system:

- central spine reduced from a wide desktop coordinate grid to a compact mobile-first coordinate grid;
- central flow remains vertical: User -> OpenWebUI -> Pantheon -> Hermes -> Evidence -> Decision;
- memory satellites moved closer to the central spine;
- LLM and MCP satellites moved closer to Hermes;
- side labels are hidden on mobile;
- fit logic allows a slightly larger scale for better readability;
- the governed memory loop remains explicit:

```text
Pantheon Memory -> Memory Gateway -> Context Pack -> Hermes
```

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

No runtime, provider routing, scheduler, queue, hidden workflow engine, automatic approval, automatic memory promotion or skill installation was added.
