# Hermes Skill Supply Chain — magnus919/agent-skills

Status: external reference — skill-source and binding review — to verify.
Boundary profile: candidate_support_note.

Reviewed source: `https://github.com/magnus919/agent-skills`
Review date: 2026-07-26

## Purpose

This review evaluates `magnus919/agent-skills` as an external source of Hermes-compatible skills and uses it to test a broader Pantheon distinction:

```text
Skill Source
!= Skill Candidate
!= Capability Binding
!= Installed Skill
!= Approved Skill
!= Activated Skill
!= Task-authorized Skill
```

The review does not install a skill, adopt a framework dependency, authorize an update, activate a capability, or modify Hermes runtime configuration.

## Boundary

```text
exposed_by: OpenWebUI or another cockpit may display source, binding and lifecycle state.
executed_by: Hermes owns skill discovery, loading, installation and execution where separately configured.
governed_by: Pantheon governs placement, status, scope, evidence expectations, installation proposals, activation and consequential gates.
approved_by: human review where installation, activation, sensitive scope or consequential effects require it.
forbidden: Pantheon as skill hub, plugin manager, installer, updater, runtime, automatic trust authority or automatic approval engine.
```

## Why the source is relevant

Hermes currently supports on-demand `SKILL.md` skills, skill discovery and installation from skill sources, update checks, and external skill directories. Full skill instructions are loaded when relevant rather than injected into every request. This makes external skill repositories technically suitable as discovery sources without requiring Pantheon to absorb their runtime logic.

This compatibility is only an execution fact. It is not a governance decision.

```text
Hermes can load it != Pantheon approved it
source available != install instruction
update detected != update authorized
```

## Candidate supply-chain model

The recommended lifecycle is:

```text
External Skill Source
        |
        v
Discovery observation
        |
        v
Skill Candidate
        |
        v
Capability Slot classification
        |
        v
Binding review
        |
        v
Installation proposal
        |
     human gate
        |
        v
Hermes installation
        |
        v
Health / version observation
        |
        v
Sandbox activation
        |
        v
Scoped project or dossier activation
        |
        v
Task authorization remains separate
```

Pantheon stores or projects governance-readable status. Hermes remains the execution/runtime owner.

## Minimum source record

Candidate support shape only; not an executable schema:

```yaml
skill_source:
  source_id:
  upstream:
  source_kind: repository | hub | local_reviewed_source
  retrieved_at:
  license_status:
  maintainer_status:
  trust_status: external | reviewed_source
  discovery_allowed: true | false
  auto_install: false
  auto_update: false
  notes:
```

`trust_status: reviewed_source` would mean only that the source itself passed a bounded review. It would not approve every skill contained in it.

## Minimum skill candidate record

```yaml
skill_candidate:
  skill_id:
  source_id:
  upstream_path:
  capability_slot:
  skill_version:
  binding_target:
  permissions_required:
  network_behavior:
  filesystem_behavior:
  external_effects:
  sensitive_data_surface:
  install_status:
  health_status:
  update_status:
  activation_status:
  task_authorization_status:
  evidence_expectation:
  rollback_expectation:
  review_status:
```

This record deliberately keeps installation, health, approval, activation and task authorization on separate axes.

## Review of `magnus919/agent-skills`

Recommended classification:

```text
object: magnus919/agent-skills
nature: external skill catalogue / source repository
placement: Hermes skill-source candidate
Pantheon role: discovery, classification, review and lifecycle governance only
repo state: documented non-implemented
installation: not established
activation: inactive
approval: not granted by this review
```

The repository should not be treated as:

```text
approved skill catalogue
trusted dependency bundle
auto-install source
auto-update source
Pantheon capability registry
proof of skill safety
proof of framework suitability
```

## Haystack classification

Haystack should not be adopted merely because a Haystack skill exists.

Two separate objects must remain visible:

```text
Haystack
= external framework / possible Hermes-side capability binding

skill: haystack
= competence/instructions allowing Hermes to work with Haystack
```

Current Pantheon Next already has `document_parsing_rag_ingestion`, with RAGFlow recorded as a candidate. Haystack overlaps that area but also covers retrieval pipelines, ranking/reranking, generation pipelines and agent-oriented composition.

Therefore this review does **not** replace the existing binding. It proposes a placement decision before registry modification:

```text
Option A
Haystack -> fallback/watch candidate under document_parsing_rag_ingestion

Option B
Create a distinct abstract slot only if a durable need is demonstrated:
knowledge_retrieval_pipeline
```

Recommended abstract function for Option B:

```text
index governed corpus references
retrieve within declared scope
filter
rank / rerank
assemble grounded context
return provenance-linked candidates
```

The slot must be justified without naming Haystack. If the need only exists because Haystack exposes the feature, no new kernel-level capability should be created.

## LangChain, LlamaIndex and LangGraph

Recommended initial posture:

| External tool | Candidate placement | Review posture |
|---|---|---|
| Haystack | retrieval / RAG pipeline binding candidate | compare before registry selection |
| LlamaIndex | retrieval / indexing alternative | watch / compare |
| LangChain | broad component and integration framework | watch / compare; avoid making it a default abstraction layer by implication |
| LangGraph | existing `bounded_workflow_runtime` candidate | no architecture change |

LangGraph already has a defined place behind Hermes or a governed bridge for long-running, interruptible or checkpoint-heavy runtime work. This review does not reopen that decision.

## Relationship to document architecture

The preferred decomposition to test is:

```text
document_source_management
  -> optional Paperless-ngx binding

document_extraction
  -> Docling / OCR candidates

knowledge_retrieval_pipeline
  -> Haystack / LlamaIndex / other candidate bindings, if the slot is justified

document_parsing_rag_ingestion
  -> integrated products such as RAGFlow where useful

bounded_workflow_runtime
  -> LangGraph candidate behind Hermes
```

This decomposition is a review hypothesis, not doctrine and not a binding change.

## OpenWebUI projection

A future cockpit may show, without becoming the manager:

```text
Capability
Selected / candidate binding
Skill source
Install status
Health status
Version
Update status
Activation scope
Approval state
Risk level
Rollback expectation
Task authorization state
```

Actions such as `propose install`, `propose update`, `request benchmark`, or `request activation` are decision requests only. OpenWebUI does not perform the underlying lifecycle operation unless a separately governed external adapter exists.

## Hermes responsibilities

Hermes may, under separate operator/runtime configuration:

```text
discover skills
inspect SKILL.md metadata
install reviewed skills
load relevant skills on demand
execute skill procedures
report version / health / errors
check for updates
return Result Candidates / Evidence Pack Candidates / Capability Gaps
```

Hermes must not convert skill availability into governance approval or task authorization.

## Pantheon responsibilities

Pantheon may govern:

```text
source qualification
Capability Slot placement
binding status
installation proposal status
health observation status
update review status
activation scope
risk classification
evidence expectation
approval floor / ceiling
rollback visibility
consequential action gate
```

Pantheon must not execute the skill lifecycle.

## Human decisions

Human approval remains required where the reviewed capability or its lifecycle operation can materially change:

```text
installed dependencies
sensitive data exposure
network access
filesystem mutation
external API effects
project or production activation
breaking updates
professional outputs or decisions
```

Low-risk read-only discovery may be automatic as observation, but discovery never authorizes installation.

## Decision from this review

```text
magnus919/agent-skills:
  decision: retain as external Hermes skill-source candidate
  install: no
  activate: no
  auto_update: no

Haystack:
  decision: candidate binding to compare
  current preferred binding replacement: no
  new capability slot: not yet promoted

LlamaIndex:
  decision: watch / compare

LangChain:
  decision: watch / compare

LangGraph:
  decision: keep existing bounded_workflow_runtime placement
```

## Next admissible step

Before editing `HERMES_CAPABILITY_BINDINGS.md`, compare the existing `document_parsing_rag_ingestion` function against a proposed tool-agnostic `knowledge_retrieval_pipeline` function using at least one concrete Pantheon vertical:

```text
scoped project documents
-> extraction already completed
-> retrieval / reranking
-> Hermes candidate answer
-> provenance-linked Evidence Pack Candidate
-> human review
```

If the distinction proves useful independently of Haystack, add the slot to the registry as candidate support doctrine. Otherwise keep Haystack under an existing slot as a fallback/watch binding.

## Non-equivalences

```text
skill_source_reviewed != every_skill_reviewed
skill_discovered != skill_selected
skill_selected != skill_installed
skill_installed != skill_approved
skill_healthy != skill_safe
skill_active != task_authorized
framework_available != dependency_adopted
update_available != update_authorized
runtime_success != evidence
```
