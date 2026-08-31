# 2026-08-31 — remediation batch 1: make a green lab mean something again

## Objective

First batch of the remediation plan. All four items answer the same question in different places: **can a green result be read as what it appears to claim?**

Independent of PRs #877 and #881: this branch is based on current `main` and touches no file either of them changes.

## Exact repository state

```text
base = 5fd43c2160ee3073bcb041827724b2ad57812c54
```

`main` advanced by one commit (#880, review-context source preservation) between the analysis and this batch. It adds one private helper to `runner.py` and no mutation entry point, so the consequential-mutation inventory in #877 is unaffected. Both open branches merge cleanly against it.

## 1. The Obsidian e2e labs failed roughly a third of the time

### Correcting two things stated earlier

**First correction.** The PR #881 description and the remediation plan both said S4 was fragile *because* it runs Pantheon-authored code against upstream internals, while S3 and S5 run upstream's own suites and therefore survived the version jump.

That is wrong. S3 failed at the same harness line as S4 — `startObsidianPluginSession`, `session.ts:337`, the same fixed 60 s wait — while running `security-seed-reconnect.ts`, upstream's own scenario. Authorship is not the factor.

**Second correction.** Both said *six* labs depend on that call. It is **four**: S2, S3, S4, S5. Those are the only workflows invoking `xvfb-run`. S1 drives the headless CLI and starts no Electron session.

### What the evidence actually shows

Same commit, same pins, two observations on 2026-08-31:

```text
S4  60 s timeout under 35 parallel checks  ->  19 s when re-run nearly alone
S3  60 s timeout under 35 parallel checks  ->  33 s when re-run nearly alone
```

And it long predates this work: of the **28 runs of the S3 workflow before this branch existed** — on `codex/*` and Dependabot branches touching no LiveSync pin — **11 failed**. Runs 26, 27, 31, 32, 33, 34, 35, 37, 38, 43 (on attempt 2) and 45. Roughly 39 %.

The driver is contention: four real Obsidian/Electron sessions under Xvfb, plus Docker CouchDB fixtures, competing on GitHub-hosted runners against a wait the repository does not control.

### A fix considered and rejected

The obvious idea was a shared `concurrency` group across the four labs, to serialize them. **That would have been wrong.** GitHub Actions concurrency is not a queue: with one group and `cancel-in-progress: false`, only one run may be pending, so a newer run cancels the older pending one. Four labs sharing a group would see three of them cancelled rather than queued — a worse failure mode, and a silent one.

Recorded because the idea is attractive and wrong.

### What was done

`implementation/tools/obsidian_e2e_with_flake_report.sh` — one bounded retry, in one place, called by all four labs.

It is not a skipped, disabled or quarantined test. The scenario runs in full and must pass; two consecutive failures are a real failure and the second exit code is propagated verbatim. What it removes is the single-attempt contention flake.

The flake is never silent. A first-attempt failure always writes to `$GITHUB_STEP_SUMMARY`, so the fragility stays countable rather than absorbed by a green tick.

```text
bounded retry != skipped test
silent retry != honest gate
green after retry != green
```

The script also carries the *investigative* half of the plan's P2‑5, which this session could not perform: on a flake it reports the installed `@vrtmrz/obsidian-test-session` version and greps its shipped sources for `waitForFunction` / `timeout` sites, into the run summary. The authoring session cannot read that package — GitHub and the CDNs are unreachable from it, and guessing an environment variable name would produce a change that silently does nothing. The next run that flakes will answer the question from a real observation.

Exercised locally on all four paths: success first try, flake then success, two failures, and non-1 exit propagation.

The durable fix remains upstream: a configurable readiness timeout, or these labs not competing for one runner.

## 2. O3 no longer runs where its green reads as a qualification

`implementation-hindsight-obsidian-hermes-o3-lab.yml` is frozen against versions the canonical registry no longer targets:

```text
registry hindsight            0.9.2     O3 runs 0.8.5
registry hindsight-obsidian   0.2.1     O3 runs 0.2.0  (b627aa6f)
registry hermes-agent         5fc308a7  O3 runs 3c27eb62
```

`HISTORICAL_ACTIVE_PATHS` exempts it from the pin-drift guard, so nothing reported the gap, and it ran on `pull_request` where a green result read as a qualification of a combination it no longer tests.

It is now `workflow_dispatch` only, with the reason inline, and declared in `WHAT_RUNS.md` using that file's existing vocabulary.

**Adding the pin registry to its triggers was explicitly not done.** It would not fix anything: the scenario is written against the older Hindsight API and would simply fail. Rebuilding it against current pins, or retiring it, is a scope decision left open — rebuilding is only worth it if shared memory between vaults still guards a real decision.

## 3. The README installed something Governance CI does not

`README.md` documented `pip install "mcp-server/.[test]"` while `governance-ci.yml` uses `-e`. A contributor following the README resolves `pantheon_mcp` from `site-packages` and silently tests a snapshot instead of the working tree.

This is not theoretical: it bit the authoring session earlier today. New MCP annotation tests passed against a stale installed copy and reported 24 failures that did not exist in the tree.

## 4. One ported fix

`check_internal_links` fails on `main`: `CAPABILITY_REGISTRY.md:74` contains the English phrase "Runtime implementation/release provenance", which the checker reads as a path now that `implementation/` is a real directory.

#877 already fixes it. The same one-line rewording is ported here so this branch is not red for a known reason; it no-ops once #877 merges.

## Validation

```text
tests/                  554 passed
mcp-server/tests        226 passed
implementation/tests   1217 passed, 352 skipped (no local PostgreSQL)
.github/scripts         23/23 OK, including check_internal_links
retry script            4 paths exercised locally
4 workflows             YAML re-parsed; a duplicated `shell: bash` introduced
                        by the first edit was caught and removed before commit
```

## Boundary

```text
lab green != qualification
bounded retry != skipped test
frozen fixture != current target
dispatch-only != retired
README install != CI install
```

## Deliberately not in this batch

The composite action factoring the lab preamble (plan P2‑3) was sequenced first, then moved back: it changes the checkout and identity-verification path every lab depends on, and it cannot be exercised locally. Breaking it would break all four labs at once. It belongs in its own change, after this one is observed green.

## Next

The generalized required-path check (P1‑2) and the test-altitude migration (P1‑1) are the remaining root-cause items. The seven ungated mutation entry points (P1‑3) are each a separate review, not a mechanical pass.


## Amendment, 2026-08-31 — O3 conceded to #893, and a framing corrected

**O3 is no longer part of this change.** PR #893 retires the O3 live lane
outright — workflow, harness and contract removed, with the two provider-neutral
assertions O3 carried retained under the current O1 contract and a guard that
the retired paths do not reappear. That is a better answer than the
`workflow_dispatch`-only holding position taken here, so this branch drops its
O3 edits rather than run a parallel path. Convergence over two owners.

**A framing in the companion lab-accounting work was wrong.** It said seventeen
labs "block merges". They do not. The active `protect-main` ruleset requires
four status contexts — `mcp-server module tests`, `Read-only governance checks`,
`Packaging and release contract`, `Obsolete document authority consistency` —
and no qualification lab is among them. Running on `pull_request` is not the
same as gating a merge.

This is independently visible in data collected during that work: while
`real-restart-reconnect` was failing on this branch, GitHub reported the pull
request as `unstable`, not `blocked`. A failing *required* check yields
`blocked`.

```text
runs on pull_request != required status check
required status check != gates the merge button
red non-required check != blocked merge
```

What survives that correction is the cost question, unchanged in substance:
every lab's path filter watches the whole of `external-pins.json`, so one pin
move fires all seventeen at once — which is the runner contention behind the
Obsidian family's flake rate. Each lab already names the pins it consumes on its
exporter command line; the trigger simply does not use that declaration.


## Amendment, 2026-08-31 — two review findings, both correct

### The retry was not restricted to the condition it was written for

The wrapper retried *every* nonzero exit, and then wrote into the run summary
that the first failure was a session-start flake and that the pins under test
were unaffected — **regardless of what had actually failed**. An assertion
failure, a CouchDB error or a real LiveSync regression that happened to pass on
the second attempt would have been reported green and mislabelled as contention.

That is precisely the "re-run until green" pathology this script was written to
remove, reproduced inside the script itself.

The first attempt's output is now captured and matched against the diagnosed
signature — `startObsidianPluginSession` together with a readiness timeout —
and the retry applies only on a match. Anything else fails immediately on the
first attempt, with the summary stating that it was not retried and why. The
contention claim now rests on the matched signature rather than on the retry
having succeeded.

Exercised on every decision path before pushing:

```text
pass first try                              exit 0
matching signature, then pass               exit 0
matching signature, fails twice             exit 1
non-matching failure                        exit 1, no retry
non-matching failure that would pass on a
  retry (CouchDB, exit 4)                   exit 4, not 0
matching signature, non-1 exit              exit 7 propagated
```

The fifth case is the one that matters: under the previous version it was a
green tick with a false label.

### The shared wrapper was not a trigger for its own consumers

All four labs execute the wrapper, but none listed it in `pull_request.paths`.
A pull request changing only the wrapper would have run none of the labs that
depend on it — the common execution path merging without a single consumer
exercised. The same class of gap as an import edge that no call ever takes.

The path is added to all four filters, and each lab's contract test now asserts
it is present in the trigger section specifically, not merely somewhere in the
file — referencing it in `run:` was what made the omission easy to miss.
Verified to bite: removing the path from one workflow fails that lab's contract.

```text
executed by a lab != a trigger for that lab
referenced in the file != declared as a path
retry on any failure != bounded retry
```
