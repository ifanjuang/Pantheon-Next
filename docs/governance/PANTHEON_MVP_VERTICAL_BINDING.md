# Pantheon MVP Vertical Binding

Status: candidate support doctrine — documented non-implemented / external executable binding candidate.

Boundary profile: runtime-adapter support / external executable candidate.

This document classifies the external `pantheon-mvp-vertical` bundle as a candidate binding for a bounded Block 1 governed task loop.

It does not import the bundle into Pantheon Next.

It does not approve installation, execution, activation, adoption, deployment, memory promotion, external send, provider routing or professional validation.

## Source under review

```text
working name: pantheon-mvp-vertical
candidate target repository: https://github.com/ifanjuang/pantheon-mvp-vertical
observed artifact: pantheon-mvp-vertical.bundle
observed commit: 4ce16b7
commit subject: feat: Block 1 of the Pantheon MVP governed task loop
tracked files: 19
vendored Pantheon commit: 58d6bef
```

At review time, the GitHub target repository was not treated as the authority source. The local bundle observation is a candidate review input only.

The bundle has a Git packaging quirk: cloning it may leave no checked-out local branch because the bundle's remote HEAD is not set to `origin/main`. The safe checkout pattern is:

```bash
git clone pantheon-mvp-vertical.bundle pantheon-mvp-vertical
cd pantheon-mvp-vertical
git switch -c main origin/main
```

## Abstract capability slot

```text
capability_slot: governed_task_loop_block_1
abstract_function: bounded Task Contract ingestion, scope-filtered retrieval and candidate return
candidate_binding: pantheon-mvp-vertical
execution_owner: external repository / future Hermes-side or human-run adapter
pantheon_role: govern status, scope, evidence posture, activation and approval gates
```

## Observed execution shape

The bundle contains:

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
produce a refusal/capability-gap report
run acceptance tests against pgvector
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
review gate prompt
activation warning
```

OpenWebUI display must not become approval, evidence validation, memory admission, external send or runtime authority.

## Human approval points

Human approval is required for:

```text
publishing the external repository
adopting this candidate binding
running it on a real dossier
changing the Task Contract perimeter
accepting any result candidate
treating any evidence-pack candidate as validated evidence
sending any message externally
writing to any register
promoting any memory
updating the external binding
replacing the deterministic embedder or adding an LLM/provider
```

## Required fixes before adoption

### P0 — Task Contract schema alignment

The fixture Task Contract observed in the bundle uses `declared_scope` and `expected_output` while the vendored schema expects `scope` and `expected_outputs` for `task_contract` objects.

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

### P0 — Fixture-specific drafting status

The current runner is a deterministic vertical slice for the fictional `devis_reprise` fixture. It should be labelled as a fixture-specific Block 1 demonstrator, not a general professional answer engine.

### P1 — Unit tests without pgvector

The bundle includes pgvector-backed acceptance tests. Before adoption, it should also include always-on unit tests for:

```text
contract loading
schema validation
path-boundary validation
forbidden operation detection
deterministic embedder shape
output status vocabulary
```

### P1 — External repo governance status file

The external repo should add a small `GOVERNANCE_STATUS.md` stating that it executes Block 1 and does not govern, approve, send, remember, validate truth, schedule, route providers or promote memory.

### P1 — Vendored upstream freshness

The vendored Pantheon commit `58d6bef` must be compared with the current Pantheon Next main branch before adoption. A stale vendored schema may still be useful for a bundle review, but it cannot be treated as current authority.

## Non-equivalence rules

```text
bundle_exists ≠ repository_published
repository_published ≠ binding_adopted
binding_adopted ≠ activated
six_tests_exist ≠ six_tests_currently_verified_by_pantheon
ci_green ≠ professional_evidence
retrieved ≠ true
result_candidate ≠ approved_result
evidence_pack_candidate ≠ validated_evidence
runtime_success ≠ approval
deterministic_output ≠ safe_output
source_declared ≠ path_safe
schema_vendored ≠ schema_current
external_repo ≠ Pantheon runtime
```

## Capability Slot record

```yaml
capability_slot: governed_task_loop_block_1
function: bounded retrieval and candidate generation under Task Contract
candidate_binding: ifanjuang/pantheon-mvp-vertical
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

implemented externally, observed from bundle only:
  Block 1 vertical code, fixtures, tests and CI definition.

partial:
  scope-filtered retrieval and candidate-output shape are promising but adoption is blocked by schema-alignment and path-boundary fixes.

to verify:
  published repository state, CI result after push, vendored schema freshness, P0 fixes, future Hermes/OpenWebUI integration.
```

## Final rule

```text
Pantheon may govern this binding.
Pantheon must not become this binding.
```
