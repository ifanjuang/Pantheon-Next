# P0.6 Read Order Governance Stubs

Date: 2026-05-12

## Objective

Close the remaining gaps in the canonical read order defined by `CLAUDE.md` and indexed by `docs/governance/README.md` by adding the missing governance stub files. No real doctrine is migrated in this pass.

## Files created

- `docs/governance/MODULES.md`
- `docs/governance/HERMES_INTEGRATION.md`
- `docs/governance/OPENWEBUI_INTEGRATION.md`
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`
- `docs/governance/KNOWLEDGE_TAXONOMY.md`
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`
- `docs/assets/README.md`

Each file carries the exact stub header:

```text
Status: stub — Non implémenté — à migrer depuis Pantheon-OS
```

## Why these are stubs

Every file is a migration placeholder.

A stub:

- preserves the canonical filename so that references and the canonical read order do not break;
- prevents accidental promotion of placeholder text to canonical status;
- must be replaced by migrated content under controlled review before it counts as doctrine.

The stubs describe `Intended scope after migration` only. They do not encode policy, contracts, approvals, schemas, endpoints, versions or commands.

## These stubs are not migrated doctrine

None of these files represents canonical Pantheon Next governance.

Readers must check `docs/governance/STATUS.md` before treating any of these files as implemented doctrine.

## Anti-runtime reminder

No runtime, scheduler, queue, provider router, installer, endpoint, Docker stack, schema, test, operations tooling, platform API or pyproject change is introduced by this pass.

No version-dependent Hermes or OpenWebUI content is introduced.

No IRIS or HEPHAISTOS profile is created in this pass.

## STATUS update reminder

`docs/governance/STATUS.md` must be updated by the doctrine owner (ChatGPT) after verification of this PR.

Expected STATUS update:

- move the seven files above out of the `Absent` section;
- add them under the `Stub present — non implemented` section;
- keep `IRIS` and `HEPHAISTOS` profiles, schemas, tests and read-only tooling under the `Absent` section.

## Out of scope for this pass

- migration of real content from Pantheon-OS;
- IRIS Hermes profile;
- HEPHAISTOS Hermes profile;
- schemas;
- operations tooling;
- tests;
- modifications to `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, root `README.md` or `docs/governance/README.md`;
- modifications to `pyproject.toml`, `.env`, Docker, `platform/api`.

## Next required action

Doctrine owner verifies the seven stubs, then updates `docs/governance/STATUS.md` to reflect their new `Stub present — non implemented` status. P0.6 then proceeds with IRIS and HEPHAISTOS Hermes profiles.
