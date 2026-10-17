assert pgcd(252, 198) == 18
assert pgcd(1071, 462) == 21
assert pgcd(17, 5) == 1
assert pgcd(7, 0) == 7
assert pgcd(0, 7) == 7
assert pgcd(1920, 1080) == 120
assert pgcd(756, 540) == 108
import math
assert all(pgcd(a, b) == math.gcd(a, b) for a in range(0, 50) for b in range(0, 50) if a + b > 0)
