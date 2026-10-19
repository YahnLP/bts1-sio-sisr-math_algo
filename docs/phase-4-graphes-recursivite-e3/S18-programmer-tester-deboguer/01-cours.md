# Cours – Écrire, tester et déboguer un algorithme

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S18 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S03, S04, S12 (conditions, boucles, fonctions, tableaux) ; S15 (validation de données).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Reformuler** un énoncé : entrées, sortie, exemple à la main ;
- [ ] **Écrire** un algorithme en pseudo-code puis en Python ;
- [ ] **Choisir** des jeux de tests avec des cas limites ;
- [ ] **Dérouler** un algorithme par un suivi de variables ;
- [ ] **Repérer** et **corriger** des erreurs classiques.

## I. De l'énoncé au programme

À l'épreuve écrite, un exercice demande d'**écrire un programme** à partir d'un énoncé. La démarche suivante évite la plupart des erreurs.

1. **Reformuler** : quelles sont les **entrées** (types, valeurs possibles) ? Quelle est la **sortie** ?
2. **Faire un exemple à la main** sur un petit jeu de données, et noter le résultat attendu.
3. **Repérer le schéma** : accumulation (somme, compteur), recherche (arrêt dès qu'on trouve), maximum, série consécutive.
4. **Écrire le pseudo-code**, puis le traduire en Python.
5. **Tester** sur l'exemple et sur les cas limites (partie II).

### Les quatre schémas à connaître

| Schéma | Idée | Initialisation | Exemple |
|---|---|---|---|
| **Compteur** | ajouter 1 quand la condition est vraie | `n = 0` | nombre de relevés en alerte |
| **Accumulateur** | ajouter une valeur à chaque tour | `s = 0` | somme |
| **Recherche avec arrêt** | renvoyer dès qu'on trouve ; sinon valeur par défaut après la boucle | `-1` | premier relevé en alerte |
| **Maximum** | garder la meilleure valeur vue | première valeur de la liste | plus grand écart |

### Exemple complet : la plus longue série en alerte

**Énoncé.** Un relevé est une liste de températures. Un relevé est *en alerte* s'il est strictement supérieur au seuil. Écrire une fonction qui renvoie le plus grand nombre de relevés **consécutifs** en alerte.

- **Entrées :** une liste de nombres, un seuil. **Sortie :** un entier.
- **Exemple à la main** : `[21, 25, 27, 26, 31, 32, 33, 24, 29, 30]` avec le seuil 25. Les relevés en alerte sont 27, 26, 31, 32, 33 (cinq de suite), puis 29, 30 (deux de suite). Résultat attendu : 5.
- **Idée.** On garde deux compteurs : `courante` (longueur de la série en cours) et `meilleure` (plus longue série vue).

```text
ALGORITHME plus_longue_serie
RÔLE : plus grand nombre de relevés consécutifs au-dessus du seuil
ENTRÉE : releves, une liste de nombres ; seuil, un nombre
SORTIE : un entier
VARIABLES : courante, meilleure : entiers
DÉBUT
  courante ← 0
  meilleure ← 0
  POUR CHAQUE r DANS releves FAIRE
    SI r > seuil ALORS
      courante ← courante + 1
    SINON
      courante ← 0
    FIN SI
    SI courante > meilleure ALORS
      meilleure ← courante
    FIN SI
  FIN POUR
  RENVOYER meilleure
FIN
```

```python
def plus_longue_serie(releves, seuil):
    courante = 0
    meilleure = 0
    for r in releves:
        if r > seuil:
            courante = courante + 1
        else:
            courante = 0
        if courante > meilleure:
            meilleure = courante
    return meilleure
```

## II. Tester : choisir les cas limites

Un test réussi ne prouve pas que le programme est correct ; un jeu de tests bien choisi donne simplement **confiance**. Pour une fonction qui parcourt un tableau, on teste toujours :

- un cas **normal** ;
- le tableau **vide** ;
- un tableau d'**un seul** élément ;
- des **valeurs égales** ou **à la frontière** (ici : un relevé exactement égal au seuil) ;
- le cas où la condition est **toujours** vraie et celui où elle est **jamais** vraie ;
- une valeur recherchée en **première** et en **dernière** position.

Pour `plus_longue_serie` avec le seuil 25 : `[]` donne 0 ; `[25]` donne 0 (25 n'est pas strictement supérieur à 25) ; `[30]` donne 1 ; `[30, 10, 30]` donne 1 ; `[30, 31, 32]` donne 3 (la série est à la fin : `meilleure` doit être mise à jour **dans** la boucle).

## III. Suivre les variables

Pour comprendre ce que fait un algorithme, ou pour trouver pourquoi il se trompe, on écrit un **tableau de suivi** : une ligne par tour de boucle, une colonne par variable.

Suivi de `plus_longue_serie` sur l'exemple (seuil 25) :

| Tour | `r` | `r > seuil` | `courante` | `meilleure` |
|---|---|---|---|---|
| 1 | 21 | non | 0 | 0 |
| 2 | 25 | non | 0 | 0 |
| 3 | 27 | oui | 1 | 1 |
| 4 | 26 | oui | 2 | 2 |
| 5 | 31 | oui | 3 | 3 |
| 6 | 32 | oui | 4 | 4 |
| 7 | 33 | oui | 5 | 5 |
| 8 | 24 | non | 0 | 5 |
| 9 | 29 | oui | 1 | 5 |
| 10 | 30 | oui | 2 | 5 |

Le résultat est `meilleure = 5`, conforme à l'exemple à la main.

## IV. Repérer et corriger des erreurs

On distingue les erreurs de **syntaxe** (le programme ne démarre pas), d'**exécution** (il plante : message d'erreur) et de **logique** (il tourne mais donne un mauvais résultat). Les plus difficiles sont les dernières : on les trouve par le suivi de variables.

**Méthode.** (1) Reproduire l'erreur avec un petit exemple ; (2) écrire sur papier la valeur des variables à chaque tour ; (3) repérer le premier tour où une valeur n'est pas celle attendue ; (4) corriger ; (5) retester, y compris les cas limites.

| Erreur classique | Exemple | Résultat observé | Correction |
|---|---|---|---|
| **Indice hors domaine** | `for i in range(len(t) + 1): s += t[i]` | IndexError | `range(len(t))` |
| **Début de parcours oublié** | `for i in range(1, len(t))` pour parcourir tout le tableau | le premier élément est ignoré | `range(len(t))` |
| **Mauvaise initialisation** | maximum avec `m = 0` sur `[-5, -2, -9]` | renvoie 0, valeur absente de la liste | `m = t[0]` |
| **Arrêt trop tôt** | `return True` dans la boucle dès qu'un couple est bon | un seul couple est examiné | renvoyer `False` dans la boucle, `True` **après** |
| **Variant non modifié** | `while i < 10:` sans `i = i + 1` | boucle infinie | mettre à jour `i` |
| **Égalité de flottants** | `0.1 + 0.2 == 0.3` | False (la somme vaut `0.30000000000000004`) | comparer avec une tolérance, ou travailler en entiers / `Fraction` |
| **Division entière** | `1 // 4 * 100` au lieu de `1 * 100 / 4` | 0 au lieu de 25 | multiplier avant de diviser, ou utiliser `/` |
| **Effet de bord** | `def f(l): l.append(1)` sur la liste de l'appelant | la liste de l'appelant est modifiée | travailler sur une copie `list(l)` |
| **Confusion `=` et `==`** | `if x = 5:` | `SyntaxError` | `if x == 5:` |

**Exemple de suivi de variables.** Cette fonction doit renvoyer la moyenne des valeurs positives ; elle contient une erreur :

```python
def moyenne_positifs(t):
    s = 0
    n = 0
    for x in t:
        if x > 0:
            s = s + x
        n = n + 1
    return s / n
```

Pour `t = [4, -2, 6]` :

| Tour | `x` | `x > 0` | `s` | `n` |
|---|---|---|---|---|
| 1 | 4 | oui | 4 | 1 |
| 2 | −2 | non | 4 | **2** |
| 3 | 6 | oui | 10 | 3 |

Le compteur `n` s'incrémente **même quand \(x\) est négatif** : on obtient \(10 / 3\) au lieu de \(10 / 2 = 5\). Correction : placer `n = n + 1` **dans** le `if`. De plus, si aucune valeur n'est positive, `n` vaut 0 et la division échoue : c'est un cas limite à traiter.

## À retenir

- Énoncé → entrées, sortie, exemple à la main, schéma (compteur, accumulateur, recherche, maximum), pseudo-code, Python, tests.
- Tester : cas normal, vide, un élément, égalités et frontières, toujours vrai, jamais vrai, début et fin.
- Un tableau de suivi (une ligne par tour, une colonne par variable) trouve le premier écart.
- Erreurs fréquentes : mauvaise initialisation, parcours incomplet, arrêt trop tôt, division entière, effet de bord.
