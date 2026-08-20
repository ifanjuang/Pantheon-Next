# Hermes Profiles

Hermes profiles are execution-profile templates aligned with Pantheon Roles.

Canonical role definitions remain in:

```text
docs/governance/AGENTS.md
```

Each profile folder contains only:

```text
README.md
profile.yaml
soul.md
```

Shared adapter notes may live at the root of `hermes/profiles/` when they coordinate profile use without creating executable configuration.

No profile folder is a canonical governance source.
No profile folder is automatically installed into Hermes.
No profile may approve, canonize, promote memory, mutate doctrine or merge code.

## Role coverage is not profile cardinality

Pantheon currently has eight canonical governance Roles, including `MNEMOSYNE`.

This directory still contains seven role-aligned execution-profile candidates. That is deliberate.

```text
canonical Pantheon Role
!= required Hermes profile
```

`MNEMOSYNE` governs memory continuity, memory-oriented retrieval framing, version/current-state review and retention-placement proposals. Those judgments do not require a dedicated Hermes runtime identity.

When actual retrieval is required, an admitted external executor may perform it under Task Contract. Creating a `mnemosyne-agent` folder merely to mirror the governance registry would add a parallel runtime identity without a demonstrated execution responsibility, so this repository does not do so.

## Functional profiles and runtime modes

The folders in this directory describe functional execution profiles such as document intake, evidence review or repository maintenance.

They do not select the runtime memory, retrieval or OpenWebUI enrichment posture by themselves.

Every functional profile that receives a Pantheon Task Contract must inherit the `pantheon-governed` runtime mode defined in `PROFILE_CONSTITUTION.md`.

```text
functional profile
+ pantheon-governed runtime mode
+ admitted Task Contract
+ explicit tool allowlist
= candidate execution posture
```

`pantheon-governed` is a runtime mode, not a Pantheon Role and not automatically an additional functional profile folder.

The governed mode requires all Hermes memory inputs to be inert for the admitted run:

```text
external provider: off
built-in MEMORY.md injection: off
built-in USER.md profile injection: off
memory tool: off
X-Hermes-Session-Key: not sent
```

`hermes memory off` establishes only the first line. It does not prove the built-in injection or tool states.

`assistant-personal` is a separate non-governed runtime mode. It may use one optional external memory provider and user-selected built-in memory behavior, but it must not receive Pantheon Task Contracts, professional task authorization or canonical memory authority.

```text
functional profile selected != runtime mode observed
runtime mode configured != task authorized
profile route reachable != profile safe
hermes memory off != built-in memory injection off
external provider absent from tool list != external memory proven off
memory tool absent != memory injection disabled
```

If the active runtime mode or complete memory posture cannot be observed, the profile remains `not_qualified` for governed execution and must emit a Capability Gap.

## Adapter constitution

`PROFILE_CONSTITUTION.md` records a candidate profile-routing constitution for Hermes execution profiles.

It is an adapter note only.

It does not create profiles, configure Hermes, route gateways, create Kanban boards, authorize execution, approve outputs or promote memory.

## Read order

Before using or reviewing a profile, read:

1. `docs/governance/AGENTS.md`
2. `docs/governance/HERMES_INTEGRATION.md`
3. `hermes/profiles/PROFILE_CONSTITUTION.md`
4. `hermes/profiles/_base/README.md`
5. `hermes/profiles/_base/base-soul-rules.md`
6. `hermes/profiles/<profile>/README.md`
7. `hermes/profiles/<profile>/profile.yaml`
8. `hermes/profiles/<profile>/soul.md`
