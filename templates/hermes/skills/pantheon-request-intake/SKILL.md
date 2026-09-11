---
name: pantheon-request-intake
description: "Use before Pantheon request classification when raw user language must be translated into a minimal request candidate: intent, governed conditions, optional coordination relations and observable completion requirements. Produces candidate observations only; never derives K/V/C, approval, truth or authorization."
metadata:
  owner_layer: hermes
  status: candidate_template_only
  governed_by: docs/governance/REQUEST_LIFECYCLE.md
  policy_contract: mcp-server/docs/HERMES_INTEGRATION_CONTRACT.md
  upstream: "agentskills.io SKILL.md standard; exact Hermes runtime compatibility must be qualified before admission"
---

# Pantheon request intake

Bounded semantic adapter for Hermes. Use it to describe a raw request in the
smallest vocabulary needed by the existing Pantheon policy surface.

It is not a planner, router, Role, workflow engine, risk classifier or approval
engine.

```text
semantic candidate != truth
condition candidate != consequence classification
coordination relation != dispatch
completion requirement != approval
Hermes interpretation != Pantheon decision
```

## Purpose

Translate only what is materially observable in the user's request into a
request candidate that `classify_request` can govern.

```text
raw request
-> minimal semantic candidate
-> Pantheon classify_request
-> PROCEED / CONSULT / GATE
```

Pantheon owns K/V/C and the resulting handling. Do not reproduce that policy in
this skill.

## Minimal output

Return only fields that are supported by the request. Omit unsupported fields.

```yaml
intent: "..."
requested_transformation: rewrite
conditions: []
coordination:
  requires: []
  independent: []
  synthesize: false
  branch_on: []
  repeat_until: []
completion_requirements: []
current_state: optional_label
target_state: optional_label
```

`intent` should preserve the user's actual cap rather than expand it into a
larger project.

Use `requested_transformation` only for an explicit harmless transformation such
as rewrite, wording, polish, formatting or summary. Do not use it to hide a
material change of meaning, status, responsibility or consequence.

## Condition vocabulary

Use only existing trigger names from `docs/governance/ROLE_ACTIVATION.md` that
are accepted by the current Pantheon request-handling surface.

Common examples include:

```text
complex_task
scope_split_required
multi_step_workflow
factual_claim
external_reference
source_required
evidence_gap
source_freshness_risk
provenance_unclear
memory_recall_requested
prior_decision_reuse
project_history_reuse
duplicate_or_supersession_risk
memory_candidate
memory_promotion
approval_required
legal_or_professional_risk
external_effect
policy_conflict
liability_risk
unclear_output
narrative_or_editorial_work
delivery_quality_required
artifact_fabrication
external_transmission
client_delivery
public_output
handoff_required
recipient_specific_format
```

Do not invent a synonym merely because it sounds more precise. If no governed
condition is materially supported, emit none.

## Materiality rule

Emit a condition only when omitting it could materially change at least one of:

```text
meaning
reliability / source need
responsibility / risk boundary
authorization / external effect
continuity / current version
retention / memory posture
next legitimate transition
```

Do not emit a condition merely because a word appears in the request.

## Memory direction

Distinguish retrieval or reuse of already-retained information from a request to
make information persistent for future use.

```text
memory_recall_requested / prior_decision_reuse
= retrieve or reuse information that is already retained

memory_candidate
= information is being proposed for possible retention

memory_promotion
= the user asks to make information persistent, canonical, official, or a
  governed reference for future sessions or future reuse
```

When the user explicitly asks for governed persistence, emit all materially
required conditions:

```text
memory_candidate
memory_promotion
approval_required
```

`approval_required` here describes the need for a governed gate; it is not an
approval and does not authorize persistence.

Do not emit `prior_decision_reuse` merely because the user says the information
should be reusable later. If the information is being stored now for future
reuse, that describes promotion, not reuse of an already-retained decision.

## External action direction

Distinguish preparing content for an external audience from asking Hermes to
cause an actual effect outside the current interaction.

```text
external_transmission
= information is requested to be sent, submitted, published, or otherwise
  transmitted outside the current interaction

client_delivery
= the requested external recipient is a client

external_effect
= the request asks Hermes to cause a real-world or external-system effect,
  including sending, publishing, submitting, changing, creating, deleting,
  booking, paying, approving, or otherwise acting outside the conversation
```

When the user asks to actually send or publish information, emit all materially
required transmission conditions:

```text
external_transmission
external_effect
```

Add `client_delivery` when the requested recipient is a client.

A draft, rewrite, message preparation, or recipient-specific formatting request
does not imply `external_effect` unless actual transmission or another external
action is requested. `external_effect` describes the requested consequence; it
does not authorize that consequence or imply that it occurred.

Examples:

```text
"Corrige les fautes de ce texte"
-> requested_transformation: wording
-> no source/risk/external condition solely because the text mentions a contract

"Vérifie le montant de ce devis contre le CCTP"
-> source_required
-> factual_claim
-> legal_or_professional_risk only when the requested use actually carries that consequence

"Retrouve ce qu'on avait décidé hier"
-> memory_recall_requested
-> prior_decision_reuse

"Envoie cette réponse au client"
-> external_transmission
-> client_delivery
-> external_effect

"Fais trois idées de logo"
-> artifact_fabrication
-> no source_required unless the user also asks to reproduce or verify an external reference
```

## Coordination

Describe coordination only when the request itself or already-observed task
state supports a material relation.

```yaml
coordination:
  requires:
    - [supporting_basis, consequence_review]
  independent:
    - [option_a, option_b, option_c]
  synthesize: true
  branch_on:
    - observed_result
  repeat_until:
    - tests_pass
```

Rules:

- `requires`: one named state genuinely must precede another;
- `independent`: work items can proceed without an ordering dependency;
- `synthesize`: independent results need one shared synthesis;
- `branch_on`: an observed result determines the next path;
- `repeat_until`: another attempt may be useful until an observable criterion is met.

Do not choose a topology. Pantheon derives topology from relations when useful.
Do not infer ordering from Role names or domain names.

## Completion requirements

Prefer observable task acceptance criteria when the user or task makes them
clear:

```text
tests_pass
requested_fact_resolved
three_distinct_options_produced
inconsistencies_identified
response_candidate_ready
```

Do not invent pseudo-certainty such as `answer_is_true`, `client_will_accept` or
`professional_validation_complete`.

If no useful observable criterion is clear, omit it and let Pantheon project its
bounded fallback requirements.

## Ambiguity and conservative behavior

Do not turn every ambiguity into `complex_task`, `source_required` or risk.

When ambiguity does not materially affect the answer, preserve the narrow shared
meaning and continue. When it would materially alter scope, consequence or the
next legitimate action, expose the applicable governed condition or request one
targeted clarification.

```text
uncertain interpretation != permission to guess
uncertainty != automatic high risk
missing detail != automatic source requirement
```

## Reconsultation

During execution, re-run this semantic intake only when a material fact changes
the governed frame, for example a newly discovered external effect, missing
source, contradiction, version conflict, liability boundary, memory promotion or
approval need.

Do not reconsult after every internal step.

## Return rules

- Return a request candidate, never K/V/C.
- Do not state `PROCEED`, `CONSULT` or `GATE`; Pantheon returns those.
- Do not authorize a tool, profile, send, write, memory promotion or external action.
- Do not promote retrieved material to Evidence.
- Do not create a Task Contract unless the Pantheon response requires the existing Task Contract path.
- Preserve the user's requested effect and audience rather than silently weakening or strengthening them.
- Prefer the smallest sufficient candidate.

## Final invariant

```text
Hermes describes material conditions.
Pantheon classifies consequence and exposes the smallest governance handling.
Hermes executes inside that admitted boundary.
Material changes trigger reconsultation.
The human decides consequential effects.
```
