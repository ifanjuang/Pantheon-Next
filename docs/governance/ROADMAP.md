# Pantheon Next Roadmap

Status: active support doctrine — outcome-oriented repository roadmap — implemented as documentation.
Boundary profile: active_support_doctrine.

This roadmap states the next governed outcomes for Pantheon Next. It is not a document inventory and it is not a runtime implementation plan.

Use the repository status spine for current facts:

```text
STATUS.md          -> current repository posture and unresolved clusters
WHAT_RUNS.md       -> what actually runs, is static, is partial or is absent
AUTHORITY_INDEX.md -> authority and repository state
MODULES.md         -> ownership and boundary by governance area
```

If this roadmap conflicts with that spine, the status spine wins.

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```

Pantheon may govern consequential status: truth, memory, evidence, approval, scope, external action, activation, proposed installation, update authorization, runtime-health visibility and rollback visibility.

Pantheon must not become an execution runtime, installer, scheduler, queue, provider router, MCP host, plugin manager, memory engine, automatic approval system or external sender.

## Current position

Status: partial but structurally coherent.

### Repository foundation

Outcome: implemented.

Current evidence:

- Pantheon Next is self-contained and has no active dependency on its retired predecessor;
- the repository-status spine is established;
- contribution, protected-path and promotion rules are documented;
- the repository root is deliberately non-distributable;
- pull-request review and governance checks are the normal change path.

Remaining checkpoint:

- publish the maintainer-created `v0.1.62` tag on commit `70d3a7bdf6b40807c0ba01ccc159945e43458e2c` and verify the tag-triggered checks.

### Governance kernel

Outcome: coherent baseline, still under controlled consolidation.

Current evidence:

- roles, Task Contracts, Evidence Packs, approvals, scope, knowledge, runtime-memory and Registre Probatoire boundaries are documented;
- capability placement and external-adapter boundaries are explicit;
- status headers, boundary profiles and non-equivalence rules reduce free-form drift;
- Card Stack, Context Stack and Method Card models exist as candidate UX/governance doctrine.

Remaining work:

- reduce navigation cost;
- close obsolete active references and terminology debt;
- promote, merge, archive or refuse candidates instead of creating parallel models.

### Read-only policy and verification surface

Outcome: implemented read-only / partial / protected path.

Current evidence:

- `mcp-server/` exposes bounded consultation, classification and validation tools;
- the Governance Doctor fails closed when mandatory checks cannot run;
- authority resolution is shared between the MCP and repository checks;
- packaging is limited to the `mcp-server/` distribution.

Remaining work:

- normalize the repeated verification family;
- remove migration-era CI checks that no longer represent active repository work;
- keep collection of runtime evidence outside the MCP.

### External execution bindings

Outcome: first slices implemented and tested externally; no binding adopted.

Current evidence:

- the external `pantheon-mvp` candidate implements a bounded task loop, Work Issues, document extraction, Project Document Cards, versioned Knowledge publication and conflict-safe mobile editing at a pinned reviewed commit;
- external tests establish implementation evidence for that commit.

Still absent:

- installation in the real environment;
- live Hermes proposal binding;
- authorization for real dossiers;
- production activation;
- professional validation.

### Cockpit and visual surfaces

Outcome: candidate models and static or external prototypes.

Current evidence:

- Card Stack is the single current owner of Card, Scene, Deck, Constellation and navigation grammar;
- Pantheon Control assets are static prototypes;
- the Hermes dashboard template has one shared renderer for its installable external plugin and synthetic public preview.

Remaining work:

- validate one complete decision journey before expanding the UX grammar;
- keep synthetic, external-live and governed status visibly distinct.

### Professional corpus and adapters

Outcome: external / to verify.

Current position:

- `base_metier/architecte/` is a professional corpus and adapter proving area, not Pantheon authority or proof;
- source licensing remains to verify;
- ingestion and transformation scripts belong on the Hermes/adapters side;
- real professional and client data must remain outside the public governance repository.

## Governed outcomes

### R1 — Reduce repository navigation cost

Status: in progress.

Target outcome:

```text
one short stable read path
+ task-based read paths
+ roadmap limited to outcomes, blockers and exit criteria
+ explicit kernel / adapter / corpus boundaries
```

Exit criteria:

- the default read path is no longer an exhaustive document list;
- `ROADMAP.md` does not duplicate authority or module indexes;
- active summaries contain no stale path to a removed document;
- `base_metier/architecte/` no longer claims to be an internal Pantheon RAG runtime.

### R2 — Close terminology and schema debt

Status: pending reviewed changes.

Target outcome:

```text
no unjustified retired Register vocabulary
+ one governed certainty representation
+ reliable Project Understanding references
```

Tracked blockers:

- issue #90: classify and resolve remaining retired Register vocabulary;
- issue #169: reconcile shared definitions, certainty vocabulary and referential integrity before Project Understanding promotion.

Exit criteria:

- every retained historical vocabulary occurrence is explicit;
- E0-E4 is the single governed certainty representation;
- schema references and identifiers fail closed when inconsistent;
- no ontology expansion is bundled into the debt-payment change.

### R3 — Simplify read-only verification

Status: planned / protected review required.

Target outcome:

```text
one internal verification result contract
+ explicit MCP tools
+ one CLI family
+ shared checks between CI and Doctor
```

Exit criteria:

- install, observability, backup, exposure and update verifiers use a consistent envelope;
- existing external command names remain compatible during transition;
- no verifier probes, installs, updates, writes, approves or gathers secrets;
- migration-era CI checks are replaced by a current predecessor-independence check.

### R4 — Prove one external vertical

Status: documented and ready for an external operator; not executed.

Candidate vertical:

```text
architecture_devis_reprise
```

Target loop:

```text
OpenWebUI
-> bounded Task Contract
-> Hermes execution
-> Result Candidate + Evidence Pack Candidate
-> Pantheon read-only structural/status checks
-> explicit human decision
-> verified rollback
```

Entry conditions:

- audited Pantheon tag and MCP wheel;
- isolated external environment;
- exact Hermes, OpenWebUI and adapter versions recorded;
- fictional data only;
- read-only Pantheon checkout;
- separate credentials and rollback plan.

Exit criteria:

- runtime trace, candidate result, candidate evidence and human decision are separate;
- no client data or external consequential action is used;
- rollback is demonstrated;
- observed doctrine gaps become separate issues or PRs, not opportunistic patches in the validation record.

### R5 — Decide adoption after evidence

Status: blocked by R4.

Possible decisions:

```text
refuse adoption
continue a bounded trial
adopt one binding for one scope
request more evidence
```

Adoption must remain separate from installation, health, enablement and runtime success.

## Work-selection rule

Before adding a new permanent model or document, answer:

1. Which existing owner document cannot express the needed rule?
2. What observed consequence requires the addition?
3. What referent will support promotion?
4. What is the exit criterion: promote, merge, archive or refuse?
5. Does the proposal reduce or increase the repository's navigation and maintenance cost?

Default:

```text
extend an existing owner
before creating a new model
```

## Current priority order

```text
1. create and verify the v0.1.62 maintainer tag
2. reduce navigation and clarify repository boundaries
3. close terminology debt
4. reconcile Project Understanding schemas
5. simplify the MCP verification family and active CI
6. tag the resulting bounded MCP checkpoint
7. execute the first fictional external vertical
8. decide adoption from evidence
```

## Final rule

```text
Do not expand the doctrine to avoid testing it.
Reduce.
Stabilize the contracts.
Run one bounded vertical.
Measure the gaps.
Promote, merge, archive or refuse.
```
