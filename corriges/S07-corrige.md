# Corrigé S07

## Exercices

1. Vraies : 38 ≡ 3 [7], −5 ≡ 9 [7], 100 ≡ 1 [9], 52 ≡ 4 [12] ; fausse : 17 ≡ 5 [8] (17 ≡ 1).
2. 6 ; 1 et 3 ; 2 et 2.
3. 6 ; pas d'inverse car PGCD(6, 9) = 3.
4. Cases 0, 6, 12, 3, 9 ; oui ; 1, 2, 4, 7, 8, 11, 13, 14.
5. WJXJFZ ; HELLO WORLD ; XV ; PGCD(13, 26) = 13.
6. 49 ; ​valide ; multiple de 97.
7. Voir le tableau.

## TP Python – solutions

```python
def puissance_mod(a, k, n):
    """Renvoie a**k modulo n en réduisant à chaque multiplication."""
    resultat = 1
    for _ in range(k):
        resultat = (resultat * a) % n
    return resultat % n
```

```python
def inverse_mod(a, n):
    """Inverse de a modulo n (entre 1 et n-1), ou None s'il n'existe pas."""
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return None
```

```python
def inverse_mod(a, n):
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return None

def chiffrer(texte, a, b):
    """Chiffre un texte en majuscules avec y = a*x + b (mod 26)."""
    resultat = ""
    for lettre in texte:
        if "A" <= lettre <= "Z":
            x = ord(lettre) - 65
            y = (a * x + b) % 26
            resultat = resultat + chr(y + 65)
        else:
            resultat = resultat + lettre
    return resultat

def dechiffrer(texte, a, b):
    """Déchiffre : x = a' * (y - b) (mod 26), où a' est l'inverse de a."""
    a_inv = inverse_mod(a, 26)
    resultat = ""
    for lettre in texte:
        if "A" <= lettre <= "Z":
            y = ord(lettre) - 65
            x = (a_inv * (y - b)) % 26
            resultat = resultat + chr(x + 65)
        else:
            resultat = resultat + lettre
    return resultat
```

```python
def cle_nir(numero):
    """Clé de contrôle : 97 - (numero modulo 97)."""
    return 97 - numero % 97
```

```python
def isbn13_valide(code):
    """True si la somme pondérée (1, 3, 1, 3, ...) des 13 chiffres est un multiple de 10."""
    somme = 0
    for i in range(len(code)):
        chiffre = int(code[i])
        if i % 2 == 0:
            somme = somme + chiffre
        else:
            somme = somme + 3 * chiffre
    return len(code) == 13 and somme % 10 == 0
```

```python
def cases_visitees(n, k):
    """Ensemble des cases visitées en partant de 0 par sauts de k (modulo n), jusqu'à revenir en 0."""
    cases = {0}
    position = k % n
    while position != 0:
        cases.add(position)
        position = (position + k) % n
    return cases
```
