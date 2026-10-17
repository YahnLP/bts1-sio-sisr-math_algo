def est_premier(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True

def premiers_palindromes(N):
    """Liste croissante des nombres premiers palindromes <= N."""
    ...
