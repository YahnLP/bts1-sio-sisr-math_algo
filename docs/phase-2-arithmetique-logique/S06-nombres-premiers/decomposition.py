def decomposition(n):
    """Dictionnaire {premier: exposant} de la décomposition de n >= 2."""
    resultat = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat[d] = resultat.get(d, 0) + 1
            n = n // d
        d = d + 1
    # À compléter : s'il reste un facteur n > 1, c'est un nombre premier
    return resultat
