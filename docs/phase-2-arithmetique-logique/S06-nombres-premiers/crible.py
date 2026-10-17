def crible(N):
    """Liste des nombres premiers <= N (crible d'Ératosthène)."""
    est_premier = [True] * (N + 1)
    # À compléter : 0 et 1 ne sont pas premiers ;
    # pour p de 2 à racine de N, si p est encore marqué premier,
    # marquer False tous ses multiples à partir de p * p.
    return [k for k in range(N + 1) if est_premier[k]]
