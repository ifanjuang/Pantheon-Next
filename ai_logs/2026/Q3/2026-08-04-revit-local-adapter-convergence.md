# Revit local adapter authority convergence

Date: 2026-08-04
Status: validation-only intervention trace.

## Objective

Resolve issue #501 by rebuilding the useful historical Revit boundary from current `main`, without merging the divergent generation-named branch or creating a parallel execution model.

## Observed state

- the historical branch was four commits ahead and eighty-seven commits behind current `main`;
- current `main` already contained capability exploration, sandbox, action-contract, prototype and developer documents;
- those documents overlapped but did not identify one canonical adapter boundary;
- `revit-plugin/` remained a non-compiling skeleton inside the governance repository.

## Convergence

- add `REVIT_LOCAL_ADAPTER.md` as the single responsibility boundary;
- map historical warning levels to existing requested-effect classes instead of retaining a second approval vocabulary;
- carry blockers through existing Work Issue, run, Result Candidate and Capability Gap surfaces;
- keep Revit API execution in an external add-in;
- keep Task Contract, Context Pack, ChangeCandidate, Trace, Evidence and human gates in their current owners;
- retain specialized material as subordinate support;
- clarify that `revit-plugin/` is a reference skeleton, not a runtime-code precedent.

```text
preflight_passed != effect_authorized
transaction_success != accepted_result
runtime_success != Evidence
```

No schema, route, runtime, installer, scheduler, queue, provider router, plugin manager, memory engine or automatic approval is added.
