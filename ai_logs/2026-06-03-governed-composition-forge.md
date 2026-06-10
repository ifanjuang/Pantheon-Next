# AI Log — Governed composition (HÉPHAÏSTOS forges, capability registry, two gates)

Date: 2026-06-03

## Scope

Proposed and documented an architecture for *governed composition*: how a workflow
can be forged on the fly for a specific cap and still be governed. Three artifacts:

- `docs/governance/CAPABILITY_REGISTRY.md` — capabilities declared by governance
  metadata only, organized as a dependency graph; the index the forge reads from.
- `docs/governance/WORKFLOW_SCHEMA.md` — new "Governed composition" section:
  HÉPHAÏSTOS forges a Workflow Manifest candidate; retrieve/reuse/revise/retain
  loop; two governance gates; per-step signatures. Forged != authorized.
- `docs/governance/reference_reviews/SKILL_FORGE_RUNTIMES.md` and
  `docs/governance/reference_reviews/SKILL_GOVERNANCE.md` — the external sources
  the architecture distils from, with explicit rejected imports.

## Inspiration, distilled not imported

Drawn from external work, then reduced to governance vocabulary:

- **Voyager** — forge skills on the fly + reusable library indexed by description.
- **DSPy** — declarative signatures (input/output spec) per step.
- **Graph of Skills / Semantic Kernel** — dependency-aware retrieval; metadata-first
  selection, implementation invoked only on selection.
- **Case-Based Reasoning (retrieve/reuse/revise/retain)** — the spine of the loop;
  it maps almost exactly onto Pantheon's existing cap, revision and memory gates.
- **EviBound** — pre-execution approval gate + post-execution verification gate.
- **SkillsVote / GovernSpec (Contractual Skills) / MedSkillAudit** — lifecycle
  governance of skills, contractual framing, domain-scoped readiness review.

The CBR loop was the key insight: its four R's are governance Pantheon already has,
so the loop names existing doctrine rather than adding machinery.

## Why

The user asked for an intelligent architecture well-inspired by these repos, for
modular workflow composition that does not duplicate the execution runtime. The
forge (HÉPHAÏSTOS) was already named in the College as the one who forges workflow
candidates; this gives it a registry to compose from, a loop to compose by, and two
gates to keep the result governed.

## Boundary

Documentation only. No forge engine, compiler, scheduler, queue, provider router,
autonomous approval engine, automatic skill installer, automatic skill promotion or
automatic memory promotion. The forge proposes governance structure; execution
stays external under Task Contract. The gate is a governance decision (ZEUS
arbitrates, the human engages), never an automatic mechanism. The re-evaluable
professional cap (MÈTIS) and the responsibility limit remain Pantheon's own and are
not outsourced to any external system.

## Files changed

- `docs/governance/CAPABILITY_REGISTRY.md` (new);
- `docs/governance/WORKFLOW_SCHEMA.md` (governed composition section);
- `docs/governance/reference_reviews/SKILL_FORGE_RUNTIMES.md` (new);
- `docs/governance/reference_reviews/SKILL_GOVERNANCE.md` (new);
- `docs/governance/reference_reviews/README.md`, `docs/governance/MODULES.md`,
  `docs/governance/AUTHORITY_INDEX.md` (indexing);
- `CHANGELOG.md`;
- `ai_logs/2026-06-03-governed-composition-forge.md`.

## Explicit non-implementation

No files were touched under:

```text
schemas/
tests/
operations/
platform/
Docker
.env
pyproject.toml
CLAUDE.md
```

## Boundary phrase

```text
HÉPHAÏSTOS forges the recipe.
PANTHEON governs the cap, the proof and the status.
The execution runtime executes outside.
The human engages.
```
