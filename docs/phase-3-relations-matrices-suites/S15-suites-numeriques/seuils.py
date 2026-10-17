def seuil_croissant(u0, q, limite):
    """Plus petit n tel que u0 q^n >= limite (q > 1)."""
    n = 0
    u = u0
    while u < limite and n < 10000:
        # À compléter : passer au terme suivant (u et n)
        pass
    return n

def seuil_decroissant(u0, q, limite):
    """Plus petit n tel que u0 q^n <= limite (0 < q < 1)."""
    n = 0
    u = u0
    while u > limite and n < 10000:
        # À compléter : passer au terme suivant (u et n)
        pass
    return n
