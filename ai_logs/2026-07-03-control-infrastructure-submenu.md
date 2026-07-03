# AI Log — Pantheon Control infrastructure submenu consolidation

Date: 2026-07-03

## Scope

Integrated the hidden technical pages into `infrastructure.html` as internal submenu sections.

Files changed:

```text
modified: docs/assets/pantheon-control/infrastructure.html
created: ai_logs/2026-07-03-control-infrastructure-submenu.md
```

## User intent

The user clarified that the other pages should be integrated into the same page as submenu sections rather than kept as separate primary pages.

## Work performed

Expanded `infrastructure.html` into a parent page with internal anchors:

```text
Services;
Machines;
Installations;
Observabilité;
Sources;
Journal.
```

The page now absorbs the useful editorial role of the former standalone technical pages:

```text
services.html;
machines.html;
installations.html;
observability.html;
files.html;
surveillance.html;
runtime-health.html as detailed prototype link only.
```

The page makes clear that Pantheon Control:

```text
displays state;
surfaces risk;
prepares qualification;
does not operate infrastructure;
does not validate connectors;
does not launch services;
does not wake machines;
does not install tools;
does not turn traces into proof.
```

## Boundary

Static prototype content consolidation only.

No deletion was performed.

No runtime, OpenWebUI plugin, Hermes skill, connector, scheduler, queue, approval engine, memory engine, backend route, schema, test, operations file, platform file, Docker file, `.env`, `CLAUDE.md`, `mcp-server/` or GitHub Action was created.

## Repo state

```text
static prototype update
documented non-implemented
progressive editorial consolidation
```

## Follow-up

Next recommended pass:

```text
1. Verify the rendered Infrastructure page.
2. Tighten wording if the page feels too long.
3. If the submenu works, delete or archive old standalone technical pages in a later pass.
```
