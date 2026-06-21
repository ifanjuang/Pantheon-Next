/* Pantheon Control — connexions externes, accès réseau et instances locales.
   Documenté non implémenté. Aucune clé, aucun compte, aucun accès et aucune instance réelle ne sont modifiés. */

const EXTERNAL_CONNECTIONS = [
  {nom:'Claude (Anthropic)', type:'Compte IA cloud', etat:['Connecté','green'], identite:'Compte API', usage:'Raisonnement et rédaction longue. Toute utilisation reste cadrée par mission, coût et périmètre.'},
  {nom:'ChatGPT (OpenAI)', type:'Compte IA cloud', etat:['Non connecté','muted'], identite:'Clé API à configurer', usage:'IA polyvalente. Connexion externe soumise à configuration, coût et autorisation.'},
  {nom:'Gemini (Google)', type:'Compte IA cloud', etat:['Non connecté','muted'], identite:'Compte Google / API', usage:'Modèles multimodaux et grand contexte. Connexion externe à cadrer.'},
  {nom:'Mistral', type:'Compte IA cloud', etat:['Non connecté','muted'], identite:'Clé API à configurer', usage:'Modèles cloud européens. Connexion externe à cadrer.'},
  {nom:'Google Workspace', type:'Connecteur externe', etat:['À vérifier','yellow'], identite:'OAuth / compte agence', usage:'Gmail, Drive, Calendar. Accès externe soumis à scope, preuve et approval.'},
  {nom:'Notion', type:'Connecteur externe', etat:['Connecté','green'], identite:'Workspace Pantheon Next', usage:'Pilotage Kanban. Ne remplace pas le repo canonique.'},
  {nom:'GitHub', type:'Connecteur externe', etat:['Connecté','green'], identite:'Repo Pantheon-Next', usage:'Source canonique du dépôt, issues, PR et fichiers.'},
];

const ACCESS_CONNECTIONS = [
  {nom:'VPN agence', type:'Accès distant privé', etat:['À configurer','yellow'], identite:'VPN existant', usage:'Accéder au cockpit et aux services internes sans exposition publique directe. Accès réseau seulement : ne vaut pas autorisation fonctionnelle.'},
  {nom:'Synology NAS', type:'Ressource locale exposable', etat:['À vérifier','yellow'], identite:'NAS / stockage agence', usage:'Stockage, sauvegarde ou reverse proxy possible. Ne doit pas devenir source canonique sans statut documentaire.'},
  {nom:'Sous-domaine IFJ', type:'Routage externe', etat:['Candidate','blue'], identite:'subdomain.ifja.fr', usage:'Point d’entrée public ou semi-public possible vers un reverse proxy. À limiter aux vues explicitement autorisées.'},
  {nom:'Reverse proxy', type:'Passerelle d’accès', etat:['Candidate','blue'], identite:'NAS ou serveur frontal', usage:'Route un sous-domaine vers un service interne. Doit imposer authentification, TLS, scope et journalisation.'},
];

const LOCAL_INSTANCES = [
  {nom:'Ollama — Atelier-01', machine:'Atelier-01', service:'Ollama', port:'11434', etat:['En ligne','green'], modeles:['qwen2.5:14b','qwen2.5-coder:14b','llava:13b'], usage:'Instance locale GPU. Les modèles tournent sur la machine, pas dans Pantheon.'},
  {nom:'Ollama — Atelier-02', machine:'Atelier-02', service:'Ollama', port:'11434', etat:['En ligne','green'], modeles:['bge-m3','nomic-embed-text'], usage:'Instance locale orientée embeddings / recherche. À traiter comme capacité locale.'},
  {nom:'Ollama — Portable-Archi', machine:'Portable-Archi', service:'Ollama', port:'11434', etat:['Éteint','muted'], modeles:['llama-guard'], usage:'Instance locale disponible seulement si la machine est réveillée.'},
];
