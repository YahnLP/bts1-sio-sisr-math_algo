# S05 – Divisibilité, division euclidienne et PGCD

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S05 (séance 5 sur 19) – Phase 1 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Arithmétique – division euclidienne, PGCD |
| **Prérequis** | S01 ; S04 (boucle tant que). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Comment savoir si un nombre en divise un autre, et comment trouver leur plus grand diviseur commun sans énumérer tous les diviseurs ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Effectuer** une division euclidienne et **énoncer** son résultat \(a = bq + r\) avec \(0 \le r < b\) ;
2. **Utiliser** les critères de divisibilité (2, 3, 5, 9, 10) ;
3. **Déterminer** les diviseurs et les multiples d'un entier ;
4. **Calculer** un PGCD par l'algorithme d'Euclide et **justifier** que l'algorithme s'arrête ;
5. **Reconnaître** deux entiers premiers entre eux et **calculer** un PPCM.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Divisibilité et PGCD](01-cours.md) | Cours |
| [Exercices – Division euclidienne, diviseurs, PGCD](02-exercices.md) | Exercices |
| [TP Python – Algorithme d'Euclide](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Division euclidienne et PGCD](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Accroche** : découper un écran de 1 920 × 1 080 en carrés identiques | Oral |
| 0 h 20 – 1 h 30 | **Cours** : division euclidienne, diviseurs, algorithme d'Euclide | Cours et questions |
| 1 h 30 – 2 h 45 | **Exercices** | Individuel, puis binômes |
| 2 h 45 – 3 h 45 | **TP Python** : Euclide, PPCM, critères | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Découper un espace en blocs identiques, synchroniser deux tâches périodiques (PPCM), comprendre pourquoi des cycles de parcours se recoupent (S07).

## Évaluation

- Feuille d'exercices corrigée, scripts du TP validés.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)) ; la répartition en séances est une proposition à valider.
- **Corrigé :** dans `corriges/` à la racine du dépôt (hors du site publié).
- Le programme demande le PGCD de deux entiers ; la relation de Bézout n'est pas exigée et n'est pas traitée.

</details>
