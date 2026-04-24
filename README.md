# Pantheon Next

Pantheon Next is a modular multi-agent operating system for complex professional work.

It is designed for high-expertise environments such as architecture, project management, legal work, compliance, consulting, audit and IT.

Pantheon Next is not a chatbot. It is a controlled execution system where specialized agents, reusable skills, governed tools, structured memory and versioned workflows work together to produce reliable professional outputs.

## Core Idea

Pantheon Next turns AI from a free-form chat interface into a structured expert team.

The system is built around five principles:

1. agents are modular execution units
2. workflows define reasoning pipelines
3. skills encode reusable reasoning capabilities
4. tools are governed by policies
5. evaluation and feedback improve future workflow versions

OpenWebUI can be used as the user-facing interface, but it is not the runtime engine. Pantheon Next owns orchestration, state, policies, memory, evaluation and execution.

## Architecture Summary

Pantheon Next is organized into three main layers:

```text
core/        generic runtime, contracts, state, decision, execution, policies
modules/     agents, skills, tools, workflows, prompts, templates
platform/    API, UI, persistence, deployment, infrastructure
```

The core remains domain-agnostic. Business logic lives in modules.

## Main Concepts

### Agent

An agent is a specialized execution unit with a clear role, such as planning, extraction, validation, synthesis or communication.

Examples:

- ATHENA plans
- METIS deliberates
- PROMETHEUS challenges
- APOLLO validates
- ARGOS extracts facts
- IRIS writes final responses

### Skill

A skill is a reusable reasoning capability.

Examples:

- `research.crosscheck`
- `document.dossier_build`
- `critique.baloney_detection`
- `legal.citation_enforcer`

### Tool

A tool performs an external action.

Examples:

- PDF reading
- local search
- web search
- database query
- document export
- email draft

Tools are never executed freely. They pass through a policy gate.

### Workflow Pack

A Workflow Pack is the main product unit of Pantheon Next.

It contains:

- graph or steps
- agent configuration
- enabled tools
- enabled skills
- prompt references
- templates
- policies
- evaluation settings
- metrics

Workflow Packs are versioned, tested, compared, rolled back and promoted.

Statuses:

- `draft`
- `candidate`
- `active`
- `archived`

## Control Plane and Data Plane

Pantheon Next separates decision from execution.

### Control Plane

The control plane decides what should happen.

It includes:

- planning
- deliberation
- challenge
- validation
- routing
- clarification decisions

### Data Plane

The data plane executes what has been validated.

It includes:

- agent runtime
- tool execution
- skill injection
- artifact creation
- logs and scores

This separation makes the system easier to test, secure and improve.

## Target Stack

Initial stack:

- Python
- FastAPI
- PostgreSQL
- pgvector
- Docker Compose
- OpenWebUI as interface
- Ollama or OpenAI-compatible LLM provider

Later optional components:

- LangGraph for graph orchestration
- Redis / ARQ for async jobs
- MinIO for object storage
- Langfuse for observability
- DSPy for offline optimization

## Repository Structure

Planned structure:

```text
core/
  contracts/
  registry/
  decision/
  execution/
  state/
  policies/
  evaluation/
  learning/
  memory/
  documents/
  observability/

modules/
  agents/
  skills/
  tools/
  workflows/
  prompts/
  templates/

platform/
  api/
  ui/
  data/
  infra/

config/
tests/
```

## Documentation

- `ROADMAP.md` explains the full implementation path.
- `ARCHITECTURE.md` explains the system design.
- `AGENTS.md` explains the Pantheon agent map.

## First Milestone

The first working version should include:

1. core contracts
2. manifest loader
3. agent registry
4. workflow pack loader
5. one minimal workflow
6. one minimal agent
7. one FastAPI endpoint
8. one OpenWebUI-compatible chat route

## Product Thesis

Pantheon Next should become a modular, inspectable and controlled execution environment where:

- agents remain replaceable
- workflows remain versioned
- skills remain reusable
- tools remain governed
- memory remains structured
- evaluation drives improvement
- human validation controls risky changes

Final objective:

> Turn AI from a chatbot into a thinking team for complex professional work.
