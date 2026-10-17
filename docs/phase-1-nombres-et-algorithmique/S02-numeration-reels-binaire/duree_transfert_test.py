assert duree_transfert(2_000_000_000, 100_000_000) == 160
assert duree_transfert(2_000_000_000, 1_000_000_000) == 16
assert duree_transfert(125, 1000) == 1
assert abs(duree_transfert(50_000_000_000, 1_000_000_000) - 400) < 1e-9
