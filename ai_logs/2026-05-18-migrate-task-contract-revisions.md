# Migrate TASK_CONTRACT_REVISIONS.md

Date: 2026-05-18

## Scope

Migrated `docs/governance/TASK_CONTRACT_REVISIONS.md` from a stub into Pantheon Next Task Contract revision doctrine.

Updated related tracking documents:

- `docs/governance/STATUS.md`;
- `docs/governance/ROADMAP.md`;
- `docs/governance/README.md`;
- `ai_logs/migration-mapping.md`.

## Source reviewed

Source repository:

```text
ifanjuang/Pantheon-OS
```

Source file:

```text
docs/governance/TASK_CONTRACT_REVISIONS.md
```

Live OS commit used for focused distillation:

```text
fd0beba83528bd5c92244d76a5643646dfae2d87
```

## Transformation applied

The source contained useful doctrine around single-role tasks, revision signals, ZEUS arbitration, Task Contract revisions, resume policies, reset-to-baseline and Evidence Pack fragments.

The migration preserved those concepts while removing any implication that Pantheon Next executes workflows, resumes jobs, mutates runtime state or approves automatically.

Retained as doctrine:

- when revision is required;
- when revision is not required;
- single-role contract boundaries;
- escalation from single-role to workflow frame;
- revision signal semantics;
- Role Signal triggers;
- ZEUS procedural arbitration;
- revision record structure;
- resume policy vocabulary;
- reset-to-baseline rules;
- Evidence Pack requirements;
- Hermes and OpenWebUI boundaries.

Reframed or removed:

- YAML examples that looked like runtime objects;
- language implying automatic Hermes continuation;
- any suggestion that signals mutate contracts;
- any suggestion that ZEUS decides truth instead of procedure;
- any implication of automatic workflow resume or hidden orchestration.

## Result

`TASK_CONTRACT_REVISIONS.md` now defines Task Contract lifecycle doctrine:

```text
Task Contract frame
→ revision signal
→ procedural arbitration
→ visible revision record
→ approval impact
→ resume policy or stop condition
→ Evidence Pack fragment
```

It states explicitly that:

- Hermes may execute only inside an approved current frame;
- OpenWebUI may expose the decision;
- Pantheon governs status and procedure;
- the human decides at User Decision Gates.

## Reconciliation

`STATUS.md` now lists `TASK_CONTRACT_REVISIONS.md` under migrated Pantheon-OS doctrine and active governance documents.

`ROADMAP.md` now lists `TASK_CONTRACT_REVISIONS.md` as migrated from Pantheon-OS.

`docs/governance/README.md` now lists `TASK_CONTRACT_REVISIONS.md` under migrated documents and active governance documents, not under stubs.

`ai_logs/migration-mapping.md` now marks `TASK_CONTRACT_REVISIONS.md` as migrated.

## Doctrine boundary

No runtime was introduced.

No workflow execution was implemented.

No resume engine was implemented.

No scheduler, queue, message bus, provider router, endpoint, Doctor, test or schema behavior was introduced.

No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, environment or pyproject file was modified.

Pantheon Next remains governance.

Hermes Agent executes externally.

OpenWebUI exposes.

## Next recommended action

Continue one file at a time.

Recommended next candidates:

1. `EXECUTION_DISCIPLINE.md` to lock execution boundaries;
2. `ROLE_SIGNALS.md` because Task Contract revisions now refer to role-triggered signals;
3. schema reconciliation only after the governance target documents are stable.
