assert parties([]) == [set()]
assert parties(["a"]) == [set(), {"a"}]
p = parties(["a", "b", "c"])
assert len(p) == 8
assert p[0] == set() and p[7] == {"a", "b", "c"}
assert p[5] == {"a", "c"}
assert len(parties([1, 2, 3, 4, 5])) == 32
assert all(x in p for x in [{"a"}, {"b"}, {"c"}, {"a", "b"}, {"b", "c"}])
