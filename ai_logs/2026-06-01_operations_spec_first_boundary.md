# AI Log — Operations spec-first boundary

Date: 2026-06-01

## Change

Added an operations boundary rule to `docs/governance/CAPABILITY_PLACEMENT.md`.

## Decision captured

```text
Spec first.
Operations second.
Execution elsewhere.
```

No file under `operations/` may be created or modified before a governing documentation spec has been explicitly validated.

## Classification

- Decision Zeus: Accepted.
- Repo state: Documented, not implemented.
- Scope: Governance Markdown only.
- Modified sensitive paths: none.
- Operations files modified: none.

## Rationale

The rule prevents `operations/` from becoming a back door for unvalidated runtime behavior, hidden workflow authority, scheduler behavior, approval logic or memory mechanisms.

`operations/` may only translate validated governance into procedural guidance. It must not invent doctrine, promote candidates, define runtime behavior or bypass approval.

## Verification

Checked active governance context before modification:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

Open PR check found no open pull requests in the repository at the time of intervention.

## Notes

This change is documentation only. It does not add a schema, CI check, hook, operation file, runtime behavior or automated enforcement.
