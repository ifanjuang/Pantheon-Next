# Pantheon system ownership registry

Status: candidate support registry — documented non-implemented.

`PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json` records separate ownership dimensions for the principal concepts used across Pantheon governance, Pantheon implementation, Hermes and Cockpit/OpenWebUI.

It supports monorepo-zone convergence checks. It does not replace `AUTHORITY_INDEX.md`, promote a candidate, authorize an execution, admit Evidence, approve a binding or make an implementation authoritative.

## Ownership rule

```text
one governed concept
→ one semantic owner
→ one implementation owner when implemented
→ one runtime owner when execution is involved
→ one projection owner when interaction is involved
```

These dimensions must not be collapsed.

Owner identities name responsibilities. They are deliberately independent from Git repository names and filesystem paths.

```text
repository != owner identity
zone/path != owner identity
co-location != authority transfer
```

The expected allocation is:

- `Pantheon governance`: doctrine, governed semantics, schemas, statuses, scope, approvals and Capability Slots;
- `Pantheon implementation`: PostgreSQL persistence, APIs, executable projections, bounded adapters and integration seams;
- `Hermes/external runtime`: execution, tools, provider routing and runtime-local state;
- `Cockpit/OpenWebUI`: interaction, display and decision surfaces.

The first two responsibilities are currently co-located in the `Pantheon-Next` monorepo. Governance material primarily lives at the repository root while the bounded executable candidate lives under `implementation/`. This physical topology does not merge their responsibilities or authority.

A concept appearing in several zones is not automatically a contradiction. It becomes a priority finding only when a zone exceeds its assigned dimension, for example by redefining a lifecycle it only implements, by executing work it only governs, or by treating a projection as authorization.

## Repository-name migration

Registry revision 3 retires repository names as active owner identities:

- former semantic-owner label `Pantheon-Next` → `Pantheon governance`;
- former implementation-owner label `pantheon-mvp` → `Pantheon implementation`.

This is an identity clarification, not a responsibility transfer. Historical documents may continue to mention the former repositories when describing repository history or provenance.

The Architecture Audit keeps an independently pinned copy of this registry. Adoption of revision 3 therefore requires a separate pin change after this revision is merged; the registry cannot rewrite the rule used to judge its own pull request.

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

The executable audit is co-located under `implementation/tools/` and consumes this registry through an independently pinned authority snapshot. The registry remains authoritative for ownership expectations; the audit remains report-only.

```text
audit finding != deletion proof
semantic owner != implementation owner
implementation owner != runtime owner
projection owner != authorization authority
runtime success != Evidence
```
