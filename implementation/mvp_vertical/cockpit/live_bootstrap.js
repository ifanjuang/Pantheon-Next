(() => {
  "use strict";

  const SWIPER_VERSION = "14.0.7";

  function loadExternalScript(src) {
    return new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.crossOrigin = "anonymous";
      script.onload = () => resolve(true);
      script.onerror = () => reject(new Error(`Impossible de charger ${src}`));
      document.head.append(script);
    });
  }

  async function ensureSwiper() {
    if (typeof window.Swiper === "function") {
      document.documentElement.dataset.swiperReady = "true";
      document.documentElement.dataset.swiperVersion = SWIPER_VERSION;
      return true;
    }

    const candidates = [
      `https://cdn.jsdelivr.net/npm/swiper@${SWIPER_VERSION}/swiper-bundle.min.js`,
      `https://unpkg.com/swiper@${SWIPER_VERSION}/swiper-bundle.min.js`,
    ];

    for (const src of candidates) {
      try {
        await loadExternalScript(src);
        if (typeof window.Swiper === "function") {
          document.documentElement.dataset.swiperReady = "true";
          document.documentElement.dataset.swiperVersion = SWIPER_VERSION;
          return true;
        }
      } catch (error) {
        console.warn(`Swiper indisponible depuis ${src}`, error);
      }
    }

    document.documentElement.dataset.swiperReady = "false";
    delete document.documentElement.dataset.swiperVersion;
    return false;
  }

  async function start() {
    const params = new URLSearchParams(window.location.search);
    const isDemo = params.get("mode") === "demo";

    window.PANTHEON_COCKPIT_DEMO = isDemo;
    document.documentElement.dataset.cockpitMode = isDemo ? "demo" : "live";

    function loadScript(src) {
      return new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = src;
        script.onload = resolve;
        script.onerror = () => reject(new Error(`Impossible de charger ${src}`));
        document.body.append(script);
      });
    }

    if (isDemo) await import("./demo_bootstrap.js");

    const swiperReady = await ensureSwiper();
    if (swiperReady) await import("./live_collection_adapter.js");
    const scripts = [
      "shell_controls.js",
      "structured_interface.js",
      "context_resolver.js",
      "agency_data_binding.js",
      "spatial_navigation.js",
      "v2_app_schema.js",
      "v2_interaction_policy.js",
      "project_claim_view_adapter.js",
      "information_view_adapter.js",
      "v2_context.js",
      "v2_handoff.js",
      "v2_hermes_send.js",
      "v2_actions.js",
      "v2_candidate_actions.js",
      "schema_editor.js",
      "contacts_editor.js",
      "information_create.js",
      "v3/cockpit_v3.js",
    ];

    for (const src of scripts) await loadScript(src);

    if (isDemo && window.PantheonDemoBootstrap?.start) {
      await window.PantheonDemoBootstrap.start();
    }

    const network = document.getElementById("v2-network");
    if (network && window.matchMedia("(max-width: 620px)").matches && !swiperReady) {
      network.textContent = "navigation tactile simplifiée";
    }
  }

  start().catch(error => {
    console.error(error);
    document.documentElement.dataset.cockpitLoad = "failed";
    const network = document.getElementById("v2-network");
    if (network) network.textContent = "chargement impossible";
    const stage = document.getElementById("v2-stage");
    if (stage) {
      stage.replaceChildren();
      const message = document.createElement("p");
      message.className = "v2-empty";
      message.textContent = "Le Cockpit n’a pas pu être chargé. Rechargez la page.";
      stage.append(message);
    }
  });
})();
