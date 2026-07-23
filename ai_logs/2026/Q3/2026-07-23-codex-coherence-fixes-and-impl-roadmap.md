# 2026-07-23 — Codex coherence fixes and implementation roadmap

Status: validation-only intervention trace.
Boundary profile: candidate_support_note.

## Change

Two things, documentation only:

1. Resolve the seven Codex review findings left on the freshly merged cockpit /
   platform doctrine (#460, #461, #462).
2. Add `docs/roadmaps/PLATFORM_IMPLEMENTATION_ROADMAP.md` — a phased plan to turn
   the merged doctrine into a working platform one governed vertical slice at a
   time, wired to the chokepoint.

## Codex findings resolved

```text
IA §3   Decision is a distinct linked object, not a Work Issue projection
IA §4.6 a pre-response card is a Decision Request / Gate, not yet a Decision
IA §5.5 Kanban columns map onto the owner Work Issue vocabulary (Besoin de vous / À relire / Bloqué)
prod §9 distribution_record keeps an exact-output ref (version + hash) when not archived
nav §10.4 engagements reference identity records; no duplicated master fields (optional dated snapshot)
arch index  PROJECT_NAVIGATION_UX.md gets an explicit authority row (was grouped-visibility only → to verify)
runbook §13 /health probe is optional / version-guarded; /v1/models is the authoritative check
```

Findings 1–2 confirm the Decision-inbox coherence concern raised before the merge;
finding on the authority row is the same class gap already fixed for the IA doc.

## Files changed

```text
docs/governance/PANTHEON_COCKPIT_INFORMATION_ARCHITECTURE.md
docs/governance/DOCUMENT_PRODUCTION_LIFECYCLE.md
docs/domain-packs/architecture/PROJECT_NAVIGATION_UX.md
docs/governance/authority/ARCHITECTURE_AUTHORITY_INDEX.md
docs/install/COMMON_BASELINE_RUNBOOK.md
docs/roadmaps/PLATFORM_IMPLEMENTATION_ROADMAP.md (new)
ai_logs/2026/Q3/2026-07-23-codex-coherence-fixes-and-impl-roadmap.md (new)
ai_logs/INDEX.md (regenerated)
```

## Boundary

```text
review finding resolved != doctrine promoted
roadmap != implementation
authority row added != capability approved
```

No runtime, schema, test, protected path, `mcp-server/` code, CI script or
external action is introduced.
