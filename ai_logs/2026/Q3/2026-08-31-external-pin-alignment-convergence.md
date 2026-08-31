# External qualification pin alignment — 2026-08-31

Status: validation / intervention trace — not doctrine.

## Baseline

Current `main` after #877:

```text
aaf9b95261f71492d7d7e7787ce50d9278f6d368
```

The freshness observation merged in #877 records newer upstream heads for Hindsight, Self-hosted LiveSync and CouchDB. This change decides only whether the qualification targets move to those observed heads.

## Decision

Move the current qualification targets to:

```text
hindsight                 0.9.1      -> 0.9.2
self-hosted-livesync      1.0.18     -> 1.0.21
self-hosted-livesync-cli  1.0.18-cli -> 1.0.21-cli
couchdb                    3.5.0      -> 3.5.2
```

`self-hosted-livesync` resolves to reviewed ref:

```text
f5f7aab11f03f62c6946d2fa296c50bb5df5b2a4
```

The move closes the recorded version lag. It does not make any component mandatory, installed, activated or adopted.

## Why the targets move

- Hindsight 0.9.2 is the currently observed upstream release. Its BM25 change overlaps the hand-written lexical fallback added in #874, but Hindsight is not wired into that retrieval path; lexical-lane ownership remains a separate design question and is not decided here.
- LiveSync 1.0.20+ contains an upstream correction for settings-page behaviour on the Obsidian 1.13 release line. Moving to the observed 1.0.21 head avoids continuing to qualify a combination with a documented upstream interaction defect.
- CouchDB backs that reference topology and moves to the observed 3.5.2 image tag.
- the LiveSync CLI target is derived from the selected LiveSync pin rather than independently selected.

A controlled follow-up comparison recorded on #884 did **not** demonstrate that LiveSync 1.0.21 fixes the intermittent Obsidian test-session timeout. This pin decision is therefore based on currentness and qualification alignment, not a claimed stability benefit.

## Deployment lock convergence

`deployment/ubuntu/release.env` was already ahead of the qualification registry for Hindsight. The release lock is aligned to the same reviewed targets and the existing bootstrap contract is extended so Hindsight and the LiveSync CLI cannot drift silently from the qualification registry again.

```text
deployment target != qualified artifact
```

## Deliberate non-change

No policy chokepoint wiring, LiveSync retry helper, workflow trigger, blocking-lab arbitration, runtime activation, Evidence admission or professional adoption changes here.

The existing external labs may re-run because their path filters include the pin registry. Their output is qualification evidence for the moved target; a green lab is not operational acceptance. Known lab flakiness must not be reinterpreted as a version claim.

```text
observed upstream != selected pin
pin moved != qualification passed
qualification passed != operational acceptance
deployment lock aligned != deployment activated
provider selected != authority transfer
```

## Verification

Protected qualification/deployment/test paths are changed. Exact-head PR CI and the applicable external qualification workflows are the verification surface before merge.
