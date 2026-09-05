# 2026-09-05 — Obsidian operational-health pilot

## Objective

Prepare a bounded report-only qualification corpus for silent Obsidian/workspace failures observed in external operational prior art, without importing a new workspace-health engine, synchronization owner, plugin authority or automatic repair path.

## Verified baseline

```text
Pantheon-Next main = fd39f1d377d57eb2dc03060c0f93b21763b745b7
```

Current main, recent commits, open PRs/issues, current Obsidian/Hindsight workspace owner, manifest-inspector owner, existing graph-health qualification and LiveSync/Hindsight issues were checked before the slice.

Existing owners already establish:

- `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`: optional workspace/second-brain layering and report-only workspace audit;
- `WORKSPACE_MANIFEST_INSPECTOR_CANDIDATE.md`: local workspace-health and deterministic validation posture;
- #660: synchronization/materialization qualification and real conflict observation;
- existing `obsidian_graph_health_pilot.json`: provider-specific graph/link-health qualification for `Ar9av/obsidian-wiki`.

The new corpus does not widen that provider-specific graph fixture. It covers a different operational failure class: silent plugin/config/sync and post-mutation observations.

## Prior art

Reviewed external repository:

```text
dtiger1889-ops/obsidian-agent-integration
main = 6f1d58ceb49e3fbb69e52b502e1f9d794fb173b3
```

Relevant operational documents:

- `operations/vault-maintenance.md`;
- `operations/context-budget.md`.

This repository remains prior art only. It is not added to `external-pins.json`, adopted as a dependency or made authoritative.

## Prepared corpus

`tests/fixtures/obsidian_operational_health_pilot.json` prepares seven report-only cases:

1. move/archive inbound-link impact candidate;
2. malformed multi-link frontmatter shape;
3. timestamp writer ambiguity from plugin/linter behavior;
4. per-device plugin setting divergence despite synced configuration;
5. live-file versus sync-conflict-copy ambiguity;
6. scripted/local filesystem success without observed sync convergence;
7. external leaf pointer becoming stale after vault rename/move.

The corpus also defines a post-mutation review posture for bulk moves, scripted writes, plugin/template configuration changes, sync-conflict resolution and workspace restructure.

## Preserved boundaries

```text
workspace health observation != professional currentness
health finding != defect confirmed
filesystem mutation success != sync convergence
config snapshot != active per-device state
metadata field != source-authored observation
conflict copy != stale by definition
bulk mutation != authorization to auto-fix
audit clean != Evidence
workspace path != governed identity
```

The fixture is `prepared_not_executed`; it contains no observed results and cannot be cited as proof that a real Pantheon/Obsidian deployment exhibited any listed failure.

## Verification

`tests/test_obsidian_operational_health_pilot.py` checks owner reuse, prior-art non-adoption, exact case boundaries, report-only posture and absence of fabricated observations.

GitHub CI is the executable verification gate because the local container cannot reach GitHub.

## Open

A later bounded execution may exercise selected cases against an isolated or explicitly authorized real Obsidian/LiveSync setup. That later observation must preserve exact device/plugin/sync identities and must not turn a health finding into automatic repair or professional truth.
