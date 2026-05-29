# Example — OpenWebUI Module Panel — Architecture and Legal Domains

Status: fictional UI example — educational support only.

This example shows how a future OpenWebUI cockpit could expose Pantheon role activation, domain activation, skill eligibility, dependency blockers and Zeus workflow proposal for a sensitive architecture/legal dossier.

It is not an implementation.

It is not a UI specification ready for development.

It is not legal advice.

It is not architectural advice.

It is not insurance advice.

It does not validate any professional position.

It does not authorize OpenWebUI, Hermes or Pantheon to perform real professional acts without human review.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Scenario

A user is working on a construction dispute dossier.

A contractor failed before completion.

A replacement company submitted a recovery quote.

The client asks the architect to explain whether the quote can be approved and whether some items may be charged as extras.

The user wants Pantheon to prepare:

- an internal risk note;
- a quote comparison candidate;
- a neutral client email candidate;
- a list of missing sources;
- a memory candidate only if useful and scoped.

The situation activates both domains:

```text
architecture
legal
```

This increases governance pressure.

It does not create professional validation.

## Requested cockpit view

The future OpenWebUI panel should show a compact state like this:

```text
Pantheon Module Panel — Fictional Dossier

Task status:
  candidate_task_contract_required

Active domains:
  architecture: candidate / project_enabled
  legal: candidate / project_enabled

Professional reliance:
  draft_only_until_human_review

Transmission:
  blocked_pending_decision

Memory:
  memory_candidate_only
```

## Domain activation state

```yaml
domain_activation:
  architecture:
    status: project_enabled
    reason: quote_review_and_architect_client_response
    mandatory_roles:
      - ATHENA
      - ARGOS
      - THEMIS
    optional_roles:
      - APOLLO
      - HEPHAISTOS
      - IRIS
    professional_reliance: draft_only_until_architect_review
    blocks_if_disabled:
      - architecture_skill_candidates
      - architecture_domain_templates
      - architecture_memory_candidate_review
      - architecture_external_transmission_as_domain_output

  legal:
    status: project_enabled
    reason: contractual_or_liability_risk_in_quote_validation_wording
    mandatory_roles:
      - ARGOS
      - THEMIS
      - ZEUS
    optional_roles:
      - ATHENA
      - APOLLO
      - IRIS
    professional_reliance: draft_only_until_lawyer_or_competent_professional_review
    blocks_if_disabled:
      - legal_skill_candidates
      - legal_note_templates
      - legal_memory_candidate_review
      - legal_external_transmission_as_domain_output
```

## Role readiness brief to Zeus

This is a compact preflight.

It is not a hidden multi-agent debate.

```yaml
role_readiness_brief:
  ATHENA:
    status: active
    reason: task_needs_decomposition_between_quote_review_risk_note_and_email
    mandatory_trigger_detected: complex_task
    risk_if_inactive: scope_confusion

  ARGOS:
    status: mandatory_for_risk
    reason: factual_claims_depend_on_CCTP_quote_site_reports_and_reception_status
    mandatory_trigger_detected: evidence_gap
    risk_if_inactive: unsupported_professional_position

  THEMIS:
    status: mandatory_for_risk
    reason: external_effect_and_professional_liability_risk
    mandatory_trigger_detected: legal_or_professional_risk
    risk_if_inactive: unsafe_validation_wording

  APOLLO:
    status: standby
    reason: needed_when_client_facing_wording_is_prepared
    mandatory_trigger_detected: false
    risk_if_inactive: unclear_or_overconfident_delivery

  HEPHAISTOS:
    status: active
    reason: candidate_artifacts_are_requested
    mandatory_trigger_detected: artifact_fabrication
    risk_if_inactive: no_structured_output_candidate

  IRIS:
    status: standby
    reason: external_transmission_not_yet_authorized
    mandatory_trigger_detected: false
    risk_if_inactive: premature_or_poorly_scoped_transmission

  ZEUS:
    status: active
    reason: procedure_and_status_arbitration_required
    mandatory_trigger_detected: always_procedural
    risk_if_inactive: no_clear_next_step
```

## Zeus workflow proposal

Zeus composes a workflow proposal.

Zeus does not run the workflow.

Zeus does not decide truth.

```yaml
zeus_workflow_proposal:
  workflow_status: proposed
  recommended_path:
    - confirm_task_contract_candidate
    - verify_domain_activation_architecture_and_legal
    - build_context_pack_from_selected_sources
    - run_argos_source_gap_review_candidate
    - run_hephaistos_quote_comparison_candidate
    - run_themis_risk_boundary_review_candidate
    - prepare_evidence_pack_candidate
    - expose_user_decision_gate_if_transmission_requested
    - keep_memory_candidate_blocked_until_review

  blocked_paths:
    - direct_client_validation_email
    - external_transmission_without_approval
    - legal_conclusion_without_professional_review
    - architecture_code_compliance_claim_without_source_review
    - memory_promotion_from_current_run

  user_decision_required: true
  reason: client_transmission_and_professional_validation_risk
```

## Effective Policy snapshot

```yaml
effective_policy:
  task_contract:
    required: true
    status: candidate_required

  context_pack:
    required: true
    status: missing
    blocks:
      - hermes_dispatch
      - langgraph_runtime_candidate
      - evidence_pack_completion

  evidence_surface:
    required: true
    status: incomplete
    blocks:
      - approval_prompt
      - delivery_gate
      - memory_candidate_review
      - external_transmission_gate

  approval:
    required: true
    status: missing
    approval_level: professional_review_required

  memory:
    allowed: memory_candidate_only
    canonical_memory_write: forbidden
    promotion: blocked_until_evidence_and_approval

  external_transmission:
    status: blocked
    reason: evidence_and_approval_missing
```

## OpenWebUI dependency blockers

The cockpit should not hide blocked functions.

It should show why they are unavailable.

```yaml
dependency_blockers:
  hermes_dispatch:
    status: blocked_by_missing_context_pack
    parent: task_contract_surface
    allowed_user_actions:
      - create_context_pack_candidate
      - attach_missing_sources
      - narrow_scope

  approval_prompt:
    status: blocked_by_missing_evidence
    parent: evidence_surface
    allowed_user_actions:
      - request_evidence_pack_candidate
      - request_source_gap_review

  memory_candidate_review:
    status: blocked_by_missing_evidence_and_scope
    parent: memory_surface
    allowed_user_actions:
      - keep_as_context_only
      - request_memory_candidate_later

  external_transmission_gate:
    status: blocked_by_missing_approval
    parent: decision_surface
    allowed_user_actions:
      - prepare_draft_only
      - request_user_decision_gate
      - cancel_transmission
```

## Eligible and blocked skill candidates

Domain activation may make skills eligible.

It does not authorize execution.

```yaml
skill_candidates:
  eligible_after_task_contract:
    - architecture_devis_analysis_candidate
    - architecture_cctp_review_candidate
    - legal_source_review_candidate
    - legal_issue_framing_candidate

  blocked_now:
    architecture_devis_analysis_candidate:
      reason: context_pack_missing
      can_become_authorized_if:
        - task_contract_confirmed
        - selected_quote_uploaded
        - CCTP_or_scope_source_selected
        - evidence_requirements_declared

    legal_note_draft_candidate:
      reason: legal_domain_draft_only_and_source_freshness_missing
      can_become_authorized_if:
        - jurisdiction_scope_declared
        - legal_sources_selected
        - professional_review_gate_visible

    external_client_email_candidate:
      reason: transmission_risk
      can_become_authorized_if:
        - internal_note_prepared
        - evidence_pack_candidate_visible
        - user_decision_gate_resolved
        - approval_state_explicit
```

## What the panel should make visible

```text
Visible:
- architecture and legal domains are active;
- professional reliance is draft-only;
- Argos and Themis are mandatory because risk is present;
- Hermes skills may become eligible but are not yet authorized;
- approval is blocked until evidence exists;
- transmission is blocked until User Decision Gate is resolved;
- memory promotion is forbidden.
```

## What the panel must not imply

```text
Forbidden implication:
- architecture domain active means the architect validated the position;
- legal domain active means the system gave legal advice;
- skill eligible means skill installed;
- skill eligible means skill authorized for the task;
- Zeus workflow proposal means execution started;
- Evidence Pack candidate means approval;
- User Decision Gate visible means the user has approved;
- memory candidate visible means Canonical Memory.
```

## User Decision Gate excerpt

If the user asks to send a client email, the panel should expose the decision rather than silently preparing transmission.

```text
User Decision Gate — Client transmission blocked

Object of conflict:
The client wants a position on the recovery quote, but the current dossier does not yet establish which items are in scope, additional, remedial, technically verified or legally sensitive.

Severity:
high

Options:
1. prepare internal note only;
2. prepare neutral clarification email marked draft-only;
3. request missing sources first;
4. request professional legal review before any position;
5. stop transmission.

Recommended procedure:
Do not send a global validation email.
Prepare internal note and source-gap list first.
```

## Candidate OpenWebUI panel summary

```text
Panel state:
  blocked_safe_mode

Reason:
  architecture + legal domains active;
  evidence incomplete;
  context pack missing;
  client transmission requested;
  professional risk high.

Next safe action:
  create Context Pack Candidate from selected quote, CCTP, site reports and contract notes.

Forbidden action:
  approve quote or send validation email.
```

## Boundary

This example is non-executable.

It does not create:

- an OpenWebUI template;
- an OpenWebUI Function;
- an OpenWebUI Tool;
- an OpenWebUI Pipeline;
- a Hermes skill;
- a domain authority engine;
- a legal agent;
- an architecture agent;
- a memory writer;
- an approval engine.

It only shows how a future cockpit could expose Pantheon governance without bypassing it.

## Final rule

```text
The panel may show that a capability exists.
It must also show why it cannot yet be used.
```