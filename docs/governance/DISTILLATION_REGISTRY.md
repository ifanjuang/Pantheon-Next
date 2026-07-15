# Distillation Registry

Status: active support doctrine — extracted pattern registry only.

This document records patterns that Pantheon Next has extracted from external references.

It is not a dependency list.

It is not an implementation backlog.

It is not a runtime plan.

It does not approve integrations, tools, skills, providers, plugins, MCP servers, observability backends, GraphRAG runtimes, LangGraph runtimes, schedulers, queues or automatic memory systems.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

External references are useful only when their value is distilled into explicit Pantheon governance patterns.

This document answers:

```text
What have we actually extracted, where does it belong, and what remains forbidden?
```

It prevents vague inspiration from turning into architecture by implication.

## Registry record format

Recommended fields:

```text
pattern_name
source_reference
source_class
extracted_problem
pantheon_distillation
intended_destination
allowed_use
forbidden_import
status
review_notes
```

## Status values

```text
candidate
active_support_pattern
active_governance_pattern
hermes_candidate_constraint
openwebui_exposure_candidate
method_review_required
rejected
superseded
archived
```

A pattern is not active doctrine unless the destination governance document explicitly adopts it.

## Current distilled patterns

| Pattern | Source reference | Pantheon distillation | Destination | Status |
|---|---|---|---|---|
| Human-owned contract boundary | contracts-skill | separate human intent from machine-maintained mapping | `TASK_CONTRACTS.md`, future `SKILL_LIFECYCLE.md` reconciliation | active_support_pattern |
| Preflight before mutation | contracts-skill, coding agent practice | check scope, constraints, protected files, evidence need and approval before changes | `EXECUTION_DISCIPLINE.md`, `EXTERNAL_TOOLS_POLICY.md` | active_support_pattern |
| Acceptance and verification trace | contracts-skill | record acceptance and verification expectations without claiming implementation | `EVIDENCE_PACK.md`, `APPROVALS.md` | active_support_pattern |
| Interruptible workflow point | LangGraph | treat human-in-the-loop as approval interruption vocabulary, not runtime graph | `TASK_CONTRACTS.md`, `USER_DECISION_GATE.md` | candidate |
| Runtime state visibility | LangGraph | summarize relevant external runtime state into evidence without owning it | `RUN_GRAPH.md`, `EVIDENCE_PACK.md` | candidate |
| Trace hierarchy summary | LangSmith, Langfuse | compress trace information into governance-relevant evidence summaries | `EVIDENCE_PACK.md`, `EXTERNAL_TOOLS_POLICY.md` | candidate |
| Evaluation score as signal | LangSmith, Langfuse | use scores as review signals only, never as approval | `APPROVALS.md`, `TENSIONS_AND_RISKS.md` | active_support_pattern |
| Measurability coverage disclosure | iFixAi | expose runtime-observed, declared, synthesized, judge-assessed, unmeasurable and insufficient-evidence coverage beside any aggregate result | `EVIDENCE_PACK.md`, `EXTERNAL_TOOL_PLACEMENT_REGISTER.md` | candidate |
| Declared governance demotion | iFixAi | treat governance supplied by fixtures or synthesized from configuration as declaration candidates, never as runtime verification, evidence sufficiency or approval | `EVIDENCE_PACK.md`, `EXTERNAL_TOOLS_POLICY.md`, `EXTERNAL_TOOL_PLACEMENT_REGISTER.md` | candidate |
| Pre-execution simulation | Future AGI | stress-test high-risk candidate actions before execution, delivery, memory or doctrine change | `PRE_EXECUTION_SIMULATION.md`, `TASK_CONTRACTS.md`, `EVIDENCE_PACK.md`, `USER_DECISION_GATE.md` | active_support_pattern |
| Trajectory evaluation | Future AGI, LangSmith, Langfuse | evaluate the path, tool-use sequence or multi-step behavior as a review signal, not approval | `PRE_EXECUTION_SIMULATION.md`, `EVIDENCE_PACK.md`, `TENSIONS_AND_RISKS.md` | candidate |
| Improvement Candidate | Future AGI | convert feedback or optimization output into reviewable candidate change rather than self-improvement | `PRE_EXECUTION_SIMULATION.md`, `MEMORY.md`, `APPROVALS.md`, `REJECTED_PATTERNS.md` | active_support_pattern |
| Prompt version as review artifact | LangSmith, Langfuse | preserve prompt/config version when it affects output legitimacy | `EVIDENCE_PACK.md`, `CONTEXT_PACKS.md` | candidate |
| Source graph candidate | GraphRAG | represent corpus structure and relationships as retrieved context, not truth | `RAG_INGESTION_PIPELINE.md`, `KNOWLEDGE_TAXONOMY.md` | candidate |
| Contradiction graph | GraphRAG, Governance College doctrine | map conflicting claims and sources without smoothing them into consensus | `GOVERNANCE_COLLEGE.md`, `EVIDENCE_PACK.md` | candidate |
| Skill anatomy card | Shokunin, Agensi | skill records need trigger, scope, anti-patterns, evidence, risk and compatibility notes | `SKILL_WATCHLIST.md`, future `SKILL_LIFECYCLE.md` | active_support_pattern |
| Skill anti-pattern library | Shokunin | record when a skill should not activate | `SKILL_WATCHLIST.md`, `REJECTED_PATTERNS.md` | active_support_pattern |
| Skill eval report | Shokunin | skill quality must be reviewed through evidence and task fit | `SKILL_WATCHLIST.md`, `EVIDENCE_PACK.md` | candidate |
| Marketplace signal demotion | Agensi | popularity, price, votes and installs are signals, not approval | `SKILL_WATCHLIST.md`, `REFERENCE_BOUNDARIES.md` | active_governance_pattern |
| Least capability principle | external tools and connector ecosystems | use the narrowest tool and avoid write-capable surfaces for read-only tasks | `EXTERNAL_TOOLS_POLICY.md` | active_governance_pattern |
| Draft-only professional posture | professional vertical assistants | regulated or liability-sensitive outputs remain drafts until review | `USER_DECISION_GATE.md`, examples | active_support_pattern |
| Source freshness disclosure | research, RAG and professional workflows | expose date, version, staleness and source limitations | `EVIDENCE_PACK.md`, `KNOWLEDGE_TAXONOMY.md` | active_support_pattern |
| Memory candidate discipline | shared memory and persistent agent systems | every durable memory-like claim requires claim, scope, evidence, risk and approval | `MEMORY.md`, `SCOPE_ISOLATION.md` | active_governance_pattern |
| Context pack as adapter-safe bundle | assistant instruction ecosystems | bounded task context can travel, but does not become doctrine or memory | `CONTEXT_PACKS.md` | active_governance_pattern |
| Anti-collusion role separation | multi-agent frameworks as counter-models | roles must preserve distinct review pressures, not simulate a hidden agent team | `GOVERNANCE_COLLEGE.md` | active_governance_pattern |
| User Decision Gate | professional workflow risk patterns | unresolved high-impact tension must be exposed to the human | `USER_DECISION_GATE.md` | active_governance_pattern |
| Context Sufficiency Gate | contextschema-py | retrieved context should be checked for required fields, source, freshness and invalidation before action | `TASK_CONTRACTS.md`, `EVIDENCE_PACK.md`, `KNOWLEDGE_TAXONOMY.md` | candidate |
| Chunking Fitness Evaluation | chunk-norris | chunking strategies should be tested against representative questions and retrieval traces before Knowledge ingestion | `RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md`, `RAG_INGESTION_PIPELINE.md` | candidate |
| Evidence Page and Modality Mapping | MMLongBench-Doc | document answers should preserve page-level and source-type evidence metadata | `EVIDENCE_PACK.md`, `KNOWLEDGE_TAXONOMY.md`, `OPENWEBUI_INTEGRATION.md` | candidate |
| Unanswerable Question Testing | MMLongBench-Doc | document QA systems should test refusal when available evidence is insufficient | `USER_DECISION_GATE.md`, `EVIDENCE_PACK.md`, `TENSIONS_AND_RISKS.md` | candidate |
| Memory Curation Report | agent_memory_curator_agent | memory proposals should report accepted, proposed, rejected, redacted, conflict and deprecation status | `MEMORY.md`, `EVIDENCE_PACK.md`, `SCOPE_ISOLATION.md` | candidate |
| Skill Manager Demotion | skillsgate | skill inventory and compatibility UX may inform cockpit display but not installation authority | `SKILL_WATCHLIST.md`, `REJECTED_PATTERNS.md`, `REFERENCE_BOUNDARIES.md` | candidate |
| Profile identity layer | SOUL.md, Hermes Personality & SOUL.md | stabilize Hermes execution posture without granting governance authority | `HERMES_INTEGRATION.md`, `reference_reviews/SOUL_MD_HERMES_PROFILE.md`, future `hermes/profiles` writing guidance | hermes_candidate_constraint |

## Candidate future pattern cards

The following patterns deserve future cards or checklists, but they are not implementation plans:

```text
Governance Doctor Pattern
Retrieval Evaluation Pattern
Observability-to-Evidence Summary Pattern
GraphRAG Source Graph Pattern
Contradiction Ledger Pattern
Skill Candidate Lifecycle Pattern
Professional Dossier Preflight Pattern
OpenWebUI User Decision Surface Pattern
Hermes Capability Gap Pattern
Context Sufficiency Gate
Chunking Fitness Evaluation
Long Document Evidence Locality Pattern
Unanswerable Question Testing
Pre-Execution Simulation Pattern
Trajectory Evaluation Pattern
Improvement Candidate Pattern
Profile Identity Layer Checklist
```

Each future card must define:

```text
FOR
NOT FOR
required evidence
approval implication
memory implication
runtime boundary
failure modes
related documents
```

## Distillation rules

A distilled pattern must:

- name the external source;
- identify the governance problem it helps solve;
- define the Pantheon destination;
- preserve forbidden imports;
- avoid vendor or framework lock-in;
- stay compatible with Task Contracts, Evidence Packs, approvals and memory policy;
- preserve the OpenWebUI / Hermes / Pantheon boundary.

## What does not count as distillation

The following are not valid distillation:

- copying a framework architecture;
- importing code because the pattern is useful;
- treating a popular repository as authority;
- treating a runtime capability as governance requirement;
- adding a dependency without a governance decision;
- converting external documentation into Pantheon doctrine without review;
- creating a skill because a marketplace lists one;
- creating memory because a system stores user history.

## Relationship to rejected patterns

When a pattern is useful but dangerous, split it:

```text
useful part → DISTILLATION_REGISTRY.md
forbidden part → REJECTED_PATTERNS.md
```

Example:

```text
Shokunin SKILL.md anatomy → distill.
Shokunin persistent memory / MCP / auto-save / scheduler → reject as Pantheon core pattern.
```

## Relationship to approvals

Adding a support pattern to this registry is not the same as modifying canonical doctrine.

Changing active governance documents may require stronger approval, especially when it affects:

- memory promotion;
- approval thresholds;
- protected files;
- Task Contract semantics;
- external tool authorization;
- OpenWebUI or Hermes integration boundaries;
- professional liability posture.

## Forbidden drift

The registry must never become:

- implementation backlog;
- dependency manifest;
- vendor ranking;
- plugin catalog;
- skill marketplace;
- runtime roadmap;
- automatic adoption queue;
- authority substitute;
- proof of safety.

If a registry entry is treated as permission to implement runtime behavior, the boundary has failed.

## Final rule

```text
Distillation records what Pantheon learned.
It does not grant Pantheon new runtime power.
```
