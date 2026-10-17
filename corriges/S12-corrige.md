# Corrigé S12

## Exercices

Les réponses détaillées figurent dans les encadrés de la feuille d'exercices. Rappel :

- Exercice 1 : 16 ; exercice 2 : `4 10 10`.
- Exercice 5 : totaux par ligne [45, 41, 53], par colonne [37, 35, 32, 35].
- Exercice 8 : 6 comparaisons, 1 échanges.
- Exercice 9 : au plus 10 étapes pour 1 000 éléments, 20 pour un million.

## TP Python – solutions

```python
def moyenne(t):
    s = 0
    for x in t:
        s = s + x
    return s / len(t)

def maximum(t):
    m = t[0]
    for i in range(1, len(t)):
        if t[i] > m:
            m = t[i]
    return m

def indice_du_max(t):
    imax = 0
    for i in range(1, len(t)):
        if t[i] > t[imax]:
            imax = i
    return imax
```

```python
def position(t, x):
    for i in range(len(t)):
        if t[i] == x:
            return i
    return -1

def compte(t, x):
    n = 0
    for y in t:
        if y == x:
            n = n + 1
    return n

def dichotomie(t, x):
    debut = 0
    fin = len(t) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if t[milieu] == x:
            return milieu
        elif t[milieu] < x:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1
```

```python
def tri_selection(t):
    r = list(t)
    n = len(r)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if r[j] < r[m]:
                m = j
        r[i], r[m] = r[m], r[i]
    return r
```

```python
def somme_lignes(g):
    resultat = []
    for ligne in g:
        s = 0
        for x in ligne:
            s = s + x
        resultat.append(s)
    return resultat

def somme_colonnes(g):
    resultat = []
    for j in range(len(g[0])):
        s = 0
        for i in range(len(g)):
            s = s + g[i][j]
        resultat.append(s)
    return resultat

def transposee(g):
    resultat = []
    for j in range(len(g[0])):
        ligne = []
        for i in range(len(g)):
            ligne.append(g[i][j])
        resultat.append(ligne)
    return resultat
```

```python
def inverse(s):
    r = ""
    for c in s:
        r = c + r
    return r

def est_palindrome(s):
    s = s.lower()
    return s == inverse(s)

def acronyme(phrase):
    r = ""
    for mot in phrase.split():
        r = r + mot[0].upper()
    return r
```

```python
def echecs_par_adresse(lignes):
    d = {}
    for ligne in lignes:
        c = ligne.split()
        if c[3] == "LOGIN_FAILED":
            if c[2] in d:
                d[c[2]] = d[c[2]] + 1
            else:
                d[c[2]] = 1
    return d

def adresses_suspectes(lignes, seuil):
    d = echecs_par_adresse(lignes)
    liste = []
    for adresse in d:
        if d[adresse] >= seuil:
            liste.append(adresse)
    return sorted(liste)
```
