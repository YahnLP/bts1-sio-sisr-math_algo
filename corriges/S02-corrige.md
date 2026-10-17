# Corrigé S02

## Exercices

1. 6,625 ; 11,1875 ; 0,3125.
2. 101,11 ; 0,0101 ; 1101,011 ; 0,(0011) périodique.
3. Finies : 0,5 ; 0,75 ; 0,375 ; 0,0625. Non finies : 0,1 ; 0,2.
4. 000110 ; erreur 0,00625 < 0,015625.
5. 10010 ; 1001 ; 1000001.
6. 11001000 ; quotient 13, reste 5.
7. 270 → 14 = 00001110.
8. 11101110 ; -16.
9. 1,82 Tio ; 734,0 Mo ; 400 s (6 min 40 s) ; 6 220 800 o, 5,93 Mio.

## TP Python – solutions

```python
def chiffres_apres_virgule(x, p):
    """p premiers chiffres binaires de la partie fractionnaire de x (0 <= x < 1)."""
    texte = ""
    for _ in range(p):
        x = x * 2
        chiffre = int(x)
        texte = texte + str(chiffre)
        x = x - chiffre
    return texte
```

```python
def addition_binaire(a, b):
    """Somme de deux nombres binaires donnés sous forme de textes."""
    n = max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)
    resultat = ""
    retenue = 0
    for i in range(n - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + retenue
        resultat = str(total % 2) + resultat
        retenue = total // 2
    if retenue == 1:
        resultat = "1" + resultat
    return resultat
```

```python
def addition_n_bits(a, b, n):
    """Renvoie (résultat sur n bits, débordement) pour a + b."""
    somme = a + b
    return (somme % 2 ** n, somme > 2 ** n - 1)
```

```python
def duree_transfert(taille_octets, debit_bits_par_s):
    """Durée théorique (en secondes) d'un transfert."""
    return taille_octets * 8 / debit_bits_par_s
```

`flottants.py` : affiche `0.30000000000000004`, puis `False`, `True` (0,5 et 0,25 sont des puissances de 2 inverses : exacts), `True` (`isclose`), `True` (`Fraction`).
