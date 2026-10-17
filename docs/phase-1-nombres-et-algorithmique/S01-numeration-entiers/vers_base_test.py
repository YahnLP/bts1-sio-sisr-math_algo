assert vers_base(0, 2) == "0"
assert vers_base(205, 16) == "CD"
assert vers_base(205, 2) == "11001101"
assert vers_base(1000, 16) == "3E8"
assert vers_base(255, 8) == "377"
assert vers_base(100, 5) == "400"
assert all(int(vers_base(k, b), b) == k for k in range(0, 200) for b in range(2, 17))
