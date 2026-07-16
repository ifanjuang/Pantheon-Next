(function () {
  "use strict";

  const SDK = window.__HERMES_PLUGIN_SDK__;
  const registry = window.__HERMES_PLUGINS__;
  if (!SDK || !registry) return;

  const React = SDK.React;
  const hooks = SDK.hooks;
  const C = SDK.components;

  const POLICY = Object.freeze({
    mem0: {
      label: "Mem0",
      category: "Memory",
      risk: "high",
      governance: "candidate",
      scope: "project",
      reason:
        "Optional long-term memory provider. Hermes owns the runtime; Pantheon only governs what may become durable memory.",
      constraints: [
        "Only one external Hermes memory provider can be selected at a time.",
        "Provider selection does not promote content into Pantheon canonical memory.",
        "Configuration and dependencies must be ready before selection.",
      ],
    },
    n8n: {
      label: "n8n",
      category: "Automation",
      risk: "high",
      governance: "candidate",
      scope: "sandbox",
      reason:
        "Useful for deterministic integrations and recurring workflows. It complements Hermes execution; it must not become a second reasoning or approval layer.",
      constraints: [
        "The official Hermes catalog enables eight read-mostly tools by default.",
        "activate_workflow, deactivate_workflow, and container_logs are excluded by default.",
        "Installation or Hermes enablement never authorizes a workflow for a task.",
      ],
    },
    "pantheon-policy": {
      label: "Pantheon policy wiki",
      category: "Governance MCP",
      risk: "low",
      governance: "active_support",
      scope: "read_only",
      reason:
        "Gives Hermes on-demand, source-aware explanations of Pantheon structure and the reasons behind it.",
      constraints: [
        "Only list_sources, read_doctrine, and explain_governance_structure should be exposed.",
        "The Pantheon checkout must be mounted read-only.",
        "MCP sampling, prompts, and resources stay disabled.",
      ],
    },
    langgraph: {
      label: "LangGraph",
      category: "External runtime",
      risk: "critical",
      governance: "candidate",
      scope: "sandbox",
      reason:
        "A possible Hermes-side runtime for interruptible graphs. It is not the Pantheon workflow engine.",
      constraints: [
        "A native Hermes adapter and a scoped Task Contract are required before use.",
        "Graph state is runtime state, not evidence or canonical memory.",
        "No automatic install or activation is offered here.",
      ],
    },
    memvid: {
      label: "Memvid",
      category: "External memory candidate",
      risk: "high",
      governance: "watch",
      scope: "none",
      reason:
        "Interesting external memory technology, but no native Hermes memory-provider adapter is visible in the audited APIs.",
      constraints: [
        "No activation action is available until a reviewed Hermes adapter exists.",
        "Detection would not imply adoption or memory authority.",
      ],
    },
  });

  const N8N_DEFAULT_TOOLS = Object.freeze([
    "health",
    "list_workflows",
    "get_workflow",
    "find_workflows",
    "list_executions",
    "get_execution",
    "recent_failures",
    "export_workflow",
  ]);
  const N8N_WITHHELD_TOOLS = Object.freeze([
    "activate_workflow",
    "deactivate_workflow",
    "container_logs",
  ]);

  const EXTERNAL_CANDIDATES = Object.freeze([
    { id: "langgraph", aliases: ["langgraph", "langgraph-agent-stack"] },
    { id: "memvid", aliases: ["memvid"] },
  ]);

  const NIGHT_OPERATIONS = Object.freeze([
    {
      id: "backup_preflight",
      label: "Backup and restore preflight",
      jobName: "pantheon-night:backup-preflight",
      order: 10,
      schedule: "30 0 * * *",
      scheduleLabel: "00:30 every day",
      cadence: "daily trial",
      trialRuns: 7,
      risk: "medium",
      effectClass: "durable backup write",
      executionMode: "reviewed script only",
      maxRuntimeMinutes: 30,
      reason: "Verify a scoped backup artifact and restore posture before heavier night work starts.",
      prerequisites: [
        "Exact source paths and backup destination are visible.",
        "Retention, free space, and the restore command are reviewed.",
      ],
      outputs: ["backup receipt", "checksum report", "restore-readiness report candidate"],
      forbidden: ["source deletion", "automatic retention purge", "success without a verified artifact"],
    },
    {
      id: "pdf_ingestion_vectorization",
      label: "PDF ingestion and scoped vectorization",
      jobName: "pantheon-night:pdf-ingestion-vectorization",
      order: 20,
      schedule: "0 1 * * *",
      scheduleLabel: "01:00 every day",
      cadence: "daily trial",
      trialRuns: 7,
      risk: "high",
      effectClass: "scoped knowledge and index write",
      executionMode: "reviewed external ingestion adapter",
      maxRuntimeMinutes: 90,
      reason: "Prepare traceable Markdown, chunks, quality reports, and a scoped retrieval index without treating indexed content as evidence.",
      prerequisites: [
        "Input, output, project, and vector namespaces are explicit.",
        "Converter and embedding model versions are pinned; originals remain immutable.",
      ],
      outputs: ["ingestion manifest candidate", "source-linked chunks", "quality report", "scoped index receipt"],
      forbidden: ["indexed means evidence", "retrieved means truth", "automatic general-memory promotion"],
    },
    {
      id: "retrieval_quality_review",
      label: "Retrieval and index quality review",
      jobName: "pantheon-night:retrieval-quality-review",
      order: 30,
      schedule: "45 2 * * *",
      scheduleLabel: "02:45 every day",
      cadence: "daily trial",
      trialRuns: 7,
      risk: "medium",
      effectClass: "read-only quality analysis",
      executionMode: "bounded agent review",
      maxRuntimeMinutes: 45,
      reason: "Check missing, duplicate, stale, and poorly retrieved chunks after a completed ingestion receipt.",
      prerequisites: [
        "The preceding ingestion receipt exists or the run exits before inference.",
        "Representative scoped retrieval questions and trace fields are reviewed.",
      ],
      outputs: ["missing-chunk report candidate", "duplicate or stale-index report", "retrieval smoke-test report"],
      forbidden: ["source mutation", "automatic reindex", "quality score means proof"],
    },
    {
      id: "memory_consolidation_review",
      label: "Memory consolidation review",
      jobName: "pantheon-night:memory-consolidation-review",
      order: 40,
      schedule: "45 3 * * 0",
      scheduleLabel: "03:45 every Sunday",
      cadence: "weekly trial",
      trialRuns: 4,
      risk: "high",
      effectClass: "read-only memory candidate analysis",
      executionMode: "bounded agent review",
      maxRuntimeMinutes: 60,
      reason: "Propose duplicate, stale, superseded, and conflicting memory candidates for human review.",
      prerequisites: [
        "Exactly one Hermes memory provider and its scope are explicit.",
        "Project and general memory remain separate; durable claims retain sources.",
      ],
      outputs: ["duplicate candidate list", "stale or superseded candidate list", "conflict candidate list"],
      forbidden: ["memory deletion", "automatic merge", "automatic canonicalization or promotion"],
    },
    {
      id: "contradiction_drift_review",
      label: "Contradiction and governance-drift review",
      jobName: "pantheon-night:contradiction-drift-review",
      order: 50,
      schedule: "0 5 * * *",
      scheduleLabel: "05:00 every day",
      cadence: "daily trial",
      trialRuns: 7,
      risk: "medium",
      effectClass: "read-only governance analysis",
      executionMode: "bounded agent review",
      maxRuntimeMinutes: 60,
      reason: "Surface contradictions, source drift, status ambiguity, and decisions that need a human without resolving them automatically.",
      prerequisites: [
        "The Pantheon policy MCP is reachable with only its three read-only wiki tools.",
        "Repository and knowledge sources are read-only and the comparison baseline is explicit.",
      ],
      outputs: ["contradiction ledger candidate", "governance-drift review candidate", "Evidence Pack Candidate"],
      forbidden: ["automatic contradiction resolution", "doctrine or repository mutation", "automatic status promotion"],
    },
    {
      id: "morning_decision_digest",
      label: "Morning decision digest",
      jobName: "pantheon-night:morning-decision-digest",
      order: 60,
      schedule: "15 6 * * *",
      scheduleLabel: "06:15 every day",
      cadence: "daily trial",
      trialRuns: 7,
      risk: "low",
      effectClass: "local candidate summary",
      executionMode: "bounded agent review",
      maxRuntimeMinutes: 20,
      reason: "Summarize completed local outputs, failed runs, and decisions required from the operator.",
      prerequisites: [
        "Only completed local outputs from preceding operations are included.",
        "Failures and missing or contradictory upstream results stay visible.",
      ],
      outputs: ["local morning status candidate", "failed-run list", "operator decision list"],
      forbidden: ["external delivery without approval", "approval by summary", "hiding upstream failures"],
    },
  ]);

  function asArray(value) {
    return Array.isArray(value) ? value : [];
  }

  function cleanId(value) {
    return String(value || "").trim().toLowerCase();
  }

  function defaultPolicy(item) {
    return {
      label: item.name || item.id,
      category: item.kind === "mcp" ? "MCP" : item.kind === "plugin" ? "Plugin" : "Module",
      risk: "unassessed",
      governance: "detected",
      scope: "none",
      reason:
        "Observed through Hermes. No Pantheon-specific activation policy is encoded for this capability yet.",
      constraints: ["Hermes enablement does not establish task authorization."],
    };
  }

  function policyFor(item) {
    return POLICY[cleanId(item.id)] || defaultPolicy(item);
  }

  function normalizeMemory(payload) {
    const active = cleanId(payload && payload.active);
    return asArray(payload && payload.providers).map(function (provider) {
      const id = cleanId(provider.name);
      const status = String(provider.status || "unknown");
      const item = {
        id: id,
        name: provider.name || id,
        kind: "memory",
        description: provider.description || "Hermes memory provider.",
        source: "Hermes memory registry",
        listed: true,
        detected: status !== "missing",
        installed: status !== "missing",
        configured: typeof provider.configured === "boolean" ? provider.configured : null,
        enabled: active === id,
        reachable: null,
        health: "unknown",
        nativeStatus: status,
        setup: provider.setup || {},
      };
      item.policy = policyFor(item);
      return item;
    });
  }

  function normalizeMcps(catalogPayload, serverPayload, probes) {
    const catalog = asArray(catalogPayload && catalogPayload.entries);
    const servers = asArray(serverPayload && serverPayload.servers);
    const serverByName = new Map();
    servers.forEach(function (server) {
      serverByName.set(cleanId(server.name), server);
    });

    const rows = [];
    catalog.forEach(function (entry) {
      const id = cleanId(entry.name);
      const server = serverByName.get(id);
      const requiredEnv = asArray(entry.required_env);
      const probe = probes && probes[id];
      const installed = Boolean(entry.installed || server);
      const item = {
        id: id,
        name: entry.name || id,
        kind: "mcp",
        description: entry.description || "Hermes MCP catalog entry.",
        source: entry.source || "Hermes MCP catalog",
        listed: true,
        detected: installed,
        installed: installed,
        configured: requiredEnv.length ? null : installed ? true : null,
        enabled: server ? server.enabled !== false : Boolean(entry.enabled),
        reachable: probe ? Boolean(probe.ok) : null,
        health: probe ? (probe.ok ? "healthy" : "unhealthy") : "unknown",
        nativeStatus: installed ? "installed" : "catalog_only",
        requiredEnv: requiredEnv,
        needsInstall: Boolean(entry.needs_install),
        command: entry.command || (server && server.command) || null,
        args: asArray(entry.args || (server && server.args)),
        url: entry.url || (server && server.url) || null,
        installUrl: entry.install_url || null,
        installRef: entry.install_ref || null,
        bootstrap: asArray(entry.bootstrap),
        defaultEnabled: asArray(entry.default_enabled),
        selectedTools: server && Array.isArray(server.tools) ? server.tools : null,
        postInstall: entry.post_install || "",
        probe: probe || null,
        catalogEntry: true,
      };
      item.policy = policyFor(item);
      rows.push(item);
      serverByName.delete(id);
    });

    serverByName.forEach(function (server, id) {
      const probe = probes && probes[id];
      const item = {
        id: id,
        name: server.name || id,
        kind: "mcp",
        description: "MCP server configured directly in Hermes.",
        source: server.url || server.command || "Hermes configuration",
        listed: true,
        detected: true,
        installed: true,
        configured: null,
        enabled: server.enabled !== false,
        reachable: probe ? Boolean(probe.ok) : null,
        health: probe ? (probe.ok ? "healthy" : "unhealthy") : "unknown",
        nativeStatus: "configured",
        requiredEnv: [],
        needsInstall: false,
        command: server.command || null,
        args: asArray(server.args),
        url: server.url || null,
        installUrl: null,
        installRef: null,
        bootstrap: [],
        defaultEnabled: [],
        selectedTools: Array.isArray(server.tools) ? server.tools : null,
        postInstall: "",
        probe: probe || null,
        catalogEntry: false,
      };
      item.policy = policyFor(item);
      rows.push(item);
    });

    return rows.sort(function (a, b) {
      return a.name.localeCompare(b.name);
    });
  }

  function normalizePlugins(hubPayload, memoryNames) {
    return asArray(hubPayload && hubPayload.plugins)
      .filter(function (plugin) {
        const id = cleanId(plugin.name);
        return id !== "pantheon-modules" && !memoryNames.has(id);
      })
      .map(function (plugin) {
        const item = {
          id: cleanId(plugin.name),
          name: plugin.name,
          kind: "plugin",
          description: plugin.description || "Hermes plugin.",
          source: plugin.source || "Hermes plugin registry",
          listed: true,
          detected: true,
          installed: true,
          configured: null,
          enabled: plugin.runtime_status === "enabled",
          reachable: null,
          health: "unknown",
          nativeStatus: plugin.runtime_status || "unknown",
          version: plugin.version || "",
          authRequired: Boolean(plugin.auth_required),
        };
        item.policy = policyFor(item);
        return item;
      })
      .sort(function (a, b) {
        return a.name.localeCompare(b.name);
      });
  }

  function normalizeExternal(observedItems) {
    return EXTERNAL_CANDIDATES.map(function (candidate) {
      const matches = observedItems.filter(function (item) {
        const haystack = cleanId(item.id + " " + item.name + " " + item.description);
        return candidate.aliases.some(function (alias) {
          return haystack.indexOf(alias) !== -1;
        });
      });
      const policy = POLICY[candidate.id];
      return {
        id: candidate.id,
        name: policy.label,
        kind: "candidate",
        description: policy.reason,
        source: matches.length ? "Observed through Hermes APIs" : "Pantheon candidate registry",
        listed: true,
        detected: matches.length > 0,
        installed: matches.length ? matches.some(function (item) { return item.installed; }) : false,
        configured: null,
        enabled: matches.length ? matches.some(function (item) { return item.enabled; }) : false,
        reachable: null,
        health: "unknown",
        nativeStatus: matches.length ? "observed" : "no_native_adapter_observed",
        policy: policy,
      };
    });
  }

  function normalizeInventory(payloads, probes) {
    const memory = normalizeMemory(payloads.memory || {});
    const memoryNames = new Set(memory.map(function (item) { return item.id; }));
    const mcps = normalizeMcps(payloads.catalog || {}, payloads.servers || {}, probes || {});
    const plugins = normalizePlugins(payloads.hub || {}, memoryNames);
    const candidates = normalizeExternal(memory.concat(mcps, plugins));
    return { memory: memory, mcps: mcps, plugins: plugins, candidates: candidates };
  }

  function normalizeOperations(cronPayload) {
    const jobs = Array.isArray(cronPayload)
      ? cronPayload
      : asArray(cronPayload && cronPayload.jobs);

    return NIGHT_OPERATIONS.map(function (operation) {
      const matches = jobs.filter(function (job) {
        return cleanId(job && job.name) === cleanId(operation.jobName);
      });
      const job = matches.length === 1 ? matches[0] : null;
      const repeatTimes = job && job.repeat ? job.repeat.times : null;
      const bounded = typeof repeatTimes === "number" && repeatTimes > 0;
      const enabled = job ? job.enabled !== false && String(job.state || "scheduled") !== "paused" : false;
      const lastStatus = job ? String(job.last_status || "never_run") : "not_scheduled";
      const governance = matches.length > 1
        ? "blocked_ambiguous"
        : job && !bounded
          ? "blocked_unbounded"
          : job
            ? "bounded_trial_observed"
            : "operator_review_required";

      return Object.assign({}, operation, {
        kind: "operation",
        listed: true,
        detected: matches.length > 0,
        jobCount: matches.length,
        job: job,
        bounded: job ? bounded : null,
        enabled: enabled,
        profile: job ? (job.profile_name || job.profile || "unknown") : "not selected",
        scheduleObserved: job ? (job.schedule_display || (job.schedule && job.schedule.display) || "unknown") : "not scheduled",
        nextRunAt: job ? (job.next_run_at || null) : null,
        lastRunAt: job ? (job.last_run_at || null) : null,
        lastStatus: lastStatus,
        health: lastStatus === "ok" ? "healthy" : lastStatus === "error" ? "unhealthy" : "unknown",
        governance: governance,
        policy: {
          label: operation.label,
          category: "Night operation",
          risk: operation.risk,
          governance: governance,
          scope: "operator reviewed trial",
          reason: operation.reason,
          constraints: operation.forbidden,
        },
      });
    }).sort(function (a, b) { return a.order - b.order; });
  }

  function isSecretEnv(name) {
    return /(KEY|TOKEN|SECRET|PASSWORD|PASSCODE|CREDENTIAL)/i.test(String(name || ""));
  }

  function triLabel(value) {
    if (value === true) return "yes";
    if (value === false) return "no";
    return "unknown";
  }

  function triTone(value) {
    if (value === true) return "good";
    if (value === false) return "muted";
    return "unknown";
  }

  window.__PANTHEON_MODULES_TEST__ = Object.freeze({
    normalizeInventory: normalizeInventory,
    normalizeMemory: normalizeMemory,
    normalizeMcps: normalizeMcps,
    normalizePlugins: normalizePlugins,
    normalizeOperations: normalizeOperations,
    isSecretEnv: isSecretEnv,
    policy: POLICY,
    nightOperations: NIGHT_OPERATIONS,
    n8nDefaultTools: N8N_DEFAULT_TOOLS,
    n8nWithheldTools: N8N_WITHHELD_TOOLS,
  });

  function StateCell(props) {
    return React.createElement(
      "div",
      { className: "pm-state" },
      React.createElement("span", { className: "pm-state-label" }, props.label),
      React.createElement(
        "span",
        { className: "pm-state-value pm-tone-" + (props.tone || "unknown") },
        props.value,
      ),
    );
  }

  function StateGrid(props) {
    const item = props.item;
    const healthTone = item.health === "healthy" ? "good" : item.health === "unhealthy" ? "danger" : "unknown";
    return React.createElement(
      "div",
      { className: "pm-states", "aria-label": "Module states" },
      React.createElement(StateCell, { label: "Listed", value: triLabel(item.listed), tone: triTone(item.listed) }),
      React.createElement(StateCell, { label: "Detected", value: triLabel(item.detected), tone: triTone(item.detected) }),
      React.createElement(StateCell, { label: "Installed", value: triLabel(item.installed), tone: triTone(item.installed) }),
      React.createElement(StateCell, { label: "Configured", value: triLabel(item.configured), tone: triTone(item.configured) }),
      React.createElement(StateCell, { label: "Hermes enabled", value: triLabel(item.enabled), tone: triTone(item.enabled) }),
      React.createElement(StateCell, { label: "Reachable", value: triLabel(item.reachable), tone: triTone(item.reachable) }),
      React.createElement(StateCell, { label: "Health", value: item.health, tone: healthTone }),
      React.createElement(StateCell, { label: "Governance", value: item.policy.governance, tone: "policy" }),
      React.createElement(StateCell, { label: "Task use", value: "not established", tone: "danger" }),
    );
  }

  function PolicyBlock(props) {
    const policy = props.item.policy;
    return React.createElement(
      "details",
      { className: "pm-policy" },
      React.createElement("summary", null, "Why this placement"),
      React.createElement("p", null, policy.reason),
      React.createElement(
        "ul",
        null,
        policy.constraints.map(function (constraint) {
          return React.createElement("li", { key: constraint }, constraint);
        }),
      ),
    );
  }

  function McpTechnicalDetails(props) {
    const item = props.item;
    if (item.kind !== "mcp") return null;
    const defaults = item.id === "n8n" ? N8N_DEFAULT_TOOLS : item.defaultEnabled;
    return React.createElement(
      "details",
      { className: "pm-technical" },
      React.createElement("summary", null, "Hermes connection details"),
      React.createElement(
        "dl",
        null,
        React.createElement("dt", null, "Source"),
        React.createElement("dd", null, item.source || "unknown"),
        item.installRef && React.createElement("dt", null, "Pinned ref"),
        item.installRef && React.createElement("dd", { className: "pm-mono" }, item.installRef),
        item.command && React.createElement("dt", null, "Command"),
        item.command && React.createElement("dd", { className: "pm-mono" }, item.command),
        item.url && React.createElement("dt", null, "URL"),
        item.url && React.createElement("dd", { className: "pm-mono" }, item.url),
        defaults.length > 0 && React.createElement("dt", null, "Default tools"),
        defaults.length > 0 && React.createElement("dd", { className: "pm-mono" }, defaults.join(", ")),
        item.id === "n8n" && React.createElement("dt", null, "Excluded by default"),
        item.id === "n8n" && React.createElement("dd", { className: "pm-mono" }, N8N_WITHHELD_TOOLS.join(", ")),
      ),
      item.bootstrap.length > 0 && React.createElement(
        "div",
        { className: "pm-bootstrap" },
        React.createElement("strong", null, "Bootstrap to review"),
        item.bootstrap.map(function (command) {
          return React.createElement("code", { key: command }, command);
        }),
      ),
    );
  }

  function InstallForm(props) {
    const item = props.item;
    const values = props.values || {};
    return React.createElement(
      "div",
      { className: "pm-install-form" },
      React.createElement("strong", null, "Explicit Hermes install request"),
      item.requiredEnv.length === 0 && React.createElement(
        "p",
        null,
        "This catalog entry declares no required environment values.",
      ),
      item.requiredEnv.map(function (field) {
        return React.createElement(
          "label",
          { key: field.name, className: "pm-field" },
          React.createElement(
            "span",
            null,
            field.prompt || field.name,
            field.required === false ? " (optional)" : "",
          ),
          React.createElement(C.Input, {
            type: isSecretEnv(field.name) ? "password" : "text",
            autoComplete: "off",
            value: values[field.name] || "",
            placeholder: field.name,
            onChange: function (event) {
              props.onChange(field.name, event.target.value);
            },
          }),
        );
      }),
      React.createElement(
        "p",
        { className: "pm-secret-note" },
        "Values remain only in this form until submission. The plugin keeps no browser copy. Hermes persists submitted values through its native API.",
      ),
      React.createElement(
        "div",
        { className: "pm-actions" },
        React.createElement(C.Button, { onClick: props.onSubmit, disabled: props.busy }, props.busy ? "Submitting…" : "Install via Hermes"),
        React.createElement(C.Button, { variant: "outline", onClick: props.onCancel, disabled: props.busy }, "Cancel"),
      ),
    );
  }

  function ModuleActions(props) {
    const item = props.item;
    const busy = props.busy === item.kind + ":" + item.id;

    if (item.kind === "candidate") {
      return React.createElement("p", { className: "pm-no-action" }, "No native activation action is exposed for this candidate.");
    }

    if (item.kind === "memory") {
      if (item.nativeStatus !== "ready") {
        return React.createElement(
          "div",
          { className: "pm-actions" },
          React.createElement(C.Button, { variant: "outline", onClick: props.onOpenNativePlugins }, "Open native setup"),
        );
      }
      return React.createElement(
        "div",
        { className: "pm-actions" },
        React.createElement(
          C.Button,
          { onClick: function () { props.onMemory(item); }, disabled: busy },
          busy ? "Applying…" : item.enabled ? "Use built-in memory" : "Select in Hermes",
        ),
      );
    }

    if (item.kind === "plugin") {
      return React.createElement(
        "div",
        { className: "pm-actions" },
        React.createElement(
          C.Button,
          { variant: item.enabled ? "outline" : "default", onClick: function () { props.onPlugin(item); }, disabled: busy },
          busy ? "Applying…" : item.enabled ? "Disable in Hermes" : "Enable in Hermes",
        ),
      );
    }

    if (item.kind === "mcp") {
      if (!item.installed && item.catalogEntry) {
        return React.createElement(
          "div",
          { className: "pm-actions" },
          React.createElement(
            C.Button,
            { onClick: function () { props.onPrepareInstall(item); } },
            props.installTarget === item.id ? "Install form open" : "Prepare install",
          ),
        );
      }
      return React.createElement(
        "div",
        { className: "pm-actions" },
        React.createElement(C.Button, { variant: "outline", onClick: function () { props.onProbe(item); }, disabled: busy }, "Test connection"),
        React.createElement(
          C.Button,
          { variant: item.enabled ? "outline" : "default", onClick: function () { props.onMcpToggle(item); }, disabled: busy },
          busy ? "Applying…" : item.enabled ? "Disable in Hermes" : "Enable in Hermes",
        ),
      );
    }

    return null;
  }

  function ModuleCard(props) {
    const item = props.item;
    return React.createElement(
      C.Card,
      { className: "pm-card" },
      React.createElement(
        C.CardHeader,
        { className: "pm-card-header" },
        React.createElement(
          "div",
          { className: "pm-card-title-row" },
          React.createElement(
            "div",
            null,
            React.createElement(C.CardTitle, null, item.policy.label || item.name),
            React.createElement("p", { className: "pm-native-name" }, item.name !== item.policy.label ? item.name : item.source),
          ),
          React.createElement(
            "div",
            { className: "pm-badges" },
            React.createElement(C.Badge, { variant: "outline" }, item.policy.category),
            React.createElement(C.Badge, { variant: item.policy.risk === "low" ? "secondary" : "outline", className: "pm-risk-" + item.policy.risk }, "risk: " + item.policy.risk),
          ),
        ),
      ),
      React.createElement(
        C.CardContent,
        { className: "pm-card-content" },
        React.createElement("p", { className: "pm-description" }, item.description),
        React.createElement(StateGrid, { item: item }),
        React.createElement(
          "div",
          { className: "pm-native-status" },
          React.createElement("span", null, "Native status"),
          React.createElement("code", null, item.nativeStatus),
          React.createElement("span", null, "Policy scope"),
          React.createElement("code", null, item.policy.scope),
        ),
        item.authRequired && React.createElement("p", { className: "pm-warning" }, "Hermes reports that authentication is still required."),
        item.probe && !item.probe.ok && React.createElement("p", { className: "pm-warning" }, item.probe.error || "Connection test failed."),
        item.probe && item.probe.ok && React.createElement("p", { className: "pm-success" }, "Observed " + asArray(item.probe.tools).length + " MCP tools during the latest test."),
        React.createElement(PolicyBlock, { item: item }),
        React.createElement(McpTechnicalDetails, { item: item }),
        React.createElement(ModuleActions, Object.assign({}, props, { item: item })),
        props.installTarget === item.id && React.createElement(InstallForm, {
          item: item,
          values: props.envValues[item.id] || {},
          busy: props.busy === "mcp:" + item.id,
          onChange: function (name, value) { props.onEnvChange(item.id, name, value); },
          onSubmit: function () { props.onInstall(item); },
          onCancel: props.onCancelInstall,
        }),
      ),
    );
  }

  function OperationStateGrid(props) {
    const item = props.item;
    const healthTone = item.health === "healthy" ? "good" : item.health === "unhealthy" ? "danger" : "unknown";
    const boundedTone = item.bounded === true ? "good" : item.bounded === false ? "danger" : "unknown";
    return React.createElement(
      "div",
      { className: "pm-states", "aria-label": "Scheduled operation states" },
      React.createElement(StateCell, { label: "Catalog", value: "listed", tone: "good" }),
      React.createElement(StateCell, { label: "Cron job", value: item.detected ? (item.jobCount === 1 ? "observed" : "ambiguous") : "not observed", tone: item.jobCount === 1 ? "good" : item.jobCount > 1 ? "danger" : "muted" }),
      React.createElement(StateCell, { label: "Finite trial", value: triLabel(item.bounded), tone: boundedTone }),
      React.createElement(StateCell, { label: "Hermes enabled", value: item.detected ? triLabel(item.enabled) : "not scheduled", tone: item.detected ? triTone(item.enabled) : "muted" }),
      React.createElement(StateCell, { label: "Last result", value: item.lastStatus, tone: healthTone }),
      React.createElement(StateCell, { label: "Governance", value: item.governance, tone: item.governance.indexOf("blocked") === 0 ? "danger" : "policy" }),
    );
  }

  function OperationList(props) {
    if (!props.items.length) return null;
    return React.createElement(
      "div",
      { className: "pm-operation-list" },
      React.createElement("strong", null, props.label),
      React.createElement(
        "ul",
        null,
        props.items.map(function (item) {
          return React.createElement("li", { key: item }, item);
        }),
      ),
    );
  }

  function OperationCard(props) {
    const item = props.item;
    const repeat = item.job && item.job.repeat;
    const repeatDisplay = repeat && typeof repeat.times === "number"
      ? String(repeat.completed || 0) + "/" + String(repeat.times)
      : item.job ? "unbounded" : "not scheduled";
    return React.createElement(
      C.Card,
      { className: "pm-card pm-operation-card" },
      React.createElement(
        C.CardHeader,
        { className: "pm-card-header" },
        React.createElement(
          "div",
          { className: "pm-card-title-row" },
          React.createElement(
            "div",
            null,
            React.createElement(C.CardTitle, null, item.label),
            React.createElement("p", { className: "pm-native-name" }, item.jobName),
          ),
          React.createElement(
            "div",
            { className: "pm-badges" },
            React.createElement(C.Badge, { variant: "outline" }, item.cadence),
            React.createElement(C.Badge, { variant: item.risk === "low" ? "secondary" : "outline", className: "pm-risk-" + item.risk }, "risk: " + item.risk),
          ),
        ),
      ),
      React.createElement(
        C.CardContent,
        { className: "pm-card-content" },
        React.createElement("p", { className: "pm-description" }, item.reason),
        React.createElement(OperationStateGrid, { item: item }),
        React.createElement(
          "dl",
          { className: "pm-operation-meta" },
          React.createElement("dt", null, "Recommended"),
          React.createElement("dd", null, item.scheduleLabel + " (" + item.schedule + ")"),
          React.createElement("dt", null, "Timezone"),
          React.createElement("dd", { className: "pm-warning" }, "REQUIRED — Hermes host local time"),
          React.createElement("dt", null, "Trial limit"),
          React.createElement("dd", null, String(item.trialRuns) + " runs before review"),
          React.createElement("dt", null, "Max window"),
          React.createElement("dd", null, String(item.maxRuntimeMinutes) + " minutes (runtime enforcement required)"),
          React.createElement("dt", null, "Effect"),
          React.createElement("dd", null, item.effectClass),
          React.createElement("dt", null, "Mode"),
          React.createElement("dd", null, item.executionMode),
          React.createElement("dt", null, "Observed schedule"),
          React.createElement("dd", null, item.scheduleObserved),
          React.createElement("dt", null, "Profile"),
          React.createElement("dd", null, item.profile),
          React.createElement("dt", null, "Finite runs"),
          React.createElement("dd", null, repeatDisplay),
          item.nextRunAt && React.createElement("dt", null, "Next run"),
          item.nextRunAt && React.createElement("dd", { className: "pm-mono" }, item.nextRunAt),
          item.lastRunAt && React.createElement("dt", null, "Last run"),
          item.lastRunAt && React.createElement("dd", { className: "pm-mono" }, item.lastRunAt),
        ),
        item.jobCount > 1 && React.createElement("p", { className: "pm-warning" }, "Several jobs use this governed name. Resolve the ambiguity in native Cron before relying on any status."),
        item.job && item.bounded === false && React.createElement("p", { className: "pm-warning" }, "Unbounded recurrence observed. Pause it and recreate a finite trial through a reviewed native Hermes path."),
        !item.job && React.createElement("p", { className: "pm-no-action" }, "No matching Hermes Cron job is observed. The catalog entry is a proposal, not an active schedule."),
        React.createElement(
          "details",
          { className: "pm-policy" },
          React.createElement("summary", null, "Activation contract"),
          React.createElement(OperationList, { label: "Prerequisites", items: item.prerequisites }),
          React.createElement(OperationList, { label: "Allowed candidate outputs", items: item.outputs }),
          React.createElement(OperationList, { label: "Forbidden effects", items: item.forbidden }),
        ),
        React.createElement(
          "div",
          { className: "pm-actions" },
          React.createElement(C.Button, { variant: "outline", onClick: props.onOpenNativeCron }, "Open native Cron"),
        ),
      ),
    );
  }

  function callApi(name) {
    const fn = SDK.api && SDK.api[name];
    if (typeof fn !== "function") {
      return Promise.reject(new Error("Hermes API method unavailable: " + name));
    }
    const args = Array.prototype.slice.call(arguments, 1);
    return Promise.resolve(fn.apply(SDK.api, args));
  }

  function PantheonModulesPage() {
    const useState = hooks.useState;
    const useEffect = hooks.useEffect;
    const useCallback = hooks.useCallback;
    const useMemo = hooks.useMemo;
    const [payloads, setPayloads] = useState({ memory: {}, catalog: {}, servers: {}, hub: {}, jobs: [] });
    const [probes, setProbes] = useState({});
    const [loading, setLoading] = useState(true);
    const [errors, setErrors] = useState([]);
    const [message, setMessage] = useState(null);
    const [busy, setBusy] = useState("");
    const [filter, setFilter] = useState("all");
    const [query, setQuery] = useState("");
    const [installTarget, setInstallTarget] = useState("");
    const [envValues, setEnvValues] = useState({});

    const refresh = useCallback(function () {
      setLoading(true);
      const calls = [
        ["memory", "getMemory"],
        ["catalog", "getMcpCatalog"],
        ["servers", "getMcpServers"],
        ["hub", "getPluginsHub"],
        ["jobs", "getCronJobs", "all"],
      ];
      return Promise.allSettled(calls.map(function (entry) {
        return callApi.apply(null, [entry[1]].concat(entry.slice(2)));
      }))
        .then(function (results) {
          const next = { memory: {}, catalog: {}, servers: {}, hub: {}, jobs: [] };
          const nextErrors = [];
          results.forEach(function (result, index) {
            const key = calls[index][0];
            if (result.status === "fulfilled") next[key] = result.value || {};
            else nextErrors.push(key + ": " + String(result.reason && result.reason.message ? result.reason.message : result.reason));
          });
          setPayloads(next);
          setErrors(nextErrors);
        })
        .finally(function () { setLoading(false); });
    }, []);

    useEffect(function () { refresh(); }, [refresh]);

    const inventory = useMemo(function () {
      return normalizeInventory(payloads, probes);
    }, [payloads, probes]);

    const operations = useMemo(function () {
      return normalizeOperations(payloads.jobs);
    }, [payloads.jobs]);

    const sections = [
      { id: "memory", label: "Memory", items: inventory.memory },
      { id: "mcp", label: "MCP & automation", items: inventory.mcps },
      { id: "plugins", label: "Hermes plugins", items: inventory.plugins },
      { id: "candidates", label: "External candidates", items: inventory.candidates },
    ];

    const visibleSections = sections.map(function (section) {
      const needle = cleanId(query);
      const items = section.items.filter(function (item) {
        if (filter !== "all" && filter !== section.id) return false;
        if (!needle) return true;
        const haystack = cleanId(item.name + " " + item.description + " " + item.policy.category + " " + item.policy.reason);
        return haystack.indexOf(needle) !== -1;
      });
      return { id: section.id, label: section.label, items: items };
    }).filter(function (section) { return section.items.length > 0; });

    const operationNeedle = cleanId(query);
    const visibleOperations = filter !== "all" && filter !== "operations"
      ? []
      : operations.filter(function (item) {
          if (!operationNeedle) return true;
          const haystack = cleanId(
            item.label + " " + item.jobName + " " + item.reason + " " +
            item.effectClass + " " + item.governance,
          );
          return haystack.indexOf(operationNeedle) !== -1;
        });

    function runMutation(key, successText, action) {
      setBusy(key);
      setMessage(null);
      return Promise.resolve()
        .then(action)
        .then(function (result) {
          setMessage({ tone: "success", text: typeof successText === "function" ? successText(result) : successText });
          return refresh().then(function () { return result; });
        })
        .catch(function (error) {
          setMessage({ tone: "error", text: String(error && error.message ? error.message : error) });
          return null;
        })
        .finally(function () { setBusy(""); });
    }

    function handleMemory(item) {
      const next = item.enabled ? "" : item.id;
      const action = item.enabled ? "return to Hermes built-in memory" : "select " + item.name + " as the exclusive external memory provider";
      if (!window.confirm("Confirm: " + action + ". This changes Hermes configuration but does not promote or authorize Pantheon memory.")) return;
      runMutation("memory:" + item.id, "Hermes memory provider updated. Start a fresh session before relying on the change.", function () {
        return callApi("setMemoryProvider", next);
      });
    }

    function handlePlugin(item) {
      const verb = item.enabled ? "disable" : "enable";
      if (!window.confirm("Confirm: " + verb + " Hermes plugin '" + item.name + "'. Runtime enablement does not establish Pantheon governance activation or task authorization.")) return;
      runMutation("plugin:" + item.id, "Hermes plugin state updated. A fresh session may be required.", function () {
        return callApi(item.enabled ? "disableAgentPlugin" : "enableAgentPlugin", item.name);
      });
    }

    function handleMcpToggle(item) {
      const next = !item.enabled;
      if (!window.confirm("Confirm: " + (next ? "enable" : "disable") + " MCP server '" + item.name + "' in Hermes. This takes effect for new sessions and does not authorize its tools for a task.")) return;
      runMutation("mcp:" + item.id, "Hermes MCP state updated. Start a fresh session to load the new tool surface.", function () {
        return callApi("setMcpServerEnabled", item.name, next);
      });
    }

    function handleProbe(item) {
      if (!window.confirm("Run a Hermes connectivity test for '" + item.name + "'? The probe may start the MCP process and contact its configured service.")) return;
      setBusy("mcp:" + item.id);
      setMessage(null);
      callApi("testMcpServer", item.name)
        .then(function (result) {
          setProbes(function (current) {
            return Object.assign({}, current, { [item.id]: result || { ok: false, error: "Empty response", tools: [] } });
          });
          setMessage({ tone: result && result.ok ? "success" : "error", text: result && result.ok ? "Connection observed. This is liveness evidence, not task authorization." : (result && result.error) || "Connection test failed." });
        })
        .catch(function (error) {
          setProbes(function (current) {
            return Object.assign({}, current, { [item.id]: { ok: false, error: String(error.message || error), tools: [] } });
          });
          setMessage({ tone: "error", text: String(error.message || error) });
        })
        .finally(function () { setBusy(""); });
    }

    function handleEnvChange(id, name, value) {
      setEnvValues(function (current) {
        const nextForItem = Object.assign({}, current[id] || {}, { [name]: value });
        return Object.assign({}, current, { [id]: nextForItem });
      });
    }

    function handleInstall(item) {
      const values = envValues[item.id] || {};
      const missing = item.requiredEnv.filter(function (field) {
        return field.required !== false && !String(values[field.name] || "").trim();
      });
      if (missing.length) {
        setMessage({ tone: "error", text: "Missing required values: " + missing.map(function (field) { return field.name; }).join(", ") });
        return;
      }
      const installEffect = item.needsInstall
        ? "Hermes will clone the pinned source, run the displayed bootstrap commands, persist supplied environment values, and enable the MCP when installation completes."
        : "Hermes will persist supplied environment values and add this MCP to its configuration.";
      if (!window.confirm("Confirm installation of '" + item.name + "'. " + installEffect + " This is a privileged configuration action, not task authorization.")) return;
      runMutation(
        "mcp:" + item.id,
        function (result) {
          return result && result.background
            ? "Hermes started the background install. Refresh after the native action completes, then test the connection."
            : "Hermes installed the MCP. Test it before relying on the connection.";
        },
        function () { return callApi("installMcpCatalogEntry", item.name, values, true); },
      ).then(function (result) {
        if (!result) return;
        setEnvValues(function (current) {
          const next = Object.assign({}, current);
          delete next[item.id];
          return next;
        });
        setInstallTarget("");
      });
    }

    const actionProps = {
      busy: busy,
      installTarget: installTarget,
      envValues: envValues,
      onMemory: handleMemory,
      onPlugin: handlePlugin,
      onMcpToggle: handleMcpToggle,
      onProbe: handleProbe,
      onPrepareInstall: function (item) { setInstallTarget(item.id); setMessage(null); },
      onCancelInstall: function () { setInstallTarget(""); },
      onEnvChange: handleEnvChange,
      onInstall: handleInstall,
      onOpenNativeCron: function () {
        const current = window.location.pathname;
        const target = current.replace(/\/pantheon-modules\/?$/, "/cron");
        window.location.assign(target === current ? "/cron" : target);
      },
      onOpenNativePlugins: function () {
        const current = window.location.pathname;
        const target = current.replace(/\/pantheon-modules\/?$/, "/plugins");
        window.location.assign(target === current ? "/plugins" : target);
      },
    };

    return React.createElement(
      "div",
      { className: "pm-page" },
      React.createElement(
        "section",
        { className: "pm-hero" },
        React.createElement(
          "div",
          null,
          React.createElement("div", { className: "pm-kicker" }, "Governed module inventory"),
          React.createElement("h1", null, "Pantheon Modules"),
          React.createElement("p", null, "Hermes observes and executes. Pantheon governs. The human decides."),
        ),
        React.createElement(C.Button, { variant: "outline", onClick: refresh, disabled: loading }, loading ? "Refreshing…" : "Refresh observations"),
      ),
      React.createElement(
        "section",
        { className: "pm-boundary", role: "note" },
        React.createElement("strong", null, "State boundary"),
        React.createElement("span", null, "listed ≠ installed ≠ configured ≠ enabled ≠ reachable ≠ healthy"),
        React.createElement("span", null, "Hermes enabled ≠ Pantheon governance activation ≠ task authorization"),
      ),
      message && React.createElement("div", { className: "pm-message pm-message-" + message.tone, role: "status" }, message.text),
      errors.length > 0 && React.createElement(
        "div",
        { className: "pm-message pm-message-error", role: "alert" },
        "Partial inventory — " + errors.join(" | "),
      ),
      React.createElement(
        "div",
        { className: "pm-toolbar" },
        React.createElement(C.Input, {
          value: query,
          onChange: function (event) { setQuery(event.target.value); },
          placeholder: "Search modules, risks, or reasons",
          "aria-label": "Search modules",
        }),
        React.createElement(
          "div",
          { className: "pm-filters", "aria-label": "Module type filters" },
          [
            ["all", "All"],
            ["memory", "Memory"],
            ["mcp", "MCP"],
            ["plugins", "Plugins"],
            ["candidates", "Candidates"],
            ["operations", "Night ops"],
          ].map(function (entry) {
            return React.createElement(
              "button",
              { key: entry[0], className: filter === entry[0] ? "active" : "", onClick: function () { setFilter(entry[0]); } },
              entry[1],
            );
          }),
        ),
      ),
      loading && React.createElement("div", { className: "pm-loading" }, "Reading native Hermes inventories…"),
      !loading && visibleOperations.length === 0 && visibleSections.length === 0 && React.createElement("div", { className: "pm-empty" }, "No modules or operations match this view."),
      !loading && visibleOperations.length > 0 && React.createElement(
        "section",
        { className: "pm-section pm-operations-section" },
        React.createElement(
          "div",
          { className: "pm-section-heading" },
          React.createElement("h2", null, "Governed night operations"),
          React.createElement("span", null, visibleOperations.length + " catalog entries"),
        ),
        React.createElement(
          "div",
          { className: "pm-operations-note", role: "note" },
          React.createElement("strong", null, "Observe and prepare only"),
          React.createElement("span", null, "Hermes owns Cron. This plugin does not create recurring jobs because the audited dashboard create API cannot record a finite run limit."),
          React.createElement("span", null, "Confirm host timezone, profile, workdir, scopes, adapter, and expiry before activation."),
        ),
        React.createElement(
          "div",
          { className: "pm-grid" },
          visibleOperations.map(function (item) {
            return React.createElement(OperationCard, { key: item.id, item: item, onOpenNativeCron: actionProps.onOpenNativeCron });
          }),
        ),
      ),
      !loading && visibleSections.map(function (section) {
        return React.createElement(
          "section",
          { key: section.id, className: "pm-section" },
          React.createElement(
            "div",
            { className: "pm-section-heading" },
            React.createElement("h2", null, section.label),
            React.createElement("span", null, section.items.length + " observed/listed"),
          ),
          React.createElement(
            "div",
            { className: "pm-grid" },
            section.items.map(function (item) {
              return React.createElement(ModuleCard, Object.assign({ key: item.kind + ":" + item.id, item: item }, actionProps));
            }),
          ),
        );
      }),
    );
  }

  registry.register("pantheon-modules", PantheonModulesPage);
})();
