# 2026-05-29 - Rites invocation policy hardening

## Summary

Hardened the Rites governance layer against workflow drift.

This pass focused only on the Rites lane.

## Files changed

- `docs/governance/rites/RITE_INVOCATION_POLICY.md`
- `docs/governance/rites/README.md`
- `docs/governance/rites/_TEMPLATE_RITE.md`

## Added

`RITE_INVOCATION_POLICY.md` defines:

- invocation authority;
- ZEUS authorization;
- ZEUS closure statuses;
- rite budget;
- anti-chaining rule;
- trigger thresholds;
- no-rite-for-style-only rule;
- Rite Review Card format;
- Refoundation safeguard;
- OpenWebUI display-label recommendations;
- Hermes boundary;
- forbidden drift.

## Changed

`docs/governance/rites/README.md` now references `RITE_INVOCATION_POLICY.md`, records the anti-chaining rule, adds a rite budget, adds ZEUS closure statuses and defines the Rite Review Card.

`docs/governance/rites/_TEMPLATE_RITE.md` now uses less agentic vocabulary:

- `Role viewpoints involved` instead of `Roles called`;
- `Governance sequence` instead of `Procedure`.

It also includes a reusable Rite Review Card section and closure requirements.

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

## OpenWebUI note

`OPENWEBUI_INTEGRATION.md` still contains the older display labels `rite_active` and `rite_completed`.

A direct update was not performed in this pass because the file is long and active parallel developments make full-file replacement risky.

The new preferred labels are now recorded in `RITE_INVOCATION_POLICY.md`:

```text
rite_proposed
rite_not_needed
rite_review_open
rite_under_governance_review
rite_review_closed
rite_rejected
rite_superseded
rite_escalated_to_user_decision_gate
```

A future micro-pass should update `OPENWEBUI_INTEGRATION.md` to align with those labels when no concurrent edit is in progress.

## Changelog note

A changelog entry should be added in a future micro-pass when `CHANGELOG.md` is not being updated by parallel work.

## Risk addressed

The main risk was that rites could become implicit workflows through chaining, ambiguous UI labels or missing closure.

The new doctrine requires visible reason, authorization, effect and closure for every invoked rite.

## Final rule

A rite is safe only when its reason, authorization, effect and closure are visible.
