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

def identite(n):
    m = []
    for i in range(n):
        ligne = []
        for j in range(n):
            # À compléter : 1 sur la diagonale (i == j), 0 ailleurs
            ligne.append(0)
        m.append(ligne)
    return m

def puissance(a, p):
    r = identite(len(a))
    for _ in range(p):
        # À compléter : multiplier r par a
        pass
    return r
