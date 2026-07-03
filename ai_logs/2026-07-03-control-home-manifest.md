# AI Log — Pantheon Control home manifest narrative

Date: 2026-07-03

## Scope

Reworked the Pantheon Control home-page introduction as a narrative manifest rather than a technical module inventory.

Files changed:

```text
created: docs/assets/pantheon-control/pages/home-manifest.js
modified: docs/assets/pantheon-control/index.html
created: ai_logs/2026-07-03-control-home-manifest.md
```

## Reason

The previous page explanation had become too slogan-like and then risked becoming too tool-centric.

The user approved the direction:

```text
home page = clear introduction to the problem and organizational choice;
modules.html = secondary deep-dive on module assets and usages.
```

## Content added

The new home narrative is structured in three parts:

```text
Pourquoi ce projet existe;
Pourquoi cette organisation;
Ce que Pantheon refuse.
```

It explains that AI can produce clean, structured and convincing outputs while leaving unresolved questions about:

```text
sources;
verification;
method;
working memory;
professional use;
human validation.
```

It keeps the role split:

```text
OpenWebUI makes the work visible;
Hermes prepares and documents;
Pantheon qualifies evidence, scope, status, memory and validation.
```

## Boundary

Static prototype wording update only.

No runtime, OpenWebUI plugin, Hermes skill, connector, scheduler, queue, approval engine, memory engine, backend route, schema, test, operations file, platform file, Docker file, `.env`, `CLAUDE.md`, `mcp-server/` or GitHub Action was created.

## Repo state

```text
static prototype update
documented non-implemented
```

## Note

The existing `home.js` was not replaced directly because earlier connector updates on that file were blocked. A separate `home-manifest.js` file overrides `renderHomePage()` after `home.js` loads.
