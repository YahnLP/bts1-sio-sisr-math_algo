assert produit({1, 2}, {"a"}) == {(1, "a"), (2, "a")}
assert produit(set(), {1, 2}) == set()
assert produit({1, 2, 3}, {4, 5}) == {(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)}
assert len(produit(range(3), range(4))) == 12
assert produit({1}, {2}) != produit({2}, {1})
