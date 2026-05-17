# AI Log — Practitioner hooks and regulatory watch example

Date: 2026-05-17

## Scope

Integrated practitioner-facing example work to make Pantheon Next more concrete for non-technical professionals.

## Files changed

- `docs/examples/architecture_devis_reprise/README.md`
- `docs/examples/PRACTITIONER_HOOKS.md`
- `docs/examples/regulatory_watch_conflict/README.md`
- `docs/examples/README.md`
- `ai_logs/2026-05-17-practitioner-hooks-regulatory-watch.md`

## Summary

Strengthened the architecture / MOE demo case so it shows the core practitioner hook:

```text
Pantheon stops the AI from turning a well-written draft into a risky professional act.
```

Added:

- raw unsafe AI answer;
- Pantheon interpretation;
- Governance College status;
- User Decision Gate;
- decision effects;
- explicit mistake-prevention framing.

Created `PRACTITIONER_HOOKS.md` to list high-impact scenarios by profession.

Added regulatory watch versus active dossier assumptions as a high-priority hook.

Created `regulatory_watch_conflict/README.md` to illustrate how a new regulation, doctrine, case law, technical standard or professional recommendation may create a review alert without automatically mutating active dossiers.

Updated `docs/examples/README.md` to index the new example and recommend a first reading path.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

No runtime was added.

No scheduler or watch automation was added.

No regulatory monitoring implementation was added.

No external source was treated as automatically applicable.

No automatic dossier mutation was added.

No automatic memory promotion was added.

## Boundary note

The new examples are fictional educational support only.

They are not legal, medical, technical, accounting, tax, regulatory or professional advice.

They do not claim that Pantheon prevents professional fault.

They show how a governance method can expose source gaps, contradictions, external effects, applicability uncertainty and human decision needs.

## Status

Documentation examples only.
