A = {1, 2, 3, 4, 5, 6}
B = {2, 4, 6, 8}
assert operations(A, B) == ({2, 4, 6}, {1, 2, 3, 4, 5, 6, 8}, {1, 3, 5}, {1, 3, 5, 8})
assert operations(set(), {1}) == (set(), {1}, set(), {1})
assert operations({1, 2}, {1, 2}) == ({1, 2}, {1, 2}, set(), set())
assert operations({1}, {2}) == (set(), {1, 2}, {1}, {1, 2})
