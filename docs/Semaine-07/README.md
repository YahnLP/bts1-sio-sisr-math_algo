# 01 – Objectifs et ressources

---

## Informations Générales

| **Champ** | **Détail** |
|-----------|-----------|
| **Semaine** | S7 — Année 1 |
| **Module** | Mathématiques pour l'Informatique — Algorithmique |
| **Durée totale** | 4 heures |
| **Public** | Apprentis BTS SIO SISR — septième semaine du module |
| **Modalité** | Présentiel — salle de cours avec tableau blanc |
| **Prérequis** | S1–S6 complets — binaire, AND/OR/NOT, masques de sous-réseau, VLSM, pseudo-code, variables et types |

---

## Compétences RNCP Visées

| **Code** | **Intitulé de la compétence** | **Niveau visé** |
|----------|-------------------------------|-----------------|
| **B2.1** | Exploiter des serveurs Windows et Linux (scripting, automatisation) | Application |
| **B2.2** | Exploiter des équipements réseau (filtrage, décision réseau) | Application |
| **B3.2** | Mettre en œuvre les mesures de sécurité de base (règles, contrôle d'accès) | Application |

> 📌 **S7 approfondit la structure algorithmique la plus fondamentale : la décision.** Si S6 a introduit le SI comme une structure parmi d'autres, S7 en fait le sujet central, avec toutes ses formes (simple, double, multiple, imbriquée) et ses pièges. L'exercice d'appartenance à un sous-réseau est idéal : il exige une chaîne de conditions imbriquées qui mobilise simultanément les calculs de S4 et la logique de S3 dans un cadre algorithmique formalisé.

---

## Objectifs Pédagogiques

À l'issue de cette séance, l'apprenant sera capable de :

**Structures conditionnelles — Maîtrise complète :**
- ✅ Maîtriser la **forme simple** (SI...ALORS...FIN SI) et la **forme complète** (SI...ALORS...SINON...FIN SI)
- ✅ Maîtriser les **conditions multiples** (SINON SI) pour éviter les SI imbriqués inutiles
- ✅ Maîtriser les **conditions imbriquées** et comprendre quand les utiliser vs. conditions multiples
- ✅ Construire des **conditions composées** avec ET/OU/NON (lien S3 — Boole)
- ✅ Identifier et corriger les **antipatterns** : condition redondante, SI sans SINON, double négation inutile

**Application réseau :**
- ✅ Formaliser en pseudo-code l'**algorithme d'appartenance** d'une IP à un sous-réseau
- ✅ Étendre l'algorithme à la **classification d'une IP** dans un plan d'adressage multi-sous-réseaux
- ✅ Comprendre le lien entre structure conditionnelle et **politique de routage / filtrage pare-feu**

