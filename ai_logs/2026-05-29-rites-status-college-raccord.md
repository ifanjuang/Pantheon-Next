# 2026-05-29 - Rites status and Governance College raccord

## Summary

Raccorded the new Rites governance layer to `docs/governance/STATUS.md` and `docs/governance/GOVERNANCE_COLLEGE.md`.

## Files changed

- `docs/governance/STATUS.md`
- `docs/governance/GOVERNANCE_COLLEGE.md`

## Reason

The first Rites pass added the doctrine files, governance index entry, changelog entry and AI log.

This follow-up makes the repository state and Governance College doctrine explicit:

- Rites are active shared governance doctrine.
- Rites coordinate methods across roles.
- Rites do not create new roles.
- Rites do not implement runtime behavior.
- Agora remains the visible deliberation space.
- ZEUS arbitrates status and procedure.
- The human decides when procedural arbitration is insufficient.

## Boundary

This pass does not modify schemas, tests, operations, Docker, environment files or runtime configuration.

It does not implement:

- rite runtime;
- automatic rite trigger engine;
- hidden rite debate loop;
- role runtime;
- Hermes skill installation;
- OpenWebUI plugin;
- automatic approval;
- automatic memory promotion.

## Risk note

The main risk is treating a rite as an executable workflow or hidden orchestration system.

The mitigation is now recorded in both `STATUS.md` and `GOVERNANCE_COLLEGE.md`.
