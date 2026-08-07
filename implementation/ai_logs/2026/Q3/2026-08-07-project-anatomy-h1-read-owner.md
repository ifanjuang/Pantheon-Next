# Project Anatomy H1 — executable read owner

Date: 2026-08-07
Status: implementation candidate; CI pending.

## Objective

Begin tranche H from the merged Project Anatomy convergence trajectory without
creating a second graph, ontology or runtime path.

H1 establishes one project-scoped executable APU persistence owner and a server-side
read projection for an explicitly reviewed bootstrap dossier.

## Verified starting state

```text
Pantheon-Next main: 0da3cffcda288a26f62cf2e01b7358268ce054c1
pantheon-mvp main: 757518459380ca953bf68b28dae28e3adbea15de
```

The current repositories already contained:

```text
APU schemas and read-only referential checks
Execution Result -> APU mapping candidates
human mapping review
immutable add_match_to_existing_object write-command preparation
human write authorization
EntityRef and WorkIssue scope resolver arms for apu_object
```

The resolver arms intentionally failed closed because `agency_apu_objects` did not
yet exist. No open pantheon-mvp PR or Anatomy/APU branch overlapped this slice.

## Reused authority

The MVP vendors exact snapshots of the existing Pantheon-Next schemas for:

```text
shared APU vocabulary
stable_object
object_identity
object_relation
```

Each snapshot records its upstream repository, path, commit and blob SHA. Vendoring
is a local validation mechanism and transfers no authority.

## H1 owner

The executable owner adds:

```text
agency_apu_project_state
agency_apu_objects
agency_apu_object_relations
agency_apu_events
```

The Project state owns the optimistic aggregate revision used by later H2 command
application. `agency_apu_objects` is also the owner table already named by the
existing `apu_object` EntityRef and WorkIssue scope resolvers.

The owner validates stable objects, optional durable object identities and typed APU
relations against the governed schemas before persistence. PostgreSQL additionally
binds indexed identity/scope/relation columns to their JSON payloads and enforces
same-Project relation endpoints with composite foreign keys.

## Bootstrap boundary

`store_reviewed_dossier()` is an initialization seam for an already reviewed APU
dossier. It is not a runtime `create_stable_object` operation and is not exposed as
a Cockpit or Hermes write API in H1.

It requires:

```text
exact Project scope on every stable object
explicit review_ref
explicit actor
idempotency key
all relation endpoints inside the same reviewed dossier
```

A second bootstrap is refused unless it is the exact idempotent replay.

## Read projection

`get_project_anatomy()` returns:

```text
Project identity
owner revision
active stable objects
optional object_identity data
APU domain relations
explicit non-authority posture
```

It does not expose an H4 Cockpit surface yet.

## Boundaries

```text
reviewed dossier imported != automatic object creation admitted
APU object stored != Evidence
APU object stored != claim canonized
APU relation stored != Information relation
projection returned != editable UI truth
H1 owner exists != H2 write command applied
```

No Hermes runtime write, Evidence admission, Decision transition, WorkIssue closure,
ProjectClaim mutation, memory promotion or external effect is introduced.

## Required verification

```text
schema validation of stable_object / object_identity / object_relation
exact Project scope refusal
unknown relation endpoint refusal
idempotent replay and conflict
same-Project relational FK enforcement
append-only event history
composed migration order
Pantheon Architecture Audit
contract-tests
full PostgreSQL suite
```

H1 is complete only when those checks are green on the final PR head.
