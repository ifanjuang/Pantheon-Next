# AI Log — Authority Index Full Decomposition (checker extension + PR D/E)

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Context

Explicit user approval ("Vasy") in the same session, in response to the
offer to prepare the `.github/scripts/check_index_coverage.py` extension
that the remaining migration groups were blocked on. This completes the
sequence of `docs/governance/AUTHORITY_INDEX_DECOMPOSITION_PLAN.md`:
the checker extension (the step §7 required approval for), the remaining
PR D groups and the PR E master reduction, on the same branch/PR (#287)
as the first migration commit.

## Changes made

```text
1. .github/scripts/check_index_coverage.py (approved script change):
   coverage now reads AUTHORITY_INDEX.md plus every *.md under
   docs/governance/authority/ (at the working tree and at the baseline
   ref). A candidate doc counts as indexed when mentioned in the master
   or any sub-index; grouped rows in either provide coverage; the
   missing-path validation spans the combined text. Negative test run:
   an unindexed candidate doc still fails the check.

2. .github/scripts/truncation_ack.txt: added
   docs/governance/AUTHORITY_INDEX.md as the documented deliberate-split
   acknowledgment for check_no_net_truncation.py (423 -> 320 lines vs
   origin/main sits at the 75%-kept boundary).

3. Row migration (verbatim, no class or state changed):
   - GOVERNANCE_AUTHORITY_INDEX.md: 52 governance-kernel rows,
     including the grouped rows docs/governance/DATA_PLATFORM_*.md and
     docs/governance/rites/.
   - RUNTIME_ADAPTERS_AUTHORITY_INDEX.md: 13 adapter rows (Hermes,
     MCP, Nango, PaddleOCR, Page-Agent, Understand-Anything,
     tripartite interface, refusal fixtures, external runtime
     threat-model/memory boundaries).
   - IMPLEMENTATION_ARTIFACTS_AUTHORITY_INDEX.md: 13 artifact and
     protected-path rows (mcp-server/, docs/assets/pantheon-control/,
     base_metier/architecte/, templates/, examples/, ai_logs/ and the
     protected paths). Status visibility only; relaxes no protected
     path.
   - ARCHITECTURE_AUTHORITY_INDEX.md: added the three Revit Gate docs,
     ARCHITECTURAL_PROJECT_GRAPH.md and the grouped row
     docs/domain-packs/architecture/ (moved from the master).
   - EXTERNAL_REFERENCES_AUTHORITY_INDEX.md: added the grouped row
     docs/governance/reference_reviews/ (movable now that grouped
     coverage spans sub-indexes).

4. AUTHORITY_INDEX.md reduced per plan PR E (423 -> 320 lines): keeps
   the authority classes, promotion rule, a two-row anchor map (this
   file + the authority/ grouped row), the sub-index map, bootstrap
   stub rule, placement test, tool naming rule, terminology boundary
   rule, domain pack rule, external runtime memory adapter rule, data
   platform rule and the sensitive-path guardrail (tail and
   end-sentinel untouched; still above the 300-line MANIFEST floor of
   check_no_truncation.py, left unchanged).
```

## Classification judgment calls (placement only, no class change)

```text
ARCHITECTURAL_PROJECT_GRAPH.md -> architecture map (domain subject).
EXTERNAL_RUNTIME_THREAT_MODEL_REVIEW.md and
EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md and TRIPARTITE_INTERFACE_SPEC.md
-> runtime adapters map (external runtime / interface subjects).
BOOTSTRAP_INSTALLATION_LADDER.md and NAS_INSTALLATION_PROFILES.md
-> governance kernel (orientation docs, not artifacts).
Any of these may be re-shelved by review; placement moves no authority.
```

## Verification

```text
All eight local governance checks pass with
GOVERNANCE_BASE_REF=origin/main (coverage, internal links, truncation,
net truncation, status headers, axis vocabulary, register instances,
vertical slice). Negative coverage test: a temporary unindexed
candidate doc fails the check, then passes after removal.
check_apu_referential_integrity remains a local-environment failure
(missing jsonschema) identical on the clean tree.
```

## Boundary

```text
Script change was explicitly user-approved in-session.
No schema, test, operation, platform, Docker, pyproject or .env change.
No authority class changed; no candidate promoted; rows moved verbatim.
The master index remains the single authority interpreter.
```
