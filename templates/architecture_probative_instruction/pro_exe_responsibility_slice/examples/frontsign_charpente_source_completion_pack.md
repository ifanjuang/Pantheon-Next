# Source Completion Pack — Frontsign / charpente / PRO-EXE boundary

Status: example — source completion pack candidate, documented non-implemented.  
Linked evidence tree: `frontsign_charpente_evidence_tree_candidate.md`.  
Risk level: Haut until source completion proves otherwise.  
External transmission: blocked until human approval.

This pack exists to replace conversation-derived assumptions with original project sources before any external communication.

It is not a project record, not proof, not approval, not a VISA and not an instruction.

## 1. Required source inventory

| Source | Required? | Status | Why it matters | Locator to fill |
|---|---:|---|---|---|
| Exact Frontsign email / request | Yes | Missing | Defines what is actually asked and whether the request seeks EXE validation. |  |
| Plan sheets concerned | Yes | Missing | Identifies drawings, indices, phase label, dimensions and technical notes. |  |
| Plan cartouche / footer | Yes | Missing | Determines whether non-EXE status is visible or ambiguous. |  |
| Contract / mission scope | Yes | Missing | Confirms whether EXE production is excluded or included. |  |
| CCTP charpente / structure clauses | Yes | Missing | Defines contractor lot scope and execution obligations. |  |
| BET structure note / pre-dimensioning note | If applicable | Missing | Determines who calculated or pre-dimensioned and with which scope. |  |
| Contractor EXE submission, if any | If applicable | Missing | Distinguishes PRO/DCE clarification from VISA review. |  |
| Role of Mayon | Yes | Missing | Avoids bypassing a relevant party in the responsibility chain. |  |
| Bureau de controle / SPS / OPC presence | If applicable | Missing | Determines additional review or coordination gates. |  |
| Prior client instruction / arbitration | If applicable | Missing | Clarifies whether client has already decided a scope or direction. |  |

## 2. Admission test for each source

For each source, fill:

```text
source_id:
title:
date:
index:
author / issuer:
recipient:
status: draft | issued | received | validated | superseded | unknown
source_type: mail | plan | CCTP | contract | BET_note | EXE_document | meeting_minutes | other
authority_class: project_controlled | specialist_project_source | derived | conversation_brief | unknown
locator:
relevant_excerpt_or_observation:
limitation:
```

## 3. Decision questions to resolve

```text
1. What exactly did Frontsign ask?
2. Does the question ask for information, coordination, validation, calculation, execution production or instruction?
3. Which plan sheets or notes are at risk of being read as EXE?
4. Do the sheets already say PRO, DCE, pre-dimensioning or non-EXE?
5. Does the architect contract include or exclude EXE production?
6. Does the contractor contract / CCTP require the company to produce EXE and final dimensions?
7. Is a BET structure note available, and what is its mission scope?
8. Is there an actual EXE document submitted for VISA, or only a PRO/DCE exchange?
9. Who is Mayon in this chain and what must not be bypassed?
10. Is the client in copy for information, arbitration, or approval?
```

## 4. Source-based status update

After source completion, update:

```text
risk_level: Bas | Moyen | Haut | Critique
source_basis: conversation_only | partial_project_sources | complete_project_sources
phase_reading:
mission_scope_reading:
professional_act:
responsibility_chain_complete: yes | no | uncertain
external_effect_possible: true | false | uncertain
output_status: result_candidate | needs_human_arbitrage | blocked | approved_for_external_transmission
```

## 5. Gate condition before mail

External mail may only move from candidate to approved when all are true:

```text
- exact request inspected;
- relevant plan indices inspected;
- mission scope inspected;
- CCTP / contractor responsibility inspected or absence stated;
- role of Mayon clarified or explicitly marked not relevant;
- wording avoids EXE validation language;
- architect approves final text;
- recipient list is intentional.
```

## 6. Current provisional status

```text
source_basis:
  conversation_only

risk_level:
  Haut

output_status:
  needs_human_arbitrage

external_transmission:
  blocked

allowed_next_action:
  collect and inspect sources

forbidden_next_action:
  send the mail candidate as final
```
