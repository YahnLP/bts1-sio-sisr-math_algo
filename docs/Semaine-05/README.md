## Informations Générales

| **Champ** | **Détail** |
|-----------|-----------|
| **Semaine** | S5 — Année 1 |
| **Module** | Mathématiques pour l'Informatique — Algorithmique |
| **Durée totale** | 4 heures |
| **Public** | Apprentis BTS SIO SISR — cinquième semaine du module |
| **Modalité** | Présentiel — salle de cours avec tableau blanc |
| **Prérequis** | S1 à S4 complets — binaire, AND bit à bit, algorithme de sous-réseau, calcul réseau/broadcast/plage |

## Compétences RNCP Visées

| **Code** | **Intitulé de la compétence** | **Niveau visé** |
|----------|-------------------------------|-----------------|
| **B2.1** | Exploiter des serveurs Windows et Linux (adressage réseau) | Application avancée |
| **B2.2** | Exploiter des équipements réseau (sous-réseaux, plan d'adressage) | Application avancée |
| **B3.2** | Mettre en œuvre les mesures de sécurité de base (segmentation réseau) | Application |

> 📌 **S5 est la synthèse algorithmique du module réseau.** VLSM *(Variable Length Subnet Masking)* n'est pas une nouvelle notion — c'est l'algorithme de S4 appliqué de manière itérative et planifiée. L'enjeu n'est plus de "calculer un sous-réseau" mais de **concevoir une architecture réseau** en allouant l'espace d'adressage sans gaspillage. C'est la première vraie compétence de conception que vous allez acqurir dans le module.

---

## Objectifs Pédagogiques

À l'issue de cette séance, l'apprenant sera capable de :

**VLSM — Compréhension algorithmique :**
- ✅ Comprendre pourquoi le découpage en sous-réseaux de **taille identique** (FLSM) est gaspilleur
- ✅ Comprendre le principe de VLSM : **adapter le masque à la taille réelle du besoin**
- ✅ Maîtriser l'**algorithme VLSM en 4 étapes** (trier → calculer → allouer → vérifier)
- ✅ Identifier les **contraintes d'alignement** : un sous-réseau doit commencer à une adresse multiple de sa taille

**Plan d'adressage :**
- ✅ Construire un **plan d'adressage complet** pour une petite entreprise (3 services)
- ✅ Allouer les sous-réseaux dans l'ordre **du plus grand au plus petit** (règle fondamentale)
- ✅ Vérifier l'absence de **chevauchement** entre les sous-réseaux alloués
- ✅ Documenter le plan sous forme de **tableau professionnel**

**Application sécurité :**
- ✅ Relier la **segmentation VLSM** à la mesure de sécurité B3.2 (isolation des services)
- ✅ Comprendre que chaque sous-réseau peut faire l'objet de **règles de filtrage distinctes**

---
