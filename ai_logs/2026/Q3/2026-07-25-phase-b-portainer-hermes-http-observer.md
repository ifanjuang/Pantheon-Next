# AI intervention trace — Phase B Portainer and Hermes HTTP observer

Date: 2026-07-25
Status: validation-only trace
Boundary profile: validation_only_trace.

## Human direction

The repository owner asked to continue from the merged Paperless/Hermes/Cockpit stack toward real Phase B deployment and explicitly warned that repository updates had to be considered before acting.

No SSH or Portainer control connector was available in the working session. The target host was therefore not modified and no deployment/health claim is recorded.

## Repository recheck

Before the deployment-preparation change, the current main heads were rechecked.

```text
Pantheon Next main      a488d915329cab62465c7aef5c026f6e11f55b23
pantheon-mvp main       3a622a3fc33be4b9461cd7b46aed295824697bd2
```

External runtime work was then implemented and merged as:

```text
pantheon-mvp #76
merge: 86530e536d758a1931267f54081fa51aa76dfab9
```

## External implementation added by #76

```text
compose.phase-b.yaml
mvp_vertical.document_runtime_network_observer
docs/PHASE_B_PORTAINER_DEPLOYMENT.md
network/secret boundary tests
Hermes HTTP inventory tests
```

The composition is additive: it does not recreate an existing OpenWebUI or SearXNG service.

## Hermes update incorporated

The reviewed Hermes API surface supports an authenticated read-only skill inventory endpoint:

```text
GET /v1/skills
Authorization: Bearer <API_SERVER_KEY>
```

The external network observer therefore no longer requires CLI co-location for the reference multi-container/Portainer layout.

The legacy fixed `hermes skills list` observation remains available for local/offline use.

Preserved distinctions:

```text
skill listed != capability approved
skill listed != task authorized
runtime observation != activation decision
```

## Deployment placement

```text
Pantheon policy stack
  compose.policy-api.yaml
  governance/policy only

External runtime stack
  pantheon-mvp compose.phase-b.yaml
  pgvector + Docling + Paperless + gateway + Cockpit + Hermes + observer

Existing OpenWebUI
  reused
  attached separately to private ai-net by the operator
  server-to-server Hermes connection when selected
```

Pantheon does not become the installer or Portainer controller.

## Secret boundary

The deployment candidate preserves:

```text
Cockpit does not receive Paperless/PDP/issuer secrets.
Hermes does not receive Paperless/PDP/database/issuer secrets.
Paperless gateway owns bounded Paperless/PDP credentials server-side.
Network observer owns read credentials server-side and does not project them.
```

No target secret value or private host path is committed to the repositories.

## Target status

At the time of this trace:

```text
Phase B external compose implementation   merged candidate
network-native Hermes observer            merged candidate
Portainer operator handoff                documented candidate
existing target OpenWebUI modification    not executed
target ai-net                             not observed
target Pantheon PDP deployment            not observed
target Paperless installation             not observed
target Hermes installation                not observed
target Hermes skill inventory             not observed
target Docling health                     not observed
target synthetic intake                   not run
target issuer-authenticated proof         not run
activation                                not authorized
real-dossier use                          not authorized
production adoption                       not decided
```

```text
compose present != target deployed
installed != approved
healthy != safe
runtime success != Evidence
```
