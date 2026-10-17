e = set(range(1, 11))
r = {(x, y) for x in e for y in e if (x - y) % 3 == 0}
assert classes(r, e) == [{1, 4, 7, 10}, {2, 5, 8}, {3, 6, 9}]
pairs = {(x, y) for x in range(1, 7) for y in range(1, 7) if (x - y) % 2 == 0}
assert classes(pairs, set(range(1, 7))) == [{1, 3, 5}, {2, 4, 6}]
assert classes({(1, 1), (2, 2)}, {1, 2}) == [{1}, {2}]
assert classes(set(), set()) == []
