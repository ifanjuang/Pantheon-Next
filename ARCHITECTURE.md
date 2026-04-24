#Pantheon OS — Architecture
## Overview
Pantheon Next is a modular multi-agent execution system built around a strict separation between:
- control plane
- data plane
The system is designed for complex professional work where reasoning, execution, validation, and memory must remain explicit, inspectable, and governed.
Pantheon Next is not a chatbot.
It is a controlled execution environment in which agents, skills, tools, workflows, policies, and memory cooperate as a structured expert system.
---
# High-Level Architecture
```text
User / External Channel
        ↓
OpenWebUI / API Adapters
        ↓
FastAPI API Layer
        ↓
Session Manager
        ↓
Manifest Loader / Registries
        ↓
Workflow Engine
        ↓
Decision Engine (Control Plane)
        ↓
Execution Engine (Data Plane)
        ↓
Agents / Skills / Tools
        ↓
Memory / Documents / Knowledge
        ↓
Artifacts / Outputs

⸻

Architectural Principles

1. Domain-agnostic core

The core/ layer must remain generic.

It provides:

* contracts
* registries
* state management
* workflow coordination
* decision engine
* execution engine
* policy enforcement
* evaluation
* learning
* observability
* memory abstractions
* document services

No business-specific logic should live in the core.

2. Filesystem-driven modularity

Pantheon loads runtime building blocks dynamically from the filesystem.

This applies to:

* agents
* skills
* tools
* workflows
* prompts
* templates

Each runtime block is defined by a manifest and validated at startup.

3. Domain overlays stay outside the core

Domain-specific behavior lives in domains/{domain}/.

An overlay may define:

* prompts
* skills
* workflows
* policies
* trusted sources
* templates
* evaluation cases
* domain-specific agents if needed

Examples:

* domains/architecture/
* domains/legal/
* domains/software/

⸻

Core Layers

1. Core

The core/ layer contains the runtime engine and generic system logic.

Responsibilities:

* contracts and interfaces
* registries and manifest loading
* state management
* workflow engine
* decision engine
* execution engine
* policy engine
* evaluation
* learning
* observability
* memory routing
* document intelligence services

The core must remain portable across domains.

2. Modules

The modules/ layer contains reusable runtime building blocks.

Components:

* agents
* skills
* tools
* workflows
* prompts
* templates

These are not necessarily domain-specific.
They are the reusable execution blocks of the system.

3. Domains

The domains/ layer contains business overlays.

This is where domain-specific business behavior lives.

Examples:

* architecture-specific decision skills
* legal citation policies
* software review workflows
* trusted source lists
* domain templates

4. Platform

The platform/ layer handles delivery and infrastructure.

Components:

* FastAPI services
* OpenWebUI integration
* persistence
* background jobs
* deployment
* streaming adapters
* admin console

⸻

Control Plane

The control plane is responsible for reasoning, planning, and governance before execution.

Main responsibilities:

* task classification
* decomposition
* deliberation
* contradiction detection
* uncertainty detection
* clarification decisions
* policy-aware routing
* escalation decisions
* final orchestration judgment

Main objects:

* DecisionContext
* DecisionAction
* DecisionPlan

Main agents involved:

* ATHENA
* METIS
* PROMETHEUS
* THEMIS
* APOLLO
* ZEUS
* HECATE
* HERMES (precheck and source strategy)

The control plane must decide what should happen before the data plane executes it.

⸻

Data Plane

The data plane executes validated decisions.

Main responsibilities:

* run agents
* inject tools and skills
* execute tasks
* manage sequential and parallel execution
* produce artifacts
* persist results
* log execution traces

Main objects:

* ExecutionState
* ExecutionResult

The data plane must never bypass the policy and governance layers.

⸻

Workflow Engine

The Workflow Engine coordinates the execution of a workflow pack.

A workflow is an explicit execution structure, not an implicit prompt chain.

Capabilities:

* solo
* parallel
* cascade
* arena
* conditional routing
* clarification checkpoints
* pause and resume
* merge and fork flows
* child workflows later

The Workflow Engine orchestrates both the control plane and the data plane.

Future extension:

* LangGraph adapter
* checkpoint-backed resume
* graph-based execution for complex workflows

⸻

Manifest Loader and Registries

Pantheon relies on manifests and registries as the runtime source of truth.

Responsibilities:

* discover agents, skills, tools, and workflows from disk
* validate manifests at startup
* register identities and metadata
* expose enabled/disabled state
* support version-aware loading later

Typical registry domains:

* AgentRegistry
* SkillRegistry
* ToolRegistry
* WorkflowRegistry

Manifests should eventually define:

* id
* role
* inputs
* outputs
* dependencies
* constraints
* policy
* enabled state

⸻

Governance Layer

Pantheon governs execution through explicit runtime controls.

Criticity

Criticity levels C1-C5 control:

* execution depth
* number of agents
* approval requirements
* veto activation
* clarification thresholds

Reversibility

Actions are classified by reversibility, for example:

* internal note
* memory write
* external communication
* critical or irreversible action

Draft-first

Serious outputs must follow:

* generate
* validate
* execute

Decision Debt

Pantheon tracks provisional or blocked decisions through explicit decision debt states.

Escalation

High-risk cases trigger escalation rather than silent continuation.

⸻

Policy Layer

All tool calls and side-effectful actions pass through a policy gate.

Policy decisions:

* allow
* block
* require_approval

The policy layer ensures:

* safety
* auditability
* compliance
* bounded execution

Risky actions must never be silently executed.

Examples:

* sending emails
* modifying persistent records
* external API actions with side effects
* destructive file operations
* irreversible workflow mutations

⸻

Veto Chain

Pantheon uses a structured veto chain.

A veto is not a raw boolean.
It is a structured decision containing:

* verdict
* justification
* severity
* lift condition

Typical flow:

execute_agents
→ veto_check
→ veto_themis
→ veto_zeus
→ zeus_judge

Veto levels:

* warning
* blocking

This allows the system to stop unsafe or procedurally invalid runs in a traceable way.

⸻

Memory System

Pantheon uses multiple memory layers.

1. Session Memory

Short-term runtime continuity.

Contents:

* current run context
* recent clarifications
* intermediate artifacts
* current workflow state

2. Project Memory

Project-specific continuity.

Contents:

* decisions
* constraints
* assumptions
* decision debt
* validated project history

Primary owner:

* HESTIA

3. Agency / Global Memory

Reusable long-term knowledge.

Contents:

* reusable patterns
* templates
* reference cases
* internal know-how
* validated cross-project lessons

Primary owner:

* MNEMOSYNE

4. Graph Memory (later)

Future structured relational memory.

Possible contents:

* entities
* relations
* contradictions
* dependency links

Memory must remain selective.
Not everything should be stored.

⸻

Post-Run Memory Routing

Pantheon should explicitly route results after synthesis.

Examples:

* validated project decision → project memory
* reusable pattern → agency/global memory proposal
* temporary context → session only
* noise → ignored

This keeps memory useful and avoids uncontrolled accumulation.

⸻

Knowledge Layer

The knowledge layer is distinct from runtime memory.

It may contain:

* prompts
* templates
* indexed markdown
* documentation
* examples
* trusted source corpora

This layer supports retrieval, not just continuity.

⸻

Document Intelligence Layer

This layer handles document processing and retrieval.

Responsibilities:

* ingestion
* parsing
* chunking
* indexing
* hybrid retrieval
* citation tracking
* synthesis cache
* multilingual support

Target metadata:

* file
* page
* section
* language
* source id

Later multimodal extension:

* images
* plans
* sections
* site photos
* visual descriptions
* technical qualification

⸻

Evaluation and Learning

Evaluation

Pantheon evaluates:

* structure
* confidence
* citation quality
* latency
* clarification count
* workflow quality
* supervision quality

Core mechanisms:

* scorecards
* regression tests
* workflow comparison
* Hera scoring
* Apollo validation

Learning

Pantheon improves through controlled learning.

Mechanisms:

* feedback collection
* gap analysis
* candidate workflow generation
* reusable pattern proposals
* controlled promotion

Learning must remain reviewed and explicit.
No silent self-mutation.

⸻

Observability

Pantheon tracks:

* agent execution
* tool calls
* prompts
* decisions
* workflow versions
* scores
* feedback
* blocked actions
* approvals
* vetoes

The system must remain inspectable in production.

⸻

External Interfaces

OpenWebUI is the main user-facing interface, not the runtime engine.

Other interfaces may be added later:

* Telegram
* WhatsApp
* voice input/output
* external API triggers

All external channels should route through the same governed runtime.

⸻

Design Constraints

* no business logic in core/
* no uncontrolled tool execution
* no hidden workflow mutation
* no silent risky actions
* no runtime dependency on the UI layer
* no collapse of agent / skill / tool / workflow roles
* no uncontrolled memory growth

⸻

Relationship to the Roadmap

This document describes the target structure and stable architectural principles.

Implementation sequencing is defined in ROADMAP.md.

In particular, the roadmap controls:

* MVP order
* orchestration phases
* context and memory upgrades
* policy and governance rollout
* evaluation and learning phases
* domain overlay delivery
* durable execution and scaling

⸻

Key Outcome

Pantheon Next becomes a controlled multi-agent system where reasoning, execution, validation, memory, and governance are explicit, modular, portable, and testable.