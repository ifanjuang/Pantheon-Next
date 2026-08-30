# 2026-08-30 — converge bounded obsidian-wiki maintenance patterns

## Objective

Review the current `Ar9av/obsidian-wiki` maintenance model against current Pantheon Next `main` and retain only behavior that fills a demonstrated gap without creating a parallel Knowledge, manifest, retrieval, provenance or approval owner.

## Current-state checks

- #848 is merged and already owns `search-before-create` plus explicit conversation consolidation in `docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`.
- `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md` already owns reusable Markdown Knowledge organization and the visible `generated_unreviewed | needs_review | reviewed | superseded` review posture.
- `docs/governance/DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md` plus `implementation/mvp_vertical/knowledge.py` already provide source refs/digests, optimistic versions, idempotent material writes and candidate edit requests for the implemented candidate Knowledge slice.
- `docs/architecture/WORKSPACE_MANIFEST_INSPECTOR_CANDIDATE.md` already owns manifestability and local package-health semantics.
- Hindsight remains the qualified/recommended optional derived retrieval provider in the current Obsidian reference profile; the generic external runtime-memory binding remains unbound.
- #852 adds Word-Smith only as optional Obsidian authoring/document-assembly UX in the same owner. That addition is preserved and does not replace or conflict with the maintenance behavior distilled here.
- #855 is merged and changes only Hermes pin assertions; it does not overlap this workspace slice.
- #849 is merged and remains confined to the professional quote-review qualification corpus; it does not overlap this workspace slice.

## External patterns reviewed

The current `Ar9av/obsidian-wiki` architecture demonstrates useful ideas including:

- staged LLM writes;
- source-delta manifest tracking;
- statement posture such as extracted/inferred/ambiguous;
- lint/dedup/cross-link maintenance;
- whole-vault equilibrium checks;
- tiered graph/query behavior.

Its current repository also has open edge cases around reserved staging paths and valid Obsidian wikilink/embed forms. Those observations support retaining maintenance as report-only by default rather than importing automatic rewrite behavior into professional workspaces.

## Convergence decision

Do not import the upstream subsystem.

The staging, source-delta ledger, lifecycle/trust and retrieval responsibilities are already covered by existing Pantheon owners or would create parallel authority if copied literally.

Retain only two additive behaviors inside the existing optional second-brain owner:

1. a bounded report-only workspace audit that may surface duplicate candidates, malformed/unresolved links, stale summaries/source refs, contradiction candidates, orphans and missing cross-links, while refusing automatic mutation;
2. lightweight narrative annotations `extracted`, `inferred` and `ambiguous` when useful for human legibility, explicitly non-authoritative and subordinate to existing Pantheon provenance/Claim/Evidence owners.

```text
audit finding != defect confirmed
duplicate candidate != merge authorization
local equilibrium != professional review completion
workspace annotation != Evidence provenance owner
```

## Deliberate non-change

This slice introduces no:

- `_staging` directory contract;
- `.manifest.json` contract;
- trust ledger;
- required frontmatter lifecycle;
- second Knowledge lifecycle;
- second provenance schema;
- graph-query/retrieval engine;
- Hindsight replacement;
- automatic contradiction reconciliation;
- automatic whole-vault rewrite;
- runtime activation or dependency on `Ar9av/obsidian-wiki`.

Word-Smith remains a separate optional authoring UX classification and is not widened by this change.

## Follow-up qualification reconstruction — #854

The graph/health qualification was revalidated after `main` advanced to `dfa7264cfc759f64e5c71016d3dc791f54577f03`.

The earlier #854 draft duplicated a larger structural/health doctrine block into `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`. That duplication is no longer justified because #851 already absorbed the report-only maintenance boundary, valid-link edge-case warning, local-equilibrium posture and the rule that upstream graph query must not replace bounded Hindsight retrieval.

The reconstruction therefore keeps the existing owner unchanged and narrows #854 to a qualification corpus plus regression. This is a convergence change, not a capability removal.

The external snapshot remains:

- stable qualification baseline: `Ar9av/obsidian-wiki` `v2026.08.6`, release commit `8b5859d0f895e51e785d3ba22ed8008297e8d367`;
- current upstream observation: `main` `37596cffeef43faecd9b61246b0b119b11a87bc4`;
- notable post-release graph-query fix: `427a9016b6aea04625133bd1a4ee00238c8c8518`, reducing false positives for non-English gap questions;
- open write-path issue #199 remains a reason to exclude memory-server/write behavior;
- open link-resolution issues #176 and #177 demonstrate false positives and destructive-risk around valid Obsidian attachment, `.base`, `.canvas`, explicit `.md`, heading, alias and escaped-pipe forms.

The bounded corpus now carries ten human-labelled cases. In addition to the existing false-hub, `_raw`, shortest-path, isolate, true broken-link, duplicate, contradiction, scope and protected-material cases, it includes a negative control proving that valid Obsidian-native link forms must not become broken-link findings:

```text
![[plan.pdf]]
![[perspective.png]]
[[planning.base]]
[[schema.canvas]]
[[cctp.md]]
[[cctp#Menuiseries]]
[[cctp|CCTP courant]]
| [[chauffage\|Chauffage]] |
```

The corpus remains prepared, not executed.

```text
fixture prepared != provider qualified
expected finding != observed result
passing static regression != behavioral acceptance
valid link != safe automatic rewrite target
```

No provider binding, runtime activation, automatic maintenance path or professional authority changes through this qualification.

## Executed qualification after #854

#854 merged on Pantheon `main` as `c351b12f2b6167865d62b5a008c7e670f79bd0da`. The prepared corpus was then executed against the deterministic graph/link-health surfaces pinned by the qualification.

Upstream pins inspected immediately before execution:

- stable baseline: `Ar9av/obsidian-wiki` `v2026.08.6`, commit `8b5859d0f895e51e785d3ba22ed8008297e8d367`;
- current upstream `main`: `37596cffeef43faecd9b61246b0b119b11a87bc4`;
- `graph_analysis.py` blob on both stable and current main: `9e2ff9be961f4149aa09d490e10089fb1d700c69`;
- `lint.py` blob on both stable and current main: `09a2b8207e02296455fd4d9a9401e6aa1fbdd66d`.

The current-main multilingual graph-query fix therefore does not alter the deterministic graph parser or lint resolver exercised here.

The execution sandbox had no outbound DNS access, so the upstream wheel was not installed from the network. Instead, the exact relevant deterministic function logic from the pinned source blobs was exercised in a disposable local harness. No memory server, capture hook, trust ledger, lifecycle, manifest or write path was started. This is qualification evidence for the named source surfaces only, not for the whole provider package.

Observed result:

```text
PASS
- root bookkeeping index exclusion
- _raw staging exclusion
- programme -> chauffage -> cctp shortest path
- isolated question detection
- true missing details-menuiseries link detection
- no mutation of the disposable workspace

FAIL
- valid Obsidian link precision: 6 false positives
- bounded scope: out-of-scope sentinel entered the full-vault graph

NOT DEMONSTRATED
- near-duplicate semantic detection
- semantic contradiction detection
```

The six valid-link false positives were:

```text
plan.pdf
perspective.png
planning.base
schema.canvas
cctp.md
chauffage\
```

The scope failure is structural rather than semantic: the upstream graph parser walks all non-skipped Markdown below the supplied vault root and exposes no task/project prefix parameter. A caller or adapter can pass a narrower materialized root, but that is external scope enforcement and must not be misreported as provider-native scope safety.

The duplicate and contradiction cases are marked `not_demonstrated`, not failed, because the deterministic `graph_analysis.py` / `lint.py` surfaces exercised here do not contain the corresponding semantic detectors. Missing implementation is not converted into an invented behavioral result.

Qualification decision:

```text
partial capability observations accepted
!= provider accepted

obsidian-wiki provider-wide qualification = not accepted
binding change = none
automatic writes = not approved
```

Reusable observations remain valid for the tested blobs: bookkeeping and `_raw` exclusion, basic structural graph parsing, shortest paths, isolates and true broken-link signals. Whole-vault link health, native task/project scoping, semantic duplicate/contradiction quality and automatic repair remain unqualified or blocked.

The raw observed result is retained separately in `tests/fixtures/obsidian_graph_health_observed_v2026.08.6.json`; the original prepared fixture remains unchanged as `prepared_not_executed`, preserving expectation versus observation.

```text
observed result != provider-wide truth
partial capability pass != provider adoption
read-only success != authorization
graph relation != Evidence
health finding != defect confirmed
provider output != governed Knowledge
```

## Lotus renderer source qualification follow-up

After the obsidian-wiki graph/health qualification, the separate visualization question was checked against exact current repository state rather than folded into the graph provider.

Pantheon basis at the start of this follow-up:

- `Pantheon-Next/main`: `fc5aae73f3933709e79deabcbe30bf34fcbca00f`;
- the existing external-tool placement register remains the support owner for any future placement decision and is deliberately unchanged by this source-only qualification.

Lotus upstream state observed:

- repository: `TzadikimBIU/lotus`;
- latest stable release: `1.2.3`;
- current `main`: `b3b4dec3095d6cfe32d1443ad8a4a87ea50dd3e4`;
- open pull requests observed: zero;
- open issues observed: zero;
- exact-head upstream smoke run `32519680456`: success.

Relevant source findings at that pin:

- `src/engine/managedOutput.ts` defines the `lotus-display` Markdown language and parses its source with `JSON.parse` into validated MIME display records;
- `src/plugin/main.ts` registers `lotus-display` as a Markdown code-block processor and passes parsed display records directly to `renderDisplayOutput`; this path is distinct from `runBlock` and the local-execution consent gate;
- current defaults keep local execution, note write-back, auto-run, API and logging disabled;
- `application/vnd.lotus.d3+json` is rendered from a declarative chart spec limited by the reviewed adapter to `bar`, `line` or `scatter` plus JSON data/key values;
- the reviewed D3 display path constructs SVG through bundled D3 and does not evaluate JavaScript carried in the display payload;
- the Cytoscape adapter accepts a materially wider partial `CytoscapeOptions` object and is therefore deferred until an allowlisted projection is demonstrated;
- Graphviz is excluded from this slice because it can invoke the `dot` process; HTML, Plotly, JSXGraph and all code-runner surfaces are also excluded.

The smallest candidate profile is therefore:

```text
authorized Markdown note
-> existing lotus-display JSON fence
-> application/vnd.lotus.d3+json only
-> Lotus first-party D3 renderer
-> SVG projection
```

The source review supports preparing this profile for an Obsidian runtime smoke. It does not establish installed-runtime behavior or authorize the wider Lotus plugin runtime.

```text
generated data != executable code
display record != Evidence
rendered node or edge != governed relation
view model != canonical model
visualization success != professional validation
renderer available != renderer authorized
projection != persistence
```

Creating or replacing a `lotus-display` fence remains a workspace persistence action and therefore requires explicit authorized workspace-persistence intent under existing owners. Rendering an already-present fence is the read-only path being qualified.

Qualification status:

```text
Lotus source review = passed for preparing renderer-only D3 smoke
Lotus runtime smoke = pending
Lotus provider placement = not yet recorded
Lotus execution runtime adoption = no
Pantheon capability binding = none
workspace automatic write = not approved
```

A real isolated Obsidian test-vault smoke against release `1.2.3` is required before the external-tool placement register may record Lotus as a renderer candidate. That smoke must keep the renderer-only settings disabled, retain before/after note hashes, verify no output file or note mutation, and show that the D3 display renders without enabling local execution.

The prepared source-review contract is retained in `tests/fixtures/lotus_renderer_pilot.json` and protected by `tests/test_lotus_renderer_qualification.py`.

## Changed paths

The #854 reconstruction changed:

- `tests/fixtures/obsidian_graph_health_pilot.json`;
- `tests/test_workspace_organization_routing.py`;
- this existing intervention log.

The executed-qualification follow-up adds:

- `tests/fixtures/obsidian_graph_health_observed_v2026.08.6.json`;
- `tests/test_obsidian_graph_health_observed.py`;
- this existing intervention log.

The Lotus source-qualification follow-up adds:

- `tests/fixtures/lotus_renderer_pilot.json`;
- `tests/test_lotus_renderer_qualification.py`;
- this existing intervention log.

No new doctrine owner, generated index entry, runtime component or provider binding is introduced.

## Verification target

Keep observed runtime results separate from prepared expectations. For Lotus, run static regression and normal governance CI now; execute the isolated Obsidian runtime smoke separately before any placement-register change.

## Status

The obsidian-wiki qualification is executed for the named deterministic surfaces and remains partial/not accepted provider-wide. The Lotus renderer-only D3 profile is source-reviewed and prepared for runtime smoke, not runtime-qualified or adopted. Doctrine ownership, runtime status, professional authority and external bindings are unchanged.
