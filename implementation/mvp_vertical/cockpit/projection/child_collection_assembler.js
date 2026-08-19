(() => {
  "use strict";

  function decisionProjection() {
    const projection = window.PantheonDecisionRequestProjection;
    if (!projection?.normalize || !projection?.rootCard) {
      throw new Error("Decision Request projection unavailable");
    }
    return projection;
  }

  function anatomyProjection() {
    const projection = window.PantheonProjectAnatomyProjection;
    if (!projection?.projectCards) {
      throw new Error("Project Anatomy projection unavailable");
    }
    return projection;
  }

  function projectChildCollection(model) {
    const projectId = String(model?.source_project_id || "").trim();
    const entityId = String(model?.entity_id || "").trim();
    if (!projectId || !entityId) return model;
    return {
      ...model,
      child_collection: Object.freeze({
        state: "available",
        collection_id: `children:${entityId}`,
        load_action: Object.freeze({ kind: "project_bundle", context_id: projectId }),
        can_add: true,
        create_action: Object.freeze({
          kind: "information_create",
          context_id: projectId,
          title: "Nouvelle information",
          detail: "Ajouter une carte à cette affaire",
        }),
      }),
    };
  }

  function withLoadedChildCollection(model, collectionId) {
    if (!model || !collectionId) return model;
    const current = model.child_collection && typeof model.child_collection === "object"
      ? model.child_collection
      : {};
    return {
      ...model,
      child_collection: Object.freeze({
        ...current,
        state: "loaded",
        collection_id: collectionId,
        can_add: current.can_add === true,
        create_action: current.create_action || null,
      }),
    };
  }

  const SOURCE_RESOLVERS = Object.freeze({
    pending_change_candidates(context) {
      return context.state.changeCandidates
        .filter(item => ["pending_review", "revision_requested"].includes(item.status))
        .map(context.normalizeChangeCandidate);
    },
    decision_requests(_context) {
      const projection = decisionProjection();
      return (window.PantheonGlobalDecisionRequests || []).map(projection.normalize);
    },
    current_runs(context) {
      return context.currentRunItems().map(context.normalizeCurrentRun);
    },
    projects(context) {
      const models = context.state.projects.map(item => projectChildCollection(context.normalizeProject(item, {
        selected: item.project_id === context.selectedProjectId,
      })));
      const ids = new Set(models.map(model => model.entity_id));
      if (context.selectedProjectId && context.selectedCardId && !ids.has(context.selectedCardId)) {
        models.push(projectChildCollection(context.normalizeProject({
          project_id: context.selectedProjectId,
          display_name: context.selectedProjectId,
          code: context.selectedProjectId,
          status: "active",
          contacts: [],
          attributes: {},
        }, { selected: true })));
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

  function ensureRootCard(rootId, context) {
    if (context.state.cards.has(rootId)) return;
    if (rootId === "space:decisions") {
      context.putCard(decisionProjection().rootCard());
      return;
    }
    throw new Error(`Navigation root card is missing: ${rootId}`);
  }

  function registerCollection(parentId, models, context) {
    const ids = models.map(model => context.putCard(model));
    const collectionId = `children:${parentId}`;
    const parent = context.state.cards.get(parentId);
    if (parent) context.putCard(withLoadedChildCollection(parent, collectionId));
    context.setChildren(parentId, ids);
    return ids;
  }

  function assembleRootCollections(context) {
    for (const rootId of context.rootItemIds) {
      ensureRootCard(rootId, context);
      const sources = context.sourcesFor(rootId);
      registerCollection(rootId, modelsForSources(sources, context), context);
    }
  }

  function assembleAnatomy(context) {
    const anatomy = context.state.projectAnatomy;
    if (!anatomy || anatomy.project_ref !== context.selectedProjectId) return [];
    const projection = anatomyProjection().projectCards(anatomy);
    if (!projection?.root) return [];
    const rootId = context.putCard(projection.root);
    const childIds = (projection.children || []).map(model => context.putCard(model));
    const root = context.state.cards.get(rootId);
    if (root) context.putCard(withLoadedChildCollection(root, `children:${rootId}`));
    context.setChildren(rootId, childIds);
    return [rootId];
  }

  function assembleSelectedProject(context) {
    if (!context.selectedCardId || !context.state.cards.has(context.selectedCardId)) return;
    const contactsId = context.putCard(context.normalizeContacts(
      context.selectedProjectId,
      context.selected?.contacts || [],
    ));
    const projectDecisionModels = (window.PantheonProjectDecisionRequests || [])
      .map(decisionProjection().normalize);
    const models = [
      ...context.state.information.map(context.normalizeInformation),
      ...context.state.legacyDocuments.map(context.normalizeLegacyDocument),
      ...context.state.workIssues.map(context.normalizeWork),
      ...projectDecisionModels,
    ];
    context.setChildren(contactsId, []);
    const childIds = [
      contactsId,
      ...assembleAnatomy(context),
      ...models.map(model => context.putCard(model)),
    ];
    const selected = context.state.cards.get(context.selectedCardId);
    if (selected) {
      const collectionId = selected.child_collection?.collection_id || `children:${context.selectedCardId}`;
      context.putCard(withLoadedChildCollection(selected, collectionId));
    }
    context.setChildren(context.selectedCardId, childIds);
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
