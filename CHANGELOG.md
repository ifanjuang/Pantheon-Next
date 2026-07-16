# Changelog

## 0.1.61 - 2026-07-05

Release status correction (2026-07-15): this heading records a repository and
MCP-package checkpoint, not a published GitHub release. No repository tag was
present when the packaging contract was verified. `VERSION` is now the single
authoritative marker; MCP metadata and this heading mirror it under CI. A future
published release must use a matching `v<VERSION>` tag.

Full repository audit lands with the latent guard-debt purge and the first governance cleanup: `docs/governance/` drops from 241 to 167 documents.

### Removed

- **Governance cleanup, passes A and B** (approved plan: standard scope, removal + mapping log, ARBITRAGE list untouched): 61 spent documents removed (17 obsolete tombstones, 36 one-shot external reference reviews, 8 one-shot reconciliation/landing documents) and 13 satellite documents absorbed verbatim into their mother document (`EXTERNAL_TOOLS_POLICY.md`, `HERMES_INTEGRATION.md`, `OPENWEBUI_INTEGRATION.md`, `CARD_STACK_MODEL.md`, `DATA_PLATFORM_ARCHITECTURE.md`). Every reference is rewritten; full mappings in `ai_logs/2026-07-07-governance-cleanup-pass-a.md` and `ai_logs/2026-07-07-governance-cleanup-pass-b.md`; `STATUS.md` gains a one-line historical record per removed reconciliation.

### Added

- `docs/audits/2026-07-04-analyse-complete-repository.md` — complete, strict external audit of `main` at `3375fcb` (test-suite and guard execution, CI failure rate, release-tag invariant gap, latent guard debt, candidate-queue load, hygiene), with prioritized recommendations. Trace in `ai_logs/`.
- `templates/hermes/dashboard-plugins/pantheon-modules/` — installable external
  Hermes dashboard-plugin template that inventories memory providers, MCP
  servers/catalog entries and plugins through native authenticated APIs. It
  preserves separate install/configuration/enablement/liveness/governance/task
  states, adds explicit confirmation for Hermes mutations and records cautious
  placements for Mem0, n8n, LangGraph, Memvid and the Pantheon policy MCP.
- `templates/hermes/dashboard-plugins/pantheon-modules/night-operations.template.yaml`
  and the dashboard `Night ops` view — ordered, finite-trial proposals for
  backup preflight, PDF ingestion/vectorization, retrieval quality, memory
  consolidation review, contradiction/drift review and a local morning digest.
  Schedule creation and deletion remain outside the plugin. For one existing,
  unambiguous finite job, separately confirmed controls can pause/resume,
  retime it while paused and request one immediate run while enabled.

- `docs/assets/pantheon-control/hermes-modules.html` — GitHub Pages
  demonstration running the exact native Hermes plugin JavaScript and CSS
  renderer through a synthetic, read-only SDK harness. Generated preview assets
  are byte-for-byte guarded against the installable bundle; every mutation is
  disabled and all six bounded night-operation examples remain paused.
- The Pantheon Control preview and installable Hermes dashboard plugin now share
  the `control-v1` visual contract: design tokens, hero, toolbar, cards, badges,
  nine-state grid and responsive behavior. Because the public preview executes
  the exact generated plugin bundle, its existing byte-for-byte guard also
  prevents visual drift while preserving separate data and action boundaries.

### Fixed

- The Hermes Modules preview now resolves its synthetic fixture from the page directory, reports demo failures as demo failures, and presents governed night operations in operator-friendly French with raw Cron and native identifiers folded into technical details.
- **16 latent guard violations purged** (they were grandfathered by the 2026-06-11 diff-scoped baseline and invisible in CI):
  - internal links ×4: two references to never-created documents reworded as name-only mentions (`reference_reviews/COGNICORE_RUNTIME_REVIEW.md`, `reference_reviews/PYTHIA_GOVERNANCE_STATE_REVIEW.md`); two `docs/...` git branch names in `OPEN_BRANCH_LANDING_PLAN.md` reworded so they no longer parse as repository paths.
  - index coverage ×4: `MISSING_INFORMATION_DISCIPLINE.md`, `WORKFLOW_DEPTH_POLICY.md`, `CARD_STACK_KNOWLEDGE_CORPUS_ALIGNMENT.md` and `METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md` are now indexed in `AUTHORITY_INDEX.md` as candidate entries.
  - axis vocabulary ×8: the `confidence` fields of `role_signal` and `evidence_pack` (schema + examples + topology examples) are explicitly marked as legacy, superseded by the certainty axis, per the `register_candidate` precedent; two `approval_impact` example values no longer mix the C-axis into an approval context.
- **Full-tree CI switch prepared as a maintainer action**: with the baseline debt purged, the `GOVERNANCE_BASE_REF` grandfathering can be removed for the five tree checks (`check_no_net_truncation` keeps the base ref — it is a diff check by nature). The exact patch is recorded in `ai_logs/2026-07-05-guard-debt-purge-and-full-tree-ci.md`. It is deliberately not applied by this PR: pushes touching `.github/workflows/` from the automated session cause GitHub to stop creating CI runs for the PR, so the workflow edit stays a maintainer action, consistent with the protected-path rule.

### Changed

- Governed night-operation cards are compact by default and reveal their state grid, activation conditions, technical data and native Hermes controls in place; only one card remains open at a time.
- `VERSION`, the former root package metadata and `mcp-server/pyproject.toml` were bumped to `0.1.61`. The root metadata was later removed because the repository root is not a Python distribution. No tag is claimed for this checkpoint; the earlier tag instruction is superseded by the release status correction above.

### Boundary clarification

Protected `schemas/` + CI change (authorized maintainer request). Descriptions, comments and index rows only — no schema contract change (no field added, removed or renamed; enums intact), no runtime, approval engine or memory promotion. Full `tests/` suite green (12 passed), mcp-server suite green (122 passed), all guards green full-tree.

---

## 0.1.60 - 2026-07-01

Governed composition schema fields land on main, with complete step signatures and a conditional evidence gate (#218).

### Added

- `schemas/workflow_manifest.schema.yaml` gains the optional `governed_composition` object (validation metadata only) — re-landing the fields stranded when PR #53 closed, aligned to the composition doctrine already on `main`: `forged_by`/`forge_status`, `composition_loop`, `capability_steps` and the two `gates` (ZEUS pre-execution eligibility; post-execution evidence with `answer_verification` V0–V4 and `probative_certainty` E0–E4).
- `docs/examples/governed_composition_cerfa/` and `docs/examples/governed_composition_marche_public/` — fictional end-to-end and reuse examples; `schemas/README.md`, `docs/governance/CAPABILITY_REGISTRY.md` and `docs/examples/README.md` updated.
- `tests/test_schema_examples.py` gains negative tests for the block (incomplete step signature, required-evidence gate missing V/E, bad gate-decision enum).

### Changed

- **Complete step signatures**: a `capability_step` now requires its full governance signature (`declared_scope`, `forbidden_scope`, `required_task_contract`, `evidence_pack_shape`, `approval_ceiling`, `register_behavior`, `risk_class`, `refusal_tests`); `skill_manifest_ref` and `depends_on` stay optional. A step can no longer be declared with a partial, unreviewable signature.
- **Mandatory V/E when evidence is required**: when `post_execution_evidence.required` is `true`, `answer_verification` and `probative_certainty` become required (JSON Schema `if/then`); when it is `false` they may be omitted.
- `VERSION`, `pyproject.toml` and `mcp-server/pyproject.toml` bumped to `0.1.60` to keep the B-7 invariant (VERSION = CHANGELOG head = pyproject version).

### Boundary clarification

Protected `schemas/` + `tests/` change (authorized). Structure only — no forge engine, dispatch, scheduling or memory promotion. `forged != authorized`; `completed != approved`; `returned != a Registre Probatoire entry`. Full `tests/` suite green (12 passed); governance guard clean.

---

## 0.1.59 - 2026-07-01

Realign `VERSION` with the CHANGELOG head (arbitration B-7).

### Fixed

- `VERSION` was stuck at `0.1.0` while the CHANGELOG had reached `0.1.58`, contradicting a project whose thesis is status honesty (flagged by the #246 audit). It was set to `0.1.59` and the then-present package markers were aligned. Status correction (2026-07-15): no `v0.1.59` tag was published, so this heading is a repository checkpoint, not a release claim; the current packaging contract supersedes the former mandatory-tag invariant.

### Boundary clarification

Metadata realignment only. No doctrine, schema, test, `mcp-server/`, runtime or other protected-path change. Status correction (2026-07-15): the previously stated `v0.1.59` tag was not created.

---

## 0.1.58 - 2026-06-30

Unblock CI: reword the affirmative "landing queue" so the runtime-phrase guard passes.

### Fixed

- The `runtime_phrases` governance guard was red on `main`: affirmative uses of `queue` (a branch/PR landing order, not a runtime queue) in two planning docs, flagged in both `Read-only governance checks` and the mcp-server doctor's blocking check.
  - `docs/governance/REPOSITORY_CONSOLIDATION_LANDING_PLAN.md`: reworded the concept "landing queue" → "landing sequence" (4 affirmative occurrences; lines 217 and 540 were the flagged ones).
  - `docs/governance/OPEN_BRANCH_LANDING_PLAN.md`: reworded the `## Current queue` heading → `## Current landing sequence` (line 51).
  - Negation uses ("does not create … a queue") are left intact. Verified by running the guard locally against the full tree → 0 violations. Semantics preserved; no doctrine altered.

### Boundary clarification

Documentation wording only. No schema, test, `mcp-server/`, runtime or other protected-path change. The fix aligns the document with the guard rather than weakening the guard.

---

## 0.1.57 - 2026-06-26

MODULES.md: index the runtime-review validation promotion and repair a truncation.

### Changed

- `docs/governance/MODULES.md` adds the canonical-module-map row for `RUNTIME_REVIEW_MODEL_PASSPORT_VALIDATION_PROMOTION.md` (status `to_verify`: validation-only promotion proposal; modifying `schemas/`, `tests/` and `mcp-server/` stays blocked pending explicit approval). `AUTHORITY_INDEX.md` already indexed it and is unchanged.

### Fixed

- `docs/governance/MODULES.md` was truncated by commit `37c51c4` (481 → 302 lines), which had dropped the narrative tail from the Approval module body through the Final rule. Restored verbatim from the last complete version (`9d6cdb7`, which already carries the current Registre Probatoire vocabulary); the restored tail is byte-identical, no section is duplicated, and all current table rows are preserved (302 → 525 lines).

### Added

- `.github/scripts/check_no_truncation.py` and a step in `governance-ci.yml`: a CI tripwire that fails the build if a curated long governance file (`MODULES.md`, `AUTHORITY_INDEX.md`) drops below a minimum line count or loses its end-sentinel — so a future truncation cannot land silently. Read-only; reports, never edits.
- `ai_logs/2026-06-26-modules-index-runtime-review-and-truncation-repair.md` as the intervention trace.

### Boundary clarification

Documentation reconciliation plus a read-only CI guard. No doctrine authored or altered — the lost content was recovered from git history; one index row was added. No schema, test, mcp-server, runtime or protected-path change (`.github/` is CI infrastructure). Governance lint clean; the guard self-tested (passes on the repaired tree, fails on a simulated truncation).

---

## 0.1.55 - 2026-06-14

Promote register-instance validation into the doctor as a single source of truth.

### Added

- `mcp-server/pantheon_mcp/doctor.py` gains `check_register_instances` (read-only): validates each Registre Probatoire instance under `docs/examples/cascade_register/` against its schema (`register_candidate`, `register_link`, `impact_review`), verifies `link_ids` referential integrity, and applies the cascade rule via `evaluate_impact_review`. Added to `run_all`, so Hermes, OpenWebUI or the dashboard can ask "are register instances coherent?" without running CI. `mcp-server/tests/test_cascade_doctor.py` covers it (3 new tests, 8 total).

### Changed

- `.github/scripts/check_register_instances.py` now imports and runs `check_register_instances` from the doctor instead of reimplementing schema loading, referential integrity and the cascade rule. The doctor is the single source of truth; CI mirrors it.

### Removed

- `tmp_should_not_create.txt`: a stray test artifact that was accidentally committed and merged. It is not governance, schema, validation or documentation.

### Boundary clarification

The doctor flags, cites and reports; it never edits, fixes or decides. No runtime, scheduler, queue, provider router, approval engine, memory promotion or automatic cascade resolution is introduced.

---

## 0.1.54 - 2026-06-14

Validated register-instance dossier and CI enforcement of the cascade rule.

### Added

- `docs/examples/cascade_register/`: a fictional, validated mini-dossier — two `register_candidate` entries (basement ERP reclassification trigger + current ERP classification), two `register_link` entries (one high, one critical) and one `impact_review`. The critical impact routes to `critical_arbitration`, never a silent downgrade.
- `.github/scripts/check_register_instances.py`: read-only check that validates each instance against its schema, verifies `link_ids` referential integrity, and applies the cascade rule by reusing `evaluate_impact_review` from the mcp-server doctor (single source of truth).
- A `Register instance + cascade rule validation` step in `.github/workflows/governance-ci.yml`, so the cascade invariant is enforced in CI.

### Boundary clarification

The check flags, cites and reports; it never edits, fixes or decides. Instances record proposals and per-target human decisions. No runtime, scheduler, queue, provider router, approval engine, memory promotion or automatic cascade resolution is introduced.

---

## 0.1.53 - 2026-06-14

Cascade follow-ups: enforce the rule, reference links, wire the mockup.

### Added

- `mcp-server/pantheon_mcp/doctor.py` gains `check_cascade_rule` (read-only) and the pure `evaluate_impact_review` helper: validates `impact_review` instances against the schema and enforces the cascade rule — a critical impact must route to `critical_arbitration` (never silently downgraded), and a resolved review must carry a recorded decision per target. Added to `run_all`. `mcp-server/tests/test_cascade_doctor.py` covers it (5 tests).

### Changed

- `schemas/register_candidate.schema.yaml` gains an optional `link_ids` array referencing `register_link` entries; the example references the foundations/seismic link.
- `docs/assets/pantheon-control/` Preuves page now speaks the schema vocabulary: each entry carries `register_link`-shaped links, and validating one builds an `impact_review`-shaped object that applies the cascade rule on screen (critical targets show “Arbitrage requis”, never a silent downgrade).

### Boundary clarification

The doctor flags, cites and reports; it never edits, fixes or decides. The schemas and the mockup record proposals and human decisions; no runtime, scheduler, queue, provider router, approval engine, memory promotion or automatic cascade resolution is introduced.

---

## 0.1.52 - 2026-06-14

Register link and impact (cascade) schemas, applied after approval of the proposal.

### Added

- `schemas/register_link.schema.yaml` and `schemas/impact_review.schema.yaml`: validation contracts for typed relations between Registre Probatoire entries (depends_on, impacts, conflicts_with, supersedes…) and for the cascade review opened when an entry changes. Each carries an `x-boundary` block with every runtime flag false, including `automatic_cascade_resolution: false`.
- `schemas/examples/register_link.example.yaml` and `schemas/examples/impact_review.example.yaml` as fictional fixtures (architecture cascade: foundations / seismic, ERP basement reclassification).
- `docs/governance/REGISTER_LINK_CASCADE_SCHEMA_PROPOSAL.md` and `ai_logs/2026-06-14-register-link-cascade-schema-proposal.md` as the proposal and intervention trace.

### Changed

- `schemas/README.md` lists the two new schemas.
- `tests/test_schema_examples.py` and `tests/test_governance_schemas.py` cover the two new schema/example pairs (7 schema tests pass).
- `docs/governance/AUTHORITY_INDEX.md` indexes the proposal.

### Boundary clarification

Schemas are validation contracts only. They record proposed relations and proposed cascade consequences with per-target human decisions; they promote, downgrade, archive and resolve nothing on their own. No runtime, scheduler, queue, provider router, approval engine or memory promotion is introduced. Critical impacts route to arbitration and are never silently downgraded.

---

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

- `docs/governance/AUTHORITY_INDEX.md` indexes the keystone.

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
