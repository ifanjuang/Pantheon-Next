# Authority Index MCP Alignment

Status: validation-only / authority-index alignment note — to apply.

Date: 2026-06-30

This note records the intended `AUTHORITY_INDEX.md` alignment after PR #239 and the status-spine updates.

It exists because `AUTHORITY_INDEX.md` is a long authority table. Directly rewriting it without a complete non-truncated file view risks accidental data loss. This note should be used to apply a targeted row update in a controlled pass.

It does not create runtime behavior, approve a protected-path change, execute Hermes, send anything externally, authorize tools, create a dashboard or promote memory.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Reconciliation basis

PR #239 has been reviewed and merged.

```text
PR #239: fix(update): treat purely non-numeric versions as unknown
Merge SHA: af1f8d8df31b3268f38a53ac12263924771a733f
```

The status spine now says:

```text
mcp-server/ = implemented read-only / partial / protected path
```

This status is already reflected in:

- `docs/governance/WHAT_RUNS.md`;
- `docs/governance/STATUS.md`;
- `docs/governance/STATUS_SPINE_RECONCILIATION.md`;
- `docs/governance/MODULES.md`.

## Row to add or update in `AUTHORITY_INDEX.md`

Recommended grouped row:

```markdown
| `mcp-server/` | implementation artifact / read-only verification surface | implemented read-only / partial / protected path | Bounded read-only MCP policy / verification surface. PR #239 confirms the update verifier path as protected, tested read-only behavior. May validate structure/status and return status data only. Must not execute, approve, send, schedule, queue, route providers, install, update, write external systems or promote memory. Broader server coverage remains to verify. |
```

## Existing rows to preserve

Do not delete the existing candidate documentation rows automatically:

```text
docs/governance/MCP_POLICY_SERVER_CANDIDATE.md
docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md
```

They remain useful as design / development doctrine and history unless a later consolidation explicitly supersedes them.

Suggested future classifications:

```markdown
| `docs/governance/MCP_POLICY_SERVER_CANDIDATE.md` | candidate / to verify | documented non-implemented | Candidate doctrine for MCP policy-plane boundaries. Does not itself create runtime behavior. |
| `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` | candidate / development note | partially superseded by `mcp-server/` read-only artifact | Development sequence remains useful historically, but must not contradict `WHAT_RUNS.md` or `MODULES.md`. |
```

## `docs/assets/pantheon-control/` row to add or update

Recommended grouped row:

```markdown
| `docs/assets/pantheon-control/` | implementation artifact / static prototype | static prototype / partial read-only mirror / to verify | Static Pantheon Control prototype. Some logic mirrors read-only verification behavior, including the update verifier after PR #239, but the surface is not a live cockpit, approval engine, memory engine, runtime, sender, scheduler or provider router. |
```

## Boundary

The authority index should recognize implemented read-only artifacts without granting them governance authority.

```text
Implementation artifact != authority.
Read-only verification != approval.
Static prototype != live cockpit.
Candidate doctrine != runtime.
```

## Next action

Apply the above rows to `AUTHORITY_INDEX.md` in a controlled edit when a complete file view or safe patch workflow is available.

Until then, this note is the active validation-only alignment record.
