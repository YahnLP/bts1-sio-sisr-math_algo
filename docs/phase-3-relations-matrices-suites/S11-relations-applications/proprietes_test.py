E = {1, 2, 3, 4}
leq = {(x, y) for x in E for y in E if x <= y}
assert est_reflexive(leq, E) and est_antisymetrique(leq) and est_transitive(leq)
assert not est_symetrique(leq)
div = {(x, y) for x in E for y in E if y % x == 0}
assert est_reflexive(div, E) and est_antisymetrique(div) and est_transitive(div) and not est_symetrique(div)
diff = {(x, y) for x in E for y in E if x != y}
assert not est_reflexive(diff, E) and est_symetrique(diff) and not est_antisymetrique(diff) and not est_transitive(diff)
r = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
assert est_reflexive(r, {1, 2, 3}) and est_symetrique(r) and est_transitive(r) and not est_antisymetrique(r)
assert est_symetrique(set()) and est_antisymetrique(set()) and est_transitive(set()) and not est_reflexive(set(), {1})
somme7 = {(x, y) for x in range(1, 7) for y in range(1, 7) if x + y == 7}
assert est_symetrique(somme7) and not est_transitive(somme7) and not est_reflexive(somme7, range(1, 7))
