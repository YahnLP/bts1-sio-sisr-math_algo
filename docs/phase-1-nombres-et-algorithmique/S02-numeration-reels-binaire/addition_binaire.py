def addition_binaire(a, b):
    """Somme de deux nombres binaires donnés sous forme de textes."""
    n = max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)
    resultat = ""
    retenue = 0
    for i in range(n - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + retenue
        resultat = ... + resultat    # à compléter : chiffre à écrire (total modulo 2)
        retenue = ...                # à compléter : nouvelle retenue (total // 2)
    if retenue == 1:
        resultat = "1" + resultat
    return resultat
