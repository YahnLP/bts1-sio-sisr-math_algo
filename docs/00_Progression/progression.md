# 🛣️ Progression
## BTS SIO SISR – MATHS / ALGO (U2)
### Année 1 – Mathématiques informatiques contextualisées (20 semaines – 80h)

---

## 🎯 Objectif

Construire les compétences fondamentales **Maths / Algo (U2)** en lien direct avec les situations réelles d’un futur technicien SISR :

- Maîtriser les **systèmes de numération** (binaire / hexa) utiles aux adresses IP/MAC et aux données
- Comprendre et exploiter l’**algèbre de Boole** (logique, conditions, filtrage)
- Réaliser les **calculs réseaux** indispensables : masques, CIDR, réseau/broadcast, plages, VLSM
- Mettre en œuvre les bases de l’**algorithmique** : variables, conditions, boucles, fonctions
- Manipuler des **structures de données** simples (listes, tableaux, chaînes, ensembles) appliquées à des cas IT
- Introduire la **complexité** et les choix d’algorithmes (recherche / tri)
- Se préparer progressivement à l'examen **CCF de Mathématiques (U2)** (exercices type, rigueur, justifications)

> Cette progression reprend **strictement** l’organisation hebdomadaire A1 du plan de formation (S1→S20) et conserve la structure du modèle de progression.
---

## 🧩 Principes structurants

- Maths **100% contextualisées** : chaque notion est reliée à un problème informatique concret (adressage, règles de filtrage, logs, dimensionnement).
- Progressivité renforcée : démarrage par les fondamentaux (numération + masques), puis algorithmique, puis synthèse et automatisation légère.
- Spirale de compétences : le subnetting revient à plusieurs reprises (bases → VLSM → VLSM multi-sites + projet).
- Rigueur attendue : méthode écrite (étapes), contrôle de cohérence, justification des résultats.
- Préparation examen : entraînements réguliers + synthèses + simulation en S20.
---

## 🧾 Légende

- 🔎 Notions / Compréhension (cours + exercices guidés)
- 🛠️ Entraînement appliqué (cas IT / mini-problèmes contextualisés)
- 🧭 Préparation CCF (méthodo + sujets type)
- ✅ Évaluation
- ⭐ Projet intégré (liens directs avec le projet d’infrastructure A1)

---

# 🔵 PHASE 1 – Numération & premiers calculs réseau (S1 à S5)

| Semaine | Situation professionnelle | Compétences Maths/Algo (U2) | Statut | Livrable attendu |
|----------|---------------------------|-----------------------------|:------:|------------------|
| S1 | Décoder une adresse MAC et comprendre pourquoi le binaire est au cœur du numérique | Systèmes de numération (décimal/binaire/hexa) ; conversions guidées ; lien MAC/IP | 🔎 | Fiche “Conversions + usages (MAC/IP)” + série d’exercices corrigés |
| S2 | Estimer une capacité disque et convertir des volumes pour une commande de matériel | Conversions approfondies ; unités (bit/octet/Ko/Mo/Go/To) ; calculs de capacité | 🛠️ | Mini-tableau de conversion + 10 calculs contextualisés (stockage) |
| S3 | Comprendre une logique de filtrage “autoriser si…” (pare-feu) | Algèbre de Boole : AND/OR/NOT/XOR ; tables de vérité ; lecture de conditions | 🔎 | Table(s) de vérité + traduction d’une règle simple en logique |
| S4 | Créer un plan d’adressage simple : réseau / broadcast / plage | Masques : décimal ↔ CIDR ; calcul réseau/broadcast/hôtes ; exercices pas à pas | 🛠️ | Fiche méthode “Subnetting base” + 6 exercices corrigés |
| S5 | Découper un réseau pour 3 services (petite PME) | Introduction VLSM : découpage par tailles différentes ; plan d’adressage simple | 🛠️ | Plan d’adressage VLSM (3 services) + justification des choix |

> Contenus alignés sur A1 S1→S5 du plan de formation.
---

# 🟠 PHASE 2 – Algorithmique de base & subnetting opérationnel (S6 à S10)

| Semaine | Situation professionnelle | Compétences Maths/Algo (U2) | Statut | Livrable attendu |
|----------|---------------------------|-----------------------------|:------:|------------------|
| S6 | Écrire une procédure de contrôle qualité : “IP valide / non valide” | Intro algorithmique ; pseudo-code ; variables/types ; validation simple | 🛠️ | Pseudo-code “validation IPv4” + jeux de tests |
| S7 | Vérifier si une IP appartient à un sous-réseau donné | Conditions (Si/Alors/Sinon) ; calcul d’appartenance à un sous-réseau ; méthode | 🛠️ | Procédure + 8 cas “appartient / n’appartient pas” |
| S8 | Générer automatiquement les IP utilisables d’un sous-réseau | Boucles (Pour/Tant que) ; parcours ; génération de plages d’adresses | 🛠️ | Algo + tableau d’IPs générées (exemples) |
| S9 | Calculer rapidement le nombre d’hôtes disponibles à partir d’un masque | Fonctions/procédures ; paramètres/retour ; calcul “nombre d’hôtes” depuis CIDR | 🛠️ | Fonction (pseudo-code) “nb_hotes(cidr)” + validation |
| S10 | Préparer un mini-contrôle : subnetting + algo | Tableaux/listes (structures simples) ; synthèse subnetting + algo ; premières exigences CCF | ✅ | Éval formative 1 (subnetting + algo de base) |

> Contenus alignés sur A1 S6→S10 du plan de formation.

---

# 🟡 PHASE 3 – Manipulations, tri, logique avancée & complexité (S11 à S15)

| Semaine | Situation professionnelle | Compétences Maths/Algo (U2) | Statut | Livrable attendu |
|----------|---------------------------|-----------------------------|:------:|------------------|
| S11 | Trier une liste de serveurs par charge CPU pour prioriser une intervention | Algorithmes de tri : bulle, insertion (pseudo-code) ; critères de tri | 🛠️ | 2 tris en pseudo-code + comparaison (cas “serveurs”) |
| S12 | Extraire des infos d’un log simple (date, IP, code erreur) | Chaînes de caractères : extraction/concaténation ; parsing simple | 🛠️ | Procédure “parser_log” + exemples d’entrées/sorties |
| S13 | Raisonner sur des groupes AD (union/intersection) pour des droits | Ensembles/relations : appartenance, union, intersection ; modélisation | 🔎 | Schémas d’ensembles + exercices “groupes AD” |
| S14 | Formaliser des règles de filtrage et vérifier leur cohérence | Logique du 1er ordre : prédicats/quantificateurs (niveau intuitif) ; règles | 🔎 | 6 règles de filtrage formalisées + test de cohérence |
| S15 | Choisir une méthode de recherche adaptée (linéaire vs dichotomique) | Complexité intuitive : O(n), O(n²) ; comparaison recherche linéaire/dichotomique | 🧭 | Tableau comparatif + mini-sujet type CCF “choix d’algo” |

> Contenus alignés sur A1 S11→S15 du plan de formation.
---

# 🟢 PHASE 4 – Synthèse, VLSM avancé, dimensionnement & CCF (S16 à S20)

| Semaine | Situation professionnelle | Compétences Maths/Algo (U2) | Statut | Livrable attendu |
|----------|---------------------------|-----------------------------|:------:|------------------|
| S16 | Dimensionner un transfert (temps, débit, latence) et finaliser un VLSM multi-sites | Subnetting avancé : VLSM multi-sites ; calculs débit/latence/temps de transfert | 🛠️ | Feuille d’exercices “VLSM avancé + débit/latence” corrigée |
| S17 | ⭐ Projet 1 : établir le plan d’adressage complet d’une PME (VLANs + services) | Application projet : plan d’adressage complet ; cohérence réseau/broadcast/plages ; justification | ⭐ | Dossier “Plan d’adressage Projet 1” (table + justification) |
| S18 | Construire un diagnostic réseau structuré | Arbres de décision : représentation d’un diagnostic ; logique de test ; synthèse numération/subnetting | 🛠️ | Arbre de décision + cas “diagnostic ping/DNS/DHCP” |
| S19 | Réviser efficacement en conditions type examen | Révisions : Boole, subnetting, algorithmique ; préparation CCF (exercices type) | 🧭 | Pack “Révisions générales + sujets type CCF” |
| S20 | 📝 Examen blanc : simulation CCF Maths (U2) | Épreuve blanche CCF : méthode, rigueur, gestion du temps ; correction guidée | ✅ | Copie évaluée + grille de critères + axes de progrès |

> Contenus alignés sur A1 S16→S20 du plan de formation.

---

# 🏆 Attendus opérationnels fin Année 1

## Compétences mathématiques & informatiques

- Convertir **décimal ↔ binaire ↔ hexadécimal** et interpréter une MAC / une IP
- Manipuler les **unités** (bits/octets/Ko/Mo/Go/To) et réaliser des calculs de capacité
- Utiliser l’**algèbre de Boole** pour comprendre/écrire une logique conditionnelle
- Réaliser des calculs **CIDR / masque / réseau / broadcast / plage d’hôtes**
- Concevoir un **plan d’adressage** simple puis **VLSM** (jusqu’au multi-sites niveau A1)
- Écrire des algorithmes en pseudo-code : **variables, conditions, boucles, fonctions**
- Manipuler **listes/tableaux/chaînes/ensembles** dans des situations IT
- Choisir une méthode (recherche/tri) et justifier simplement par la **complexité** (intuitive)
- Être prêt à une **simulation examen** : méthode + exactitude + justification

---

# 📋 Correspondance (Plan de formation) ↔ Progression Maths/Algo A1

| Thème U2 (A1) | Semaines concernées |
|--------------|---------------------|
| Numération (binaire/hexa) + conversions + unités | S1, S2 |
| Algèbre de Boole + tables de vérité | S3 |
| Subnetting de base (masques/CIDR, réseau/broadcast, plages) | S4 |
| VLSM (intro puis consolidation) | S5, S16, S17 |
| Algorithmique : intro, types, conditions, boucles, fonctions | S6 à S9 |
| Structures de données simples (listes/tableaux) | S10 |
| Tri / insertion / bulle (pseudo-code) | S11 |
| Chaînes (parsing log simple) | S12 |
| Ensembles (analogie groupes AD) | S13 |
| Logique du 1er ordre (appli filtrage) | S14 |
| Complexité intuitive + choix d’algo | S15 |
| Dimensionnement débit/latence/temps | S16, S17 |
| Arbres de décision (diagnostic) | S18 |
| Préparation CCF + révisions + simulation | S19, S20 |

---
