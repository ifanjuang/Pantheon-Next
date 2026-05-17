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

In plain language:

- **OpenWebUI** is the chat application: the visible place where the user talks to AI, uploads or consults documents, sees answers and gives approvals. It can be self-hosted and open source.
- **Hermes Agent** is the external workshop: the part that can perform technical work such as searching, extracting, comparing, transcribing, preparing files or producing candidates.
- **Pantheon Next** is the rulebook and control frame: it says what is allowed, what must be checked, what needs proof, what needs approval and what may become memory.

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

Less technically: it is a set of rules, methods and reference documents for using AI on real professional dossiers without turning every answer into truth.

It defines:

| Area | Plain-language meaning |
|---|---|
| Doctrine | The basic rules of the system. |
| Roles | Review viewpoints: planning, evidence, risk, quality, arbitration, wording and implementation preparation. |
| Task Contracts | Mission sheets that say what is being asked, with which limits and which expected result. |
| Evidence Packs | Proof folders that show sources, assumptions, risks and what was actually used. |
| Approval levels | Decision thresholds: what can be drafted, changed, transmitted, memorized or rejected. |
| Memory policy | The rule that nothing becomes durable memory by accident. |
| Knowledge taxonomy | The distinction between a source, a useful reference, evidence, context and validated memory. |
| External tools policy | The rules for search, email, files, connectors, providers, writes and sensitive data. |
| Integration boundaries | What the chat app may show and what the execution workshop may do. |

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

Less technically: Pantheon is not the machine that does everything by itself. It is the frame that prevents the machine from doing the wrong thing silently.

The rule is simple:

```text
Pantheon Next governs execution.
It does not execute.
```

---

## The operating model

Pantheon Next is built around three distinct surfaces.

| Surface | Plain-language role | Boundary |
|---|---|---|
| Chat application — OpenWebUI | The visible cockpit. The professional asks questions, brings documents, sees results and gives approvals. | It may display information, but display does not make something true. It does not validate memory by itself. |
| Execution workshop — Hermes Agent | The external worker. It may search, extract, compare, transcribe, draft, prepare files or return candidate results. | It executes under rules. It does not approve its own work and does not decide what becomes memory. |
| Governance frame — Pantheon Next | The rulebook. It defines roles, task framing, evidence, approvals, memory rules and tool limits. | It governs legitimacy. It does not become a hidden execution engine. |

The short doctrine remains:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

A result visible in the chat is not automatically validated. Work completed by an execution tool is not automatically approved. A document found by search is not automatically proof. A useful answer is not automatically memory.

---

## Key vocabulary in ordinary words

| Pantheon term | Ordinary meaning |
|---|---|
| Task Contract | A mission sheet: what to do, with which documents, under which limits and with which expected output. |
| Evidence Pack | A proof folder: sources used, assumptions, risks, contradictions, actions and review state. |
| Memory Candidate | Something that may be useful later, but still needs review before being kept. |
| Canonical Memory | Validated memory, scoped and linked to evidence. |
| Context Pack | The minimum useful context sent to a worker for a specific task. |
| Pantheon Role | A review angle: plan, verify, check risk, improve wording, arbitrate or prepare a patch. |
| Knowledge Base | A document library. It helps find information, but it is not truth by itself. |
| Approval | A visible professional decision, not a technical click hidden in the system. |

This vocabulary matters because most AI risk comes from confusing these layers.

---

## Professional loop

Pantheon turns a vague AI request into a controlled professional path.

```text
User request
→ mission sheet
→ source intake
→ scope and context selection
→ work strategy
→ external execution
→ proof folder
→ human review
→ approved output, rejected output or memory proposal
→ validated memory only after approval
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
→ mission sheet
→ external execution
→ proof folder
→ human review
→ validated output or memory proposal
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
- memory proposals;
- final validation checklist.

A successful demonstration should show what was asked, which sources were used, what was assumed, what remains uncertain, what contradicts what, what requires validation, what can be transmitted, what can become memory and what must be rejected.

---

## Core governance objects

| Object | Role |
|---|---|
| Task Contract | Mission sheet that frames intent, scope, sources, constraints, allowed outputs, forbidden outputs, approval ceiling and memory rules. |
| Evidence Pack | Proof folder that records sources, assumptions, actions, risks, outputs, reviews, memory proposals and approval state. |
| Approval Levels | Decision thresholds for reading, drafting, reversible actions, persistent changes, external effects and critical actions. |
| Memory Candidate | Proposed durable information. It is not validated memory by default. |
| Canonical Memory | Approved, scoped and evidence-linked memory. |
| Context Pack | Bounded context package that may be sent to an external worker. |
| External Tools Policy | Rules for capabilities that read, transform, write, send, publish, configure, execute or influence memory. |
| AI Log | Record of significant AI-assisted repository interventions. |

---

## Pantheon roles

The file [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) keeps its historical name, but the canonical concept is **Pantheon Role**.

Roles are review viewpoints. They are not autonomous agents.

| Role | Plain-language function |
|---|---|
| ATHENA | Organizes the problem and prepares the plan. |
| ARGOS | Looks for sources and checks traceability. |
| THEMIS | Checks risk, rules and approval limits. |
| APOLLO | Reviews clarity, completeness and delivery quality. |
| ZEUS | Arbitrates when several options conflict. |
| IRIS | Reformulates, clarifies and prepares user-facing communication. |
| HEPHAISTOS | Prepares build work, patch candidates and implementation candidates. |

Hermes profiles may align with these roles, but they remain candidate-only execution profiles. They do not approve, canonize or promote memory.

---

## Knowledge, evidence and memory

Pantheon Next does not use one flat truth bucket.

```text
Raw Source       material that exists
Knowledge        organized reference material
Context          information useful for one task
Evidence         selected support for one claim or output
Memory Candidate proposed information to keep
Canonical Memory approved memory with scope and evidence
Doctrine         the rule layer
Runtime State    external execution state, never validated memory
```

A source is not automatically evidence.

A retrieved document is not automatically truth.

A Knowledge Base is a document library, not validated memory.

A model output is not memory.

A repeated observation is not memory.

Memory becomes canonical only through evidence, review, scope and approval.

---

## Everyday tools as governed entry points

Pantheon Next does not replace professional tools. It governs how information from those tools may enter a dossier.

| Channel | Plain-language role | Current status |
|---|---|---|
| OpenWebUI | Self-hostable AI chat application where the user interacts with the system. | Target cockpit doctrine. |
| Hermes Agent | External technical workshop that performs controlled work. | Target runtime doctrine. |
| Local files and PDFs | The documents already present in the professional dossier. | Target input. |
| Email, Gmail, Outlook | Messages and attachments that may become sources. | Target governed entry point. |
| Google Drive, Docs, Sheets | Shared documents and tables that may support work. | Target governed entry point. |
| Office documents | Professional files and exports. | Target governed entry point. |
| Calendar and notes | Deadlines, reminders and working notes. | Target governed entry point. |
| Notion, Trello, Slack | Project knowledge and team discussions. | Target governed entry point. |
| WhatsApp, Telegram | Messages, voice notes and images. | Future governed entry point. |
| Web search | External source discovery. | Governed external flow. |

These are not automatic built-in Pantheon connectors unless separately implemented in the external execution layer.

Tools remain channels. They do not become truth.

---

## Visual reading path

Pantheon uses a city-game metaphor to explain the governance model to non-technical professional users. The visual layer is explanatory doctrine. It does not redefine Pantheon as a game engine, autonomous city, hidden workflow runner or runtime system.

The README visual sequence should follow the user journey, not the technical stack.

### 1. Player — the professional decides

<table>
<tr>
<td width="52%" align="center">
<a href="docs/assets/pantheon-rpg/references/player_01.jpg">
<img src="docs/assets/pantheon-rpg/references/player_01.jpg" width="520" alt="Pantheon RPG Player">
</a>
</td>
<td width="48%" valign="top">

The player is the professional user.

They bring the intent, sources, context, constraints, expertise and final judgment.

Pantheon structures the path.

AI accelerates selected tasks.

Responsibility remains human.

</td>
</tr>
</table>

### 2. Worldmap — the outside information world

<table>
<tr>
<td width="52%" align="center">
<a href="docs/assets/pantheon-rpg/references/worldmap_01.jpg">
<img src="docs/assets/pantheon-rpg/references/worldmap_01.jpg" width="520" alt="Pantheon RPG World Map">
</a>
</td>
<td width="48%" valign="top">

AI, the web and external knowledge form an unstable world.

Useful knowledge, weak sources, obsolete information, contradictions and unexpected discoveries coexist.

Pantheon does not close that world.

It gives the professional a method to cross it without confusing signal, source, evidence and memory.

</td>
</tr>
</table>

### 3. Port — sources and channels enter under control

<table>
<tr>
<td width="52%" align="center">
<a href="docs/assets/pantheon-rpg/references/port_01.jpg">
<img src="docs/assets/pantheon-rpg/references/port_01.jpg" width="520" alt="Pantheon RPG Port">
</a>
</td>
<td width="48%" valign="top">

The port represents external flows: web, email, files, APIs, messengers and connectors.

Pantheon governs what may enter the dossier, what must remain temporary, what must be rejected and what may become evidence.

Tools remain channels.

They do not become truth.

</td>
</tr>
</table>

### 4. Citadel — the governed dossier

<table>
<tr>
<td width="52%" align="center">
<a href="docs/assets/pantheon-rpg/references/citadel_01.jpg">
<img src="docs/assets/pantheon-rpg/references/citadel_01.jpg" width="520" alt="Pantheon RPG Citadel">
</a>
</td>
<td width="48%" valign="top">

The citadel represents the governed professional dossier.

Sources pass through controlled gates.

Assumptions remain visible.

Memory does not promote itself.

The professional decides what remains.

</td>
</tr>
</table>

### 5. Evidence — proof before trust

Image to produce: `docs/assets/pantheon-rpg/references/evidence_01.jpg`.

This board should show selected sources, assumptions, contradictions, review tables and a sealed Evidence Pack. Its message is precise: evidence supports review, but evidence does not approve itself.

### 6. Livrables — candidate outputs before transmission

Image to produce: `docs/assets/pantheon-rpg/references/livrables_01.jpg`.

This board should show reports, tables, letters, diagrams, presentations and export bundles leaving the workshops only after review. A deliverable is a candidate until the required approval path is complete.

### 7. Pantheon — roles of judgment, not autonomous agents

<table>
<tr>
<td width="52%" align="center">
<a href="docs/assets/pantheon-rpg/references/olympus_01.jpg">
<img src="docs/assets/pantheon-rpg/references/olympus_01.jpg" width="520" alt="Pantheon RPG Olympus">
</a>
</td>
<td width="48%" valign="top">

Pantheon represents governed cognitive roles.

Planning, evidence, risk review, quality, arbitration, formulation and implementation candidates remain distinct.

These figures are governance roles and cognitive functions.

They are not autonomous runtime agents.

</td>
</tr>
</table>

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
- produce the missing `evidence_01.jpg` and `livrables_01.jpg` visual boards;
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
