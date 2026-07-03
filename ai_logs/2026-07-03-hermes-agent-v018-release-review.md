# AI Log — Hermes Agent v0.18.0 release boundary review

Date: 2026-07-03

## Scope

Added a documentation-only external reference review for Hermes Agent v0.18.0:

```text
docs/governance/reference_reviews/HERMES_AGENT_V018_RELEASE_REVIEW.md
```

## Why

Hermes Agent v0.18.0 introduces several runtime surfaces that are relevant for Pantheon Next adapter review:

```text
MoA as first-class selectable model;
/goal completion contracts;
verification evidence for coding work;
/learn skill distillation;
/journey runtime memory timeline;
background delegate fan-out;
gateway lifecycle hardening;
desktop coding projects;
provider and security improvements.
```

The review classifies these as external runtime capabilities and adapter-review signals, not Pantheon doctrine or implementation evidence.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The review preserves these boundaries:

```text
Hermes runtime evidence may feed an Evidence Pack Candidate.
Hermes done does not mean Pantheon approved.
MoA is not the Governance College.
/learn creates Skill Candidates, not approved skills.
/journey exposes runtime memory, not Registre Probatoire entries.
Background fan-out does not change scope, approval or output status.
```

## Files changed

```text
created: docs/governance/reference_reviews/HERMES_AGENT_V018_RELEASE_REVIEW.md
created: ai_logs/2026-07-03-hermes-agent-v018-release-review.md
```

## Repo state

```text
external reference / support review
candidate only
documented non-implemented
```

No runtime, schema, test, operation, platform component, Docker file, `.env`, `CLAUDE.md`, `mcp-server/`, GitHub Action, Hermes profile, Hermes skill, OpenWebUI plugin, approval engine, memory engine, provider router, scheduler, queue or external action was created.

## Risks and limitations

The source reviewed is the upstream release note. The review does not independently verify that the upstream implementation works locally.

Open PR #266 already discusses tripartite interfaces and MCP refusal posture. This review does not modify or supersede that PR. It can later be reconciled with `HERMES_INTEGRATION.md`, `CARD_STACK_MODEL.md`, capability passports and the tripartite interface grammar if maintainers decide to promote any adapter mapping.

## Pending

```text
To verify: local Hermes v0.18 availability and output shapes.
To arbitrate: whether HERMES_INTEGRATION.md receives a formal v0.18 runtime-surface table.
To arbitrate: whether CARD_STACK_MODEL.md receives the proposed Goal Contract / Verification Evidence / MoA Divergence / Learned Skill Candidate cards.
```
