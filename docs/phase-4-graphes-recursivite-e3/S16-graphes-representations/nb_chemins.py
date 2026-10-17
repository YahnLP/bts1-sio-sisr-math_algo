def produit(a, b):
    n = len(a)
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            s = 0
            for k in range(n):
                # À compléter : ajouter a[i][k] * b[k][j]
                pass
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def nb_chemins(m, p, i, j):
    n = len(m)
    r = []
    for a in range(n):
        r.append([1 if a == b else 0 for b in range(n)])   # matrice identité
    for _ in range(p):
        pass   # À compléter : multiplier r par m
    return r[i][j]
