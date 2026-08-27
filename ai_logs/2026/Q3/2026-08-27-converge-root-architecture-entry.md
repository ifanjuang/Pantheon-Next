# Converge root architecture entry

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: active-owner reconciliation
Space: repository root architecture/read path
Change level: semantic

## Objective

Align the repository's first-read architecture surfaces with the current selected owner split after the OpenWebUI/Paperless retirement campaign, without creating a new doctrine owner.

## Verified state

Current `main` before the change: `4d1cdd9ae16cfb0d7cfef0fd44de8d5ebbbb7816` (merge of PR #780).

`docs/governance/STATUS.md` currently owns the canonical posture:

```text
Hermes Web/dashboard -> chat, sessions and runtime controls
Hermes Agent -> external execution
Pantheon Next -> consequential governance
Pantheon Cockpit -> governed Cards/navigation/decisions/status projections
OpenWebUI / Paperless-ngx -> refused/retired target integrations, no target role
```

The root entry surfaces contradicted that current posture:

- `CLAUDE.md` still said `OpenWebUI exposes.`;
- its Runtime policy still said `OpenWebUI is the cockpit/exposure surface when installed`;
- its repository description still named OpenWebUI/Paperless/Hermes adapters as current implementation contents after the product-specific OpenWebUI and Paperless paths had been retired;
- `README.md` and `README.fr.md` still assigned user interaction/decision projections to `Cockpit / OpenWebUI`.

No open PR referencing #666 was found. Two surviving `666-*` branches are fully behind current `main`; the remaining old cockpit branch diverges from a much older base and still modifies the now-deleted OpenWebUI owner, so it is historical and not a valid continuation path.

## Change

- align `CLAUDE.md` doctrine and runtime policy with the current `STATUS.md` responsibility split;
- keep `implementation/` described generically as PostgreSQL/APIs/Cockpit/bounded adapters rather than naming retired product compatibility;
- make compatible runtime clients explicitly replaceable and non-authoritative;
- make Pantheon Cockpit explicitly the governed projection surface;
- state that OpenWebUI and Paperless-ngx are retired/refused target integrations and historical references do not restore ownership;
- align English and French README system-boundary tables with the same owners;
- add root regression tests preventing the retired ownership statements from returning.

## Authority impact

No authority is transferred or created. This removes a contradiction between canonical `STATUS.md` and root orientation/work-rule surfaces.

## Runtime impact

None. No client is installed, removed, activated or prohibited by this documentation/test change. Hermes remains external execution; Pantheon Cockpit remains a candidate governed projection; compatible clients remain replaceable.

## Invariants

```text
client selected != governance authority
projection != persistence
runtime success != authorization
repository co-location != authority transfer
historical reference != active owner
removed compatibility path != removed capability
```

## Exit criteria

- root architecture surfaces no longer assign current ownership to OpenWebUI;
- root README EN/FR and `CLAUDE.md` agree with current `STATUS.md`;
- the convergence rule for new candidate-support doctrine remains intact;
- tests and governance checks are green on the exact PR head before merge.
