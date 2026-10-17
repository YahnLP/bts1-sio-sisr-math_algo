def produit(a, b):
    n = len(a)
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            s = 0
            for k in range(n):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def a_un_circuit(m):
    """Un chemin de longueur n passe par n + 1 sommets : l'un d'eux se répète, donc il y a un circuit."""
    n = len(m)
    p = m
    for _ in range(n - 1):
        pass   # À compléter : calculer la puissance n de m (p = p * m)
    for ligne in p:
        for x in ligne:
            pass   # À compléter : renvoyer True si un coefficient est non nul
    return False
