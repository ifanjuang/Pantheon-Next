# Pantheon Control HTML Consolidation Decision

Status: active support note — static prototype consolidation.

Date: 2026-07-04

## Decision

The Pantheon Control cockpit keeps a short primary navigation and consolidates former technical pages under `docs/assets/pantheon-control/infrastructure.html`.

Primary visible navigation remains:

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

## Absorbed pages

The following former standalone pages have been absorbed editorially into the Infrastructure page:

```text
services.html
machines.html
installations.html
observability.html
files.html
surveillance.html
```

They are not part of the primary navigation anymore.

## Deletion status

Attempted deletion / redirection of the old standalone HTML shells was blocked by the GitHub connector safety layer during this session.

Therefore the decision is:

```text
Keep old pages in repository for now.
Treat them as hidden legacy shells.
Do not use them as primary cockpit structure.
Do not claim they are deleted.
```

This is safer than forcing deletion or manually recreating a risky state.

## Runtime boundary

This consolidation is static documentation / prototype work only.

It does not create:

```text
runtime behavior;
service launch;
machine wake;
installation procedure;
connector validation;
OpenWebUI plugin;
Hermes skill;
queue;
scheduler;
approval engine;
memory engine;
external action.
```

## Editorial rule going forward

If a page only explains infrastructure, service state, machine state, source intake or journal signals, it belongs under `infrastructure.html` unless it becomes a distinct governed decision surface.

If a page governs proof, memory, approval, scope, status, decision, or external action, it may remain a primary cockpit page.

## Current state

```text
Implemented: static HTML navigation and content consolidation.
Documented non-implemented: all runtime implications.
Partiel: old standalone HTML shells still exist but are out of navigation.
```
