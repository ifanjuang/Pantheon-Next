# OpenWebUI central-owner convergence

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: active-owner reconciliation
Space: governance status / runtime interaction ownership
Change level: semantic

## Observed state

After merge of #767, `main` was revalidated at `6cc8dc4ee90f81a0e180bfbd561b0a21565e31c2`. `WHAT_RUNS.md` already selected Hermes Web/dashboard for chat, sessions and runtime controls and Pantheon Cockpit for governed projections. `STATUS.md` still carried the older doctrine `OpenWebUI exposes`, creating two incompatible active architecture descriptions.

The OpenWebUI documentation/template surface still has active incoming links. It is therefore not deleted in this slice; deletion requires a separate incoming-link convergence rather than leaving broken active owners.

## Change

- reconcile the canonical `STATUS.md` with the current target responsibility split;
- state Hermes Web/dashboard as the selected interaction baseline and Hermes Agent as external executor;
- state Pantheon Cockpit as governed Cards/navigation/decision/status projection, not a second generic chat frontend;
- mark OpenWebUI and Paperless-ngx as refused/retired target integrations with no current target responsibility;
- preserve optional/replaceable status for clients and provider bindings;
- make recurring governance invariants explicit in the central status owner;
- add a regression test that prevents `OpenWebUI exposes` from returning to canonical status.

## Deferred by evidence

`docs/governance/OPENWEBUI_INTEGRATION.md` and `templates/openwebui/` are not removed here because current active documents/examples still point to them. The next slice must classify each incoming link, preserve useful generic Hermes/Cockpit contracts under existing owners where needed, remove obsolete links, and only then delete the superseded OpenWebUI-owned surface.

## Invariants

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
folder/path != governed identity
provider selected != authority transfer
source capture != Evidence
green CI != adoption
```
