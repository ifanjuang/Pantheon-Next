# Pantheon Revit Gate — developer framing dossier

Status: candidate support doctrine — Pantheon Revit Gate framing. Repository state: documented non-implemented.

This dossier frames a **local Revit plugin** governed by Pantheon. The plugin is
**runtime and lives outside Pantheon** (Hermes / local NAS side). Pantheon governs
the control bands, the gate, the warnings surfaced and the refusal posture. Nothing
here is implemented.

It implements no plugin, no Revit add-in, no MCP server, no schema, no test, no
Docker, no operations change. It does not claim the plugin exists.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A Revit plugin can read a model and, later, propose changes to it. That is
consequential and irreversible territory. The Pantheon Revit Gate is the
governance framing that keeps such a plugin **read-first, candidate-only and
human-gated**: it never lets the plugin act on a model without an explicit,
recorded human decision.

At MVP the plugin is **read-only**: it produces candidates (see the APU adapter
contract) and never writes to Revit.

## Control Band / Control Matrix

The **Control Band** classifies every plugin capability by reversibility and
consequence:

```text
B0 read-only        inspect model, export candidates           no write
B1 ephemeral        preview / temporary view, discarded         no persisted write
B2 reversible       a change with a guaranteed undo + diff       gated, dry-run first
B3 persistent       a change that survives save / sync           gated, high approval
B4 destructive      delete / move / parameter overwrite / sync   forbidden at MVP
```

The **Control Matrix** is capability × mode → required approval ceiling. It is a
documentation table, not an engine: it states what *would* be required, the
decision stays with the human gate.

```text
capability          dry-run   preview   temporary   persist
read model            n/a       n/a        n/a        n/a   (B0, always allowed read)
annotate candidate    allowed   allowed    allowed    gated (B2)
move / modify         allowed   allowed    allowed    forbidden at MVP (B3/B4)
delete / sync         n/a       n/a        n/a        forbidden at MVP (B4)
```

## Action modes and the governed decision queue

Candidate actions never apply directly. They pass through modes:

- **dry-run** — compute what the action would do, produce a before/after diff,
  apply nothing;
- **preview** — show the candidate effect in a discardable view;
- **temporary** — an effect that exists only for the session and is rolled back;
- **persist** — only after the human gate, and never at MVP.

Candidate actions wait in a **governed decision queue**: a review queue of
candidate actions awaiting the User Decision Gate. This decision queue decides
nothing on its own; it is a human-decision surface, not a runtime message queue
and not a scheduler. Items leave the review queue only by an explicit human
decision (accept / refuse / defer).

## Warning Broker

The **Warning Broker** surfaces Revit warnings, conflicts and the plugin's own
doubts to the human, with locators and context. It only surfaces and explains; it
resolves nothing and decides nothing. Every refusal it carries must be
explainable (which rule, which evidence, what is missing).

## Revit 2027 MCP / API capability notes

- Read-first: the gate's MVP relies on reading rooms, doors, walls, levels,
  grids, parameters, the active view and the current selection.
- The official Autodesk Revit 2027 MCP read-tools preview and community Revit MCP
  bridges are external-reference candidates only; see
  `PROJECT_UNDERSTANDING_EXTERNAL_REFERENCES.md`.
- Revit 2027 moves add-ins to .NET 10; any plugin must be built/ported
  accordingly. This is a runtime concern outside Pantheon.
- No write capability is described as available; write tools, if any, stay B3/B4
  and forbidden at MVP.

## Spatial understanding notes (Architectonics / Revit Dialect)

The plugin's reads map to the Architecture Project Understanding vocabulary, not
to a Revit-specific language:

```text
Revit Room            -> stable_object kind: space
Revit Door / Window   -> stable_object kind: opening
Revit Level           -> spatial_node node_kind: level
Revit GlobalId/ElementId -> source / evidence, never the internal stable_id
Revit parameter        -> attribute_claim (modality observed, E0-E4 certainty)
```

The plugin is one APU adapter among PDF/IFC/image readers and must respect the
APU adapter contract (`PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md`):
Task Contract in → Result Candidate + Evidence Pack Candidate out, candidate-only,
per-attribute provenance, no canonization, one-way dependency. "Revit Dialect" is
the source-specific surface; "Architectonics" is the governed, source-agnostic
project understanding it feeds.

## Installable packs (Hermes / external runtime side)

The plugin and its tools are distributed as packs that live outside Pantheon. The
dossier distinguishes four **separate** states, which must never be conflated:

```text
1. documented catalogue   a pack is described, with capability and band claims   (Pantheon documents this)
2. real installation      the pack is actually installed on a host / NAS         (runtime)
3. technical verification  install verified from its own logs and liveness        (dashboard verifies)
4. local execution        the pack actually runs and produces candidates          (runtime executes)
```

Pantheon owns only state 1 (the documented catalogue and the band/approval claims)
and the verification *criteria* of state 3. Installation and execution are runtime
zones; "documented" never implies "installed", and "installed" never implies
"verified" or "executed".

## Missing operational safeguards

A real Revit plugin is not safe until these are designed (all out of MVP scope,
listed so they are not forgotten):

- **worksharing / central file**: behavior with central models, workset
  ownership, sync conflicts, borrowing;
- **backup and restore**: a guaranteed restore point before any B2+ action;
- **idempotence**: re-running an action must not double-apply;
- **units and tolerances**: explicit unit system and geometric tolerance per
  measurement;
- **phases and variants**: which phase / design option an action targets;
- **linked models**: read vs act across links; never act in a linked model;
- **coordinates and project north**: survey vs project base point, true vs
  project north, shared coordinates;
- **selection scope**: an action applies only to an explicit, bounded selection;
- **user roles**: who may request, who may approve, per band;
- **family / parameter quality audit**: detect malformed families/parameters
  before relying on them;
- **temporary artifact cleanup**: remove preview/temporary artifacts reliably;
- **log confidentiality**: project logs may contain client-sensitive data;
- **doctor checks**: read-only health checks before and after a run;
- **Revit 2026 / 2027 compatibility**: .NET and API differences;
- **fictional test sets**: governed, non-client test models for validation;
- **explainable refusals**: every refusal names rule, evidence and what is
  missing;
- **safe-subset execution**: ability to run on a small, bounded safe subset
  first;
- **before / after diff**: every B2+ action carries a reviewable diff;
- **project-data vs graphic-projection separation**: a measured fact is not the
  same as how it is drawn;
- **Architectonics compatibility**: output conforms to the APU vocabulary and
  adapter contract.

## Boundary

- No plugin, add-in, MCP server, runtime, schema, test, Docker or operations
  change is added.
- The gate governs; the plugin (a separate `ifj-*` runtime repo) executes;
  the human decides.
- Repository state: documented non-implemented.

## Governance references

- docs/domain-packs/architecture/PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md
- docs/domain-packs/architecture/PROJECT_UNDERSTANDING_EXTERNAL_REFERENCES.md
- docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md
- docs/governance/CAPABILITY_PLACEMENT.md
- docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md
- docs/governance/APPROVALS.md
- docs/governance/BRIDGE_CONTRACT.md
