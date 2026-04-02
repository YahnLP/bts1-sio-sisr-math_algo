---
author: YLP
title: 📖 Cahier des Charges Projet
---

# 🎯 CAHIER DES CHARGES DU PROJET
## PME "TechServices" - Audit et Dimensionnement Réseau

---

## 📌 Objectif de l'Activité

**Mission :** Analyser le contexte de l'entreprise TechServices et identifier ses besoins en infrastructure réseau.

**Compétence ciblée :** Comprendre les besoins d'un client et les traduire en spécifications techniques.

---

## 🏢 PRÉSENTATION DE L'ENTREPRISE

### Identité

| **Champ** | **Détail** |
|-----------|-----------|
| **Nom** | TechServices SARL |
| **Secteur** | Services informatiques (conseil, développement, infogérance) |
| **Effectif actuel** | 50 employés |
| **Effectif prévu (3 ans)** | 60 employés (+20%) |
| **Sites** | 2 sites (siège à Lyon + agence à Grenoble) |
| **CA annuel** | 5 millions d'euros |

### Organisation

**Siège social (Lyon) — 40 employés :**
- 🏢 Direction : 5 personnes (direction générale, comptabilité, RH)
- 💻 Développement : 15 développeurs (web, mobile, logiciels)
- 🛠️ Support : 10 techniciens (hotline, infogérance)
- 📊 Commercial : 5 commerciaux
- 🔧 IT interne : 5 administrateurs systèmes/réseau

**Agence (Grenoble) — 10 employés :**
- 💻 Développement : 5 développeurs
- 📊 Commercial : 3 commerciaux
- 🛠️ Support : 2 techniciens

---

## 🖥️ INFRASTRUCTURE ACTUELLE (À MODERNISER)

### Réseau Existant (Lyon)

**Situation actuelle :**
```
┌─────────────────────────────────────────────────────────────┐
│                      INTERNET                                │
│                   (Fibre 100 Mbps)                           │
└─────────────────┬───────────────────────────────────────────┘
                  │
         ┌────────▼────────┐
         │   Routeur ADSL  │
         │   (Ancien)      │
         └────────┬────────┘
                  │
         ┌────────▼────────┐
         │  Switch 48 ports│
         │  (Non managé)   │
         └────────┬────────┘
                  │
        ┌─────────┴──────────┐
        │                    │
    Postes utilisateurs  Serveurs (3)
    (40 postes)          - SRV-WEB
                         - SRV-MAIL
                         - SRV-FILE
```

**Problèmes identifiés :**
- ❌ Aucune segmentation réseau (tous dans le même réseau plat)
- ❌ Switch non managé (pas de VLAN possible)
- ❌ Adressage IP anarchique (DHCP mal configuré)
- ❌ Bande passante insuffisante aux heures de pointe
- ❌ Pas de redondance (point de défaillance unique)
- ❌ Stockage saturé (serveur de fichiers plein à 90%)

### Réseau Existant (Grenoble)

**Situation actuelle :**
- 📡 Connexion Internet ADSL 20 Mbps
- 🔗 Liaison VPN vers Lyon (instable)
- 🖥️ 1 serveur local de fichiers (partagés locaux uniquement)
- 📊 Pas de serveurs métiers (tout est à Lyon)

---

## 📋 BESOINS EXPRIMÉS PAR LA DIRECTION

### Cahier des Charges

**1. Segmentation du réseau par services**

La direction souhaite **séparer le réseau** en plusieurs zones :
- 🏢 **VLAN Direction** : Direction, comptabilité, RH (données sensibles)
- 💻 **VLAN Développement** : Développeurs (accès serveurs de développement)
- 🛠️ **VLAN Support** : Techniciens support (accès aux outils d'administration)
- 📊 **VLAN Commercial** : Commerciaux (accès CRM et Internet)
- 🔧 **VLAN IT** : Administrateurs (accès complet)
- 🖥️ **VLAN Serveurs** : Serveurs de production
- 🌐 **VLAN DMZ** : Serveurs web accessibles depuis Internet
- 📱 **VLAN IoT** : Imprimantes, téléphones IP, caméras

**Justification :** Sécurité (cloisonnement), performance (réduction domaine de broadcast), gestion (politiques différenciées).

---

**2. Augmentation de la bande passante**

**Problème actuel :**
- Lenteurs aux heures de pointe (9h-10h, 14h-15h)
- Visioconférences qui coupent (Teams, Zoom)
- Sauvegardes qui saturent la connexion

**Applications critiques :**

| **Application** | **Utilisateurs** | **Débit par user** | **Priorité** |
|---|---|---|---|
| Navigation web | 40 users | 2 Mbps | Moyenne |
| Email (Exchange) | 50 users | 0.5 Mbps | Moyenne |
| CRM (SalesForce) | 8 users | 1 Mbps | Haute |
| Visioconférence | 10 users simultanés | 5 Mbps | Très haute |
| VPN Grenoble | 10 users | 10 Mbps total | Haute |
| Sauvegardes cloud | — | 20 Mbps | Basse (nocturne) |

**Besoin :** Dimensionner la connexion Internet et les switchs internes.

---

**3. Dimensionnement du stockage**

**Situation actuelle :**
- 💾 Serveur de fichiers : 2 To (utilisés à 90% → 1.8 To)
- 📧 Serveur mail : 500 Go (utilisés à 70% → 350 Go)
- 🗄️ Bases de données : 300 Go

**Besoins par service :**

| **Service** | **Nombre d'users** | **Quota par user** | **Total** |
|---|---|---|---|
| Direction | 5 | 50 Go | 250 Go |
| Développement | 20 | 100 Go | 2000 Go |
| Support | 12 | 30 Go | 360 Go |
| Commercial | 8 | 20 Go | 160 Go |
| IT | 5 | 200 Go | 1000 Go |
| **TOTAL** | **50** | — | **3770 Go** |

**Partages réseau (communs) :**
- 📂 Partage Direction : 200 Go
- 📂 Partage Développement : 500 Go
- 📂 Partage Support : 300 Go
- 📂 Partage Commercial : 100 Go
- **TOTAL partages** : 1100 Go

**Mail (Exchange Online) :**
- Boîtes mail : 50 users × 10 Go = 500 Go

**Sauvegardes :**
- Appliquer la règle **3-2-1** : 3 copies, 2 supports, 1 hors site
- Rétention : 30 jours de sauvegardes différentielles + 1 complète mensuelle

**Besoin :** Calculer le stockage total nécessaire (production + sauvegardes) et choisir entre local et cloud.

---

**4. Anticipation de la croissance**

**Projection 3 ans :**
- 👥 Effectif : +20% (50 → 60 employés)
- 📊 Données : ×2 (croissance exponentielle)
- 🌐 Bande passante : +50% (nouveaux usages : vidéo 4K, VR)

**Contrainte :** Le plan d'adressage et le dimensionnement doivent **anticiper cette croissance** sans refonte complète.

---

## 🎯 ACTIVITÉ : ANALYSE DES BESOINS (20 min)

### Consigne

**Par binômes**, analysez le cahier des charges et remplissez la grille d'analyse suivante.

### Grille d'Analyse (à remplir)

```
═══════════════════════════════════════════════════════════════
ANALYSE DU CONTEXTE - BINÔME : _______________
═══════════════════════════════════════════════════════════════

1. IDENTIFICATION DES VLAN
───────────────────────────────────────────────────────────────
Listez les VLAN nécessaires avec leur nombre d'hôtes :

VLAN 1 : __________________ → Nombre d'hôtes : _______
VLAN 2 : __________________ → Nombre d'hôtes : _______
VLAN 3 : __________________ → Nombre d'hôtes : _______
VLAN 4 : __________________ → Nombre d'hôtes : _______
VLAN 5 : __________________ → Nombre d'hôtes : _______
VLAN 6 : __________________ → Nombre d'hôtes : _______
VLAN 7 : __________________ → Nombre d'hôtes : _______
VLAN 8 : __________________ → Nombre d'hôtes : _______

TOTAL : _______ VLAN / _______ hôtes

2. ESTIMATION BANDE PASSANTE
───────────────────────────────────────────────────────────────
Quelle est la bande passante totale nécessaire (pic) ?

Navigation : 40 users × 2 Mbps = _______ Mbps
Email : 50 users × 0.5 Mbps = _______ Mbps
CRM : 8 users × 1 Mbps = _______ Mbps
Visio : 10 users × 5 Mbps = _______ Mbps
VPN : 10 Mbps = _______ Mbps

TOTAL : _______ Mbps

Avec marge de 50% : _______ Mbps × 1.5 = _______ Mbps

Connexion Internet recommandée : _______ Mbps

3. ESTIMATION STOCKAGE
───────────────────────────────────────────────────────────────
Quel est le stockage total nécessaire ?

Quotas utilisateurs : _______ Go
Partages réseau : _______ Go
Mail : _______ Go
Bases de données : _______ Go

SOUS-TOTAL production : _______ Go

Sauvegardes (règle 3-2-1) :
- Copie 1 (serveur principal) : déjà compté
- Copie 2 (serveur secondaire) : _______ Go
- Copie 3 (hors site / cloud) : _______ Go

TOTAL avec sauvegardes : _______ Go = _______ To

4. ANTICIPATION CROISSANCE
───────────────────────────────────────────────────────────────
Dans 3 ans :

Nombre d'hôtes total : _______ × 1.2 = _______
Stockage total : _______ Go × 2 = _______ Go
Bande passante : _______ Mbps × 1.5 = _______ Mbps

5. QUESTIONS / PROBLÈMES IDENTIFIÉS
───────────────────────────────────────────────────────────────
Quels sont les 3 principaux défis de ce projet ?

1. ___________________________________________________________
2. ___________________________________________________________
3. ___________________________________________________________
═══════════════════════════════════════════════════════════════
```

---

## 💡 TRANSITION VERS LE PROJET

### Synthèse Collective (5 min)

L'enseignant fait une synthèse rapide au tableau :

**VLAN identifiés (8) :**
1. Direction (5 hôtes)
2. Développement (20 hôtes)
3. Support (12 hôtes)
4. Commercial (8 hôtes)
5. IT (5 hôtes)
6. Serveurs (10 serveurs)
7. DMZ (3 serveurs web)
8. IoT (20 équipements)

**TOTAL : ~85 hôtes actuels → prévoir 100-110 avec la croissance**

**Bande passante estimée :**
- Pic : ~150 Mbps
- Avec marge : ~225 Mbps
- **Recommandation : Fibre 300 Mbps**

**Stockage estimé :**
- Production : ~5.5 To
- Avec sauvegardes : ~16.5 To
- Dans 3 ans : ~33 To

### Lancement du Travail (dernières minutes)

**L'enseignant :**

> "Vous venez d'identifier les besoins de TechServices.
> 
> Maintenant, vous allez passer à la **conception** :
> 
> **Étape 1** (1h15) : Concevoir le **plan d'adressage IP complet**
> - Choisir un réseau de base (ex: 10.0.0.0/16 ou 172.16.0.0/16)
> - Découper en sous-réseaux (1 par VLAN)
> - Attribuer les plages d'adresses
> - Dessiner le schéma réseau
> 
> **Étape 2** (1h) : Calculer la **bande passante** en détail
> - Par VLAN
> - Pics et moyennes
> - Dimensionner la connexion Internet
> 
> **Étape 3** (40 min) : Calculer le **stockage**
> - Détailler les quotas
> - Appliquer la règle 3-2-1
> - Comparer local vs cloud
> 
> **Étape 4** (15 min) : Rédiger le **document de synthèse**
> 
> **C'est parti !**"

---

## 📊 Données Complémentaires (Annexes)

### Annexe A : Débits Moyens par Application

| **Application** | **Débit/user (Mbps)** | **Commentaire** |
|---|---|---|
| Navigation web | 2 | Pages riches, images, vidéos |
| Email (IMAP/SMTP) | 0.5 | Texte + pièces jointes légères |
| CRM web (SalesForce) | 1 | Interface riche |
| ERP web | 1.5 | Requêtes base de données |
| Visioconférence HD | 5 | Teams, Zoom, Google Meet |
| Partage de fichiers | 3 | Accès aux shares réseau |
| VoIP | 0.1 | Téléphonie IP |

### Annexe B : Quotas de Stockage Recommandés

| **Profil utilisateur** | **Quota mail** | **Quota home** | **Total** |
|---|---|---|---|
| Direction | 10 Go | 50 Go | 60 Go |
| Développeur | 10 Go | 100 Go | 110 Go |
| Technicien | 10 Go | 30 Go | 40 Go |
| Commercial | 10 Go | 20 Go | 30 Go |
| Admin IT | 10 Go | 200 Go | 210 Go |

### Annexe C : Masques Recommandés

| **Nombre d'hôtes** | **Masque** | **CIDR** | **Adresses utilisables** |
|---|---|---|---|
| 1-2 | 255.255.255.252 | /30 | 2 |
| 3-6 | 255.255.255.248 | /29 | 6 |
| 7-14 | 255.255.255.240 | /28 | 14 |
| 15-30 | 255.255.255.224 | /27 | 30 |
| 31-62 | 255.255.255.192 | /26 | 62 |
| 63-126 | 255.255.255.128 | /25 | 126 |
| 127-254 | 255.255.255.0 | /24 | 254 |

---
