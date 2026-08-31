# A2UI Cockpit qualification

Date: 2026-08-31

Status: validation-only trace — implementation qualification candidate, not adopted.
Boundary profile: validation_only_trace.

## Change

- Added an isolated `implementation/labs/a2ui-cockpit/` qualification surface using A2UI protocol `v0.9.1` and the Lit renderer path.
- Added a deterministic synthetic multi-source research-summary fixture and a closed six-component presentation catalog.
- Added a fail-closed pre-processor guard for protocol/catalog/surface identity, component/action allowlists, `functionCall`, `sendDataModel`, secret-like state and size bounds.
- Added structural regression coverage under `implementation/tests/test_a2ui_cockpit_qualification.py`.
- Corrected the lab HTML to use local relative asset references after Governance CI rejected root-relative `/style.css` and `/main.js` references.
- Added a path-scoped GitHub Actions qualification workflow that resolves the exact top-level package pins, runs the guard tests, builds the isolated Vite/Lit surface and executes a headless Chrome render/click smoke.
- Added a dependency-free browser harness using loopback Vite preview and Chrome DevTools to verify the official processor/renderer displays the fixture and keeps the admitted click intent-only.

## Why

Pantheon Cockpit already owns governed Card/navigation/status projections and bounded action seams. The qualification tests whether A2UI can remain a replaceable declarative presentation protocol downstream of those owners, rather than creating a second Card model, UI authority, persistence path or business-action channel.

`research.multi_source_summary` is now a merged Workflow Manifest on current `main`. The lab mirrors that workflow identifier and a synthetic research-result shape only as presentation data; it does not import the manifest, redefine its outputs or modify its Source/Evidence owners.

## Repository state

The qualification branch was reconstructed on current `main` after #878 merged:

```text
e933ac81dd20125bc841f0990dd4a4780ec1abcf
```

#878 changed the template registry, the source-research Workflow Manifest and its root contract tests. Those paths are disjoint from the A2UI lab, so the qualification remains downstream and does not create a second research owner.

No overlapping A2UI implementation path was observed on current `main`. The branch `codex/a2ui-cockpit-qualification` is the bounded qualification branch used by PR #882.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: yes — `.github/workflows/`, `implementation/`, `implementation/tests/`, `ai_logs/`.
Runtime impact: none on Pantheon product/runtime; only an isolated lab and CI qualification path are added.
Authority impact: none.
Schema/test/CI impact: no schema change; one structural test and one path-scoped lab CI workflow added.
External action: package resolution/build in GitHub Actions plus loopback browser qualification only; no Pantheon business endpoint or external professional effect.
Memory behavior: none.

The only admitted A2UI event is `pantheon.prepare_hermes_handoff`. In the lab it becomes a local `cockpit_intent_candidate` with:

```text
executed  = false
persisted = false
authorized = false
```

`main.js` contains no business HTTP request, runtime WebSocket connection or browser persistence path. The browser qualification harness uses loopback HTTP to Vite preview and a loopback Chrome DevTools WebSocket solely to observe the rendered surface and click behavior.

## Qualification observations

The first PR head exposed one repository-integration defect: Governance CI correctly rejected root-relative lab asset URLs. The asset references were changed to `./style.css` and `./main.js`; subsequent Governance CI passed.

The dedicated A2UI workflow observed:

```text
Node                    22.23.2
npm                     10.9.8
resolved packages       31
guard tests             4 / 4 passed
Vite                    8.2.2
modules transformed     462
main JS bundle          236.68 kB raw / 58.05 kB gzip
```

The first headless-browser run reached and passed the substantive assertions — surface rendered, action button clicked, and intent remained non-executed/non-persisted/non-authorized — but the job ended false-negative on `ENOTEMPTY` while deleting Chrome's temporary profile. The harness was corrected to await Chrome/Vite termination and make temporary-profile removal retryable/best-effort without changing any A2UI assertion.

The corrected browser run then completed successfully and retained this observed result:

```text
rendered       = true
action_clicked = true
action         = pantheon.prepare_hermes_handoff
executed       = false
persisted      = false
authorized     = false
```

On that corrected qualification head, A2UI Cockpit Qualification, Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency completed successfully. Pantheon implementation CI was still running when this trace was updated; exact-head completion after final one-commit reconstruction remains required before merge/readiness.

These are qualification observations, not dependency-adoption evidence. Green CI or successful rendering does not adopt A2UI, activate it in Cockpit or authorize an adapter.

## Local distinctions

```text
A2UI message != governed object
A2UI data model != persistence
rendered status != authorization
A2UI event != approved action
research summary != Evidence
retrieved != truth
runtime success != Evidence
package resolved != dependency adopted
lab present != Cockpit integration
CI green != adoption
```

## Open after this slice

- Reconstruct the final branch as one commit above exact current `main` and observe all exact-head repository checks.
- Review PR comments/threads against that exact head.
- Only after qualification is green should a separate slice consider a tiny adapter inside the existing Cockpit boot chain and action boundary.
- A reviewed lockfile remains a later integration requirement; the qualification workflow intentionally does not imply production dependency adoption.
