(() => {
  "use strict";

  const SOURCE_RESOLVERS = Object.freeze({
    pending_change_candidates(context) {
      return context.state.changeCandidates
        .filter(item => ["pending_review", "revision_requested"].includes(item.status))
        .map(context.normalizeChangeCandidate);
    },
    work_decisions(context) {
      return context.state.workIssues
        .filter(item => ["review", "needs_review"].includes(context.workData(item).status))
        .map(context.normalizeWorkDecision);
    },
    current_runs(context) {
      return context.currentRunItems().map(context.normalizeCurrentRun);
    },
    projects(context) {
      const models = context.state.projects.map(item => context.normalizeProject(item, {
        selected: item.project_id === context.selectedProjectId,
      }));
      const ids = new Set(models.map(model => model.entity_id));
      if (context.selectedProjectId && context.selectedCardId && !ids.has(context.selectedCardId)) {
        models.push(context.normalizeProject({
          project_id: context.selectedProjectId,
          display_name: context.selectedProjectId,
          code: context.selectedProjectId,
          status: "active",
          contacts: [],
          attributes: {},
        }, { selected: true }));
      }
      return models;
    },
    knowledge(context) {
      return context.state.knowledge.map(context.normalizeKnowledge);
    },
    tools(context) {
      return context.buildToolCards();
    },
  });

  function modelsForSources(sources, context) {
    const models = [];
    for (const source of sources) {
      const resolver = SOURCE_RESOLVERS[source];
      if (!resolver) throw new Error(`Unsupported child collection source: ${source}`);
      models.push(...resolver(context));
    }
    return models;
  }

  function registerCollection(parentId, models, context) {
    const ids = models.map(model => context.putCard(model));
    context.setChildren(parentId, ids);
    return ids;
  }

  function assembleRootCollections(context) {
    for (const rootId of context.rootItemIds) {
      const sources = context.sourcesFor(rootId);
      registerCollection(rootId, modelsForSources(sources, context), context);
    }
  }

  function assembleSelectedProject(context) {
    if (!context.selectedCardId || !context.state.cards.has(context.selectedCardId)) return;
    const contactsId = context.putCard(context.normalizeContacts(
      context.selectedProjectId,
      context.selected?.contacts || [],
    ));
    const models = [
      ...context.state.information.map(context.normalizeInformation),
      ...context.state.legacyDocuments.map(context.normalizeLegacyDocument),
      ...context.state.workIssues.map(context.normalizeWork),
    ];
    context.setChildren(contactsId, []);
    context.setChildren(context.selectedCardId, [
      contactsId,
      ...models.map(model => context.putCard(model)),
    ]);
  }

  function assemble(context) {
    if (!Array.isArray(context.rootItemIds) || typeof context.sourcesFor !== "function") {
      throw new Error("Child collection assembly requires registry-backed root sources");
    }
    assembleRootCollections(context);
    assembleSelectedProject(context);
  }

  window.PantheonChildCollectionAssembler = Object.freeze({
    assemble,
    supportedSources: Object.freeze(Object.keys(SOURCE_RESOLVERS)),
  });
})();