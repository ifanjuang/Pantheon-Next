# Base métier architecture

Ce dossier reçoit les documents métier de référence utilisés par Pantheon pour les recherches RAG internes.

Principe d'organisation :

```txt
knowledge/base_metier_architecture/
  sources/   # PDF, MD ou documents originaux déposés manuellement
  corpus/    # versions Markdown regroupées, lisibles et relues
  chunks/    # fiches atomiques optimisées pour le RAG
  indexes/   # manifestes d'ingestion et index reconstruisibles
  schemas/   # schémas de validation des chunks
```

Règle de gouvernance : les fichiers du dossier `sources/` ne sont pas modifiés par les scripts. Ils servent de référence. Les index vectoriels sont des artefacts reconstruisibles.

Usage prévu : déposer les PDF dans `sources/`, générer ou relire les fichiers Markdown dans `corpus/`, puis lancer le futur skill d'ingestion locale pour produire les chunks et embeddings.
