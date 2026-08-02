# Tag Registry specialized schema

Date: 2026-08-03

Status: implemented validation candidate — no runtime instance moved.

## Existing implementation

`pantheon-mvp/mvp_vertical/cockpit/registries/tag_registry.json` already serves the server/Cockpit, demo fixtures and bounded Hermes context. This slice does not copy or replace that operational instance.

## Change

Pantheon-Next adds:

```text
schemas/tag_registry.schema.yaml
schemas/examples/tag_registry.example.yaml
tests/test_tag_registry_schema.py
```

The specialized contract preserves the current implementation vocabulary:

- `schema_id` and numeric `revision`;
- groups `type` and `subject`;
- stable tag `slug` values;
- descriptions and bounded Hermes context;
- aliases and applicable projection surfaces;
- icon provider, icon key and color presentation;
- maximum five visible subjects per card.

## Boundaries

```text
tag description != source truth
tag presence != Evidence
tag context != scope expansion
tag context != task authorization
presentation metadata != semantic authority
schema valid != registry adopted
```

No API, loader, runtime, Hermes binding, Cockpit behavior, approval or Evidence promotion changes in this repository slice.

## Next slice

Vendor the schema reference into `pantheon-mvp`, validate the existing operational tag registry against it, and add deterministic drift detection. The instance remains in the implementation repository unless a later ownership decision explicitly moves it.
