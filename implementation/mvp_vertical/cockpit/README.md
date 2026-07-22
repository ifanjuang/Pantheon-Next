# Cards-first Cockpit Candidate

Status: implemented external UI, bounded write and proposal-only resource/navigation candidates — not adopted, not activated, not production-authorized.

This directory contains the cards-first cockpit served at `/cockpit/`. It composes existing bounded Document, Knowledge and Work Issue projections. It does not add a card database, crawler, skill installer, scheduler, workflow engine, runtime, provider router, approval engine or memory engine.

```text
Pantheon Next governs.
Hermes executes explicit bounded handoffs.
The cockpit exposes projections and narrow owner actions.
The human decides.
```

## Implemented projections

- Project Document cards.
- Knowledge cards.
- Work Issue cards.
- Read-only Resource Profiles.
- Proposal-only Effect preview.
- Proposal-only structure manifest preview.
- Proposal-only site navigation profile preview.
- One signed, human-confirmed Knowledge `UPDATE` Gate.

## Site resources

A Knowledge card may contain several linked addresses. Those addresses remain attributes of the Knowledge projection; this candidate does not create one persistent Site object or one card per URL.

Current retrieval posture:

```text
address_only
crawl_status: not_authorized
vector_status: not_indexed
```

The structure manifest preview lets a human propose exact sites, path prefixes and depth. It performs zero network requests and persists nothing.

## Site-specific navigation profile preview

Route:

```text
POST /v1/projects/{project}/knowledge/{knowledge}/navigation-profiles/preview
```

Input:

```text
task
selected linked URLs (optional)
```

The route classifies already-linked sites into bounded navigation archetypes such as:

```text
legal_database
hierarchical_safety_reference
interactive_geospatial_portal
public_information_portal
generic_web_information_site
```

It returns:

- probable entry points;
- task families;
- preferred navigation strategy;
- verification fields;
- a read-only navigation sequence;
- candidate binding classes:
  - browse.sh task-specific skill;
  - controlled local Hermes skill;
  - generic Hermes web tools fallback.

The profile is deterministic orientation only. It does not query browse.sh, inspect a real skill, access the target site, install anything or claim that the proposed navigation still matches the current site.

```text
profile candidate != site understood
skill discovered != skill installed
installed != approved
healthy != safe
navigation success != Evidence
page found != rule applicable to the project
```

Capability Slot:

```text
function: site_specific_information_retrieval
candidate Hermes binding: per site and task, to verify
installation status: not assessed
health: not checked
update status: not checked
activation: not authorized
```

Open Gates:

```text
skill discovery or local-skill review
human task-scope approval
binding health review
activation authorization
```

## Responsibility split

```text
Pantheon governs
- admitted sites and task scope
- candidate binding posture
- installation, approval, health, update and activation distinctions
- required result and trace fields

Hermes executes
- only after a separate bounded handoff and authorization
- site search, extraction or browser navigation

Cockpit / OpenWebUI expose
- linked sites
- candidate profile
- binding and Gate posture
- result and trace candidates

Human approves
- task scope
- skill admission or installation proposal
- activation and consequential use
```

## Not implemented

- live browse.sh catalog search;
- skill inspection or security review;
- skill installation;
- local skill generation;
- site crawl or navigation execution;
- persistent navigation profiles;
- structure index persistence;
- health probes;
- update monitoring;
- activation or rollback;
- Site as a new first-class persisted ontology object.

## Knowledge UPDATE boundary

The signed Knowledge update routes remain:

```text
POST /v1/projects/{project}/knowledge/{knowledge}/updates/preview
POST /v1/projects/{project}/knowledge/{knowledge}/updates/apply
```

The current review status is preserved. Applying an update does not review the Knowledge or turn it into Evidence.

## Maintenance boundary

`app.js` owns the common card renderer. `resources.js` enriches cards with file and linked-site profiles. Backend modules own proposal-only manifest and navigation-profile contracts. No hidden browser or install action is attached to card rendering.

## Validation

Validated on head `9c7c3aac04bf01aca31703e1f7e1919b6c4de3eb`:

- static cockpit and API shell contracts;
- proposal-only effect contracts;
- Resource Profile and structure-manifest contracts;
- site navigation archetype and binding-candidate contracts;
- exact-project, exact-Knowledge and linked-URL route boundaries;
- signed Knowledge UPDATE contracts;
- complete PostgreSQL/pgvector test suite.

Both GitHub Actions jobs passed.
