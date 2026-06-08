# Changelog

## 0.1.45 - 2026-06-08

Corpus-wide Registre Probatoire vocabulary sweep (issue #90).

### Changed

- Across `docs/governance/**/*.md` (89 files), retire the object terms repo-wide: `Memory Candidate(s)` → `Register Candidate(s)`, `Canonical Memory` → `Registre Probatoire entry` (with article handling). Excludes the deliberate "formerly" notes and the two rename-describing meta-docs (`REGISTRE_PROBATOIRE_DIRECTION.md`, `OPEN_PR_RECONCILIATION.md`); boundary phrases such as "automatic memory promotion" and historical `CHANGELOG` / `ai_logs` are untouched. Pure rename (352/352), lint-clean, zero residual.

### Added

- `ai_logs/2026-06-08-registre-vocabulary-sweep.md` as the intervention trace.

### Boundary clarification

Documentation only. No schema, test, runtime, file rename or protected-path change. With this sweep the Registre Probatoire vocabulary is consistent across the whole governance corpus. (CHANGELOG entry numbered 0.1.45 to leave 0.1.44 for the pending CI vocabulary guard #92.)

---

## 0.1.43 - 2026-06-08

Governed composition in WORKFLOW_SCHEMA (two gates) + Registre alignment.

### Changed

- `docs/governance/WORKFLOW_SCHEMA.md` gains a `Governed composition` section: HÉPHAÏSTOS forges a Workflow Manifest candidate for a cap from capabilities declared in `CAPABILITY_REGISTRY.md`, via a retrieve/reuse/revise/retain loop and two governance gates (pre-execution eligibility arbitrated by ZEUS; post-execution evidence verification using `V0–V4` and `E0–E4`), with per-step governance signatures. `forged != authorized`. The file's memory references are aligned to the Registre Probatoire (`Memory rules` → `Register rules`; `Memory Candidate` → `Register Candidate`; `Canonical Memory` → `Registre Probatoire entry`).

### Added

- `ai_logs/2026-06-08-workflow-schema-governed-composition.md` as the intervention trace.

### Boundary clarification

Documentation only. No forge engine, compiler, scheduler, queue, provider router or runtime; no schema, test or protected-path change. Execution stays external under Task Contract. The role-registry touches (`AGENTS.md` / `GOVERNANCE_COLLEGE.md` for HÉPHAÏSTOS) remain a separate follow-up.

---

## 0.1.42 - 2026-06-08

Governed composition keystone (capability registry, two gates), rebased and indexed.

### Added

- `docs/governance/CAPABILITY_REGISTRY.md` — capabilities declared by governance metadata only, as a dependency graph HÉPHAÏSTOS forges from; declarations are candidates until reviewed; the registry records nothing executable, promotes no memory and is not a Registre Probatoire entry. Includes the SkillsGate MCP skill-admission distillation (admission discipline, not an installer).
- `docs/governance/reference_reviews/SKILL_FORGE_RUNTIMES.md` (Voyager, DSPy) and `docs/governance/reference_reviews/SKILL_GOVERNANCE.md` (EviBound, SkillsVote, GovernSpec, MedSkillAudit) — distilled forge/composition and gate/lifecycle vocabulary; `forged != authorized`; the gate stays a governance decision.
- `ai_logs/2026-06-03-governed-composition-forge.md`, `ai_logs/2026-06-08-skillsgate-mcp-skill-admission.md` and `ai_logs/2026-06-08-pr53-keystone-index-completion.md` as intervention traces.

### Changed

- `docs/governance/AUTHORITY_INDEX.md`, `docs/governance/MODULES.md` and `docs/governance/reference_reviews/README.md` now index the capability registry, the governed-composition module and the two reference reviews.

### Boundary clarification

Documentation and indexing only. No forge engine, compiler, scheduler, queue, provider router, autonomous approval engine, skill installer or memory promotion. Execution stays external under Task Contract. Rebased clean onto the Registre Probatoire `main`; aligned to `GLOSSARY` (no "Canonical Memory" / "Memory Candidate"). The `WORKFLOW_SCHEMA.md` governed-composition prose and any role-registry touches are separate follow-ups; the original `#53` is left intact.

---

## 0.1.41 - 2026-06-08

Registre Probatoire downstream E5: reindex the authority map to the new vocabulary.

### Changed

- `docs/governance/AUTHORITY_INDEX.md` and `docs/governance/MODULES.md` retire the retired object terms: `Memory Candidate` → `Register Candidate`, `Canonical Memory` → `Registre Probatoire entry`. The MODULES "Memory module" is reframed as the "Memory and Registre Probatoire module" (memory belongs to Hermès, ungoverned; Pantheon governs the Registre Probatoire). Boundary phrases ("automatic memory promotion" / "promote memory") are kept verbatim; `STATUS.md` and `README.md` contained only such boundary phrases and are unchanged.

### Added

- `ai_logs/2026-06-08-registre-e5-reindex.md` as the intervention trace.

### Boundary clarification

Documentation only. No schema, test, runtime or protected-path change. With E1–E3 and E5 landed, the Registre Probatoire vocabulary is consistent across the corpus and the index files. Remaining: E4 (bridge rule in the Answer Verification Gate, parallel track on #71) and the protected E6 schema rename.

---

## 0.1.40 - 2026-06-08

Registre Probatoire downstream E3: promote the canonicalization doc as the central register document.

### Changed

- `docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md` retitled to "Registre Probatoire — evidence canonicalization" and reframed as the central document for the `Registre Probatoire`. Retires the "Canonical Memory" wording (`Canonical Memory` → `Registre Probatoire entry`, `Memory Candidate` → `Register Candidate`), reframes the core distinction (memory = Hermès's ungoverned recall; the register entry is the approved, dated, cited record) and maps certainty onto the `E0–E4` scale. Filename unchanged so inbound links stay valid.

### Added

- `ai_logs/2026-06-08-registre-e3-canonicalization-doc.md` as the intervention trace.

### Boundary clarification

Documentation only. No schema, test, runtime or protected-path change. Remains a candidate support note (documented non-implemented). Reindexing (E5) and the schema rename (protected, E6) are later steps.

---

## 0.1.39 - 2026-06-07

Registre Probatoire downstream E2: reframe MEMORY.md.

### Changed

- `docs/governance/MEMORY.md` reframed so "memory" belongs to Hermès (free, self-evolving runtime memory, ungoverned, no authority) and the governed durable object is the `Registre Probatoire` in place of "Canonical Memory". Adds an explicit Bridge rule (Hermès memory may speak; only a Registre Probatoire entry may be cited for a consequential decision), renames `Memory Candidate` to `Register Candidate` and `Canonical Memory` to `Registre Probatoire entry` (one former-name note kept for each), adds the `E0–E4` certainty field, and reframes the Hermès relationship. All still-valid distinctions, scopes, statuses and forbidden-drift rules are preserved.

### Added

- `ai_logs/2026-06-07-registre-e2-memory-reframe.md` as the intervention trace.

### Boundary clarification

Documentation only. No schema, test, runtime or protected-path change. `MEMORY.md` stays a CI-mandatory file and is lint-clean. The `schemas/memory_candidate.schema.yaml` rename remains deferred and protected (E6). The reframe strengthens the existing boundary rather than loosening it.

---

## 0.1.38 - 2026-06-07

Registre Probatoire downstream E1: GLOSSARY owns the vocabulary and the three axes.

### Changed

- `docs/governance/GLOSSARY.md` now records the governed rename (memory reserved to Hermès; Pantheon governs the `Registre Probatoire` in place of "Canonical Memory"), adds the `Registre Probatoire` and `Hermès memory` terms, reframes `Memory Candidate` as `Register Candidate`, and owns the three distinct certainty/decision axes: `E0–E4` probative certainty (defined here), `V0–V4` answer verification (name owned here, levels owned by the Answer Verification Gate candidate), `C0–C5` approval ceiling (owned by `APPROVALS.md`, not redefined).

### Added

- `ai_logs/2026-06-07-registre-e1-glossary-axes.md` as the intervention trace.

### Boundary clarification

Documentation only. No schema, test, runtime or protected-path change. `C0–C5` stays owned by `APPROVALS.md`; the `V` levels stay with the candidate Answer Verification Gate. The "Memory Candidate" name is retained where the corpus and `schemas/` are not yet migrated (later steps E2–E6; the schema rename is protected).

---

## 0.1.37 - 2026-06-07

self-inspect-mcp review and the Rite Trigger Catalogue candidate.

### Added

- `docs/governance/reference_reviews/SELF_INSPECT_MCP.md` — review of the deterministic metacognition prompter: distill the metathought pattern (a question, never a verdict; deterministic, no-LLM, drift-verified) to operationalize the rites; its founding premise (an agent cannot reliably self-correct) matches Pantheon's thesis; forbidden self-correction-loop / runtime import; Hermès-side or read-only MCP resource only.
- `docs/governance/rites/RITE_TRIGGER_CATALOGUE.md` — candidate / to verify: express the front edge of the rites as a deterministic `signal -> metathought question` catalogue (owned spec, served read-only externally), with a starter table mapped to existing rites and an execution target. A signal suggests a question; it never triggers a rite; ZEUS still decides; the rite budget and anti-chaining rules still apply.
- `ai_logs/2026-06-07-self-inspect-rite-trigger-catalogue.md` as the intervention trace.

### Changed

- `docs/governance/reference_reviews/README.md` and `docs/governance/rites/README.md` now index the new review and the catalogue candidate.

### Boundary clarification

Reference review and candidate direction only. No dependency, installation, runtime, MCP server, classifier, trigger engine, schema, test, served surface or protected-path change. The catalogue auto-triggers nothing and promotes no memory.

---

## 0.1.36 - 2026-06-07

External reference reviews: ASSERT and directory-mcp.

### Added

- `docs/governance/reference_reviews/ASSERT.md` — review of the spec-driven evaluation and regression-testing framework: distill the spec-to-executable-check and trace-grounded regression patterns (the "regression review for governance behavior" keeper); boundary that an LLM-judge verdict is a review signal, never truth, certainty, evidence or approval; Hermès-side under Task Contract.
- `docs/governance/reference_reviews/DIRECTORY_MCP.md` — review of the local MCP entity/identity directory: distill the graph schema (Entities / Anchors / Edges / Observations / Interactions) for the Registre Probatoire actor layer; the tool is a write-capable runtime memory kept Hermès-side under an MCP capability passport; Observations enter the register as Evidence Candidates, never canon or approval.
- `ai_logs/2026-06-07-assert-directory-mcp-reference-reviews.md` as the intervention trace.

### Changed

- `docs/governance/reference_reviews/README.md` now indexes the ASSERT and directory-mcp reviews.

### Boundary clarification

Reference reviews only. No dependency added, no installation approved, no runtime, MCP server, evaluation backend, memory engine, schema, test or protected-path change. Both projects are young; distill the pattern, do not depend on the tool.

---

## 0.1.35 - 2026-06-07

Memory becomes Hermès-owned; Pantheon governs the Registre Probatoire.

### Added

- `docs/governance/REGISTRE_PROBATOIRE_DIRECTION.md` as a validation-only direction record: "memory" is reserved to Hermès (free, self-evolving runtime memory via mem0 or another system, ungoverned); Pantheon governs the `Registre Probatoire` (the evidence register with certainty levels, exhibits, dates and citations) in place of "Canonical Memory". Captures the bridge rule (free memory may speak; only the register may be cited for consequential decisions), three orthogonal certainty axes (E0–E4 / V0–V4 / C0–C5, GLOSSARY-owned), the register entry fields, the corpus realignment list and a file-by-file execution checklist (steps E1–E6) for the executor, with a surgical rename map and a whole-effort acceptance gate.
- `ai_logs/2026-06-07-registre-probatoire-direction.md` as the intervention trace.

### Boundary clarification

Direction record only. No doctrine file rewritten, no schema, test or runtime added, no protected path touched. The schema rename and the corpus realignment are downstream work. Hermès memory remaining free does not make it authoritative; only the Registre Probatoire is probative, and only a human gate makes a consequential entry binding.

---

## 0.1.34 - 2026-06-07

Open PR reconciliation and integration plan.

### Added

- `docs/governance/OPEN_PR_RECONCILIATION.md` as a validation-only reconciliation trace: it takes stock of the recent merges and the ten open PRs (MCP, Pantheon Control, evidence/memory, governed composition, reference reviews), classifies them into clusters and a keystone, surfaces the cross-cutting risks (index contention, doctrine sprawl, C-scale collision, the separate-repo fork), lists the maintainer decisions needed and proposes a sequenced merge order.
- `ai_logs/2026-06-07-review-recent-merges-architecture.md` as the intervention trace.

### Changed

- `docs/governance/AUTHORITY_INDEX.md` now indexes the reconciliation trace.

### Boundary clarification

Documentation only. No schema, test, runtime, dashboard, MCP server, connector, scheduler, queue, approval engine, memory promotion or protected-path change. No open governance fork was decided; forks were surfaced for the maintainer.

---

## 0.1.33 - 2026-06-07

Green the Governance CI by widening the forbidden-phrase lint.

### Changed

- `.github/workflows/governance-ci.yml`: the forbidden-phrase lint now recognizes `Refused` as a negation token and `Impact queue` as a governed review surface. Seven pre-existing false failures (in `MCP_POLICY_SERVER_CANDIDATE.md`, `EVIDENCE_MEMORY_CANONICALIZATION.md`, `EVIDENCE_MEMORY_DEV_PLAN.md` and `reference_reviews/ELT_REFERENCE_REVIEW.md`) clear; the guard still fails on genuinely affirmative runtime-suggesting phrasing.

### Added

- `ai_logs/2026-06-07-green-governance-ci-lint-precision.md` as the intervention trace.

### Boundary clarification

CI workflow precision only. No doctrine wording changed. `.github/workflows/` is not a doctrine-protected path; no change under `schemas/`, `tests/`, `operations/`, `platform/`, `pyproject.toml`, Docker or `.env`.

---

## 0.1.31 - 2026-06-07

External runtime memory adapter boundary.

### Added

- `docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` as active support doctrine for external runtime memory, checkpoint, graph recall, observability and loop-detection adapters.
- `ai_logs/2026-06-07-external-runtime-memory-adapters.md` as the intervention trace.

### Changed

- `docs/governance/AUTHORITY_INDEX.md`, `docs/governance/MODULES.md` and `docs/governance/README.md` now index the generic external runtime memory adapter boundary.

### Boundary clarification

Documentation only.

No runtime, memory backend, vector store, graph database, checkpoint engine, observability backend, MCP server, connector, schema, test, operations tooling, platform component, Docker change, approval engine or automatic memory promotion was implemented.

Core rule:

```text
External runtime memory may store, recall, rank, summarize, checkpoint or trace.
It may propose Memory Candidates and Evidence Pack Candidates.
It must not promote Canonical Memory, validate truth, approve action, decide scope or authorize external effects.
```

---

## 0.1.30 - 2026-06-01

Request lifecycle doctrine (MÈTIS, the cap, memory gates).

### Added

- `docs/governance/REQUEST_LIFECYCLE.md` as active support doctrine: the governed lifecycle of a request. MÈTIS is a situated-comprehension role activated conditionally (only on fuzzy/indirect/implicit/contradictory/vague-but-consequential demands; a light triage decides, MÈTIS may be convened mid-course) that establishes the real demand, the goal (the cap), the watch-points and the responsibility limit, and holds and re-reads the cap. The cap lives in the Task Contract; re-evaluation is a governed revision. Zeus arbitrates the cap (validated / back to MÈTIS to deepen / routed to human), with a bounded loop and framing-not-engagement separation. Cerbère and Charon are memory-threshold gates (filter what returns from the past; archive what must stop acting), not judges. Distinct natures: roles vs gates vs runtime vs human.
- `ai_logs/2026-06-01-request-lifecycle-metis.md` as the intervention trace.

### Changed

- `docs/governance/MODULES.md` and `docs/governance/AUTHORITY_INDEX.md` now index the request lifecycle.

### Boundary clarification

Documentation only — governance moments, not an execution pipeline. No runtime, scheduler, message bus, workflow engine, orchestration loop, automatic approval or automatic memory promotion. Promoting MÈTIS into the canonical role registry (`AGENTS.md`, `GOVERNANCE_COLLEGE.md`) and the gates into `MEMORY.md` / `CORE_RECORDS_MODEL.md` is a separate governed step.

```text
MÈTIS understands and holds the cap, when the demand is unclear.
ZEUS arbitrates the status, on evidence.
The human decides at the cliffs and engages.
```

---

## 0.1.26 - 2026-06-01

Optimize and de-duplicate the governance index files (STATUS.md and README.md).

### Changed

- `docs/governance/STATUS.md` reduced from 368 to ~75 lines. It no longer mirrors the full document listing, the read path or the per-doctrine summaries. It now records posture, the migration rule, a single boundary statement, and a `Live exceptions` table for candidate / to-verify items, with precedence rules pointing to the authoritative indexes.
- `docs/governance/README.md` reduced from 637 to ~150 lines. It is now the entry point and read path only. The two exhaustive document listings and the ~13 per-doctrine "boundary" sections were removed (each duplicated `STATUS.md`, `AUTHORITY_INDEX.md`, `MODULES.md` or the source doc itself). README now carries one consolidated boundary statement and a thematic read path, and delegates enumeration/classification with explicit precedence rules.

### Ownership (who owns what)

- `README.md` — entry point and read path.
- `STATUS.md` — posture and live exceptions.
- `AUTHORITY_INDEX.md` — authority class and status of each item.
- `MODULES.md` — module map per governance area.

### Boundary clarification

Documentation only. No doctrine removed in substance; redundant restatements consolidated and enumeration delegated. No runtime, schema, test or executable change. CI checks verified locally (no stub section; queue/scheduler lint clean on README, STATUS and AUTHORITY_INDEX).

---

## 0.1.24 - 2026-06-01

AgentOS external reference review.

### Added

- `docs/governance/reference_reviews/AGENTOS.md` as an external reference review for runtime boundary vocabulary, memory review signals and claim review;
- `ai_logs/2026-06-01-agentos-reference-review.md` as the intervention trace.

### Boundary clarification

Documentation and reference review only.

It does not implement a runtime, generated capability execution, provider routing, scheduler, queue, OpenWebUI extension, Hermes skill, schema change, test, operations tooling, automatic approval or automatic memory promotion.

---

## 0.1.23 - 2026-05-31

Modular domain reorientation reconciliation (#25) and governance indexing.

### Changed

- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md` now uses abstract role names in the body, tables and diagram, confines product names to the bindings registry (with an explicit bindings/adapters exception), reconciles the module manifest `status` with `MODULE_ACTIVATION.md` (status, activation and task authorization as three separate axes), adds a hierarchy note that it reconciles rather than replaces existing doctrine, and clarifies that a domain pack is a governed methodology configuration, not an executable runtime module;
- `docs/governance/ADAPTERS_AND_BINDINGS.md` now records that it is part of the bindings and adapters naming exception;
- `docs/governance/STATUS.md`, `docs/governance/README.md`, `docs/governance/MODULES.md` and `docs/governance/CORE_CONCEPTS_MAP.md` now index `MODULAR_DOMAIN_REORIENTATION.md`, `ADAPTERS_AND_BINDINGS.md`, `CAPABILITY_PLACEMENT.md`, `ARCHITECTURE_AGENCY_DOMAIN_PACK.md`, `KNOWLEDGE_INGESTION_AND_MEMORY.md` and `WORKFLOW_LIFECYCLE.md` in the read path.

### Added

- `ai_logs/2026-05-31-modular-domain-reorientation-reconciliation.md` as the intervention trace;
- `ai_logs/2026-05-31-data-platform-boundary-review.md` as the data-platform boundary-review trace.

### To verify

- `DATA_PLATFORM_ARCHITECTURE.md`, `DATA_PLATFORM_INDEX.md` and `DATA_PLATFORM_STATUS.md` are indexed with a `to verify` status, pending a boundary review against `CLAUDE.md`. Indexing does not endorse them as canonical; a data platform must not become a Pantheon runtime.

### Data platform boundary review (#30)

- `DATA_PLATFORM_ARCHITECTURE.md`: `Directus exposes and controls` → `Directus exposes controlled records`; the deployment section is reframed as `Candidate deployment profiles outside Pantheon` with a no-authorization disclaimer; table families are marked conceptual registry families, not approved schema; an adapter/binding status note is added.
- `ARCHITECTURE_AGENCY_DOMAIN_PACK.md`, `KNOWLEDGE_INGESTION_AND_MEMORY.md` and `WORKFLOW_LIFECYCLE.md` are realigned to `candidate / to verify` in `STATUS.md`, `README.md` and `MODULES.md` to match their own headers and the #30 boundary review.
- `DATA_PLATFORM_RECONCILIATION.md` (added to `main` as candidate reconciliation doctrine) is indexed in `STATUS.md`, `README.md` and `MODULES.md`.

### Not included

AgentOS distillation (Issue #27) is intentionally out of scope and left to its own change.

### Boundary clarification

Documentation and indexing only.

It does not implement a runtime, a bridge, a plugin manager, a skill installer, a module registry runtime, an executable schema, automatic approval or automatic memory promotion.

Central rule:

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```

---

## 0.1.22 - 2026-05-31

Adapters and bindings support doctrine.

### Added

- `docs/governance/ADAPTERS_AND_BINDINGS.md` as active support doctrine for the blueprint-in-Pantheon and adapter-outside model, defining where tool-specific templates and configurations live (OpenWebUI, Hermes, Langfuse and others) and the four disciplines that keep them adapted to Pantheon without coupling Pantheon to any tool;
- `ai_logs/2026-05-31-adapters-and-bindings.md` as the intervention trace.

### Boundary clarification

This release documents a configuration-placement model only.

It does not implement a configuration, an OpenWebUI Function, a Hermes skill, a Langfuse project, a runtime, a bridge or any executable artifact.

Central rule:

```text
The blueprint lives in Pantheon.
The adapter lives in the tool.
The dependency always points to Pantheon.
The validated remains.
```

---

## 0.1.21 - 2026-05-31

Modular domain reorientation coordination artifact.

### Added

- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md` as active support doctrine for tool-agnostic placement, the modular capability contract (manifest plus envelope) and the domain-pack projection model, including a bindings registry, the placement test, the complete module manifest shape, the domain-pack section-to-layer table and a Mermaid diagram;
- `ai_logs/2026-05-31-modular-domain-reorientation.md` as the intervention trace.

### Boundary clarification

This release documents a coordination and placement model only.

It does not implement a runtime, a bridge, a plugin manager, a skill installer, a module registry runtime, a domain-pack worker, an OpenWebUI Function, a Hermes skill, an executable schema, automatic approval or automatic memory promotion.

The complete manifest is recorded as a shape only. A canonical executable schema under `schemas/` requires explicit approval before being added.

Central rule:

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```

---

## 0.1.20 - 2026-05-31

SOUL.md Hermes profile identity boundary review and integration.

### Added

- `docs/governance/reference_reviews/SOUL_MD_HERMES_PROFILE.md` as a support review and pattern card for SOUL-like identity layers in Hermes profiles;
- `Profile identity layer` entry in `docs/governance/DISTILLATION_REGISTRY.md` with status `hermes_candidate_constraint`.

### Changed

- `docs/governance/HERMES_INTEGRATION.md` now defines the allowed and forbidden use of SOUL-like Hermes profile identity layers;
- `docs/governance/reference_reviews/README.md` now indexes the SOUL.md review.

### Boundary clarification

This release documents profile identity governance only.

It does not install `SOUL.md`, modify Hermes runtime behavior, deploy profiles, create Pantheon Roles, authorize tool use, approve outputs, promote memory, create a profile marketplace, add a plugin manager or create runtime behavior inside Pantheon Next.

Central rule:

```text
A SOUL-like file may stabilize how Hermes executes.
It must never decide what Pantheon validates.
```

---

## 0.1.19 - 2026-05-30

Evidence Topology doctrine, examples and index reconciliation.

### Added

- `docs/governance/EVIDENCE_TOPOLOGY_GATE.md` as active doctrine for reasoning topology selection, proof-chain preservation, persistent role-team handoff and bounded Hermes swarm constraints;
- `docs/governance/EVIDENCE_TOPOLOGY_ROADMAP.md` as a roadmap addendum for single-context, fan-out extraction, role-team handoff and swarm boundaries;
- `docs/governance/EVIDENCE_TOPOLOGY_RECONCILIATION.md` as a safe reconciliation note for index and status alignment;
- `docs/governance/EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md` as a non-executable schema candidate note, without modifying `schemas/`;
- `docs/governance/EVIDENCE_TOPOLOGY_BRIDGES.md` to link the doctrine to Task Contracts, Evidence Packs, Hermes, OpenWebUI, memory, scope, tools, Governance College and User Decision Gate;
- `docs/governance/EVIDENCE_TOPOLOGY_CHECKLIST.md` as a practical checklist for selecting topology;
- `docs/governance/evidence_topology_antipatterns/` with support cards for summary-only handoff, swarm as authority, role memory as Canonical Memory, conductor as ZEUS and canvas as Evidence Pack;
- `docs/examples/evidence_topology/` with fictional Task Contract and Evidence Pack examples;
- `docs/examples/architecture_devis_reprise/EVIDENCE_TOPOLOGY_EXAMPLE.md` as a fictional architecture / MOE topology example.

### Changed

- `README.md` and `README.fr.md` now explain Evidence Topology in public-facing language and link to the gate and checklist;
- `docs/governance/STATUS.md` now records Evidence Topology as active doctrine;
- `docs/governance/README.md` now indexes Evidence Topology in the read order, document lists and boundary section;
- `docs/examples/README.md` now indexes the `evidence_topology/` example folder.

### Boundary clarification

This release documents governance and examples only.

It does not implement a topology router, scheduler, queue, worker dispatcher, graph runtime, swarm controller, OpenWebUI plugin, Hermes configuration, automatic approval, automatic memory promotion, schemas, tests, operations tooling, platform files, Docker changes or environment configuration.

Central rule:

```text
The unit of reasoning is not the agent.
The unit of reasoning is the proof chain.
```

Operational boundary:

```text
Swarm for collection.
Role-team handoff for bounded artifact stages.
Single context for inference when evidence must connect.
Governance College for review.
User Decision Gate for unresolved stakes.
Human decision for consequential approval.
```

---

## 0.1.18 - 2026-05-30

Core concepts map and doctrine navigation consolidation.

### Added

- `docs/governance/CORE_CONCEPTS_MAP.md` as active navigation doctrine for Pantheon core concepts and relationships;
- compact object map for Task Contracts, Context Packs, Evidence Packs, approvals, memory, roles, rites, domain packs, skill candidates, modules, Effective Policy, OpenWebUI Templates, User Decision Gates, external tools and reference reviews;
- authority ladder separating source, evidence, approval, Memory Candidate and Canonical Memory;
- execution ladder separating Task Contract, Context Pack, Hermes execution, candidate return, Pantheon review and OpenWebUI exposure;
- high-risk shortcut list to reject concept collapses such as `retrieved = evidence`, `schema valid = approved`, `Nango connection = authorized external action` or `OpenWebUI Function = Pantheon runtime`.

### Changed

- `docs/governance/README.md` now indexes `CORE_CONCEPTS_MAP.md`, adds a short stable reading path and records the core concepts boundary;
- `README.md` now links to `CORE_CONCEPTS_MAP.md` from the public vocabulary section and key entry points;
- `docs/governance/STATUS.md` now tracks the core concepts map as active navigation doctrine and records the associated non-runtime boundary and risk.

### Boundary clarification

This release documents navigation support only.

It does not implement a schema, runtime model, workflow engine, module registry, plugin manager, approval engine, memory engine, OpenWebUI UI, Hermes integration, tests, operations tooling, automatic approval or automatic memory promotion.

Central rule:

```text
Every concept has one job.
Every promotion requires governance.
Every external action requires a boundary.
Every unresolved tension must remain visible.
```

---

## 0.1.17 - 2026-05-30

Public and governance index reconciliation.

### Changed

- `README.md` now reflects the reconciled declarative schema baseline, first read-only schema validation test, RAG evidence-boundary doctrine and current fictional example set;
- `README.fr.md` now mirrors the same public status and example updates in French;
- `docs/governance/README.md` now indexes Nango, Future AGI and the connector gateway boundary, and no longer states that tests are entirely absent;
- `docs/governance/STATUS.md` now records Nango support doctrine, Future AGI support doctrine, connector/reliability non-implementation boundaries and related risks;
- `docs/governance/ROADMAP.md` now records Nango/Future AGI support doctrine, current examples, first read-only schema test coverage and future connector/reliability read-only consistency checks.

### Clarification

The historical `0.1.11` entry remains accurate for the moment it was written: the Phase D1 schema baseline was not yet backed by tests at that time.

The current repository state is later than that entry and now includes a first read-only schema validation test file.

### Boundary clarification

This release documents public-index and governance-index reconciliation only.

It does not implement connector runtime, credential storage, OAuth provider configuration, Future AGI installation, observability backend, simulation runtime, provider gateway, broad test suite, CI coverage, read-only operations tooling, automatic approval or automatic memory promotion.

Central rule:

```text
Indexes describe the current doctrine surface.
They do not install, execute, validate or approve anything by themselves.
```

---

## 0.1.16 - 2026-05-29

Understand-Anything graph authority boundary lock.

### Changed

- `docs/governance/UNDERSTAND_ANYTHING_HERMES_ADAPTER.md` now links to the fictional structural-analysis examples;
- `docs/governance/REJECTED_PATTERNS.md` now explicitly rejects generated repository graphs as architecture truth;
- `docs/governance/TENSIONS_AND_RISKS.md` now records repository radiography vs graph authority as a persistent governance tension.

### Boundary clarification

This release documents rejection memory and tension preservation only.

It does not implement graph analysis, GraphRAG runtime, repository graph validation, automatic enforcement, runtime blocking, OpenWebUI plugin behavior, Hermes skill installation, repository automation, tests or operations tooling.

Central rule:

```text
A graph may reveal structure.
It does not validate structure.
It does not approve architecture.
It does not create memory.
```

---

## 0.1.15 - 2026-05-29

RAG evidence-boundary reconciliation across status, roadmap and ingestion doctrine.

### Changed

- `docs/governance/STATUS.md` now indexes `RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md`, records RAG evidence-boundary doctrine and explicitly marks RAG runtime, retrieval runtime, chunking runtime, benchmark runner, scoring backend and OpenWebUI Knowledge mutation as not implemented;
- `docs/governance/ROADMAP.md` now lists `RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` in active doctrine, adds a RAG evidence-boundary section and includes future read-only RAG evidence-boundary consistency checks;
- `docs/governance/RAG_INGESTION_PIPELINE.md` now aligns its doctrine chain with `RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` by adding `Ingestion Candidate`, `Chunk / Retrieval Unit` and `Context Sufficiency Check`.

### Boundary clarification

This release documents reconciliation only.

It does not implement RAG runtime, retrieval runtime, chunking runtime, benchmark runner, scoring backend, OpenWebUI Knowledge mutation, Hermes ingestion worker, tests, operations tooling, automatic approval or automatic memory promotion.

Central rule:

```text
RAG ingestion can prepare sources.
RAG evidence boundaries decide what the preparation means.
Neither creates proof, approval or memory by itself.
```

---

## 0.1.14 - 2026-05-29

Understand-Anything structural-analysis fictional examples.

### Added

- `docs/examples/understand_anything_structural_analysis/README.md` as a non-executable example index;
- `docs/examples/understand_anything_structural_analysis/TASK_CONTRACT_STRUCTURAL_ANALYSIS.md` as a fictional `STRUCTURAL_ANALYSIS` Task Contract example;
- `docs/examples/understand_anything_structural_analysis/EVIDENCE_PACK_CANDIDATE.md` as a fictional Evidence Pack Candidate example for external structural-analysis output.

### Changed

- `docs/examples/README.md` now indexes the Understand-Anything structural-analysis example.

### Boundary clarification

These examples are fictional and educational only.

They do not implement Understand-Anything, install Hermes skills, create command syntax, create repository hooks, commit generated graph artifacts, approve graph output, create GraphRAG runtime, create Canonical Memory or authorize repository mutation.

Central rule:

```text
The graph may help review the repository.
It does not decide what the repository is.
It does not approve what should change.
It does not remember anything by itself.
```

---

## 0.1.13 - 2026-05-29

Rites governance layer.

### Added

- `docs/governance/rites/README.md` as the index for shared governance rites;
- `docs/governance/rites/_TEMPLATE_RITE.md` as a rite documentation template;
- `docs/governance/rites/RITE_DIVERGENCE_CONTROLEE.md` for divergent option exploration before convergence;
- `docs/governance/rites/AUTOCRITIQUE_CONTRADICTOIRE.md` for structured post-draft contradiction;
- `docs/governance/rites/CONCORDANCE_DES_SOURCES.md` for source comparison and claim support review;
- `docs/governance/rites/PREMISSES_CACHEES.md` for implicit assumption extraction;
- `docs/governance/rites/REFONDATION_DE_SESSION.md` for controlled reset when session context becomes polluted.

### Changed

- `docs/governance/README.md` now indexes the Rites layer and active rite documents;
- `ai_logs/2026-05-29-rites-governance-layer.md` records the intervention, rationale, boundary and limitations.

### Boundary clarification

Rites are documentation-level governance procedures.

They do not implement a runtime, scheduler, queue, provider router, tool runtime, hidden debate system, OpenWebUI plugin, Hermes skill installation, automatic approval or automatic memory promotion.

Central rule:

```text
Roles judge.
Rites coordinate.
Task Contracts bound.
Evidence Packs prove.
ZEUS states procedure.
The human decides.
```

---

## 0.1.12 - 2026-05-29

Understand-Anything external reference review and Hermes Skill Candidate boundary.

### Added

- `docs/governance/reference_reviews/UNDERSTAND_ANYTHING.md` as an external reference review for Understand-Anything, Hermes Agent and Hermes Desktop boundary classification;
- `docs/governance/UNDERSTAND_ANYTHING_HERMES_ADAPTER.md` as support doctrine for a non-implemented Hermes-side structural analysis skill candidate;
- Understand-Anything watch record in `docs/governance/SKILL_WATCHLIST.md`;
- Understand-Anything reference review index entry in `docs/governance/reference_reviews/README.md`.

### Changed

- `docs/governance/README.md` now indexes the Understand-Anything reference review and Hermes adapter support doctrine;
- `docs/governance/STATUS.md` now tracks Understand-Anything support doctrine, Hermes Desktop non-adoption and the explicitly absent implementation areas.

### Boundary clarification

This release documents governance support only.
