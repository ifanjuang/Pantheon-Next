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

### HERA
Role: post-synthesis supervision and run scoring.

Responsibilities:

- score orchestration quality
- evaluate coherence after synthesis
- produce an aligned / misaligned / degraded verdict
- explain supervision feedback

Limits:

- does not replace APOLLO validation
- does not perform end-user evaluation

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
Role: research routing and preprocessing.

Responsibilities:

- choose where to search
- route between local, web, database, markdown and graph sources
- prepare source strategy
- run the precheck gate before ZEUS plans

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
- never auto-activated

---

## 3.5 System Agents

### ARES
Role: fast execution fallback and security guard.

Responsibilities:

- handle simple or urgent tasks
- provide degraded fast mode
- provide veto authority from medium criticality upward

---

### POSEIDON
Role: load and flow control.

Responsibilities:

- manage parallelism
- monitor execution load
- control unstable execution cascades

---

# 4. Phase 0 — Infrastructure

## Goal

Create the platform foundation before the agent runtime.

## Tasks

- Create FastAPI application skeleton with lifespan.
- Add PostgreSQL + pgvector + async SQLAlchemy.
- Add MinIO / S3 object storage interface.
- Add JWT authentication.
- Add RBAC roles:
  - admin
  - operator
  - reader
- Add SSE streaming endpoints.
- Add WebSocket streaming endpoints.
- Add environment and secret management:
  - `.env`
  - vault-ready structure
- Add Docker Compose:
  - API
  - PostgreSQL
  - Redis
  - MinIO
  - Ollama
- Add health checks.
- Add graceful shutdown.
- Add multi-tenancy model.
- Add row-level isolation per organization.
- Add SSE event naming convention:
  - all agent events follow `{agent}.{event}`
  - examples:
    - `hermes.preprocess_ready`
    - `zeus.plans_ready`
    - `zeus.decision`
    - `agent.subtask_done`
    - `themis.veto_detected`
    - `hera.run_score`
    - `kairos.final_answer`
  - system events:
    - `run_created`
    - `phase_start`
    - `done`
    - `error`
- Add Alembic migration strategy:
  - sequential numbered migrations: `0001`, `0002`, ...
  - schema evolution is a runtime contract
  - every model change requires a migration

## Suggested Files

```text
platform/api/main.py
platform/api/lifespan.py
platform/api/auth/
platform/api/streaming/
platform/data/models/
platform/data/migrations/
platform/infra/docker-compose.yml
.env.example
```

## Inspirations to Review

- `tiangolo/fastapi`
- `pgvector/pgvector-python`
- `sqlalchemy/sqlalchemy`

## Success Criteria

- API starts with health checks.
- Database migrations run from scratch.
- Streaming endpoint emits named events.
- Multi-tenant organization isolation is defined.

---

# 5. Phase 1 — Runtime Contracts

## Goal

Create a strict and reusable foundation.

## Tasks

- Create `AgentBase`.
- Create `SkillBase`.
- Create `ToolBase`.
- Create `WorkflowBase`.
- Create `MemoryAdapter`.
- Create `AgentResult`.
- Create `Artifact`.
- Create `SessionState`.
- Create `RunState`.
- Create `OrchestraState`.
- Create lifecycle hooks:
  - `before_run`
  - `run`
  - `after_run`
  - `on_error`
- Add strict manifest validation.
- Add `AgentRegistry` as source of truth for all agent identities:
  - name
  - role
  - layer
  - class path
  - triggers
  - veto authority
- Add memory isolation scopes:
  - session: TTL Redis
  - project: affaire lifetime
  - agency: permanent
- Add agent versioning:
  - `SOUL.md` changes are tracked
  - config changes are tracked
  - rollback is supported
- Add domain overlay injection mechanism:
  - `domains/{domain}/prompts/context.yaml`
  - injected into all agent system prompts at runtime
  - active domain set via `DOMAIN=architecture`
  - overlays carry:
    - trusted_sources
    - criticality_keywords
    - veto_patterns

## Suggested Files

```text
core/contracts/agent.py
core/contracts/skill.py
core/contracts/tool.py
core/contracts/workflow.py
core/contracts/artifact.py
core/contracts/memory.py
core/state/session.py
core/state/run.py
core/state/orchestra.py
core/registry/agent_registry.py
core/registry/manifest_loader.py
config/agent_registry.yaml
config/domains/architecture/prompts/context.yaml
```

## Inspirations to Review

- `All-Hands-AI/OpenHands`
- `pydantic/pydantic-ai`
- `instructor-ai/instructor`
- `guardrails-ai/guardrails`

## Success Criteria

- Agents, tools, skills and workflows share strict contracts.
- Modules can be discovered through manifests.
- Invalid manifests fail at startup.
- Domain overlays are injected deterministically at runtime.

---

# 6. Phase 2 — LLM Provider Abstraction

## Goal

Create provider-neutral model access.

## Tasks

- Create unified LLM interface.
- Support providers:
  - Ollama
  - OpenAI
  - Anthropic
  - Azure OpenAI
- Add token budget control per run.
- Add token budget control per agent.
- Add token budget control per workflow.
- Add cost tracking.
- Add spend limits.
- Add circuit breaker pattern.
- Add fail-fast behavior on provider outage.
- Add retry logic with exponential backoff.
- Add structured output enforcement.

## Suggested Files

```text
core/llm/provider.py
core/llm/router.py
core/llm/budget.py
core/llm/costs.py
core/llm/retry.py
core/llm/structured_output.py
```

## Inspirations to Review

- `BerriAI/litellm`
- `jd/tenacity`

## Success Criteria

- Agents call a unified provider interface.
- Provider failure does not crash the runtime.
- Token and cost budgets are enforced.

---

# 7. Phase 3 — Decision Engine

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
- Add agent communication protocol:
  - structured state passing between agents
  - TypedDict schema
- Add conflict resolution protocol:
  - when agents disagree, ZEUS arbitrates using a defined schema
  - no ad hoc arbitration
- Add criticality levels C1-C5 controlling:
  - max agent count
  - approval requirements
  - max depth
  - max subtasks
- Add precheck gate:
  - runs before ZEUS plans
  - runs on every instruction
  - executed by HERMES as preprocessing
  - verdicts:
    - approved
    - trim
    - upgrade
    - clarification
    - blocked
  - if blocked or clarification: workflow stops before any agent is activated
- Add `COGNITIVE_LIMITS` enforced at runtime:
  - C1: max 1 agent, 1 subtask, depth 1
  - C2: max 2 agents, 2 subtasks, depth 1
  - C3: max 4 agents, 3 subtasks, depth 2
  - C4: max 6 agents, 5 subtasks, depth 3
  - C5: max 8 agents, 6 subtasks, depth 3
- Add `AGENT_TRIGGERS`:
  - per agent, which criticality levels activate it automatically
  - examples:
    - PROMETHEUS: C4, C5 only
    - THEMIS: C4, C5 only
    - ARES: C3, C4, C5
    - APHRODITE: never auto-activated
    - KAIROS: C1 through C5
  - agents outside their trigger range are not instantiated for that run

## Suggested Files

```text
core/decision/context.py
core/decision/action.py
core/decision/plan.py
core/decision/engine.py
core/decision/router.py
core/decision/validator.py
core/decision/precheck.py
core/decision/criticality.py
core/decision/triggers.py
```

## Inspirations to Review

- `salesforce-misc/switchplane`
- `beomwookang/deliberate`
- Anthropic multi-agent research system

## Success Criteria

- Pantheon can produce a decision plan without executing tools.
- Decision plans can be tested independently.
- Missing information can trigger `WAIT_FOR_USER`.
- Blocked instructions stop before agent activation.
- Cognitive limits are enforced by the runtime.

---

# 8. Phase 4 — Execution Engine

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
- Add background job queue:
  - ARQ / Redis
  - async execution requires the queue in the first execution design
- Add sandboxing:
  - tool execution is isolated
  - blast radius is bounded per call
- Add fallback strategies:
  - simplified plan on primary failure
- Add background memory extraction job:
  - after every completed run, lessons and patterns are extracted and stored
  - not fire-and-forget
  - traced job with its own run ID
  - failure handling required
  - primary path: ARQ / Redis
  - fallback: local async task with error logging if queue is unavailable

## Suggested Files

```text
core/execution/state.py
core/execution/result.py
core/execution/engine.py
core/execution/jobs.py
core/execution/sandbox.py
core/runtime/agent_runtime.py
core/runtime/workspace.py
core/memory/extraction_job.py
```

## Inspirations to Review

- `All-Hands-AI/OpenHands`
- `samuelcolvin/arq`

## Success Criteria

- A `DecisionPlan` can be executed.
- Parallel groups can run safely.
- Execution generates artifacts, scores and logs.
- Memory extraction is tracked as its own job.

---

# 9. Phase 5 — Workflow Pack Versioning

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
- Add `FlowManager` runtime CRUD API for workflow definitions.
- Add endpoints:
  - `GET /flows`
  - `POST /flows`
  - `GET /flows/{name}`
  - `PATCH /flows/{name}`
  - `DELETE /flows/{name}`
  - `POST /flows/{name}/trigger`
- On startup, seed missing workflow YAMLs from disk into the registry automatically.
- Store workflow definitions in the DB.
- Load workflow definitions from `config/workflows/*.yaml`.

## Suggested Files

```text
core/workflows/version.py
core/workflows/registry.py
core/workflows/loader.py
core/workflows/diff.py
core/workflows/flow_manager.py
config/workflows/example.workflow.yaml
platform/api/apps/flows/router.py
```

## Inspirations to Review

- `JustVugg/distillery`
- `micpet7514088/skills-manager`

## Success Criteria

- A workflow version can be loaded from YAML.
- A candidate workflow can be compared with an active workflow.
- A previous version can be restored.
- Runtime workflow CRUD is available through the API.

---

# 10. Phase 6 — Policy and Security

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
- Add data lineage:
  - chunks
  - tools
  - agents
  - claims
  - final output links
- Add veto authority:
  - designated agents can block execution before it completes
  - designated agents include ARES and THEMIS
- Add veto severity levels:
  - `bloquant`: stops execution immediately, run cannot continue
  - `avertissement`: flags the issue but execution continues with a warning
- Add condition levée:
  - every veto carries a structured resolution condition
  - the condition states what must change for the veto to be lifted
  - stored alongside the veto in the run record

## Suggested Files

```text
core/policies/engine.py
core/policies/rules.py
core/policies/action_gate.py
core/policies/veto.py
core/policies/lineage.py
platform/api/apps/approvals/router.py
```

## Inspirations to Review

- `wiserautomation/SupraWall`
- `open-policy-agent/opa`

## Success Criteria

- Risky actions are blocked or paused.
- Tool calls are auditable.
- Sensitive credentials are never exposed to agents.
- Every output claim can be traced to chunks, tools and agents.

---

# 11. Phase 7 — Testing Infrastructure

## Goal

Create deterministic tests before evaluation.

## Tasks

- Add mock LLM client with recorded responses.
- Add agent test fixtures and harness.
- Add workflow integration test runner.
- Add deterministic agent runs for regression testing.
- Add skill unit tests.
- Add tool mock layer.

## Suggested Files

```text
tests/unit/
tests/integration/
tests/fixtures/
tests/workflows/
core/testing/mock_llm.py
core/testing/harness.py
core/testing/tool_mocks.py
```

## Inspirations to Review

- `pytest-dev/pytest-asyncio`
- `lundberg/respx`

## Success Criteria

- Agents can be tested without live LLM providers.
- Workflows can be regression-tested deterministically.
- Tools can be mocked.

---

# 12. Phase 8 — Evaluation Engine

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
- Add Hera supervision scoring:
  - runs on every orchestration
  - separate from general workflow evaluation
  - post-synthesis supervision
  - not end-user evaluation
  - 5-axis run score:
    - quality: 0-100
    - coherence: 0-100
    - confidence: 0-100
    - risk: 0-100
  - Hera verdict:
    - aligned
    - misaligned
    - degraded
  - Hera feedback:
    - structured text explaining the verdict
- Add decision scoring:
  - structured 100-point score across 5 axes for project decisions
  - stored separately from run scores in `decision_scores`
  - used for C4/C5 decisions to produce a traceable quality rating

## Suggested Files

```text
core/evaluation/runner.py
core/evaluation/scorecard.py
core/evaluation/metrics.py
core/evaluation/hera.py
core/evaluation/decision_scores.py
tests/evals/
```

## Inspirations to Review

- `langchain-ai/openevals`
- `promptfoo/promptfoo`
- `langfuse/langfuse`

## Success Criteria

- Workflow versions can be benchmarked.
- A candidate version cannot be promoted without evaluation.
- Hera produces a structured supervision score for every orchestration.

---

# 13. Phase 9 — Deliberation and Anti-Bullshit

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

# 14. Phase 10 — Structured Skills Library

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

- `microsoft/semantic-kernel`
- `JustVugg/distillery`
- `micpet7514088/skills-manager`

## Success Criteria

- Skills are reusable across workflows.
- Skills can be tested independently.

---

# 15. Phase 11 — Document Intelligence Layer

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
- Add hybrid search using Reciprocal Rank Fusion (RRF):
  - combine pgvector cosine similarity for semantic retrieval
  - combine PostgreSQL GIN full-text index for BM25-style keyword match
  - rank results by fused score, not by either signal alone
- Add synthesis cache:
  - after high-criticality runs C4/C5, final synthesis is promoted to a wiki page
  - wiki page receives its own vector embedding
  - subsequent similar queries retrieve the cached synthesis before running agents

## Suggested Files

```text
core/documents/ingestion.py
core/documents/indexing.py
core/documents/retrieval.py
core/documents/citations.py
core/documents/rrf.py
core/documents/synthesis_cache.py
modules/tools/documents/pdf_reader/
modules/tools/documents/docx_reader/
```

## Inspirations to Review

- `deepset-ai/haystack`
- `run-llama/llama_index`
- `sahilalaknur21/SmartDocs-Multillingual-Agentic-Rag`

## Success Criteria

- Retrieved chunks preserve source, page and section metadata.
- Documents can be cited reliably.
- Hybrid retrieval uses fused semantic and keyword ranking.
- C4/C5 syntheses can be reused through the synthesis cache.

---

# 16. Phase 12 — Graph Orchestration

## Goal

Enable graph-based dynamic orchestration.

## Tasks

- Create `GraphState`.
- Wrap agents as LangGraph nodes.
- Add conditional edges.
- Add `WAIT_FOR_USER` node.
- Add partial replan support.
- Add child workflows.
- Add PostgreSQL checkpointer for HITL resume:
  - graph state persisted to PostgreSQL at every node boundary
  - after human approval, graph resumes from the exact checkpoint
  - completed steps are not re-run
  - required for reliable `WAIT_FOR_USER`

## Suggested Files

```text
core/graph/state.py
core/graph/adapter.py
core/graph/nodes.py
core/graph/routes.py
core/graph/checkpointer.py
```

## Inspiration

- `langchain-ai/langgraph`

## Success Criteria

- Complex workflows can be represented as graphs.
- User clarification can pause and resume a workflow.
- Same-topic messages can be merged into running workflows.
- HITL resumes from PostgreSQL checkpoints.

---

# 17. Phase 13 — Observability and Admin Console

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

# 18. Phase 14 — Feedback and Learning Engine

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

- `stanfordnlp/dspy`
- `NousResearch/hermes-agent-self-evolution`
- `micpet7514088/autogap`

## Success Criteria

- Negative feedback can generate improvement suggestions.
- The system proposes candidate workflow versions, not silent mutations.

---

# 19. Phase 15 — Graph Memory and Knowledge

## Goal

Add structured relational memory.

## Tasks

- Create `GraphMemory`.
- Extract entities.
- Extract relations.
- Track contradictions.
- Support hybrid vector + graph retrieval.
- Connect to METIS, PROMETHEUS and APOLLO.
- Add Markdown knowledge indexing:
  - headings
  - sections
  - anchors
  - internal playbooks
  - skill documentation

## Suggested Files

```text
core/memory/graph_memory.py
core/knowledge/markdown_index.py
modules/tools/graph/
modules/tools/markdown/md_index/
knowledge/
```

## Inspirations to Review

- `ADVASYS/ragraph`
- `Fusion/mdidx`
- `neo4j/neo4j-python-driver`

## Success Criteria

- The system can reason over relations, not only similar chunks.
- Markdown files can be searched by heading path and section.
- Internal docs become retrievable knowledge.

---

# 20. Phase 16 — Durable Execution and Scaling

## Goal

Prepare for longer and heavier workflows.

## Tasks

- Add checkpoints.
- Add retries.
- Add replay runner.
- Add workflow bundles.
- Consider durable workflow orchestration later.

## Suggested Files

```text
core/checkpoints/store.py
core/replay/runner.py
core/packaging/workflow_bundle.py
```

## Inspirations to Review

- `temporalio/temporal`
- `awizemann/scarf`

## Success Criteria

- Failed workflows can resume.
- Long workflows do not lose state.
- Workflow bundles support replay and export.

---

# 21. Initial Repository Setup

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

Implement exactly:

1. Core runtime contracts: `AgentBase`, `SkillBase`, `ToolBase`
2. `AgentRegistry` loading from `config/agent_registry.yaml`
3. Manifest loader for agents, skills, and tools
4. Workflow Pack loader: YAML to `WorkflowBase`
5. One minimal workflow: two agents, one tool
6. One minimal agent with a `SOUL.md` and a test
7. One FastAPI endpoint triggering the workflow
8. One OpenWebUI-compatible chat route returning streamed output

No LangGraph. No graph memory. No learning engine. One working controlled execution loop.

---

# 22. Implementation Order

## Build First — Phases 0-6

0. Infrastructure
1. Runtime Contracts
2. LLM Provider Abstraction
3. Decision Engine
4. Execution Engine
5. Workflow Pack Versioning
6. Policy and Security

## Build Second — Phases 7-11

7. Testing Infrastructure
8. Evaluation Engine
9. Deliberation and Anti-Bullshit
10. Structured Skills Library
11. Document Intelligence Layer

## Build Third — Phases 12-16

12. Graph Orchestration
13. Observability and Admin Console
14. Feedback and Learning Engine
15. Graph Memory and Knowledge
16. Durable Execution and Scaling

---

# 23. Non-Goals for the First Version

- Do not version every agent independently in the UI.
- Do not allow uncontrolled workflow mutation.
- Do not let agents call tools directly without a policy gate.
- Do not put business logic inside `core/`.
- Do not make OpenWebUI the runtime engine.
- Do not over-engineer graph memory before basic document retrieval works.
- Do not add LangGraph before the controlled execution loop works.

---

# 24. Inspiration Index

## Infrastructure

- `tiangolo/fastapi`
- `pgvector/pgvector-python`
- `sqlalchemy/sqlalchemy`

## Runtime Contracts

- `All-Hands-AI/OpenHands`
- `pydantic/pydantic-ai`
- `instructor-ai/instructor`
- `guardrails-ai/guardrails`

## LLM Provider Abstraction

- `BerriAI/litellm`
- `jd/tenacity`

## Core Orchestration

- Anthropic multi-agent research system
- `salesforce-misc/switchplane`
- `langchain-ai/langgraph`

## Execution

- `samuelcolvin/arq`
- `All-Hands-AI/OpenHands`

## Security

- `wiserautomation/SupraWall`
- `open-policy-agent/opa`

## Testing

- `pytest-dev/pytest-asyncio`
- `lundberg/respx`

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

- `microsoft/semantic-kernel`
- `JustVugg/distillery`
- `micpet7514088/skills-manager`

## Documents and Knowledge

- `deepset-ai/haystack`
- `run-llama/llama_index`
- `sahilalaknur21/SmartDocs-Multillingual-Agentic-Rag`
- `Fusion/mdidx`
- `ADVASYS/ragraph`
- `neo4j/neo4j-python-driver`

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
