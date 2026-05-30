# AI Learning Repositories Distillation

Status: draft support note — pending governance index reconciliation.

Date: 2026-05-29

This document records five public AI learning repositories as external learning references for Pantheon Next.

It does not add dependencies.

It does not authorize implementation.

It does not approve a provider, runtime, plugin, skill, MCP server, tool gateway, workflow engine, evaluation engine or memory system.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The five repositories reviewed here are useful because they expose recurring AI work patterns:

- prompt framing;
- context and retrieval discipline;
- tool use;
- evaluations;
- application lifecycle;
- model internals;
- deployment and security concerns.

Pantheon Next must learn from these patterns without copying their runtimes, examples or product assumptions into its governance core.

The goal is distillation, not adoption.

```text
Popularity is not approval.
A course is not doctrine.
A notebook is not runtime authority.
A prompt persona is not a Pantheon Role.
An eval pass is not governed approval.
```

## Source set

This distillation covers:

| Repository | Primary learning value | Pantheon relevance | Hermes relevance | OpenWebUI relevance | Boundary |
|---|---|---|---|---|---|
| `f/prompts.chat` | Prompt persona and framing examples | Useful as anti-confusion material between prompt persona, Pantheon Role, Hermes Profile and Task Contract | May inspire candidate prompt templates under contract only | May be browsed or exposed as non-canonical reference material | Must not become a role registry, skill marketplace or internal MCP layer |
| `dair-ai/Prompt-Engineering-Guide` | Prompt, context, RAG, agent and adversarial prompting taxonomy | Useful for prompt/context risk vocabulary, adversarial review and method distillation | May inform execution prompts or checklists under Task Contract | May serve as a learning Knowledge Item | Must not import agentic RAG or LLM-as-judge authority into Pantheon |
| `anthropics/courses` | First-party notebook courses for API use, prompting, evaluations and tool use | Strong reference for Evidence Pack expectations, evaluation discipline and tool-use boundaries | May inform Hermes-side tool-use and eval candidates | May expose eval results, approval surfaces and review notes | Provider-specific reference, not a provider routing decision |
| `microsoft/generative-ai-for-beginners` | Broad generative AI application curriculum, including responsible AI, UX, lifecycle and security | Useful for product lifecycle, safety, security and professional onboarding vocabulary | May inform a broad capability map, not a runtime plan | May inspire cockpit explanation and training surfaces | Microsoft ecosystem bias must not become Pantheon architecture |
| `mlabonne/llm-course` | LLM internals, fine-tuning, quantization, RAG, agents, deployment and security | Useful for Skill Watchlist, tool risk classification and external capability boundaries | Strongest relevance to optional Hermes skill candidates and technical execution patterns | May display candidate outputs and learning references only | Must not make Pantheon a training, fine-tuning or quantization runtime |

## Pantheon reading order

The learning order for a beginner is not the governance order for Pantheon.

For Pantheon Next, the priority is:

1. `anthropics/courses` — evaluation and tool-use discipline.
2. `dair-ai/Prompt-Engineering-Guide` — prompt, context, RAG and adversarial taxonomy.
3. `microsoft/generative-ai-for-beginners` — lifecycle, UX, security and responsible AI framing.
4. `mlabonne/llm-course` — Hermes-facing capability and skill-watch vocabulary.
5. `f/prompts.chat` — persona examples and anti-confusion material.

Reason:

```text
Pantheon should first strengthen proof, boundaries and approvals.
Only then should it absorb broader curricula, technical capability maps or prompt examples.
```

## Overlap map

### Prompt framing

Relevant references:

- `f/prompts.chat`;
- `dair-ai/Prompt-Engineering-Guide`;
- `anthropics/courses`;
- `microsoft/generative-ai-for-beginners`.

Pantheon distillation:

```text
Prompt framing can change output behavior.
It does not create governance authority.
```

A prompt persona may be useful for drafting, review or exploration.

It must not be confused with:

- a Pantheon Role;
- a Hermes Profile;
- a Task Contract;
- an Evidence Pack;
- approval;
- Canonical Memory.

### Context, RAG and retrieval

Relevant references:

- `dair-ai/Prompt-Engineering-Guide`;
- `microsoft/generative-ai-for-beginners`;
- `mlabonne/llm-course`.

Pantheon distillation:

```text
Retrieval improves access.
Retrieval does not validate.
Retrieved Knowledge may become Evidence only when selected, scoped and recorded.
```

This supports `KNOWLEDGE_TAXONOMY.md`, `SCOPE_ISOLATION.md`, `CONTEXT_PACKS.md` and RAG evidence-boundary doctrine.

### Tool use and agents

Relevant references:

- `anthropics/courses`;
- `dair-ai/Prompt-Engineering-Guide`;
- `microsoft/generative-ai-for-beginners`;
- `mlabonne/llm-course`.

Pantheon distillation:

```text
Tool use is a capability surface.
It is not authorization.
```

Tool patterns may inform Hermes execution candidates, but all tool use remains governed by:

- Task Contract scope;
- External Tools Policy;
- evidence expectations;
- approval level;
- memory rules.

### Evaluations, safety and security

Relevant references:

- `anthropics/courses`;
- `microsoft/generative-ai-for-beginners`;
- `dair-ai/Prompt-Engineering-Guide`;
- `mlabonne/llm-course`.

Pantheon distillation:

```text
An evaluation can reveal quality or failure modes.
It does not replace approval.
```

Useful future distillation targets:

- evaluation checklist for Evidence Packs;
- model-graded output caution note;
- adversarial prompt risk card;
- tool-use risk classification examples;
- delivery-readiness versus correctness distinction.

### Model internals and deployment

Relevant reference:

- `mlabonne/llm-course`.

Pantheon distillation:

```text
Model internals help classify capability and risk.
They do not require Pantheon to own model training or deployment.
```

Fine-tuning, quantization, inference optimization and model deployment belong, if ever used, to external execution environments such as Hermes-side capability candidates.

They are not Pantheon governance primitives.

### Product lifecycle and UX

Relevant reference:

- `microsoft/generative-ai-for-beginners`.

Pantheon distillation:

```text
A governed AI workflow is not only prompting.
It also needs user action clarity, lifecycle discipline, safety posture and delivery-state vocabulary.
```

This is useful for OpenWebUI cockpit design, approval visibility, user-facing language and onboarding.

## Candidate distillations

The following are candidate documentation work items, not implementation tasks.

| Candidate | Source inspiration | Possible Pantheon location | Status |
|---|---|---|---|
| Evaluation checklist for candidate outputs | `anthropics/courses` | `EXTERNAL_METHOD_REVIEWS.md` or future non-executable checklist | candidate |
| Prompt persona versus Pantheon Role clarification | `f/prompts.chat` | `REJECTED_PATTERNS.md` or pattern card | candidate |
| Adversarial prompt and prompt-injection review note | `dair-ai/Prompt-Engineering-Guide` | `EXTERNAL_METHOD_REVIEWS.md`, `TENSIONS_AND_RISKS.md` | candidate |
| Tool-use boundary checklist | `anthropics/courses`, `mlabonne/llm-course` | `EXTERNAL_TOOLS_POLICY.md` support note | candidate |
| AI application lifecycle vocabulary | `microsoft/generative-ai-for-beginners` | `EDITORIAL_LANGUAGE.md`, `OPENWEBUI_TEMPLATES.md` | candidate |
| Hermes technical skill watch records | `mlabonne/llm-course` | `SKILL_WATCHLIST.md` | candidate, separate review required |

These candidates must not be treated as approved doctrine until separately reviewed.

## Rejected patterns

Pantheon Next should explicitly reject the following drifts:

| Pattern | Why rejected |
|---|---|
| Star count as adoption signal | Popularity is visibility, not evidence or approval |
| Prompt persona as Pantheon Role | A persona changes style; a role carries governed responsibility |
| Course notebook as Pantheon runtime | Learning material must not become execution architecture |
| Eval pass as approval | Evaluation is evidence input, not governance decision |
| RAG demo as proof | Retrieval demonstrates access, not truth |
| Agent lesson as architecture commitment | Agentic examples must not import a hidden runtime |
| Tool-use tutorial as tool authorization | Tool availability never bypasses Task Contract and approval |
| Fine-tuning guide as Pantheon capability | Training and quantization are external technical capabilities, not governance core |
| LLM-as-judge as human decision replacement | Judgment aids may assist review but cannot replace governed approval |
| MCP example as internal connector policy | MCP remains an external capability surface, not a Pantheon internal layer |

## Placement across Pantheon, Hermes and OpenWebUI

### Pantheon Next

Pantheon may keep these repositories as:

- external references;
- Knowledge Items;
- method-review sources;
- candidate distillation sources;
- rejected-pattern sources.

Pantheon must not use them as:

- dependencies;
- runtime engines;
- approval authorities;
- memory authorities;
- role registries;
- plugin catalogs;
- provider-routing sources.

### Hermes Agent

Hermes may later use selected patterns as candidate execution support, only when governed by Task Contract.

Potential Hermes relevance:

- evaluation candidate generation;
- tool-use candidate workflows;
- technical skill candidates;
- capability-gap vocabulary;
- implementation candidate checklists.

Hermes must not:

- install skills automatically;
- promote memory;
- approve its own outputs;
- broaden scope silently;
- import a course as a standing runtime behavior.

### OpenWebUI

OpenWebUI may expose these materials as learning references, Knowledge Items or review surfaces.

OpenWebUI must not:

- turn them into Canonical Memory;
- treat retrieved course content as proof;
- authorize Hermes access to all learning material by default;
- convert prompt examples into hidden system behavior;
- approve or transmit based only on UI selection.

## Governance decision rule

Before any pattern from these repositories is promoted into Pantheon doctrine, ask:

```text
What exact pattern is useful?
Which confusion does it reduce?
Does it preserve source -> evidence -> approval -> memory separation?
Does it require runtime ownership?
Does it affect external transmission?
Does it affect memory?
Can it remain optional and replaceable?
What Evidence Pack or review note supports it?
Which approval level is required?
```

If the pattern blurs proof, approval, memory or runtime boundary, reject or quarantine it.

If the pattern is useful but execution-facing, send it to Hermes as a candidate under Task Contract.

If the pattern is cockpit-facing, expose it through OpenWebUI without giving it authority.

## Indexing rule

This note is intentionally marked as draft until `docs/governance/README.md`, `docs/governance/STATUS.md` and `CHANGELOG.md` can be reconciled in a small follow-up pass.

It must not be treated as active support doctrine until that indexing pass is complete.

## Status

Research and support note only.

No dependency added.

No implementation started.

No OpenWebUI plugin added.

No Hermes skill added.

No MCP layer added.

No provider routing added.

No evaluation engine added.

No schema added.

No test added.

No operations tooling added.

No memory promoted.

No external repository adopted.
