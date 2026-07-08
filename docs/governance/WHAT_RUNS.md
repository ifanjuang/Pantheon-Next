# What Runs

Status: active support / repository runtime-status map — to verify.

Date: 2026-07-08

This document states what currently runs, what is static documentation, what is partial or to verify, and what is intentionally absent.

It is a status-honesty map. It does not create runtime behavior, approve any tool, install an adapter, authorize external action, create a scheduler, create a queue, create an approval engine or promote memory.

Runtime boundary in this file is expressed as operational fields, not by repeating the doctrine slogan.

```text
exposed_by  -> display or publication surface
executed_by -> runtime or implementation artifact, when one exists
governed_by -> Pantheon boundary and status rule
approved_by -> human approval where consequential
forbidden   -> behavior that must not be inferred
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
implemented read-only / to verify
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
| `docs/assets/pantheon-control/` | static prototype / partial read-only mirror | Static Pantheon Control prototype assets and pages. PR #239 confirms at least the update verifier mirror can remain aligned with the Python read-only verifier. | Prototype display is not a live cockpit, approval engine, memory engine or runtime. |
| `schemas/` | partial / protected review required | Validation artifacts may exist. Exact status must be checked before relying on them. | Schemas validate structure; they do not execute or approve. |
| `tests/` | partial / protected review required | Validation tests exist where present. Exact coverage must be checked before relying on them. | Tests do not promote doctrine by themselves. |
| `mcp-server/` | implemented read-only / partial / protected path | Repository contains a bounded read-only MCP policy / verification surface. PR #239 was reviewed and merged as a protected-path read-only fix. The broader server remains partial/to verify until full-suite status is reconciled. | The surface may return status data only; it must not execute, approve, send, schedule, route providers, install, update or promote memory. |
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
| `revit-plugin/` | documented non-implemented / skeleton only | Future local Revit 2027 adapter prototype folder. | Current repo state is documentation and placeholder material only; future C#/.NET add-in remains to verify. |

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
docs/governance/README.md
docs/governance/STATUS.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/MODULES.md
README.md
CONTRIBUTING.md
```

A mergeable PR is not necessarily admissible.
A branch with useful content may still be superseded, overbroad, protected, contradictory or outside Pantheon.

## Next reconciliations

### MCP / dashboard / Pantheon Control

Current position after PR #239:

```text
mcp-server/ is no longer only a future candidate in repository terms.
It is an implemented read-only verification artifact, still partial / to verify as a whole.
```

Status implication:

```text
AUTHORITY_INDEX.md and MODULES.md should classify the MCP surface as a protected read-only implementation artifact / active support surface, not as a general runtime.
```

Boundary to keep:

```text
The MCP surface may validate structure/status and return status data.
It must not execute, approve, send, schedule, route providers, install, update or promote memory.
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
