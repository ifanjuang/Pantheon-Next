# Governance Index

Status: active support doctrine — governance entry point and read paths — implemented as documentation.
Boundary profile: active_support_doctrine.

This directory contains Pantheon Next governance references.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```

Pantheon Next is governance-first. It is not an autonomous runtime.

## Status spine

Do not infer repository state from a diagram, candidate note, prototype or old log. Use the current status spine:

- `STATUS.md` — repository posture and unresolved clusters;
- `WHAT_RUNS.md` — what runs, is static, is partial, is external or is absent;
- `AUTHORITY_INDEX.md` — authority class and repository state;
- `MODULES.md` — ownership and boundary by governance area;
- `CONTRIBUTING.md` — change discipline and protected paths.

Supporting vocabularies:

- `STATUS_HEADER_RULES.md` — `Status:` header grammar;
- `BOUNDARY_PROFILES.md` — reusable non-runtime boundaries;
- `NON_EQUIVALENCE_RULES.md` — recurring distinctions such as installed != approved;
- `GLOSSARY.md` — canonical concepts and E/V/K/C axes.

```text
What state is this in?       -> STATUS.md
What actually runs?          -> WHAT_RUNS.md
What authority does it have? -> AUTHORITY_INDEX.md
Which area owns it?          -> MODULES.md
How may it be changed?       -> CONTRIBUTING.md
```

If files disagree:

```text
existence and placement -> registered authority index corpus
runtime availability    -> WHAT_RUNS.md, otherwise partial / to verify
repository posture      -> STATUS.md
concept vocabulary      -> GLOSSARY.md
```

## Short stable path

Read these before significant repository work:

1. `STATUS.md`
2. `WHAT_RUNS.md`
3. `AUTHORITY_INDEX.md`
4. `MODULES.md`
5. `CONTRIBUTING.md`
6. `GLOSSARY.md`
7. `NON_EQUIVALENCE_RULES.md`
8. `CAPABILITY_PLACEMENT.md`
9. `TASK_CONTRACTS.md`
10. `EVIDENCE_PACK.md`
11. `APPROVALS.md`
12. `MEMORY.md`

Then select the relevant task path below. Do not read the whole corpus by default.

## Task-based read paths

### Repository status or audit

```text
STATUS.md
-> WHAT_RUNS.md
-> AUTHORITY_INDEX.md
-> MODULES.md
-> CODE_AUDIT_POST_PIVOT.md when code or protected artifacts are involved
```

Use this path to determine whether a claim is implemented, partial, external, candidate, obsolete or voluntarily absent.

### Changing the repository

```text
CONTRIBUTING.md
-> STATUS_HEADER_RULES.md
-> BOUNDARY_PROFILES.md
-> NON_EQUIVALENCE_RULES.md
-> relevant owner document
```

Protected paths include schemas, tests, MCP code, CI, operations, platform, Docker, environment files and repository instructions. A useful prototype or green local run does not authorize a protected-path change.

### Capability, tool, skill, connector or external repository

```text
CAPABILITY_PLACEMENT.md
-> UNIFORM_CAPABILITY_GOVERNANCE.md
-> EXTERNAL_TOOLS_POLICY.md
-> ADAPTERS_AND_BINDINGS.md
-> MODEL_CAPABILITY_PASSPORT.md when model-specific
-> HERMES_INTEGRATION.md when Hermes executes
-> OPENWEBUI_INTEGRATION.md when OpenWebUI exposes
```

Classify concrete cases as a Capability Slot:

```text
abstract capability
-> candidate binding
-> installation status
-> health status
-> update status
-> activation status
-> Pantheon gates
-> human approval
```

Always state:

```text
exposed_by
executed_by
governed_by
approved_by
forbidden
```

### Governed professional work

```text
DOSSIER_SITUATION_INTAKE.md
-> TASK_CONTRACTS.md
-> CONTEXT_PACKS.md
-> WORKFLOW_FORGING_PROTOCOL.md when a workflow candidate is needed
-> HERMES_INTEGRATION.md for external execution
-> EVIDENCE_PACK.md
-> APPROVALS.md
-> USER_DECISION_GATE.md
```

Core sequence:

```text
clarify the situation
-> bind scope and consequences
-> prepare context
-> execute externally under contract
-> return candidates and evidence
-> verify status and gaps
-> human decision
```

A workflow may be forged or repeated externally. Its authority is never automatic.

### Context and cockpit UX

```text
CONTEXT_PACKS.md
-> CONTEXT_STACK.md
-> CARD_STACK_MODEL.md
-> DECISION_SURFACE_SPEC.md
-> OPENWEBUI_INTEGRATION.md
```

Ownership rule:

- `CONTEXT_PACKS.md` owns bounded context bundles;
- `CONTEXT_STACK.md` owns the candidate visible dynamic context stack;
- `CARD_STACK_MODEL.md` is the single current owner of Card, Scene, Deck, Constellation and navigation grammar;
- `DECISION_SURFACE_SPEC.md` specializes review display and capture;
- `OPENWEBUI_INTEGRATION.md` owns exposure boundaries.

Do not create a parallel State, View or Card model unless an observed consequence cannot be expressed by these owners.

### Knowledge, evidence, memory and the Registre Probatoire

```text
KNOWLEDGE_TAXONOMY.md
-> RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md
-> EVIDENCE_PACK.md
-> EVIDENCE_TOPOLOGY.md
-> MEMORY.md
```

Keep these distinctions:

```text
source != knowledge
knowledge != evidence
evidence != approval
runtime memory != Registre Probatoire
retrieval score != truth
runtime success != evidence
```

### Documents and reusable Knowledge

```text
MARKDOWN_DOSSIER_WORKFLOW.md
-> RAG_INGESTION_PIPELINE.md
-> DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md
-> relevant domain-pack document organization
-> PANTHEON_MVP_VERTICAL_BINDING.md for the observed external candidate
```

Pantheon defines and validates contracts. Parsing, persistence, synchronization, editing and retrieval execute in separately reviewed external bindings.

### Architecture domain

Start from the domain-pack index and then read only the relevant cluster:

```text
docs/domain-packs/architecture/
-> project understanding, proof register, document review or method cluster
-> corresponding schemas only when structural validation is material
```

Architecture material remains subject to professional review. A schema-valid or model-generated result is not professional validation.

### Roles, rites and methods

```text
AGENTS.md
-> GOVERNANCE_COLLEGE.md
-> ROLE_SIGNALS.md
-> METHOD_TAXONOMY.md
-> rites/README.md
-> USER_DECISION_GATE.md
```

```text
The method advances.
The role guards.
The quality expresses.
The reflex alerts.
The gate exposes.
The human decides.
```

Pantheon Roles and gods are governance viewpoints or qualities. They are not autonomous agents.

### External references and inspirations

```text
WATCHLIST.md or SKILL_WATCHLIST.md
-> REFERENCE_BOUNDARIES.md
-> reference review when needed
-> DISTILLATION_REGISTRY.md or REJECTED_PATTERNS.md
-> EXTERNAL_TOOLS_POLICY.md
```

```text
observe -> understand -> decide -> preserve
```

A watchlist item is not an installation instruction. Pattern distillation is allowed. Runtime migration is not.

### Product and public explanation

```text
PRODUCT_DIFFERENTIATION.md
-> EDITORIAL_LANGUAGE.md
-> NARRATIVE.md
-> VISUAL_LANGUAGE.md
-> docs/assets/README.md
```

Public and static assets must expose their own implementation status. A static cockpit mockup is not a live control plane.

## Ownership and anti-sprawl rule

Before creating a permanent document:

1. identify the existing owner document;
2. state the observed consequence the owner cannot express;
3. define the new document's authority class and repository state;
4. identify its promotion referent;
5. define its exit criterion: promote, merge, archive or refuse.

Default:

```text
extend the existing owner
before creating a parallel model
```

A roadmap, log, diagram or prototype does not become authority through repetition.

## Repository layer boundary

```text
Pantheon kernel
  tool-agnostic doctrine, contracts, status and read-only verification

External adapters
  Hermes execution, OpenWebUI plugins, ingestion, persistence, connectors,
  local professional tools and other runnable bindings

Professional storage
  client sources, licensed corpus, generated indexes, credentials and real data
```

A temporary in-repository adapter candidate must be labeled honestly and moved out when it becomes a runnable product component, unless an explicit human decision establishes a bounded exception.

## Boundary rule

No governance document may introduce an autonomous execution runtime, hidden scheduler, message/job/agent queue, provider router, automatic memory promotion, hidden workflow execution, automatic skill installation, agent self-approval or swarm controller.

External references may inform vocabulary, contracts, evidence expectations, gates and candidate constraints. They do not authorize dependency adoption, installation, activation, provider routing, external action or memory promotion.

```text
Pantheon defines the contract and consequential status.
External tools carry the work.
The human decides.
```
