arcs = {("S", "A"): 4, ("S", "B"): 2, ("B", "A"): 1, ("A", "C"): 5, ("B", "C"): 8, ("B", "D"): 10, ("C", "D"): 2, ("C", "T"): 6, ("D", "T"): 3}
d, p = dijkstra(arcs, "S", ["S", "A", "B", "C", "D", "T"])
assert d == {"S": 0, "A": 3, "B": 2, "C": 8, "D": 10, "T": 13}
assert reconstruire(p, "T") == ["S", "B", "A", "C", "D", "T"]
assert reconstruire(p, "S") == ["S"]
w = {("A", "B"): 7, ("A", "C"): 9, ("A", "F"): 14, ("B", "C"): 10, ("B", "D"): 15, ("C", "D"): 11, ("C", "F"): 2, ("D", "E"): 6, ("F", "E"): 9}
d2, p2 = dijkstra(w, "A", ["A", "B", "C", "D", "E", "F"])
assert d2 == {"A": 0, "B": 7, "C": 9, "D": 20, "E": 20, "F": 11}
assert reconstruire(p2, "E") == ["A", "C", "F", "E"]
assert dijkstra({("A", "B"): 1}, "A", ["A", "B", "C"])[0]["C"] == float("inf")
