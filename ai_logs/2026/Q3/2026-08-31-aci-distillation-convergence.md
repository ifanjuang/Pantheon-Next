# ACI distillation convergence — 2026-08-31

Status: validation / intervention trace — not doctrine.

## Baseline observed before intervention

Pantheon `main` at the start of this intervention:

```text
a67226759df58029394199cc6201f87b659b6c1f
```

Repository state had already moved beyond the earlier review:

- #886 had merged asserted-property controls, symbol call-reachability and candidacy-aging checks;
- #884 had merged the qualification retry/diagnostic correction;
- #892 had merged the reviewed external-pin alignment;
- #887 was closed without merge after its blocking-workflow premise was corrected;
- #891 remained open on an older base and was no longer mergeable as-is.

The external reference reviewed for this convergence was the public ACI reference architecture at public `main` commit:

```text
e6f58014888160d413104e24cf9bebaa20a58213
```

That repository is a reference source, not Pantheon authority or Evidence. Its documented tests and acceptance claims were not independently replayed in this intervention.

## Objective

Distill only the mechanisms that close a demonstrated Pantheon gap, into existing owners, without importing ACI code, terminology or a second architecture.

## What was already absorbed

The useful category-collapse discipline was already substantially present after #886 and existing contract tests:

```text
retrieved != truth
memory != Evidence
execution success != authorization
projection != persistence
installed != approved
```

The repository now enumerates these asserted properties and binds most to schema or behavioural controls. Existing policy qualification tests also attempt adversarial decision/effect crossings and replay.

No ACI-specific invariant registry was therefore added.

## Distillation 1 — exact decision/effect non-broadening on a real write

The Knowledge UPDATE owner already accepted an optional `policy_client`, but the Cockpit did not assemble one. More importantly, `policy_request.bind_decision_payload()` intentionally treats `candidate.decision_expectation` as PEP-owned authority when present. A caller that supplied a preflight candidate could therefore attempt to redefine the expectation unless the concrete owner re-bound it.

This branch makes the bounded Knowledge path enforce its own exact effect facts before the shared chokepoint:

```text
intent             -> knowledge_update
writes_state       -> true
external_effect    -> false
scope              -> exact opened project
object_identity    -> exact Knowledge id + proposed digest
expected_digest    -> exact signed proposed digest
required_ceiling   -> owner-required ceiling
```

Caller-provided candidate fields may add context but cannot broaden those facts. Tests deliberately supply attacker-controlled scope, intent, write flag and decision expectation and require the PEP-bound values to win.

The decision reference is kept distinct from the idempotency key. An allowed result exposes an `effect_binding` beside the applied snapshot so the authorized digest and resulting digest/version can be compared without claiming the response is Evidence or approval.

## Distillation 2 — application assembly, not merely implemented gate code

The Cockpit factory now assembles the existing `HttpPolicyClient` when its endpoint and credential configuration are both available.

Consequential Knowledge enforcement defaults to `required`:

- an unconfigured decision point refuses the write;
- local-guards-only operation requires an explicitly named `disabled` posture;
- read-only surfaces do not require a PDP;
- transport failure is distinct from an ordinary candidate refusal.

The #886 call-path register is advanced accordingly: `HttpPolicyClient` is now expected to be entry-reachable. The generic `governed_effect` helper remains test-only; the owner-specific Knowledge path calls the shared `enforce_consequential` seam directly and keeps `knowledge.revise_knowledge` as the persistence/transaction owner.

```text
gate implemented != gate invoked
entry reachable != deployed enforcement
decision validated != effect applied
effect-binding response != Evidence
```

## Distillation 3 — measure governance damage, not only aggregate score

`PRE_EXECUTION_SIMULATION.md` now owns paired baseline/candidate accounting for interventions that may alter utility.

The method freezes baseline, candidate, cases and evaluator before observation and classifies:

```text
pass -> fail = damage
fail -> pass = rescue
pass -> pass = survival
fail -> fail = unchanged failure
```

Damage, rescue and pass-survival rates are reported with denominators. Abstention and runtime/liveness failure stay separate. A material post-observation change creates a new candidate/version rather than silently tuning the frozen comparison.

The prior `DISTILLATION_REGISTRY.md` candidate row for baseline-versus-candidate paired evaluation was removed because its destination owner now contains the rule. Git history and this intervention trace retain provenance.

## Deliberate non-imports

This work does not add:

- an Integrated Cognitive Cycle;
- ACI graph containers;
- an ACI AlgorithmRegistry;
- GEA/CRA/PCA/MSSA/CGA runtime owners;
- an IdentityKernel;
- ACI budgets, thresholds or scale semantics;
- a Pantheon Transaction Engine;
- an ACI dependency;
- a second evaluation runtime.

The existing owner boundaries remain:

```text
Pantheon governs.
Hermes executes externally.
Knowledge persists through its existing owner.
Simulation is a method/test seam, not an execution engine.
```

## Mutation-surface honesty

The current inventory remains 72 entry points:

```text
17 reviewed
55 unreviewed
```

This branch changes the reviewed Knowledge UPDATE entry from `optional` to `enforce_consequential`. It does not mechanically place all 72 entries behind the PDP.

Two reviewed entries remain explicitly `gate_required_not_wired`:

```text
human_access.bind_oidc_identity
apu_owner.store_reviewed_dossier
```

They remain visible debt rather than being folded into this change.

## Verification posture

This intervention was authored through the repository API against the observed current `main`. A local checkout/test replay was not available in the authoring environment.

Protected implementation, tests, call-path declarations and governance support documents were changed together so pull-request CI can verify the branch as one bounded candidate.

No test-pass claim is made in this trace until repository CI reports it.
