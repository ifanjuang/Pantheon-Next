# Monorepo placement language reconciliation

Date: 2026-08-24
Status: validation trace — no authority transfer

## Objective

Reconcile active repository, template and documentation placement language after the `pantheon-mvp` history import, direct canonical contract consumption and architecture-owner migration.

The change distinguishes current implementation placement from historical repository provenance. It does not erase historical PRs, issues, commits or source references.

## Verified starting state

Before this tranche:

```text
Pantheon-Next/main = 16688770e7e51097fca05053adaf040ca9fcd1f0
pantheon-mvp/main  = d960862dd0e23b7003a0f3e4ee0ea630ffc12af9
```

The former `ifanjuang/pantheon-mvp` repository was still public and unarchived, but its `main` remained exactly at the imported cutoff and it had no open pull requests. No parallel implementation trajectory was therefore observed.

The current Pantheon-Next implementation is co-located under `implementation/`.

## Prior convergence already merged

This reconciliation follows completed structural work:

- history-preserving import of former `pantheon-mvp` under `implementation/`;
- direct canonical root schema consumption with generated wheel snapshots only;
- Hermes distribution composition resolved from one monorepo source root;
- architecture audit expressed through physical zones rather than repository count;
- ownership registry revision 3 using `Pantheon governance` and `Pantheon implementation` instead of repository names;
- Architecture Audit adoption of those logical owner identities.

The relevant ownership migration was merged through PRs #699 and #700. Green CI for that migration established implementation/audit consistency only; it did not create authorization, Evidence or deployment.

## Observed stale active language

Fresh repository review found several active surfaces that still described the imported implementation as an external `pantheon-mvp` owner or current consumer even though canonical status documents already described the monorepo placement.

Examples included:

- root work rules describing initial vendoring/repository-label debt as still pending;
- Hermes template review instructions naming current `pantheon-mvp/main`;
- Tool Card ownership assigning concrete projection to `pantheon-mvp`;
- Registry Foundation describing cross-repository validation and future vendored references;
- Card Stack and Pantheon Control orientation pointing to the former external Cockpit as current source;
- Runtime Adapters authority-map Tool Card row retaining the former implementation owner.

These were current-placement contradictions, not historical evidence.

## Changes in this tranche

Active placement language now uses:

```text
Pantheon governance
Pantheon implementation
implementation/
implementation/mvp_vertical/cockpit/
```

The former repository name remains only where it identifies historical provenance, such as:

```text
former repository
source cutoff
historical PR / issue
historical commit
historical public demo observation
```

The following surfaces were reconciled:

- `CLAUDE.md`;
- `docs/governance/NEXT_MVP_REPOSITORY_PLACEMENT.md`;
- `templates/hermes/CLAUDE.md`;
- `templates/hermes/DESIGN.md`;
- `templates/hermes/README.md`;
- `docs/assets/README.md`;
- `docs/assets/card-stack/README.md`;
- `docs/assets/pantheon-control/README.md`;
- `docs/assets/pantheon-control/index.html`;
- `registries/README.md`;
- `docs/governance/TOOL_CARD_MODEL.md`;
- the Tool Card row and interpretation note in `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`.

A focused regression test under `tests/test_monorepo_placement_language.py` refuses the retired active-placement phrases while explicitly requiring historical provenance to remain readable.

## Deliberately open follow-up

This tranche does not rewrite every old `external implementation` phrase in one pass.

A separate runtime/operator reconciliation remains necessary for documents whose placement wording is coupled to deployment or runtime semantics, including Phase B, Paperless, Portainer, Hermes Run and related Runtime Adapters index rows. Those files must be reviewed against their current implementation paths and tests rather than mechanically renamed.

The Revit block is also deliberately separate. The server-side Pantheon implementation references should converge on `implementation/`, while the actual Revit add-in/Host Agent external implementation boundary must remain distinct. That distinction must be preserved across `REVIT_LOCAL_ADAPTER.md` and `revit-plugin/` together.

Historical validation traces such as `PANTHEON_MVP_COCKPIT_RECONCILIATION.md`, imported implementation `ai_logs/`, and former PR/commit references are intentionally not rewritten.

## Invariants

```text
repository != owner identity
folder/path != governed identity
historical source != current implementation path
co-location != authority transfer
retrieved != truth
memory != Evidence
runtime success != authorization
runtime success != Evidence
projection != persistence
```

## Completion criteria for this tranche

The tranche is complete when:

- active surfaces changed here no longer point current implementation ownership to `pantheon-mvp`;
- historical repository provenance remains explicit;
- Runtime Adapters map agrees with the changed Tool Card owner;
- the focused regression test passes;
- repository CI passes on the final pull-request head;
- no review blocker remains.

This trace records repository convergence only. It installs, activates, deploys, authorizes and admits no Evidence.
