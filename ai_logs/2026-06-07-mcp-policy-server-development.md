# AI Log — MCP Policy Server development roadmap

Date: 2026-06-07

## Context

The user asked to keep installer work in a separate discussion and to focus this discussion on the MCP Policy Server.

The user requested documentation first, specifically on development steps rather than executable implementation.

Related context:

```text
PR #67 — Pantheon Control dashboard candidate doctrine
PR #72 — Pantheon Control installation boundary
PR #53 — governed composition / capability registry / two gates
PR #66 — module invocation and connectivity preflight doctrine
```

## Action

Created documentation-only roadmap:

```text
docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md
```

The document defines phases for future MCP development:

```text
0. Boundary freeze
1. Canonical source map
2. Resources
3. Prompts
4. Read-only validation tools
5. Hermes integration contract
6. Development fixtures
7. Refusal tests
8. Implementation candidate gate
```

## Decision classification

Accepted:

```text
MCP Policy Server as read-only / validation / candidate-preparation layer.
Hermes remains execution runtime.
Pantheon remains governance authority.
Installer/dashboard work remains under Pantheon Control and separate from this thread.
```

Refused:

```text
MCP as runtime.
MCP as scheduler or queue.
MCP as approval engine.
MCP as memory promotion engine.
MCP as connector gateway.
MCP as plugin manager or skill installer.
MCP as Docker/installer concern.
```

To verify:

```text
Exact source files to expose as MCP resources once related candidate PRs are merged or rejected.
Whether PR #53 and PR #66 become canonical before implementation starts.
Whether PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md should be indexed in MODULES.md / STATUS.md / AUTHORITY_INDEX.md after review.
```

To arbitrate:

```text
Whether future implementation may live under pantheon-control/mcp-policy-server/.
Whether MCP tools should be modeled as capability declarations in the capability registry.
Which refusal tests are mandatory for v0.1.
```

## Repo state

```text
documented non-implemented
```

No MCP server, Docker stack, `.env`, installer, dashboard, platform code, operations procedure, schema, test suite, scheduler, queue, approval engine, memory engine, provider router or external action was implemented.

## Next

Review the roadmap, then decide whether to open a dedicated draft PR and how to reconcile it with PR #67, PR #66 and PR #53.
