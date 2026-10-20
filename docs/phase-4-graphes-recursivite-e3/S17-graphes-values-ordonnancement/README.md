# S17 – Graphes valués et ordonnancement (MPM)

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S17 (séance 17 sur 19) – Phase 4 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Théorie des graphes et ordonnancement |
| **Prérequis** | S16 (graphes, niveaux). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Comment trouver le chemin le moins coûteux, et planifier un projet en identifiant les tâches qui ne doivent pas prendre de retard ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Définir** un graphe valué et la longueur (valeur) d'un chemin ;
2. **Déterminer** un chemin de valeur minimale par une méthode donnée ;
3. **Construire** le graphe d'ordonnancement MPM d'un projet à partir d'un tableau de tâches ;
4. **Calculer** les dates au plus tôt et au plus tard, les marges totale, libre et certaine ;
5. **Identifier** les tâches critiques et le chemin critique, et **conclure** sur la durée minimale du projet.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Graphes valués et MPM](01-cours.md) | Cours |
| [Exercices – Chemin optimal et planification](02-exercices.md) | Exercices |
| [TP Python – Dates au plus tôt et au plus tard](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Chemin optimal et MPM](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Rappel** S16 et accroche : migrer des serveurs dans l'ordre | Oral |
| 0 h 20 – 1 h 35 | **Cours** : valuations, chemin optimal, MPM, marges | Cours et questions |
| 1 h 35 – 2 h 50 | **Exercices** | Individuel, puis binômes |
| 2 h 50 – 3 h 45 | **TP Python** : calcul des dates MPM | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Chemin de moindre coût entre deux sites d'un réseau, planification d'un projet de déploiement ou de migration, repérage des tâches critiques.

## Évaluation

- Feuille d'exercices corrigée, scripts du TP validés.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)).
- Le programme traite l'ordonnancement manuellement sur des cas modestes et demande que l'énoncé indique la méthode ; les définitions de marge libre et certaine sont rappelées dans le cours pour lever toute ambiguïté de vocabulaire.

</details>
