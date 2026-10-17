def produit(a, b):
    """Produit de a (m x n) par b (n x p), ou None si les tailles sont incompatibles."""
    if len(a[0]) != len(b):
        return None
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                # À compléter : ajouter a[i][k] * b[k][j] à s
                pass
            ligne.append(s)
        resultat.append(ligne)
    return resultat
