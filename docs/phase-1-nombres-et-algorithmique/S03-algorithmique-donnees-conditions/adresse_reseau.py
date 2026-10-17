def adresse_reseau(adresse, masque):
    """Adresse de réseau (texte) : ET bit à bit, octet par octet."""
    a = adresse.split(".")
    m = masque.split(".")
    resultat = []
    for i in range(4):
        resultat.append(str(...))   # à compléter : ET bit à bit des deux octets (entiers)
    return ".".join(resultat)
