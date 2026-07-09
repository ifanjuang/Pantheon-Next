# 2026-07-08 — Public cockpit wording rule

## Status

Validation-only trace.

This log records a documentation-assets wording rule. It does not create doctrine, runtime behavior, approval, memory promotion, provider routing, scheduling, installation, update execution or external action.

## Scope

Files changed:

```text
docs/assets/README.md
```

## What changed

`docs/assets/README.md` now includes a public landing and cockpit wording rule:

```text
Preferred public labels:
- Maquette cockpit
- Maquette Pantheon Control
- Prototype statique

Avoid unqualified labels:
- Cockpit
- Control plane
- Dashboard live
- Services en ligne
- Connexions actives
```

unless the same visible block clearly states that the state is declared, fictive, static or target behaviour.

It also records that `docs/index.html` is still a monolithic landing page and should not be broadly hand-edited for wording cleanup before shared labels/components are extracted or refactored.

## Why

After the static pages wording pass, Pantheon Control itself was clarified as a static mockup, and `rag-probatoire.html` was updated to label the link as `Maquette cockpit`.

The remaining public landing page still contains short labels that should eventually be aligned, but replacing the whole monolithic HTML file through a full-file connector update would be riskier than the value of the small label change.

This rule makes the next refactor explicit and prevents future assets from reintroducing ambiguous live-cockpit language.

## Boundary kept

This intervention did not add or authorize:

```text
runtime
agent loop
scheduler
queue
provider router
MCP host gateway
plugin manager
installer
updater
automatic approval
automatic memory promotion
external sender
service control
account connection
external routing
```

## Risks and limitations

- No CI or full link checker was run in this intervention.
- `docs/index.html` still needs a future component/label refactor before durable public wording alignment.
- This log records a rule and limitation; it does not itself update the monolithic landing page.

## Result

The assets registry now governs public cockpit labels before the next landing-page refactor.
