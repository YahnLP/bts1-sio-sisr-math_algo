from fractions import Fraction

def identite(n):
    m = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(Fraction(1 if i == j else 0))
        m.append(ligne)
    return m

def produit(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = Fraction(0)
            for k in range(len(b)):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def inverse(a):
    """Inverse de a par la méthode des lignes, ou None si a n'est pas inversible."""
    n = len(a)
    g = []
    for i in range(n):
        g.append([Fraction(x) for x in a[i]] + identite(n)[i])   # la matrice [A | I]
    for j in range(n):
        p = None
        for i in range(j, n):
            if g[i][j] != 0:
                p = i
                break
        if p is None:
            return None
        # À compléter : échanger les lignes j et p
        # À compléter : diviser la ligne j par le pivot g[j][j]
        # À compléter : pour chaque autre ligne i, retrancher g[i][j] fois la ligne j
    return [ligne[n:] for ligne in g]
