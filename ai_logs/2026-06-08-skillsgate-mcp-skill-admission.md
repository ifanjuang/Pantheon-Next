# AI Log — SkillsGate MCP skill admission guard

Date: 2026-06-08

## Context

The maintainer asked to continue the MCP-oriented review after Row-Bot and to include `https://github.com/skillsgate/skillsgate`.

SkillsGate is a stronger admission case than a generic MCP server because it can manage AI-agent skills across many agents and exposes skill operations through CLI / TUI / desktop and MCP surfaces.

## What was reviewed

External reference:

```text
https://github.com/skillsgate/skillsgate
```

Relevant observed pattern:

```text
browse public skills
install skills to one or more agents
manage global vs project scope
sync skills from packages / node_modules
expose list / add / remove / update / sync through MCP-like tooling
```

## Change made

Updated `docs/governance/CAPABILITY_REGISTRY.md` inside PR #53 instead of creating a new standalone doctrine document.

The existing `Skill admission guard` section already stated the core rule:

```text
Availability is not authorization.
Installability is not capability approval.
```

This intervention hardens it with the SkillsGate case:

- added `visible != admitted`, `synced != reviewed`, `MCP available != task-authorized`;
- added content hash / immutable source reference to the admission metadata;
- added `sandbox_only` and `project_enabled` statuses;
- treated global install, multi-agent install, remote synchronization and automatic update as governance risks;
- added an explicit `MCP write-capable skill managers` subsection;
- separated read-only inventory, preview-before-install and write-capable external actions;
- added refusal tests for public-skill global install, multi-agent install, package sync, unpinned sources, broad file / shell / network / connector access, catalogue ranking, edited skills and client/project-data use.

## Decision posture

Accepted:

```text
Use SkillsGate as an external reference for skill inventory, per-agent status,
preview-before-install, scope distinction and MCP write-tool risk.
```

Refused:

```text
Do not adopt SkillsGate as Pantheon runtime.
Do not treat skills.sh or catalogue visibility as approval.
Do not let MCP skill installation become authorization.
Do not create a Pantheon skill marketplace or installer.
```

To verify:

```text
Whether this is sufficient inside CAPABILITY_REGISTRY.md,
or whether a later support review `reference_reviews/SKILLSGATE_MCP_SKILL_ADMISSION.md`
should be added after #53 is rebased and reviewed.
```

## Related issue

```text
#86 — MCP Skill Admission Guard — SkillsGate reference review
```

## Boundary

Documentation only. No dependency, install, runtime, MCP server, skill manager, schema, test, operation, platform, Docker or environment change.

No protected paths were touched.

The registry declares capability eligibility. The runtime may install or use skills. Pantheon admits or blocks eligibility. The human approves consequential use.
