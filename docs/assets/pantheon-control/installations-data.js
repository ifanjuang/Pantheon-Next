/* Pantheon Control — données candidates pour Installations & bootstrap.
   Documenté non implémenté. Aucun service, conteneur, paquet, port ou runtime n’est créé. */

const INSTALL_LAYERS = [
  {id:'L0', titre:'Accès humain / baseline', etat:['À confirmer','yellow'], dependances:'Machine choisie, accès admin, réseau, stockage, sauvegarde.', owner:'Humain', pantheon:'Checklist, risque, décision candidate.', next:'Confirmer accès, sauvegarde et périmètre.'},
  {id:'L1', titre:'Support bootstrap', etat:['À préparer','blue'], dependances:'Guide, bundle local, dépôt Git, package vendeur ou dossier local.', owner:'Humain / outil vendeur', pantheon:'Plan candidat, preflight, rollback, état attendu.', next:'Choisir support : manuel, bundle, outil vendeur.'},
  {id:'L2', titre:'Capacité machine / NAS', etat:['À classifier','yellow'], dependances:'OS, CPU, RAM, stockage, réseau, conteneurs, VM, GPU/NPU/iGPU.', owner:'Humain', pantheon:'Classification NAS-0 à NAS-6, rôle recommandé.', next:'Renseigner profil matériel.'},
  {id:'L3', titre:'Substrat services', etat:['Absent','muted'], dependances:'Natif, conteneur, VM, système NAS ou service manager.', owner:'Humain / installateur externe', pantheon:'Plan candidat, ports, volumes, secrets, rollback.', next:'Décider si substrat nécessaire.'},
  {id:'L4', titre:'Surface statique minimale', etat:['Candidate','blue'], dependances:'HTML statique, docs locales, NAS static host, GitHub Pages ou LAN privé.', owner:'Hébergement statique', pantheon:'Afficher état installation sans prétendre qu’un runtime existe.', next:'Publier ou pointer une page statique.'},
  {id:'L5', titre:'Hermes candidat', etat:['Non installé','muted'], dependances:'Substrat existant, volumes, logs, secrets, health check.', owner:'Humain / bootstrap / substrat', pantheon:'Plan d’installation candidat et statut après résultat.', next:'Préparer plan Hermes après substrat.'},
  {id:'L6', titre:'Surface d’exposition', etat:['Non installée','muted'], dependances:'OpenWebUI ou surface équivalente, auth, scope, réseau.', owner:'Humain / substrat', pantheon:'Préciser local, VPN, public read-only, approvals requis.', next:'Décider surface après Hermes ou statique.'},
  {id:'L7', titre:'Modules runtime', etat:['Bloqué','red'], dependances:'Hermes ou installateur externe, health checks, ressources.', owner:'Hermes autorisé / humain', pantheon:'Préparer candidats : OCR, modèles, vector DB, mémoire, GraphRAG, LangGraph.', next:'Attendre runtime ou installateur externe.'},
  {id:'L8', titre:'Admission & task authorization', etat:['Non applicable','muted'], dependances:'Modules installés, manifest, passport, preflight, Task Contract.', owner:'Pantheon + humain', pantheon:'Gouverner admission, scope, approval, statut.', next:'Seulement après installation vérifiée.'},
];

const INSTALL_PROFILES = [
  {nom:'NAS stockage + cockpit statique', score:'Recommandé', role:'Stockage, sauvegarde, documentation, redirection contrôlée.', risque:'Faible', notes:'Point de départ le plus sûr si le NAS est inconnu.'},
  {nom:'NAS passerelle / redirection', score:'Candidat', role:'Reverse proxy, accès privé, sous-domaines, routage vers compute.', risque:'Moyen', notes:'Ne doit pas exposer les runtimes internes publiquement.'},
  {nom:'NAS runtime léger', score:'À prouver', role:'Petits services, inventaire, index léger, health checks.', risque:'Moyen', notes:'Dépend fortement CPU/RAM/I/O et support conteneurs.'},
  {nom:'NAS GPU/NPU', score:'À vérifier', role:'OCR, vision, embeddings ou inference locale si support réel.', risque:'Élevé', notes:'GPU présent ne veut pas dire LLM prêt. Drivers et benchmarks requis.'},
  {nom:'NAS + compute externe', score:'Recommandé', role:'NAS stocke et route ; workstation/mini-PC/GPU exécute.', risque:'Faible à moyen', notes:'Sépare stockage durable et calcul volatil.'},
];

const INSTALL_STATES = ['absent','unknown','detected','planned','ready_for_manual_install','ready_for_handoff','installed_unverified','healthy','blocked','rolled_back','retired'];

const NAS_PROFILE_FIELDS = [
  ['vendor','Marque','text','Synology / QNAP / Unraid / TrueNAS / autre'],
  ['model','Modèle','text','Modèle exact si connu'],
  ['ram','RAM estimée','select',['inconnue','≤ 4 Go','8 Go','16 Go','32 Go +']],
  ['containers','Conteneurs','select',['inconnu','non','oui']],
  ['vm','VM','select',['inconnu','non','oui']],
  ['gpu','GPU / iGPU','select',['inconnu','aucun','iGPU média','GPU exploitable']],
  ['npu','NPU / accélérateur IA','select',['inconnu','non','oui']],
  ['reverse_proxy','Reverse proxy / gateway','select',['inconnu','non','oui']],
  ['vpn','VPN / accès privé','select',['inconnu','non','oui']],
  ['backup','Backup / snapshot','select',['inconnu','non','oui']],
];

const NAS_PROFILE_DEFAULT = {
  vendor:'', model:'', ram:'inconnue', containers:'inconnu', vm:'inconnu', gpu:'inconnu', npu:'inconnu', reverse_proxy:'inconnu', vpn:'inconnu', backup:'inconnu'
};
