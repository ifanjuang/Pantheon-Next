# Pantheon ecosystem map

Status: visual support asset — documentation only.

This folder contains an interactive HTML map showing why Pantheon Next needs a governance layer between professional users, AI execution, runtime memory, cockpit views and probative records.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The Registre Probatoire proves.
The human decides.
```

## Interactive map

- [`pantheon_next_mindmap_d3_v3_animated.html`](pantheon_next_mindmap_d3_v3_animated.html)

The map shows:

- the professional request and the human decision gate;
- OpenWebUI as the visible exposure surface;
- Pantheon Next as the law and gate layer for scope, status, evidence, approvals and external-action boundaries;
- Hermes Agent as the execution runtime;
- Hermes runtime memory as recall without authority;
- Evidence Packs and Register Candidates as reviewable candidate material;
- the Registre Probatoire as the only governed record that may be cited for consequential decisions;
- Notion or another database view as an optional synchronized cockpit, not as the probative source of truth by itself;
- blocked shortcuts such as `Hermes memory -> client commitment` and `database row -> proof`.

## Why the wording changed

The former map used `memory` at the bottom. That was misleading after the Registre Probatoire direction: memory belongs to Hermes and external runtime adapters. Pantheon governs what may become probative: a scoped, dated, cited and approved Registre Probatoire entry.

```text
Memory may speak.
Only the Registre Probatoire may be cited.
```

## README embedding note

GitHub README files should link to the HTML file rather than embed it as an iframe.

A future documentation site may render this map directly or embed it inside an iframe.

## Doctrine boundary

This asset is explanatory only.

It does not implement runtime integration, provider routing, connector sync, database storage, Registre Probatoire storage, automatic approval, skill installation, scheduling, queues or hidden workflow execution.

The animation shows conceptual flows. It does not mean Pantheon executes those flows.
