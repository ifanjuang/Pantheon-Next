# 2026-07-09 — Pantheon MVP Vertical binding review

Status: validation-only trace.

Boundary profile: validation_only_trace.

## What changed

Added a Pantheon-side review and classification for the external `pantheon-mvp-vertical` bundle.

Files added:

```text
docs/governance/PANTHEON_MVP_VERTICAL_BINDING.md
docs/governance/reference_reviews/PANTHEON_MVP_VERTICAL_REVIEW.md
```

Files updated:

```text
docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
docs/governance/reference_reviews/README.md
```

## Observed bundle facts

The local bundle was inspected without importing its executable code into Pantheon Next.

Observed facts:

```text
commit: 4ce16b7
subject: feat: Block 1 of the Pantheon MVP governed task loop
tracked files: 19
vendored Pantheon commit: 58d6bef
package: mvp_vertical
fixture: dossiers/devis_reprise
tests file: tests/test_block1.py
```

The bundle includes a CI definition with pgvector and a six-test acceptance suite. Those are useful runtime signals, not Pantheon-validated evidence by themselves.

## Why

The bundle is a plausible external executable binding for a bounded Block 1 governed task loop:

```text
Task Contract loading
bounded source ingestion
SQL-scoped retrieval before vector ranking
result_candidate output
evidence_pack_candidate output
forbidden-scope refusal
outside-perimeter refusal
```

Pantheon Next should govern it as an external candidate binding rather than absorb it as an internal runtime.

## Boundary

This intervention does not:

```text
import executable code into Pantheon Next
create a runtime
install the external repo
run the external repo
approve adoption
approve activation
approve external send
write memory
validate professional evidence
modify protected implementation paths
```

## Review findings

Adoption is blocked pending P0 fixes:

```text
Task Contract schema alignment
Task Contract fixture validation test
canonical path-boundary checks
path traversal refusal tests
fixture-specific runner label
```

P1 follow-ups:

```text
unit tests without pgvector
GOVERNANCE_STATUS.md in the external repo
vendored upstream freshness check
external CI verification after publication
```

## Status classification

```text
implemented in Pantheon Next:
  none.

documented non-implemented in Pantheon Next:
  binding classification, external review, adoption gates.

external executable candidate:
  pantheon-mvp-vertical bundle.

adoption:
  blocked pending P0 fixes and human approval.
```
