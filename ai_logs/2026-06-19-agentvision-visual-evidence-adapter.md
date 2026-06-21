# AI Log — AgentVision / Visual Evidence Adapter Review

Date: 2026-06-19

## Trigger

The user asked to proceed after reviewing AgentVision, an external project presented as a visual feedback loop for AI coding agents.

The goal was to classify the idea inside Pantheon Next without turning the tool into a governance authority or implementation dependency.

## Doctrine read / active constraints

The active project instruction requires significant Pantheon Next work to start from:

```text
docs/governance/STATUS.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
```

The current repository pattern was also checked through the recent Langfuse observability adapter review, which placed a named product under `docs/governance/reference_reviews/` and kept Pantheon authority separate from observability tooling.

Relevant prior classification pattern:

```text
Langfuse observes the run.
Hermes carries the work.
The Dashboard exposes the trace.
Pantheon qualifies the status.
The human decides.
```

## Repository coordination checked

Recent PRs and review comments were inspected to identify live conflicts and useful precedents.

Relevant signals:

```text
PR #147 — Langfuse / Hermes observability adapter review.
PR #151 — Architecture OS reconciliation accepted as validation-only.
PR #155 — Architecture Source Policy candidate, still documented non-implemented.
PR #156 — dashboard UX review found a rendering-breaking JavaScript quote issue.
PR #157 — landing review found mobile source-card selector mismatch and possible overflow.
PR #158 — shared schema definitions seed is open and not wired.
PR #159 — dashboard dependency mockup review found shared toast styles conflicting with evidence toasts.
```

These discussions are not canonical doctrine by themselves.

They were used as coordination signals only.

## External reference

External references recorded in the review document:

```text
https://github.com/amitpatole/agent-vision
https://pypi.org/project/agentvision/
```

The document intentionally does not lock current package maturity, release status or security posture as stable doctrine.

Those facts must be rechecked before any implementation pass.

## Change made

Added:

```text
docs/governance/reference_reviews/AGENTVISION_VISUAL_EVIDENCE_ADAPTER.md
```

The document classifies AgentVision as a candidate visual evidence adapter.

It defines accepted, refused, to verify and to arbitrate sections.

It keeps AgentVision outside Pantheon core and outside canonical validation.

## Classification

```text
Accepted:
- AgentVision as a candidate visual evidence adapter.
- Hermes may request visual observation in a future implementation.
- The Dashboard may expose read-only report/status summaries.
- Visual findings may support Visual Evidence Pack Candidates.
- Pantheon retains authority over status, evidence, approval, scope and memory.

Refused:
- AgentVision as Pantheon runtime.
- AgentVision PASS as approval.
- AgentVision PASS as accessibility compliance.
- Vision critique as source of truth.
- Visual report as Evidence Pack, memory promotion or external-action authorization.
- Auto-fix loop as permission to commit, merge, publish or deploy.

To verify:
- package maturity, license, release state and maintenance signals;
- sandboxing and data retention;
- stable report format;
- whether grounded local checks are enough for the first pass;
- whether a generic Visual Evidence Candidate contract is needed before schema work.

To arbitrate:
- first evaluation scope;
- CLI vs Hermes adapter vs MCP vs REST vs CI advisory;
- whether visual failures block PRs or only warn;
- where screenshots, diffs and reports live;
- whether semantic critique is disabled initially.
```

## Boundary

Documentation only.

No Python dependency added.
No `pyproject.toml` change.
No Docker change.
No `.env` change.
No `operations/` change.
No `platform/` change.
No schema change.
No test change.
No CI change.
No runtime code added.
No Dashboard implementation added.
No Hermes integration added.
No connector added.
No approval engine added.
No memory engine added.
No external action authorized.

Repository state: documented non-implemented.

## Verification target

Real diff should show exactly two added files:

```text
docs/governance/reference_reviews/AGENTVISION_VISUAL_EVIDENCE_ADAPTER.md
ai_logs/2026-06-19-agentvision-visual-evidence-adapter.md
```

No protected path should be touched.
