# 01 – Objectifs et ressources

## Informations Générales

| **Champ** | **Détail** |
|-----------|-----------|
| **Semaine** | S9 — Année 1 |
| **Module** | Mathématiques pour l'Informatique — Algorithmique |
| **Durée totale** | 4 heures |
| **Public** | Apprentis BTS SIO SISR — neuvième semaine du module |
| **Modalité** | Présentiel — salle de cours avec tableau blanc |
| **Prérequis** | S6–S8 complets — pseudo-code, types, SI/SINON, boucles, utilisation implicite de fonctions comme `ValiderIPv4`, `IP_VERS_ENTIER`, `AppartientAuSousReseau` |

---

## Compétences Visées

| **Code** | **Intitulé de la compétence** | **Niveau visé** |
|----------|-------------------------------|-----------------|
| **B2.1** | Exploiter des serveurs Windows et Linux (scripting modulaire) | Application avancée |
| **B2.2** | Exploiter des équipements réseau (bibliothèque de fonctions réseau) | Application |
| **B3.2** | Mettre en œuvre les mesures de sécurité (factoriser les validations) | Application |

> 📌 Depuis S6, on a utilisé `ValiderIPv4`, `AppartientAuSousReseau`, `IP_VERS_ENTIER` comme des boîtes noires. S9 explique comment ces boîtes sont construites, et comment eux-mêmes peuvent en fabriquer. La fonction n'est pas un concept nouveau, c'est la formalisation de quelque chose de déjà vécu.

---

## Objectifs Pédagogiques

**Fonctions et procédures — Fondements :**
- ✅ Distinguer **fonction** (retourne une valeur) et **procédure** (produit un effet sans retour)
- ✅ Maîtriser la notion de **paramètre** : paramètre formel (dans la définition) vs. argument (à l'appel)
- ✅ Comprendre la **portée locale** des variables déclarées à l'intérieur d'une fonction
- ✅ Maîtriser le mécanisme de **retour** (`RETOURNER`) et son effet immédiat sur le flux d'exécution
- ✅ Comprendre pourquoi la modularité améliore la lisibilité, la réutilisabilité et la maintenabilité

**Application — Bibliothèque réseau :**
- ✅ Écrire `NombreHotes(cidr)` qui calcule 2^(32−cidr) − 2 avec précondition et valeur sentinelle
- ✅ Écrire `CalculerBroadcast(ip, cidr)` en réutilisant les fonctions existantes de la bibliothèque
- ✅ Refactoriser `GenererIPsReseau` (S8) pour déléguer ses calculs aux nouvelles fonctions
- ✅ Comprendre le concept de **bibliothèque de fonctions** comme modèle professionnel

---
