# Target Architecture — coherence compass

Status: validation-only proposal — current architecture direction — documented non-implemented.
Boundary profile: validation_only_trace.

This document is a direction record, not a runtime or adoption proof. It names the smallest target composition justified by current owners and observed implementation.

## Target composition

```text
USER INTERACTION
  Hermes Desktop
  selected rich interaction host
        |
        | local backend or authenticated remote Hermes connection
        v
EXECUTION
  Hermes Agent
  native context / files / memory when sufficient
        |
        | governed request / observation boundary
        v
GOVERNANCE
  Pantheon Next
  Task Contracts · policy/admission · Evidence · approval · Register
        |
        +-> Pantheon Cockpit
              governed projections and decision/review surfaces

BROWSER / ADMIN FALLBACK
  Hermes Web/dashboard
  browser interaction · runtime administration · remote-backend service surface

OPTIONAL REPLACEABLE BINDINGS
  workspace / note client
  synchronization transport
  retrieval / indexing / RAG
  external runtime memory

PROFESSIONAL SOURCES
  exact files / source representations under existing document/source owners
```

Pantheon does not require one particular workspace, synchronization product, RAG stack, memory engine or permanent Hermes client implementation.

## Responsibilities

| Layer | Owns | Does not own |
|---|---|---|
| Hermes-compatible clients | conversation, sessions and runtime interaction | Pantheon governance or professional truth |
| Hermes Desktop | selected rich interaction host, including local or remote Hermes runtime interaction when deployed | Pantheon authorization, governed persistence or professional truth |
| Hermes Web/dashboard | browser/admin fallback and Hermes remote-backend service surface where selected | Pantheon governance, Evidence admission or a second Pantheon projection owner |
| Hermes Agent | external execution, native runtime context/files/memory, tools and skills | approval, Evidence admission or Registre Probatoire promotion |
| Pantheon Next | consequential status, contracts, gates, Evidence/approval/Register rules | general agent runtime, provider routing, chat UI, RAG engine or memory engine |
| Pantheon Cockpit | governed product projections, Cards, navigation, review/decision surfaces | general-purpose chat frontend, source store or memory engine |
| Optional workspace binding | human working notes and editable projections when selected | governed Project identity, Evidence or canonical memory |
| Optional synchronization binding | convergence between selected workspace representations | knowledge authority, memory authority or professional approval |
| Optional retrieval / RAG binding | candidate retrieval, ranking and derived context when selected | truth, Evidence or scope authority |
| Optional external-memory binding | additional conversational/workstream recall when selected | truth, Evidence or automatic durable promotion |
| Source/document owners | exact professional source identity and provenance | semantic truth merely because material exists |

One implementation may provide several external functions, but the responsibilities remain separable and replaceable.

## Core invariants

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
folder != governed identity
sync success != professional approval
provider selected != Pantheon dependency
client selected != authority transfer
remote connection established != task authorized
UI action emitted != consequential effect authorized
```

## Zero-extra-provider posture

A valid Pantheon deployment may use Hermes without any external workspace, RAG or memory provider when its native capabilities are sufficient.

Current Hermes provides bounded persistent `MEMORY.md` / `USER.md`, session search and project/context-file loading. Those are Hermes runtime facilities, not Pantheon Knowledge or Evidence authority.

```text
Hermes native context/memory sufficient
-> no external provider required
-> Pantheon governance boundaries unchanged
```

External providers are justified only by a demonstrated capability need.

## Reference implementations, not prerequisites

The repository contains qualification evidence for a useful reference composition:

```text
Obsidian / Markdown
  -> workspace example

Self-hosted LiveSync / CouchDB
  -> synchronization example

Hindsight
  -> retrieval / external-memory example
```

These are recommendations and qualification targets, not Pantheon prerequisites.

```text
qualified implementation != architecture requirement
recommended binding != mandatory dependency
working integration != authority transfer
```

A user may prefer Hermes-native context and memory, Obsidian plus Hindsight, or another compatible implementation. Pantheon should care about the contract and governance boundary, not the product name.

## RAG posture

Pantheon does not own or require a canonical RAG stack.

The required boundary is narrower:

```text
identified source / scope
-> optional replaceable retrieval implementation
-> candidate context with provenance
-> task reasoning
-> Evidence only through the existing governed path
```

Vector stores, embeddings, rerankers, knowledge graphs and retrieval frameworks remain implementation choices. They must not become project identity, source truth, Evidence or authorization merely because retrieval succeeds.

A task that can be satisfied from explicitly selected source files or Hermes-native context does not need a RAG layer added merely for architectural symmetry.

## Memory posture

Pantheon governs no conversational-memory engine.

Hermes native memory is a valid baseline. An external memory provider may be selected when greater recall, semantic retrieval, sharing or another demonstrated capability is required.

Hindsight is currently a well-qualified candidate in this repository, but it remains replaceable. Mnemosyne and other reviewed providers are historical/candidate alternatives, not parallel mandatory paths.

Workspace-derived retrieval and conversational/workstream memory remain distinct responsibilities even when one provider can implement both. Separation may be expressed through banks, scopes, stores or an equivalent provider-specific mechanism.

```text
same provider != same responsibility
memory recall != source retrieval
memory persistence != Registre Probatoire
```

The existing Pantheon `external_runtime_memory` Capability Binding may remain unbound when Hermes native memory is sufficient.

## Why OpenWebUI and Paperless are absent

Neither product owns a distinct target responsibility anymore.

Hermes-compatible clients already cover runtime interaction, while existing source/document owners cover exact files and provenance. Keeping OpenWebUI or Paperless as target dependencies would create parallel product paths without a demonstrated necessary capability.

Their historical material remains provenance; compatibility code may be removed when no current consumer depends on it.

## Client posture

Hermes client implementations remain replaceable, but the current direction now distinguishes their roles.

Hermes Desktop is the selected rich interaction host. The reviewed Hermes line supports a native Desktop interaction surface and remote-backend operation, so the user-facing client may stay on one workstation while the Hermes runtime executes on another authenticated machine. That topology is an interaction/deployment choice, not an authority transfer.

Hermes Web/dashboard remains the browser/admin fallback and, where the Hermes remote topology requires it, the remotely reachable backend service surface. It is not removed and does not become a Pantheon Cockpit substitute.

The current generative-UI direction is to qualify A2UI, if still justified, inside the Hermes Desktop interaction layer rather than adding a general-purpose generative chat path to the Pantheon Cockpit. Any such renderer must remain presentation-only until an emitted UI intent passes the existing Pantheon/runtime effect boundary.

```text
Desktop selected != Desktop mandatory forever
remote Hermes reachable != remote Hermes qualified for governed work
A2UI rendered != A2UI adopted
A2UI surface != governed object
A2UI action != Pantheon authorization
client works != client selected
client selected != Pantheon dependency
```

A compatible mobile/PWA client can still be selected separately when its API compatibility, authentication and deployment boundaries are verified.

## Coherence criterion

The architecture is coherent when one bounded professional task can:

```text
start from an identified scope/source
-> use only the context/retrieval capability actually needed
-> interact through a replaceable Hermes client
-> pass existing Pantheon admission/policy boundaries when consequential
-> execute through local or authenticated remote Hermes
-> return reviewable candidates/observations
-> preserve Evidence/approval distinctions
-> project governed status in the Cockpit when useful
-> leave durable governed state only through the existing owner
```

No additional general-purpose frontend, DMS, scheduler, queue, RAG framework, provider router or memory authority is required by Pantheon itself.

## Final rule

```text
Pantheon specifies governance contracts, not a preferred personal knowledge stack.
Hermes Desktop is the current rich interaction direction, not a Pantheon authority.
Hermes Web/dashboard remains a replaceable browser/admin and remote-backend surface.
Hermes native facilities are sufficient when they satisfy the task.
External workspace, retrieval and memory providers stay optional and replaceable.
Sources, retrieved context, memory and Evidence remain distinct.
Remove superseded mandatory paths instead of replacing them with new mandatory products.
```