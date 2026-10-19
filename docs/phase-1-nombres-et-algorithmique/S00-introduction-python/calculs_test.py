assert quotient_reste(17, 5) == (3, 2)
assert quotient_reste(20, 5) == (4, 0)
assert quotient_reste(3, 7) == (0, 3)
assert est_multiple(15, 5) is True
assert est_multiple(16, 5) is False
assert est_multiple(0, 7) is True
assert conversion_secondes(3725) == (1, 2, 5)
assert conversion_secondes(59) == (0, 0, 59)
assert conversion_secondes(3600) == (1, 0, 0)
assert conversion_secondes(86399) == (23, 59, 59)
