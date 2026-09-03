# 2026-09-03 — Governed cognitive ecology grammar

## Objective

Converge the existing Pantheon Roles / Rites / governed Spaces doctrine into a compact explanatory grammar before the next ProjectClaim provenance slice, and surface the same reflection on the public landing page.

This intervention is explanatory and navigational. It creates no new governance authority, schema family, registry, runtime, persistence model, lifecycle or executable path.

## Repository state checked

Base `main` at the start of this intervention:

```text
f72cf87645656e4121312535a28b404ca622edbe
```

This is the merge commit of PR #947 (`feat(agency): add temporal ProjectClaim reconstruction`).

Open PRs reviewed before modification concerned MarkdownDB qualification, Google Drive qualification and Hermes Desktop direction; none owned this conceptual convergence.

Existing owners already established the relevant distinctions:

- `docs/governance/AGENTS.md`: Pantheon Roles are standing governance responsibilities, not executable agents;
- `docs/governance/rites/README.md`: Rites are bounded governance methods, not workflows or runtimes;
- `docs/governance/EVOLUTION_OF_ROLES_RITES_AND_SPACES.md`: governed Spaces are durable activity distinctions, not screens or lifecycle owners;
- `docs/governance/CORE_CONCEPTS_MAP.md`: compact navigation and ownership entry point;
- `docs/governance/MODULES.md`: architecture responsibility families;
- `docs/governance/authority/PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json`: machine-readable ownership dimensions.

## Interpretation retained

Pantheon may be understood as a **governed cognitive ecology** rather than a central brain or a multi-agent execution team.

The phrase is a navigation model only.

```text
Roles                  -> who carries a standing judgment responsibility
Rites                  -> how bounded review is structured
Governed Spaces        -> where a durable kind of activity belongs
Governed Objects       -> what carries identity, state and lifecycle
Rules / Contracts /
Invariants             -> what constrains interpretation and effects

Hermes                 -> executes admitted work
Human                  -> decides consequential effects where required
```

The mythological vocabulary is a memory aid for human readers, not an ownership model.

## Four complementary maps

The intervention makes four existing views explicit instead of collapsing them:

```text
1. concept grammar
   Role / Rite / Space / Object / Rules-Contracts-Invariants

2. architecture placement
   Governance Kernel / Governed State / Admission / Execution / Projection

3. authority topology
   semantic / implementation / transition / persistence / runtime / projection owners

4. governed flow
   source or observation -> candidate -> governed state -> review / decision -> effect -> new observation
```

These maps answer different questions and must not redefine one another.

## Changes

### `docs/governance/CORE_CONCEPTS_MAP.md`

Added a `Governed cognitive ecology` navigation section that:

- defines the concept grammar;
- keeps `Rules / Contracts / Invariants` descriptive rather than creating a machine category;
- distinguishes the module-family map from the ownership registry;
- describes the governed flow;
- adds an extension-before-creation placement test.

### `docs/governance/EVOLUTION_OF_ROLES_RITES_AND_SPACES.md`

Added an explicit boundary stating that the cognitive-ecology metaphor:

- does not create a `cognitive_ecology`, `god`, `law`, `object` or `space` registry;
- does not create a schema family, runtime or new authority plane;
- leaves governed Objects, Rules, Contracts and Invariants with their existing owners.

### `docs/index.html` and `docs/index-en.html`

Matured the existing Roles / Spaces / Rites landing section rather than adding a parallel section.

Public framing:

```text
Pas un cerveau central : une écologie de l’attention.
Not a central brain: an ecology of attention.
```

The landing explains that distinct forms of attention can coexist, disagree and correct one another while Objects retain their own history/provenance and Rules retain their owners.

No new CSS or presentation component was introduced.

## Preserved distinctions

```text
mythology != authority
Role != executable agent
Rite != workflow runtime
Space != object lifecycle owner
Scene / screen != governed Space
Object displayed != object authorized
Rule constrains != rule executes
confidence != authority
candidate != governed state
retrieved != truth
memory != Evidence
projection != persistence
runtime success != authorization
```

## Relationship to P2

This intervention does not replace or broaden the planned structured-provenance work.

The next functional slice remains the observed ProjectClaim provenance loss:

```text
ProjectClaimCandidate.basis_refs
        -> human reviewed candidate
        -> ProjectClaim.provenance.basis_refs
```

The cognitive-ecology grammar is intended to make placement decisions easier before P2/P3/P4, especially to avoid prematurely inventing a universal Derivation authority, a Conflict authority or a global Identity resolver.

## Scope deliberately excluded

- no schema change;
- no SQL migration;
- no ownership-registry change;
- no PDP/PEP change;
- no runtime or Hermes binding change;
- no Cockpit implementation change;
- no new governed Object;
- no new Role, Rite or governed Space;
- no authority promotion.

## Review context

PR #948 opened from `docs/cognitive-ecology-grammar`.

The first Governance CI run correctly refused the PR because the Role / Rite / governed-Space change guard requires explicit review-context sections in the PR body. The body was then completed with:

```text
Change level
Observed need
Existing owners checked
Overlap analysis
Affected consumers
Migration and rollback
Authority impact
Runtime impact
```

The declared change level is guidance/explanatory convergence with no Role jurisdiction, Rite purpose/lifecycle, governed Space identity, authority boundary or runtime change.

## Status

PR #948 is the review surface for this bounded conceptual convergence.

Repository CI and review remain the merge gate.
