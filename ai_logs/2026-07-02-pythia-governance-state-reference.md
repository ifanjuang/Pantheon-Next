# AI Log — Pythia governance-state reference review

Date: 2026-07-02

Branch: `docs/governance-state-api`

## Trigger

User asked to review:

```text
https://github.com/jangles-byte/Pythia
```

The useful signal was Pythia's one-call agent-facing situational view, especially the idea that a downstream agent can inspect a compact machine-readable state rather than reconstructing all sources.

## Repository checks

Read before intervention:

```text
docs/governance/STATUS.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/CARD_STACK_MODEL.md
docs/governance/MODULES.md
docs/governance/README.md
```

Relevant open signals checked:

```text
PR #259 — governed vertical slice architecture_devis_reprise
PR #189 / #190 — external capability candidates and effect-review posture
Issue #192 — Intent Candidate log in Pantheon Control
Issue #182 — static cockpit refactor
Issue #146 — Langfuse observability adapter candidate
Issue #128 — AgentCanvas trace visualization reference
Issue #135 — AI tool capability placement matrix
Issue #41 — prefer PRs over direct-to-main and avoid doctrine sprawl
```

## Decision

Accepted:

```text
Pythia as external reference for a single machine-readable situational view.
```

Accepted:

```text
Distill the idea into a candidate `governance_state_view` shape inside a reference review.
```

Refused:

```text
Pythia as Pantheon dependency, runtime, oracle, prediction authority, approval engine,
memory engine, source of truth or action mechanism.
```

Refused for now:

```text
Creating a standalone `GOVERNANCE_STATE_API.md` immediately.
```

Reason:

```text
CARD_STACK_MODEL.md already exists and is indexed as candidate support doctrine.
Issue #41 warns against doctrine sprawl.
The safer first step is a reference review under `reference_reviews/`, which is already indexed as a grouped row in AUTHORITY_INDEX.md.
```

To verify:

```text
Whether `governance_state_view` should later become a dedicated candidate support doctrine document,
be folded into CARD_STACK_MODEL.md, or remain adapter/reference material.
```

To arbitrate:

```text
Whether a future read-only MCP policy surface should expose a full governance-state view or only narrow status checks.
```

## Files changed

```text
Added docs/governance/reference_reviews/PYTHIA_GOVERNANCE_STATE_REVIEW.md
Added ai_logs/2026-07-02-pythia-governance-state-reference.md
```

## Repo state

```text
Documented non-implemented.
```

No schema, test, operations, platform, Docker, `.env`, `pyproject.toml`, `mcp-server/` or runtime file was changed.

## Boundary

```text
A governance-state view may expose what is known, proposed, blocked or awaiting decision.
It must not decide truth, proof, approval, memory or action authorization.
```

The validated remains.
