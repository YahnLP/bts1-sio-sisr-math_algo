assert est_premier(0) is False
assert est_premier(1) is False
assert est_premier(2) is True
assert est_premier(4) is False
assert est_premier(91) is False
assert est_premier(97) is True
assert est_premier(997) is True
assert est_premier(1001) is False
assert [k for k in range(50) if est_premier(k)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
