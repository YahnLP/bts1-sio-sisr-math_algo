m = matrice_adjacence(4, [(0, 1), (0, 2), (1, 3)])
assert m == [[0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
assert successeurs(m, 0) == [1, 2] and successeurs(m, 3) == []
assert demi_degres(m) == ([2, 1, 0, 0], [0, 1, 1, 1])
g = matrice_adjacence(6, [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)])
assert demi_degres(g) == ([2, 1, 2, 1, 1, 0], [0, 1, 1, 2, 1, 2])
assert matrice_adjacence(2, []) == [[0, 0], [0, 0]]
