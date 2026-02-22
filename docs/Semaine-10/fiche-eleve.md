# 📚 FICHE DE COURS ÉLÈVE
## "Gestion des Configurations · Versioning · ITIL Configuration Management"

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 10*

---

## 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|---------------|
| **B1.2** | Exploiter des référentiels (ITIL Configuration Management) |
| **B2.3** | Gérer les accès et services réseaux (configs équipements) |
| **B3.3** | Documenter les configurations |

---

## PARTIE I — Gestion des Configurations selon ITIL

### I.A. Configuration Management — Définition

En ITIL 4, la **gestion des configurations** (Configuration Management) est la pratique qui consiste à maintenir une information fiable et à jour sur tous les **éléments de configuration** (CI — Configuration Items) de l'infrastructure IT et leurs relations.

```
   CMDB (Configuration Management DataBase)
   ────────────────────────────────────────────────────────────
   Base de données centrale contenant tous les CI et leurs relations

   Exemples de CI :
   ├── Serveurs (physiques, virtuels)
   ├── Équipements réseau (switches, routeurs, firewalls)
   ├── Postes de travail (fixes, portables)
   ├── Logiciels (OS, applications, versions)
   ├── Licences (nombre, type, expiration)
   ├── Documents (DAT, procédures, schémas)
   └── Relations entre CI (ce serveur héberge cette application,
       cette application utilise cette base de données...)
```

---

### I.B. Baseline de Configuration

Une **baseline** (ou **référence de configuration**) est un instantané figé de la configuration d'un CI à un moment donné, qui sert de référence pour les changements futurs.

```
   EXEMPLE — Baseline Serveur Web Production
   ─────────────────────────────────────────────────────────────
   Baseline v1.0 — 2024-09-15
   ├── Serveur : SRV-WEB-01 / Ubuntu 22.04.3 LTS
   ├── Apache 2.4.52
   ├── PHP 8.1.12
   ├── MariaDB 10.6.12
   ├── Sites hébergés : intranet.siosarl.local, catalogue.siosarl.local
   ├── Certificat SSL : Let's Encrypt — expire 2024-12-10
   ├── Configuration réseau : IP 192.168.10.50/24, GW .1, DNS .10
   ├── Fichiers de config : /etc/apache2/sites-available/*
   └── Date de création baseline : 2024-09-15

   → Tout changement par rapport à cette baseline doit être documenté
     et validé (Change Management)
```

> 💡 **Pourquoi une baseline ?** Sans baseline, on ne peut pas savoir si une configuration actuelle est conforme à ce qu'elle devrait être. C'est la référence pour les audits de conformité et les retours arrière (rollback) en cas de problème.

---

### I.C. Relations entre CI dans la CMDB

Un CI ne vit jamais seul. La CMDB enregistre les **dépendances** entre CI :

```
   Exemple de relations :
   ─────────────────────────────────────────────────────────────
   APPLICATION INTRANET
       │
       ├── Hébergée sur → SRV-WEB-01
       ├── Utilise → BASE-INTRANET (MariaDB sur SRV-DB-01)
       ├── Nécessite → Licence PHP (10 utilisateurs simultanés)
       └── Accessible via → Switch-CoreN1 (VLAN 20)

   Impact :
   Si SRV-WEB-01 tombe en panne → l'intranet est inaccessible
   Si Switch-CoreN1 redémarre → tous les services sur VLAN 20 coupés
   Si la licence PHP expire → l'intranet peut cesser de fonctionner
```

> 📌 **Utilité en gestion d'incidents :** Quand un incident P1 survient ("L'intranet est HS"), la CMDB permet de voir immédiatement tous les composants impliqués et de remonter la chaîne de dépendance pour identifier la cause.

---

## PARTIE II — Versioning des Configurations

### II.A. Pourquoi Versionner ?

Le **versioning** (ou **gestion de versions**) consiste à garder une trace de toutes les versions successives d'un fichier de configuration, avec l'horodatage et l'auteur de chaque modification.

| **Sans versioning** | **Avec versioning** |
|---|---|
| On écrase l'ancienne config à chaque modification | Chaque modification crée une nouvelle version datée |
| En cas d'erreur, on ne peut pas revenir en arrière | On peut restaurer n'importe quelle version antérieure |
| On ne sait pas qui a changé quoi ni quand | Chaque changement est tracé (auteur, date, raison) |
| Impossible de comparer deux états du système | Diff entre versions pour voir ce qui a changé |

---

### II.B. Méthodes de Versioning

| **Méthode** | **Principe** | **Avantages** | **Inconvénients** | **Usage** |
|---|---|---|---|---|
| **Fichiers horodatés** | Copier le fichier avec date dans le nom | Simple, universel | Pas de diff automatique, volume de stockage | Petite infra, configs manuelles |
| **Git / SVN** | Dépôt versionné avec historique complet | Diff, merge, rollback, commentaires | Nécessite apprentissage Git | Infra moyenne à grande |
| **Outils spécialisés** | Rancid, Oxidized (pour équipements réseau) | Automatisation, alertes sur changement non autorisé | Configuration initiale complexe | Datacenter, parc réseau important |
| **Backup CMDB** | Sauvegarde automatique de la CMDB GLPI | Intégré ITSM | Pas de granularité fichier | PME avec GLPI |

---

### II.C. Fichiers Horodatés — Convention de Nommage

Si vous gérez les configurations manuellement (sans Git), respecter une **convention de nommage stricte** :

```
   Format recommandé :
   [Type]_[Équipement]_[YYYYMMDD]_[Version].[extension]

   Exemples :
   config_Switch-Core1_20241015_v1.0.txt
   config_SRV-DHCP_20241022_v2.3.conf
   baseline_Firewall-PFSense_20241101_v1.0.xml

   Arborescence :
   /backup/configs/
   ├── switches/
   │   ├── Switch-Core1/
   │   │   ├── config_Switch-Core1_20241001_v1.0.txt
   │   │   ├── config_Switch-Core1_20241015_v1.1.txt
   │   │   └── config_Switch-Core1_20241101_v2.0.txt
   │   └── Switch-Distrib-RH/
   ├── serveurs/
   └── firewalls/

   + Un fichier CHANGELOG.md par équipement :
   Switch-Core1 — Historique des modifications
   v2.0 — 2024-11-01 — Ajout VLAN 30 pour Marketing — Auteur: [Nom]
   v1.1 — 2024-10-15 — Correction ACL port 22 — Auteur: [Nom]
   v1.0 — 2024-10-01 — Configuration initiale — Auteur: [Nom]
```

---

## PARTIE III — Configurations Réseau (Running vs Startup)

### III.A. Cisco IOS — Deux Configurations

Les équipements réseau Cisco (et la plupart des constructeurs) utilisent deux emplacements de stockage pour la configuration :

```
   ┌──────────────────────────────────────────────────────────────┐
   │               RUNNING-CONFIG                                  │
   │  Stockage : RAM (volatile — effacée au redémarrage)           │
   │  Fichier  : running-config                                    │
   │  Rôle     : Configuration ACTIVE, en cours d'utilisation       │
   │  Commande : show running-config                                │
   │                                                               │
   │  C'est la config actuellement appliquée sur l'équipement.     │
   │  Toute modification (ajout VLAN, changement IP...) modifie     │
   │  d'abord la running-config.                                    │
   └──────────────────────────────────────────────────────────────┘

   ┌──────────────────────────────────────────────────────────────┐
   │               STARTUP-CONFIG                                  │
   │  Stockage : NVRAM (non-volatile — survit au redémarrage)       │
   │  Fichier  : startup-config                                    │
   │  Rôle     : Configuration SAUVEGARDÉE, chargée au boot         │
   │  Commande : show startup-config                                │
   │                                                               │
   │  C'est la config que l'équipement chargera au prochain         │
   │  redémarrage. Si on ne sauvegarde pas la running-config        │
   │  vers la startup-config, les modifications sont perdues.       │
   └──────────────────────────────────────────────────────────────┘
```

---

### III.B. Commandes Cisco IOS Essentielles

```cisco
! ─── Voir la configuration active ───
Switch# show running-config
! Affiche toute la config en RAM (peut être long)

! ─── Voir la configuration de démarrage ───
Switch# show startup-config
! Affiche la config qui sera chargée au prochain boot

! ─── Comparer les deux configs ───
Switch# show archive config differences
! Montre les différences entre running et startup (si disponible)

! ─── Sauvegarder la running-config vers la startup-config ───
Switch# copy running-config startup-config
! ou raccourci :
Switch# write memory
Switch# wr

! ─── Exporter la config vers un serveur TFTP ───
Switch# copy running-config tftp:
! Puis entrer l'IP du serveur TFTP et le nom de fichier

! ─── Restaurer une config depuis TFTP ───
Switch# copy tftp: running-config
! Attention : fusionne avec la config existante, ne la remplace pas

! ─── Effacer la startup-config (reset factory) ───
Switch# erase startup-config
! Au prochain redémarrage, l'équipement démarre vierge
```

---

### III.C. Workflow Professionnel de Modification

```
   ÉTAPE 1 — SAUVEGARDE PRÉVENTIVE
   ──────────────────────────────────────────────────────────────
   Avant toute modification, sauvegarder la config actuelle :
   Switch# copy running-config tftp:
   Destination : backup_Switch-Core1_20241115_avant-modif.txt

   ÉTAPE 2 — MODIFICATION EN MODE CONFIG
   ──────────────────────────────────────────────────────────────
   Switch# configure terminal
   Switch(config)# [commandes de modification]
   Switch(config)# exit

   ÉTAPE 3 — TEST ET VALIDATION
   ──────────────────────────────────────────────────────────────
   Vérifier que la modification fonctionne (ping, accès, VLAN...)
   Si KO → annuler (reload sans sauvegarder)
   Si OK → passer à l'étape 4

   ÉTAPE 4 — SAUVEGARDE PERMANENTE
   ──────────────────────────────────────────────────────────────
   Switch# copy running-config startup-config
   → La modification survivra au redémarrage

   ÉTAPE 5 — DOCUMENTATION
   ──────────────────────────────────────────────────────────────
   Exporter la nouvelle config et mettre à jour le CHANGELOG :
   Switch# copy running-config tftp:
   Destination : config_Switch-Core1_20241115_v2.1.txt

   Fichier CHANGELOG.md :
   v2.1 — 2024-11-15 — Ajout VLAN 40 Commerce — Auteur: [Nom]
```

---

### III.D. Comparer Deux Versions de Configuration

Pour identifier ce qui a changé entre deux versions, utiliser un outil de diff :

**Sous Linux :**
```bash
diff -u config_Switch_20241001_v1.0.txt config_Switch_20241115_v2.1.txt

# Ou pour une sortie plus lisible :
diff -u config_Switch_20241001_v1.0.txt config_Switch_20241115_v2.1.txt | colordiff
```

**Sous Windows :**
- WinMerge (gratuit, interface graphique)
- Notepad++ avec plugin Compare
- Visual Studio Code avec extension GitLens

**En ligne :**
- diffchecker.com (copier-coller les deux configs)

---

## PARTIE IV — Versioning avec Git (Aperçu)

### IV.A. Pourquoi Git pour les Configs ?

**Git** n'est pas réservé au code source — il est parfait pour versionner des fichiers de configuration texte :

| **Avantage Git** | **Exemple sur configs réseau** |
|---|---|
| Historique complet | Voir tous les changements depuis 2 ans |
| Auteur et date | Savoir qui a modifié quoi et quand |
| Commentaire de commit | "Ajout VLAN 40 pour le service Commerce — Ticket GLPI #1234" |
| Diff automatique | `git diff` montre exactement les lignes modifiées |
| Rollback facile | Revenir à une version antérieure en 1 commande |
| Branches | Tester une modif dans une branche sans toucher à la prod |

---

### IV.B. Workflow Git pour Configs — Exemple

```bash
# ─── Initialisation du dépôt (une seule fois) ───
cd /backup/configs
git init
git config user.name "Technicien Réseau"
git config user.email "technicien@siosarl.local"

# ─── Ajouter une première config ───
# (après avoir exporté depuis le switch)
cp ~/downloads/config_Switch-Core1.txt switches/Switch-Core1.txt
git add switches/Switch-Core1.txt
git commit -m "Config initiale Switch-Core1 — v1.0"

# ─── 2 semaines plus tard : modification du switch ───
# (exporter la nouvelle config)
cp ~/downloads/config_Switch-Core1_nouvelle.txt switches/Switch-Core1.txt
git add switches/Switch-Core1.txt
git commit -m "Ajout VLAN 40 Commerce — Ticket GLPI #1234"

# ─── Voir l'historique ───
git log --oneline
# Affiche :
# a3f82c1 Ajout VLAN 40 Commerce — Ticket GLPI #1234
# e7b12f4 Config initiale Switch-Core1 — v1.0

# ─── Voir ce qui a changé entre deux commits ───
git diff e7b12f4 a3f82c1

# ─── Revenir à une version antérieure (rollback) ───
git checkout e7b12f4 -- switches/Switch-Core1.txt
# Le fichier est restauré à la version initiale
# Il faut ensuite le réappliquer sur le switch
```

---

## V. Vocabulaire Clé

| **Terme** | **Définition** |
|-----------|---------------|
| **Configuration Management** | Pratique ITIL de gestion de tous les CI et leurs relations dans la CMDB |
| **CI (Configuration Item)** | Tout élément de l'infrastructure géré dans la CMDB (serveur, switch, logiciel...) |
| **Baseline** | Référence de configuration figée à un instant T, servant de base pour les changements |
| **Versioning** | Gestion des versions successives d'un fichier avec horodatage et traçabilité |
| **Running-config** | Configuration active d'un équipement réseau (stockée en RAM, volatile) |
| **Startup-config** | Configuration de démarrage d'un équipement réseau (stockée en NVRAM, persistante) |
| **NVRAM** | Non-Volatile RAM — mémoire qui conserve les données sans alimentation |
| **TFTP** | Trivial File Transfer Protocol — protocole simple pour transférer des fichiers (configs) |
| **Diff** | Comparaison de deux fichiers pour identifier les lignes modifiées |
| **Rollback** | Retour à une version antérieure d'une configuration |
| **Commit** | Enregistrement d'une version dans un système de versioning (Git) |
| **CHANGELOG** | Fichier documentant l'historique des modifications d'une configuration |
| **Copy run start** | Commande Cisco pour sauvegarder la running-config vers la startup-config |

---

## ✅ Auto-évaluation : Suis-je Prêt ?

- [ ] Je définis Configuration Management selon ITIL
- [ ] J'explique ce qu'est une baseline et pourquoi elle est utile
- [ ] Je distingue running-config (RAM) et startup-config (NVRAM)
- [ ] Je sais sauvegarder une running-config vers startup-config
- [ ] J'applique une convention de nommage cohérente aux fichiers de config
- [ ] J'explique pourquoi versionner les configs est essentiel
- [ ] Je documente un changement de configuration (qui, quoi, quand, pourquoi)
- [ ] Je peux comparer deux versions de configuration avec diff

