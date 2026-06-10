# CLAUDE.md

This repository is Pantheon Next.

## Doctrine

OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.

Pantheon Next is a governance, documentation and policy layer. Its governance core must not become an autonomous agent runtime.

The repository may host two bounded modules that consume the governance core — never the reverse (see Repository structure).

## Repository structure (monorepo with hard boundary)

Pantheon Next is a monorepo with one hard internal boundary. Three zones:

- the governance core — doctrine, schemas, validation, read-only checks. It is pure: it depends on nothing in the other zones.
- `mcp-server/` — a read-only policy / validation MCP surface centered on the capability passport: it serves and validates passports and exposes the governance core (and its read-only checks) to Hermes Agent and OpenWebUI. It is the connection point to Hermes.
- `dashboard/` — a thin, light surface that verifies installs from their logs (is it installed, does it answer, are the checks green), including on a NAS, and lets the user view evidence logs and propose governed edits to Registre Probatoire entries. It runs no agent and decides nothing; any proposed evidence edit is a governed candidate through the chokepoint, not a direct write.

The dependency is one-way: `mcp-server/` and `dashboard/` depend on the governance core; the governance core never depends on them. The boundary moves from the repo edge to the module edge. Pantheon still governs and does not execute; exposure and verification live in their own modules and remain candidates until reviewed.

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

- `mcp-server/` stays read-only / validation / candidate-preparation, centered on the capability passport. It serves and validates passports, checks scope and approval level, runs read-only doctor checks and returns the policy decision as data. It does not execute a capability, route a provider, send externally, schedule, queue or promote memory.
- `dashboard/` stays a thin, light surface: it verifies installs from their logs and liveness, shows state and gate decisions, lets the user view evidence logs and prepare proposed Registre Probatoire edits. A proposed evidence edit is a governed candidate that routes through the chokepoint and the User Decision Gate — never a direct write. It must not become a heavy dashboard, an automatic skill installer, an orchestrator, an approval engine or any runtime. It decides nothing; the gate decides.

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

This repository is a clean extraction from the historical Pantheon OS repository.

Do not bulk-copy runtime folders from Pantheon OS.
Migrate only governance, schemas, validation, read-only doctor checks, context packs and documented policies into the governance core unless explicitly approved.

The `mcp-server/` and `dashboard/` modules are built here as new, bounded code — not bulk-copied from Pantheon OS runtime. Anything placed in them stays read-only or thin per the boundaries above, and remains a candidate until reviewed.
