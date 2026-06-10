# Understand-Anything Reference Review

Status: support review only — external reference, Hermes candidate boundary and forbidden-import record.

Observed date: 2026-05-29

Reviewed sources:

- `https://github.com/Lum1104/Understand-Anything`, README blob observed at `3bdb4db2bb6d3878e45028602b290a8641dbc80b`;
- `https://github.com/Lum1104/Understand-Anything`, installer script blob observed at `8ff429356e720753d6d3fc610b102efc5e0b47cd`;
- `https://github.com/NousResearch/hermes-agent`, README blob observed at `fa2795305059c816467da435d8c44293bacf3592`;
- `https://github.com/fathah/hermes-desktop`, README blob observed at `fa3d04238b19abbf442bffecf500a22197030150`.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Review scope

This review evaluates Understand-Anything as an external project-understanding and knowledge-graph tool that may inspire a bounded Hermes Skill Candidate.

It also records why Hermes Desktop is not adopted as a Pantheon cockpit.

This document does not approve installation.

This document does not add a dependency.

This document does not create a Pantheon runtime, GraphRAG runtime, knowledge graph runtime, tool runtime, provider router, skill installer, scheduler, queue, memory engine or OpenWebUI plugin.

## External project summary

Understand-Anything presents itself as a tool that turns a codebase, knowledge base or documentation set into an interactive knowledge graph.

The README describes:

- analysis of files, functions, classes and dependencies;
- an interactive dashboard;
- semantic and fuzzy search;
- guided tours;
- diff impact analysis;
- business-domain mapping;
- knowledge-base analysis for Karpathy-pattern LLM wikis;
- saved graph output at `.understand-anything/knowledge-graph.json`;
- multi-platform skill installation including Hermes.

The project is useful because it makes repository and documentation structure visible.

The project is risky because its output can look more authoritative than it is.

## Technical characterization

Understand-Anything uses a hybrid model:

```text
Tree-sitter/static analysis -> structural facts
LLM semantic layer          -> summaries, labels, business interpretation and tours
```

Pantheon interpretation:

```text
structural graph edges are candidate structural evidence
LLM summaries are candidate interpretation
business-domain mapping is hypothesis
knowledge-base implicit relationships are hypothesis
```

The graph is therefore not a source of truth.

It is a reviewable artifact.

## Pipeline characterization

The README describes a pipeline with these analysis roles:

```text
project-scanner
file-analyzer
architecture-analyzer
tour-builder
graph-reviewer
domain-analyzer
article-analyzer
```

Pantheon classification:

```text
external analysis pipeline
not Pantheon Roles
not Governance College
not autonomous Pantheon agents
not hidden role debate
```

The wording `multi-agent` must not be imported into Pantheon as a runtime claim.

If the pipeline is referenced, call it an external analysis pipeline or external tool pipeline.

## Hermes installation surface

The external installer supports a Hermes platform value and can create links into a local Hermes skills directory.

Pantheon interpretation:

```text
installer = privileged external configuration action
link into Hermes skills = Hermes runtime mutation
one-line remote shell installer = supply-chain and permission risk
```

This is outside Pantheon Next.

It may be considered only as a sandboxed Hermes-side action after explicit review.

## Hermes Agent context

Hermes Agent is an external execution runtime.

Its public README describes skills, memory, scheduled automations, messaging gateways, terminal backends, toolsets, model switching and self-improvement claims.

Pantheon interpretation:

```text
Hermes Agent is powerful because it executes.
Hermes Agent is risky because it can persist, schedule, install skills and use tools.
Pantheon must constrain Hermes through Task Contracts.
```

Hermes may execute Understand-Anything only as an external runtime under a governed Task Contract.

Hermes must not canonize the resulting graph, summary, domain map or memory suggestion.

## Hermes Desktop context

Hermes Desktop is a community GUI for installing, configuring and chatting with Hermes Agent.

Its README says it can manage chat, sessions, profiles, memory, skills, tools, scheduling and gateways.

Pantheon interpretation:

```text
Hermes Desktop overlaps with cockpit responsibility.
OpenWebUI remains the Pantheon cockpit.
Hermes Desktop is not adopted as a Pantheon surface.
```

Decision:

```text
Hermes Desktop -> not installed for Pantheon Next at this stage
Hermes Agent   -> external runtime candidate only
OpenWebUI      -> cockpit remains primary
```

## Pantheon layer mapping

| Layer | Classification |
|---|---|
| Pantheon Next | governance review, boundary doctrine, evidence status and approval path |
| Hermes Agent | optional external execution runtime under Task Contract |
| Understand-Anything | optional external structural intelligence tool executed by Hermes |
| OpenWebUI | cockpit exposure of request, result, Evidence Pack Candidate and User Decision Gate |
| Hermes Desktop | excluded optional GUI; not part of Pantheon architecture |

## Recommended classification

```text
name: understand-anything
classification: External Structural Intelligence Tool
pantheon_status: reference_review_only
hermes_status: optional_skill_candidate
openwebui_status: cockpit_exposure_candidate
memory_status: non_canonical
approval_status: not_approved_for_installation
```

## Valuable patterns to distill

The following patterns are useful for Pantheon if stripped of runtime authority:

```text
repository radiography
structural graph as candidate evidence
diff impact report before patch review
onboarding tour as output candidate
business-domain graph as hypothesis
knowledge-base relationship map as hypothesis
separation between deterministic extraction and semantic interpretation
```

## Forbidden imports

Pantheon must not import:

```text
self-updating graph as truth
auto-update repository hook as governance validation
committed graph as a Registre Probatoire entry
LLM domain map as business authority
knowledge graph as GraphRAG runtime
Hermes skill installation as Pantheon module activation
Hermes Desktop as Pantheon cockpit
automatic skill installation
one-line remote shell installer as default setup path
```

## Auto-update posture

Understand-Anything documents an auto-update mode that installs a repository hook and patches the graph after commits.

Pantheon posture:

```text
forbidden by default
```

Reason:

```text
graph updated does not mean evidence validated
graph freshness does not mean doctrine correctness
repository hook is a mutation surface
```

A future exception would require explicit protected review, repository policy, rollback plan, evidence expectation and human approval.

## Committed graph posture

Understand-Anything suggests committing the generated graph folder except local scratch files.

Pantheon posture:

```text
not default
```

A committed graph may be useful as a review artifact, but only if it is labeled as candidate evidence and kept out of a Registre Probatoire entry.

Recommended rule:

```text
Commit graph artifacts only after review.
Never treat committed graph JSON as doctrine, proof or memory by itself.
```

## Evidence interpretation

The generated graph may support an Evidence Pack Candidate as:

```text
Source Reference
Tool Output
Structural Analysis Artifact
Candidate Evidence Item
```

It must not become:

```text
Registre Probatoire entry
Doctrine
Approval
Source of Truth
Runtime State
```

## User Decision Gate triggers

Use a User Decision Gate when Understand-Anything output affects:

- repository mutation;
- doctrine-sensitive interpretation;
- protected files;
- dependency adoption;
- memory promotion;
- external tool installation;
- auto-update hooks;
- graph commit policy;
- broad cross-repository conclusions;
- business-domain or professional-domain interpretation.

## Decision

```text
Adopt the pattern.
Do not adopt the runtime.
Do not install by implication.
Keep as Hermes sandbox candidate only.
Represent output as Evidence Pack Candidate.
```

## Final rule

```text
Understand-Anything may help Hermes see structure.
It must not help Pantheon forget the difference between structure, evidence, approval and memory.
```