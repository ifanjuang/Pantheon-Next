# Hermes Skills Surface

Status: candidate template only — collection-level index.

Authoritative skill instructions remain in `templates/hermes/skills/<skill-name>/SKILL.md`. This file does not duplicate them; it defines the minimum review contract for the collection.

A Hermes skill is bounded execution guidance for an external runtime. It may reference a Pantheon Competence or Capability Slot, but it is not a Role, tool installation, binding activation, task authorization, Evidence or canonical Knowledge.

## Minimum skill contract

Each `SKILL.md` must identify:

- stable purpose and candidate status;
- governing owner or Capability Slot;
- expected inputs and Context assumptions;
- allowed abstract capabilities and prohibited effects;
- return, provenance, trace and uncertainty requirements;
- escalation behavior for contradictions, missing authorization and capability gaps;
- material upstream or runtime-version assumptions.

## Review sequence

Review separately: abstract function, candidate binding, installation, health, compatibility, safety, activation, task authorization and return/Evidence/human gates. No state implies the next.

Skills in this repository stay declarative. Executable Pantheon adapters belong under the bounded `implementation/` responsibility governed by `docs/governance/REPOSITORY_PLACEMENT.md`; Hermes runtime execution remains external under `docs/governance/HERMES_INTEGRATION.md`. Executable scripts, installers, provider routers, queues and schedulers do not belong in this template surface.

When either repository evolves, check active skills for stale routes or names, changed Claim/Evidence/ChangeCandidate semantics, changed capability and authorization gates, and dependencies presented as adopted merely because they are available.

Runtime Profile and Runtime Observation support described by open PRs remains candidate until those PRs merge. A textual review is not runtime acceptance against an exact external installation.