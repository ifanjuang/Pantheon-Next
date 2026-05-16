# Pantheon Next

> Version française : [README.fr.md](README.fr.md)

> Sources. Evidence. Memory. Validation.  
> A governance layer for professional AI work.

**Current status:** Pantheon Next is a governance and documentation repository under controlled bootstrap. It is structurally coherent, but partial. Some documents are active doctrine. Some are stubs. Some implementation areas are still absent. For authoritative status, read [`docs/governance/STATUS.md`](docs/governance/STATUS.md).

Pantheon Next helps professionals use AI on sensitive dossiers without losing control of sources, assumptions, evidence, memory and validation.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

AI can accelerate reading, comparison, drafting, extraction and review. It can also blur contexts, flatten contradictions and turn weak assumptions into apparent certainty.

Pantheon Next exists to prevent that drift.

It frames the task, separates source from evidence, keeps memory candidate until approved, and makes human validation explicit.

```text
AI opens possibilities.
Pantheon organizes them.
The human decides.
Only the validated remains.
```

---

## What this repository is

Pantheon Next is a **governance layer** for professional AI workflows.

It defines:

| Area | Purpose |
|---|---|
| Doctrine | The operating boundaries of the system. |
| Roles | Cognitive governance roles, not autonomous agents. |
| Task Contracts | The frame for a delegated task. |
| Evidence Packs | The proof package that makes a result reviewable. |
| Approval levels | The thresholds for action, memory, doctrine and risk. |
| Memory policy | The path from candidate information to approved memory. |
| Knowledge taxonomy | The distinction between source, knowledge, context, evidence, memory and doctrine. |
| External tools policy | The rules for tools, connectors, writes, providers and sensitive data. |
| Integration boundaries | What OpenWebUI may expose and what Hermes Agent may execute. |

Pantheon Next does not replace professional judgment. It structures the conditions under which AI output can become professional work.

---

## What this repository is not

Pantheon Next is not:

- a chatbot;
- an autonomous agent runtime;
- a tool runtime;
- an LLM provider router;
- a scheduler;
- a queue or message bus;
- a central LangGraph runtime;
- a hidden workflow engine;
- a free plugin manager;
- a self-promoting memory system;
- an automatic skill installer;
- a dashboard to monitor all day;
- a replacement for professional responsibility.

The rule is simple:

```text
Pantheon Next governs execution.
It does not execute.
```

---

## The operating model

Pantheon Next is built around three distinct surfaces.

| Surface | Role | Boundary |
|---|---|---|
| OpenWebUI | User cockpit | Chat, files, Knowledge Bases, approval prompts, results and Evidence Pack display. It does not canonize memory or become truth. |
| Hermes Agent | External execution runtime | Tools, skills, terminal, file operations, search, workers, subagents and operational work. It returns candidates and evidence. |
| Pantheon Next | Governance source | Doctrine, roles, Task Contracts, approvals, Evidence Packs, Canonical Memory rules, policies and context packs. |

OpenWebUI may display. Hermes may execute. Pantheon decides what is legitimate.

Hermes done does not mean Pantheon approved. OpenWebUI display does not mean canonical truth. Retrieved knowledge does not mean memory.

---

## Professional loop

Pantheon turns a vague AI request into a controlled professional path.

```text
User request
→ task framing
→ source intake
→ scope and context selection
→ strategy
→ external execution
→ Evidence Pack
→ human review
→ approved output, rejected output or Memory Candidate
→ possible Canonical Memory only after approval
```

The loop should stay continuous where the system can work safely. It should stop only when the user must validate, verify, choose, supply missing information or accept a responsibility-bearing action.

This is the central product idea: AI can do more work between validation gates, but it must not cross governance gates silently.

---

## Why this matters

Professional dossiers are not just documents. They contain obligations, risks, contradictions, deadlines, private information and decisions that can engage responsibility.

A dossier may include contracts, plans, reports, emails, quotes, regulations, meeting notes, PDFs, web sources, images, spreadsheets and conflicting versions.

Without governance, AI tends to produce an answer. With Pantheon, the target is different: a result that can be reviewed, challenged, limited, approved, rejected or memorized with traceability.

| Without Pantheon | With Pantheon |
|---|---|
| A useful answer, hard to verify. | A reviewable output linked to sources and assumptions. |
| Sources scattered across tools. | Sources identified, scoped and recorded. |
| Hypotheses can become hidden facts. | Assumptions remain visible and discussable. |
| Memory keeps too much or the wrong thing. | Memory remains candidate until approved. |
| Decisions are hard to retrace. | Evidence and approval state remain visible. |
| AI usage becomes fragmented. | AI work follows a governed professional path. |

---

## First demonstrable scenario

The first clear scenario is a controlled review of a sensitive dossier.

```text
Sensitive dossier
→ Task Contract
→ External execution
→ Evidence Pack
→ Human review
→ Validated output or Memory Candidate
```

Typical inputs:

- contract;
- CCTP or technical specification;
- quote;
- technical report;
- legal memo;
- project folder;
- email thread;
- meeting transcript;
- contradictory document versions.

Typical outputs:

- risk summary;
- obligation list;
- contradiction report;
- missing information;
- assumptions to verify;
- sourced synthesis;
- Memory Candidates;
- final validation checklist.

A successful demonstration should show what was asked, which sources were used, what was assumed, what remains uncertain, what contradicts what, what requires validation, what can be transmitted, what can become memory and what must be rejected.

---

## Core governance objects

| Object | Role |
|---|---|
| Task Contract | Frames intent, scope, sources, constraints, allowed outputs, forbidden outputs, approval ceiling and memory rules. |
| Evidence Pack | Records the reviewable proof package: sources, assumptions, actions, risks, outputs, reviews, memory candidates and approval state. |
| Approval Levels | Define decision thresholds for reading, drafting, reversible actions, persistent changes, external effects and critical actions. |
| Memory Candidate | Proposed durable information. It is not canonical by default. |
| Canonical Memory | Approved, scoped and evidence-linked memory. |
| Context Pack | A bounded context artifact that may be sent to an external runtime. |
| External Tools Policy | Governs capabilities that read, transform, write, send, publish, configure, execute or influence memory. |
| AI Log | Records significant AI-assisted repository interventions. |

---

## Pantheon roles

The file [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) keeps its historical name, but the canonical concept is **Pantheon Role**.

Roles are governance viewpoints. They are not autonomous runtime agents.

| Role | Function |
|---|---|
| ATHENA | Planning, decomposition and workflow strategy. |
| ARGOS | Source research, evidence and traceability. |
| THEMIS | Risk, policy compliance and approval boundaries. |
| APOLLO | Quality review, completeness and delivery readiness. |
| ZEUS | Arbitration between conflicts or variants. |
| IRIS | Formulation, transmission and user-facing clarification. |
| HEPHAISTOS | Build preparation, patch candidates and implementation candidates. |

Hermes profiles may align with these roles, but they remain candidate-only execution profiles. They do not approve, canonize or promote memory.

---

## Knowledge, evidence and memory

Pantheon Next does not use one flat truth bucket.

```text
Raw Source       available material
Knowledge        organized reference information
Context          task-bounded information
Evidence         selected support for a claim or output
Memory Candidate proposed durable information
Canonical Memory approved, scoped and evidence-linked memory
Doctrine         the rule layer
Runtime State    external execution state, never canonical memory
```

A source is not automatically evidence.

A retrieved document is not automatically truth.

An OpenWebUI Knowledge Base is not Canonical Memory.

A model output is not memory.

A repeated observation is not memory.

Memory becomes canonical only through evidence, review, scope and approval.

---

## Everyday tools as governed entry points

Pantheon Next does not replace professional tools. It governs how information from those tools may enter a dossier.

| Channel | Role | Current status |
|---|---|---|
| OpenWebUI | Main user cockpit | Target cockpit doctrine. |
| Hermes Agent | External execution runtime | Target runtime doctrine. |
| Local files and PDFs | Dossier material | Target input. |
| Email, Gmail, Outlook | Messages and attachments | Target governed entry point. |
| Google Drive, Docs, Sheets | Documents and tabular sources | Target governed entry point. |
| Office documents | Professional files and exports | Target governed entry point. |
| Calendar and notes | Deadlines, reminders and working notes | Target governed entry point. |
| Notion, Trello, Slack | Project knowledge and team discussions | Target governed entry point. |
| WhatsApp, Telegram | Messages, voice notes and images | Future governed entry point. |
| Web search | External source discovery | Governed external flow. |

These are not automatic built-in Pantheon connectors unless separately implemented in the external execution layer.

Tools remain channels. They do not become truth.

---

## Visual language

Pantheon also uses a city-game metaphor to make the governance model easier to understand.

<table>
<tr>
<td width="52%" align="center">
<a href="docs/assets/pantheon-rpg/references/citadel_01.jpg">
<img src="docs/assets/pantheon-rpg/references/citadel_01.jpg" width="520" alt="Pantheon RPG Citadel">
</a>
</td>
<td width="48%" valign="top">

The citadel represents the professional dossier.

Sources enter through controlled gates.

Evidence remains visible.

Assumptions do not become truth by accident.

Memory does not promote itself.

The professional decides what remains.

</td>
</tr>
</table>

The visual layer is explanatory doctrine. It does not redefine Pantheon as a game engine, autonomous city, hidden workflow runner or runtime system.

---

## Current implementation status

Pantheon Next currently provides a documentation-level governance baseline.

Implemented or documented:

- governance doctrine;
- runtime boundary doctrine;
- Pantheon Role registry;
- Task Contract doctrine;
- Evidence Pack doctrine;
- approval doctrine;
- memory doctrine;
- external tools policy;
- OpenWebUI integration doctrine;
- Hermes integration doctrine;
- knowledge taxonomy and scope framing;
- narrative and visual assets;
- lightweight Hermes profile templates.

Not implemented in this repository:

- autonomous runtime;
- OpenWebUI runtime integration;
- Hermes runtime integration;
- automatic Evidence Pack generation;
- Memory Candidate review UI;
- provider routing;
- plugin management;
- schemas reconciliation;
- tests;
- read-only operations tooling;
- deployment stack.

Status must be verified capability by capability in [`docs/governance/STATUS.md`](docs/governance/STATUS.md).

---

## Repository structure

```text
docs/governance/     governance doctrine and status documents
hermes/profiles/     lightweight candidate-only Hermes profile templates
docs/assets/         narrative and visual references
ai_logs/             AI-assisted intervention history
legacy/              historical Pantheon OS source material
schemas/             expected declarative contracts, not reconciled yet
operations/          expected read-only tooling, not implemented yet
tests/               expected tests, not implemented yet
```

Key entry points:

| Document | Purpose |
|---|---|
| [`docs/governance/STATUS.md`](docs/governance/STATUS.md) | Authoritative repository status. |
| [`docs/governance/README.md`](docs/governance/README.md) | Governance index and read order. |
| [`docs/governance/ARCHITECTURE.md`](docs/governance/ARCHITECTURE.md) | Governance anatomy and boundary model. |
| [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) | Canonical Pantheon Role registry. |
| [`docs/governance/TASK_CONTRACTS.md`](docs/governance/TASK_CONTRACTS.md) | Task framing doctrine. |
| [`docs/governance/EVIDENCE_PACK.md`](docs/governance/EVIDENCE_PACK.md) | Evidence doctrine. |
| [`docs/governance/MEMORY.md`](docs/governance/MEMORY.md) | Memory promotion doctrine. |
| [`docs/governance/APPROVALS.md`](docs/governance/APPROVALS.md) | Approval levels. |
| [`docs/governance/HERMES_INTEGRATION.md`](docs/governance/HERMES_INTEGRATION.md) | Hermes boundary doctrine. |
| [`docs/governance/OPENWEBUI_INTEGRATION.md`](docs/governance/OPENWEBUI_INTEGRATION.md) | OpenWebUI boundary doctrine. |
| [`docs/governance/EXTERNAL_TOOLS_POLICY.md`](docs/governance/EXTERNAL_TOOLS_POLICY.md) | External capability governance. |
| [`docs/governance/KNOWLEDGE_TAXONOMY.md`](docs/governance/KNOWLEDGE_TAXONOMY.md) | Source, knowledge, context, evidence and memory vocabulary. |

When documents disagree, treat `STATUS.md` as the first status reference until reconciliation.

---

## Near-term priorities

- build a fictional demo dossier;
- provide a sample Task Contract;
- provide a sample Evidence Pack;
- clarify implementation status by capability;
- document first professional use-case packs;
- prepare OpenWebUI and Hermes handoff examples;
- reconsider schemas under the protected-file rule;
- add read-only validation tooling only if it preserves the governance boundary.

---

## Final principle

```text
AI produces possibilities.
Pantheon governs the path.
Hermes executes the work.
OpenWebUI exposes the result.
The human decides.
Only the validated remains.
```
