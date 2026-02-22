# 📚 FICHE DE COURS ÉLÈVE
## "Catalogue de Services IT"

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 9*

---

## 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|---------------|
| **B1.2** | Exploiter des référentiels (ITIL — Gestion du catalogue de services) |
| **B1.5** | Mettre à disposition des utilisateurs un service informatique |
| **B3.3** | Documenter et communiquer professionnellement |

---

## PARTIE I — Définition et Rôle du Catalogue de Services

### I.A. Définition ITIL

En ITIL 4, le **catalogue de services** est la liste complète et structurée de tous les services IT disponibles, publiée à destination des utilisateurs et des clients internes.

Il répond à la question fondamentale que tout utilisateur se pose :

> *"Qu'est-ce que la DSI peut faire pour moi, et comment le demander ?"*

### I.B. Les Deux Vues du Catalogue

ITIL distingue deux catalogues complémentaires qui servent des publics différents :

```
   ┌───────────────────────────────────────────────────────────────┐
   │              CATALOGUE DE SERVICES                            │
   │                                                               │
   │   VUE MÉTIER (Utilisateurs)     VUE TECHNIQUE (DSI)          │
   │   ──────────────────────────    ───────────────────────────   │
   │   "Accès à la messagerie"       Serveur Exchange 2019         │
   │   "Que peut-il faire ?"         Architecture HA, 2 nœuds      │
   │   "Comment y accéder ?"         Composants : AD, DNS, MX...   │
   │   "Que faire si ça ne marche    SLA : 99,9% / RTO 2h          │
   │    pas ?"                       Responsable technique : X      │
   │   "Quel délai si panne ?"       Procédures exploitation        │
   │                                                               │
   │   → Publié sur le portail       → Document interne DSI        │
   │     GLPI, intranet                (DAT, CMDB)                 │
   └───────────────────────────────────────────────────────────────┘
```

> 💡 **La règle d'or de la vue métier :** Jamais de jargon technique. Si l'utilisateur doit connaître un terme technique pour comprendre la fiche de service, c'est que la fiche est mal rédigée.

---

### I.C. Pourquoi un Catalogue de Services ?

| **Bénéfice** | **Pour les utilisateurs** | **Pour la DSI** |
|---|---|---|
| **Visibilité** | Savent ce qui existe | Peuvent communiquer leur offre |
| **Autonomie** | Savent comment accéder sans appeler | Réduction des demandes informelles |
| **Attentes réalistes** | Connaissent les SLA et délais | Réduction des plaintes injustifiées |
| **Gouvernance** | — | Base pour les priorités budgétaires |
| **Onboarding** | Nouveaux employés autonomes plus vite | Réduction des appels helpdesk N1 |
| **Amélioration continue** | Peuvent évaluer les services | Mesure de satisfaction formalisée |

---

## PARTIE II — La Fiche de Service

### II.A. Structure d'une Fiche de Service

Une **fiche de service** est le document unitaire décrivant un service spécifique. Elle contient :

| **Section** | **Contenu** | **Exemple — Service Messagerie** |
|---|---|---|
| **Nom du service** | Nom clair et court en termes métier | Messagerie d'entreprise |
| **Description** | Ce que le service fait pour l'utilisateur (2-3 phrases, zéro jargon) | "Permet d'envoyer et recevoir des emails professionnels depuis votre poste, smartphone ou navigateur web." |
| **Bénéficiaires** | Qui peut utiliser ce service | Tous les employés de SimIO SARL |
| **Conditions d'accès** | Ce qu'il faut pour en bénéficier | Compte Active Directory actif |
| **Comment accéder** | Procédure simple pour commencer | "Ouvrir Outlook sur votre poste — vos identifiants réseau sont les mêmes" |
| **Fonctionnalités incluses** | Ce que couvre le service | Email, agenda partagé, contacts, salle de réunion |
| **Ce qui est EXCLU** | Limitations importantes | Pièces jointes > 25 Mo — stockage personnel illimité (OneDrive séparé) |
| **Disponibilité** | Plage horaire + SLA | 24h/24 — SLA 99,9% — hors maintenance planifiée dimanche 22h-6h |
| **Délai de support** | Selon priorité | P1 < 4h, P3 < 24h |
| **Comment signaler un problème** | Canal de contact | Ticket GLPI — Catégorie : Logiciel > Messagerie |
| **Responsable technique** | Contact DSI | [Technicien désigné] |
| **Dernière révision** | Date et version | 2024-09-01 — v1.0 |

---

### II.B. Les Catégories de Services IT

Un catalogue de services est organisé en **catégories** cohérentes. Voici une organisation typique pour une PME :

```
   CATALOGUE DE SERVICES IT — SimIO SARL
   ─────────────────────────────────────────────────────────────────

   📧 COMMUNICATION
   ├── Messagerie d'entreprise
   ├── Calendrier et salles de réunion
   └── Téléphonie (fixe / mobile)

   💾 DONNÉES ET STOCKAGE
   ├── Partage de fichiers (dossiers réseau)
   ├── Sauvegarde et restauration
   └── Archivage

   🖥️ POSTE DE TRAVAIL
   ├── Installation et configuration d'un poste
   ├── Logiciels métier et bureautique
   └── Impression

   🔒 ACCÈS ET IDENTITÉ
   ├── Création / modification de compte
   ├── Réinitialisation de mot de passe
   └── Accès VPN (télétravail)

   🌐 RÉSEAU ET CONNECTIVITÉ
   ├── Accès Internet
   ├── WiFi entreprise
   └── Connexion filaire

   🛠️ SUPPORT ET ASSISTANCE
   ├── Helpdesk N1 (centre de services)
   ├── Dépannage sur site
   └── Formation utilisateur
```

---

### II.C. Le Catalogue dans GLPI

GLPI peut exposer le catalogue de services directement sur le **portail utilisateur**. Chaque service du catalogue devient une **catégorie de ticket** avec des formulaires adaptés.

```
   PORTAIL GLPI UTILISATEUR
   ─────────────────────────────────────────────────────────────────
   L'utilisateur arrive sur le portail et voit :

   ┌────────────────────────────────────────────────────────────┐
   │  🔑 Problème avec mon mot de passe                        │
   │  📧 Ma messagerie ne fonctionne pas                       │
   │  🖨️ Mon imprimante ne répond pas                          │
   │  💾 Je ne peux pas accéder à un dossier partagé           │
   │  💻 Je souhaite installer un logiciel                     │
   │  🆕 Demande de création de compte                        │
   │  📞 Autre demande                                         │
   └────────────────────────────────────────────────────────────┘

   Chaque tuile crée automatiquement un ticket avec :
   - La catégorie pré-remplie
   - Les champs adaptés à ce type de demande
   - L'affectation automatique au bon groupe technique
   - Le SLA correspondant appliqué automatiquement
```

---

### II.D. Cycle de Vie d'un Service dans le Catalogue

Un service n'est pas éternel. ITIL définit son cycle de vie dans le catalogue :

```
   NOUVEAU SERVICE          SERVICE ACTIF           SERVICE RETIRÉ
   ───────────────          ─────────────           ──────────────
   Analyse du besoin   →    Disponible dans    →    Annonce de
   Construction            le catalogue            fin de service
   Tests                   SLA suivi               Migration
   Communication           Améliorations           Retrait du
   → Mise en service        selon retours           catalogue
     (PV — S7)                                     Archivage
```

---

## III. Vocabulaire Clé

| **Terme** | **Définition** |
|-----------|---------------|
| **Catalogue de services** | Liste structurée de tous les services IT disponibles, publiée pour les utilisateurs |
| **Vue métier** | Version du catalogue rédigée en termes compréhensibles par les utilisateurs non-techniciens |
| **Vue technique** | Version interne du catalogue décrivant l'infrastructure supportant chaque service |
| **Fiche de service** | Document décrivant un service individuel (description, SLA, accès, contact) |
| **Portail utilisateur** | Interface GLPI permettant aux utilisateurs de créer des tickets depuis le catalogue |
| **Service actif** | Service disponible dans le catalogue et supporté par la DSI |
| **Service déprécié** | Service maintenu temporairement mais en cours de remplacement |
| **Service retiré** | Service supprimé du catalogue (ne doit plus être demandé) |
| **Onboarding IT** | Processus d'intégration d'un nouvel employé — le catalogue accélère son autonomie |

---

---

# 📚 FICHE DE COURS ÉLÈVE
## "Portfolio E5 — La Situation Professionnelle Significative"

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 9*

---

## 🎯 L'Épreuve E5 en Résumé

| **Paramètre** | **Détail** |
|---|---|
| **Épreuve** | E5 — Support et mise à disposition de services informatiques |
| **Coefficient** | 4 |
| **Format** | 1h30 de préparation + 40 min devant le jury |
| **Supports** | Dossier de SPS remis avant l'oral + supports visuels optionnels |
| **Jury** | 2 membres : 1 professionnel + 1 enseignant (BTS différent) |
| **Ce que le jury évalue** | Votre capacité à décrire, justifier et réfléchir sur vos réalisations |

---

## PARTIE I — Qu'est-ce qu'une SPS ?

### I.A. Définition

Une **Situation Professionnelle Significative (SPS)** est la description structurée d'une réalisation technique concrète que vous avez conduite, en formation ou en entreprise, qui mobilise une ou plusieurs compétences du référentiel RNCP.

> 📌 **"Significative" ne signifie pas "impressionnante".** Une SPS n'a pas besoin d'être un projet de migration d'infrastructure. Remplir une fiche technique (S2), résoudre un incident imprimante (S4), configurer GLPI (S6) — tout cela peut être une SPS si c'est bien documenté.

### I.B. Ce qu'une SPS N'est Pas

| **Ce n'est pas...** | **C'est plutôt...** |
|---|---|
| Un résumé de votre BTS | Une réalisation précise, datée, sur un périmètre défini |
| Une liste de technologies | Une narration de ce que VOUS avez fait et décidé |
| Un tutoriel technique | Une description de votre démarche professionnelle |
| Un copier-coller du cours | Votre expérience personnelle avec ses difficultés et apprentissages |

---

## PARTIE II — Structure Officielle d'une SPS

### II.A. Les 6 Sections Obligatoires

```
   ① CONTEXTE
   ──────────────────────────────────────────────────────────────
   Qui est l'organisation (taille, secteur, structure IT) ?
   Quel est l'environnement technique pertinent ?
   Quelle est votre place dans cet environnement ?

   ② MISSION
   ──────────────────────────────────────────────────────────────
   Quel était l'objectif assigné ?
   Par qui ? Dans quel cadre ?
   Quelles étaient les contraintes (délais, budget, périmètre) ?

   ③ RÉALISATION
   ──────────────────────────────────────────────────────────────
   Ce que VOUS avez fait, étape par étape
   Les décisions prises et leur justification
   Les difficultés rencontrées et comment vous les avez résolues
   → C'est la section la plus longue et la plus importante

   ④ COMPÉTENCES MOBILISÉES
   ──────────────────────────────────────────────────────────────
   Code RNCP + intitulé pour chaque compétence mobilisée
   Ex : B1.1 — Recenser et identifier les ressources numériques
   Ex : B1.6 — Assurer le support des utilisateurs

   ⑤ RÉSULTATS ET VALIDATION
   ──────────────────────────────────────────────────────────────
   Comment la réussite a été vérifiée et par qui
   Résultats mesurables si possible (MTTR, tickets résolus, SLA...)
   Retour utilisateur / superviseur

   ⑥ RÉFLEXIVITÉ — CE QUE J'AI APPRIS
   ──────────────────────────────────────────────────────────────
   Ce que vous feriez différemment
   Ce que cette expérience vous a apporté professionnellement
   Lien avec la suite (compétences à approfondir)
```

> ⭐ **La section ⑥ est souvent négligée et pourtant décisive.** Le jury E5 peut passer 10 minutes sur cette section seule. Un apprenant capable de dire "j'aurais dû faire X plutôt que Y parce que..." démontre une maturité professionnelle que le jury valorise fortement.

---

### II.B. Format et Volume

| **Paramètre** | **Recommandation** |
|---|---|
| **Longueur de la fiche SPS** | 2 pages maximum (sans les preuves) |
| **Preuves associées** | 3 à 8 documents (captures, tickets, DAT, schémas) |
| **Nombre de SPS dans le dossier** | 3 minimum, 5 recommandées, 6 maximum |
| **Variété des compétences** | Couvrir au minimum B1.1, B1.2, B1.3, B1.6 et un B2 |
| **Répartition formation/entreprise** | Au moins 2 SPS issues de missions en entreprise |
| **Format** | PDF ou présentation — pas de Word non converti |

---

### II.C. Ce que le Jury Cherche à Comprendre

Pendant les 40 minutes d'oral, le jury cherche à valider 3 choses :

```
   1. VOUS AVEZ VRAIMENT FAIT ÇA
      → Questions de détail : "Quelle commande avez-vous utilisée ?"
        "Qu'est-ce qui s'est passé quand vous avez fait X ?"
        Réponse attendue : précise, personnelle, avec les détails d'un praticien

   2. VOUS COMPRENEZ CE QUE VOUS AVEZ FAIT
      → Questions de compréhension : "Pourquoi ce choix ?"
        "Qu'est-ce qui se serait passé si vous aviez fait Y ?"
        Réponse attendue : justification technique et professionnelle

   3. VOUS ÊTES CAPABLE D'ÉVOLUER
      → Questions de réflexion : "Qu'auriez-vous fait différemment ?"
        "Comment ce service pourrait-il être amélioré ?"
        Réponse attendue : critique constructive de son propre travail
```

---

### II.D. Les Preuves — Ce qui Compte

Les **preuves** (pièces jointes à la SPS) servent à crédibiliser votre réalisation. Elles doivent être :

| **Type de preuve** | **Exemples** | **Valeur** |
|---|---|---|
| **Captures d'écran** | Interface GLPI avec votre ticket, console OCS avec votre poste, fiche technique remplie | Moyenne — montre que c'est réel |
| **Documents produits** | Fiche technique S2, PV de mise en service S7, SLA rédigé S7 | Élevée — prouve une démarche |
| **Tickets GLPI** | Export PDF d'un ticket traité, avec votre nom comme technicien | Élevée — traçabilité |
| **Schémas et DAT** | Architecture réseau SimIO, diagramme de flux | Très élevée — compétence technique |
| **Scripts / Commandes** | Script PowerShell de collecte OCS, commandes icacls utilisées | Très élevée — compétence opérationnelle |

> ⚠️ **Ce qui ne vaut pas comme preuve :** Des captures du cours ou du TP tel qu'il était fourni. La preuve doit montrer VOTRE travail — pas le modèle de l'enseignant.

