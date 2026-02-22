# 🖥️ FICHE TP — DISPONIBILITÉ · SLA · PV DE MISE EN SERVICE

*Durée : 50 minutes — Individuel*

---

## MODULE 1 — Calculs de Disponibilité (15 min)

### Exercice 1.1 — Calcul de base

Un service de messagerie a été en panne pendant les durées suivantes en 2024 :
- 12 février : 2 heures 30 minutes (panne réseau)
- 15 mai : 45 minutes (mise à jour planifiée)
- 3 août : 6 heures (disque défaillant)
- 19 novembre : 1 heure 15 minutes (coupure électrique)

2024 est une **année bissextile** (366 jours).

| **Question** | **Calcul** | **Résultat** |
|---|---|---|
| Durée totale d'indisponibilité | | h min |
| Temps total de l'année (en heures) | | h |
| Taux de disponibilité | | % |
| Le SLA de 99,5% est-il respecté ? | | ☐ Oui ☐ Non |

---

### Exercice 1.2 — Objectif de disponibilité → temps de panne

Calculer l'indisponibilité maximale tolérable par an et par mois pour chaque SLA :

| **SLA contractuel** | **Indisponibilité max / an** | **Indisponibilité max / mois** |
|---|---|---|
| 99% | | |
| 99,5% | | |
| 99,9% | | |
| 99,99% | | |

*(Utiliser : 1 an = 8 760h, 1 mois = 730h)*

---

### Exercice 1.3 — Analyse d'un rapport mensuel

Le rapport de supervision du mois d'octobre (744 heures) indique :

| **Service** | **Temps d'indisponibilité** | **Dont planifié** | **Disponibilité réelle** | **SLA contractuel** | **Respecté ?** |
|---|---|---|---|---|---|
| Messagerie | 2h 15min | 30min | | 99,9% | |
| Partage de fichiers | 5h 00min | 1h 00min | | 99,5% | |
| Intranet | 0h 45min | 0h | | 99,5% | |
| VPN | 12h 30min | 2h | | 99% | |

> **Question :** Pour le service VPN, en distinguant indisponibilité planifiée et non planifiée, quel est le taux de disponibilité "hors maintenance" ? Le SLA est-il respecté sur cette base ?

```
Calcul : _______________________________________________________________
Réponse : ______________________________________________________________
```

---

## MODULE 2 — Rédiger un SLA (20 min)

### Contexte

SimIO SARL (80 employés) vient de déployer un **serveur de fichiers partagés** sur Windows Server. Vous êtes technicien DSI et vous devez rédiger le SLA de ce service pour les 6 prochains mois.

Informations à votre disposition :
- Le service est utilisé par tous les employés du lundi au vendredi, de 7h30 à 19h
- La maintenance est possible chaque dimanche entre 22h et 6h
- Le serveur est sauvegardé toutes les nuits à 23h
- Une panne du serveur de fichiers bloquerait le travail de tous les services
- L'équipe DSI (2 techniciens) travaille de 8h à 18h en semaine

Rédiger un SLA en complétant le modèle ci-dessous :

---

**SLA — Service de Partage de Fichiers — SimIO SARL**

| **Section** | **Contenu à rédiger** |
|---|---|
| **1. Parties** | Prestataire : DSI SimIO SARL / Bénéficiaire : |
| **2. Service couvert** | |
| **3. Ce qui est EXCLU du service** | |
| **4. Plage horaire du SLA** | |
| **5. Disponibilité contractuelle** | % |
| **6. Maintenance planifiée** | Fenêtre : ___ Préavis : ___ |
| **7. Délais de support P1** | Prise en charge < ___ Résolution < ___ |
| **8. Délais de support P2** | Prise en charge < ___ Résolution < ___ |
| **9. Délais de support P3** | Prise en charge < ___ Résolution < ___ |
| **10. RPO (perte données max)** | |
| **11. RTO (reprise max après incident majeur)** | |
| **12. KPI mesurés** | |
| **13. Rapport mensuel** | Fourni le : ___ Par : ___ |
| **14. Exclusions** | |

---

**Question de réflexion :** Vous avez défini un RTO de 4h pour ce service. Quelle infrastructure technique est nécessaire pour tenir cet objectif en cas de panne du serveur principal ? Citez au moins 2 éléments.

```
Élément 1 : ____________________________________________________________
Élément 2 : ____________________________________________________________
```

---

## MODULE 3 — PV de Mise en Service + Communication (15 min)

### Contexte

Vous venez de déployer le serveur de fichiers partagés de SimIO SARL. Tous les tests sont passés. Vous devez maintenant :
1. Rédiger le **PV de mise en service** (version simplifiée)
2. Rédiger la **communication** envoyée aux 80 employés

---

### 3.1 — PV de Mise en Service (simplifié)

| **Section** | **Contenu** |
|---|---|
| **Service** | Partage de fichiers SimIO SARL |
| **Technicien** | [Votre nom] |
| **Date de mise en service** | |
| **Version** | 1.0 |
| **Tests réalisés** | |
| Test 1 | Accès depuis un poste VLAN RH → Résultat : |
| Test 2 | Accès refusé pour un utilisateur sans droits → Résultat : |
| Test 3 | Sauvegarde nocturne → Résultat : |
| Test 4 | Restauration d'un fichier sauvegardé → Résultat : |
| Test 5 | Accès depuis un poste hors domaine → Résultat : |
| **Anomalies constatées** | |
| **Conditions de mise en service** | |
| **SLA applicable** | Référence : SLA-SimIO-Fichiers-v1.0 |
| **Signature technicien** | |
| **Signature responsable DSI** | |

---

### 3.2 — Communication aux Utilisateurs

Rédiger l'email envoyé aux 80 employés de SimIO SARL pour leur annoncer la mise en service du partage de fichiers. Respecter les bonnes pratiques du cours (pas de jargon, bénéfice clair, procédure simple, contact support).

```
DE      : dsi@siosarl.local
À       : tous@siosarl.local
OBJET   : _______________________________________________________________

Bonjour à toutes et tous,

________________________________________________________________________
________________________________________________________________________
________________________________________________________________________
________________________________________________________________________
________________________________________________________________________
________________________________________________________________________
________________________________________________________________________
________________________________________________________________________

Cordialement,
L'équipe DSI SimIO SARL
```
