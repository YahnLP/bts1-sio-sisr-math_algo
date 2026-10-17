# Corrigé S01

## Cours (valeurs de contrôle)

- 205 en binaire : 11001101 ; en hexadécimal : CD.

## Exercices

1. 45 ; 1 000 ; 255 ; 8.
2. 37 = 100101 ; 100 = 1100100 ; 255 = 11111111 ; 1 000 = 1111101000.
3. 255 = FF ; 1 000 = 3E8 ; 4 096 = 1000 ; 65 535 = FFFF.
4. B7 ; 3E8 ; 010110100011.
5. 1 024 ; 4 096 ; 1 023 ; 10 bits ; 9 bits.
6. 00001010.00000000.00000000.11111111 ; 172.16.5.20 ; 256 > 255 ; 4294967296.
7. 00111100 ; 48 bits, 281474976710656 ; (30, 144, 255).
8. 41 ; 100101.

## TP Python – solutions

```python
def en_binaire(n):
    """Renvoie l'écriture binaire (texte) de l'entier naturel n."""
    if n == 0:
        return "0"
    texte = ""
    while n > 0:
        reste = n % 2
        texte = str(reste) + texte
        n = n // 2
    return texte
```

```python
CHIFFRES = "0123456789ABCDEF"

def vers_base(n, b):
    """Renvoie l'écriture de l'entier naturel n en base b (2 <= b <= 16)."""
    if n == 0:
        return "0"
    texte = ""
    while n > 0:
        texte = CHIFFRES[n % b] + texte
        n = n // b
    return texte
```

```python
def ip_en_binaire(adresse):
    """Renvoie l'adresse IPv4 écrite avec ses 4 octets en binaire."""
    octets = adresse.split(".")
    return ".".join(format(int(o), "08b") for o in octets)
```

```python
def octet_valide(texte):
    """Renvoie True si texte est l'écriture décimale d'un entier de 0 à 255."""
    return texte.isdigit() and 0 <= int(texte) <= 255
```

`octet_valide("")` : `"".isdigit()` vaut `False`, donc le `and` court-circuite et renvoie `False`.
