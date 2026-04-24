# Pantheon Next — Architecture

## Overview

Pantheon Next is a modular multi-agent system built around a strict separation between:

- control plane (decision)
- data plane (execution)

The system is designed to remain scalable, testable and maintainable while supporting complex workflows involving multiple agents, tools, skills and data sources.

---

# High-Level Architecture

```text
User (OpenWebUI)
        ↓
API (FastAPI)
        ↓
Session Manager
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
```

---

# Core Layers

## 1. Core

The `core/` layer contains the runtime engine and system logic.

Responsibilities:

- contracts and interfaces
- registries
- state management
- decision engine
- execution engine
- policy enforcement
- evaluation
- learning
- observability
- memory abstraction

The core must remain domain-agnostic.

---

## 2. Modules

The `modules/` layer contains all business logic.

Components:

- agents
- skills
- tools
- workflows
- prompts
- templates

Modules are loaded dynamically through manifests.

---

## 3. Platform

The `platform/` layer handles delivery and infrastructure.

Components:

- FastAPI services
- OpenWebUI integration
- persistence
- background jobs
- deployment

---

# Control Plane

The control plane is responsible for reasoning and planning.

Main responsibilities:

- task classification
- decomposition
- deliberation
- contradiction detection
- policy validation
- routing decisions
- clarification decisions

Main objects:

- DecisionContext
- DecisionAction
- DecisionPlan

Main agents involved:

- ATHENA
- METIS
- PROMETHEUS
- THEMIS
- APOLLO
- ZEUS

---

# Data Plane

The data plane executes validated decisions.

Main responsibilities:

- run agents
- inject tools and skills
- execute actions
- manage parallel tasks
- generate artifacts
- log execution

Main objects:

- ExecutionState
- ExecutionResult

---

# Workflow Engine

The Workflow Engine coordinates the execution of a workflow pack.

Capabilities:

- sequential execution
- parallel execution
- conditional routing
- pause and resume
- user clarification
- merge and fork flows

Future extension:

- LangGraph adapter

---

# Policy Layer

All tool calls pass through a policy gate.

Decisions:

- allow
- block
- require_approval

The policy layer ensures:

- safety
- auditability
- compliance

---

# Memory System

Pantheon Next uses multiple memory layers:

## Short-Term Memory

- session context
- recent messages
- intermediate artifacts

## Knowledge Memory

- templates
- prompts
- documentation
- examples

## Long-Term Memory

- vector store
- document archive
- project history

## Graph Memory (later)

- entities
- relations
- contradictions

---

# Document Intelligence Layer

This layer handles document processing.

Responsibilities:

- ingestion
- parsing
- chunking
- indexing
- retrieval
- citation tracking

---

# Evaluation and Learning

## Evaluation

- scorecards
- regression tests
- workflow comparison

## Learning

- feedback collection
- gap analysis
- candidate workflow generation
- controlled promotion

---

# Observability

Pantheon Next tracks:

- agent execution
- tool calls
- prompts
- decisions
- workflow versions
- evaluation scores

---

# Design Constraints

- no business logic in core
- no uncontrolled tool execution
- no hidden reasoning steps
- no silent workflow mutation
- no dependency on UI layer for logic

---

# Evolution Path

Phase 1:

- contracts
- workflow packs
- decision + execution engine

Phase 2:

- policy gate
- evaluation
- deliberation

Phase 3:

- learning
- skills
- document intelligence

Phase 4:

- graph workflows
- graph memory
- observability UI

Phase 5:

- scaling
- distributed execution

---

# Key Outcome

Pantheon Next becomes a controlled multi-agent system where reasoning, execution and validation are explicit, modular and testable.
