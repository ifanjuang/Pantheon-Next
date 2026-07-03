# AI Log — Pantheon Control modules usage page

Date: 2026-07-03

## Scope

Added a dedicated static HTML page explaining the role, advantages and professional use of each major module in the Pantheon Control stack.

Files changed:

```text
created: docs/assets/pantheon-control/modules.html
modified: docs/assets/pantheon-control/nav.js
created: ai_logs/2026-07-03-control-modules-usage-page.md
```

## User intent

The user asked for a less slogan-like, more detailed explanation of the assets and use cases of each module, including:

```text
LangFlow;
LangGraph;
LangChain;
Mem0 or another memory approach;
pgvector;
and related stack modules.
```

## Content added

The page explains the modules in professional language:

```text
OpenWebUI — visible work interface;
Hermes Agent — skills, working memory, tools and execution traces;
Pantheon — status, proof, scope, memory and validation frame;
LangFlow — visual prototyping of AI methods;
LangChain — composition of models, documents, tools and connectors;
LangGraph — long-running, stateful workflows with human intervention;
Memory agent / Mem0-style memory — useful recall, not validated memory;
pgvector — semantic search inside PostgreSQL;
RAG documentaire — source-grounded retrieval;
Langfuse — observability and trace review;
Ollama — local model hosting;
n8n — routine automation;
```

Each module is described by:

```text
atout;
usage concret;
limite Pantheon.
```

## Boundary

Static prototype and documentation only.

No runtime, OpenWebUI plugin, Hermes skill, connector, scheduler, queue, approval engine, memory engine, backend route, schema, test, operations file, platform file, Docker file, `.env`, `CLAUDE.md`, `mcp-server/` or GitHub Action was created.

## Repo state

```text
static prototype update
documented non-implemented
```

## Notes

A direct large edit to `home.js` was blocked by the connector guard. The safer route was to create a dedicated `modules.html` page and link it from the shared navigation.
