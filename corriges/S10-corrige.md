# Corrigé S10

## Exercices

1. Voir les réponses repliables (chacune est vérifiée par table de ​vérité).
2. Idem.
3. \(f = \overline{b} + a\,c\).
4. \(g = b + \overline{a}\,\overline{c}\).
5. Majorité : \(a\,b + a\,c + b\,c\).
6. Voir cours (VI) ; \(\text{NAND}(a, \text{NAND}(a,b)) = \overline{a} + b\).
7. \(0110_2 + 0111_2 = 01101_2\) (13).
8. Voir la réponse repliable.

## TP Python – solutions

```python
def mintermes(f, n):
    """Numéros des lignes (0 à 2**n - 1) pour lesquelles f vaut 1."""
    resultat = []
    for k in range(2 ** n):
        valeurs = []
        for i in range(n):
            valeurs.append((k >> (n - 1 - i)) & 1)
        if f(*valeurs):
            resultat.append(k)
    return resultat
```

```python
def meme_fonction(f, g, n):
    """Vrai si f et g donnent le même résultat sur les 2**n combinaisons."""
    for k in range(2 ** n):
        valeurs = []
        for i in range(n):
            valeurs.append((k >> (n - 1 - i)) & 1)
        if bool(f(*valeurs)) != bool(g(*valeurs)):
            return False
    return True
```

```python
def nand(a, b):
    return 1 - (a & b)

def non_nand(a):
    return nand(a, a)

def et_nand(a, b):
    return nand(nand(a, b), nand(a, b))

def ou_nand(a, b):
    return nand(nand(a, a), nand(b, b))

def xor_nand(a, b):
    n = nand(a, b)
    return nand(nand(a, n), nand(b, n))
```

```python
def additionneur_complet(a, b, c):
    """Renvoie (somme, retenue) pour trois bits."""
    somme = a ^ b ^ c
    retenue = (a & b) | (c & (a ^ b))
    return (somme, retenue)

def additionne(x, y):
    """Additionne deux chaînes de bits de même longueur ; résultat sur une position de plus."""
    n = len(x)
    resultat = ""
    retenue = 0
    for i in range(n - 1, -1, -1):
        s, retenue = additionneur_complet(int(x[i]), int(y[i]), retenue)
        resultat = str(s) + resultat
    return str(retenue) + resultat
```

```python
def prefixe_vers_masque(n):
    """Masque décimal pointé d'un préfixe n (0 à 32)."""
    octets = []
    for i in range(4):
        bits = min(8, max(0, n - 8 * i))
        octets.append(str(256 - 2 ** (8 - bits)))
    return ".".join(octets)

def adresse_reseau(ip, masque):
    """ET bit à bit, octet par octet."""
    a = ip.split(".")
    m = masque.split(".")
    return ".".join(str(int(a[i]) & int(m[i])) for i in range(4))

def diffusion(ip, masque):
    """Adresse réseau dont tous les bits de machine sont à 1."""
    a = ip.split(".")
    m = masque.split(".")
    return ".".join(str((int(a[i]) & int(m[i])) | (255 - int(m[i]))) for i in range(4))

def nb_machines(n):
    """Nombre d'adresses utilisables pour le préfixe n."""
    return 2 ** (32 - n) - 2
```
