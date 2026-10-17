def meme_fonction(f, g, n):
    """Vrai si f et g donnent le même résultat sur les 2**n combinaisons."""
    for k in range(2 ** n):
        valeurs = []
        for i in range(n):
            valeurs.append((k >> (n - 1 - i)) & 1)
        # À compléter : renvoyer False si f et g diffèrent sur cette combinaison
    return True
