f = {x: x % 5 for x in range(10)}
assert image_directe(f, {0, 1, 2, 3}) == {0, 1, 2, 3}
assert image_directe(f, {2, 7, 9}) == {2, 4}
assert image_reciproque(f, {0}) == {0, 5}
assert image_reciproque(f, {1, 2}) == {1, 2, 6, 7}
assert image_reciproque(f, {5}) == set()
u = {1: 3, 2: 5}
v = {3: "x", 5: "y"}
assert composee(v, u) == {1: "x", 2: "y"}
assert reciproque({1: "a", 2: "b", 3: "c"}) == {"a": 1, "b": 2, "c": 3}
assert reciproque({1: "a", 2: "a"}) is None
assert reciproque({}) == {}
assert composee(reciproque(u), u) == {1: 1, 2: 2}
