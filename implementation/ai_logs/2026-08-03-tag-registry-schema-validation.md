# Tag Registry schema validation

Date: 2026-08-03

Status: implementation candidate — dependent on Pantheon-Next #514.

## Change

- vendor `schemas/tag_registry.schema.yaml` from Pantheon-Next as a reference;
- retain provenance and a deterministic content digest;
- validate the existing operational `tag_registry.json` against the contract;
- verify unique group and tag identities;
- verify every tag references a declared group;
- preserve the maximum of five visible subjects per card.

The operational registry remains at:

```text
mvp_vertical/cockpit/registries/tag_registry.json
```

No consumer path, tag value, icon, Hermes context or projection behavior changes.

## Boundaries

```text
vendored schema != governance authority transfer
schema-valid registry != source truth
tag description != Evidence
tag context != scope expansion
tag context != task authorization
```

## Follow-up

After Pantheon-Next #514 is merged, refresh the provenance marker to the merged upstream commit if required. Navigation reconciliation remains a separate tranche.
