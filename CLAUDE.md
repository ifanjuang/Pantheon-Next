# CLAUDE.md

This repository is Pantheon Next.

## Doctrine

OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.

Pantheon Next is a governance, documentation and policy layer. Its governance core must not become an autonomous agent runtime.

The repository may host bounded surfaces that consume the governance core — never the reverse (see Repository structure).

## Repository structure (monorepo with hard boundary)

Pantheon Next is a monorepo with one hard internal boundary. Its zones:

- the governance core — doctrine, schemas, validation, read-only checks. Its *artifacts* are pure: no doctrine, schema or governed document depends on another zone. Its CI checks under `.github/scripts/` may import the read-only validators `mcp-server/` already exposes (`pantheon_mcp.doctor`, `pantheon_mcp.authority_index`) rather than duplicate them; that is a validation-time reuse of a pure function, not a doctrinal dependency, and it never runs, executes or exposes anything.
- `mcp-server/` — the read-only policy / validation surface. It serves and validates the capability passport and runs the read-only verifications (install, observability, backup, exposure, update — the `verify_*` doctor checks), returning verdicts as data. It is the connection point to Hermes Agent and OpenWebUI. It verifies; it is not the UI.
- the exposure surface — the executable candidate cockpit is owned by the external repository `ifanjuang/pantheon-mvp`. In Pantheon Next, `docs/assets/pantheon-control/` is only an orientation point plus explicitly allowlisted validation-support artifacts. A real in-repo `dashboard/` module is **voluntarily absent**. The UI exposes; `mcp-server/` verifies.

The dependency is one-way: `mcp-server/`, bounded validation-support artifacts and external consumers may depend on the governance core; the governance core never depends on them. External consumption follows `docs/governance/NEXT_MVP_REPOSITORY_PLACEMENT.md`: explicit manifest, exact pin, upstream priority on divergence and report-only drift detection owned by the consumer. Pantheon still governs and does not execute; verification and exposure remain candidates until reviewed.

## Non-negotiable boundaries

The governance core must not recreate:

- Execution Engine;
- Agent Runtime;
- Tool Runtime;
- LLM Provider Router;
- internal scheduler;
- central LangGraph runtime;
- message bus;
- mandatory agent queue;
- auto-promoted memory;
- self-evolution auto-merge;
- free plugin manager;
- hidden workflow runtime.

The in-repo modules are bounded, not free:

- `mcp-server/` stays read-only / validation / candidate-preparation, centered on the capability passport. It serves and validates passports, checks scope and approval level, runs the read-only doctor / verification checks and returns the decision as data. It does not execute a capability, route a provider, send externally, schedule, queue or promote memory, and it does not become the UI.
- `docs/assets/pantheon-control/` stays an orientation point plus a closed inventory of validation-support artifacts: a mutation-disabled synthetic Hermes preview, six read-only classifier mirrors and one still-referenced governance specification. It is not a product cockpit, fallback UI, runtime probe or project-data surface. Any executable cockpit belongs in `pantheon-mvp`; any future in-repo `dashboard/` requires a separate reviewed boundary decision.

A consequential effect still routes through the governance check (the chokepoint). No module bypasses it.

## Work rules

Before proposing or changing governance, read the relevant Markdown source of truth first.

Before creating a new Markdown governance document under `docs/governance/`, first verify that no existing canonical, active or candidate owner can absorb the responsibility. Prefer updating, merging, promoting or archiving existing doctrine. A new `candidate support doctrine` document must name a genuinely distinct responsibility, identify its relationship to the existing concept/authority owner and state its intended convergence or retirement path. `ai_logs/`, generated reports and required conformance fixtures are intervention or validation artifacts, not doctrine expansion.

Before significant parallel work, announce the repository paths that may be changed. A rename announces both the old and new path. When two active announcements overlap, divide or sequence the shared paths before modification.

The announcement is a coordination signal only. It is not a lock, does not grant authority and does not reserve a responsibility.

Markdown governance documents are authoritative over code unless code exposes a demonstrably better implementation. In that case, propose the documentation update first.

Do not claim that a component is implemented if it is only documented.

Always distinguish:

- implemented;
- documented but not implemented;
- implemented but not documented;
- partial;
- obsolete;
- contradictory;
- to verify;
- non implemented.

Every significant AI intervention must add an entry under `ai_logs/<year>/Q<n>/`. Existing flat logs remain valid historical paths and are not migrated automatically.

## Runtime policy

OpenWebUI is the cockpit.
Hermes Agent is the execution runtime.
Pantheon Next is the governance source of truth.
The human decides what is consequential.

Hermes profiles may produce candidates under Task Contract.
They must not approve, canonize, promote memory, bypass approvals or merge changes.

OpenWebUI functions, actions, pipes, filters and pipelines are execution surfaces. They must remain candidates until reviewed.

## Repository migration policy

This repository is the self-contained canonical governance repository. Its historical predecessor is retired and is not a source dependency.

Do not reintroduce runtime folders from historical sources.
Migrate only governance, schemas, validation, read-only doctor checks, context packs and documented policies into the governance core unless explicitly approved.

The `mcp-server/` module and the allowlisted validation-support artifacts under `docs/assets/pantheon-control/` are bounded code and documentation. The executable cockpit and product demos live in `ifanjuang/pantheon-mvp`. Nothing in Next may silently recreate a second cockpit, import its executable assets or infer adoption, installation or activation from an external implementation.
