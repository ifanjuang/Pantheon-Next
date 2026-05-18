# AI Log — Vertical central flow map

Date: 2026-05-18

## Scope

Updated the interactive Pantheon map to remove the fixed horizontal bands and switch to a vertical central composition.

## Files changed

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `ai_logs/2026-05-18-vertical-central-flow-map.md`

## Summary

Changed the map layout to a vertical central flow:

```text
User
-> OpenWebUI
-> Pantheon
-> Hermes
-> Evidence Pack
-> Human Decision
```

The diagram now uses side satellites instead of fixed horizontal bands:

- left side: documents, evidence, memory, Memory Gateway, Context Pack, Postgres;
- right side: LLM, MCP, external tools, web watch and skills;
- center: the governed dossier flow.

Clarified that:

- MCP is primarily connected to Hermes as the execution-side connector layer;
- Pantheon governs permissions, scope, evidence and memory use;
- Pantheon memory is reused by Hermes only through the governed chain:

```text
Pantheon Memory -> Memory Gateway -> Context Pack -> Hermes
```

Removed the large fixed bands because they made the map too rigid and visually confusing.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The map remains a documentation asset only.

No runtime, provider routing, scheduler, queue, hidden workflow engine, automatic approval, automatic memory promotion or skill installation was added.
