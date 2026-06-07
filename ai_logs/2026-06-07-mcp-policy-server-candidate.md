# 2026-06-07 — MCP policy server candidate

## Context

A follow-up decision was requested after review of `stormaref/Sub-Agent-MCP` and discussion of whether Pantheon could benefit from MCP.

The accepted direction is not to turn Pantheon into an MCP runtime, host or action server, but to document a candidate policy plane for MCP capability passporting and validation-only governance checks.

## Files changed

Created:

- `docs/governance/MCP_POLICY_SERVER_CANDIDATE.md`
- `templates/mcp_capability_passport.yaml`
- `templates/mcp_external_tool_review.md`

Updated:

- `templates/README.md`
- `templates/TEMPLATE_REGISTRY.md`
- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/STATUS.md`

Attempted but not completed:

- `docs/governance/README.md` index update was attempted, but the connector blocked the long update payload. No change was applied to that file.

## Classification

```text
Status: candidate / to verify.
Authority: candidate-only.
Repo state: documented non-implemented.
```

No executable server, host, gateway, client, schema, endpoint, Docker file, operations file, scheduler, queue, provider router, approval engine, memory engine or external action was added.

## Decision captured

Accepted:

- MCP can be used as interoperability vocabulary for external tools and adapters.
- Pantheon may expose governance documents as read-only MCP resources in a future external adapter.
- Pantheon may expose validation-only policy checks in a future external adapter.
- MCP capabilities should be reviewed through a Pantheon capability passport before use.

Refused:

- Pantheon as MCP host.
- Pantheon as MCP runtime.
- Pantheon as tool executor.
- Pantheon as connector gateway with implicit authority.
- Pantheon as provider router.
- Pantheon as automatic approval or memory promotion engine.

To verify:

- Whether an external `pantheon-mcp-policy-adapter` repository should be created later.
- Whether Pantheon Control should display MCP capability passports and preflight status.
- Whether the passport should later become an executable schema under `schemas/`, which would require explicit approval.

To arbitrate:

- Whether `MCP_POLICY_SERVER_CANDIDATE.md` should be promoted to active support doctrine after review.

## Boundary statement

```text
Pantheon may speak MCP.
Pantheon must not become the MCP runtime.
MCP exposes capabilities.
Pantheon governs eligibility, proof, scope, memory, approval and status.
The execution runtime acts only under contract.
The human decides.
```
