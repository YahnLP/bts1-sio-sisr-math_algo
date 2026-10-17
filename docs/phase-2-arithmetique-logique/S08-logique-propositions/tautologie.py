def combinaisons(n):
    liste = []
    for k in range(2 ** n):
        ligne = []
        for i in range(n):
            ligne.append(bool((k >> (n - 1 - i)) & 1))
        liste.append(tuple(ligne))
    return liste

def est_tautologie(f, n):
    """True si f vaut True pour toutes les combinaisons."""
    ...

def nombre_de_vrais(f, n):
    """Nombre de combinaisons pour lesquelles f vaut True."""
    ...
