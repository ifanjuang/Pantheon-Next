# Modules

Status: active support doctrine — governance-area ownership map — implemented as documentation.
Boundary profile: active_support_doctrine.

Pantheon Next modules are governance areas, not runtime packages.

```text
module != plugin
module != worker
module != runtime service
module != scheduler or queue
module != provider router
module != automatic authority
```

Current operating boundary:

```text
Hermes clients handle runtime interaction.
Hermes Agent executes externally.
Pantheon Cockpit exposes governed projections.
Pantheon Next governs consequential status.
The human decides.
```

## Canonical module map

| Governance area | Current owner(s) | Boundary |
|---|---|---|
| Repository status | `STATUS.md`, `WHAT_RUNS.md`, `AUTHORITY_INDEX.md` | Describes state; creates no runtime/adoption. |
| Core concept navigation | `CORE_CONCEPTS_MAP.md` | Navigation/ownership entry point only. |
| Architecture direction | `ARCHITECTURE.md`, `TARGET_ARCHITECTURE.md`, `ECOSYSTEM_MAP.md` | Architecture/governance composition; no runtime instantiation. |
| Terminology and non-equivalence | `TERMINOLOGY_BOUNDARIES.md`, `GLOSSARY.md`, `NON_EQUIVALENCE_RULES.md` | Vocabulary/semantic boundaries only. |
| Roles / governance college | `AGENTS.md`, `GOVERNANCE_COLLEGE.md`, `ROLE_SIGNALS.md` | Roles judge; they are not autonomous agents. |
| Rites / methods | `rites/README.md`, `METHOD_TAXONOMY.md`, related method owners | Bounded governance method; not workflow execution. |
| User decision | `USER_DECISION_GATE.md` | Exposes consequential choice; not automatic approval. |
| Task Contracts | `TASK_CONTRACTS.md` | Bounds work; does not start or approve execution. |
| Context | `CONTEXT_PACKS.md`, `CONTEXT_STACK.md` | Bounded context/projection; not memory or proof. |
| Evidence | `EVIDENCE_PACK.md`, `EVIDENCE_TOPOLOGY.md` | Reviewable support; not runtime logs or approval. |
| Approvals | `APPROVALS.md` | Legitimacy decision; runtime success is not approval. |
| Register / durable governed assertions | `MEMORY.md` and existing Register contracts | Governed durable promotion only; runtime memory remains separate. |
| Knowledge | `KNOWLEDGE_TAXONOMY.md`, RAG boundary owners | Consultable material; retrieval is not truth/Evidence. |
| Workspace / derived recall | `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` | Obsidian = Markdown workspace; Hindsight = derived recall; neither owns professional truth. |
| Document/source lifecycle | `DOCUMENT_LIFECYCLE_GOVERNANCE.md` and related source contracts | Exact source/provenance and derived representation boundaries; no required DMS product. |
| Pantheon Cockpit product composition | `PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md` | Governed projection/product composition; not a general-purpose chat runtime. |
| Card grammar | `CARD_STACK_MODEL.md` | Generic Card/Scene/Deck/Constellation presentation grammar. |
| Card projection mapping | `CARD_PROJECTION_DEFINITION_MODEL.md` + executable registry where present | Machine-readable mapping into renderer; does not own root topology or business rules. |
| Capability placement | `CAPABILITY_PLACEMENT.md`, `UNIFORM_CAPABILITY_GOVERNANCE.md` | Common governance/placement; does not install or execute. |
| Capability binding/activation | existing binding, activation and passport contracts | Selected implementation and eligibility remain distinct from task authorization. |
| Hermes execution integration | `HERMES_INTEGRATION.md`, Task Contract/admission owners | Hermes executes externally; no self-approval or automatic Evidence promotion. |
| External client selection | `EXTERNAL_TOOLS_POLICY.md`, `EXTERNAL_TOOL_PLACEMENT_REGISTER.md` | Clients remain replaceable; compatibility is not architecture authority. |
| External tools/connectors | `EXTERNAL_TOOLS_POLICY.md`, `ADAPTERS_AND_BINDINGS.md` | External capability surfaces under least-capability/governed boundaries. |
| Domain packs | `DOMAIN_PACK_SPEC.md` and domain-pack owners | Professional constraints/methodology configuration; not professional authority. |
| Architecture Project Understanding | existing APU schema and validator owners plus domain owners | Structural validation only; no professional canonization. |
| MCP/policy verification | `MCP_PANTHEON_MINIMAL_PROFILE.md`, `mcp-server/docs/HTTP_API_CONTRACT.md`, `mcp-server/` | Bounded read-only policy/verification service; no effect execution. |
| Governance CI | `GITHUB_REPOSITORY_GOVERNANCE.md`, `.github/` checks | Read-only enforcement of repository contracts; green CI is not approval. |
| Co-located candidate implementation | `implementation/` + `NEXT_MVP_REPOSITORY_PLACEMENT.md` | Executable candidate behavior; co-location does not transfer governance authority or adoption. |
| External references/distillation | `WATCHLIST.md`, `REFERENCE_BOUNDARIES.md`, `DISTILLATION_REGISTRY.md`, `REJECTED_PATTERNS.md` | Observe/distil/refuse; reference review is not adoption. |

## Selected interaction and workspace composition

```text
Hermes Web/dashboard
  baseline chat/session/runtime-control client

compatible Hermes mobile/PWA
  optional replaceable client after separate verification

Pantheon Cockpit
  governed status/navigation/review projection

Obsidian
  human Markdown workspace and editable working projections

Hindsight / Hermes memory
  optional derived/runtime recall
```

These are responsibilities, not a single merged product.

## Refused historical product paths

### OpenWebUI

OpenWebUI is no longer a governance module or target dependency.

Its former responsibilities have converged into:

```text
runtime interaction -> Hermes clients
governed projection -> Pantheon Cockpit
workspace/notes      -> Obsidian where appropriate
execution            -> Hermes Agent
```

`OPENWEBUI_INTEGRATION.md` remains only as a refused transition pointer until active references and historical compatibility code are retired.

### Paperless-ngx

Paperless is no longer a governance module, preferred binding or target dependency.

Its useful generic concerns remain with existing document/source owners. Core local/NAS ingestion does not require a DMS product, and Obsidian does not become a DMS by replacing Paperless in the selected stack.

`PAPERLESS_NGX_DOCUMENT_RUNTIME.md` remains only as a refused transition pointer until active references and historical compatibility code are retired.

## Module rule

A governance module may define:

- scope and authority;
- vocabulary;
- Evidence/approval expectations;
- capability constraints;
- memory/Register rules;
- schemas or read-only checks where useful.

It must not silently define:

- execution workers;
- hidden orchestration;
- provider routing;
- autonomous scheduling/queues;
- automatic external effects;
- automatic memory promotion;
- a second registry or plugin marketplace.

## Placement test

Before adding a new module or document:

```text
1. Which existing owner already covers this responsibility?
2. Is the proposed responsibility genuinely distinct?
3. Can an existing owner be extended/simplified instead?
4. Is a machine contract/test better than repeated prose?
5. What is the convergence/retirement path?
```

Default: reuse and consolidate.

## Final boundary

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
folder != governed identity
client selected != governance owner
```

Pantheon governs consequential status without absorbing the runtime, clients, workspace or source systems it does not need to own.
