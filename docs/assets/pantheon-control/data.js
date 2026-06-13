/* Pantheon Control — données mock partagées. Documenté non implémenté.
   Aucune de ces données n'est réelle ; aucune action n'a d'effet runtime. */

/* Helpers de rendu de chips à ton explicite (pas de devinette par sous-chaîne). */
function chip(label, tone){ return '<span class="chip '+(tone||'muted')+'">'+label+'</span>'; }

/* Services installés : statut RUNTIME et statut GOUVERNANCE séparés. */
const STACKS = [
  {name:'OpenWebUI',  kind:'Surface',        port:'3000',  run:['Online','green'],       gov:['Surface active','green']},
  {name:'Hermes Agent',kind:'Runtime',       port:'8000',  run:['Online','green'],       gov:['Candidate-only','yellow']},
  {name:'Ollama',     kind:'Model host',     port:'11434', run:['Online','green'],       gov:['Hôte de modèles','blue']},
  {name:'SearXNG',    kind:'Source',         port:'8080',  run:['Online','green'],       gov:['Source candidate','yellow']},
  {name:'Qdrant',     kind:'Index',          port:'6333',  run:['Online','green'],       gov:['Index seul','blue']},
  {name:'RAGFlow',    kind:'RAG',            port:'9380',  run:['Offline','red'],        gov:['Candidate','yellow']},
  {name:'n8n',        kind:'Workflow',       port:'5678',  run:['Suspended','red'],      gov:['Non autorisé','red']},
  {name:'DocuSeal',   kind:'Adapter',        port:'3001',  run:['Non installé','muted'], gov:['Gate requis','orange']},
];

/* Base & Mémoire : canon vs projections. */
const BASE = [
  {name:'PostgreSQL',           role:'Registre canonique',          status:['Source de vérité','green']},
  {name:'pgvector',             role:'Récupération par similarité', status:['Projection','blue']},
  {name:'mem0',                 role:'Mémoire agent (projetée)',    status:['Projection','blue']},
  {name:'Registre Probatoire',  role:'Entrées gouvernées',          status:['Canon','green']},
  {name:'Registre de candidats',role:'Avant gate',                  status:['Candidate','yellow']},
  {name:'Backend sync',         role:'État de synchronisation',     status:['1 hors-sync','orange']},
];

/* Modèles LAN + agents. */
const MODELS = [
  {name:'qwen2.5:14b',       kind:'chat',     use:'rédaction'},
  {name:'qwen2.5-coder:14b', kind:'code',     use:'config'},
  {name:'nomic-embed-text',  kind:'embedding',use:'RAG'},
  {name:'llava:13b',         kind:'vision',   use:'image'},
  {name:'bge-m3',            kind:'embedding',use:'multilingue'},
  {name:'llama-guard',       kind:'safety',   use:'filtrage'},
];

/* Connexions / catalogue — DIAGNOSTIC lecture seule, jamais d'installation ici. */
const CONNECTIONS = [
  {name:'OpenWebUI',                  type:'Stack',          group:'Accès utilisateur', diag:['Opérationnel','green'],         gov:['Surface active','green'],   note:'Interface principale utilisateur.'},
  {name:'Notion API',                 type:'API',            group:'Connecteurs',       diag:['Config requise','orange'],      gov:['Pilotage only','yellow'],   note:'Interface technique Notion.'},
  {name:'Notion MCP Server',          type:'MCP Server',     group:'Connecteurs',       diag:['Disponible','blue'],            gov:['Read-only first','yellow'], note:'Expose Notion via MCP.'},
  {name:'notion.update_page',         type:'MCP Tool',       group:'Connecteurs',       diag:['Dépendance manquante','orange'],gov:['Gate requis','orange'],     note:'Action d’écriture Notion.'},
  {name:'source-audit',               type:'Skill Hermes',   group:'Recherche',         diag:['Disponible','blue'],            gov:['Candidate','yellow'],       note:'Vérifie autorité, date, version, contradiction.'},
  {name:'Google Workspace CLI',       type:'Standalone Tool',group:'Connecteurs',       diag:['Disponible','blue'],            gov:['Read-only first','yellow'], note:'Gmail, Drive, Docs, Sheets, Calendar.'},
  {name:'OpenWebUI source-audit',     type:'Plugin OpenWebUI',group:'Accès utilisateur',diag:['Disponible','blue'],            gov:['Non autorisé','red'],       note:'Bouton UI vers Hermes.'},
  {name:'RAGFlow',                    type:'Stack',          group:'Documents / RAG',   diag:['Disponible','blue'],            gov:['Candidate','yellow'],       note:'RAG documentaire.'},
];

/* Evidence → Mémoire. Le statut affiché est l'état GOUVERNÉ courant ;
   le dashboard ne le change jamais directement (voir evidence.html). */
const EVIDENCE = [
  {id:'EV-142', subject:'RE2020 rénovation bar ERP',     status:['Questioned','orange'], risk:['High','red'],   why:'Source ABF locale absente.'},
  {id:'EV-156', subject:'Inventaire pièces Maison Lierre',status:['Candidate','yellow'], risk:['Medium','yellow'],why:'14 pièces reçues, 3 absentes.'},
  {id:'EV-177', subject:'Notion pilotage only',          status:['Promoted','green'],   risk:['Medium','yellow'],why:'Notion n’est pas canonique.'},
];

/* File d'impact (cœur métier du cockpit). */
const IMPACTS = [
  {trigger:'Suppression piscine', impacted:'PAC piscine · terrasse · fondations · budget', sev:['Critique','red'],   path:'governance_path'},
  {trigger:'Maj budget client',   impacted:'Programme · arbitrage terrasse',               sev:['Élevé','orange'],   path:'review_path'},
];

/* Doctor checks read-only exposés par le mcp-server (le dashboard AFFICHE, n'exécute pas). */
const CHECKS = [
  'Role boundary','Task Contract required','External effect gate','Runtime success ≠ approval',
  'Source candidate ≠ proof','Scope isolation','Memory promotion blocked','Capability gap visible',
  'Installed ≠ authorized','Latest ≠ stable','Idempotency','Evidence questioned',
].map((label,i)=>({id:String(i+1).padStart(2,'0'), label, result: i%5===0?['Warning','orange']:['Pass','green']}));

/* Journal d'audit append-only (lecture seule). */
const AUDIT = [
  {t:'2026-06-13 08:02', msg:'EV-177 promu → décision enregistrée par le User Decision Gate (réf. GATE-204).'},
  {t:'2026-06-12 17:44', msg:'Candidat d’édition EV-156 soumis au chokepoint depuis le dashboard.'},
  {t:'2026-06-12 09:10', msg:'Doctor check « Memory promotion blocked » = Warning.'},
  {t:'2026-06-11 14:20', msg:'n8n marqué Non autorisé — runtime suspendu, statut gouvernance inchangé.'},
];
