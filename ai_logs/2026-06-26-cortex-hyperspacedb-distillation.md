# AI log — CORTEX / HyperspaceDB distillation

Date: 2026-06-26

## Request

Distill two external references for Pantheon Next / Hermes qualification:

- `https://github.com/SaiAkhil066/CORTEX-AI-SUPER-RAG`
- `https://github.com/YARlabs/hyperspace-db`

## Canonical context read

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

Relevant coordination checked:

- Issue #90: freezes new reference fiches until backlog / Registre Probatoire sequencing is stabilized.
- Issue #118: Hermes-first external modules shortlist.
- Prior RAG intake issue #179: external RAG references remain candidate-only and do not define truth, proof, evidence, approval, scope or external action.

## Action taken

No new `reference_reviews/` fiche was created because issue #90 records an active freeze on new reference fiches.

A distillation comment was added to issue #118 instead, with the following placement:

```text
CORTEX proposes a RAG pipeline pattern.
HyperspaceDB proposes a vector-store / spatial-index backend.
Hermes may test either under contract.
Pantheon governs what their outputs are allowed to mean.
```

Notion tracking cards were already created for both references and kept as external reference / to verify.

## Distilled placement

### CORTEX-AI-SUPER-RAG

Accepted as candidate patterns:

- local-first RAG pipeline shape;
- hybrid lexical + vector retrieval;
- contextual chunking;
- query expansion / RRF;
- reranking;
- relevance grading;
- source-card UX.

Refused placement:

- not Pantheon kernel;
- not OpenWebUI/Pantheon Control replacement;
- not proof layer;
- not Registre Probatoire layer;
- not install target for the first Hermes module set.

To verify:

- dependency posture;
- file handling;
- citation stability;
- GraphRAG robustness;
- raw reasoning display risk;
- local model and reranker behavior;
- ability to emit Result Candidate + Evidence Pack Candidate without overclaiming.

### HyperspaceDB

Accepted as candidate patterns:

- Rust vector-store backend candidate;
- MRL / cascade retrieval idea;
- typed metadata filtering;
- sidecar document storage pattern;
- low-RAM claim worth benchmarking;
- possible local / edge deployment fit.

Refused placement:

- not Pantheon kernel;
- not governance layer;
- not proof validator;
- not Registre Probatoire layer;
- not data platform by implication;
- not accepted on benchmark claims alone.

To verify:

- reproducible install;
- smoke tests;
- deterministic rebuild / export / backup;
- RAM and latency against baseline;
- citation and source-span traceability;
- security posture around raw text storage, API keys and endpoint exposure.

## Candidate benchmark frame

```text
Task Contract in
-> Hermes read-only RAG benchmark
-> Result Candidate + Evidence Pack Candidate out
```

Baseline:

- existing FAISS/BM25 or simple local RAG.

Candidate A:

- CORTEX-like retrieval composition, without adopting its UI or memory semantics.

Candidate B:

- HyperspaceDB as vector-store backend, compared against baseline and optionally Qdrant/Chroma.

Required outputs:

- retrieved source spans;
- source authority class;
- retrieval/rerank scores where available;
- negative results;
- contradictions surfaced;
- result status: candidate / to verify only;
- no approval, no Registre Probatoire entry, no external action.

## Decision Zeus proposed

- CORTEX: À vérifier as method/pipeline reference; refused as install target for first set.
- HyperspaceDB: À vérifier as backend benchmark candidate; refused as governance, memory or proof layer.

## Repo state

Documented non implemented.

No protected paths modified.
