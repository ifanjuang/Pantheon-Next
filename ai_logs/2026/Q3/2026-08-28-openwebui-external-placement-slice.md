# OpenWebUI external-tool placement convergence — 2026-08-28

## Objective

Continue #785 from merged main `ac0c0557a3a4779a5bd312de806fd04ee1ec1c4c` with a bounded external-tool placement slice. Remove current OpenWebUI ownership from the external-tool placement register while preserving product-specific historical, comparative and rejected references. Reduce the machine-tracked allowlist from 3 paths to 2.

## Scope

- `docs/governance/EXTERNAL_TOOL_PLACEMENT_REGISTER.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Observed need

The placement register still carried the old global OpenWebUI ownership block and several current placement decisions assigned governed decision, observability or approval projection to OpenWebUI. The same file also contains legitimate product-specific prohibitions and historical/comparative references that must remain visible.

## Owner review

`EXTERNAL_TOOL_PLACEMENT_REGISTER.md` remains a support register for lightweight placement decisions, not doctrine by itself. Canonical placement remains owned by `CAPABILITY_PLACEMENT.md`, `MODULAR_DOMAIN_REORIENTATION.md`, `EXTERNAL_TOOLS_POLICY.md`, `ADAPTERS_AND_BINDINGS.md` and `HERMES_INTEGRATION.md` for the runtime/client/PDP/PEP split.

## Overlap analysis

The slice does not re-review the external tools, change their adoption decisions, install or select a client, alter Hermes bindings, or erase rejected product-specific patterns. It changes only the current placement vocabulary that still treated OpenWebUI as the governed projection surface.

## Affected consumers

- maintainers consulting external-tool placement decisions;
- future tool/binding qualification work;
- future Pantheon Cockpit projections of governed summaries or approval state;
- #785 regression tests.

## Convergence

Spice decision-surface inspiration now maps to Pantheon Cockpit. Opik and LangGraph Agent Stack governed summaries/status/approval projections map to Pantheon Cockpit, while optional runtime clients remain interaction-only. Hermes Uplink is no longer compared against OpenWebUI as the selected cockpit; the register states that Pantheon Cockpit remains governed projection and no runtime client is selected by the register. Explicit rejected references such as `OpenWebUI filter installation without separate review` remain because they record a concrete unsafe pattern rather than current ownership.

## Migration and rollback

Documentation-only convergence. No external tool, runtime, client, adapter, connector, dashboard or plugin is installed, selected, enabled, disabled or reconfigured. No persistent state changes. Rollback is a normal Git revert.

## Role / Rite / Space

- Role: MNEMOSYNE for placement/provenance continuity, with THEMIS authority-boundary review.
- Rite: Concordance des sources across exact main, #785, the placement owners and `HERMES_INTEGRATION.md`.
- Space: Pantheon Next governance repository.

These labels describe review context only and create no runtime state.

## Authority impact

None. The register cannot select a runtime client or grant governance authority to an external tool. Pantheon policy remains the bounded PDP, Hermes/external runtime remains PEP/executor, and Pantheon Cockpit remains governed projection.

## Runtime impact

None. No API, runtime, client, tool execution, provider, external effect, installation or deployment behavior changes.

## Preserved invariants

```text
external reference != selected architecture
placement record != adoption
client available != client selected
runtime interaction != governed projection
projection != approval
trace != Evidence
runtime success != authorization
```

## Boundary

Documentation and regression-only convergence. The register was read through EOF before editing. Compare statistics are bounded despite the file size: 11 additions and 14 deletions in the register, plus one allowlist deletion. `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior check evidence. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final head and reviews/threads/comments have been read.
