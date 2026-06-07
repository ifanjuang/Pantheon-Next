# BrainAPI Architecture Workflow Reference Review

Status: support review only — external reference, architecture-workflow candidate and forbidden-import record.

Observed date: 2026-06-07

Reviewed sources:

- `https://github.com/Lumen-Labs/brainapi2`, repository README observed on `main` at commit `57d772f71ebccfe3b85d74273bb2d912cb3ddc04`;
- `https://github.com/Lumen-Labs/brainapi2/blob/main/LICENSE`, community license package observed on `main`;
- Pantheon Next active placement doctrine: `STATUS.md`, `MODULAR_DOMAIN_REORIENTATION.md`, `CAPABILITY_PLACEMENT.md`, `DOMAIN_PACK_SPEC.md`, `AUTHORITY_INDEX.md`, `ARCHITECTURE_TARGET_WORKFLOWS.md`.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Review scope

This review evaluates BrainAPI as an external event-centric knowledge graph and provenance-graph reference for architecture-agency workflows.

It does not approve installation.

It does not approve a dependency.

It does not create a Pantheon data platform, graph runtime, GraphRAG runtime, memory engine, approval engine, MCP runtime, plugin system, scheduler, queue, connector gateway, Hermes skill or OpenWebUI integration.

The goal is narrower:

```text
Can BrainAPI's event-centric graph model help describe how architecture workflow evidence should be linked, without importing BrainAPI as Pantheon machinery?
```

## External project summary

BrainAPI presents itself as a knowledge-graph-powered AI memory layer that turns raw text, documents and events into structured knowledge for search, recommendations and contextual memory.

The README describes:

- ingestion of raw text, documents, APIs and event streams;
- a dynamic event-centric architecture;
- graph reasoning and multi-hop retrieval;
- traceable graph paths rather than only similarity scores;
- REST, Python SDK, Node SDK and MCP query surfaces;
- plugin extensibility for ontology, routes, prompts and MCP tools;
- local setup through a TUI plus Docker-backed services.

For Pantheon, this is useful because architecture practice is event-heavy:

```text
site meeting
-> observation
-> enterprise concerned
-> lot
-> source document
-> reminder
-> decision
-> reserve
-> closure
-> trace
```

It is risky because BrainAPI uses the vocabulary of memory, reasoning and living knowledge. In Pantheon vocabulary, those outputs are not truth. They are relationship candidates, retrieval context candidates and evidence-support candidates.

## Technical characterization

BrainAPI should be interpreted as an external provenance-graph / knowledge-graph system.

```text
raw sources
-> ingestion pipeline
-> extracted entities / events / properties
-> linked graph
-> retrieval or graph path
-> Result Candidate + Evidence Pack Candidate support
```

The risky part is the same part that makes it powerful: the system does not merely store. It extracts, links, deduplicates and may consolidate inferred graph knowledge.

Pantheon interpretation:

```text
extracted node        = candidate observation
extracted relation    = relationship candidate
multi-hop path        = retrieval context candidate
consolidated inference = inferred candidate, never canonical memory
graph trace           = evidence support, not evidence by itself
```

A graph path can help explain why a result was produced. It cannot decide whether the result is professionally valid.

## Architecture-agency value

BrainAPI's event-centric model is relevant to architecture work because many agency problems are not isolated question-answer problems. They are chained dossier histories.

### 1. Site report and reserve chronology

Potential pattern:

```text
CR07 records point P
-> enterprise E is responsible
-> point P is reminded in CR08 and CR09
-> photo F supports persistent observation
-> reserve R is opened at reception
-> reserve R is lifted after evidence L
```

Useful output candidate:

```text
subject
lot
enterprise
date first observed
source reports
number of reminders
contradictory sources
resolution or last appearance
evidence pack candidate
```

Boundary:

```text
last mention in a CR does not prove resolution
photo metadata does not prove finding
enterprise linkage does not prove liability
human review remains required
```

### 2. Document intake and source qualification

BrainAPI could help connect project sources:

```text
signed quote
-> lot
-> amount
-> invoice
-> amendment
-> site report
-> visa note
```

The useful output is not an answer. It is a structured review surface:

```text
candidate source chain
version conflict
missing amendment
outdated reference
source status question
```

This fits `ARCHITECTURE_TARGET_WORKFLOWS.md`: source intake, source qualification, RAG retrieval, quality gate and trace decision remain separate atoms.

### 3. Photo review and CR escalation

Potential pattern:

```text
photo
-> EXIF candidate
-> project / address candidate
-> visual observation candidate
-> lot candidate
-> matching CCTP clause candidate
-> previous CR point candidate
-> proposed CR entry candidate
```

Boundary:

```text
image analysis is an index
not a formal site finding
not a measurement proof
not a contractor instruction
not a transmitted CR entry
```

A photo-derived observation may trigger a question or a draft CR point. It must not silently become a finding, reserve or instruction.

### 4. Repository governance and doctrine history

BrainAPI's graph model is also relevant to Pantheon repository work:

```text
issue
-> PR
-> comment
-> objection
-> decision
-> document
-> authority status
-> ai_log
```

Useful output candidate:

```text
open contradiction
candidate proposal
accepted / refused / to verify / to arbitrate classification
related doctrine
missing ai_log
```

Boundary:

```text
graph relation does not arbitrate doctrine
recent comment does not override canonical file
assistant proposal remains candidate until Zeus / human decision
```

## Layer mapping

| Layer | Classification |
|---|---|
| Pantheon Next | governance review, placement rule, evidence status, memory rule and approval boundary |
| Hermes Agent | possible external execution runtime for a sandboxed graph-preparation task under Task Contract |
| BrainAPI | optional external provenance graph / event graph candidate, not adopted |
| OpenWebUI | possible cockpit exposure of graph candidates, contradictions, source chains and User Decision Gates |
| Notion / project register | optional tracking surface for reviewed status, not source of truth by itself |

## Recommended classification

```text
name: brainapi
classification: External Provenance Graph / Event Graph Reference
pantheon_status: reference_review_only
hermes_status: optional_sandbox_candidate_only
openwebui_status: cockpit_exposure_candidate_only
memory_status: candidate_only / never_canonical
approval_status: not_approved_for_installation
dependency_status: not_approved
license_status: commercial-use review required before any professional integration
```

## Module-envelope interpretation

If BrainAPI is ever tested, its output must use the shared envelope:

```text
Task Contract in
-> external graph preparation or retrieval task
-> Result Candidate + Evidence Pack Candidate out
```

Allowed outputs:

```text
Graph Relation Candidate
Contradiction Candidate
Source Chain Candidate
Timeline Candidate
Retrieval Context Candidate
Evidence Pack Candidate support
Memory Candidate proposal
```

Forbidden outputs:

```text
Canonical Memory
approved truth
professional conclusion
source authority status
approval state
external action authorization
contractor instruction
formal reserve
signed or transmitted document
```

## Valuable patterns to distill

The following patterns are worth keeping, stripped of runtime authority:

```text
event-centric dossier modeling
actor / event / target / context attribution
time-aware relationship tracking
multi-hop source-chain review
contradiction surfacing
relationship candidate vs proof distinction
source graph as review interface
traceable path behind retrieval
```

For architecture workflows, the strongest distillation is:

```text
A dossier is not only a folder of files.
It is a chain of dated events, sources, claims, approvals, refusals, reminders and closures.
```

That insight belongs in Pantheon governance and domain packs. BrainAPI itself does not.

## Forbidden imports

Pantheon must not import:

```text
BrainAPI memory = Canonical Memory
knowledge graph = source of truth
graph path = proof
retrieval trace = Evidence Pack
consolidated inference = validated fact
plugin installed = capability approved
MCP available = tool authorized
BrainAPI pipeline = Pantheon workflow runtime
BrainAPI agent prompt = Pantheon Role
BrainAPI ontology = Pantheon doctrine
local console = Pantheon cockpit
```

## License and adoption warning

BrainAPI's license package is AGPLv3 plus Commons Clause with explicit commercial restrictions and a separate Enterprise License path.

Pantheon posture:

```text
reference review allowed
conceptual distillation allowed
installation not approved
professional integration not approved
commercial or agency use requires separate legal/licensing review
```

This is not a minor compliance note. For IFJ / professional architecture usage, the license may be blocking unless clarified or licensed separately.

## User Decision Gate triggers

Use a User Decision Gate before any of the following:

- installing BrainAPI;
- adding BrainAPI as dependency;
- using BrainAPI on real client or project data;
- exposing BrainAPI through MCP;
- installing BrainAPI plugins;
- treating graph output as evidence;
- promoting any graph-derived item to Memory Candidate;
- connecting BrainAPI to project registers, Notion, Gmail, OpenWebUI or Hermes;
- using BrainAPI output in a transmitted CR, visa note, reserve list, formal email or contractual position.

## Decision

```text
Accept the pattern.
Do not adopt the runtime.
Do not install by implication.
Keep as external reference and optional sandbox candidate only.
Represent output as Result Candidate + Evidence Pack Candidate support.
```

## Final rule

```text
BrainAPI may help map professional events.
It must not help Pantheon confuse mapped relations with proof, approval, memory or professional decision.
```
