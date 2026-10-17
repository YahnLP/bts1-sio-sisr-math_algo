assert est_tautologie(lambda p: p or not p, 1) is True
assert est_tautologie(lambda p: p and not p, 1) is False
assert est_tautologie(lambda p, q: (not p) or q, 2) is False
assert est_tautologie(lambda p, q: (not (((not p) or q) and p)) or q, 2) is True
assert est_tautologie(lambda p, q: (not (p or q)) or p, 2) is False
assert nombre_de_vrais(lambda p, q: p or q, 2) == 3
assert nombre_de_vrais(lambda p, q, r: (p and not q) or r, 3) == 5
assert nombre_de_vrais(lambda p, q: p != q, 2) == 2
