# AI Log — Repository Review Watcher workflow candidate

Date: 2026-06-06  
Status: documentation intervention  
Repo state: documented non-implemented

## Context

The user asked to identify which Hermes Agent automation patterns are useful for Pantheon Next.

The useful pattern retained was not autonomous background execution. It was a governed repository-review watcher: a way to notice repository movement, classify it, attach evidence and route consequential status decisions back to governance.

## Sources reviewed

Repository documents reviewed before the change:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/MODULES.md`
- `docs/governance/HERMES_INTEGRATION.md`
- `docs/governance/TASK_CONTRACTS.md`
- `docs/governance/WORKFLOW_LIFECYCLE.md`
- `docs/governance/SKILL_WATCHLIST.md`
- `docs/governance/EXTERNAL_AGENTIC_INSPIRATIONS.md`
- `ai_logs/README.md`

Related GitHub issues searched:

- `#48` — request-lifecycle orchestrator implementation spec. Relevant because it explicitly places orchestrator/runtime behavior outside Pantheon.
- `#29` — review queue / swipe review. Relevant for decision queues and candidate action discipline.
- `#12` — governed OpenWebUI Knowledge handoff to Hermes. Relevant for scoped handoff discipline.
- `#30` — data-platform boundary review. Relevant for keeping data/workflow surfaces non-runtime unless explicitly approved.

No existing issue or document was found for a dedicated repository review watcher.

## Changes made

Added:

- `docs/governance/REPOSITORY_REVIEW_WATCHER.md`

Updated:

- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/MODULES.md`
- `CHANGELOG.md`

Dashboard follow-up:

- A Notion governance card should track this as candidate / to verify with repo state documented non-implemented.

## Rationale

The Hermes patterns around goals, schedules, webhooks, Kanban and sub-agents are useful only if translated into Pantheon vocabulary:

```text
Task Contract in
-> external execution runtime
-> Result Candidate + Evidence Pack Candidate out
-> governance review
-> human decision
```

The new watcher document captures this as a Workflow Manifest candidate.

It lets a future external runtime notice and classify repository movement, but prevents repository movement from becoming governance truth.

## Boundary

This intervention is documentation only.

It does not implement:

- cron;
- webhook;
- scheduler;
- queue;
- worker;
- provider routing;
- dashboard automation;
- GitHub App;
- Notion automation;
- Hermes skill;
- OpenWebUI Action;
- schema;
- test;
- operations tooling;
- platform code;
- Docker configuration;
- environment configuration;
- automatic approval;
- automatic memory promotion;
- external action.

## Risks and limitations

The new document remains candidate / to verify.

Before any operational use, it still needs:

- shadow traces;
- explicit Task Contract examples;
- source-scope limits;
- disableability conditions;
- failure behavior;
- dashboard write boundaries;
- review against `WORKFLOW_LIFECYCLE.md` and `HERMES_INTEGRATION.md`;
- human arbitration on whether it stays candidate-only or becomes support doctrine.

## Status statement

```text
The watcher notices.
The evidence supports.
Zeus qualifies procedure.
The human decides.
The repository keeps doctrine.
```
