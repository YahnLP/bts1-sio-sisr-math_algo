# Corrigé S18

## Exercices

Réponses détaillées dans les encadrés de la feuille d'exercices. Résultats clés :

- `fact(5)` = 120 ; \(\gcd(252, 105) = 21\) ; \(\gcd(1071, 462) = 21\).
- Appels de `fib` : 15 pour \(n = 5\), 177 pour \(n = 10\).
- Comparaisons au pire cas, \(n = 100\) : 100 (séquentielle), 7 (dichotomie) ; tri par sélection de 1000 éléments : 499500.

## TP Python – solutions

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

```python
def binaire_rec(n):
    if n < 2:
        return str(n)
    return binaire_rec(n // 2) + str(n % 2)

def binaire_iter(n):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s
```

```python
def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

def fib_iter(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

def appels_fib(n):
    if n < 2:
        return 1
    return 1 + appels_fib(n - 1) + appels_fib(n - 2)
```

```python
def recherche_sequentielle(t, x):
    comparaisons = 0
    for i in range(len(t)):
        comparaisons = comparaisons + 1
        if t[i] == x:
            return (i, comparaisons)
    return (-1, comparaisons)

def dichotomie(t, x):
    debut = 0
    fin = len(t) - 1
    comparaisons = 0
    while debut <= fin:
        milieu = (debut + fin) // 2
        comparaisons = comparaisons + 1
        if t[milieu] == x:
            return (milieu, comparaisons)
        elif t[milieu] < x:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return (-1, comparaisons)
```

```python
def maximum(t):
    m = t[0]
    for x in t:
        if x > m:
            m = x
    return m

def somme_positifs_moyenne(t):
    s = 0
    n = 0
    for x in t:
        if x > 0:
            s = s + x
            n = n + 1
    if n == 0:
        return 0
    return s / n

def trie_sans_modifier(t):
    r = list(t)
    r.sort()
    return r
```

Erreurs de `debug.py` : (1) `maximum` : `m` initialisé à 0 au lieu de `t[0]` ; (2) `somme_positifs_moyenne` : le compteur `n` s'incrémente aussi pour les valeurs négatives ou nulles ; (3) `trie_sans_modifier` : `r = t` ne copie pas la liste, `r.sort()` modifie donc `t`.
