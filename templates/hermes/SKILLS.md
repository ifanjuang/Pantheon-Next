# Hermes Skills Surface

Status: candidate template only — declarative skill index and review contract.

The authoritative skill artifacts in this template are the individual files under:

```text
templates/hermes/skills/<skill-name>/SKILL.md
```

This file does not duplicate their instructions. It defines how they are classified and reviewed as a set.

## Meaning of a skill

A Hermes skill is bounded execution guidance loaded by an external runtime. It may reference a Pantheon Competence or Capability Slot, but it is not itself:

- a Pantheon governance role;
- an approval;
- an installed tool;
- an activated binding;
- a task authorization;
- Evidence;
- canonical Knowledge.

```text
skill documented != skill installed
skill installed != binding healthy
binding healthy != binding safe
skill loaded != task authorized
skill completed != result accepted
```

## Required skill metadata and content

Each `SKILL.md` must make the following explicit in human-readable form or front matter when supported by the upstream standard:

- stable skill identity and purpose;
- candidate status;
- owner layer (`hermes`);
- governing Pantheon owners or Capability Slot;
- expected inputs and Context Pack assumptions;
- allowed tools or abstract capabilities;
- prohibited effects and escalation conditions;
- expected candidate return shape;
- provenance and trace requirements;
- uncertainty, contradiction and capability-gap behavior;
- external version or upstream assumptions when material.

## Review sequence

Before a skill is considered usable by an external Hermes installation, review separately:

1. abstract function and overlap with existing Competence or Capability Slot;
2. candidate binding;
3. installation state;
4. health observation;
5. compatibility with the observed Runtime Profile;
6. safety and policy constraints;
7. activation state;
8. task-specific authorization;
9. return, Evidence and human-review gates.

No step implies the next.

## Repository constraints

Skills in this repository remain declarative. Do not add executable scripts, packages, installers, provider routers, queues or schedulers under `templates/hermes/skills/`.

The executable-code boundary is owned by:

```text
docs/governance/HERMES_CODE_HOSTING_BOUNDARY.md
```

## Evolution checks

When Pantheon or `pantheon-mvp` evolves, review all active skills for:

- stale internal route names, especially removed `/v1` prefixes;
- obsolete generation labels or renamed active artifacts;
- changed Claim, Evidence, ChangeCandidate or approval semantics;
- changed Capability Slot, binding, activation or task-authorization semantics;
- changed Runtime Profile or Runtime Observation envelopes;
- implicit source-of-truth, memory-promotion or approval claims;
- dependencies mentioned as adopted solely because they are available upstream.

A successful textual review is not runtime acceptance. Runtime acceptance requires observation against an exact external installation and version.
