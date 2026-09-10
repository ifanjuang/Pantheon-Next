# Conversation Activity Projection

Status: candidate support doctrine — compact conversation projection of observable governed work. Repository state: documented non-implemented.
Boundary profile: candidate_support_note.

## Objective

Expose meaningful progress from Pantheon-governed Hermes work in chat surfaces without turning the chat into a technical log and without exposing hidden chain-of-thought.

The user-facing grammar stays compact but must expose both the symbolic Pantheon identity and its plain semantic meaning.

```text
[icon] [name] · [semantic label] — [brief observable rationale]
```

Examples:

```text
🦉 Athena · Analyse / structuration — Le C2 est plus ancien que le DCE. Je vérifie si son estimation reste cohérente avec le périmètre actuel.

⚙ Hermes · Exécution — C2 et CCTP retrouvés. Je poursuis sur les dernières pièces identifiées.

⚖ Themis · Risque / conformité — Cette réponse engage une information financière : validation humaine nécessaire.
```

The same dual-label rule applies when a Rite or governed Space becomes materially relevant to the visible progression.

```text
🔁 Concordance des Sources · Rite de vérification — Les pièces financières ne portent pas toutes le même périmètre. Je compare leur date, leur portée et leurs contradictions avant de conclure.

🏛 Agora · Espace de délibération — Deux lectures restent défendables. La divergence est rendue visible pour décision plutôt que lissée automatiquement.
```

This is a projection of observable work, not a new reasoning system, workflow engine, role system, Rite system, Space system or authority layer.

## Existing authority reused

This projection reuses rather than duplicates:

- `ROLE_DIALOGUE_TRACE.md` for observable role moves and safe rationale summaries;
- `GOVERNANCE_COLLEGE.md` for Pantheon Role jurisdictions and plain-language responsibilities;
- `docs/governance/rites/README.md` and the Rite catalogue for governed methods;
- `EVOLUTION_OF_ROLES_RITES_AND_SPACES.md` for the distinction between Roles, Rites, governed Spaces and presentation structures;
- Task Contracts for intent, owner role, scope, constraints and evidence expectations;
- Role Signals for declared role-to-role governance signals;
- Workflow Manifests for governed phases and entry/exit conditions;
- Hermes integration/runtime contracts for external execution boundaries;
- `HERMES_PROGRESS_ERROR_RETRY_UX.md` for measurable runtime progress, errors and retries when Hermes exposes them.

A conversation activity line does not replace any of those objects and is not itself Evidence, approval, memory or authorization.

## Semantic identity rule

The mythological or symbolic name must never be the only explanation presented to the user when the semantic function is known.

```text
Athena
!= sufficient user explanation

Athena · Analyse / structuration
= preferred compact display
```

The presentation label explains the current responsibility without redefining the underlying object.

```text
symbolic name != semantic authority
presentation label != new Role
presentation label != new Rite
presentation label != new governed Space
```

Owner documents remain authoritative for identity, jurisdiction, lifecycle and status. The projection may shorten a semantic label for readability but must not invent a new responsibility.

### Roles

Recommended compact presentation derived from the current Governance College:

```text
🦉 Athena · Analyse / structuration
🔎 Argos · Sources / traçabilité
⚖ Themis · Risque / conformité
☀ Apollo · Clarté / synthèse
🛠 Hephaistos · Fabrication / production
📨 Iris · Transmission / adaptation
⚡ Zeus · Arbitrage / statut
🧠 Mnemosyne · Continuité / mémoire
```

Hermes remains distinct because it is an external execution runtime, not a Pantheon Role:

```text
⚙ Hermes · Exécution
```

Adapters may expose other bounded runtime or boundary identities only when their underlying status is already defined elsewhere. A presentation label must not promote an adapter into a Pantheon Role.

### Rites

A Rite is a governed method, not an actor. When a Rite materially affects the current progression, display its governed name plus a short method label.

Examples:

```text
🔁 Divergence Contrôlée · Rite d'exploration
🔁 Autocritique Contradictoire · Rite de critique
🔁 Concordance des Sources · Rite de vérification
🔁 Prémisses Cachées · Rite d'explicitation
🔁 Refondation de Session · Rite de recadrage
```

The label is explanatory only. Rite lifecycle, authorization, closure and retained outputs remain owned by the Rite doctrine.

```text
rite visible != rite authorized
rite selected != rite running
rite completed != output approved
```

A Rite should appear in chat only when its invocation, result, tension or closure materially helps the user understand why the work changed direction.

### Governed Spaces

A governed Space is a durable distinction between kinds of activity. When a Space materially explains where an activity or deliberation belongs, display its governed name plus its semantic purpose.

Examples based on current doctrine:

```text
🏛 Agora · Espace de délibération
📁 Project Space · Espace projet
📚 Governance Reference Space · Référentiel de gouvernance
```

The exact visible label should follow the active Cockpit/navigation owner when a localized product label already exists.

```text
space visible != space owns object
space displays status != space owns status
new screen != new governed Space
```

Scenes, Decks and Constellations remain presentation structures and must not be presented as governed Spaces merely because they are visible.

## Runtime separation

```text
Pantheon constrains legitimacy and status.
Hermes performs admitted runtime work outside Pantheon.
Observable runtime/governance events may be projected into a conversation.
The channel renders the projection.
The human remains the decision authority at applicable gates.
```

Therefore:

```text
conversation line != chain-of-thought
conversation line != Evidence
conversation line != approval
role badge != autonomous authority
rite badge != runtime execution
space badge != persistence authority
Hermes success != Pantheon validation
channel delivery != action authorization
```

## Minimal projection

Do not create a parallel canonical event model merely for chat.

When a compatible `trace_event` exists, the conversation renderer should consume only the fields needed for display and resolve labels from existing owner doctrine or presentation registries.

```yaml
conversation_projection:
  trace_event_ref: trace-123
  visible_identity:
    kind: role
    id: ATHENA
    name: Athena
    semantic_label: Analyse / structuration
  event_type: review
  summary: >-
    Le C2 est plus ancien que le DCE. Je vérifie si son estimation
    reste cohérente avec le périmètre actuel.
  conversation_visibility: visible
```

For a Rite or Space, the same display shape may be derived without asserting a new persisted schema:

```yaml
visible_identity:
  kind: rite
  id: CONCORDANCE_DES_SOURCES
  name: Concordance des Sources
  semantic_label: Rite de vérification
```

```yaml
visible_identity:
  kind: governed_space
  id: AGORA
  name: Agora
  semantic_label: Espace de délibération
```

These examples describe presentation projection only. No new persisted field is required until a concrete runtime producer demonstrates that existing trace/event and owner surfaces cannot provide the necessary identity safely.

## Progressive delivery

Conversation activity is intended to arrive progressively when meaningful work milestones occur.

```text
meaningful step
-> observable event
-> safe summary
-> resolve visible identity + semantic label
-> channel projection
```

The projection should not wait for the final answer when the runtime can safely expose an intermediate milestone.

It also must not publish every tool call, token, retry or retrieval attempt.

### Publishable milestones

A chat surface may show a line when one of these materially changes:

- responsibility or visible Role;
- Rite invocation, material result or closure;
- governed Space when it clarifies a deliberation or activity boundary;
- source/evidence coverage;
- important finding or contradiction;
- bounded delegation or return from research;
- approval or governance posture;
- blocking uncertainty;
- user decision required;
- task completion.

### Suppressed noise

Do not project by default:

- repeated semantic searches;
- individual low-level tool calls;
- unchanged Role/Rite/Space metadata repeated on every line;
- retries with no user-relevant state change;
- raw connector payloads;
- raw prompts;
- private reasoning;
- internal token/context management;
- duplicate status messages.

A burst of runtime operations may therefore produce one conversation line.

## Summary style

Target one or two short sentences. The preferred content is:

```text
observation + consequence/next move
```

Good:

```text
🦉 Athena · Analyse / structuration — Le C2 est antérieur au DCE actuel. Je vérifie les écarts de périmètre avant de retenir son estimation.
```

Too thin:

```text
🦉 Athena · Analyse / structuration — Analyse en cours.
```

Too detailed:

```text
A transcript of internal model deliberation, intermediate scoring, hidden prompt state or scratchpad.
```

## Channel neutrality

The same projection may be rendered by Telegram, WhatsApp, OpenWebUI, a Hermes WebUI or another admitted chat surface.

The channel must not invent governance semantics. It receives or derives a display projection from an observable event and renders it.

```text
same governed event
-> Telegram line
-> OpenWebUI line
-> cockpit timeline entry
```

Transport-specific formatting may differ; identity and semantic status must not.

## Relationship with Role Signals

Do not overload `role_signal.schema.yaml` for general runtime progress.

Role Signals are declared governance communications between Pantheon Roles. Hermes runtime progress, Rite projection, Space projection, source retrieval and generic activity are broader than that contract.

```text
Role Signal != conversation activity
conversation activity != Role Signal
```

## Compatibility with Hermes progress UX

`HERMES_PROGRESS_ERROR_RETRY_UX.md` already owns measurable runtime progress, explicit errors, diagnosis and bounded retry display. This conversation projection must not duplicate those semantics.

When useful, a compact activity line may summarize the latest meaningful runtime observation:

```text
⚙ Hermes · Exécution — OCR : 18/42 pages traitées. La progression est mesurée par le runtime ; aucune conclusion documentaire n'est encore tirée.
```

Quantified progress remains runtime-reported progress, not Pantheon-measured truth.

## Compatibility with Hermes adaptive execution

Hermes may adaptively select qualified tools, skills, plugins, MCP capabilities, retrieval providers, models or bounded delegation inside the admitted task boundary.

The conversation projection describes the meaningful outcome or next move, not a frozen tool path. Changing tools without changing user-relevant state should normally produce no new conversation line.

If a new mechanism changes data exposure, effect ceiling, approval posture, source scope or another governed boundary, that change is significant and may be projected.

## Failure and user-question behavior

When work cannot continue safely:

```text
⛔ Athena · Analyse / structuration — Les pièces retrouvées se contredisent sur le montant. Je ne peux pas conclure sans une source plus récente.
```

When only the user can resolve the remaining ambiguity:

```text
❓ Athena · Analyse / structuration — Les documents permettent deux lectures. Souhaites-tu conserver l'enveloppe C2 ou recalculer depuis le DCE actuel ?
```

A user question is a real workflow boundary, not a cosmetic progress message.

## Initial acceptance scenario — Floquet

A controlled test should verify the following observable sequence without requiring every internal call to be displayed:

```text
1. Professional financial request enters the governed path.
2. Pantheon classification is observable as consulted/qualified, not as blanket approval.
3. Athena identifies the need for current financial sources.
4. Hermes retrieves the exact C2 and current DCE/CCTP sources through the admitted IFJA retrieval path.
5. Athena records the material date/scope difference.
6. Concordance des Sources may be projected if a governed Rite is actually invoked and materially changes the review.
7. Themis or the applicable governance review qualifies the professional/financial delivery boundary.
8. Agora may be projected only if a real visible deliberation or unresolved human choice is opened there.
9. If evidence is sufficient, a Result Candidate is prepared; otherwise a user/source gap is shown.
10. The chat receives only meaningful compact activity lines plus the final candidate response.
```

Expected compact shape:

```text
🦉 Athena · Analyse / structuration — Je vérifie d'abord quelles pièces financières sont actuellement applicables.

⚙ Hermes · Exécution — C2 et DCE retrouvés. Le DCE est postérieur et décrit un périmètre plus précis.

🔁 Concordance des Sources · Rite de vérification — Les périmètres diffèrent. Je conserve l'écart visible avant toute conclusion financière.

⚖ Themis · Risque / conformité — Information financière destinée au client : la réponse reste candidate jusqu'à validation humaine.
```

## Implementation order

1. Keep `ROLE_DIALOGUE_TRACE` as the conceptual trace authority; do not create a competing canonical event family.
2. Reuse canonical Role, Rite and governed Space identities and resolve short semantic labels at presentation time.
3. Identify the smallest existing Hermes/runtime progress hook able to emit meaningful milestones.
4. Map milestones to safe summaries without exposing hidden reasoning.
5. Add deduplication/throttling so repeated operations or unchanged identity metadata do not flood chat.
6. Render the same projection through the active gateway/chat adapter.
7. Add the Floquet controlled test covering Pantheon classification, IFJA retrieval, source comparison, optional Rite/Space projection, approval boundary and progressive delivery.

If Hermes exposes no suitable progress/event hook, return a Capability Gap and implement the smallest adapter at the Hermes boundary rather than adding execution logic to Pantheon.

## Completion criteria

This feature is complete only when a controlled live run demonstrates that:

- activity arrives progressively rather than only at final response;
- a visible Pantheon identity shows both its governed name and a plain semantic label;
- Rite and governed Space labels appear only when those objects are actually relevant;
- Hermes remains visibly identified as runtime execution rather than a Pantheon Role;
- summaries are concise and contain no hidden reasoning;
- low-level tool noise is suppressed;
- source retrieval is not represented as truth;
- Rite completion is not represented as output approval;
- Space projection is not represented as persistence or authority;
- Hermes execution is not represented as approval;
- a blocking ambiguity can route to the user;
- Telegram/chat transport does not acquire governance authority;
- the final result remains subject to the existing Pantheon gates.

## Current status

This document defines the converged projection contract only.

It does not claim that Hermes currently emits these events or that Telegram/OpenWebUI currently streams them. Those runtime capabilities must be verified against the installed Hermes version and gateway before implementation is described as complete.
