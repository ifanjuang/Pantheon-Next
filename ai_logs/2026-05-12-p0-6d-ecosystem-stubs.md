# P0.6D Ecosystem Read-Order Stubs

Date: 2026-05-12

## Objective

Close the remaining ecosystem references listed by `docs/governance/README.md` (section `Referenced ecosystem documents not created yet`) by adding governance stub files for each. No real doctrine is migrated.

This pass runs in parallel with `chore/p0-6c-governance-safety-stubs` (ChatGPT side) and does not touch any file owned by P0.6C.

## Files created

- `docs/governance/REQUEST_ORCHESTRATION.md`
- `docs/governance/ROLE_SIGNAL_PROFILES.md`
- `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`
- `docs/governance/OPENWEBUI_PLUGIN_POLICY.md`
- `docs/governance/EPISTEMIC_CONTROL.md`
- `docs/governance/EPISTEMIC_CONTROL_PROPAGATION.md`
- `docs/governance/EXTERNAL_RUNTIME_OPTIONS.md`

Each file carries the exact stub header:

```text
Status: stub — Non implémenté — à migrer depuis Pantheon-OS
```

## Why these are stubs

Every file is a migration placeholder.

A stub:

- preserves the canonical filename so that ecosystem references in the governance index do not break;
- prevents accidental promotion of placeholder text to canonical status;
- must be replaced by migrated content under controlled review before it counts as doctrine.

The stubs declare `Intended scope after migration` only. They do not encode policy, contracts, approvals, schemas, endpoints, versions or commands.

## These stubs are not migrated doctrine

None of these files represents canonical Pantheon Next governance.

Readers must check `docs/governance/STATUS.md` before treating any of these files as implemented doctrine.

## Anti-runtime reminder

No runtime, scheduler, queue, message bus, provider router, installer, endpoint, Docker stack, schema, test, operations tooling, platform API or pyproject change is introduced by this pass.

No version-dependent Hermes or OpenWebUI content is introduced.

Each stub repeats an explicit anti-runtime reminder so that future readers cannot confuse the governance scope with an execution scope.

## Parallel coordination with P0.6C

P0.6C (`chore/p0-6c-governance-safety-stubs`) is creating the governance safety stubs:

- `TASK_CONTRACT_REVISIONS.md`;
- `RUN_GRAPH.md`;
- `EXECUTION_DISCIPLINE.md`;
- `MODEL_ROUTING_POLICY.md`;
- `ROUTING_FOUNDATION.md`.

P0.6D (this pass) does not touch any of those files.

After both passes are merged, every governance document referenced by the canonical read order and the index becomes either implemented, stub-present or explicitly deferred.

## STATUS update reminder

`docs/governance/STATUS.md` must be updated by the doctrine owner (ChatGPT) after verification of this PR and after the P0.6C merge:

- move the seven ecosystem files above out of `Referenced ecosystem documents not created yet`;
- list them under `Stub present — non implemented`;
- keep schemas, tests, read-only tooling and any other absent assets under their respective absent sections.

## Out of scope for this pass

- migration of real content from Pantheon-OS;
- any file already owned by P0.6C;
- modifications to `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, root `README.md`, `docs/governance/README.md`;
- modifications to existing Hermes profiles;
- creation of IRIS or HEPHAISTOS profile content (already delivered);
- `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml`.

## Next required action

Doctrine owner verifies the seven ecosystem stubs, lets P0.6C complete, then updates `docs/governance/STATUS.md` and `docs/governance/README.md` to reflect the new stub-present status. After that, controlled migration from Pantheon-OS may begin.
