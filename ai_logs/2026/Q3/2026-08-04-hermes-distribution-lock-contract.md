# Hermes distribution lock contract

Date: 2026-08-04

Status: candidate declarative template change; no installation, activation, runtime execution or task authorization.

## Verified context

The current repositories already separate:

- the external Hermes run binding;
- the bounded Pantheon context bridge plugin;
- runtime observation;
- optional policy MCP consultation;
- optional dashboard observation;
- independently selected skills.

The missing surface was a reproducible composition record that could pin these independently owned components and require composed acceptance checks without turning them into one runtime or approval object.

## Change

Added:

```text
templates/hermes/distribution/distribution-lock.schema.yaml
templates/hermes/distribution/distribution-lock.example.yaml
templates/hermes/distribution/README.md
tests/test_hermes_distribution_contract.py
```

Updated the Hermes README and design owner map.

## Boundary

The distribution lock is a template and deployment composition record, not a governed Pantheon identity.

```text
composition pinned != components installed
components installed != binding activated
acceptance passed != task authorized
runtime success != accepted result
runtime output != Evidence
```

The schema fixes all authority effects to `false` and keeps every component independently reviewable and default-off.
