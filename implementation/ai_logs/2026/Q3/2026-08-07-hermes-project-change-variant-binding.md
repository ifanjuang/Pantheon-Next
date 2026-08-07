# Hermes Project change variant binding

Date: 2026-08-07
Status: G2 implementation and Hermes 0.20.0 laboratory verified on candidate head; final protections must remain green after this journal update.

## Objective

Complete tranche G by producing the merged `project_change_variant` contract through
the existing external Hermes run binding, retaining the typed Execution Result under
the consumed admission, and exposing a separate human selection route.

The binding must not select an alternative, create a ChangeCandidate automatically,
apply a Project mutation, create a Decision, admit Evidence or authorize a follow-up.

## Existing responsibilities reused

```text
ExternalHermesRunBinding
-> one-shot qualification, launch reservation, run submission, start record and reconciliation.

Hermes runtime return route
-> admission-bound transactional return normalization.

Execution Results
-> immutable project_change_variant persistence.

project_change_variants
-> separate human selection into the existing ChangeCandidate owner.
```

G2 is implemented inside the existing `run-binding` distribution component. The
initial parallel reconciliation module was removed before acceptance so the
standard distribution still has exactly three components: `run-binding`,
`context-bridge`, `runtime-observer`. There is no second runtime path, scheduler,
queue, polling loop, automatic retry or provider router.

## Structured return contract

The canonical `reconcile` path recognizes this optional closed JSON envelope:

```json
{
  "kind": "pantheon_project_change_variants",
  "summary": "...",
  "execution_result": {}
}
```

When this exact envelope kind is present, it must contain at least two unique
`project_change_variant` alternatives. Malformed variant envelopes, one alternative,
duplicate labels or another result kind are refused before the Pantheon return write.
Non-variant output continues through the pre-existing generic candidate path.

## Server-side admission checks

The Pantheon return validates:

- exact Task Contract identity against the consumed admission;
- the Project identity inside the immutable Context Pack;
- canonical equivalence between transport refs such as `project:<id>` and the
  governed unprefixed ID required by the variant schema, without widening scope;
- only Project change variant result kinds;
- unique result identities;
- payload Project consistency;
- every basis reference inside the immutable Context Pack;
- exact vendored candidate schema during Execution Result persistence.

The typed Execution Result and generic Hermes ResultCandidate are stored inside the
same return transaction. An out-of-scope basis, stale Work Issue version or
idempotency conflict retains neither record and leaves the run unreturned.

## Human selection surface

A separate editor-key route requires `X-Pantheon-Human-Actor` and an idempotency
key. It calls the G1 transition and returns a pending existing ChangeCandidate.
The response explicitly keeps Project mutation, Decision, Evidence, memory and
external-effect posture false. Selection still does not apply the Project change.

## Distribution convergence

`pantheon-standard.lock.yaml` remains on schema revision 2, as required by the
pinned authority schema. It keeps the same three components and adds
`record-typed-project-variant-return` to the existing `run-binding` capability list.
Its file digest is:

```text
sha256:ae07a87ead1e160335e453cfe4c20af8c728ae534f65424ee8642f7c84a40426
```

The `pantheon_mvp` source pin points to commit
`5886f2de78125265dc73011f1d820965a449bd85`, which contains those exact binding
bytes. The distribution remains `candidate`, `not_observed`, `not_activated` and
`not_authorized` for production.

## Hermes 0.20.0 laboratory result

Real GitHub-hosted ephemeral acceptance:

```text
workflow run: 31139256797
artifact:     8979188157
Hermes:       0.20.0
source digest sha256:b1fe80817e230da0e0d5d847ef709a7c6570c60b9e7195366bfc58bcc6cdafbe
provider calls: 7
```

Observed result:

```text
context manifest read = true
admitted Project read = true
outside Project refused = true
Execution Result stored = true
project_change_variant count = 2
variants = option-zinc, option-ardoise
review disposition returned by Hermes = false
variant selected = false
Project mutated = false
Decision created = false
Evidence admitted = false
external effect authorized = false
rollback verified = true
```

The ordinary Hermes 0.20.0 laboratory also remained green on workflow run
`31139256792`, proving that generic reconciliation was not regressed by the typed
variant path.

## Required completion checks

Verified on candidate head `b586bdf19e1187cd8650cd9569839307720c2c1b` before this documentation update:

```text
Pantheon Architecture Audit                 success
contract-tests                              success
Hermes 0.20.0 Project Variant Lab           success
Hermes 0.20.0 generic Lab Acceptance        success
```

A later documentation-only lock edit briefly changed the lock to unsupported
revision 3; architecture and both laboratories correctly failed closed at schema
validation before executing G2. Revision 2 was restored without changing the
binding bytes or runtime behavior. All protections and both laboratories must be
green again on this final documentation head before merge.

## Non-equivalences

```text
runtime completed != alternatives selected
Execution Result stored != ChangeCandidate created
variant selected != Project mutation applied
technical receipt != Evidence
lab acceptance != agency/NAS activation
```
