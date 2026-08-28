# OpenWebUI capability-governance convergence — 2026-08-28

## Objective

Continue #785 from merged main `43959224b17d9de92c1008e3a620c0d398f7e13d` with a bounded capability-governance slice. Retire present-tense OpenWebUI ownership without replacing it with Hermes WebUI and reduce the machine-tracked allowlist from 25 paths to 23.

## Scope

- `docs/governance/MODEL_CAPABILITY_PASSPORT.md`
- `docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Owner review

`MODEL_CAPABILITY_PASSPORT.md` remains the model-specific specialization of the universal capability passport.

`UNIFORM_CAPABILITY_GOVERNANCE.md` remains the keystone rulebook for capability passports and the consequential-effect gate.

`MODULE_ACTIVATION.md` and `MODULAR_DOMAIN_REORIENTATION.md` were inspected but deliberately excluded. They contain broader current UI/binding assumptions whose correction requires a dedicated owner-aware rewrite rather than a mechanical top-block substitution.

## Convergence

Both edited owners now inherit runtime/client/authority placement from `HERMES_INTEGRATION.md`.

The uniform capability owner now states the current generic split explicitly:

```text
Pantheon policy service = bounded PDP interface
Hermes / external runtime = PEP for consequential effects
optional runtime client = replaceable runtime interaction
Pantheon Cockpit = governed projection
Pantheon Next = governance / authority semantics
human = consequential decision when required
```

Model and runtime-client selection remain non-authoritative.

No Hermes WebUI dependency or new governance owner is introduced.

## Preserved invariants

```text
model selected != output approved
client selected != authority transfer
PDP decision != PEP execution
runtime success != authorization
runtime output != Evidence
projection != persistence
memory != Evidence
```

## Boundary

Documentation and regression-only convergence. No runtime, API, schema, persistence, provider, installation, approval, memory or external-effect behavior changes.

No long document was truncated or substantially reduced, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior check evidence. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact published head and reviews/threads/comments have been read.
