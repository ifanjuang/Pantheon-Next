# Role Activation

Status: active support doctrine — role, domain and skill activation semantics only.

This document defines how Pantheon Next may activate, deactivate, require or suspend Pantheon Roles, professional domains and candidate skills for a session, task, dossier or project.

It does not add agents.

It does not add a role runtime.

It does not add a skill runtime.

It does not create a marketplace.

It does not implement a UI.

It does not authorize automatic skill installation, automatic role execution, automatic approval, automatic memory promotion or autonomous professional advice.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon must support modular governance without turning roles, skills or business domains into autonomous agents.

The user may want to activate or deactivate:

- governance roles;
- professional domain packs;
- Hermes skill candidates;
- OpenWebUI cockpit templates;
- review gates;
- source policies;
- memory policies.

This document defines the activation rules for roles, domain packs and skill candidates.

## Core rule

```text
Roles may be inactive by default.
Risks may reactivate them.
Domain packs may constrain work.
Skill candidates may execute only through Hermes.
Zeus composes the workflow from active, standby and mandatory roles.
```

## What role activation means

A Pantheon Role is a governance viewpoint.

It is not an autonomous worker.

Activating a role means:

- its review pressure is included;
- its signals may be requested;
- its risk triggers are monitored;
- its dissent may affect procedure;
- Zeus may include it in the workflow.

Deactivating a role means:

- it does not participate actively by default;
- it may still be reactivated by mandatory risk triggers;
- its doctrine remains available;
- it does not disappear from the system.

## What domain activation means

A professional domain pack is a governed configuration of vocabulary, source expectations, risk triggers, templates and review gates.

It is not a profession-specific autonomous agent.

Activating a domain pack means:

- domain-specific source policies apply;
- domain-specific evidence expectations apply;
- domain-specific approval and delivery gates may apply;
- some roles may become mandatory by default;
- some OpenWebUI templates may become visible;
- some Hermes skill candidates may become eligible for task authorization.

Activating a domain pack does not mean:

- automatic professional advice;
- automatic legal, medical, architectural or financial authority;
- automatic source validity;
- automatic skill execution;
- automatic memory promotion;
- automatic external transmission.

## What skill activation means

A skill candidate is a bounded capability candidate, usually executed outside Pantheon by Hermes or another external runtime.

A skill candidate is not a Pantheon Role.

A skill candidate is not a domain authority.

Skill activation means:

- the skill candidate may be considered for a Task Contract;
- its FOR and NOT FOR boundaries apply;
- its required inputs, tools, evidence and approval ceiling apply;
- Hermes may execute it only if task-authorized.

Skill activation does not mean:

- automatic installation;
- automatic execution;
- direct OpenWebUI execution;
- direct Pantheon execution;
- professional validation;
- memory promotion;
- approval.

## Activation classes

Recommended activation classes:

```text
governance_role
professional_domain_pack
hermes_skill_candidate
openwebui_template_pack
evidence_policy_pack
memory_policy_pack
approval_gate_pack
external_tool_candidate
```

## Role statuses

Recommended role statuses:

```text
active
standby
disabled_by_user
disabled_by_scope
not_relevant
mandatory_for_risk
blocked
suspended
```

## Domain statuses

Recommended domain statuses:

```text
inactive
watch
candidate
sandbox_enabled
project_enabled
dossier_enabled
domain_enabled
organization_enabled
suspended
rejected
```

## Skill statuses

Recommended skill statuses:

```text
unavailable
detected
watch
candidate
sandbox_enabled
project_enabled
dossier_enabled
task_authorized
suspended
rejected
```

## Zeus Role Readiness Brief

Before a significant session or task, roles may emit a short readiness signal to Zeus.

This is not a hidden multi-agent debate.

It is a compact governance-status preflight.

Recommended format:

```yaml
role_signal:
  role: ARGOS
  status: standby
  reason: no factual or external source claim yet
  mandatory_trigger_detected: false
  recommended_involvement: source_check_if_claims_appear
  risk_if_inactive: unsupported_evidence
```

Zeus then produces a session brief:

```yaml
zeus_session_brief:
  session_type: repo_governance_work
  active_roles:
    - ATHENA
    - THEMIS
    - HEPHAISTOS
    - ZEUS
  standby_roles:
    - ARGOS
    - APOLLO
    - IRIS
  disabled_roles: []
  mandatory_roles:
    - THEMIS
  enabled_domains:
    - pantheon_repo_governance
  candidate_skills: []
  proposed_workflow:
    - scope_check
    - protected_file_check
    - doctrine_update
    - ai_log
    - diff_review
  user_decision_required: false
```

## Mandatory role triggers

Some triggers override user convenience.

A role may be inactive by default, but must reactivate when its mandatory trigger appears.

```yaml
mandatory_role_triggers:
  ATHENA:
    - complex_task
    - architecture_decision
    - scope_split_required
    - multi_step_workflow

  ARGOS:
    - factual_claim
    - external_reference
    - legal_or_regulatory_source
    - source_required
    - evidence_gap
    - freshness_risk
    - provenance_unclear

  THEMIS:
    - approval_required
    - legal_or_professional_risk
    - external_effect
    - protected_file
    - memory_promotion
    - policy_conflict
    - liability_risk

  APOLLO:
    - public_readme
    - client_explanation
    - unclear_output
    - narrative_or_editorial_work
    - delivery_quality_required

  HEPHAISTOS:
    - patch_candidate
    - file_creation
    - template_creation
    - implementation_candidate
    - artifact_fabrication

  IRIS:
    - external_transmission
    - client_delivery
    - public_output
    - handoff_required
    - recipient_specific_format

  ZEUS:
    - always_procedural
```

## Domain pack anatomy

A professional domain pack should define:

```yaml
domain_id: architecture
status: candidate
scope: project
purpose: govern architecture-related professional dossier work
mandatory_roles:
  - ATHENA
  - ARGOS
  - THEMIS
optional_roles:
  - APOLLO
  - HEPHAISTOS
  - IRIS
required_evidence:
  - source_status
  - scope_status
  - assumptions
  - limitations
approval_gates:
  - professional_review_required_before_external_reliance
memory_policy:
  - memory_candidate_only_by_default
skill_candidates: []
openwebui_templates: []
```

A domain pack should also define:

- FOR;
- NOT FOR;
- source expectations;
- freshness requirements;
- role activation defaults;
- approval implications;
- memory implications;
- external transmission constraints;
- skill eligibility constraints;
- user decision triggers.

## Example domain: architecture

The architecture domain may support professional dossier work such as:

- CCTP and descriptive notes;
- quote or devis analysis;
- site observation notes;
- administrative dossier framing;
- accessibility or ERP notice drafting;
- material or equipment comparison;
- project-scope memory candidates;
- client-facing explanation drafts.

Default posture:

```yaml
domain_id: architecture
status: candidate
professional_reliance: draft_only_until_review
mandatory_roles:
  - ATHENA
  - ARGOS
  - THEMIS
role_defaults:
  APOLLO: active_for_client_facing_output
  HEPHAISTOS: active_for_artifact_or_template_creation
  IRIS: active_for_external_transmission
required_gates:
  - source_scope_check
  - professional_review_before_reliance
  - external_transmission_gate
memory_policy:
  - project_scoped_memory_candidate_only
```

Architecture domain activation must not imply:

- automatic architectural advice;
- automatic code compliance;
- automatic regulatory validity;
- replacement of architect judgment;
- automatic client transmission;
- automatic memory promotion.

## Example domain: legal

The legal domain may support legal-note drafting, legal-source review and issue framing.

Default posture:

```yaml
domain_id: legal
status: candidate
professional_reliance: draft_only_until_lawyer_review
mandatory_roles:
  - ARGOS
  - THEMIS
  - ZEUS
role_defaults:
  ATHENA: active_for_issue_framing
  APOLLO: active_for_plain_language_summary
  IRIS: active_for_external_transmission
required_gates:
  - source_freshness_check
  - jurisdiction_scope_check
  - professional_review_before_reliance
  - external_transmission_gate
memory_policy:
  - sensitive_scope_required
  - memory_candidate_only_by_default
```

Legal domain activation must not imply:

- legal advice authority;
- lawyer substitution;
- automatic legal validity;
- automatic source sufficiency;
- automatic external sending;
- automatic memory promotion.

## Domain dependency rules

Domain packs may depend on parent governance surfaces.

Examples:

```yaml
domain_dependencies:
  architecture:
    requires:
      - task_contract_surface
      - evidence_surface
      - approval_gate_pack
      - memory_policy_pack
    enables_if_authorized:
      - architecture_dossier_templates
      - cctp_review_candidate
      - devis_analysis_candidate
    blocks_if_disabled:
      - architecture_skill_candidates
      - architecture_memory_candidates
      - architecture_external_transmission

  legal:
    requires:
      - task_contract_surface
      - source_freshness_policy
      - evidence_surface
      - professional_review_gate
      - memory_policy_pack
    enables_if_authorized:
      - legal_note_template
      - legal_source_review_candidate
    blocks_if_disabled:
      - legal_skill_candidates
      - legal_memory_candidates
      - legal_external_transmission
```

## Skill-domain relationship

A skill candidate may require a domain pack.

A domain pack may make a skill candidate eligible.

Neither relationship authorizes execution by itself.

```text
Domain enabled
→ skill candidate eligible
→ Task Contract authorizes skill for this task
→ Hermes executes if allowed
→ Evidence Pack returns
→ Pantheon reviews status
```

## Skill candidate anatomy

Recommended fields:

```yaml
skill_id: architecture_devis_analysis_candidate
status: candidate
owner_layer: hermes
requires_domain:
  - architecture
for:
  - compare_quotes_against_project_scope
  - identify_missing_items
  - flag_cost_or_scope_risks
not_for:
  - final_contractual_decision
  - legal_liability_opinion
  - automatic_client_instruction
required_inputs:
  - task_contract
  - selected_quotes
  - project_scope
  - evidence_requirements
forbidden_inputs:
  - unscoped_client_history
  - unrelated_project_memory
required_outputs:
  - analysis_candidate
  - assumptions
  - evidence_notes
  - missing_information
  - approval_implications
approval_ceiling: candidate_only
memory: memory_candidate_only_if_explicit
```

## Example skill-domain candidates

Architecture candidates:

```text
architecture_devis_analysis_candidate
architecture_cctp_review_candidate
architecture_accessibility_notice_candidate
architecture_material_moodboard_review_candidate
architecture_site_observation_summary_candidate
```

Legal candidates:

```text
legal_source_review_candidate
legal_note_draft_candidate
legal_issue_framing_candidate
legal_contradiction_summary_candidate
legal_freshness_check_candidate
```

These names are illustrative.

They are not installed skills.

They are not approved capabilities.

## Cross-domain activation

Some tasks may activate several domains.

Example:

```yaml
enabled_domains:
  - architecture
  - legal
reason: construction_dispute_or_contractual_risk
mandatory_roles:
  - ATHENA
  - ARGOS
  - THEMIS
  - ZEUS
additional_gates:
  - source_freshness_check
  - jurisdiction_scope_check
  - professional_review_before_reliance
  - external_transmission_gate
```

Cross-domain activation increases risk.

It should generally raise approval and evidence requirements.

## Domain and role dependency examples

Architecture tends to require:

```text
ATHENA for scope and sequencing.
ARGOS for sources, documents and traceability.
THEMIS for liability, approval and professional boundary.
APOLLO for client-readable deliverables.
HEPHAISTOS for artifact candidates.
IRIS for transmission.
ZEUS for workflow and status arbitration.
```

Legal tends to require:

```text
ARGOS for source, version, jurisdiction and freshness.
THEMIS for risk, contradiction and approval boundary.
ZEUS for procedural status and escalation.
ATHENA for issue structure.
APOLLO for plain-language explanation.
IRIS for controlled transmission.
```

## Disable effects

Disabling a role, domain or skill should have visible effects.

Examples:

```yaml
disable_architecture_domain:
  blocks:
    - architecture_skill_candidates
    - architecture_domain_templates
    - architecture_memory_candidate_review
    - architecture_external_transmission_as_domain_output
  preserves:
    - generic_governance_review
    - generic_evidence_pack_display

:disable_legal_domain:
  blocks:
    - legal_skill_candidates
    - legal_note_templates
    - legal_memory_candidate_review
    - legal_external_transmission_as_domain_output
  preserves:
    - generic_source_review
    - generic_risk_note

:disable_themis:
  allowed_only_when:
    - no_approval_risk
    - no_professional_risk
    - no_external_effect
    - no_protected_file
  reactivates_when:
    - approval_required
    - liability_risk
    - memory_promotion
    - external_transmission
```

## Draft-only professional rule

Professional domains default to draft-only until human professional review.

```text
Domain activation may prepare.
It may not professionally validate.
```

This applies especially to:

- architecture;
- legal;
- medical;
- financial;
- regulatory;
- contractual;
- insurance;
- construction dispute contexts.

## Memory rule

Domain activation does not promote memory.

Skill output does not promote memory.

Role signal output does not promote memory.

A durable domain claim may become a Memory Candidate only if it includes:

- claim;
- scope;
- source or evidence;
- confidence;
- risk;
- review horizon;
- approval state.

## OpenWebUI exposure

OpenWebUI may expose:

- active roles;
- standby roles;
- disabled roles;
- mandatory roles;
- enabled domains;
- disabled domains;
- eligible skill candidates;
- blocked skill candidates;
- role readiness brief;
- Zeus session workflow;
- Effective Policy;
- dependency blockers.

OpenWebUI must not:

- make a role autonomous;
- make a domain authoritative;
- install a skill;
- execute a skill;
- approve a professional output;
- promote memory;
- bypass mandatory reactivation triggers.

## Hermes execution

Hermes may execute a skill candidate only when:

- the relevant domain is enabled when required;
- the Task Contract authorizes the skill;
- the skill has FOR and NOT FOR boundaries;
- allowed tools are declared;
- evidence return is required;
- approval ceiling is explicit;
- memory rule is explicit.

Hermes must not treat a domain pack as professional authority.

## Zeus workflow composition

Zeus should compose the minimal safe workflow from:

- user request;
- enabled roles;
- standby roles;
- disabled roles;
- mandatory role triggers;
- enabled domain packs;
- eligible skill candidates;
- task risk;
- scope;
- external effect;
- memory implication;
- evidence requirement.

Zeus may propose:

- minimal workflow;
- expanded workflow;
- blocked workflow;
- User Decision Gate;
- domain activation request;
- role reactivation request;
- skill task authorization request.

Zeus does not decide truth.

Zeus arbitrates status and procedure.

## Relationship to Module Activation

`MODULE_ACTIVATION.md` defines generic detection, activation and task authorization semantics.

This document specializes them for:

- Pantheon Roles;
- professional domains;
- Hermes skill candidates.

## Relationship to Governance College

`GOVERNANCE_COLLEGE.md` defines why roles exist.

This document defines how roles may be activated, deactivated or reactivated by risk.

## Relationship to Skill Watchlist

`SKILL_WATCHLIST.md` watches external skills.

This document defines how a candidate skill may become eligible inside a domain and task scope.

Watching a skill is not activation.

Activating a skill candidate is not task authorization.

Task authorization is not approval.

## Relationship to OpenWebUI Templates

`OPENWEBUI_TEMPLATES.md` defines future cockpit surfaces.

This document defines what those surfaces may display for roles, domains and skills.

## Forbidden drift

Role, domain or skill activation must never become:

- autonomous role agents;
- hidden multi-agent runtime;
- profession-specific AI authority;
- skill marketplace;
- automatic skill installer;
- automatic domain expert;
- automatic approval;
- automatic memory promotion;
- OpenWebUI runtime;
- Pantheon runtime.

## Final rule

```text
Activate roles to reveal tensions.
Activate domains to constrain context.
Activate skills only as task-bound Hermes candidates.
Validate nothing by activation alone.
```