const SWIPER_VERSION = "14.0.6";
const stage = document.getElementById("v2-stage");
const breadcrumb = document.getElementById("v2-breadcrumb");
const status = document.getElementById("v2-status");
const network = document.getElementById("v2-network");
const spaceButtons = [...document.querySelectorAll("[data-space]")];

if (!stage) throw new Error("Cockpit stage unavailable");

async function ensureSwiper() {
  if (typeof window.Swiper === "function") return;
  const candidates = [
    `https://cdn.jsdelivr.net/npm/swiper@${SWIPER_VERSION}/swiper-bundle.min.js`,
    `https://unpkg.com/swiper@${SWIPER_VERSION}/swiper-bundle.min.js`,
  ];
  for (const src of candidates) {
    try {
      await new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = src;
        script.async = true;
        script.onload = resolve;
        script.onerror = () => reject(new Error(`Swiper unavailable: ${src}`));
        document.head.append(script);
      });
      if (typeof window.Swiper === "function") return;
    } catch (_) {
      // Try next CDN.
    }
  }
  throw new Error("Swiper runtime unavailable");
}

const fixture = await fetch("demo-data.json", { cache: "no-store" }).then(response => {
  if (!response.ok) throw new Error(`Fixture indisponible (${response.status})`);
  return response.json();
});

await ensureSwiper();

document.documentElement.dataset.swiperReady = "true";
document.documentElement.dataset.swiperVersion = SWIPER_VERSION;
document.documentElement.dataset.cockpitMode = "demo";
window.PANTHEON_COCKPIT_DEMO = true;
if (network) network.textContent = "démo · données fictives";

const ROOT_ITEMS = [
  { id: "space:pantheon", title: "Pantheon", category: "Pantheon", family: "pantheon", status: "active", summary: "Contexte, gouvernance et décisions conséquentes.", details: "Pantheon gouverne ; il ne devient ni runtime, ni scheduler, ni moteur d’approbation automatique." },
  { id: "space:decisions", title: "Décisions", category: "Décisions", family: "decision", status: "review", summary: "Validations humaines et propositions à examiner." },
  { id: "space:affaires", title: "Affaires", category: "Projets", family: "project", status: "active", summary: "Projets, Informations, Contacts et Travaux." },
  { id: "space:connaissances", title: "Connaissances", category: "Références", family: "information", status: "neutral", summary: "Références réutilisables et état de revue." },
  { id: "space:outils", title: "Outils", category: "Outils", family: "tool", status: "neutral", summary: "Outils, skills, bindings et runtimes observés ou candidats." },
];

const stack = [];
const horizontalSwipers = new Map();
let levelSwiper = null;
let levelSlides = null;
let pendingChildFrame = null;
let levelTransitionLocked = false;

function model(id, title, category, family, summary, statusValue = "neutral", details = "") {
  return { id, title, category, family, summary, status: statusValue, details };
}

function projectModels() {
  return fixture.projects.map(project => model(
    `project:${project.project_id}`,
    project.display_name || project.code,
    "Projet",
    "project",
    [project.code, project.phase, project.location].filter(Boolean).join(" · "),
    project.status || "active",
    [
      project.primary_client ? `Client : ${project.primary_client}` : null,
      project.claim_values?.budget_target != null ? `Budget cible : ${new Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR", maximumFractionDigits: 0 }).format(project.claim_values.budget_target)}` : null,
      project.claim_values?.surface_projected != null ? `Surface projetée : ${project.claim_values.surface_projected} m²` : null,
    ].filter(Boolean).join("\n"),
  ));
}

function projectChildren(projectId) {
  const project = fixture.projects.find(item => item.project_id === projectId);
  const payload = fixture.project_payloads[projectId] || {};
  return [
    model(`contacts:${projectId}`, "Contacts", "Contacts", "contact", `${project?.contacts?.length || 0} contact(s)`, "neutral", (project?.contacts || []).map(item => [item.name, item.role, item.organization].filter(Boolean).join(" · ")).join("\n")),
    ...(payload.information || []).map(item => model(`information:${item.information_id}`, item.title, item.category || "Information", "information", item.summary, item.status, item.details || item.source_ref || "")),
    ...(payload.documents || []).map(item => model(`document:${item.document_id}`, item.title || item.naming?.object_name || "Document", item.naming?.document_type || "Document", "information", item.source_ref || "Document source", item.status || "ready", item.document_date || "")),
    ...(payload.knowledge || []).map(item => model(`knowledge:${item.knowledge_id}`, item.title, item.family || "Référence", "information", item.markdown || "Référence", item.review_status || "neutral", `Version ${item.version || 1}`)),
    ...(payload.work_issues || []).map(entry => {
      const item = entry.work_issue || entry;
      return model(`work:${item.issue_id}`, item.title, "Travail", "work", item.description || "Travail à traiter", item.status || "open", (item.tags || []).join(" · "));
    }),
  ];
}

function decisionModels() {
  return Object.values(fixture.project_payloads).flatMap(payload => (payload.change_candidates || []).map(item => model(
    `decision:${item.candidate_id}`,
    item.reason || "Modification à valider",
    "Décision",
    "decision",
    `Révision de base ${item.base_revision ?? "?"} · ${item.proposer || "Provenance non renseignée"}`,
    item.status || "pending_review",
    (item.changes || []).map(change => `${change.field}: ${change.before ?? "—"} → ${change.proposed ?? "—"}`).join("\n"),
  )));
}

function toolModels() {
  return (fixture.tool_catalog?.items || []).map(item => model(
    `tool:${item.tool_id}`,
    item.name || item.tool_id,
    item.category || "Outil",
    "tool",
    item.short_description || "Outil candidat",
    item.governance_state || "neutral",
    [
      `Installation : ${item.installation_state || "unknown"}`,
      `Santé : ${item.health_state || "unknown"}`,
      `Activation : ${item.activation_state || "unknown"}`,
      `Evidence : ${item.evidence_expectation || "À définir"}`,
    ].join("\n"),
  ));
}

function knowledgeModels() {
  return Object.values(fixture.project_payloads).flatMap(payload => (payload.knowledge || []).map(item => model(
    `knowledge:${item.knowledge_id}`,
    item.title,
    item.family || "Référence",
    "information",
    item.markdown || "Référence",
    item.review_status || "neutral",
    `Version ${item.version || 1}`,
  )));
}

function collectionFor(item) {
  if (item.id === "space:affaires") return { id: "projects", title: "Affaires", items: projectModels(), canCreate: true };
  if (item.id === "space:decisions") return { id: "decisions", title: "Décisions", items: decisionModels(), canCreate: false };
  if (item.id === "space:connaissances") return { id: "knowledge", title: "Connaissances", items: knowledgeModels(), canCreate: true };
  if (item.id === "space:outils") return { id: "tools", title: "Outils", items: toolModels(), canCreate: true };
  if (item.id.startsWith("project:")) {
    const projectId = item.id.slice("project:".length);
    return { id: `project:${projectId}:children`, title: item.title, items: projectChildren(projectId), canCreate: true };
  }
  return null;
}

function createFace(className, item, hydrated) {
  const face = document.createElement("div");
  face.className = `v2-card-face ${className}`;
  const top = document.createElement("header");
  top.className = "v2-card-top";
  top.innerHTML = `<div class="v2-card-identity"><div class="v2-card-identity-line"><span class="v2-family-mark">${item.family.slice(0, 1).toUpperCase()}</span><span class="v2-card-category"></span></div></div><span class="v2-state-icon"></span>`;
  top.querySelector(".v2-card-category").textContent = item.category;
  top.querySelector(".v2-state-icon").textContent = String(item.status || "").slice(0, 2).toUpperCase();
  const body = document.createElement("div");
  body.className = className.includes("back") ? "v2-back-body" : "v2-card-body";
  const title = document.createElement("h2");
  title.className = className.includes("back") ? "v2-back-title" : "v2-card-title";
  title.textContent = item.title;
  const copy = document.createElement("p");
  copy.className = className.includes("back") ? "v2-back-multiline" : "v2-card-summary";
  copy.textContent = hydrated ? (className.includes("back") ? item.details || item.summary : item.summary) : "Chargement des informations…";
  body.append(title, copy);
  face.append(top, body);
  return face;
}

function createCard(item, hydrated = false) {
  const article = document.createElement("article");
  article.className = "v2-card";
  article.dataset.entityId = item.id;
  article.dataset.family = item.family;
  article.dataset.status = item.status;
  article.dataset.cockpitV3 = "living-card";
  article.dataset.flipped = "false";
  article.tabIndex = 0;
  const inner = document.createElement("div");
  inner.className = "v2-card-inner";
  inner.append(createFace("v2-card-front", item, hydrated), createFace("v2-card-back", item, hydrated));
  article.append(inner);
  article.addEventListener("click", event => {
    if (event.target.closest("button,a,input,textarea,select")) return;
    article.dataset.flipped = article.dataset.flipped === "true" ? "false" : "true";
  });
  return article;
}

function hydrateSlide(slide, item) {
  if (!slide || slide.dataset.hydrated === "true") return;
  const previous = slide.querySelector(".v2-card");
  const flipped = previous?.dataset.flipped === "true";
  const card = createCard(item, true);
  card.dataset.flipped = String(flipped);
  slide.replaceChildren(card);
  slide.dataset.hydrated = "true";
}

function createNewSlide(collection) {
  const slide = document.createElement("div");
  slide.className = "swiper-slide v2-swiper-slide v3-swiper-slide";
  slide.dataset.synthetic = "create";
  const button = document.createElement("button");
  button.type = "button";
  button.className = "v2-swiper-create-card swiper-no-swiping";
  button.innerHTML = `<span class="v2-swiper-create-mark">+</span><span class="v2-swiper-create-copy"><strong>Nouveau</strong><small>Créer dans ${collection.title}</small></span>`;
  button.addEventListener("click", () => stage.dispatchEvent(new CustomEvent("pantheon:create-requested", { bubbles: true, detail: { collection_id: collection.id } })));
  slide.append(button);
  return slide;
}

function currentFrame() {
  return stack[stack.length - 1];
}

function createFrame(collection, rootSpace) {
  return { ...collection, index: 0, activeSynthetic: false, rootSpace };
}

function activeItem(frame) {
  if (!frame || frame.activeSynthetic) return null;
  return frame.items[frame.index] || null;
}

function childFrameFor(frame) {
  const item = activeItem(frame);
  if (!item) return null;
  const collection = collectionFor(item);
  if (!collection || !collection.items.length) return null;
  return createFrame(collection, frame.rootSpace || item.id.replace("space:", ""));
}

function updateLocation() {
  const labels = stack.map(frame => frame.title);
  if (breadcrumb) breadcrumb.textContent = labels.join(" / ");
  const frame = currentFrame();
  const active = activeItem(frame);
  if (status) {
    status.textContent = frame.activeSynthetic
      ? `Créer dans ${frame.title}`
      : active ? `${frame.items.length} carte(s) · ${active.title}` : "Collection vide";
  }
  spaceButtons.forEach(button => button.classList.toggle("is-active", frame.rootSpace === button.dataset.space));
}

function hydrateNear(frame, instance, index) {
  if (!frame || !instance || instance.destroyed) return;
  const offset = frame.canCreate ? 1 : 0;
  [index - 1, index, index + 1].forEach(swiperIndex => {
    const itemIndex = swiperIndex - offset;
    if (itemIndex < 0 || itemIndex >= frame.items.length) return;
    hydrateSlide(instance.slides[swiperIndex], frame.items[itemIndex]);
  });
  const idle = window.requestIdleCallback || (callback => window.setTimeout(callback, 20));
  idle(() => {
    if (instance.destroyed) return;
    frame.items.forEach((item, itemIndex) => hydrateSlide(instance.slides[itemIndex + offset], item));
  });
}

function buildHorizontalShell(frame) {
  const shell = document.createElement("div");
  shell.className = "swiper v3-swiper v3-collection-swiper";
  const wrapper = document.createElement("div");
  wrapper.className = "swiper-wrapper v2-swiper-wrapper";
  if (frame.canCreate) wrapper.append(createNewSlide(frame));
  frame.items.forEach(item => {
    const slide = document.createElement("div");
    slide.className = "swiper-slide v2-swiper-slide v3-swiper-slide";
    slide.dataset.entityId = item.id;
    slide.append(createCard(item, false));
    wrapper.append(slide);
  });
  shell.append(wrapper);
  return shell;
}

function buildLevelSlide(role, frame) {
  const slide = document.createElement("div");
  slide.className = `swiper-slide v3-level-slide v3-level-slide--${role}`;
  slide.dataset.levelRole = role;
  if (!frame) {
    slide.dataset.empty = "true";
    slide.setAttribute("aria-hidden", "true");
    return slide;
  }
  slide.append(buildHorizontalShell(frame));
  return slide;
}

function destroyHorizontal(role) {
  const instance = horizontalSwipers.get(role);
  instance?.destroy(true, true);
  horizontalSwipers.delete(role);
}

function initHorizontal(role, frame, { interactive = false } = {}) {
  if (!frame || !levelSlides) return null;
  const shell = levelSlides[role].querySelector(".v3-collection-swiper");
  if (!shell) return null;
  const initialSlide = frame.index + (frame.canCreate ? 1 : 0);
  const instance = new window.Swiper(shell, {
    direction: "horizontal",
    nested: true,
    initialSlide,
    slidesPerView: 1,
    speed: 320,
    threshold: 10,
    touchAngle: 45,
    resistanceRatio: 0.72,
    allowTouchMove: interactive,
    preventClicks: true,
    preventClicksPropagation: true,
    touchStartPreventDefault: false,
    touchMoveStopPropagation: false,
    noSwiping: true,
    noSwipingSelector: "button,input,select,textarea,a,[contenteditable='true']",
    roundLengths: true,
    a11y: { enabled: interactive, containerMessage: `Cartes de ${frame.title}`, slideLabelMessage: "Carte {{index}} sur {{slidesLength}}" },
    on: {
      init(swiperInstance) { hydrateNear(frame, swiperInstance, swiperInstance.activeIndex); },
      slideChange(swiperInstance) {
        if (!interactive) return;
        const activeSlide = swiperInstance.slides[swiperInstance.activeIndex];
        frame.activeSynthetic = activeSlide?.dataset.synthetic === "create";
        if (!frame.activeSynthetic) frame.index = swiperInstance.activeIndex - (frame.canCreate ? 1 : 0);
        hydrateNear(frame, swiperInstance, swiperInstance.activeIndex);
        updateLocation();
      },
      slideChangeTransitionEnd() {
        if (interactive) refreshChildLevel();
      },
    },
  });
  horizontalSwipers.set(role, instance);
  return instance;
}

function refreshChildLevel() {
  if (!levelSwiper || levelSwiper.destroyed || !levelSlides || levelSwiper.activeIndex !== 1) return;
  pendingChildFrame = childFrameFor(currentFrame());
  destroyHorizontal("child");
  const replacement = buildLevelSlide("child", pendingChildFrame);
  levelSlides.child.replaceWith(replacement);
  levelSlides.child = replacement;
  if (pendingChildFrame) initHorizontal("child", pendingChildFrame, { interactive: false });
  levelSwiper.allowSlideNext = Boolean(pendingChildFrame);
  levelSwiper.update();
}

function destroyLevelDeck() {
  horizontalSwipers.forEach(instance => instance?.destroy(true, true));
  horizontalSwipers.clear();
  levelSwiper?.destroy(true, true);
  levelSwiper = null;
  levelSlides = null;
  pendingChildFrame = null;
  levelTransitionLocked = false;
}

function commitLevelMove(instance) {
  if (levelTransitionLocked || instance.activeIndex === 1) return;
  levelTransitionLocked = true;
  if (instance.activeIndex === 2 && pendingChildFrame) {
    stack.push(pendingChildFrame);
    renderLevelDeck();
    return;
  }
  if (instance.activeIndex === 0 && stack.length > 1) {
    stack.pop();
    renderLevelDeck();
    return;
  }
  instance.slideTo(1, 180, false);
  levelTransitionLocked = false;
}

function renderLevelDeck() {
  destroyLevelDeck();
  const current = currentFrame();
  const parent = stack.length > 1 ? stack[stack.length - 2] : null;
  pendingChildFrame = childFrameFor(current);

  const shell = document.createElement("div");
  shell.className = "swiper v3-level-swiper";
  const wrapper = document.createElement("div");
  wrapper.className = "swiper-wrapper v3-level-wrapper";
  levelSlides = {
    parent: buildLevelSlide("parent", parent),
    current: buildLevelSlide("current", current),
    child: buildLevelSlide("child", pendingChildFrame),
  };
  wrapper.append(levelSlides.parent, levelSlides.current, levelSlides.child);
  shell.append(wrapper);
  stage.replaceChildren(shell);

  levelSwiper = new window.Swiper(shell, {
    direction: "vertical",
    nested: true,
    initialSlide: 1,
    slidesPerView: 1,
    speed: 320,
    threshold: 12,
    touchAngle: 45,
    resistanceRatio: 0.72,
    allowSlidePrev: Boolean(parent),
    allowSlideNext: Boolean(pendingChildFrame),
    preventClicks: true,
    preventClicksPropagation: true,
    touchStartPreventDefault: false,
    touchMoveStopPropagation: false,
    noSwiping: true,
    noSwipingSelector: "button,input,select,textarea,a,[contenteditable='true']",
    roundLengths: true,
    a11y: { enabled: true, containerMessage: "Navigation verticale entre les niveaux", slideLabelMessage: "Niveau {{index}} sur {{slidesLength}}" },
    on: {
      slideChangeTransitionEnd(instance) { commitLevelMove(instance); },
    },
  });

  if (parent) initHorizontal("parent", parent, { interactive: false });
  initHorizontal("current", current, { interactive: true });
  if (pendingChildFrame) initHorizontal("child", pendingChildFrame, { interactive: false });
  updateLocation();
}

function descend() {
  if (!pendingChildFrame) {
    if (status) status.textContent = "Cette carte ne contient pas encore de sous-cartes.";
    return;
  }
  levelSwiper?.slideNext();
}

function ascend() {
  if (stack.length <= 1) return;
  levelSwiper?.slidePrev();
}

spaceButtons.forEach(button => button.addEventListener("click", () => {
  const index = ROOT_ITEMS.findIndex(item => item.id === `space:${button.dataset.space}`);
  if (index < 0) return;
  stack.splice(1);
  stack[0].index = index;
  stack[0].activeSynthetic = false;
  renderLevelDeck();
}));

document.getElementById("v2-descend")?.addEventListener("click", descend);
document.getElementById("v2-ascend")?.addEventListener("click", ascend);
document.getElementById("v2-previous")?.addEventListener("click", () => horizontalSwipers.get("current")?.slidePrev());
document.getElementById("v2-next")?.addEventListener("click", () => horizontalSwipers.get("current")?.slideNext());
document.getElementById("v2-flip")?.addEventListener("click", () => {
  const currentSwiper = horizontalSwipers.get("current");
  const card = currentSwiper?.slides[currentSwiper.activeIndex]?.querySelector(".v2-card");
  if (card) card.dataset.flipped = card.dataset.flipped === "true" ? "false" : "true";
});

stack.push({ id: "root", title: "Pantheon", items: ROOT_ITEMS, index: 0, activeSynthetic: false, canCreate: false, rootSpace: "pantheon" });
renderLevelDeck();
