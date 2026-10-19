# Corrigé S15

## Exercices

Réponses détaillées dans les encadrés de la feuille d'exercices. Résultats clés :

- Octets : `"192"` et `"0"` valides ; `"256"`, `"07"`, `""`, `"12a"` invalides.
- IPv4 : `10.0.0.1` valide ; `10.0.0` (3 morceaux), `172.16.256.1` (256), `192.168.1.1.` (5 morceaux), `1.2.3.04` (zéro initial) invalides.
- Octets de masque : 0, 128, 192, 224, 240, 248, 252, 254, 255.
- Bits de parité : `1011001` → 0 ; `1110000` → 1 ; `0000000` → 0 ; `1111111` → 1. Deux erreurs (rangs 3 et 8 de `10110010`) ne sont pas détectées.
- Parité à deux dimensions : ligne 1 et colonne 2 fausses, on corrige `g[1][2]` (0 devient 1).
- Somme de contrôle de \(200, 100, 50\) : \(c = 162\) ; \([200, 100, 51]\) est détecté, \([201, 99, 50]\) ne l'est pas.
- \(\texttt{0xC0} \oplus \texttt{0xA8} \oplus \texttt{0x0A} \oplus \texttt{0x4D} = \texttt{0x2F}\) (47).

## TP Python – solutions

```python
def est_octet(s):
    if s == "" or not s.isdigit():
        return False
    if len(s) > 1 and s[0] == "0":
        return False
    return 0 <= int(s) <= 255

def ipv4_valide(s):
    morceaux = s.split(".")
    if len(morceaux) != 4:
        return False
    for m in morceaux:
        if not est_octet(m):
            return False
    return True

def mac_valide(s):
    hexa = "0123456789abcdefABCDEF"
    groupes = s.split(":")
    if len(groupes) != 6:
        return False
    for g in groupes:
        if len(g) != 2:
            return False
        for c in g:
            if c not in hexa:
                return False
    return True
```

```python
def bit_parite(bits):
    n = 0
    for b in bits:
        if b == 1:
            n = n + 1
    return n % 2

def ajoute_parite(bits):
    r = list(bits)
    r.append(bit_parite(bits))
    return r

def mot_valide(mot):
    return bit_parite(mot) == 0
```

```python
def lignes_incorrectes(g):
    res = []
    for i in range(len(g)):
        if sum(g[i]) % 2 == 1:
            res.append(i)
    return res

def colonnes_incorrectes(g):
    res = []
    for j in range(len(g[0])):
        total = 0
        for i in range(len(g)):
            total = total + g[i][j]
        if total % 2 == 1:
            res.append(j)
    return res

def corrige(g):
    copie = [ligne[:] for ligne in g]
    lignes = lignes_incorrectes(g)
    colonnes = colonnes_incorrectes(g)
    if len(lignes) == 1 and len(colonnes) == 1:
        i = lignes[0]
        j = colonnes[0]
        copie[i][j] = 1 - copie[i][j]
    return copie
```

```python
def somme_controle(octets):
    return (-sum(octets)) % 256

def trame_valide(octets, c):
    return (sum(octets) + c) % 256 == 0

def xor_controle(octets):
    r = 0
    for o in octets:
        r = r ^ o
    return r
```

