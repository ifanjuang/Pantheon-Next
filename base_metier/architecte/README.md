# Base métier architecte

Ce dossier regroupe la base métier architecture utilisée par Pantheon pour les recherches RAG internes, les prompts, les skills et les workflows associés.

Organisation cible :

```txt
base_metier/architecte/
  knowledge/
    sources/   # PDF, MD ou documents originaux déposés manuellement
    corpus/    # versions Markdown regroupées, lisibles et relues
    chunks/    # fiches atomiques optimisées pour le RAG
    indexes/   # manifestes d'ingestion et index reconstruisibles
    schemas/   # schémas de validation des chunks

  skills/      # skills métier : ingestion, recherche, rédaction, contrôle
  prompts/     # prompts système et templates de réponse
  workflows/   # workflows gouvernés : extraction, validation, vectorisation
  evaluations/ # jeux de questions/réponses pour tester la qualité du RAG
```

Règle de gouvernance : les fichiers du dossier `knowledge/sources/` ne sont pas modifiés par les scripts. Ils servent de référence. Les index vectoriels sont des artefacts reconstruisibles.

Usage prévu : déposer les PDF dans `knowledge/sources/`, générer ou relire les fichiers Markdown dans `knowledge/corpus/`, puis lancer le futur skill d'ingestion locale pour produire les chunks et embeddings.
