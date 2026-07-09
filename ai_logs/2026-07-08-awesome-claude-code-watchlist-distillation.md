# awesome-claude-code watchlist distillation

Date: 2026-07-08

## Change

Distilled `https://github.com/hesreallyhim/awesome-claude-code` into the existing Pantheon Next watchlist structure.

Touched files:

- `docs/governance/WATCHLIST.md`
- `docs/governance/SKILL_WATCHLIST.md`

## Why

`awesome-claude-code` is useful as an ecosystem map for Claude Code-related skills, hooks, MCP servers, sandboxes, memory/context tools, observability, cost monitoring and security resources.

Pantheon should watch this ecosystem without importing it as a dependency, trust registry, marketplace, plugin manager, MCP catalogue, install queue or approval source.

## Governance classification

```text
status: documented non-implemented / watchlist only
implementation_added: no
runtime_added: no
dependency_added: no
schema_added: no
protected_paths_touched: no
approval_created: no
memory_promoted: no
```

## Distillation

`WATCHLIST.md` now records `hesreallyhim/awesome-claude-code` as a Claude Code ecosystem watch item with status `boundary_required`.

`SKILL_WATCHLIST.md` now records it as a watched source with explicit forbidden imports:

- no automatic skill, hook, MCP, plugin or command installation;
- no trust by catalogue inclusion;
- no hook execution treated as workflow governance;
- no MCP connection treated as external-action authorization;
- no memory/context tool treated as Pantheon memory;
- no observability dashboard treated as proof, approval or professional validation.

## Risks and limits

This change does not review each listed third-party repository.

Each concrete resource from the catalogue still requires separate boundary review before it may become:

- a Hermes Skill Candidate;
- a Hermes capability binding candidate;
- an OpenWebUI exposure pattern;
- an operational-state card;
- a rejected pattern.

The catalogue remains an external reference and cannot govern Pantheon.

## Result

```text
OpenWebUI may expose the watch item.
Hermes may later test a specific reviewed binding.
Pantheon governs the status and gates.
The human decides.
```
