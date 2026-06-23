# Evidence Tree Candidate — Frontsign / charpente / PRO-EXE boundary

Status: example — candidate output, documented non-implemented.  
Template source: `templates/architecture_probative_instruction/pro_exe_responsibility_slice/`.  
Doctrine source: `docs/governance/ARCHITECTURE_PROBATIVE_INSTRUCTION.md`.  
Authority status: candidate-only / to verify.

This example is based on user-provided project context in conversation. It is not a validated project record, not a legal opinion, not a BET review, not a VISA, not an execution instruction and not an external communication.

It should be treated as an Architecture Evidence Tree Candidate for review by the architect.

```text
Retrieval finds material.
Instruction qualifies material.
Evidence supports a candidate.
Approval gates external effect.
The architect decides.
```

## 1. Question instructed

```text
question:
  How should the agency frame the Frontsign / charpente / structure-plan exchange so that PRO / DCE coordination material is not interpreted as EXE production or final execution validation?

professional_act:
  clarify + alert + draft boundary wording

project_phase:
  PRO / DCE boundary, with execution responsibility risk

mission_scope:
  architecture / MOE coordination and design documentation; EXE production and final execution dimensions excluded unless a specific contract proves otherwise

output_status:
  evidence_pack_candidate + mail_candidate + plan_footer_candidate
```

## 2. Candidate claim table

| Claim | Source support | Phase reading | Responsibility reading | Risk | Required gate |
|---|---|---|---|---|---|
| Plans / notes must be presented as PRO / DCE coordination or pre-dimensioning, not EXE. | User-provided brief; architecture probative instruction doctrine; PRO/EXE slice template. | PRO / DCE. | Architect may coordinate design intent; execution production remains contractor / BET chain. | High if drawings contain precise dimensions or technical notes. | Human review before external send. |
| Final foundation dimensions, execution details and calculations must come from the contractor or competent BET, not be silently assumed by the architect. | User-provided brief; safe wording candidates template. | EXE responsibility boundary. | Contractor / BET produces and assumes final EXE; architect may check coherence within mission. | High: liability shift if agency language says validate / final / à réaliser. | Human arbitration. |
| Any sheet footer should state that the document does not constitute an execution plan. | User-provided brief; safe output candidate template. | PRO / DCE document-status clarification. | Architect controls document labeling; contractor remains responsible for EXE. | Medium to high depending on sheet precision and recipients. | Architect approval before issue. |
| Any mail to Frontsign / BET / client should avoid wording that suggests final technical validation. | User-provided brief; risk phrase list in template. | External communication risk. | Agency may clarify scope but not validate EXE outside mission. | High because client is in copy and may read the message as responsibility allocation. | External communication approval. |
| Pre-drilling / prepercement should not be described as a confirmed execution requirement if the project is standard timber framing and no such pre-drilling is intended. | User-provided brief only. | To verify against actual CCTP/plans. | Contractor execution method and BET checks remain outside automatic agency validation. | Medium: wrong technical instruction possible. | To verify against project documents before wording. |
| Mayon or any other party in the responsibility chain should not be bypassed or omitted if they are contractually relevant. | User-provided brief only. | Responsibility-chain completeness. | Missing a responsible party may distort liability or coordination. | Medium: chain-of-responsibility confusion. | To verify against contract / participants list. |

## 3. Source items

```text
source_items:
  - source_ref: user_context_2026-06-pro-exe-frontsign
    source_type: conversation_brief
    authority_class: source_candidate / to_verify
    index_or_date: 2026-06 conversation context
    issuer: user / architect
    recipient: assistant
    locator: current Pantheon Next working discussion
    observation: User instructed that Frontsign should indicate plans are pre-dimensioning / phase PRO for charpente and not execution plans; final foundation dimensions should come from the company; client should understand the responsibility chain; no pre-drilling in classic timber frame unless verified.
    limitation: Not an original project source. Must be checked against contract, plans, CCTP, BET notes and correspondence before external use.
    supersession_risk: unknown

  - source_ref: docs/governance/ARCHITECTURE_PROBATIVE_INSTRUCTION.md
    source_type: governance_document
    authority_class: candidate support doctrine
    index_or_date: repository current
    issuer: Pantheon Next repository
    recipient: Pantheon Next users
    locator: Architecture Probative Instruction
    observation: A point of architecture is not true because it was retrieved; it becomes usable only when situated in source, version, phase, mission scope, responsibility, external-effect risk, evidence status and human decision path.
    limitation: Candidate support doctrine; method only; non-runtime.
    supersession_risk: low unless doctrine changes

  - source_ref: templates/architecture_probative_instruction/pro_exe_responsibility_slice/README.md
    source_type: template
    authority_class: support material / candidate
    index_or_date: repository current
    issuer: Pantheon Next repository
    recipient: Pantheon Next users
    locator: PRO / EXE Responsibility Slice
    observation: The slice exists for questions where a request, drawing, note or wording may make the agency appear to produce or validate execution work outside its mission.
    limitation: Template only; not doctrine by itself; does not govern.
    supersession_risk: low unless template changes

  - source_ref: templates/architecture_probative_instruction/pro_exe_responsibility_slice/safe_output_candidates.md
    source_type: template
    authority_class: support material / candidate
    index_or_date: repository current
    issuer: Pantheon Next repository
    recipient: Pantheon Next users
    locator: Plan footer, contractor/BET clarification, client explanation, VISA comment and boundary candidates
    observation: Provides candidate wording for non-EXE footer and clarification that final dimensions, calculations and execution details remain contractor / BET responsibility.
    limitation: Wording candidates only; must be adapted and approved by the architect.
    supersession_risk: low unless template changes
```

## 4. Responsibility chain

```text
requester:
  Frontsign / contractor / BET chain — to verify from actual correspondence

producer_of_current_document:
  architect / MOE and/or BET, depending on the actual plan or note issuer — to verify

producer_of_execution_document:
  contractor and/or contractor-appointed BET, unless contract states otherwise

calculation_owner:
  competent BET / contractor-side engineering chain for final EXE calculations

checker:
  architect may check architectural coherence within mission; BET / bureau de controle may check within their own missions if applicable

decision_owner:
  project owner for project choices and contractual decisions; architect for agency wording before transmission

executor:
  contractor / lot holder

recipient:
  Frontsign / BET / client in copy — to verify

party_bearing_consequence:
  contractor for execution production; BET for calculations within mission; architect only within MOE mission and wording actually issued; client for arbitration/contract decisions

unknowns:
  exact contract mission, exact plan index, exact author of plan/note, exact CCTP clauses, exact Frontsign question, whether Mayon is a contractor/BET/intermediary, whether bureau de controle exists on the operation
```

## 5. Contradictions and tensions

```text
contradictions:
  - tension: drawings or notes may be precise enough to look like EXE while the intended phase is PRO / DCE
    source_a: user_context_2026-06-pro-exe-frontsign
    source_b: actual plan sheets / cartouches needed
    affected_output: plan footer + mail wording
    required_arbitrage: verify document index, cartouche and mission scope before issue

  - tension: Frontsign or another party may ask the agency to confirm final dimensions, while final execution dimensions should be produced by contractor / BET
    source_a: user_context_2026-06-pro-exe-frontsign
    source_b: contract / CCTP / BET note needed
    affected_output: contractor/BET clarification mail
    required_arbitrage: refuse final EXE validation wording; allow only coherence / coordination wording

  - tension: pre-drilling / prepercement language may imply a specific execution method, while user context says no pre-drilling in classic timber frame
    source_a: user_context_2026-06-pro-exe-frontsign
    source_b: CCTP / charpente details / contractor method statement needed
    affected_output: any technical wording about pre-drilling
    required_arbitrage: mark to_verify and avoid instruction wording

  - tension: client in copy needs clarity without turning the mail into a legal-looking blame transfer
    source_a: user_context_2026-06-pro-exe-frontsign
    source_b: mail candidate needed
    affected_output: client-facing explanation
    required_arbitrage: use neutral chain-of-responsibility wording, not accusatory wording
```

## 6. Risk classification

```text
risk_level: high
external_effect_possible: true
why:
  The exchange concerns responsibility allocation between PRO / DCE coordination and EXE production. If the agency wording says or implies 'validated', 'definitive', 'bon pour execution', 'a realiser' or 'prepercement', it may be read as technical approval or execution instruction.

forbidden_wording_found_or_to_avoid:
  - bon pour execution
  - plan d'execution
  - dimensions definitives
  - valide / validé
  - conforme
  - visa favorable
  - prepercement / prépercement unless explicitly verified and correctly scoped
  - a realiser / à réaliser
  - synthese complete
  - sans reserve

unsafe_interpretation:
  The client, Frontsign, BET or contractor may interpret agency-provided PRO / DCE information as final EXE validation, shifting responsibility from the contractor / BET chain back to the architect.
```

## 7. Candidate conclusion

```text
candidate_conclusion:
  The agency should answer by clarifying the status of the documents and the responsibility chain, not by confirming final execution dimensions or execution methods. The plans / notes should be framed as PRO / DCE design or consultation support, with explicit wording that they do not constitute execution plans. Final foundation dimensions, calculations, pre-drilling if any, assemblies and execution details must be produced and verified by the responsible contractor / BET chain under the contract. The architect may review architectural coherence and coordination within mission scope.

status:
  needs_human_arbitrage

confidence_note:
  Medium. The professional logic is strong, but the evidence base is currently conversation-derived. Actual contract, plans, cartouches, CCTP, BET notes and correspondence must be inspected before external use.
```

## 8. Safe wording candidate — plan / sheet footer

```text
Document de conception / consultation — ne vaut pas plan d'execution.

Les dimensions, assemblages, percements, notes de calcul et dispositions finales d'execution sont a etablir, verifier et assumer par l'entreprise titulaire et, le cas echeant, par son BET, dans le respect des pieces marche et de ses obligations contractuelles.
```

## 9. Safe wording candidate — contractor / BET clarification mail

```text
Bonjour,

Pour clarifier le statut des documents transmis : les indications figurant sur les pieces PRO / DCE constituent un support de conception et de consultation. Elles ne valent pas plan d'execution.

Les dimensions finales des fondations, les notes de calcul, les assemblages, les percements eventuels et les dispositions d'execution restent a etablir et verifier par l'entreprise titulaire et, le cas echeant, par son BET, conformement aux pieces marche et a ses obligations contractuelles.

Dans le cadre de notre mission, nous pouvons verifier la coherence architecturale et la coordination avec les pieces du projet, sans nous substituer a la production EXE ni a la responsabilite technique de l'entreprise et de ses intervenants competents.

Merci egalement de veiller a ne pas court-circuiter les intervenants concernes dans la chaine de responsabilite et de validation.

Cordialement,
```

## 10. Safe wording candidate — client-facing explanation

```text
Bonjour,

Le point a clarifier porte sur la frontiere entre les documents de conception / consultation et les documents d'execution.

En phase PRO / DCE, les documents de maitrise d'oeuvre cadrent le projet, les prestations attendues et les hypotheses de coordination. Ils ne se substituent pas aux plans d'execution, notes de calcul, dimensions finales et dispositions techniques que l'entreprise doit produire et assumer dans son propre perimetre, avec son BET le cas echeant.

Notre role reste de verifier la coherence avec le projet et les pieces marche, sans reprendre a notre charge la production EXE de l'entreprise ou de son BET.

Cordialement,
```

## 11. Human gate

```text
decision_needed:
  to_verify + architect approval

approval_needed_before_external_transmission:
  yes

reviewer:
  architect / IFJ Architecture

review_date:
  to_fill

final_decision:
  pending
```

## 12. Missing evidence before external use

```text
missing_sources:
  - exact Frontsign email or request
  - plan sheet references and indices
  - plan cartouches and any existing footer
  - contract / mission scope
  - CCTP charpente / structure clauses
  - BET structure note or lack thereof
  - identity and role of Mayon in the responsibility chain
  - whether any bureau de controle / SPS / OPC is involved
  - whether the issue concerns PRO, DCE, VISA or actual EXE submitted by contractor
```

## 13. Final status

```text
Evidence Tree Candidate created.
Not validated.
Not externally transmissible as-is.
Ready for architect review and source completion.
```
