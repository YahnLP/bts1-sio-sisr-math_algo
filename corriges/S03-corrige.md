# Corrigé S03

## Exercices

1. int ; float ; str ; bool ; str ; bool ; int ; float.
2. 4 ; 5 ; 32 ; -4 ; 3 ; False ; True ; False ; 8 ; 14 ; 6 ; 32 ; 25.
3. 101 (lecture + exécution) ; `5 | 2` = 7 ; `7 & ~4` = 3 ; `(6 & 1) != 0` = False.
4. tous, trois, cinq, aucun.
5. Voir les réponses de l'énoncé.
6. Voir le tableau de l'énoncé.
7. 192.168.5.64 ; 172.16.32.0.
8. `==` ; `int(input(…))` ; ordre des tests.

## TP Python – solutions

```python
LECTURE = 4
ECRITURE = 2
EXECUTION = 1

def ajouter(droits, masque):
    """Ajoute le(s) droit(s) du masque."""
    return droits | masque

def retirer(droits, masque):
    """Retire le(s) droit(s) du masque."""
    return droits & ~masque

def accorde(droits, masque):
    """Renvoie True si tous les bits du masque sont à 1 dans droits."""
    return (droits & masque) == masque
```

```python
def est_bissextile(annee):
    """Renvoie True si l'année est bissextile."""
    return (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0
```

```python
def adresse_privee(adresse):
    """Renvoie True si l'adresse IPv4 (texte) est privée."""
    octets = adresse.split(".")
    a = int(octets[0])
    b = int(octets[1])
    return a == 10 or (a == 172 and 16 <= b <= 31) or (a == 192 and b == 168)
```

```python
def adresse_reseau(adresse, masque):
    """Adresse de réseau (texte) : ET bit à bit, octet par octet."""
    a = adresse.split(".")
    m = masque.split(".")
    resultat = []
    for i in range(4):
        resultat.append(str(int(a[i]) & int(m[i])))
    return ".".join(resultat)
```

```python
def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0

def jours_du_mois(mois, annee):
    """Nombre de jours du mois (1 à 12) de l'année donnée."""
    if mois == 2:
        if est_bissextile(annee):
            return 29
        else:
            return 28
    elif mois in (4, 6, 9, 11):
        return 30
    else:
        return 31
```
