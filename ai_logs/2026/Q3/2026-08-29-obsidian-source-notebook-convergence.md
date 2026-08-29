# Obsidian source notebook convergence — 2026-08-29

## Objective

Make a human-maintained source notebook in an optional Markdown workspace
discoverable to bounded Hermes research without creating a second Source
Registry, a fixed Obsidian folder convention or one manifest per website.

## Repository checkpoint

```text
Pantheon-Next/main = ce8321ce074fa1343c8915dbaec6e4e98e308c3b
```

## Observed owners

- `SOURCE_NEED_AND_REGISTRY.md` already owns Source Needs, Source Leads, Source
  Addition Candidates, Source Registry Entries and freshness policy.
- `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` owns the qualified optional workspace
  reference and keeps workspace paths separate from governed identity.
- `templates/hermes/skills/source-research/SKILL.md` is the single surviving
  bounded Hermes research-skill candidate.
- existing source-owner and source-research tests already guard these boundaries.

No distinct owner, registry engine, Obsidian plugin, Cockpit implementation,
schema or per-site manifest is required for this slice.

## Decision

Extend the existing source owner with one optional `workspace source notebook`
concept. It is a human discovery surface containing Source Leads and working
annotations. It may be a single note organized by source family, and its path is
a deployment choice rather than a Pantheon contract.

Allow the existing Hermes research-skill candidate to consult that notebook only
inside authorized task/context scope. Every listed route still requires exact
source inspection. Recurrent or consequential routes use the existing Source
Addition Candidate and Source Registry review path.

## Changed surfaces

```text
docs/governance/SOURCE_NEED_AND_REGISTRY.md
docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md
templates/hermes/skills/source-research/SKILL.md
tests/test_source_document_owner_convergence.py
tests/test_source_research_skill_contract.py
```

The protected test changes are part of the explicitly authorized work package and
only verify existing-owner convergence and non-equivalence boundaries.

## Runtime and adoption impact

None.

The skill remains a non-executable candidate template. The Obsidian/Hindsight
composition remains optional and external. No notebook, registry database,
retrieval runtime, Cockpit Card, source write, Evidence admission, memory
promotion or external action is implemented by this change.

## Preserved invariants

```text
workspace source notebook != Source Registry
notebook entry != Source Registry Entry
listed route != inspected source
workspace path != governed identity
workspace access != task authorization
registered source != Evidence
projection != persistence
```

## Verification

Run the existing targeted source-owner and source-research tests, then the
repository governance checks required for documentation and protected-path
changes. Merge remains a separate reviewed decision.
