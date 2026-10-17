def combinaisons(n):
    liste = []
    for k in range(2 ** n):
        ligne = []
        for i in range(n):
            ligne.append(bool((k >> (n - 1 - i)) & 1))
        liste.append(tuple(ligne))
    return liste

def equivalentes(f, g, n):
    """True si f et g donnent le même résultat sur toutes les combinaisons de n booléens."""
    ...
