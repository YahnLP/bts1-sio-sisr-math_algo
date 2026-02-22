# Semaine 7 (S7) - BLOC 1
## 🚀 Mise à Disposition de Services · Qualité de Service · SLA · Disponibilité

---

# 📚 FICHE DE COURS ÉLÈVE
## "Mise à Disposition · Qualité de Service · SLA · Disponibilité"

*Version 1.0 — BTS SIO SISR — Année 1 — Semaine 7*

---

## 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|---------------|
| **B1.5** | Mettre à disposition des utilisateurs un service informatique |
| **B1.2** | Exploiter des référentiels et standards (ITIL) |
| **B1.6** | Assurer le support des utilisateurs |

---

## PARTIE I — Mettre à Disposition un Service IT

### I.A. Les 5 Étapes de la Mise à Disposition

Mettre un service à disposition des utilisateurs est un **processus en 5 étapes**. Chaque étape produit un livrable documentaire.

```
  ①  ANALYSE DU BESOIN
  ───────────────────────────────────────────────────
  Comprendre ce que les utilisateurs ont besoin de faire
  (pas seulement ce qu'ils demandent).

  Livrables : cahier des charges, expression de besoins
  Questions clés :
    - Combien d'utilisateurs utiliseront ce service ?
    - Quand ont-ils besoin d'y accéder ? (horaires, mobilité)
    - Quelles données traitera ce service ? (sensibilité RGPD)
    - Quel niveau de disponibilité est requis ?
    - Quel est le délai de mise en place ?

  ───────────────────────────────────────────────────
  ②  INSTALLATION ET TESTS
  ───────────────────────────────────────────────────
  Déployer le service dans un environnement de test,
  puis en production après validation.

  Livrables : plan de tests, PV de recette (résultats des tests)
  Bonnes pratiques :
    - Tester AVANT la mise en production
    - Tester les cas normaux ET les cas limites
    - Tester la restauration (pas seulement la sauvegarde)
    - Faire valider les tests par quelqu'un d'autre que celui
      qui a installé le service

  ───────────────────────────────────────────────────
  ③  DOCUMENTATION TECHNIQUE
  ───────────────────────────────────────────────────
  Documenter le service pour permettre sa maintenance
  par n'importe quel technicien de l'équipe.

  Livrables : DAT (Dossier d'Architecture Technique),
              procédures d'exploitation, guide de dépannage
  Contenu minimal :
    - Architecture (schéma + description)
    - Configuration (paramètres, fichiers de conf)
    - Procédures : démarrage, arrêt, sauvegarde, restauration
    - Contacts (responsable technique, fournisseur, support N2)

  ───────────────────────────────────────────────────
  ④  COMMUNICATION AUX UTILISATEURS
  ───────────────────────────────────────────────────
  Informer les utilisateurs de l'existence du service,
  de comment y accéder et de comment obtenir du support.

  Livrables : email/note d'information, guide utilisateur,
              entrée dans la base de connaissances GLPI
  Contenu obligatoire :
    - Quoi : nom et description du service en termes métier
    - Pourquoi : bénéfice pour l'utilisateur
    - Comment accéder : procédure simple, pas de jargon
    - Qui contacter en cas de problème
    - Date de disponibilité

  ───────────────────────────────────────────────────
  ⑤  VALIDATION ET SUIVI (PV de Mise en Service)
  ───────────────────────────────────────────────────
  Formaliser la mise en production et définir
  les indicateurs de suivi.

  Livrables : PV de mise en service signé,
              SLA défini, supervision configurée
  Ce qui est validé :
    - Tests de recette passés avec succès
    - Documentation disponible et à jour
    - Utilisateurs informés
    - Supervision active (alertes configurées)
    - SLA formalisé et accepté par les parties
```

---

### I.B. Le PV de Mise en Service

Le **Procès-Verbal de Mise en Service** (ou **PV de recette**) est le document qui formalise qu'un service est prêt à être utilisé en production. C'est la signature qui marque le passage de "en test" à "en production".

Il contient systématiquement :

| **Section** | **Contenu** |
|---|---|
| **Identification** | Nom du service, version, date, technicien responsable |
| **Périmètre** | Ce qui est mis en service (et ce qui ne l'est pas encore) |
| **Tests réalisés** | Liste des tests avec résultat attendu / résultat obtenu |
| **Anomalies constatées** | Problèmes identifiés (même mineurs) avec leur statut |
| **Conditions de mise en service** | Réserves éventuelles (ex : "sous réserve de la sauvegarde quotidienne") |
| **Validation** | Signature du technicien + du responsable DSI (+ client si externe) |
| **SLA applicable** | Référence au SLA en vigueur pour ce service |

> 📌 **Lien avec l'E5 :** Le jury E5 peut demander "comment avez-vous validé que votre service était prêt à être mis en production ?" Un PV de mise en service est la réponse professionnelle à cette question.

---

### I.C. Communication Utilisateur — Bonnes Pratiques

La communication aux utilisateurs est souvent négligée par les techniciens. Pourtant, un service inconnu ou mal expliqué n'est pas utilisé — et un service pas utilisé n'a aucune valeur.

**Les 5 erreurs courantes dans une communication IT :**

| **Erreur** | **Exemple** | **Bonne pratique** |
|---|---|---|
| **Jargon technique** | "Le serveur SFTP est accessible sur le port 22" | "Vos fichiers sont maintenant accessibles depuis n'importe où" |
| **Oublier le bénéfice** | "Un partage réseau a été créé" | "Fini les clés USB : vos fichiers sont maintenant partagés et sauvegardés automatiquement" |
| **Procédure trop complexe** | 2 pages de configuration | 3 étapes illustrées |
| **Pas de contact support** | — | "En cas de problème : ticket GLPI, catégorie Réseau > Partage de fichiers" |
| **Pas de date** | "Disponible prochainement" | "Disponible à partir du lundi 15 mars à 8h" |

---

## PARTIE II — Qualité de Service

### II.A. La Disponibilité

La **disponibilité** d'un service IT est le pourcentage de temps pendant lequel ce service est accessible et fonctionnel. C'est l'indicateur de qualité de service le plus fondamental.

```
   Disponibilité (%) =  Temps de fonctionnement  × 100
                        ──────────────────────────────
                         Temps total de la période
```

**Les "nines" — Référence universelle en DSI :**

| **Disponibilité** | **Indisponibilité / an** | **Indisponibilité / mois** | **Usage typique** |
|---|---|---|---|
| **90%** ("one nine") | 36 jours 12h | 73 heures | Service non critique |
| **99%** ("two nines") | 3 jours 15h | 7h 18 min | Service standard |
| **99,5%** | 1 jour 19h | 3h 39 min | SLA PME typique |
| **99,9%** ("three nines") | 8h 45 min | 43 min | Service professionnel |
| **99,99%** ("four nines") | 52 min | 4 min 22s | Service critique (banque, santé) |
| **99,999%** ("five nines") | 5 min 15s | 26s | Téléphonie, bloc opératoire |

> 💡 **Le déclic pédagogique :** "99% de disponibilité ça semble très bien... jusqu'à ce qu'on réalise que ça représente 3 jours et demi de panne par an. Si votre service de messagerie est en panne 3 jours et demi, que se passe-t-il dans l'entreprise ?"

---

### II.B. Calcul de Disponibilité — Formules

**Formule de base :**
```
   Disponibilité = (Temps total - Temps d'indisponibilité) / Temps total × 100

   Exemple :
   Service disponible 8 715 heures sur 8 760 heures (1 an)
   → Disponibilité = 8 715 / 8 760 × 100 = 99,49%
   → Indisponibilité = 8 760 - 8 715 = 45 heures dans l'année
```

**Indisponibilité tolérable selon un SLA :**
```
   Indisponibilité max = Temps total × (1 - Disponibilité contractuelle)

   Exemple : SLA 99,9% sur 1 an (8 760 heures)
   → Indisponibilité max = 8 760 × (1 - 0,999) = 8,76 heures/an
   → Soit environ 8 heures 45 minutes de panne autorisées sur l'année
```

**Disponibilité sur une période personnalisée :**
```
   Heures disponibles dans 1 an  = 365 × 24 = 8 760 h
   Heures disponibles en 1 mois  = 730 h (moyenne)
   Heures disponibles en 1 semaine = 168 h

   Disponibilité 99,9% mensuelle :
   → 730 × (1 - 0,999) = 0,73 heure = 43 minutes 48 secondes
```

---

### II.C. Disponibilité Planifiée vs Non Planifiée

Toute indisponibilité n'est pas équivalente. Une DSI mature distingue deux types :

| **Type** | **Définition** | **Exemple** | **Comptabilisé dans le SLA ?** |
|---|---|---|---|
| **Maintenance planifiée** | Interruption programmée, annoncée à l'avance | Mise à jour Windows, sauvegarde hebdomadaire | Souvent **exclu** du SLA |
| **Indisponibilité non planifiée** | Panne ou interruption imprévue | Disque dur défaillant, panne réseau | Toujours **inclus** dans le SLA |

> 📌 **Pourquoi cette distinction est-elle cruciale ?** Un SLA à 99,9% qui exclut les maintenances planifiées (30 minutes/semaine = 26h/an) est très différent d'un SLA à 99,9% sur le temps total. La **plage horaire** et les **exclusions** d'un SLA sont aussi importantes que le pourcentage lui-même.

---

### II.D. Le SLA Complet — Toutes les Composantes

En S3, vous avez vu les composantes de base d'un SLA. En S7, voici le SLA complet tel qu'il est rédigé en contexte professionnel :

```
╔══════════════════════════════════════════════════════════════════╗
║              SERVICE LEVEL AGREEMENT — STRUCTURE COMPLÈTE        ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  1. PARTIES ET OBJET                                             ║
║     Prestataire de service (DSI), client (département/entité)   ║
║     Service concerné, durée du SLA, conditions de révision      ║
║                                                                  ║
║  2. DESCRIPTION DU SERVICE                                       ║
║     Ce que le service fait (en termes métier, pas technique)    ║
║     Ce qu'il ne fait PAS (périmètre explicite)                   ║
║     Conditions d'utilisation nominale                            ║
║                                                                  ║
║  3. DISPONIBILITÉ                                                ║
║     Taux de disponibilité contractuel (ex : 99,5%)              ║
║     Plage horaire couverte (ex : lundi-vendredi 8h-19h)         ║
║     Maintenance planifiée : fenêtre et préavis                   ║
║     Méthode de calcul et de mesure                               ║
║                                                                  ║
║  4. DÉLAIS DE SUPPORT                                            ║
║     Priorité P1 : prise en charge < 15 min, résolution < 4h     ║
║     Priorité P2 : prise en charge < 1h, résolution < 8h         ║
║     Priorité P3 : prise en charge < 4h, résolution < 24h        ║
║     Priorité P4 : résolution < 5 jours ouvrés                   ║
║                                                                  ║
║  5. CONTINUITÉ ET REPRISE (RTO / RPO)                           ║
║     RTO : délai maximum de reprise après incident majeur        ║
║     RPO : perte de données maximale acceptable                  ║
║                                                                  ║
║  6. EXCLUSIONS ET LIMITATIONS                                    ║
║     Cas non couverts (erreur utilisateur, cas de force majeure) ║
║     Conditions d'annulation du SLA                              ║
║                                                                  ║
║  7. INDICATEURS ET REPORTING                                     ║
║     KPIs mesurés, fréquence des rapports, responsable           ║
║                                                                  ║
║  8. PÉNALITÉS ET COMPENSATIONS                                   ║
║     Conséquences en cas de non-respect (réduction facture,      ║
║     crédits de service...)                                       ║
║                                                                  ║
║  9. RÉVISION ET RÉSILIATION                                      ║
║     Fréquence de révision du SLA, conditions de résiliation     ║
╚══════════════════════════════════════════════════════════════════╝
```

---

### II.E. RTO et RPO — Continuité de Service

Ces deux indicateurs définissent les **objectifs de reprise** après un incident majeur (panne grave, sinistre, cyberattaque) :

```
   INCIDENT MAJEUR
   ──────────────────────────────────────────────────────────────────

   Dernière        Incident         Reprise du        Retour
   sauvegarde      survient         service           à la normale
   propre          │                │                 │
       │           │                │                 │
       ├───────────┼────────────────┼─────────────────┤
       │           │                │
       ◄── RPO ───►◄───── RTO ──────►

   RPO (Recovery Point Objective)
   ────────────────────────────────
   Perte de données maximale acceptable.
   "Jusqu'où peut-on remonter dans le temps ?"
   Ex : RPO = 4h → on accepte de perdre au maximum 4h de données
   → Sauvegarde toutes les 4h minimum

   RTO (Recovery Time Objective)
   ────────────────────────────────
   Durée maximale acceptable pour reprendre le service.
   "En combien de temps maximum faut-il être rétabli ?"
   Ex : RTO = 2h → le service doit être restauré en moins de 2h
   → Nécessite un serveur de secours, des procédures de bascule...
```

**Les RTO/RPO varient selon la criticité du service :**

| **Type de service** | **RTO typique** | **RPO typique** |
|---|---|---|
| Service critique (messagerie, ERP) | < 2 heures | < 1 heure |
| Service important (partage de fichiers) | < 8 heures | < 4 heures |
| Service standard (intranet) | < 24 heures | < 24 heures |
| Service non critique (outil interne) | < 72 heures | < 24 heures |

> 💡 **Relation RTO/RPO avec la sauvegarde :** Un RPO de 4h impose une sauvegarde au moins toutes les 4h. Un RTO de 2h impose de disposer d'un environnement de secours capable de prendre le relais en moins de 2h. Ces exigences ont un **coût** direct — c'est pourquoi chaque service n'a pas les mêmes objectifs.

---

### II.F. Supervision et Alertes — Mesurer la Disponibilité

Un SLA ne peut pas être tenu sans **supervision** : il faut mesurer la disponibilité réelle pour la comparer à la disponibilité contractuelle.

```
   OUTILS DE SUPERVISION (aperçu — détaillés en S9)
   ─────────────────────────────────────────────────
   Nagios / Centreon     → Supervision infrastructure (ping, ports, services)
   Zabbix                → Supervision avancée (métriques, graphiques, alertes)
   PRTG                  → Supervision réseau et système (Windows/Linux)
   Uptime Robot          → Supervision web simple (gratuit, SaaS)
   Windows SNMP / WMI    → Intégré Windows Server pour la supervision locale

   Ce que la supervision mesure pour calculer la disponibilité :
   ├── Le service répond-il ? (ping, port TCP ouvert, HTTP 200)
   ├── Depuis quand est-il injoignable ? (horodatage de la panne)
   ├── Durée totale d'indisponibilité sur la période
   └── → Calcul automatique du taux de disponibilité réel
```

---

## PARTIE III — Synthèse Bloc 1 — Vue Complète

Le Bloc 1 (S1-S7) vous a donné une vision complète du **support et de la mise à disposition des services IT** :

```
   INVENTORIER               QUALIFIER                 TRAITER
   ──────────                ─────────                 ───────
   S2 Fiche technique   →    S3 ITIL, tickets,    →    S4 Incidents :
   S5 OCS Inventory          SLA, niveaux N1/2/3       diagnostic,
   S6 GLPI CMDB                                        résolution,
                                                       documentation

                                    ↓

   OUTILLER                  METTRE À DISPOSITION      MESURER
   ────────                  ────────────────────       ───────
   S6 GLPI tickets,     →    S7 Les 5 étapes,      →   S7 Disponibilité,
   base de connaissances,     PV de mise en service,    SLA complet,
   statistiques               communication users       RTO / RPO
```

---

## IV. Vocabulaire Clé

| **Terme** | **Définition** |
|-----------|---------------|
| **Mise à disposition** | Processus complet rendant un service accessible, documenté et utilisable par les utilisateurs |
| **PV de mise en service** | Document formalisant la mise en production d'un service après validation des tests |
| **Disponibilité** | Pourcentage de temps pendant lequel un service est accessible et fonctionnel |
| **Uptime** | Temps de fonctionnement d'un service (anglais pour "disponibilité") |
| **Downtime** | Temps d'indisponibilité d'un service |
| **"Nines"** | Convention de notation de la disponibilité : 99% = "two nines", 99,9% = "three nines"... |
| **Maintenance planifiée** | Interruption programmée et annoncée à l'avance (souvent exclue du SLA) |
| **RTO** | Recovery Time Objective — délai maximum pour reprendre un service après incident |
| **RPO** | Recovery Point Objective — perte de données maximale acceptable |
| **SLA** | Service Level Agreement — contrat définissant le niveau de service attendu |
| **Supervision** | Surveillance automatisée de l'état des services pour détecter les pannes |
| **Taux de disponibilité** | Pourcentage calculé : temps de fonctionnement / temps total × 100 |
| **Plage horaire** | Période durant laquelle le SLA s'applique (ex : 8h-18h jours ouvrés) |
| **Fenêtre de maintenance** | Créneau prévu et communiqué pour les interventions planifiées |
| **Continuité de service** | Capacité à maintenir ou reprendre rapidement un service après incident |
| **Critère d'acceptation** | Condition qui doit être remplie pour valider la mise en production |

---

## ✅ Auto-évaluation : Suis-je Prêt ?

- [ ] Je décris les 5 étapes de mise à disposition d'un service
- [ ] J'explique la différence entre "installer" et "mettre à disposition"
- [ ] Je calcule un taux de disponibilité à partir d'un temps d'indisponibilité
- [ ] Je convertis un % de disponibilité en heures de panne annuelles
- [ ] Je distingue maintenance planifiée et indisponibilité non planifiée
- [ ] J'explique RTO et RPO avec un exemple concret
- [ ] Je rédige les sections essentielles d'un SLA
- [ ] Je rédige une communication utilisateur pour un nouveau service

