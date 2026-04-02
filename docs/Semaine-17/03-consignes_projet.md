---
author: YLP
title: 📝 PROJET
---

# 📝 PROJET
## Dimensionnement Réseau PME TechServices

---

## ℹ️ Informations Générales

| **Champ** | **Détail** |
|-----------|-----------|
| **À rendre pour** | Fin de la séance S17 (présentation orale) |
| **Format** | Document PDF + Présentation orale (10 min) |
| **Modalité** | Travail en binôme |
| **Durée** | 4 heures de travail encadré |
| **Notation** | /100 points |

---

## 🎯 Objectifs du Projet

Ce projet a pour but de :
- ✅ Concevoir un **plan d'adressage IP complet** pour une PME
- ✅ Dimensionner la **bande passante** réseau nécessaire
- ✅ Calculer les besoins en **stockage** (production + sauvegardes)
- ✅ Produire un **livrable professionnel** pour le portfolio E4/E5
- ✅ Présenter et **justifier** vos choix techniques

---

## 📋 Consignes Générales

### Travail Attendu

**Vous devez produire :**

1. **Un document de synthèse** (format PDF, 10-15 pages) contenant :
   - Page de garde professionnelle
   - Sommaire
   - Présentation du contexte (PME TechServices)
   - Plan d'adressage IP complet (tableau + schéma)
   - Calculs de bande passante détaillés
   - Calculs de stockage détaillés
   - Recommandations finales
   - Conclusion

2. **Une présentation orale** (10 minutes) devant la classe :
   - Support PowerPoint/PDF (5-8 slides)
   - Présentation du projet
   - Justification des choix techniques
   - Réponses aux questions

### Structure du Document

```
═══════════════════════════════════════════════════════════════
STRUCTURE DU DOCUMENT DE SYNTHÈSE
═══════════════════════════════════════════════════════════════

1. PAGE DE GARDE
   - Titre : "Dimensionnement Réseau PME TechServices"
   - Noms des étudiants
   - Date
   - BTS SIO SISR — Année 1 — S17

2. SOMMAIRE
   - Liste des sections avec numéros de page

3. INTRODUCTION (1 page)
   - Présentation de TechServices
   - Contexte du projet
   - Objectifs

4. PLAN D'ADRESSAGE IP (3-4 pages)
   - Identification des VLAN
   - Tableau récapitulatif des sous-réseaux
   - Schéma réseau complet
   - Justification des choix de masques

5. DIMENSIONNEMENT BANDE PASSANTE (2-3 pages)
   - Applications identifiées
   - Calculs par VLAN
   - Calcul de la bande passante totale
   - Recommandation connexion Internet
   - Dimensionnement des switchs

6. DIMENSIONNEMENT STOCKAGE (2-3 pages)
   - Quotas utilisateurs
   - Partages réseau
   - Serveurs et BDD
   - Application règle 3-2-1
   - Total avec sauvegardes
   - Comparaison local vs cloud

7. RECOMMANDATIONS (1-2 pages)
   - Matériel recommandé (switchs, routeur, stockage)
   - Planning de déploiement
   - Budget estimé (optionnel)
   - Anticipation croissance

8. CONCLUSION (1 page)
   - Synthèse des résultats
   - Points d'attention
   - Perspectives

═══════════════════════════════════════════════════════════════
```

---

## 🗂️ PARTIE 1 : PLAN D'ADRESSAGE IP (30 points)

### Consignes

**Objectif :** Concevoir un plan d'adressage IP complet pour TechServices.

**Étapes à suivre :**

1. **Identifier les VLAN nécessaires** (au moins 7) :
   - VLAN utilisateurs (par service)
   - VLAN serveurs
   - VLAN DMZ (si applicable)
   - VLAN IoT (imprimantes, téléphones)

2. **Estimer le nombre d'hôtes** par VLAN :
   - Nombre actuel
   - Croissance +20% sur 3 ans
   - Marge de sécurité +30%

3. **Choisir les masques** de sous-réseau adaptés

4. **Attribuer les plages d'adresses** IP :
   - Partir d'un réseau privé (10.0.0.0/16 ou 172.16.0.0/16)
   - Allouer les sous-réseaux du plus grand au plus petit

5. **Créer le tableau récapitulatif** :

| **VLAN** | **Nom** | **Réseau** | **Masque** | **1ère IP** | **Dernière IP** | **Broadcast** | **Hôtes** |
|---|---|---|---|---|---|---|---|
| 10 | ... | ... | /... | ... | ... | ... | ... |

6. **Dessiner le schéma réseau** avec :
   - Routeur/pare-feu
   - Switchs
   - VLAN avec leurs adresses
   - Serveurs principaux

### Livrables Attendus

- ✅ Tableau complet des VLAN (Excel ou LibreOffice Calc)
- ✅ Schéma réseau (Draw.io, Lucidchart, ou Packet Tracer)
- ✅ Justification des choix de masques (2-3 paragraphes)

---

## 📊 PARTIE 2 : DIMENSIONNEMENT BANDE PASSANTE (25 points)

### Consignes

**Objectif :** Calculer la bande passante nécessaire pour chaque VLAN et dimensionner la connexion Internet.

**Étapes à suivre :**

1. **Lister les applications** utilisées (voir cahier des charges)

2. **Estimer le débit par utilisateur** pour chaque application

3. **Calculer la bande passante par VLAN** :
   ```
   BP VLAN = Σ (Nb users × Débit/user × Taux simultanéité)
   ```

4. **Ajouter une marge** :
   - +30% par VLAN (variations)
   - +50% sur le total (pics d'utilisation)

5. **Dimensionner la connexion Internet** :
   - Recommander un débit (100 Mbps, 300 Mbps, 1 Gbps...)
   - Justifier le choix

6. **Dimensionner les liens internes** (optionnel pour profils avancés) :
   - Switchs accès → distribution
   - Switchs distribution → core

### Livrables Attendus

- ✅ Tableau de calculs par VLAN
- ✅ Calcul de la bande passante totale
- ✅ Recommandation connexion Internet justifiée

### Tableau de Calculs (Exemple)

| **VLAN** | **App 1** | **App 2** | **App 3** | **Total** | **Avec marge** |
|---|---|---|---|---|---|
| Développement | 32 Mbps | 5 Mbps | 36 Mbps | 73 Mbps | 95 Mbps |
| Support | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| **TOTAL** | — | — | — | **XXX Mbps** | **YYY Mbps** |

---

## 💾 PARTIE 3 : DIMENSIONNEMENT STOCKAGE (20 points)

### Consignes

**Objectif :** Calculer le stockage nécessaire (production + sauvegardes) et choisir entre local et cloud.

**Étapes à suivre :**

1. **Calculer les quotas utilisateurs** :
   - Par profil (Direction, Devs, Support, Commercial, IT)
   - Mail + Home

2. **Estimer les partages réseau** :
   - Par service
   - Données communes

3. **Estimer les serveurs et BDD** :
   - Bases de données
   - Serveurs applicatifs

4. **Calculer le total production** :
   ```
   Total = Quotas + Partages + Serveurs
   ```

5. **Appliquer la règle 3-2-1** :
   ```
   Stockage total = Production × 3
   ```

6. **Anticiper la croissance** (3 ans) :
   ```
   Année 0, 1, 2, 3 : ×1.5 chaque année
   ```

7. **Comparer local vs cloud** (avantages/inconvénients)

### Livrables Attendus

- ✅ Tableau de calculs détaillé
- ✅ Application de la règle 3-2-1
- ✅ Projection sur 3 ans
- ✅ Comparaison local vs cloud (1 page)

### Tableau de Calculs (Exemple)

| **Catégorie** | **Détail** | **Taille** |
|---|---|---|
| **Quotas utilisateurs** | 50 users × quotas | XXX Go |
| **Partages réseau** | 4 partages | XXX Go |
| **Serveurs/BDD** | CRM + ERP + Web | XXX Go |
| **TOTAL Production** | — | **XXX Go** |
| **Sauvegardes (3-2-1)** | ×3 | **XXX Go** |
| **TOTAL FINAL** | — | **XXX Go = XX To** |

---

## 🎤 PARTIE 4 : PRÉSENTATION ORALE (10 points)

### Consignes

**Durée :** 10 minutes maximum

**Support :** PowerPoint ou PDF (5-8 slides)

**Contenu :**
1. Présentation du contexte (1 slide)
2. Plan d'adressage IP (2 slides : tableau + schéma)
3. Bande passante (1 slide : résultats)
4. Stockage (1 slide : résultats + règle 3-2-1)
5. Recommandations finales (1 slide)
6. Questions/réponses (3-5 min)

**⚠️ Important :** Les deux membres du binôme doivent parler.

---

## 📄 PARTIE 5 : QUALITÉ DU DOCUMENT (15 points)

### Critères de Qualité

**Forme (5 points) :**
- ✅ Page de garde professionnelle
- ✅ Sommaire avec pagination
- ✅ Mise en page soignée (marges, polices, couleurs)
- ✅ Pas de fautes d'orthographe

**Tableaux et Schémas (5 points) :**
- ✅ Tableaux clairs et lisibles
- ✅ Schéma réseau professionnel (pas un brouillon)
- ✅ Légendes explicites

**Rigueur (5 points) :**
- ✅ Calculs détaillés et justifiés
- ✅ Sources citées (si applicable)
- ✅ Cohérence globale du document

---

## 📊 GRILLE D'ÉVALUATION DÉTAILLÉE

### Plan d'Adressage IP (30 points)

| **Critère** | **Points** | **Description** |
|---|---|---|
| Identification des VLAN | 5 | Tous les groupes logiques identifiés |
| Estimation nb d'hôtes | 5 | Calculs avec croissance + marge |
| Choix des masques | 10 | Masques adaptés aux besoins |
| Attribution des plages | 5 | Plages correctement allouées |
| Schéma réseau | 5 | Schéma clair, complet, professionnel |

### Bande Passante (25 points)

| **Critère** | **Points** | **Description** |
|---|---|---|
| Applications identifiées | 3 | Liste complète des applications |
| Calculs par VLAN | 10 | Formules correctes, détails |
| Marge pour les pics | 4 | Marge de 30-50% appliquée |
| Recommandation Internet | 5 | Débit justifié et cohérent |
| Dimensionnement switchs | 3 | Liens internes (optionnel) |

### Stockage (20 points)

| **Critère** | **Points** | **Description** |
|---|---|---|
| Quotas utilisateurs | 4 | Par profil, mail + home |
| Partages et serveurs | 4 | Estimations justifiées |
| Règle 3-2-1 | 5 | Correctement appliquée |
| Croissance anticipée | 4 | Projection sur 3 ans |
| Local vs cloud | 3 | Comparaison argumentée |

### Présentation Orale (10 points)

| **Critère** | **Points** | **Description** |
|---|---|---|
| Clarté de l'exposé | 4 | Bien structuré, compréhensible |
| Maîtrise du sujet | 4 | Réponses aux questions pertinentes |
| Support visuel | 2 | Slides claires et professionnelles |

### Qualité du Document (15 points)

| **Critère** | **Points** | **Description** |
|---|---|---|
| Forme professionnelle | 5 | Page de garde, sommaire, mise en page |
| Tableaux et schémas | 5 | Clarté, lisibilité, légendes |
| Rigueur et cohérence | 5 | Calculs justifiés, pas d'incohérences |

**TOTAL : 100 points**

---

## 🎯 Conseils pour Réussir

### Organisation du Travail

**Jalons horaires à respecter :**
- H+1:30 : Plan d'adressage IP **terminé** ✅
- H+2:45 : Bande passante **terminée** ✅
- H+3:35 : Stockage **terminé** ✅
- H+3:50 : Document **finalisé** ✅

**⚠️ Si retard :** Passer à l'étape suivante quand même. Mieux vaut un projet complet avec moins de détails qu'un projet incomplet.

### Répartition des Rôles

**Binôme :**
- Étudiant 1 : Responsable Plan IP + Stockage
- Étudiant 2 : Responsable Bande Passante + Schéma réseau

**Mais :** Validation croisée (chacun vérifie le travail de l'autre).

### Utilisation des Outils

**Tableur (Excel/Calc) :**
- Créer un fichier avec plusieurs onglets :
  - Onglet 1 : Plan IP
  - Onglet 2 : Bande passante
  - Onglet 3 : Stockage
- Utiliser des formules pour automatiser les calculs

**Schéma (Draw.io recommandé) :**
- Utiliser les formes prédéfinies (routeur, switch, serveur)
- Ajouter les VLAN avec leurs adresses IP
- Utiliser des couleurs pour différencier les zones

---

## 📅 Intégration au Portfolio E4/E5

**Ce projet est un élément MAJEUR de votre portfolio.**

**Compétences démontrées :**
- ✅ **B1.1** : Gestion du patrimoine (plan d'adressage)
- ✅ **B2.1** : Administration réseau (dimensionnement)
- ✅ **B2.3** : Proposition d'amélioration (recommandations)
- ✅ **B3.1** : Protection des données (segmentation, sauvegardes)

**Traces à conserver :**
- Document de synthèse complet (PDF)
- Schéma réseau (PNG/PDF)
- Tableur de calculs (XLSX/ODS)
- Slides de présentation (PDF)

**Utilisation en E4/E5 :**
- Présenter ce projet comme une **étude de cas complète**
- Expliquer la méthodologie utilisée
- Justifier les choix techniques
- Montrer la rigueur des calculs

---

## 💬 FAQ (Questions Fréquentes)

**Q1 : Peut-on choisir un autre réseau que 10.0.0.0 ou 172.16.0.0 ?**
R : Oui, tant que c'est un réseau privé (RFC 1918). Vous pouvez aussi utiliser 192.168.0.0/16.

**Q2 : Combien de VLAN minimum ?**
R : Au moins 7 VLAN pour couvrir tous les groupes logiques identifiés.

**Q3 : Faut-il chiffrer le budget matériel ?**
R : C'est optionnel. Si vous le faites, c'est un bonus. Sinon, pas de pénalité.

**Q4 : Peut-on utiliser Packet Tracer pour le schéma ?**
R : Oui, c'est même recommandé si vous êtes à l'aise avec l'outil.

**Q5 : Quelle longueur pour le document ?**
R : 10-15 pages est l'idéal. Moins de 8 pages = trop court. Plus de 20 pages = trop verbeux.

**Q6 : Les deux membres du binôme doivent-ils présenter ?**
R : Oui, absolument. Répartissez-vous les slides.

