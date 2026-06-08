# Changelog

## 0.1.31 - 2026-06-03

Governed composition: HÉPHAÏSTOS forges, the capability registry declares, Pantheon governs.

### Added

- `docs/governance/CAPABILITY_REGISTRY.md` as active support doctrine: a governance declaration of capabilities organized as a dependency graph (metadata only; the executable lives in the execution runtime). It is the index HÉPHAÏSTOS forges from. A declaration is a candidate until reviewed; enrichment is governed; superseded declarations are archived, not deleted. It is not a runtime, installer, marketplace or tool dispatch table.
- `docs/governance/WORKFLOW_SCHEMA.md` gains a "Governed composition" section: HÉPHAÏSTOS forges a Workflow Manifest candidate for a specific cap; a retrieve/reuse/revise/retain composition loop mapped to existing governance; two governance gates (pre-execution eligibility arbitrated by ZEUS, post-execution evidence verification); per-step signatures as governance contracts. Forged != authorized.
- `docs/governance/reference_reviews/SKILL_FORGE_RUNTIMES.md` (Voyager, DSPy): forge and composition vocabulary distilled; forge mechanics rejected as Pantheon architecture — they belong to the execution runtime.
- `docs/governance/reference_reviews/SKILL_GOVERNANCE.md` (EviBound, SkillsVote, GovernSpec, MedSkillAudit): convergent gate and lifecycle vocabulary distilled; the gate stays a governance decision, never an autonomous approval or promotion engine.

### Changed

- `docs/governance/MODULES.md`, `docs/governance/AUTHORITY_INDEX.md` and `docs/governance/reference_reviews/README.md` now index the capability registry, governed composition and the two new reviews.
- `docs/governance/AGENTS.md` and `docs/governance/GOVERNANCE_COLLEGE.md`: HÉPHAÏSTOS's canonical role now explicitly includes forging Workflow Manifest candidates (compose declared capabilities into a recipe for the cap). A forged recipe stays a candidate; forging does not authorize execution; eligibility is arbitrated by ZEUS and execution stays external under Task Contract.
- `docs/governance/CAPABILITY_REGISTRY.md` now hardens the skill admission guard with the SkillsGate / SkillsGate-like MCP skill-manager case: visible / installed / synced / MCP-available skills remain non-admitted, write-capable install / update / remove / sync operations are external actions requiring gated review, and refusal tests cover global install, multi-agent install, package sync, unpinned sources, broad permissions, catalogue ranking, local edits and client-data use. This integrates #86 without creating a separate doctrine document.

### Boundary clarification

Documentation only. Inspired by external skill-forge runtimes (Voyager, DSPy), skill-governance work (EviBound, SkillsVote, GovernSpec, MedSkillAudit) and the SkillsGate skill-manager boundary, but importing none of them: no forge engine, compiler, scheduler, queue, provider router, autonomous approval engine, skill installer, MCP server, skill manager, automatic skill promotion or automatic memory promotion. Execution remains external. The re-evaluable professional cap (MÈTIS) and the responsibility limit remain Pantheon's own.

```text
HÉPHAÏSTOS forges the recipe.
PANTHEON governs the cap, the proof and the status.
The execution runtime executes outside.
The human engages.
```

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
