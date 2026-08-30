# 2026-08-30 — converge bounded obsidian-wiki maintenance patterns

## Objective

Evaluate `Ar9av/obsidian-wiki` against the current Pantheon workspace model, retain only useful bounded behavior, and avoid creating parallel Knowledge, retrieval, manifest, provenance, lifecycle or approval authorities.

## Existing Pantheon owners reused

Before this qualification, Pantheon already owned the relevant boundaries:

- #848: `search-before-create` and explicit conversation consolidation in `docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`;
- `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`: reusable Markdown organization and review posture;
- `docs/governance/DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md` plus `implementation/mvp_vertical/knowledge.py`: governed Knowledge candidate writes/versioning;
- `docs/architecture/WORKSPACE_MANIFEST_INSPECTOR_CANDIDATE.md`: manifestability/local package-health semantics;
- Hindsight: qualified/recommended optional derived retrieval provider, while the generic runtime-memory binding remains unbound;
- Word-Smith: separate optional authoring/document-assembly UX only.

The upstream subsystem is therefore not imported wholesale.

## Patterns retained

Only bounded, provider-neutral patterns are retained:

1. report-only workspace maintenance observations such as unresolved links, orphan candidates, duplicate/consolidation candidates, contradiction candidates and missing cross-links;
2. optional human-legibility annotations such as `extracted`, `inferred` and `ambiguous`, subordinate to Pantheon Claim/provenance/Evidence owners.

```text
audit finding != defect confirmed
duplicate candidate != merge authorization
local equilibrium != professional review completion
workspace annotation != Evidence provenance owner
```

No `_staging` contract, upstream `.manifest.json`, trust ledger, lifecycle, second provenance schema, Hindsight replacement, automatic contradiction reconciliation or automatic whole-vault rewrite is adopted.

## Prepared qualification — #854

PR #854 converged the graph/health work into the existing owner and prepared `tests/fixtures/obsidian_graph_health_pilot.json` without changing runtime or bindings.

Stable candidate snapshot:

- repository: `Ar9av/obsidian-wiki`;
- release: `v2026.08.6`;
- release commit: `8b5859d0f895e51e785d3ba22ed8008297e8d367`;
- current upstream `main` observed: `37596cffeef43faecd9b61246b0b119b11a87bc4`;
- `graph_analysis.py` blob on stable/current: `9e2ff9be961f4149aa09d490e10089fb1d700c69`;
- `lint.py` blob on stable/current: `09a2b8207e02296455fd4d9a9401e6aa1fbdd66d`.

The corpus contains ten human-labelled cases, including bookkeeping exclusion, `_raw` exclusion, shortest path, isolate, true broken link, valid native Obsidian link negative controls, semantic duplicate/contradiction candidates, an observable out-of-scope sentinel, and protected source/Evidence material.

```text
fixture prepared != provider qualified
expected finding != observed result
passing static regression != behavioral acceptance
valid link != safe automatic rewrite target
```

## First observed record — #856

PR #856 created the first separate observed-result owner:

- `tests/fixtures/obsidian_graph_health_observed_v2026.08.6.json`;
- `tests/test_obsidian_graph_health_observed.py`.

Its local sandbox could not install/run the upstream package and instead reproduced selected deterministic source logic in a local harness. That was useful as an initial observation, but it materialized the graph differently from the canonical corpus and reported `programme -> chauffage -> cctp` as a passing path.

That local-harness path result is superseded by the real-upstream execution below. The #856 owner paths are retained; no second observation registry is created.

## Real upstream execution — #857 Q1

PR #857 adds a reproducible qualification harness rather than a provider integration.

`implementation/qualification/external-pins.json` gains the qualification-only candidate pin:

```text
obsidian-wiki
repository = Ar9av/obsidian-wiki
version    = 2026.8.6
ref        = 8b5859d0f895e51e785d3ba22ed8008297e8d367
```

`.github/workflows/obsidian-wiki-graph-health-q1.yml` follows the established external-qualification pattern:

1. export the canonical pin;
2. checkout the exact upstream commit;
3. materialize the canonical pilot fixture into a disposable vault without normalizing away explicit `.md` targets;
4. execute the real upstream `python -m obsidian_wiki graph-analyse` and `lint` commands;
5. run graph/lint against `projects/maison/` and a whole-vault negative control;
6. hash tracked workspace/source/Evidence material before and after execution;
7. retain raw outputs as a 30-day GitHub Actions artifact.

Excluded surfaces remain setup, capture, cache/manifest writes, trust recording, sync, memory server and automatic repair.

Run record:

- workflow run: `33331529533`;
- execution head: `5fb920e57610cf7c46f41be3c8d75b85813c702b`;
- artifact: `9737779875` / `obsidian-wiki-graph-health-q1-33331529533`;
- artifact digest: `sha256:1dabfa025b443970a97743bba53a954206afeddfb50ea641ef1def04c8253f97`;
- harness result: success.

## Corrected observed result

The exact upstream CLI produced a materially different structural result from the #856 local harness.

Observed positives:

- root `index.md` is excluded from graph ranking;
- `_raw/` is excluded;
- passing `projects/maison/` as the vault root excludes the out-of-scope sentinel;
- all 16 tracked synthetic workspace/source/Evidence files were byte-identical after execution;
- no Pantheon state, Evidence status, runtime activation or Capability Binding changed.

Observed blockers:

1. **explicit `.md` links break the graph**: the canonical corpus contains targets such as `[[projects/maison/decisions.md]]`, while upstream graph pages are keyed by stems. The real `programme -> cctp` query therefore returned `path: null`;
2. **false isolates**: because those edges disappear, `programme`, `decisions`, `chauffage` and `chauffage-notes` were reported isolated alongside the true `question-ouverte` isolate;
3. **broken-link precision fails**: `lint` produced 15 broken-link findings. The true `details-menuiseries.md` miss was present, but valid explicit `.md`, PDF/PNG embed, `.base`, `.canvas` and escaped-pipe alias forms were also reported broken;
4. **provider schema noise**: neutral Pantheon pages also received missing `base_confidence`/`lifecycle` findings and a missing trust-ledger finding, although that provider lifecycle is outside this qualification target;
5. **semantic duplicate/contradiction capabilities remain unexecuted** by deterministic Q1.

The whole-vault negative control contains `sentinel-hors-perimetre`; the scoped run does not. This means subtree scoping is usable when the caller supplies the correct root, but Pantheon authorization remains caller/wrapper-owned and is not inferred by the provider.

Current upstream `main` was rechecked after the run. Its `graph_analysis.py` and `lint.py` blobs are identical to the tested stable release, so these deterministic link-resolution observations remain current for those surfaces.

The single canonical observed record remains:

`tests/fixtures/obsidian_graph_health_observed_v2026.08.6.json`

The prepared expectation corpus remains unchanged.

## Qualification decision

```text
obsidian-wiki v2026.08.6 direct graph/health qualification = not accepted
provider binding change = none
runtime activation = none
automatic writes = not approved
```

Accepted observations are limited to bookkeeping exclusion, `_raw` exclusion, read-only behavior of the tested surfaces and caller-enforced subtree scoping.

Not accepted are explicit-`.md` graph correctness, shortest-path qualification on the canonical corpus, isolate precision, whole-vault link-health reliability, provider-native task/project authorization, semantic duplicate/contradiction quality, automatic repair and provider-wide adoption.

```text
observed result != provider-wide truth
partial capability pass != provider adoption
read-only success != authorization
graph relation != Evidence
health finding != defect confirmed
provider output != governed Knowledge
caller-supplied scope != provider-owned authorization
```

## Lotus renderer source qualification — #861

The separate visualization question remains intentionally independent from the `obsidian-wiki` provider decision.

Reviewed Lotus upstream state:

- repository: `TzadikimBIU/lotus`;
- stable release: `1.2.3`;
- reviewed upstream `main`: `b3b4dec3095d6cfe32d1443ad8a4a87ea50dd3e4`;
- the source-qualified path is an existing `lotus-display` JSON fence using `application/vnd.lotus.d3+json` and the first-party D3 renderer;
- current defaults keep local execution, note write-back, auto-run, API and logging disabled;
- Cytoscape remains deferred behind an explicit allowlisted payload profile; Graphviz, HTML, Plotly, JSXGraph and code-runner surfaces remain excluded from this first qualification.

The smallest candidate profile remains:

```text
authorized Markdown note
-> existing lotus-display JSON fence
-> application/vnd.lotus.d3+json only
-> Lotus first-party D3 renderer
-> SVG projection
```

```text
generated data != executable code
display record != Evidence
rendered node or edge != governed relation
view model != canonical model
visualization success != professional validation
renderer available != renderer authorized
projection != persistence
```

PR #861 merged the source-review fixture and regression only. It did not add Lotus to the external-tool placement register, install the plugin, activate a runtime or create a Capability Binding.

Current Lotus qualification status:

```text
Lotus source review = passed for preparing renderer-only D3 smoke
Lotus runtime smoke = pending
Lotus provider placement = not recorded
Lotus execution runtime adoption = no
Pantheon capability binding = none
workspace automatic write = not approved
```

A real isolated Obsidian test-vault smoke against release `1.2.3` remains required before any placement-register entry. The smoke must retain before/after note hashes, keep execution/write/API/logging disabled, verify no output-file or Markdown mutation and demonstrate that the D3 display renders without enabling a code runner.

The prepared source-review contract remains `tests/fixtures/lotus_renderer_pilot.json`, protected by `tests/test_lotus_renderer_qualification.py`.

## Next action

Keep `obsidian-wiki` unbound. Retain the report-only patterns already distilled into Pantheon. Re-run the same real-upstream corpus after upstream link-resolution changes. Do not introduce a Pantheon-specific compatibility adapter solely to compensate for this release unless a demonstrated workflow later justifies the maintenance cost.

If semantic near-duplicate/contradiction behavior remains desirable, qualify it separately through an agent-capable test rather than inferring it from the deterministic CLI.

For Lotus, execute the isolated Obsidian renderer-only smoke before any provider-placement decision.

## Status

#854 is merged and the corpus is prepared. #856 established the observed-result owner. #857 supersedes the local-harness observation with a real upstream execution and keeps one canonical observed record. #861 separately prepares the Lotus D3 renderer-only runtime smoke. Doctrine ownership, professional authority, runtime state and external bindings remain unchanged.
