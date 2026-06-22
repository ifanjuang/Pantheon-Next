# 2026-06-21 Landing → RAG probatoire navigation link (issue #183)

Status: implemented (documentation/landing only; minimal change).

Issue #183 (landing refactor) is mostly addressed: the cockpit pages were already
factored into shared data/nav/ui/style layers, and `rag-probatoire.html` exists
and links back to the landing. The one missing piece in the "Done expected" was a
controlled navigation path **from** the public landing **to**
`docs/rag-probatoire.html`. The landing is dense, so this is a deliberately
minimal, surgical change — no structural refactor, no editorial edits, no change
to the "Documenté, non runtime" status line.

Changes (docs/index.html only):

- Sidebar "Références" nav: adds a `RAG probatoire` entry pointing to
  `rag-probatoire.html`, reusing the already-defined `#i-graph` symbol, mirroring
  the sibling reference links exactly.
- Footer `flinks`: adds a `RAG probatoire` link ("Retrouver une source n’est pas
  prouver."), same pattern as the other footer links.

Both new links target the existing `docs/rag-probatoire.html`. No top-nav change,
no new asset, no SVG symbol added.

Verified: two `href="rag-probatoire.html"` links present, target exists,
`#i-graph` symbol defined; `check_internal_links` scans only `*.md` (HTML is out
of its scope); status_headers / internal_links / index_coverage green vs
baseline. CI does not lint docs HTML.

Boundary: landing documentation only. No runtime, approval engine, memory engine
or action surface introduced; the page stays "documenté, non runtime".
