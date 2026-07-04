# AI log — maintainer release and licence checklist

Date: 2026-07-04

## Scope

Continued after #273 protocol preparation by addressing the remaining maintainer/legal blocks from #264.

## Checked

- Issue #261 — post-consolidation git tags.
- Issue #262 — PDF licence qualification and optional history purge.
- Issue #264 — out-of-repo handoff.
- Existing repository search for an equivalent maintainer checklist.

## File added

```text
docs/governance/MAINTAINER_RELEASE_AND_LICENSE_CHECKLIST.md
```

## Purpose

Consolidate the release-tag and PDF licence/history actions that are outside the assistant connector.

## Decision classification

Accepted:

- create one maintainer checklist under `docs/governance/`;
- keep tags as maintainer-side release markers;
- keep PDF licence and history purge as maintainer/legal decisions;
- keep `base_metier` out of vertical-slice grounding until qualified.

Refused:

- no release automation;
- no legal conclusion;
- no history rewrite;
- no runtime implication;
- no approval or memory effect.

## Issues updated

- #261 linked to the checklist and closure criteria.
- #262 linked to the checklist and closure criteria.
- #264 linked to the checklist and global closure criteria.

## Repo state

- Documentation checklist: implemented.
- Runtime implication: non applicable.
- Protected paths touched: none.
