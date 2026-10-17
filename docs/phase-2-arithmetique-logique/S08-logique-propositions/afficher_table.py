def combinaisons(n):
    liste = []
    for k in range(2 ** n):
        ligne = []
        for i in range(n):
            ligne.append(bool((k >> (n - 1 - i)) & 1))
        liste.append(tuple(ligne))
    return liste

def afficher_table(f, n):
    """Affiche une ligne par combinaison : les valeurs puis le résultat, en V / F."""
    for valeurs in combinaisons(n):
        ...

afficher_table(lambda p, q: p and q, 2)
