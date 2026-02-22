# 📚 FICHE DE COURS ÉLÈVE
## "Gestion des Actifs Logiciels · Licences · Conformité"

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 11*

---

## 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|---------------|
| **B1.1** | Recenser et identifier les ressources numériques (logiciels) |
| **B1.4** | Mettre en place et exploiter des outils de gestion de parc (licences) |
| **B1.2** | Exploiter des référentiels (conformité légale) |

---

## PARTIE I — Les Types de Licences Logicielles

### I.A. Les 7 Familles de Licences

| **Type** | **Définition** | **Droit d'usage** | **Exemple** | **Coût** |
|---|---|---|---|---|
| **OEM** | Original Equipment Manufacturer | Liée au matériel d'origine, non transférable | Windows préinstallé sur un PC Dell | Inclus dans le prix du PC |
| **Retail / Box** | Achat en magasin | Utilisable sur un seul poste à la fois, transférable entre machines | Office 2021 acheté en grande surface | 100-400 € |
| **Volume / VL** | Licence en volume pour organisations | Nombre défini de postes, gestion centralisée | Microsoft Open License (50 licences Office) | 150-250 €/licence |
| **SaaS** | Software as a Service | Abonnement mensuel/annuel, accès cloud | Microsoft 365, Adobe Creative Cloud | 10-60 €/mois/utilisateur |
| **Open Source** | Logiciel libre | Usage, modification, distribution libres | Linux, LibreOffice, GIMP, Firefox | Gratuit |
| **Freeware** | Gratuit mais propriétaire | Usage gratuit, code fermé | 7-Zip, VLC, Acrobat Reader | Gratuit |
| **Shareware** | Essai gratuit limité | Gratuit en version bridée ou limitée dans le temps | WinRAR (40 jours d'essai), WinZip | Payant après essai |

---

### I.B. Les Pièges Classiques

```
   PIÈGE N°1 — "C'est gratuit pour un usage personnel"
   ──────────────────────────────────────────────────────────────
   Beaucoup de logiciels sont gratuits en usage personnel mais
   PAYANTS en usage commercial.

   Exemples :
   • WinRAR : gratuit en usage perso, 29 € en entreprise
   • Certaines polices de caractères : gratuites en perso, licence
     commerciale nécessaire pour les logos d'entreprise
   • Slack : gratuit jusqu'à 10 000 messages, payant au-delà

   ⚠️ Installer un logiciel "gratuit perso" sur un PC d'entreprise
      = violation de licence


   PIÈGE N°2 — "On a acheté X licences il y a 5 ans"
   ──────────────────────────────────────────────────────────────
   Certaines licences sont PERPÉTUELLES (Office 2019 standalone),
   d'autres sont TEMPORAIRES (Office 365 — 1 an).

   • Licence perpétuelle : payée une fois, utilisable indéfiniment
     (mais les mises à jour majeures sont payantes)
   • Licence temporaire (subscription) : payée chaque mois/an,
     arrêt du paiement = arrêt du logiciel

   ⚠️ Ne pas renouveler une licence temporaire = utilisation illégale


   PIÈGE N°3 — "On a désinstallé, donc on peut réutiliser la licence"
   ──────────────────────────────────────────────────────────────
   Certaines licences sont NOMINATIVES (liées à un utilisateur),
   d'autres sont FLOTTANTES (pool partagé).

   • Licence nominative (Named User) : achetée pour "Alice Martin",
     utilisable uniquement par elle — même si désinstallée sur son
     ancien PC, elle reste "sa" licence
   • Licence flottante (Concurrent) : pool de N licences utilisables
     par N utilisateurs simultanés maximum

   ⚠️ Réattribuer une licence nominative sans en informer l'éditeur
      peut violer le contrat
```

---

## PARTIE II — La Conformité Logicielle

### II.A. Qu'est-ce que la Conformité ?

Une organisation est **conforme** si :
1. Tous les logiciels installés sont couverts par une licence valide
2. Le nombre d'installations ne dépasse pas le nombre de licences
3. Les preuves d'achat sont conservées et accessibles
4. Les renouvellements sont effectués avant expiration

---

### II.B. Les Risques du Non-Respect

| **Risque** | **Conséquence** | **Exemple chiffré** |
|---|---|---|
| **Amende BSA** | L'organisme BSA peut exiger des dommages-intérêts | 150 000 € pour une PME de 80 personnes (jurisprudence française) |
| **Poursuite éditeur** | Microsoft, Adobe, Autodesk peuvent attaquer en justice | Oracle a obtenu 1,3 milliard $ contre Google (cas extrême) |
| **Réputation** | Publication de l'amende, impact image | "Entreprise X condamnée pour piratage logiciel" |
| **Blocage logiciel** | Certains éditeurs peuvent désactiver les licences à distance | Adobe CC cesse de fonctionner si l'abonnement expire |
| **Audit informatique bloquant** | Lors d'un audit ISO 27001 ou NIS2, la non-conformité bloque la certification | Perte d'un marché public exigeant ISO 27001 |

---

### II.C. Les Organismes de Contrôle

| **Organisme** | **Rôle** | **Secteur** |
|---|---|---|
| **BSA** | Business Software Alliance — représente les grands éditeurs (Microsoft, Adobe, Autodesk...) | Logiciels professionnels |
| **SACEM** | Société des Auteurs, Compositeurs et Éditeurs de Musique | Musique (si diffusée en entreprise) |
| **APP** | Alliance for Intellectual Property — UK, mais influence européenne | Propriété intellectuelle globale |
| **Éditeurs directs** | Microsoft, Adobe, Oracle mènent leurs propres audits | Leurs logiciels uniquement |

> 📌 **Comment sont déclenchés les audits ?** Plusieurs déclencheurs :
> - Dénonciation anonyme (ancien employé mécontent, concurrent...)
> - Campagne d'audit aléatoire de la BSA dans un secteur
> - Détection automatique par les éditeurs (certains logiciels "appellent à la maison")
> - Lors d'une fusion/acquisition (due diligence)

---

## PARTIE III — L'Audit de Conformité

### III.A. Méthodologie d'Audit Interne

Un audit de conformité se déroule en 6 étapes :

```
   ① INVENTAIRE LOGICIEL
   ──────────────────────────────────────────────────────────────
   Lister tous les logiciels installés sur tous les postes
   Outils : OCS Inventory, GLPI, Lansweeper, SCCM
   Export : Fichier CSV avec Poste / Logiciel / Version / Éditeur

   ② INVENTAIRE DES LICENCES
   ──────────────────────────────────────────────────────────────
   Lister toutes les licences achetées
   Sources : factures, contrats, emails de confirmation, clés de licence
   Base : Fichier Excel ou module Licences de GLPI

   ③ RAPPROCHEMENT (RECONCILIATION)
   ──────────────────────────────────────────────────────────────
   Comparer les deux listes :
   Installations > Licences → SOUS-LICENSING (illégal)
   Installations < Licences → SUR-LICENSING (gaspillage)

   ④ IDENTIFICATION DES ÉCARTS
   ──────────────────────────────────────────────────────────────
   Produire 3 listes :
   • Logiciels sans licence (à acheter ou désinstaller)
   • Licences inutilisées (renégocier ou réaffecter)
   • Licences expirées (renouveler ou migrer)

   ⑤ PLAN DE REMÉDIATION
   ──────────────────────────────────────────────────────────────
   Décider pour chaque écart :
   • Acheter les licences manquantes
   • Désinstaller les logiciels non autorisés
   • Migrer vers des alternatives (LibreOffice au lieu d'Office)
   • Renégocier avec l'éditeur (volume discount)

   ⑥ SUIVI ET REPORTING
   ──────────────────────────────────────────────────────────────
   Produire un rapport de conformité mensuel/trimestriel
   Dashboard GLPI : % de conformité, nombre d'alertes, coût
```

---

### III.B. Formule de Conformité

```
   Taux de conformité = (Licences valides / Logiciels installés) × 100

   Exemple :
   Logiciels installés : 450 (tous postes confondus)
   Licences valides    : 380
   Conformité          : (380 / 450) × 100 = 84,4%

   Seuil acceptable : ≥ 98% (marge de tolérance pour renouvellements en cours)
   Seuil critique   : < 90% → audit externe probable
```

---

## PARTIE IV — Le Coût Total de Possession (TCO)

### IV.A. Définition

Le **TCO** (Total Cost of Ownership) est le coût réel d'un logiciel sur toute sa durée de vie, incluant :

| **Composante** | **Exemple** |
|---|---|
| **Achat initial** | 300 € pour Office 2021 |
| **Support et maintenance** | 50 €/an (updates, hotline) |
| **Formation** | 200 € pour former 1 utilisateur |
| **Coût de déploiement** | 2h technicien × 50 €/h = 100 € |
| **Coût de migration** | Passage de Office 2016 → 2021 : 4h × 50 € = 200 € |
| **Coût d'opportunité** | Temps perdu si le logiciel est lent ou inadapté |

```
   TCO sur 5 ans — Office 2021 (1 utilisateur)

   Achat initial          : 300 €
   Support (5 × 50 €)     : 250 €
   Formation              : 200 €
   Déploiement            : 100 €
   Migrations (× 2)       : 400 €
   ─────────────────────────────
   TCO 5 ans              : 1 250 €
   Coût annualisé         : 250 €/an
```

**Comparaison SaaS vs Perpétuel :**

| **Critère** | **Office 2021 (perpétuel)** | **Microsoft 365 (SaaS)** |
|---|---|---|
| Achat initial | 300 € | 0 € |
| Coût annuel | 50 € (support) | 120 €/an (abonnement) |
| Mises à jour majeures | Payantes (nouvelle version) | Incluses |
| TCO 5 ans | 1 250 € | 600 € (abonnement) + 300 € (support/formation) = 900 € |
| **Bilan** | Plus cher sur 5 ans | Moins cher si mises à jour fréquentes |

> 💡 **Enseignement :** Le SaaS est souvent plus économique sur le long terme si on valorise les mises à jour continues et la flexibilité (ajout/retrait d'utilisateurs). Le perpétuel est préférable si l'organisation veut contrôler les montées de version.

---

## PARTIE V — Gestion dans GLPI

### V.A. Module Licences GLPI

GLPI dispose d'un module dédié à la gestion des licences :

```
   GLPI → Parc → Licences
   ──────────────────────────────────────────────────────────────

   Informations à renseigner pour chaque licence :
   ├── Nom (ex : Microsoft Office Standard 2021)
   ├── Éditeur (Microsoft Corporation)
   ├── Type (OEM, Volume, SaaS, Open Source...)
   ├── Nombre acheté (ex : 80 licences)
   ├── Date d'achat
   ├── Date d'expiration (si temporaire)
   ├── Coût total
   ├── Numéro de commande / facture
   ├── Clé de licence (si applicable)
   └── Association avec les logiciels inventoriés (lien vers le logiciel)

   Vue consolidée :
   • Licences expirées dans les 30 jours (alerte)
   • Licences surexploitées (plus d'installations que de licences)
   • Licences sous-utilisées (licences achetées mais non déployées)
```

---

### V.B. Alertes Automatiques

Configurer GLPI pour envoyer des alertes :

| **Alerte** | **Condition** | **Action recommandée** |
|---|---|---|
| Expiration proche | Licence expire dans < 30 jours | Prévoir renouvellement |
| Sur-utilisation | Installations > Licences | Acheter ou désinstaller |
| Sous-utilisation | Licences inutilisées depuis 90 jours | Réattribuer ou annuler |
| Licence non attribuée | Achetée mais jamais déployée | Déployer ou annuler |

---

## VI. Vocabulaire Clé

| **Terme** | **Définition** |
|-----------|---------------|
| **Actif logiciel** | Tout logiciel déployé dans l'organisation, qu'il soit licencié ou non |
| **Conformité** | État où tous les logiciels installés sont couverts par des licences valides |
| **BSA** | Business Software Alliance — organisme représentant les éditeurs pour les audits |
| **Sous-licensing** | Situation où le nombre d'installations dépasse le nombre de licences (illégal) |
| **Sur-licensing** | Situation où des licences payées ne sont pas utilisées (gaspillage) |
| **TCO** | Total Cost of Ownership — coût total d'un logiciel sur sa durée de vie |
| **Named User** | Licence nominative attribuée à une personne précise |
| **Concurrent License** | Licence flottante utilisable par N utilisateurs simultanés (pool) |
| **Volume License** | Licence achetée en volume pour une organisation (tarif dégressif) |
| **Perpetual License** | Licence perpétuelle payée une fois, utilisable indéfiniment |
| **Subscription** | Licence par abonnement payée mensuellement ou annuellement |
| **Audit trail** | Trace documentaire prouvant la légalité des licences (factures, contrats) |
| **Réconciliation** | Processus de rapprochement entre licences achetées et logiciels installés |

---

## ✅ Auto-évaluation : Suis-je Prêt ?

- [ ] Je distingue les 7 types de licences logicielles
- [ ] J'explique le risque juridique et financier du non-respect des licences
- [ ] Je calcule un taux de conformité à partir d'un inventaire
- [ ] Je calcule le TCO d'un logiciel sur 5 ans
- [ ] Je configure une alerte d'expiration dans GLPI
- [ ] Je produis un rapport de conformité à partir d'un inventaire OCS/GLPI
- [ ] J'explique la différence entre Named User et Concurrent License
