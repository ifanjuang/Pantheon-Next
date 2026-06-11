# Changelog

## 0.1.51 - 2026-06-12

Governed execution handoff boundary and architecture / urbanisme example.

### Changed

- `docs/governance/CAPABILITY_PLACEMENT.md` gains a governed execution handoff section: minimum handoff shape, effect classes, preflight outcomes, Capability Gap shape, idempotency discipline, Outcome Observation Candidate and rejected collapses. The section stays non-runtime and clarifies that delivery, runtime success and governance approval are separate states.
- `docs/examples/README.md` indexes the new architecture / ABF handoff example and updates example wording to Registre vocabulary.

### Added

- `docs/examples/architecture_abf_handoff/README.md` as a fictional architecture / urbanisme vertical: mairie / ABF reply preparation through Task Contract, Context Pack, Decision Gate, governed handoff, invalid handoffs, Capability Gaps, runtime return and Outcome Observation Candidate.
- `ai_logs/2026-06-12-governed-execution-handoff.md` as the intervention trace.

### Boundary clarification

Documentation and fictional example only. No runtime bridge, OpenWebUI Action, Hermes skill, MCP change, schema, test, operation file, Docker change, `.env` change, queue, scheduler, provider router, approval engine or memory promotion. The handoff is documented non-implemented and remains candidate support until reviewed.

---

## 0.1.50 - 2026-06-10

CHANGELOG rotation: archive older entries to keep the active file editable.

### Changed

- `CHANGELOG.md` now keeps the recent versions (0.1.42 and later); entries 0.1.41 and earlier move to `CHANGELOG_ARCHIVE.md`. The active changelog had reached 775 lines / 32 versions, too long for reliable editing through the connector; rotation keeps it short. No history is lost.

### Added

- `CHANGELOG_ARCHIVE.md` holding versions 0.1.12 -> 0.1.41.
- `ai_logs/2026-06-10-changelog-rotation.md` as the intervention trace.

### Boundary clarification

Documentation housekeeping only. No doctrine, schema, test or protected-path change. CI checks that `CHANGELOG.md` exists; it still does.

---

## 0.1.49 - 2026-06-09

Make the consequential chokepoint explicit (the rule that makes Pantheon master).

### Changed

- `docs/governance/HERMES_INTEGRATION.md` gains a "Consequential effects route through Pantheon — the chokepoint" section: before a consequential effect, Hermès (the PEP) asks Pantheon's policy check (the PDP) and proceeds only on allow / allow_with_gate, under the capability passport's required envelope; non-consequential effects proceed freely; the decision is data, not execution; a bypass makes Pantheon master only in advice; no per-capability rule is added. Wiring lives in the runtime (Phase 3), outside Pantheon.
- `docs/governance/REQUEST_LIFECYCLE.md` gains a short "The consequential chokepoint" cross-reference (the lifecycle decides what is consequential; the chokepoint decides whether it may proceed; neither runs the work).

### Added

- `ai_logs/2026-06-09-chokepoint-enforcement-rule.md` as the intervention trace.

### Boundary clarification

Documentation only. No runtime, schema, test, policy engine or protected-path change; enforcement lives in the execution runtime honouring the check. Closes the target-architecture Gap #1 in doctrine.

---

## 0.1.48 - 2026-06-09

Target Architecture coherence compass.

### Added

- `docs/governance/TARGET_ARCHITECTURE.md` (validation-only): one compass for a coherent end-to-end system — the layered PDP/PEP picture (surface / law / execution / proof / observability) with per-layer reality state; the absorption map (which external pattern fills which slot: PDP-PEP & OPA for the gate, in-toto/SLSA for signed proof, Backstage for Control, TUF for install/update, directory-mcp / ASSERT / self-inspect / SkillsGate / CBR for their slots); the ranked coherence gaps (the gate is not enforced; no Registre; no validator; no proven vertical); the sprawl to consolidate; and the sequence (name+enforce the chokepoint → harden the spine → wire proof/observability → prove one vertical → consolidate).
- `ai_logs/2026-06-09-target-architecture-coherence-compass.md` as the intervention trace.

### Changed

- `docs/governance/AUTHORITY_INDEX.md` indexes the compass.

### Boundary clarification

Direction record only. No runtime, schema, test, installer, policy engine or protected-path change. It maps the target; it instantiates none of it.

---

## 0.1.47 - 2026-06-09

Uniform Capability Governance keystone.

### Added

- `docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md` as active support doctrine: one rulebook, one passport per capability, no per-module rules; consequential effects route through an unbypassable gate. The runtime honouring the gate is what makes Pantheon master (not where code lives). Frames the architecture as PDP/PEP (Pantheon = decision point, Hermès = enforcement point, OpenWebUI = surface, Control = eyes and hands), with PDP/PEP, OPA/Gatekeeper, in-toto/SLSA and Backstage cited as distilled external grounding. Unifies the capability passport, the two gates and the placement test.
- `ai_logs/2026-06-09-uniform-capability-governance.md` as the intervention trace.

### Changed

- `docs/governance/AUTHORITY_INDEX.md`, indexes the keystone.

### Boundary clarification

Documentation only. No runtime, scheduler, queue, provider router, policy engine, installer or MCP host inside Pantheon Next; enforcement lives in the execution runtime honouring the gate. Coordinates existing canonical doctrine; does not replace it. The cross-reference reconciliation of the activation/lifecycle/tool docs and the Pantheon Control reframe are follow-ups.

---

## 0.1.46 - 2026-06-08

CI guard against Registre Probatoire vocabulary regression.

### Changed

- `.github/workflows/governance-ci.yml`: `checkout` now fetches full history, and a new `pull_request`-only step fails when a PR *adds* a line under `docs/` containing `Canonical Memory` or `Memory Candidate` (the deliberate "formerly / in place of" notes are allowed). It diffs against the PR merge base, so existing not-yet-swept occurrences do not trip it and sweep PRs that remove the terms pass. Boundary phrases such as "automatic memory promotion" are unaffected. This locks in the rename now that the corpus-wide sweep (issue #90) has landed.

### Added

- `ai_logs/2026-06-08-ci-vocabulary-regression-guard.md` as the intervention trace.

### Boundary clarification

CI workflow precision only. No doctrine, schema, test or protected-path change. The guard adds no runtime; it only prevents vocabulary regression on pull requests. Verified locally against a real diff; YAML parses.

---

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

Older entries (0.1.41 and earlier) are archived in [CHANGELOG_ARCHIVE.md](CHANGELOG_ARCHIVE.md).
