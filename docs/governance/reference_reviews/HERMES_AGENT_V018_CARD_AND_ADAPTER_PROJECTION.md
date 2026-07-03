# Hermes Agent v0.18.0 — Adapter and Card Projection Candidate

Status: external reference / support projection — candidate only.

Date: 2026-07-03

Related review:

```text
docs/governance/reference_reviews/HERMES_AGENT_V018_RELEASE_REVIEW.md
```

Related active doctrine:

```text
docs/governance/HERMES_INTEGRATION.md
docs/governance/CARD_STACK_MODEL.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/SKILL_LIFECYCLE.md
```

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

This projection turns the Hermes Agent v0.18.0 release review into candidate adapter and cockpit-card implications.

It is a working projection only. It does not modify `HERMES_INTEGRATION.md`, does not modify `CARD_STACK_MODEL.md`, does not create a UI, does not create a renderer, does not install Hermes, does not create a skill, does not create a provider route and does not authorize a runtime capability.

The intent is to prepare later arbitration without silently promoting the release note into doctrine.

## Placement posture

Hermes v0.18.0 adds or strengthens runtime affordances. Pantheon classifies the consequences.

```text
runtime affordance -> adapter mapping candidate
runtime evidence -> Evidence Pack Candidate input
runtime memory -> Runtime Memory Candidate
runtime skill generation -> Skill Candidate
runtime model ensemble -> Viewpoint / Divergence / Synthesis Candidates
runtime fan-out -> delegated execution under Task Contract
```

Forbidden collapse:

```text
runtime done -> approved
runtime evidence -> proof
runtime memory -> Registre Probatoire
learned skill -> admitted competence
MoA aggregator -> Zeus
fan-out -> scope expansion
release maturity -> capability approval
```

## Candidate adapter mapping

| Hermes v0.18 surface | Adapter object candidate | Effect class | Required Pantheon gate |
|---|---|---|---|
| `/goal` completion contracts | `goal_completion_candidate` | read_only / internal_state_change | Task Contract + Evidence Pack Candidate review |
| Verification evidence ledger | `verification_evidence_candidate` | read_only | Evidence Pack review; no self-approval |
| `pre_verify` hook | `runtime_check_policy_binding` | read_only / internal_state_change | evidence expectation and adapter-version review |
| MoA first-class provider | `moa_viewpoint_bundle_candidate` | read_only | model/capability passport; synthesis remains candidate |
| Labelled reference-model outputs | `viewpoint_candidate` / `divergence_candidate` | read_only | claim-level evidence review before relying on conclusions |
| Streaming aggregator answer | `synthesis_candidate` | read_only | status remains candidate until review |
| `/learn` skill distillation | `learned_skill_candidate` | internal_state_change | SKILL_LIFECYCLE admission, capability passport, source review |
| `/journey` memory timeline | `runtime_memory_candidate` | read_only / internal_state_change | memory review; Registre Probatoire promotion forbidden by runtime |
| Desktop radial memory graph | `memory_visibility_view` | read_only | cockpit display only |
| Background `delegate_task` fan-out | `delegate_fanout_candidate` | read_only / internal_state_change | linked Task Contract, delegated scope, trace refs, outcome observation |
| Desktop coding Projects | `runtime_project_surface` | internal_state_change | repository/protected-path discipline; Patch Candidate only |
| Gateway scale-to-zero / drain | `runtime_lifecycle_signal` | read_only | observability only; no governance status change |
| Auxiliary-model self-review | `self_review_candidate` | internal_state_change | may propose Register Candidates; no promotion |
| `/prompt` editor flow | `input_preparation_surface` | read_only | no gate unless consequential content enters task scope |
| Vertex AI provider support | `provider_capability_candidate` | read_only / internal_state_change | model passport before consequential use |
| Security hardening | `runtime_security_signal` | read_only | reduces risk signal; does not replace gates |

## Candidate card projection

If later folded into `CARD_STACK_MODEL.md`, these cards should remain display and review grammar. They must not create execution authority.

### Goal Contract Card

Purpose:

```text
display the requested done condition, linked Task Contract, runtime checks and completion status.
```

Minimum fields:

```yaml
goal_contract_card:
  linked_task_contract:
  declared_done_condition:
  checks_expected:
  checks_run:
  checks_failed_or_skipped:
  runtime_completion_status: success | partial | failed | blocked | unknown
  governance_status: candidate | to_verify | approved | rejected | blocked
  evidence_refs:
  trace_refs:
```

Visible warning:

```text
Hermes done does not mean Pantheon approved.
```

### Verification Evidence Card

Purpose:

```text
show what Hermes actually checked before claiming work is done.
```

Minimum fields:

```yaml
verification_evidence_card:
  source_runtime: hermes
  check_family: tests | lint | typecheck | command | diff_review | manual_runtime_observation
  command_or_method:
  result:
  failures:
  skipped_items:
  limitation:
  evidence_pack_candidate_ref:
```

Visible warning:

```text
verification evidence is candidate evidence, not self-approving proof.
```

### MoA Divergence Card

Purpose:

```text
show model disagreement without turning disagreement into arbitration.
```

Minimum fields:

```yaml
moa_divergence_card:
  model_outputs:
  disagreement_points:
  convergence_points:
  claim_requiring_source:
  unresolved_risk:
  synthesis_candidate_ref:
  arbitration_required: true | false
```

Visible warning:

```text
MoA is not the Governance College. Zeus still arbitrates status where required.
```

### Learned Skill Candidate Card

Purpose:

```text
surface a Hermes-generated skill draft for admission review.
```

Minimum fields:

```yaml
learned_skill_candidate_card:
  origin: directory | url | observed_workflow | session_trace
  generated_skill_ref:
  claimed_reusable_scope:
  source_material_refs:
  forbidden_effects:
  required_capability_passport:
  admission_status: candidate | to_verify | admitted | rejected | blocked
```

Visible warning:

```text
a learned skill is not an approved competence.
```

### Runtime Memory Candidate Card

Purpose:

```text
show what Hermes thinks it remembers, so drift can be rejected, kept runtime-local or proposed for governed register review.
```

Minimum fields:

```yaml
runtime_memory_candidate_card:
  origin_runtime: hermes
  runtime_memory_ref:
  statement_summary:
  scope:
  source_or_event_ref:
  proposed_action: keep_runtime_local | reject | propose_register_candidate
  register_promotion_allowed: false
  review_status: candidate | to_verify | rejected | routed_to_register_review
```

Visible warning:

```text
runtime memory is not the Registre Probatoire.
```

### Delegate Fan-out Card

Purpose:

```text
show delegated runtime work and keep scope, evidence and status visible.
```

Minimum fields:

```yaml
delegate_fanout_card:
  linked_task_contract:
  delegates:
  delegated_scopes:
  consolidated_result_candidate:
  evidence_refs:
  trace_refs:
  scope_gaps:
  blocked_items:
  approval_still_required:
```

Visible warning:

```text
parallel execution does not expand scope or lower approval.
```

### Gateway Health Card

Purpose:

```text
show runtime service health without implying governance validity.
```

Minimum fields:

```yaml
gateway_health_card:
  runtime:
  version:
  lifecycle_state:
  drain_state:
  last_seen:
  degraded_capabilities:
  adapter_version_status: reviewed | to_verify | blocked
```

Visible warning:

```text
healthy runtime does not mean approved capability.
```

## Decision surface implications

The exposure surface may display these cards when useful, but it must keep the action vocabulary narrow:

```text
inspect;
request evidence;
request revision;
reject candidate;
route to Task Contract;
route to Skill Lifecycle;
route to User Decision Gate;
route to Register review.
```

Forbidden exposure-surface actions:

```text
approve automatically;
promote memory automatically;
install skill automatically;
send externally;
merge code;
select provider by itself;
resolve MoA disagreement as final truth.
```

## Relationship with open PRs and discussions

This projection must not silently supersede open work.

Relevant signals at time of writing:

```text
PR #266: tripartite interfaces and MCP V0 refusal posture.
PR #265: Forever Components card-affordance review.
Issue #118: Hermes-first external modules shortlist.
Issue #192: Intent Candidate log in Pantheon Control.
```

Classification:

```text
Accepted: compatibility with the tripartite interface direction and card-affordance review as candidate references.
Refused: direct promotion into doctrine or UI implementation.
To verify: whether this projection should merge into HERMES_INTEGRATION.md, CARD_STACK_MODEL.md, DECISION_SURFACE_SPEC.md or a future adapter note.
To arbitrate: whether the card candidates deserve a dedicated card-stack section after PR #265 / #266 reconciliation.
```

## Suggested next move

Do not implement UI first.

Recommended sequence:

```text
1. Verify local Hermes v0.18 surfaces and output shapes.
2. Compare actual outputs with this projection.
3. Distill only stable adapter objects into HERMES_INTEGRATION.md.
4. Distill only stable visual review objects into CARD_STACK_MODEL.md.
5. Leave executable configuration outside Pantheon.
```

## Boundary phrase

```text
Hermes v0.18 can make the runtime smarter.
Pantheon makes the consequences governable.
The card shows the tension.
The gate preserves the status.
The human decides.
```
