# AI log — realign VERSION with the CHANGELOG head (B-7)

Date: 2026-07-01.

Actor: Claude Code.

## Intent

Arbitration B-7 from the maintainer's consolidated decision on the #246 audit:
`VERSION` had drifted to `0.1.0` while the CHANGELOG head was `0.1.58`. For a
project whose thesis is status honesty, this is a bad signal at near-zero cost to
fix. Establish and apply the invariant: `VERSION` = CHANGELOG head = git tag.

## Change

- `VERSION`: `0.1.0` -> `0.1.59`.
- `CHANGELOG.md`: new `0.1.59` entry recording the realignment (it becomes the
  head, so `VERSION` matches it).
- A `v0.1.59` git tag is created on the merge commit after this lands, so the
  three references agree.

## Boundary

Metadata realignment only. No doctrine authored or altered; no schema, test,
`mcp-server/`, runtime or other protected-path change. Automation of the invariant
(a CI check / release step) is deferred per the maintainer's "realign manually
first" instruction.
