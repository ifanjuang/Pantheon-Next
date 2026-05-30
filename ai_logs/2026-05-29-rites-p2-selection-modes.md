# 2026-05-29 - Rites P2 selection matrix and modes

## Summary

Added P2 ergonomic support for the Rites lane only.

This pass does not create new operational rites.

It adds selection and intensity guidance so existing rites are easier to choose and less likely to be overused.

## Files changed

- `docs/governance/rites/RITE_SELECTION_MATRIX.md`
- `docs/governance/rites/RITE_MODES.md`
- `docs/governance/rites/README.md`

## Added

`RITE_SELECTION_MATRIX.md` maps governance symptoms to candidate rites, anti-risks and required outputs.

It explicitly states that a symptom may suggest a rite but does not trigger it.

ZEUS still decides whether the rite is allowed.

`RITE_MODES.md` defines three non-executable rite intensity modes:

```text
mode_light
mode_standard
mode_full
```

The modes are review-intensity labels only.

They are not runtime modes, task runners or OpenWebUI pipeline states.

## README raccord

`docs/governance/rites/README.md` now indexes:

- `RITE_SELECTION_MATRIX.md`
- `RITE_MODES.md`

It adds the core P2 rules:

```text
A symptom may suggest a rite.
It does not trigger the rite.
ZEUS decides whether the rite is allowed.
```

```text
Choose the smallest rite mode that can safely expose the useful tension.
```

## Boundary

This pass is documentation-only.

It does not implement:

- rite runtime;
- automatic rite trigger engine;
- automatic selection engine;
- runtime mode engine;
- hidden rite debate loop;
- scheduler;
- queue;
- OpenWebUI function, tool, pipe, filter, action or pipeline;
- Hermes skill installation;
- automatic approval;
- automatic memory promotion.

## Deferred raccords

`STATUS.md`, `CHANGELOG.md` and `OPENWEBUI_INTEGRATION.md` were not rewritten in this pass.

Reason: those files are long and affected by parallel development lanes.

They should be reconciled in a separate low-conflict micro-pass when safe.

## Final rule

Choose the rite from the symptom.

Choose the mode from the risk.

Let ZEUS authorize the procedure.
