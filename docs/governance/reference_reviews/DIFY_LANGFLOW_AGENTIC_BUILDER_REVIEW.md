# Dify / Langflow Agentic Builder Review

Status: external reference / support review — candidate app-surface and workflow-lab placement, documented non-implemented.

This document records how Dify and Langflow may be considered around Pantheon Next after reviewing a public comparison article and official project references.

It does not install Dify, install Langflow, add Docker Compose, modify `operations/`, modify `platform/`, modify `.env`, modify `pyproject.toml`, create a workflow runtime, create an app runtime, create a connector, create a schema, create a test, create a memory engine, create an approval engine, create an Evidence Pack authority or authorize external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## External references

Primary references to recheck before any implementation:

```text
https://interconnectd.com/blog/175/dify-vs-langflow-2026-the-ultimate-agentic-ai-comparison-review/
https://docs.dify.ai/
https://github.com/langgenius/dify
https://docs.langflow.org/
https://github.com/langflow-ai/langflow
```

Current public positioning, as reviewed:

```text
Dify presents itself as an open-source platform for building agentic workflows / LLM applications, with visual workflow definition, data-source connection and deployment of AI applications.
Langflow presents itself as a visual / Python-friendly framework for composing flows, agents, components and tool-connected workflows.
```

The comparison article is useful as orientation, not as doctrine.

Any technical claim from the article must be checked against official docs, repository state and an internal proof-of-concept before it influences placement.

## Core classification

```text
Dify packages AI applications.
Langflow prototypes and composes flows.
Hermes executes governed work.
Pantheon governs consequence.
```

Dify and Langflow are not equivalent to Pantheon.

They are candidate external tools that may help expose, compose or package AI workflows.

They do not decide what is true, approved, remembered or allowed to act.

## Placement

### Dify

Dify belongs, if used, near the exposure surface / application surface.

Possible role:

```text
specialized AI app surface
prototype-to-application shell
workflow-backed mini-app
RAG / knowledge app front-end
API-published assistant shell
```

Dify may be useful for bounded architecture-office apps such as:

```text
quote vs CCTP review assistant
candidate PLU note assistant
project-document Q&A assistant
client email draft assistant
meeting-summary assistant
source-backed note assistant
```

Pantheon placement rule:

```text
Dify may package a governed application.
Dify must not be the governance authority.
```

### Langflow

Langflow belongs, if used, near the workflow lab / visual composition layer.

Possible role:

```text
visual workflow lab
RAG pipeline prototyping
agent tool-chain sketching
component-level experiment surface
flow debugging surface
```

Langflow may be useful for designing and testing candidate workflows before they are rewritten, bounded or executed by Hermes.

Pantheon placement rule:

```text
Langflow may prototype a governed workflow.
Langflow must not be the production authority.
```

## Accepted

Accepted as candidate external patterns:

- Dify as a candidate specialized AI app surface for bounded, user-facing or team-facing AI applications.
- Langflow as a candidate visual workflow lab for prototyping RAG, tool and agent flows.
- Dify or Langflow outputs may become Result Candidates.
- Dify or Langflow traces, reports or intermediate artifacts may support Evidence Pack Candidates if source, scope and limitations are explicit.
- Dify may be evaluated for simple professional mini-apps where the user sees sources, status and decision gates.
- Langflow may be evaluated for flow design before a stable Hermes implementation.
- Either tool may be referenced by the Dashboard as an external tool, status card or link, subject to separate implementation approval.

## Refused

Refused as Pantheon authority or professional control:

- Dify app = approved output.
- Langflow flow = valid professional method.
- Successful Dify run = truth.
- Successful Langflow run = proof.
- Published app = authorized external action.
- RAG answer = Evidence Pack.
- Tool trace = Registre Probatoire entry.
- Flow memory = canonical Pantheon memory.
- App workspace = project source of truth.
- Visual workflow = approval gate.
- Dify or Langflow as replacement for Hermes execution discipline.
- Dify or Langflow as replacement for Pantheon governance.

A working flow proves only that a flow ran.

It does not prove that its conclusion is right, current, authorized, safe, in scope or professionally usable.

## Relationship with existing stack

Current candidate stack logic:

```text
OpenWebUI
= general conversational exposure surface

Dify
= specialized AI application surface, if needed

Langflow
= visual workflow lab, if needed

Hermes
= execution runtime

n8n
= deterministic automation / connector workflows

LiteLLM
= model gateway

Langfuse / Promptfoo / AgentVision
= observability, tests, visual evidence candidates

Pantheon
= status, evidence, scope, approval, validated memory and external-action governance
```

This means Dify and Langflow should not be added just because they are powerful.

They should be added only if they reduce friction that OpenWebUI, Hermes, n8n and the Dashboard do not already solve.

## Candidate architecture-office uses

### Dify candidates

```text
CCTP / devis comparison app
Source-backed permit note app
Client-facing draft assistant with explicit approval gate
Internal project-document Q&A app
Knowledge-base assistant for office methods
```

Required boundaries:

```text
all outputs candidate
sources visible
scope explicit
external sending disabled or approval-gated
memory candidate-only
no canonical project facts without validation
```

### Langflow candidates

```text
RAG pipeline prototype
source-selection experiment
flow-level prompt strategy test
tool-call sequence draft
Evidence Pack Candidate assembly experiment
```

Required boundaries:

```text
lab first
no external action by default
no write access to project sources
no canonical memory
handoff to Hermes before production execution when consequential
```

## First safe test

Recommended first test, if this line is pursued:

```text
Dify only.
One bounded internal app.
No external action.
No memory promotion.
No client data until sandbox reviewed.
No production deployment claim.
```

Suggested test case:

```text
Input: fictional CCTP excerpt + fictional quote.
Task: produce a comparison note candidate.
Expected output: Result Candidate + source references + limitations + approval need.
Forbidden output: final validation, external email, contract instruction, memory write.
```

Langflow should remain second-pass unless Dify proves too restrictive for workflow logic.

## Security and data boundary

Before any installation or test on real project data, decide:

```text
authentication
user roles
workspace isolation
project isolation
local vs cloud deployment
model routing
secrets storage
network egress
logs and traces
retention
backup and restore
client-data redaction
whether app outputs may be exported
whether tool calls can mutate external systems
```

No external app builder should receive unrestricted project data by default.

No app builder should keep canonical memory by default.

## To verify

- Current Dify deployment model, API stability, app types, workflow limitations, auth model and self-host maintenance cost.
- Current Langflow deployment model, component model, tool-action safety, flow export format, auth model and self-host maintenance cost.
- Whether Dify can expose sources and status in a way compatible with Pantheon output discipline.
- Whether Langflow flows can be serialized, reviewed and translated into Hermes-executable tasks.
- Whether either tool can emit stable metadata for Task Contract, Result Candidate and Evidence Pack Candidate linkage.
- Whether their logs should be linked to Langfuse or kept separate.
- Whether their memory features must be disabled, sandboxed or treated as candidate-only.

## To arbitrate

- Add Dify as a real candidate app surface, or keep OpenWebUI as the only exposure surface for now.
- Add Langflow as a workflow lab, or rely on Hermes/n8n/Python directly.
- Which tool, if any, gets the first sandbox trial.
- Whether the trial is local-only, Tailscale-only or GitHub Pages/documentation-only.
- Whether any Docker, `.env`, `operations/`, `platform/`, schema or test change is justified later.
- Whether Dify/Langflow deserve a future adapter document after a sandbox test.

## Decision posture

```text
Accepted: Dify and Langflow as external candidates to study.
Refused: Dify or Langflow as governance authority.
To verify: actual integration friction, security, metadata and workflow handoff.
To arbitrate: whether adding another surface is worth the operational cost.
```

## Boundary phrase

```text
Dify can package governed AI applications.
Langflow can prototype governed workflows.
Neither validates truth, approval, memory or action.
Pantheon governs the consequence.
The human decides.
```
