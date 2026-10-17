from fractions import Fraction
assert seuil_croissant(1000, Fraction(21, 20), 2000) == 15
assert seuil_croissant(100, Fraction(103, 100), 200) == 24
assert seuil_croissant(1, 2, 10 ** 9) == 30
assert seuil_croissant(5, 2, 3) == 0
assert seuil_decroissant(1200, Fraction(4, 5), 300) == 7
assert seuil_decroissant(1, Fraction(1, 2), Fraction(1, 1000)) == 10
assert seuil_decroissant(10, Fraction(1, 2), 20) == 0
