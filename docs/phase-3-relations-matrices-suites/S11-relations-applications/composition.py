def image_directe(f, x):
    """Ensemble des images des éléments de x."""
    resultat = set()
    for a in x:
        # À compléter : ajouter l'image de a
        pass
    return resultat

def image_reciproque(f, y):
    """Ensemble des éléments de départ dont l'image est dans y."""
    resultat = set()
    for a in f:
        # À compléter : ajouter a si f[a] est dans y
        pass
    return resultat

def composee(g, f):
    """Dictionnaire de g o f : x -> g(f(x))."""
    resultat = {}
    for x in f:
        # À compléter : resultat[x] = g(f(x))
        pass
    return resultat

def reciproque(f):
    """Application réciproque (b -> a), ou None si f n'est pas injective."""
    inverse = {}
    for a in f:
        # À compléter : si f[a] est déjà une clé de inverse, renvoyer None ;
        # sinon associer f[a] à a
        pass
    return inverse
