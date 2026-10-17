def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0

def jours_du_mois(mois, annee):
    """Nombre de jours du mois (1 à 12) de l'année donnée."""
    ...
