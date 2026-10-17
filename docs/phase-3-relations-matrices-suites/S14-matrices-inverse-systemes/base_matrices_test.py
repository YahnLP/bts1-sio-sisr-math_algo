assert identite(2) == [[1, 0], [0, 1]]
assert identite(3)[1][1] == 1 and identite(3)[0][2] == 0
assert produit([[2, 1], [5, 3]], [[3, -1], [-5, 2]]) == [[1, 0], [0, 1]]
assert produit([[1, 2, 3]], [[1], [1], [1]]) == [[6]]
assert produit([[Fraction(1, 2), 0], [0, 2]], [[2, 0], [0, Fraction(1, 2)]]) == [[1, 0], [0, 1]]
