# Governance documentation topology — method boundary deduplication — 2026-08-29

## Objective

Start #787 from exact merged `main` `f0ed52efa784fe479dfe03cd25be1e0937360564` with a low-risk convergence slice in the governed-method family. Reuse the existing `BOUNDARY_PROFILES.md`, `STATUS_HEADER_RULES.md`, `NON_EQUIVALENCE_RULES.md` and `HERMES_INTEGRATION.md` owners to reduce repeated boundary boilerplate before deciding whether any method-family document should be absorbed or reclassified.

## Scope

- `docs/governance/REQUEST_LIFECYCLE.md`
- `docs/governance/DOSSIER_SITUATION_INTAKE.md`
- `docs/governance/ADAPTIVE_REQUEST_METHOD.md`

No schema, test, CI, runtime, implementation, index placement or authority class is changed by this slice.

## Repository checks

Before editing:

- #785 was closed/completed with zero machine-tracked current-authority OpenWebUI residues;
- `main` was `f0ed52efa784fe479dfe03cd25be1e0937360564`;
- only Dependabot PRs #721 and #722 were open and neither overlaps governance Markdown;
- `AUTHORITY_INDEX.md`, `GOVERNANCE_AUTHORITY_INDEX.md`, `STATUS_HEADER_RULES.md`, `BOUNDARY_PROFILES.md` and `NON_EQUIVALENCE_RULES.md` were re-read;
- the governed-method family named by #787 was read through EOF before selecting this slice.

## Observed need

The three selected active-support documents repeated the same generic negative boundary in slightly different forms: no runtime, no scheduler, no queue, no memory engine, no approval engine and no authority transfer from a client or execution runtime. Those rules already have explicit owners.

The repeated text creates maintenance surface without adding local responsibility.

## Existing owners checked

- `BOUNDARY_PROFILES.md` already defines `active_support_doctrine` specifically to reduce repeated non-runtime boilerplate.
- `STATUS_HEADER_RULES.md` already defines the separate `Boundary profile:` line and normalized repo-state wording.
- `NON_EQUIVALENCE_RULES.md` already owns recurring status-collapse distinctions.
- `HERMES_INTEGRATION.md` already owns the runtime-client / Hermes / PDP / PEP / Cockpit boundary.

No new documentation framework, front matter, YAML registry, invariant taxonomy or ADR subsystem is introduced.

## Historical convergence precedent

Repository history contains commit `1abd2bfffbd3d5e6a4734f0f2bc3a547e2d675b2` (`docs: governance cleanup pass B — absorb 13 satellites into mother docs`). That approved cleanup used mother-document absorption, repo-wide reference rewrites, redundant-index-row removal and Git history as provenance. It also deliberately left files untouched when no valid mother owner existed.

This slice does not perform an absorption yet. It uses the same owner-first principle and prepares the family for a later responsibility-based decision.

## Overlap analysis

The method-family audit recorded in #787 currently finds:

- `GOVERNED_METHOD_STANDARD.md` retains the generic professional-method responsibility;
- `GOVERNED_AUTONOMY_GRADIENT.md` retains the complementary autonomy envelope;
- `WORKFLOW_FORGING_PROTOCOL.md` retains a distinct Approach → runtime-facing Workflow Candidate handoff responsibility for now;
- `PRE_EXECUTION_SIMULATION.md` remains a specialization whose independent-owner need still requires review;
- `REQUEST_LIFECYCLE.md`, `ADAPTIVE_REQUEST_METHOD.md` and `DOSSIER_SITUATION_INTAKE.md` overlap materially around request framing, admission, context and qualification;
- `DOSSIER_SITUATION_INTAKE.md` is the narrowest owner and remains the first likely absorption candidate, but no deletion is authorized by this PR.

## Changes

For each selected document:

1. normalize the `Status:` line to include a repository state where needed;
2. add `Boundary profile: active_support_doctrine.`;
3. remove only the generic repeated non-runtime disclaimer;
4. replace repeated runtime/client architecture prose with a short reference to `HERMES_INTEGRATION.md`;
5. retain locally material boundaries and all substantive method/intake/lifecycle content.

No role, gate, source class, status, candidate shape, method rule or workflow rule is removed.

## Affected consumers

Documentation maintainers, authority-map reviewers and future #787 consolidation slices. No runtime consumer changes because these files remain documentation-only.

## Migration and rollback

Documentation-only convergence. No migration, deployment, persistence, provider, client, runtime or external-system change exists. Rollback is a normal Git revert.

## Role / Rite / Space

- Role: MNEMOSYNE for owner continuity, ATHENA for method-family composition, THEMIS for authority-boundary review.
- Rite: Concordance des sources across exact `main`, #787, the authority indexes and the existing deduplication owners.
- Space: Pantheon Next governance repository.

These labels describe review context only and create no runtime state.

## Authority impact

None. All three documents remain `active support doctrine`; their current distinct responsibilities are preserved. `HERMES_INTEGRATION.md` remains the integration-boundary owner. No runtime client, Role, Gate or Workflow Candidate is promoted by this slice.

## Runtime impact

None. No execution, scheduler, queue, provider routing, client, Cockpit, policy service, connector, memory, approval or external action behavior changes.

## Preserved invariants

```text
retrieved != truth
memory != Evidence
runtime success != authorization
runtime output != Evidence
projection != persistence
PDP decision != PEP execution
client selected != governance authority
boundary profile != authority transfer
method doctrine != runtime workflow
```

## Truncation / full-file verification

All three selected documents were read through EOF from the exact base before replacement. Compare after the three edits shows:

```text
ADAPTIVE_REQUEST_METHOD.md      +5 / -8
DOSSIER_SITUATION_INTAKE.md     +4 / -7
REQUEST_LIFECYCLE.md            +5 / -6
```

Only status/profile/boundary wording changed. No substantive section was deleted.

## Verification rule

The PR must be reviewed by patch and pass Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency on its exact final HEAD. Any later modification invalidates prior check evidence. Reviews, threads and comments must be read before merge.

After this slice, #787 should test `DOSSIER_SITUATION_INTAKE.md` against the established mother-document absorption precedent rather than mechanically merging the entire method family.