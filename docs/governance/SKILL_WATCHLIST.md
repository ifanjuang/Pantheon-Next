# Skill Watchlist

Status: active support doctrine — watchlist only.

This document defines how Pantheon Next may monitor external `SKILL.md` ecosystems without installing, approving or adopting skills automatically.

It does not add dependencies.

It does not define a skill marketplace.

It does not approve external skills.

It does not define a runtime, installer, scheduler, queue, MCP layer, plugin manager, automatic skill loader, automatic memory system or self-update mechanism.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

External skill marketplaces and repositories can reveal useful operational patterns.

Pantheon Next should be able to watch those patterns without copying them.

A watched skill is not a Pantheon Skill.

A popular skill is not approved.

A paid skill is not more legitimate.

A downloaded skill is not evidence.

A `SKILL.md` file is not doctrine.

The watchlist exists to decide whether a pattern deserves distillation into governance vocabulary.

## Core rule

```text
Watch skill ecosystems.
Distill patterns.
Do not install by default.
Do not approve by popularity.
Do not promote skill outputs to memory.
```

## Watched source: Agensi skills marketplace

Source: `https://www.agensi.io/skills`

Observed status on 2026-05-17:

- marketplace for portable AI agent skills;
- skills presented as `SKILL.md` instruction sets;
- compatibility claims across multiple AI coding agents;
- browse by category;
- free and paid skill listings;
- sorting by trending, newest, most voted, best rated and most installed;
- skill cards with author, price, description, category tags, install counts or ratings when available;
- visible categories including frontend and design, testing and QA, DevOps and deployment, code review, documentation, productivity, data engineering and API development.

Pantheon interpretation:

```text
Agensi is a skill discovery and market signal source.
It is not a Pantheon dependency, authority or approval source.
```

Useful patterns to watch:

- skill naming conventions;
- skill description and trigger wording;
- category taxonomy;
- professional task coverage;
- evidence-oriented skills;
- audit and review skills;
- RAG and knowledge architecture skills;
- code review and migration audit skills;
- environment doctor and setup doctor skills;
- API contract and testing skills;
- prompt engineering and evaluation skills;
- documentation generation skills.

High-value examples to monitor as patterns, not products:

```text
code-reviewer
migration-auditor
designing-hybrid-context-layers
evaluating-ai-harness-dimensions
temporal-reasoning-sleuth
diagnosing-rag-failure-modes
rag-architect
research-to-decision-pro-skill
prompt-engineer
prompt-engineer-pro
env-doctor
api-contract-tester
benchmarking-ai-agents-beyond-models
context-switch-protector
```

High-risk examples to treat with caution:

```text
subagent-orchestrator
multi-agent-coordinator
deep-research-team
endless-loop
browser-automation skills
automated external-action skills
skills that imply working while the user sleeps
skills that send, publish, deploy, install or mutate systems
```

## Watchlist record format

A skill watch record should remain small and reviewable.

Recommended fields:

```text
source_platform
source_url
skill_name
author_or_publisher
observed_date
category
price_status
popularity_signal
capability_summary
pantheon_concern
allowed_distillation
runtime_surface_if_any
evidence_expectation
approval_implication
memory_implication
risk_class
forbidden_import
status
review_notes
```

Recommended statuses:

```text
watch
pattern_candidate
distill_into_doctrine
distill_into_hermes_candidate
reject_runtime_drift
reject_memory_drift
reject_external_effect_risk
archive
```

## Governance classification

### Watch

Use when a skill is interesting but not yet analyzed.

The skill remains an external signal only.

### Pattern candidate

Use when a skill suggests a useful pattern but needs review.

### Distill into doctrine

Use when the pattern improves Pantheon governance vocabulary, status discipline, evidence discipline, approval clarity or memory discipline.

### Distill into Hermes candidate

Use when the pattern is operational and could belong to Hermes or another external runtime under Task Contract.

### Reject runtime drift

Use when the skill would push Pantheon toward execution, scheduling, orchestration, installation, tool dispatch or autonomous runtime behavior.

### Reject memory drift

Use when the skill collapses retrieval, recall, user history, trace logs or repeated observations into memory without governed approval.

### Reject external effect risk

Use when the skill creates external writes, communication, deployment, scraping, browser automation, financial, legal, contractual or irreversible effects without strong approval framing.

## Scoring lens

A watched skill may be scored lightly across six axes.

```text
governance_value: 0-3
evidence_value: 0-3
professional_relevance: 0-3
runtime_drift_risk: 0-3
memory_drift_risk: 0-3
external_effect_risk: 0-3
```

Interpretation:

```text
high value + low risk → pattern candidate
high value + high risk → distill carefully or keep Hermes-only
low value + high risk → reject
```

Popularity, rating or install count must not override governance risk.

## Candidate Pantheon uses

A governed skill watchlist may support:

- future `SKILL_LIFECYCLE.md` reconciliation;
- Hermes Skill Candidate discovery;
- Setup Doctor checklist design;
- Evidence Pack completeness checklist design;
- RAG failure mode taxonomy;
- professional dossier mode expansion;
- code review and migration audit pattern discovery;
- prompt and evaluation discipline;
- skill sprawl detection.

## Forbidden uses

The watchlist must not become:

- skill marketplace;
- plugin manager;
- automatic installer;
- dependency registry;
- runtime capability registry;
- ranking system that implies approval;
- revenue or marketplace endorsement;
- external skill mirror;
- automatic skill update channel;
- automatic memory system;
- self-evolution mechanism.

## Relationship to Shokunin

Shokunin is useful for studying skill anatomy, lifecycle and evaluation loops.

Agensi is useful for market and ecosystem watch.

Pantheon should combine them only at the governance level:

```text
Agensi shows what skills exist.
Shokunin shows how skill ecosystems can be structured.
Pantheon decides what can be distilled, rejected or kept external.
```

## Relationship to Hermes

A watched skill may become a Hermes Skill Candidate only after separate review.

A Hermes Skill Candidate must still define:

- Task Contract fit;
- allowed inputs;
- allowed outputs;
- forbidden outputs;
- tool risk class;
- evidence expectations;
- approval implications;
- memory behavior;
- source requirements;
- rollback or mitigation when relevant.

Hermes execution remains external.

Pantheon does not install or execute watched skills.

## Relationship to OpenWebUI

OpenWebUI may later expose a read-only skill watch dashboard or list.

Such a surface would be display only.

Displaying a skill does not approve it.

Selecting a skill does not authorize execution.

Approving a skill pattern requires governed review.

## Final rule

```text
A watched skill is a signal.
A distilled pattern is a proposal.
A Hermes skill is an external execution capability.
A Pantheon Skill is a governed capability contract.
None of these become canonical by popularity.
```

## Status

Watchlist doctrine only.

No skill imported.

No skill purchased.

No skill installed.

No Hermes tool added.

No OpenWebUI surface added.

No scheduler added.

No marketplace added.

No schema added.

No tests added.
