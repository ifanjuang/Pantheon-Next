# Contributing

Status: active support — repository contribution guardrail.

This file does not create doctrine by itself. It explains the minimum review discipline for changing Pantheon Next.

The canonical architecture boundary is stated in `README.md`, `STATUS.md` and `AUTHORITY_INDEX.md`. Contribution material should not repeat the slogan mechanically; use explicit boundary fields when reviewing a concrete change.

## Before significant work

Read these files first:

```text
docs/governance/STATUS.md
docs/governance/WHAT_RUNS.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/MODULES.md
docs/governance/README.md
docs/governance/BOUNDARY_PROFILES.md
docs/governance/NON_EQUIVALENCE_RULES.md
```

The repository overrides prompts, comments, historical plans and previous assistant summaries.

## Classify the change

Every significant change should say what it is:

```text
canonical doctrine
active support doctrine
candidate / to verify
validation-only
external reference
implementation artifact
voluntarily absent
obsolete / refused
not applicable
```

Do not let examples, comments, diagrams, static prototypes, watchlists or candidate notes imply live behavior.

## Keep the boundary

Pantheon Next may govern consequential decisions:

```text
truth status
memory status
evidence requirement
approval path
scope boundary
external action
activation
installation proposal
update authorization
runtime health visibility
rollback visibility
```

Pantheon Next must not silently become:

```text
execution runtime
agent loop
scheduler
queue
provider router
MCP host
plugin manager
memory engine
automatic approval system
installer
updater
external sender
```

For concrete capabilities, repos, skills, connectors, workflows or runtime changes, express the boundary as fields:

```text
exposed_by
executed_by
governed_by
approved_by
forbidden
```

For repeated non-runtime disclaimers, use `docs/governance/BOUNDARY_PROFILES.md` instead of copying a long boilerplate paragraph.

For repeated “X does not mean Y” lists, use `docs/governance/NON_EQUIVALENCE_RULES.md` and repeat only the local distinctions that matter.

Boundary profiles and non-equivalence rules reduce repetition. They do not hide consequential effects.

## Protected paths

Changes under these paths require explicit review:

```text
schemas/
tests/
pyproject.toml
operations/
platform/
Docker files
.env files
CLAUDE.md
mcp-server/
GitHub Actions / CI scripts
```

A green check, a useful prototype or a successful local run does not authorize a protected-path change.

## Capability review

Before adopting, documenting, activating or recommending an external capability, classify it as a Capability Slot:

```text
abstract capability
→ candidate Hermes binding
→ installation status
→ health status
→ update status
→ activation status
→ Pantheon gates
→ human approval
```

Answer these questions:

1. What consequence can it produce?
2. What executes it?
3. What does Pantheon govern?
4. What evidence is required?
5. What human approval is needed?
6. What must remain forbidden?

Use local distinctions from `docs/governance/NON_EQUIVALENCE_RULES.md`, especially:

```text
installed        ≠ approved
healthy          ≠ safe
update_available ≠ update_authorized
runtime_success  ≠ evidence
binding_selected ≠ dependency_adopted
watchlist_item   ≠ install_instruction
```

## Promotion rule

A candidate does not become active doctrine because it is repeated, useful or old.

Promotion requires a referent:

```text
schema
test
end-to-end example
read-only verification surface
explicit dated human decision in ai_logs/
```

Without a referent, keep the material candidate, support, validation-only or reference.

## Commit and PR discipline

A good change states:

- what changed;
- which authority class it affects;
- whether it changes runtime status;
- whether protected paths are touched;
- what remains non-implemented or to verify.

Prefer small, reviewable changes. Do not bundle doctrine, runtime artifacts and public wording unless the relation is explicit.

## Final rule

```text
Documentation may describe.
Static pages may expose.
Read-only checks may verify structure or status.
External runtimes may execute under contract.
Pantheon governs consequential status.
The human decides.
```
