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

- the governance core — doctrine, schemas, validation, read-only checks. It is pure: it depends on nothing in the other zones.
- `mcp-server/` — the read-only policy / validation surface. It serves and validates the capability passport and runs the read-only verifications (install, observability, backup, exposure, update — the `verify_*` doctor checks), returning verdicts as data. It is the connection point to Hermes Agent and OpenWebUI. It verifies; it is not the UI.
- the exposure surface — where decisions and state are shown. Today it exists only as a static prototype in `docs/assets/pantheon-control/` (an HTML/JS mockup that mirrors the read-only verdicts and lets a user view evidence logs and prepare governed edits). A real `dashboard/` module is **voluntarily absent** until it is actually built; when it exists it will display, not verify — the UI exposes, `mcp-server/` verifies.

The dependency is one-way: `mcp-server/` and the exposure surface depend on the governance core; the governance core never depends on them. The boundary moves from the repo edge to the module edge. Pantheon still governs and does not execute; verification and exposure live in their own zones and remain candidates until reviewed.

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
- the exposure surface (`docs/assets/pantheon-control/` prototype today; a `dashboard/` module later) stays thin: it displays install / liveness verdicts, state and gate decisions, and lets the user view evidence logs and prepare proposed Registre Probatoire edits. A proposed evidence edit is a governed candidate that routes through the chokepoint and the User Decision Gate — never a direct write. It must not become a heavy dashboard, an automatic skill installer, an orchestrator, an approval engine or any runtime. It decides nothing; the gate decides.

A consequential effect still routes through the governance check (the chokepoint). No module bypasses it.

## Work rules

Before proposing or changing governance, read the relevant Markdown source of truth first.

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

Every significant AI intervention must add an entry in `ai_logs/`.

## Runtime policy

OpenWebUI is the cockpit.
Hermes Agent is the execution runtime.
Pantheon Next is the governance source of truth.

Hermes profiles may produce candidates under Task Contract.
They must not approve, canonize, promote memory, bypass approvals or merge changes.

OpenWebUI functions, actions, pipes, filters and pipelines are execution surfaces. They must remain candidates until reviewed.

## Repository migration policy

This repository is the self-contained canonical governance repository. Its historical predecessor is retired and is not a source dependency.

Do not reintroduce runtime folders from historical sources.
Migrate only governance, schemas, validation, read-only doctor checks, context packs and documented policies into the governance core unless explicitly approved.

The `mcp-server/` module and the exposure-surface prototype (`docs/assets/pantheon-control/`) are built here as new, bounded code rather than inherited runtime. Anything placed in them stays read-only or thin per the boundaries above, and remains a candidate until reviewed.
