# AI Log — Architecture Proof Register Implementation Spec

Date: 2026-05-31

## Intervention

Added a compact implementation candidate specification for the architecture proof register and indexed document version model.

Files touched:

```text
docs/governance/ARCHITECTURE_PROOF_REGISTER_IMPLEMENTATION_SPEC.md
ai_logs/2026-05-31-architecture-proof-register-implementation-spec.md
```

## Status

```text
documented: yes
implemented: no
partial: yes — implementation candidate spec only
```

No SQL schema, migration, Postgres table, RLS policy, Directus collection, object storage layout, OpenWebUI form, Hermes skill, queue runtime, scheduler, approval engine, memory engine or connector was implemented.

## Scope

The candidate implementation slice is:

```text
document family
-> indexed document version
-> version event
-> phase attachment
-> effect class
-> proof entry
-> review trigger
```

## Boundary maintained

The spec defines conceptual entities and validation rules only.

It does not authorize changes in `schemas/`.

It preserves the rule:

```text
Store every index.
Govern the effect.
Never let the latest filename decide authority.
```

## Tool note

The first, longer create-file attempt was blocked by connector safety checks. A compact version was created successfully.

## Notes

Index files were not edited.
