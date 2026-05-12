# CLAUDE.md

This repository is Pantheon Next.

## Doctrine

OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.

Pantheon Next is a governance, documentation and policy layer. It must not become an autonomous agent runtime.

## Non-negotiable boundaries

Do not recreate in Pantheon Next:

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
- heavy dashboard;
- free plugin manager;
- hidden workflow runtime;
- automatic skill installer.

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
Migrate only governance, schemas, validation, read-only doctor checks, context packs and documented policies unless explicitly approved.
