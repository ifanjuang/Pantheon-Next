# AI Log — MCP and memory flow clarification

Date: 2026-05-18

## Scope

Clarified MCP placement and governed memory reuse in the interactive Pantheon map.

## Files changed

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `ai_logs/2026-05-18-mcp-memory-flow-clarification.md`

## Summary

Updated the map to show that:

- MCP is connected primarily to Hermes as an execution-side tool gateway;
- OpenWebUI remains the visible cockpit for display, selection, approval and user interaction;
- Pantheon governs MCP usage through Task Contracts, scope, permissions and evidence expectations, but does not execute MCP directly;
- Pantheon also governs memory, including scope, evidence, approval, candidate memory, promotion, obsolescence and reuse;
- validated Pantheon memory can be reused by Hermes only through a governed path:

```text
Pantheon Memory -> Memory Gateway -> Context Pack -> Hermes
```

The map explicitly avoids the unsafe interpretations:

```text
Hermes -> Postgres direct
MCP -> Canonical Memory direct
LLM -> Memory direct
```

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

No runtime, provider routing, scheduler, queue, hidden workflow engine, automatic approval, automatic memory promotion or skill installation was added.
