(() => {
  "use strict";

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

    const { ensureSwiper } = await import("./navigation/swiper_loader.js");
    const swiperReady = await ensureSwiper();
    if (swiperReady) await import("./live_collection_adapter.js");
    const scripts = [
      "shell_controls.js",
      "structured_interface.js",
      "context_resolver.js",
      "agency_data_binding.js",
      "spatial_navigation.js",
      "projection/cockpit_projection.js",
      "interactions/interaction_policy.js",
      "project_claim_view_adapter.js",
      "information_view_adapter.js",
      "context/context_selection.js",
      "handoff/handoff_lifecycle.js",
      "handoff/handoff_send.js",
      "actions/card_actions.js",
      "actions/change_candidate_actions.js",
      "schema_editor.js",
      "contacts_editor.js",
      "information_create.js",
      "interactions/card_interactions.js",
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
