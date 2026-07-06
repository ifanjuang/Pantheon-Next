# Pantheon Next — Implementation Artifacts Authority Index

Status: candidate support map — populated (implementation-artifacts migration group); awaiting review.

This sub-index carries the implementation-artifact and protected-path rows migrated out of the Current authority map of `docs/governance/AUTHORITY_INDEX.md`, per `docs/governance/AUTHORITY_INDEX_DECOMPOSITION_PLAN.md` (PR D/E, after the coverage checker was extended to read sub-indexes). It stays conservative: it continues to distinguish implemented, implemented read-only, partial, protected path and documented non-implemented.

It does not override the authority vocabulary, promotion rule, placement test, tool naming rule, terminology boundary rule or sensitive-path guardrail of `docs/governance/AUTHORITY_INDEX.md`. The master index defines how to read authority; this file only lists where artifacts sit. Listing a protected path here is status visibility only — it relaxes no protected path; the sensitive-path guardrail in the master index still applies in full.

## Implementation artifacts map

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `mcp-server/` | implementation artifact / read-only verification surface | implemented read-only / partial / protected path | Bounded read-only MCP policy / verification surface (capability-passport validation and the install / observability / backup / exposure / update verifiers). Validates structure and status and returns status data only; must not execute, approve, send, schedule, queue, route providers, install, update, write external systems or promote memory. Implementation artifact, not authority; broader server coverage remains to verify. Changes are a protected path. |
| `docs/assets/pantheon-control/` | implementation artifact / static prototype | static prototype / partial read-only mirror / to verify | Static Pantheon Control prototype (the surface `CLAUDE.md` names `dashboard/`). Some logic mirrors read-only verification behaviour (including the update verifier after PR #239); it is not a live cockpit, approval engine, memory engine, runtime, sender, scheduler or provider router. Static prototype, not authority. |
| `revit-plugin/` | implementation artifact candidate / external adapter prototype | skeleton / documented non-implemented | Future local Revit 2027 adapter prototype folder. Current state is documentation and placeholder material only. It must not redefine Pantheon doctrine, approval, memory, proof or scope rules. |
| `base_metier/architecte/` | external professional corpus / to verify | documented non-implemented | Architecture professional RAG corpus (knowledge / skills / prompts / workflows). Candidate corpus, **not authority and not proof**. Source PDFs are kept out of git (`.gitignore`) with a reconstructible manifest at `knowledge/sources/SOURCES.manifest.yaml`; licence is to verify per source (MAF / Ordre des Architectes material is copyrighted). The two ingestion skills execute (PyMuPDF) and belong Hermes-side. Frozen pending the B-2 licence decision; do not ground a vertical slice on it until qualified. |
| `templates/` | support material / candidates | to verify | Non-executable scaffolds. Templates instantiate doctrine; they do not govern. |
| `examples/` | illustrative material | to verify | Fictional examples. They do not override doctrine. |
| `ai_logs/` | validation-only / trace | to verify | Intervention trace, not canonical doctrine. |
| `schemas/` | implementation artifact | protected path | Do not modify without explicit confirmation. |
| `tests/` | implementation artifact | protected path | Do not modify without explicit confirmation. |
| `operations/` | implementation / operational artifact | protected path | Spec first; no operations file before validated governing documentation. |
| `platform/` | implementation artifact | protected path | Do not modify without explicit confirmation. |
| `pyproject.toml` | packaging / implementation artifact | protected path | Do not modify without explicit confirmation. |
| `Docker*` | infrastructure / runtime artifact | protected path | Do not modify without explicit confirmation. |
| `.env*` | environment / secret boundary | protected path | Do not modify. |

## Boundary

This file moves rows; it decides nothing. Authority classes and repo states are copied verbatim from the master index at migration time. Any class change routes through its own reviewed PR against the master index rules.
