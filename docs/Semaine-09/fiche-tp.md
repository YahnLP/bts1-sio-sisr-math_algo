# 🖥️ TP PARTIE 1 — CATALOGUE DE SERVICES SIMIO SARL

*Durée : 35 minutes — En binôme*

---

## Objectif

Construire le catalogue de services IT de SimIO SARL (80 employés) à partir de tous les services abordés depuis S2. Chaque binôme se voit attribuer 2 services à documenter complètement.

---

## Attribution des Services

| **Binôme** | **Services à documenter** |
|---|---|
| Binôme 1 | Messagerie d'entreprise + Réinitialisation de mot de passe |
| Binôme 2 | Partage de fichiers + Impression réseau |
| Binôme 3 | Helpdesk N1 (centre de services) + Accès VPN |
| Binôme 4 | Gestion des postes de travail + Installation de logiciels |
| Binôme 5 | Accès Internet + WiFi entreprise |
| Binôme 6 (si présent) | Sauvegarde et restauration + Création de compte utilisateur |

---

## Modèle de Fiche de Service à Compléter

*(Utiliser le modèle Annexe 1 — 1 fiche par service)*

Pour chaque service, vous devrez renseigner :

**Fiche vue MÉTIER (pour le portail GLPI / utilisateurs) :**

| **Section** | **Instructions de rédaction** |
|---|---|
| **Nom du service** | Court, clair, en termes métier — pas d'acronyme |
| **Description en 3 lignes** | Ce que ça fait pour l'utilisateur — pas comment ça marche |
| **Bénéficiaires** | Qui y a accès (tous ? certains services ?) |
| **Conditions d'accès** | Prérequis (compte AD, être employé, avoir demandé...) |
| **Comment y accéder** | Procédure en 2-3 étapes simples |
| **Fonctionnalités incluses** | Liste des capacités couvertes |
| **Exclusions importantes** | Ce que le service ne fait PAS (2-3 points max) |
| **Disponibilité** | Plage horaire + taux SLA (choisir un niveau cohérent) |
| **Délai si problème** | Priorité et délai de résolution |
| **Comment signaler un problème** | Catégorie GLPI + canal |

**Fiche vue TECHNIQUE (pour la DSI — interne) :**

| **Section** | **Instructions** |
|---|---|
| **Infrastructure support** | Serveur(s), logiciel(s) qui délivrent ce service |
| **Composants dépendants** | Ce dont ce service a besoin (ex : AD pour la messagerie) |
| **SLA interne** | RTO + RPO définis |
| **Responsable technique** | Qui maintient ce service |
| **Procédures associées** | Démarrage, arrêt, sauvegarde (référence DAT) |
| **Supervision** | Comment la disponibilité est mesurée |

---

## Mise en Commun (10 min inclus)

En fin de TP, chaque binôme présente ses 2 fiches en 3 minutes. La classe vote pour les formulations "vue métier" les plus claires (sans jargon). L'enseignant consolide le catalogue SimIO final sur un document partagé.

---

---

# ✍️ TP PARTIE 2 — RÉDIGER LA SPS #1

*Durée : 80 minutes — Individuel*

---

## Étape 0 — Choisir sa Réalisation (10 min)

Parmi tous les travaux réalisés depuis S2, choisir celui qui vous semble le plus riche à formaliser comme SPS. Utiliser la grille suivante pour choisir :

| **Réalisation** | **Preuves disponibles** | **Compétences RNCP** | **Score (1-5)** |
|---|---|---|---|
| Fiche technique poste de TP (S2) | Fiche remplie, rapport OCS | B1.1 | |
| Incidents résolus (S4) | Tickets, fiches KB | B1.6, B1.3 | |
| GLPI — tickets traités (S6) | Export tickets, captures | B1.3, B1.4 | |
| PV de mise en service (S7) | PV, SLA, email communication | B1.5, B1.2 | |
| Catalogue de services (S9) | Fiches de service, catalogue | B1.2, B1.5 | |

> **Conseil :** Choisir la réalisation pour laquelle vous avez le plus de preuves concrètes ET pour laquelle vous pouvez expliquer en détail ce que vous avez décidé et pourquoi.

**Réalisation choisie :** ________________________________________________

---

## Étape 1 — Rédiger le Contexte (10 min)

```
Contexte à rédiger (5-8 lignes) :

Organisation : SimIO SARL — PME de 80 employés dans le secteur [à compléter]
Infrastructure IT : [décrire l'environnement technique pertinent]
Votre rôle : Apprenti technicien SISR — dans le cadre de la formation BTS SIO
Période : [mois/année]

Votre rédaction :
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

---

## Étape 2 — Rédiger la Mission (8 min)

```
Mission à rédiger (3-5 lignes) :

Quel était l'objectif ? Qui vous l'a assigné ?
Quelles contraintes (délai, outils imposés, périmètre) ?

Votre rédaction :
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

---

## Étape 3 — Rédiger la Réalisation (25 min)

*C'est la section la plus longue — minimum 15 lignes. Répondre aux 4 questions suivantes :*

**3.1 — Qu'avez-vous fait, étape par étape ?**
```
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

**3.2 — Quelles décisions avez-vous prises et pourquoi ?**
*(Ex : "J'ai choisi de vérifier d'abord la couche physique parce que...")*
```
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

**3.3 — Quelles difficultés avez-vous rencontrées et comment les avez-vous surmontées ?**
```
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

**3.4 — Quels outils, commandes ou méthodes avez-vous utilisés ?**
*(Citer les outils/commandes spécifiques avec leur usage)*
```
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

---

## Étape 4 — Compétences Mobilisées (5 min)

Lister les compétences RNCP mobilisées. Pour chacune, indiquer 1 action concrète qui la justifie :

| **Code RNCP** | **Intitulé** | **Action concrète qui justifie** |
|---|---|---|
| | | |
| | | |
| | | |

---

## Étape 5 — Résultats et Validation (7 min)

```
Comment avez-vous vérifié que la réalisation était réussie ?
Qui a validé ? Y a-t-il des indicateurs mesurables ?

Votre rédaction :
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

---

## Étape 6 — Réflexivité (15 min)

*Section souvent bâclée — prenez le temps. Le jury y revient systématiquement.*

**6.1 — Qu'auriez-vous fait différemment si vous recommenciez ?**
```
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

**6.2 — Qu'est-ce que cette réalisation vous a appris professionnellement ?**
*(Pas "j'ai appris à utiliser GLPI" — mais "j'ai compris que la documentation en temps réel est indispensable parce que...")*
```
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________
```

**6.3 — Comment cette compétence est-elle utile dans votre futur métier ?**
```
___________________________________________________________________
___________________________________________________________________
```

---

## Étape 7 — Preuves (5 min)

Lister les preuves que vous allez joindre à cette SPS :

| **N°** | **Description de la preuve** | **Type** | **Disponible ?** |
|---|---|---|---|
| P1 | | | ☐ Oui ☐ À constituer |
| P2 | | | ☐ Oui ☐ À constituer |
| P3 | | | ☐ Oui ☐ À constituer |
| P4 | | | ☐ Oui ☐ À constituer |

---

## Étape 8 — Peer Review (15 min — En binôme)

Échanger votre brouillon de SPS avec votre voisin. Chacun lit la SPS de l'autre et remplit la grille ci-dessous :

| **Critère** | **Présent ?** | **Commentaire** |
|---|---|---|
| Le contexte permet de comprendre l'organisation sans question | ☐ Oui / ☐ Partiel | |
| La mission est clairement délimitée | ☐ Oui / ☐ Partiel | |
| La réalisation dit CE QUE l'auteur a fait (pas "on a fait") | ☐ Oui / ☐ Partiel | |
| Des décisions sont justifiées | ☐ Oui / ☐ Partiel | |
| Une difficulté est mentionnée avec sa résolution | ☐ Oui / ☐ Partiel | |
| Les compétences RNCP sont précisément citées | ☐ Oui / ☐ Partiel | |
| La section réflexivité va au-delà du résumé | ☐ Oui / ☐ Partiel | |
| Les preuves mentionnées correspondent à la réalisation | ☐ Oui / ☐ Partiel | |
| **La SPS est prête pour le jury ?** | ☐ Oui / ☐ À améliorer | |

**Mon conseil principal pour améliorer cette SPS :**
```
___________________________________________________________________
___________________________________________________________________
```

