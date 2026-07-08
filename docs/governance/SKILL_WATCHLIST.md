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

## Watched source: awesome-claude-code

Source: `https://github.com/hesreallyhim/awesome-claude-code`

Observed status on 2026-07-08:

- public awesome-list style catalogue for the Claude Code ecosystem;
- aggregates commands, agents, hooks, MCP servers, skills, security tools, provider layers, sandboxes, memory/context persistence tools, observability, usage/cost monitoring, testing and linting resources;
- points to many third-party repositories rather than providing one reviewed runtime;
- mixes low-risk documentation resources with high-risk execution, hook, browser, MCP, memory, sandbox and automation surfaces;
- useful as a map of ecosystem pressure, not as a trust source.

Pantheon interpretation:

```text
awesome-claude-code is an ecosystem map and pattern discovery source.
It is not a Pantheon dependency, approval source, marketplace, installer queue, Hermes binding registry, MCP catalogue, plugin manager or trust registry.
```

Useful patterns to watch:

- classification of Claude Code surrounding capabilities;
- skill and command packaging conventions;
- hook-related approval and sandboxing pressure;
- MCP server and connector boundary patterns;
- observability, cost and runtime-status dashboard patterns;
- memory/context persistence anti-patterns;
- linting and safety-check vocabulary;
- sandbox and host-control separation;
- candidates for future Hermes-side capability binding review.

Candidate Pantheon distillation:

```text
awesome-list category -> watchlist domain, not approval category
third-party skill repo -> Skill Watchlist record, not adopted skill
hook / MCP / plugin -> privileged capability candidate requiring boundary review
observability tool -> Runtime Status Candidate only, not Evidence Pack
memory tool -> external runtime memory adapter candidate, not Registre Probatoire
security tool -> review signal, not proof of safety
```

Forbidden import:

- copying the catalogue as a Pantheon registry;
- treating inclusion in the list as trust, maturity, safety or approval;
- automatic installation of Claude Code skills, hooks, plugins, MCP servers or commands;
- treating hook execution as a governed workflow;
- treating MCP connection as external-action authorization;
- treating memory/context tools as Pantheon memory;
- treating observability or cost dashboards as proof, approval or professional validation;
- turning the list into a provider router, plugin marketplace, install queue or update channel.

Status:

```text
status: boundary_required
risk_class: T1/T2 for observation and distillation; T5 if installation, hooks, credentials, MCP exposure, browser automation, memory persistence, protected repository mutation or external writes are involved
primary_route: WATCHLIST.md -> SKILL_WATCHLIST.md -> HERMES_CAPABILITY_BINDINGS.md when a concrete binding candidate survives review
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

## Watched source: kombifyio/contracts-skill

Source: `https://github.com/kombifyio/contracts-skill`

Observed status on 2026-05-17:

- public repository for contract-guided AI-assisted development;
- uses a human-owned `CONTRACT.md` and an AI-maintained `CONTRACT.yaml`;
- emphasizes contract preflight before implementation;
- checks drift, constraints, verification tests, acceptance tests and attestation;
- uses stable traceability identifiers such as `F-001`, `REQ-001`, `AC-001`, `AT-001` and `VT-001`;
- writes files only after explicit user approval during initialization;
- treats locked `CONTRACT.md` files as read-only guardrails.

Pantheon interpretation:

```text
contracts-skill is a contract discipline and preflight inspiration source.
It is not a Pantheon dependency, installer, runtime skill or approval source.
```

Useful patterns to watch:

- human-owned specification separated from machine-maintained mapping;
- preflight before modification;
- drift check between intent and technical state;
- explicit acceptance and verification traces;
- attestation discipline;
- stable traceability IDs;
- refusal to claim implementation without real verification;
- read-only locking of approved intent.

Candidate Pantheon distillation:

```text
CONTRACT.md -> governed human intent or module contract inspiration
CONTRACT.yaml -> technical mapping inspiration, not source of truth
contract preflight -> Doctor or governance preflight inspiration
VT and AT -> verification and acceptance trace inspiration
attestation -> Evidence Pack or validation record inspiration
lock mode -> approval boundary inspiration
```

Forbidden import:

- automatic skill installation;
- automatic project hook mutation;
- dependency on the external repository;
- treating `CONTRACT.yaml` as a Registre Probatoire entry;
- treating contract lock scripts as Pantheon governance;
- declaring implementation from lifecycle status without Evidence Pack;
- bypassing Task Contracts, approvals or User Decision Gates.

## Watched source: Lum1104/Understand-Anything

Source: `https://github.com/Lum1104/Understand-Anything`

Observed status on 2026-05-29:

- external codebase, documentation and knowledge-base understanding tool;
- produces an interactive structural graph and generated graph artifact;
- supports a Hermes installation target in its external installer;
- combines deterministic structural extraction with LLM semantic interpretation;
- supports diff impact, onboarding, domain and knowledge-base analysis modes;
- positions generated graphs as shareable project artifacts.

Pantheon interpretation:

```text
Understand-Anything is a structural-intelligence skill candidate.
It is not a Pantheon dependency, installed skill, memory engine or graph authority.
```

Useful patterns to watch:

- repository radiography before mutation;
- deterministic versus semantic finding separation;
- diff impact as Evidence Pack support;
- onboarding guide as Output Candidate;
- generated graph references inside Evidence Pack Candidates;
- dashboard as review surface, not authority.

Candidate Pantheon distillation:

```text
structural graph -> candidate evidence, not truth
diff impact -> review signal, not approval
dashboard -> display artifact, not cockpit authority
domain graph -> hypothesis, not business canon
knowledge graph -> review aid, not GraphRAG runtime
```

Forbidden import:

- automatic skill installation;
- one-line remote shell installation as default setup path;
- automatic repository hooks;
- automatic graph artifact commits;
- treating graph output as a Registre Probatoire entry;
- treating LLM summaries or domain graphs as proof;
- using the tool as a Pantheon GraphRAG runtime;
- making Hermes Desktop the Pantheon cockpit.

Status:

```text
status: distill_into_hermes_candidate
risk_class: T2/T3 normally, T5 if installation, hooks, credentials, protected files or memory are involved
```

## Watched source: Neeeophytee/finding-unknowns-skills

Source: `https://github.com/Neeeophytee/finding-unknowns-skills`

Observed status on 2026-07-08:

- community collection of eight `SKILL.md` skills for Claude Code and OpenAI Codex, distilling Thariq Shihipar's finding-unknowns essay;
- core framing: the prompt is a map, the codebase is the territory; unknowns left in the "unknown" row become expensive once implementation starts;
- skills grouped by phase — before implementation (`blindspot-pass`, `brainstorm-prototypes`, `interview-me`, `reference-hunt`, `implementation-plan`), during (`implementation-notes`), after (`pitch-packager`, `change-quiz`);
- pure Markdown protocols: questioning, note-keeping and packaging disciplines with no runtime surface of their own;
- installable as a Claude Code plugin or by copying folders; also usable passively via `CLAUDE.md` / `AGENTS.md` guidance;
- community distillation, not an official Anthropic artifact.

Pantheon interpretation:

```text
finding-unknowns-skills is a methodology source for unknowns discipline.
It is not a Pantheon dependency, installed skill set, approval source or runtime.
```

Useful patterns to watch:

- explicit known/unknown taxonomy, adjacent to the mandated implemented / documented / partial / to-verify status discipline;
- `interview-me` — architecture-changing questions surfaced one at a time before acting, adjacent to User Decision Gate preparation;
- `implementation-notes` — every deviation from the plan is logged, adjacent to the `ai_logs/` obligation and workflow traces;
- `pitch-packager` — spec, prototype and notes bundled into a reviewable package, adjacent to candidate preparation for the chokepoint;
- `change-quiz` — comprehension verification before merge, adjacent to gate review discipline;
- cheap pre-implementation passes that move unknowns into the open before they become expensive.

Candidate Pantheon distillation:

```text
blindspot-pass -> governance audit pass inspiration (doc-vs-code unknowns, classified per the status vocabulary)
interview-me -> User Decision Gate question-preparation inspiration
implementation-notes -> ai_logs / workflow trace discipline reinforcement
pitch-packager -> candidate packaging inspiration (Evidence Pack / Registre Probatoire edit preparation)
change-quiz -> gate comprehension-check inspiration
before/after protocols -> governance-side doctrine; during protocols -> Hermes-side candidates under Task Contract
```

Forbidden import:

- automatic installation of the plugin or skills;
- treating the skill texts as doctrine before distillation;
- adopting the "during implementation" protocols as governance-core behavior — they belong to an execution runtime;
- claiming the methodology is implemented in Pantheon while it is only watched.

Status:

```text
status: pattern_candidate
risk_class: T1 — Markdown questioning protocols; no runtime surface unless installed, which is not authorized here
primary_route: SKILL_WATCHLIST.md -> distill_into_doctrine review for the before/after protocols; distill_into_hermes_candidate review for the during protocols
```

## Watched source: vercel-labs/skills

Source: `https://github.com/vercel-labs/skills`

Observed status on 2026-07-08:

- CLI (`npx skills`) for discovering, installing and managing agent skills across 70+ coding agents (Claude Code, Cursor, Codex, Copilot and others);
- built on an emerging open specification (agentskills.io): a skill is a folder with a `SKILL.md` carrying YAML frontmatter (name, description);
- discovers skills by convention in `skills/`, `.agents/skills/`, agent-specific directories and plugin manifests such as `.claude-plugin/marketplace.json`;
- installs by copy or symlink, project-scoped or global; `npx skills use` generates a prompt without installing;
- infrastructure and packaging standard, not a methodology or curated catalogue.

Pantheon interpretation:

```text
vercel-labs/skills is a packaging-standard and distribution-channel signal.
The format is watchable; the installer is exactly the free plugin manager the governance core must not recreate.
It is not a Pantheon dependency, installer, marketplace or approval source.
```

Useful patterns to watch:

- the `SKILL.md` + frontmatter packaging convention as a candidate format for governance-authored protocols, so external runtimes can pull them without Pantheon pushing anything;
- directory and manifest discovery conventions (`skills/`, marketplace manifests);
- cross-agent portability pressure — the same skill text consumed by many runtimes;
- the temporary-use mode (`use` without install) as a lighter-exposure pattern worth naming in boundary reviews.

Candidate Pantheon distillation:

```text
SKILL.md format -> candidate packaging convention for distilled Pantheon protocols (passive source, ecosystem pulls)
skill installation -> governed capability decision: candidate -> read-only verification -> User Decision Gate -> Hermes-side install gesture
discovery conventions -> SKILL_LIFECYCLE declared-state manifest inspiration
```

Forbidden import:

- vendoring or wrapping the CLI inside this repository;
- any auto-install of skills at setup, in CI or from the governance core;
- treating agentskills.io compatibility as trust, maturity or approval;
- letting `mcp-server/` trigger an installation — it may verify a skill candidate read-only and return a verdict as data, never execute the install;
- turning the format convention into a skill marketplace, install queue or update channel.

Status:

```text
status: boundary_required
risk_class: T1 for format observation; T5 if installation, hooks or repository mutation are involved
primary_route: SKILL_WATCHLIST.md -> SKILL_LIFECYCLE.md admission path for any concrete skill; format adoption is a separate doctrine review
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
- skill sprawl detection;
- governance preflight pattern design;
- module contract review pattern design;
- acceptance and verification trace discipline.

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
