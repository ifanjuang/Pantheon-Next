# Stable active artifact identities

Date: 2026-08-03

Status: validation trace — no doctrine created.

## Context

The cross-repository architecture convergence baseline still listed seven active Pantheon-Next paths whose identities contained implementation-generation or working-revision markers.

The repository rule is now:

```text
stable active identity
+ explicit document or asset revision inside content / metadata
+ Git history for previous revisions
```

This does not apply blindly to migrations, external protocol releases, coexistence-required exports or historical logs.

## Renamed active assets

```text
docs/assets/pantheon-dashboard/pantheon-next-gate-page-v15-mobile-drawer.html
-> docs/assets/pantheon-dashboard/pantheon-next-gate-page-mobile-drawer.html

docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html
-> docs/assets/pantheon-map/pantheon-next-governed-ecosystem-map.html
```

The HTML blobs were moved without content modification. The map redirect and README now reference the stable path.

## Renamed visual prompts

```text
prompt-city-memory-v01.md
-> prompt-city-memory.md

prompt-composition-study-v01.md
-> prompt-composition-study.md

prompt-master-poster-v01.md
-> prompt-master-poster.md

prompt-negative-v01.md
-> prompt-negative.md
```

Prompt identities are responsibility-based. Their current revision is declared inside the Markdown document. Versioned binary exports and provenance files may retain explicit revision identifiers when multiple export revisions legitimately coexist.

## Renamed governed candidate

```text
docs/governance/MCP_PANTHEON_MINIMAL_V0.md
-> docs/governance/MCP_PANTHEON_MINIMAL_PROFILE.md
```

The document remains candidate support doctrine. Its first technical/document revision is declared inside the document rather than encoded as a permanent architecture generation.

The runtime-adapters authority index now references the stable owner path.

## Historical references

Historical `ai_logs/` entries are not rewritten. They record the path and revision that existed at the time of the intervention.

```text
historical path reference != active architecture identity
```

## Boundaries

```text
stable filename != semantic promotion
renamed asset != implemented runtime
visual revision != governance generation
MCP profile documented != MCP deployment
link updated != capability activated
CI success != authority approval
```

No runtime, API, schema, provider route, scheduler, queue, plugin manager, automatic approval, memory promotion or external action is added.

## Cross-repository consequence

After this change is merged, `pantheon-mvp` may remove the seven Pantheon-Next generation-named artifact exceptions from `ARCHITECTURE_DEBT_BASELINE.json`.

Expected remaining generation-named active artifacts:

```text
0
```
