(() => {
  "use strict";

  if (typeof window.Swiper !== "function") return;

  const stage = document.getElementById("v2-stage");
  if (!stage) return;

  const mobileMedia = window.matchMedia("(max-width: 620px)");
  const nativeReplaceChildren = stage.replaceChildren.bind(stage);
  const nativeAppend = stage.append.bind(stage);
  const nativeAppendChild = stage.appendChild.bind(stage);

  let shell = null;
  let wrapper = null;
  let slides = null;
  let swiper = null;
  let latestNodes = [];
  let currentNode = null;
  let previousProjection = null;
  let nextProjection = null;
  let rendererClearedStage = false;
  let pendingClearToken = 0;
  let navigationLocked = false;
  let userGestureActive = false;
  let pendingDirection = 0;
  let navigationTimeout = 0;
  let refreshFrame = 0;

  function cardIdentity(node) {
    if (!(node instanceof Element)) return "";
    const card = node.matches(".v2-card") ? node : node.querySelector(".v2-card");
    if (!card) return "";
    return card.dataset.entityId
      || card.getAttribute("data-card-id")
      || card.querySelector("[data-entity-id]")?.dataset.entityId
      || card.querySelector("h1,h2,h3,.v2-card-title")?.textContent?.trim()
      || "";
  }

  function inertPreview(node) {
    if (!node) return null;
    const clone = node.cloneNode(true);
    clone.removeAttribute?.("id");
    clone.removeAttribute?.("data-v3-flip-bound");
    clone.removeAttribute?.("data-flipped");
    clone.querySelectorAll?.("[id]").forEach(item => item.removeAttribute("id"));
    clone.querySelectorAll?.("[data-v3-flip-bound],[data-flipped]").forEach(item => {
      item.removeAttribute("data-v3-flip-bound");
      item.removeAttribute("data-flipped");
    });
    clone.querySelectorAll?.("button,input,select,textarea,a,[tabindex]").forEach(item => {
      item.setAttribute("tabindex", "-1");
      if ("disabled" in item) item.disabled = true;
    });
    return clone;
  }

  function createPlaceholder() {
    const placeholder = document.createElement("div");
    placeholder.className = "v3-stack-placeholder";
    placeholder.setAttribute("aria-hidden", "true");
    return placeholder;
  }

  function createCardShell(node) {
    const cardShell = document.createElement("div");
    cardShell.className = "v3-card-shell";
    cardShell.append(createPlaceholder(), createPlaceholder());
    if (node) cardShell.prepend(node);
    return cardShell;
  }

  function createSlide(role) {
    const slide = document.createElement("div");
    slide.className = `swiper-slide v2-swiper-slide v3-swiper-slide v3-swiper-slide--${role}`;
    slide.dataset.swiperRole = role;
    if (role !== "current") {
      slide.setAttribute("aria-hidden", "true");
      slide.inert = true;
    }
    return slide;
  }

  function createActionCard() {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "v2-swiper-create-card swiper-no-swiping";
    button.setAttribute("aria-label", "Ajouter un nouvel élément");
    button.innerHTML = '<span class="v2-swiper-create-mark">+</span><span class="v2-swiper-create-copy"><strong>Nouvel élément</strong><small>Créer dans la collection courante</small></span>';
    button.addEventListener("click", () => {
      if (window.PantheonInformationCreate?.open) {
        try {
          window.PantheonInformationCreate.open();
          return;
        } catch (error) {
          window.alert(error.message || String(error));
          return;
        }
      }
      stage.dispatchEvent(new CustomEvent("pantheon:create-requested", { bubbles: true }));
    });
    return button;
  }

  function createShell() {
    if (shell?.isConnected) return;

    shell = document.createElement("div");
    shell.className = "swiper v2-swiper v3-swiper";
    shell.setAttribute("role", "region");
    shell.setAttribute("aria-label", "Navigation horizontale entre les cartes sœurs");
    shell.setAttribute("aria-roledescription", "carrousel");

    wrapper = document.createElement("div");
    wrapper.className = "swiper-wrapper v2-swiper-wrapper";

    slides = {
      previous: createSlide("previous"),
      current: createSlide("current"),
      next: createSlide("next"),
    };

    wrapper.append(slides.previous, slides.current, slides.next);
    shell.append(wrapper);
    nativeReplaceChildren(shell);
  }

  function restoreCurrentSlide(speed = 0) {
    if (!swiper || swiper.destroyed) return;
    swiper.slideTo(1, speed, false);
  }

  function finishNavigation() {
    window.clearTimeout(navigationTimeout);
    navigationTimeout = 0;
    restoreCurrentSlide(0);
    navigationLocked = false;
    pendingDirection = 0;
    userGestureActive = false;
    delete stage.dataset.swiperNavigation;
    delete stage.dataset.swiperTransition;
  }

  function moveFromSwiper(instance) {
    if (!userGestureActive || navigationLocked || instance.activeIndex === 1) return;
    userGestureActive = false;

    const active = instance.slides[instance.activeIndex];
    if (active?.dataset?.swiperAction === "create") {
      restoreCurrentSlide(180);
      return;
    }

    pendingDirection = instance.activeIndex < 1 ? -1 : 1;
    const button = document.getElementById(pendingDirection < 0 ? "v2-previous" : "v2-next");

    navigationLocked = true;
    stage.dataset.swiperNavigation = "true";

    if (button && !button.disabled) {
      button.click();
      navigationTimeout = window.setTimeout(finishNavigation, 900);
      return;
    }

    restoreCurrentSlide(180);
    navigationTimeout = window.setTimeout(finishNavigation, 200);
  }

  function initSwiper() {
    if (swiper || !shell?.isConnected) return;

    swiper = new window.Swiper(shell, {
      init: false,
      initialSlide: 1,
      runCallbacksOnInit: false,
      slidesPerView: 1,
      speed: 300,
      threshold: 12,
      resistance: true,
      resistanceRatio: 0.72,
      watchOverflow: false,
      allowTouchMove: true,
      preventInteractionOnTransition: true,
      preventClicks: true,
      preventClicksPropagation: true,
      touchStartPreventDefault: false,
      touchMoveStopPropagation: true,
      noSwiping: true,
      noSwipingSelector: "button,input,select,textarea,a,[contenteditable='true']",
      observer: false,
      observeParents: false,
      observeSlideChildren: false,
      resizeObserver: true,
      roundLengths: true,
      keyboard: { enabled: false },
      a11y: {
        enabled: true,
        containerMessage: "Navigation horizontale entre les cartes sœurs",
        slideLabelMessage: "Carte {{index}} sur {{slidesLength}}",
      },
      on: {
        init() {
          restoreCurrentSlide(0);
        },
        touchStart() {
          if (!navigationLocked) userGestureActive = true;
        },
        touchEnd(instance) {
          if (instance.activeIndex === 1 && !instance.animating) userGestureActive = false;
        },
        slideChangeTransitionStart() {
          stage.dataset.swiperTransition = "true";
        },
        slideChangeTransitionEnd(instance) {
          delete stage.dataset.swiperTransition;
          moveFromSwiper(instance);
        },
      },
    });

    swiper.init();
  }

  function replaceSlideContent(slide, node) {
    const existingIdentity = cardIdentity(slide.firstElementChild);
    const nextIdentity = cardIdentity(node);
    if (existingIdentity && nextIdentity && existingIdentity === nextIdentity) return false;
    slide.replaceChildren(createCardShell(node));
    return true;
  }

  function scheduleSwiperRefresh() {
    if (!swiper || swiper.destroyed) return;
    window.cancelAnimationFrame(refreshFrame);
    refreshFrame = window.requestAnimationFrame(() => {
      refreshFrame = 0;
      if (!swiper || swiper.destroyed) return;
      swiper.update();
      restoreCurrentSlide(0);
    });
  }

  function updateMobile(node) {
    createShell();

    const previousButton = document.getElementById("v2-previous");
    if (currentNode && cardIdentity(currentNode) !== cardIdentity(node)) {
      if (pendingDirection > 0) previousProjection = inertPreview(currentNode);
      if (pendingDirection < 0) nextProjection = inertPreview(currentNode);
    }
    currentNode = node;

    slides.previous.dataset.swiperAction = previousButton?.disabled ? "create" : "";
    const changed = [
      replaceSlideContent(slides.previous, previousButton?.disabled ? createActionCard() : (previousProjection || inertPreview(node))),
      replaceSlideContent(slides.current, node),
      replaceSlideContent(slides.next, nextProjection || inertPreview(node)),
    ].some(Boolean);

    if (!swiper) initSwiper();
    else if (changed) scheduleSwiperRefresh();

    if (navigationLocked) finishNavigation();
  }

  function destroyProjection() {
    window.clearTimeout(navigationTimeout);
    window.cancelAnimationFrame(refreshFrame);
    navigationTimeout = 0;
    refreshFrame = 0;
    swiper?.destroy(true, true);
    swiper = null;
    shell = null;
    wrapper = null;
    slides = null;
    latestNodes = [];
    currentNode = null;
    previousProjection = null;
    nextProjection = null;
    userGestureActive = false;
    navigationLocked = false;
    pendingDirection = 0;
    delete stage.dataset.swiperNavigation;
    delete stage.dataset.swiperTransition;
  }

  function mount(nodes) {
    pendingClearToken += 1;
    rendererClearedStage = false;
    latestNodes = nodes;

    const node = nodes.find(item => item instanceof Node) || null;
    if (!node || node.classList?.contains("v2-empty")) {
      destroyProjection();
      nativeReplaceChildren(...nodes);
      return;
    }

    if (mobileMedia.matches) {
      updateMobile(node);
      return;
    }

    destroyProjection();
    latestNodes = nodes;
    const grid = document.createElement("div");
    grid.className = "v2-card-grid";
    const gridWrapper = document.createElement("div");
    gridWrapper.className = "v2-card-grid-wrapper";
    gridWrapper.append(createCardShell(node));
    grid.append(gridWrapper);
    nativeReplaceChildren(grid);
  }

  function scheduleConfirmedClear() {
    const token = ++pendingClearToken;
    requestAnimationFrame(() => requestAnimationFrame(() => {
      if (!rendererClearedStage || token !== pendingClearToken) return;
      destroyProjection();
      nativeReplaceChildren();
    }));
  }

  stage.replaceChildren = (...nodes) => {
    rendererClearedStage = nodes.length === 0;
    if (rendererClearedStage) {
      scheduleConfirmedClear();
      return;
    }
    mount(nodes);
  };

  stage.append = (...nodes) => {
    if (rendererClearedStage) {
      rendererClearedStage = false;
      pendingClearToken += 1;
      mount(nodes);
      return;
    }
    nativeAppend(...nodes);
  };

  stage.appendChild = node => {
    if (rendererClearedStage) {
      rendererClearedStage = false;
      pendingClearToken += 1;
      mount([node]);
      return node;
    }
    return nativeAppendChild(node);
  };

  mobileMedia.addEventListener?.("change", () => {
    if (latestNodes.length) mount(latestNodes);
  });

  window.addEventListener("pagehide", destroyProjection, { once: true });
})();