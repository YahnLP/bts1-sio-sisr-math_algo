from fractions import Fraction

def terme_arith(u0, r, n):
    return 0   # À compléter : u0 + n r

def terme_geom(u0, q, n):
    return 0   # À compléter : u0 q^n

def somme_arith(u0, r, n):
    """u0 + ... + un : (nombre de termes) x (premier + dernier) / 2."""
    return 0   # À compléter, en Fraction : Fraction(..., 2)

def somme_geom(u0, q, n):
    """u0 + ... + un."""
    if q == 1:
        return (n + 1) * u0
    return 0   # À compléter : u0 (1 - q^(n+1)) / (1 - q)
