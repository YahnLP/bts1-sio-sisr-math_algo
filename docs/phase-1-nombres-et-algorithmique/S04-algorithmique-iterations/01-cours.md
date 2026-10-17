# Cours – Algorithmique : itérations

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S04 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S03 (instructions, conditionnelles).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Choisir** entre une itération déterministe (pour) et indéterministe (tant que, répéter… jusqu'à ce que) ;
- [ ] **Construire** une boucle avec la méthode : initialisation, condition, mise à jour, traitement final ;
- [ ] **Justifier** qu'une boucle se termine et ce qu'elle calcule (idée d'invariant) ;
- [ ] **Écrire** des boucles imbriquées (deux niveaux au plus) ;
- [ ] **Programmer** les algorithmes classiques : somme, comptage, maximum, conversion en base \(b\).

## I. Pourquoi répéter ?

Parcourir les adresses d'un réseau, additionner des valeurs, chercher un maximum, convertir un nombre en binaire : tous ces traitements **répètent** une même suite d'instructions. Une **itération** (ou **boucle**) exécute un bloc plusieurs fois.

Il existe deux familles :

| Famille | Quand on l'utilise | Structures |
|---|---|---|
| **Déterministe** | On connaît à l'avance le nombre de tours | `POUR` |
| **Indéterministe** | Le nombre de tours dépend d'une condition qui évolue | `TANT QUE`, `RÉPÉTER … JUSQU'À` |

## II. La boucle `POUR`

```text
POUR i DE a À b FAIRE
  bloc
FIN POUR
```

La variable `i` prend successivement les valeurs \(a, a+1, \dots, b\) : il y a \(b - a + 1\) tours (aucun si \(b < a\)).

En Python :

```python
for i in range(a, b + 1):
    bloc
```

> [!WARNING]
> **`range(a, b)` s'arrête à \(b - 1\).** Pour aller **jusqu'à** \(b\) inclus, il faut `range(a, b + 1)`. `range(n)` donne \(0, 1, \dots, n-1\), soit \(n\) valeurs ; `range(a, b, pas)` avance de `pas` à chaque tour.

**Exemple : somme des entiers de 1 à \(n\).**

```text
ALGORITHME somme_entiers
  RÔLE      : calculer 1 + 2 + … + n
  ENTRÉE    : n (entier naturel)
  SORTIE    : s (entier)
  VARIABLES : i, s (entiers)
DÉBUT
  s ← 0                     // initialisation de l'accumulateur
  POUR i DE 1 À n FAIRE
    s ← s + i
  FIN POUR
  RETOURNER s
FIN
```

Trace pour \(n = 5\) :

| Tour | `i` | `s` après le tour |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |
| 4 | 4 | 10 |
| 5 | 5 | 15 |

Le résultat est \(15\). Pour \(n = 100\) on obtient \(5050\), ce que la formule \(\dfrac{n(n+1)}{2} = \dfrac{100 \times 101}{2}\) confirme (S15).

## III. Les boucles `TANT QUE` et `RÉPÉTER … JUSQU'À`

```text
TANT QUE condition FAIRE          RÉPÉTER
  bloc                              bloc
FIN TANT QUE                      JUSQU'À condition
```

| | `TANT QUE` | `RÉPÉTER … JUSQU'À` |
|---|---|---|
| La condition est testée | **avant** chaque tour | **après** chaque tour |
| Le bloc s'exécute au moins une fois ? | Non (peut ne jamais s'exécuter) | Oui |
| On continue tant que… | la condition est **vraie** | la condition est **fausse** |
| Python | `while condition:` | `while True:` … `if condition: break` |

```python
n = 40
while n >= 10:      # tant que
    n = n - 10
```

```python
while True:         # répéter … jusqu'à
    saisie = int(input("Un nombre positif : "))
    if saisie > 0:
        break
```

### Le risque : la boucle infinie

Une boucle `TANT QUE` est **sûre** seulement si on sait montrer qu'elle s'arrête. La condition doit donc devenir fausse au bout d'un nombre fini de tours : c'est le rôle de la **mise à jour**.

**Exemple.** Compter le nombre de doublements à partir de 1 pour atteindre ou dépasser 100.

| Avant le test | `i` | `i < 100` ? | Action |
|---|---|---|---|
| test n° 1 | 1 | oui | `i ← i × 2` |
| test n° 2 | 2 | oui | `i ← i × 2` |
| test n° 3 | 4 | oui | `i ← i × 2` |
| test n° 4 | 8 | oui | `i ← i × 2` |
| test n° 5 | 16 | oui | `i ← i × 2` |
| test n° 6 | 32 | oui | `i ← i × 2` |
| test n° 7 | 64 | oui | `i ← i × 2` |
| test n° 8 | 128 | non | sortie de la boucle |

La boucle s'est exécutée 7 fois, `i` vaut 128 à la sortie, et \(2^{7} = 128 \ge 100\).

## IV. Construire une boucle : la méthode

1. **Ce que fait un tour.** Que doit-on calculer, répéter, accumuler ?
2. **Initialisation.** Avant la boucle : valeur de départ de chaque variable (accumulateur à 0 pour une somme, 1 pour un produit).
3. **Condition.** Quand continue-t-on ? (nombre de tours connu → `POUR` ; sinon `TANT QUE`).
4. **Mise à jour.** Chaque tour doit **rapprocher** de la fin.
5. **Terminaison.** Exhiber une quantité entière positive qui **diminue strictement** à chaque tour (le **variant**) : elle ne peut pas diminuer indéfiniment, donc la boucle s'arrête.
6. **Après la boucle.** Mise en forme du résultat (retour, affichage).

### Ce que calcule la boucle : l'invariant

Pour contrôler un algorithme, on énonce une propriété vraie **avant chaque tour** (un **invariant**). Dans la somme des entiers : *avant le tour où `i` vaut \(k\), `s` vaut \(1 + 2 + \dots + (k-1)\)*. Elle est vraie au départ (\(k=1\), somme vide, `s = 0`), et chaque tour la conserve. À la sortie (\(k = n+1\)), `s` vaut \(1 + \dots + n\).

> [!NOTE]
> Cette façon de raisonner (une propriété qui « passe » de tour en tour) est un **raisonnement par récurrence**, que tu retrouveras avec les suites (S15).

**Une boucle dont la terminaison est incertaine.** La suite de Syracuse remplace \(n\) par \(n/2\) si \(n\) est pair, par \(3n+1\) sinon, jusqu'à obtenir 1. Pour \(n = 7\), on obtient 7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1, en 16 étapes. Personne ne sait démontrer qu'on atteint 1 pour tout départ (conjecture de Syracuse) : un `TANT QUE n ≠ 1` n'a donc pas de variant évident. À l'épreuve, on exhibera toujours un variant.

## V. Les algorithmes types

| Besoin | Initialisation | Corps de boucle |
|---|---|---|
| **Somme** | `s ← 0` | `s ← s + valeur` |
| **Produit** (factorielle) | `p ← 1` | `p ← p × valeur` |
| **Comptage** | `c ← 0` | `SI condition ALORS c ← c + 1` |
| **Maximum** | `m ← premier élément` | `SI valeur > m ALORS m ← valeur` |
| **Recherche** | `trouve ← faux` | `SI valeur = cherchée ALORS trouve ← vrai` |

Pour la **factorielle**, \(n! = 1 \times 2 \times \dots \times n\) avec \(0! = 1\) : par exemple \(5! = 120\) et \(10! = 3 628 800\).

### Chiffres d'un nombre

Les divisions successives donnent les chiffres d'un entier : `n % 10` est le dernier chiffre, `n // 10` supprime ce chiffre. Le variant est `n`, qui diminue jusqu'à 0.

```text
ALGORITHME nombre_de_chiffres
  RÔLE      : compter les chiffres de l'écriture décimale de n (n ≥ 1)
  ENTRÉE    : n (entier, n ≥ 1)
  SORTIE    : c (entier)
DÉBUT
  c ← 0
  TANT QUE n > 0 FAIRE
    n ← n div 10
    c ← c + 1
  FIN TANT QUE
  RETOURNER c
FIN
```

Pour \(n = 2024\) : \(2024 \to 202 \to 20 \to 2 \to 0\), soit 4 tours. Pour \(n = 0\), la boucle ne s'exécute pas et renvoie 0 : **cas particulier** à traiter à part si on veut 1.

### Convertir un entier en base \(b\) (lien avec S01)

La méthode des divisions successives est une boucle `TANT QUE` : le variant est `n`.

```text
ALGORITHME vers_base
  ENTRÉES   : n (entier ≥ 0), b (entier, 2 ≤ b ≤ 16)
  SORTIE    : texte (chaîne)
DÉBUT
  SI n = 0 ALORS RETOURNER "0"
  texte ← ""
  TANT QUE n > 0 FAIRE
    texte ← chiffre(n mod b) + texte      // le dernier reste devient le premier chiffre
    n ← n div b
  FIN TANT QUE
  RETOURNER texte
FIN
```

Ici `chiffre(r)` désigne le caractère associé au reste `r` (`0` à `9`, puis `A` à `F` pour 10 à 15). Trace pour \(n = 13\), \(b = 2\) :

| Tour | `n` avant | `reste` | `n` après | `texte` |
|---|---|---|---|---|
| 1 | 13 | 1 | 6 | `1` |
| 2 | 6 | 0 | 3 | `01` |
| 3 | 3 | 1 | 1 | `101` |
| 4 | 1 | 1 | 0 | `1101` |

## VI. Boucles imbriquées

On peut placer une boucle dans une boucle. Le programme limite à **deux niveaux** les boucles dépendantes. Le nombre total de tours est le produit (ou la somme, si la boucle intérieure dépend de l'extérieure).

```text
POUR i DE 1 À 3 FAIRE
  POUR j DE 1 À i FAIRE
    afficher (i, j)
  FIN POUR
FIN POUR
```

Cette double boucle affiche \(1 + 2 + 3 = 6\) couples : \(\sum_{i=1}^{n} i = \dfrac{n(n+1)}{2}\) tours en tout (pour \(n=10\) : 55).

## À retenir

- `POUR` : nombre de tours connu ; `TANT QUE` : condition testée **avant** ; `RÉPÉTER` : testée **après**.
- `range(a, b)` exclut \(b\) : écrire `range(a, b + 1)` pour inclure \(b\).
- Méthode : initialisation, condition, mise à jour, **variant** (terminaison), traitement final.
- Un **invariant** dit ce que la boucle a calculé à chaque tour.
- Somme : `s ← 0` ; produit : `p ← 1` ; maximum : on part du premier élément.
- Au plus **deux niveaux** de boucles imbriquées.
