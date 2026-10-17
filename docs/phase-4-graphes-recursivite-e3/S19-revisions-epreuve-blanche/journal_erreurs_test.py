log = ["2026-03-14 08:12:45 10.0.0.5 INFO login alice", "2026-03-14 08:13:02 10.0.0.9 ERROR timeout db", "2026-03-14 08:13:09 10.0.0.9 ERROR timeout db", "2026-03-14 08:14:20 10.0.0.5 ERROR disque plein", "2026-03-14 08:15:01 10.0.0.7 INFO login bob"]
assert compte_erreurs(log) == {"10.0.0.9": 2, "10.0.0.5": 1}
assert compte_erreurs([]) == {}
assert adresse_la_plus_active(log) == "10.0.0.9"
assert adresse_la_plus_active([]) is None
assert adresse_la_plus_active(["d h 10.0.0.2 ERROR x", "d h 10.0.0.1 ERROR y"]) == "10.0.0.1"
assert compte_erreurs(["d h 10.0.0.2 INFO x"]) == {}
