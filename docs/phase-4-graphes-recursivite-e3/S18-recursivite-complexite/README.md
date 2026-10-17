# S18 – Algorithmique : récursivité, complexité et débogage

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S18 (séance 18 sur 19) – Phase 4 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Algorithmique appliquée – récursivité, complexité, effets indésirables |
| **Prérequis** | S04, S12 (boucles, fonctions, tableaux) ; S15 (suites). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Comment écrire un algorithme qui s'appelle lui-même sans tourner indéfiniment, et comparer deux algorithmes sans les chronométrer ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Écrire** un algorithme récursif avec test d'arrêt et cas de base ;
2. **Dérouler** les appels récursifs et **vérifier** la terminaison ;
3. **Passer** d'une version récursive à une version itérative (récursivité terminale) ;
4. **Compter** le nombre d'opérations significatives dans le pire cas (recherche séquentielle, dichotomique, tri par sélection) ;
5. **Repérer** et **corriger** des erreurs classiques (indices hors domaine, effets de bord, approximations) par suivi de variables.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Récursivité et complexité](01-cours.md) | Cours |
| [Exercices – Algorithmes récursifs, coût et erreurs](02-exercices.md) | Exercices |
| [TP Python – Récursivité et débogage](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Récursivité et complexité](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 15 | **Rappel** S04 et S12 | Oral |
| 0 h 15 – 1 h 30 | **Cours** : récursivité, complexité, effets indésirables | Cours et questions |
| 1 h 30 – 2 h 30 | **Exercices** | Individuel |
| 2 h 30 – 3 h 45 | **TP Python** : récursivité, compteurs, algorithmes à corriger | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Parcours récursif d'une arborescence de dossiers, choix entre recherche séquentielle et dichotomique selon la taille des données, diagnostic d'un script qui boucle ou plante.

## Évaluation

- Feuille d'exercices corrigée, scripts du TP validés.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)) ; la répartition en séances est une proposition à valider.
- **Corrigé :** dans `corriges/` à la racine du dépôt (hors du site publié).
- Le programme exclut la récursivité mutuelle ; la complexité est limitée au calcul d'un nombre minimal ou maximal d'opérations significatives.

</details>
