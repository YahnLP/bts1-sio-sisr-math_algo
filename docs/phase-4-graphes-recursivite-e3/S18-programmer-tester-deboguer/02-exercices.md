# Exercices – Énoncés, tests et erreurs

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S18*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, la calculatrice est autorisée selon les consignes du sujet : entraîne-toi à poser les calculs.

## Exercice 1 – Reformuler un énoncé

**Énoncé.** *Écrire une fonction `premiere_alerte(releves, seuil)` qui renvoie l'indice du premier relevé strictement supérieur au seuil, ou \(-1\) s'il n'y en a pas.*

1. Donner les entrées et la sortie.
2. Donner le résultat pour `[21, 25, 27, 26, 31]` avec le seuil 25, puis avec le seuil 40.
3. Écrire le pseudo-code.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Entrées : une liste de nombres et un seuil. Sortie : un entier (un indice, de 0 à `len(releves) - 1`, ou \(-1\)).
2. Seuil 25 : 21 et 25 ne sont pas strictement supérieurs à 25, 27 l'est : résultat 2. Seuil 40 : aucun relevé n'est en alerte : résultat \(-1\).
3.

```text
ALGORITHME premiere_alerte
ENTRÉE : releves, une liste de nombres ; seuil, un nombre
SORTIE : un entier
DÉBUT
  POUR i DE 0 À longueur(releves) - 1 FAIRE
    SI releves[i] > seuil ALORS
      RENVOYER i
    FIN SI
  FIN POUR
  RENVOYER -1
FIN
```

Le `RENVOYER -1` est **après** la boucle : on ne le renvoie que si aucun relevé n'a dépassé le seuil.

</details>

## Exercice 2 – Suivi de variables

On exécute `ecart_max([10, 14, 12, 12, 18])` avec :

```python
def ecart_max(releves):
    e = 0
    for i in range(len(releves) - 1):
        d = abs(releves[i + 1] - releves[i])
        if d > e:
            e = d
    return e
```

1. Écrire le tableau de suivi (colonnes `i`, `d`, `e`).
2. Que calcule cette fonction ? Que renvoie-t-elle pour `[]` et pour `[7]` ? Pourquoi `range(len(releves) - 1)` ?

<details markdown="1">
<summary>Voir la réponse</summary>

1.

| Tour | `i` | `d` | `e` |
|---|---|---|---|
| 1 | 0 | 4 | 4 |
| 2 | 1 | 2 | 4 |
| 3 | 2 | 0 | 4 |
| 4 | 3 | 6 | 6 |

Résultat : 6.

2. Le plus grand écart, en valeur absolue, entre deux relevés consécutifs. Pour `[]` et `[7]`, `range(...)` est vide (`len - 1` vaut \(-1\) ou 0) : la boucle ne s'exécute pas et le résultat est 0. On s'arrête à `len(releves) - 2` pour que `releves[i + 1]` existe : sinon, `IndexError`.

</details>

## Exercice 3 – Choisir les tests

On écrit `est_croissant(t)` qui renvoie `True` si les éléments de `t` sont rangés dans l'ordre croissant (au sens large : deux éléments égaux sont permis). Proposer sept tests, avec le résultat attendu, qui couvrent les cas limites.

<details markdown="1">
<summary>Voir la réponse</summary>

| Test | Attendu | Cas couvert |
|---|---|---|
| `[]` | `True` | tableau vide |
| `[3]` | `True` | un seul élément |
| `[1, 2, 5]` | `True` | cas normal |
| `[1, 2, 2, 5]` | `True` | valeurs égales (frontière) |
| `[5, 1]` | `False` | décroissant |
| `[1, 3, 2, 5]` | `False` | l'erreur est au milieu |
| `[1, 2, 3, 2]` | `False` | l'erreur est à la fin |

</details>

## Exercice 4 – Trouver l'erreur (arrêt trop tôt)

```python
def est_croissant(t):
    for i in range(len(t) - 1):
        if t[i] <= t[i + 1]:
            return True
    return False
```

1. Que renvoie cette fonction pour `[1, 3, 2, 5]` ? pour `[3]` ? Comparer au résultat attendu.
2. Corriger la fonction.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Pour `[1, 3, 2, 5]` : au tour `i = 0`, \(1 \le 3\), la fonction renvoie `True` immédiatement, alors que \(3 > 2\) : attendu `False`. Pour `[3]` : la boucle ne s'exécute pas, elle renvoie `False`, alors qu'attendu `True`.
2. Il faut renvoyer `False` **dès qu'un couple est dans le mauvais ordre**, et `True` seulement **après** avoir examiné tous les couples :

```python
def est_croissant(t):
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return False
    return True
```

</details>

## Exercice 5 – Division entière

```python
def pourcentage(partie, total):
    if total == 0:
        return 0
    return partie // total * 100
```

1. Que renvoie `pourcentage(1, 4)` ? Que devrait-elle renvoyer ?
2. Corriger. Que renvoie la version corrigée pour `pourcentage(1, 3)` ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. `1 // 4` vaut 0 (division entière), puis \(0 \times 100 = 0\). Attendu 25.
2. Multiplier d'abord, puis diviser : `partie * 100 / total`. Pour `(1, 3)` : \(100 / 3 = 33{,}33\ldots\) (valeur approchée, car c'est un flottant).

</details>

## Exercice 6 – Suivi de variables

Voici une fonction censée renvoyer la valeur maximale d'un tableau :

```python
def maximum(t):
    m = 0
    for x in t:
        if x > m:
            m = x
    return m
```

1. Que renvoie-t-elle pour `[3, 9, 4]` ? pour `[-5, -2, -9]` ?
2. Quelle est l'erreur ? La corriger.

<details markdown="1">
<summary>Voir la réponse</summary>

1. 9 pour `[3, 9, 4]` ; 0 pour `[-5, -2, -9]`, alors que le maximum est −2.
2. `m` est initialisé à 0 : si tous les éléments sont négatifs, 0 (qui n'est pas dans le tableau) est renvoyé. Il faut `m = t[0]` (le tableau doit être non vide).

</details>

## Exercice 7 – Corriger un programme

Trouver et corriger l'erreur dans chaque extrait :

(a) `for i in range(1, len(t)): s = s + t[i]` pour la somme du tableau `t` ;
(b) `i = 0` puis `while i < 5: print(i)` ;
(c) `if 0.1 + 0.2 == 0.3: ...` pour tester une somme de prix ;
(d) `def ajoute(l): l.append(1); return l` appelée sur une liste qu'on veut garder intacte.

<details markdown="1">
<summary>Voir la réponse</summary>

(a) L'indice 0 est oublié : `range(len(t))` ou `for x in t`. (b) `i` n'est jamais modifié : boucle infinie ; ajouter `i = i + 1`. (c) False : les flottants sont approchés ; comparer à une tolérance, ou compter en centimes (entiers). (d) La liste de l'appelant est modifiée ; travailler sur `l = list(l)` avant `append`.

</details>

## Exercice 8 – Un exercice « programmer » complet

**Énoncé.** *Un script relève chaque minute le nombre de connexions à un serveur. On range les relevés dans une liste `connexions`. Écrire une fonction `pic(connexions)` qui renvoie le plus grand relevé et l'indice de sa première apparition, sous la forme d'un couple `(valeur, indice)`. On suppose la liste non vide.*

1. Faire l'exemple à la main pour `[12, 40, 33, 40, 7]`.
2. Écrire l'algorithme en pseudo-code.
3. Proposer quatre tests.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Le plus grand relevé est 40 ; il apparaît aux indices 1 et 3 ; on garde le premier : résultat `(40, 1)`.
2.

```text
ALGORITHME pic
ENTRÉE : connexions, une liste non vide de nombres
SORTIE : un couple (valeur, indice)
DÉBUT
  m ← connexions[0]
  im ← 0
  POUR i DE 1 À longueur(connexions) - 1 FAIRE
    SI connexions[i] > m ALORS
      m ← connexions[i]
      im ← i
    FIN SI
  FIN POUR
  RENVOYER (m, im)
FIN
```

Le test est `>` (strict) : une valeur égale au maximum déjà trouvé ne remplace pas l'indice, donc on garde la première apparition.

3. `[5]` → `(5, 0)` ; `[12, 40, 33, 40, 7]` → `(40, 1)` ; `[-5, -2, -9]` → `(-2, 1)` (valeurs négatives) ; `[9, 3, 1]` → `(9, 0)` (maximum au début).

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Reformuler un énoncé (entrées, sortie, exemple) ;
- [ ] Écrire un algorithme de comptage, de recherche avec arrêt, de maximum ;
- [ ] Choisir des cas limites pour tester une fonction ;
- [ ] Écrire un tableau de suivi de variables ;
- [ ] Corriger un algorithme erroné.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________
