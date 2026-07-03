# AI Log — Pantheon Control home navigation cache refresh

Date: 2026-07-03

## Scope

Updated `docs/assets/pantheon-control/index.html` to load the shortened navigation with the current cache-busting version.

Files changed:

```text
modified: docs/assets/pantheon-control/index.html
created: ai_logs/2026-07-03-control-home-nav-cache.md
```

## Reason

After `infrastructure.html` became the parent page for the former technical pages, `nav.js` contained the correct `Infrastructure` link, but `index.html` still loaded the navigation with an older query string:

```text
nav.js?v=20260621-connections-1
```

This could leave the home page using a cached older navigation in the browser.

## Change

Updated the home page to load:

```text
nav.js?v=20260703-editorial-nav-1
```

## Boundary

Static HTML cache/version update only.

No runtime, connector, approval, memory, backend, schema, test, protected path, Docker, `.env`, `CLAUDE.md`, `mcp-server/` or GitHub Action was changed.

## Repo state

```text
static prototype update
documented non-implemented
```
