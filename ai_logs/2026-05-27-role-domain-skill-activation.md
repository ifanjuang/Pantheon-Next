# AI Log — Role, Domain and Skill Activation

Date: 2026-05-27

## Context

The user asked whether Pantheon Roles could be disabled and whether each session could begin with a short role report to Zeus so Zeus can compose a workflow from active roles.

The user then asked whether the same activation logic could apply to skills and business domains, with examples such as architecture and legal.

## Action

Created:

```text
docs/governance/ROLE_ACTIVATION.md
```

Updated:

```text
docs/governance/README.md
docs/governance/STATUS.md
docs/governance/ROADMAP.md
CHANGELOG.md
```

## Doctrine added

`ROLE_ACTIVATION.md` defines activation semantics for:

- Pantheon Roles;
- professional domain packs;
- Hermes skill candidates.

Core rule:

```text
Activate roles to reveal tensions.
Activate domains to constrain context.
Activate skills only as task-bound Hermes candidates.
Validate nothing by activation alone.
```

## Role activation

Roles may be active, standby, disabled by user, disabled by scope, not relevant, mandatory for risk, blocked or suspended.

A role can be inactive by default.

A risk can reactivate it.

Zeus may receive a compact Role Readiness Brief and compose the minimal safe workflow from active, standby and mandatory roles.

## Domain activation

Professional domain packs are governed configurations of vocabulary, source expectations, risk triggers, templates and review gates.

Architecture and legal were added as initial examples.

They are draft-only professional domains.

They do not create professional validation, legal advice authority, architectural advice authority, autonomous domain agents or automatic external transmission.

## Skill activation

Skill candidates may become eligible through domain activation, but they execute only if task-authorized through Hermes.

Skill activation does not mean installation, execution, approval, professional validation or memory promotion.

## Explicitly not implemented

This intervention did not implement:

- autonomous role agents;
- role runtime;
- hidden role debate runtime;
- skill runtime;
- professional-domain authority engine;
- architecture agent authority;
- legal agent authority;
- automatic domain activation;
- automatic role execution;
- automatic skill installation;
- skill marketplace;
- OpenWebUI UI implementation;
- Hermes skill implementation;
- schemas;
- tests;
- operations tooling.

## Risk notes

Main risk: role activation could be mistaken for autonomous role agents.

Mitigation: the document states that roles are governance viewpoints only.

Second risk: architecture or legal domain activation could be mistaken for professional validation.

Mitigation: both domains are explicitly draft-only until human professional review.

Third risk: skill-domain eligibility could be mistaken for skill installation.

Mitigation: skill candidates require Task Contract authorization and Hermes execution boundaries.

## Status impact

Pantheon Next now has support doctrine for future UI toggles covering roles, domain packs and skill candidates while preserving:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```