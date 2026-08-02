(() => {
  "use strict";

  const registry = window.PantheonNavigationRegistry;
  const navigation = window.PantheonSpatialNavigation;
  if (!registry) throw new Error("Navigation registry unavailable");
  if (!navigation?.create) throw new Error("Spatial navigation unavailable");

  const root = registry.root_collection;
  const originalCreate = navigation.create.bind(navigation);

  navigation.create = options => originalCreate({
    ...options,
    root_collection_id: root.id,
    root_item_ids: root.items.map(item => item.id),
  });

  window.PantheonNavigationProjection = Object.freeze({
    rootCollectionId: root.id,
    rootItemIds: Object.freeze(root.items.map(item => item.id)),
    sourcesFor(spaceId) {
      const item = root.items.find(entry => entry.id === spaceId);
      return item ? item.sources.slice() : [];
    },
  });
})();
