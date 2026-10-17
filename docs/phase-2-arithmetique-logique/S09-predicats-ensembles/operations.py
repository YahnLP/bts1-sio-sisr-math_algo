def operations(a, b):
    """Renvoie (a ∩ b, a ∪ b, a \\ b, a Δ b) sans les opérateurs d'ensembles."""
    inter = set()
    reunion = set()
    diff = set()
    sym = set()
    for x in a:
        # À compléter : x est dans la réunion ; dans l'intersection ou la différence ?
        pass
    for x in b:
        # À compléter : x est dans la réunion ; dans la différence symétrique s'il n'est pas dans a
        pass
    # À compléter : la différence symétrique contient aussi a \ b
    return (inter, reunion, diff, sym)
