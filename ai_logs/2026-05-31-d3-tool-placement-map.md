# AI Log — D3 Tool Placement Map

Date: 2026-05-31

## Context

The user requested a clearer D3.js HTML schema to understand what belongs in Pantheon, OpenWebUI, Hermes, Langflow, LangGraph, Langfuse and provenance / GraphRAG support.

The requested visual distinction was:

- solid lines for mandatory core / continuous flows;
- dotted lines for optional modular capabilities;
- click behavior showing the file list and a plain-language explanation of each layer.

The user chose to modify the existing asset directly instead of creating a separate HTML file.

## Changed file

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`

## What changed

The existing D3 map was refocused as a tool-placement architecture map.

It now includes:

- a simplified title and legend;
- a mandatory core zone;
- an optional modules zone;
- solid and dotted link semantics;
- interactive click details for each node;
- file lists linked from the map;
- plain-language descriptions and boundary reminders for:
  - human decision;
  - OpenWebUI;
  - Pantheon Next;
  - Task Contracts;
  - Evidence Packs;
  - memory;
  - Pantheon Bridge;
  - Hermes Agent;
  - templates;
  - Langflow;
  - LangGraph;
  - Langfuse;
  - provenance / GraphRAG support;
  - rejected drift patterns.

## Boundary

This intervention updates a static documentation asset only.

It does not implement OpenWebUI, Hermes, Langflow, LangGraph, Langfuse or provenance runtime behavior.

It does not create an agent runtime, tool runtime, scheduler, queue, provider router, bridge API, OpenWebUI Function, Hermes skill, Langflow flow, Langfuse backend or graph runtime.

## Risk and limitation

The file is a monolithic HTML asset using D3 from a CDN, as before.

The map is intended for conceptual understanding and navigation.

It is not canonical doctrine by itself; the governance documents remain the authority.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```
