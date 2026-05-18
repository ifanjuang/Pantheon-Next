# AI Log — Optimized bubble map

Date: 2026-05-18

## Scope

Optimized the interactive Pantheon connection map while preserving the bubble visual language.

## Files changed

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `ai_logs/2026-05-18-optimized-bubble-map.md`

## Summary

Replaced the dense network-style mindmap with a clearer bubble-based backbone:

```text
User -> OpenWebUI -> Pantheon -> Hermes -> Evidence Pack -> Decision -> Memory
```

Preserved bubbles, but reduced visual confusion by:

- making the main flow visible by default;
- placing secondary concepts around the backbone;
- adding a `Vue simple` mode;
- adding a `Vue technique` mode for documents, Knowledge, skills, LLM details, MCP, web and Postgres;
- adding an `Interdits` toggle for blocked paths;
- reducing link crossings;
- keeping click-to-detail behavior with tags and usage examples;
- keeping the fixed mobile menu.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The map remains a documentation asset only.

No runtime, provider routing, scheduler, queue, hidden workflow engine, automatic approval, automatic memory promotion or skill installation was added.
