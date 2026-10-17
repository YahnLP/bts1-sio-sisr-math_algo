assert jours_du_mois(1, 2024) == 31
assert jours_du_mois(2, 2024) == 29
assert jours_du_mois(2, 2023) == 28
assert jours_du_mois(2, 1900) == 28
assert jours_du_mois(4, 2024) == 30
assert jours_du_mois(11, 2023) == 30
assert jours_du_mois(12, 2023) == 31
assert sum(jours_du_mois(m, 2024) for m in range(1, 13)) == 366
assert sum(jours_du_mois(m, 2023) for m in range(1, 13)) == 365
