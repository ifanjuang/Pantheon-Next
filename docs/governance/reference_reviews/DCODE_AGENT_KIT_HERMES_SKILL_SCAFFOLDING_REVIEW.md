# dcode-agent-kit — Hermes Skill Scaffolding Placement Review

Status: external reference / support review — candidate only.

Date: 2026-06-28

External source reviewed:

```text
https://github.com/EliaAlberti/dcode-agent-kit
```

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## What it is

`dcode-agent-kit` is a Claude Code skill and plugin package centered on `/new-dcode-agent`.

The useful pattern is not a new Pantheon runtime. The useful pattern is a bounded scaffolding sequence:

```text
interview
-> spec
-> explicit confirmation
-> scaffold
-> smoke-test
```

The generated artifact may be a standalone Deep Agents SDK program, a dcode CLI agent, or both. The generated agent is self-contained, provider-agnostic through environment variables, and may add an approval gate for mutating tools.

## Initial qualification

Accepted:

```text
as an external reference for capability / skill candidate scaffolding;
as an inspiration for a Hermes-side skill generator or adapter pattern;
as a useful example of interview -> spec -> confirmation -> scaffold -> smoke-test;
as a reminder that mutating tools require a verified approval pause;
as a source for card-stack vocabulary around Capability Candidate, Skill Candidate and Gate cards.
```

Refused:

```text
as Pantheon runtime;
as Pantheon skill installer;
as autonomous agent authority;
as Governance College role authority;
as source of truth;
as Evidence Pack by itself;
as approval engine;
as memory engine;
as automatic capability admission;
as automatic external-action authorization;
as a dependency to install in Pantheon Next.
```

To verify:

```text
whether Hermes should later receive a bounded skill-scaffolding adapter;
whether existing SKILL_LIFECYCLE and CAPABILITY_PLACEMENT documents already cover all needed gates;
whether card-stack vocabulary needs a dedicated Capability Candidate sub-card shape;
whether smoke-test evidence should become part of a Capability Evidence Pack Candidate;
whether any generated dcode agent memory file can be safely treated only as runtime context, never as Registre Probatoire.
```

To arbitrate:

```text
whether a future Hermes skill generator is worth building;
whether generated skills should enter through SKILL_LIFECYCLE, CAPABILITY_REGISTRY, or a narrower Capability Candidate card;
whether card-stack changes should wait for the open method-card / card-stack reconciliation PRs.
```

Repo state:

```text
documented non-implemented
```

No runnable Hermes skill is installed. No dependency, agent generator, scaffold command, Claude plugin, Deep Agents runtime, dcode CLI configuration, schema, test, operation, platform file, Docker file, `.env` file or external action is added by this review.

## Placement

```yaml
reference_review:
  reviewed_item: dcode-agent-kit
  source_url: https://github.com/EliaAlberti/dcode-agent-kit
  authority_class: external_reference
  repo_state: documented_non_implemented
  pantheon_use:
    - scaffolding_pattern_reference
    - capability_candidate_vocabulary
    - skill_lifecycle_boundary_check
  refused_as:
    - pantheon_runtime
    - skill_installer
    - approval_engine
    - memory_engine
    - source_of_truth
    - role_authority
```

Candidate module placement, if a future adapter is ever proposed:

```yaml
module_manifest_candidate:
  id: hermes-skill-scaffolding-adapter
  owner_layer: execution_runtime
  type: skill
  status: candidate
  activation:
    state: unavailable
    scope: task
  task_authorization:
    state: unauthorized
  interface:
    allowed_inputs:
      - task_contract
      - capability_candidate
      - skill_purpose
      - tool_scope
      - mutation_policy
      - model_policy
    allowed_outputs:
      - skill_scaffold_candidate
      - spec_candidate
      - smoke_test_observation_candidate
      - capability_gap
      - evidence_pack_candidate
    forbidden_outputs:
      - approved_capability
      - installed_skill_authority
      - final_approval
      - canonical_memory
      - registre_probatoire_entry
      - unapproved_external_effect
      - doctrine_mutation
  governance:
    consequential: true
    risk_level: high
    approval_behavior: C3_or_higher_if_mutating
    memory_behavior: never_canonical
    scope_behavior: strict_task_scope
```

## Card-stack implication

This review suggests one card-stack refinement, but does not apply it directly to `CARD_STACK_MODEL.md` because card-stack and method-card reconciliation is already active in open PR discussions.

Candidate vocabulary:

```text
Capability Candidate Card
Skill Candidate Card
Scaffold Spec Card
Smoke-test Observation Candidate
Capability Gap
Gate Zeus
```

Suggested card rule:

```text
Capability / Skill Candidate appears as a field when normal.
It becomes a visible sub-card only when it is missing, newly proposed, mutating, failed, repeated, blocked, or requires arbitration.
```

Minimum Capability Candidate card fields:

```yaml
capability_candidate_card:
  title:
  source:
  purpose:
  proposed_runtime_projection:
  owner_layer:
  type:
  task_contract_ref:
  allowed_inputs:
  allowed_outputs:
  forbidden_outputs:
  mutation_possible:
  approval_required:
  evidence_expectation:
  smoke_test_required:
  smoke_test_observation:
  capability_gap:
  memory_behavior:
  external_effect:
  zeus_status:
  decision_owner:
  trace_refs:
```

This card does not authorize installation, execution, memory promotion, truth status, approval or external action. It only makes the candidate visible for review.

## Boundary with dcode agents and AGENTS.md

A dcode agent identity or `AGENTS.md` file remains runtime-side context.

It must not be confused with:

```text
Pantheon Role authority;
Governance College participation;
approved competence;
canonical memory;
Registre Probatoire entry;
Evidence Pack;
external-action approval.
```

A generated agent may assist execution only under a bounded Task Contract and must return candidates.

```text
Task Contract in
-> execution runtime / generated skill candidate
-> Result Candidate + Evidence Pack Candidate out
```

## Approval-gate lesson

The external reference is useful because it makes a concrete technical point: a mutating tool needs a real interrupt / checkpoint mechanism, and smoke-test verification must prove that the gate actually pauses.

Pantheon should treat that as evidence about runtime posture only.

```text
technical pause observed != governance approval
smoke-test passed != capability admitted
agent scaffolded != skill approved
runtime identity != Pantheon role
AGENTS.md context != Registre Probatoire
```

## Candidate phase sequence

```text
Phase 0 — reference review only, no install.
Phase 1 — compare against SKILL_LIFECYCLE and CAPABILITY_PLACEMENT.
Phase 2 — decide whether Capability Candidate card vocabulary should be folded into CARD_STACK_MODEL.md.
Phase 3 — if useful, draft a Hermes-side scaffold template outside the kernel.
Phase 4 — require bounded Task Contract, Capability Gap behavior and smoke-test observation before any sandbox use.
```

## Boundary note

`dcode-agent-kit` should not be added to Pantheon Next as a dependency. If a similar pattern is used, it belongs in Hermes or another execution runtime as an adapter that reads Pantheon doctrine and returns candidates. Pantheon governs admission, status, evidence, approval, memory, scope and external action boundaries.

The validated remains.
