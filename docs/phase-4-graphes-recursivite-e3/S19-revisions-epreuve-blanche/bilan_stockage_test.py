from fractions import Fraction
assert volumes(120, Fraction(27, 25), 3) == [120, Fraction(648, 5), Fraction(17496, 125), Fraction(472392, 3125)]
assert volumes(10, 2, 4) == [10, 20, 40, 80, 160]
assert volumes(5, 3, 0) == [5]
assert bilan(120, Fraction(27, 25), 200) == (7, 120 * Fraction(27, 25) ** 7)
assert bilan(1, 2, 1000) == (10, 1024)
assert bilan(300, Fraction(11, 10), 200) == (0, 300)
