# P0.7 Hermes Profiles: IRIS and HEPHAISTOS

Date: 2026-05-12

## Objective

Complete Hermes profile coverage required by `docs/governance/AGENTS.md` by adding the IRIS and HEPHAISTOS profile templates, following the lightweight three-file structure already used by ATHENA, ARGOS, THEMIS, APOLLO and ZEUS.

## Files created

- `hermes/profiles/iris/README.md`
- `hermes/profiles/iris/profile.yaml`
- `hermes/profiles/iris/soul.md`
- `hermes/profiles/hephaistos/README.md`
- `hermes/profiles/hephaistos/profile.yaml`
- `hermes/profiles/hephaistos/soul.md`

## Profiles are templates only

Every file added in this pass is a **template**.

No Hermes profile is installed.

No Hermes runtime is activated.

No `SOUL.md` is deployed to a Hermes home directory.

No installation script is created.

No execution endpoint, scheduler, queue, provider router, message bus or LangGraph runtime is introduced.

The templates only declare:

- the canonical Pantheon Role they align with (`pantheon_role_id`);
- the canonical role source file (`pantheon_role_doc: docs/governance/AGENTS.md`);
- the profile identifier (`hermes_profile_id`);
- the soul template path (`soul_template`);
- candidate-only execution boundaries.

## Profile constraints respected

For both profiles:

- `profile_can_govern: false`
- `candidate_only: true`
- `evidence_required: true`
- `pantheon_role_doc: docs/governance/AGENTS.md`
- canonical forbidden outputs: `approval_final`, `memory_promotion`, `doctrine_change`, `direct_merge`, `external_send`, `source_of_truth_mutation`

### IRIS

- Scope: formulation, transmission, clarification, interface language, user-facing synthesis.
- IRIS does not decide, does not govern, does not validate, does not canonize.
- Additional forbidden output: `substantive_decision_change`.
- Default approval ceiling: `C1` (formulation level, no substantive decision).

### HEPHAISTOS

- Scope: build, patch and implementation candidates under Task Contract.
- HEPHAISTOS does not merge, does not validate, does not canonize, does not modify governance.
- Additional forbidden outputs: `self_approval`, `governance_mutation`.
- Default approval ceiling: `C3` (technical changes require review).
- Canonical spelling enforced: `HEPHAISTOS`, `hephaistos-agent`, `hermes/profiles/hephaistos/`.
- Non canonical spelling `HEPHAESTUS` is mentioned only as a non-canonical warning.

## Out of scope for this pass

- modifications to `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, root `README.md`, `docs/governance/README.md`;
- modifications to any governance document;
- modifications to existing Hermes profiles (ATHENA, ARGOS, THEMIS, APOLLO, ZEUS);
- creation of `governance.md` per profile;
- creation of `capabilities.yaml`, `outputs.yaml`, `kanban.yaml`;
- creation of `hermes/capabilities/`, `hermes/policies/`;
- creation of Hermes installation scripts;
- creation of `SOUL.md` deployed to a Hermes home directory;
- changes to `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml`;
- migration of real Pantheon-OS content;
- introduction of any execution runtime, scheduler, queue, provider router or workflow engine.

## Anti-runtime reminder

Pantheon Next governs.

Hermes Agent executes.

OpenWebUI exposes.

This pass adds template files only. It does not activate Hermes execution, does not install profiles and does not introduce any runtime component into Pantheon Next.

## STATUS update reminder

`docs/governance/STATUS.md` should be updated by the doctrine owner (ChatGPT) after verification of this PR:

- move `iris-agent` and `hephaistos-agent` from `Hermes profiles not implemented yet` into the `Hermes profile templates` block;
- update `Next required action` to point at controlled migration from Pantheon-OS (schemas, operations tooling and tests still absent).
