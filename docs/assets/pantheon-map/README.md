# Pantheon interactive connection map

Status: visual support asset — documentation only.

This folder contains an interactive D3.js map showing how the main Pantheon Next ecosystem parts relate to each other.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Interactive map

- [`pantheon_next_mindmap_d3_v3_animated.html`](pantheon_next_mindmap_d3_v3_animated.html)

The map shows:

- the user request and project dossier;
- OpenWebUI as the visible screen and container for documents, Knowledge and project spaces;
- Pantheon Next as the frame for entry, minimum necessary context, output and memory;
- Hermes Agent as the execution workshop;
- Hermes skills as execution capabilities, not approvals;
- local and external LLMs such as Ollama, ChatGPT, Claude and Gemini;
- MCP and external tools such as Google Workspace, Notion and Trello;
- Pantheon memory, for example Postgres, behind a governed Memory Gateway;
- blocked direct paths such as `Documents → LLM` without framing and `Hermes → Postgres` direct write.

## README embedding note

GitHub README files should link to the HTML file rather than embed it as an iframe.

A future GitHub Pages or documentation site may render this map directly or embed it inside an iframe.

## Doctrine boundary

This asset is explanatory only.

It does not implement:

- OpenWebUI runtime integration;
- Hermes runtime integration;
- LLM provider routing;
- MCP integration;
- Postgres memory runtime;
- automatic memory promotion;
- automatic approvals;
- skill installation;
- scheduler;
- queue;
- hidden workflow runtime.

The animation shows conceptual flows.

It does not mean Pantheon executes those flows.
