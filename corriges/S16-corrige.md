# Corrigé S16

## Exercices

Réponses détaillées dans les encadrés de la feuille d'exercices. Résultats clés :

- \(M^3\) du graphe des services : \((M^3)_{af} = 3\) ; ​niveaux : [[0], [1, 2], [3, 4], [5]] (indices 0 à 5 = \(a\) à \(f\)).
- Fermeture transitive du graphe de l'exercice 6 : \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \end{pmatrix}.
- Ordre de démarrage des services : Réseau ; DNS, Base ; Web, Proxy ; Supervision.

## TP Python – solutions

```python
def matrice_adjacence(n, arcs):
    m = []
    for i in range(n):
        m.append([0] * n)
    for (a, b) in arcs:
        m[a][b] = 1
    return m

def successeurs(m, i):
    liste = []
    for j in range(len(m)):
        if m[i][j] == 1:
            liste.append(j)
    return liste

def demi_degres(m):
    n = len(m)
    ext = []
    inte = []
    for i in range(n):
        ext.append(sum(m[i]))
    for j in range(n):
        s = 0
        for i in range(n):
            s = s + m[i][j]
        inte.append(s)
    return (ext, inte)
```

```python
def produit(a, b):
    n = len(a)
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            s = 0
            for k in range(n):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def nb_chemins(m, p, i, j):
    n = len(m)
    r = []
    for a in range(n):
        r.append([1 if a == b else 0 for b in range(n)])
    for _ in range(p):
        r = produit(r, m)
    return r[i][j]
```

```python
def produit(a, b):
    n = len(a)
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            s = 0
            for k in range(n):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def a_un_circuit(m):
    """Un chemin de longueur n passe par n + 1 sommets : l'un d'eux se répète, donc il y a un circuit."""
    n = len(m)
    p = m
    for _ in range(n - 1):
        p = produit(p, m)
    for ligne in p:
        for x in ligne:
            if x != 0:
                return True
    return False
```

```python
def produit_bool(a, b):
    n = len(a)
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            v = 0
            for k in range(n):
                if a[i][k] == 1 and b[k][j] == 1:
                    v = 1
            ligne.append(v)
        resultat.append(ligne)
    return resultat

def fermeture(m):
    n = len(m)
    t = [ligne[:] for ligne in m]
    p = [ligne[:] for ligne in m]
    for _ in range(n - 1):
        p = produit_bool(p, m)
        for i in range(n):
            for j in range(n):
                if p[i][j] == 1:
                    t[i][j] = 1
    return t
```

```python
def niveaux(m):
    """Niveaux d'un graphe sans circuit, ou None s'il y a un circuit."""
    n = len(m)
    restants = list(range(n))
    resultat = []
    while len(restants) > 0:
        niveau = []
        for j in restants:
            sans_pred = True
            for i in restants:
                if m[i][j] == 1:
                    sans_pred = False
            if sans_pred:
                niveau.append(j)
        if len(niveau) == 0:
            return None
        resultat.append(niveau)
        restants = [x for x in restants if x not in niveau]
    return resultat
```
