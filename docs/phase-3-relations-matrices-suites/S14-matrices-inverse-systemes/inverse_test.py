assert inverse([[2, 1], [5, 3]]) == [[3, -1], [-5, 2]]
assert inverse([[1, 2, 3], [0, 1, 4], [5, 6, 0]]) == [[-24, 18, 5], [20, -15, -4], [-5, 4, 1]]
assert inverse([[0, 1], [1, 0]]) == [[0, 1], [1, 0]]
assert inverse([[1, 2], [2, 4]]) is None
assert inverse([[1, 1, 1], [1, 2, 3], [2, 3, 4]]) is None
assert inverse([[2, 0], [0, 4]]) == [[Fraction(1, 2), 0], [0, Fraction(1, 4)]]
assert produit([[2, 1, 1], [1, 3, 2], [3, 2, 1]], inverse([[2, 1, 1], [1, 3, 2], [3, 2, 1]])) == identite(3)
