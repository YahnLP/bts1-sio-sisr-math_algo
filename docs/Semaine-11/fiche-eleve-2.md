# 📚 FICHE DE COURS ÉLÈVE
## "Documentation Technique · Rédaction de Procédures"

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 11*

---

## 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|---------------|
| **B2.1** | Installer et configurer un service (documentation) |
| **B3.3** | Documenter professionnellement |

---

## PARTIE I — Procédure vs Guide vs DAT

### I.A. Les 3 Types de Documentation Technique

| **Type** | **Public** | **Objectif** | **Contenu** | **Exemple** |
|---|---|---|---|---|
| **Procédure** | Technicien qui exécute | Reproduire une tâche précise | Étapes numérotées, commandes, captures | "Procédure d'installation Apache sur Ubuntu 22.04" |
| **Guide utilisateur** | Utilisateur final | Utiliser un service | Fonctionnalités, astuces, FAQ | "Guide d'utilisation de la messagerie" |
| **DAT** | DSI / auditeur | Comprendre l'architecture | Schémas, choix techniques, justifications | "Dossier d'Architecture Technique SimIO" |

> 📌 **Erreur courante :** Mélanger les trois dans un seul document. Une procédure d'installation qui explique aussi l'architecture et comment utiliser le service devient illisible.

---

### I.B. Caractéristiques d'une Bonne Procédure

| **Critère** | **Bonne pratique** | **Mauvaise pratique** |
|---|---|---|
| **Reproductibilité** | N'importe quel technicien peut suivre sans aide | "Configurer le serveur comme d'habitude" |
| **Précision** | Commandes exactes, chemins complets | "Modifier le fichier de config" (lequel ?) |
| **Captures d'écran** | À chaque étape clé, annotées | Captures floues ou sans légende |
| **Numérotation** | Étapes numérotées hiérarchiquement (1, 1.1, 1.2, 2, 2.1...) | Puces désordonnées |
| **Prérequis** | Clairement listés en début | Découverts en cours de route |
| **Résultat attendu** | "À la fin, vous devez voir X" | Pas de validation |

---

## PARTIE II — Structure d'une Procédure Technique

### II.A. Les 10 Sections Obligatoires

```
╔══════════════════════════════════════════════════════════════════════╗
║              STRUCTURE STANDARD D'UNE PROCÉDURE                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ① EN-TÊTE                                                           ║
║     Titre, version, date, auteur, statut (brouillon/validé)          ║
║                                                                      ║
║  ② OBJECTIF                                                          ║
║     Ce que cette procédure permet d'accomplir (1-2 phrases)          ║
║                                                                      ║
║  ③ PÉRIMÈTRE                                                         ║
║     Ce qui est couvert / ce qui ne l'est pas                         ║
║                                                                      ║
║  ④ PRÉREQUIS                                                         ║
║     Matériel, logiciels, accès, compétences nécessaires              ║
║                                                                      ║
║  ⑤ DURÉE ESTIMÉE                                                     ║
║     Temps nécessaire pour exécuter la procédure                      ║
║                                                                      ║
║  ⑥ ÉTAPES D'INSTALLATION                                             ║
║     Numérotation hiérarchique, commandes, captures                   ║
║                                                                      ║
║  ⑦ VÉRIFICATION                                                      ║
║     Tests à effectuer pour valider que tout fonctionne               ║
║                                                                      ║
║  ⑧ DÉPANNAGE (TROUBLESHOOTING)                                       ║
║     Erreurs courantes + résolutions                                  ║
║                                                                      ║
║  ⑨ RÉFÉRENCES                                                        ║
║     Documentation officielle, liens utiles, tickets liés             ║
║                                                                      ║
║  ⑩ HISTORIQUE DES VERSIONS                                           ║
║     v1.0 — Date — Auteur — Modification                              ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

### II.B. Exemple d'En-Tête Professionnel

```
═══════════════════════════════════════════════════════════════════════
                          PROCÉDURE TECHNIQUE
                   Installation Serveur Apache 2.4
                          Ubuntu Server 22.04 LTS
═══════════════════════════════════════════════════════════════════════
Version      : 1.2
Date         : 2024-11-20
Auteur       : [Votre nom]
Réviseur     : [Nom du superviseur]
Statut       : ☑ Validé  ☐ Brouillon  ☐ Obsolète
Référence    : PROC-SRV-APACHE-001
═══════════════════════════════════════════════════════════════════════
```

---

## PARTIE III — Les Captures d'Écran Professionnelles

### III.A. Quand Capturer ?

| **Situation** | **Capturer ?** | **Raison** |
|---|---|---|
| Commande à exécuter | ✅ Oui | Montrer la syntaxe exacte |
| Résultat de la commande | ✅ Oui | Montrer ce qui est attendu |
| Menu de configuration | ✅ Oui | Éviter l'ambiguïté ("onglet Avancé" — lequel ?) |
| Message d'erreur | ✅ Oui | Aider au dépannage |
| Fenêtre standard Windows | ⚠️ Optionnel | Si c'est évident (ex : "Suivant" dans un wizard), peut être omis |
| Longue sortie texte | ❌ Non | Copier-coller le texte dans un bloc code |

---

### III.B. Règles de Capture

```
   RÈGLE 1 — RÉSOLUTION ADAPTÉE
   ──────────────────────────────────────────────────────────────
   Pas trop grande (fichier lourd), pas trop petite (illisible)
   Recommandation : 1280×720 ou 1920×1080, rognée sur la zone utile

   RÈGLE 2 — ANNOTATIONS
   ──────────────────────────────────────────────────────────────
   Flécher les boutons à cliquer, encadrer les champs à remplir
   Outils : ShareX, Greenshot, Snagit, Paint.NET

   RÈGLE 3 — NUMÉROTATION COHÉRENTE
   ──────────────────────────────────────────────────────────────
   Nommer les captures selon l'étape :
   01_installation_apache_apt.png
   02_verification_version.png
   03_configuration_vhost.png

   RÈGLE 4 — LÉGENDE OBLIGATOIRE
   ──────────────────────────────────────────────────────────────
   Chaque capture doit avoir une légende :
   "Figure 1.2 — Installation d'Apache via apt"
   "Figure 2.1 — Vérification du statut du service"

   RÈGLE 5 — FORMAT
   ──────────────────────────────────────────────────────────────
   PNG pour les captures d'interface (sans compression)
   JPEG uniquement si photo réelle (pas de capture d'écran)
```

---

## PARTIE IV — Versioning de la Documentation

### IV.A. Pourquoi Versionner ?

Une procédure évolue : changement d'OS, nouvelle version du logiciel, correction d'erreurs. Sans versioning, impossible de savoir quelle version est la bonne.

```
   SANS VERSIONING                  AVEC VERSIONING
   ───────────────                  ───────────────
   Procédure_Apache.docx       →    Procédure_Apache_v1.0.docx
   Procédure_Apache_NEW.docx   →    Procédure_Apache_v1.1.docx
   Procédure_Apache_FINAL.docx →    Procédure_Apache_v2.0.docx
   Procédure_Apache_FINAL2.docx     (pas de "FINAL2")

   Historique intégré au document :
   v2.0 — 2024-11-15 — Migration vers Ubuntu 24.04
   v1.1 — 2024-08-10 — Ajout section SSL
   v1.0 — 2024-05-20 — Version initiale
```

---

### IV.B. Numérotation Sémantique

```
   VERSION   X.Y.Z
            │ │ │
            │ │ └─ Patch (correction mineure, typo, capture mise à jour)
            │ └─── Minor (ajout d'une section, amélioration sans changement majeur)
            └───── Major (changement de version d'OS, refonte complète)

   Exemples :
   1.0.0 → Version initiale
   1.1.0 → Ajout section "Troubleshooting"
   1.1.1 → Correction typo + mise à jour capture étape 3
   2.0.0 → Migration Ubuntu 22.04 → 24.04 (procédure adaptée)
```

---

## V. Vocabulaire Clé

| **Terme** | **Définition** |
|-----------|---------------|
| **Procédure** | Document décrivant les étapes pour accomplir une tâche technique reproductible |
| **Guide utilisateur** | Document décrivant comment utiliser un service (destiné aux non-techniciens) |
| **DAT** | Dossier d'Architecture Technique — document décrivant l'infrastructure |
| **Capture annotée** | Image d'écran avec flèches, encadrés ou texte ajouté pour guider |
| **Versioning** | Gestion des versions successives d'un document avec numérotation sémantique |
| **Troubleshooting** | Section d'une procédure listant les erreurs courantes et leurs résolutions |
| **Prérequis** | Conditions devant être remplies avant d'exécuter une procédure |
| **Résultat attendu** | État ou sortie du système après exécution réussie de la procédure |
| **Validation** | Tests confirmant que la procédure a été correctement suivie |

