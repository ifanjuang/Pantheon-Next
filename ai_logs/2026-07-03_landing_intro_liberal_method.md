# AI log — landing intro liberal-method repositioning

Date: 2026-07-03

## Scope

Updated the public HTML landing page to put the liberal-profession argument at the very beginning.

## Files changed

- `docs/index.html`

## Change summary

- Replaced the former opening example with a doctrinal introduction centered on professional method, traceability and responsibility.
- Removed the initial “mail mairie à 17h / 20 minutes” framing, which was considered devaluing.
- Added a new `Pourquoi ce dépôt existe` section before the user journey.
- Reframed AI output as candidate material requiring status, evidence, limits and human arbitration.
- Kept the boundary aligned with the active doctrine: OpenWebUI exposes, Hermes Agent executes, Pantheon governs, the professional decides.

## Repo state

- Static landing content: implemented.
- Runtime / automation implication: non applicable.
- Doctrine effect: editorial support only, aligned with active support doctrine.

## Verification

- Fetched `docs/index.html` after update and confirmed the new title, meta description, hero and `Pourquoi ce dépôt existe` section are present.
- Searched the repository for the removed “mail mairie 17h / 20 minutes” wording; no remaining match found.

## Commit

- `c32a2710755fa90add9bcccca1c06c5e8681d289`

## Follow-up — signability example

Added a `Peut-on signer ?` section immediately after `Pourquoi ce dépôt existe`.

Purpose:

- Make the public example less about speed and more about professional assumption.
- Show that a clean AI-generated dossier is not necessarily verified, sourced, methodologically intelligible or signable.
- State the key professional question: `pouvons-nous signer ce travail ?`

Navigation updated:

- Added `#signer` to the left documentation navigation.
- Added `#signer` to the right page table of contents.

Repo state:

- Static landing content: implemented.
- Runtime / automation implication: non applicable.
- Doctrine effect: editorial support only, aligned with candidate/status/proof boundary.

Verification:

- Fetched `docs/index.html` after update and confirmed the new `id="signer"` section and navigation link are present.

Commit:

- `ab112db95b5633f0c564451fce1d1e7626761099`
