assert non_nand(0) == 1 and non_nand(1) == 0
assert [et_nand(a, b) for a in (0, 1) for b in (0, 1)] == [0, 0, 0, 1]
assert [ou_nand(a, b) for a in (0, 1) for b in (0, 1)] == [0, 1, 1, 1]
assert [xor_nand(a, b) for a in (0, 1) for b in (0, 1)] == [0, 1, 1, 0]
