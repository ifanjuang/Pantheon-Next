# AI Log — Doctor module specification

Date: 2026-06-01

## Change

Added `docs/governance/DOCTOR_MODULE_SPEC.md` and indexed it in:

- `docs/governance/MODULES.md`
- `docs/governance/STATUS.md`

## Decision captured

```text
Doctor verifies, cites, classifies and flags.
Doctor does not edit, fix, promote or decide.
```

Boundary phrase:

```text
Doctor audits.
Zeus arbitrates.
Pantheon records status.
Humans decide.
```

## Classification

- Decision Zeus: Accepted.
- Repo state: Documented, not implemented.
- Scope: Governance Markdown only.
- Modified sensitive paths: none.
- Operations files modified: none.
- Schemas/tests/platform/Docker modified: none.

## Rationale

Doctor is now explicitly bounded as an audit-only support module. It may verify, cite, classify, flag and produce an Audit Report Candidate. It must not edit files, apply patches, promote candidates, approve outputs, create operations files, mutate memory or decide status.

## Prior checks

Checked for existing Doctor or audit-report equivalents before creating the file. No dedicated Doctor spec or Audit Report Candidate equivalent was found.

Checked repository discussions/issues for related tensions. Issue #11 contains a relevant Markdown editing/coherence-review tension: Hermes may execute editing and checking under Task Contract, but Doctor must remain audit-only and not become an editor.

## Notes

This is documentation only. It does not add executable schemas, tests, CI checks, operations files, runtime behavior, external dispatch or automatic enforcement.
