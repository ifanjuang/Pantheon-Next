# Capability, Resource and Installation Composition Model

Status: obsolete — superseded by the common installation baseline.
Boundary profile: historical_record_only.

This document formerly proposed an installation-composition object between capabilities, resources, bindings and external provisioners.

That model is no longer part of the active Pantheon installation architecture.

The current owners are:

```text
docs/governance/COMMON_INSTALLATION_BASELINE.md
  single required component baseline

docs/governance/INSTALL_MODULE_CATALOG.md
  independent module records, status, dependencies, gates and rollback

docs/install/COMMON_BASELINE_RUNBOOK.md
  manual operator installation sequence
```

The historical composition model must not be used to:

```text
select an alternative stack
classify a component as optional for one installation
create a package-selection UI
compose an automatic installer
infer activation or authorization
```

Historical examples remain recoverable through Git history and earlier ai_logs. They are not active doctrine, implementation instructions or an installation contract.

```text
historical model != current authority
catalog record != installation composition
required presence != active binding
installed != approved
```
