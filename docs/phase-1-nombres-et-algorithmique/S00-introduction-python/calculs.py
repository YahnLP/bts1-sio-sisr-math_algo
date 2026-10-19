def quotient_reste(a, b):
    """Renvoie le couple (quotient, reste) de la division euclidienne de a par b (b > 0)."""
    q = ...   # à compléter : quotient
    r = ...   # à compléter : reste
    return (q, r)

def est_multiple(a, b):
    """Renvoie True si a est un multiple de b (b > 0), False sinon."""
    return ...   # à compléter : comparer le reste de a par b à 0

def conversion_secondes(s):
    """Renvoie (heures, minutes, secondes) pour une durée de s secondes."""
    heures = ...      # à compléter
    reste = s % 3600
    minutes = ...     # à compléter
    secondes = ...    # à compléter
    return (heures, minutes, secondes)
