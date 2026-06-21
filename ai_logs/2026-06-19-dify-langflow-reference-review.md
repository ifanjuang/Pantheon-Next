# AI Log — Dify / Langflow Agentic Builder Review

Date: 2026-06-19

## Trigger

The user asked to proceed after reviewing an external Dify vs Langflow comparison article.

The goal was to classify Dify and Langflow inside Pantheon Next without treating either tool as a governance authority or installing anything.

## Doctrine and placement constraints

Relevant Pantheon Next constraints followed:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Tool-specific names belong in bindings, adapters, integration notes or reference reviews, not in generic doctrine.

The work therefore created a product-specific reference review under:

```text
docs/governance/reference_reviews/
```

## Repository coordination checked

Repository search found no existing Dify/Langflow review document or PR.

Notion search found an existing planning signal:

```text
Installer — sélection outils / skills / plugins pour Hermes
Ring 3: Langflow/Flowise/Dify/GraphRAG/Agent Framework en lab uniquement.
```

That was treated as a planning signal, not as canonical doctrine.

Related reference-review precedent checked:

```text
PR #147 — Langfuse / Hermes observability adapter review
PR #160 — AgentVision visual evidence adapter review, currently draft
```

## External references checked

Current public sources checked for orientation:

```text
https://interconnectd.com/blog/175/dify-vs-langflow-2026-the-ultimate-agentic-ai-comparison-review/
https://docs.dify.ai/
https://github.com/langgenius/dify
https://docs.langflow.org/
https://github.com/langflow-ai/langflow
```

The comparison article was treated as orientation only.

Official documentation and repository positioning must win before any implementation pass.

## Change made

Added:

```text
docs/governance/reference_reviews/DIFY_LANGFLOW_AGENTIC_BUILDER_REVIEW.md
```

The document classifies:

```text
Dify = candidate specialized AI app surface
Langflow = candidate visual workflow lab
Hermes = execution runtime
Pantheon = governance layer
```

## Classification

```text
Accepted:
- Dify as candidate specialized AI app surface.
- Langflow as candidate visual workflow lab.
- Outputs may become Result Candidates.
- Reports or traces may support Evidence Pack Candidates if source, scope and limitations are explicit.

Refused:
- Dify or Langflow as governance authority.
- Successful run as truth.
- RAG answer as Evidence Pack.
- Published app as authorized external action.
- Flow memory as canonical Pantheon memory.
- Visual workflow as approval gate.

To verify:
- actual deployment model and maintenance cost;
- auth and workspace isolation;
- stable metadata for Task Contract / Result Candidate / Evidence Pack Candidate linkage;
- whether memory features must be disabled or candidate-only;
- whether Dify can show sources and status enough for Pantheon output discipline;
- whether Langflow flows can be serialized and translated into Hermes tasks.

To arbitrate:
- whether adding another surface is worth the operational cost;
- whether Dify or Langflow gets a sandbox trial;
- whether any future Docker, `.env`, `operations/`, `platform/`, schema or test work is justified.
```

## Boundary

Documentation only.

No Dify installation.
No Langflow installation.
No Docker change.
No `.env` change.
No `operations/` change.
No `platform/` change.
No `pyproject.toml` change.
No schema change.
No test change.
No runtime code added.
No Dashboard implementation added.
No Hermes integration added.
No connector added.
No memory engine added.
No approval engine added.
No external action authorized.

Repository state: documented non-implemented.

## Verification target

Real diff should show exactly two added files:

```text
docs/governance/reference_reviews/DIFY_LANGFLOW_AGENTIC_BUILDER_REVIEW.md
ai_logs/2026-06-19-dify-langflow-reference-review.md
```

No protected path should be touched.
