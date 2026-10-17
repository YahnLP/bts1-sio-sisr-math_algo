def isbn13_valide(code):
    """True si la somme pondérée (1, 3, 1, 3, ...) des 13 chiffres est un multiple de 10."""
    somme = 0
    for i in range(len(code)):
        chiffre = int(code[i])
        # À compléter : poids 1 si i est pair, 3 sinon
    return len(code) == 13 and somme % 10 == 0
