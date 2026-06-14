# External Tool Placement Register

Status: active support register — lightweight placement decisions for external tools, skills and products.

This register records placement decisions for external repositories and tools reviewed during Pantheon Next governance work.

It is a support register, not doctrine by itself.

It does not install dependencies, create a runtime, create a connector, create a Hermes skill, create an OpenWebUI plugin, approve a tool for production use or promote any output to proof or memory.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

External tools are useful, but they must not blur Pantheon's boundary.

This register answers one narrow question:

```text
Where does this external capability belong, and what must Pantheon govern if it is used?
```

Canonical placement remains governed by:

- `CAPABILITY_PLACEMENT.md`;
- `MODULAR_DOMAIN_REORIENTATION.md`;
- `DOMAIN_PACK_SPEC.md`;
- `EXTERNAL_TOOLS_POLICY.md`;
- `ADAPTERS_AND_BINDINGS.md`.

If this register contradicts those documents, the canonical governance documents win.

## Placement rule

For every external tool, skill, connector, workflow, module or product, ask:

```text
If this goes wrong, can it produce a false truth,
an unapproved external effect,
a wrong memory,
or an unauthorized action?
```

- No — it is a feature. Place it in the tool layer that is best at using it.
- Yes — Pantheon governs the decision, status, proof, approval, scope or memory. Execution still remains outside Pantheon.

Governing a capability is not implementing it.

## Reviewed external tools

| Tool / repository | Nature | Placement | Status | Risk | Decision Zeus | Repo state | Next action |
|---|---|---|---|---|---|---|---|
| `greensock/gsap-skills` | Official GSAP AI coding skill set for animation, timelines, ScrollTrigger and framework integration. | Hermes skill candidate, frontend / motion. | Candidate / to verify | Low | Accepté | Documented non implemented | Verify license, integration target and accessibility rules before use. |
| `sujan1-3/browser-eyes-mcp` | MCP browser inspection and control layer using Chromium / CDP operations such as screenshots, DOM, network, storage and interaction. | Hermes MCP skill candidate with privileged modes. | Candidate / to verify | Medium to high | Accepté with constraints | Documented non implemented | Define read-only, interactive and mutation modes; require scope and approval for mutation, interception, cookies, storage and sensitive sessions. |
| `rowboatlabs/rowboat` | Local-first AI coworker / external product with long-lived context, knowledge graph, local notes and tool integrations. | External reference, possible future adapter; not a Hermes skill and not Pantheon core. | Candidate / to verify | High if absorbed directly | À vérifier / À arbitrer | Documented non implemented | Study only as external reference for inspectable working memory and graph context; never import its memory as a Registre Probatoire entry without governed promotion. |
| `Dyalwayshappy/Spice` | Decision-layer runtime above agents, with Decision Cards, read-only perception, decision guidance, approval checkpoints, executor handoff, outcomes and decision memory. | External reference only. May inspire OpenWebUI decision surfaces and Pantheon handoff vocabulary. Not a Hermes default runtime and not Pantheon core. | Reference / to verify | Critical if absorbed as decision authority | Refusé dans le core; à vérifier as UX/method reference | Documented non implemented | Distill compatible patterns only: Decision Card, sources/why/details/json inspection, unsupported-semantics reporting, read-only perception and approval-gated handoff. Do not install as governance runtime. |
| `PaddlePaddle/PaddleOCR` | OCR and document parsing toolkit for PDFs, images, layout, tables and structured extraction. | Hermes document-extraction capability candidate. Dashboard may expose install, configure, health and logs; Hermes owns installation and execution; Pantheon has no dependency. | Candidate / to verify | Medium to high if OCR output is treated as truth | Accepté with constraints | Documented non implemented | Add as dashboard-installable Hermes-managed capability only. Benchmark on CERFA, mairie arrêté, devis, chantier CR and surface tables. Outputs remain Extraction Candidates / Evidence Pack Candidates. |
| `12britz/awesome-free-models` | Curated list of free AI models, API tiers, local inference tools, chatbot UIs, RAG/vector databases, agentic frameworks, fine-tuning tools, datasets, hosting platforms and learning resources. | External tooling watchlist source only. It may seed dashboard watchlist cards or Hermes capability review candidates, but it is not a catalogue of approved models, tools or providers. | External reference / candidate-only | Medium; high if free-tier, license, privacy, benchmark or availability claims are trusted without review | Accepté as watchlist only | Documented non implemented | Use only to discover candidates. Verify license, commercial terms, data policy, retention, local/cloud boundary, version/date, quota, stability and IFJ benchmark before any admission or configuration. |

## Tool notes

### GSAP Skills

Accepted as a lightweight Hermes skill candidate.

It may help produce frontend animation code, UI micro-interactions, educational interfaces, dashboard motion, scroll-driven explanations and visual prototypes.

It must return code candidates and integration notes. It must not decide UX acceptance, publish to production, bypass accessibility constraints or make candidate status look validated.

Governance trigger: animation becomes consequential if it hides a warning, changes the interpretation of a status, pushes a user toward an approval or visually confuses candidate and validated states.

### Browser Eyes MCP

Accepted as a privileged Hermes MCP skill candidate.

Recommended modes:

1. read-only audit — screenshots, DOM inspection, accessibility tree, console logs, network read, HAR export;
2. interactive test — click, type, scroll, navigation and device emulation within declared scope;
3. mutation / interception — DOM edit, JS edit, cookie and storage mutation, request interception, header injection or environment falsification.

The third mode requires explicit approval and a bounded scope.

All outputs are Evidence Pack Candidates until Pantheon qualifies their status.

### Rowboat

Not accepted as a skill.

Rowboat is a product / runtime / workspace pattern, not a bounded execution capability.

Its useful pattern is inspectable working memory and graph-based context accumulation.

Pantheon boundary:

```text
Rowboat records and organizes working context.
Hermes may execute bounded tasks.
Pantheon governs promotion, status, proof, memory and approval.
```

Rowboat memory, notes, summaries or graph relations are not a Registre Probatoire entry or proof by default. They may only enter Pantheon as Register Candidates or Evidence Pack Candidates under a governed promotion rule.

### Spice

Not accepted as Pantheon core, Hermes default runtime or approval authority.

Spice is valuable because it makes the pre-execution decision visible: candidate options, selected option, rejected trade-offs, sources, why, simulation metadata, approval checkpoints and executor handoff.

The compatible pattern is not the Spice runtime. The compatible pattern is a displayable and reviewable decision surface:

```text
Decision surface in OpenWebUI
-> governed Task Contract / Context Pack / Evidence Pack Candidate
-> Hermes bounded execution if approved
-> Outcome Observation Candidate
-> Pantheon status review
```

Patterns to distill:

- Decision Card as a compact decision review surface;
- `/sources` as Evidence Pack display;
- `/why` as structured decision rationale and objection view;
- `/details` as expanded audit card;
- `/json` as raw artifact inspection for developers;
- `decision.md` as inspiration for bounded decision guidance, not as runtime policy owner;
- explicit support contract for what the active adapter can actually evaluate;
- unsupported semantics reporting instead of guessing;
- read-only perception before any execution request;
- approval-gated executor handoff;
- outcome observation separated from governance validation.

Patterns to refuse:

- Spice as decision authority above Pantheon;
- Spice memory as canonical memory;
- Spice approvals as Pantheon approvals;
- Spice Decision Card as Evidence Pack or Registre Probatoire entry;
- Spice executor handoff as authorized execution by itself;
- Spice runtime state as governance state;
- automatic reflection or decision evolution as memory promotion.

Boundary:

```text
Spice may inspire Pantheon decision surfaces.
Spice must not become Pantheon's decision authority.
```

### PaddleOCR

Accepted only as a Hermes-managed document extraction capability candidate.

The dashboard may expose user and admin controls:

```text
install via Hermes;
configure;
check health;
view logs;
run benchmark;
show capability gap when unavailable.
```

The dashboard must not become the installer, OCR runtime, document authority or proof engine. It can request or display Hermes-managed capability state.

Hermes may install and run PaddleOCR as an OCR / document parsing tool, but it must return candidates only:

```text
Document Source
-> Extraction Candidate
-> Fragment Candidate
-> Evidence Pack Candidate
```

PaddleOCR output must carry at least:

```text
source_id;
source_version;
page_or_location;
extraction_method;
model_or_tool_version;
extraction_confidence;
layout/table confidence when available;
produced_at;
scope_id;
known_limits;
```

Pantheon governs the status, evidence rule, approval rule, memory rule and promotion path. It must not depend on PaddleOCR and must not treat OCR success as proof.

Minimum benchmark before operational use:

```text
CERFA;
mairie arrêté;
devis;
chantier compte rendu;
tableau de surfaces.
```

Benchmark result remains `Candidate / to verify` until reviewed.

### Awesome Free Models

Accepted only as an external tooling watchlist source.

`12britz/awesome-free-models` is useful as a radar for candidate models, local inference tools, API tiers, chatbot UIs, RAG/vector tools, agentic frameworks, fine-tuning tools, datasets and hosting platforms.

It must not be treated as:

```text
approved model catalogue;
approved provider list;
approved install source;
license authority;
privacy authority;
benchmark authority;
production readiness signal;
Pantheon capability registry;
Hermes skill registry.
```

The dashboard may expose a `Tooling Watchlist` view derived from reviews, but the view remains display and qualification only:

```text
watchlist item;
category;
source URL;
local_or_cloud;
data_sensitivity_fit;
license_status;
commercial_terms_status;
privacy_status;
quota_status;
benchmark_status;
Pantheon placement;
Decision Zeus;
repo_state;
next_action.
```

A listed model, API, framework or tool may become eligible only through a separate review. Each candidate must record at least:

```text
exact upstream source;
pinned version or retrieval date;
license and commercial-use status;
data retention and training policy;
local / cloud processing boundary;
required permissions;
quota or free-tier volatility;
professional-domain benchmark result;
forbidden outputs and effects;
owner and review date.
```

Free availability is not authorization.

Catalogue visibility is not admission.

A model that answers well in a benchmark still returns candidates, not truth.

## Current decision

```text
GSAP skills -> Hermes skill candidate.
Browser Eyes MCP -> Hermes privileged MCP skill candidate.
Rowboat -> external reference / possible adapter candidate.
Spice -> external reference / UX and method distillation only; refused as core or decision runtime.
PaddleOCR -> dashboard-installable, Hermes-managed document extraction candidate; no Pantheon dependency.
Awesome Free Models -> external tooling watchlist source only; may seed candidates, never approve them.
```

Do not add any of these to Pantheon core.

Do not call them implemented until a real Hermes skill, adapter, profile or integration exists outside Pantheon and has been reviewed.
