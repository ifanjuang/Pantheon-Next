# ACI distillation finish — 2026-09-01

Status: validation / intervention trace — not doctrine.

## Objective

Finish PR #898 on the current Pantheon-Next trajectory without restoring stale mutation-review state.

## Current baseline revalidated

Before the finish pass:

```text
Pantheon-Next/main = 17105e0474009a21c52d92619da2241243615c43
```

The original #898 head was 18 commits behind current `main`. Those commits materially expanded the consequential-mutation review, so the old branch was not merged or copied wholesale.

The #898 branch was rebuilt from current `main`. Files that had not changed since the original #898 base reused the reviewed #898 versions. `implementation/tests/test_consequential_mutation_inventory.py` was deliberately left on the newer `main` version.

Current inventory truth at the rebase point:

```text
92 mutation entry points
71 individually reviewed
21 explicitly unreviewed
9 reviewed as gate_required_not_wired
```

The owner primitive `knowledge_update.apply_knowledge_update` still accepts an optional `policy_client` for bounded direct/test use. The Cockpit application route is the fail-closed boundary: policy enforcement defaults to `required`, and an absent PDP refuses the consequential write unless the deployment explicitly declares `disabled`.

This distinction is retained rather than rewriting the function-level inventory to claim universal enforcement.

## Historical test correction

The three old `test_knowledge_update_chokepoint.py` cases predated the explicit governance-reference contract. Their shared fixture now provides synthetic valid:

```text
task_contract_ref
evidence_pack_candidate_ref
human_decision_ref
```

The production contract was not weakened to preserve stale fixtures.

## Effect-binding digest correction

Knowledge persistence currently stores/returns `markdown_digest` as raw 64-character SHA-256 hex. Signed preview and policy decision material use `sha256:<hex>`.

The effect-binding response now canonicalizes the returned persisted digest into `sha256:<hex>` for comparison only.

```text
persistent digest storage = unchanged
authorized digest representation = sha256:<hex>
applied binding representation = sha256:<hex>
```

Unexpected legacy digest strings are surfaced rather than causing a post-commit exception. A successful persistence must not be converted into an error response by response-format validation.

A focused regression test uses the real persisted representation shape (raw hex) and proves that the effect binding exposes matching authorized/applied canonical digests while the returned Knowledge snapshot remains raw.

## ACI boundary

This remains distillation, not integration.

No ACI code, cognitive cycle, graph container, AlgorithmRegistry, IdentityKernel, threshold model, transaction engine or dependency is imported.

```text
reference pattern != authority
paired evaluation != approval
decision validated != effect applied
effect binding != Evidence
```

## Completion condition

PR #898 may leave draft only after all repository workflows on the rebuilt head are green. Merge is appropriate only after a final `main`/head revalidation shows no new divergence requiring convergence.
