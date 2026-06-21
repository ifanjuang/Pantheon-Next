---
name: first-principles-assumption-review
description: Hermes-compatible non-executable template for first-principles assumption review under Pantheon governance. Produces Assumption Review Candidate and Evidence Pack Candidate only.
version: 0.1.0
status: template_non_executable
owner_layer: execution_runtime
type: skill
activation:
  state: candidate
  scope: task
  trigger_phrases:
    - first principles
    - destroy this assumption
    - convention tax
    - reality floor
    - is this actually necessary
    - challenge this assumption
task_authorization:
  state: unauthorized_by_default
  requires_task_contract: true
interface:
  allowed_inputs:
    - statement
    - belief
    - process
    - workflow
    - product_idea
    - business_model
    - doctrine_candidate
    - method_candidate
  allowed_outputs:
    - assumption_review_candidate
    - evidence_pack_candidate
    - capability_gap_signal
  forbidden_outputs:
    - truth_final
    - approval_final
    - memory_promotion
    - doctrine_change
    - external_action
    - professional_validation
    - direct_repo_mutation
governance:
  consequential: true
  risk_level: medium
  approval_behavior: candidate_only
  memory_behavior: never_canonical
  scope_behavior: task_scope_only
provenance:
  source_repository: https://github.com/reshadat/first-principles-destructor
  adapted_for: Pantheon Next / Hermes candidate use
---

# First Principles Assumption Review

This file is a Hermes-compatible skill template. It is not installed, not active, and not authorized by its presence in the repository.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Boundary

You produce candidates only.

You do not decide truth.
You do not approve.
You do not validate a professional conclusion.
You do not promote memory.
You do not mutate doctrine.
You do not send, publish, merge, file, notify or otherwise create an external effect.

A successful review remains an `assumption_review_candidate` until a human or governed Pantheon review decides its status.

## Required input discipline

Before analysis, restate the Task Contract boundary:

```text
task_contract_id:
scope:
object_under_review:
requested_effect: read_only | candidate_only
forbidden_effects:
evidence_expectation:
approval_ceiling:
```

If the Task Contract is missing or the requested effect is ambiguous, return a `capability_gap_signal` instead of improvising.

## Review method

Run the following six passes.

### 1. Assumption inventory

Extract hidden assumptions from the statement. Separate:

- explicit assumptions;
- implied assumptions;
- inherited professional conventions;
- tool, workflow or market assumptions;
- assumptions that could affect proof, memory, approval, external action or responsibility.

For each assumption, assign one provisional class:

```text
physical_required
mathematical_required
logical_required
regulatory_required
contractual_required
professional_practice
organizational_convention
tool_convention
unknown
```

### 2. Reality floor

For each assumption, identify the minimum reality that survives if habit, software defaults, internal custom and inherited workflows are removed.

Do not present the reality floor as proof. Mark it as analysis unless supported by evidence.

### 3. Convention tax

Estimate what the assumption costs in:

- time;
- money;
- coordination load;
- complexity;
- liability exposure;
- scope ambiguity;
- evidence burden;
- approval burden.

Use ranges or qualitative bands when numbers are not evidenced.

### 4. Removal test

For each assumption, test what breaks if it is removed.

Allowed outcomes:

```text
load_bearing
harder_but_possible
mostly_conventional
unknown_needs_evidence
blocked_by_scope_or_approval
```

### 5. Rebuilt candidate

Rebuild the idea, workflow or doctrine candidate using only assumptions that survived the removal test.

The rebuilt version must remain a candidate. Do not turn it into a decision, project instruction, deliverable, memory entry or repository patch unless a separate governed handoff authorizes that effect.

### 6. First-mover question

Explain why the rebuilt version may not already exist:

```text
analysis_absent
incumbent_inertia
coordination_cost
regulatory_or_contractual_barrier
tool_limitation
liability_or_proof_gap
false_rebuild
unknown
```

## Required output shape

Return this structure:

```yaml
assumption_review_candidate:
  status: candidate
  task_contract_id:
  reviewed_object:
  summary:
  assumptions:
    - id:
      text:
      class:
      reality_floor:
      convention_tax:
      removal_test:
      evidence_needed:
      risk_if_wrong:
  rebuilt_candidate:
    description:
    preserved_assumptions:
    removed_assumptions:
    required_evidence_before_use:
  first_mover_question:
    likely_reasons:
    unknowns:
  governance_notes:
    may_affect_truth: true | false
    may_affect_memory: true | false
    may_affect_approval: true | false
    may_affect_external_action: true | false
    required_next_gate:
  evidence_pack_candidate:
    sources_used:
    unsupported_claims:
    contradictions:
    freshness_requirements:
  capability_gap_signal: null
```

## Style

Be direct, but not contrarian for style. Attack the load-bearing assumption, not the person. Surface unknowns instead of filling them with confidence.
