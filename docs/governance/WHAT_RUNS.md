# What Runs

Status: active support / repository runtime-status map — to verify.

Date: 2026-06-30

This document states what currently runs, what is static documentation, what is partial or to verify, and what is intentionally absent.

It is a status-honesty map. It does not create runtime behavior, approve any tool, install an adapter, authorize external action, create a scheduler, create a queue, create an approval engine or promote memory.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon governs status. Therefore the repository must state its own operational status plainly.

A static prototype is not a live cockpit.
A read-only checker is not an approval engine.
A documented workflow is not an implemented workflow.
A candidate adapter is not an installed capability.
A demo fixture is not a production data platform.

## Status vocabulary

Use these labels in this file:

```text
runs
static prototype
partial / to verify
documented non-implemented
candidate only
voluntarily absent
protected review required
external / outside Pantheon
```

## Runs or exists now

| Area | Current status | Meaning | Boundary |
|---|---|---|---|
| Repository documentation | runs | Markdown doctrine, support doctrine, candidates, examples and logs exist in the repo. | Documentation does not implement execution. |
| GitHub Pages landing | runs / static documentation | Public documentation pages are served as static files. | Static publication is not product availability. |
| `docs/index.html` | static documentation | Public-facing landing page. | Must not imply live runtime capabilities beyond status docs. |
| `docs/rag-probatoire.html` | static documentation | Public explanatory page for RAG probatoire. | Demonstrates doctrine, not a running RAG engine. |
| `docs/assets/pantheon-control/` | static prototype / to verify | Static Pantheon Control prototype assets and pages. | Prototype display is not a live cockpit, approval engine, memory engine or runtime. |
| `schemas/` | partial / protected review required | Validation artifacts may exist. Exact status must be checked before relying on them. | Schemas validate structure; they do not execute or approve. |
| `tests/` | partial / protected review required | Tests may exist. Exact coverage must be checked before relying on them. | Tests do not promote doctrine by themselves. |
| `mcp-server/` | partial / to verify / protected review required | Repository appears to contain or reference a read-only policy / verification surface, but the exact status must be reconciled across `STATUS.md`, `AUTHORITY_INDEX.md` and `MODULES.md`. | A read-only verification surface may return status data only; it must not execute, approve, send, schedule, route providers or promote memory. |
| `ai_logs/` | runs as trace | Intervention logs exist as validation-only trace. | Logs are not doctrine and do not approve changes. |
| Notion Kanban | external / outside Pantheon | Project tracking exists outside the repo. | Notion is pilotage only; GitHub remains canonical. |

## Documented but not implemented

| Area | Current status | Meaning | Boundary |
|---|---|---|---|
| OpenWebUI integration | documented non-implemented / to verify | Doctrine describes OpenWebUI as exposure surface. | No claim of installed OpenWebUI extension from this repo. |
| Hermes integration | documented non-implemented / external | Doctrine describes Hermes as execution runtime. | Hermes execution remains outside Pantheon unless separately configured. |
| Hermes skills from Pantheon | documented non-implemented | Skill governance and templates may exist. | Pantheon does not install or run Hermes skills. |
| Architecture domain pack | candidate only / to verify | Architecture pack and method documents may frame professional method. | Domain pack does not advise, validate, execute, send or remember by itself. |
| Architecture vertical slice | documented non-implemented | A future `architecture_devis_reprise` proof loop is proposed. | No end-to-end slice is implemented by this status file. |
| Data platform | candidate only / to verify | Candidate orientation for records, evidence and approval boundaries. | Data platform must not become ERP, scheduler, queue, runtime, approval engine or memory engine. |
| Capability registry / skill lifecycle | candidate only / to verify | Candidate governance vocabulary may exist. | Capability declaration is not capability authorization. |
| Method Cards and Card Stack | candidate only / documented non-implemented | Candidate cockpit/method grammar may exist. | Cards are not agents, runtime state, approvals or memory. |
| Governed form filling | candidate only / to verify | Candidate method for field-as-claim form filling. | No PDF filler, connector, sender or form runtime is implemented by doctrine. |
| Revit Gate | candidate only / documented non-implemented | Developer dossier may describe a future local add-in boundary. | No Revit plugin is implemented by Pantheon unless separately shown in protected artifacts. |

## Voluntarily absent

These are not gaps to fill silently.

```text
Pantheon internal execution runtime
hidden agent loop
autonomous approval engine
automatic memory promotion engine
scheduler
queue
provider router
plugin marketplace
automatic external sender
unrestricted connector gateway
ERP
production data platform runtime
```

If any future proposal introduces one of these, it must be classified as a doctrine conflict or an explicitly external adapter/runtime.

## Protected-path status rule

The following paths require explicit approval before modification:

```text
schemas/
tests/
pyproject.toml
operations/
platform/
Docker files
.env files
CLAUDE.md
mcp-server/
GitHub Actions / CI scripts
```

A status mention in this file does not authorize modifying those paths.

## Read before merging branches

Before merging or closing significant branches, read this file with:

```text
docs/governance/STATUS.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/MODULES.md
docs/governance/REPOSITORY_CONSOLIDATION_LANDING_PLAN.md
```

A mergeable PR is not necessarily admissible.
A branch with useful content may still be superseded, overbroad, protected, contradictory or outside Pantheon.

## Next reconciliations

### MCP / dashboard / Pantheon Control

Decision needed:

```text
Is `mcp-server/` candidate-only, or an implementation artifact for read-only verification?
```

Recommended short-term target from the consolidation plan:

```text
Classify as read-only verification artifact if the code and tests confirm that it only returns status data and cannot approve, execute, send, schedule, route providers or promote memory.
```

Until reconciled, status remains:

```text
partial / to verify / protected review required
```

### Static prototype language

`docs/index.html` and Pantheon Control pages must not imply that target behavior is already a live product capability.

Required wording pattern:

```text
prototype / target behavior / documented non-implemented
```

## Final rule

```text
Documentation may describe.
Static pages may expose.
Read-only checks may verify structure or status.
External runtimes may execute under contract.
Pantheon governs consequential status.
The human decides.
```
