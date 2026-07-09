# Pantheon MVP Vertical — External Reference Review

Status: validation-only external reference review — candidate / to verify.

Boundary profile: reference_review.

Reviewed artifact: `pantheon-mvp-vertical.bundle`.

This review records observations about an external executable bundle. It does not approve the dependency, install the repo, import the code into Pantheon Next, authorize execution, validate professional truth, approve memory promotion or authorize external action.

## Review posture

```text
Pantheon   -> governance distillation and adoption gates
Hermes     -> possible future execution binding, if bounded and approved
OpenWebUI  -> possible exposure surface only, not runtime authority
```

## Observed bundle facts

```text
bundle commit: 4ce16b7
commit subject: feat: Block 1 of the Pantheon MVP governed task loop
tracked files: 19
vendored Pantheon commit: 58d6bef
local package: mvp_vertical
fixture dossier: dossiers/devis_reprise
schema/validator material: vendor/pantheon
CI file: .github/workflows/ci.yml
acceptance test file: tests/test_block1.py
```

The bundle's remote HEAD is not set to the branch that contains the commit. A simple clone can produce no checked-out local branch. The safe checkout command is:

```bash
git clone pantheon-mvp-vertical.bundle pantheon-mvp-vertical
cd pantheon-mvp-vertical
git switch -c main origin/main
```

## What looks strong

The bundle cleanly separates execution from governance. Its README states that the repository executes and does not govern.

The technical loop is useful as a Block 1 vertical slice:

```text
Task Contract load
bounded ingestion of declared sources
pgvector storage
SQL source-perimeter filtering before vector ranking
deterministic candidate drafting
Evidence Pack Candidate output
forbidden-operation refusal
outside-perimeter refusal
```

The retrieval boundary is better than a naive RAG demo because the SQL query filters by dossier and declared sources before vector ranking.

The output shape preserves Pantheon distinctions:

```text
result_candidate
evidence_pack_candidate
status: draft_to_review
external_action_authorized: false
support_status: sourced_not_verified
```

## What remains weak

### Schema / fixture mismatch

The Task Contract fixture uses fields such as:

```text
declared_scope
expected_output
```

The vendored schema expects Task Contract fields closer to:

```text
scope
expected_outputs
```

The tests validate the runner outputs against the vendored schema, but the observed test suite does not validate the Task Contract fixture itself against that schema.

### Path boundary

The ingestion path builds `root / source_ref` after checking that `source_ref` is declared by the contract. That is not enough for adoption. A malicious or malformed declared source can still attempt to escape the workspace if canonical path checks are absent.

Before adoption, source resolution should reject:

```text
absolute paths
.. traversal
symlink escape outside root
non-file sources where a file is expected
```

### Fixture-specific runner

The deterministic runner is useful, but it is specific to the fictional `devis_reprise` fixture. It must not be presented as a general answer engine or professional decision tool.

### Test semantics

The bundle contains six acceptance tests. That is a useful runtime signal, but in Pantheon terms:

```text
six_tests_exist ≠ six_tests_currently_verified_by_pantheon
ci_green ≠ professional_evidence
runtime_success ≠ approval
```

## Recommended classification

```text
abstract capability:
  governed_task_loop_block_1

candidate binding:
  ifanjuang/pantheon-mvp-vertical

status:
  external executable repo / candidate binding / not adopted

adoption posture:
  blocked until P0 fixes are made and reviewed
```

## Recommended P0 fixes

```text
1. Align the Task Contract fixture with the vendored schema or document the dialect explicitly.
2. Add a test validating the Task Contract fixture against the schema.
3. Add canonical path boundary checks under the workspace root.
4. Add tests for path traversal and absolute-path refusal.
5. Label the deterministic runner as fixture-specific Block 1, not a general answer engine.
```

## Recommended P1 fixes

```text
1. Add unit tests that run without pgvector.
2. Add GOVERNANCE_STATUS.md in the external repo.
3. Compare vendored Pantheon commit 58d6bef to current Pantheon Next main.
4. Re-run external CI after publishing the repository.
```

## Distillation target

The review is distilled into:

```text
docs/governance/PANTHEON_MVP_VERTICAL_BINDING.md
```

## Final review result

```text
watch: yes
distill: yes
adopt now: no
import into Pantheon Next: no
keep as external executable candidate: yes
```
