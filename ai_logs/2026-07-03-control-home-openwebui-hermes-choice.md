# AI Log — Pantheon Control home stack choice explanation

Date: 2026-07-03

## Scope

Updated the static Pantheon Control home page to explain why the stack separates OpenWebUI, Hermes and Pantheon.

Files changed:

```text
docs/assets/pantheon-control/pages/home.js
docs/assets/pantheon-control/index.html
```

Added:

```text
Pourquoi OpenWebUI + Hermes + Pantheon ?
```

The section explains:

```text
OpenWebUI exposes the dossier and decision surface.
Hermes executes bounded runtime work and returns candidates/traces.
Pantheon governs scope, evidence, status, memory, approval and external effects.
```

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The page states that a technically successful action remains a candidate until its status is validated.

## Boundary

Documentation/static prototype only.

No runtime, OpenWebUI plugin, Hermes skill, connector, scheduler, queue, approval engine, memory engine, backend route, schema, test, operations file, platform file, Docker file, `.env`, `CLAUDE.md`, `mcp-server/` or GitHub Action was created.

## Repo state

```text
static prototype update
documented non-implemented
```
