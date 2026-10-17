def mintermes(f, n):
    """Numéros des lignes (0 à 2**n - 1) pour lesquelles f vaut 1."""
    resultat = []
    for k in range(2 ** n):
        valeurs = []
        for i in range(n):
            # À compléter : le bit de rang (n - 1 - i) de k
            valeurs.append(0)
        if f(*valeurs):
            resultat.append(k)
    return resultat
