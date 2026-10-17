log = ["2026-03-14 08:12:45 192.168.1.23 LOGIN_OK alice", "2026-03-14 08:13:02 192.168.1.77 LOGIN_FAILED admin", "2026-03-14 08:13:09 192.168.1.77 LOGIN_FAILED admin", "2026-03-14 08:13:15 192.168.1.77 LOGIN_FAILED root", "2026-03-14 08:14:20 192.168.1.23 LOGIN_FAILED alice", "2026-03-14 08:15:01 192.168.1.40 LOGIN_OK bob"]
assert echecs_par_adresse(log) == {"192.168.1.77": 3, "192.168.1.23": 1}
assert echecs_par_adresse([]) == {}
assert adresses_suspectes(log, 2) == ["192.168.1.77"]
assert adresses_suspectes(log, 1) == ["192.168.1.23", "192.168.1.77"]
assert adresses_suspectes(log, 4) == []
