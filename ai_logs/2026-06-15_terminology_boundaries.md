# AI log — terminology boundaries

Date: 2026-06-15

## Request

User asked to add the new Pantheon Next terminology to the repository for future development and cleanup of existing vocabulary.

## Canonical sources read

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/README.md`
- `docs/governance/CORE_CONCEPTS_MAP.md`
- `docs/governance/EDITORIAL_LANGUAGE.md`
- `docs/governance/WORKFLOW_FORGING_PROTOCOL.md`
- `docs/governance/REQUEST_LIFECYCLE.md`

## GitHub coordination

Searched open issues and pull requests for terminology / vocabulary / lexicon / workflow / capability / skill / memory / assertion / approach conflicts. No directly matching open issue or PR was found.

Attempted branch creation first, but the connector required a concrete commit SHA and branch creation was not completed. The documentation-only changes were then applied directly to the default branch under allowed documentation paths.

## Changes made

Created:

- `docs/governance/TERMINOLOGY_BOUNDARIES.md`

Updated:

- `docs/governance/README.md`
- `docs/governance/AUTHORITY_INDEX.md`

No protected paths were modified.

## Doctrine added

The new terminology boundary document establishes:

- `Case / Affaire` as professional unit.
- `Situation` as concrete trigger or tension.
- `Approach / Démarche` as governed reusable handling of a recurring situation.
- `Capability / Capacité` as Pantheon-governed function.
- `Assertion` as truth-status object.
- `Evidence / Preuve` as review support, status-qualified.
- `Recall / Rappel` as runtime memory output, candidate only.
- `Register / Registre` as validated durable memory.
- `Workflow`, `Skill`, `Tool`, `Plugin`, `Job`, `Action`, `State`, `Run`, `Node`, `Edge`, `Checkpoint`, `Thread`, `Queue`, `Scheduler`, `Worker` as reserved runtime or host-system terms.

## Decision status

Accepted:

- Use `Case / Affaire` instead of `Matter` or system-level `Dossier`.
- Use `Approach / Démarche` instead of `Path` or `meta-workflow`.
- Use `Assertion` instead of `Claim` / `Affirmation` as canonical truth-status object.
- Use `Capability / Capacité` in Pantheon and reserve `Skill` for Hermes/runtime execution.
- Use `Recall / Rappel` for external memory output and `Register / Registre` for validated memory.
- Treat `Attribute / Attribut` as descriptive metadata only, not authority.

Refused:

- `meta-workflow` as a canonical term.
- `agent` for Pantheon Roles.
- unqualified `memory` as a governance object.
- `skill` as Pantheon canonical capability language.

To verify:

- Progressive cleanup of older documents that still use `dossier path`, `workflow` or `memory` in broader senses.
- Whether `Domain Pack` should remain internal canonical vocabulary or be progressively paired with `Method / Méthode`.

## Repo state

Documented non-implemented / active support doctrine.

No schema rename, runtime behavior, terminology linter, field migration or external action was implemented.
