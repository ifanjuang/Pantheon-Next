# 2026-09-07 — Exact source materialization convergence

## Scope

Freeze the next Workspace -> Hermes execution seam without introducing a second source owner, parser pipeline, context browser, persistence path or contradiction engine.

Repository basis before the intervention:

```text
Pantheon-Next/main = 898f2fe05ddccf7952a932259aafdef7b42e648d
Pantheon-plugins PR #4 = merged as 5f874c58b64b09b4467c204901f770cdc84ae990
```

## Observed state

- Workspace qualification already emits exact `workspace://...?...sha256=...` source refs.
- Scoped Hermes Context deliberately exposes `source_dereference_available = false`.
- Launch Context Snapshot deliberately records `source_binary_included = false`.
- `implementation/mvp_vertical/documents.py` already owns a replaceable `DocumentConverter` abstraction and the current bounded Docling Serve adapter.
- Context Admission v2 already frames model-bound content as untrusted data with no instruction authority.
- The external `ExternalHermesRunBinding` already owns the one-shot native `/v1/runs` junction.
- No current adapter was found that provides a qualified architectural PDF visual/raster channel.

## Converged contract

```text
exact source_ref explicitly admitted in Context Pack
        ↓
external Run Binding materializes only that source
        ↓
secure exact read + admitted SHA-256 verification
        ↓
0..n transient replaceable representations
        ├── structural/text via existing DocumentConverter seam
        └── visual via a future separately qualified adapter
        ↓
Context Admission v2
        ↓
bounded Hermes run material
```

The existing closed boundaries remain unchanged:

```text
source_dereference_available = false
source_binary_included = false
```

Exact materialization is therefore not a global source-dereference feature and must not be added to the Pantheon context plugin.

## Workspace vocabulary preserved

```text
Source    = original file
Infos     = <basename>.yaml
Dialogue  = <basename>.dialogue.md
Contenu   = <basename>.md only after explicit ingestion
Notes     = independent working Markdown notes
Connaissances = existing transversal Pantheon Knowledge corpus
```

Qualification remains transient:

```text
Qualifier != Ingérer
transient representation != Contenu persisted
conversion success != Evidence
folder/package != governed identity
```

## Provider posture

Docling is an available structural-analysis provider behind the existing converter seam. It is not frozen as the architecture.

Architectural plans require the contract to permit multiple transient representations from the same exact source. A future visual adapter may provide rendered pages/images or other bounded visual material without creating a second source identity or persistence owner.

## Product proof target

The enabling infrastructure is justified by issue #986, not by a desire to add another architecture layer.

The relevant success condition is stronger than `Hermes read the PDF`:

```text
multiple explicitly admitted project sources
→ Hermes keeps conflicting source-backed statements separate
→ sources / timing / uncertainty remain visible
→ contradiction is surfaced before a professional decision
→ Hermes does not select a winner without an admitted basis
```

Existing ProjectClaim conflict detection, bitemporal reads and Missing Information doctrine remain separate owners. This intervention does not wire them together automatically and does not implement #1012.

## Changed paths

```text
implementation/docs/HERMES_RUN_LAUNCH_JUNCTION.md
tests/test_exact_source_materialization_contract.py
ai_logs/2026/Q3/2026-09-07-exact-source-materialization-contract.md
```

## Not implemented by this intervention

- Workspace source byte/path materializer in the Run Binding;
- Docling conversion wired into `/v1/runs` input;
- visual/raster PDF adapter;
- multi-source runtime materialization;
- `<basename>.md` ingestion;
- structured Hermes -> Infos YAML persistence;
- proactive Cockpit contradiction attention;
- historical as-of conflict reconstruction (#1012).

## Done criterion for this slice

The architecture is frozen only as a contract and regression guard. Implementation must reuse the named existing owners and demonstrate one exact Workspace PDF end to end before widening to multi-source/visual qualification.
