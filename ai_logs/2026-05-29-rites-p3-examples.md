# 2026-05-29 - Rites P3 examples

## Summary

Added P3 usage examples for the Rites lane only.

This pass tests the usability of existing rite doctrine in realistic fictional situations.

It does not create new rites.

It does not add schemas, tests, prompts, runtime behavior, OpenWebUI components or Hermes skills.

## Files changed

- `docs/governance/rites/RITE_EXAMPLES.md`
- `docs/governance/rites/README.md`

## Added

`RITE_EXAMPLES.md` contains fictional examples for:

1. `RITE_DIVERGENCE_CONTROLEE.md` applied to a Pantheon architecture decision about cockpit exposure;
2. `AUTOCRITIQUE_CONTRADICTOIRE.md` applied to a professional client email;
3. `REFONDATION_DE_SESSION.md` applied to a Hydre-like long thread;
4. a conflict between rites leading to a User Decision Gate.

## README raccord

`docs/governance/rites/README.md` now indexes `RITE_EXAMPLES.md` and adds the examples rule:

```text
Examples test usability.
They do not authorize execution.
They do not add new doctrine beyond the active rite policy.
```

## Boundary

This pass is documentation-only.

It does not implement:

- rite runtime;
- automatic rite trigger engine;
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

Examples test usability.

They do not authorize execution.
