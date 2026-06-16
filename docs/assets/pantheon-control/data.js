/* Pantheon Control — données mock partagées. Documenté non implémenté.
   Aucune donnée réelle ; aucune action n'a d'effet réel. */

const CHIP_ICONS = {green:'✓',red:'✕',yellow:'⚠',orange:'⚠',blue:'●'};
function chip(label, tone){
  const t = tone||'muted';
  const ic = CHIP_ICONS[t];
  return '<span class="chip '+t+'">'+(ic?'<span class="ci" aria-hidden="true">'+ic+'</span>':'')+label+'</span>';
}
/* Petit « i » d'aide : info d'usage au survol. */
function info(text){ return ' <span class="i" title="'+text.replace(/"/g,'&quot;')+'">i</span>'; }

/* Machines : postes et serveurs du réseau. Les modèles LLM vivent ICI
   (là où est le GPU), pas sur le serveur de gouvernance. */
const MACHINES = [
  {nom:'Atelier-01', ip:'192.168.1.21', etat:['Allumé','green'],  gpu:'RTX 4090 · 24 Go', ram:'64 Go', cpu:'Ryzen 9', modeles:['qwen2.5:14b','qwen2.5-coder:14b','llava:13b']},
  {nom:'Atelier-02', ip:'192.168.1.22', etat:['Allumé','green'],  gpu:'RTX 3090 · 24 Go', ram:'32 Go', cpu:'Core i7', modeles:['bge-m3','nomic-embed-text']},
  {nom:'NAS-Synology',ip:'192.168.1.10',etat:['Allumé','green'],  gpu:'aucun',            ram:'8 Go',  cpu:'Celeron', modeles:[]},
  {nom:'Portable-Archi',ip:'192.168.1.45',etat:['Éteint','muted'],gpu:'RTX 4060 · 8 Go',  ram:'16 Go', cpu:'Core i7', modeles:['llama-guard']},
];

/* Services & outils : état, version, mise à jour, dépôt, dépendances,
   service système ou non, installé ou non. */
const SERVICES = [
  {nom:'OpenWebUI', categorie:'Interface',      port:'3000',  etat:['En ligne','green'],  installe:true,  systeme:true,  version:'0.5.4',  maj:null,    depot:'github.com/open-webui/open-webui', deps:['Docker'],            role:'Interface utilisateur générique et back-office IA.'},
  {nom:'Hermes Agent', categorie:'Exécution',   port:'8000',  etat:['En ligne','green'],  installe:true,  systeme:true,  version:'1.2.0',  maj:'1.3.0', depot:'dépôt interne',                    deps:['Python 3.12'],       role:'Moteur d’exécution. Prépare des propositions, ne valide rien.'},
  {nom:'Ollama', categorie:'Modèles',           port:'11434', etat:['En ligne','green'],  installe:true,  systeme:true,  version:'0.3.10', maj:null,    depot:'github.com/ollama/ollama',         deps:['GPU NVIDIA'],        role:'Hôte des modèles locaux (voir Machines).'},
  {nom:'SearXNG', categorie:'Recherche',        port:'8080',  etat:['En ligne','green'],  installe:true,  systeme:false, version:'2024.7', maj:'2024.9',depot:'github.com/searxng/searxng',       deps:['Docker'],            role:'Métamoteur de recherche.'},
  {nom:'RAGFlow', categorie:'Documents',        port:'9380',  etat:['Hors ligne','red'],  installe:true,  systeme:false, version:'0.11',   maj:null,    depot:'github.com/infiniflow/ragflow',    deps:['Docker','Qdrant'],   role:'Recherche dans les documents.'},
  {nom:'n8n', categorie:'Automatisation',       port:'5678',  etat:['Suspendu','orange'], installe:true,  systeme:false, version:'1.4',    maj:'1.6',   depot:'github.com/n8n-io/n8n',            deps:['Docker'],            role:'Automatisation de tâches (suspendu).'},
  {nom:'DocuSeal', categorie:'Documents',       port:'3001',  etat:['Non installé','muted'],installe:false,systeme:false, version:'—',      maj:null,    depot:'github.com/docusealco/docuseal',   deps:['Docker','PostgreSQL'],role:'Signature de documents.'},
];

/* Preuves & sources : éléments du dossier, avec leur nature, source, détail, alerte et
   les conséquences en cascade si on les retient comme preuve après décision humaine. */
const EVIDENCE = [
  {
    id:'P-201', sujet:'Fondations profondes imposées par l’étude de sol',
    nature:['Technique','blue'], source:'Étude géotechnique reçue (06/2026)',
    statut:['À examiner','yellow'], risque:['Élevé','red'],
    detail:'L’étude de sol impose des fondations profondes (pieux) à environ −4,5 m et écarte la semelle filante envisagée au stade esquisse.',
    alerte:'Retenir cet élément figerait le type de fondations : impacte structure, planning gros œuvre et budget.',
    links:[
      {relation:'impacts', to_id:'P-204', dependency_type:'technical_dependency', impact_level:'high',   note:'interaction sol / système constructif'},
      {relation:'impacts', to_id:'Estimatif fondations', dependency_type:'budget_dependency',   impact_level:'medium', note:'à réviser à la hausse'},
      {relation:'impacts', to_id:'Planning gros œuvre',  dependency_type:'planning_dependency', impact_level:'medium', note:'à décaler'},
    ],
  },
  {
    id:'P-202', sujet:'Aménagement du sous-sol demandé par le client (ERP)',
    nature:['Décision client ?','orange'], source:'Demande client en cours de projet',
    statut:['Supposition','muted'], risque:['Élevé','red'],
    detail:'Le client souhaite aménager le sous-sol en cours de projet. Cela change la catégorie / classification ERP et oblige à revoir l’entrée, les issues de secours et le désenfumage. À trancher : simple souhait (supposition) ou décision validée ?',
    alerte:'Si retenu : reclassement ERP — plusieurs preuves devront être revues en cascade.',
    links:[
      {relation:'impacts', to_id:'P-150', dependency_type:'regulatory_dependency', impact_level:'high',     note:'classification ERP à recalculer'},
      {relation:'impacts', to_id:'Étude désenfumage', dependency_type:'regulatory_dependency', impact_level:'high',     note:'à reprendre'},
      {relation:'impacts', to_id:'Issues de secours', dependency_type:'regulatory_dependency', impact_level:'critical', note:'arbitrage sécurité incendie'},
    ],
  },
  {
    id:'P-203', sujet:'DTU étanchéité mis à jour — détails constructifs',
    nature:['Réglementaire','blue'], source:'Veille — dernière version du DTU',
    statut:['À confirmer client','yellow'], risque:['Moyen','yellow'],
    detail:'La dernière version du DTU modifie les détails constructifs d’étanchéité. À faire confirmer avant de l’inscrire comme preuve du dossier.',
    alerte:'',
    links:[
      {relation:'impacts', to_id:'Carnet de détails', dependency_type:'technical_dependency', impact_level:'medium', note:'à mettre à jour'},
    ],
  },
  {
    id:'P-204', sujet:'Système constructif à vérifier en zone sismique',
    nature:['Technique','blue'], source:'Analyse parasismique (zone 4)',
    statut:['En doute','orange'], risque:['Élevé','red'],
    detail:'Le terrain est en zone de sismicité élevée. Le système constructif retenu doit être vérifié pour les contraintes parasismiques, en lien direct avec le choix des fondations.',
    alerte:'Dépend du choix de fondations (P-201).',
    links:[
      {relation:'depends_on', to_id:'P-201', dependency_type:'technical_dependency', impact_level:'high', note:'choix de fondations'},
    ],
  },
  {
    id:'P-150', sujet:'Classification ERP type N, 5ᵉ catégorie',
    nature:['Réglementaire','blue'], source:'Programme initial',
    statut:['Référence','green'], risque:['Moyen','yellow'],
    detail:'Classement ERP établi sur le programme initial, sans sous-sol aménagé.',
    alerte:'',
    links:[],
  },
];

/* Conséquences globales : ce qu'une décision fait bouger ailleurs (page Accueil). */
const IMPACTS = [
  {declencheur:'Sous-sol aménagé (P-202)', touche:'classification ERP · désenfumage · issues', gravite:['Critique','red'],    niveau:'décision encadrée'},
  {declencheur:'Fondations profondes (P-201)', touche:'structure · planning · budget',          gravite:['Important','orange'],niveau:'revue simple'},
];

/* Workflow Proposal : proposition visible avant action sensible. */
const WORKFLOW_PROPOSALS = [
  {
    id:'WF-IT249-001',
    titre:'Réponse entreprise — façade / IT249',
    demande:'Répondre à une demande de “validation pour exécution” sur un principe de façade.',
    risque:['Risque haut','red'],
    statut:['Décision humaine requise','yellow'],
    mission:'VISA / cohérence architecturale à confirmer. EXE technique non présumée.',
    manques:['PV feu','note technique','détail jonction façade-plancher','avis BET ou contrôleur technique'],
    etapes:[
      'Qualifier la mission, la phase et le risque de validation technique implicite.',
      'Contrôler les sources disponibles : contrat, CCTP, mail entrant, pièces entreprise.',
      'Préparer une réponse cadrée : avis architectural uniquement, sous réserve de justificatifs.',
      'Créer un dossier probatoire candidat : sources, dates, hypothèses, pièces absentes, décision humaine.'
    ],
    sortie:'Brouillon candidat non transmis.',
    effet:'Aucun effet externe sans gate humain.'
  }
];

/* Discussion hiérarchique : branches de raisonnement / rédaction, toutes fictives. */
const BRANCHES = [
  {id:'BR-A', titre:'Réponse prudente retenue', statut:['Retenue draft','green'], risque:['Sensible','orange'], origine:'Mail entreprise façade', note:'Formulation avec réserve technique et demande de justificatifs.'},
  {id:'BR-B', titre:'Réponse plus ferme', statut:['À vérifier','yellow'], risque:['Ton contractuel','orange'], origine:'Variante de BR-A', note:'Plus adaptée en contexte tendu, mais à relire avant transmission.'},
  {id:'BR-C', titre:'Recherche complémentaire IT249', statut:['Approfondir','blue'], risque:['Source à dater','yellow'], origine:'Branche depuis la question réglementaire', note:'À utiliser si les pièces entreprise sont insuffisantes.'},
  {id:'BR-D', titre:'Validation directe', statut:['Refusée','red'], risque:['Validation technique implicite','red'], origine:'Ancienne proposition', note:'Conservée comme branche refusée ; ne doit pas contaminer la version retenue.'},
];

/* Rédaction assistée : sélection et remplacement candidat. */
const DRAFT_ANCHORS = [
  {
    id:'DA-001',
    document:'Mail entreprise — façade',
    scope:'paragraphe sélectionné',
    selection:'Nous validons le principe proposé par l’entreprise pour exécution.',
    proposition:'Notre avis porte uniquement sur la cohérence architecturale du principe proposé, sous réserve des justificatifs techniques à produire par l’entreprise avant toute exécution.',
    statut:['Proposition','blue'],
    risque:['Terme dangereux : valider','red']
  },
  {
    id:'DA-002',
    document:'Réponse client — OPC absent',
    scope:'phrase sélectionnée',
    selection:'Nous allons coordonner les entreprises cette semaine.',
    proposition:'Nous pouvons demander aux entreprises de préciser leurs interfaces, mais la mission actuelle ne comprend pas l’OPC ni le pilotage détaillé des interventions.',
    statut:['À vérifier','yellow'],
    risque:['Hors mission possible','orange']
  },
];

/* Coûts IA : chiffres fictifs de pilotage, pas de facturation réelle. */
const AI_COSTS = [
  {poste:'Aujourd’hui', montant:'3.42 EUR', detail:'coût estimé toutes demandes'},
  {poste:'Projet FLOQUET', montant:'0.84 EUR', detail:'rédaction + recherche'},
  {poste:'Analyse PDF', montant:'0.62 EUR', detail:'extraction / synthèse'},
  {poste:'Recherche réglementaire', montant:'0.31 EUR', detail:'sources externes'},
];

/* Fichiers : matière brute ingérée. */
const FICHIERS = [
  {nom:'avis_ERP_bar.pdf',        type:'PDF',         projet:'Maison Lierre', lecture:['Texte extrait','green'],   statut:['Source à valider','yellow']},
  {nom:'inventaire_pieces.xlsx',  type:'Tableur',     projet:'Maison Lierre', lecture:['Lu','green'],              statut:['Source à valider','yellow']},
  {nom:'plan_terrasse_v3.dwg',    type:'Plan',        projet:'Champsaur',     lecture:['Non lu','orange'],         statut:['À traiter','orange']},
  {nom:'mail_budget_client.eml',  type:'Email',       projet:'Champsaur',     lecture:['Lu','green'],              statut:['Source à valider','yellow']},
  {nom:'compte_rendu_chantier.jpg',type:'Image',      projet:'Champsaur',     lecture:['Texte partiel','orange'],  statut:['À revoir','orange']},
  {nom:'devis_pcompe_chaleur.pdf',type:'PDF scanné',  projet:'Champsaur',     lecture:['Texte extrait','green'],   statut:['Reliée à P-142','blue']},
];

/* Base & mémoire : référence vs copies de travail. */
const BASE = [
  {nom:'PostgreSQL',           role:'Registre de référence',          statut:['Référence','green']},
  {nom:'Index de recherche',   role:'Retrouver par similarité',       statut:['Copie de travail','blue']},
  {nom:'Mémoire agent',        role:'Aide à l’exécution',             statut:['Copie de travail','blue']},
  {nom:'Registre des preuves', role:'Entrées validées',               statut:['Référence','green']},
  {nom:'Brouillons',           role:'Avant validation',               statut:['À valider','yellow']},
  {nom:'Synchronisation',      role:'État des copies',                statut:['1 à resynchroniser','orange']},
];

/* Surveillance : contrôles automatiques (lecture seule). */
const CONTROLES = [
  'Rôles respectés','Cadre de tâche présent','Effet externe protégé','Réussite ≠ approbation',
  'Source ≠ preuve','Cloisonnement des projets','Pas de mémoire automatique','Manques visibles',
  'Installé ≠ autorisé','Récent ≠ stable','Idempotence','Preuve mise en doute',
].map((label,i)=>({id:String(i+1).padStart(2,'0'), label, resultat: i%5===0?['Alerte','orange']:['OK','green']}));

/* Fournisseurs IA : Ollama en local + fournisseurs cloud. Statut + configuration. */
const PROVIDERS = [
  {nom:'Ollama (local)',     type:'Local', etat:['Connecté','green'],     modeles:'voir page Machines',   usage:'Modèles ouverts exécutés sur vos machines (GPU). Confidentiel, rien ne sort du réseau.'},
  {nom:'Claude (Anthropic)', type:'Cloud', etat:['Connecté','green'],     modeles:'Opus · Sonnet · Haiku',usage:'Modèles haut de gamme pour le raisonnement et la rédaction longue.'},
  {nom:'ChatGPT (OpenAI)',   type:'Cloud', etat:['Non connecté','muted'], modeles:'GPT-4o · série o',     usage:'Polyvalent. Nécessite une clé API.'},
  {nom:'Gemini (Google)',    type:'Cloud', etat:['Non connecté','muted'], modeles:'Gemini 2.x',           usage:'Multimodal, très grand contexte.'},
  {nom:'Mistral',            type:'Cloud', etat:['Non connecté','muted'], modeles:'Large · Codestral',    usage:'Européen, bon rapport coût / performance.'},
];

/* Skills actifs : ce que l'utilisateur peut mobiliser et à quoi ça sert. */
const SKILLS = [
  {nom:'Audit de source',         actif:true,  usage:'Vérifie l’autorité, la date, la version et les contradictions d’une source.'},
  {nom:'Extraction de pièces',    actif:true,  usage:'Repère dates, montants, lots et pénalités dans un document.'},
  {nom:'Comparaison de documents',actif:true,  usage:'Compare deux versions (CCTP, devis…) et signale les écarts.'},
  {nom:'Lecture d’image (OCR)',   actif:true,  usage:'Transforme un scan ou une photo en texte exploitable.'},
  {nom:'Recherche web',           actif:true,  usage:'Cherche des sources externes via SearXNG.'},
  {nom:'Synthèse de réunion',     actif:false, usage:'Résume un compte rendu et liste les actions à faire.'},
];

/* Journal (lecture seule, ajout uniquement en simulation locale). */
const JOURNAL = [
  {t:'2026-06-13 08:02', msg:'P-177 retenu comme référence après décision humaine simulée (réf. VAL-204).'},
  {t:'2026-06-12 17:44', msg:'Proposition d’édition de P-156 préparée depuis le tableau de bord.'},
  {t:'2026-06-12 09:10', msg:'Contrôle « Pas de mémoire automatique » : alerte.'},
  {t:'2026-06-11 14:20', msg:'n8n suspendu — état d’exécution seulement, statut inchangé.'},
];
