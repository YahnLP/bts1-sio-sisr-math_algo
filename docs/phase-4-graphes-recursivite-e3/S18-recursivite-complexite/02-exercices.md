# Exercices – Algorithmes récursifs, coût et erreurs

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S18*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Dérouler un appel récursif

Écrire la pile d'appels de `fact(5)` (appels, cas de base, résultats qui remontent).

<details markdown="1">
<summary>Voir la réponse</summary>

| Appel | Test d'arrêt | Calcul en remontant |
|---|---|---|
| `fact(5)` | non | `5 * fact(4)` = 5 × 24 = **120** |
| `fact(4)` | non | `4 * fact(3)` = 4 × 6 = **24** |
| `fact(3)` | non | `3 * fact(2)` = 3 × 2 = **6** |
| `fact(2)` | non | `2 * fact(1)` = 2 × 1 = **2** |
| `fact(1)` | non | `1 * fact(0)` = 1 × 1 = **1** |
| `fact(0)` | **oui** : renvoie 1 |  |

Résultat : 120.

</details>

## Exercice 2 – Écrire des fonctions récursives

Écrire en Python, avec cas de base et appel récursif :

1. `somme(n)` : \(1 + 2 + \dots + n\) (avec `somme(0) = 0`) ;
2. `puissance(x, n)` : \(x^n\) pour \(n \ge 0\) ;
3. `pgcd(a, b)`.

Vérifier : `somme(10)` = 55 ; `puissance(2, 10)` = 1024.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def somme(n):
    if n == 0:
        return 0
    return n + somme(n - 1)

def puissance(x, n):
    if n == 0:
        return 1
    return x * puissance(x, n - 1)

def pgcd(a, b):
    if b == 0:
        return a
    return pgcd(b, a % b)
```

Pour la terminaison : \(n\) (ou \(b\)) est un entier naturel qui décroît strictement à chaque appel. Contrôles : `somme(10)` = 55 ; `puissance(2, 10)` = 1024 ; `pgcd(252, 105)` = 21.

</details>

## Exercice 3 – Dérouler Euclide

Dérouler `pgcd(1071, 462)`.

<details markdown="1">
<summary>Voir la réponse</summary>

| Appel | \(a\) | \(b\) | Suite |
|---|---|---|---|
| `pgcd(1071, 462)` | 1071 | 462 | `pgcd(462, 147)` (reste 1071 mod 462 = 147) |
| `pgcd(462, 147)` | 462 | 147 | `pgcd(147, 21)` (reste 462 mod 147 = 21) |
| `pgcd(147, 21)` | 147 | 21 | `pgcd(21, 0)` (reste 147 mod 21 = 0) |
| `pgcd(21, 0)` | 21 | 0 | \(b = 0\) : renvoie 21 |

\(\gcd(1071, 462) = 21\) (\(1071 = 3^2 \times 7 \times 17\), \(462 = 2 \times 3 \times 7 \times 11\) : \(3 \times 7 = 21\)).

</details>

## Exercice 4 – Terminaison

Pour chaque fonction, dire si elle s'arrête et pourquoi :

```python
def f(n):
    return n * f(n - 1)

def g(n):
    if n == 0:
        return 1
    return g(n + 1)

def h(n):
    if n <= 1:
        return 1
    return h(n - 2) + 1
```

<details markdown="1">
<summary>Voir la réponse</summary>

- `f` : **ne s'arrête pas** (aucun cas de base) : `RecursionError`.
- `g` : **ne s'arrête pas** pour \(n > 0\) : l'argument augmente, il s'éloigne du cas de base.
- `h` : s'arrête pour tout entier : \(n\) diminue de 2 et le test `n <= 1` couvre aussi les valeurs négatives ou nulles. (Avec le test `n == 0` seul, un \(n\) impair ne s'arrêterait pas : on passerait de 1 à −1 en sautant 0.) Par exemple `h(5)` = 3 (appels : h(5) → h(3) → h(1)).

</details>

## Exercice 5 – Fibonacci

1. Combien d'appels fait `fib(5)` ? `fib(10)` ?
2. Écrire une version itérative de Fibonacci. Combien d'additions pour `n = 10` ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. 15 appels pour `fib(5)` et 177 pour `fib(10)` (formule \(2F_{n+1} - 1\) : \(2 \times 8 - 1 = 15\), \(2 \times 89 - 1 = 177\)).
2. ```python
   def fib_iter(n):
       a, b = 0, 1
       for _ in range(n):
           a, b = b, a + b
       return a
   ```
   10 additions pour `n = 10` ; résultat 55.

</details>

## Exercice 6 – Récursif et itératif

1. Écrire `binaire(n)` récursive (S01) et vérifier pour \(n = 13\) et \(n = 100\).
2. Écrire une version itérative.

<details markdown="1">
<summary>Voir la réponse</summary>

1. ```python
   def binaire(n):
       if n < 2:
           return str(n)
       return binaire(n // 2) + str(n % 2)
   ```
   `binaire(13)` = `1101` ; `binaire(100)` = `1100100`.
2. ```python
   def binaire_iter(n):
       s = ""
       while n > 0:
           s = str(n % 2) + s
           n = n // 2
       return s if s != "" else "0"
   ```

</details>

## Exercice 7 – Compter

1. Nombre maximal de comparaisons pour chercher une valeur dans un tableau de 100 éléments : (a) séquentiellement ; (b) par dichotomie (tableau trié).
2. Même question pour 1 000 000 d'éléments.
3. Nombre de comparaisons du tri par sélection pour \(n = 50\) et \(n = 1000\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. (a) 100 ; (b) \(\lfloor \log_2 100 \rfloor + 1 = 7\).
2. (a) 1000000 ; (b) 20.
3. \(\dfrac{50 \times 49}{2} = 1225\) ; \(\dfrac{1000 \times 999}{2} = 499500\).

</details>

## Exercice 8 – Suivi de variables

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
2. `m` est initialisé à 0 : si tous les éléments sont négatifs, 0 (qui n'est pas dans le tableau) est renvoyé. Il faut `m = t[0]` (et parcourir à partir de l'indice 1).

</details>

## Exercice 9 – Corriger un programme

Trouver et corriger l'erreur dans chaque extrait :

(a) `for i in range(1, len(t)): s = s + t[i]` pour la somme du tableau `t` ;
(b) `i = 0` puis `while i < 5: print(i)` ;
(c) `if 0.1 + 0.2 == 0.3: ...` pour tester une somme de prix ;
(d) `def ajoute(l): l.append(1); return l` appelée sur une liste qu'on veut garder intacte.

<details markdown="1">
<summary>Voir la réponse</summary>

(a) L'indice 0 est oublié : `range(len(t))` ou `for x in t`. (b) `i` n'est jamais modifié : boucle infinie ; ajouter `i = i + 1`. (c) False : les flottants sont approchés ; comparer à une tolérance, ou compter en centimes (entiers). (d) La liste de l'appelant est modifiée ; travailler sur `l = list(l)` avant `append`.

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Écrire une fonction récursive avec test d'arrêt ;
- [ ] Dérouler les appels d'une fonction récursive ;
- [ ] Transformer une récursion terminale en boucle ;
- [ ] Compter les comparaisons d'un algorithme de recherche ou de tri ;
- [ ] Corriger un algorithme erroné par suivi de variables.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________
