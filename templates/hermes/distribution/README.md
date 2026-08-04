# Hermes Distribution Lock

Status: template-only composition contract — no installer, runtime or authority.

This directory defines how an operator or implementation repository may record one reproducible composition of Pantheon artifacts for an external Hermes installation.

```text
distribution-lock.schema.yaml   validation contract
distribution-lock.example.yaml  fictional example only
```

The lock records:

- exact `Pantheon-Next` and `pantheon-mvp` commit pins;
- the observed external Hermes runtime version;
- independently reviewable components;
- which components are required or optional;
- the abstract capabilities each component exposes;
- the acceptance checks required for the composition;
- factual installation and acceptance observations.

It does not merge the components into a new runtime or authority layer.

```text
composition pinned != components installed
components installed != binding activated
acceptance passed != task authorized
runtime success != accepted result
runtime output != Evidence
```

## Ownership

`Pantheon-Next` owns this declarative template contract. A candidate operational lock belongs with the implementation or deployment material that it describes, normally in `pantheon-mvp` or an external operator repository.

Each component retains its owner and lifecycle. A dashboard update does not require treating the run binding as changed, and a skill may remain absent even when the required execution bridge is installed.

## Validation

A consumer should validate the lock against the schema, resolve every declared path inside the exact pinned checkout, verify the route and plugin contracts, and run one composed read-only acceptance scenario.

A check result is a technical observation only. Human activation and per-task admission remain separate decisions.
