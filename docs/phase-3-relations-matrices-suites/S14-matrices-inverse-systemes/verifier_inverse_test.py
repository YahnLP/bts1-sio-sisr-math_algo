assert est_inverse([[2, 1], [5, 3]], [[3, -1], [-5, 2]]) is True
assert est_inverse([[2, 1], [5, 3]], [[3, 1], [5, 2]]) is False
assert est_inverse([[1, 2, 3], [0, 1, 4], [5, 6, 0]], [[-24, 18, 5], [20, -15, -4], [-5, 4, 1]]) is True
assert est_inverse([[2, 0], [0, 2]], [[Fraction(1, 2), 0], [0, Fraction(1, 2)]]) is True
assert est_inverse([[1, 2], [2, 4]], [[1, 0], [0, 1]]) is False
