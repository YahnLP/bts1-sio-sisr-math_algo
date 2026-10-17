def chiffres_apres_virgule(x, p):
    """p premiers chiffres binaires de la partie fractionnaire de x (0 <= x < 1)."""
    texte = ""
    for _ in range(p):
        x = ...            # à compléter : on multiplie par 2
        chiffre = ...      # à compléter : partie entière de x (0 ou 1)
        texte = texte + str(chiffre)
        x = ...            # à compléter : on garde la partie fractionnaire
    return texte
