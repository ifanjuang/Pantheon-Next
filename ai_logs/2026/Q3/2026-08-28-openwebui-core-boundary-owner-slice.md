# OpenWebUI core-boundary owner convergence — 2026-08-28

## Objective

Reduce the machine-tracked debt in issue #785 through one owner-coherent slice. Remove present-tense OpenWebUI ownership from the authority interpreter, the standard non-implementation boundary and the controlled terminology owner without replacing it mechanically with Hermes WebUI.

## Revalidated base

Pantheon-Next `main`: `0f0e45c2c800333aa0bc5aeaacac84ae27c09ade`, merge of #784.

Open pull requests at slice start were #721 and #722, both dependency-only GitHub Actions updates. No parallel pull request touched issue #785 or the selected owners.

The current regression contained exactly 33 paths in `KNOWN_CURRENT_AUTHORITY_OPENWEBUI_RESIDUES`. This slice reviews and removes three paths from that temporary allowlist:

- `docs/governance/AUTHORITY_INDEX.md`;
- `docs/governance/BOUNDARY_STANDARD.md`;
- `docs/governance/TERMINOLOGY_BOUNDARIES.md`.

## Role / Rite / Space / change level

- Role: MNEMOSYNE for convergence and placement continuity, with THEMIS boundary review.
- Rite: Concordance des sources between current `main`, #785, the regression and the stable `HERMES_INTEGRATION.md` boundary.
- Space: Pantheon Next governance repository.
- Change level: doctrine-preserving active-support convergence plus a bounded regression-allowlist reduction. No runtime, schema, API, persistence, installation, provider or approval behavior changes.

Roles and Rites describe the review method; they are not autonomous runtime agents or executable workflow state.

## Owner classification

`AUTHORITY_INDEX.md` remains the sole authority interpreter and sub-index registration point.

`BOUNDARY_STANDARD.md` remains the single reusable non-implementation boundary.

`TERMINOLOGY_BOUNDARIES.md` remains the controlled vocabulary and progressive-cleanup owner. Its OpenWebUI term mapping is retained only as explicitly historical/refused integration vocabulary, so provenance remains readable without assigning current ownership.

## Convergence

The three current-owner headers now express the selected generic split:

```text
optional compatible runtime client = runtime interaction
Hermes Agent = external execution runtime
runtime adapter / Hermes = PEP for consequential effects
Pantheon Cockpit = governed projection
Pantheon policy service = bounded deterministic PDP interface
Pantheon Next = governance, authority and PDP semantics
human = consequential decision when required
```

The terminology owner also defines generic optional-runtime-client terms before retaining the historical/refused OpenWebUI vocabulary. Availability, selection and runtime approval controls remain non-authoritative.

## Preserved invariants

```text
client selected != governance authority
PDP decision != PEP execution
runtime approval UI != Pantheon human approval
runtime output != Evidence
projection != persistence
projection != approval
memory != Evidence
runtime memory != Registre Probatoire
```

Hermes WebUI is not introduced as a replacement owner or required dependency.

## History and truncation

Historical and refused OpenWebUI vocabulary remains where it explains provenance. No long document was truncated or substantially reduced, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification

Local verification before commit:

- focused OpenWebUI retirement regression: 7 passed;
- documented root validation suite: 491 passed;
- bounded MCP server suite: 226 passed;
- governance status, links, assets, index coverage, vocabulary, truncation, predecessor, schema, Register, vertical-slice, APU and packaging checks: passed;
- obsolete-authority consistency: passed;
- architecture inventory, module-usage, Hermes distribution-lock and convergence-closure audit: passed.

These results must be rerun or rechecked on the exact committed PR head. Any subsequent modification invalidates the previous result.
