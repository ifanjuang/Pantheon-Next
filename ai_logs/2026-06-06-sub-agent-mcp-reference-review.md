# 2026-06-06 — Sub-Agent-MCP reference review

## Context

A review was requested for `stormaref/Sub-Agent-MCP` and its possible interest for Pantheon Next.

The repository describes a Python MCP server that exposes YAML-defined sub-agents as MCP tools, builds LangChain agents with OpenAI-compatible models and optional downstream MCP servers, and returns sub-agent responses to a parent LLM.

## Files changed

Created:

- `docs/governance/reference_reviews/SUB_AGENT_MCP.md`

Updated:

- `docs/governance/reference_reviews/README.md`

## Classification

```text
Status: documented, not implemented.
Authority: external reference / support review only.
Repo state: documented non-implemented.
```

The review does not approve installation, dependency adoption, runtime migration, OpenWebUI tool exposure, Hermes skill installation, MCP runtime creation, automatic approval, automatic memory promotion or external-action automation.

## Decision captured

Accepted:

- Sub-Agent-MCP is useful as an external runtime / adapter reference.
- Its per-agent model, prompt, MCP server and allowlist pattern can inform adapter vocabulary.
- Its delegation model may be tested outside Pantheon as a Hermes-side candidate under Task Contract.

Refused:

- Sub-Agent-MCP as Pantheon runtime.
- YAML agent configuration as doctrine.
- MCP tool availability as capability authorization.
- Sub-agent completion as truth, approval, proof or Canonical Memory.

To verify:

- Whether a future external adapter should wrap Sub-Agent-MCP calls with the Pantheon envelope:

```text
Task Contract in
-> adapter
-> Result Candidate + Evidence Pack Candidate out
```

To arbitrate:

- Whether Sub-Agent-MCP deserves future prototype testing behind Hermes, starting with a low-risk `source_auditor` agent.

## Risks and limitations

Main risks identified:

- runtime drift;
- authorization drift;
- evidence drift;
- approval drift;
- memory drift;
- scope drift.

The current Sub-Agent-MCP response shape is not enough for Pantheon-governed work because raw `{ response }` output must be downgraded to `Result Candidate` and supported by an `Evidence Pack Candidate` before review.

## Boundary statement

```text
Sub-Agent-MCP may delegate execution.
It does not authorize capability, truth, memory, approval or action.
Runtime may propose.
Pantheon governs eligibility, proof, status and approval.
The human decides.
```
