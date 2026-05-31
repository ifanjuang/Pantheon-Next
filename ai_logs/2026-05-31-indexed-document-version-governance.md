# AI Log — Indexed Document Version Governance

Date: 2026-05-31

## Intervention

Updated the architecture proof register to include indexed document version governance.

Files touched:

```text
docs/governance/ARCHITECTURE_PROOF_REGISTER.md
ai_logs/2026-05-31-indexed-document-version-governance.md
```

## User input integrated

The user clarified that architecture pieces evolve through indices / versions. Some indices are key, such as the signature of a contract or market, while others are ordinary modifications. Each index must be stored and attached to a phase.

## Status

```text
documented: yes
implemented: no
partial: yes — candidate support doctrine only
```

No SQL schema, migration, table, storage backend, Directus cockpit, OpenWebUI UI, Hermes skill, approval engine, graph runtime or queue implementation was created.

## Added concepts

```text
document family
indexed version
phase attachment
revision reason
index effect class
key index versus ordinary revision
supersession without deletion
version event shape
```

## Boundary maintained

Every index is stored.

Only a governed key index can change phase status, contractual status, approval status or external-action authority.

Ordinary revisions may be useful evidence, but they do not automatically create gate effects.

## Notes

The conceptual shapes added are not approved database schemas.

Index files were not edited.
