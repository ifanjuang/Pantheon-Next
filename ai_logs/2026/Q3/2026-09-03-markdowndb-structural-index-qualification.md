# MarkdownDB structural-index qualification — completed convergence

Date: 2026-09-03
Status: historical qualification result — provider not accepted for direct integration.
Boundary profile: qualification provenance only.

## Objective

Close the MarkdownDB Q1 qualification by preserving the executed result and the provider-neutral structural-index pattern while removing a rejected provider from Pantheon's **current** external qualification inputs.

## Exact executed candidate

```text
repository = flowershow/markdowndb
package    = mddb
version    = 0.9.5
ref        = f53cfef49ffcd267fc200d2dc451ed6f37b4523a
```

Real execution provenance is retained in:

```text
tests/fixtures/markdowndb_structural_index_observed_v0.9.5.json
```

The record includes the exact workflow run, artifact identity/digest, corpus observations, identity/digest probes, reconstruction result, write check and final classification.

## Observed result

Useful observations:

- caller-bounded filesystem scan works;
- direct parsing recognizes the tested Markdown/Obsidian structural forms substantially better than the previously qualified `obsidian-wiki` CLI;
- raw frontmatter, tags and Markdown task syntax are observable;
- cache deletion followed by rebuild reproduces the same structural projection;
- the cache can remain outside the synchronized vault;
- the bounded synthetic workspace was not mutated.

Blocking observations for direct Pantheon index use:

- unresolved targets observed by the parser disappear from the SQL `links` projection;
- tested existing PDF/PNG, `.base`, `.canvas` and heading-anchor links are also absent from that SQL projection;
- provider `_id` is path-derived: rename changes it while identical bytes keep the same content digest;
- byte changes at the same path preserve provider `_id` while changing SHA-256;
- whole-vault indexing reaches staging, protected Source/Evidence material and the explicit out-of-scope sentinel unless the caller bounds the root;
- provider frontmatter/tag/task semantics remain raw provider observations only.

## Decision

```text
classification = C
MarkdownDB direct workspace-index implementation = not accepted
runtime dependency = not adopted
provider binding = none
compatibility adapter = not justified
new Capability Slot = none
new workspace/index authority = none
```

Retain only the provider-neutral pattern already owned by the Workspace Manifest Inspector candidate:

```text
authorized workspace scope
-> deterministic structural observation
-> reconstructible local index
-> bounded query / health / Card enrichment
```

## Why the active qualification machinery is removed

`implementation/qualification/external-pins.json` explicitly owns **current external-component qualification inputs** and explicitly says it is not a historical qualification-run record.

After Q1, no current Pantheon decision depends on continuously re-running MarkdownDB:

```text
provider tested
-> direct implementation rejected
-> useful pattern absorbed by existing owner
-> exact observed result retained
```

Therefore keeping a current pin, freshness observation and pull-request qualification workflow would turn a completed rejected candidate into a quasi-component by inertia.

The convergence is:

```text
remove current MarkdownDB pin
remove current upstream-freshness observation
remove active MarkdownDB Q1 workflow
retain exact observed fixture
retain compact regression of the decision and owner boundaries
```

No historical-pin lifecycle or second registry is introduced.

## Preserved boundaries

```text
index row != source record
provider file id != governed identity
path hash != source digest
frontmatter type != governed Document kind
raw tag != Tag Registry tag
wikilink != governed relation
Markdown task != WorkIssue
index current != professionally current
cache persistence != professional persistence
caller-supplied scope != provider-owned authorization
rebuild success != authorization
qualification success != dependency adopted
```

## Reopen condition

Requalify MarkdownDB only if a concrete Cockpit/Inspector workflow later demonstrates that the smallest deterministic implementation should be reconsidered and upstream has materially changed the blocking structural-index behavior.

Do not build a Pantheon adapter solely to compensate for the rejected provider gaps.
