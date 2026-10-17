def produit(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def fibonacci(n):
    """F(n) avec F(1) = F(2) = 1, par la puissance n de [[1, 1], [1, 0]]."""
    r = [[1, 0], [0, 1]]
    for _ in range(n):
        # À compléter : multiplier r par [[1, 1], [1, 0]]
        pass
    return 0   # À compléter : un coefficient de r
