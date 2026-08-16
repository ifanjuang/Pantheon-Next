# 2026-08-16 — architecture economy convergence

Status: repository-convergence intervention trace. No runtime, authorization, Capability Slot or professional state is created by this record.

## Objective

Review the architecture-economy findings raised after #655, distinguish observed defects from misleading symptoms, and route each real gap into the smallest existing responsibility rather than adding another doctrinal layer.

## Repository state checked

- `Pantheon-Next/main` at start: `b446bfd2ee9260f63345aae9dada25058b9ea520` (merge #663).
- `pantheon-mvp/main` at start: `4f9d6ffcf5c8b6509044977933fc0c7dcfcf6c80` (merge #316).
- Open Pantheon-Next PRs #657 and #658 touch landing/README surfaces, not the paths changed by this intervention.
- Open pantheon-mvp PR #315 touches migration fixtures/tests, not the architecture-audit workflow changed here.

## Findings corrected by repository inspection

### 1. Policy chokepoint: composition gap, with a corrected validator baseline

Observed:

- `mcp-server/pantheon_mcp/service.py` preflight keeps `external_effect_allowed=false`, `canonical_effect_allowed=false` and `gate_signal_validation_performed=false` in the current V0 disposition;
- preflight requirement checks establish the presence of gate references but do not themselves cryptographically validate a gate signal;
- `mcp-server/pantheon_mcp/gate_validation.py` validates decision structure, human signer, scope, approval level, expiry when supplied, object identity, digest and optional issuer authentication;
- the current validator is read-only and side-effect-free: it does **not** resolve or persist a Task Contract, does **not** consume a decision, and therefore does **not** implement one-use replay protection;
- a signature binds the decision envelope so it cannot be reused for a *different* scope/object/ceiling/expiry without failing verification, but that is distinct from preventing a second use of the same valid decision;
- `pantheon-mvp/mvp_vertical/policy_gate.py` is an actual fail-closed PEP: transport/malformed/non-eligible cases block, explicit PDP effect denial is checked before human-decision validation, and an effect runs only after a valid verdict.

Correction recorded during #664 qualification:

The earlier wording in this log and the initial #664 baseline overstated `gate_validation.py` by attributing Task Contract binding and replay/idempotency to it. Repository inspection of the actual implementation does not support that claim. For #664, exact fixture/Task Contract binding is composed around the existing validator, while one-shot decision consumption belongs at the operational PEP immediately before the effect. Pantheon remains a read-only PDP and does not acquire execution persistence merely to make the test green.

Interpretation:

The missing proof is still not another general authorization model. It is one bounded end-to-end composition in which preflight, signed-gate validation, PDP external-effect permission and PEP execution all participate in a real positive path while negative paths remain fail-closed. The synthetic qualification path must remain narrower than production effects and must keep `canonical_effect_allowed=false`.

Follow-up: Pantheon-Next #664.

### 2. `sha256:aaaa...`: synthetic vertical presented like an observation registry entry

Observed:

- `catalog/observations/document-analysis-docling-compatibility.yaml` has `metadata.status: observed` and an `aaaa...` content digest;
- the same anchor is intentionally shared by `catalog/bindings/document-analysis-docling.yaml`, the example Capability Passport and `catalog/examples/i8-capability-vertical-qualification.yaml`;
- I8 explicitly mutates the anchor to `bbbb...` to test release/binding drift.

Interpretation:

The placeholder is not an isolated fabricated field observation. It is part of a synthetic conformance vertical. The real defect is classification/placement: a synthetic fixture sits in `catalog/observations/` with an `observed` status, so a reader can reasonably mistake it for a field observation.

Follow-up: Pantheon-Next #665.

### 3. #655 does not currently fit `CapabilityCompatibilityObservation` without semantic distortion

Observed:

- the compatibility-observation schema is explicitly scoped to one existing `binding_id` and exact implementation anchor;
- #655 produced exact Hindsight/Hermes/Obsidian runtime identities and compatibility findings;
- the canonical `external_runtime_memory` binding record remains `unbound`, with no Hindsight CapabilityBinding adopted or selected.

Interpretation:

Creating a Hindsight binding solely to store #655 would turn observation into implied selection. The #655 log remains the correct durable field record until #665 establishes a legitimate pre-binding landing rule or demonstrates that an existing record can be safely extended.

```text
field observation != binding selection
binding selected != dependency adopted
runtime success != Evidence
```

### 4. Cross-repository architecture audit mixes merge gate and floating drift check

Observed:

- `pantheon-mvp/.github/workflows/architecture-audit.yml` checks out `Pantheon-Next` at floating `main` for the architecture inventory and permanent convergence closure;
- the same workflow separately resolves an exact distribution schema pin;
- the general vendored Pantheon snapshot records `mvp_vertical/vendor/pantheon/UPSTREAM_COMMIT = e9c237bb3995deb68685b097edae98f8c0efb9ed`;
- repository inspection showed that this old vendor pin predates `docs/governance/authority/PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json`, so it cannot mechanically become the architecture-audit authority pin;
- `Pantheon-Next@b446bfd2ee9260f63345aae9dada25058b9ea520` contains the registry and is the exact reviewed Next baseline at the start of this correction;
- `NEXT_MVP_REPOSITORY_PLACEMENT.md` requires exact pinned external consumption and makes drift detection consumer-owned; correction is reviewed, never silent synchronization.

Decision:

The merge-gating audit gets its own explicit exact authority snapshot, initially `b446bfd2ee9260f63345aae9dada25058b9ea520`, because that is the actual governance input set the audit requires. The older vendor pin and the separate Hermes distribution schema pin retain their existing meanings and are not silently reinterpreted. Current `Pantheon-Next/main` remains useful as a drift signal, but its comparison is report-only so an unrelated governance commit cannot retroactively change the contractual basis of an MVP PR.

If repeated independent pins become materially costly, they should converge later through an existing manifest responsibility rather than hidden synchronization or a new automatic updater.

Implementation belongs in `pantheon-mvp`; no Next runtime or reverse dependency is created. Follow-up: pantheon-mvp #317.

### 5. Doctrine economy

`CORE_CONCEPTS_MAP.md` already exists to prevent doctrine sprawl. Adding another doctrine-management document would reproduce the problem.

Decision:

Use the existing concept map and work rules. #666 establishes a consolidation campaign and a working freeze: prefer merge/extension/promotion/archive of existing candidate-support doctrine; a new candidate-support document needs a distinct responsibility and explicit convergence path. `ai_logs`, required fixtures and generated reports are not doctrine expansion.

## Resulting issues

- #664 — qualify one consequential green path through preflight, gate validation and PEP.
- #665 — close the capability observation loop with field qualifications without inventing bindings.
- #666 — consolidate candidate-support doctrine before expanding governance corpus.
- `pantheon-mvp` #317 — make the cross-repository architecture audit deterministic against an exact audit-authority snapshot while preserving current-main drift reporting.

These are intentionally separate from #659/#660/#661/#662, which remain the operational Hindsight/LiveSync/Rowboat/Marker follow-ups extracted from #655.

## Authority preserved

```text
validated gate != automatic approval
field observation != Evidence
synthetic fixture != field observation
current upstream drift != audited authority snapshot
current upstream drift != vendored snapshot
reported drift != automatic re-vendoring
candidate support doctrine != canonical authority
runtime decision consumption != Pantheon execution state
```

No schema, Capability Slot, binding selection, activation, runtime or professional record is changed by this intervention.
