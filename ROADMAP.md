# Pantheon Next — Roadmap

## Vision

Pantheon Next is a modular multi-agent operating system for complex professional work.

It is designed for high-expertise environments such as architecture, project management, legal work, compliance, consulting, audit and IT.

The goal is not to build a chatbot.

Pantheon Next is a controlled execution system where:

- agents are modular execution units
- workflows define reasoning pipelines
- skills encode reusable reasoning capabilities
- tools execute external actions
- policies govern risk
- evaluation measures quality
- feedback and learning improve workflow versions over time

The system must behave like a structured expert team, not like a free-form prompt interface.

---

# 1. Core Design Principles

## 1.1 Modularity First

Everything must be modular and replaceable:

- agents
- skills
- tools
- workflows
- prompts
- policies
- memory adapters
- evaluators
- UI panels

No business logic should live in the core runtime.

The core provides contracts, execution, routing, state, registries, policy enforcement and observability.

Business behavior lives in modules.

---

## 1.2 Runtime Over Prompts

Pantheon Next should not rely on long prompt chains alone.

Prompts describe behavior. The runtime controls execution.

Workflows define what happens. Policies define what is allowed. Evaluators define what is good enough.

---

## 1.3 Workflow Pack as the Main Product Unit

A workflow is not only a list of steps.

A Workflow Pack is a complete versioned execution configuration.

It contains:

- graph or steps
- agent configuration
- enabled tools
- enabled skills
- prompt references
- templates
- policies
- evaluation settings
- learning settings
- metrics

Workflow Packs are versioned, tested, compared, rolled back and promoted.

Statuses:

- draft
- candidate
- active
- archived

---

## 1.4 Control Plane / Data Plane

Pantheon Next separates decision from execution.

Control Plane:

- decides what should happen
- plans
- deliberates
- challenges
- validates
- routes

Data Plane:

- executes validated actions
- calls agents
- injects tools and skills
- writes artifacts
- returns results

This avoids agents mixing reasoning, tool execution and final response generation in one uncontrolled flow.

---

## 1.5 Human Control for Risky Actions

Risky actions must never be silently executed.

Examples:

- sending emails
- deleting files
- writing to a database
- executing Python
- calling external APIs with side effects
- modifying user data

Policy decisions:

- allow
- block
- require_approval

---

## 1.6 OpenWebUI is the Interface, Not the Engine

OpenWebUI should remain the user-facing chat layer.

The intelligence, routing, workflow execution, policies and evaluation live in Pantheon Next.

---

# 2. Target Architecture

```text
platform/
  api/              FastAPI apps
  ui/               OpenWebUI integration + admin console
  data/             persistence and runtime state
  infra/            Docker, deployment, scripts

core/
  contracts/        base types and interfaces
  registry/         agent, tool, skill, workflow registries
  decision/         control plane
  execution/        data plane
  state/            session and run state
  policies/         policy engine and action gate
  evaluation/       scorecards and tests
  learning/         workflow improvement loop
  observability/    traces, logs, runs
  memory/           vector, graph, markdown adapters
  documents/        document intelligence services
  packaging/        context and artifact bundles

modules/
  agents/           modular agents
  skills/           reusable reasoning skills
  tools/            external actions and connectors
  workflows/        workflow packs
  prompts/          prompt libraries
  templates/        document and output templates
```

---

# 3. Agent Pantheon

## 3.1 Meta / Control Agents

### ZEUS
Role: orchestration and arbitration.

Responsibilities:

- supervise global run strategy
- arbitrate between conflicting agent outputs
- decide when replanning is needed
- enforce final coordination

Limits:

- should not perform domain work directly
- should not become a god-object

---

### ATHENA
Role: planning and decomposition.

Responsibilities:

- classify the task
- decompose into subtasks
- propose initial execution plan
- select relevant workflows or workflow candidates

Limits:

- should not execute tools
- should not write final answers

---

### METIS
Role: structured deliberation.

Responsibilities:

- frame the real problem
- list hypotheses
- identify uncertainty
- identify conflicts
- recommend checks before synthesis

Limits:

- must not invent facts
- must not produce the final answer

Inspiration:

- `beomwookang/deliberate`

---

### PROMETHEUS
Role: challenge, contradiction and adversarial review.

Responsibilities:

- detect contradictions
- challenge weak reasoning
- identify unsupported claims
- prevent false consensus
- preserve divergent positions

Limits:

- can become too skeptical if not calibrated

Inspirations:

- `jrcruciani/baloney-detection-kit`

---

### THEMIS
Role: procedural legitimacy and policy coherence.

Responsibilities:

- verify required steps
- enforce process rules
- check policies before execution
- block non-compliant workflows

Limits:

- does not judge factual truth
- does not produce content

---

### APOLLO
Role: validation and confidence scoring.

Responsibilities:

- score confidence
- validate source traceability
- check final answer consistency
- accept, warn or block output

Limits:

- depends on quality of upstream evidence

---

### HECATE
Role: uncertainty and missing-information detection.

Responsibilities:

- detect missing context
- calculate uncertainty score
- decide whether user clarification is needed
- prevent unsafe answers when information is insufficient

Limits:

- does not write final answers
- should produce structured clarification needs only

---

## 3.2 Research and Analysis Agents

### HERMES
Role: research routing.

Responsibilities:

- choose where to search
- route between local, web, database, markdown and graph sources
- prepare source strategy

---

### DEMETER
Role: data fetching and normalization.

Responsibilities:

- fetch documents
- normalize files
- preserve metadata
- prepare corpus for extraction

---

### ARGOS
Role: objective extraction.

Responsibilities:

- extract facts
- extract citations
- extract entities
- extract relations
- avoid interpretation

---

### ARTEMIS
Role: relevance filtering.

Responsibilities:

- remove noise
- keep relevant evidence
- focus agent context

---

## 3.3 Memory Agents

### HESTIA
Role: session memory.

Responsibilities:

- maintain short-term context
- keep current run state
- store user clarifications

---

### MNEMOSYNE
Role: knowledge library.

Responsibilities:

- manage templates
- manage reference cases
- manage skill documentation
- manage reusable patterns

---

### HADES
Role: deep memory.

Responsibilities:

- vector retrieval
- archive search
- long-term project memory

---

## 3.4 Output Agents

### KAIROS
Role: contextual synthesis.

Responsibilities:

- select essential information
- structure the response
- adapt level of detail to context

---

### DAEDALUS
Role: document building.

Responsibilities:

- assemble reports, briefs and dossiers
- structure sections
- include appendices and references

---

### IRIS
Role: communication and tone.

Responsibilities:

- adapt tone
- formulate clarification questions
- rewrite output for audience
- keep language clear and measured

---

### HEPHAESTUS
Role: diagrams and technical artifacts.

Responsibilities:

- generate diagrams
- create Mermaid graphs
- add legends and structured visual explanations

---

### APHRODITE
Role: presentation polish.

Responsibilities:

- improve appeal and emotional impact
- polish marketing or public-facing output

Limits:

- should not be used for strict legal or technical validation

---

## 3.5 System Agents

### ARES
Role: fast execution fallback.

Responsibilities:

- handle simple or urgent tasks
- provide degraded fast mode

---

### POSEIDON
Role: load and flow control.

Responsibilities:

- manage parallelism
- monitor execution load
- control unstable execution cascades

---

# 4. Phase 1 — Core Runtime Contracts

## Goal

Create a strict and reusable foundation.

## Tasks

- Create `AgentBase`.
- Create `SkillBase`.
- Create `ToolBase`.
- Create `WorkflowBase`.
- Create `AgentResult`.
- Create `Artifact`.
- Create `SessionState`.
- Create `RunState`.
- Create lifecycle hooks:
  - `before_run`
  - `run`
  - `after_run`
  - `on_error`
- Add strict manifest validation.

## Suggested Files

```text
core/contracts/agent.py
core/contracts/skill.py
core/contracts/tool.py
core/contracts/workflow.py
core/contracts/artifact.py
core/state/session.py
core/state/run.py
core/registry/manifest_loader.py
```

## Inspirations to Review

- `OpenHands/software-agent-sdk`
- `pydantic/pydantic-ai`
- `instructor-ai/instructor`
- `guardrails-ai/guardrails`

## Success Criteria

- Agents, tools, skills and workflows share strict contracts.
- Modules can be discovered through manifests.
- Invalid manifests fail at startup.

---

# 5. Phase 2 — Workflow Pack Versioning

## Goal

Make workflows reproducible, comparable and deployable.

## Tasks

- Create `WorkflowVersion`.
- Create `WorkflowRegistry`.
- Add workflow pack YAML loading.
- Add version statuses.
- Add diff between versions.
- Add rollback.
- Add fork from existing version.
- Add candidate promotion.

## Suggested Files

```text
core/workflows/version.py
core/workflows/registry.py
core/workflows/loader.py
core/workflows/diff.py
modules/workflows/example.workflow.yaml
platform/api/apps/workflows/router.py
```

## Inspirations to Review

- `JustVugg/distillery`
- `micpet7514088/skills-manager`

## Success Criteria

- A workflow version can be loaded from YAML.
- A candidate workflow can be compared with an active workflow.
- A previous version can be restored.

---

# 6. Phase 3 — Decision Engine

## Goal

Separate reasoning from execution.

## Tasks

- Create `DecisionContext`.
- Create `DecisionAction`.
- Create `DecisionPlan`.
- Create `DecisionEngine`.
- Support routes:
  - `CONTINUE`
  - `WAIT_FOR_USER`
  - `MERGE`
  - `FORK`
  - `CHILD_FORK`
- Integrate ATHENA, METIS, PROMETHEUS, THEMIS and APOLLO.

## Suggested Files

```text
core/decision/context.py
core/decision/action.py
core/decision/plan.py
core/decision/engine.py
core/decision/router.py
core/decision/validator.py
```

## Inspirations to Review

- `salesforce-misc/switchplane`
- `beomwookang/deliberate`
- Anthropic multi-agent research system

## Success Criteria

- Pantheon can produce a decision plan without executing tools.
- Decision plans can be tested independently.
- Missing information can trigger `WAIT_FOR_USER`.

---

# 7. Phase 4 — Execution Engine

## Goal

Execute validated decision plans safely.

## Tasks

- Create `ExecutionState`.
- Create `ExecutionResult`.
- Create `ExecutionEngine`.
- Support sequential actions.
- Support parallel action groups.
- Support blocked actions.
- Support approval-needed actions.
- Inject tools, skills and configs into agent runtime.
- Persist artifacts and scores.

## Suggested Files

```text
core/execution/state.py
core/execution/result.py
core/execution/engine.py
core/runtime/agent_runtime.py
core/runtime/workspace.py
```

## Inspirations to Review

- `OpenHands/software-agent-sdk`
- `langchain-ai/langgraph`

## Success Criteria

- A `DecisionPlan` can be executed.
- Parallel groups can run safely.
- Execution generates artifacts, scores and logs.

---

# 8. Phase 5 — LangGraph Adapter

## Goal

Enable graph-based dynamic orchestration.

## Tasks

- Create `GraphState`.
- Wrap agents as LangGraph nodes.
- Add conditional edges.
- Add `WAIT_FOR_USER` node.
- Add partial replan support.
- Add child workflows.

## Suggested Files

```text
core/graph/state.py
core/graph/adapter.py
core/graph/nodes.py
core/graph/routes.py
```

## Inspiration

- `langchain-ai/langgraph`

## Success Criteria

- Complex workflows can be represented as graphs.
- User clarification can pause and resume a workflow.
- Same-topic messages can be merged into running workflows.

---

# 9. Phase 6 — Policy Gate and Runtime Security

## Goal

Prevent uncontrolled tool execution.

## Tasks

- Create `PolicyEngine`.
- Create `ActionGate`.
- Add decisions:
  - `allow`
  - `block`
  - `require_approval`
- Log every tool call.
- Add approval API.
- Keep secrets hidden from agents.

## Suggested Files

```text
core/policies/engine.py
core/policies/rules.py
core/policies/action_gate.py
platform/api/apps/approvals/router.py
```

## Inspiration

- `wiserautomation/SupraWall`

## Success Criteria

- Risky actions are blocked or paused.
- Tool calls are auditable.
- Sensitive credentials are never exposed to agents.

---

# 10. Phase 7 — Evaluation and Scorecards

## Goal

Measure quality before learning.

## Tasks

- Create `EvaluationRunner`.
- Create scorecards.
- Add regression test cases.
- Add workflow comparison.
- Track metrics:
  - confidence
  - structure
  - latency
  - clarification count
  - citation quality
  - user feedback

## Suggested Files

```text
core/evaluation/runner.py
core/evaluation/scorecard.py
core/evaluation/metrics.py
tests/evals/
```

## Inspirations to Review

- `langchain-ai/openevals`
- `promptfoo/promptfoo`
- `langfuse/langfuse`

## Success Criteria

- Workflow versions can be benchmarked.
- A candidate version cannot be promoted without evaluation.

---

# 11. Phase 8 — Deliberation and Anti-Bullshit

## Goal

Reduce hallucination, weak reasoning and fake confidence.

## Tasks

- Implement METIS as deliberation agent.
- Add deliberation artifacts:
  - hypotheses
  - uncertainties
  - conflicts
  - missing checks
- Add `critique.baloney_detection` skill.
- Add `bullshit_risk_score`.
- Integrate score into APOLLO validation.

## Suggested Files

```text
modules/agents/meta/metis_deliberator/
modules/skills/critique/baloney_detection/
```

## Inspirations to Review

- `beomwookang/deliberate`
- `jrcruciani/baloney-detection-kit`

## Success Criteria

- Final outputs can be rejected for weak claims or unsupported authority.
- Overconfident language is detected.

---

# 12. Phase 9 — Feedback and Learning Engine

## Goal

Improve workflow versions through controlled learning.

## Tasks

- Create `FeedbackEvent`.
- Add discreet feedback:
  - positive
  - negative
  - reason tags
- Track implicit signals:
  - copy
  - export
  - continue
  - rewrite
- Create `LearningEngine`.
- Create `GapAnalyzer`.
- Generate candidate workflow versions.
- Require human approval before activation.

## Suggested Files

```text
core/learning/feedback.py
core/learning/engine.py
core/learning/gap_analyzer.py
platform/api/apps/feedback/router.py
platform/api/apps/learning/router.py
```

## Inspirations to Review

- `NousResearch/hermes-agent-self-evolution`
- `stanfordnlp/dspy`
- `micpet7514088/autogap`

## Success Criteria

- Negative feedback can generate improvement suggestions.
- The system proposes candidate workflow versions, not silent mutations.

---

# 13. Phase 10 — Structured Skills Library

## Goal

Move repeated reasoning behaviors into reusable skills.

## Tasks

- Create `SkillRegistry`.
- Add skill manifests.
- Add skill versions.
- Add skill tests.
- Add YAML skill definitions.
- Build initial skills:
  - `research.crosscheck`
  - `document.dossier_build`
  - `communication.professional_rewrite`
  - `critique.baloney_detection`
  - `legal.citation_enforcer`

## Suggested Files

```text
core/registry/skill_registry.py
modules/skills/research/crosscheck/
modules/skills/document/dossier_build/
modules/skills/communication/professional_rewrite/
modules/skills/critique/baloney_detection/
modules/skills/legal/citation_enforcer/
```

## Inspirations to Review

- `JustVugg/distillery`
- `micpet7514088/skills-manager`
- `microsoft/semantic-kernel`

## Success Criteria

- Skills are reusable across workflows.
- Skills can be tested independently.

---

# 14. Phase 11 — Document Intelligence Layer

## Goal

Build a document-first intelligence layer.

## Tasks

- Create `DocumentIngestionService`.
- Create `DocumentIndexService`.
- Create `DocumentRetrievalService`.
- Create `DocumentCitationService`.
- Preserve metadata:
  - file
  - page
  - section
  - language
  - source id
- Support multilingual documents.

## Suggested Files

```text
core/documents/ingestion.py
core/documents/indexing.py
core/documents/retrieval.py
core/documents/citations.py
modules/tools/documents/pdf_reader/
modules/tools/documents/docx_reader/
```

## Inspirations to Review

- `sahilalaknur21/SmartDocs-Multillingual-Agentic-Rag`
- `deepset-ai/haystack`
- `run-llama/llama_index`

## Success Criteria

- Retrieved chunks preserve source, page and section metadata.
- Documents can be cited reliably.

---

# 15. Phase 12 — Markdown Knowledge Layer

## Goal

Use Markdown as structured internal knowledge.

## Tasks

- Create `MarkdownIndexLayer`.
- Index headings, sections and anchors.
- Use it for prompts, skills docs and playbooks.
- Connect to MNEMOSYNE.

## Suggested Files

```text
core/knowledge/markdown_index.py
modules/tools/markdown/md_index/
knowledge/
```

## Inspiration

- `Fusion/mdidx`

## Success Criteria

- Markdown files can be searched by heading path and section.
- Internal docs become retrievable knowledge.

---

# 16. Phase 13 — Graph Memory

## Goal

Add structured relational memory.

## Tasks

- Create `GraphMemory`.
- Extract entities.
- Extract relations.
- Track contradictions.
- Support hybrid vector + graph retrieval.
- Connect to METIS, PROMETHEUS and APOLLO.

## Suggested Files

```text
core/memory/graph_memory.py
modules/tools/graph/
```

## Inspirations to Review

- `ADVASYS/ragraph`
- Neo4j patterns
- Memgraph patterns

## Success Criteria

- The system can reason over relations, not only similar chunks.

---

# 17. Phase 14 — Context and Artifact Packaging

## Goal

Improve context handoff between agents and workflows.

## Tasks

- Create `ContextPackager`.
- Create `ArtifactPackager`.
- Create `WorkflowBundle`.
- Support replay and export.

## Suggested Files

```text
core/packaging/context.py
core/packaging/artifacts.py
core/packaging/workflow_bundle.py
```

## Inspiration

- `awizemann/scarf`

## Success Criteria

- Each agent receives only the relevant context.
- Workflows can be replayed from bundled artifacts.

---

# 18. Phase 15 — Observability and Admin Console

## Goal

Make Pantheon inspectable.

## Tasks

- Trace prompts.
- Trace decisions.
- Trace tool calls.
- Track workflow version per run.
- Track scores and feedback.
- Show blocked actions.
- Add workflow comparison UI.

## Suggested Files

```text
core/observability/logs.py
core/observability/traces.py
platform/api/apps/runs/router.py
platform/ui/admin/
```

## Inspirations to Review

- `langfuse/langfuse`
- `wandb/wandb`
- `dagster-io/dagster`

## Success Criteria

- A user can inspect why a workflow produced a result.
- A developer can compare two workflow versions.

---

# 19. Phase 16 — Durable Execution and Scaling

## Goal

Prepare for longer and heavier workflows.

## Tasks

- Add checkpoints.
- Add retries.
- Add job queue if needed.
- Add replay runner.
- Consider durable workflow orchestration later.

## Suggested Files

```text
core/checkpoints/store.py
core/jobs/queue.py
core/replay/runner.py
```

## Inspirations to Review

- `temporalio/temporal`
- Redis / ARQ patterns

## Success Criteria

- Failed workflows can resume.
- Long workflows do not lose state.

---

# 20. Initial Repository Setup

## Minimum Files to Create First

```text
README.md
ROADMAP.md
pyproject.toml
.env.example
docker-compose.yml

core/
modules/
platform/
tests/
config/
```

## First Milestone

Implement:

1. core contracts
2. manifest loader
3. basic agent registry
4. basic workflow registry
5. one minimal workflow pack
6. one minimal agent
7. one API endpoint

---

# 21. Implementation Order

## Build First

1. Runtime contracts
2. Manifest loader
3. Agent registry
4. Workflow pack loader
5. Workflow registry
6. Decision engine
7. Execution engine
8. Policy gate
9. Evaluation runner

## Build Second

10. METIS deliberation
11. Anti-bullshit skill
12. Feedback events
13. Learning engine
14. Skill registry
15. Document intelligence layer

## Build Third

16. LangGraph adapter
17. Markdown index
18. Graph memory
19. Observability UI
20. Durable execution

---

# 22. Non-Goals for the First Version

- Do not version every agent independently in the UI.
- Do not allow uncontrolled workflow mutation.
- Do not let agents call tools directly without a policy gate.
- Do not put business logic inside `core/`.
- Do not make OpenWebUI the runtime engine.
- Do not over-engineer distributed execution before the runtime is stable.
- Do not add graph memory before basic document retrieval works.

---

# 23. Inspiration Index

## Core Orchestration

- `langchain-ai/langgraph`
- Anthropic multi-agent research system
- `salesforce-misc/switchplane`

## Agent Runtime

- `OpenHands/software-agent-sdk`
- `pydantic/pydantic-ai`
- `instructor-ai/instructor`
- `guardrails-ai/guardrails`

## Security

- `wiserautomation/SupraWall`

## Evaluation

- `langchain-ai/openevals`
- `promptfoo/promptfoo`
- `langfuse/langfuse`

## Deliberation and Critique

- `beomwookang/deliberate`
- `jrcruciani/baloney-detection-kit`

## Learning

- `stanfordnlp/dspy`
- `NousResearch/hermes-agent-self-evolution`
- `micpet7514088/autogap`

## Skills

- `JustVugg/distillery`
- `micpet7514088/skills-manager`
- `microsoft/semantic-kernel`

## Documents and Knowledge

- `sahilalaknur21/SmartDocs-Multillingual-Agentic-Rag`
- `deepset-ai/haystack`
- `run-llama/llama_index`
- `Fusion/mdidx`
- `ADVASYS/ragraph`

## Packaging and Handoff

- `awizemann/scarf`

## Scaling and Observability

- `wandb/wandb`
- `dagster-io/dagster`
- `temporalio/temporal`

---

# Final Target

Pantheon Next should become a modular, inspectable and controlled execution environment where:

- agents remain replaceable
- workflows remain versioned
- skills remain reusable
- tools remain governed
- memory remains structured
- evaluation drives improvement
- human validation controls risky changes

Final product thesis:

> Turn AI from a chatbot into a thinking team for complex professional work.
