# MEMORY.md — Pantheon Next Runtime Memory

This file defines the hot operational memory for Pantheon Next.

It is not a knowledge base.
It is not a project archive.
It is not a place for long documents.

It contains compact, high-signal memory that should be injected into every assistant/session run.

Stable knowledge must be promoted to the appropriate memory layer:
- Session memory → short-lived execution context
- Project memory → dossier / affaire / workflow-specific memory
- Agency memory → reusable methods, patterns, lessons and standards

---

# 1. Product Identity

§
PROJECT_NAME: Pantheon Next

§
PRODUCT_THESIS: Pantheon Next turns AI from a chatbot into a thinking team for complex professional work.

§
CORE_POSITIONING: Pantheon Next is a modular multi-agent operating system for high-expertise environments: architecture, project management, legal, compliance, audit, consulting and IT.

§
NOT_A_CHATBOT: Pantheon Next is not a chatbot wrapper, not a prompt chaining framework, not a LangChain clone, not an OpenAI Assistants replacement, and not a low-code automation tool.

§
INTERFACE_RULE: OpenWebUI is only the interface layer. Pantheon Next owns orchestration, state, policies, memory, evaluation and execution.

---

# 2. Architecture Principles

§
MODULARITY_FIRST: Everything must remain modular and replaceable: agents, skills, tools, workflows, prompts, policies, memory adapters, evaluators and UI panels.

§
NO_BUSINESS_LOGIC_IN_CORE: The core runtime must remain domain-agnostic. Business behavior lives in modules.

§
RUNTIME_OVER_PROMPTS: Prompts describe behavior, but runtime controls execution. Workflows define what happens. Policies define what is allowed. Evaluators define what is good enough.

§
WORKFLOW_PACK_UNIT: The main product unit is the Workflow Pack. A workflow pack includes graph/steps, agent config, tools, skills, prompts, policies, templates, evaluation settings, learning settings and metrics.

§
CONTROL_DATA_SPLIT: Pantheon Next separates the control plane from the data plane. Control decides. Data executes.

§
NO_DIRECT_TOOL_CALLS: Agents must never execute tools directly. Every risky tool call passes through PolicyEngine / ActionGate.

§
HUMAN_CONTROL: Risky actions require explicit approval. Examples: email send, file delete, database write, Python execution, external API side effects and user-data mutation.

---

# 3. Repository Model

§
REPO_STRUCTURE: Pantheon Next uses core/, modules/, platform/, config/, tests/.

§
CORE_SCOPE: core/ contains contracts, registries, decision, execution, state, policies, evaluation, learning, memory, documents and observability.

§
MODULES_SCOPE: modules/ contains agents, skills, tools, workflows, prompts and templates.

§
PLATFORM_SCOPE: platform/ contains FastAPI, OpenWebUI integration, persistence, deployment and infrastructure.

§
CONFIG_SCOPE: config/ contains agent_registry.yaml, workflow_registry.yaml, settings.yaml and domain overlays.

§
TEST_SCOPE: tests/ contains unit, integration, fixtures and workflow tests.

---

# 4. Phase Order

§
ROADMAP_ORDER: Phase 0 Infrastructure; Phase 1 Runtime Contracts; Phase 2 LLM Provider Abstraction; Phase 3 Decision Engine; Phase 4 Execution Engine; Phase 5 Workflow Pack Versioning; Phase 6 Policy and Security; Phase 7 Testing Infrastructure; Phase 8 Evaluation Engine; Phase 9 Deliberation and Anti-Bullshit; Phase 10 Skill System; Phase 11 Document Intelligence; Phase 12 Graph Orchestration; Phase 13 Observability; Phase 14 Learning Engine; Phase 15 Graph Memory and Knowledge; Phase 16 Durable Execution and Scale.

§
BUILD_FIRST: Build phases 0–6 first: infrastructure, runtime contracts, LLM abstraction, decision engine, execution engine, workflow versioning, policy and security.

§
BUILD_SECOND: Build phases 7–11 second: testing, evaluation, deliberation, skills, document intelligence.

§
BUILD_THIRD: Build phases 12–16 third: graph orchestration, observability, learning, graph memory, durable execution.

§
FIRST_MILESTONE: First milestone is one working controlled execution loop: core contracts, AgentRegistry from config, manifest loader, Workflow Pack loader, minimal workflow with two agents and one tool, minimal agent with SOUL.md and test, FastAPI endpoint, OpenWebUI-compatible streamed route.

§
FIRST_MILESTONE_EXCLUSIONS: No LangGraph, no graph memory, no learning engine in the first milestone.

---

# 5. Infrastructure Rules

§
INFRA_STACK: FastAPI, PostgreSQL, pgvector, async SQLAlchemy, Redis/ARQ, MinIO/S3 interface, Docker Compose, JWT auth, RBAC, SSE/WebSocket streaming, Ollama/OpenAI-compatible provider.

§
TENANCY_RULE: Multi-tenancy requires row-level isolation per organization.

§
MIGRATION_RULE: Alembic migrations must be sequentially numbered 0001, 0002, etc. Schema evolution is a runtime contract. Every model change requires a migration.

§
SSE_EVENT_NAMING: SSE agent events follow {agent}.{event}. Examples: hermes.preprocess_ready, zeus.plans_ready, zeus.decision, themis.veto_detected, hera.run_score, kairos.final_answer. System events: run_created, phase_start, done, error.

---

# 6. Runtime Contracts

§
CORE_CONTRACTS: Required base contracts: AgentBase, SkillBase, ToolBase, WorkflowBase, MemoryAdapter, AgentResult, Artifact, SessionState, RunState, OrchestraState.

§
MANIFEST_RULE: Agents, skills and tools are loaded through manifests. Invalid manifests must fail at startup.

§
AGENT_REGISTRY_RULE: AgentRegistry is the single source of truth for all agent identities: name, role, layer, class path, triggers, veto authority and config.

§
AGENT_VERSIONING: SOUL.md and config changes must be tracked and rollback-capable.

§
SKILL_AS_CORE_PRIMITIVE: SkillBase belongs in Runtime Contracts, not later as an optional feature. Skills are core primitives.

§
MEMORY_SCOPES: MemoryAdapter supports three scopes: session, project and agency.

§
SESSION_MEMORY: Session memory is TTL-bounded, Redis-backed, and limited to the current thread/run.

§
PROJECT_MEMORY: Project memory is scoped to the dossier, affaire or project lifetime.

§
AGENCY_MEMORY: Agency memory stores permanent cross-project patterns, methods, lessons and standards.

§
DOMAIN_OVERLAY: Domain overlays live in domains/{domain}/prompts/context.yaml and are injected into all agent system prompts at runtime.

§
DOMAIN_ENV: Active domain is set via DOMAIN=architecture or another domain name.

§
DOMAIN_OVERLAY_CONTENT: Domain overlays carry trusted_sources, criticality_keywords and veto_patterns.

---

# 7. LLM Provider Rules

§
LLM_ABSTRACTION: All agents call a unified LLM interface. No direct provider-specific calls inside agents.

§
LLM_PROVIDERS: Supported providers should include Ollama, OpenAI, Anthropic and Azure OpenAI.

§
LLM_BUDGETS: Token budgets must be enforceable per run, per agent and per workflow.

§
LLM_COSTS: Cost tracking and spend limits are runtime concerns.

§
LLM_RESILIENCE: Provider calls require circuit breaker behavior, fail-fast on outage, retry with exponential backoff, and structured output enforcement.

§
LLM_REFERENCES: Useful references: BerriAI/litellm and jd/tenacity.

---

# 8. Decision Engine Rules

§
DECISION_ENGINE_ROLE: DecisionEngine belongs to the control plane. It decides what should happen before execution.

§
DECISION_OBJECTS: Required objects: DecisionContext, DecisionAction, DecisionPlan.

§
DECISION_ROUTES: Supported routes: CONTINUE, WAIT_FOR_USER, MERGE, FORK, CHILD_FORK.

§
PRECHECK_GATE: HERMES runs a precheck gate before ZEUS plans, on every instruction.

§
PRECHECK_VERDICTS: Precheck verdicts: approved, trim, upgrade, clarification, blocked.

§
PRECHECK_STOP_RULE: If HERMES returns blocked or clarification, the workflow stops before any agent is activated.

§
AGENT_COMMUNICATION: Agents pass structured state through TypedDict or equivalent schema. No ad hoc state blobs.

§
CONFLICT_RESOLUTION: When agents disagree, ZEUS arbitrates using a defined schema. No implicit or improvised conflict resolution.

§
CRITICALITY_LEVELS: Runs use C1–C5 criticality levels controlling max agent count, approvals, depth and subtasks.

§
COGNITIVE_LIMITS: C1 max 1 agent/1 subtask/depth 1. C2 max 2 agents/2 subtasks/depth 1. C3 max 4 agents/3 subtasks/depth 2. C4 max 6 agents/5 subtasks/depth 3. C5 max 8 agents/6 subtasks/depth 3.

§
COGNITIVE_LIMITS_ENFORCEMENT: Cognitive limits are runtime constraints enforced by ExecutionEngine, not suggestions.

§
AGENT_TRIGGERS: Agents have criticality trigger ranges. Agents outside trigger range are not instantiated for that run.

§
DEFAULT_TRIGGERS: PROMETHEUS C4/C5 only. THEMIS C4/C5 only. ARES C3/C4/C5. APHRODITE never auto-activated. KAIROS C1–C5.

§
TRIGGER_OVERRIDE_RULE: Workflow Packs may override default triggers when explicitly configured and policy allows it.

---

# 9. Execution Engine Rules

§
EXECUTION_ENGINE_ROLE: ExecutionEngine belongs to the data plane. It executes validated DecisionPlans. It does not decide strategy.

§
EXECUTION_OBJECTS: Required objects: ExecutionState, ExecutionResult.

§
EXECUTION_MODES: ExecutionEngine supports sequential actions, parallel action groups, blocked actions and approval-needed actions.

§
RUNTIME_INJECTION: ExecutionEngine injects agent config, tools and skills into AgentRuntime per action.

§
JOB_QUEUE_REQUIRED: Async execution requires ARQ/Redis early. Do not defer basic job queue design to the scaling phase.

§
SANDBOXING_RULE: Tool execution is isolated. Blast radius is bounded per call.

§
FALLBACK_RULE: Primary execution failure should allow simplified fallback plans where safe.

§
MEMORY_EXTRACTION_JOB: After every completed run, lessons and patterns are extracted and stored through a traced background job with its own run ID and failure handling.

§
MEMORY_EXTRACTION_FALLBACK: Primary memory extraction path is ARQ/Redis. Fallback is local async task with error logging if queue unavailable.

---

# 10. Workflow Pack Rules

§
WORKFLOW_PACK_TIMING: Workflow Pack versioning comes after DecisionEngine and ExecutionEngine design. Do not version what is not yet structurally defined.

§
WORKFLOW_STATUSES: Workflow version statuses are draft, candidate, active, archived.

§
FLOW_MANAGER: FlowManager provides runtime CRUD API for workflow definitions.

§
FLOW_ENDPOINTS: Required endpoints: GET /flows, POST /flows, GET /flows/{name}, PATCH /flows/{name}, DELETE /flows/{name}, POST /flows/{name}/trigger.

§
FLOW_SEEDING: On startup, missing workflow YAMLs from disk are seeded into the registry automatically.

§
FLOW_STORAGE: Workflow definitions are stored in DB and loaded from config/workflows/*.yaml.

---

# 11. Policy and Security Rules

§
POLICY_GATE_RULE: Every tool call and every risky agent action passes through PolicyEngine before execution.

§
POLICY_OUTCOMES: Policy outcomes are allow, block, require_approval.

§
VETO_AUTHORITY: Designated agents can block execution before completion. ARES and THEMIS have veto authority by default.

§
VETO_SEVERITY: Veto severity levels: bloquant and avertissement.

§
BLOQUANT_VETO: Bloquant stops execution immediately. Run cannot continue.

§
AVERTISSEMENT_VETO: Avertissement flags the issue but execution continues with warning.

§
CONDITION_LEVEE: Every veto carries a structured resolution condition explaining what must change for veto to be lifted.

§
VETO_STORAGE: Veto and condition levée are stored alongside the run record.

§
DATA_LINEAGE: Every output claim must be traceable to chunks, tools and agents.

§
SECURITY_REFERENCES: Useful references: wiserautomation/SupraWall and open-policy-agent/opa.

---

# 12. Testing and Evaluation Rules

§
TESTING_BEFORE_EVAL: Testing infrastructure comes before EvaluationEngine.

§
TESTING_STACK: Required testing elements: mock LLM client with recorded responses, agent fixtures, agent harness, workflow integration runner, deterministic agent runs, skill unit tests, tool mock layer.

§
TESTING_REFERENCES: Useful references: pytest-dev/pytest-asyncio and lundberg/respx.

§
EVALUATION_ENGINE_ROLE: EvaluationRunner measures quality and regression. It does not mutate workflows.

§
HERA_ROLE: HERA performs post-synthesis supervision on every orchestration. It is separate from general workflow evaluation and separate from end-user evaluation.

§
HERA_SCORE: HERA uses 5-axis run score: quality 0–100, coherence 0–100, confidence 0–100, risk 0–100, plus structured feedback.

§
HERA_VERDICT: HERA verdicts: aligned, misaligned, degraded.

§
DECISION_SCORING: C4/C5 project decisions receive structured 100-point decision scores across 5 axes, stored separately in decision_scores.

§
EVAL_REFERENCES: Useful references: langchain-ai/openevals, promptfoo/promptfoo, langfuse/langfuse.

---

# 13. Deliberation and Anti-Bullshit

§
METIS_ROLE: METIS handles structured deliberation: hypotheses, uncertainties, conflicts and recommended checks.

§
PROMETHEUS_ROLE: PROMETHEUS challenges weak reasoning, contradictions, unsupported claims and false consensus.

§
BALONEY_SKILL: critique.baloney_detection detects unsupported claims, vague authority, overconfidence and false absence claims.

§
APOLLO_VALIDATION: APOLLO integrates confidence, traceability, coherence, citation quality and bullshit_risk_score.

§
DELIBERATION_REFERENCES: Useful references: beomwookang/deliberate and jrcruciani/baloney-detection-kit.

---

# 14. Skill System Rules

§
SKILL_REGISTRY: SkillRegistry manages skill identities, manifests, versions and tests.

§
SKILL_FOLDER_RULE: One folder per skill. Each skill has manifest, prompt/procedure and tests.

§
INITIAL_SKILLS: Initial skills: research.crosscheck, document.dossier_build, communication.professional_rewrite, critique.baloney_detection, legal.citation_enforcer.

§
SKILL_REFERENCES: Useful references: microsoft/semantic-kernel, JustVugg/distillery, micpet7514088/skills-manager.

---

# 15. Document Intelligence Rules

§
DOCUMENT_LAYER: Document Intelligence provides ingestion, indexing, retrieval and citation tracking.

§
DOCUMENT_METADATA: Preserve file, page, section, language and source_id metadata.

§
HYBRID_SEARCH: Hybrid search uses Reciprocal Rank Fusion.

§
RRF_RULE: RRF combines pgvector cosine similarity with PostgreSQL GIN full-text index for BM25-style keyword match. Results are ranked by fused score, not either signal alone.

§
SYNTHESIS_CACHE: After C4/C5 runs, final synthesis is promoted to a wiki page with its own vector embedding.

§
SYNTHESIS_CACHE_LOOKUP: Similar future queries retrieve cached synthesis before running full agent orchestration.

§
DOCUMENT_REFERENCES: Useful references: deepset-ai/haystack, run-llama/llama_index, sahilalaknur21/SmartDocs-Multillingual-Agentic-Rag.

---

# 16. Graph Orchestration Rules

§
LANGGRAPH_TIMING: LangGraph comes after controlled execution loop, workflow versioning, policy and testing. Do not start with LangGraph.

§
LANGGRAPH_ROLE: LangGraph is an adapter for dynamic orchestration, not the whole architecture.

§
CHECKPOINTER_RULE: PostgreSQL checkpointer is required for HITL resume.

§
HITL_RESUME: Graph state is persisted to PostgreSQL at every node boundary. After human approval, graph resumes from the exact checkpoint without re-running completed steps.

§
LANGGRAPH_REFERENCE: Useful reference: langchain-ai/langgraph.

---

# 17. Observability Rules

§
OBSERVABILITY_SCOPE: Track prompts, decisions, tool calls, workflow version, scores, feedback, blocked actions, cost, latency and decision logs.

§
TRACE_EVERYTHING: Every run must be inspectable after completion.

§
OBSERVABILITY_REFERENCES: Useful references: langfuse/langfuse, wandb/wandb, dagster-io/dagster.

---

# 18. Learning and Memory Promotion

§
LEARNING_ENGINE_ROLE: LearningEngine proposes improvements. It does not silently mutate active workflows.

§
CANDIDATE_ONLY: Learning creates candidate workflow versions requiring human approval.

§
GAP_ANALYZER: GapAnalyzer compares expected vs actual run behavior and proposes improvements.

§
MEMORY_PROMOTION: Information moves session → project → agency depending on stability, reuse frequency and criticality.

§
OBSIDIAN_INTERPRETATION: Obsidian-like vault patterns are useful as inspiration for markdown export and knowledge navigation, not as primary source of truth.

§
SOURCE_OF_TRUTH: Structured DB is the source of truth. Markdown is export, knowledge layer or adapter.

§
LEARNING_REFERENCES: Useful references: stanfordnlp/dspy, NousResearch/hermes-agent-self-evolution, micpet7514088/autogap.

---

# 19. Graph Memory and Knowledge

§
GRAPH_MEMORY_ROLE: GraphMemory stores entities, relations, contradictions and authority relationships.

§
MARKDOWN_INDEX: Markdown knowledge indexing supports headings, sections, anchors, internal playbooks and skill documentation.

§
GRAPH_REFERENCES: Useful references: ADVASYS/ragraph, Fusion/mdidx, neo4j/neo4j-python-driver.

---

# 20. Durable Execution and Scale

§
DURABLE_EXECUTION_ROLE: Durable execution handles checkpoints, retries, replay runner, workflow bundles and large workflow recovery.

§
TEMPORAL_TIMING: Temporal-like durability is a late-stage option, not an MVP dependency.

§
DURABLE_REFERENCES: Useful references: temporalio/temporal and awizemann/scarf.

---

# 21. First Milestone

§
MILESTONE_EXACT: First working version must include exactly: AgentBase, SkillBase, ToolBase, AgentRegistry from config/agent_registry.yaml, manifest loader for agents/skills/tools, Workflow Pack loader YAML to WorkflowBase, one minimal workflow with two agents and one tool, one minimal agent with SOUL.md and a test, one FastAPI endpoint triggering workflow, one OpenWebUI-compatible streamed chat route.

§
MILESTONE_EXCLUSIONS: No LangGraph. No graph memory. No learning engine. One working controlled execution loop.

---

# 22. Naming and Writing Style

§
VOICE: Documentation should be direct, technical and product-minded. Avoid hype. Avoid bloated marketing language.

§
PROJECT_NAME_RULE: Use Pantheon Next for the new repo. Avoid ARCEUS unless explicitly referring to legacy work.

§
README_ROLE: README is product and system overview.

§
ARCHITECTURE_ROLE: ARCHITECTURE.md explains system design.

§
AGENTS_ROLE: AGENTS.md explains agent roles, responsibilities and limits.

§
ROADMAP_ROLE: ROADMAP.md explains implementation path, phase order and references.

---

# 23. Current Best Next Step

§
NEXT_STEP: Implement Phase 0 and Phase 1 minimally before adding agent sophistication.

§
SPRINT_1_TARGET: Build a minimal controlled run: FastAPI endpoint → Hermes precheck → Athena simple plan → Kairos answer → SSE streamed output.

§
DO_NOT_OVERBUILD: Do not implement graph orchestration, graph memory or learning before the controlled execution loop works.