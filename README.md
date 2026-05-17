# Pantheon Next

> Version française : [README.fr.md](README.fr.md)

> **AI opens possibilities. Pantheon organizes them. The human decides. Only the validated remains.**

<sub><strong>Current status:</strong> Pantheon Next is a method and documentation repository under active structuring. It is coherent, but partial. For authoritative implementation status, read <a href="docs/governance/STATUS.md">docs/governance/STATUS.md</a>.</sub>

Pantheon Next helps professionals use AI on serious dossiers without losing control of sources, assumptions, evidence, deliverables, memory and validation.

For liberal professions and responsibility-bearing work, Pantheon can be understood as an **AI ethics and working-method register**. Before an AI receives a request and produces an answer, Pantheon frames the method: which information may be used, what must be checked, what needs evidence, what requires approval and what may be kept.

It is not another AI tool. It is a professional method for keeping AI work framed, traceable and reviewable.

<details>
<summary>Table of contents</summary>

- [Pantheon Next in 1 minute](#pantheon-next-in-1-minute)
- [The four professional fears Pantheon addresses](#the-four-professional-fears-pantheon-addresses)
- [From raw AI to a controlled dossier](#from-raw-ai-to-a-controlled-dossier)
- [Who does what?](#who-does-what)
- [Governance college and decision gates](#governance-college-and-decision-gates)
- [Where does the AI model run?](#where-does-the-ai-model-run)
- [The professional path](#the-professional-path)
- [Concrete examples: lawyer and general practitioner](#concrete-examples-lawyer-and-general-practitioner)
- [Who is it for?](#who-is-it-for)
- [Key working objects](#key-working-objects)
- [Pantheon roles](#pantheon-roles)
- [What next?](#what-next)

</details>

## Pantheon Next in 1 minute

- **Frames the request** before the AI acts — mission, sources and limits are set first.
- **Keeps proof visible** — sources, assumptions, contradictions and missing information remain on display.
- **Leaves the decision to the professional** — the AI proposes, the human approves or rejects.
- **Compartmentalizes memory** — nothing becomes durable without review, scope and approval.
- **Works with ChatGPT, Claude, Gemini or a local model** — the method adapts to the sensitivity of the dossier.

In the public-facing explanation, the three parts are simple:

```text
The screen shows.
The workshop prepares.
Pantheon frames the method.
The human decides.
```

The internal doctrine remains:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## The four professional fears Pantheon addresses

| Professional fear | Pantheon response |
|---|---|
| Will my data leave uncontrolled? | Information can be minimized, obfuscated or processed locally depending on sensitivity. |
| Will AI invent things? | Sources, assumptions, contradictions and missing information remain visible. |
| Who decides? | AI proposes. The professional validates. |
| What remains afterward? | Only validated, scoped and contextualized information may become memory. |

## From raw AI to a controlled dossier

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg" width="100%" alt="Pantheon RPG before and after controlled dossier">
  </a>
</p>

AI alone can answer quickly. That is useful, but not enough for responsibility-bearing work.

Pantheon frames the request, separates sources from evidence, keeps uncertainty visible, preserves contradictions and leaves validation to the professional.

```text
Use AI faster without losing the dossier method.
```

## Who does what?

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg" width="100%" alt="Pantheon RPG who does what board">
  </a>
</p>

For a non-technical reader, Pantheon Next is easier to understand as three parts:

| Simple view | Technical name | What it means |
|---|---|---|
| **The screen** | OpenWebUI | The local open-source AI chat application where the professional asks, reads, selects documents, sees sources and validates. |
| **The workshop** | Hermes Agent | The worker that can search, extract, compare, convert, draft and prepare candidate outputs under a limited mission. |
| **The method** | Pantheon Next | The rules of work: what can be used, what must be checked, what needs evidence, what needs approval and what may be kept. |

A visible answer is not automatically true. A finished task is not automatically approved. A useful output is not automatically memory.

## Governance college and decision gates

Pantheon does not try to be more rigorous by multiplying autonomous agents.

It separates responsibilities of judgment.

The Greek figures are **Pantheon Roles**: review angles and governance magistratures. They are not autonomous workers. Their value is that they can expose useful disagreement before the professional validates anything.

```text
AI opens possibilities.
Roles organize tensions.
Evidence constrains.
Zeus arbitrates status and procedure.
The human decides.
Only the validated remains.
```

A role has value only if it can reveal, preserve or escalate a useful tension. For example, Apollo may make a message clear while Themis blocks transmission because the risk is too high; Argos may find a source gap while Hephaistos can still prepare a draft artifact; Zeus may decide that the safe next procedure is not delivery, but a human decision gate.

When disagreement is too strong, Pantheon must not hide it behind a smooth answer. It exposes the discord, presents bounded options and asks the user to decide.

```text
Smooth answer ≠ safe answer.
Produced artifact ≠ deliverable.
Retrieved source ≠ evidence.
Role agreement ≠ approval.
```

See [`docs/governance/GOVERNANCE_COLLEGE.md`](docs/governance/GOVERNANCE_COLLEGE.md) and [`docs/governance/USER_DECISION_GATE.md`](docs/governance/USER_DECISION_GATE.md).

## Where does the AI model run?

Pantheon does not force one model strategy.

A team can use external AI services such as ChatGPT, Claude or Gemini when the dossier allows it. In that case, Pantheon helps reduce exposure before anything leaves the controlled environment: private names, project addresses, client references, contract identifiers and sensitive excerpts can be replaced, minimized or obfuscated. The answer that comes back remains a candidate.

A team can also use a local model. In that case, the model runs in a controlled environment: for example on a workstation with a **GPU** (dedicated graphics card), on a dedicated local machine, or on a **NAS** (office file server) isolated with **Docker** (software container). This keeps more data inside the office infrastructure, but requires hardware, maintenance and operational discipline.

In both cases, the rule is the same:

```text
The model proposes.
Pantheon frames the method.
The professional validates.
```

## The professional path

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg" width="100%" alt="Pantheon RPG player journey from request to deliverable">
  </a>
</p>

The player is the professional user. They bring the question, the dossier, the constraints, the expertise and the final judgment.

Pantheon turns a vague AI request into a controlled professional path:

```text
User request
→ mission sheet
→ source intake
→ scope and context selection
→ work strategy
→ external execution
→ proof folder
→ candidate deliverable
→ human review
→ approved output, rejected output or memory proposal
→ validated memory only after approval
```

AI may do more work between validation gates, but it must not cross those gates silently.

## Concrete examples: lawyer and general practitioner

Two professional scenarios that show the difference between a raw AI answer and a Pantheon-framed deliverable.

### Law firm — preparing a case management hearing

> **Request**: "From opposing counsel's 52-page brief, the disputed contract and my 8 exhibits, prepare a strategy note for the case management hearing."

**Without Pantheon.** The AI produces 4 well-written pages. They may include nonexistent case law — already documented before French courts — mix exhibits and smooth over contradictions. Professional secrecy may be breached if party names leave for a public service.

**With Pantheon.**

- **Mission sheet** — scope: this case only. Allowed sources: the 10 exhibits in the file. Case law: to be verified on Légifrance before citation. Expected output: a 3-page strategy note.
- **Minimization before external transmission** — party names, docket numbers and client identifiers replaced with neutral tags.
- **Proof folder** — 6 arguments identified (with exhibit number and page), 2 contradictions between the adverse brief and exhibit P-3, 3 hypotheses to confirm, 1 case-law reference flagged "to verify".
- **Candidate deliverable** — 3-page note, 11 sourced citations, contradictions highlighted.
- **Validation** — the lawyer decides, signs and files. Nothing is memorized until they decide.

<details>
<summary>Sample — mission sheet (Task Contract)</summary>

```text
Mission        : Strategy note — case management hearing
Scope          : Case [DOCKET-MASKED], firm [ID-MASKED]
Allowed        : P-01 to P-08 (client exhibits)
                 Adverse brief (PDF, 52 p.)
                 Disputed contract dated [DATE-MASKED]
                 Légifrance (case-law verification only)
Forbidden      : other firm cases, internal HR base
Output         : 3-page note — arguments, contradictions, hypotheses
Ceiling        : internal transmission only; no external send without lawyer sign-off
Memory         : nothing enters firm memory without signature
```

</details>

<details>
<summary>Sample — candidate deliverable (strategy note)</summary>

```text
## Arguments identified

1. Contractual non-performance (French Civil Code art. 1217)
   Source       : exhibit P-03, p. 4 (formal notice of [DATE])
   Reinforced   : exhibit P-05 (email exchange of [DATE])
   Status       : to confirm — proof of receipt missing

2. Contradiction adverse brief / exhibit P-03
   Adverse §17 : alleged delivery on [DATE]
   Exhibit P-03 : delivery slip signed [DATE + 15 d]
   Status       : key exhibit for the hearing

3. Cass. com., [DATE], no. [REF]
   Status       : TO VERIFY on Légifrance before oral citation
```

`[MASKED]` placeholders are re-identified locally after review; they never leave the firm in nominal form.

</details>

### General practitioner — referral letter to a cardiologist

> **Request**: "Prepare a referral letter to the cardiologist from my consultation notes and the latest lab results."

**Without Pantheon.** Strong temptation to paste the identifying consultation note into a public AI. Potential breach of medical secrecy (French Public Health Code art. R.4127-4) and GDPR if the AI is not hosted under health-data certification.

**With Pantheon.**

- **Mission sheet** — scope: this patient, this referral. Sources: consultation note, labs, ECG. Expected output: a 1-page referral letter. External AI allowed only on a pseudonymized version.
- **Pseudonymization first** — name, date of birth, national health ID, address replaced before any send.
- **Proof folder** — 4 clinical elements cited (blood pressure, heart rate, history, current treatment), 2 lab results attached, 1 explicit question to the specialist.
- **Candidate deliverable** — 1-page letter, identifiers re-injected locally after review.
- **Validation** — the doctor signs and files in the patient record. Identifying data never left the practice.

<details>
<summary>Sample — mission sheet (Task Contract)</summary>

```text
Mission        : Referral letter — cardiology
Scope          : Patient [PSEUDO-A7], consultation of [DATE-MASKED]
Allowed        : today's consultation note (pseudonymized)
                 labs of [DATE] (numeric values only)
                 ECG of [DATE]
                 relevant history (hypertension, current treatment)
Forbidden      : other patient records, unrelated history
Output         : 1-page referral letter — clinical tone, explicit question
Ceiling        : local re-identification only; send after signature
Memory         : filed in the patient record; no durable AI memory
```

</details>

<details>
<summary>Sample — candidate deliverable (referral letter)</summary>

```text
Dear colleague,

I am referring my patient [PSEUDO-A7], 58 years old, hypertensive
treated with [current-treatment], for a cardiology opinion.

Reason: intermittent palpitations onset 3 weeks ago, no syncope,
no chest pain.

Today's clinical findings:
  - BP   : 142/88 mmHg
  - HR   : 92/min, irregular on auscultation
  - ECG  : ventricular extrasystoles (tracing attached)

Labs of [DATE]:
  - potassium 3.9 mmol/L
  - TSH normal
  - troponin not measured

Question: diagnostic confirmation and indication for a 24h Holter?

Kind regards,
Dr [NAME-MASKED]
```

The version sent to external AI remains pseudonymized; identifiers (`[PSEUDO-A7]`, `[NAME-MASKED]`, dates) are re-injected on the doctor's workstation before signature.

</details>

In both cases, the message is the same: **AI accelerates, Pantheon frames, the professional validates.**

## Who is it for?

| Profession | Typical use case |
|---|---|
| Architect, project manager, owner assistant | Review a technical dossier, compare quotes, specifications, exchanges and risks before decision. |
| Lawyer or legal counsel | Prepare a sourced note, identify obligations, contradictions and points to verify. |
| Notary | Structure dossier documents, isolate missing information and trace assumptions. |
| Accountant or consultant | Produce a usable synthesis from documents, spreadsheets and client exchanges. |
| Doctor or healthcare professional | Organize a documentary analysis without confusing hypothesis, source and clinical decision. |
| DPO, judicial expert, executive | Keep track of sources, validations, limits and responsibilities in AI-assisted work. |

The common point: use AI without abandoning method, confidentiality and professional responsibility.

## Sources are not proof

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/port_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/port_01_fr.jpg" width="100%" alt="Pantheon RPG controlled source port">
  </a>
</p>

The port represents external flows: web, email, files, APIs, messengers, local folders and connectors.

Pantheon defines what may enter the dossier, what remains temporary, what must be rejected and what may become evidence.

```text
Found source ≠ proof.
Retrieved document ≠ truth.
Document library ≠ memory.
Useful answer ≠ validation.
```

## Evidence before trust

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/evidence_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/evidence_01_fr.jpg" width="100%" alt="Pantheon RPG evidence workshop">
  </a>
</p>

A professional dossier needs more than citations. It needs reviewable support.

Pantheon keeps visible:

| Element | Why it matters |
|---|---|
| Sources used | The user can check where the answer comes from. |
| Assumptions | The system does not hide what is still assumed. |
| Contradictions | Conflicts remain visible instead of being smoothed away. |
| Missing information | The system can stop and request what is needed. |
| Evidence state | A source becomes evidence only through review. |
| Approval state | The professional decides what can be used, transmitted or retained. |

Evidence supports review. Evidence does not approve itself.

## From candidate output to professional deliverable

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/livrables_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/livrables_01_fr.jpg" width="100%" alt="Pantheon RPG deliverables production workshop">
  </a>
</p>

Pantheon is not only about answering a question. The goal is to produce something useful: a note, a table, a letter, a synthesis, a diagram, a report, a checklist or an export bundle.

A deliverable remains candidate until the required review and approval path is complete.

```text
Draft ≠ deliverable.
Candidate deliverable ≠ validated output.
Validated output ≠ memory.
```

## Memory stays compartmentalized

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg" width="100%" alt="Pantheon RPG compartmentalized memory">
  </a>
</p>

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

Memory does not promote itself. A useful output remains candidate until review, evidence, scope and approval make retention legitimate.

## The controlled dossier city

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/citadel_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/citadel_01_fr.jpg" width="100%" alt="Pantheon RPG citadel">
  </a>
</p>

The citadel represents the professional dossier under control.

Sources pass through controlled gates. Assumptions remain visible. Sessions, versions, evidence and memory stay scoped. The professional decides what remains.

## A method around AI tools

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg" width="100%" alt="Pantheon RPG system summary">
  </a>
</p>

Pantheon does not replace the screen or the workshop. It makes their configuration, outputs, evidence discipline, validation thresholds and decision memory reviewable.

That is the difference between powerful AI tooling and a professional working method.

## The outside world remains open

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg" width="100%" alt="Pantheon RPG world map AI and Internet">
  </a>
</p>

AI, the web and external knowledge form rich but unstable worlds. Useful knowledge, weak sources, obsolete information, contradictions and unexpected discoveries coexist.

Pantheon does not close that world. It gives the professional a method to cross it without confusing signal, source, evidence and memory.

## What Pantheon is not

Pantheon Next is not a chatbot, not an autonomous AI worker, not an automatic memory, and not a substitute for professional responsibility.

It does not decide alone. It does not approve its own outputs. It does not turn every answer into truth.

The technical boundary is:

```text
Pantheon Next frames and controls execution.
It does not execute.
```

## Key working objects

| Object | Plain-language meaning |
|---|---|
| Task Contract | A mission sheet: what to do, with which documents, under which limits and with which expected output. |
| Evidence Pack | A proof folder: sources used, assumptions, risks, contradictions, actions and review state. |
| Memory Candidate | Something that may be useful later, but still needs review before being kept. |
| Canonical Memory | Validated memory, scoped and linked to evidence. |
| Context Pack | The minimum useful context sent to a worker for a specific task. |
| Pantheon Role | A review angle: plan, verify, check risk, improve wording, arbitrate or prepare a correction. |
| Knowledge Base | A document library. It helps find information, but it is not truth by itself. |
| Approval | A visible professional decision, not a technical click hidden in the system. |

## Pantheon roles

You do not need to memorize these names. They are seven internal review angles; the professional sees them as review modes, not autonomous agents.

The file [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) keeps its historical name, but the canonical concept is **Pantheon Role**.

| Role | Plain-language function |
|---|---|
| ATHENA | Organizes the problem and prepares the plan. |
| ARGOS | Looks for sources and checks traceability. |
| THEMIS | Checks risk, rules and approval limits. |
| APOLLO | Reviews clarity, completeness and delivery quality. |
| ZEUS | Arbitrates when several options conflict. |
| IRIS | Reformulates, clarifies and prepares user-facing communication. |
| HEPHAISTOS | Prepares technical files, proposed corrections and implementation paths. |

Hermes profiles may align with these roles, but they remain limited execution profiles. They do not approve, canonize or promote memory.

<details>
<summary>Project status and structure</summary>

Pantheon Next currently provides a documentation-level governance baseline.

Implemented or documented:

- governance doctrine;
- runtime boundary doctrine;
- Pantheon Role registry;
- Governance College doctrine;
- User Decision Gate doctrine;
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

Not implemented in this project:

- autonomous runtime;
- OpenWebUI runtime integration;
- Hermes runtime integration;
- automatic Evidence Pack generation;
- Memory Candidate review UI;
- AI provider routing;
- free plugin manager;
- schema reconciliation;
- tests;
- read-only operations tooling;
- deployment stack.

Structure:

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
| [`docs/governance/STATUS.md`](docs/governance/STATUS.md) | Authoritative project status. |
| [`docs/governance/README.md`](docs/governance/README.md) | Governance index and read order. |
| [`docs/governance/ARCHITECTURE.md`](docs/governance/ARCHITECTURE.md) | Governance anatomy and boundary model. |
| [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) | Canonical Pantheon Role registry. |
| [`docs/governance/GOVERNANCE_COLLEGE.md`](docs/governance/GOVERNANCE_COLLEGE.md) | Role separation, useful tensions and procedural arbitration. |
| [`docs/governance/USER_DECISION_GATE.md`](docs/governance/USER_DECISION_GATE.md) | Human decision escalation when discord exceeds safe arbitration. |
| [`docs/governance/TASK_CONTRACTS.md`](docs/governance/TASK_CONTRACTS.md) | Task framing doctrine. |
| [`docs/governance/EVIDENCE_PACK.md`](docs/governance/EVIDENCE_PACK.md) | Evidence doctrine. |
| [`docs/governance/MEMORY.md`](docs/governance/MEMORY.md) | Memory promotion doctrine. |
| [`docs/governance/APPROVALS.md`](docs/governance/APPROVALS.md) | Approval levels. |
| [`docs/governance/HERMES_INTEGRATION.md`](docs/governance/HERMES_INTEGRATION.md) | Hermes boundary doctrine. |
| [`docs/governance/OPENWEBUI_INTEGRATION.md`](docs/governance/OPENWEBUI_INTEGRATION.md) | OpenWebUI boundary doctrine. |
| [`docs/governance/EXTERNAL_TOOLS_POLICY.md`](docs/governance/EXTERNAL_TOOLS_POLICY.md) | External capability governance. |
| [`docs/governance/KNOWLEDGE_TAXONOMY.md`](docs/governance/KNOWLEDGE_TAXONOMY.md) | Source, knowledge, context, evidence and memory vocabulary. |

When documents disagree, treat `STATUS.md` as the first status reference until reconciliation.

</details>

## What next?

### For the professional reader

- **Test the doctrine on a real case** — mentally re-read a recent dossier and ask: what could I have framed as a mission sheet? What should have remained a candidate? What should never have become memory?
- **Follow the project** — Watch this repository on GitHub to track the evolution of the method and documented use cases.
- **Propose a professional case** — open an issue with an anonymized real case so it can be studied and added to the public examples.
- **Go deeper into the doctrine** — read [`docs/governance/STATUS.md`](docs/governance/STATUS.md) for the authoritative status, then [`docs/governance/README.md`](docs/governance/README.md) for the reading order.

### For contributors and the project team

- build a complete fictional demo dossier;
- provide a full sample Task Contract and Evidence Pack;
- document the first professional use-case packs by profession;
- prepare OpenWebUI ↔ Hermes handoff examples.

## Final principle

```text
AI produces possibilities.
Pantheon frames the path.
Hermes prepares the work.
OpenWebUI shows the result.
The human decides.
Only the validated remains.
```
