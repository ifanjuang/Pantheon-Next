(() => {
  "use strict";

  const PRIMARY_SPACES = Object.freeze(["pantheon", "decisions", "affaires", "connaissances", "outils"]);
  const CARD_ROLES = Object.freeze(["conversation", "container", "entity"]);
  const CARD_FAMILIES = Object.freeze([
    "pantheon",
    "decision",
    "project",
    "document",
    "evidence",
    "knowledge",
    "capability",
    "runtime-host",
    "role-reference",
  ]);

  function buildTagProjection(tag) {
    return {
      tag_id: tag.tag_id ?? tag.id ?? null,
      name: String(tag.name ?? tag.label ?? "").trim(),
      description: String(tag.description ?? "").trim(),
      icon_key: tag.icon_key ?? null,
      color: tag.color ?? null,
      aliases: Array.isArray(tag.aliases) ? tag.aliases : [],
      status: tag.status ?? null,
    };
  }

  function buildCardContextEnvelope({ root, descendants = [], sources = [], additions = [], exclusions = [] }) {
    if (!root?.entity_id || !root?.entity_type) {
      throw new Error("Card context root requires entity_id and entity_type");
    }
    return {
      root_entity: {
        entity_id: root.entity_id,
        entity_type: root.entity_type,
      },
      descendants: descendants.map(item => ({ entity_id: item.entity_id, entity_type: item.entity_type })),
      source_refs: sources.filter(Boolean),
      explicit_additions: additions.map(item => ({ entity_id: item.entity_id, entity_type: item.entity_type })),
      explicit_exclusions: exclusions.map(item => ({ entity_id: item.entity_id, entity_type: item.entity_type })),
      scope_widened_implicitly: false,
    };
  }

  function validateCardModel(card) {
    const errors = [];
    if (!card?.entity_id) errors.push("entity_id required");
    if (!card?.entity_type) errors.push("entity_type required");
    if (!CARD_ROLES.includes(card?.role)) errors.push("invalid card role");
    if (!CARD_FAMILIES.includes(card?.family)) errors.push("invalid card family");
    if (!card?.title) errors.push("title required");
    return { valid: errors.length === 0, errors };
  }

  window.PantheonStructuredInterface = Object.freeze({
    primarySpaces: PRIMARY_SPACES,
    cardRoles: CARD_ROLES,
    cardFamilies: CARD_FAMILIES,
    buildTagProjection,
    buildCardContextEnvelope,
    validateCardModel,
  });
})();
