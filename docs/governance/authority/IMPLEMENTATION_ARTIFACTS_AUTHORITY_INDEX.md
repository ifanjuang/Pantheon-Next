# Pantheon Next — Implementation Artifacts Authority Index

Status: candidate support map — populated (implementation-artifacts migration group); awaiting review.

This sub-index carries the implementation-artifact and protected-path rows migrated out of the Current authority map of `docs/governance/AUTHORITY_INDEX.md`, per `docs/governance/AUTHORITY_INDEX_DECOMPOSITION_PLAN.md` (PR D/E, after the coverage checker was extended to read sub-indexes). It stays conservative: it continues to distinguish implemented, implemented read-only, partial, protected path and documented non-implemented.

It does not override the authority vocabulary, promotion rule, placement test, tool naming rule, terminology boundary rule or sensitive-path guardrail of `docs/governance/AUTHORITY_INDEX.md`. The master index defines how to read authority; this file only lists where artifacts sit. Listing a protected path here is status visibility only — it relaxes no protected path; the sensitive-path guardrail in the master index still applies in full.

## Implementation artifacts map

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `mcp-server/` | implementation artifact / read-only policy, verification and consultation surface | implemented read-only / partial / protected path | Contains one transport-neutral `PantheonPolicyService`, a local stdio MCP projection and an authenticated internal HTTP policy/preflight projection. It serves governed sources, explains allowlisted placement, classifies requests, evaluates candidate-work preflight, prepares candidate contracts/evidence, validates governed structures and classifies caller-provided evidence. No live inventory, unrestricted runtime probe, private knowledge retrieval, scoped identity authority, external execution, approval store or remote MCP transport is implemented. It must not execute, approve, send, schedule, queue, route providers, install, update, write external systems or promote memory. Implementation artifact, not authority; deployment and live Hermes enforcement remain to verify. Changes are a protected path. |
| `mcp-server/docs/HTTP_API_CONTRACT.md` | implementation support contract / transport adapter boundary | implemented documentation for partial HTTP projection | Defines the authenticated internal HTTP policy/preflight contract, common response envelope, fail-closed consequential posture, Context Pack plan/validate split and legacy-route refusal. It grants no runtime, approval or deployment authority. |
| `Dockerfile.policy-api`, `compose.policy-api.yaml` | infrastructure / deployment candidate | implemented candidate / protected path / not activated | Hardened candidate deployment for `pantheon-policy-api` on external `ai-net`, with no host port, read-only checkout/filesystem, dropped Linux capabilities, no Docker socket and application-level bearer authentication. File presence is not installation, health, activation, approval or production authorization. |
| `docs/assets/pantheon-control/` | implementation artifact / static prototype | static prototype / partial read-only mirror / to verify | Static Pantheon Control prototype (the surface `CLAUDE.md` names `dashboard/`). Some logic mirrors read-only verification behaviour (including the update verifier after PR #239); it is not a live cockpit, approval engine, memory engine, runtime, sender, scheduler or provider router. Static prototype, not authority. |
| `revit-plugin/` | implementation artifact candidate / external adapter prototype | skeleton / documented non-implemented | Future local Revit 2027 adapter prototype folder. Current state is documentation and placeholder material only. It must not redefine Pantheon doctrine, approval, memory, proof or scope rules. |
| `base_metier/architecte/` | external professional corpus / to verify | documented non-implemented | Architecture professional RAG corpus (knowledge / skills / prompts / workflows). Candidate corpus, **not authority and not proof**. Source PDFs are kept out of git (`.gitignore`) with a reconstructible manifest at `knowledge/sources/SOURCES.manifest.yaml`; licence is to verify per source (MAF / Ordre des Architectes material is copyrighted). The two ingestion skills execute (PyMuPDF) and belong Hermes-side. Frozen pending the B-2 licence decision; do not ground a vertical slice on it until qualified. |
| `templates/` | support material / candidates | to verify | Non-executable scaffolds. Templates instantiate doctrine; they do not govern. |
| `examples/` | illustrative material | to verify | Fictional examples. They do not override doctrine. |
| `ai_logs/` | validation-only / trace | to verify | Intervention trace, not canonical doctrine. |
| `schemas/` | implementation artifact / validation contracts | partial / protected review required | Validation contracts may exist. They validate structure only; they do not execute, approve or promote doctrine by themselves. Do not modify without explicit confirmation. |
| `tests/` | implementation artifact / validation tests | implemented read-only / partial / protected path | Validation tests exist where present; exact coverage must be checked before relying on them. Tests do not promote doctrine or approve changes by themselves. Do not modify without explicit confirmation. |
| `operations/` | implementation / operational artifact | protected path | Spec first; no operations file before validated governing documentation. |
| `platform/` | implementation artifact | protected path | Do not modify without explicit confirmation. |
| `pyproject.toml` | packaging / implementation artifact | protected path | Do not modify without explicit confirmation. |
| `setup.py` | packaging rejection guard / implementation artifact | implemented explicit rejection / protected path | Refuses fallback setuptools build/install attempts at the non-distributable repository root. It defines no package, distribution or runtime. |
| `requirements-dev.txt` | development dependency manifest / implementation artifact | implemented support | Explicit root validation dependencies. Installing them does not install or distribute the repository root. |
| `CLAUDE.md` | repository instruction / operational guardrail | protected path | Repository operating instruction and protected-path boundary. Do not modify without explicit confirmation. |
| `.github/workflows/` and CI scripts | automation / validation infrastructure | protected path | GitHub Actions and CI scripts are protected. Do not modify without explicit confirmation. |
| `Docker*`, `compose*.yaml` | infrastructure / runtime artifact | protected path | Do not modify without explicit confirmation. A reviewed candidate file is not an activated deployment. |
| `.env*` | environment / secret boundary | protected path | Do not modify. |

## Boundary

This file moves rows; it decides nothing. Authority classes and repo states are copied verbatim from the master index at migration time. Any class change routes through its own reviewed PR against the master index rules.
