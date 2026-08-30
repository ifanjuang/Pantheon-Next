# 2026-08-30 — observe first #827 professional quote-review baseline

## Objective

Execute the existing first professional-value corpus through the current project-aware stand-in path before adding any new professional-review method, retrieval policy or evaluation subsystem.

This is an observed baseline, not a claim that #827 is solved.

## Repository state

Baseline branch started from:

```text
main = fc5aae73f3933709e79deabcbe30bf34fcbca00f
```

At that point:

- #849 had already merged the nine-case human-labelled `devis_reprise` qualification corpus;
- #858 had already merged access + Project Document currentness + exact preserved-source retrieval into `runner.run_accessible_applicable(...)`;
- `DOCUMENT_REVIEW.md` already owned the review claim types;
- `FINANCIAL_LOT_INSURANCE_REVIEW.md` already owned the relevant exclusion/scope/quantity/ambiguity controls;
- no new professional taxonomy or doctrine owner was required.

PR #857 remained a separate Obsidian qualification and did not overlap this work.

## Executed path

The qualification materialized the three selected synthetic source files as Project Documents and assigned each a qualification-only `current_working` posture:

```text
status           = issued
effect_class     = working_revision
authority_status = internal_working_authority
```

That posture exists only to exercise the currentness owner in the synthetic corpus. It does not establish contractual or execution authority.

The executed path was:

```text
Task Contract
+ authenticated test principal
+ selected Project Documents
-> human access
-> current_working resolution
-> exact document_version_id
-> preserved source_ref + source_digest + source_version
-> digest-exact hybrid retrieval
-> runner.run_accessible_applicable(...)
-> DeterministicDrafter
-> Result Candidate + Evidence Pack Candidate
```

## First CI execution

Initial implementation head:

```text
40a55e5a1fda1d58c43d94d97b7f2eefec47c36c
```

All four normal gates completed successfully:

- Governance CI;
- Pantheon Architecture Audit;
- Obsolete Authority Consistency;
- Pantheon implementation CI.

The PostgreSQL-backed implementation suite completed with:

```text
1549 passed
```

The new professional baseline test passed inside that suite.

Pytest captured stdout for passing tests, so the exact observation was not visible in the normal job log. No conclusion about retrieval breadth was inferred from code alone.

## Exact observation replay

A temporary PR-only workflow was added solely to rerun the same PostgreSQL-backed test with `pytest -s` and expose its observation line. Temporary observation head:

```text
684abc23b7297e7eb8c885128324705e5714cf0f
```

The temporary workflow is measurement instrumentation only and is removed from the final branch.

Observed result:

```text
output_kind                   = candidates
result_status                 = draft_to_review
resolved_source_count         = 3
resolved sources              = CCTP B + DPGF B + quote Q-2026-041
evidence_item_count           = 4
evidence sources              = CCTP B + DPGF B
quote present in evidence     = no
retrieved distribution        = 3 DPGF chunks + 1 CCTP chunk + 0 quote chunks
expected attention cases      = 7
explicit claim types          = 0
explicitly typed cases        = 0
claim support status          = no_assertive_claims
forbidden claim hits          = 0
external action authorized    = false
```

The evidence previews confirmed that the four admitted retrieval candidates were three DPGF passages and one CCTP passage. No passage from `quote_Q-2026-041.md` reached the drafter.

## Observed classification

### Fact

Access and professional-currentness composition resolved all three selected documents correctly, while the exact hybrid retrieval top four omitted the contractor quote entirely.

### Interpretation

The first demonstrated blocker is therefore retrieval coverage, before professional judgment:

```text
selected comparison document resolved
!=
selected comparison document represented in retrieved context
```

A quote-review drafter cannot compare the quote when no quote chunk reaches it.

The existing `DeterministicDrafter` is also deliberately non-analytic and produced zero explicit professional claim types. That is a second known limitation, but this run does not justify correcting it before the upstream context coverage defect.

### Recommendation

The next #827 slice should stay inside the existing retrieval owner and qualify a bounded source-coverage rule for comparative review:

- preserve the existing exact source identities and RRF ranking;
- do not merely increase `top_k` blindly;
- ensure that intentionally selected comparison sources can each contribute candidate context before remaining slots are filled by global ranking;
- keep the behavior opt-in/bounded so generic retrieval semantics are not silently changed;
- retain source/digest/currentness provenance and all existing authority boundaries.

Only after all comparison sources are represented should the professional-method/drafter seam be evaluated against the seven attention cases.

## Baseline test posture

The permanent test is an observer plus hard-boundary regression. It must not freeze the current defect as desired behavior.

It therefore protects:

- exact selected-source resolution;
- exclusion of the planted revision-A control;
- no Evidence-source leakage outside the qualification perimeter;
- no forbidden professional/contractual claim;
- no external authorization;
- no authority widening by scope resolution.

It measures, but does not require, the current number of professional findings or the completeness of retrieval source coverage. Improvements must be allowed to improve those observations without breaking the baseline regression.

## Review hardening

Two PR review findings identified test-integrity issues and were corrected before merge:

1. a configured CI database/schema failure must fail loudly rather than be converted to a local-environment skip;
2. repeated qualification runs must not collide with a previously persisted fixed `devis_reprise` project.

The final test therefore:

- converts only an unconfigured local `psycopg.OperationalError` into `pytest.skip`;
- re-raises configured connection failures and every migration/schema/permission failure;
- clones the base Task Contract into a unique qualification-only `project_id` / dossier namespace for each execution;
- keeps `devis_reprise` unchanged as the human-labelled corpus identity and source oracle;
- preserves the same declared source refs and governance boundary.

After this hardening, Governance CI, Architecture Audit and Obsolete Authority were green, and the PostgreSQL-backed implementation suite passed again on the hardened branch head.

```text
isolated test namespace != new governed dossier identity
corpus identity != persistence namespace used by one qualification run
configured DB failure != optional local dependency
```

## Boundaries

```text
currentness resolved != professional approval
retrieved context != truth
retrieval coverage != Evidence admission
runtime output != Evidence
baseline green != professional value demonstrated
human oracle != automatic approval authority
```

No ACT engine, schema, provider binding, parser, Role, Rite, governed Space, Evidence owner, generic eval framework or new professional taxonomy is created by this slice.

## Status

Baseline behavior is now observed and reproducible.

The current #827 question is no longer “which layer might fail first?” The first observed correction layer is retrieval coverage across intentionally selected comparison documents.
