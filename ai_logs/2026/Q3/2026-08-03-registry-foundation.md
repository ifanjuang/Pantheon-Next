# Registry foundation

Date: 2026-08-03

Status: implemented validation candidate — non-runtime, no business registry migrated.

## Observed need

Pantheon-Next increasingly relies on schema-driven configuration, but no common technical contract exists for machine-readable registries shared by Pantheon, pantheon-mvp, Hermes or Cockpit consumers.

## Existing owners checked

- `docs/governance/EVOLUTION_OF_ROLES_RITES_AND_SPACES.md`;
- `docs/governance/CAPABILITY_PLACEMENT.md`;
- `docs/governance/CARD_STACK_MODEL.md`;
- `schemas/README.md`;
- `.github/scripts/check_register_instances.py`.

The existing Register Candidate / Registre Probatoire schemas concern governed evidence and cascade review. They are not reused as configuration registries.

## Change

Add a generic validation-only foundation:

```text
registries/README.md
registries/registry_index.json
schemas/registry.schema.yaml
.github/scripts/check_registry_foundation.py
tests/test_registry_foundation.py
```

The index intentionally contains no business registry.

## Boundaries

```text
registry != Registre Probatoire
registry entry != complete doctrine
schema-valid != approved
indexed != activated
consumed != task-authorized
```

No runtime, API, provider router, scheduler, queue, approval engine, Evidence promotion or memory promotion is introduced.

## Next admissible step

Select one pilot registry only after two real consumers and an explicit semantic owner are identified. Capability Slots, statuses, tags, subjects and Cockpit field definitions are candidates for later review; Roles, Rites and governed Spaces are not migrated by this change.
