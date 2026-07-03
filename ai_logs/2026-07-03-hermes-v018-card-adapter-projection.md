# AI Log — Hermes v0.18 card and adapter projection

Date: 2026-07-03

## Scope

Added a documentation-only projection candidate:

```text
docs/governance/reference_reviews/HERMES_AGENT_V018_CARD_AND_ADAPTER_PROJECTION.md
```

This follows the previous release review:

```text
docs/governance/reference_reviews/HERMES_AGENT_V018_RELEASE_REVIEW.md
```

## Why

The Hermes Agent v0.18.0 release introduces runtime surfaces that may need future adapter and cockpit projection:

```text
/goal completion contracts;
verification evidence ledger;
MoA first-class provider;
/learn skill distillation;
/journey runtime memory visibility;
delegate_task fan-out;
gateway health / lifecycle signals;
provider and security capability signals.
```

Rather than modifying `HERMES_INTEGRATION.md` directly, the projection keeps the mapping candidate-only under `reference_reviews/`, which is already covered by `AUTHORITY_INDEX.md` as external reference / support review.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The projection preserves these boundaries:

```text
runtime done != Pantheon approved;
runtime evidence != self-approving proof;
runtime memory != Registre Probatoire;
learned skill != admitted competence;
MoA aggregator != Zeus;
fan-out != scope expansion;
healthy runtime != approved capability.
```

## Files changed

```text
created: docs/governance/reference_reviews/HERMES_AGENT_V018_CARD_AND_ADAPTER_PROJECTION.md
created: ai_logs/2026-07-03-hermes-v018-card-adapter-projection.md
```

## Repo state

```text
external reference / support projection
candidate only
documented non-implemented
```

No runtime, UI, renderer, schema, test, operation, platform component, Docker file, `.env`, `CLAUDE.md`, `mcp-server/`, GitHub Action, Hermes profile, Hermes skill, OpenWebUI plugin, provider router, scheduler, queue, approval engine, memory engine or external action was created.

## Risks and limitations

This is a projection from upstream release notes and existing Pantheon doctrine. It is not based on local execution of Hermes v0.18.

It must not silently supersede:

```text
PR #266 — tripartite interfaces and MCP V0 refusal posture;
PR #265 — Forever Components card-affordance review;
HERMES_INTEGRATION.md;
CARD_STACK_MODEL.md.
```

## Pending

```text
To verify: local Hermes v0.18 outputs for /goal, /learn, /journey, MoA and delegate fan-out.
To arbitrate: whether stable parts should be distilled into HERMES_INTEGRATION.md and CARD_STACK_MODEL.md.
```
