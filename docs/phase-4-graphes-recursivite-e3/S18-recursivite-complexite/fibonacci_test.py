assert [fib_rec(n) for n in range(0, 11)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
assert [fib_iter(n) for n in range(0, 11)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
assert fib_iter(50) == 12586269025
assert appels_fib(5) == 15 and appels_fib(10) == 177 and appels_fib(1) == 1
assert all(appels_fib(n) == 2 * fib_iter(n + 1) - 1 for n in range(0, 16))
