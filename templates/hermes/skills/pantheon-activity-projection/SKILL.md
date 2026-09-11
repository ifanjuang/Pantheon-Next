---
name: pantheon-activity-projection
description: "Project meaningful observable progress from non-trivial Pantheon-governed Hermes work into chat: plan, action/reason/goal, real sources and metadata, methods, skills/tools actually used, result, limits and explicit responsibility handoff. Presentation only."
metadata:
  owner_layer: hermes
  status: candidate_template_only
  governed_by: docs/governance/CONVERSATION_ACTIVITY_PROJECTION.md
  trace_reference: docs/governance/ROLE_DIALOGUE_TRACE.md
  upstream: "Hermes chat/interim-message presentation convention; exact runtime delivery behavior must be observed before qualification"
---

# Pantheon activity projection

Lightweight presentation adapter for non-trivial governed chat work.

```text
projection != persistence
visible role != activated role
handoff line != runtime dispatch
retrieved source != truth
runtime success != approval
summary rationale != hidden chain-of-thought
```

## When to use it

Keep simple requests quiet. For a bounded non-trivial task, normally show one
initial plan, 2-4 meaningful milestones, then a compact final summary. Show more
only when a new material finding, source, contradiction, blocker, responsibility,
approval posture or result actually changes the user's understanding.

Do not publish every tool call, retrieval attempt, retry, token, internal branch
or unchanged runtime state.

## Initial plan

Before substantial execution, show the intended path without pretending it is a
guaranteed runtime transcript.

```text
[visible identity] · Plan
Objectif: ...
Étapes: ...
Sources attendues: ...        # only when already known
Méthode prévue: ...           # only when already selected/required
→ Premier relais: ...         # only when the next responsibility is established
```

If new evidence materially invalidates the plan, show one short adjustment.

## Milestone grammar

Use the smallest useful subset of:

```text
[visible identity] · [semantic function]
Action: observable work performed or completed
Raison: observable condition making it relevant now
But: concrete result sought
Sources: [S1], [S2] ...       # when material
Méthode: ...                  # only when actually selected/applied
Skill: ...                    # only when actually used
Outil: ...                    # only when actually invoked/observed
Résultat: finding, blocker or changed status
Limite: ...                   # when material
→ Relais: next responsibility — reason
```

`Raison` is a concise observable rationale, not private reasoning. Never output a
scratchpad, hidden chain-of-thought, token-level alternatives or invented debate.

## Identity and handoff

Use only a visible identity already established by the governed task/context.
Do not activate a Role or invent a Rite to make the display look structured.

Current compact labels:

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

Hermes is a runtime, not a Pantheon Role.

A `→ Relais` line means the next responsibility, not a new agent or dispatch. If
Hermes actually delegates runtime work, report that separately as an observed
Hermes delegation.

## Source citation

When a source materially supports or limits a milestone, assign stable task-local
references and reuse them consistently.

```text
[S1] <observed title>
     Indice/révision: <observed value or non identifié>
     Date: <observed value or non identifiée>
     Origine: <observed repository/vault/location>
     Page/section: <observed locator when useful>
```

Include metadata only when it is present in the source or returned by the
qualified retrieval path. Never infer a missing title, date, index, revision,
author or version from context.

```text
source returned != source verified
source name guessed from context != source citation
old source != current source
```

## Method, skill and tool

Keep the categories distinct:

```text
Méthode = governed/task method actually selected and applied
Skill   = Hermes skill actually used in the current task
Outil   = runtime tool, connector or capability actually invoked or observed
```

Availability does not mean use. Do not claim Docling, Hindsight, MCP, Drive,
filesystem access or another mechanism merely because it would have been useful.
Repeated low-level calls may be collapsed into one factual summary only when the
count/result is observable.

## Progressive delivery

When the active Hermes/channel surface supports safe interim assistant messages,
publish meaningful milestones progressively. Otherwise preserve the same
structure in a compact final response; do not introduce a second transport
mechanism solely for progress display.

Transport-specific formatting may vary across Telegram, Discord, WhatsApp,
WebUI or another admitted surface. Governance meaning must not depend on message
editing, color or another channel-specific feature.

## Final summary

When useful, close non-trivial work with only the categories actually present:

```text
Plan / réalisation
✓ ...
✕ ...

Sources
[S1] ...
[S2] ...

Méthodes
- ...

Skills utilisés
- ...

Outils utilisés
- ...

Parcours responsabilité / exécution
Athena -> Argos -> Hermes -> Themis

Résultat
...

Ouvert
...
```

Do not manufacture a complete-looking path, source set, method or tool list.

## Floquet acceptance shape

For a real Floquet source-verification test, use only corpus facts actually
retrieved during that run:

```text
🦉 Athena · Plan
Objectif: vérifier l'affirmation demandée à partir des pièces applicables.
→ Premier relais: Argos

🔎 Argos · Sources / traçabilité
Action: identifier la pièce pertinente.
Raison: l'affirmation nécessite une source identifiable.
But: déterminer le document applicable, son indice et sa date.
Source: [S1] <document réel> — <indice observé> — <date observée/non identifiée>
Résultat: <constat réellement supporté>.
→ Relais: Hermes — <action d'exécution réellement nécessaire>.

⚙ Hermes · Exécution
Skill: <skill réellement utilisé>
Outil: <outil réellement invoqué>
Résultat: <résultat runtime observé>
```

This is a presentation shape, not a claim about the real Floquet corpus.

## Final invariant

```text
Show what changed, why it matters, what was sought and what was observed.
Cite only real sources and observed metadata.
Name only methods, skills and tools actually selected or used.
Make responsibility changes explicit without inventing dispatch.
Never expose hidden reasoning and never turn presentation into authority.
```
