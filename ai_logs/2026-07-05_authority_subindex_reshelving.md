# AI Log — Authority Sub-Index Re-Shelving After Review

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Context

After PR #287 (authority index decomposition) merged, the assistant
flagged its own placement judgment calls for human review and offered to
re-shelve the debatable ones. The user answered "Vas-y fais ça" — an
explicit, dated human decision to apply the flagged re-shelving.

## Changes made

```text
Moved verbatim from RUNTIME_ADAPTERS_AUTHORITY_INDEX.md to
GOVERNANCE_AUTHORITY_INDEX.md (a re-shelving note appended to each row):

- docs/governance/EXTERNAL_RUNTIME_THREAT_MODEL_REVIEW.md
  Reason: tool-agnostic review method; the adapters map is for
  tool-specific material. Sits with the other method/review doctrine.

- docs/governance/TRIPARTITE_INTERFACE_SPEC.md
  Reason: tool-agnostic interface grammar for the three system roles
  (exposure / execution / governance); kernel material, not an adapter
  placement note.

Deliberately left in place after the same review:

- EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md stays in the adapters map (its
  subject is the adapter boundary itself; the master index keeps the
  external runtime memory adapter rule).
- BOOTSTRAP_INSTALLATION_LADDER.md and NAS_INSTALLATION_PROFILES.md stay
  in the kernel (orientation documents, not implementation artifacts).
- ARCHITECTURAL_PROJECT_GRAPH.md stays in the architecture map.
```

## Boundary

```text
Placement only; no authority class or repo state changed; rows moved
verbatim plus a re-shelving note. No script, schema, test, operation,
platform, Docker, pyproject or .env change. Sub-index Status headers
remain candidate/awaiting review: this re-shelving does not promote
the maps.
```
