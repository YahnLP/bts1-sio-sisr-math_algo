assert equivalentes(lambda p, q: not (p and q), lambda p, q: (not p) or (not q), 2) is True
assert equivalentes(lambda p, q: not (p or q), lambda p, q: (not p) and (not q), 2) is True
assert equivalentes(lambda p, q: (not p) or q, lambda p, q: (not q) or p, 2) is False
assert equivalentes(lambda p, q, r: p and (q or r), lambda p, q, r: (p and q) or (p and r), 3) is True
assert equivalentes(lambda p, q, r: p or (q and r), lambda p, q, r: (p or q) and r, 3) is False
