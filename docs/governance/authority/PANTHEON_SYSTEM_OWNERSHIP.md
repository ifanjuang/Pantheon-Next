# Pantheon system ownership registry

Status: candidate support registry — documented non-implemented.

`PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json` records separate ownership dimensions for the principal concepts used across `Pantheon-Next`, `pantheon-mvp`, Hermes and Cockpit/OpenWebUI.

It supports cross-repository convergence checks. It does not replace `AUTHORITY_INDEX.md`, promote a candidate, authorize an execution, admit Evidence, approve a binding or make an implementation authoritative.

## Ownership rule

```text
one governed concept
→ one semantic owner
→ one implementation owner when implemented
→ one runtime owner when execution is involved
→ one projection owner when interaction is involved
```

These dimensions must not be collapsed.

For example, Pantheon Next may own the semantics and limits of a Cockpit projection while `pantheon-mvp` owns its server-side implementation and Cockpit/OpenWebUI owns its interactive rendering. Likewise, Pantheon Next governs the admission and boundaries of Hermes execution while Hermes owns the runtime execution itself.

The expected allocation is:

- `Pantheon-Next`: doctrine, governed semantics, schemas, statuses, scope, approvals and Capability Slots;
- `pantheon-mvp`: PostgreSQL persistence, APIs, executable projections, bounded adapters and integration seams;
- Hermes or another selected external runtime: execution, tools, provider routing and runtime-local state;
- Cockpit/OpenWebUI: interaction, display and decision surfaces.

A concept appearing in several repositories is not automatically a contradiction. It becomes a priority finding only when a repository exceeds its assigned dimension, for example by redefining a lifecycle it only implements, by executing work it only governs, or by treating a projection as authorization.

## Naming

Active concepts, modules, routes and contracts use responsibility-based names. Generation labels such as `v0`, `v1`, `v2` or `v3` are not stable architectural identities.

Revisions remain valid where they carry real history:

- ordered database migrations;
- source and Information revisions;
- ChangeCandidate base revisions;
- schema revisions;
- external protocol versions isolated at an adapter boundary.

A reference to an externally versioned endpoint is not equivalent to an internally versioned architecture. The adapter must isolate that protocol detail instead of propagating it into domain or Cockpit identities.

## Use

The executable audit lives in `pantheon-mvp` and consumes this registry from a sibling checkout. The registry remains authoritative for ownership expectations; the audit remains report-only.

```text
audit finding != deletion proof
semantic owner != implementation owner
implementation owner != runtime owner
projection owner != authorization authority
runtime success != Evidence
```
