def decomposition(n):
    resultat = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat[d] = resultat.get(d, 0) + 1
            n = n // d
        d = d + 1
    if n > 1:
        resultat[n] = resultat.get(n, 0) + 1
    return resultat

def nombre_de_diviseurs(n):
    """Nombre de diviseurs positifs de n >= 1."""
    ...
