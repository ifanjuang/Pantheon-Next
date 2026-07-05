# Loop Governance Model — Authority Index Row Candidate

Status: validation-only.

Repo state: documented non-implemented.

This note records the candidate `AUTHORITY_INDEX.md` row for PR #282. It does not replace the authority index.

## Candidate row

```markdown
| `docs/governance/LOOP_GOVERNANCE_MODEL.md` | candidate support doctrine | documented non-implemented | Bounded runtime-loop governance model: admissibility, candidate data shapes, blockers, stop rules, event/status separation and checker gates. No loop engine, scheduler, queue, runtime, schema, test, approval engine, memory engine or external action. |
```

## Decision

Accepted:

```text
- The document should be indexed before promotion or merge.
- Authority class remains candidate support doctrine.
- Repo state remains documented non-implemented.
```

Refused:

```text
- Active support doctrine status now.
- Executable schema status now.
- Any implementation claim.
```

To arbitrate:

```text
- Insert directly in PR #282, or during a safe authority-index pass.
```
