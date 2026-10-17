assert cases_visitees(12, 5) == set(range(12))
assert cases_visitees(12, 4) == {0, 4, 8}
assert cases_visitees(10, 4) == {0, 2, 4, 6, 8}
assert cases_visitees(15, 6) == {0, 3, 6, 9, 12}
assert cases_visitees(15, 4) == set(range(15))
assert len(cases_visitees(7, 3)) == 7
