# Pantheon system ownership registry

Status: candidate support registry — documented non-implemented.

`PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json` records the expected canonical owner of the principal concepts used across `Pantheon-Next`, `pantheon-mvp`, Hermes and Cockpit/OpenWebUI.

It supports cross-repository convergence checks. It does not replace `AUTHORITY_INDEX.md`, promote a candidate, authorize an execution, admit Evidence, approve a binding or make an implementation authoritative.

## Ownership rule

```text
one governed concept
→ one canonical semantic owner
→ zero or more conforming implementations
→ zero or more replaceable adapters
→ zero or more projections
```

The expected allocation is:

- `Pantheon-Next`: doctrine, governed semantics, schemas, statuses, scope, approvals and Capability Slots;
- `pantheon-mvp`: PostgreSQL persistence, APIs, executable projections, bounded adapters and integration seams;
- Hermes or another selected external runtime: execution, tools, provider routing and runtime-local state;
- Cockpit/OpenWebUI: interaction, display and decision surfaces.

A concept appearing in several repositories is not automatically a contradiction. It becomes a priority finding when a non-owner repository defines competing lifecycle, authority, status or approval semantics.

## Naming

Active concepts, modules, routes and contracts use responsibility-based names. Generation labels such as `v0`, `v1`, `v2` or `v3` are not stable architectural identities.

Revisions remain valid where they carry real history:

- ordered database migrations;
- source and Information revisions;
- ChangeCandidate base revisions;
- schema revisions;
- external protocol versions isolated at an adapter boundary.

## Use

The executable audit lives in `pantheon-mvp` and consumes this registry from a sibling checkout. The registry remains authoritative for ownership expectations; the audit remains report-only.

```text
audit finding != deletion proof
implementation != governance authority
projection != semantic owner
runtime success != Evidence
```
