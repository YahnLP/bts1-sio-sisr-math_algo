def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def ppcm(a, b):
    """PPCM de deux entiers strictement positifs."""
    ...

def premiers_entre_eux(a, b):
    """True si a et b sont premiers entre eux."""
    ...
