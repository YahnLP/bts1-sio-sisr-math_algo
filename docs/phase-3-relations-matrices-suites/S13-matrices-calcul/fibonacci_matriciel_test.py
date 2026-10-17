assert fibonacci(1) == 1 and fibonacci(2) == 1 and fibonacci(3) == 2
assert fibonacci(10) == 55
assert fibonacci(20) == 6765
assert [fibonacci(n) for n in range(1, 9)] == [1, 1, 2, 3, 5, 8, 13, 21]
