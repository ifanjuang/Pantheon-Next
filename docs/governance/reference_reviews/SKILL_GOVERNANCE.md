# Skill Governance Reference Review (EviBound, SkillsVote, GovernSpec, MedSkillAudit)

Status: external reference — convergent vocabulary to distill.

Date: 2026-06-03

A 2026 wave of work governs *the composition and lifecycle of agent skills*: when
a skill may run, how it is reviewed, how it is promoted, how its claims are proven.
This converges closely with Pantheon's own posture, so it is worth distilling — not
importing.

These are external references.

They do not govern Pantheon. They do not authorize a runtime, an approval engine,
automatic memory promotion or autonomous skill promotion inside Pantheon.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## The references

- **EviBound — Evidence-Bound Autonomous Research**
  (`https://arxiv.org/pdf/2511.05524`) — a pre-execution approval gate validates
  acceptance criteria before code runs, and a post-execution verification gate
  validates artifacts, to eliminate false claims.
- **SkillsVote — Lifecycle Governance of Agent Skills**
  (`https://arxiv.org/abs/2605.18401`) — governs the skill lifecycle from
  collection through recommendation to evolution.
- **Contractual Skills / GovernSpec**
  (`https://arxiv.org/html/2605.22634`) — skills placed under explicit contract for
  enterprise agents.
- **MedSkillAudit** (`https://arxiv.org/html/2604.20441`) — a domain-specific audit
  of a skill's release readiness before deployment.

## Why this matters

Earlier review assumed governing composition was an empty niche. It is not: this
work converges on the same gates Pantheon already states. The value is convergent
vocabulary that confirms and sharpens existing doctrine, not new architecture to
import.

## Accepted distillation

Pantheon may use these as vocabulary sources for:

- pre-execution eligibility and post-execution evidence as two gates
  (`WORKFLOW_SCHEMA.md`, governed composition);
- the rule that an unsupported claim does not become truth (`EVIDENCE_PACK.md`);
- a skill lifecycle of candidate, reviewed, promoted, superseded
  (`CAPABILITY_REGISTRY.md`);
- a contract framing per capability (Task Contract, `TASK_CONTRACTS.md`);
- domain-scoped readiness review before a capability is trusted in a domain.

This is support vocabulary only.

It does not create a runtime, an approval engine, an audit engine, a schema, a
memory engine or an automatic promotion mechanism.

## Rejected import

Pantheon must not import these as:

- an autonomous approval engine that approves on its own;
- an automatic skill promotion or skill evolution loop;
- a runtime that executes gates;
- a memory promotion mechanism;
- a source-of-truth system;
- a substitute for the human decision at the cliffs.

These systems propose useful gate vocabulary. The gate decision in Pantheon
remains a governance act (ZEUS arbitrates, the human engages), never an automatic
mechanism.

## What stays distinctly Pantheon

None of these references carries the part Pantheon treats as central: the
re-evaluable professional cap (MÈTIS, `REQUEST_LIFECYCLE.md`) and the
responsibility limit of the liberal profession. They govern skills to act
reliably; Pantheon governs work to be *right and revisable*. That is the part not
to outsource.

## Boundary phrase

```text
EviBound, SkillsVote, GovernSpec and MedSkillAudit confirm the gates.
They are distilled as vocabulary, not imported as engines.
The gate is a governance decision, not an automatic mechanism.
The cap and the responsibility limit remain Pantheon's own.
The human decides.
```
