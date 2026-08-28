# Reference Boundaries

Status: active support doctrine — external reference boundary control.

This document defines what Pantheon Next may learn from external systems and what it must not import from them.

It does not approve dependencies.

It does not approve integrations.

It does not define runtime adoption.

It does not authorize a LangGraph runtime, GraphRAG runtime, observability backend, MCP layer, skill marketplace, provider router, scheduler, queue, tool runtime, automatic memory system or hidden workflow runner inside Pantheon Next.

Runtime/client/authority placement is inherited from `HERMES_INTEGRATION.md`: optional compatible runtime clients expose runtime interaction only, Hermes/the external runtime executes admitted work, Pantheon Cockpit projects governed state, and external references cannot transfer authority to any tool or surface.

## Purpose

External references are useful because they reveal patterns, failure modes and vocabulary.

They are dangerous when they silently become architecture.

This document answers:

```text
What may Pantheon learn from a reference without absorbing its runtime responsibilities?
```

## Canonical boundary rule

```text
External references may inspire governance patterns.
They do not authorize importing runtime responsibility into Pantheon.
```

A reference may inform:

- doctrine;
- Task Contract vocabulary;
- Evidence Pack expectations;
- approval thresholds;
- memory boundaries;
- scope isolation;
- role review responsibilities;
- User Decision Gate triggers;
- Hermes candidate constraints;
- runtime-client interaction requirements;
- Pantheon Cockpit projection requirements;
- rejected-pattern memory.

A reference must not authorize:

- execution engine;
- agent runtime;
- tool runtime;
- provider router;
- scheduler;
- queue;
- message bus;
- hidden workflow runner;
- LangGraph central runtime;
- GraphRAG runtime;
- observability backend;
- MCP server layer inside Pantheon;
- skill installer;
- plugin marketplace;
- automatic memory promotion;
- automatic approval;
- self-evolution.

## Reference classification

| Reference class | Allowed use | Forbidden use |
|---|---|---|
| Runtime framework | vocabulary for external execution boundaries | Pantheon execution engine |
| Observability system | trace summary and evaluation inspiration | Pantheon observability backend or approval authority |
| Graph/RAG system | provenance and corpus-structure inspiration | graph truth or memory runtime |
| Skill ecosystem | skill anatomy and lifecycle inspiration | marketplace, installer or auto-loader |
| Connector ecosystem | least-capability and scoped-access inspiration | plugin manager or provider router |
| Coding agent | patch-candidate and controlled-terminal discipline | internal coding runtime |
| Professional vertical agent | domain review gates and source discipline | autonomous professional authority |
| Prompting method | review method or signal pattern | hidden orchestration or self-approval loop |

## Current boundary notes

| Reference | Legitimate Pantheon distillation | Boundary |
|---|---|---|
| LangGraph | interruption points, state visibility vocabulary, resumable external work as evidence surface | no LangGraph runtime or executable graph inside Pantheon |
| LangSmith | trace inspection, evaluation reports, audit logs as support signals | traces and evals are not Evidence Pack approval |
| Langfuse | self-hostable observability inspiration, prompt and evaluation review signals | no Langfuse-backed Pantheon memory or approval authority |
| GraphRAG | structured corpus preparation, graph-aware retrieval status, contradiction maps | graph output is not proof, doctrine or a Registre Probatoire entry |
| GenAI_Agents | broad pattern catalog and professional-use-case discovery | tutorial code is not Pantheon architecture |
| Shokunin | `SKILL.md` anatomy, skill lifecycle, checklists, anti-patterns | no memory, MCP, auto-save, scheduler or self-update import |
| Agensi skills | market and skill discovery signal | popularity, price, rating or install count is not approval |
| contracts-skill | contract preflight, acceptance and verification traces | no external skill dependency or contract file as governance authority |
| Hermes Workspace | external runtime cockpit and execution reference | not a Pantheon model, not an OpenWebUI replacement |
| SmallCode | small-model/coding-agent discipline and controlled execution | no coding runtime inside Pantheon |
| Glia-like shared memory | local-first memory and retrieval tension | shared memory is not a Registre Probatoire entry |
| contextschema-py | context sufficiency, freshness, provenance and invalidation vocabulary | context sufficiency score is not C0-C5 approval |
| chunk-norris | chunking fitness evaluation before Knowledge ingestion | selected chunker is not global KB doctrine or evidence authority |
| MMLongBench-Doc | long-document, multimodal, cross-page and unanswerable QA evaluation | benchmark score is not professional validation or delivery approval |
| Medium RAG 10M+ article | large-scale RAG reliability vocabulary and caution signal | near-zero hallucination claim is not evidence without benchmark and audit |
| Reddit r/RAG discussions | practitioner weak signals and recurring failure vocabulary | anecdote is not doctrine, benchmark or implementation basis |
| agent_memory_curator_agent | memory event emission and curation-report vocabulary | curator must not become a Registre Probatoire entry authority |
| skillsgate | skill inventory and compatibility UX signal | no skill marketplace, installer, remote sync or OpenWebUI plugin surface |

## RAG evidence boundary notes

RAG references may help Pantheon define:

- source preparation expectations;
- chunking fitness vocabulary;
- retrieval limitation disclosure;
- context sufficiency status;
- evidence page and modality mapping;
- unanswerable question handling;
- User Decision Gate triggers.

They must not authorize:

- automatic Knowledge Base rewrite;
- automatic source validation;
- retrieval score as proof;
- benchmark score as approval;
- OpenWebUI ingestion runtime;
- Hermes sovereign ingestion policy;
- Pantheon parsing, chunking or retrieval runtime.

## Boundary test

Before citing or importing a reference, ask:

```text
Does this pattern improve governance visibility?
Does it preserve human approval?
Does it preserve Evidence Pack discipline?
Does it preserve candidate versus canonical distinction?
Does it preserve scope isolation?
Does it keep execution outside Pantheon?
Does it keep runtime clients as non-authoritative interaction surfaces?
Does it keep Pantheon Cockpit as projection rather than authority or persistence?
Does it keep Hermes as runtime rather than governance authority?
```

If the answer is unclear, the reference must remain on `WATCHLIST.md` or move to `EXTERNAL_TOOLS_POLICY.md` before distillation.

## Distillation permission levels

| Level | Meaning | Allowed destination |
|---|---|---|
| R0 observe | reference is interesting but unreviewed | `WATCHLIST.md` |
| R1 boundary | reference requires explicit limit | `REFERENCE_BOUNDARIES.md` |
| R2 method review | reference is a reasoning or workflow method | `EXTERNAL_TOOLS_POLICY.md` |
| R3 pattern candidate | reference yields a possible governance pattern | `DISTILLATION_REGISTRY.md` |
| R4 doctrine candidate | pattern may update active doctrine | relevant governance document with approval |
| R5 rejected | pattern would violate doctrine | `REJECTED_PATTERNS.md` |

## Relationship to external agentic inspiration

`EXTERNAL_TOOLS_POLICY.md` contains detailed review notes for specific systems.

This document defines the boundary rule that applies across those notes.

If the two documents appear to conflict, the stricter anti-runtime interpretation wins until a governed review resolves the conflict.

## Relationship to Skill Watchlist

`SKILL_WATCHLIST.md` is the specialized watchlist for external skill ecosystems.

This document controls the boundary around how those ecosystems may be interpreted.

A watched skill can become a pattern candidate.

It cannot become a Pantheon dependency, runtime capability or approved skill without separate review.

## Relationship to Evidence Packs

An external reference can support an Evidence Pack only when it is cited as a source, limitation, comparison or rationale.

The reference itself does not validate the output.

Evidence must still identify claim, scope, source, assumptions, risk and approval state.

## Relationship to Memory

An external reference may produce a Register Candidate only when the claim, scope, evidence and approval path are explicit.

A reference must not become a Registre Probatoire entry because it is popular, repeated, embedded, retrieved or technically impressive.

## Forbidden drift

Reference use must never become:

- appeal to authority;
- vendor endorsement;
- dependency commitment;
- implementation approval;
- architecture import;
- hidden runtime migration;
- skill marketplace approval;
- memory promotion shortcut;
- automatic approval shortcut;
- professional liability substitute.

If a reference is cited as proof that Pantheon should implement a runtime feature, the boundary has failed.

## Final rule

```text
Pattern distillation is allowed.
Runtime migration is not.
```