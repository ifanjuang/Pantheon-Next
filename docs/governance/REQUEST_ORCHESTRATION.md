# Request Orchestration

Status: stub — Non implémenté — à migrer depuis Pantheon-OS

This file is a placeholder to preserve governance references during Pantheon-Next bootstrap.

It is not canonical yet.

Do not use this file as implemented governance doctrine until migration and review are completed.

## Intended scope after migration

- governance-side rules for orchestrating a user request across Pantheon Roles;
- entry point classification (intake, clarification, planning, execution candidate, review, arbitration);
- role activation order recommendations;
- escalation policy between roles;
- evidence and approval bindings per orchestration step;
- safe degradation behavior when a role or capability is unavailable;
- separation between governance-side orchestration rules and runtime-side execution.

## Anti-runtime reminder

This document governs orchestration doctrine only.

It does not implement a runtime orchestrator, a scheduler, a queue, a message bus, a workflow engine or a LangGraph runtime.

Pantheon Next governs.

Hermes Agent executes.

OpenWebUI exposes.
