# Landing page — stack, local deployment and access revision

Status: candidate editorial patch.

This document defines the next landing-page revision before editing `docs/index.html` directly.

It is not doctrine, not runtime behavior and not an implementation.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon governs.
```

## Purpose

The landing page must explain Pantheon Next in a way that is immediately understandable for an agency or professional user.

The current page is doctrinally coherent but still too abstract for a first visitor. PR #54 adds a useful detailed diagram, but the practical stack and access model should appear before the dense diagram.

## Recommended page hierarchy

1. Hero: status, proof, decision, memory.
2. Concrete risk block: old version, source mistaken for proof, message that engages, dirty memory.
3. Simple dossier path: pieces -> context -> AI work -> candidate -> human decision -> memory or action.
4. Installation block: local / server / NAS / browser / mobile.
5. Software block: required and optional components.
6. Architecture use cases.
7. Honest status and non-runtime boundary.
8. Detailed iterative diagram: lower, collapsed or moved to a detail page.

## Hero rewrite

```text
L'IA rédige.
Pantheon garde le statut.
```

Supporting line:

```text
Pantheon Next cadre l'usage de l'IA dans les dossiers professionnels : pièces, sources, versions, décisions, preuves, engagements externes et mémoire validée.
```

Clarification:

```text
Le sujet n'est pas de faire répondre l'IA plus vite. Le sujet est de savoir ce qu'elle a utilisé, ce qu'elle affirme, ce qui reste à vérifier, ce qui engage l'agence et ce qui peut être conservé.
```

## Concrete risk block

### Retrouvé ne veut pas dire vrai

Un extrait de CCTP, de PLU ou de compte rendu reste une source candidate tant que son statut n'est pas qualifié.

### Ancienne version, mauvaise décision

Une pièce peut être utile, obsolète, remplacée, partielle ou contradictoire. Pantheon force cette distinction.

### Le mail qui engage

Préparer un message n'est pas l'envoyer. Valider un devis, accepter un périmètre ou répondre à un client reste un acte visible.

### La mémoire sale

Un échange utile ne devient pas mémoire canonique par accident. Seul le validé, borné et sourcé peut rester.

## Simple dossier path

```text
1. Pièces
   plans, comptes rendus, devis, mails, photos, règlements, pièces marché.

2. Contexte
   strict nécessaire transmis, périmètre et source visibles.

3. Travail IA
   recherche, extraction, comparaison, rédaction, synthèse.

4. Résultat candidat
   réponse avec sources, hypothèses, limites et contradictions.

5. Décision humaine
   valider, refuser, corriger, envoyer, signer ou ne rien faire.

6. Mémoire ou action
   seul le validé peut être transmis ou conservé.
```

## Installation block

The landing should state this plainly:

```text
Le déploiement cible est simple à comprendre : une interface accessible par navigateur, un agent d'exécution qui fait le travail, un modèle IA au choix, et un cadre Pantheon qui qualifie les décisions.
```

Local / NAS wording:

```text
Les dossiers peuvent rester sur l'infrastructure de l'agence : poste, serveur local, NAS ou dépôt documentaire contrôlé. Un modèle local peut être utilisé pour limiter les sorties de données. Un fournisseur IA externe peut aussi être utilisé quand le cadre de confidentialité l'autorise.
```

Access wording:

```text
L'utilisateur accède au cockpit depuis un navigateur. Selon la configuration réseau, cela peut être un poste d'agence, un portable, une tablette ou un téléphone. Des entrées par discussion ou message peuvent exister si un connecteur est installé, mais elles restent des entrées candidates et ne contournent pas les gates Pantheon.
```

## Software block

### Required: OpenWebUI

OpenWebUI is the exposure surface.

It provides:

- browser access;
- user accounts and conversations;
- model selection;
- display of status, evidence and decision prompts;
- the user-facing cockpit.

It does not become Canonical Memory, governance authority or automatic approval surface.

### Required: Hermes Agent

Hermes Agent is the execution runtime.

It may:

- read and prepare files;
- search, extract, compare and summarize;
- call authorized tools;
- produce Result Candidates and Evidence Pack Candidates.

It must not approve, canonize, promote memory or bypass human decision.

### Choice: local model or external provider

Pantheon does not impose the model.

Possible posture:

- local model for sensitive or bounded work;
- external provider for stronger models, multimodal work or specialized reasoning;
- in all cases, the transmitted context remains minimal and explicit.

### Optional: Langfuse

Langfuse can observe traces, costs, latency and execution metadata.

It is useful for diagnostics and audit support. It is not an Evidence Pack and does not validate an answer.

### Optional: Langflow

Langflow can prepare deterministic or visual flows: extraction, cleaning, chunking, pre-checking and context assembly.

It prepares candidates. It does not validate, approve or remember.

### Optional: LangGraph

LangGraph may be useful later for long-running or interruptible workflows.

Its state is runtime state. It is not Canonical Memory, approval or proof.

### Optional: provenance graph

A graph can link sources, claims, contradictions, decisions and memory candidates.

A relation is not proof until selected and represented in an Evidence Pack.

## Architecture use-case additions

Add or revise use cases with more field language:

- CR chantier: detect recurring issues, follow reservations, count reminders, keep dates and lots visible.
- Photo chantier: describe the photo, suggest the likely lot, identify a doubt, ask for validation before inserting in a report.
- Marches and contracts: compare CCTP, DPGF, planning and penalties without replacing legal review.
- Situations and invoices: compare progress, invoiced items and missing posts.
- Permits and administrative forms: prepare candidates, never file or validate without explicit decision.

## PR #54 placement

Decision: accept the concept, but revise placement.

The detailed diagram should be either:

- lower than the practical stack section;
- inside a collapsed details block;
- or moved to a dedicated detail page.

It should not be the first complex object a new visitor sees.

## Repository state

Documented non-implemented.

This file is an editorial candidate for revising `docs/index.html`. It does not add runtime behavior, schema, tests, operations, platform, Docker or environment changes.
