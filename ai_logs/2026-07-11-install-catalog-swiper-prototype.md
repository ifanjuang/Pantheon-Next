# Install catalog Swiper prototype trace

Date: 2026-07-11

Status: validation-only trace.

## Change

Added `docs/assets/pantheon-control/install-catalog.html` as a standalone static prototype inside the existing Pantheon Control prototype assets.

The page demonstrates:

- horizontal Swiper navigation across resource families;
- vertical Swiper navigation across resources inside a family;
- simple Resource Card fronts;
- detailed lifecycle/status views on click;
- mandatory Pantheon preconfiguration options;
- simulated preparation of an Installation Candidate;
- candidate entries for the modules and bindings currently named in repository doctrine plus explicitly marked review/watchlist items.

## Boundary

This prototype is static and non-executable.

It does not create or promote a real `dashboard/` module. It does not create a live install catalog, schemas, presets, a registry, a provisioner, Docker or Portainer access, a shell runner, an SSH runner, a package manager, a connector gateway, a scheduler, a queue, a secret store, an approval engine, a memory engine or an external action.

The `Prepare candidate` interaction changes local browser text only. It does not persist state or execute commands.

## Responsibility split

```text
Pantheon Control exposes cards, status distinctions, preconfiguration and candidate preparation.
Pantheon governs classification, gates, adoption, activation and rollback visibility.
An external provisioner would execute only after a later reviewed implementation and human approval.
Hermes may execute authorized post-bootstrap operations only after it exists and is admitted.
The human decides installation, adoption, activation, update and rollback.
```

## Preserved distinctions

```text
static_prototype != dashboard_implementation
card_visible != module_listed_in_live_registry
candidate_prepared != installation_authorized
installation_authorized != installation_executed
installed != activated
healthy != safe
watchlist_item != install_instruction
preset_named != preset_implemented
```

## Validation

Manual source review only. No runtime, browser automation, build, test or deployment claim is made.
