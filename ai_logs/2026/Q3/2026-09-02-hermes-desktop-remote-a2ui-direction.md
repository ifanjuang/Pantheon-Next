# Hermes Desktop remote/A2UI convergence — 2026-09-02

Status: validation-only architecture trace — no installation, activation, adoption or task authorization.
Boundary profile: validation_only_trace.

## Objective

Reconcile the generative-UI direction with the current repository after the Hermes target moved to 0.21.0 and after reviewing Hermes Desktop as a client capable of driving a Hermes backend on another machine.

## Repository preflight

Current Pantheon `main` observed before this change:

```text
main: d336e35af873be2a52bbda88607a01d8f7353435
latest merge: #873 — Hermes 0.21 runtime boundary
Hermes candidate target: 0.21.0 / v2026.8.31
Hermes release commit: 29112bef099274229cadff79cdff7bf7b99c4b77
```

PR #882 (`test(cockpit): qualify A2UI as bounded generative projection`) was still open/draft, one commit ahead of its old merge base and 134 commits behind current `main`. It had no submitted reviews or review threads. Its own convergence note required reconstruction on exact current `main` or closure if the qualification no longer answered a current decision.

## External facts retained

The prior bounded source review established that Hermes Desktop can act as a frontend for another Hermes backend rather than only its bundled local backend. Remote connectivity/authentication/deployment remains an external runtime concern and is not proven by Pantheon repository state.

Hermes upstream PR #88024 merged before the currently pinned 0.21.0 release line and introduced the Desktop transcript contribution surface `transcript.directives`, where a plugin can register a named inline component addressed by a model-emitted directive. The contribution treats attributes as untrusted model output and keeps rendering inside the Desktop interaction layer.

A fresh exact-file fetch against the upstream 0.21 release commit was attempted during this reconciliation but the GitHub intermediary returned HTTP 429. The repository's already-merged #873 exact-tag review remains the authority for the 0.21 pin; this trace therefore does not invent a second release review or claim a new exact-source observation beyond the retained upstream facts above.

## Convergence decision

The selected interaction roles are now:

```text
Hermes Desktop
  -> selected rich interaction host
  -> local Hermes or authenticated remote Hermes backend

Hermes Web/dashboard
  -> browser/admin fallback
  -> remote-backend service surface where selected

Pantheon Cockpit
  -> governed projections / Cards / review / decisions
  -> not a second general-purpose chat frontend
```

The generative-UI direction becomes:

```text
Hermes Desktop interaction
  -> candidate A2UI presentation renderer
  -> bounded UI intent
  -> existing Pantheon/runtime effect boundary

NOT:
A2UI -> direct business mutation
A2UI -> second Cockpit chat path
```

## PR #882 disposition

#882 was closed without merge. Its guard/browser observations remain historical qualification input only. The old `a2ui-cockpit` implementation is not carried forward merely to preserve the branch.

Any new qualification must start on current `main`, reuse only the protocol/guard pieces that still answer the present question, and target the Hermes Desktop host seam.

## Non-equivalences preserved

```text
Desktop selected != Desktop mandatory forever
remote connection established != remote runtime qualified
remote runtime qualified != task authorized
A2UI rendered != A2UI adopted
A2UI surface != governed object
UI action != Pantheon authorization
runtime success != Evidence
projection != persistence
```

## Files changed in this slice

- `docs/governance/TARGET_ARCHITECTURE.md`
- `docs/governance/WHAT_RUNS.md`
- this validation trace

No implementation, schema, registry, Cockpit boot path, Hermes binding, deployment file, dependency pin, runtime configuration or Evidence owner is changed.

## Next bounded slice

Create a fresh implementation qualification on current `main` for the Hermes Desktop host contract. It should verify the current Hermes pin and Desktop plugin/transcript contribution seam, reuse a closed A2UI component/action catalog, and prove that a rendered interaction remains intent-only until an existing effect gate admits it.

Do not add an `A2UISurfaceRecord`, GenUI registry, second navigation root, second Cockpit boot chain or direct generated-button mutation endpoint.
