g = [[0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
assert nb_chemins(g, 2, 0, 3) == 2
assert nb_chemins(g, 3, 0, 5) == 3
assert nb_chemins(g, 2, 2, 5) == 2
assert nb_chemins(g, 4, 0, 5) == 0
assert nb_chemins(g, 0, 1, 1) == 1 and nb_chemins(g, 0, 1, 2) == 0
c = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
assert nb_chemins(c, 4, 0, 0) == 1 and nb_chemins(c, 2, 0, 2) == 1 and nb_chemins(c, 3, 0, 2) == 0
