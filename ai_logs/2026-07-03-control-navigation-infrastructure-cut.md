# AI Log — Pantheon Control navigation and infrastructure cut

Date: 2026-07-03

## Scope

Applied the first progressive editorial cut to the Pantheon Control static HTML prototype.

Files changed:

```text
created: docs/assets/pantheon-control/infrastructure.html
modified: docs/assets/pantheon-control/nav.js
created: ai_logs/2026-07-03-control-navigation-infrastructure-cut.md
```

## User intent

The user approved the progressive cleanup approach:

```text
reduce the visible promise of the cockpit;
keep playful / useful cards;
remove noise from primary navigation;
do not delete old HTML immediately;
merge technical pages into a condensed infrastructure view first.
```

## Work performed

Created `infrastructure.html` as a condensed infrastructure page covering:

```text
visible surface;
execution;
observation;
service count;
machine / instance count;
connection / access count;
what stays outside Pantheon;
link to runtime-health prototype.
```

Shortened `nav.js` to the following visible navigation:

```text
Pilotage
- Accueil
- Preuves & statuts
- Décisions
- Rédaction candidate

Méthodes
- Skills & mémoire
- Références
- Modules & usages

Infrastructure
- Infrastructure
- Prototype UX
```

Removed from primary navigation, but did not delete:

```text
surveillance.html
services.html
machines.html
installations.html
observability.html
runtime-health.html
files.html
```

`runtime-health.html` remains reachable through `infrastructure.html` because it appears to be a useful detailed prototype, but it is no longer a top-level navigation item.

## Boundary

Static prototype navigation and HTML consolidation only.

No HTML deletion was performed.

No runtime, OpenWebUI plugin, Hermes skill, connector, scheduler, queue, approval engine, memory engine, backend route, schema, test, operations file, platform file, Docker file, `.env`, `CLAUDE.md`, `mcp-server/` or GitHub Action was created.

## Repo state

```text
static prototype update
documented non-implemented
progressive editorial cut
```

## Follow-up

Next recommended pass:

```text
1. Tighten home-manifest.js wording.
2. Reduce modules.html into grouped families.
3. Rewrite skills.html as reusable methods + memory posture.
4. After one verification pass, delete old technical pages only if no longer useful.
```
