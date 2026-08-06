# Vendored governance artifacts (from Pantheon-Next)

This directory is a **read-only snapshot** of a small, explicit subset of
[`ifanjuang/Pantheon-Next`](https://github.com/ifanjuang/Pantheon-Next). MVP is
an external executable candidate; it consumes governance shapes, it never edits
this copy and pushes nothing back. The dependency is one-way — MVP depends on
Next, never the reverse.

Every vendored file carries its own provenance sidecar, `<name>.source.json`,
recording the upstream commit, the upstream blob sha and the sha256 of the bytes
on disk. That per-file record is the authority: it is verified by
`tests/test_vendored_contract_conformance.py`, and a schema without one has no
recorded origin at all.

The four older pin files, `UPSTREAM_COMMIT`, `PROJECT_CLAIM_UPSTREAM_COMMIT`,
`WORK_ISSUE_SCOPE_UPSTREAM_COMMIT` and `DECISION_REQUEST_UPSTREAM_COMMIT`, predate
the sidecars. Their separation still records something true — adding a later
contract does not imply that an older aggregate was re-reviewed — but a pin file
states one commit for a whole lineage, and the schemas here come from many
different commits, most of which the pin files cannot express at all. They also
carry no digest, so a pin cannot be checked against the bytes it claims to
describe.

`UPSTREAM_COMMIT` named `f8bc3bd` until 2026-08-06. Its *content* was right — the
three schemas it covers are byte-identical there — but that commit sits on the
retired predecessor history and has **no merge-base with the current `main`**, so
it could not be resolved upstream and the drift monitor reported a HEAD/pin gap on
every run that had nothing to do with upstream moving. It now names `e9c237bb`,
which is on the current history and carries the same bytes.

Where a pin file and a sidecar disagree, the sidecar wins: it names one file, and
its digest makes the claim checkable.

## What is vendored, and from where

| Vendored file | Upstream source | Kind |
|---|---|---|
| `mvp_governed_loop_objects.schema.yaml` | `schemas/mvp_governed_loop_objects.schema.yaml` | verbatim copy |
| `document_knowledge_slice.schema.yaml` | `schemas/document_knowledge_slice.schema.yaml` | verbatim copy |
| `work_issue_slice.schema.yaml` | `schemas/work_issue_slice.schema.yaml` | verbatim copy |
| `work_issue_scope_link.schema.yaml` | `schemas/work_issue_scope_link.schema.yaml` | verbatim copy |
| `decision_request.schema.yaml` | `schemas/decision_request.schema.yaml` | verbatim copy |
| `project_claim.schema.yaml` | `schemas/project_claim.schema.yaml` | verbatim copy |
| `navigation_registry.schema.yaml` | `schemas/navigation_registry.schema.yaml` | verbatim copy |
| `tag_registry.schema.yaml` | `schemas/tag_registry.schema.yaml` | verbatim copy |
| `source_intake_admission.schema.yaml` | `schemas/source_intake_admission.schema.yaml` | verbatim copy |
| `information_card_projection.schema.yaml` | `schemas/information_card_projection.schema.yaml` | verbatim copy |
| `knowledge_edit_variant_candidate.schema.yaml` | `schemas/knowledge_edit_variant_candidate.schema.yaml` | verbatim copy |
| `decision_vocabulary.stand_in.yaml` | **derived**, not copied — mirrors `$defs.decision_value.enum` of `mvp_governed_loop_objects.schema.yaml` | derived |

Every vendored `*.schema.yaml` maps to `schemas/<name>` upstream. This is the
convention `tools/check_schema_drift.py` relies on. `decision_vocabulary.stand_in.yaml`
has no direct upstream file: it is the gate's authority (a single small file to
read so decision semantics cannot be driven by the candidate stream) and must
equal the schema's `$defs.decision_value` enum. If the two ever diverge the
schema is authoritative and the vocabulary must be re-synced.

No upstream `*.py` is carried here: MVP validates against the vendored
**schemas**, not against upstream scripts. `mvp_vertical/vendor_contracts.py`
loads them and refuses a non-conforming payload; conformance is not adoption,
approval or authority transfer.

## How drift is watched

- `tools/check_schema_drift.py` (scheduled, report-only — `.github/workflows/schema-drift.yml`)
  compares each vendored `*.schema.yaml` against upstream `main` structurally,
  and — offline — checks that `decision_vocabulary.stand_in.yaml` still matches
  the vendored schema's `$defs.decision_value` enum.
- A new commit upstream is INFO, not drift. Only a structural schema change, or
  a vocabulary that no longer mirrors the enum, is reported as drift.

## How to re-vendor

- `tools/revendor.sh <commit-sha>` refreshes the established governed-loop,
  document and work schemas and rewrites `UPSTREAM_COMMIT`.
- `tools/revendor_project_claim.sh <commit-sha>` refreshes only
  `project_claim.schema.yaml` and rewrites `PROJECT_CLAIM_UPSTREAM_COMMIT`.
- WorkIssue scopes and Decision Requests are currently reviewed as explicit
  one-file copies with dedicated pins; helpers may be added only if these
  contracts begin to change frequently.

All are reviewed changes, never automatic ones. After any refresh, inspect the
diff, reconcile emitted shapes and run the tests.
