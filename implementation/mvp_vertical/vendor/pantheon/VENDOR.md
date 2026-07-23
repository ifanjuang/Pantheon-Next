# Vendored governance artifacts (from Pantheon-Next)

This directory is a **read-only snapshot** of a small, explicit subset of
[`ifanjuang/Pantheon-Next`](https://github.com/ifanjuang/Pantheon-Next). MVP is
an external executable candidate; it consumes governance shapes, it never edits
this copy and pushes nothing back. The dependency is one-way — MVP depends on
Next, never the reverse.

The exact upstream commit is pinned in [`UPSTREAM_COMMIT`](./UPSTREAM_COMMIT).

## What is vendored, and from where

| Vendored file | Upstream source (at the pinned commit) | Kind |
|---|---|---|
| `mvp_governed_loop_objects.schema.yaml` | `schemas/mvp_governed_loop_objects.schema.yaml` | verbatim copy |
| `document_knowledge_slice.schema.yaml` | `schemas/document_knowledge_slice.schema.yaml` | verbatim copy |
| `work_issue_slice.schema.yaml` | `schemas/work_issue_slice.schema.yaml` | verbatim copy |
| `decision_vocabulary.stand_in.yaml` | **derived**, not copied — mirrors `$defs.decision_value.enum` of `mvp_governed_loop_objects.schema.yaml` | derived |

The three `*.schema.yaml` files map to `schemas/<name>` upstream — the
convention `tools/check_schema_drift.py` relies on. `decision_vocabulary.stand_in.yaml`
has no direct upstream file: it is the gate's authority (a single small file to
read so decision semantics cannot be driven by the candidate stream) and must
equal the schema's `$defs.decision_value` enum. If the two ever diverge the
schema is authoritative and the vocabulary must be re-synced.

Nothing else from upstream is vendored. Notably, no upstream `*.py` is carried
here: MVP validates against the vendored **schemas**, not against upstream
scripts.

## How drift is watched

- `tools/check_schema_drift.py` (scheduled, report-only — `.github/workflows/schema-drift.yml`)
  compares each vendored `*.schema.yaml` against upstream `main` structurally,
  and — offline — checks that `decision_vocabulary.stand_in.yaml` still matches
  the vendored schema's `$defs.decision_value` enum.
- A new commit upstream is INFO, not drift. Only a structural schema change, or
  a vocabulary that no longer mirrors the enum, is reported as drift.

## How to re-vendor

Run `tools/revendor.sh <commit-sha>` (see that script). It fetches the three
schemas at the given commit, rewrites `UPSTREAM_COMMIT`, and reminds you to
re-check the derived vocabulary. Re-vendoring is a reviewed change, never an
automatic one: after it, reconcile any emitted-shape changes and run the tests.
