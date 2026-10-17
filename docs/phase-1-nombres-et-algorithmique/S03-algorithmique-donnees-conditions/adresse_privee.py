def adresse_privee(adresse):
    """Renvoie True si l'adresse IPv4 (texte) est privée."""
    octets = adresse.split(".")
    a = int(octets[0])
    b = int(octets[1])
    ...
