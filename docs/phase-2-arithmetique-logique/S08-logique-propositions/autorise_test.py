assert autorise("TCP", 80) is True
assert autorise("TCP", 443) is True
assert autorise("TCP", 22) is False
assert autorise("ICMP", 0) is True
assert autorise("UDP", 53) is False
assert autorise("UDP", 443) is False
