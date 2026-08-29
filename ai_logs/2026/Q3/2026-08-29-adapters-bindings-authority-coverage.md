# Adapters and Bindings — authority coverage repair — 2026-08-29

## Objective

Continue #787 from exact `main` `68ca8e40be31c4d9e510fc51d49ec0c89b232cb0` by repairing authority-index coverage for `docs/governance/ADAPTERS_AND_BINDINGS.md` without changing its doctrine.

## Observed need

`ADAPTERS_AND_BINDINGS.md` declares active support doctrine and is consumed by `README.md`, `MODULES.md`, `MODULAR_DOMAIN_REORIENTATION.md` and related placement material, but no row existed in either current authority sub-index.

`MODULES.md` places this owner in the `External tools/connectors` governance area, so the correct placement is `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`.

## Overlap analysis

The owner remains distinct:

```text
HERMES_INTEGRATION.md
  -> stable Pantheon / Hermes / PDP / PEP / client / Cockpit boundary

BRIDGE_CONTRACT.md
  -> non-authoritative translation-adapter seam

ADAPTERS_AND_BINDINGS.md
  -> blueprint-in-Pantheon / runnable-adapter-outside placement and dependency direction
```

No absorption or doctrinal rewrite is justified.

## Changes

Exactly one authority-map row is added for `ADAPTERS_AND_BINDINGS.md`:

- authority class: active support doctrine;
- repo state: implemented as documentation;
- responsibility: non-executable Pantheon blueprints/contracts versus external runnable tool-specific configuration;
- adapter selection/conformance does not transfer runtime or governance authority.

## Affected consumers

No consumer content changes. Existing references continue to point at the same owner.

## Migration and rollback

No migration is required. Rollback is the removal of the single index row if repository evidence later shows the owner is absorbed or reclassified.

## Authority impact

No authority promotion. This repairs coverage of an already-active owner in the existing Runtime Adapters sub-index.

## Runtime impact

None. No adapter, binding, runtime, client, connector, bridge, skill, provider or executable configuration is created or activated.

## Preserved invariants

```text
blueprint != runnable adapter
adapter conformance != authorization
client/provider selected != authority transfer
runtime success != authorization
projection != persistence
PDP decision != PEP execution
```

## Verification rule

Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final HEAD and reviews/threads/comments have been read. Any later HEAD modification invalidates earlier check evidence.
