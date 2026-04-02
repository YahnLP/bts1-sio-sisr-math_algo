# 01 – Informations Générales

| **Champ** | **Détail** |
|-----------|-----------|
| **Semaine** | S4 — Année 1 |
| **Module** | Mathématiques pour l'Informatique — Algorithmique |
| **Durée totale** | 4 heures |
| **Public** | Apprentis BTS SIO SISR — quatrième semaine du module |
| **Modalité** | Présentiel — salle de cours avec tableau blanc |
| **Prérequis** | S1 (binaire), S2 (unités, octets), S3 (AND bit à bit, tables de vérité) |

---

## 🎯 Objectifs

À l'issue de cette séance, l'apprenant sera capable de :

**Masque de sous-réseau — Compréhension :**
- ✅ Définir ce qu'est un **masque de sous-réseau** et son rôle (délimiter réseau / hôte)
- ✅ Lire un masque en **notation décimale pointée** (255.255.255.0) et en **notation CIDR** (/24)
- ✅ Comprendre que le masque est un **nombre binaire de 32 bits** avec des 1 continus suivis de 0
- ✅ Convertir entre notation décimale et CIDR dans les deux sens

**Algorithmes de calcul réseau :**
- ✅ Calculer l'**adresse réseau** par l'opération AND bit à bit (IP AND masque)
- ✅ Calculer l'**adresse de broadcast** par l'algorithme NOT(masque) OR réseau
- ✅ Calculer la **plage d'hôtes** (première et dernière adresse utilisable)
- ✅ Calculer le **nombre d'hôtes** par la formule 2ⁿ − 2

**Exercices et applications :**
- ✅ Appliquer les algorithmes sur de nombreux exemples concrets
- ✅ Déterminer si deux hôtes appartiennent au **même sous-réseau**
- ✅ Lire et interpréter une notation CIDR courante (/8, /16, /24, /30)

---

## 🧠 Compétences travaillées

| **Code** | **Intitulé de la compétence** | **Niveau visé** |
|----------|-------------------------------|-----------------|
| **B2.1** | Exploiter des serveurs Windows et Linux (adressage réseau) | Application |
| **B2.2** | Exploiter des équipements réseau (sous-réseaux, routage) | Application |
| **B3.2** | Mettre en œuvre les mesures de sécurité de base (segmentation) | Fondement |

> 📌 Le calcul de sous-réseau est une compétence quotidienne du technicien SISR : configurer une interface réseau, vérifier si deux hôtes communiquent sans routeur, planifier un plan d'adressage. 

---
