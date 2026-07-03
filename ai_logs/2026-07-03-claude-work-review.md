# AI log — Claude work review

Date: 2026-07-03

## Scope

Reviewed recent Claude-authored or Claude-generated work visible in the repository, especially PRs #250 to #268 and the handoff issue #264.

## Doctrine baseline read

Active sources checked before review:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

Baseline retained:

- OpenWebUI exposes.
- Hermes Agent executes.
- Pantheon Next governs.
- Pantheon is not a runtime, scheduler, queue, provider router, approval engine, memory promotion engine or external-action system.

## Review result

### Accepted

- PR #267: upstream alignment of OpenWebUI/Hermes templates is coherent as candidate/non-executable adapter material.
- PR #268: OpenWebUI primitive mapping is coherent and prevents confusing native primitives with Pantheon cockpit concepts.
- PR #256: referent rule is a useful anti-sprawl rule; it governs promotion and demotes nothing by itself.
- PR #258: architecture domain-pack move is coherent with B-4, but it touches protected references as part of the approved move.
- PR #259 and #263: vertical slice phase 1 and phase-2 bridge remain honest: proof of governance spine and candidate wiring, not runtime execution.

### To verify

- PR #250: description says no protected-path change, but changed files include `pyproject.toml` and `mcp-server/pyproject.toml`. The version metadata change may be acceptable, but the description was inaccurate under the protected-path rule.
- PR #251: `CLAUDE.md` was modified; accepted as explicitly B-1 protected edit, but it remains a protected-path precedent.
- PR #267: `templates/hermes/connection/hermes_openai_connection.template.yaml` names `GET /health`; endpoint availability should remain to verify against the actual Hermes runtime.
- PR #267/#268: OpenWebUI event wording should avoid brittle counts such as `28+` and say current event catalog must be verified at implementation time.

### To arbitrate / maintainer-only

- Issue #264 remains open:
  - tags `v0.1.59` and `v0.1.60` still require maintainer action if not created elsewhere;
  - source-PDF licence status remains a maintainer/legal decision;
  - purging old PDFs from git history requires a coordinated history rewrite;
  - the real OpenWebUI -> Hermes run remains external infrastructure work.

## Repo state

- No rollback recommended.
- No runtime implementation should be claimed from these PRs.
- Current state is mostly documented non-implemented / candidate templates, with some read-only verification artifacts already present.

## Notion note

A Notion cleanup issue occurred during this review: several empty databases named `x` were accidentally created. One was moved to trash; other cleanup attempts were blocked by tool safety controls and need manual deletion if still visible.
