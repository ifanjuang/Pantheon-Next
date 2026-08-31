# 2026-08-31 — external pin freshness observation

## Objective

Give `external-pins.json` a mechanism that can detect it falling behind upstream, without granting anything the authority to move a pin.

Second slice on the same branch as the consequential-mutation inventory. Same shape of problem: a property the repository relies on, with nothing able to observe it being lost.

## Exact repository state

```text
branch base = db174f3b1a500fcc6c48f7c5ad1a4efea7d70002
main        = 07b28ce4f56469f2824d0e250f3d100c78090fff
```

PR #877 was green on all seven checks before this slice was added.

## Finding

Three of ten pins had drifted, and nothing in the repository could have said so:

```text
self-hosted-livesync   1.0.18  -> upstream 1.0.21   (three releases)
hindsight              0.9.1   -> upstream 0.9.2
couchdb                3.5.0   -> registry 3.5.2
```

`self-hosted-livesync` is the material one. Upstream 1.0.20 corrects settings-page behaviour under Obsidian 1.13 — the release line pinned beside it as `obsidian-desktop` — so the S1..S6 qualifications currently exercise a combination whose upstream documented an interaction defect.

`.github/dependabot.yml` covers `pip` on `/.github/requirements` and `github-actions`. It cannot cover these: they are git refs, container images and releases described in a repository-specific JSON registry. `test_external_qualification_pins.py` verifies the registry's internal consistency and its non-drift against the distribution lock — never its currency against upstream.

## Existing owners reused

`external-pins.json` remains the sole owner of which artifact each qualification targets. It is unchanged by this slice: no pin was moved.

No new governance document. No new executable component under `mvp_vertical`.

## Why a second file rather than fields on the registry

The registry records a decision. Upstream's release history is a fact about someone else's project. Keeping them in separate files preserves an existing distinction:

```text
observed != adopted
observation refreshed != pin moved
```

Refreshing an observation must never be reachable through, or look like, moving a pin. A reviewer reading a diff to `external-upstream-observations.json` knows immediately that no target changed.

## Design

`implementation/qualification/external-upstream-observations.json` records, per pin: the source its upstream head is read from, the head last seen, the date it was seen, and a `delta` verdict.

Two signals, deliberately distinct:

```text
observation_stale  -> upstream moved past what we last recorded; a human must look
unacknowledged_lag -> we recorded a newer release and never decided about it
```

`acknowledged` closes a lag as a dated human decision, with a required reason. Two pins are acknowledged today and both are real cases rather than exemptions of convenience:

- `obsidian-desktop` — `releases/latest` on `obsidianmd/obsidian-releases` returns the mobile 1.13.8 while 1.13.7 remains the desktop head; the pin is correct despite the newer tag;
- `self-hosted-livesync-cli` — not independently released; its freshness question belongs to the pin it follows, and the report gives it its own `derived` signal so the source pin's signal is not double-counted.

No mechanical comparison is made between the pinned version and the upstream head. Upstream identifiers are heterogeneous — Hermes Agent ships its version under a date-formed tag — so a human records the verdict and the tool only detects that upstream moved past the recorded observation.

`apache/couchdb` publishes no GitHub releases at all. Its pin is an image, so its head is read from the image registry's tag list, which is the authoritative answer for the artifact actually referenced. Sources are declared per pin rather than inferred from the pin kind, precisely so a case like this fails as a declaration rather than silently returning nothing.

## Workflow split

`.github/workflows/external-pin-freshness.yml` runs two jobs deliberately apart:

- `contract` — on pull requests touching the registry, the observation record or the tool. Exercises the comparison offline. A pull request is never made red by someone else's release.
- `observe` — on a weekly schedule and on manual dispatch. Reaches upstream and fails when a pin needs a human look, publishing the report as an artifact and in the run summary.

A red scheduled run is the signal. It blocks no pull request, and it will be red on its first run because three lags are undecided — which is the honest state, not a defect of the check.

## Validation

Exercised end to end from this session. GitHub's API is unreachable from here (the session proxy refuses repositories outside its scope), which incidentally proved the degradation path: Docker Hub returned `3.5.2` for `couchdb` and PyPI returned the current `mnemosyne` versions, while GitHub-backed pins reported `__unreachable__` per pin and the recorded deltas still produced the correct signals. One unreachable host does not blind the report.

```text
implementation/tests/test_external_pin_freshness.py   14 passed (offline, injected heads)
implementation/tests                                1234 passed, 352 skipped
tests/                                               554 passed
mcp-server/tests                                     229 passed
.github/scripts                                       23/23 OK
```

## Guard that fired during the work

`test_active_qualification_code_does_not_duplicate_current_pin_literals` failed on the first run: the tool's docstring used a real current pin version in an illustrative sentence. The guard was right — a freshness tool that hard-codes the versions it audits is the first thing that will drift. The docstring now quotes no pin value, and says so.

The guard scans `.yml/.yaml/.py/.sh/.ts` and not `.json`, so the observation record itself is outside its scope. That is correct here: for an aligned pin, the observed head legitimately equals the pinned version, and forbidding that would make the file unwritable.

## Boundary

```text
observation != adoption
report red != update authorized
upstream head read != artifact installed
acknowledged lag != permanent exemption
scheduled check != gate on a pull request
```

## Next admissible step

Deciding the three open lags is human work, and `self-hosted-livesync` is the one with a concrete reason to move rather than a version number to chase. Moving it means re-running S1..S6 and reading the 1.0.18..1.0.21 diff for conflict and reconnection behaviour before treating S4 and S5 as still valid. The `hindsight` decision is not purely a bump either: 0.9.2's BM25 change overlaps the hand-written lexical fallback added in #874, so it should settle which lexical lane is authoritative on which corpus.
