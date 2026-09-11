---
name: pantheon-activity-projection
description: "Project meaningful observable progress from non-trivial Pantheon-governed Hermes work into chat: initial plan, action/reason/goal, cited sources, methods, skills/tools actually used, result, limits and explicit handoff. Presentation only; never exposes hidden reasoning or creates governance state."
metadata:
  owner_layer: hermes
  status: candidate_template_only
  governed_by: docs/governance/CONVERSATION_ACTIVITY_PROJECTION.md
  trace_reference: docs/governance/ROLE_DIALOGUE_TRACE.md
  upstream: "Hermes chat/interim-message presentation convention; exact runtime delivery behavior must be observed before qualification"
---

# Pantheon activity projection

Lightweight presentation adapter for Hermes chat surfaces.

Use it only when work is non-trivial enough that progressive visibility helps the
user understand what is happening. It does not create a trace backend, workflow,
Role activation, Rite invocation, scheduler, queue, approval, Evidence, memory or
authorization.

```text
projection != persistence
visible role != activated role
handoff line != runtime dispatch
retrieved source != truth
runtime success != approval
summary rationale != hidden chain-of-thought
```

## Proportional use

Keep the surface quiet by default.

```text
simple direct request
-> no activity projection, or one compact line only when materially useful

non-trivial bounded task
-> initial plan + 2-4 meaningful milestones + final traceability summary

complex / professional task
-> initial plan + meaningful source/method/status changes + final summary
```

Do not publish every tool call, retrieval attempt, retry, token, internal branch
or unchanged status.

A milestone is useful when at least one user-relevant fact changes: source
coverage, applicable version, contradiction, material finding, method, visible
responsibility, blocker, approval posture, external-effect posture, result or
next action.

## Initial plan

For a non-trivial task, publish one compact plan before substantial execution.
Describe the intended path, not a guaranteed runtime transcript.

Prefer:

```text
[visible identity] · Plan
Objectif: ...
Étapes: ...
Sources attendues: ...        # only when already known
Méthode prévue: ...           # only when already selected/required
→ Premier relais: ...         # only when an actual next responsibility is known
```

If the observed task state later invalidates the plan, publish one short plan
adjustment rather than silently pretending the initial plan still applies.

## Milestone content

A meaningful milestone should answer, as compactly as possible:

```text
Action
= what observable work is being performed or has just completed

Reason
= the observable condition that makes the action relevant now

Goal
= the concrete result sought by this action

Result
= the observable outcome, finding, blocker or changed status
```

Add only the optional fields that materially help:

```text
Sources
Method
Skills
Tools
Limits / status
Handoff + handoff reason
```

Do not generate a private reasoning transcript. `Reason` is a concise observable
rationale such as "two document revisions exist" or "the amount is not supported
by an identified source".

## Visible identity

Use the identity already established by the governed task/context. This skill
must never activate a Role or invent a Rite merely to make the conversation look
structured.

Recommended compact labels follow the current conversation projection doctrine:

```text
🦉 Athena · Analyse / structuration
🔎 Argos · Sources / traçabilité
⚖ Themis · Risque / conformité
☀ Apollo · Clarté / synthèse
🛠 Hephaistos · Fabrication / production
📨 Iris · Transmission / adaptation
⚡ Zeus · Arbitrage / statut
🧠 Mnemosyne · Continuité / mémoire
⚙ Hermes · Exécution
```

Hermes is an execution runtime, not a Pantheon Role.

## Source citation

When a source materially supports or limits a milestone, assign stable references
for the current task and reuse them consistently:

```text
[S1] Document title
     Index/revision: C2
     Date: 2026-05-14
     Origin: IFJA_AFFAIRES
```

Include source metadata only when observed in the source or returned by the
qualified retrieval path. Useful metadata may include title, index/revision,
date, author, origin/location and exact page/section when available.

Never infer a missing date, index or version. Use `not identified` (localized to
the user's language) when the missing metadata is material; otherwise omit it.

```text
source returned != source verified
source name guessed from context != source citation
old source != current source
```

## Methods, skills and tools

Keep these categories distinct:

```text
Method
= governed or task method actually selected/applied, for example a material Rite
  or an explicit comparison/verification method

Skill
= Hermes skill actually used for the current task

Tool
= concrete runtime tool/connector/capability actually invoked or observed
```

Name a Rite or governed method only when it is actually selected/applied and
materially affects the work. Availability does not mean use.

List a skill or tool only when its use is observed in the current task context.
Do not claim Docling, Hindsight, MCP, Drive, a filesystem tool or another
mechanism merely because it would have been reasonable to use it.

Repeated low-level calls should be summarized rather than spammed, for example:

```text
Hindsight · documentary search — 7 queries, 2 retained sources
```

when those counts are actually observable.

## Handoff

When visible responsibility materially changes, end the milestone with a compact
handoff:

```text
→ Relais : Argos
Motif : qualifier la provenance et la version des pièces retrouvées.
```

A handoff line describes the next responsibility. It does not imply a new agent,
subagent, message bus or dispatch action.

If Hermes actually delegates runtime work, describe that separately as an
observable Hermes delegation; do not disguise runtime delegation as Pantheon
Role activation.

## Final traceability summary

For non-trivial projected work, end with a compact summary when it adds value:

```text
Plan / réalisation
✓ ...
✕ ...

Sources
[S1] ...
[S2] ...

Methods
- ...

Skills used
- ...

Tools used
- ...

Responsibility path
Athena -> Argos -> Hermes -> Themis -> Apollo

Result
...

Open
...
```

Include only categories that were materially present. Do not manufacture a
complete-looking path when some responsibilities were not involved.

## Transport behavior

When the active Hermes/channel surface supports safe interim assistant messages,
publish milestones progressively. When it does not, preserve the same structure
in a compact final response rather than adding a new transport mechanism.

Transport formatting may vary across Telegram, Discord, WhatsApp, WebUI or
another admitted surface. Governance meaning must not depend on color, message
editing or a platform-specific feature.

## Floquet acceptance example

A professional source-verification request such as verifying a Floquet budget
should make the following observable distinctions if the actual task state
supports them:

```text
🦉 Athena · Plan
Objectif: vérifier la justification du montant demandé.
→ Premier relais: Argos

🔎 Argos · Sources / traçabilité
Action: identifier la pièce financière pertinente.
Raison: le montant ne peut pas être retenu sans source identifiable.
But: déterminer le document, son indice et sa date.
Source: [S1] Budget estimatif C2 — indice C2 — date non identifiée
Résultat: document retrouvé; justification détaillée encore absente.
→ Relais: Hermes — poursuivre la recherche documentaire.

⚙ Hermes · Exécution
Skill: <only the skill actually used>
Tool: <only the tool actually invoked>
Résultat: <observed retrieval/runtime result>
```

The example is a presentation shape, not a claim about the real Floquet corpus.

## Final invariant

```text
Show what changed, why it matters, what was sought and what was observed.
Cite real sources with real metadata when available.
Name only methods, skills and tools actually selected or used.
Make responsibility changes explicit without inventing dispatch.
Never expose hidden reasoning and never turn presentation into authority.
```
