# Structural repository analysis binding review — 2026-08-16

Status: audit / candidate qualification note. Non-normative. No installation, activation, preferred-binding change or dependency adoption is authorized by this document.

Repository baseline inspected: `ifanjuang/Pantheon-Next` `main` through commit `31b0e180f08d869c490a054115ea699af0fbe4da`.

## Objective

Qualify current candidates against the existing `structural_repo_analysis` Capability Slot before changing any binding, schema, runtime or governance vocabulary.

This review answers five bounded questions:

1. Is the responsibility already modeled by Pantheon?
2. Which candidate best reduces repository-discovery cost without becoming an authority?
3. What is the smallest useful runtime profile for each candidate?
4. Does RepoWise `distill` justify a new Pantheon concept?
5. What must be benchmarked before any preferred-binding change?

## Authority and convergence boundary

Current Pantheon boundaries remain authoritative:

```text
Pantheon Next = governance, doctrine, schemas, status, Evidence, scopes, approvals and Capability Slots
pantheon-mvp = operational implementation candidate, APIs, PostgreSQL, Cockpit projections and adapters
Hermes = tasks, skills, tools and external runtimes
OpenWebUI / Cockpit = user and decision surfaces
human = consequential decisions
```

The responsibility already exists:

```text
Capability Slot: structural_repo_analysis
canonical registry reference: Lum1104/Understand-Anything
current upstream location observed: Egonex-AI/Understand-Anything
```

GitHub currently resolves `Lum1104/Understand-Anything` to `Egonex-AI/Understand-Anything` with the same repository identity. This is observed upstream continuity; it does not itself update Pantheon's canonical binding record.

Therefore this review does **not** create `repo_intelligence`, `codebase_memory`, `repository_graph`, `context_distillation` or another parallel Capability Slot.

Required non-equivalences remain:

```text
index_success != truth
graph_edge != proof
risk_score != authorization
health_score != safety
dead_code_candidate != deletion_authorized
mined_decision != Pantheon Decision
generated_documentation != doctrine
retrieved_context != Evidence
runtime_success != Evidence
binding_selected != dependency_adopted
```

## Candidate roles

The candidate set represents different optimizations under one responsibility.

```text
Repowise
  = persistent repo intelligence + Git behaviour + risk/health + multi-repo + reversible distillation

CodeGraph
  = narrow structural/semantic graph with a graph-only/profiled runtime option

Understand Anything
  = human-oriented architecture exploration, explanation and onboarding

Serena
  = semantic code navigation/editing; complementary responsibility, not a direct slot replacement
```

A winner-takes-all architecture is not justified.

## RepoWise qualification

Reviewed upstream: `repowise-dev/repowise`.

Observed on 2026-08-16:

```text
inspected commit: 580e17f065fd0cc73192e2bb09405aef57b9b2ae
package version: 0.43.0
license: AGPL-3.0-or-later
classifier: Development Status :: 3 - Alpha
Python requirement: >= 3.11
Hermes integration: Good tier
```

The package combines Tree-sitter parsers, graph and Git analysis, SQLite/SQLAlchemy, LanceDB, FastAPI/MCP, scheduling support and bundled model-provider SDKs. This is materially heavier than a single-purpose structural parser.

Its useful distinction for Pantheon is not authority over repository facts. It is the ability to compute repository intelligence once and expose task-shaped navigation hints that reduce repeated discovery.

Useful surfaces include:

```text
symbol/file graph
call and dependency relations
Git hotspots and ownership
co-change relations
bug-fix history
change-risk hints
related tests
multi-repository workspaces
source-linked mined/generated statements
reversible output distillation
```

The expected gain is:

```text
less repeated rediscovery
more targeted source verification
smaller agent context
fewer sequential search/read calls
better cross-repository impact discovery
```

GitHub, source and tests remain verification authority.

## Minimum useful profile principle

Qualification should start with the smallest runtime profile that demonstrates value.

For RepoWise, test the deterministic/local analysis path before enabling optional prose generation, embeddings or provider-backed features. Do not credit unused bundled capabilities as architectural value.

For CodeGraph, begin with `graph-only` and the narrowest useful graph/core tool profile. Disable or ignore memory surfaces for this slot.

For Understand Anything, measure the actual analysis/token/runtime cost of its exploration-oriented pipeline rather than assuming installation support implies efficiency.

General rule:

```text
available feature != required capability
installed component != adopted dependency
broader tool surface != better binding
```

## Distill assessment

RepoWise `distill` is useful but should remain a **binding-local context/output optimization**.

The relevant properties are:

```text
bounded output
errors and exit codes preserved
omitted raw material retained before a marker is emitted
stable references permit recovery
filter/storage failure falls back to raw output
small output passes through unchanged
```

This is preferable to blind truncation or irreversible summarization.

Governance boundary:

```text
distilled != complete
omitted_but_recoverable != reviewed
token_saving != correctness
```

Do not create a `context_distillation` Capability Slot or a top-level `DistilledContext` model from this observation.

Distillation must be benchmarked separately from structural-analysis quality so that RepoWise does not appear to have better graph quality merely because it emits fewer tokens.

## Alternative candidates

### Understand Anything

Reviewed upstream at `Egonex-AI/Understand-Anything`, inspected commit `32944829e7a63a9fa9c55d811d7f98a9530c6a6a`.

GitHub currently resolves the older canonical path `Lum1104/Understand-Anything` to this same repository identity.

Strengths:

- interactive structural knowledge graph;
- file/function/class/dependency exploration;
- guided architecture tours and onboarding;
- semantic search and explanation;
- diff-impact and knowledge-base views;
- broad agent-platform installation support including Hermes;
- MIT license.

Relative weakness for the engineering path:

- center of gravity is explanation/visualization/onboarding;
- initial analysis may use a multi-agent/LLM pipeline and significant tokens;
- less emphasis on Git behavioural intelligence, co-change, defects and deterministic risk/test context;
- no equivalent reversible output-distillation path observed.

Keep it in the benchmark. Do not replace or demote it before measured comparison.

### CodeGraph

Reviewed upstream at `codegraph-ai/CodeGraph`, inspected commit `489ccf1612555510f8367e3e673181f6a1275fe4`.

Relevant shape:

```text
native Rust engine
Apache-2.0
semantic graph
MCP + LSP / IDE clients
persistent local graph
multiple tool profiles
graph-only mode
multi-workspace paths
```

Its value is a potentially lean structural fallback. Qualification should use graph-only/profiled mode first.

Its persistent memory and documentation surfaces are not owners for Pantheon memory or doctrine and should be disabled or ignored for this slot.

### Serena

Serena is stronger for semantic symbol navigation and editing:

```text
find symbol
find references
find implementations
semantic edit
cross-file rename/refactor
diagnostics
```

That is a different responsibility. Keep Serena outside this binding decision unless a demonstrated editing/navigation gap later justifies extending an existing capability or, only if necessary, a distinct slot.

### Aider repo map and Sourcegraph

Treat these as design/scale references rather than current default bindings.

The useful Aider pattern is:

```text
full repository model outside model context
-> rank relevant files/symbols for the current task
-> enforce a context budget
-> fetch exact source only when required
```

Sourcegraph remains a scale reference for a much larger repository estate; adopting that surface now would exceed the demonstrated need.

## Target runtime topology

```text
Pantheon Next
  governs Capability Slot + binding/activation/compatibility state
                 |
                 v
        structural_repo_analysis
                 |
          selected binding
                 |
                 v
Hermes -------- MCP / bounded CLI -------- isolated repo-analysis runtime
                 |
                 +-> disposable or controlled repository clones
                 +-> local disposable/controlled index/cache
                 +-> candidate navigation/risk/graph outputs

Git/source/tests remain authority for repository facts.
```

The binding runtime must not become:

```text
Pantheon memory
Pantheon Decision owner
Evidence authority
approval engine
second scheduler/orchestrator
repository mutation authority by default
```

## Qualification matrix

Benchmark the same immutable repository snapshots and representative questions.

Minimum profiles:

```text
A. baseline Hermes + current Git/source workflow, no repo-analysis binding
B. RepoWise 0.43.x, minimum deterministic/local profile
C. CodeGraph current release, graph-only + narrow graph/core profile
D. Understand Anything current release
```

Use exact SHAs for Pantheon-Next, pantheon-mvp and Pantheon-plugins. Multi-repository cases are first-class because Pantheon's governance/implementation/plugin responsibilities cross repository boundaries.

Representative tasks:

1. Find where one governed concept is defined, projected, consumed and tested.
2. Determine the likely blast radius of changing one canonical schema field.
3. Find historical co-change and recent PR/commit context around one implementation path.
4. Identify the tests most relevant to a bounded change.
5. Trace a generated/mined statement back to exact repository sources.
6. Detect a deliberately introduced contradiction or stale relation after a new commit.
7. Reach the correct source files with the least context and tool calls.
8. Recover omitted detail without rerunning the original operation where supported.

Measure two independent dimensions.

Structural-analysis quality:

```text
correct-file recall
false-positive relations
source/provenance quality
freshness after commit
incremental update accuracy
multi-repo coverage
time/tool calls to correct owner and consumers
relevant-test recall
contradiction/staleness detection
```

Operational cost:

```text
tokens delivered to Hermes
cold-index time
incremental-update time
startup latency
CPU peak / steady state
RAM peak / steady state
disk/index footprint
failure/recovery behaviour
installation side effects
rollback/removal completeness
license implications
```

For every material candidate assertion consumed by Hermes, prefer provenance that resolves to:

```text
repository
commit SHA
path
symbol or line/span when available
```

A relation without exact provenance remains a discovery hint, not a basis for a consequential modification.

## Context contract finding discovered during audit

The audit also exposed an existing inter-repository convergence issue unrelated to RepoWise selection.

Pantheon Next now has a canonical `ContextPack` schema representing governed purpose, scope, target surface, included context/doctrine, task constraints, Evidence/approval/output expectations and forbidden assumptions.

The current MVP Hermes path uses a narrower stored context shape centered on admitted entity identities, exclusions, source references and a digest; running Hermes access then resolves current owner values for those admitted identities.

This can be a valid projection boundary, but it should be explicit:

```text
Canonical ContextPack
  -> governed scope / constraints / provenance expectations
  -> Hermes launch-context projection
  -> exact admitted identities / bounded resolution
  -> trace of context actually consumed
```

Do not solve this by creating a third context model. Treat it as contract convergence between existing owners.

This finding is **out of scope for implementation in this PR** and does not block the structural-repository benchmark. It should be addressed by the relevant ContextPack/Hermes contract owners when that path is next modified.

The reusable lineage remains:

```text
used ⊆ admitted ⊆ retrieved
```

Any future reversible compression reference should preserve that lineage rather than create a new authority.

## Current recommendation

1. Keep the existing `structural_repo_analysis` Capability Slot.
2. Do not change the preferred binding yet.
3. Add RepoWise to the comparison set and test its minimum deterministic/local profile first.
4. Add CodeGraph graph-only/profiled mode as the efficiency fallback candidate.
5. Keep Understand Anything for human exploration/onboarding comparison and preserve the canonical binding until measured evidence justifies change.
6. Keep Serena complementary and outside this slot decision.
7. Evaluate `distill` separately from graph/repository-analysis quality.
8. Do not install any candidate into the production Hermes image during qualification; use an isolated environment and controlled/disposable clones.
9. Prefer the candidate that produces the largest measured reduction in discovery work while preserving source-level verification, freshness and provenance.

## Resource-placement note

The Hermes deployment environment and any Synology target require explicit compatibility observation:

```text
Python package != guaranteed NAS compatibility
native Rust binary != guaranteed DSM/glibc compatibility
low idle RAM != safe peak indexing behaviour
successful startup != acceptable sustained footprint
```

A development-workstation benchmark should precede target-environment deployment testing. Do not pollute the existing Hermes runtime merely to compare candidates.

## Relationship to #666 and retirement rule

This file is an audit artifact, not candidate-support doctrine and not a second binding registry.

Its useful output must converge back into existing owners:

```text
benchmark observations
-> existing Capability Binding / Compatibility owners
-> canonical binding registry update only if justified
-> this audit remains historical/non-normative
```

Do not keep expanding this file as a parallel source of current binding truth. After a bounded benchmark and any resulting owner updates, future consumers should use the canonical registry/contracts rather than this audit.

This is the retirement/convergence path required to remain compatible with #666's doctrine-economy objective.

## Closure

This review closes the **placement, candidate framing and qualification method** only.

Closed:

- responsibility mapped to existing `structural_repo_analysis`;
- no new repo-intelligence or distillation concept justified;
- upstream continuity of the Understand Anything repository identified without silently rewriting canonical governance;
- RepoWise, CodeGraph and Understand Anything separated by optimization profile;
- minimum-useful-profile principle established;
- distillation separated from structural-analysis scoring;
- multi-repo, freshness, provenance and cost criteria defined;
- existing ContextPack/Hermes convergence issue recorded without creating a new model;
- audit retirement path relative to #666 defined.

Not closed:

- comparative benchmark;
- preferred-binding selection;
- canonical binding-record update;
- target-environment compatibility;
- installation or production activation;
- ContextPack/Hermes contract convergence.

Those require observed results in their respective owners. H5.9 remains independent and is not blocked by this audit.