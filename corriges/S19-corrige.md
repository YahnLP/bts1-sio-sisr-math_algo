# Corrigé et barème du sujet blanc (S19)

> Ne figure pas sur le site publié : à ​remettre après la composition.

## Exercice 1 (6 points)

**1. (1,5 pt)**
a) \(213 = 11010101_2\) (0,5 pt : \(128 + 64 + 16 + 4 + 1\)).
b) `A7` = \(10 \times 16 + 7 = 167\) (0,5 pt).
c) \(11010110_2 = 214\) et \(00101101_2 = 45\) ; somme \(= 259 > 255\) : il y a **dépassement** ; sur 8 bits le résultat tronqué est \(00000011_2\) avec une retenue sortante (0,5 pt).

**2. (1,5 pt)**
a) `255.255.255.192` (0,25 pt).
b) \(130 \,\&\, 192 = 128\) : réseau `172.16.77.128` ; diffusion : \(128 + 63 = 191\) : `172.16.77.191` (0,5 pt).
c) \(2^{6} - 2 = 62\) machines (0,25 pt).
d) \(200 \,\&\, 192 = 192\) : réseau `172.16.77.192` ≠ `172.16.77.128` : **non** (0,5 pt).

**3. (1,5 pt)**
a) \(1260 = 6 \times 198 + 72\) ; \(198 = 2 \times 72 + 54\) ; \(72 = 1 \times 54 + 18\) ; \(54 = 3 \times 18 + 0\). PGCD = **18** (1 pt).
b) \(1260 = 2^2 \times 3^2 \times 5 \times 7\), \(198 = 2 \times 3^2 \times 11\) : facteurs communs \(2 \times 3^2 = 18\) (0,5 pt).

**4. (1,5 pt)**
a) \(7 \times 15 = 105 = 4 \times 26 + 1\) donc \(7 \times 15 \equiv 1 \pmod{26}\) (0,5 pt).
b) \(x \equiv 15 \times 3 = 45 \equiv 19 \pmod{26}\) (0,5 pt). Vérification : \(7 \times 19 = 133 = 5 \times 26 + 3\) ✓ (0,5 pt).

## Exercice 2 (6 points)

**1. (2 pts)**
a) | \(a\) | \(b\) | \(c\) | \(f\) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | (1 pt).
b) Lignes à 1 : 3, 5, 6, 7. Trois rectangles de 2 cases : \(f = a\,b + a\,c + b\,c\) : l'accès est accordé quand **au moins deux** des trois conditions sont ​vraies (majorité) (1 pt).

**2. (1 pt)** \(\lvert A \cup B \rvert = 70 + 45 - 25 = 90\) ; \(100 - 90 = 10\) salariés n'utilisent aucun des deux services.

**3. (3 pts)**
a) \(\begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 11 \\ 19 \end{pmatrix}\) (1 pt).
b) \(A P = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\) et \(P A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\) (1 pt).
c) \(X = P B = \begin{pmatrix} 3 \\ 2 \end{pmatrix}\) : \(x = 3\) euros, \(y = 2\) euros ; contrôle \(3 \times 3 + 2 = 11\), \(5 \times 3 + 2 \times 2 = 19\) (1 pt).

## Exercice 3 (8 points)

**1. (3 pts)**
a) Suivi pour `[21, 26, 27, 24, 28]`, seuil 25 (1,5 pt) :

| `r` | `courante` | `meilleure` |
|---|---|---|
| 21 | 0 | 0 |
| 26 | 1 | 1 |
| 27 | 2 | 2 |
| 24 | 0 | 2 |
| 28 | 1 | 2 |

Valeur renvoyée : **2**.
b) Le plus grand nombre de relevés consécutifs strictement supérieurs au seuil ; pour une liste vide, la boucle ne s'exécute pas et la ​fonction renvoie 0 (0,5 pt).
c) Pour `[30, 31, 32]`, la série est en cours à la fin de la liste : la mise à jour n'a jamais lieu (elle n'est faite que lorsqu'un relevé n'est pas en alerte). La fonction renvoie 0 au lieu de 3 (1 pt).

**2. (2 pts)** Voir la solution Python ci-dessous (1 pt pour le parcours avec renvoi de l'indice dès qu'un relevé dépasse le seuil, 1 pt pour `-1` **après** la boucle).

**3. (2 pts)** Voir la solution Python (1 pt pour l'extraction des ​champs avec `split`, 1 pt pour le dictionnaire).

**4. (1 pt)**
a) Somme \(350\) ; \(350 \bmod 256 = 94\) ; \(c = 256 - 94 = 162\) (0,5 pt).
b) \(201 + 99 + 50 + 162 = 512 \equiv 0 \pmod{256}\) : le contrôle réussit, l'erreur **n'est pas détectée** : deux erreurs qui se compensent laissent la somme inchangée (0,5 pt).

## Solutions Python

```python
def premiere_alerte(releves, seuil):
    for i in range(len(releves)):
        if releves[i] > seuil:
            return i
    return -1
```

```python
def compte_erreurs(lignes):
    d = {}
    for ligne in lignes:
        c = ligne.split()
        if c[3] == "ERROR":
            if c[2] in d:
                d[c[2]] = d[c[2]] + 1
            else:
                d[c[2]] = 1
    return d

def adresse_la_plus_active(lignes):
    d = compte_erreurs(lignes)
    meilleure = None
    for adresse in sorted(d):
        if meilleure is None or d[adresse] > d[meilleure]:
            meilleure = adresse
    return meilleure
```

```python
def premiere_serie(releves, seuil, k):
    courante = 0
    for i in range(len(releves)):
        if releves[i] > seuil:
            courante = courante + 1
        else:
            courante = 0
        if courante == k:
            return i - k + 1
    return -1
```

```python
def bilan_releves(releves, seuil):
    mini = releves[0]
    maxi = releves[0]
    n = 0
    for r in releves:
        if r < mini:
            mini = r
        if r > maxi:
            maxi = r
        if r > seuil:
            n = n + 1
    pourcentage = n * 100 / len(releves)
    return (mini, maxi, n, pourcentage)
```

## Barème récapitulatif

| Exercice | Points |
|---|---|
| 1 | 6 |
| 2 | 6 |
| 3 | 8 |
| **Total** | **20** |

À répartir selon la qualité de la **rédaction** (méthode, ​justification, unité) à l'intérieur de chaque question.
