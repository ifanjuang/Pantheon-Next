# OpenWebUI structural bindings convergence — 2026-08-28

## Objective

Continue #785 from merged main `553ff1950d870c3e3f3f80219e574da8968216df` with a coordinated structural-binding slice. Remove current OpenWebUI ownership from module activation, modular placement, adapter/binding doctrine and the future bridge contract while reconciling those owners with the canonical PDP/PEP and runtime-client/Cockpit split. Reduce the machine-tracked allowlist from 7 paths to 3.

## Scope

- `docs/governance/ADAPTERS_AND_BINDINGS.md`
- `docs/governance/BRIDGE_CONTRACT.md`
- `docs/governance/MODULE_ACTIVATION.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Observed need

These four owners were not merely carrying the old global OpenWebUI sentence. Together they still treated OpenWebUI as the active exposure/cockpit binding, assigned governed status and decision controls to that client, and let the bridge language sound like an independent authorization layer. That conflicted with the current canonical split in `HERMES_INTEGRATION.md` and `mcp-server/docs/HTTP_API_CONTRACT.md`.

## Owner review

`HERMES_INTEGRATION.md` remains the stable runtime/client/PDP/PEP owner. The policy HTTP contract remains the current bounded PDP projection. The four edited documents keep their distinct responsibilities: adapter placement, future bridge adaptation, module activation semantics and modular/domain coordination. None becomes a replacement integration owner.

## Overlap analysis

The files are edited together because they explicitly reference one another and jointly described the same binding/activation boundary. The slice does not merge them, create a new runtime client, select Hermes WebUI, implement Pantheon Cockpit, add a bridge, create a second policy service or change executable schemas. `#787` documentation-topology consolidation remains separate.

## Affected consumers

- maintainers classifying capability activation and bindings;
- future adapter/runtime-client implementers;
- future Pantheon Cockpit projection work;
- future bridge/runtime PEP integration work;
- domain-pack projection maintainers;
- #785 regression tests.

## Convergence

The binding registry now records no selected runtime client, Hermes Agent as selected external execution runtime, and Pantheon Cockpit as the governed projection owner. Module activation separates runtime administration from governed Cockpit projection and makes activation/task authorization subordinate to applicable Pantheon policy. Adapter doctrine treats runtime clients as optional and replaceable. The bridge is explicitly neither PDP nor PEP: it may structurally preflight, consult/convey Pantheon policy, block or narrow locally, and must never widen a PDP disposition.

## Migration and rollback

Documentation-only convergence. No client, Hermes service, Cockpit, bridge, module, plugin or external system is installed, enabled, disabled or reconfigured. No persistent state or executable contract migration occurs. Rollback is a normal Git revert of the bounded slice.

## Role / Rite / Space

- Role: THEMIS for authority/PDP/PEP boundaries, with MNEMOSYNE for owner continuity and ATHENA for modular placement coherence.
- Rite: Concordance des sources across exact main, #785, `HERMES_INTEGRATION.md`, the policy HTTP contract and the four edited owners.
- Space: Pantheon Next governance repository.

These labels describe review context only and create no runtime state.

## Authority impact

No authority transfer. Pantheon policy remains the bounded PDP; Hermes/the external runtime remains PEP/executor for consequential effects; optional runtime clients expose interaction only; Pantheon Cockpit projects governed state; a bridge or activation record cannot independently authorize or execute an effect.

## Runtime impact

None. No API, runtime, provider, client, bridge, connector, installation, scheduling, external-effect or deployment behavior changes.

## Preserved invariants

```text
client available != client selected
client selected != governance authority
runtime interaction != governed projection
projection != persistence
module detected != module enabled
module enabled != task/effect authorized
PDP decision != PEP execution
bridge adaptation != policy decision
runtime success != Evidence
```

## Boundary

Documentation and regression-only convergence. The existing canonical implementation contracts and schemas are not changed.

The four documents were read from the exact merged base before editing. Compare statistics show bounded semantic reconciliation rather than truncation: adapters -3 lines net, module activation -6, bridge +20, modular reorientation +17. `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior check evidence. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the final exact head and all reviews/threads/comments have been read.
