# 2026-07-13 — MVP decision vocabulary and schema reconciliation

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Scope

Resolved issue #359 for the external candidate binding `ifanjuang/pantheon-mvp`.

## Ratified decisions

1. The canonical MVP human-decision vocabulary is closed: `approve`, `refuse`, `request_revision`, `request_more_evidence`.
2. The enum in `schemas/mvp_governed_loop_objects.schema.yaml#/$defs/decision_value` is the single machine-readable vendoring source. Candidate-provided choices may only be a subset.
3. `commitment_flags` are structured objects with required `phrase` and `risk`.
4. Decision integrity fields are formal schema properties: distinct decision identity, timestamp, optional supersession, SHA-256 digests and honest identity assurance.
5. `identity_assurance: authenticated` requires a cockpit-supplied `authenticated_principal`; a terminal stand-in emits `declared` and must not fabricate authentication.
6. Register Candidate creation requires a separate `retention_authorization`; `approve` alone does not authorize retention or memory admission.
7. `grounding_review` is formalized as advisory visibility and explicitly remains neither score, proof, truth verdict nor approval.

## Freshness finding

Before this change, the current `main` schema content was byte-identical to the copy vendored from commit `58d6bef`. That commit was therefore current structurally, but it did not ratify these semantics. After this reconciliation merges, the merge commit becomes the upstream version to re-vendor.

## Boundary

```text
implemented in Pantheon Next:
  validation schema, schema tests, aligned illustrative examples and support doctrine

implemented externally:
  candidate Blocks 1–3 in ifanjuang/pantheon-mvp

not adopted:
  external binding

not activated:
  external binding

forbidden:
  production use, automatic approval, automatic retention, memory admission,
  external send, provider routing, scheduler, queue
```

Schema validity does not execute a gate, authenticate a user, approve a candidate, retain data or admit memory.
