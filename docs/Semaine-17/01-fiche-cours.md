---
author: YLP
title: 📖 Fiche de Cours
---

# 📚 FICHE DE COURS ÉLÈVE
## Méthodologie de Dimensionnement Réseau

*BTS SIO SISR — Année 1 — Semaines 17*

---

## 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|----------------|
| **B1.1** | Gérer le patrimoine informatique |
| **B2.1** | Administrer les systèmes et les services informatiques |
| **B2.3** | Proposer des améliorations d'un service |
| **B3.1** | Protéger les données à caractère personnel |

---

## 📖 I. Introduction : Qu'est-ce que le Dimensionnement Réseau ?

### Définition

> Le **dimensionnement réseau** est le processus d'estimation des ressources nécessaires pour une infrastructure informatique : adresses IP, bande passante, stockage.

**Objectifs :**
- ✅ **Satisfaire les besoins** actuels et futurs
- ✅ **Optimiser les coûts** (ni trop, ni trop peu)
- ✅ **Anticiper la croissance** (scalabilité)
- ✅ **Garantir les performances** (pas de goulot d'étranglement)

### Les 3 Piliers du Dimensionnement

**1️⃣ Plan d'Adressage IP**
- Combien de réseaux / sous-réseaux ?
- Combien d'hôtes par réseau ?
- Quelle architecture (VLAN, hiérarchie) ?

**2️⃣ Bande Passante**
- Combien de Mbps/Gbps nécessaires ?
- Quels sont les pics d'utilisation ?
- Quels liens dimensionner (Internet, LAN, WAN) ?

**3️⃣ Stockage**
- Combien de Go/To nécessaires ?
- Où stocker (local, cloud, hybride) ?
- Comment sauvegarder (règle 3-2-1) ?

![Illustration : Triangle avec "Plan IP" en haut, "Bande Passante" en bas à gauche, "Stockage" en bas à droite]
*Légende : Les 3 piliers du dimensionnement réseau sont interdépendants.*

---

## 🗺️ II. Méthodologie : Plan d'Adressage IP

### Étape 1 : Identifier les Groupes Logiques

**Qu'est-ce qu'un groupe logique ?**
Un ensemble d'équipements qui partagent une **fonction commune** et doivent être dans le **même réseau**.

**Exemples de groupes :**
- 👥 Utilisateurs par service (Direction, RH, IT, Devs, Support...)
- 🖥️ Serveurs (Production, Développement, DMZ)
- 📱 Équipements IoT (Imprimantes, téléphones IP, caméras)
- 🔗 Liens inter-sites (VPN, WAN)

**Recommandation :** 1 groupe logique = 1 VLAN = 1 sous-réseau

### Étape 2 : Estimer le Nombre d'Hôtes par Groupe

**Formule de base :**
```
Nombre d'hôtes = Nombre actuel × (1 + % croissance) + Marge
```

**Exemple :**
- Groupe "Développement" : 20 développeurs
- Croissance prévue : +20% sur 3 ans
- Calcul : 20 × 1.2 = 24 développeurs
- Marge de sécurité : 24 × 1.3 ≈ **31 hôtes**
- Masque recommandé : /26 (62 hôtes utilisables)

**⚠️ Règle d'or :** Toujours prévoir **30-50% de marge** au-delà de la croissance prévue.

### Étape 3 : Choisir les Masques de Sous-Réseau

**Tableau de référence :**

| **Hôtes nécessaires** | **Masque** | **CIDR** | **Hôtes utilisables** |
|---|---|---|---|
| 1-2 | 255.255.255.252 | /30 | 2 |
| 3-6 | 255.255.255.248 | /29 | 6 |
| 7-14 | 255.255.255.240 | /28 | 14 |
| 15-30 | 255.255.255.224 | /27 | 30 |
| 31-62 | 255.255.255.192 | /26 | 62 |
| 63-126 | 255.255.255.128 | /25 | 126 |
| 127-254 | 255.255.255.0 | /24 | 254 |

**Principe de choix :**
Choisir le masque qui offre **juste assez d'hôtes** pour couvrir les besoins + marge.

**Exemple :**
- Besoin : 31 hôtes → Choisir /26 (62 hôtes) ✅
- Ne PAS choisir /24 (254 hôtes) → gaspillage d'adresses ❌

### Étape 4 : Attribuer les Plages d'Adresses

**Méthode recommandée :**

1. **Choisir un réseau privé** (RFC 1918) :
   - 10.0.0.0/8 → Très grandes entreprises
   - 172.16.0.0/12 → PME/ETI
   - 192.168.0.0/16 → Petites structures

2. **Allouer les sous-réseaux** dans l'ordre (du plus grand au plus petit) :
   ```
   10.0.0.0/24    → VLAN Développement (254 hôtes)
   10.0.1.0/25    → VLAN Support (126 hôtes)
   10.0.1.128/26  → VLAN Commercial (62 hôtes)
   10.0.1.192/27  → VLAN Direction (30 hôtes)
   10.0.1.224/28  → VLAN IT (14 hôtes)
   ...
   ```

3. **Documenter dans un tableau** :

| **VLAN** | **Nom** | **Réseau** | **Masque** | **Première IP** | **Dernière IP** | **Broadcast** |
|---|---|---|---|---|---|---|
| 10 | Développement | 10.0.0.0 | /24 | 10.0.0.1 | 10.0.0.254 | 10.0.0.255 |
| 20 | Support | 10.0.1.0 | /25 | 10.0.1.1 | 10.0.1.126 | 10.0.1.127 |
| 30 | Commercial | 10.0.1.128 | /26 | 10.0.1.129 | 10.0.1.190 | 10.0.1.191 |

### Étape 5 : Créer le Schéma Réseau

**Éléments à inclure dans le schéma :**
- 🌐 Connexion Internet
- 🔥 Pare-feu
- 🔀 Routeur(s)
- 🔌 Switch(s) par niveau
- 📦 VLAN avec leurs plages d'adresses
- 🖥️ Serveurs principaux
- 🔗 Liaisons inter-sites (si applicable)

![Illustration : Schéma réseau hiérarchique simple avec Internet → Pare-feu → Routeur → Switchs → VLAN]
*Légende : Exemple de schéma réseau avec segmentation en VLAN.*

---

## 📊 III. Méthodologie : Calcul de Bande Passante

### Étape 1 : Identifier les Applications

**Lister toutes les applications** utilisées dans l'entreprise :
- Navigation web (HTTP/HTTPS)
- Email (IMAP/SMTP)
- CRM (SalesForce, HubSpot)
- ERP (SAP, Odoo)
- Visioconférence (Teams, Zoom)
- Partage de fichiers (SMB, NFS)
- VoIP (téléphonie IP)
- Sauvegardes (vers cloud)

### Étape 2 : Estimer le Débit par Utilisateur

**Tableau de référence (débits moyens) :**

| **Application** | **Débit/user (Mbps)** | **Usage** |
|---|---|---|
| Navigation web | 2 | Consultation sites, vidéos |
| Email | 0.5 | Envoi/réception avec PJ |
| CRM web | 1 | Interface web dynamique |
| Visioconférence HD | 5 | Vidéo 720p-1080p |
| Partage de fichiers | 3 | Lecture/écriture réseau |
| VoIP | 0.1 | Appels audio uniquement |

**⚠️ Attention :** Ces valeurs sont des **moyennes**. Les pics peuvent être 2-3× supérieurs.

### Étape 3 : Calculer la Bande Passante par VLAN

**Formule de base :**
```
Bande passante VLAN = Σ (Nb users × Débit app × Taux simultanéité)
```

**Exemple — VLAN Développement (20 users) :**

| **Application** | **Users** | **Débit/user** | **Simultanéité** | **Total** |
|---|---|---|---|---|
| Web | 20 | 2 Mbps | 80% | 20 × 2 × 0.8 = 32 Mbps |
| Email | 20 | 0.5 Mbps | 50% | 20 × 0.5 × 0.5 = 5 Mbps |
| Partage fichiers | 20 | 3 Mbps | 60% | 20 × 3 × 0.6 = 36 Mbps |
| Visio | 5 | 5 Mbps | 100% | 5 × 5 × 1 = 25 Mbps |
| **TOTAL** | — | — | — | **98 Mbps** |

**Avec marge de 30% :** 98 × 1.3 ≈ **130 Mbps**

### Étape 4 : Calculer la Bande Passante Totale

**Additionner tous les VLAN :**

| **VLAN** | **Bande passante** |
|---|---|
| Développement | 130 Mbps |
| Support | 80 Mbps |
| Commercial | 45 Mbps |
| Direction | 30 Mbps |
| IT | 60 Mbps |
| **TOTAL** | **345 Mbps** |

**Avec marge pour les pics (+50%) :** 345 × 1.5 ≈ **520 Mbps**

**Recommandation :** Connexion Internet **≥ 600 Mbps** (ou 1 Gbps pour anticiper)

### Étape 5 : Dimensionner les Liens Internes

**Recommandations :**
- 🔌 **Switch accès → distribution** : 1 Gbps (ou agrégation de liens)
- 🔌 **Switch distribution → core** : 10 Gbps (ou agrégation)
- 🔌 **Serveurs critiques** : 10 Gbps (ou 2× 1 Gbps en agrégation)

**Règle d'or :** Le réseau interne doit avoir **10× la bande passante Internet** pour éviter les goulots.

---

## 💾 IV. Méthodologie : Calcul de Stockage

### Étape 1 : Estimer les Quotas Utilisateurs

**Par profil utilisateur :**

| **Profil** | **Nombre** | **Mail** | **Home** | **Total/user** | **Total** |
|---|---|---|---|---|---|
| Direction | 5 | 10 Go | 50 Go | 60 Go | 300 Go |
| Développeur | 20 | 10 Go | 100 Go | 110 Go | 2200 Go |
| Technicien | 12 | 10 Go | 30 Go | 40 Go | 480 Go |
| Commercial | 8 | 10 Go | 20 Go | 30 Go | 240 Go |
| Admin IT | 5 | 10 Go | 200 Go | 210 Go | 1050 Go |
| **TOTAL** | **50** | — | — | — | **4270 Go** |

### Étape 2 : Estimer les Partages Réseau

**Partages communs par service :**

| **Partage** | **Taille estimée** |
|---|---|
| Partage Direction (docs RH, compta) | 200 Go |
| Partage Développement (code, projets) | 500 Go |
| Partage Support (docs clients, KB) | 300 Go |
| Partage Commercial (devis, contrats) | 100 Go |
| **TOTAL** | **1100 Go** |

### Étape 3 : Estimer les Serveurs et Bases de Données

**Serveurs métiers :**

| **Serveur** | **Type** | **Taille** |
|---|---|---|
| Base de données CRM | PostgreSQL | 200 Go |
| Base de données ERP | MySQL | 150 Go |
| Serveur web (sites clients) | Apache/Nginx | 50 Go |
| **TOTAL** | — | **400 Go** |

### Étape 4 : Calculer le Stockage de Production

```
TOTAL Production = Quotas users + Partages + BDD
                 = 4270 + 1100 + 400
                 = 5770 Go ≈ 5.8 To
```

### Étape 5 : Appliquer la Règle 3-2-1 (Sauvegardes)

**Règle 3-2-1 :**
- **3** copies des données (1 production + 2 sauvegardes)
- **2** supports différents (disques locaux + cloud)
- **1** copie hors site (protection contre sinistre)

**Application :**
```
Production : 5.8 To
Copie 1 (serveur principal) : déjà comptée
Copie 2 (serveur secondaire local) : 5.8 To
Copie 3 (cloud hors site) : 5.8 To

TOTAL stockage nécessaire = 5.8 + 5.8 + 5.8 = 17.4 To
```

**⚠️ Attention :** Avec la rétention (30 jours), le besoin peut être multiplié par 1.5-2×.

### Étape 6 : Anticiper la Croissance

**Règle empirique :** Les données doublent tous les 18-24 mois.

```
Année 0 : 17.4 To
Année 1 : 17.4 × 1.5 = 26 To
Année 2 : 26 × 1.5 = 39 To
Année 3 : 39 × 1.5 ≈ 60 To
```

**Recommandation :** Prévoir un stockage évolutif ou cloud pour absorber la croissance.

### Étape 7 : Comparer Local vs Cloud

**Stockage local (SAN/NAS) :**

| **Avantages** | **Inconvénients** |
|---|---|
| ✅ Performances élevées (IOPS) | ❌ Investissement initial élevé (CAPEX) |
| ✅ Contrôle total | ❌ Maintenance (matériel, pannes) |
| ✅ Pas de coût récurrent | ❌ Obsolescence (remplacer tous les 5 ans) |

**Stockage cloud (AWS S3, Azure Blob) :**

| **Avantages** | **Inconvénients** |
|---|---|
| ✅ Pas d'investissement initial | ❌ Coût récurrent (OPEX) |
| ✅ Scalabilité illimitée | ❌ Dépendance Internet |
| ✅ Réplication automatique | ❌ Coûts de sortie de données |

**Approche hybride (recommandée) :**
- 💾 **Production** : Local (SAN/NAS) pour les performances
- ☁️ **Sauvegardes** : Cloud pour la sécurité et la simplicité

---

## 🔑 V. Vocabulaire Clé à Maîtriser

| **Terme** | **Définition** |
|---|---|
| **VLAN** | Virtual LAN — Segmentation logique du réseau |
| **Sous-réseau** | Division d'un réseau IP en plusieurs réseaux plus petits |
| **Masque de sous-réseau** | Détermine la partie réseau et la partie hôte d'une IP |
| **Bande passante** | Débit maximum d'un lien réseau (en Mbps/Gbps) |
| **Taux de simultanéité** | Pourcentage d'utilisateurs actifs en même temps |
| **Quota** | Limite de stockage allouée à un utilisateur |
| **Règle 3-2-1** | 3 copies, 2 supports, 1 hors site (sauvegardes) |
| **CAPEX** | Capital Expenditure — Investissement initial |
| **OPEX** | Operational Expenditure — Coûts récurrents |
| **Scalabilité** | Capacité à évoluer facilement (croissance) |

---

## 🎯 VI. Points Clés à Retenir

### ✅ Les 5 Règles d'Or

1. **Toujours anticiper la croissance** : Prévoir +30-50% de marge au-delà des besoins actuels.

2. **Segmenter le réseau** : 1 VLAN par groupe logique (sécurité + performance).

3. **Calculer les pics, pas les moyennes** : La bande passante doit absorber les pics d'utilisation.

4. **Appliquer la règle 3-2-1** : 3 copies, 2 supports, 1 hors site (non négociable).

5. **Documenter rigoureusement** : Schémas, tableaux, justifications (traçabilité).

### ⚠️ Erreurs Fréquentes

❌ **Erreur 1 : Sous-dimensionner par économie**
```
"On a 20 users, on prend un /27 (30 hôtes)"
→ Problème : Aucune marge, impossible d'ajouter des hôtes
→ Solution : Prendre un /26 (62 hôtes) ou /25 (126 hôtes)
```

❌ **Erreur 2 : Oublier les pics d'utilisation**
```
"Bande passante moyenne = 50 Mbps"
→ Problème : Aux pics (9h, 14h), ça monte à 150 Mbps → saturation
→ Solution : Dimensionner pour le pic avec marge (+50%)
```

❌ **Erreur 3 : Négliger les sauvegardes**
```
"Stockage production = 5 To, on achète 5 To"
→ Problème : Pas de place pour les sauvegardes !
→ Solution : Appliquer 3-2-1 → besoin réel = 15 To minimum
```

---

## 📝 Fiche de Référence Rapide (Aide-Mémoire)

**À garder sous les yeux pendant le projet :**

```
═══════════════════════════════════════════════════════════════
DIMENSIONNEMENT RÉSEAU - AIDE-MÉMOIRE
═══════════════════════════════════════════════════════════════

PLAN D'ADRESSAGE
───────────────────────────────────────────────────────────────
1. Identifier les groupes logiques (VLAN)
2. Estimer nb d'hôtes = Actuel × 1.2 × 1.3 (croissance + marge)
3. Choisir masque adapté (juste assez d'hôtes)
4. Attribuer plages IP (du plus grand au plus petit)
5. Documenter dans un tableau
6. Dessiner le schéma réseau

BANDE PASSANTE
───────────────────────────────────────────────────────────────
1. Lister les applications
2. Estimer débit/user pour chaque app
3. Calculer par VLAN : Σ (users × débit × simultanéité)
4. Additionner tous les VLAN
5. Ajouter marge +50% pour les pics
6. Dimensionner Internet et liens internes

STOCKAGE
───────────────────────────────────────────────────────────────
1. Calculer quotas utilisateurs (mail + home)
2. Estimer partages réseau
3. Estimer bases de données
4. TOTAL production = quotas + partages + BDD
5. Appliquer 3-2-1 → ×3 pour sauvegardes
6. Anticiper croissance : ×2 tous les 18 mois

FORMULES CLÉS
───────────────────────────────────────────────────────────────
Hôtes avec marge = Actuel × 1.2 × 1.3
BP VLAN = Σ (users × débit/user × simultanéité) × 1.3
BP totale = Σ BP VLAN × 1.5
Stockage total = Production × 3 (règle 3-2-1)

═══════════════════════════════════════════════════════════════
```

---
