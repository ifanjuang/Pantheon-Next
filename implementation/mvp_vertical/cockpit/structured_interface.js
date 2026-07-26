(() => {
  "use strict";

  const PRIMARY_SPACES = Object.freeze(["pantheon", "decisions", "affaires", "connaissances", "outils"]);
  const CARD_ROLES = Object.freeze(["conversation", "container", "entity"]);

  // Technical families stay backward-compatible with the current renderer.
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
    "contact",
    "work",
    "information",
    "tool",
  ]);

  // Simplified visual vocabulary targeted by the schema-driven renderer.
  const PRESENTATION_FAMILIES = Object.freeze([
    "project",
    "information",
    "contact",
    "work",
    "decision",
    "tool",
  ]);

  const PRESENTATION_FAMILY_ALIASES = Object.freeze({
    document: "information",
    knowledge: "information",
    evidence: "information",
    capability: "tool",
    "runtime-host": "tool",
    "role-reference": "tool",
  });

  function normalizeStringList(value) {
    if (!Array.isArray(value)) return [];
    return value
      .map(item => typeof item === "string" ? item.trim() : String(item?.slug ?? item?.name ?? item?.label ?? "").trim())
      .filter(Boolean);
  }

  function buildTagProjection(tag) {
    return {
      tag_id: tag.tag_id ?? tag.id ?? null,
      slug: String(tag.slug ?? tag.name ?? tag.label ?? "").trim(),
      name: String(tag.name ?? tag.title ?? tag.label ?? tag.slug ?? "").trim(),
      description: String(tag.description ?? "").trim(),
      icon_key: tag.icon_key ?? null,
      color: tag.color ?? null,
      aliases: Array.isArray(tag.aliases) ? tag.aliases : [],
      status: tag.status ?? null,
    };
  }

  function presentationFamily(card) {
    const explicit = card?.presentation_family;
    if (explicit && PRESENTATION_FAMILIES.includes(explicit)) return explicit;
    return PRESENTATION_FAMILY_ALIASES[card?.family] || card?.family || "information";
  }

  function buildCardProjection(input = {}) {
    return {
      category: input.category ?? null,
      index: input.index ?? null,
      date: input.date ?? null,
      author: input.author ?? null,
      type_tags: normalizeStringList(input.type_tags),
      subject_tags: normalizeStringList(input.subject_tags ?? input.tags),
      limits: normalizeStringList(input.limits),
      available_actions: normalizeStringList(input.available_actions),
      presentation_family: input.presentation_family ?? presentationFamily(input),
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

    const projection = buildCardProjection(card);
    if (!PRESENTATION_FAMILIES.includes(projection.presentation_family) && projection.presentation_family !== "pantheon") {
      errors.push("invalid presentation family");
    }
    return { valid: errors.length === 0, errors };
  }

  window.PantheonStructuredInterface = Object.freeze({
    primarySpaces: PRIMARY_SPACES,
    cardRoles: CARD_ROLES,
    cardFamilies: CARD_FAMILIES,
    presentationFamilies: PRESENTATION_FAMILIES,
    buildTagProjection,
    buildCardProjection,
    presentationFamily,
    buildCardContextEnvelope,
    validateCardModel,
  });
})();