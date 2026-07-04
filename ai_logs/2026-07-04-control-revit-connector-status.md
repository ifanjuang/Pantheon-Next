# AI Log — Revit connector status in Pantheon Control

Date: 2026-07-04

## Scope

Added a Revit connector status concept to the Pantheon Control static dashboard.

File changed:

```text
modified: docs/assets/pantheon-control/infrastructure.html
created: ai_logs/2026-07-04-control-revit-connector-status.md
```

## User intent

The user requested that the dashboard eventually show, in real time:

```text
Revit connector state;
authorized actions;
authorizations configurable from Revit.
```

## Work performed

Added a `Connecteur Revit` section to `infrastructure.html`.

The section displays the intended dashboard shape:

```text
connector status;
heartbeat / real-time signal placeholder;
active profile;
active RVT document placeholder;
authorized / configurable action families;
expected telemetry fields.
```

Action families shown:

```text
Lire / inspecter;
Capturer contexte visuel;
Annoter / paramétrer;
Créer / modifier modèle archi;
Supprimer / sauvegarder / synchroniser.
```

The page states that authorization configuration remains on the Revit plugin side. Pantheon Control reads and displays the status; it does not become the authority that activates runtime capability.

## Boundary

Static dashboard prototype only.

No Revit add-in, no connector, no heartbeat channel, no MCP service, no runtime, no backend route, no schema, no test, no operations file, no platform file, no Docker file, no `.env`, no `CLAUDE.md`, no `mcp-server/`, no GitHub Action and no external action was created.

## Repo state

```text
implemented: static HTML dashboard section
documented non-implemented: real-time Revit connector integration
runtime: absent
```

## Follow-up

When the Revit connector workstream is ready, the dashboard should read a local connector status object with at least:

```text
connected;
last_heartbeat;
revit_version;
active_document;
active_view;
selection_count;
worksharing_state;
profile;
authorized_actions;
last_transaction;
last_log_path;
stop_disable_visible;
```
