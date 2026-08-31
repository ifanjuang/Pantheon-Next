# A2UI Cockpit qualification lab

Status: implementation artifact — qualification candidate — not adopted, not activated, not production-authorized.

## Objective

Qualify A2UI as an optional declarative projection protocol for dynamic Pantheon Cockpit content without creating a new business object, persistence path, authorization path, navigation root, Card owner or second Cockpit application.

The first fixture mirrors the shape of a bounded multi-source research result discussed in open Pantheon work. It has no code dependency on that branch and does not change the source-research Workflow Manifest, Evidence, Source, Document, Knowledge or Decision owners.

```text
research result candidate
-> bounded A2UI messages
-> restricted Pantheon presentation catalog
-> Lit renderer
-> human-visible projection
```

The renderer is downstream of governed state. It is not an owner of that state.

## Qualification pins

Protocol selected for this lab:

```text
A2UI protocol: v0.9.1
```

Top-level package pins:

```text
@a2ui/lit       0.10.3
@a2ui/web_core  0.10.6
lit              3.3.3
vite             8.2.2
```

Package version and protocol version are separate facts. The v0.9 renderer path is imported explicitly and `MessageProcessor` is configured for `v0.9.1`.

This lab does not establish dependency adoption. A reviewed lockfile and executable build observation are still required before any production or Cockpit integration decision.

## Closed catalog

`catalog.js` derives a small catalog from the official Lit basic catalog and admits only:

```text
Column
Row
Text
Card
Divider
Button
```

No catalog functions are registered.

`guard.js` fails closed before A2UI messages reach the official processor:

- protocol must be exactly `v0.9.1`;
- surface and catalog IDs must match the qualification contract;
- unknown components are rejected;
- `functionCall` actions are rejected;
- unknown event actions are rejected;
- `sendDataModel=true` is rejected;
- secret-like fields are rejected from the UI data model;
- message count, component count and data-model size are bounded.

The only admitted event is:

```text
pantheon.prepare_hermes_handoff
```

In this lab it does **not** call Hermes or a Pantheon endpoint. `main.js` converts it into a local `cockpit_intent_candidate` event with:

```text
executed: false
persisted: false
authorized: false
```

## Run locally

From this directory:

```bash
npm install
npm run test:guard
npm run build
npm run test:browser
```

For interactive inspection:

```bash
npm run dev
```

`npm install` is a qualification action for this isolated lab only; it is not an installation or activation decision for Pantheon.

`test:browser` starts only a loopback Vite preview and a loopback Chrome DevTools connection. It verifies that the official A2UI processor/renderer displays the fixture, that the native rendered button can be clicked, and that the click yields only the bounded local intent.

## Boundaries

```text
A2UI message != governed object
A2UI data model != persistence
rendered status != authorization
A2UI event != approved action
retrieved source != truth
research summary != Evidence
runtime success != Evidence
package installed != dependency adopted
lab present != Cockpit integration
```

The product render path in `main.js` performs no business HTTP request, runtime WebSocket connection or browser persistence. The qualification harness uses loopback HTTP for Vite preview and a loopback Chrome DevTools WebSocket only to observe render/click behavior; it does not contact Hermes or Pantheon business endpoints.

## Integration decision after qualification

Only if this lab is separately validated should a later slice consider a tiny adapter in the current Cockpit boot chain. That later slice must reuse current Card/context/action owners and must not create:

```text
A2UISurfaceRecord
GenUI registry
second navigation root
second boot chain
direct generated-button -> business endpoint routing
```
