# Conversation Activity Projection

Status: candidate support doctrine — compact conversation projection of observable governed work. Repository state: documented non-implemented.
Boundary profile: candidate_support_note.

## Objective

Expose meaningful progress from Pantheon-governed Hermes work in chat surfaces without turning the chat into a technical log and without exposing hidden chain-of-thought.

The intended user-facing grammar is deliberately small:

```text
[icon] [visible role] — [brief observable rationale]
```

Examples:

```text
🦉 Athena — Le C2 est plus ancien que le DCE. Je vérifie si son estimation reste cohérente avec le périmètre actuel.

⚙ Hermes — C2 et CCTP retrouvés. Je poursuis sur les dernières pièces identifiées.

⚖ Themis — Cette réponse engage une information financière : validation humaine nécessaire.
```

This is a projection of observable work, not a new reasoning system, workflow engine, role system or authority layer.

## Existing authority reused

This projection reuses rather than duplicates:

- `ROLE_DIALOGUE_TRACE.md` for observable role moves and safe rationale summaries;
- Task Contracts for intent, owner role, scope, constraints and evidence expectations;
- Role Signals for declared role-to-role governance signals;
- Workflow Manifests for governed phases and entry/exit conditions;
- Hermes integration/runtime contracts for external execution boundaries.

A conversation activity line does not replace any of those objects and is not itself Evidence, approval, memory or authorization.

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
Hermes success != Pantheon validation
channel delivery != action authorization
```

## Minimal projection

Do not create a parallel canonical event model merely for chat.

When a compatible `trace_event` exists, the conversation renderer should consume only the fields needed for display:

```yaml
conversation_projection:
  trace_event_ref: trace-123
  visible_role: ATHENA
  event_type: review
  summary: >-
    Le C2 est plus ancien que le DCE. Je vérifie si son estimation
    reste cohérente avec le périmètre actuel.
  conversation_visibility: visible
```

`summary` is a concise observable rationale. It may state a relevant observation, why it matters, and the next bounded move. It must not contain private scratchpad or hidden chain-of-thought.

No new persisted field is required until a concrete runtime producer demonstrates that the existing trace/event surfaces cannot carry this projection safely.

## Progressive delivery

Conversation activity is intended to arrive progressively when meaningful work milestones occur.

```text
meaningful step
-> observable event
-> safe summary
-> channel projection
```

The projection should not wait for the final answer when the runtime can safely expose an intermediate milestone.

It also must not publish every tool call, token, retry or retrieval attempt.

### Publishable milestones

A chat surface may show a line when one of these materially changes:

- responsibility or visible role;
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
🦉 Athena — Le C2 est antérieur au DCE actuel. Je vérifie les écarts de périmètre avant de retenir son estimation.
```

Too thin:

```text
🦉 Athena — Analyse en cours.
```

Too detailed:

```text
A transcript of internal model deliberation, intermediate scoring, hidden prompt state or scratchpad.
```

## Display identities

The icon is a presentation hint only. The role name remains the semantic identity.

Recommended compact defaults:

```text
🦉 Athena      analysis / review
🔎 Argos       observation / source inspection
⚖ Themis      rule / risk / compliance review
☀ Apollo      synthesis / clarity when applicable
🛠 Hephaistos artifact / patch preparation
🧠 Mnemosyne   memory-boundary review
🛡 Cerberus    boundary/blocking surface when exposed by an adapter
⚙ Hermes       external runtime execution
❓             user decision required
✅             completed milestone
⛔             blocked milestone
```

The repository's canonical role registry wins over this presentation list. Hermes is an execution runtime identity, not a Pantheon Role. A UI may display it alongside roles only if that distinction remains clear in the underlying event metadata.

## Channel neutrality

The same projection may be rendered by Telegram, WhatsApp, OpenWebUI, a Hermes WebUI or another admitted chat surface.

The channel must not invent governance semantics. It receives or derives a display projection from an observable event and renders it.

```text
same governed event
-> Telegram line
-> OpenWebUI line
-> cockpit timeline entry
```

Transport-specific formatting may differ; semantic status must not.

## Relationship with Role Signals

Do not overload `role_signal.schema.yaml` for general runtime progress.

Role Signals are declared governance communications between Pantheon Roles. Hermes runtime progress, source retrieval and generic activity are broader than that contract.

A Role Signal may cause or support a conversation activity event, but:

```text
Role Signal != conversation activity
conversation activity != Role Signal
```

This preserves the existing role-signal authority and avoids adding Hermes to the Pantheon Role enum merely for display.

## Relationship with objectives

When an objective or Task Contract reference is available, a projected event may display progress against it. The reference should remain optional at the presentation layer.

Example:

```text
🦉 Athena — Les sources financières sont identifiées. Je vérifie maintenant si le DCE plus récent modifie l'enveloppe C2.
```

The chat does not need to display the objective identifier, place, rite, tool, risk axis or route on every line. Those may remain in structured trace metadata and be available on expansion in richer interfaces.

## Compatibility with Hermes adaptive execution

Hermes may adaptively select qualified tools, skills, plugins, MCP capabilities, retrieval providers, models or bounded delegation inside the admitted task boundary.

The conversation projection must therefore describe the meaningful outcome or next move, not freeze a particular tool path.

Changing tools without changing user-relevant state should normally produce no new conversation line.

If a new mechanism changes data exposure, effect ceiling, approval posture, source scope or another governed boundary, that boundary change is significant and may be projected.

## Failure and user-question behavior

When work cannot continue safely, project the reason at the level useful to the user.

```text
⛔ Athena — Les pièces retrouvées se contredisent sur le montant. Je ne peux pas conclure sans une source plus récente.
```

When only the user can resolve the remaining ambiguity:

```text
❓ Athena — Les documents permettent deux lectures. Souhaites-tu conserver l'enveloppe C2 ou recalculer depuis le DCE actuel ?
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
6. Themis or the applicable governance review qualifies the professional/financial delivery boundary.
7. If evidence is sufficient, a Result Candidate is prepared; otherwise a user/source gap is shown.
8. The chat receives only meaningful compact activity lines plus the final candidate response.
```

Expected conversation shape:

```text
🦉 Athena — Je vérifie d'abord quelles pièces financières sont actuellement applicables.

⚙ Hermes — C2 et DCE retrouvés. Le DCE est postérieur et décrit un périmètre plus précis.

🦉 Athena — L'enveloppe C2 reste un repère estimatif ; elle ne suffit pas seule à établir le coût actuel.

⚖ Themis — Information financière destinée au client : la réponse reste candidate jusqu'à validation humaine.
```

## Implementation order

1. Keep `ROLE_DIALOGUE_TRACE` as the conceptual trace authority; do not create a competing canonical event family.
2. Identify the smallest existing Hermes/runtime progress hook able to emit meaningful milestones.
3. Map those milestones to safe `summary` text and visible role/runtime identity.
4. Add deduplication/throttling so repeated tool operations do not flood chat.
5. Render the same projection through the active gateway/chat adapter.
6. Add the Floquet controlled test covering Pantheon classification, IFJA retrieval, source comparison, approval boundary and progressive projection.

If Hermes exposes no suitable progress/event hook, return a Capability Gap and implement the smallest adapter at the Hermes boundary rather than adding execution logic to Pantheon.

## Completion criteria

This feature is complete only when a controlled live run demonstrates that:

- activity arrives progressively rather than only at final response;
- the displayed identity matches the observed role/runtime responsibility;
- summaries are concise and contain no hidden reasoning;
- low-level tool noise is suppressed;
- source retrieval is not represented as truth;
- Hermes execution is not represented as approval;
- a blocking ambiguity can route to the user;
- Telegram/chat transport does not acquire governance authority;
- the final result remains subject to the existing Pantheon gates.

## Current status

This document defines the converged projection contract only.

It does not claim that Hermes currently emits these events or that Telegram/OpenWebUI currently streams them. Those runtime capabilities must be verified against the installed Hermes version and gateway before implementation is described as complete.
