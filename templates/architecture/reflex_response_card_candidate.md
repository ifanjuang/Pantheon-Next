# Architecture Method Response Card Candidate

Status: template candidate — non-executable.

This template is the compact first-layer answer shape for architecture-domain method objects.

It is not a runtime, UI component, decision engine, approval, memory entry or external action.

Filename note: this template keeps its historical filename for now. In content, `reflex` is used narrowly for triggered cadrage / rappel warnings.

## Identity

```text
card_id:
project_ref:
request:
prepared_date:
prepared_by:
```

## First-layer answer

```text
Depth: Fast | Normal | Deep
Status: candidate | to_verify | needs_approval | blocked
Request understood:
Method objects used:
Relevant facet expressions:
Consulted facet links:
Rite requested: yes | no
Zeus arbitration: none | needed | completed_candidate
What I can say now:
What I checked:
What I did not check:
Missing information:
Risk:
Mission boundary:
Next action:
Gate required: yes | no
```

## Facet expression trace

Only include facet expressions that materially change the answer.

```text
Relevant facet expressions:
- Role / facet:
  expression: coloring | visible | consultative | arbitral
  reason:
  output_effect:
```

Silent facets are not displayed.

Coloring facets should usually remain hidden unless their presence explains a deliberate wording or non-escalation choice.

## Facet consultation trace

Consultations happen facet-to-facet, not role-to-role.

```text
Consulted facet links:
- source: Role / facet
  consulted: Role / facet
  question:
  effect:
```

Show only consultations that change output, risk, proof requirement, wording, next action or gate.

## Method objects

```text
approaches:
disciplines:
strategies:
procedures:
tactics:
reflexes:
role_owned_reflexes:
facet_expressions:
facet_consultations:
rite_request:
zeus_arbitration:
```

## Output limits

```text
Allowed use:
Forbidden use:
External action status: none | blocked_until_user_validation | requires_User_Decision_Gate
Memory / Notion status: none | candidate | blocked | needs_approval
```

## Details on demand

```text
Evidence detail available: yes | no
Contradictions available: yes | no
Assumption ledger available: yes | no
Missing information register available: yes | no
Facet expression detail available: yes | no
Facet consultation trace available: yes | no
Draft output available: yes | no
```

## Boundary

```text
The card is a first-layer candidate summary.
It does not approve, validate, transmit, file, remember canonically or decide.
Facet expression does not create a hidden agent loop.
Facet consultation does not create a hidden agent loop.
Zeus arbitration does not approve automatically.
```
