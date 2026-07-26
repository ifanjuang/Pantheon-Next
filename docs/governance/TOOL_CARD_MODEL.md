# Tool Capability Card Contract

Status: candidate support doctrine — documented non-implemented.

Boundary profile: candidate_support_note.

This document defines the governance information that a cockpit Tool Card must preserve. It does not define the executable UI, JSON store, Hermes inventory reader, merge algorithm, React/JavaScript component, installer or runtime adapter.

The concrete card implementation belongs in the external `pantheon-mvp` repository. Product-specific candidate bindings remain in `HERMES_CAPABILITY_BINDINGS.md`.

## Purpose

A Tool Card is a governance projection over one concrete tool, skill, plugin, function, MCP binding, workflow runtime or adjacent capability product.

It must let a human distinguish what the capability is from what has actually been observed or authorized.

Minimum visible contract:

```text
identity and clear title
short description
long operational description
resource type / native owner
Capability Slot relationship
source and provenance
installation observation
native runtime observation
health observation
update observation
Pantheon governance status
scope activation status
permissions / consequence-bearing effects
evidence expectation
rollback posture
last observation
next required human decision
```

A detailed description should explain what the tool does, where it sits, typical uses, material limitations and what its outputs do not prove or authorize.

## Provenance classes

A cockpit implementation must preserve provenance instead of flattening every row into a catalogue item.

```text
hermes_native_inventory
hermes_dynamic_skill
runtime_installed
pantheon_catalog
external_reference
operator_declared
discovered_binding
```

`hermes_dynamic_skill` means a skill or capability discovered through Hermes-owned native files, directories, manifests or inventory surfaces. Hermes or its reviewed adapter owns discovery and normalization. Pantheon may qualify the normalized observation; it must not become the skill loader or patch arbitrary Hermes files.

`pantheon_catalog` means a deliberately documented candidate or reference. Catalogue presence is not runtime presence.

## Required non-equivalences

```text
catalogued       != discovered
discovered       != installed
installed        != approved
native_enabled   != scope_activated
healthy          != safe
update_available != update_authorized
runtime_success  != evidence
binding_selected != dependency_adopted
watchlist_item   != install_instruction
```

These axes must remain independently visible when applicable.

## Capability Slot placement

Every concrete tool relationship must be expressible as:

```text
abstract capability
-> candidate binding
-> installation status
-> health status
-> update status
-> activation status
-> Pantheon gates
-> human approval
```

A card must also preserve:

```text
exposed_by
executed_by
governed_by
approved_by
forbidden
```

A product may satisfy several Capability Slots, but this does not make every slot an adopted dependency.

## Consequence-bearing dimensions

When applicable, the card must expose known or unknown status for:

```text
file read
file write
command execution
network/browser access
external API read
external API write
external communication
repository mutation
runtime configuration mutation
package installation
credential handling
private project-data access
memory-candidate production
external artifact production
```

Unknown permissions are displayed as unknown, never inferred safe.

## Evidence and technical receipts

A card may display runtime traces, probes, installation receipts, update diffs and rollback receipts. They remain technical observations.

```text
technical receipt != Evidence Pack
trace             != proof
successful probe  != safety
successful run    != approved result
```

The required `evidence_expectation` for consequential use remains separate.

## Reconciliation contract

A cockpit may reconcile a Pantheon catalogue record with one or more normalized Hermes/runtime observations. It must preserve unresolved disagreement rather than silently overwrite either side.

Valid reconciliation outcomes include:

```text
catalog_only
runtime_only
matched
version_drift
metadata_drift
possible_duplicate
source_unknown
adapter_incompatible
to_verify
```

Preferred matching signals are stable native identifier, admitted capability/skill identifier, pinned source reference or explicit operator mapping. Ambiguous records remain separate.

## Ownership boundary

```text
Pantheon Next
  defines the governance contract, Capability Slot placement, status distinctions,
  evidence/approval/scope rules and candidate binding doctrine.

pantheon-mvp
  implements the concrete cockpit record, catalogue data, card projection,
  normalized Hermes inventory ingestion and UI reconciliation.

Hermes
  owns native skill/tool/plugin/MCP/workflow discovery and execution mechanics.

OpenWebUI / cockpit
  exposes the resulting projection and decision surfaces.

Human
  approves consequential adoption, installation, activation, update and use.
```

## LangChain ecosystem placement

Concrete LangChain ecosystem candidates are not duplicated in this card contract. Their Capability Slot placement belongs in `HERMES_CAPABILITY_BINDINGS.md`; concrete catalogue records and card descriptions belong in `pantheon-mvp`.

At minimum the external catalogue may include LangChain, LangGraph, LangFlow and LangSmith without implying that any of them is installed, adopted or activated.

## Boundary

This contract is documentation only. It creates no runtime behavior, executable card, installer, updater, plugin manager, skill manager, scheduler, queue, provider router, MCP host or automatic approval path.
