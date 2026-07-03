# AI Log — Pantheon Control home tool qualities explanation

Date: 2026-07-03

## Scope

Expanded the Pantheon Control home-page explanation to answer why OpenWebUI and Hermes were chosen.

Files changed:

```text
docs/assets/pantheon-control/pages/home.js
docs/assets/pantheon-control/index.html
```

Added two explanatory cards:

```text
Pourquoi OpenWebUI ?
Pourquoi Hermes ?
```

## Rationale

The page now presents OpenWebUI as the exposure surface because it gives a readable discussion surface for models, knowledge bases, documents and team use.

The page presents Hermes as the execution runtime because it can carry profiles, skills, tools, verifications, long-running tasks and execution traces outside Pantheon.

The distinction remains:

```text
OpenWebUI quality: ergonomic exposure without final authority.
Hermes quality: operational execution without validation authority.
Pantheon quality: governance of status, evidence, memory, approval and external effects.
```

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Boundary

Static prototype update only.

No runtime, OpenWebUI plugin, Hermes skill, connector, scheduler, queue, approval engine, memory engine, backend route, schema, test, operations file, platform file, Docker file, `.env`, `CLAUDE.md`, `mcp-server/` or GitHub Action was created.

## Repo state

```text
static prototype update
documented non-implemented
```
