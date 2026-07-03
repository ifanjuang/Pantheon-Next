# AI Log — Hermes Page-Agent Integration Framing

Date: 2026-07-03

## Context

The user asked to continue from the Page-Agent Chrome / Hermes skill candidate review and think concretely about how to integrate it into Hermes.

## Repository action

Created:

```text
docs/governance/HERMES_PAGE_AGENT_INTEGRATION.md
```

## Classification

```text
Authority: candidate support doctrine
Repo state: documented non-implemented
Decision Zeus: to verify / to arbitrate before runtime use
```

## Accepted

- Hermes may wrap Page-Agent MCP as a candidate browser-control adapter.
- The raw Page-Agent `execute_task` must not be exposed as an unrestricted user-facing command.
- The first admissible prototype is P0 read-only: status + observe only.
- The adapter must distinguish installed, connected, available, preflighted, task-authorized and action-approved.
- The adapter must return Result Candidate, Evidence Pack Candidate, Outcome Observation Candidate or Capability Gap.

## Refused

- No Page-Agent installation.
- No Chrome extension activation.
- No Hermes skill implementation.
- No MCP server process.
- No runtime endpoint.
- No schema or test changes.
- No browser execution authorization.
- No default `execute_javascript`.
- No silent submit, send, delete, publish, upload, filing, signature, payment or status change.

## Key boundary

```text
The browser extension exposes page capability.
Page-Agent MCP carries browser-control transport.
Hermes constrains and executes bounded adapter calls.
Pantheon governs scope, status, evidence, memory and approval.
OpenWebUI / Pantheon Control exposes warnings and gates.
The human decides.
```

## Next action

Review and merge this documentation if accepted, then create a separate runtime-side implementation plan for a sandbox P0 read-only adapter outside Pantheon.
