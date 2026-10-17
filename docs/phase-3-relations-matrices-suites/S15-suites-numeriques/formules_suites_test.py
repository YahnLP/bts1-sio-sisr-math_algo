assert terme_arith(7, 4, 10) == 47 and terme_arith(5, -3, 4) == -7
assert terme_geom(5, 3, 6) == 3645 and terme_geom(1, 2, 10) == 1024
assert terme_geom(8, Fraction(1, 2), 3) == 1
assert somme_arith(7, 4, 10) == 297 and somme_arith(1, 1, 99) == 5050
assert somme_geom(5, 3, 6) == 5465 and somme_geom(1, 2, 9) == 1023
assert somme_geom(1, Fraction(1, 2), 10) == Fraction(2047, 1024)
assert somme_geom(4, 1, 9) == 40
