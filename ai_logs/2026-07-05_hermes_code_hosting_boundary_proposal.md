# AI Log — Hermes Code Hosting Boundary Proposal

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Context

The user asked whether Hermes-side code can be hosted in the Hermes
templates inside Pantheon, then approved drafting an arbitration
proposal ("vas-y"). Inventory showed the repository already hosts
declarative Hermes material (`hermes/profiles/`, `templates/hermes/`
skills in the agentskills.io SKILL.md standard, run manifests,
handoffs, connection templates), all `candidate_template_only` and
executed outside the repo by a Hermes Agent.

## Change made

```text
Added docs/governance/HERMES_CODE_HOSTING_BOUNDARY.md
(validation-only) and its AUTHORITY_INDEX.md row.

The proposal:
- restates the settled practice: declarative Hermes material stays
  in-repo, candidate until reviewed;
- draws the line inside the SKILL.md standard: instructions/YAML are
  templates; the first executable file (*.py, *.sh, *.js) under
  templates/hermes/ or hermes/ is not a template edit and reopens
  the arbitration;
- frames Option A (separate Hermes-side repository consuming
  passports and Task Contracts — recommended) versus Option B
  (bounded hermes-adapters/ zone via explicit CLAUDE.md amendment,
  mcp-server precedent, five conditions);
- recommends Option A for the first executable artifact, Revit 2027
  prototype included.
```

## Branch note

Placed on its own branch `docs/hermes-code-boundary` because the
designated session branch still carries the open PR #284 (coverage
checker extension); mixing a script change and a doctrine proposal in
one PR would weaken both reviews. If #284 merges first, ai_logs/INDEX.md
may need a trivial refresh here.

## Boundary

```text
Documentation only. No code, no zone created, no checker change,
no schema, test, operation, platform, Docker, pyproject or .env
change. The proposal decides nothing; the User Decision Gate decides.
```

## Repo state

```text
Documented non-implemented; arbitration pending.
```
