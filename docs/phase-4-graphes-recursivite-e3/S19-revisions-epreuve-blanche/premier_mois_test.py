from fractions import Fraction
assert premier_mois(120, Fraction(27, 25), 200) == 7
assert premier_mois(100, Fraction(103, 100), 200) == 24
assert premier_mois(1, 2, 1000) == 10
assert premier_mois(500, Fraction(11, 10), 200) == 0
