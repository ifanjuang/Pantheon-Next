# Registry foundation

Date: 2026-08-03

Status: implemented validation candidate — non-runtime, no business registry migrated into Pantheon-Next.

## Observed need

Pantheon-Next needs a common descriptor contract for machine-readable registries shared across Pantheon-Next, pantheon-mvp, Hermes and Cockpit consumers.

The cross-repository audit confirmed that the ecosystem is not starting from zero. `pantheon-mvp` already contains active implementation registries for tags, navigation, status presentation and visual materials.

## Existing owners checked

- `docs/governance/EVOLUTION_OF_ROLES_RITES_AND_SPACES.md`;
- `docs/governance/CAPABILITY_PLACEMENT.md`;
- `docs/governance/CARD_STACK_MODEL.md`;
- `schemas/README.md`;
- `.github/scripts/check_register_instances.py`;
- `pantheon-mvp/mvp_vertical/cockpit/registries/tag_registry.json`;
- `pantheon-mvp/mvp_vertical/cockpit/registries/navigation_registry.json`;
- `pantheon-mvp/mvp_vertical/cockpit/registries/status_registry.json`;
- `pantheon-mvp/mvp_vertical/cockpit/registries/materials.json`.

The existing Register Candidate / Registre Probatoire schemas concern governed evidence and cascade review. They are not reused as configuration registries.

## Change

Add a generic validation-only descriptor foundation:

```text
registries/README.md
registries/registry_index.json
schemas/registry.schema.yaml
schemas/examples/registry.example.json
.github/scripts/check_registry_foundation.py
tests/test_registry_foundation.py
```

The Pantheon-Next index intentionally contains no migrated business instance. The generic schema governs common descriptor metadata; specialized schemas will govern domain-specific shapes.

## Cross-repository conclusion

```text
Pantheon-Next
-> canonical schemas and boundaries

pantheon-mvp
-> operational registry instances and projections

Hermes / Cockpit
-> bounded consumers
```

The existing MVP Tag Registry is the first official reconciliation candidate because it already has multiple real consumers. The status registry is not promoted: it remains a presentation vocabulary pending an audit of independent status axes.

## Boundaries

```text
registry != Registre Probatoire
registry descriptor != specialized schema
registry entry != complete doctrine
schema-valid != approved
indexed != activated
consumed != task-authorized
status label registry != canonical lifecycle
```

No runtime, API, provider router, scheduler, queue, approval engine, Evidence promotion or memory promotion is introduced.

## Next admissible step

Define a specialized Tag Registry schema in Pantheon-Next, validate the existing MVP instance through a vendored reference and add drift detection. Do not move runtime ownership or silently rename stable tag identities.
