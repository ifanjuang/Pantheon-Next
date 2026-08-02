# Cross-repository Pantheon architecture audit

The architecture inventory considers `Pantheon-Next` and `pantheon-mvp` together.

The ownership registry is maintained in `Pantheon-Next`:

```text
docs/governance/authority/PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json
```

`pantheon-mvp` consumes that registry. It does not define the canonical ownership rules it is being checked against.

## Canonical allocation

- `Pantheon-Next`: doctrine, governed concepts, schemas, statuses, Evidence, scope, approvals and Capability Slots.
- `pantheon-mvp`: PostgreSQL, APIs, executable projections, adapters and bounded integration seams.
- Hermes or another selected external runtime: execution, tools, provider routing and runtime-local state.
- Cockpit/OpenWebUI: interaction and projection only.

## Review dimensions

Every active artifact is reviewed for:

- generation-named paths and internal identities;
- versioned internal routes;
- exact duplicates and repeated names across repositories;
- competing definitions of one governed concept;
- excessive distribution of one implementation across modules;
- runtime responsibilities implemented in Pantheon;
- obsolete compatibility paths;
- incorrect definition, implementation, adapter or projection placement.

Empty files are not treated as meaningful duplicates. Vendored, historical and migration artifacts remain visible but are assigned a lower cleanup priority.

## Priorities

```text
P0  authority conflict or forbidden runtime responsibility
P1  active versioned identity or competing execution path
P2  fragmentation, compatibility residue or internal duplicate
P3  cross-repository duplicate requiring owner selection
P4  naming, placement or reference convergence review
P5  historical, vendored or migration cleanup
```

Every finding has a deterministic identifier and starts with `review_state: unreviewed`. The identifier can later anchor a reviewed decision without turning the audit into an approval engine.

## Naming rule

Active architecture names are responsibility-based. `v0`, `v1`, `v2`, `v3` and any later generation token are not permanent identities for modules, routes, schemas, projections or folders.

Revisions remain valid where they preserve actual history:

- ordered database migrations;
- source and Information revisions;
- ChangeCandidate base revisions;
- schema revisions;
- external protocol versions isolated inside an adapter.

## Decision vocabulary

```text
retain
simplify
merge
move
vendor/reference only
deprecate
remove
```

A finding is not deletion proof. Removal requires evidence that no active import, route, script, deployment, schema, authority document or compatibility obligation remains.

## Usage

With sibling checkouts:

```bash
python tools/audit_pantheon_architecture.py \
  --repository pantheon-mvp=implementation=/path/to/pantheon-mvp \
  --repository Pantheon-Next=governance=/path/to/Pantheon-Next \
  --authority-registry /path/to/Pantheon-Next/docs/governance/authority/PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json \
  --output docs/architecture/PANTHEON_ARCHITECTURE_INVENTORY.md
```

JSON output is available for later review tooling:

```bash
python tools/audit_pantheon_architecture.py \
  --repository pantheon-mvp=implementation=/path/to/pantheon-mvp \
  --repository Pantheon-Next=governance=/path/to/Pantheon-Next \
  --authority-registry /path/to/Pantheon-Next/docs/governance/authority/PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json \
  --format json
```

The audit performs no rewrite, move, deletion, approval or runtime action.
