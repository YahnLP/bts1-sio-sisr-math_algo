# S14 – Calcul matriciel : inverse et systèmes

| Élément | Détail |
|---|---|
| **Niveau** | BTS SIO option SISR, 1re année – mathématiques pour l'informatique |
| **Séance** | S14 (séance 14 sur 19) – Phase 3 |
| **Durée** | 4 heures |
| **Chapitre du programme** | Calcul matriciel – inverse, systèmes de Cramer |
| **Prérequis** | S13 (produit de matrices). |
| **Outils** | Papier, calculatrice, éditeur Python intégré au site |

> [!NOTE]
> **Question qui guide la séance :** *« Comment résoudre un système d'équations linéaires avec des matrices ? »*

## Objectifs

À la fin de la séance, l'étudiant est capable de :

1. **Définir** l'inverse d'une matrice carrée et **vérifier** qu'une matrice en est l'inverse ;
2. **Écrire** un système linéaire sous la forme \(AX = B\) ;
3. **Résoudre** un système de Cramer avec \(X = A^{-1}B\) ;
4. **Calculer** l'inverse d'une matrice par la méthode itérative (opérations sur les lignes) ;
5. **Reconnaître** une matrice non inversible au cours du calcul.

## Contenu de la séance

| Document | Rôle |
|---|---|
| [Cours – Inverse et systèmes](01-cours.md) | Cours |
| [Exercices – Inverse et systèmes linéaires](02-exercices.md) | Exercices |
| [TP Python – Méthode de Gauss](03-tp-python.md) | TP (éditeur Python intégré) |
| [Aide-mémoire – Inverse et systèmes](04-aide-memoire.md) | Aide-mémoire |

## Déroulé conseillé (4 h)

| Durée | Activité | Format |
|---|---|---|
| 0 h 00 – 0 h 20 | **Rappel** S13 et accroche : deux commandes, deux prix inconnus | Oral |
| 0 h 20 – 1 h 30 | **Cours** : inverse, systèmes de Cramer, méthode des lignes | Cours et questions |
| 1 h 30 – 2 h 45 | **Exercices** | Individuel, puis binômes |
| 2 h 45 – 3 h 45 | **TP Python** : résolution exacte avec des fractions | Individuel |
| 3 h 45 – 4 h 00 | **Auto-évaluation** | Individuel |

*Durées indicatives : la séance dure 4 h ; l'enseignant ajuste selon le rythme du groupe.*

## Application en informatique

Retrouver des tarifs unitaires à partir de factures, dimensionner des ressources à partir de mesures, systèmes d'équations de flux.

## Évaluation

- Feuille d'exercices corrigée, scripts du TP validés.
- Auto-évaluation « Je sais faire » en fin d'exercices.

<details markdown="1">
<summary>Notes pour l'enseignant</summary>

- **Programme :** le chapitre est rattaché au programme officiel de mathématiques pour l'informatique (voir [Programme et épreuve E3](../../ressources/programme-e3.md)) ; la répartition en séances est une proposition à valider.
- Le programme exclut le déterminant et les conditions d'existence de l'inverse : la méthode des lignes montre l'inversibilité par le calcul, sans théorème. Les justifications de la méthode ne sont pas exigées.

</details>
