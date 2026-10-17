# Cours – Récursivité, complexité et débogage

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S18 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S04, S12 (boucles, fonctions, tableaux) ; S15 (suites).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Écrire** un algorithme récursif avec test d'arrêt et cas de base ;
- [ ] **Dérouler** les appels récursifs et **vérifier** la terminaison ;
- [ ] **Passer** d'une version récursive à une version itérative (récursivité terminale) ;
- [ ] **Compter** le nombre d'opérations significatives dans le pire cas (recherche séquentielle, dichotomique, tri par sélection) ;
- [ ] **Repérer** et **corriger** des erreurs classiques (indices hors domaine, effets de bord, approximations) par suivi de variables.

## I. La récursivité

Un algorithme est **récursif** quand il **s'appelle lui-même** sur un problème plus petit. Deux ingrédients obligatoires :

1. un **cas de base** (test d'arrêt) qui se résout sans nouvel appel ;
2. un **appel récursif** dont l'argument **se rapproche du cas de base**.

```text
FONCTION fact(n)
  RÔLE   : calculer n! = 1 × 2 × … × n   (0! = 1)
  ENTRÉE : n (entier ≥ 0)
  SORTIE : n! (entier)
DÉBUT
  SI n = 0 ALORS
    RETOURNER 1                  // cas de base
  SINON
    RETOURNER n × fact(n - 1)    // appel récursif
  FIN SI
FIN
```

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
```

**Déroulé pour `fact(4)`** (les appels s'empilent jusqu'au cas de base, puis les résultats remontent) :

| Appel | Test d'arrêt | Calcul en remontant |
|---|---|---|
| `fact(4)` | non | `4 * fact(3)` = 4 × 6 = **24** |
| `fact(3)` | non | `3 * fact(2)` = 3 × 2 = **6** |
| `fact(2)` | non | `2 * fact(1)` = 2 × 1 = **2** |
| `fact(1)` | non | `1 * fact(0)` = 1 × 1 = **1** |
| `fact(0)` | **oui** : renvoie 1 |  |

`fact(4)` vaut 24 ; `fact(5)` vaut 120 ; `fact(10)` vaut 3628800.

### Terminaison

Pour prouver qu'un algorithme récursif **s'arrête** : l'argument est un entier naturel qui **diminue strictement** à chaque appel (ici \(n \to n - 1\)) ; il ne peut pas diminuer indéfiniment, il atteint donc le cas de base. C'est le même raisonnement que le **variant** d'une boucle (S04).

> [!WARNING]
> **Sans cas de base, ou avec un argument qui ne se rapproche pas du cas de base, la récursion ne s'arrête jamais.** Python interrompt alors le programme avec `RecursionError` (par défaut, au bout d'environ 1 000 appels imbriqués).

### Autres exemples

**PGCD par l'algorithme d'Euclide (S05).** \(\gcd(a, b) = a\) si \(b = 0\), sinon \(\gcd(b,\ a \bmod b)\). Le second argument (le reste) diminue strictement : l'algorithme s'arrête.

```python
def pgcd(a, b):
    if b == 0:
        return a
    return pgcd(b, a % b)
```

| Appel | \(a\) | \(b\) | Suite |
|---|---|---|---|
| `pgcd(252, 105)` | 252 | 105 | `pgcd(105, 42)` (reste 252 mod 105 = 42) |
| `pgcd(105, 42)` | 105 | 42 | `pgcd(42, 21)` (reste 105 mod 42 = 21) |
| `pgcd(42, 21)` | 42 | 21 | `pgcd(21, 0)` (reste 42 mod 21 = 0) |
| `pgcd(21, 0)` | 21 | 0 | \(b = 0\) : renvoie 21 |

\(\gcd(252, 105) = 21\) (contrôle : \(252 = 2^2 \times 3^2 \times 7\), \(105 = 3 \times 5 \times 7\), donc \(3 \times 7 = 21\)).

**Conversion en binaire (S01).** \(n\) s'écrit : l'écriture de \(n \,\mathrm{div}\, 2\), suivie du bit \(n \bmod 2\).

```python
def binaire(n):
    if n < 2:
        return str(n)
    return binaire(n // 2) + str(n % 2)
```

`binaire(13)` donne `1101`.

## II. Récursif ou itératif ?

Tout algorithme récursif peut s'écrire avec une **boucle**, et inversement. La version itérative est souvent plus économe (pas d'empilement d'appels) ; la version récursive est souvent plus proche de la définition mathématique.

Une récursivité est **terminale** quand l'appel récursif est la **dernière** opération (comme dans `pgcd`) : on la transforme directement en boucle.

```python
def pgcd(a, b):          # version itérative
    while b != 0:
        a, b = b, a % b
    return a
```

**Un cas où la version récursive est très coûteuse : Fibonacci.** \(F_0 = 0\), \(F_1 = 1\), \(F_n = F_{n-1} + F_{n-2}\).

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Le nombre d'appels explose, car les mêmes valeurs sont recalculées :

| \(n\) | \(F_n\) | Nombre d'appels de `fib(n)` |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 1 | 3 |
| 5 | 5 | 15 |
| 10 | 55 | 177 |
| 20 | 6765 | 21891 |

On a exactement : nombre d'appels \(= 2F_{n+1} - 1\) (vérifié pour \(n\) de 0 à 24 ; par exemple pour \(n = 10\) : \(2 \times 89 - 1 = 177\)). La version à boucle (deux variables mises à jour) ne fait que \(n\) additions.

## III. Complexité : compter les opérations significatives

On mesure le **coût** d'un algorithme par le nombre d'**opérations significatives** (comparaisons, additions…) dans le **pire cas**, en fonction de la taille \(n\) des données.

| Algorithme | Opération comptée | Pire cas |
|---|---|---|
| Recherche séquentielle | comparaisons | \(n\) |
| Recherche dichotomique (tableau trié) | comparaisons | \(\lfloor \log_2 n \rfloor + 1\) |
| Tri par sélection | comparaisons | \(\dfrac{n(n-1)}{2}\) |
| Calcul de \(F_n\) par boucle | additions | \(n\) |

(Ces formules ont été vérifiées par comptage direct : S12.)

| \(n\) | Séquentielle (pire cas) | Dichotomie (pire cas) | Tri par sélection |
|---|---|---|---|
| 10 | 10 | 4 | 45 |
| 100 | 100 | 7 | 4 950 |
| 1 000 | 1 000 | 10 | 499 500 |
| 1 000 000 | 1 000 000 | 20 | 499 999 500 000 |

À titre d'illustration, si une opération durait une microseconde, le tri par sélection d'un million d'éléments demanderait environ 5.8 jours, la dichotomie dans un tableau d'un million d'éléments : 20 microsecondes. Ce n'est pas une mesure, mais un ordre de grandeur : **la façon dont le coût croît avec \(n\)** compte plus que la vitesse de la machine.

## IV. Repérer et corriger des erreurs

On distingue les erreurs de **syntaxe** (le programme ne démarre pas), d'**exécution** (il plante : message d'erreur) et de **logique** (il tourne mais donne un mauvais résultat). Les plus difficiles sont les dernières : on les trouve par le **suivi de variables**.

**Méthode.** (1) Reproduire l'erreur avec un petit exemple ; (2) écrire sur papier la valeur des variables à chaque tour ; (3) repérer le premier tour où une valeur n'est pas celle attendue ; (4) corriger ; (5) retester, y compris les cas limites (tableau vide, un seul élément, valeurs négatives).

| Erreur classique | Exemple | Résultat observé | Correction |
|---|---|---|---|
| **Indice hors domaine** | `for i in range(len(t) + 1): s += t[i]` | IndexError | `range(len(t))` |
| **Mauvaise initialisation** | maximum avec `m = 0` sur `[-5, -2, -9]` | renvoie 0, valeur absente de la liste | `m = t[0]` |
| **Variant non modifié** | `while i < 10:` sans `i = i + 1` | boucle infinie | mettre à jour `i` |
| **Égalité de flottants** | `0.1 + 0.2 == 0.3` | False (la somme vaut `0.30000000000000004`) | comparer avec une tolérance, ou travailler en entiers / `Fraction` |
| **Division entière** | `7 // 2` au lieu de `7 / 2` | 3 au lieu de 3,5 | choisir l'opérateur voulu |
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

Le compteur `n` s'incrémente **même quand \(x\) est négatif** : on obtient \(10 / 3\) au lieu de \(10 / 2 = 5\). Correction : placer `n = n + 1` **dans** le `if`.

## À retenir

- Récursivité : **cas de base** + appel sur un problème plus petit ; la terminaison s'appuie sur un entier qui diminue strictement.
- Tout récursif peut s'écrire en itératif ; Fibonacci récursif recalcule les mêmes valeurs (nombre d'appels \(2F_{n+1} - 1\)).
- Complexité : compter les opérations significatives dans le pire cas ; séquentielle \(n\), dichotomie \(\lfloor \log_2 n \rfloor + 1\), tri par sélection \(\frac{n(n-1)}{2}\).
- Déboguer : reproduire, tracer les variables, trouver le premier écart, corriger, retester les cas limites.
