# Pantheon Next

> Version française : [README.fr.md](README.fr.md)

> **Pantheon frames the dossier flow: what enters, what is sent to AI, what leaves, and what remains.**

<sub><strong>Current status:</strong> Pantheon Next is a method and documentation repository under active structuring. It is coherent, but partial. For authoritative implementation status, read <a href="docs/governance/STATUS.md">docs/governance/STATUS.md</a>.</sub>

Pantheon Next helps professionals use AI on serious dossiers without letting a fluent answer become an unsafe professional act.

The danger is not only that AI invents.

The danger is that AI can produce a clear, polite and convincing answer that turns too quickly an assumption into a decision, a source into proof, a draft into a deliverable, or a message into implicit approval.

Pantheon keeps the path visible: sources, doubts, contradictions, candidate outputs, human validation and scoped memory.

In one line:

```text
Enough context to work properly.
Not the whole dossier exposed unnecessarily.
Nothing leaves without status.
Nothing remains without validation.
```

<details>
<summary>Table of contents</summary>

- [Pantheon in 60 seconds](#pantheon-in-60-seconds)
- [What Pantheon frames](#what-pantheon-frames)
- [The risk: AI answers well, sometimes too well](#the-risk-ai-answers-well-sometimes-too-well)
- [Four fears, four responses](#four-fears-four-responses)
- [The email that commits too much](#the-email-that-commits-too-much)
- [When a rule changes, which dossiers are touched?](#when-a-rule-changes-which-dossiers-are-touched)
- [From raw AI to a controlled dossier](#from-raw-ai-to-a-controlled-dossier)
- [A source is not proof](#a-source-is-not-proof)
- [Useful disagreement, human decision](#useful-disagreement-human-decision)
- [A draft is not a deliverable](#a-draft-is-not-a-deliverable)
- [No memory without validation](#no-memory-without-validation)
- [Cloud or local: choose according to the dossier](#cloud-or-local-choose-according-to-the-dossier)
- [Worked dossiers: architect, lawyer, doctor](#worked-dossiers-architect-lawyer-doctor)
- [Seven review angles, one human decision](#seven-review-angles-one-human-decision)
- [Not another tool: a dossier method](#not-another-tool-a-dossier-method)
- [The vocabulary in plain language](#the-vocabulary-in-plain-language)
- [What Pantheon is not](#what-pantheon-is-not)
- [One formula](#one-formula)

</details>

## Pantheon in 60 seconds

Pantheon is a professional method around AI.

It does six things:

- frames the request before the AI acts;
- selects the minimum necessary context for the task;
- keeps sources, doubts and contradictions visible;
- marks outputs as candidates until reviewed;
- asks for human decision when risk exceeds safe procedure;
- prevents memory from becoming durable without scope and validation.

In plain language:

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

## What Pantheon frames

Pantheon frames the flows of the dossier.

It does not send the whole dossier to AI.

It prepares the minimum necessary context: enough to work correctly, not enough to expose everything unnecessarily.

```text
What enters must be admissible.
What is sent must be necessary.
What leaves must be conditioned.
What remains must be validated.
```

That creates four practical gates:

| Gate | Question |
|---|---|
| Entry | Which sources, documents or facts may enter the working perimeter? |
| Context | What is the smallest sufficient context for this task? |
| Output | What may be produced, under which status, and for which recipient? |
| Memory | What may remain, under which scope, with which proof and approval? |

A complete dossier is not automatically useful context.

A useful answer is not automatically a deliverable.

A repeated fact is not automatically memory.

## The risk: AI answers well, sometimes too well

A weak AI answer is easy to distrust.

A fluent AI answer is more dangerous.

It can sound right while hiding missing sources, unresolved contradictions, outdated assumptions or professional consequences.

Pantheon therefore treats AI output as a candidate until the dossier path is clear.

```text
Fluent ≠ safe.
Useful ≠ validated.
Fast ≠ ready to send.
```

## Four fears, four responses

| Professional fear | Pantheon response |
|---|---|
| Will my data leave uncontrolled? | Information can be minimized, masked or processed locally depending on dossier sensitivity. |
| Will AI invent things? | Sources, assumptions, contradictions and missing information remain visible. |
| Who decides? | AI proposes. The professional validates, rejects or asks for revision. |
| What remains afterward? | Only validated, scoped and contextualized information may become memory. |

## The email that commits too much

A common professional risk is not a bad answer.

It is a good-looking email that goes too far.

Example:

```text
Prepare an email to the client validating this recovery quote.
```

A generic AI may write a polite validation email.

Pantheon should instead ask:

```text
Does this email imply technical validation, acceptance, reception, scope approval or external commitment?
```

If the answer is uncertain, Pantheon opens a decision gate:

```text
Transmission blocked pending decision.
Options:
1. neutral clarification email;
2. internal note only;
3. wait for missing source;
4. prepare two variants for review.
```

See the first demo: [`docs/examples/architecture_devis_reprise/`](docs/examples/architecture_devis_reprise/).

## When a rule changes, which dossiers are touched?

Professionals also need to know when yesterday’s assumption becomes fragile.

A new regulation, case law item, official doctrine, technical standard or recommendation may affect active dossiers.

Pantheon should not rewrite those dossiers automatically.

It should create a watch alert:

```text
New source found.
Affected assumption suspected.
Applicability not confirmed.
Dossiers to review.
Human decision required before update or transmission.
```

Key distinction:

```text
New information ≠ applicable rule.
Watch alert ≠ dossier update.
Retrieved regulation ≠ evidence.
Impact suspected ≠ conclusion.
```

See the second demo: [`docs/examples/regulatory_watch_conflict/`](docs/examples/regulatory_watch_conflict/).

## From raw AI to a controlled dossier

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg" width="100%" alt="Before and after: raw AI output becomes a controlled professional dossier path">
  </a>
</p>

<p align="center"><strong>Before and after.</strong><br><em>Raw AI gives an answer. Pantheon turns the work into a visible dossier path: mission, sources, minimum context, proof, candidate output and validation.</em></p>

AI alone can answer quickly.

That is useful, but not enough for responsibility-bearing work.

Pantheon adds the missing dossier path:

```text
request
→ mission sheet
→ source and scope selection
→ minimum necessary context
→ candidate work
→ proof folder
→ review
→ human decision
→ optional scoped memory
```

## A source is not proof

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/port_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/port_01_fr.jpg" width="100%" alt="Controlled source port: external information enters only after filtering and status review">
  </a>
</p>

<p align="center"><strong>The source port.</strong><br><em>Web pages, files, emails and connectors may bring material. Pantheon marks what is found, what is usable, what is missing and what still needs review.</em></p>

The web, email, files, APIs, chat messages and Knowledge Bases can provide material.

Material is not proof.

Pantheon separates:

```text
Found source ≠ proof.
Retrieved document ≠ truth.
Searchable library ≠ memory.
Useful answer ≠ validation.
```

A source becomes useful only when its status is clear: where it comes from, what it supports, what it does not support, and whether it is still current.

## Useful disagreement, human decision

Pantheon does not become more rigorous by multiplying autonomous agents.

It separates responsibilities of judgment.

The Greek figures are **Pantheon Roles**: review angles and governance magistratures. They are not autonomous workers. Their value is that they can expose useful disagreement before the professional validates anything.

Examples:

- Apollo may make a message clear while Themis blocks transmission because risk remains too high.
- Argos may detect a source gap while Hephaistos can still prepare a draft artifact.
- Zeus may decide that the safe next procedure is not delivery, but a human decision gate.

```text
Smooth answer ≠ safe answer.
Produced artifact ≠ deliverable.
Retrieved source ≠ evidence.
Role agreement ≠ approval.
```

See [`docs/governance/GOVERNANCE_COLLEGE.md`](docs/governance/GOVERNANCE_COLLEGE.md) and [`docs/governance/USER_DECISION_GATE.md`](docs/governance/USER_DECISION_GATE.md).

## A draft is not a deliverable

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/livrables_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/livrables_01_fr.jpg" width="100%" alt="Candidate deliverables workshop: notes, tables, letters and reports remain candidates until validated">
  </a>
</p>

<p align="center"><strong>The deliverable workshop.</strong><br><em>Pantheon can help prepare notes, tables, letters and reports. They remain candidates until the review and approval path is complete.</em></p>

Pantheon helps produce useful material: a note, a table, a letter, a synthesis, a diagram, a report, a checklist or an export bundle.

But status matters.

```text
Draft ≠ deliverable.
Candidate deliverable ≠ validated output.
Validated output ≠ memory.
Sent ≠ true.
```

A deliverable remains candidate until the required review and approval path is complete.

## No memory without validation

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg" width="100%" alt="Compartmentalized memory: sources, context, evidence and approved memory remain separate">
  </a>
</p>

<p align="center"><strong>Compartmentalized memory.</strong><br><em>Pantheon does not keep one large truth bucket. Source, context, evidence, memory candidate and approved memory remain separate.</em></p>

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

A useful output stays candidate until review, evidence, scope and approval make retention legitimate.

## Cloud or local: choose according to the dossier

Pantheon does not force one model strategy.

A team can use external AI services such as ChatGPT, Claude or Gemini when the dossier allows it. In that case, Pantheon helps reduce exposure before anything leaves the controlled environment: private names, project addresses, client references, contract identifiers or sensitive excerpts can be masked, minimized or removed.

A team can also use a local model, for example on a GPU workstation, a dedicated local machine or a NAS isolated with Docker. This keeps more data inside the office infrastructure, but requires hardware, maintenance and operational discipline.

In both cases:

```text
The model receives only the necessary context.
Pantheon frames the method.
The professional validates.
```

## Worked dossiers: architect, lawyer, doctor

The examples are fictional and educational. They do not replace professional advice.

Recommended first reading path:

1. [`architecture_devis_reprise/`](docs/examples/architecture_devis_reprise/) — recovery quote and dangerous client validation.
2. [`regulatory_watch_conflict/`](docs/examples/regulatory_watch_conflict/) — new external rule versus active dossier assumptions.
3. [`legal_note/`](docs/examples/legal_note/) — legal strategy note with source verification needs.
4. [`medical_letter/`](docs/examples/medical_letter/) — referral letter with minimized data exposure.

The point is not that Pantheon decides.

The point is that Pantheon makes the decision path reviewable.

## Seven review angles, one human decision

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

Hermes profiles may align with these roles, but they remain limited execution profiles. They do not approve, canonize or promote memory.

## Not another tool: a dossier method

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg" width="100%" alt="Pantheon method around AI tools: screen, workshop and governance method remain separate">
  </a>
</p>

<p align="center"><strong>The method around the tools.</strong><br><em>OpenWebUI shows the work, Hermes prepares candidates, Pantheon frames what is allowed, reviewed, approved and remembered.</em></p>

For a non-technical reader, Pantheon Next has three parts:

| Element | Role in the dossier |
|---|---|
| **OpenWebUI (the screen)** | The visible place: ask, read, select documents, see sources, validate. |
| **Hermes Agent (the workshop)** | The preparation place: search, extract, compare, convert, draft, produce candidates. |
| **Pantheon Next (the method)** | The frame: what enters, the minimum necessary context, what leaves, what remains. |

A visible answer is not automatically true.

A finished task is not automatically approved.

A useful output is not automatically memory.

## The vocabulary in plain language

| Object | Plain-language meaning |
|---|---|
| Task Contract | A mission sheet: what to do, with which documents, under which limits and with which expected output. |
| Context Pack | The minimum necessary context sent to a worker for a specific task. |
| Evidence Pack | A proof folder: sources used, assumptions, risks, contradictions, actions and review state. |
| Memory Candidate | Something that may be useful later, but still needs review before being kept. |
| Canonical Memory | Validated memory, scoped and linked to evidence. |
| Pantheon Role | A review angle: plan, verify, check risk, improve wording, arbitrate or prepare a correction. |
| Knowledge Base | A document library. It helps find information, but it is not truth by itself. |
| Approval | A visible professional decision, not a hidden technical click. |

## What Pantheon is not

Pantheon Next is not a chatbot, not an autonomous AI worker, not an automatic memory, and not a substitute for professional responsibility.

It does not decide alone.

It does not approve its own outputs.

It does not turn every answer into truth.

```text
Pantheon Next frames and controls execution.
It does not execute.
```

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
docs/examples/       fictional professional examples
hermes/profiles/     lightweight candidate-only Hermes profile templates
docs/assets/         narrative and visual references
ai_logs/             AI-assisted intervention history
legacy/              historical Pantheon OS source material
schemas/             expected declarative contracts, not reconciled yet
operations/          expected read-only tooling, not implemented yet
tests/               tests expected, not implemented yet
```

Key entry points:

| Document | Purpose |
|---|---|
| [`docs/governance/STATUS.md`](docs/governance/STATUS.md) | Authoritative project status. |
| [`docs/governance/README.md`](docs/governance/README.md) | Governance index and read order. |
| [`docs/governance/EDITORIAL_LANGUAGE.md`](docs/governance/EDITORIAL_LANGUAGE.md) | Public-facing language and vocabulary guide. |
| [`docs/examples/README.md`](docs/examples/README.md) | Professional example index. |
| [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) | Canonical Pantheon Role registry. |
| [`docs/governance/GOVERNANCE_COLLEGE.md`](docs/governance/GOVERNANCE_COLLEGE.md) | Role separation, useful tensions and procedural arbitration. |
| [`docs/governance/USER_DECISION_GATE.md`](docs/governance/USER_DECISION_GATE.md) | Human decision escalation when discord exceeds safe arbitration. |
| [`docs/governance/TASK_CONTRACTS.md`](docs/governance/TASK_CONTRACTS.md) | Task framing doctrine. |
| [`docs/governance/EVIDENCE_PACK.md`](docs/governance/EVIDENCE_PACK.md) | Evidence doctrine. |
| [`docs/governance/MEMORY.md`](docs/governance/MEMORY.md) | Memory promotion doctrine. |
| [`docs/governance/APPROVALS.md`](docs/governance/APPROVALS.md) | Approval levels. |
| [`docs/governance/HERMES_INTEGRATION.md`](docs/governance/HERMES_INTEGRATION.md) | Hermes boundary doctrine. |
| [`docs/governance/OPENWEBUI_INTEGRATION.md`](docs/governance/OPENWEBUI_INTEGRATION.md) | OpenWebUI boundary doctrine. |
| [`docs/governance/KNOWLEDGE_TAXONOMY.md`](docs/governance/KNOWLEDGE_TAXONOMY.md) | Source, knowledge, context, evidence and memory vocabulary. |

When documents disagree, treat `STATUS.md` as the first status reference until reconciliation.

</details>

## One formula

```text
Pantheon frames the flow.
The AI receives only the necessary context.
Hermes prepares candidates.
OpenWebUI shows the result.
The human decides.
Only the validated remains.
```
