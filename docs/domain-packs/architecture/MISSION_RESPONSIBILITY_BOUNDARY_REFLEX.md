# Architecture Mission and Responsibility Boundary Reflex

Status: candidate — architecture-domain reflex for mission scope and responsibility boundaries.

This document is not canonical doctrine yet.

It does not implement legal review, insurance review, contract management, approval engine, email sending, Notion write, runtime behavior or professional validation.

It defines a candidate reflex for detecting when an answer, draft, site report line, technical comment, financial review or external reply may exceed the architect's mission or imply an unwanted responsibility.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Professional outputs can accidentally enlarge the architect's role.

A useful answer may be dangerous if it can be read as:

```text
technical validation;
execution instruction;
visa;
OPC / planning control;
financial approval;
acceptance of extra works;
insurance confirmation;
regulatory validation;
recognition of fault;
mission extension;
```

This reflex ensures that Pantheon alerts the user first, then prepares a bounded reply only when requested or clearly needed.

## Core rule

```text
If a subject is outside or unclear within the mission,
Pantheon first warns the user internally.
It does not draft an external reply unless the user asks for one or an external response is clearly expected.
If the reply is needed, it must be a limitation, orientation or clarification reply, not a validation or prescription.
```

## Trigger

Open this reflex whenever the task touches:

```text
structure;
waterproofing;
fire safety;
accessibility;
thermal / acoustic specialist input;
soil / foundation;
pathology;
OPC / planning;
financial validation;
invoice / quote / payment;
insurance / décennale;
DTU / normative compliance;
contractual responsibility;
client reproach;
formal notice;
technical solution proposed by enterprise;
mode opératoire;
support acceptance;
Notion validated write;
external message;
mission complémentaire;
```

Also open this reflex when the user asks for a mail, site report line, client response, enterprise response or decision wording.

## Mission boundary classification

Classify the subject:

```text
in_scope;
probably_in_scope;
unclear;
probably_out_of_scope;
out_of_scope;
mission_complement_required;
```

Classify responsibility risk:

```text
low;
medium;
high;
critical;
```

Classify reply posture:

```text
no_external_reply;
internal_warning_only;
cannot_pronounce;
limited_alert_and_orientation;
request_competent_party_review;
request_clarification;
propose_mission_complement;
```

Classify external action:

```text
none;
blocked_until_user_request;
blocked_until_user_validation;
requires_User_Decision_Gate;
```

## First response behavior

When mission boundary risk is detected, Pantheon responds first to the user.

Compact answer:

```text
Attention: this may be outside the mission.
Risk: the reply could be read as validation / instruction / responsibility.
Safe posture: do not pronounce on the substance, or reply only with scope limitation and referral to the competent party.
```

If the user has not clearly requested a mail, Pantheon should ask a targeted posture question:

```text
Do you want:
1. a short reply saying we cannot pronounce;
2. a bounded reply with points of vigilance and referral to the competent party;
3. a reply proposing a mission complement or specialist review?
```

Do not ask this question if the user already explicitly requested one posture.

## External reply rule

If a response is required despite the subject being outside or unclear within mission, the reply must be one of:

```text
limitation reply;
orientation reply;
request for competent party review;
request for missing source / clarification;
mission complement proposal;
```

It must not be:

```text
technical validation;
execution prescription;
approval of enterprise method;
financial approval;
acceptance of quote or avenant;
regulatory conclusion;
insurance confirmation;
recognition of responsibility;
```

## Safe wording patterns

Allowed patterns:

```text
This point does not fall within the mission entrusted to our agency.
We cannot validate the proposed solution, prescribe an execution method or assume responsibility for this point.
Our intervention may only consist in drawing attention to the issue and recommending review by the competent party.
This point should be confirmed by the relevant BET / enterprise / economist / insurer / control office before any decision.
This reply does not constitute visa, execution validation, financial acceptance or extension of our mission.
If you want our agency to instruct this point further, a mission complement must be defined and accepted beforehand.
```

French working formulations:

```text
Ce point ne relève pas de la mission confiée à notre agence.
Nous ne pouvons donc pas en assurer la validation, prescrire une solution d'exécution ou en porter la responsabilité.
Nous pouvons uniquement attirer votre attention sur la nécessité de faire vérifier ce point par l'intervenant compétent.
Dans l'attente de cette confirmation, aucune validation de notre part ne peut être considérée comme acquise.
Cette réponse ne vaut ni visa, ni validation d'exécution, ni acceptation financière, ni extension de notre mission.
```

## Dangerous wording

Avoid unless explicitly supported, in scope and approved:

```text
We validate;
You may execute;
This is compliant;
The quote is justified;
The company must do X;
We accept the extra works;
This is covered by insurance;
This is our responsibility;
We will handle the planning;
This point is closed;
```

French dangerous wording:

```text
Nous validons;
Vous pouvez réaliser;
Cette solution est conforme;
Le devis est justifié;
L'entreprise doit réaliser cette solution;
Nous acceptons l'avenant;
Cette prestation est couverte par l'assurance;
Nous prenons en charge ce point;
Nous pilotons le planning;
Ce point est levé;
```

## Common cases

### No OPC mission

Safe posture:

```text
The agency may report a delay, alert on coordination risk and record consequences.
It must not present itself as full planning pilot if OPC is excluded.
```

Suggested wording:

```text
En l'absence de mission OPC, nous attirons votre attention sur ce point de coordination sans que cela vaille pilotage général du planning.
```

### No structural mission / missing BET

Safe posture:

```text
The agency may identify that a structural point requires review.
It must not validate sizing, reinforcement or method.
```

Suggested wording:

```text
Ce point nécessite confirmation par le BET structure avant toute validation ou instruction d'exécution.
```

### Invoice / quote / extra works

Safe posture:

```text
The agency may produce a document-coherence or progress-candidate review if mission allows.
It must not issue bon à payer, accept avenant or recognize debt unless explicitly approved and in scope.
```

Suggested wording:

```text
Notre analyse porte uniquement sur la cohérence des pièces transmises et ne vaut ni acceptation d'avenant, ni bon à payer, ni validation comptable.
```

### Enterprise method / mode opératoire

Safe posture:

```text
The enterprise remains responsible for its means and methods, unless contract says otherwise.
The agency may request method description, proof, BET or system documentation.
```

Suggested wording:

```text
Nous ne pouvons pas nous substituer à l'entreprise dans le choix de son mode opératoire. Celui-ci doit être justifié par l'entreprise et, si nécessaire, validé par l'intervenant compétent.
```

### Insurance / décennale

Safe posture:

```text
The agency may note a coverage gap candidate.
It must not confirm final insurance coverage.
```

Suggested wording:

```text
L'activité assurée devra être confirmée par l'attestation et, si nécessaire, par l'assureur. Nous ne pouvons pas nous prononcer définitivement sur la couverture assurantielle.
```

## Required source check

If the consequence is material, try to retrieve:

```text
contract / letter of mission;
mission phase and scope;
excluded missions;
mission complements;
CCAP / CCTP / AE;
BET / economist / insurer / control office responsibilities;
previous written alerts;
client decisions;
```

If mission scope cannot be found:

```text
Mission boundary unknown.
Candidate internal answer may proceed, but external reply should be blocked or use limitation wording until the mission scope is confirmed.
```

## Interaction with other reflexes

This reflex applies before external-facing output from:

```text
Site Report Finalization Reflex;
Invoice / Quote Review Reflex;
Lot Scope and Insurance Reflex;
Photo Chantier Observation Reflex;
Material Choice Reflex;
CCTP from Plan Reflex;
Document Summary Reflex;
Client / Enterprise Reply Reflex;
DTU / Local Source Check Reflex;
```

## Output shape

```text
Mission boundary status:
Responsibility risk:
Reply posture:
Safe wording required:
Forbidden wording:
Need user choice before mail: yes / no
External action status:
```

## Final rule

```text
A useful answer must not become an unintended mission extension.
If the subject is outside mission, the safest reply is a boundary reply.
If guidance is useful, it remains orientation and referral, not prescription or validation.
```
