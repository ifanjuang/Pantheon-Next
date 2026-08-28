# OpenWebUI method/autonomy final convergence — 2026-08-28

## Objective

Complete #785 from merged main `5f45c2bdfaa76fe8af70598f6d6be8d6c72a877b` by reviewing the final two machine-tracked current-authority residues and reducing the allowlist from 2 paths to zero.

## Scope

- `docs/governance/GOVERNED_AUTONOMY_GRADIENT.md`
- `docs/governance/GOVERNED_METHOD_STANDARD.md`
- `tests/test_openwebui_integration_owner_retirement.py`

The only other open pull requests observed before the slice were Dependabot CI updates #721 and #722. They do not overlap the governance-document scope.

## Observed need

Both remaining documents still contained the same present-tense global ownership block:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Full-document review confirmed that their other OpenWebUI mentions are explicit non-implementation/exclusion statements (`OpenWebUI function` / `OpenWebUI plugin`), not current architecture ownership claims.

## Owner review

`GOVERNED_METHOD_STANDARD.md` remains the owner of the reusable governed professional method: Frame -> Admit -> Qualify -> Compose -> Produce Candidate -> Test -> Status.

`GOVERNED_AUTONOMY_GRADIENT.md` remains its complementary owner for the freedom/gate envelope across those movements.

`HERMES_INTEGRATION.md` remains the stable owner of runtime-client, Hermes/external-runtime, PDP/PEP and Pantheon Cockpit placement. The two method documents inherit that boundary rather than restating a product-specific client owner.

No owner merge, new abstraction, runtime client selection or #787 documentation-topology consolidation is performed.

## Convergence

In both documents the obsolete global product-binding block is replaced by the same inherited boundary:

- optional compatible runtime clients expose runtime interaction only;
- Hermes/the external runtime executes admitted work as PEP;
- Pantheon Cockpit projects governed state;
- Pantheon policy/governance remains the bounded PDP authority.

The machine-tracked residue constant is now a real empty Python set:

```python
KNOWN_CURRENT_AUTHORITY_OPENWEBUI_RESIDUES = set()
```

Using `{}` would have created a dictionary and broken the set-difference regression logic, so the explicit `set()` form is intentional.

## Preserved distinctions

```text
retrieved != truth
memory != Evidence
runtime success != authorization
runtime output != Evidence
PDP decision != PEP execution
projection != persistence
client selected != governance authority
method discipline != runtime workflow
autonomy envelope != execution authority
```

## Migration and rollback

Documentation and regression only. No client, runtime, Cockpit, bridge, connector, Revit integration, schema, policy implementation or persistent state changes. Rollback is a normal Git revert.

## Role / Rite / Space

- Role: THEMIS for authority boundaries, MNEMOSYNE for continuity, ATHENA for method coherence.
- Rite: Concordance des sources across exact main, #785, the zero-residue regression and `HERMES_INTEGRATION.md`.
- Space: Pantheon Next governance repository.

These labels describe review context only and create no runtime state.

## Truncation / full-file verification

Both documents were read through EOF from the exact base before editing. The final compare before this log showed:

```text
GOVERNED_AUTONOMY_GRADIENT.md  +1 / -5
GOVERNED_METHOD_STANDARD.md    +2 / -6
regression test                 +1 / -4
```

The method document's second changed line is EOF newline normalization only. No method movement, autonomy level, Revit example, rule, table or boundary section was truncated. `.github/scripts/truncation_ack.txt` remains unchanged.

## Done rule

This slice is not complete merely because the allowlist text is empty. It may merge only when Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final HEAD, the final PR patch is read, and all reviews/threads/comments are resolved or explicitly addressed.

After merge, `main` must be re-read to confirm the allowlist remains zero and no new current-authority offender appears. Only then may #785 be closed.