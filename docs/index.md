# Mathématiques pour l'informatique - BTS SIO1

**SUP'ADOUR - MFR de Pontonx**

<p align="center">
  <img src="./images/logo-b1.png" width="500">
</p>

---

Bienvenue sur l'espace de ressources du BTS Services Informatique aux organisations Spécialité SISR.

# 🔐 BTS SIO – Option SISR  
## Mathématiques pour l'informatique — Année 1

> 🧠 *Modéliser, calculer, raisonner et automatiser : les maths utiles pour comprendre les réseaux, les systèmes et coder proprement.*

---

## 🎯 Objectifs de l’année 1 (Maths / Algo)

En première année, l’objectif est de construire un **socle solide en mathématiques pour l’informatique**, directement exploitable en SISR :

- Maîtriser les **systèmes de numération** (binaire / hexadécimal) et les **unités** (bit/octet, Ko/Mo/Go) utiles en informatique
- Réaliser les **calculs réseaux** indispensables (CIDR, masques, réseau/broadcast, plages d’IP, VLSM)
- Comprendre et utiliser la **logique** (tables de vérité, algèbre de Boole) pour les conditions, filtrages, règles
- Développer des bases d’**algorithmique** (variables, conditions, boucles, fonctions) et une méthode de résolution
- Manipuler des **structures de données simples** (listes/tableaux/chaînes/ensembles) dans des cas concrets IT
- Introduire la **complexité** (choisir un tri/une recherche, comparer des solutions) et justifier un choix
- S’entraîner à produire des solutions **rigoureuses** (méthode, justification, vérification), en vue des évaluations

> Référentiel de progression utilisé : colonne “Maths/Algo (A1)” du plan Année 1 (S1 → S20).

---

## 🗓️ Déroulé de l’année (Année 1) — Progression par semaines

> Le tableau ci-dessous reprend **toutes les séances S1 à S20** de l’Année 1 pour le module **Maths / Algo**.

| Phase | Sem. | Thèmes / notions (Maths / Algo) | Activités / productions attendues |
|------:|:----:|----------------------------------|-----------------------------------|
| **Phase 1 – Fondamentaux numériques & réseaux** | **S1** | **Numération** : décimal ↔ binaire ↔ hexadécimal. Lecture d’octets, conversions rapides. | Exercices guidés de conversion + mini-fiche méthode “binaire/hexa” (à conserver). |
|  | **S2** | **Unités informatiques** : bit/octet, KiB/MiB/GiB, débits (Mb/s) vs volumes (MB). | Problèmes contextualisés (stockage / transfert) + tableau de conversion + contrôles de cohérence. |
|  | **S3** | **Logique & tables de vérité** : AND/OR/NOT, implication intuitive, conditions composées. | Construire et lire des tables de vérité + traduire des règles simples (“si… alors…”) en logique. |
|  | **S4** | **Adressage IPv4 (1)** : masque, CIDR, réseau, broadcast, hôtes utilisables. | Fiche méthode “calcul réseau/broadcast” + 6 exercices corrigés (pas à pas). |
|  | **S5** | **Adressage IPv4 (2)** : tailles de sous-réseaux, découpage simple. Introduction **VLSM** (niveau 1). | Mini-cas “PME 3 services” : plan d’adressage + justification + vérification (cohérence). |
| **Phase 2 – Algorithmique de base appliquée à l’IT** | **S6** | **Introduction à l’algorithmique** : variables, types, entrées/sorties, pseudo-code propre. | Écrire une procédure “valider une IPv4” (forme algorithmique) + jeux de tests. |
|  | **S7** | **Conditions** : Si / Alors / Sinon, conditions composées. Cas réseau : appartenance à un sous-réseau. | Exercices “appartient / n’appartient pas” + explication écrite de la méthode. |
|  | **S8** | **Boucles** : Pour / Tant que. Parcours et génération de données (plages IP). | Algo : générer une plage IP utilisable + tableau d’exemples + tests sur 2 sous-réseaux. |
|  | **S9** | **Fonctions / procédures** : paramètres, retour. Automatiser un calcul (hôtes, réseau). | Écrire 2 fonctions : `nb_hotes(cidr)` et `reseau(ip,cidr)` (pseudo-code) + validation sur cas. |
|  | **S10** | **Synthèse (1)** : numération + subnetting + algo (bases). | Évaluation formative : conversions + subnetting + pseudo-code (méthode attendue + justification). |
| **Phase 3 – Données, tri/recherche, logique avancée & complexité** | **S11** | **Listes / tableaux** : indices, parcours, agrégations (max/min/somme). Cas IT : inventaire matériel. | Algo : trouver le poste le plus “lourd” (RAM/CPU) + tableau d’inventaire + justification. |
|  | **S12** | **Chaînes de caractères** : découper, extraire, nettoyer (parsing simple). Cas : logs. | Mini-parser de log (pseudo-code) + exemples entrée/sortie + règles de validation. |
|  | **S13** | **Ensembles & relations** : appartenance, union, intersection, complément. Cas : groupes / droits. | Schémas d’ensembles + exercices “groupes AD” (qui a accès à quoi ?) + correction argumentée. |
|  | **S14** | **Algèbre de Boole (approfond.)** : simplification intuitive, conditions de filtrage (règles). | Traduire 6 règles (pare-feu / ACL) en logique + vérifier cohérence (cas qui passe / bloque). |
|  | **S15** | **Recherche & complexité** : linéaire vs dichotomique, tri (bulle/insertion) + coût intuitif. | Comparer 2 méthodes (vitesse/volume) + petit sujet “choisir la bonne méthode et justifier”. |
| **Phase 4 – Consolidation, VLSM avancé & préparation évaluations** | **S16** | **VLSM avancé** : multi-sous-réseaux, multi-sites (niveau A1). + Calculs de débit/temps de transfert. | Cas complet : plan VLSM + dimensionnement simple (temps de copie) + contrôles de cohérence. |
|  | **S17** | **Projet 1 (plan d’adressage)** : VLANs, services, cohérence globale. | Dossier “Plan d’adressage” : table complète + explications (choix CIDR, plages, réservations). |
|  | **S18** | **Arbres de décision** : structurer un diagnostic (tests, branches, conclusions). | Construire un arbre “panne réseau” (DNS/DHCP/ping) + 2 scénarios résolus. |
|  | **S19** | **Révisions guidées** : méthodes incontournables (subnetting, conversions, logique, algo). | Pack d’entraînement (exercices type) + auto-correction + axes de progrès personnels. |
|  | **S20** | **Évaluation de synthèse** : situation professionnelle complète (réseau + algo + justification). | Examen blanc : calculs + pseudo-code + interprétation + grille de critères + correction détaillée. |

---

## 🧪 Évaluations (Année 1)

- **Formatives** : conversions, unités, tables de vérité, exercices de subnetting, mini-algos (pseudo-code).
- **Pratiques** : plans d’adressage (cas PME), VLSM, génération de plages IP, parsing simple de logs.
- **Méthodologiques** : justification, vérification (cohérence réseau/broadcast/plage), rédaction claire des étapes.
- **Synthèse** : examen blanc (S20) sur une situation complète “réseau + logique + algorithmique”.

---

## 🧰 Livrables attendus (à conserver pour le portfolio)

- Fiche méthode “Conversions binaire / hexa + unités”
- Fiche méthode “Calcul réseau / broadcast / plage d’hôtes (CIDR)”
- Plans d’adressage (cas PME + VLSM + projet VLANs)
- Algorithmes en pseudo-code : validation IPv4, appartenance sous-réseau, génération de plage, fonctions de calcul
- Schémas / tables : tables de vérité, ensembles (groupes/droits), règles logiques (filtrage)
- Arbre de décision “diagnostic réseau”
- Pack de révision (S19) + bilan personnel (axes de progrès)

---

## 🏆 Clés de réussite (Année 1)

| À faire régulièrement | Pourquoi |
|---|---|
| S’entraîner au **subnetting** (un peu chaque semaine) | C’est une compétence pivot en SISR (réseau, projets, dépannage) |
| Écrire une **méthode** (étapes) avant de calculer | Réduit les erreurs et facilite la justification en évaluation |
| Vérifier systématiquement (cohérence réseau/broadcast/plage) | Les erreurs “bêtes” coûtent cher ; la vérification est une compétence pro |
| Faire le lien entre logique/conditions et cas IT (ACL, règles) | Rend l’algo plus naturel et utile pour filtrage/décision |
| Documenter ses solutions (claires, propres, testées) | Attendu en entreprise et valorisable en portfolio |

---

## 🔄 Mises à jour

En cas de problème technique ou de lien inaccessible, le signaler directement à l’enseignant.

---

<div align="center">

Formation professionnalisante orientée expertise technique, autonomie et réussite aux épreuves du BTS SIO

<br>

✍️ YAHN LE PRETTRE
</div>
```
