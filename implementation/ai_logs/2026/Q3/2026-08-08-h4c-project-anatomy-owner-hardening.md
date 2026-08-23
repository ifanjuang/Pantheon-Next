# H4c Project Anatomy owner hardening

Date: 2026-08-08
Repository: ifanjuang/pantheon-mvp
PR: #267

## Scope

Final pre-merge hardening of the executable Project Anatomy V0.2 owner migration.

## Changes

- preserve legacy V0.1 object integrity after relaxing historical `NOT NULL` columns by requiring `object_kind` and `proof_status` whenever the legacy `stable_object` payload is present;
- require `object_family` and `canonical_payload_digest` whenever the V0.2 `canonical_stable_object` payload is present;
- keep the exact V0.2 validation-contract authority pin in `model_authority_ref`;
- add a distinct `model_doctrine_ref` pinned to the stable active `PROJECT_ANATOMY_MODEL.md` identity;
- keep V0.1 project-state authority refs null until reviewed migration to V0.2;
- add PostgreSQL negative tests for partial legacy/canonical rows and authority-provenance tests for both migrated and directly reviewed V0.2 owners.

## Authority boundaries preserved

```text
contract schema provenance != conceptual doctrine provenance
legacy payload readable != legacy payload partially valid
source representation stored != project truth
claim stored != Evidence admitted
runtime success != governance approval
```

No adapter execution, Revit runtime, Evidence admission, automatic canonization, approval, scheduler or provider-routing responsibility is introduced.
