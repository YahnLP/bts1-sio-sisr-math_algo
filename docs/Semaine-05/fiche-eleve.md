# Semaine 5 (S5) - BLOC 1
## 📦 OCS Inventory · Agent · Évaluation Diagnostique S1→S5

---
# 📚 FICHE DE COURS ÉLÈVE
## "OCS Inventory — Gestion de Parc Automatisée"

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 5*

---

## 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|---------------|
| **B1.1** | Recenser et identifier les ressources numériques |
| **B1.4** | Mettre en place et exploiter des outils de gestion de parc |

---

## PARTIE I — Pourquoi Automatiser l'Inventaire ?

En S2, vous avez rempli manuellement la fiche technique d'un seul poste — cela a pris 30 à 45 minutes. Projetons cette expérience à l'échelle :

| **Taille du parc** | **Inventaire manuel** | **Inventaire automatisé** |
|---|---|---|
| 1 poste | 45 min | 2 min (installation agent) |
| 50 postes | 37h30 (1 semaine) | 2h (déploiement agent en masse) |
| 200 postes | 150h (1 mois) | 4h (déploiement GPO ou script) |
| 1 000 postes | — (irréaliste) | ½ journée |

**Trois problèmes supplémentaires de l'inventaire manuel :**

1. **L'information vieillit dès qu'elle est écrite.** Une mise à jour Windows, un ajout de RAM, un changement de disque — la fiche manuelle est déjà obsolète.
2. **L'inventaire n'est jamais exhaustif.** On oublie des postes, des imprimantes réseau, des équipements dans des armoires.
3. **Aucune alerte sur les changements.** Si quelqu'un installe un logiciel non autorisé ou retire une barrette de RAM, on ne le sait pas.

La **gestion de parc automatisée** résout ces trois problèmes : les agents remontent les informations périodiquement, l'inventaire se met à jour sans intervention humaine, et les modifications sont traçables.

---

## PARTIE II — OCS Inventory NG

### II.A. Présentation

**OCS Inventory NG** (Open Computer and Software Inventory Next Generation) est un logiciel **open source** de gestion d'inventaire de parc informatique. Il est utilisé par des milliers d'organisations dans le monde, particulièrement en France où il est très répandu dans les collectivités et PME.

| **Paramètre** | **Valeur** |
|---|---|
| **Licence** | GPL v2 (open source — gratuit) |
| **Site officiel** | ocsinventory-ng.org |
| **Éditeur communautaire** | OCS Inventory Team |
| **Systèmes supportés (agent)** | Windows, Linux, macOS, Android, AIX, Solaris |
| **Technologies serveur** | Apache + PHP + MySQL/MariaDB |
| **Intégration** | GLPI (via plugin FusionInventory) |

---

### II.B. Architecture Client/Serveur

```
   ┌─────────────────────────────────────────────────────────────────┐
   │                    ARCHITECTURE OCS INVENTORY                    │
   │                                                                 │
   │   POSTES DU PARC                  SERVEUR OCS                  │
   │   ─────────────                  ───────────                   │
   │                                                                 │
   │  PC Windows ──────── HTTPS ──────►┌─────────────────┐          │
   │  PC Linux   ──────── HTTPS ──────►│  Serveur Apache │          │
   │  Mac        ──────── HTTPS ──────►│  PHP            │          │
   │  Laptop     ──────── HTTPS ──────►│  MySQL/MariaDB  │          │
   │                                   └────────┬────────┘          │
   │   ↑                                        │                   │
   │   Agent OCS                                ▼                   │
   │   installé sur                    ┌─────────────────┐          │
   │   chaque poste                    │  Console Web    │          │
   │                                   │  ocsreports     │          │
   │                                   │  (navigateur)   │          │
   │                                   └─────────────────┘          │
   │                                          ↑                     │
   │                                   Admin DSI                    │
   └─────────────────────────────────────────────────────────────────┘
```

*Légende : Architecture OCS Inventory. L'agent installé sur chaque poste collecte les informations matérielles et logicielles, puis les envoie au serveur OCS via HTTPS. Le serveur stocke les données dans MySQL. L'administrateur accède aux inventaires via la console web `ocsreports`. Le protocole HTTPS garantit la confidentialité des données de parc en transit.*

---

### II.C. Fonctionnement de l'Agent

L'**agent OCS** est un service (daemon) qui s'exécute en arrière-plan sur chaque poste. Ses actions :

```
   DÉMARRAGE DU POSTE
         │
         ▼
   Agent OCS démarre
   (service Windows ou cron Linux)
         │
         ▼
   Collecte des informations :
   • Matériel (CPU, RAM, disques, cartes réseau...)
   • OS (version, patches installés, clé de licence)
   • Logiciels (liste complète avec versions)
   • Réseau (IP, MAC, VLAN si disponible)
   • Périphériques connectés
         │
         ▼
   Comparaison avec le dernier inventaire envoyé
   (changements uniquement si "ipdiscover" ou delta)
         │
         ▼
   Envoi au serveur OCS via HTTPS (XML compressé)
   URL : http(s)://[serveur]/ocsinventory
         │
         ▼
   Serveur stocke en base de données
   Console web mise à jour
```

---

### II.D. Ce qu'OCS Inventory Collecte

| **Catégorie** | **Informations collectées** |
|---|---|
| **Matériel** | CPU (modèle, fréquence, cœurs), RAM (capacité, slots), Disques (modèle, taille, type), Carte mère, BIOS (version, date), Carte réseau (MAC, IP, type) |
| **Système** | OS (nom, version, build, langue), Clé de licence OS, Domaine/groupe de travail, Nom du poste, Uptime |
| **Logiciels** | Liste complète avec éditeur, version, date d'installation, chemin |
| **Réseau** | Toutes les interfaces (IP, masque, MAC, VLAN) |
| **Périphériques** | Moniteurs (marque, résolution), Imprimantes, Ports (USB, PCI...) |
| **Sécurité** | Antivirus détecté, pare-feu, mises à jour manquantes (optionnel) |

> 📌 **Point sécurité :** OCS Inventory collecte des informations potentiellement sensibles (configuration du réseau, logiciels installés, parfois clés de licence). Le serveur OCS doit être sécurisé (HTTPS, authentification forte, accès restreint) et les données traitées conformément au RGPD.

---

### II.E. Avantages et Limites

| **Avantages** | **Limites** |
|---|---|
| ✅ Inventaire automatique et périodique | ❌ Nécessite un agent sur chaque poste |
| ✅ Détection des changements | ❌ Agent = charge CPU/RAM (légère) |
| ✅ 100% open source et gratuit | ❌ Interface web vieillissante |
| ✅ Multi-OS (Windows, Linux, Mac) | ❌ Pas de gestion native des licences avancée |
| ✅ Intégration GLPI (via plugin) | ❌ Nécessite un serveur dédié |
| ✅ API REST disponible | ❌ Configuration initiale complexe |
| ✅ Très répandu en France | ❌ Alternatives plus modernes existent (Lansweeper, Rudder) |

---

### II.F. OCS et GLPI — L'Écosystème Complet

OCS Inventory et GLPI fonctionnent souvent ensemble dans les organisations françaises :

```
   OCS INVENTORY                      GLPI
   ─────────────                      ────
   Collecte automatique   ──────────► Reçoit l'inventaire
   des données matérielles            via plugin FusionInventory
   et logicielles                     ou import natif

                                       + Gestion des tickets
                                       + CMDB relationnelle
                                       + Gestion des licences
                                       + Base de connaissances
                                       + Planification
                                       + Rapports SLA
```

> 💡 **En entreprise :** On dit souvent "on est sous GLPI + OCS". GLPI est l'outil de gestion (tickets, actifs, CMDB), OCS est le collecteur automatique qui l'alimente. L'un sans l'autre est moins efficace.

---

### II.G. Commandes de l'Agent Windows

```cmd
:: Forcer un inventaire immédiat (lancer depuis le répertoire d'installation)
"C:\Program Files\OCS Inventory Agent\OCSInventory.exe" /np /server:[IP_SERVEUR]

:: Forcer un inventaire avec logs détaillés
"C:\Program Files\OCS Inventory Agent\OCSInventory.exe" /np /server:[IP_SERVEUR] /debug /logfile:C:\Temp\ocs_debug.log

:: Vérifier le service Windows OCS
sc query OCS_AGENT
Get-Service -Name "OCS_AGENT"

:: Voir les logs de l'agent
type "C:\ProgramData\OCS Inventory Agent\OCSInventory.log"
```

---

### II.H. Comparaison des Outils de Gestion de Parc

| **Outil** | **Type** | **Inventaire Auto** | **Tickets** | **CMDB** | **Coût** |
|---|---|---|---|---|---|
| **OCS Inventory** | Open source | ✅ (agent) | ❌ | ❌ | Gratuit |
| **GLPI seul** | Open source | ❌ (manuel) | ✅ | ✅ | Gratuit |
| **GLPI + OCS** | Open source | ✅ | ✅ | ✅ | Gratuit |
| **Lansweeper** | Freemium | ✅ (agentless) | ❌ | Limité | Free/<100 |
| **SCCM/Intune** | Microsoft | ✅ (agent) | ❌ | ✅ | Inclus M365 |
| **ServiceNow** | SaaS | ✅ | ✅ | ✅ | Très élevé |

---

## III. Vocabulaire Clé

| **Terme** | **Définition** |
|-----------|---------------|
| **Agent OCS** | Logiciel installé sur chaque poste qui collecte et envoie les données au serveur |
| **Serveur OCS** | Serveur central qui reçoit, stocke et expose les inventaires |
| **ocsreports** | Interface web d'administration d'OCS Inventory |
| **XML** | Format de données utilisé par l'agent pour envoyer l'inventaire |
| **ipdiscover** | Fonctionnalité OCS qui scanne le réseau pour détecter des équipements non inventoriés |
| **FusionInventory** | Plugin GLPI permettant l'intégration avec OCS Inventory |
| **Inventaire delta** | Envoi uniquement des modifications depuis le dernier inventaire (optimisation réseau) |
| **Agentless** | Inventaire sans agent — utilise des protocoles réseau (SNMP, WMI) à distance |
| **SNMP** | Protocole permettant l'inventaire à distance des équipements réseau |
| **WMI** | Windows Management Instrumentation — interface Windows pour l'administration distante |

