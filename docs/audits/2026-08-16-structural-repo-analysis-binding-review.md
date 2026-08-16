# Structural repository analysis binding review — 2026-08-16

Status: audit / candidate qualification note. Non-normative. No installation or binding adoption is authorized by this document.

Repository baseline inspected: `ifanjuang/Pantheon-Next` `main` through commit `31b0e180f08d869c490a054115ea699af0fbe4da`.

## Objective

Review `repowise-dev/repowise` against Pantheon Next's current architecture and the existing `structural_repo_analysis` Capability Slot before changing any binding, schema or runtime.

The review must answer five questions:

1. Does Repowise cover a responsibility that Pantheon already models?
2. What does it add beyond the current Pantheon + Hermes + GitHub inspection workflow?
3. Is it a better candidate than the current `Understand-Anything` binding?
4. Are there narrower or more efficient alternatives for part of the job?
5. Does Repowise `distill` justify a new Pantheon concept?

## Authority baseline

Current Pantheon architecture remains authoritative:

```text
Pantheon Next = governance, doctrine, schemas, status, Evidence, scopes, approvals and Capability Slots
pantheon-mvp = operational implementation candidate, APIs, PostgreSQL, Cockpit projections and adapters
Hermes = tasks, skills, tools and external runtimes
OpenWebUI / Cockpit = user and decision surfaces
human = consequential decisions
```

The current binding doctrine already owns the relevant abstraction:

```text
Capability Slot: structural_repo_analysis
current preferred candidate: Egonex-AI/Understand-Anything
```

Therefore this review does **not** create `repo_intelligence`, `codebase_memory`, `repository_graph` or another parallel Capability Slot.

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

## Observed Repowise state

Reviewed upstream: [`repowise-dev/repowise`](https://github.com/repowise-dev/repowise).

Observed on 2026-08-16:

```text
current inspected commit: 580e17f065fd0cc73192e2bb09405aef57b9b2ae
package version: 0.43.0
license: AGPL-3.0-or-later
project classifier: Development Status :: 3 - Alpha
Python requirement: >= 3.11
Hermes integration: Good tier
```

The current package combines Tree-sitter language parsers, graph analysis, Git analysis, SQLite/SQLAlchemy, LanceDB, FastAPI/MCP and several optional or bundled model-provider SDKs. This is materially heavier than a single-purpose structural parser.

Repowise's useful distinction is that it computes repository intelligence once and exposes task-shaped answers to agents rather than requiring repeated raw exploration.

Its current layers cover:

```text
graph
Git history and behavioural coupling
generated / indexed documentation
mined architectural decisions with evidence spans
code health and refactoring signals
```

It also supports multi-repository workspaces and a separate output-distillation capability.

## What Repowise adds to the current Pantheon workflow

Pantheon's present method is deliberately source-first. Before a consequential repository change, the agent checks current branches, commits, PRs, issues, schemas, registries, consumers and tests.

That verification method must remain.

Repowise's value is to reduce the cost of discovering **what must be verified**.

Current recurring exploration resembles:

```text
search concept
-> find schema / doctrine owner
-> find consumers
-> inspect recent commits / PRs
-> inspect tests
-> compare Pantheon-Next / pantheon-mvp / Pantheon-plugins
-> reconstruct likely impact
```

A qualified repository-intelligence binding could precompute much of the navigation layer:

```text
symbol and file graph
call / dependency relations
Git hotspots and ownership
co-change relations
bug-fix history
change-risk hints
related tests
cross-repository contracts
repository decisions and provenance spans
```

The expected architectural gain is therefore:

```text
less repeated rediscovery
more targeted source verification
smaller agent context
fewer sequential search/read calls
better cross-repository impact discovery
```

It is not a replacement for GitHub, repository source, tests or Pantheon governance.

## Distill assessment

Repowise `distill` is significant, but it should currently be treated as an **implementation-local context optimization**, not as a new Pantheon Capability Slot.

Upstream describes Distill as reusing the existing repository index to compress command and read output before the agent consumes it. The current implementation includes command-specific filters for test, build, lint, install, infrastructure-plan, Git status/log/diff, search, file listing and logs.

The important properties are:

```text
errors survive
exit codes survive
omitted raw output is stored before a marker is emitted
omissions are reversible through a stable reference
filter/storage failure falls back to raw output
small output passes through unchanged
MCP response truncation exposes reversible omission metadata
```

This is materially better than blind truncation or an LLM summary because the discarded detail remains addressable.

For Pantheon/Hermes, three benefits are distinct.

### 1. MCP response budgeting

Repowise can return bounded MCP responses and expose omitted material through references instead of silently truncating it.

This directly reduces context pressure while preserving a route back to the source material.

Governance boundary:

```text
distilled != complete
omitted_but_recoverable != reviewed
token_saving != correctness
```

### 2. Index-aware file skeletons

Repowise can render signatures/imports plus selected important bodies based on symbol importance, hotspot state and query relevance.

This is particularly useful for large implementation files where Hermes needs orientation before deciding which exact source ranges to inspect.

### 3. Noisy command compression

`repowise distill <cmd>` can reduce test/build/lint/Git output before Hermes reads it.

However the Hermes integration boundary matters. Repowise currently classifies Hermes as **Good tier**: MCP and configuration are supported, but hook-level interception and transcript mining are not. Therefore automatic command rewriting and read interception must not be assumed for Hermes.

For Hermes, the qualified value to test is:

```text
MCP response budgeting = directly applicable
explicit Repowise distill CLI use = potentially applicable if exposed in the execution environment
explicit skeleton/context calls = directly testable
automatic hook rewrite = not currently a Hermes capability
transcript-based missed-savings analysis = not a Hermes capability
```

This distinction prevents documentation from claiming a Claude/Codex integration depth that Hermes does not have.

## Alternative candidates by responsibility

No single alternative is better on every dimension. The comparison should remain responsibility-driven.

### Existing candidate — Understand Anything

Reviewed upstream: [`Egonex-AI/Understand-Anything`](https://github.com/Egonex-AI/Understand-Anything), current inspected commit `32944829e7a63a9fa9c55d811d7f98a9530c6a6a`.

Strengths:

- interactive structural knowledge graph;
- file/function/class/dependency exploration;
- business/domain view;
- guided architecture tours;
- semantic search and explanation;
- diff impact analysis;
- knowledge-base graphing;
- broad agent-platform installation support including Hermes;
- MIT license.

Relative weakness for Pantheon engineering work:

- its center of gravity is explanation, visualization and onboarding;
- initial analysis may use a multi-agent/LLM pipeline and significant tokens;
- it exposes less Git behavioural intelligence than Repowise;
- it is less focused on co-change, defect history, test intelligence and deterministic change-risk analysis;
- it does not provide Repowise's reversible output-distillation path.

Interpretation: retain as a meaningful comparison candidate, especially for human exploration and architecture onboarding, but do not assume it remains the best Hermes-side engineering binding.

### CodeGraph — efficiency candidate

Reviewed upstream: [`codegraph-ai/CodeGraph`](https://github.com/codegraph-ai/CodeGraph), current inspected commit `489ccf1612555510f8367e3e673181f6a1275fe4`.

Observed current shape:

```text
native Rust engine
Apache-2.0
semantic graph
MCP + LSP / IDE clients
persistent local graph
multiple tool profiles
explicit graph-only mode
multi-workspace paths
```

Its current `graph-only` mode skips embeddings and is presented upstream as substantially faster than the full embedding path. The tool surface can also be narrowed (`core`, `graph`, `memory`, etc.).

This makes CodeGraph particularly relevant as the **lean structural fallback** to benchmark when runtime footprint matters.

Strengths relative to Repowise:

- native compiled engine;
- narrow graph-only execution mode;
- profile-based reduction of the MCP tool surface;
- semantic symbol/call/dependency navigation;
- direct impact / PR-context tools;
- potentially lower steady-state operational overhead for graph-only use.

Risks / architectural mismatches:

- its persistent memory surface overlaps with Pantheon's separately qualified external-memory boundary and should be disabled/ignored for this slot;
- its documentation store must not become a second doctrine owner;
- it does not currently provide the same combined Git/co-change/code-health/decision/distill package as Repowise;
- target compatibility and real resource consumption must be measured rather than inferred from implementation language.

Interpretation: CodeGraph should be included in the qualification matrix as a fallback/efficiency candidate under the **same** `structural_repo_analysis` slot, preferably with memory disabled and the narrowest useful tool profile.

### Serena — semantic editing candidate

Reviewed upstream: [`oraios/serena`](https://github.com/oraios/serena), active on 2026-08-16.

Serena is an MCP coding toolkit centered on semantic symbol retrieval and editing through language servers or an IDE backend.

It is stronger than Repowise for a different job:

```text
find symbol
find references
find implementations
semantic edit
cross-file rename/refactor
diagnostics
```

This makes Serena potentially valuable for Hermes when performing precise code modification.

It should **not** be treated as a direct winner of the current structural-repository slot merely because it edits code better. It lacks Repowise's repository-history, co-change, health and distillation center of gravity.

Interpretation: keep Serena outside the current binding decision unless a demonstrated `semantic_code_navigation_or_editing` gap requires a separately governed capability. Do not create that new slot speculatively.

### Aider repo map — optimization pattern, not current binding

Aider's repository map is a useful architectural reference because it applies graph ranking to select only the repository symbols that fit a token budget. It demonstrates a deliberately compact, query-aware context-map strategy.

For Pantheon this is more useful as a **design pattern** than as a binding because it is integrated into Aider rather than offered as the neutral Hermes-side repository-intelligence service we currently need.

Pattern worth retaining:

```text
full repository model exists outside model context
-> rank relevant symbols/files for the current task
-> enforce a bounded context budget
-> fetch exact source only when necessary
```

No new dependency is justified by this pattern alone.

### Sourcegraph — scale reference, not current default

Sourcegraph demonstrates mature large-estate code search, code graph and ranking across repositories. Its architectural value increases when repository count and organizational scale become much larger than Pantheon's current estate.

For the present topology, adopting a broader search platform would add operational surface beyond the demonstrated need. Keep it as a scale reference rather than a default binding candidate.

## Architectural comparison

The candidate set is best understood as four different optimizations:

```text
Repowise
  = persistent repo intelligence + Git behaviour + risk/health + multi-repo + reversible distillation

CodeGraph
  = fast/narrow structural and semantic graph, especially attractive in graph-only/profiled mode

Understand Anything
  = human-oriented architecture exploration, explanation, knowledge graph and onboarding

Serena
  = IDE/LSP-grade semantic code navigation and editing
```

This means a naive winner-takes-all choice would create the wrong architecture.

Pantheon should continue to own one abstract slot and allow replaceable candidate bindings.

## Recommended target topology for qualification

```text
Pantheon Next
  governs abstract Capability Slot + status + activation boundary
                 |
                 v
        structural_repo_analysis
                 |
          selected binding
                 |
                 v
Hermes -------- MCP / bounded CLI -------- isolated repo-intelligence runtime
                 |
                 +-> disposable or controlled repository clones
                 +-> local index/cache
                 +-> candidate context / risk / graph outputs

GitHub/source/tests remain verification authority for repository facts.
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

The next decision should be based on the same representative tasks and the same repository snapshots.

Minimum candidates:

```text
A. Hermes + current source/GitHub workflow, no repo-intelligence binding
B. Repowise 0.43.x, no-prose/local deterministic path first
C. CodeGraph current release, graph-only + narrow graph/core profile
D. Understand Anything current release
```

Serena should be measured only on edit/refactor tasks as a complementary candidate, not forced into the structural-analysis ranking.

Use Pantheon-Next, pantheon-mvp and Pantheon-plugins together for cross-repository cases where supported.

Representative questions:

1. Where is one governed concept defined, projected, consumed and tested?
2. What is the likely blast radius of changing one canonical schema field?
3. Which files historically co-change with the selected implementation path?
4. Which tests are most relevant to a bounded change?
5. What recent commit/PR history materially affects the proposed edit?
6. Which generated or mined architectural statements can be traced back to exact repository sources?
7. How much context is consumed before the agent reaches the correct files?
8. Can omitted detail be recovered without rerunning the original operation?

Measure:

```text
correct-file recall
false-positive relations
source/provenance quality
freshness after commit
multi-repo coverage
tokens delivered to Hermes
tool-call count
cold-index time
incremental-update time
CPU peak / steady state
RAM peak / steady state
disk/index footprint
startup latency
failure/recovery behaviour
installation side effects
rollback/removal completeness
license implications
```

For Repowise specifically, measure `distill` separately from repository analysis so its context-saving benefit is not incorrectly credited to graph quality.

## Current recommendation

Observed facts support the following bounded conclusion:

1. **Do not create a new Capability Slot.** `structural_repo_analysis` already owns the responsibility.
2. **Do not replace Understand Anything yet.** No Pantheon-local comparative benchmark has been executed.
3. **Promote Repowise to the comparison set for the existing slot.** It currently appears better aligned with Hermes engineering work because it combines repository structure with Git behaviour, change risk, tests, health signals, cross-repository workspaces and reversible output distillation.
4. **Add CodeGraph to the same comparison as the efficiency/fallback candidate.** Its graph-only/profiled native runtime may be materially cheaper for a resource-constrained deployment, but this remains unmeasured on Pantheon's target environments.
5. **Keep Understand Anything in the comparison for human exploration/onboarding strengths.**
6. **Keep Serena as a complementary semantic-editing candidate**, not as a reason to split the current slot before a real gap is demonstrated.
7. **Treat Distill as a binding-local optimization for now.** Do not create `context_distillation` governance vocabulary unless more than one implementation and a distinct cross-runtime responsibility justify it.
8. **Do not install any candidate into the production Hermes image during qualification.** Use an isolated service/environment and disposable or controlled clones.

## Resource-placement note

The current Hermes deployment environment and any Synology target must be tested explicitly. Implementation language alone is not sufficient evidence of suitability:

```text
Python package != guaranteed NAS compatibility
native Rust binary != guaranteed DSM/glibc compatibility
low idle RAM != safe peak indexing behaviour
successful startup != acceptable sustained footprint
```

A first benchmark on a development workstation is preferable to polluting the existing Hermes runtime. Deployment-profile testing can follow only if the capability proves useful enough to justify it.

## Closure

This review closes the **placement and comparison framing** only.

Closed:

- responsibility mapped to the existing `structural_repo_analysis` slot;
- Repowise value relative to the current workflow identified;
- Distill boundary identified;
- current main alternatives separated by responsibility;
- qualification criteria defined.

Not closed:

- preferred binding selection;
- installation;
- target-environment compatibility;
- production activation;
- replacement or demotion of Understand Anything.

Those require a bounded comparative qualification with observed Pantheon repositories and target-runtime measurements.
