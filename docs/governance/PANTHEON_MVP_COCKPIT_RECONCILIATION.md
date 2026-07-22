# Pantheon MVP Cockpit Reconciliation

Status: validation-only trace — external executable candidate status observation — documented non-implemented.
Boundary profile: validation_only_trace.

Date: 2026-07-22.

This document records the current Pantheon Next-side status of the external executable candidate `ifanjuang/pantheon-mvp` after the cards-first cockpit and bounded navigation-profile work merged.

It authorizes nothing, installs nothing, activates nothing and does not promote any runtime result into Evidence, approval or durable memory.

```text
Pantheon Next governs.
Hermes executes only under a separate bounded handoff.
OpenWebUI or the cockpit exposes projections.
The human decides.
```

## Pinned observation

```text
repository: ifanjuang/pantheon-mvp
merged change: pantheon-mvp#44
reviewed PR head: cdd4f793bd220dc5bb39465533988d65b5d1bf67
pinned main commit: 7f8989a670c6c476d55366bb0016a19dda3ebb6c
merge date: 2026-07-22
CI run: 29949615601
CI result: success
review threads: 6 resolved before merge
```

The candidate vendors the governed-loop schema families `mvp_governed_loop_objects`, `work_issue_slice` and `document_knowledge_slice`. Its recorded upstream pin remains `782afb474dec572e63d2c944007e1cf5bab37a09`.

A newer Pantheon Next commit is not by itself structural drift. The candidate's report-only monitor must establish actual schema divergence before any drift claim.

```text
new upstream commit != schema drift
schema coherence != adoption
CI success != professional Evidence
```

## Capability Slot

```yaml
capability_slot: governed_cards_first_cockpit
abstract_function: >-
  project-scoped Document, Knowledge and Work Issue projection; bounded resource
  orientation; proposal-only effect, site-manifest and navigation-profile previews;
  one signed and human-confirmed Knowledge update path
candidate_binding: ifanjuang/pantheon-mvp@7f8989a670c6c476d55366bb0016a19dda3ebb6c
execution_owner: external pantheon-mvp runtime / future Hermes-side bounded binding
pantheon_role: govern status, scope, evidence posture, adoption, activation and rollback visibility
implementation_status: implemented externally
installation_status: not installed by Pantheon Next
health_status: not checked on a target runtime
update_status: pinned observation recorded; operational update posture not checked
activation_status: not authorized
adoption_status: not adopted
production_use: forbidden
```

## Implemented externally

The pinned candidate contains:

- a cards-first cockpit for project Document, Knowledge and Work Issue projections;
- read-only resource profiles derived from existing project records;
- proposal-only effect rapprochement previews;
- proposal-only linked-site structure-manifest previews;
- proposal-only site navigation-profile previews;
- a signed, explicitly confirmed Knowledge `UPDATE` gate;
- browser-local offline drafts and legacy-draft recovery;
- a proposal-only Hermes edit-request seam;
- lifecycle-separated schema initialization;
- effective service-health posture;
- stable retry idempotency and post-update projection refresh;
- malformed-port, credential-bearing URL, localhost, `.local` and private-range target rejection.

These are repository implementation facts for the pinned candidate. They are not Pantheon Next implementation, installation or activation facts.

## Cockpit surfaces

### Read surface

A read-scoped key may expose project-scoped Document, Knowledge and Work Issue cards plus read-only resource profiles.

```text
projection != source
Knowledge != Evidence
card display != memory promotion
```

### Consequential Knowledge update surface

The only implemented consequential write path requires:

```text
editor credential
+ signing secret
+ declared human actor
+ exact project and Knowledge identity
+ immutable signed effect payload
+ bounded TTL
+ base-digest recheck
+ optimistic version check
+ idempotency key
+ explicit confirmation
```

The previous unsigned direct Knowledge revision route is retired with `410 Gone`.

Identity assurance remains partial: an editor credential plus a declared actor is not individual SSO or a cryptographically authenticated natural-person identity.

```text
declared != authenticated
signed effect != approved professional content
Knowledge updated != Knowledge reviewed
```

### Hermes proposal seam

A separate Hermes-scoped key may record a proposal-only edit request. Hermes receives no database credentials through this seam.

```text
queued edit request != Hermes proposal
Hermes proposal != accepted change
request recorded != runtime executed
```

## Preview posture

Effect, site-manifest and navigation-profile preview routes are implemented as proposal-only computation for the pinned candidate.

The reviewed implementation declares and tests:

```text
network requests: 0
persistence effects: 0
external action: none
approval effect: none
memory effect: none
```

The whole service may nevertheless expose the separately signed Knowledge update path. `/health` therefore reports the effective service posture as `read_only` or `bounded_read_write`, while preview effects remain separately identified as none.

```text
proposal route read-only != whole service read-only
idempotent DDL != read-only request
schema initialized != runtime request authorized
```

## Site navigation-profile status

The implemented navigation profile is deterministic orientation over public sites already linked from a Knowledge record.

It may return:

- a host-to-archetype classification;
- probable entry points;
- task families;
- a preferred retrieval strategy;
- fields that later execution should verify;
- candidate Hermes binding classes.

It does not perform:

- a network request;
- a live site inspection;
- a browse.sh catalog query;
- a skill security review;
- a skill installation;
- local skill generation;
- browser navigation execution;
- persistence of a navigation profile;
- a health probe;
- activation;
- Evidence admission.

Every related gate remains open:

```text
skill discovery or local-skill review
human task-scope approval
binding health review
activation authorization
```

Candidate bindings remain `to_verify`, `candidate_not_created` and `not_authorized`.

```text
profile candidate != site understood
skill discovered != skill installed
installed != approved
healthy != safe
navigation success != Evidence
page found != rule applicable to the project
```

## Responsibility split

### Pantheon Next governs

- Capability Slot classification;
- pinned repository and commit provenance;
- implementation, installation, health, update, adoption and activation status;
- permitted task and data scope;
- Evidence and Knowledge distinctions;
- human gates;
- rollback visibility;
- production-use prohibition.

### The external candidate executes

Only after separate installation and authorization, the external `pantheon-mvp` runtime may expose its implemented cockpit and bounded endpoints.

### Hermes may execute

Only after a separate reviewed binding, exact task scope and activation decision, Hermes may perform retrieval, navigation or proposal work. The current navigation profile does not perform that execution.

### OpenWebUI or the cockpit exposes

- project card projections;
- proposal-only previews;
- candidate binding posture;
- open gates;
- signed Knowledge update review state;
- health and boundary warnings.

### The human approves

- adoption;
- installation;
- real or client data use;
- exact task scope;
- skill admission or installation proposal;
- binding activation;
- consequential Knowledge changes;
- Evidence acceptance;
- production use.

### Forbidden in the current status

- treating merge as installation or adoption;
- treating health as safety;
- treating navigation success as Evidence;
- treating a declared actor as authenticated identity;
- automatic skill installation;
- automatic binding activation;
- unrestricted crawling;
- direct professional-dossier use;
- automatic memory promotion;
- external action without a separate current human decision.

## Adoption Gate

Adoption remains open and unauthorized.

```text
implemented externally != adopted
merged != installed
installed != approved
approved != activated
healthy != safe
runtime success != Evidence
```

A future adoption decision must identify at least:

- exact environment;
- allowed use;
- data posture;
- identity assurance;
- installed commit or image digest;
- health evidence;
- binding configuration;
- activation conditions;
- rollback procedure;
- expiry or review date.

No such adoption record is created by this reconciliation.

## Deployment posture

The eventual runtime progression remains sequential and separately gated:

```text
implemented
→ installation proposed
→ installation authorized
→ installed
→ health checked
→ binding reviewed
→ connected
→ policy enforcement verified
→ activation authorized
→ activated
```

Nothing in this document advances any step after `implemented externally`.

## Current classification

```text
implemented in Pantheon Next:
  this validation trace and the repository status boundaries that classify the external candidate.

implemented externally:
  the pinned pantheon-mvp cockpit, bounded previews and signed Knowledge update gate.

documented non-implemented in Pantheon Next:
  installation, connection, Hermes execution binding, activation and production adoption.

partially verified:
  exact pinned repository tree, CI behavior, review corrections and declared runtime contracts.

to verify:
  target-runtime installation, health, secrets, identity binding, live Hermes connection,
  operational rollback, real-data posture and professional correctness.

not adopted:
  the external candidate.

not activated:
  the external candidate.

forbidden:
  production use until a separate scoped human adoption and activation decision.
```

## Final rule

```text
Status may be recorded.
Implementation may be observed.
Hermes may later execute under a bounded contract.
OpenWebUI may expose review state.
Pantheon governs consequential status.
The human decides.
```
