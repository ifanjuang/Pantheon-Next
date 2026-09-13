# AI log — Hermes Role stage projector v2

Date: 2026-09-12
Status: implementation intervention — transient adapter, no durable trace.

## Observation

Hermes Agent 0.21.2 exposes public Runs events including `message.delta`, tool
lifecycle events and terminal run events. It does not emit a native
`role.stage` event. A live governed test returned visible `Athena`, `Hermes` and
`Zeus` sections, but only after the model had finished its private computation.
That output must not be described as Roles acting during hidden reasoning.

Observed run:

```text
run_48696b8dbd0249afb6db974a3bf1a5e8
```

## Change

- added an incremental projector for canonical public Role headers;
- projected observed `tool.started` / `tool.completed` pairs as transient
  `Hermes · Exécution` stages;
- excluded `reasoning.available` by construction;
- exposed derived stages beside raw events in the existing live-acceptance
  collector;
- added tests for split stream chunks, ordered transitions, tool pairing,
  terminal flushing, unknown labels and bounded failure.

## Boundary

```text
derived_transient role.stage != native Hermes event
public milestone != private reasoning
visible Role != autonomous agent
Role stage != Role Signal
Role stage != Evidence, approval or authorization
```

No service, Cockpit view, database, queue, workflow engine, prompt disclosure or
runtime patch was added. Progressive client delivery and UI rendering remain a
later slice.
