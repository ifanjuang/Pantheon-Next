# Pantheon MVP Vertical Binding

Status: candidate support doctrine — documented non-implemented / external executable binding candidate.

Boundary profile: candidate_support_note.

This document classifies the external `pantheon-mvp` repository target and the `pantheon-mvp-vertical` bundle family as a candidate binding for a bounded governed task loop.

It does not import the bundle into Pantheon Next.

It does not approve installation, execution, activation, adoption, deployment, memory promotion, external send, provider routing or professional validation.

## Source under review

```text
working name: pantheon-mvp-vertical
published repository target: https://github.com/ifanjuang/pantheon-mvp
published repository status observed through GitHub connector: public / initialized / main branch
observed artifact: pantheon-mvp-vertical.bundle
observed commit: 4ce16b7
commit subject: feat: Block 1 of the Pantheon MVP governed task loop
tracked files: 19
vendored Pantheon commit: 58d6bef
```

Follow-up status reported from the external bundle handoff, not independently verified by Pantheon Next in this repository:

```text
reported successor artifact: pantheon-mvp-vertical 2.bundle
reported scope: Block 2 — decision gate / review screen / signed decision trace
reported tests: 12/12 local tests
reported new files: gate.py and additional acceptance tests
verification status: to_verify after external repository push and CI run
```

The GitHub repository now exists as `ifanjuang/pantheon-mvp`, but repository existence is not adoption, activation, pushed executable content, CI evidence or professional validation.

Bundle observations and handoff reports are candidate review inputs only.

The original bundle had a Git packaging quirk: cloning it may leave no checked-out local branch because the bundle's remote HEAD is not set to `origin/main`. The safe checkout pattern is:

```bash
git clone pantheon-mvp-vertical.bundle pantheon-mvp-vertical
cd pantheon-mvp-vertical
git switch -c main origin/main
```

## Abstract capability slot

```text
capability_slot: governed_task_loop_mvp_vertical
abstract_function: bounded Task Contract ingestion, scope-filtered retrieval, candidate return and human decision gate trace
candidate_binding: ifanjuang/pantheon-mvp
execution_owner: external repository / future Hermes-side or human-run adapter
pantheon_role: govern status, scope, evidence posture, activation, refusal and approval gates
```

## Role distribution

| Layer | This vertical slice uses | Correct final reading |
|---|---|---|
| Pantheon | vendored schemas, status rules, refusal/evidence/approval vocabulary | Governs contracts, scope, evidence status, decision gates and non-equivalence rules. |
| Hermes | deterministic `runner.py` stand-in | Real Hermes later occupies this slot under the same Task Contract and tests. |
| OpenWebUI | terminal `gate.py` stand-in reported in Block 2 | OpenWebUI later exposes review surfaces and captures decisions; it does not govern. |
| Human | explicit signed decision record | Human approval remains required for consequential use. |

The external code is useful only if this distribution remains visible. The stand-ins prove the cage; they are not the final occupants.

## Observed Block 1 execution shape

The original bundle contains:

```text
Python package: mvp_vertical
Database boundary: pgvector service in docker-compose
Contract loader: mvp_vertical.contract
Deterministic local embedder: mvp_vertical.embedder
Scope-first store: mvp_vertical.store
Deterministic runner: mvp_vertical.runner
CLI: mvp_vertical.cli
Fixture dossier: dossiers/devis_reprise
Vendored schema/validator material: vendor/pantheon
CI workflow: .github/workflows/ci.yml
Acceptance tests: tests/test_block1.py
```

The runner produces data objects such as:

```text
result_candidate
evidence_pack_candidate
refused_capability_gap
```

The observed design keeps Block 1 deterministic: no LLM call is required for the drafting step, and model/provider exposure is deferred to later blocks.

## Reported Block 2 execution shape

The follow-up handoff reports a decision gate layer:

```text
terminal review surface: gate.py
user choices: approve | refuse | request_revision | request_more_evidence
signed decision trace: dated file with actor, reason and decision
system signer refusal: a decision signed by system is refused
external action refusal: draft preparation remains separate from send authorization
reported total tests: 12/12
```

This is promising because it exercises the User Decision Gate without requiring the final OpenWebUI surface.

The status remains `to_verify` until the external repository is pushed, CI is visible, and the changed files are reviewed against this document.

## Naming rule for stand-ins

Before adoption, any file that occupies another actor's seat must say so in its name or header.

Required clarification:

```text
mvp_vertical/runner.py -> mvp_vertical/hermes_standin_runner.py
```

or an equivalent explicit header stating:

```text
This runner is a deterministic Hermes stand-in.
It exists only to test the governed cage: scope, refusal, evidence shape, commitment flags and decision gates.
It is not Hermes Agent.
It must be replaced by a real Hermes binding.
The acceptance tests remain authoritative.
```

Likewise, `gate.py` must be classified as an OpenWebUI stand-in or terminal review stand-in. It must not be presented as a live cockpit.

## What Pantheon governs

Pantheon may govern:

```text
capability-slot classification
source and bundle provenance status
adoption status
activation status
scope boundaries
Task Contract status
candidate result status
evidence-pack candidate status
commitment-risk flags
external-send refusal
memory-promotion refusal
human decision gate
update review
rollback visibility
```

Pantheon may display the external binding as a governed resource or capability candidate.

Pantheon must not treat the external runtime's success as evidence validation or approval.

## What the external binding executes

The external binding may execute, if separately installed and run outside Pantheon:

```text
load a declared Task Contract
ingest declared sources into pgvector
chunk and embed declared sources
retrieve with SQL perimeter filtering before vector ranking
produce a deterministic draft candidate
produce an evidence-pack candidate
produce refusal/capability-gap reports
render a terminal review gate
record a signed decision trace
run acceptance tests against pgvector and gate fixtures
```

This is external execution. It is not Pantheon execution.

## What OpenWebUI may expose

OpenWebUI may later expose:

```text
capability card
run status
candidate output
refusal output
evidence-pack candidate
commitment-risk flags
review gate prompt
activation warning
signed decision trace
```

OpenWebUI display must not become approval, evidence validation, memory admission, external send or runtime authority.

## Human approval points

Human approval is required for:

```text
pushing executable content into the external repository
adopting this candidate binding
running it on a real dossier
changing the Task Contract perimeter
accepting any result candidate
treating any evidence-pack candidate as validated evidence
sending any message externally
writing to any register
promoting any memory
updating the external binding
replacing the deterministic embedder
replacing the deterministic stand-in runner with a real Hermes/LLM binding
```

## Required fixes before adoption

### P0 — Task Contract schema alignment

The fixture Task Contract observed in the original bundle uses `declared_scope` and `expected_output` while the vendored schema expects `scope` and `expected_outputs` for `task_contract` objects.

Before adoption, one of these must be true:

```text
fixture contract validates against the vendored schema; or
the schema is updated by a reviewed Pantheon decision; or
the fixture dialect is explicitly documented as local and non-authoritative.
```

Preferred fix: align the fixture and add a test named along these lines:

```text
test_task_contract_validates_against_vendored_schema
```

### P0 — Source path boundary

The observed ingestion path joins `root / source_ref` after checking that the string was declared in the contract.

Before adoption, source resolution must also prove that the resolved path stays under the declared workspace root and refuses absolute paths, `..` escapes and symlink escapes.

Preferred helper shape:

```text
resolve_under_root(root, source_ref) -> resolved_path
```

### P0 — Stand-in naming and status

The deterministic runner must be renamed or locally labelled as a Hermes stand-in before adoption.

The terminal decision gate must be labelled as an OpenWebUI stand-in or terminal gate stand-in.

This prevents the external repo from being read as the final Hermès/OpenWebUI implementation.

### P0 — Gate decision semantics

The decision trace must preserve at least:

```text
actor
actor_type: human | system | runtime
selected_gate_option
reason
linked_result_candidate
linked_evidence_pack_candidate
approval_scope
external_action_authorized
memory_promotion_authorized
created_at
```

A `system` actor must never approve.

A decision on a draft must not authorize external sending unless the gate explicitly records that effect.

### P1 — Unit tests without pgvector

The bundle includes pgvector-backed acceptance tests. Before adoption, it should also include always-on unit tests for:

```text
contract loading
schema validation
path-boundary validation
forbidden operation detection
deterministic embedder shape
output status vocabulary
gate option vocabulary
system-signer refusal
```

### P1 — External repo governance status file

The external repo should add a small `GOVERNANCE_STATUS.md` stating that it executes a stand-in vertical slice and does not govern, approve, send, remember, validate truth, schedule, route providers or promote memory.

### P1 — Vendored upstream freshness

The vendored Pantheon commit `58d6bef` must be compared with the current Pantheon Next main branch before adoption. A stale vendored schema may still be useful for a bundle review, but it cannot be treated as current authority.

## Non-equivalence rules

```text
bundle_exists ≠ repository_published
repository_exists ≠ executable_content_pushed
repository_published ≠ binding_adopted
binding_adopted ≠ activated
six_tests_exist ≠ six_tests_currently_verified_by_pantheon
twelve_tests_reported ≠ twelve_tests_currently_verified_by_pantheon
ci_green ≠ professional_evidence
retrieved ≠ true
result_candidate ≠ approved_result
evidence_pack_candidate ≠ validated_evidence
runtime_success ≠ approval
deterministic_output ≠ safe_output
source_declared ≠ path_safe
schema_vendored ≠ schema_current
stand_in_runner ≠ Hermes Agent
terminal_gate ≠ OpenWebUI cockpit
external_repo ≠ Pantheon runtime
```

## Capability Slot record

```yaml
capability_slot: governed_task_loop_mvp_vertical
function: bounded retrieval, candidate generation and human decision trace under Task Contract
candidate_binding: ifanjuang/pantheon-mvp
binding_status: candidate / external executable / not adopted
installation_status: not installed by Pantheon
health_status: to_verify
update_status: to_verify
activation_status: blocked_until_p0_fixes
pantheon_gates:
  - source_perimeter_gate
  - schema_alignment_gate
  - path_boundary_gate
  - evidence_status_gate
  - commitment_risk_gate
  - external_action_gate
  - memory_gate
  - human_approval_gate
human_approval_required_for:
  - adoption
  - activation
  - real_dossier_use
  - perimeter_change
  - output_acceptance
  - external_send
  - memory_promotion
```

## Status classification

```text
implemented in Pantheon Next:
  none.

documented non-implemented in Pantheon Next:
  external binding classification, adoption gates and review findings.

published external repository observed:
  ifanjuang/pantheon-mvp exists and is initialized, but executable MVP content is not verified here.

implemented externally, observed from original bundle only:
  Block 1 vertical code, fixtures, tests and CI definition.

reported externally, not independently verified here:
  Block 2 terminal gate, signed decision trace and 12/12 tests.

partial:
  scope-filtered retrieval, candidate-output shape and reported decision gate are promising but adoption is blocked by P0 fixes.

to verify:
  executable content push to pantheon-mvp, CI result after push, vendored schema freshness, P0 fixes, future Hermes/OpenWebUI integration.
```

## Final rule

```text
Pantheon may govern this binding.
Pantheon must not become this binding.
```
