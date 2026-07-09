# Hermes Code Hosting Boundary

Status: validation-only — arbitrated: Option A (explicit maintainer decision, 2026-07-08).

Repository state: documented non-implemented.

This document arbitrates one question: **where may executable Hermes-side code live**, now that `templates/hermes/` and `hermes/profiles/` host declarative Hermes material inside Pantheon Next. It creates no code, no zone, no skill, no runtime and no checker change.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Arbitration outcome (2026-07-08)

The maintainer decided: **Option A**. Executable vertical code (Hermes-side runner, ingestion, retrieval store configuration) lives in a separate sibling repository (`pantheon-mvp-vertical`); this repository keeps only read-only artifacts — doctrine, schemas, fixtures, validators, traces. The decision is recorded in `ai_logs/2026-07-08-hosting-arbitration-option-a.md` and satisfies the B-5 referent rule. Any future proposal to host executable runtime code in this repository reopens the arbitration; it does not inherit this one.

## 1. What is already settled

Pantheon Next already hosts **declarative** Hermes material, and this is doctrine-compatible:

```text
hermes/profiles/            profile.yaml + soul.md + README per profile
templates/hermes/skills/    SKILL.md instruction skills (agentskills.io standard)
templates/hermes/           run manifests, Task Contract handoffs, returns,
                            connection templates
```

These artifacts are text that a Hermes Agent loads and executes **outside the repository**. They carry `status: candidate_template_only`, an `owner_layer: hermes` marker and a `governed_by:` pointer. Pantheon versions them with the doctrine that governs them; it does not install, activate or run them. This pattern needs no new decision.

## 2. The line this proposal draws

The `SKILL.md` standard allows a skill folder to embed executable scripts. That is where the nature changes:

```text
Declarative (stays in Pantheon):    instructions, prompts, YAML manifests,
                                    profile souls, method cards, handoffs.
Executable (triggers this rule):    scripts inside skill folders, Python
                                    tools, connectors, installable packages,
                                    OpenWebUI functions/pipes/filters as code.
```

Proposed trigger rule:

```text
The first executable file under templates/hermes/ or hermes/
(for example *.py, *.sh, *.js) is not a template edit.
It reopens this arbitration and must not merge before it.
```

## 3. Option A — separate Hermes-side repository (recommended)

Executable Hermes-side code lives in its own repository, which **consumes** Pantheon artifacts: capability passports, Task Contracts, SKILL.md templates, context packs.

```text
+ preserves the non-negotiable boundary: no Tool Runtime in the
  governance layer, no bulk runtime material in this repo;
+ the dependency stays one-way (code depends on governance, never
  the reverse) without amending CLAUDE.md;
+ Pantheon CI stays a documentation CI; code CI failures cannot
  block doctrine work, and doctrine checks cannot mask code defects;
+ the Revit 2027 prototype plan already assumes plugin code lives
  outside Pantheon.

- one more repository to operate;
- cross-repo traceability requires discipline (passport and Task
  Contract references must name the governing commit or tag).
```

## 4. Option B — bounded in-repo zone (`hermes-adapters/`)

The precedent exists: `mcp-server/` entered the monorepo through an explicit `CLAUDE.md` amendment (monorepo integration proposal) with a hard one-way boundary, its own tests and protected-path status.

The same door could admit a bounded `hermes-adapters/` zone, under the same conditions plus one:

```text
1. explicit CLAUDE.md amendment defining the zone and its refusals;
2. one-way dependency: the zone consumes the governance core and
   never the reverse;
3. protected path: no change without explicit approval;
4. its own tests, run by CI as a separate job;
5. additional condition: the code is adapter/skill code executed by
   an external Hermes Agent — the repository still never executes it,
   schedules it or routes it.
```

```text
+ one clone carries doctrine and adapters; atomic cross-references;
- every safeguard is procedural: the zone sits one bad merge away
  from the governance core, and this week showed merges can go wrong;
- CI, review culture and release cadence of code and doctrine differ
  and would be forced together.
```

## 5. Recommendation

```text
Adopt the trigger rule in section 2.
Choose Option A for the first executable artifact (Revit 2027
prototype included). Revisit Option B only if cross-repo friction
is demonstrated in practice, and then only through a CLAUDE.md
amendment, never through a quiet commit.
```

## 6. Decision classification

```text
Accepté (already practiced, restated here):
- declarative Hermes material hosted in templates/hermes/ and
  hermes/profiles/, candidate until reviewed.

Arbitré (explicit maintainer decision, 2026-07-08 — see Arbitration outcome above):
- Option A for the first real code: separate sibling repository
  (`pantheon-mvp-vertical`);
- the trigger rule stands: the first executable runtime file proposed
  inside this repository reopens the arbitration.

Refusé (either option):
- executable code merged into templates/ or hermes/ as if it were
  a template edit;
- any zone whose code the repository itself would run;
- a plugin manager, skill auto-installer or hidden workflow surface.
```

## 7. Boundary

This proposal changes no file outside itself and its index row. It adds no schema, test, operation, platform file, Docker configuration, packaging change, environment file, checker change or runtime. The User Decision Gate decides; this document only frames the decision.
