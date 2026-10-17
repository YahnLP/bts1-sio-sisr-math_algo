assert mois_avant_saturation(1) == 0
assert mois_avant_saturation(2) == 1
assert mois_avant_saturation(100) == 7
assert mois_avant_saturation(128) == 7
assert mois_avant_saturation(129) == 8
assert mois_avant_saturation(1000) == 10
assert mois_avant_saturation(4000) == 12
