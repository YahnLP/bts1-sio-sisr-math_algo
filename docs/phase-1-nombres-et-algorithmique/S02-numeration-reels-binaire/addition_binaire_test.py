assert addition_binaire("1011", "0111") == "10010"
assert addition_binaire("1", "1") == "10"
assert addition_binaire("0", "0") == "0"
assert addition_binaire("111", "1") == "1000"
assert addition_binaire("11001101", "101") == "11010010"
assert all(int(addition_binaire(bin(x)[2:], bin(y)[2:]), 2) == x + y for x in range(0, 40) for y in range(0, 40))
