# Architecture

Status: active doctrine — migrated from Pantheon-OS snapshot at `legacy/Pantheon-OS-main.zip` (Pantheon-Next commit `9c2354b`).

Source: `Pantheon-OS/docs/governance/ARCHITECTURE.md` (509 lines, condensed under playbook rule D3=a).

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next is a governance-first declarative layer. It defines authority, contracts, evidence, approvals, allowed transitions, memory rules and integration boundaries that external runtimes must respect.

Pantheon Next must not reimplement subsystems that belong to Hermes Agent: agent loop, prompt assembly, provider resolution, tool registry, terminal, browser, web actions, MCP backends, session storage, scheduler, gateways, optional skills hub.

## Layered anatomy

```text
OpenWebUI
  user cockpit
  Knowledge surface
  approval surface
  Evidence Pack display

Pantheon Next
  governance source of truth
  Pantheon Roles
  skill governance and candidate skill declarations
  Task Contracts
  approval policy (C0-C5)
  Evidence policy
  Memory policy
  Knowledge taxonomy
  Hermes integration rules
  OpenWebUI integration rules
  External tools policy
  workflow and skill governance declarations

Hermes Agent
  operational runtime
  executable skills
  tools
  session execution
  provider runtime
  local operational memory
  candidate emission
```

Hermes is the runtime.

Pantheon Next is the definition, governance and domain-specialization layer.

OpenWebUI is the cockpit and Knowledge surface.

## Domain packages

Pantheon Next governs domain-specific scopes through declarative packages.

A domain package describes:

- domain identity and scope;
- governance rules and policies;
- knowledge policy and admissible sources;
- output formats and quality criteria;
- candidate skills and candidate workflows;
- templates.

A domain package is governance content. It is not runtime configuration. It does not register tools and does not start execution.

Domain registration, packaging conventions and concrete domain identifiers are defined per project and recorded in `MODULES.md`. Pantheon Next does not hard-code historical Pantheon-OS domain identifiers.

## Task Contracts

Reference: `TASK_CONTRACTS.md`.

A Task Contract frames a bounded task by declaring:

- task identity and purpose;
- domain;
- mode (read, draft, action, external);
- inputs and outputs;
- allowed and forbidden capabilities;
- approval ceiling;
- aligned Pantheon Roles and Hermes profiles;
- memory impact;
- evidence requirement.

A Task Contract frames execution. It does not authorize execution by itself. Authorization comes from the approval path and the evidence policy.

## Approval policy

Reference: `APPROVALS.md`.

```text
C0 — read or diagnostic
C1 — draft or suggestion
C2 — reversible low-risk action
C3 — persistent internal change
C4 — external, contractual, financial or responsibility action
C5 — critical, irreversible, secret-related or destructive
```

No persistent, external, critical or irreversible action without a visible approval path.

No self-approval by any Hermes profile.

## Evidence Pack

Reference: `EVIDENCE_PACK.md`.

A consequential output requires an Evidence Pack.

Minimum frame:

```text
files_read
sources_used
commands_run
tools_used
knowledge_bases_consulted
documents_used
assumptions
unsupported_claims
limitations
outputs
approval_required
next_safe_action
```

A model statement is not evidence.

## Skill strategy

Reference: `SKILL_LIFECYCLE.md`.

Before accepting a new skill governance declaration or Hermes Skill Candidate:

```text
1. search existing governance declarations and candidates;
2. check whether Hermes already provides the technical capability;
3. review external capabilities as inspiration only;
4. decide: use_existing, wrap_hermes_skill, create_candidate, reject_duplicate;
5. keep the declaration candidate until validation.
```

```text
Pantheon skill declaration = governance wrapper or capability expectation.
Hermes Skill                = executable runtime capability.
```

If Hermes already provides a technical capability, Pantheon Next must not recode it. Pantheon Next may declare a governance wrapper that defines context, inputs, outputs, approvals, privacy, memory impact and templates.

## Workflows

Reference: `WORKFLOW_SCHEMA.md`, `WORKFLOW_ADAPTATION.md`.

Workflows describe structured, reviewable procedures. A workflow is governance content, not a long prompt and not hidden orchestration.

Workflow files declare scope, allowed roles, allowed capabilities, approval ceilings, evidence requirements and adaptation rules. Execution of a workflow happens on the Hermes side, never inside Pantheon Next.

## Memory

Reference: `MEMORY.md`, `MEMORY_EVENT_SCHEMA.md`.

Conceptual memory layers:

```text
session     temporary
candidates  persisted but not validated
project     validated project context
system      validated reusable rules, methods and patterns
```

Promotion cycle:

```text
SESSION → CANDIDATES → Evidence Pack → validation → PROJECT or SYSTEM
```

Memory promotion is at least C3. No automatic promotion. Hermes operational memory is not Pantheon canonical memory.

## Knowledge taxonomy

Reference: `KNOWLEDGE_TAXONOMY.md`.

OpenWebUI Knowledge is not Pantheon canonical memory.

```text
Documents are knowledge.
Validated reusable facts become memory candidates.
Pantheon Next alone canonizes memory.
```

## Privacy by default

No real data from private conversations, real projects, clients, organizations, sites, addresses, persons or identifiable situations may be written into the repository.

Examples, tests and templates are fictional, neutral and non-traceable.

Every memory promotion checks anonymization.

## Change triage

Before any change, Pantheon Next classifies the request:

```text
situation
project_memory
system_memory
skill_update
workflow_update
new_capability
policy_update
code_patch
external_action
```

The classification determines the Task Contract, the approval ceiling, the relevant Pantheon Roles, the relevant Hermes profiles, the Evidence Pack requirement and the next safe action.

## Runtime boundary

Reference: `EXTERNAL_TOOLS_POLICY.md`, `HERMES_INTEGRATION.md`, `OPENWEBUI_INTEGRATION.md`.

Risky capabilities stay on the Hermes side and remain policy-gated by Pantheon Next:

- browser automation;
- terminal;
- web actions;
- MCP;
- file mutations;
- scheduler;
- gateways;
- memory providers;
- optional or community skills.

Governance rules applied to those capabilities:

- sandbox or containerized execution for risky tools;
- no privileged sockets at startup;
- no secret access without policy;
- no external action without approval;
- visible execution and traceable logs;
- candidate-only invocation until reviewed.

Pantheon Next does not implement any of these capabilities. It declares the rules.

## Integration context

Reference: `HERMES_INTEGRATION.md`, `OPENWEBUI_INTEGRATION.md`.

Pantheon Next exposes governance content through controlled documentation only. No runtime endpoint, no provider router, no execution API is introduced.

Hermes consumes Pantheon Next governance content as input for Task Contracts and operational decisions. Hermes returns candidates, never canonical doctrine.

OpenWebUI displays Pantheon Next governance content, approval requests and Evidence Packs. It does not canonize, does not promote memory and does not execute on behalf of Pantheon Next.

## Three-party operating protocol

```text
OpenWebUI    = user cockpit and approval surface
Hermes Agent = operational worker under Task Contract
Pantheon Next = governance source of truth
```

Operating rule:

```text
Hermes operates.
Pantheon Next arbitrates.
OpenWebUI pilots and displays.
```

Hermes may inspect, prepare, test, research, draft candidate skills, propose patches, create candidate assets and return evidence.

Hermes must not canonize.

Pantheon Next remains the authority for:

- skill and workflow governance declarations;
- project and system memory;
- doctrine, governance rules, validations, vetoes;
- criticality assessment;
- candidate promotion.

OpenWebUI remains cockpit and approval surface.

## Legacy audit

Reference: `CODE_AUDIT_POST_PIVOT.md`.

The historical Pantheon-OS repository contains FastAPI applications, registries, workflow loaders, installers, migrations and legacy tests. Pantheon Next does not import those by default.

Legacy components are audited and classified as `implemented`, `documented but not implemented`, `implemented but not documented`, `partial`, `obsolete`, `contradictory`, `to verify` or `non implemented` before any reuse.

No automatic deletion before diagnosis.

## Final rule

Pantheon Next must remain simpler than the runtime it governs.

If a capability already exists in Hermes, Pantheon Next governs it. It does not duplicate it.

## Doctrinal transformations applied during migration

- `Pantheon OS` renamed to `Pantheon Next` throughout.
- OS-specific domain identifiers (`architecture_fr`, `software`) removed from the canonical body; domain registration deferred to `MODULES.md`.
- OS legacy mentions (FastAPI apps, NAS/Portainer install, Docker tags, Hermes context export paths) condensed into generic doctrine and references; no concrete version, port, env var or command kept.
- OS sections 8 (skill XP and lifecycle implementation), 14 (runtime security execution detail), 15 (Hermes context exports), 17 (installation operations) condensed or replaced with references to Pantheon Next governance docs.
- Pantheon Next canonical positioning enforced: `OpenWebUI exposes. Hermes Agent executes. Pantheon Next governs.`
- HEPHAISTOS canonical spelling enforced. No occurrence of `HEPHAESTUS`.
- 509 source lines condensed to under 300 lines per playbook rule D3=a. No content split into multiple files.
- All references point to existing Pantheon Next stubs or active documents.

## Anti-runtime reminder

This document describes governance anatomy.

It does not introduce an execution runtime, a scheduler, a queue, a message bus, a provider router, an installer, an endpoint, a Docker stack, a schema, a test or operations tooling inside Pantheon Next.

OpenWebUI exposes.

Hermes Agent executes.

Pantheon Next governs.
