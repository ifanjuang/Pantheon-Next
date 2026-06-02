# Pantheon Next

> Version française : [README.fr.md](README.fr.md)

> **The professional-conduct frame between you, your usual tools, and AI engines: what enters, what is sent out, what leaves, and what remains.**

<sub><strong>Current status:</strong> Pantheon Next is a method and documentation repository under active structuring. It is coherent, but partial. For authoritative implementation status, read <a href="docs/governance/STATUS.md">docs/governance/STATUS.md</a>.</sub>

<p><strong>Landing page:</strong> <a href="docs/index.html">open the Pantheon Next page</a>.</p>

**You already use AI. But who answers for what it writes? You do.**

You would not hand a whole dossier to an outside engineering office: you give it a clear brief and just what it needs to work. Pantheon does the same with AI — from the tool you already use, with the engine of your choice (ChatGPT, Claude, Gemini, or a local model).

```text
your tools carry the work:   you → prepare → AI → return → you decide
Pantheon governs the line:        what may enter · what may leave · what remains
```

It frames what enters, what is sent to the AI, what leaves, and what remains, according to the rules of your profession. *Answering is not acting:* the AI proposes, you decide. You keep your hand on sources, decisions and signatures — from the first draft to your sign-off.

**One example.** A recovery quote needs a client email. Most assistants will hand you a polished message that says *yes* — and quietly commit you. Pantheon stops on the question that matters: *does this email validate, accept, approve a scope, or engage you externally?* If it does, it prepares the message but holds the send: transmission stays your visible decision. If not, it lets you send it. Nothing commits you by accident.

**In plain terms:**

- you write from your usual channel;
- only the minimum necessary context reaches the AI, never the whole dossier — that is Pantheon's rule, your tools carry it out;
- the answer comes back with a status — draft, to verify, candidate;
- you validate, correct or reject;
- nothing leaves without a status, nothing remains without validation.

```text
Fluent answer ≠ safe answer.
Answering     ≠ acting.
Drafted       ≠ sent.
Sent          ≠ true.
```

## Four questions, four answers

For an architect still on the fence.

| Your question | Pantheon's answer |
|---|---|
| *What does the AI see of my dossier?* | The minimum the task needs. For a surface note to a client, it gets the floor area and the brief — not the client's identity or the rest of the dossier. |
| *What if it gets it wrong?* | Every output comes with a status and its sources. A setback line taken from an old zoning plan is marked "to verify", not delivered as settled. |
| *Do I keep control?* | Always. The AI drafts the quote-approval email; you decide to send it. The signature stays yours. |
| *And next time?* | Pantheon keeps only what you validated and scoped. The height allowed on one plot stays tied to that plot, not reused elsewhere by mistake. |

## Who this is for

Professionals who answer for what they send: architects, lawyers, doctors, accountants, engineers, consultants. Regulated work, real liability, no room for a confident answer that turns out wrong.

No technical skill required. You keep control of sources, decisions and signatures.

## What you get

- **Nothing leaves by accident.** Every output carries a status. Transmission is a decision, not a side effect.
- **An audit-ready trail.** Sources, assumptions, contradictions and approvals stay visible and reviewable.
- **The right work shape before execution.** Pantheon asks whether the task needs one reasoning context, distributed extraction, role-team handoff or bounded swarm before the engine works.
- **Memory you can trust.** Only validated, scoped, evidence-linked information is kept for later.

## How a dossier flows

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg" width="100%" alt="Before and after: a raw answer becomes a controlled professional dossier path">
  </a>
</p>

<p align="center"><strong>Before and after.</strong><br><em>A raw answer is fast. Pantheon turns the work into a visible dossier path.</em></p>

Speed is easy. Control is the hard part. Pantheon adds the path that responsibility-bearing work needs:

```text
request
→ mission sheet
→ source and scope selection
→ minimum necessary context
→ evidence topology check
→ candidate work
→ proof folder
→ review
→ human decision
→ optional scoped memory
```

It never exposes the whole dossier. It prepares the minimum necessary context — enough to work, not enough to expose everything. Four gates govern the flow:

| Gate | Question |
|---|---|
| Entry | Which sources, documents or facts may enter the working perimeter? |
| Context | What is the smallest sufficient context for this task? |
| Output | What may be produced, under which status, and for which recipient? |
| Memory | What may remain, under which scope, with which proof and approval? |

An interactive map shows how the pieces connect — the screen, the workshop, the method, the engines, the documents and the memory: [open the interactive map](docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html). (GitHub does not render it inline; open it by link.)

## You hand over the dossier, the system sorts it

You do not have to carve up your dossier yourself. You hand over your material — a zoning plan, a soil report, client exchanges, a specification — and, depending on your request, the system reads it, classifies it, and decides what to do with each piece:

| Action | What it means |
|---|---|
| **Keep** | information useful to the task is held for the work at hand. |
| **Flag** | a sensitive point is raised — a contradiction, a doubtful figure, a clause that commits you. |
| **Send** | only the strict minimum goes to the AI; the rest of the dossier never leaves your perimeter. |
| **Ask** | when in doubt, the system puts the question back to you instead of deciding alone. |

The sorting depends on your request. A surface note and a commitment letter do not trigger the same filter: the first needs the floor area and the brief; the second needs every phrase that could bind you to be spotted.

### RAG, in plain terms

"RAG" is a technical term most people have never met. In plain terms it is simply this: **instead of giving everything to the AI, we first search your documents for the passages that answer the question, and send only those.**

Picture an assistant who, before answering, opens your binders, finds the two pages about your plot, and works from those pages — not the whole binder. That is RAG: *retrieve first, answer second, from your own sources.*

Two consequences for you:

- **less exposure** — the AI sees only the useful excerpt, not the whole dossier;
- **answers tied to your material** — each element can be traced back to its source, so it is checkable.

Finding the right passage is not proving it. A retrieved excerpt stays a *candidate*: it is marked, linked to its source, and you validate it. The filtering and document search are described here as method; for what is actually available, read [`docs/governance/STATUS.md`](docs/governance/STATUS.md).

## Six honest distinctions

The whole method fits in six lines:

```text
Fluent answer  ≠ safe answer.
Found source   ≠ proof.
Draft          ≠ deliverable.
Sent           ≠ true.
Repeated fact  ≠ memory.
Role agreement ≠ approval.
```

The tool proposes. The professional validates, rejects or asks for revision. Pantheon keeps the path between those two reviewable, and asks for a human decision when risk exceeds safe procedure.

## Cloud or local: your choice

Pantheon does not lock you into one engine. Use an external service such as ChatGPT, Claude or Gemini, with private names, addresses, client references or sensitive excerpts masked or minimized before anything leaves. Or run a local model on your own hardware for more containment, at the cost of maintenance and discipline.

Either way: the engine receives only the necessary context, Pantheon frames the method, and the professional validates.

## From your usual channels

Pantheon does not ask you to adopt a new interface. It sits behind the one you already use — a messaging app such as WhatsApp or Telegram, your email, or the OpenWebUI cockpit. You write where you are used to writing; the professional-conduct frame applies the same way everywhere.

And the distinction that matters: *answering is not acting*. The AI can draft an email, prepare a letter, propose a reply. But preparing is not sending. Sending stays a visible decision by the practitioner — or, if the practitioner explicitly decides so, a bounded and traced action, never a side effect.

```text
Answering ≠ acting.
Drafted   ≠ sent.
```

These channels and assisted sending are described here as method. For what is actually available today, read [`docs/governance/STATUS.md`](docs/governance/STATUS.md).

## See it on real dossiers

The examples are fictional and educational. They do not replace professional advice.

1. [`architecture_devis_reprise/`](docs/examples/architecture_devis_reprise/) — recovery quote and dangerous client validation.
2. [`architecture_legal_module_panel/`](docs/examples/architecture_legal_module_panel/) — future cockpit panel for architecture + legal domains, role readiness, blockers and skill eligibility.
3. [`regulatory_watch_conflict/`](docs/examples/regulatory_watch_conflict/) — new external rule versus active dossier assumptions.
4. [`evidence_topology/`](docs/examples/evidence_topology/) — topology examples for context, fan-out extraction, handoff and Evidence Pack structure.
5. [`understand_anything_structural_analysis/`](docs/examples/understand_anything_structural_analysis/) — external graph analysis framed as candidate evidence, not authority.
6. [`legal_note/`](docs/examples/legal_note/) — legal strategy note with source verification needs.
7. [`medical_letter/`](docs/examples/medical_letter/) — referral letter with minimized data exposure.

The point is not that Pantheon decides. The point is that the decision path stays reviewable.

<details>
<summary>Under the hood (vocabulary, roles, architecture)</summary>

### Three parts

| Element | Role in the dossier |
|---|---|
| **OpenWebUI (the screen)** | The visible place: ask, read, select documents, see sources, validate. |
| **Hermes Agent (the workshop)** | The preparation place: search, extract, compare, convert, draft, produce candidates. |
| **Pantheon Next (the method)** | The frame: what enters, the minimum necessary context, what leaves, what remains. |

The internal doctrine:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### The modules and how they relate

The diagram below shows the division of labor. Your tools carry the work end to end — OpenWebUI exposes the dossier, Hermes prepares and masks it, calls the AI engine (interchangeable) and produces candidates. Pantheon does not sit in the middle of that pipe: it attaches only where a decision is consequential — the rule on what may enter and leave, the gate on status and delivery, and what may remain in memory.

```mermaid
flowchart TB
    U([You · the practitioner])

    subgraph WORK["The work — your tools carry it, end to end"]
      direction LR
      OW["OpenWebUI · exposes<br/>dossier, statuses, decisions"]
      HX["Hermes · executes<br/>prepares, masks, drafts,<br/>calls the engine, produces candidates"]
      ENG[("AI engines · interchangeable<br/>ChatGPT · Claude · Gemini · local")]
      OW <--> HX
      HX <--> ENG
    end

    subgraph PAN["Pantheon · governs — attaches only at consequential decisions"]
      direction TB
      RULE["The rule<br/>what may enter · what is masked<br/>what an Evidence Pack must carry"]
      GATE{"Decision gate<br/>status · delivery · signature"}
      MEM["Scoped memory<br/>keeps only the validated"]
    end

    U -->|dossier + request| OW
    RULE -.->|bounds prep and transmission| HX
    HX -->|output candidate + Evidence Pack| GATE
    GATE -->|consequential? the question comes back| U
    GATE -->|validated| MEM
    MEM -.->|reusable, scoped| RULE
    GATE -->|status| OW
    OW -->|reviewable result| U
```

Most of the work never needs Pantheon; it attaches only when something could become a false truth, an unapproved external effect, a wrong memory or an unauthorized action. An output stays a *candidate* until you validate it; a retrieved excerpt is not proof; nothing enters memory without approval. For the full model, read [`docs/governance/CORE_CONCEPTS_MAP.md`](docs/governance/CORE_CONCEPTS_MAP.md) and [`docs/governance/MODULAR_DOMAIN_REORIENTATION.md`](docs/governance/MODULAR_DOMAIN_REORIENTATION.md).

### Seven review angles, one human decision

You do not need to memorize these names. They are internal review angles, not autonomous agents.

| Role | Plain-language function |
|---|---|
| ATHENA | Organizes the problem and prepares the plan. |
| ARGOS | Looks for sources and checks traceability. |
| THEMIS | Checks risk, rules and approval limits. |
| APOLLO | Reviews clarity, completeness and delivery quality. |
| ZEUS | Arbitrates status and next procedure when options conflict. |
| IRIS | Reformulates, clarifies and prepares user-facing communication. |
| HEPHAISTOS | Prepares files, correction candidates and implementation paths. |

These angles can expose useful disagreement before the professional validates anything. Hermes profiles may align with them, but they remain limited execution profiles: they do not approve, canonize or promote memory. See [`docs/governance/GOVERNANCE_COLLEGE.md`](docs/governance/GOVERNANCE_COLLEGE.md) and [`docs/governance/USER_DECISION_GATE.md`](docs/governance/USER_DECISION_GATE.md).

### Evidence topology

Pantheon does not choose between single-agent and multi-agent as a slogan. It first asks what shape the proof has.

If the answer depends on connecting evidence across sources, Pantheon preserves one primary reasoning context. If the work can be safely distributed, workers return Evidence Items or Handoff Artifacts, not authority.

See [`docs/governance/EVIDENCE_TOPOLOGY_GATE.md`](docs/governance/EVIDENCE_TOPOLOGY_GATE.md) and [`docs/governance/EVIDENCE_TOPOLOGY_CHECKLIST.md`](docs/governance/EVIDENCE_TOPOLOGY_CHECKLIST.md).

### Compartmentalized memory

Pantheon does not use one flat truth bucket.

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

### The vocabulary in plain language

| Object | Plain-language meaning |
|---|---|
| Task Contract | A mission sheet: what to do, with which documents, under which limits and with which expected output. |
| Context Pack | The minimum necessary context sent to a worker for a specific task. |
| Evidence Pack | A proof folder: sources used, assumptions, risks, contradictions, actions and review state. |
| Evidence Topology Gate | A topology check: one context, fan-out extraction, role-team handoff or bounded swarm, depending on the proof chain. |
| Memory Candidate | Something that may be useful later, but still needs review before being kept. |
| Canonical Memory | Validated memory, scoped and linked to evidence. |
| Pantheon Role | A review angle: plan, verify, check risk, improve wording, arbitrate or prepare a correction. |
| Knowledge Base | A document library. It helps find information, but it is not truth by itself. |
| Approval | A visible professional decision, not a hidden technical click. |

For the compact map of the full vocabulary, read [`docs/governance/CORE_CONCEPTS_MAP.md`](docs/governance/CORE_CONCEPTS_MAP.md).

### What Pantheon is not

Pantheon Next is not a chatbot, not an autonomous worker, not an automatic memory, and not a substitute for professional responsibility. It does not decide alone, does not approve its own outputs, and does not turn every answer into truth.

```text
Pantheon Next frames and controls execution.
It does not execute.
```

</details>

<details>
<summary>Developer view</summary>

### Repository status

This repository is governance-first. It contains Markdown doctrine, examples, templates and selected implementation artifacts. It is not an execution platform.

For current status, read:

- [`docs/governance/STATUS.md`](docs/governance/STATUS.md)
- [`docs/governance/AUTHORITY_INDEX.md`](docs/governance/AUTHORITY_INDEX.md)
- [`docs/governance/MODULES.md`](docs/governance/MODULES.md)

### Canonical read path

Start here:

1. [`docs/governance/STATUS.md`](docs/governance/STATUS.md)
2. [`docs/governance/MODULAR_DOMAIN_REORIENTATION.md`](docs/governance/MODULAR_DOMAIN_REORIENTATION.md)
3. [`docs/governance/CAPABILITY_PLACEMENT.md`](docs/governance/CAPABILITY_PLACEMENT.md)
4. [`docs/governance/DOMAIN_PACK_SPEC.md`](docs/governance/DOMAIN_PACK_SPEC.md)
5. [`docs/governance/AUTHORITY_INDEX.md`](docs/governance/AUTHORITY_INDEX.md)
6. [`docs/governance/MODULES.md`](docs/governance/MODULES.md)

### Core doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Abstract form:

```text
The exposure surface exposes.
The execution runtime executes.
Pantheon governs.
```

Pantheon governs consequential decisions: truth status, memory status, approval, evidence, scope and external action. Execution remains in the appropriate tools.

### Main governance areas

- [`docs/governance/APPROVALS.md`](docs/governance/APPROVALS.md)
- [`docs/governance/EVIDENCE_PACK.md`](docs/governance/EVIDENCE_PACK.md)
- [`docs/governance/MEMORY.md`](docs/governance/MEMORY.md)
- [`docs/governance/SCOPE_ISOLATION.md`](docs/governance/SCOPE_ISOLATION.md)
- [`docs/governance/TASK_CONTRACTS.md`](docs/governance/TASK_CONTRACTS.md)
- [`docs/governance/USER_DECISION_GATE.md`](docs/governance/USER_DECISION_GATE.md)

### Domain packs and examples

- [`docs/governance/DOMAIN_PACK_SPEC.md`](docs/governance/DOMAIN_PACK_SPEC.md)
- [`docs/governance/ARCHITECTURE_AGENCY_DOMAIN_PACK.md`](docs/governance/ARCHITECTURE_AGENCY_DOMAIN_PACK.md) — candidate / to verify
- [`docs/examples/`](docs/examples/)

### Boundaries

Pantheon Next must not become:

- an agent runtime;
- a tool runtime;
- a provider router;
- a scheduler;
- a queue;
- a hidden workflow runner;
- an automatic approval system;
- an automatic memory promotion engine.

```text
Governing is not implementing.
```

</details>
