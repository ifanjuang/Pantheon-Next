# AI log — Hermes Role trace relay v3

Date: 2026-09-12
Status: implementation intervention — bounded transient transport.

## Problem

Hermes Runs exposes one live queue per run. Independent Cockpit and runtime
clients must not compete for that source stream or infer that it is a durable
multi-reader bus.

## Change

- added a one-source in-memory relay for already-admitted run events;
- added a fixed-upstream, read-only Hermes Runs SSE source with run-boundary,
  event-count and terminal-event checks;
- reused the v2 public Role projector rather than creating a second parser;
- added bounded replay and identical multi-subscriber delivery;
- added authenticated Cockpit status and SSE read routes with
  `Last-Event-ID` support;
- mounted those routes before the existing static Cockpit mount;
- added core, authorization, replay and route-order tests.

## Limits

```text
relay registration != run creation
relay observation != task authorization
bounded replay != persistence
SSE delivery != Evidence
multiple readers != message bus
```

The relay cannot launch, stop, approve or retry Hermes. Automatic attachment to
the governed one-shot run binding and the browser dialogue component remain
unimplemented. The filesystem-only Linux Workspace Cockpit was not given a
Hermes credential or outbound runtime dependency.

## Live acceptance

Synthetic run `run_2a643bdfe4a1442aa569c69dc7e2c678` was submitted directly to
the `pantheon-governed` Runs test surface and attached to the fixed upstream
reader immediately after admission. Two concurrent relay subscribers received
the same 12 projected events in the same order, with no relay diagnostic.

Observed public-stage starts relative to subscription:

```text
49.92s  Athena · Plan
55.58s  Hermes · Exécution
60.54s  Zeus · Statut
66.00s  terminal completion
```

The model did not invoke the requested read-only terminal tool. The observed
Hermes stage therefore came from its canonical public response header, not a
fabricated tool lifecycle event. This run proves progressive public-text
projection and two-reader fan-out only; it does not prove tool-stage projection
against the live runtime or visibility during private reasoning.
