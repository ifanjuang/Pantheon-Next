# Governance cleanup — absorb Adaptive Request Method into Request Lifecycle — 2026-08-29

## Objective

Continue #787 from merged `main` `f78bb126b67bd86837c3bbad5e7209ffe48610b6` with the first actual owner/file reduction of the current documentation-topology campaign: absorb the remaining distinct responsibility of `ADAPTIVE_REQUEST_METHOD.md` into its indexed mother owner `REQUEST_LIFECYCLE.md`, rewrite the only active doctrinal consumer, and remove the satellite.

## Repository evidence

The decision follows two prior #787 slices:

- #803 removed repeated boundary boilerplate by reusing `BOUNDARY_PROFILES.md` and `HERMES_INTEGRATION.md`;
- #804 removed Context Stack and Source Need multi-ownership from Adaptive.

After #804, Adaptive's remaining core was limited to proportional request activation, request decomposition, input/output consequence, complexity drivers and safe defaults.

`ADAPTIVE_REQUEST_METHOD.md` declared active support doctrine but was not listed in `GOVERNANCE_AUTHORITY_INDEX.md`. `REQUEST_LIFECYCLE.md` is indexed active support doctrine and already owns direct/fuzzy triage, cap handling, lifecycle choreography, status arbitration and consequential chokepoints.

The only active doctrinal exact-file consumer found for Adaptive was `SOURCE_NEED_AND_REGISTRY.md`; other exact-file hits were historical ai_logs.

## Historical precedent

This absorption follows the repository's established cleanup precedent in commit `1abd2bfffbd3d5e6a4734f0f2bc3a547e2d675b2`: when an existing mother owner is demonstrated, preserve useful responsibility in that owner, rewrite active references, remove the satellite and rely on Git history plus the ai_log for provenance.

Unlike that earlier verbatim pass, this absorption intentionally does not re-import the ~100 lines of Context Stack and Source Need doctrine already removed in #804, because those rules remain owned by `CONTEXT_STACK.md` and `SOURCE_NEED_AND_REGISTRY.md`.

## Scope

- absorb Adaptive's remaining local rules into `docs/governance/REQUEST_LIFECYCLE.md`;
- retarget `docs/governance/SOURCE_NEED_AND_REGISTRY.md` to `REQUEST_LIFECYCLE.md` for request-time source-need activation;
- remove `docs/governance/ADAPTIVE_REQUEST_METHOD.md`.

No schema, test, CI, runtime, role registry, PDP/PEP, Cockpit, provider, client or implementation artifact changes.

## Absorbed responsibility

`REQUEST_LIFECYCLE.md` now also owns the request-level proportional activation specialization:

```text
proportional request activation
request decomposition candidates
input != output consequence relationship
complexity drivers
Context Stack / Source Need owner seams
output consequence and safe defaults
```

Detailed Context Stack, Source Need, Evidence, approval and memory semantics remain with their respective owners.

## Reference migration

`SOURCE_NEED_AND_REGISTRY.md` now states:

```text
REQUEST_LIFECYCLE.md -> proportional request handling activates source need
```

Historical ai_logs are intentionally not rewritten.

`ADAPTIVE_REQUEST_METHOD.md` had no authority-index row, so no index row is removed or migrated.

## Overlap analysis

The absorption does not make Request Lifecycle a runtime workflow. It extends the already-owned lifecycle choreography with one method-level rule: activate only the governance owners required by the request's consequence.

It does not absorb `GOVERNED_METHOD_STANDARD.md`, `GOVERNED_AUTONOMY_GRADIENT.md`, `WORKFLOW_FORGING_PROTOCOL.md`, Context Stack or Source Need responsibilities.

## Affected consumers

Documentation readers and Source Need doctrine only. No executable consumers exist for the removed file.

## Migration and rollback

Documentation-only. The removed satellite remains recoverable from Git history. Rollback is a normal Git revert.

## Role / Rite / Space

- Role: MNEMOSYNE for owner continuity, ATHENA for method composition, THEMIS for authority-boundary review.
- Rite: Concordance des sources across exact main, #787, the indexed method owner and active file references.
- Space: Pantheon Next governance repository.

These labels create no runtime state.

## Authority impact

One unindexed overlapping active-support document is removed. No new authority is created. `REQUEST_LIFECYCLE.md` keeps its existing active-support authority class and now explicitly contains the proportional activation specialization that previously sat in the satellite.

## Runtime impact

None. Method composition remains documentation; execution remains external.

## Preserved invariants

```text
method doctrine != runtime workflow
owner absorption != authority promotion
context != Evidence
retrieved != truth
registered source != Evidence
memory != Evidence
runtime success != authorization
PDP decision != PEP execution
projection != persistence
```

## Quantitative convergence

Before this ai_log, exact compare shows:

```text
ADAPTIVE_REQUEST_METHOD.md    removed: -210
REQUEST_LIFECYCLE.md          +109 / -5
SOURCE_NEED_AND_REGISTRY.md   +2 / -2
```

Net governance-doctrine reduction: roughly 106 lines plus one standalone file/owner surface removed.

This is not a verbatim relocation: duplicated context/source doctrine intentionally stays deleted because its existing owners already preserve it.

## Verification rule

The PR must pass Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency on its exact final HEAD. The final patch and all reviews/threads/comments must be read. Active references must not depend on the removed file; historical ai_logs may continue to mention it as provenance.