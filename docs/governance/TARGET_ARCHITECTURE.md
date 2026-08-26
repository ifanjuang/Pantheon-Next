# Target Architecture — coherence compass

Status: validation-only proposal — current architecture direction — documented non-implemented.
Boundary profile: validation_only_trace.

This document is a direction record, not a runtime or adoption proof. It names the smallest target composition justified by current owners and observed implementation.

## Target composition

```text
USER INTERACTION
  Hermes Web/dashboard
  optional compatible Hermes mobile/PWA client
        |
        v
EXECUTION
  Hermes Agent
        |
        | governed request / observation boundary
        v
GOVERNANCE
  Pantheon Next
  Task Contracts · policy/admission · Evidence · approval · Register
        |
        +-> Pantheon Cockpit
        |     governed projections and decision/review surfaces
        |
        +-> Obsidian workspace
              human Markdown notes and editable working projections
              |
              +-> Hindsight / runtime recall when separately selected

PROFESSIONAL SOURCES
  exact files / source representations under existing document/source owners
```

The target intentionally does not require OpenWebUI or Paperless.

## Responsibilities

| Layer | Owns | Does not own |
|---|---|---|
| Hermes Web/dashboard | chat, sessions, runtime controls, attachments | Pantheon governance or professional truth |
| Compatible mobile/PWA client | replaceable mobile projection of supported Hermes contracts | runtime authority, governance or durable truth |
| Hermes Agent | external execution, tools, skills, provider/session/runtime behavior | approval, Evidence admission or Registre Probatoire promotion |
| Pantheon Next | consequential status, contracts, gates, Evidence/approval/Register rules | general agent runtime, provider routing or chat UI |
| Pantheon Cockpit | governed product projections, Cards, navigation, review/decision surfaces | second general-purpose chat frontend or source of truth |
| Obsidian | human-authored Markdown workspace and editable working projections | DMS, governed Project identity, Evidence or canonical memory |
| Hindsight / Hermes memory | derived/runtime recall when selected | truth, Evidence or automatic durable promotion |
| Source/document owners | exact professional source identity and provenance | semantic truth merely because material exists |

## Core invariants

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
folder != governed identity
client compatibility != architecture authority
```

## Why OpenWebUI is absent

OpenWebUI previously filled chat/cockpit/Knowledge responsibilities that are now either native to Hermes clients or owned by the Pantheon Cockpit and existing Knowledge/workspace contracts.

Keeping it would create a second general interaction path without a demonstrated distinct responsibility. The integration is therefore refused as a target dependency.

## Why Paperless is absent

Core document intake and exact source/provenance handling do not require a DMS product. The co-located implementation already contains a bounded local/NAS source-ingestion path, while tool-agnostic document lifecycle owners govern source identity and derived representations.

Obsidian is not a Paperless replacement: it remains a Markdown workspace. Professional files keep their own source identity.

Paperless is therefore refused as a target dependency unless a future demonstrated capability gap cannot be met by existing source/document owners and a replaceable adapter.

## Hermes mobile/PWA posture

A mobile PWA is useful only as a replaceable Hermes client.

The reviewed `willscott-v2/hermes-mobile-pwa` repository is a plausible candidate because it is designed as a thin client for Hermes dashboard REST/WebSocket contracts rather than a second agent runtime. Selection, installation, network exposure and authentication still require separate verification.

```text
client works != client selected
client selected != Pantheon dependency
private-network reachable != safe public exposure
```

## Coherence criterion

The architecture is coherent when one bounded professional task can:

```text
start from an identified scope/source
-> pass existing Pantheon admission/policy boundaries
-> execute through Hermes
-> return reviewable candidates/observations
-> preserve Evidence/approval distinctions
-> project status in the Cockpit when useful
-> leave durable state only through the existing governed owner
```

No additional general-purpose frontend, DMS, scheduler, queue, provider router or memory authority is required to satisfy this criterion.

## Remaining proof gaps

Current repository implementation and documentation do not by themselves establish:

- production Hermes/Pantheon enforcement on the target host;
- selected mobile/PWA deployment;
- real-dossier authorization;
- production adoption of the co-located Cockpit;
- complete hardening of Obsidian/Hindsight synchronization and exposure;
- removal of all historical OpenWebUI/Paperless implementation compatibility code.

Those gaps must remain explicit rather than being filled with another architecture layer.

## Final rule

```text
Use Hermes for interaction and execution.
Use Pantheon for governance.
Use the Cockpit only for governed projections.
Use Obsidian for the human Markdown workspace.
Keep sources, memory and Evidence distinct.
Keep clients and adapters replaceable.
Remove superseded paths instead of maintaining parallel products.
```
