# AI log — responsive mobile diagrams, animation, agentic/RAG glossary

Date: 2026-06-04

## Scope

`docs/index.html` only. Mobile-friendly responsive diagrams and a plain-language
glossary, following review.

## Changes

- The three detailed diagrams (`#flow2a`, `#flow2b`, `#flow3`) are now **responsive
  D3**: a `responsive(id, vbDesktop, vbMobile, deskFn, mobFn)` helper picks a layout
  by container width (<560px = mobile) and re-renders on resize. Desktop keeps the
  full rich layout; mobile gets a vertical, phone-friendly stack with adapted block
  proportions and text sizes. Removed the horizontal-scroll container (`.diagram
  scroll` → `.diagram`).
- Light, safe **animation**: CSS fade-in on `.diagram svg` (fill mode `both`, so the
  end state is visible even without animation support) and marching-ants on `.flow`
  arrows (reusing the existing `@keyframes dash`); both disabled under
  `prefers-reduced-motion`.
- New **"En clair" glossary** at the top of the "Architecture détaillée" section:
  système agentique, RAG (recherche augmentée), runtime, skills — honest one-liners.
- Schema 1 (`#dossierFlow`) already responsive; unchanged here.

## Doctrine fidelity

No doctrine change. The RAG/agentic/runtime/skills definitions stay within the
documented boundary: runtimes and orchestration (incl. LangChain/LangGraph) live on
the Hermes side; Pantheon governs and keeps memory local. Skills are described as
governed candidates, not implemented features.

## Repo state

Documented, non-implemented. Documentation surface only; no runtime added.

## Risk

Low. Single file. All four D3 scripts stay guarded (`typeof d3`, `svg.empty()`).
Rendered headless (jsdom + d3) at 900px and 380px: desktop 69/80/74/44 elements,
mobile 49/63/46/39 — all draw cleanly. No bare ampersands outside `<script>`.

## Follow-up

Check the live mobile rendering after GitHub Pages redeploys; tune font sizes if a
label feels tight on very small screens.
