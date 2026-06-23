# Run 001 — Review Card Candidate

Status: static cockpit card candidate — fictional MVP manual run.

This card is a compact decision surface derived from:

```text
00_task_contract_candidate.md
01_context_pack_candidate.md
02_evidence_pack_candidate.md
03_result_candidate_note.md
```

It is not proof, not approval, not professional validation, not a client-facing deliverable and not an external-action authorization.

## Card identity

```text
review_card_id: RCARD-MVP-ARCH-FICTIF-001-RUN-001
linked_task_contract: TC-MVP-ARCH-FICTIF-001-RUN-001
linked_context_pack: CP-MVP-ARCH-FICTIF-001-RUN-001
linked_evidence_pack_candidate: EP-MVP-ARCH-FICTIF-001-RUN-001
linked_result_candidate: RC-MVP-ARCH-FICTIF-001-RUN-001
project_alias: MVP-ARCH-FICTIF-001
prepared_date: 2026-06-22
prepared_by: ChatGPT manual review
```

## Display status

```text
status: internal candidate only
approval_ceiling: C1
requested_effect: internal_state_change
external_action_status: none / blocked
memory_status: none / no Registre Probatoire entry
risk_level: high
decision_gate: required if any client-facing or contractor-facing response is prepared
```

## One-line verdict

```text
Do not answer the contractor as if the opening or extension is validated; request missing evidence first.
```

## Corpus snapshot

```text
received_sources: 10 fictive Markdown sources
absent_critical_sources: 8
source_authority_warning: PLU excerpt is fictive and non-official; no source is authoritative by itself.
```

Critical absent sources:

```text
- dimensioned existing plan;
- dimensioned proposed plan;
- current official PLU extract;
- structural engineer calculation note;
- existing wall composition investigation;
- formal client approval for external message;
- contractor execution study;
- current energy regulation note.
```

## Key claims

| Claim | Status | Evidence refs | Risk |
|---|---|---|---|
| Client wants quick validation and contractor response. | supported | CL-001, FR-001, FR-002 | high |
| Dimensioned plans are missing. | supported | CL-003, FR-004, FR-007 | high |
| PLU conclusion is not possible from current corpus. | supported | CL-004, FR-005, CT-002 | high |
| Enlarged opening is not validated. | supported | CL-006, CL-008, CL-009, CL-012, CT-003 | high |
| Contractor estimate excludes decisive scopes. | supported | CL-011, FR-018, FR-019, CT-004 | high |
| Thermal performance remains assumption-based. | supported | CL-013, FR-022, FR-023, FR-024 | medium |
| Dampness / slope / water risk requires verification. | supported | CL-005, CL-010, CL-014, CT-006 | medium |
| External response would be unsafe now. | supported synthesis | CL-015, RC-002, RC-008 | high |

## Contradictions

| Tension | Why it matters | Required handling |
|---|---|---|
| Client asks for quick validation and contractor answer, but CR and structure note block validation. | External communication could be read as approval. | Do not send; open User Decision Gate if a draft is required. |
| PLU excerpt suggests possible extension, but it is fictive and non-official. | False regulatory certainty risk. | Verify official PLU before any planning conclusion. |
| CCTP mentions enlarged opening, but structure and CR state no execution validation. | Structural liability risk. | Require sondage, relevé and engineering input. |
| Contractor estimate describes works, but excludes key studies. | Scope and cost appear more complete than they are. | Classify estimate as incomplete for decision. |
| Thermal note assumes continuity, but wall composition and dimensions are missing. | Thermal claim would be assumption, not conclusion. | Keep thermal position as to verify. |
| Damp traces are visible, but no cause is established. | Pathology / substrate risk may be under-scoped. | Request verification before closing scope. |

## Risk stack

```text
urbanism: high — official PLU, parcel area and emprise data absent.
structure: high — wall status, lintel and reinforcement unresolved.
thermal_energy: medium — assumptions only, no regulatory calculation.
water_substrate: medium — sloping terrain, undocumented void, damp traces.
scope_cost: high — estimate excludes structure, urbanism, humidity, thermal items.
communication_liability: high — contractor-facing statement would imply approval.
```

## What the AI may say

Internal candidate wording only:

```text
À ce stade, les pièces disponibles ne permettent pas de valider l’ouverture élargie ni de répondre à l’entreprise comme si l’exécution était acquise. Les plans cotés, le PLU officiel, le sondage du linteau, la composition du mur et le pré-dimensionnement structurel restent nécessaires. Le devis reçu exclut en outre plusieurs postes déterminants : étude structure, renfort, dossier urbanisme, traitement humidité et étude thermique. La suite sûre est donc de compléter les pièces avant toute instruction externe.
```

This wording is not approved for sending.

## What the AI must not say

```text
- “Le projet est validé.”
- “Vous pouvez prévoir l’ouverture.”
- “La mairie ne posera pas de problème.”
- “Le mur n’est pas porteur.”
- “Aucun renfort n’est nécessaire.”
- “Le devis est complet.”
- “Les performances thermiques sont conformes.”
```

## Decision expected

```text
recommended_default: request more evidence before any external response.

allowed_human_choices:
1. Accept the internal candidate as a basis for evidence requests.
2. Ask for a short internal draft listing missing documents.
3. Open a User Decision Gate for any client/contractor-facing message.
4. Reject any wording that implies validation.

user_decision_gate: UDG-MVP-ARCH-FICTIF-001-RUN-001
```

## Next evidence requests

```text
- official current PLU extract;
- existing and proposed dimensioned plans;
- structural sondage of lintel and wall composition;
- engineer pre-dimensioning if opening remains in scope;
- contractor clarification of exclusions;
- dampness / substrate verification;
- thermal/regulatory note after dimensions and wall composition are known;
- explicit approval before any external message.
```

## Card-level output posture

```text
Result status: candidate.
Evidence status: candidate support.
External status: blocked.
Memory status: none.
Human action required: yes.
```

## Boundary footer

```text
This card displays candidate status.
It does not approve.
It does not validate.
It does not transmit.
It does not create memory.
The human decides.
```
