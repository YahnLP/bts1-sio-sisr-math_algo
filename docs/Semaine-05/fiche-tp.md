# Semaine 5 (S5) - BLOC 1
## 📦 OCS Inventory · Agent · Évaluation Diagnostique S1→S5

---

# 🖥️ FICHE TP — DÉCOUVERTE OCS INVENTORY

*Durée : 50 minutes — En binôme*

---

## Étape 1 — Connexion à la Console OCS (5 min)

Ouvrir un navigateur et accéder à la console OCS :

```
URL : http://[IP_SERVEUR_OCS]/ocsreports
Login : admin
Mot de passe : admin (à changer en production !)
```

> ⚠️ **Sécurité :** En production, le mot de passe `admin/admin` est une faille critique. Tout serveur OCS accessible depuis Internet avec ces identifiants par défaut sera compromis en quelques heures.

Explorer l'interface 5 minutes :

| **Section** | **Ce que vous trouvez** |
|---|---|
| Inventaire → Tous les ordinateurs | |
| Inventaire → Softwares | |
| Configuration → Générale | |
| Rapports | |

---

## Étape 2 — Téléchargement et Installation de l'Agent Windows (20 min)

### 2.1 — Téléchargement

```
Site officiel : https://github.com/OCSInventory-NG/WindowsAgent/releases
Fichier à télécharger : OCS-NG-Windows-Agent-Setup-[version].exe
```

Si le réseau ne le permet pas, l'enseignant fournit le fichier sur le partage réseau de TP.

### 2.2 — Installation

Lancer l'installeur en **tant qu'administrateur** et noter les paramètres configurés :

| **Paramètre d'installation** | **Valeur saisie** |
|---|---|
| Adresse du serveur OCS | |
| Port (par défaut 80 ou 443) | |
| TAG (étiquette de groupe) | `TP-BTS-SIO` |
| Fréquence d'inventaire | |
| Service Windows créé ? | ☐ Oui / ☐ Non |

### 2.3 — Premier Inventaire Forcé

Après installation, forcer immédiatement un inventaire :

```cmd
:: Ouvrir CMD en administrateur
cd "C:\Program Files\OCS Inventory Agent"
OCSInventory.exe /np /server:[IP_SERVEUR] /debug /logfile:C:\Temp\ocs.log
```

Observer la sortie du terminal et noter :

| **Information dans les logs** | **Valeur** |
|---|---|
| Connexion au serveur réussie ? | ☐ Oui / ☐ Non |
| Nombre d'éléments matériels envoyés | |
| Nombre de logiciels détectés | |
| Durée de l'inventaire | s |
| Erreur éventuelle | |

---

## Étape 3 — Vérification dans la Console (10 min)

Retourner dans la console OCS et vérifier que le poste est apparu :

```
Inventaire → Tous les ordinateurs → Chercher votre poste (nom ou IP)
```

Comparer l'inventaire OCS avec la fiche manuelle réalisée en S2 :

| **Information** | **Fiche manuelle S2** | **OCS Inventory** | **Identique ?** |
|---|---|---|---|
| Nom du poste | | | ☐ Oui / ☐ Non |
| CPU | | | ☐ Oui / ☐ Non |
| RAM totale | | | ☐ Oui / ☐ Non |
| OS + version | | | ☐ Oui / ☐ Non |
| Adresse IP | | | ☐ Oui / ☐ Non |
| Adresse MAC | | | ☐ Oui / ☐ Non |
| Nb logiciels | | (OCS compte tout) | — |
| Numéro de série | | | ☐ Oui / ☐ Non |

**Observations :**

```
Différences constatées : ____________________________________________
__________________________________________________________________
```

---

## Étape 4 — Questions de Réflexion (15 min)

**Q1.** OCS Inventory a détecté _____ logiciels sur votre poste. Lors de la fiche manuelle S2, vous en aviez listé _____. Comment expliquez-vous la différence ?

```
Réponse : ___________________________________________________________
```

**Q2.** Le service Windows OCS_AGENT est configuré pour démarrer automatiquement. Cela signifie que l'inventaire sera mis à jour à chaque démarrage du PC. Citez **2 situations** où cette mise à jour automatique est particulièrement utile pour la DSI.

```
Situation 1 : _______________________________________________________
Situation 2 : _______________________________________________________
```

**Q3.** Un utilisateur découvre qu'OCS Inventory surveille les logiciels installés sur son PC et s'y oppose au nom de sa vie privée. Que lui répondez-vous ? Comment la DSI doit-elle encadrer cet outil ?

```
Réponse : ___________________________________________________________
__________________________________________________________________
```

**Éléments de réponse Q3 :** L'inventaire de parc d'entreprise ne surveille pas l'activité personnelle — il recense uniquement les logiciels installés et la configuration matérielle pour des raisons légitimes (licences, sécurité, conformité). Il doit être mentionné dans la charte informatique de l'entreprise que les utilisateurs signent. En France, le RGPD impose une information préalable des personnes concernées par tout traitement de leurs données — un inventaire de parc sur un équipement professionnel est généralement couvert par la charte SI.

**Q4.** Votre entreprise d'alternance utilise-t-elle un outil d'inventaire de parc ? Lequel ? Comment les données sont-elles exploitées ?

```
Réponse : ___________________________________________________________
__________________________________________________________________
```

