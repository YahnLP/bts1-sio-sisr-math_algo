assert somme_termes(lambda k: k, 1, 100) == 5050
assert somme_termes(lambda k: 2 ** k, 0, 9) == 1023
assert somme_termes(lambda k: 7 + 4 * k, 0, 10) == 297
assert somme_termes(lambda k: k, 5, 4) == 0
assert all(somme_termes(lambda k: k, 1, n) == n * (n + 1) // 2 for n in range(1, 51))
