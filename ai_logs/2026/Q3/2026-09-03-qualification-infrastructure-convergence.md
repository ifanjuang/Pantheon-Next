# External qualification infrastructure convergence

Date: 2026-09-03
Status: implementation-support correction — review pending.
Boundary profile: validation / qualification support.

## Objective

Repair two concrete qualification-harness defects exposed independently by the open MarkdownDB and Graphify qualification work without adding a provider-specific workaround or a new governance concept.

## Repository state checked

Baseline before change:

```text
Pantheon-Next/main = d3f0fab72f64714010e30abc3e03c001b441eb1b
```

This baseline includes merged #951 (`docs(memory): preserve free episodic memory beside structured project knowledge`). That change touches Memory doctrine only and does not own external qualification infrastructure.

Open work checked before modification included:

- #925 Hermes Desktop direction;
- #930 Google Drive read qualification;
- #944 MarkdownDB structural-index qualification;
- #950 Graphify structural-gain qualification.

No open change owned the shared qualification support defect described below.

## Observed defect 1 — current-pin literal guard was globally over-broad

`implementation/tests/test_external_qualification_pins.py` previously collected every current provider `version` and `ref` and forbade those strings across all Python/YAML/shell/TypeScript files in broad test/tool/workflow trees.

That correctly catches a qualification consumer which restates its provider pin instead of importing it from `external-pins.json`, but it also makes an unrelated application/test datum illegal when it happens to equal a short semantic version currently used by any provider.

The MarkdownDB qualification exposed this with an unrelated RuntimeObservation test value.

The ownership rule remains:

```text
external-pins.json = sole current qualification-pin owner
```

The correction narrows only the collision domain:

```text
provider consumer + provider current literal copied
= reject

unrelated code/test datum + coincidental same short version
= allowed
```

A file is treated as a consumer of a specific provider when it names that provider by pin id, env prefix, repository, package or image. The guard still rejects current version/ref literals in that consumer.

Regression tests prove both sides with synthetic provider data.

## Observed defect 2 — read-only repository baseline treated gitlinks as files

The first Graphify Q2 run failed before Graphify extraction while recording the Pantheon tracked-material baseline.

The harness used:

```text
git ls-files
-> Path.read_bytes() for every tracked path
```

Pantheon contains a real gitlink/submodule path:

```text
implementation/mvp_vertical/cockpit/vendor/radix-icons/upstream
```

A gitlink is an index object reference, not an ordinary tracked file. A read-only qualification baseline must therefore distinguish Git object kinds instead of assuming every tracked entry is a file.

## Reusable correction

Added `implementation/tools/git_material_snapshot.py`.

Its contract is deliberately small:

```text
regular tracked file
-> SHA-256 current worktree bytes

tracked symlink
-> SHA-256 link-target text, without following the target

gitlink/submodule
-> exact index object id, without opening it as a file

working-tree mutation
-> complementary git status --porcelain --untracked-files=all
```

The helper does not interpret a clean snapshot as Evidence, authorization, deployment truth or professional currentness.

Tests cover:

- changed ordinary bytes change the snapshot and dirty Git status;
- a synthetic mode-160000 gitlink is recorded without filesystem access;
- symlink identity is hashed independently of target-file bytes when symlinks are available.

## Qualification lifecycle kept existing

No new lifecycle registry or status field is introduced.

The existing registry already states that `external-pins.json` contains **current external-component qualification inputs** and is not a historical qualification-run record. The separate upstream-observation file remains one-to-one with those current pins.

Therefore the existing convergence rule remains sufficient:

```text
provider still guards a current qualification decision
-> current pin + current upstream observation + active qualification surface when needed

qualification completed/rejected and no current decision depends on rerunning it
-> preserve observed result/provenance
-> remove it from current qualification inputs rather than inventing a historical pin lifecycle
```

That rule will be applied separately to #944 after this shared infrastructure correction is accepted.

## Preserved boundaries

```text
qualification success != dependency adopted
qualification failure != provider failure when the harness failed first
pin registry != deployment truth
upstream observation != update authorization
clean repository snapshot != Evidence
provider graph/index != governed relation
provider id != governed identity
runtime success != authorization
projection != persistence
```

## Not in scope

- no Workspace, Graph, Memory, Source or Evidence owner change;
- no Capability Slot;
- no schema or SQL migration;
- no provider binding;
- no runtime dependency;
- no Graphify or MarkdownDB acceptance decision;
- no change to #925 or #930 in this intervention.

## Done criteria

- provider-scoped current-pin guard passes unrelated semantic-version data while still rejecting a provider consumer that copies its current version/ref;
- Git material snapshot handles ordinary files, symlinks and gitlinks deterministically;
- repository CI passes on current main;
- Graphify Q2 can then consume the helper and reach actual upstream extraction;
- MarkdownDB #944 can then be converged using the existing current-vs-historical qualification distinction rather than a provider-specific exemption.
